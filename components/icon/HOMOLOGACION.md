# Homologación de componentes — Nexus V2

**Fuente de verdad:** archivo Figma [Nexus V2](https://www.figma.com/design/agWwqm17qIvfveD8CQwSRz/Nexus-V2) — página **`Components`** (`0:1`)
**Fecha del inventario:** 3 de septiembre de 2026
**Objetivo:** dejar cada componente del archivo listo para homologar entre Figma, el canon y el código.

> Este documento **no renombra nada**. Registra el estado real y propone el nombre destino, para
> que el renombrado en Figma y la actualización del código se hagan con una lista cerrada.

---

## El criterio

**Una fila por componente de Figma.** Un componente es un nodo `COMPONENT` (⬦) o
`COMPONENT_SET`; los frames, grupos e instancias no cuentan. Las variantes **no generan filas**:
se listan como propiedad y valores en la columna correspondiente.

Este es el criterio único para todas las familias. Un botón con 18 variantes es **un**
componente, igual que un logo con 2 y un icono con 4.

De ahí salen dos unidades que conviene no confundir:

| Unidad | Qué es | Total en el archivo |
|---|---|---|
| **Componente raíz** | lo que se homologa: el set, o el componente suelto | **331** |
| **Nodo componente** | cada `COMPONENT` del archivo, variantes incluidas | **668** |

331 = 148 sets + 183 componentes sueltos. 668 = 485 variantes dentro de sets + esos mismos 183.

> **Excepción declarada, no un criterio distinto.** `icons.ts` necesita una clave por glifo
> dibujable, así que de los 142 componentes de iconos se derivan **222 glifos** desplegando las
> variantes que son dibujos distintos. Es una derivación para el código, documentada en §1.4;
> el conteo de homologación sigue siendo 142.

### La regla de nombre

`ICONOGRAPHY.md §8` ya define la forma para iconos, y sirve para todo:

```
{familia}/{categoría}/{nombre}
```

Minúsculas, sin espacios, sin `&`, sin acentos, sin sufijos de duplicado de Figma.

---

## Dónde está el sistema

El archivo tiene dos páginas. La que Figma lista primero **no** es la que importa:

| Página | Node | Contenido |
|---|---|---|
| `Cover & documentation` | `232:14855` | portada, guía de uso, estructura, principios — 0 componentes |
| **`Components`** | **`0:1`** | **todo el sistema: 331 componentes** |

Dentro de `Components`, los frames de primer nivel:

| Frame | Node | Sets | Sueltos | **Raíz** | Variantes |
|---|---|---:|---:|---:|---:|
| `Icons` | `25:4520` | 26 | 116 | **142** | 66 |
| `Icons-logos` | `244:12451` | 84 | 9 | **93** | 198 |
| `Icon-menu` | `25:3428` | 1 | 33 | **34** | 2 |
| `ATOMS` | `1:652` | 22 | 3 | **25** | 155 |
| `MOLECULES 4` | `224:9054` | 5 | 4 | **9** | 20 |
| `MOLECULES 3` | `244:17077` | 3 | 4 | **7** | 14 |
| `MOLECULES 2` | `69:4133` | 0 | 7 | **7** | 0 |
| `MOLECULES` | `5:3591` | 4 | 1 | **5** | 14 |
| `MENU` | `232:7239` | 1 | 0 | **1** | 9 |
| `Item menu` | `561:8931` | 1 | 0 | **1** | 4 |
| `item submenu` | `561:8969` | 1 | 0 | **1** | 3 |
| *(sueltos en la raíz de la página)* | — | 0 | 6 | **6** | 0 |
| **TOTAL** | | **148** | **183** | **331** | **485** |

Los 6 sueltos de la última fila están **fuera de todo frame**, tirados en el lienzo:
`preference` (`1233:8264`), `preference-vertical` (`1233:8215`), `filter-horizontal`
(`1233:8161` **y** `1233:8265`, duplicado), `mail-open` (`1233:8151`),
`message-notification-01` (`1233:8150`). Los cinco últimos nombres no siguen ninguna
convención del archivo y parecen pegados de una librería externa.

---

## Lo que no es componente

Tres frames grandes no contienen ni un solo componente. Es el hallazgo que más cuesta ver desde
Figma, porque **visualmente se ven igual** que los que sí lo son:

| Frame | Node | Qué contiene de verdad | Consecuencia |
|---|---|---|---|
| `Banderas` | `244:10459` | **255 instancias**, 0 componentes | los componentes viven en otra librería; este archivo solo los consume |
| `Banks` | `244:10134` | **82 entradas** como frames y rectángulos, 0 componentes | no se pueden instanciar ni publicar |
| `MOLECULES 5` | `1134:8526` | 263 nodos: frames, textos e instancias | es una maqueta de especificación, no componentes |

Detalle en §7 y §8.

---

## Los cinco problemas transversales

Salen en todas las familias y son los que hay que resolver a nivel de archivo, no caso por caso:

| # | Problema | Alcance | Dónde |
|---|---|---:|---|
| 1 | **Propiedad sin renombrar** — el set usa `Property 1` en vez de decir qué varía | **126 de 148 sets (85 %)** | todas |
| 2 | **Variantes sin nombrar** — `Variant2`, `Variant8`, `Property 13` | **20 sets** | §3, §4, §1 |
| 3 | **Nombres repetidos** — dos componentes distintos con el mismo nombre | **9 nombres, 18 nodos** | §1, §3, §4, §5 |
| 4 | **Nombres con espacio, `&`, dígito inicial o barra final** | **55 componentes** | §2 sobre todo |
| 5 | **Nombre por defecto de Figma** — `Component`, `Frame 1000007109`, `icon`, `icon-action/` | **5 componentes** | §1, §3, §5 |

### Los 9 nombres repetidos

| Nombre | Nodos | Familia |
|---|---|---|
| `input a` | `1:1195`, `1:1233` | ATOMS |
| `input b` | `1:1216`, `1:1258` | ATOMS |
| `icon` | `25:5039`, `25:5061` | Icons |
| `able` | `25:4915`, `25:4928` | Icons |
| `disabled` | `25:4921`, `25:4933` | Icons |
| `icon/finance/store-credit` | `55:3994`, `55:3995` | Icons |
| `Tabs` | `119:4183` (set), `119:4181` (comp) | MOLECULES 4 |
| `t1score-imagotipo` | `244:12538`, `1184:8119` | Icons-logos |
| `filter-horizontal` | `1233:8161`, `1233:8265` | raíz de página |

> El recuento de la fila 4 usa un criterio estricto y comprobable: espacio, `&`, dígito inicial,
> barra final o nombre por defecto de Figma. No incluye las mayúsculas inconsistentes
> (`Telmex-iso`, `TikTok-logo`, `grupoAmPm`), que se listan aparte en §3.3.

Ninguno se puede resolver desde el código: **un registro no admite dos claves iguales**, así que
mientras existan, cualquier catálogo generado tiene que elegir uno y descartar el otro en
silencio. Es la única de las cinco que bloquea de verdad.

---

# 1. Iconos — 142 componentes

Frame `Icons` (`25:4520`). 26 sets + 116 sueltos. **El 81 % ya cumple `ICONOGRAPHY.md §8`.**

| Estado | Componentes | % |
|---|---:|---:|
| Conformes con §8 | 112 | 79 % |
| Renombrado mecánico | 15 | 11 % |
| Requieren decisión de diseño | 15 | 11 % |

### Categorías reales en Figma (17)

`nav` (18) · `builder` (13) · `commerce` (12) · `text` (11) · `data` (11) · `action` (11) ·
`finance` (10) · `system` (7) · `transform` (6) · `status` (6) · `math` (5) · `file` (5) ·
`communication` (5) · `time` (3) · `media` (3) · `t1pagos` (2) · `clipboard` (2)

`ICON-COMPONENT.md §4` lista además **USER** y **MISC**, que no existen como categoría en Figma.
Y Figma tiene **`t1pagos`** y **`clipboard`**, que el canon no lista.

## 1.1 Renombrado mecánico — 15

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

## 1.2 Requieren decisión de diseño — 15

No se pueden homologar sin que alguien decida a qué categoría pertenecen o si deben existir.

| En Figma hoy | Qué pasa |
|---|---|
| `able` | sin categoría — y **duplicado** (`25:4915`, `25:4928`) |
| `bookmark` | sin categoría — asignar una de las 17 existentes |
| `CVV` | sin categoría — asignar una de las 17 existentes |
| `disabled` | sin categoría — y **duplicado** (`25:4921`, `25:4933`) |
| `eclipse` | sin categoría — asignar una de las 17 existentes |
| `icon` | nombre por defecto — **dos componentes distintos lo usan** |
| `icon-action/` | nombre vacío, termina en barra — retirar |
| `icon-ruler` | nombre genérico — revisar o retirar |
| `Icons` | nombre genérico — revisar o retirar |
| `loader` | sin categoría — 4 de sus 5 variantes sin nombrar |
| `minus 1` | sufijo de duplicado de Figma |
| `plus 1` | sufijo de duplicado de Figma |
| `pos` | sin categoría — asignar una de las 17 existentes |
| `pos-profile` | sin categoría — asignar una de las 17 existentes |
| `top-badge` | sin categoría — asignar una de las 17 existentes |

Tres son basura clara: **`icon-action/`** no tiene nombre (termina en barra), y **`minus 1`** /
**`plus 1`** llevan el sufijo ` 1` que Figma añade al duplicar una capa.

`pos`, `pos-profile` y `top-badge` salen del rango `61:39xx`, junto a `icon/t1pagos/user` y
`icon/t1pagos/perfiles`, y son de dominio POS. **Propuesta:** `icon/t1pagos/pos`,
`icon/t1pagos/pos-profile`, `icon/t1pagos/top-badge`. El `.tsv` conserva el nombre de Figma
hasta que diseño lo confirme.

Y uno más, que no es de categoría sino de carácter: **`icon/nav/chevron/up&down`**
(`26:11545`) lleva un `&`. Propuesta: `icon/nav/chevron/up-down`.

## 1.3 Lo que sale de Figma al exportar

| Aspecto | Lo que dice el canon | Lo que sale de Figma |
|---|---|---|
| Color | `currentColor` (§7, regla 3) | `#4C4C4C` fijo — y **`#272532`**, que **no está en `COLORS.md`** |
| Stroke | `1.5px` (§1) | `1.2` y `2` |
| Contenido | solo el icono | incluye el **rect de fondo del artboard** (`1646×3499`) y un rect de fondo del propio icono |

Los tres se corrigen al generar `icons.ts`, pero conviene arreglarlos en Figma: mientras estén
así, cualquiera que exporte a mano se lleva el artboard entero dentro del SVG.

`#272532` es el hallazgo que más importa: es un color fuera del sistema de tokens.

## 1.4 De 142 componentes a 222 glifos

`components/icon/icons.ts` está **completo: 222 de 222 glifos**, generado y validado por
**`generar-icons.py`**.

Los 34 que en su momento «faltaban» no estaban perdidos: eran **variantes dentro de 26 sets**.
En un volcado plano, una variante no sale con el nombre del icono sino como `Property 1=line`,
`Property 1=24x24`, `Property 1=t1envios, Property 2=hand`… El nombre real está en el nodo padre.
Es exactamente el mismo efecto que hace que `Banderas` parezca tener 255 componentes y tenga 0.

**Regla al desplegar un set:** una fila por glifo distinto. Las variantes que solo cambian de
tamaño (`16x16`/`24x24`, `Sm`/`Md`, `sm`/`md`/`lg`) se colapsan en una sola fila con el nombre
del set; las que son dibujos distintos (`line`/`fill`, `left`/`right`, `ascending`/`descending`)
van como `{set}/{variante}`. Los 17 nodos descartados a propósito —duplicados exactos, tamaños
redundantes, los 4 fotogramas del spinner y los sets con sufijo ` 1`— están al final de
`figma-nodes.tsv`, comentados y con el motivo.

### Uso

```bash
export FIGMA_TOKEN=figd_xxxxxxxxxxxxxxxx
cd components/icon
python3 generar-icons.py                   # los 222
python3 generar-icons.py --solo math       # solo una categoría
python3 generar-icons.py --dry-run         # lista sin descargar nada
python3 generar-icons.py --urls urls.json  # sin token, con las URLs ya resueltas
```

**El token** se saca en Figma → avatar → *Settings* → *Security* → *Personal access tokens* →
*Generate new token*, con permiso de lectura de contenido. Es personal: no se sube al repo.

`--urls` toma un JSON `{node_id: url}` con las descargas ya resueltas y se salta la llamada a la
API. Sirve cuando no hay token a mano: las URLs pueden venir del MCP de Figma, o ser rutas
`file://` a SVG ya bajados. Es la vía por la que se generó el `icons.ts` actual.

### Qué hace

1. Lee `figma-nodes.tsv` — el mapa `nombre en Figma → node_id`: **185 glifos** del frame `Icons`
   y **37** de `Icon-menu`.
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
`icon-info/abacus` → `info/abacus`), con lo que **los 15 renombrados mecánicos de §1.1 quedan
resueltos automáticamente**. Los 15 de §1.2 salen con su nombre tal cual, y ahí sí hace falta la
decisión de diseño.

## 1.5 Lo que el pipeline destapó

Cinco cosas que no se veían con 5 iconos y sí con 222:

| # | Qué | Alcance | Estado |
|---|---|---|---|
| 1 | El recorte por regex desbalanceaba las etiquetas y dejaba un `</g>` huérfano | 3 de los 5 iconos ya commiteados | **corregido** — `limpiar()` parsea el SVG como XML |
| 2 | **`clip0_0_1` repetido en 12 iconos.** Figma exporta cada icono como documento suelto y numera desde cero. Con dos en la misma página, el `clip-path` del segundo apunta al recorte del primero | 12 iconos | **corregido** — los ids de `<defs>` se prefijan con la clave |
| 3 | `action/check` traía una **sombra** (`<filter>`) con un morado fijo fuera de tokens. Viene de la instancia colocada en el artboard, no del icono | 1 icono | **corregido** — se retiran los `filter` |
| 4 | **7 iconos usan blanco de *knockout*** (`fill="white"` / `stroke="white"`) para calar sobre una forma rellena | `commerce/box/fill`, `file/excel`, `file/pdf`, `info/abacus`, `math/plus/fill`, `nav/menu/waffle/variant2`, `t1envios/flash-on` | **corregido en código** — sale como `var(--icon-knockout, #FFFFFF)` |
| 5 | **27 iconos no medían 24×24.** Figma exporta cada componente con su marco, y los marcos no son uniformes: 16×16, 25×25, 30×30, 25×17… Como `<Icon>` pinta `width=size height=size viewBox=vb`, un icono de caja 16 a 24px escalaba ×1.5 y su trazo pasaba de 1.5 a **2.25px**; uno de caja 30 lo adelgazaba a 1.2px | 27 iconos | **corregido** — se encajan en 24×24 y el `stroke-width` se compensa con la inversa |

Los dos últimos merecen detalle.

**El calado (4).** Ese blanco no es tinta: es «el color de la superficie de detrás». Como literal
se queda blanco sobre fondo oscuro. Ahora sale del generador como
`var(--icon-knockout, #FFFFFF)`: sin definir nada se comporta igual que antes, y quien pinte sobre
otra superficie define la variable. **Esto es un parche en el consumidor, no el arreglo de fondo:**
lo correcto sigue siendo dibujar el hueco como hueco en Figma (`fill-rule="evenodd"`, sin blanco
encima), que es lo único que deja el icono monocromo de verdad.

**El lienzo (5).** Este rompía la regla de 1.5px del canon en 27 de 222 iconos, y hacía que a
igual `size` unos ocuparan más caja óptica que otros. La normalización va en el generador, no a
mano: se centra y escala el bounding box real dentro de 24×24 y se reparte la inversa de esa
escala en el `stroke-width`. Comprobado: **los 222 dan 1.5px exactos**. Lo de fondo también es de
Figma — los componentes deberían medir todos 24×24.

## 1.6 Verlos: `hoja-iconos.html`

`generar-hoja.py` construye una hoja de contacto con los 222 en una rejilla, leyendo `icons.ts` y
`figma-nodes.tsv`. Es la forma de comprobar de un vistazo que todos dibujan lo que deben — las
validaciones del generador son estructurales, no visuales.

```bash
cd components/icon
python3 generar-hoja.py        # escribe hoja-iconos.html
open hoja-iconos.html
```

Trae búsqueda, filtro por categoría, cambio de tamaño (20/24/32/48) y un botón **Invertir fondo**,
que es como se comprueba el calado: la hoja redefine `--icon-knockout` y se ve si los 7 iconos
afectados siguen el fondo en vez de quedarse blancos. Cada celda muestra el marco original en
Figma y el node id, y al hacer clic copia la clave.

## 1.7 Estado del archivo Figma

Comprobado contra la API el **3 de septiembre de 2026**: los SVG que devuelve Figma son byte a
byte los mismos que generaron este `icons.ts`. El `rect` de fondo `#272532`, los blancos de
calado y los marcos que no son 24×24 **siguen ahí**. Si se han corregido en el editor, el cambio
no ha llegado a la API todavía — suele ser porque está sin guardar, en una *branch* de Figma, o
en otro archivo.

---

# 2. Iconos de menú — 34 componentes

Frame `Icon-menu` (`25:3428`). 33 sueltos + 1 set (`menu/crown`, `Color`/`Line`).
El canon declara 31.

**Es la familia peor nombrada del archivo: 30 de 34 tienen espacio en el nombre**, y ninguno
sigue la forma `{familia}/{categoría}/{nombre}`.

El patrón es un adjetivo en español pegado al concepto, **y ni siquiera en el mismo orden**:

| Orden | Nº | Ejemplos |
|---|---:|---|
| `Nuevo {cosa}` | 24 | `Nuevo pedidos`, `Nuevo canales`, `Nuevo home`, `Nuevo llave`, `Nuevo Hub` |
| `{cosa} nuevo` | 3 | `Saldos nuevo`, `Facturacion nuevo`, `User nuevo` |
| plural | 1 | `Nuevos planes` |
| sin «Nuevo» | 6 | `menu/crown`, `payments`, `marketing`, `gallery`, `antifraude 2/Default`, `insumos 3` |

«Nuevo» no describe el icono: describe que en su momento sustituyó a otro. Cuando el viejo ya no
existe, el adjetivo no distingue nada — solo estorba.

Además arrastran sufijos de duplicado de Figma: `antifraude 2/Default`, `insumos 3`,
`Nuevo transacciones 2`.

**Propuesta:** `icon/menu/{nombre}` en minúsculas, sin «Nuevo», sin acentos y en inglés como el
resto del sistema. `Nuevo pedidos` → `icon/menu/orders`; `Saldos nuevo` → `icon/menu/balance`;
`Nuevo liquidacion` → `icon/menu/settlement`. Los 34 caben en una tabla de renombrado mecánico
en cuanto diseño confirme el idioma.

> **Decisión pendiente:** el resto del sistema está en inglés (`action`, `commerce`, `finance`).
> Esta familia está en español. Hay que elegir uno para todo el archivo.

---

# 3. Logos e imagotipos — 93 componentes

Frame `Icons-logos` (`244:12451`). 84 sets + 9 sueltos, **198 variantes**. Es la segunda familia
más grande del archivo y **la que más divergencia acumula**, porque creció por acumulación: cada
logo se añadió con la convención de quien lo añadió.

## 3.1 Ocho sufijos para tres conceptos

| Sufijo | Componentes | Ejemplos |
|---|---:|---|
| `-iso` | 28 | `dhl-iso`, `meli-iso`, `whatsapp-iso` |
| `-imagotipo` | 16 | `t1pagos-imagotipo`, `spei-imagotipo` |
| *(sin sufijo)* | 14 | `moova`, `walmart`, `cargamos`, `tookan` |
| `-iso-plataforma` | 13 | `magento-iso-plataforma`, `wix-iso-plataforma` |
| `-iso-marketplace` | 8 | `linio-iso-marketplace`, `coppel-iso-marketplace` |
| `-isotipo` | 6 | `mastercard-isotipo`, `oxxo-isotipo` |
| `-logotipo` | 4 | `visa-logotipo`, `amex-logotipo` |
| `-logo` | 4 | `redpack-logo`, `fedex-logo`, `TikTok-logo` |

`-iso`, `-isotipo` e `-iso-plataforma` significan lo mismo. `-logo` y `-logotipo` también.
`BRAND-ASSETS.md` usa una novena forma —`t1pagos-default.svg`— que no coincide con ninguna.

Y el sufijo está haciendo **dos trabajos a la vez**: decir qué tipo de marca es (isotipo /
logotipo / imagotipo) y decir dónde se usa (plataforma / marketplace). Son dos ejes distintos y
no deberían compartir el mismo hueco del nombre. Es lo que produce el caso de `tienda-nube`, que
existe **tres veces con tres formas**:

```
tienda-nube-iso-plataforma      244:13005
icono/plataforma/Tienda nube    244:14526
Component                       244:13446   ← sin nombrar
```

**Propuesta:** `logo/{contexto}/{marca}` — el contexto es el eje de uso (`pago`, `carrier`,
`marketplace`, `plataforma`, `social`, `marketing`, `t1`), y el tipo de marca pasa a ser una
**propiedad de variante**, que es donde le toca.

## 3.2 Treinta vocabularios para «a color o en negro»

Los 84 sets usan **30 combinaciones distintas de valores** para decir esencialmente lo mismo:

| Valores | Sets |
|---|---:|
| `Black` / `Color` | 24 |
| `black` / `color` | 8 |
| `Default` / `White` | 5 |
| `Default` / `Variant2` | 4 |
| `color` / `off` | 4 |
| `Default` / `b/n` | 3 |
| `Black` / `Color` / `app` | 3 |
| `Color` / `app` | 3 |
| `Default` / `bn` | 2 |
| `color` / `gray` | 2 |
| …y 20 combinaciones más, casi todas de un solo uso | 20 |

`Black`/`black`, `b/n`/`bn`, `off`/`gray`/`White` — mismo concepto, ocho grafías. `b/n` además
**lleva una barra**, que es el separador de jerarquía del propio sistema de nombres.

**Propuesta:** una sola propiedad `tono` con tres valores fijos: `color`, `mono`, `inverso`.
Y una segunda, `forma`, donde hoy conviven `isologo`, `app`, `SinEnvolvente`, `Sin BG`,
`rectangle`, `square`, `Isotipo`, `Fill`.

## 3.3 Lo roto

| Componente | Node | Qué pasa |
|---|---|---|
| `Component` | `244:13446` | **sin nombrar** — es el nombre por defecto de Figma |
| `analitycs-iso` | `680:8923` | **typo** — es *analytics* |
| `t1score-imagotipo` | `244:12538` y `1184:8119` | **duplicado**, con variantes distintas |
| `t1-logotipo` / `t1-logotipo-2` | `244:12581` / `244:13628` | duplicado; el `-2` es sufijo de Figma |
| `total-iso` / `total-iso-v2` | `244:13582` / `244:13598` | duplicado; y `total-iso` usa la propiedad `Totalplay` con el valor **`ml`**, copiado de Mercado Libre |
| `shopify-iso` / `shopify-iso-plataforma` | `244:14275` / `244:14257` | duplicado |
| `stripe-iso` / `stripe-logotipo` | `244:14303` / `244:12669` | duplicado |
| `amazon-iso` / `amazon-iso-marketplace` | `244:13558` / `244:13708` | duplicado |
| `meli-iso` / `meli-iso-marketplace` | `244:13566` / `244:13794` | duplicado |
| `shein-iso` / `shein-iso-marketplace` | `244:13749` / `244:13770` | duplicado |
| `TikTok-logo` / `tiktok-isotipo` / `tiktokshop` | `244:14490` / `244:12852` / `244:14483` | tres capitalizaciones |
| `Telmex-iso` / `telmex-iso-marketplace` | `244:13758` / `244:13781` | mayúscula inconsistente |
| `j&texpress-iso`, `fb&IG-iso` | `244:13292`, `680:8926` | **`&` en el nombre** |
| `grupoAmPm` | `244:13399` | camelCase, único caso del archivo |
| `7-eleven-imagotipo`, `99min-iso` | `244:12720`, `244:14003` | empiezan con dígito |
| `payment card` | `244:14549` | espacio; y 2 de sus 12 variantes son `Variant11`/`Variant12` |
| `t1pagos-imagotipo` | `244:12494` | variantes `Property 13`, `Property 14`, `T1 pagos`, `White` — **dos sin nombrar y una con espacio** |
| `amazon-iso-marketplace` | `244:13708` | usa **dos propiedades** (`Property 1=color`, `Property 2=black`) donde debería usar una con dos valores |

Diez de estos son **el mismo logo dos veces**. Antes de renombrar hay que decidir cuál se queda.

## 3.4 La propiedad lleva el nombre de la marca

12 sets nombran la propiedad con la marca en vez de con lo que varía: `Claroshop{color|imagotipo|off}`,
`Sears{Isotipo|color|off}`, `Sanborns`, `Amazon`, `ML`, `Totalplay`, `Aliexpress`, `Shein`,
`Shopify`, `Stripe`, `default`, `Style`.

La marca ya está en el nombre del componente. La propiedad tiene que decir **qué cambia entre
variantes**, no repetir de quién es el logo.

---

# 4. Átomos — 25 componentes

Frame `ATOMS` (`1:652`). 22 sets + 3 sueltos, **155 variantes** — la familia con más variantes
por componente del archivo.

| Componente | Node | Var | Propiedades |
|---|---|---:|---|
| `TextField` | `1:961` | 20 | `Type{Input\|Multiline\|Prefix\|Subfix}` · `State{Default\|Disabled\|Error\|Focus\|Hover}` |
| `Button` | `1:669` | 18 | `Type{Icon\|Link\|Primary\|Secondary}` · `Status{Default\|Disabled\|Hover\|Loading\|Pressed}` |
| `user-letter` | `1:1470` | 18 | `Type{Photo\|Store\|User}` · `Size{Md\|Sm}` · `Status{Default\|Hover\|Pressed}` |
| `Control` | `1:1089` | 17 | `Type{Check\|Radi\|Radio\|Selec\|Select\|Switch}` · `State{…}` |
| `text-link` | `1:909` | 12 | `Type{Disclosure\|Multiline\|Text}` · `Status{…}` |
| `icon/exclamation-triangle` | `1:1585` | 10 | `Property 1{Alert\|Error\|Info\|Success\|Warning}` · `Style{Default\|Lin\|Line}` |
| `Select` | `1:1534` | 8 | `Type{Check\|Radio}` · `Status{Disabled\|Hover\|Off\|On}` |
| `Chips` | `1:1433` | 5 | `Type{Blue\|Gray\|Green\|Red\|Violet}` |
| `button/ia` | `328:9117` | 5 | `Property 1{Default\|Hover\|Loading\|Pressed\|Variant5}` |
| `Social` | `667:7717` | 5 | `Property 1{Default\|Disabled\|Error\|Focus\|Hover}` |
| `Action 1` | `1:760` | 4 | `Property 1{Default\|Disabled\|Hover\|Pressed}` |
| `action2` | `1:777` | 4 | `Property 1{…}` |
| `input a` | `1:1195` | 4 | `Property 1{Default\|Variant2\|Variant3\|Variant4}` |
| `input b` | `1:1216` | 4 | idem |
| `input a` | `1:1233` | 4 | idem — **duplicado** |
| `input b` | `1:1258` | 4 | idem — **duplicado** |
| `dropdown` | `1:1351` | 4 | `Status{Default\|Error\|Focus\|Hover}` |
| `fav` | `1:1527` | 2 | `Property 1{off\|on}` |
| `premium` | `1:1567` | 2 | `Property 1{Default\|Variant2}` |
| `Image-radio` | `1:1559` | 2 | `Property 1{Default\|Select}` |
| `Input` | `81:4700` | 2 | `Property 1{Error\|number}` |
| `Badges` | `1:1423` | 1 | `Type{IA}` |
| `Barra-Progreso B` | `526:9195` | — | componente suelto |
| `progress select` | `1:1522` | — | componente suelto |
| `Button/Split` | `5:3939` | — | componente suelto |

## 4.1 Typos dentro de las variantes

Estos rompen el componente en silencio: quien selecciona `Type=Radio` no encuentra la variante
que en realidad se llama `Radi`.

| Componente | Valor roto | Debería ser |
|---|---|---|
| `Control` (`1:1089`) | `Radi` | `Radio` |
| `Control` (`1:1089`) | `Selec` | `Select` |
| `icon/exclamation-triangle` (`1:1585`) | `Lin` | `Line` |
| `Carga` (`224:6092`, §5) | `7` | `70` |

## 4.2 El botón está partido en cinco componentes

`ATOMS.md §1` declara **8 variantes de botón** en un solo componente. En Figma son **cinco
componentes distintos**, con cinco convenciones de nombre distintas, y una de las 8 vive dentro
de un componente que no es un botón:

| Variante del canon | Dónde está de verdad |
|---|---|
| Primary, Secondary, Link, Icon | `Button` (`1:669`) — `Type{…}` |
| Split | `Button/Split` (`5:3939`) — componente suelto |
| IA | `button/ia` (`328:9117`) |
| Social | `Social` (`667:7717`) |
| Disclosure | `text-link` (`1:909`) — `Type=Disclosure` |

`Button`, `Button/Split`, `button/ia`, `Social`. Mayúscula, barra, minúscula, y ninguna.
`ATOMS.md:65` ya cita los 4 primeros nodos, así que el canon **sabe** que están separados y aun
así los documenta como uno. Cualquiera que implemente `<Button variant="split">` leyendo el canon
va a buscar una variante que en Figma no existe.

**Propuesta:** un solo set `button` con `tipo{primary|secondary|link|icon|split|ia|social|disclosure}`
× `estado{default|hover|pressed|disabled|loading}`. Si no se pueden unificar en Figma, al menos
homologar los nombres: `button/split`, `button/ia`, `button/social`.

## 4.3 Los cuatro `input`

`input a` y `input b` existen **dos veces cada uno** (`1:1195`/`1:1233`, `1:1216`/`1:1258`), los
cuatro con `Property 1{Default|Variant2|Variant3|Variant4}` — es decir, **12 variantes sin
nombrar**. Y por separado existen `TextField` (`1:961`, 20 variantes, bien nombrado) e `Input`
(`81:4700`).

Seis componentes para el mismo átomo. `TextField` es el único que está homologado; los otros
cinco hay que decidir si son casos que le faltan o si sobran.

---

# 5. Moléculas — 28 componentes

Repartidas en cuatro frames, sin criterio visible de qué va en cuál.

| Frame | Componentes |
|---|---|
| `MOLECULES` (`5:3591`) | `Number-calendar`, `buscador_desktop`, **`Frame 1000007109`**, `Upload`, `Color Picker` |
| `MOLECULES 2` (`69:4133`) | `Modal`, `Slot/modal/empty`, `Slot/modal/Map`, `Slot/modal/Toma+logo`, `Slot/modal/Text`, `Slot/modal/Top`, `Slot/modal/button` |
| `MOLECULES 3` (`244:17077`) | `Timeline`, `Timeline/indicator`, `Messages`, `Slot/timeline/empty`, `Slot/timeline/products`, `Slot/timeline/address`, `Slot/timeline/customer info` |
| `MOLECULES 4` (`224:9054`) | `Steps container`, `Slot/steps/row`, `Carga`, `Tabs`, `Item pestañas`, `Slot/steps/card`, `Slot/steps/empty`, `Pestañas`, `Tabs` |
| `MOLECULES 5` (`1134:8526`) | **ninguno** — 263 nodos sin un solo componente |

## 5.1 Lo bueno: `Slot/`

**El patrón `Slot/{componente}/{parte}` es la mejor convención del archivo.** Es la única familia
donde el nombre dice a qué pertenece cada pieza y qué hueco llena, y se sostiene sola en tres
frames distintos. Es el modelo a seguir para todo lo demás.

Dos detalles: `Slot/modal/Toma+logo` y `Slot/timeline/customer info` rompen el patrón con una
mayúscula, un `+` y un espacio.

## 5.2 Lo roto

| Qué | Node | Problema |
|---|---|---|
| `Frame 1000007109` | `99:3932` | **set sin nombrar** — nombre por defecto de Figma, con `Variant2` dentro |
| `Tabs` (set) / `Tabs` (comp) | `119:4183` / `119:4181` | mismo nombre, dos componentes |
| `Pestañas` / `Item pestañas` | `119:4182` / `119:4218` | **español**, con `ñ`, junto a los `Tabs` en inglés — es el mismo componente traducido |
| `Carga` | `224:6092` | español; variantes `0,10,20,30,40,50,60,7,80,90` — **`7` debería ser `70`** |
| `buscador_desktop` | `87:3934` | español y **guion bajo**, el único del archivo |
| `Number-calendar` | `67:5227` | mezcla inglés con guion medio y mayúscula |
| `Color Picker` | `99:4011` | espacio |
| `Steps container` | `224:5753` | espacio |
| `MOLECULES 5` | `1134:8526` | 263 nodos, 0 componentes — o se componentiza o no es parte del sistema |

`Tabs` + `Pestañas` + `Item pestañas` es el caso más claro de todo el archivo: **el mismo
componente existe en dos idiomas a la vez**, y ninguno es la fuente de verdad.

---

# 6. Menú — 3 componentes

| Componente | Node | Var | Valores |
|---|---|---:|---|
| `Menu` | `232:7297` | 9 | `POS`, `POS-2`, `T1`, `T1-colapsed`, `T1Cuenta Full`, `T1envios full`, `T1envios small`, `T1pagos`, **`Variant8`** |
| `Item menu` | `561:8931` | 4 | `Default`, `Select_main`, `Select_sub`, **`Variant4`** |
| `item submenu` | `561:8969` | 3 | `Default`, `Hover`, `Select` |

`Item menu` e `item submenu` viven **fuera** del frame `MENU`, cada uno como frame de primer
nivel — y difieren en la mayúscula inicial.

Las variantes de `Menu` mezclan tres cosas en un solo eje: **producto** (`T1`, `T1pagos`,
`T1envios`, `POS`, `T1Cuenta`), **estado** (`colapsed`) y **tamaño** (`full`, `small`). Y con tres
grafías: `T1-colapsed`, `T1envios full`, `T1Cuenta Full`.

`Select_main` / `Select_sub` son los únicos `snake_case` del archivo.

**Propuesta:** separar en tres propiedades — `producto{t1|t1pagos|t1envios|t1cuenta|pos}` ×
`estado{expandido|colapsado}` × `tamano{full|small}`.

---

# 7. Banderas — 255 instancias, 0 componentes

Frame `Banderas` (`244:10459`).

**Es la familia mejor nombrada del archivo y la única que nadie ha documentado.** 255 entradas,
`flag/{ISO-3166-alpha-2}`: `flag/MX`, `flag/US`, `flag/ZW`. Sin un solo duplicado, sin espacios,
sin acentos, con un estándar internacional detrás.

El problema es otro: **no son componentes de este archivo, son instancias**. Los componentes
viven en otra librería. Consecuencias:

- No se pueden exportar con el pipeline de iconos — `generar-icons.py` resuelve node ids de este archivo.
- No se pueden versionar con el resto del sistema.
- Si esa librería cambia o deja de estar compartida, las 255 se rompen a la vez.

**Antes de homologar hay que averiguar de qué librería vienen y si el equipo la controla.** Es la
única pregunta de este documento que no se puede responder desde el archivo.

---

# 8. Bancos — 82 entradas, 0 componentes

Frame `Banks` (`244:10134`). 77 frames + 5 instancias, y dentro rectángulos con relleno de imagen.

**No son componentes.** No se pueden instanciar, ni publicar en la librería, ni referenciar desde
otro archivo. Hoy la única forma de usar un logo de banco es copiar y pegar el frame.

Y el nombre va en **mayúsculas con espacios**, que no se parece a nada más en el archivo:

```
ABC · ACCIVAL · ACTINVER · AFIRME · AMERICAN EXPRESS · ASEA · AUTOFIN · AZTECA
B&B · BAJIO · BAMSA · BANCOMEXT · BANCOPPEL · BANJERCITO · BANOBRAS · BANREGIO
BANSEFI · BANSI · BARCLAYS · BBASE · BMONEX · BMULTIVA · BULLTICK · CB INTERCAM
CI BOLSA · CIBANCO · CLS · COMPARTAMOS · CONSUBANCO · CREDIT SUISSE · DEUTSCHE
EVERCORE · FAMSA · FINAMEX · FINCOMUN · GBM · HDI · HIPOTECARIA FEDERAL · HSBC
INDEVAL · …
```

`B&B` lleva `&`. `CB INTERCAM`, `AMERICAN EXPRESS`, `HIPOTECARIA FEDERAL` y `CI BOLSA` llevan
espacio.

Los bancos mexicanos tienen **clave de institución de 3 dígitos** asignada por Banxico, que es el
identificador que ya usa cualquier integración de SPEI. **Propuesta:** `logo/banco/{clave}`
(`logo/banco/012` para BBVA) o `logo/banco/{slug}` (`logo/banco/bbva`), y componentizarlos.

Mientras no sean componentes, esta familia no puede entrar en ningún catálogo generado.

---

# 9. Qué hacer con esto

Ordenado por lo que desbloquea, no por esfuerzo.

| # | Acción | Dónde | Alcance | Bloquea a |
|---|---|---|---|---|
| 1 | **Resolver los 9 nombres repetidos** | Figma | 18 nodos | cualquier catálogo generado |
| 2 | **Elegir idioma del sistema** (inglés o español) | equipo de diseño | archivo entero | 3, 6, 7 |
| 3 | Renombrar los 15 mecánicos de §1.1 | Figma | 15 | código y canon |
| 4 | Decidir categoría de los 15 de §1.2 | equipo de diseño | 15 | 3 |
| 5 | **Componentizar `Banks`** | Figma | 82 | que existan en el sistema |
| 6 | **Averiguar de qué librería vienen las banderas** | equipo de diseño | 255 | poder versionarlas |
| 7 | Renombrar `Icon-menu` sin «Nuevo» | Figma | 34 | canon |
| 8 | Unificar sufijos de logos a `logo/{contexto}/{marca}` | Figma | 93 | `BrandLogo` |
| 9 | Unificar los 30 vocabularios de variante a `tono{color\|mono\|inverso}` | Figma | 84 sets | 8 |
| 10 | Resolver los 10 logos duplicados de §3.3 | equipo de diseño | 20 nodos | 8 |
| 11 | Corregir los 4 typos de variante (`Radi`, `Selec`, `Lin`, `7`) | Figma | 4 | — |
| 12 | Nombrar los 5 componentes por defecto (`Component`, `Frame 1000007109`, `icon`×2, `icon-action/`) | Figma | 5 | — |
| 13 | Nombrar las variantes de los 20 sets con `VariantN` | Figma | 20 sets | — |
| 14 | Renombrar `Property 1` en los 126 sets que lo usan | Figma | 126 sets | — |
| 15 | Unificar `Button` + `Button/Split` + `button/ia` + `Social` + `Disclosure` | equipo de diseño | 5 | `ATOMS.md §1` |
| 16 | Decidir si `MOLECULES 5` es sistema o maqueta | equipo de diseño | 1 frame | — |
| 17 | Colocar los 6 componentes sueltos de la raíz | Figma | 6 | — |
| 18 | Dibujar el calado de los 7 iconos como hueco real (`fill-rule="evenodd"`) | Figma | 7 | retirar `--icon-knockout` |
| 19 | Llevar a 24×24 los 27 componentes con marco distinto | Figma | 27 | retirar el `<g transform>` |
| 20 | Arreglar el `#272532` de fondo y los `stroke-width` 1.2 / 2 | Figma | — | exportación manual |

**Solo la 1 bloquea al código de verdad.** El pipeline ya normaliza nombre, lienzo, trazo y color
al generar, pero no puede inventar cuál de dos componentes homónimos es el bueno.

De la 11 a la 14 son mecánicas: no necesitan decisión, solo tiempo en Figma. **La 14 sola toca
126 de 148 sets** y es la que más cambia la experiencia de quien usa la librería, porque hoy el
panel de propiedades dice «Property 1» en el 85 % de los componentes.

## Lo que sigue sin cerrar con el código

`@t1/nexus-react` no tiene catálogo —su `<Icon />` recibe el path SVG crudo— y `t1components`
nombra los archivos por hash. Mientras eso siga así, ningún renombrado en Figma llega solo al
producto: hay que regenerar y publicar.

---

## Alcance de este documento

Cubre los **331 componentes** de la página `Components` (`0:1`), más las 255 instancias de
`Banderas` y las 82 entradas de `Banks`, que se documentan precisamente porque **no** son
componentes.

**No cubre** la página `Cover & documentation` (`232:14855`), que no contiene componentes, ni los
tokens de color, tipografía y espaciado, que tienen su propio cruce en `foundation/`.
