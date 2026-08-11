# METRICS — NEXUS V2.0 Design System

> **Categoría:** components
> **Nivel:** Sistema de visualización de datos (paneles, KPIs y gráficas)
> **Contexto:** Dashboard / Admin — exclusivo. No aplica a landing ni a T1 App.
> **Fuente:** Figma `Componentes-DB` (`0jfN4VM6aaB0JZARFg8JxF`) · section `Componentes` (`79:7231`)
> **Última actualización:** 2026
> **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Grid de paneles](#1-grid-de-paneles)
2. [Panel contenedor](#2-panel-contenedor)
3. [Card Data](#3-card-data)
4. [Gráfica de barras verticales](#4-gráfica-de-barras-verticales)
5. [Gráfica de barras horizontales](#5-gráfica-de-barras-horizontales)
6. [Lista de estatus](#6-lista-de-estatus)
7. [Tabla de cohortes](#7-tabla-de-cohortes)
8. [Dona de distribución](#8-dona-de-distribución)
9. [Estado vacío](#9-estado-vacío)
10. [Tokens de data visualization](#10-tokens-de-data-visualization)
11. [Reglas de implementación](#11-reglas-de-implementación)
12. [Discrepancias detectadas](#12-discrepancias-detectadas)

---

## Convenciones de este archivo

- Todos los colores se referencian por token de `foundation/COLORS.md`. Ningún hex directo.
- Tipografía: **Manrope exclusivamente**. Sora e Inter están prohibidos en dashboard — ver `platforms/DASHBOARD.md`.
- Los componentes de este archivo son de contexto admin. No existe variante landing.
- Las animaciones de conteo (count-up) están **prohibidas** en dashboard. Solo transiciones funcionales.

---

## 1. Grid de paneles

Todas las vistas de métricas se construyen sobre un grid de 12 columnas dentro del área de contenido del dashboard.

### 1.1 Tokens del grid

| Propiedad | Valor |
|---|---|
| Ancho de contenido | `1134px` |
| Columnas | `12` |
| Gutter | `20px` |
| Ancho de columna | `76.17px` (calculado) |
| Gap vertical entre filas | `20px` |

> El ancho de contenido de `1134px` corresponde al área útil con sidebar expandido (`184px`) dentro del max-width de `1600px`. Ver `components/ORGANISMS.md § 1.1`.

### 1.2 Spans permitidos

Un panel solo puede ocupar **3, 4, 6 o 12 columnas**. Cualquier otro span es una desviación.

| Span | Ancho resultante | Uso típico |
|---|---|---|
| `3` | `268.5px` | Card Data (KPI). Cuatro por fila. |
| `4` | `364.7px` | Panel compacto. Tres por fila. |
| `6` | `557px` | Panel medio. Dos por fila. |
| `12` | `1134px` | Panel de ancho completo: mapas, tablas largas. |

**Fórmula:** `ancho = (span × 76.17) + ((span − 1) × 20)`

### 1.3 Reglas del grid

- Una fila nunca mezcla alturas distintas: todos los paneles de una misma fila se estiran a la altura del más alto (`align-items: stretch`).
- Los KPIs siempre van en la primera fila, cuatro paneles de span 3.
- Ningún panel baja de span 3. Por debajo de ese ancho el número deja de ser legible.
- La personalización de paneles (drag, resize, ocultar) **no está definida**. Hasta que se decida, el orden de paneles es fijo por vista.

---

## 2. Panel contenedor

Todo bloque de métricas vive dentro del mismo contenedor. Es el único envoltorio permitido.

### 2.1 Tokens

| Propiedad | Valor | Token |
|---|---|---|
| Background | blanco | `color/base/white` |
| Border radius | `10px` | — |
| Shadow | `0 0 5px 1px rgba(0,0,0,0.1)` | `shadow_card` |
| Padding | `16px` | — |
| Gap interno | `16px` (`24px` si el panel contiene tabla) | — |
| Border | ninguno | — |

### 2.2 Título del panel

| Propiedad | Valor |
|---|---|
| Familia | Manrope Bold |
| Tamaño | `14px` |
| Color | `color/base/black-oxford` |
| Posición | Primer elemento del panel, ancho completo |

### 2.3 Snippet

```tsx
<section className="flex flex-col gap-4 rounded-[10px] bg-white p-4 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
  <h3 className="font-manrope text-[14px] font-bold text-oxford">
    Título del panel
  </h3>
  {/* contenido */}
</section>
```

---

## 3. Card Data

El KPI base del dashboard. Es la **misma card de métrica** documentada en `components/MOLECULES.md § 13.2`, extendida aquí con variantes y estados propios del contexto de reportes.

> **Nota de arquitectura:** la definición completa del componente vive en este archivo. `MOLECULES.md` conserva únicamente un puntero.

### 3.1 Anatomía

```
┌──────────────────────────────────┐
│ Número de envíos                 │  ← Título
│ 312                    [↗ +50%]  │  ← Monto + Chip de comparativa
│ 02 Seleccionados de           ⌄  │  ← Selector (opcional)
└──────────────────────────────────┘
```

| Elemento | Tipografía | Color | Notas |
|---|---|---|---|
| **Título** | Manrope SemiBold `14px` | `color/base/black-oxford` | Una línea, sin truncado |
| **Monto** | Manrope Bold `24px` | `color/base/black-oxford` | Valor principal |
| **Chip comparativa** | Manrope `12px` | según delta | Alto `14px`, ícono `12×12` |
| **Selector** | Manrope `12px` | `color/base/black-oxford` | Chevron `16×16` a la derecha |

### 3.2 Tokens del contenedor

| Propiedad | Valor |
|---|---|
| Border radius | `10px` |
| Padding | `16px 14px` |
| Gap interno | `4px` |
| Border (default) | `1px solid` · `color/brand/gray/200` |
| Border (seleccionada) | `1px solid` · `color/brand/red/200` |

### 3.3 Variantes

| Variante | Descripción |
|---|---|
| **Default** | Título + monto. Sin comparación. |
| **Comparativa** | Añade el chip de delta contra el periodo anterior. |
| **Con selector** | Añade la fila inferior de filtro (`N Seleccionados de`). |
| **Seleccionada** | Border en `red/200`. Marca la métrica activa cuando la card controla una gráfica. |

### 3.4 Estados

| Estado | Comportamiento |
|---|---|
| **Default** | Border `gray/200` |
| **Hover** | Border `red/200` · transición `150ms ease` |
| **Seleccionada** | Border `red/200` persistente |
| **Empty** | Monto en `0`, chip reemplazado por el texto `Sin comparación` |

> **Excepción documentada:** `MOLECULES.md` establece que las cards no tienen hover ni selected salvo el Card Selector. El Card Data es la segunda excepción a esa regla, porque actúa como control de filtro y no como contenedor pasivo.

### 3.5 Chip de comparativa

| Delta | Ícono | Color |
|---|---|---|
| Positivo | `arrow-up-right-01-round` | `color/dataviz/positive` |
| Negativo | `arrow-down-left-01-round` | `color/brand/red/700` |

- Formato: signo + porcentaje con espacio (`+ 50%`, `- 12%`).
- El chip **nunca** aparece si no hay periodo de comparación seleccionado.

---

## 4. Gráfica de barras verticales

Para evolución temporal. Es la gráfica principal del sistema.

### 4.1 Tokens

| Propiedad | Valor |
|---|---|
| Ancho de barra | `24px` |
| Radius de barra | `4px` (solo extremo superior) |
| Color de serie | `color/dataviz/series/1` |
| Degradado de fondo | Vector bajo las barras, mismo tono al 0–20% |
| Gap entre barras | `36px` |
| Altura del área | `184px` |

### 4.2 Ejes

| Elemento | Tipografía | Color |
|---|---|---|
| Escala vertical (valores) | Manrope Medium `10px`, alineada a la derecha | `color/base/black-oxford` |
| Escala horizontal (fechas) | Manrope Medium `10px` | `color/base/black-oxford` |
| Líneas de guía | `1px` horizontal | `color/brand/gray/200` |

- La escala vertical siempre muestra **cinco valores**, incluyendo el `0`.
- Las fechas se abrevian en formato `DD mmm` (`2 jun`).

### 4.3 Hover

Al hover sobre una barra se muestra un tooltip con el valor exacto y la fecha completa. El resto de las barras **no** se atenúa.

---

## 5. Gráfica de barras horizontales

Para distribuciones ordenadas por magnitud (ej. días de entrega promedio).

### 5.1 Tokens

| Propiedad | Valor |
|---|---|
| Alto de barra | `8px` |
| Radius | `2px` (solo extremo derecho) |
| Color de barra | `color/dataviz/series/1` |
| Color de track | `color/dataviz/track` |
| Gap entre filas | `16px` |
| Gap barra–valor | `16px` |

### 5.2 Etiquetas

| Elemento | Tipografía | Color |
|---|---|---|
| Etiqueta de categoría | Manrope Regular `11px` | `color/base/black-oxford` |
| Valor | Manrope Medium `12px`, alineado a la derecha, ancho fijo `39px` | `color/base/black-oxford` |

El track siempre se dibuja completo, incluso cuando el valor es `0`.

---

## 6. Lista de estatus

Desglose vertical de un total por categorías. No es una gráfica: es una tabla de dos columnas sin encabezado.

### 6.1 Tokens

| Propiedad | Valor |
|---|---|
| Padding de fila | `6px 7px` |
| Radius de fila | `2px` |
| Background fila par | `color/dataviz/track` |
| Background fila impar | transparente |
| Etiqueta | Manrope Medium `12px` · `color/base/black-oxford` |
| Valor | Manrope SemiBold `12px`, alineado a la derecha, ancho `32px` |

Las filas alternan fondo empezando por la **segunda** fila.

---

## 7. Tabla de cohortes

Matriz de retención tipo heatmap. Siempre ocupa span completo o span 8.

### 7.1 Estructura

| Zona | Tipografía | Color |
|---|---|---|
| Encabezado | Manrope Bold `12px` | `color/brand/gray/600` |
| Alto de encabezado | `41px` | — |
| Columna de etiqueta | Manrope Medium `12px` | `color/base/black-oxford` |
| Celda de dato | Manrope Medium `12px`, centrada | `color/base/black-oxford` |
| Padding vertical de celda | `12px` | — |

### 7.2 Escala de intensidad

| Valor | Background | Color de texto |
|---|---|---|
| Sin dato (fuera de rango) | `color/base/white` | — |
| `0%` | `color/dataviz/track` | `color/base/black-oxford` |
| Con valor | `color/brand/red/300` | `color/base/white` |

> **Pendiente:** la escala actual solo tiene dos niveles (con valor / sin valor). Una matriz de retención real necesita al menos cuatro pasos de intensidad. Definir antes de implementar.

---

## 8. Dona de distribución

Para composición de un total en categorías (ej. tipos de incidencia).

### 8.1 Tokens

| Propiedad | Valor |
|---|---|
| Diámetro | `134px` (versión estándar) · `100px` (versión compacta) |
| Valor central | Manrope Bold `24px` · `color/base/black-oxford` |
| Etiqueta central | Manrope `12px` · `color/base/black-oxford` |

### 8.2 Asignación de colores

Los segmentos se asignan **en orden**, empezando siempre por el estado positivo.

| Orden | Token | Uso |
|---|---|---|
| 1 | `color/dataviz/positive` | Estado sano / sin incidencia |
| 2 | `color/dataviz/series/2` | Primera categoría |
| 3 | `color/dataviz/series/3` | Segunda categoría |
| 4 | `color/dataviz/series/4` | Tercera categoría |
| 5 | `color/dataviz/series/5` | Cuarta categoría |

### 8.3 Leyenda

La leyenda va a la derecha de la dona, con gap `32px`. Cada fila: indicador de color + etiqueta + valor alineado a la derecha, altura `16px`, gap vertical `24px`.

- Una dona nunca lleva más de **cinco segmentos**. Con más categorías, agrupar en "Otros".

---

## 9. Estado vacío

Cuando no hay datos en el periodo consultado, la vista **conserva su estructura completa**. No se reemplaza por una ilustración.

| Elemento | Comportamiento en vacío |
|---|---|
| Card Data — monto | `0` |
| Card Data — chip | Texto `Sin comparación`, sin ícono ni color |
| Gráfica de barras | Ejes y guías visibles, sin barras |
| Barras horizontales | Track visible al 100%, valor `0` |
| Lista de estatus | Todas las filas con valor `0` |
| Tabla de cohortes | Celdas en `0%` con background `track` |
| Dona | Círculo completo en `color/brand/gray/200` |

**Razón:** mantener el esqueleto comunica que la consulta funcionó y no arrojó resultados, en vez de sugerir un error de carga. Esto difiere del patrón general de `patterns/EMPTY-STATES.md`, que sí usa ilustración + CTA — ese patrón aplica a vistas sin configurar, no a periodos sin datos.

---

## 10. Tokens de data visualization

Bloque a agregar en `foundation/COLORS.md`.

| Token | Referencia | Hex | Uso |
|---|---|---|---|
| `color/dataviz/series/1` | `red/400` | `#E26153` | Serie principal: barras, líneas de tendencia |
| `color/dataviz/series/2` | `blue/500` | `#2180FF` | Segunda categoría |
| `color/dataviz/series/3` | `yellow/500` | `#EDBD55` | Tercera categoría |
| `color/dataviz/series/4` | — | `#4F6EE0` | Cuarta categoría |
| `color/dataviz/series/5` | `red/200` | `#F1B0A9` | Quinta categoría |
| `color/dataviz/positive` | `green/500` | `#4FC153` | Estado sano, deltas al alza |
| `color/dataviz/negative` | `red/700` | `#CC0000` | Deltas a la baja |
| `color/dataviz/track` | `gray/50` | `#F8F8F8` | Base de barra, celda sin valor, fila alterna |
| `color/dataviz/accent` | `red/200` | `#F1B0A9` | Border de Card Data seleccionada / hover |

### 10.1 Excepción semántica

Estos tokens **rompen deliberadamente** la regla de `COLORS.md` que prohíbe usar colores semánticos como decoración.

En data visualization, el amarillo **no significa** precaución y el azul **no significa** información: son categorías sin carga semántica. La única excepción dentro de la excepción es `positive` / `negative`, donde el verde y el rojo sí conservan su significado.

Fuera de gráficas, la regla original sigue vigente sin cambios.

### 10.2 `series/4` — token sin escala base

`#4F6EE0` es el único token de la paleta que **no referencia un color de la escala de marca**. Es un azul violáceo exclusivo de data visualization. No debe usarse en ningún otro contexto ni agregarse a la escala Blue.

### 10.3 Advertencia de accesibilidad

`series/1` (`#E26153`) y `series/5` (`#F1B0A9`) son ambos rojos. En segmentos pequeños de dona la diferencia se reduce a luminosidad, y bajo deuteranopia son difíciles de separar.

**Mitigación obligatoria:** toda dona y toda gráfica multiserie debe llevar leyenda con etiqueta de texto. El color nunca es el único canal de información. Ver `accessibility/A11Y.md`.

---

## 11. Reglas de implementación

- **Manrope siempre.** Sora e Inter no existen en dashboard.
- **Rojo en data-viz es color de serie, no error.** Es la única zona del dashboard donde el rojo no significa error ni CTA. Esta excepción se limita a gráficas; fuera de un panel de métricas, el rojo mantiene su significado original.
- **Sin count-up.** Los números aparecen en su valor final. Las animaciones de conteo son exclusivas de landing.
- **Transiciones funcionales.** Solo hover (`150ms ease`) y carga. Nada decorativo.
- **Skeleton durante carga**, nunca spinner: el panel conserva su altura y evita el salto de layout.
- **Un panel, una métrica.** No apilar dos gráficas sin relación en el mismo contenedor.
- **Ningún hex directo.** Todo color entra por token de `foundation/COLORS.md`.
- **Máximo cinco series por gráfica.** La paleta no tiene un sexto color y no debe inventarse.

---

## 12. Discrepancias detectadas

Hallazgos del archivo `Componentes-DB` contra NEXUS. Categorías: **(a)** error de implementación · **(b)** Figma contradice el MD · **(c)** no documentado.

| # | Hallazgo | Ubicación | Cat. | Resolución |
|---|---|---|---|---|
| 1 | Escala de variables desplazada: `red-400`=`#F1B0A9`, `red-600`=`#E9897E`, `red-800`=`#E26153`, `gray-100`=`#F8F8F8`, `gray-400`=`#E7E7E7` | Todo el archivo | (b) | Manda `COLORS.md`. Corregir nombres en Figma. |
| 2 | Namespace `color/neutral/` en vez de `color/brand/` | Grises | (b) | Manda `COLORS.md`. |
| 3 | Radius de panel `12px` | Todos los paneles | (a) | Corregir a `10px`. |
| 4 | `#828282` hardcodeado en encabezado de tabla | Cohortes | (a) | → `gray/600` (`#9CA3AF`). **Cambia visualmente.** |
| 5 | `#111827` hardcodeado en título de panel | Cohortes | (a) | → `oxford` (`#4C4C4C`). **Cambia visualmente.** |
| 6 | `#4A4A4A` hardcodeado en celdas | Cohortes | (a) | → `oxford` (`#4C4C4C`). |
| 7 | `#F3F4F6` hardcodeado en track de barra | Días de entrega | (a) | → `gray/50` (`#F8F8F8`). |
| 8 | Cinco segmentos de dona nombrados `Rojo`, `Verde 02–05`; ninguno corresponde a su nombre | `68:4817`–`68:4821` | (a) | Renombrar por categoría, no por color. |
| 9 | Panel de Cohortes con span 8 (`744px`), fuera de los spans permitidos | Cohortes | (b) | Redimensionar a span 6, o admitir span 8 en el grid. |
| 10 | Sidebar `241px` / header `60px` | Todos los frames | (a) | Valores vigentes: `184px` / `48px` (`ORGANISMS.md`). |
| 11 | Título de panel con tamaños inconsistentes (`12px`, `14px`, `16px`) | Varios | (a) | Unificar en `14px` Bold. |
| 12 | `#FE4D61` usado sólido como color de serie | Dona | (b) | Descartado. En `COLORS.md` es `color/overlay/red`, solo para 10% de opacidad. |
| 13 | Escala de cohortes con solo dos niveles de intensidad | Cohortes | (c) | Definir escala de cuatro pasos. |
| 14 | Personalización de paneles no definida | Sistema | (c) | Decidir antes de implementar. |
| 15 | Librería de charting sin confirmar | Sistema | (c) | Pendiente de Franco / Mario. |

---

## Referencias cruzadas

| Archivo | Relación |
|---|---|
| `foundation/COLORS.md` | Tokens base y bloque de data visualization |
| `foundation/TYPOGRAPHY.md` | Escala Manrope |
| `foundation/ELEVATION.md` | `shadow_card` |
| `components/MOLECULES.md` | Card Data — puntero a este archivo |
| `components/ORGANISMS.md` | Layout del dashboard, sidebar y header |
| `components/TABLES.md` | Tablas de datos generales — la de cohortes vive aquí |
| `patterns/DASHBOARD-LAYOUTS.md` | Composición de vistas |
| `patterns/EMPTY-STATES.md` | Patrón general de vacío — este archivo documenta la excepción |
| `platforms/DASHBOARD.md` | Reglas de plataforma |
| `accessibility/A11Y.md` | Contraste y canales redundantes |

---

## Notas para Claude

- Este archivo es la **fuente única** del Card Data. No tomar su definición de `MOLECULES.md`.
- Nunca asignar un color de serie fuera del orden establecido en § 8.2.
- El rojo dentro de un panel de métricas es color de serie. Fuera del panel, sigue significando error o CTA primario.
- Ante cualquier duda de valor, Figma manda sobre este archivo — salvo en los puntos listados en § 12, ya resueltos a favor de NEXUS.
- Las secciones marcadas como pendientes (§ 7.2, § 11 charting) no deben completarse por inferencia.
