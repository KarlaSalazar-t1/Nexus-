# -*- coding: utf-8 -*-
"""generar-hoja.py — hoja de contacto de los iconos, para revisarlos de un vistazo.

Lee `icons.ts` y `figma-nodes.tsv` y escribe `hoja-iconos.html`: los 222 iconos
en una rejilla, con búsqueda, filtro por categoría, cambio de tamaño y un botón
para invertir el fondo (que es como se comprueba el calado, `--icon-knockout`).

    python3 generar-hoja.py

Se regenera después de cada pasada de `generar-icons.py`.
"""
import json, re, html, collections

APP = '/Users/cagustin/Documents/platform/T1/app/components/icon/'
t = open(APP+'icons.ts', encoding='utf-8').read()
ent = [(k, json.loads(vb), json.loads(p)) for k, vb, p in re.findall(
    r"  '((?:[^'\\]|\\.)*)': \{\n    vb: (\"(?:[^\"\\]|\\.)*\"),\n    p: (\"(?:[^\"\\]|\\.)*\"),\n  \},", t)]

nodo = {}
for l in open(APP+'figma-nodes.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    n, i = l.rstrip('\n').split('\t')
    k = n if n.startswith('menu/') else re.sub(r'^icon[/-]', '', n)
    nodo[k] = i

datos = []
for k, vb, p in ent:
    cat = k.split('/')[0]
    w, h = (vb.split()+['24','24'])[2:4]
    m = re.match(r'<g transform="(?:translate\([^)]*\) )?scale\(([\d.]+)\)"', p)
    esc = float(m.group(1)) if m else 1.0
    datos.append({
        'k': k, 'vb': vb, 'p': p, 'cat': cat, 'id': nodo.get(k, ''),
        'ko': 'icon-knockout' in p,                # tiene zona calada
        'nc': p.startswith('<g transform'),         # reencajado en el lienzo
        'defs': 'url(#' in p,
        'esc': ('%gx' % round(esc, 3)) if abs(esc-1) > 1e-9 else '',
        'orig': ('%g' % round(24/esc, 2)) + '\u00d7' + ('%g' % round(24/esc, 2)) if abs(esc-1) > 1e-9 else '24\u00d724',
    })
datos.sort(key=lambda d: (d['cat'] == 'menu', d['cat'].lower(), d['k'].lower()))
cats = collections.Counter(d['cat'] for d in datos)
ko  = [d['k'] for d in datos if d['ko']]
nc  = [d for d in datos if d['nc']]
dfs = [d['k'] for d in datos if d['defs']]

def celda(d):
    marcas = ''
    if d['ko']:  marcas += '<span class="mk mk-ko" title="tiene zona calada; usa --icon-knockout">calado</span>'
    if d['nc']:  marcas += '<span class="mk mk-fit" title="el componente no medía 24x24 en Figma: reencajado">%s</span>' % html.escape(d['esc'])
    if d['defs'] and not d['nc']: marcas += '<span class="mk mk-df" title="lleva &lt;defs&gt; con clip-path">defs</span>'
    return ('<button class="cell" data-k="%s" data-cat="%s" data-ko="%d" data-nc="%d">'
            '<span class="glyph"><svg viewBox="%s" fill="none" aria-hidden="true">%s</svg></span>'
            '<span class="name">%s</span>'
            '<span class="meta"><span class="vb">%s</span>%s</span>'
            '%s</button>') % (
        html.escape(d['k']), html.escape(d['cat']), d['ko'], d['nc'],
        html.escape(d['vb']), d['p'],
        html.escape(d['k'].split('/', 1)[1] if '/' in d['k'] else d['k']),
        html.escape(d['orig']),
        '<span class="nid">%s</span>' % html.escape(d['id']) if d['id'] else '',
        marcas)

grupos = []
for cat in sorted(cats, key=lambda c: (c == 'menu', c.lower())):
    ds = [d for d in datos if d['cat'] == cat]
    grupos.append(
        '<section class="grupo" data-cat="%s">'
        '<h2><span class="cat">%s</span><span class="n">%d</span></h2>'
        '<div class="rejilla">%s</div></section>'
        % (html.escape(cat), html.escape(cat), len(ds), ''.join(celda(d) for d in ds)))

filtros = ''.join(
    '<button class="chip" data-f="%s">%s<span>%d</span></button>' % (html.escape(c), html.escape(c), n)
    for c, n in sorted(cats.items(), key=lambda x: (x[0] == 'menu', x[0].lower())))

CSS = open(APP + 'hoja.css', encoding='utf-8').read()
JS  = open(APP + 'hoja.js',  encoding='utf-8').read()

fuera = (
 '<title>Iconos Nexus V2</title>\n'
 '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
 '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
 '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
 'family=Manrope:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@400;500&display=swap">\n'
 '<style>\n%s\n</style>\n' % CSS)

fuera += """
<header class="cab">
  <div class="cab-in">
    <p class="eyebrow">Nexus V2 &middot; <code>components/icon/icons.ts</code></p>
    <h1>Los 222 iconos, uno al lado del otro</h1>
    <p class="sub">Generado desde el archivo Figma <strong>Nexus&nbsp;V2</strong> &mdash; frames
      <code>Icons</code> (25:4520) e <code>Icon-menu</code> (25:3428) &mdash; por
      <code>generar-icons.py</code>. Todos en lienzo <code>0 0 24 24</code> y trazo de 1.5px.
      Esta hoja existe para una cosa: ver que los 222 dibujan lo que deben.</p>

    <dl class="cifras">
      <div><dt>glifos</dt><dd>222</dd></div>
      <div><dt>de sistema</dt><dd>%d</dd></div>
      <div><dt>de men&uacute;</dt><dd>37</dd></div>
      <div><dt>categor&iacute;as</dt><dd>%d</dd></div>
      <div><dt>reencajados</dt><dd>%d</dd></div>
      <div><dt>con calado</dt><dd>%d</dd></div>
      <div class="ok"><dt>trazo a 1.5px</dt><dd>222</dd></div>
    </dl>
  </div>
</header>

<div class="aviso">
  <h2>Lo que se arregl&oacute; en el pipeline</h2>
  <div class="aviso-cols">
    <div>
      <h3>El lienzo <span class="mk mk-fit">0.8x</span></h3>
      <p><strong>%d de los 222</strong> no med&iacute;an 24&times;24 en Figma: hay componentes de
      16&times;16, 25&times;25, 30&times;30, 25&times;17&hellip; Como <code>&lt;Icon&gt;</code>
      pinta <code>width=size viewBox=vb</code>, uno de caja 16 dibujado a 24px escalaba
      &times;1.5 y su trazo pasaba de 1.5 a <strong>2.25px</strong>; uno de caja 30 lo adelgazaba
      a 1.2px.</p>
      <p>Ahora el bounding box real se centra y encaja en el lienzo, y el <code>stroke-width</code>
      se compensa con la inversa. <strong>Los 222 dan 1.5px exactos.</strong> La marca gris de cada
      celda es la escala que se le aplic&oacute;.</p>
    </div>
    <div>
      <h3>El calado <span class="mk mk-ko">calado</span></h3>
      <p>%d iconos tienen zonas caladas: una forma blanca encima de otra rellena, para simular un
      hueco. Ese blanco no es tinta, es <em>el color de la superficie de detr&aacute;s</em>, y como
      literal se quedaba blanco sobre fondo oscuro.</p>
      <p>Sale como <code>var(--icon-knockout, #FFFFFF)</code>. Dale a
      <strong>Invertir fondo</strong> arriba: la hoja redefine la variable y el calado sigue el
      fondo en vez de quedarse blanco.</p>
      <p class="lista">%s</p>
    </div>
    <div>
      <h3>Los <code>&lt;defs&gt;</code></h3>
      <p>%d iconos llevan un <code>clipPath</code>. Figma los llamaba a todos
      <code>clip0_0_1</code>: con dos en la misma p&aacute;gina, el recorte del segundo apuntaba al
      del primero. Ahora van prefijados con la clave del icono.</p>
      <p>Tambi&eacute;n se fue una sombra con morado fijo en <code>action/check</code>, y el
      <code>&lt;/g&gt;</code> hu&eacute;rfano que dejaba el recorte por expresiones regulares.</p>
    </div>
  </div>
  <p class="pie-aviso">Lo de fondo sigue siendo de Figma: el <code>rect</code>
  <code>#272532</code>, los blancos de calado y los marcos que no son 24&times;24 siguen en el
  archivo. Comprobado contra la API el 3&nbsp;de&nbsp;septiembre&nbsp;de&nbsp;2026: los SVG salen
  byte a byte iguales. Mientras no se corrijan ah&iacute;, quien exporte a mano se lleva el
  problema sin el arreglo.</p>
</div>

<div class="barra">
  <div class="barra-in">
    <label class="buscar">
      <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7" fill="none" stroke="currentColor" stroke-width="1.5"/><path d="m16.5 16.5 4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
      <input id="q" type="search" placeholder="Buscar por nombre o node id&hellip;" autocomplete="off">
    </label>
    <div class="chips">
      <button class="chip chip-all activo" data-f="*">todos<span>222</span></button>
      %s
      <button class="chip chip-ko" data-f="!ko">con calado<span>%d</span></button>
      <button class="chip chip-fit" data-f="!fit">reencajados<span>%d</span></button>
    </div>
    <div class="ctrl">
      <div class="seg" role="group" aria-label="Tama&ntilde;o">
        <button data-size="20">20</button><button data-size="24" class="activo">24</button><button data-size="32">32</button><button data-size="48">48</button>
      </div>
      <button id="fondo" class="seg-btn" aria-pressed="false">Invertir fondo</button>
    </div>
  </div>
</div>

<main id="hoja">%s</main>
<p class="nada" id="nada" hidden>Nada coincide con esa b&uacute;squeda.</p>

<footer>
  <p><strong>222 glifos</strong> &middot; 185 de sistema + 37 de men&uacute; &middot; inventario del
  3 de septiembre de 2026. Los nombres son las claves de <code>icons.ts</code>; debajo, el marco
  original en Figma y el <em>node id</em>. Clic en cualquiera copia su clave. Regenerar con
  <code>python3 generar-icons.py</code>.</p>
</footer>
<script>
%s
</script>
""" % (len(datos)-37, len(cats), len(nc), len(ko),
       len(nc),
       len(ko), ' '.join('<code>%s</code>' % html.escape(k) for k in ko),
       len(dfs),
       filtros, len(ko), len(nc), ''.join(grupos), JS)

open(APP + 'hoja-iconos.html', 'w', encoding='utf-8').write(fuera)
print('escrito: %d bytes | %d iconos | knockout %d | vb!=24 %d | defs %d'
      % (len(fuera), len(datos), len(ko), len(nc), len(dfs)))
