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
    python3 generar-icons.py --urls urls.json # sin token: mapa {node_id: url} ya resuelto

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
import xml.etree.ElementTree as ET

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


def _sin_ns(root):
    for el in root.iter():
        el.tag = el.tag.split("}")[-1]
        for a in list(el.attrib):
            if "}" in a:
                el.attrib[a.split("}")[-1]] = el.attrib.pop(a)


def _es_fondo(el, vb):
    """Forma sin `id` que no dibuja el icono, sino el lienzo detras.

    Figma mete dos: el `rect` del artboard y, en los iconos anidados, un `path`
    con el fondo del frame padre. Ninguno lleva `id` --- Figma nombra las capas
    reales --- y ambos se salen del viewBox.
    """
    if el.get("id") or el.tag not in ("rect", "path"):
        return False
    if el.get("transform", "").startswith("translate"):
        return True

    if el.tag == "rect":
        try:
            w, h = float(el.get("width", 0)), float(el.get("height", 0))
        except ValueError:
            return False
        return w >= vb[2] - 0.01 and h >= vb[3] - 0.01

    # `path`: si las coordenadas se salen del lienzo, esta dibujando el fondo
    nums = [float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", el.get("d", ""))]
    if not nums:
        return False
    return min(nums) < -4 or max(nums) > 2 * max(vb[2], vb[3])


def _podar(padre, vb):
    for hijo in list(padre):
        _podar(hijo, vb)
        if _es_fondo(hijo, vb):
            padre.remove(hijo)
        elif hijo.tag == "g" and len(hijo) == 0 and not (hijo.text or "").strip():
            padre.remove(hijo)


def _desenvolver(padre):
    """Colapsa los `<g>` que solo agrupan: un hijo unico y ningun atributo
    salvo `id`. Asi se van `<g id="Icons">` y los grupos intermedios de Figma."""
    while len(padre) == 1 and padre[0].tag == "g" \
            and set(padre[0].attrib) <= {"id"} and not (padre[0].text or "").strip():
        unico = padre[0]
        padre.remove(unico)
        for nieto in list(unico):
            padre.append(nieto)
    for hijo in padre:
        _desenvolver(hijo)


def _sin_sombras(padre):
    """Retira los efectos `filter` de Figma.

    Vienen de la instancia colocada en el artboard, no del icono: son sombras
    con un color fijo fuera del sistema de tokens. El canon (ICONOGRAPHY.md
    sec.1) define el icono como trazo plano de 1.5px, sin sombra.
    """
    for hijo in list(padre):
        _sin_sombras(hijo)
        if hijo.tag == "filter":
            padre.remove(hijo)
        elif hijo.tag == "defs" and len(hijo) == 0:
            padre.remove(hijo)
        elif hijo.get("filter", "").startswith("url(#"):
            del hijo.attrib["filter"]


def _sin_ids_decorativos(cuerpo):
    """Quita los `id` que nadie referencia.

    Son los nombres de capa de Figma (`Vector`, `Union`, `Path`...). Se repiten
    entre iconos, y dos elementos con el mismo id en una pagina es HTML invalido.
    Los que si se referencian --- los de `<defs>` --- se conservan.
    """
    usados = set(re.findall(r"url\(#([^)]+)\)", cuerpo))
    return re.sub(r' id="([^"]+)"',
                  lambda m: m.group(0) if m.group(1) in usados else "", cuerpo)


def _ids_unicos(cuerpo, clave_icono):
    """Prefija los ids de `<defs>` con la clave del icono.

    Figma exporta cada icono como documento suelto y numera desde cero, asi que
    doce iconos distintos salen todos con `clip0_0_1`. Al inyectar dos en la
    misma pagina, el `clip-path` del segundo apunta al recorte del primero y el
    icono se dibuja mal.
    """
    refs = set(re.findall(r"url\(#([^)]+)\)", cuerpo))
    if not refs:
        return cuerpo
    pref = re.sub(r"[^a-z0-9]+", "-", clave_icono.lower()).strip("-") or "icon"
    for r in sorted(refs, key=len, reverse=True):
        cuerpo = cuerpo.replace("url(#%s)" % r, "url(#%s-%s)" % (pref, r))
        cuerpo = cuerpo.replace('id="%s"' % r, 'id="%s-%s"' % (pref, r))
    return cuerpo


def limpiar(raw, clave_icono=""):
    """Quita el envoltorio del artboard y normaliza color y stroke.

    Se parsea el SVG como XML en lugar de recortarlo con expresiones regulares:
    el recorte por regex desbalanceaba las etiquetas `<g>` y metia un `</g>`
    huerfano en cada icono anidado.
    """
    try:
        root = ET.fromstring(raw)
    except ET.ParseError:
        return ""

    try:
        vb = [float(x) for x in (root.get("viewBox") or "0 0 24 24").split()]
    except ValueError:
        vb = [0.0, 0.0, 24.0, 24.0]

    _sin_ns(root)
    _podar(root, vb)
    _sin_sombras(root)
    _desenvolver(root)

    for el in root.iter():
        for a in ("fill", "stroke"):
            v = el.get(a)
            if v and (v.startswith("#") or v.lower() in ("black", "#000")):
                el.set(a, "currentColor")
        if el.get("stroke-width"):
            el.set("stroke-width", "1.5")

    cuerpo = "".join(ET.tostring(h, encoding="unicode") for h in root)
    cuerpo = _ids_unicos(re.sub(r"\s+", " ", cuerpo).strip(), clave_icono)
    return _sin_ids_decorativos(cuerpo)


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

    urls_previas = None
    if "--urls" in sys.argv:
        with open(sys.argv[sys.argv.index("--urls") + 1], encoding="utf-8") as f:
            urls_previas = json.load(f)

    filas = leer_nodos(filtro)
    print("iconos a procesar: %d" % len(filas))
    if seco:
        for n, i in filas[:10]:
            print("  %-34s %s" % (n, i))
        print("  ... (--dry-run: no se descarga nada)")
        return

    tok = None if urls_previas else token()

    entradas, fallos = {}, []
    for k in range(0, len(filas), LOTE):
        trozo = filas[k:k + LOTE]
        print("lote %d-%d de %d" % (k + 1, k + len(trozo), len(filas)))
        mapa = (urls_previas if urls_previas
                else urls_svg([i for _, i in trozo], tok))
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
            k = clave(nombre)
            entradas[k] = {
                "vb": vb.group(1) if vb else "0 0 24 24",
                "p": limpiar(raw, k),
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
    for aviso, patron in (("restos del artboard", r'width=\\"1646'),
                          ("colores hardcodeados", r"#[0-9A-Fa-f]{6}"),
                          ("blancos de knockout", r"white")):
        n = len(re.findall(patron, cuerpo_txt))
        if n:
            print("  aviso: %d %s" % (n, aviso))

    vistos = {}
    for k, v in entradas.items():
        for i in re.findall(r'id=\\"([^\\"]+)\\"', v["p"]):
            vistos.setdefault(i, []).append(k)
    choques = {i: ks for i, ks in vistos.items() if len(ks) > 1}
    if choques:
        print("  aviso: %d ids de <defs> repetidos entre iconos" % len(choques))


if __name__ == "__main__":
    main()
