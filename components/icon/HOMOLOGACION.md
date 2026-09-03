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

Los conteos del canon están desactualizados. El total real es **197**, no 153.

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

`components/icon/icons.ts` está generado y validado, hoy con **5 de 197 iconos**. Para completarlo
no hace falta repetir el trabajo a mano: el script **`generar-icons.py`** lo hace de una pasada.

### Uso

```bash
export FIGMA_TOKEN=figd_xxxxxxxxxxxxxxxx
cd components/icon
python3 generar-icons.py                 # los 163 con nodeId conocido
python3 generar-icons.py --solo math     # solo una categoría
python3 generar-icons.py --dry-run       # lista sin descargar nada
```

**El token** se saca en Figma → avatar → *Settings* → *Security* → *Personal access tokens* →
*Generate new token*, con permiso de lectura de contenido. Es personal: no se sube al repo.

### Qué hace

1. Lee `figma-nodes.tsv` — el mapa `nombre en Figma → node_id`, ya inventariado:
   **126 iconos** del frame `Icons` y **37** de `Icon-menu`.
2. Pide los SVG a la API de Figma en lotes de 40, con pausa entre peticiones.
3. Limpia cada uno: retira el rect del artboard y los fondos sin `id`.
4. Normaliza al canon: `currentColor` y `stroke-width` 1.5.
5. Escribe `icons.ts` en el formato de `ICON-COMPONENT.md §3.1`.
6. Avisa si algo quedó sucio y lista los iconos que no pudo descargar.

Al escribir la clave elimina el prefijo (`icon/math/at` → `math/at`,
`icon-info/abacus` → `info/abacus`), con lo que **los 15 renombrados mecánicos de la sección 1
quedan resueltos automáticamente**. Los 15 de la sección 2 salen con su nombre tal cual, y ahí sí
hace falta la decisión de diseño.

### Lo que el script no cubre

Los **34 iconos sin nodeId identificable** (160 − 126). Están anidados de forma que el volcado de
metadatos no los expone como nodo propio; hay que localizarlos a mano en Figma y añadirlos a
`figma-nodes.tsv`.

---

## 4. Qué hacer con esto

| # | Acción | Dónde | Bloquea a |
|---|---|---|---|
| 1 | Renombrar los 15 mecánicos | Figma | código y canon |
| 2 | Decidir categoría de los 15 restantes | equipo de diseño | 1 |
| 3 | Retirar `icon-action/`, `minus 1`, `plus 1` | Figma | — |
| 4 | Actualizar los conteos de §4 a 160 + 37 | canon | — |
| 5 | Añadir `t1pagos` y `clipboard` a las categorías de §4 | canon | — |
| 6 | Resolver si `USER` y `MISC` existen | equipo de diseño | 5 |
| 7 | Regenerar `icons.ts` con los nombres homologados | código | 1, 2 |

El paso 7 es el que cierra el círculo con el código: hoy `@t1/nexus-react` no tiene catálogo
—su `<Icon />` recibe el path SVG crudo— y `t1components` nombra los archivos por hash.

---

## Alcance de este documento

Cubre los **197 iconos** de los frames `Icons` e `Icon-menu`. **No cubre** las 256 entradas del
frame `Banderas` ni las 83 de `Banks`, que son catálogos aparte y necesitan su propio cruce.
