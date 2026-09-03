# Homologación de nomenclatura — Iconos

**Fuente de verdad:** archivo Figma [Nexus V2](https://www.figma.com/design/agWwqm17qIvfveD8CQwSRz/Nexus-V2) — frames `Icons` (`25:4520`) e `Icon-menu` (`25:3428`)
**Fecha del inventario:** 3 de septiembre de 2026
**Objetivo:** dejar cada icono listo para homologar entre Figma, el canon y el código.

> Este documento **no renombra nada**. Registra el estado real y propone el nombre destino, para
> que el renombrado en Figma y la actualización del código se hagan con una lista cerrada.

---

## La regla

`ICONOGRAPHY.md §8` define dos formas, y ambas son válidas:

```
icon/{categoría}/{nombre}                  icon/action/trash
icon/{categoría}/{subcategoría}/{nombre}   icon/nav/arrow/left
```

**El 81 % de los iconos de Figma ya la cumple.** No hace falta inventar una convención: basta
llevar el 19 % restante a la que ya usa la mayoría y que el canon documenta.

---

## Estado del inventario

| | Iconos | Menú sidebar |
|---|---|---|
| **En Figma** | **160** | **37** |
| Declarado en `ICON-COMPONENT.md §4` | 122 | 31 |
| **Diferencia** | **+38** | **+6** |

Los conteos del canon están desactualizados. El total real es **197 nombres**, no 153.

Pero **197 no es el número de iconos dibujables**. 25 de esos nombres son *component sets*
de Figma, y cada uno contiene entre 2 y 8 variantes. Al desplegarlas, el catálogo real es de
**222 glifos** (185 de sistema + 37 de menú) — que es lo que hoy genera `icons.ts`.

| Estado | Iconos | % |
|---|---|---|
| Conformes con §8 | 130 | 81 % |
| Renombrado mecánico | 15 | 9 % |
| Requieren decisión de diseño | 15 | 9 % |

---

## Categorías reales en Figma (17)

`nav` (18) · `builder` (13) · `commerce` (12) · `text` (11) · `data` (11) · `action` (11) ·
`finance` (10) · `system` (7) · `transform` (6) · `status` (6) · `math` (5) · `file` (5) ·
`communication` (5) · `time` (3) · `media` (3) · `t1pagos` (2) · `clipboard` (2)

`ICON-COMPONENT.md §4` lista además **USER** y **MISC**, que no existen como categoría en Figma.
Y Figma tiene **`t1pagos`** y **`clipboard`**, que el canon no lista.

---

## 1. Renombrado mecánico — 15 iconos

Cambian de `icon-{cat}/` a `icon/{cat}/`. Sin ambigüedad: la categoría ya está en el nombre.

| En Figma hoy | Nombre homologado |
|---|---|
| `icon-action/check` | `icon/action/check` |
| `icon-action/check-patch` | `icon/action/check-patch` |
| `icon-edit/image+prod` | `icon/edit/image+prod` |
| `icon-edit/text-left` | `icon/edit/text-left` |
| `icon-info/abacus` | `icon/info/abacus` |
| `icon-info/box-1` | `icon/info/box-1` |
| `icon-info/box-2` | `icon/info/box-2` |
| `icon-info/card-ine` | `icon/info/card-ine` |
| `icon-info/catalog-list` | `icon/info/catalog-list` |
| `icon-info/envelope` | `icon/info/envelope` |
| `icon-info/lightbulb` | `icon/info/lightbulb` |
| `icon-nav/arrow-right` | `icon/nav/arrow-right` |
| `icon-nav/chevron/left` | `icon/nav/chevron/left` |
| `icon-nav/chevron/right` | `icon/nav/chevron/right` |
| `Icon/tablet` | `icon/tablet` |

> `icon/nav/chevron/left` y `icon/nav/chevron/right` ya existen con ese nombre en el frame.
> Al homologar `icon-nav/chevron/left` habrá que resolver el choque.

---

## 2. Requieren decisión de diseño — 15 iconos

No se pueden homologar sin que alguien decida a qué categoría pertenecen o si deben existir.

| En Figma hoy | Qué pasa |
|---|---|
| `able` | sin categoría — asignar una de las 17 existentes |
| `bookmark` | sin categoría — asignar una de las 17 existentes |
| `CVV` | sin categoría — asignar una de las 17 existentes |
| `disabled` | sin categoría — asignar una de las 17 existentes |
| `eclipse` | sin categoría — asignar una de las 17 existentes |
| `icon` | nombre genérico — revisar o retirar |
| `icon-action/` | nombre vacío — retirar |
| `icon-ruler` | nombre genérico — revisar o retirar |
| `Icons` | nombre genérico — revisar o retirar |
| `loader` | sin categoría — asignar una de las 17 existentes |
| `minus 1` | sufijo de duplicado de Figma |
| `plus 1` | sufijo de duplicado de Figma |
| `pos` | sin categoría — asignar una de las 17 existentes |
| `pos-profile` | sin categoría — asignar una de las 17 existentes |
| `top-badge` | sin categoría — asignar una de las 17 existentes |

Tres son basura clara: **`icon-action/`** no tiene nombre (termina en barra), y **`minus 1`** /
**`plus 1`** llevan el sufijo ` 1` que Figma añade al duplicar una capa.

---

## 3. Iconos de menú sidebar — 37 en Figma

El canon declara 31. El frame `Icon-menu` contiene 37 nombres únicos:

```
  antifraude 2/Default
  cashier
  Facturacion nuevo
  gallery
  Icon-menu
  insumos 3
  marketing
  menu/crown
  Nuevo canales
  Nuevo card
  Nuevo config
  Nuevo control
  Nuevo control caja
  Nuevo datos
  Nuevo descuento
  Nuevo develop
  Nuevo envios
  Nuevo home
  Nuevo Hub
  Nuevo link
  Nuevo liquidacion
  Nuevo llave
  Nuevo money
  Nuevo online store
  Nuevo pedidos
  Nuevo permisos
  Nuevo pin
  Nuevo producto
  Nuevo reportes
  Nuevo seguridad
  Nuevo transacciones 2
  Nuevo venta
  Nuevos planes
  payments
  Saldos nuevo
  shopping-bag-03
  User nuevo
```

---

## 3b. Lo que sale de Figma al exportar

Se descargaron 5 iconos como SVG para montar el pipeline. Lo que trae cada archivo:

| Aspecto | Lo que dice el canon | Lo que sale de Figma |
|---|---|---|
| Color | `currentColor` (§7, regla 3) | `#4C4C4C` fijo — y **`#272532`**, que **no está en `COLORS.md`** |
| Stroke | `1.5px` (§1) | `1.2` y `2` |
| Contenido | solo el icono | incluye el **rect de fondo del artboard** (`1646×3499`) y un rect de fondo del propio icono |

Los tres se corrigen al generar `icons.ts`, pero conviene arreglarlos en Figma: mientras estén
así, cualquiera que exporte a mano se lleva el artboard entero dentro del SVG.

`#272532` es el hallazgo que más importa: es un color fuera del sistema de tokens.

---

## 3c. Cómo generar el `icons.ts` completo

`components/icon/icons.ts` está **completo: 222 de 222 glifos**, generado y validado por
**`generar-icons.py`**.

### Uso

```bash
export FIGMA_TOKEN=figd_xxxxxxxxxxxxxxxx
cd components/icon
python3 generar-icons.py                 # los 222
python3 generar-icons.py --solo math     # solo una categoría
python3 generar-icons.py --dry-run       # lista sin descargar nada
python3 generar-icons.py --urls urls.json  # sin token, con las URLs ya resueltas
```

**El token** se saca en Figma → avatar → *Settings* → *Security* → *Personal access tokens* →
*Generate new token*, con permiso de lectura de contenido. Es personal: no se sube al repo.

`--urls` toma un JSON `{node_id: url}` con las descargas ya resueltas y se salta la llamada a la
API. Sirve cuando no hay token a mano: las URLs pueden venir del MCP de Figma, o ser rutas
`file://` a SVG ya bajados. Es la vía por la que se generó el `icons.ts` actual.

### Qué hace

1. Lee `figma-nodes.tsv` — el mapa `nombre en Figma → node_id`, ya inventariado:
   **185 glifos** del frame `Icons` y **37** de `Icon-menu`.
2. Pide los SVG a la API de Figma en lotes de 40, con pausa entre peticiones.
3. Parsea cada SVG como XML y poda lo que no es el icono: el rect del artboard, el `path` de
   fondo del frame padre, los grupos vacíos y los `<filter>` de sombra.
4. Normaliza el color al canon: `currentColor` (también sobre `black`), y el blanco de calado a
   `var(--icon-knockout, #FFFFFF)` para que no se quede blanco en fondo oscuro.
5. Encaja el bounding box real en el lienzo de **24×24**, centrado, y compensa el `stroke-width`
   con la inversa de la escala: el trazo mide 1.5px en pantalla en los 222.
6. Prefija los ids de `<defs>` con la clave del icono y borra los `id` decorativos que nadie
   referencia, para que dos iconos en la misma página no choquen.
7. Escribe `icons.ts` en el formato de `ICON-COMPONENT.md §3.1`.
8. Avisa de lo que quedó sucio: restos de artboard, colores fijos, blancos sin tokenizar, ids
   repetidos, y lista lo que no pudo descargar.

Al escribir la clave elimina el prefijo (`icon/math/at` → `math/at`,
`icon-info/abacus` → `info/abacus`), con lo que **los 15 renombrados mecánicos de la sección 1
quedan resueltos automáticamente**. Los 15 de la sección 2 salen con su nombre tal cual, y ahí sí
hace falta la decisión de diseño.

### Los 34 que faltaban: resueltos

No estaban «perdidos». Eran **variantes dentro de 25 component sets**: en el volcado plano de
metadatos, una variante no sale con el nombre del icono sino como `Property 1=line`,
`Property 1=24x24`, `Property 1=t1envios, Property 2=hand`… El nombre real está en el *frame*
padre, así que al buscar por nombre no aparecían.

Recorriendo el árbol y componiendo `{set}/{variante}` salieron los 66 nodos de esos sets, más 5
nodos sueltos (`bookmark`, `eclipse`, `pos`, `pos-profile`, `top-badge`). `figma-nodes.tsv` pasó
de **163 a 222 filas**, y ya no falta ninguna.

**Regla al desplegar un set:** una fila por glifo distinto. Las variantes que solo cambian de
tamaño (`16x16`/`24x24`, `Sm`/`Md`, `sm`/`md`/`lg`) se colapsan en una sola fila con el nombre
del set; las que son dibujos distintos (`line`/`fill`, `left`/`right`, `ascending`/`descending`)
van como `{set}/{variante}`. Los 17 nodos descartados a propósito —duplicados exactos, tamaños
redundantes, los 4 fotogramas del spinner y los sets con sufijo ` 1`— están al final del `.tsv`,
comentados y con el motivo.

Estos tres salen del rango `61:39xx`, junto a `icon/t1pagos/user` y `icon/t1pagos/perfiles`, y
son de dominio POS. **Propuesta:** `icon/t1pagos/pos`, `icon/t1pagos/pos-profile`,
`icon/t1pagos/top-badge`. El `.tsv` conserva el nombre de Figma hasta que diseño lo confirme.

### Lo que el pipeline destapó al generarlo

Cuatro cosas que no se veían con 5 iconos y sí con 222:

| # | Qué | Alcance | Estado |
|---|---|---|---|
| 1 | El recorte por regex desbalanceaba las etiquetas y dejaba un `</g>` huérfano | 3 de los 5 iconos que ya estaban commiteados | **corregido** — `limpiar()` ahora parsea el SVG como XML |
| 2 | **`clip0_0_1` repetido en 12 iconos.** Figma exporta cada icono como documento suelto y numera desde cero. Con dos en la misma página, el `clip-path` del segundo apunta al recorte del primero | 12 iconos | **corregido** — los ids de `<defs>` se prefijan con la clave del icono |
| 3 | `action/check` traía una **sombra** (`<filter>`) con un morado fijo fuera de tokens. Viene de la instancia colocada en el artboard, no del icono | 1 icono | **corregido** — se retiran los `filter` |
| 4 | **7 iconos usan blanco de *knockout*** (`fill="white"` / `stroke="white"`) para calar sobre una forma rellena | `commerce/box/fill`, `file/excel`, `file/pdf`, `info/abacus`, `math/plus/fill`, `nav/menu/waffle/variant2`, `t1envios/flash-on` | **corregido en código** — sale como `var(--icon-knockout, #FFFFFF)` |
| 5 | **27 iconos no medían 24×24.** Figma exporta cada componente con su marco, y los marcos no son uniformes: 16×16, 25×25, 30×30, 25×17… Como `<Icon>` pinta `width=size height=size viewBox=vb`, un icono de caja 16 a 24px escalaba ×1.5 y su trazo pasaba de 1.5 a **2.25px**; uno de caja 30 lo adelgazaba a 1.2px | 27 iconos | **corregido** — se encajan en el lienzo de 24×24 y el `stroke-width` se compensa con la inversa |

Los dos últimos merecen detalle.

**El calado (4).** Ese blanco no es tinta: es «el color de la superficie de detrás». Como literal
se queda blanco sobre fondo oscuro. Ahora sale del generador como
`var(--icon-knockout, #FFFFFF)`: sin definir nada se comporta igual que antes, y quien pinte sobre
otra superficie define la variable. **Esto es un parche en el consumidor, no el arreglo de fondo:**
lo correcto sigue siendo dibujar el hueco como hueco en Figma (`fill-rule="evenodd"`, sin blanco
encima), que es lo único que deja el icono monocromo de verdad. Sigue en la lista de acciones.

**El lienzo (5).** Este era el que de verdad se veía: rompía la regla de 1.5px del canon en 27 de
222 iconos, y hacía que a igual `size` unos ocuparan más caja óptica que otros. La normalización
va en el generador, no a mano: se centra y escala el bounding box real dentro de 24×24 y se
reparte la inversa de esa escala en el `stroke-width`. Comprobado: **los 222 dan 1.5px exactos**.
Lo de fondo también es de Figma — los componentes deberían medir todos 24×24.

---

### Estado del archivo Figma

Comprobado contra la API el **3 de septiembre de 2026**: los SVG que devuelve Figma son byte a
byte los mismos que generaron este `icons.ts`. El `rect` de fondo `#272532`, los blancos de
calado y los marcos que no son 24×24 **siguen ahí**. Si se han corregido en el editor, el cambio
no ha llegado a la API todavía — suele ser porque está sin guardar, en una *branch* de Figma, o
en otro archivo.

Cuando esté publicado, basta con volver a correr:

```bash
export FIGMA_TOKEN=figd_xxxxxxxx
python3 generar-icons.py
```

---

## 4. Qué hacer con esto

| # | Acción | Dónde | Bloquea a |
|---|---|---|---|
| 1 | Renombrar los 15 mecánicos | Figma | código y canon |
| 2 | Decidir categoría de los 15 restantes | equipo de diseño | 1 |
| 3 | Retirar `icon-action/`, `minus 1`, `plus 1` | Figma | — |
| 4 | Actualizar los conteos de §4 a 160 + 37 nombres / **222 glifos** | canon | — |
| 5 | Dibujar el calado de los 7 iconos como hueco real (`fill-rule="evenodd"`) | Figma | retirar `--icon-knockout` |
| 6 | Arreglar en Figma el `#272532` de fondo y los `stroke-width` 1.2 / 2 | Figma | exportación manual |
| 7 | Confirmar `icon/t1pagos/{pos, pos-profile, top-badge}` | equipo de diseño | 1 |
| 8 | Llevar a 24×24 los 27 componentes con marco distinto | Figma | retirar el `<g transform>` |

> Ninguna bloquea al código: el pipeline ya normaliza nombre, lienzo, trazo y color al generar.
> Son **higiene en Figma** — mientras no se hagan, el `icons.ts` sale correcto pero llevando
> encima el arreglo (`<g transform>` en 27 iconos, `--icon-knockout` en 7), y quien exporte a mano
> desde Figma se lleva el problema sin corregir.
| 5 | Añadir `t1pagos` y `clipboard` a las categorías de §4 | canon | — |
| 6 | Resolver si `USER` y `MISC` existen | equipo de diseño | 5 |
| 7 | Regenerar `icons.ts` con los nombres homologados | código | 1, 2 |

El paso 7 es el que cierra el círculo con el código: hoy `@t1/nexus-react` no tiene catálogo
—su `<Icon />` recibe el path SVG crudo— y `t1components` nombra los archivos por hash.

---

## Alcance de este documento

Cubre los **197 iconos** de los frames `Icons` e `Icon-menu`. **No cubre** las 256 entradas del
frame `Banderas` ni las 83 de `Banks`, que son catálogos aparte y necesitan su propio cruce.
