#!/usr/bin/env python3
"""
generar-icons.py — genera `icons.ts` desde el archivo Figma Nexus V2.

Recorre los nodeIds de `figma-nodes.tsv`, pide los SVG a la API de Figma,
los limpia y los normaliza al canon, y escribe `icons.ts`.

USO
    export FIGMA_TOKEN=figd_xxxxxxxxxxxxxxxx
    python3 generar-icons.py                 # todos
    python3 generar-icons.py --solo math     # solo una categoría
    python3 generar-icons.py --dry-run       # sin escribir, solo informa

TOKEN
    Figma → tu avatar → Settings → Security → Personal access tokens →
    "Generate new token", con permiso de lectura (File content: Read-only).
    El token es personal: no lo subas al repo.

NORMALIZACIÓN (según el canon)
    - `fill` y `stroke` → `currentColor`   ICONOGRAPHY.md §7, regla 3
    - `stroke-width`    → 1.5              ICONOGRAPHY.md §1
    - se retiran los rects de fondo del artboard que Figma incluye al exportar

Los viewBox se conservan como salen: §3.1 especifica que son los bounding boxes
reales de cada icono, no el canvas 24×24.
"""
import json, os, re, sys, time, urllib.request, urllib.error

FILE_KEY = "agWwqm17qIvfveD8CQwSRz"
AQUI     = os.path.dirname(os.path.abspath(__file__))
NODOS    = os.path.join(AQUI, "figma-nodes.tsv")
SALIDA   = os.path.join(AQUI, "icons.ts")
LOTE     = 40          # ids por petición; la API acepta varios a la vez
PAUSA    = 0.5         # segundos entre peticiones, para no chocar con el rate limit


def token():
    t = os.environ.get("FIGMA_TOKEN")
    if not t:
        sys.exit("Falta FIGMA_TOKEN. Genéralo en Figma → Settings → Security → "
                 "Personal access tokens, y expórtalo:\n"
                 "    export FIGMA_TOKEN=figd_xxxxxxxx")
    return t


def leer_nodos(filtro=None):
    filas = []
    with open(NODOS, encoding="utf-8") as f:
        for linea in f:
            if linea.startswith("#") or not linea.strip():
                continue
            nombre, node_id = linea.rstrip("\n").split("\t")
            if filtro and filtro not in nombre:
                continue
            filas.append((nombre, node_id))
    return filas


def pedir(url, tok):
    req = urllib.request.Request(url, headers={"X-Figma-Token": tok})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def urls_svg(ids, tok):
    """La API devuelve una URL temporal por nodo."""
    url = ("https://api.figma.com/v1/images/%s?ids=%s&format=svg"
           % (FILE_KEY, ",".join(ids)))
    try:
        return pedir(url, tok).get("images", {})
    except urllib.error.HTTPError as e:
        print("  ! error %s en el lote: %s" % (e.code, e.reason))
        return {}


def descargar(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return r.read().decode("utf-8")


def limpiar(raw):
    """Quita el envoltorio del artboard y normaliza color y stroke."""
    inner = re.sub(r"^.*?<svg[^>]*>", "", raw, flags=re.S)
    inner = re.sub(r"</svg>\s*$", "", inner, flags=re.S).strip()

    # quedarse solo con el contenido del <g id="icon/...">, si existe
    m = re.search(r'<g id="(icon[/-][^"]*)">(.*)</g>', inner, flags=re.S)
    if m:
        inner = m.group(2)

    # fuera el rect del artboard y los rects de fondo sin id
    inner = re.sub(r'<rect[^>]*transform="translate\([^)]*\)"[^>]*/>', "", inner)
    inner = re.sub(r'<rect(?![^>]*\bid=)[^>]*fill="(white|#FFFFFF|#fff)"[^>]*/>',
                   "", inner, flags=re.I)
    inner = re.sub(r"^\s*<rect(?![^>]*\bid=)[^>]*/>", "", inner)

    # normalizar al canon
    inner = re.sub(r'(fill|stroke)="#[0-9A-Fa-f]{3,8}"',
                   lambda x: x.group(1) + '="currentColor"', inner)
    inner = re.sub(r'stroke-width="[0-9.]+"', 'stroke-width="1.5"', inner)

    # limpiar los <g> que quedaron vacíos
    for _ in range(3):
        inner = re.sub(r"<g[^>]*>\s*</g>", "", inner)

    return re.sub(r"\s+", " ", inner).strip()


def clave(nombre):
    """`icon/math/at` → `math/at`. El prefijo `menu/` se conserva."""
    if nombre.startswith("menu/"):
        return nombre
    return re.sub(r"^icon[/-]", "", nombre)


CABECERA = '''/**
 * icons.ts - catalogo de iconos NEXUS V2.0
 *
 * GENERADO por generar-icons.py desde el archivo Figma Nexus V2
 * (%s), frames `Icons` (25:4520) e `Icon-menu` (25:3428).
 * No editar a mano: los cambios se pierden en la siguiente generacion.
 *
 * Normalizacion aplicada, segun el canon:
 *   - `fill` y `stroke` -> `currentColor`  (ICONOGRAPHY.md sec.7, regla 3)
 *   - `stroke-width`    -> 1.5             (ICONOGRAPHY.md sec.1)
 *   - se retiran los rects de fondo del artboard
 *
 * Los viewBox son los bounding boxes reales de Figma, no el canvas 24x24
 * (ICON-COMPONENT.md sec.3.1).
 *
 * ESTADO: %%d iconos.
 */

export const icons: Record<string, { vb: string; p: string }> = {
''' % FILE_KEY

PIE = """};

export type IconName = keyof typeof icons
export const iconNames = Object.keys(icons) as IconName[]
export const menuIconNames = iconNames.filter(n => n.startsWith('menu/'))
export const systemIconNames = iconNames.filter(n => !n.startsWith('menu/'))
"""


def main():
    filtro = None
    seco = "--dry-run" in sys.argv
    if "--solo" in sys.argv:
        filtro = sys.argv[sys.argv.index("--solo") + 1]

    tok = token()
    filas = leer_nodos(filtro)
    print("iconos a procesar: %d" % len(filas))
    if seco:
        for n, i in filas[:10]:
            print("  %-34s %s" % (n, i))
        print("  ... (--dry-run: no se descarga nada)")
        return

    entradas, fallos = {}, []
    for k in range(0, len(filas), LOTE):
        trozo = filas[k:k + LOTE]
        print("lote %d-%d de %d" % (k + 1, k + len(trozo), len(filas)))
        mapa = urls_svg([i for _, i in trozo], tok)
        for nombre, node_id in trozo:
            url = mapa.get(node_id)
            if not url:
                fallos.append(nombre)
                continue
            try:
                raw = descargar(url)
            except Exception as e:
                print("  ! %s: %s" % (nombre, e))
                fallos.append(nombre)
                continue
            vb = re.search(r'viewBox="([^"]+)"', raw)
            entradas[clave(nombre)] = {
                "vb": vb.group(1) if vb else "0 0 24 24",
                "p": limpiar(raw),
            }
        time.sleep(PAUSA)

    cuerpo = "".join(
        "  '%s': {\n    vb: %s,\n    p: %s,\n  },\n"
        % (k, json.dumps(v["vb"]), json.dumps(v["p"]))
        for k, v in sorted(entradas.items())
    )
    with open(SALIDA, "w", encoding="utf-8") as f:
        f.write((CABECERA % len(entradas)) + cuerpo + PIE)

    print("\nescrito %s con %d iconos" % (SALIDA, len(entradas)))
    if fallos:
        print("no se pudieron descargar %d:" % len(fallos))
        for n in fallos:
            print("  - %s" % n)

    # avisos de calidad sobre lo generado
    texto = open(SALIDA, encoding="utf-8").read()
    cuerpo_txt = texto[texto.index("export const icons"):]
    for aviso, patron in (("restos del artboard", r"1646"),
                          ("colores hardcodeados", r"#[0-9A-Fa-f]{6}"),
                          ("fondos blancos", r"white")):
        n = len(re.findall(patron, cuerpo_txt))
        if n:
            print("  aviso: %d %s" % (n, aviso))


if __name__ == "__main__":
    main()
