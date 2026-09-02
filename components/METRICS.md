# METRICS — NEXUS V2.0 Design System

> **Categoría:** components
> **Nivel:** Sistema de visualización de datos (paneles, KPIs y gráficas)
> **Contexto:** Dashboard / Admin — exclusivo. No aplica a landing ni a T1 App.
> **Fuentes:**
> · Sistema — Figma `Componentes-DB` (`0jfN4VM6aaB0JZARFg8JxF`) · section `Componentes` (`79:7231`)
> · Implementación — Figma `T1 Envíos 2026` (`DILjiDu55I7arqzmLmeXxS`) · módulo Reportes, aprobado y en producción
> **Última actualización:** Septiembre 2026
> **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Grid de paneles](#1-grid-de-paneles)
2. [Panel contenedor](#2-panel-contenedor)
3. [Card Data](#3-card-data)
4. [Gráfica de línea — evolución temporal](#4-gráfica-de-línea--evolución-temporal)
5. [Gráfica de barras verticales](#5-gráfica-de-barras-verticales)
6. [Gráfica de barras horizontales](#6-gráfica-de-barras-horizontales)
7. [Lista de estatus](#7-lista-de-estatus)
8. [Dona de distribución](#8-dona-de-distribución)
9. [Mapa de calor geográfico](#9-mapa-de-calor-geográfico)
10. [Línea de tiempo de estatus](#10-línea-de-tiempo-de-estatus)
11. [Panel de acción requerida](#11-panel-de-acción-requerida)
12. [Tabla de cohortes](#12-tabla-de-cohortes)
13. [Elementos compartidos](#13-elementos-compartidos)
14. [Comportamiento responsive](#14-comportamiento-responsive)
15. [Estados](#15-estados)
16. [Tokens de data visualization](#16-tokens-de-data-visualization)
17. [Reglas de implementación](#17-reglas-de-implementación)
18. [Cobertura de implementación](#18-cobertura-de-implementación)
19. [Discrepancias detectadas](#19-discrepancias-detectadas)

---

## Convenciones de este archivo

- Todos los colores se referencian por token de `foundation/COLORS.md`. Ningún hex directo.
- Tipografía: **Manrope exclusivamente**. Sora e Inter están prohibidos en dashboard — ver `plataform/DASHBOARD.md`.
- Los componentes de este archivo son de contexto admin. No existe variante landing.
- Las animaciones de conteo (count-up) están **prohibidas** en dashboard. Solo transiciones funcionales.
- Cada sección de gráfica tiene dos bloques: **Tokens** (lo que manda el sistema) e **Implementación** (las medidas reales del Figma aprobado). Cuando difieren, la diferencia está en § 19 y **manda el bloque de Tokens** salvo que § 19 diga lo contrario.
- Los tamaños tipográficos marcados **(der.)** están derivados de la caja de línea (`line-height 1.366em` de Manrope), no leídos de un estilo de texto.
- Las medidas fraccionarias (`210.8`, `36.71`, `179.74`) son reales, no errores de captura: vienen de repartos automáticos. Al implementar, usar la fórmula de reparto, no el número redondeado.

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

**Fórmula:** `ancho = (span × 76.17) + ((span − 1) × 20)`

> ⚠️ **El ancho de `1134px` está atado al sidebar de `241px` del Figma, no al sidebar canónico de `184px`.**
> `1134` sale de `1440 − 250 (sidebar del Figma) − 28 × 2 (padding)`. Con el sidebar vigente de `184px` y padding de `24px` (`components/ORGANISMS.md § 1.1`), el ancho útil sería `1208px` y la columna `82.33px`, lo que recalcula **todos** los spans. Ver § 19-01: es la decisión que bloquea el resto del grid.

### 1.2 Spans permitidos

Un panel solo puede ocupar **3, 4, 6 o 12 columnas**. Cualquier otro span es una desviación.

| Span | Ancho resultante | Uso típico |
|---|---|---|
| `3` | `268.5px` | Card Data (KPI). Cuatro por fila. |
| `4` | `364.7px` | Panel compacto. Tres por fila. |
| `6` | `557px` | Panel medio. Dos por fila. |
| `12` | `1134px` | Panel de ancho completo: mapas, tablas largas, líneas de tiempo. |

### 1.3 Partición de KPIs

La fila de KPIs es la única excepción al grid de 12 columnas. Se reparte el ancho útil en partes iguales:

`ancho de card = (1134 − (n − 1) × 20) ÷ n`

| n | Ancho de card | Estado |
|---|---|---|
| `4` | `268.5px` | Coincide con span 3. **Canónico.** |
| `5` | `210.8px` | En producción en T1envíos › Reportes › General. **Pendiente de decisión** — ver § 19-02 |

Por debajo de `210px` el número deja de ser legible: **`5` es el máximo**. Con más de cinco métricas, la sexta baja a una segunda fila o se convierte en gráfica.

### 1.4 Reglas del grid

- Una fila nunca mezcla alturas distintas: todos los paneles de una misma fila se estiran a la altura del más alto (`align-items: stretch`).
- Los KPIs siempre van en la primera fila.
- Ningún panel de gráfica baja de span 6. Por debajo de ese ancho el eje X deja de ser legible.
- La suma de los paneles de una fila más sus gutters es **exactamente** el ancho de contenido. Ninguna fila desborda.
- La personalización de paneles (drag, resize, ocultar) **no está definida**. Hasta que se decida, el orden de paneles es fijo por vista.

### 1.5 Grid en mobile

| Propiedad | Valor |
|---|---|
| Ancho del frame | `360px` |
| Margen lateral | `16px` |
| Ancho útil de contenido | `328px` |
| Ancho útil dentro del panel | `296px` |
| Gap vertical entre paneles | `20px` |
| Columnas | `1` — excepto la fila de KPIs y la línea de tiempo |

No existe breakpoint de tablet definido para métricas. El sistema salta de `1440` a `360`.

---

## 2. Panel contenedor

Todo bloque de métricas vive dentro del mismo contenedor. Es el único envoltorio permitido.

### 2.1 Tokens

| Propiedad | Valor | Token |
|---|---|---|
| Background | blanco | `color/brand/base/white` |
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
| Color | `color/brand/base/oxford` |
| Posición | Primer elemento del panel · `x: 16` · `y: 16` |

> En producción el título es **`16px` SemiBold** en los seis frames de T1envíos. Es la desviación más extendida del archivo. Ver § 19-03.

### 2.3 Descripción del panel (opcional)

Segunda línea bajo el título, a `31px` de su origen.

| Propiedad | Valor |
|---|---|
| Tamaño | `12px` |
| Peso | Regular 400 |
| Color | `color/brand/base/oxford` |

Se usa cuando el panel necesita explicar cómo se lee o cómo se interactúa con él: *"Zonas de calor por volumen de envíos del periodo. Pasa el cursor sobre un estado."*

### 2.4 Snippet

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

El KPI base del dashboard. Es la **misma card de métrica** referida en `components/MOLECULES.md`, extendida aquí con variantes y estados propios del contexto de reportes.

> **Nota de arquitectura:** la definición completa del componente vive en este archivo. `MOLECULES.md` debe conservar únicamente un puntero — actualmente no lo tiene. Ver § 19-04.

### 3.1 Anatomía — variante bloque

```
┌──────────────────────────────────┐
│ Número de envíos                 │  ← Título
│ 2,799                 [↘ −11.7%] │  ← Monto + Chip de comparativa
│ 02 Seleccionados de           ⌄  │  ← Selector (opcional)
└──────────────────────────────────┘
```

| Elemento | Tipografía | Color | Notas |
|---|---|---|---|
| **Título** | Manrope SemiBold `14px` | `color/brand/base/oxford` | Una línea, sin truncado |
| **Monto** | Manrope Bold `24px` | `color/brand/base/oxford` | Valor principal |
| **Chip comparativa** | Manrope `12px` | según delta | Alto `14px`, ícono `12×12` |
| **Selector** | Manrope `12px` | `color/brand/base/oxford` | Chevron `16×16` a la derecha |

### 3.2 Tokens del contenedor

| Propiedad | Valor |
|---|---|
| Border radius | `10px` |
| Padding | `16px 14px` |
| Gap interno | `4px` |
| Border (default) | `1px solid` · `color/brand/gray/200` |
| Border (seleccionada) | `1px solid` · `color/brand/red/200` |

### 3.3 Anatomía — variante inline

Usada cuando el KPI encabeza una gráfica en lugar de vivir en su propia card. **Sin contenedor, sin borde, sin chip.**

```
2.8%   En relación al total
```

| Elemento | Valor |
|---|---|
| Monto | Manrope Bold `24px` · caja `26px` |
| Leyenda | Manrope Regular `12px` · caja `14px` · alineada al baseline inferior |
| Gap monto → leyenda | `10px` |
| Alto del bloque | `26px` |

La leyenda es **texto fijo** y no cambia de color. No es el chip de comparativa de § 3.6.

Se usa en toda gráfica cuyo dato principal es una tasa: `Incidencias por periodo`, `Incidencias`, `Retornos`.

### 3.4 Implementación

| Propiedad | Desktop | Mobile — hero | Mobile — par |
|---|---|---|---|
| Ancho | `210.8px` (5 por fila) | `328px` | `156px` / `162px` |
| Alto | `96px` | `96px` | `93px` |
| Padding lateral | `14px` | `14px` | `14px` |
| Padding superior | `16px` | `16px` | `16px` |
| Título — caja | `19px` | `19px` | `16px` |
| Monto — caja | `33px` | `33px` | `33px` |
| Gap título → monto | `12px` | `12px` | `12px` |

Fila aprobada en T1envíos › Reportes › General, en este orden:

`Número de envíos` · `Entregas a tiempo` · `Costo promedio` · `Tasa de incidencia` · `Envíos con sobrepeso`

En mobile el primer KPI ocupa el ancho completo y los cuatro restantes se reparten en dos filas de dos.

### 3.5 Variantes y estados

| Variante | Descripción |
|---|---|
| **Default** | Título + monto. Sin comparación. |
| **Comparativa** | Añade el chip de delta contra el periodo anterior. |
| **Con selector** | Añade la fila inferior de filtro (`N Seleccionados de`). |
| **Seleccionada** | Border en `red/200`. Marca la métrica activa cuando la card controla una gráfica. |
| **Inline** | Sin contenedor. Encabeza una gráfica. Ver § 3.3. |

| Estado | Comportamiento |
|---|---|
| **Default** | Border `gray/200` |
| **Hover** | Border `red/200` · transición `150ms ease` |
| **Seleccionada** | Border `red/200` persistente |
| **Empty** | Monto en `0`, chip reemplazado por el texto `Sin comparación` |

> **Excepción documentada:** `MOLECULES.md` establece que las cards no tienen hover ni selected salvo el Card Selector. El Card Data es la segunda excepción a esa regla, porque actúa como control de filtro y no como contenedor pasivo.

### 3.6 Chip de comparativa

| Delta | Ícono | Color |
|---|---|---|
| Positivo | `arrow-up-right-01-round` | `color/dataviz/positive` |
| Negativo | `arrow-down-left-01-round` | `color/brand/red/700` |

| Propiedad | Valor |
|---|---|
| Tamaño | `39 × 14px` |
| Ícono | `12 × 12px` |
| Formato | signo + espacio + porcentaje (`+ 4.2%`, `− 11.7%`) |

- El chip **nunca** aparece si no hay periodo de comparación seleccionado.
- El mismo chip se usa **sin ícono** para comunicar participación en § 6, § 7 y § 11. En ese uso no lleva color de delta.

---

## 4. Gráfica de línea — evolución temporal

**La gráfica principal del sistema.** Compara el periodo seleccionado contra el periodo anterior a lo largo del tiempo.

> Reclasificación: hasta la versión 2.4.0 este rol lo tenía la gráfica de barras verticales (§ 5). En producción la evolución temporal se resuelve con línea; las barras verticales quedaron para distribución por bucket. Ver § 19-05.

### 4.1 Anatomía

```
Evolución por semana
860  [↗ +4.2%]
                                    ┌───────────────────┐
 1,012 ┼───────────────────────────  │ Semana 2          │
       │      ╱╲                     │ ● 9 jun  1,002 35%│
   752 ┼─────╱──╲───────────────────  │ ● 9 may    802 22%│
       │   ╱      ╲   ·······        └───────────────────┘
   501 ┼──────────────────╲──────────────
       │ ·····              ╲
   251 ┼───────────────────────╲─────────
       │                         ╲
     0 ┼──────────────────────────╲──────
       2 jun   9 jun   16 jun   23 jun   30 jun

            ● Envíos   ● Periodo anterior
```

### 4.2 Tokens

| Propiedad | Valor |
|---|---|
| Alto del plot | `185px` — **constante en todos los anchos** |
| Columna de eje Y | `26px` |
| Offset eje Y → plot | `42px` |
| Líneas guía | `5` horizontales · `1px` · `color/brand/gray/200` · **equidistantes** |
| Valores del eje Y | `5`, incluyendo el `0`, alineados a la derecha |
| Tipografía de ejes | Manrope Medium `10px` |
| Formato de fecha en eje X | `D mmm` (`2 jun`) · sin año |
| Etiquetas de eje X | `5` |
| Gap plot → fechas | `8px` |
| Gap fechas → leyenda | `8px` |

### 4.3 Series

Solo **dos series**. La gráfica no admite una tercera.

| Serie | Trazo | Token |
|---|---|---|
| Periodo actual | Sólido, curva suavizada | `color/dataviz/series/1` |
| Periodo anterior | Punteado, curva suavizada | `color/dataviz/series/5` |
| Degradado | Bajo la serie actual, mismo tono a transparente | `color/dataviz/series/1` |

- La serie anterior **nunca** lleva degradado.
- Ambas curvas se dibujan suavizadas (spline), no en segmentos rectos.
- El trazo punteado es el canal redundante que exige § 16.3: ambas series son rojas.

### 4.4 Hover

| Elemento | Valor |
|---|---|
| Línea vertical guía | `1px` · alto del plot completo (`184px`) · `color/brand/gray/200` |
| Marcador serie actual | Círculo `5 × 5px` · `color/dataviz/series/1` |
| Marcador serie anterior | Círculo `5 × 5px` · `color/dataviz/series/5` |
| Tooltip | § 13.1 |

El resto de la curva **no** se atenúa.

### 4.5 Implementación

| Elemento | Span 6 | Span 12 | Mobile |
|---|---|---|---|
| Ancho de panel | `555.5px` | `1134px` | `328px` |
| Alto de panel | `396px` | `385px` | `369px` |
| Área de gráfica | `523.5px` | `1102px` | `296px` |
| Ancho del plot | `482.5px` | `1060px` | `254px` |
| Alto del plot | `185px` | `185px` | `185px` |

En producción: `Evolución por semana` (General, span 6) y `Incidencias por periodo` (Incidencias y retornos, span 12).

---

## 5. Gráfica de barras verticales

Para distribución de un total entre buckets ordenados, con la distribución del periodo anterior superpuesta.

No es para evolución temporal — para eso está § 4.

### 5.1 Anatomía

```
Días de entregas promedio
100% ┼──────────────────────────────────────
     │        █
 75% ┼───█────█─────────────────────────────
     │   █    █    █     ····
 50% ┼───█────█────█──█─····────────────────
     │·······  ····   ·      ····
 25% ┼───█────█────█──█───█───█───█─────────
   0 ┼───█────█────█──█───█───█───█─────────
      1Día 2Días 3Días 4Días 5Días 6Días +7Días

            ● Envíos   ● Periodo anterior
```

### 5.2 Tokens

| Propiedad | Valor |
|---|---|
| Ancho de barra | `24px` |
| Radius de barra | `4px` — solo extremo superior |
| Color de serie | `color/dataviz/series/1` |
| Origen | Todas las barras anclan al `0` del eje |
| Gap entre barras | Calculado — ver § 5.3 |
| Alto del plot | `224px` |
| Escala del eje Y | `0` · `25%` · `50%` · `75%` · `100%` — porcentaje, no valor absoluto |
| Líneas guía | `5` horizontales · `1px` · `color/brand/gray/200` · equidistantes |
| Tipografía de ejes | Manrope Medium `10px` |

### 5.3 Reparto de barras

El gap **no es un valor fijo**: las barras se reparten el ancho de la zona de trazado.

`paso = ancho de zona ÷ n` · `gap = paso − 24`

| n | Zona `452px` | Paso | Gap |
|---|---|---|---|
| `7` | `452px` | `71.3px` | `47.3px` |

Si el gap resultante baja de `16px`, la gráfica tiene demasiadas categorías: agrupar en `Otros` o cambiar a barras horizontales (§ 6).

### 5.4 Serie de comparación

| Propiedad | Valor |
|---|---|
| Trazo | Punteado, curva suavizada, **por encima** de las barras |
| Token | `color/dataviz/series/5` |
| Degradado | Sí, bajo la curva punteada |

Cuando la línea cruza una barra, la barra queda visible por debajo. No hay recorte ni opacidad.

### 5.5 Hover

Idéntico a § 4.4, con el tooltip de § 13.1. El encabezado del tooltip es el bucket (`2 Días`), no la fecha.

### 5.6 Implementación

| Elemento | Desktop (span 6) | Mobile |
|---|---|---|
| Ancho de panel | `555.5px` | `328px` |
| Alto de panel | `381px` | `354px` |
| Área de gráfica | `523.5px` | `296px` |
| Ancho del plot | `481.5px` | `254px` |
| Alto del plot | `224px` | `231px` |
| Zona de barras | `452px` | — |
| Barras | `7` (1–6 días y +7 días) | `7` |

En producción: `Días de entregas promedio` (General).

---

## 6. Gráfica de barras horizontales

Para distribuciones ordenadas por magnitud con etiqueta larga: causas, categorías, motivos.

### 6.1 Anatomía — desktop

```
Incidencias
Consulta los envíos con incidencias y sus principales causas.
2.8%  En relación al total

Cambio de dirección    ▬▬▬▬▬▬▬▬▬▬▬░░░░░░░   37   [46%]
Paquete rechazado      ▬▬▬▬▬▬▬░░░░░░░░░░░   18   [23%]
Destinatario no local. ▬▬▬▬░░░░░░░░░░░░░░    8   [10%]
Cancelación de guía    ▬▬░░░░░░░░░░░░░░░░    5    [6%]
Reenvío a mensajería   ▬▬░░░░░░░░░░░░░░░░    5    [6%]
Demora                 ▬▬░░░░░░░░░░░░░░░░    5    [6%]
Perdido / Destruido    ▬░░░░░░░░░░░░░░░░░    2    [3%]
```

### 6.2 Tokens

| Propiedad | Valor |
|---|---|
| Alto de barra | `8px` |
| Radius | `2px` — solo extremo derecho |
| Color de barra | `color/dataviz/series/1` |
| Color de track | `color/dataviz/track` |
| Alto de fila | `16px` |
| Gap entre filas | `8px` (paso `24px`) |
| Gap etiqueta → track | `16px` |
| Gap track → valor | `16px` |
| Etiqueta de categoría | Manrope Regular `12px` · `color/brand/base/oxford` |
| Valor | Manrope Medium `12px`, alineado a la derecha, ancho fijo `39px` |
| Chip de participación | `39 × 14px`, sin ícono |

### 6.3 Estructura de fila — desktop

| Columna | Ancho | X |
|---|---|---|
| Etiqueta | `150px` | `0` |
| Gráfico (track + barra) | `250px` | `166` |
| Información (valor + chip) | `91px` | `432` |

### 6.4 Estructura de fila — mobile

La fila se parte en dos líneas: etiqueta arriba, barra y valor abajo.

```
Cambio de dirección
▬▬▬▬▬▬▬▬▬░░░░░░░░░░       37   [46%]
```

| Propiedad | Valor |
|---|---|
| Alto de fila | `36px` (paso `44px`, gap `8px`) |
| Línea 1 — etiqueta | `y: 0` · caja `16px` |
| Línea 2 — barra + valor | `y: 20` · caja `16px` |
| Ancho del track | `189px` |
| Columna de información | `91px` · `x: 205` |

### 6.5 Reglas

- El **track siempre se dibuja completo**, incluso cuando el valor es `0`.
- El ancho de la barra es proporcional **al valor máximo de la serie**, no al total. La primera fila siempre llena el track.
- Las filas se ordenan de mayor a menor. Nunca alfabéticamente.
- Máximo **7 filas**. Sin paginación ni scroll interno: con más categorías, agrupar en `Otros`.

### 6.6 Implementación

| Panel | Ancho | Alto | Filas |
|---|---|---|---|
| Incidencias | `555px` | `305px` | `7` |
| Retornos | `555px` | `281px` | `5` |

En producción: `Incidencias` y `Retornos` (Incidencias y retornos, span 6 cada uno).

---

## 7. Lista de estatus

Desglose vertical de un total por categorías. No es una gráfica: es una tabla de dos columnas sin encabezado, con navegación.

### 7.1 Anatomía

```
Estado de envíos

 Guía generada                 78   [2.8%]
 Por recolectar                 0     [0%]   ← fondo alterno
 Recolectado                    0     [0%]
 En camino                     77   [2.8%]   ← fondo alterno
 Entregado                  2,607  [93.1%]
 Retornado                     32   [1.1%]   ← fondo alterno
 Cancelado                      5   [0.2%]
```

### 7.2 Tokens

| Propiedad | Valor |
|---|---|
| Padding de fila | `6px 7px` |
| Alto de fila | `36.7px` |
| Radius de fila | `2px` |
| Background fila par | `color/dataviz/track` |
| Background fila impar | transparente |
| Etiqueta | Manrope Medium `12px` · `color/brand/base/oxford` · **subrayada** |
| Valor | Manrope SemiBold `12px`, alineado a la derecha, ancho `32px` |
| Chip de participación | `39 × 14px`, sin ícono, a `48px` del inicio de la columna de información |
| Columna de información | `87px` |

Las filas alternan fondo empezando por la **segunda**.

### 7.3 Navegación

**Las etiquetas están subrayadas porque son navegables.** Cada estatus lleva al listado de envíos filtrado por ese estatus. El subrayado es el único indicador de afordancia: no hay ícono ni chevron.

Esto es comportamiento nuevo en 2.5.0. Hasta 2.4.0 la lista era de solo lectura.

### 7.4 Orden

El orden refleja el ciclo de vida de la entidad y **no se reordena por valor**:

`Guía generada` → `Por recolectar` → `Recolectado` → `En camino` → `Entregado` → `Retornado` → `Cancelado`

### 7.5 Implementación

| Propiedad | Desktop | Mobile |
|---|---|---|
| Ancho de panel | `558.5px` | `328px` |
| Alto de panel | `396px` | `328px` |
| Contenedor de filas | `526.5 × 257px` | `296 × 257px` |
| Columna de etiqueta | `425.5px` | `195px` |
| Columna de información | `87px` · `x: 432.5` | `87px` · `x: 202` |

En producción: `Estado de envíos` (General, span 6).

---

## 8. Dona de distribución

Para composición de un total en categorías.

### 8.1 Tokens

| Propiedad | Valor |
|---|---|
| Diámetro | `180px` (L) · `134px` (estándar) · `100px` (compacta) |
| Valor central | Manrope Bold `24px` · `color/brand/base/oxford` |
| Etiqueta central | Manrope `12px` · `color/brand/base/oxford` |

| Tamaño | Cuándo |
|---|---|
| `180px` | Panel span 6 con leyenda a la derecha |
| `134px` | Mobile, o panel span 4 |
| `100px` | Dentro de una card, sin panel propio |

### 8.2 Asignación de colores

Los segmentos se asignan **en orden**, empezando siempre por el estado positivo.

| Orden | Token | Uso |
|---|---|---|
| 1 | `color/dataviz/positive` | Estado sano / sin incidencia |
| 2 | `color/dataviz/series/1` | Primera categoría |
| 3 | `color/dataviz/series/2` | Segunda categoría |
| 4 | `color/dataviz/series/3` | Tercera categoría |
| 5 | `color/dataviz/series/4` | Cuarta categoría |

> Cambio respecto de 2.4.0: la primera categoría pasa de `series/2` (azul) a `series/1` (rojo). En una dona de dos segmentos —el caso real— el contraste positivo/negativo debe leerse como verde vs. rojo, no verde vs. azul. Ver § 19-06.

- El segmento positivo abre en las 12 en punto y avanza en sentido horario.
- Una dona nunca lleva más de **cinco segmentos**. Con más categorías, agrupar en `Otros`.

### 8.3 Leyenda

| Propiedad | Valor |
|---|---|
| Posición desktop | A la derecha de la dona · gap `32px` |
| Posición mobile | Debajo de la dona · gap `32px` · centrada |
| Indicador | `8 × 8px` redondeado |
| Gap indicador → etiqueta | `18px` |
| Alto de fila | `16px` · paso `29px` |
| Valor | `32px` de ancho, alineado a la derecha |

El valor de la leyenda es **absoluto**; el valor central es **porcentual**. Es deliberado: el centro comunica la tasa, la leyenda el conteo.

### 8.4 Implementación

| Propiedad | Desktop | Mobile |
|---|---|---|
| Ancho de panel | `566px` | `328px` |
| Alto de panel | `381px` | `381px` |
| Diámetro | `180px` (`179.74`) | `134px` (`134.26`) |
| Segmentos | `2` | `2` |

En producción: `Incidencias` (General, span 6). Dos segmentos: `Sin incidencias` / `Incidencias`.

---

## 9. Mapa de calor geográfico

Choropleth de la República Mexicana por volumen, acompañado de una tabla de ranking. Siempre **span 12**.

Componente nuevo en 2.5.0.

### 9.1 Anatomía — desktop

```
Mapa de envíos por estado
Zonas de calor por volumen de envíos del periodo. Pasa el cursor sobre un estado.

┌────────────────────────┐  ┌──────────────────────────────────────┐
│      [Mapa México]     │  │ #  Estado      Envíos  Entreg.  Part.│
│         ┌────────────┐ │  │ 1  México        608   92.6%   21.7% │
│         │ Tamaulipas │ │  │ 2  CDMX          568   93.1%   20.3% │
│         │ Envíos  94 │ │  │ …                                    │
│         └────────────┘ │  │ #  Total       2,799   93.1%    100% │
│ Menos ▬▬▬▬▬▬▬▬ Más     │  └──────────────────────────────────────┘
└────────────────────────┘
```

### 9.2 Tokens

| Elemento | Valor |
|---|---|
| Zona de mapa | `537.5 × 417px` |
| SVG de México | `513 × 385px` |
| Zona de tabla | `537.5 × 440px` |
| Gap mapa ↔ tabla | `24px` |
| Barra de escala | `341 × 16px`, centrada bajo el mapa |
| Borde de estado | `1px` · `color/brand/gray/200` |

### 9.3 Escala de calor

Escala **discreta de cinco pasos**, no un degradado continuo. Los pasos se reparten por cuantiles del volumen del periodo, no por rangos absolutos.

| Paso | Token | Uso |
|---|---|---|
| Sin datos | `color/brand/base/white` + borde `gray/200` | Estado sin envíos en el periodo |
| 1 | `color/dataviz/map/1` | Cuantil más bajo |
| 2 | `color/dataviz/map/2` | |
| 3 | `color/dataviz/map/3` | |
| 4 | `color/dataviz/map/4` | |
| 5 | `color/dataviz/map/5` | Cuantil más alto |

Ver § 16 para los valores. La escala discreta se eligió sobre la continua porque una interpolación no es legible en estados pequeños y no se puede reproducir en la barra de escala ni en la leyenda.

### 9.4 Barra de escala

| Propiedad | Valor |
|---|---|
| Tamaño | `341 × 16px` (desktop) · `228 × 40px` (mobile) |
| Etiquetas | `Menos envíos` (izq.) · `Más envíos` (der.) |
| Tipografía | Manrope Regular `10px` |
| Relleno | Los cinco pasos de § 9.3, en bloques contiguos |

Sin valores numéricos: es una escala relativa al periodo consultado.

### 9.5 Tooltip de estado

| Propiedad | Valor |
|---|---|
| Tamaño | `154 × 98px` |
| Padding | `12px` |
| Encabezado | Indicador `8 × 8px` + nombre del estado · `12px` |
| Filas | `3` — `Envíos` · `Entregados` · `Participación` |
| Alto de fila | `14px` · paso `18px` |

El estado bajo el cursor se resalta; el resto **no** se atenúa.

### 9.6 Tabla de ranking

| Propiedad | Valor |
|---|---|
| Columnas | `#` · `Estado` · `Envíos` · `Entregados` · `Participación` |
| Filas visibles | `9` + fila `Total` |
| Orden | Descendente por volumen |
| Fila Total | Siempre al final · `#` en lugar de posición |
| Mobile | Se conserva, con paginación |

Tokens de tabla en `components/TABLES.md`.

### 9.7 Implementación

| Propiedad | Desktop | Mobile |
|---|---|---|
| Ancho de panel | `1131px` | `328px` |
| Alto de panel | `535px` | `832px` |
| Disposición | Mapa + tabla lado a lado | Mapa arriba, tabla abajo |

En producción: `Mapa de envíos por estado` (General, span 12).

---

## 10. Línea de tiempo de estatus

Estado vivo de la operación: cuántas entidades hay en cada etapa del ciclo en este momento. Siempre **span 12**.

Componente nuevo en 2.5.0.

### 10.1 Anatomía — desktop

```
Tus envíos en tiempo real

  📋 ┄┄┄┄┄┄ 📦 ┄┄┄┄┄┄ 🚚 ┄┄┄┄┄┄ ✓        │   ↻        ⊗
  22        14        106       205       │   106      22
Por recol. Recolect. En camino Entregado  │ Retornado Cancelado
```

El flujo lineal y los **estados terminales** están separados por una línea vertical. Los estados terminales no forman parte del flujo y por eso no se conectan con la línea punteada.

### 10.2 Tokens

| Elemento | Valor |
|---|---|
| Zona de línea de tiempo | Alto `115px` |
| Separador vertical | `0.5px` · alto `115px` · `color/brand/gray/200` |
| Nodo | `68 × 82px` |
| Ícono | `20 × 20px` · centrado |
| Número | Manrope Bold `24px` · caja `33px` |
| Etiqueta | Manrope `10px` · caja `14px` · **subrayada** |
| Conector | Punteado · a la altura del ícono · `color/brand/gray/200` |

Las etiquetas navegan al listado filtrado por esa etapa, igual que en § 7.3.

### 10.3 Reglas

- El reparto entre flujo y estados terminales es proporcional al número de nodos de cada zona.
- Los conectores unen **solo** nodos del flujo. Nunca cruzan el separador.
- Todos los nodos se muestran siempre, incluso en `0`.
- Cada etapa tiene un ícono propio. Ningún ícono se repite entre etapas.

### 10.4 Implementación

| Propiedad | Desktop | Mobile |
|---|---|---|
| Ancho de panel | `1134px` | `328px` |
| Alto de panel | `186px` | `377.5px` |
| Zona de flujo | `780px` · 4 nodos en línea | `296 × 184px` · grid 2 × 2 |
| Zona terminal | `321.5px` · 2 nodos | `296 × 82px` · 2 nodos |
| Separador | Vertical · `x: 780.5` | Horizontal · `y: 260.5` |
| Conectores | `139–145px` | **Ausentes** |

En mobile el flujo se convierte en grid 2 × 2 y los conectores desaparecen: es el único elemento del sistema que no sobrevive al cambio de breakpoint.

En producción: `Tus envíos en tiempo real` (En tiempo real, span 12).

---

## 11. Panel de acción requerida

Contadores de entidades que exigen intervención del usuario, con acceso directo a cada una. Siempre **span 12**.

Componente nuevo en 2.5.0.

### 11.1 Anatomía — desktop

```
┌──────────────────────────────────────────────────────────────┐
│ Requiere acción                          [ Ir a incidencias ]│
├──────────────────┬──────────────────────┬────────────────────┤
│ Cambio de        │ Destinatario no      │ Envíos con         │
│ dirección        │ localizado           │ sobrepeso          │
│ 5    [63%]       │ 2      [25%]         │ 1      [13%]       │
│      Ver detalle›│        Ver detalle › │      Ver detalle › │
└──────────────────┴──────────────────────┴────────────────────┘
```

### 11.2 Tokens

| Elemento | Valor |
|---|---|
| Celdas | `3` — se reparten el ancho útil en tercios |
| Separador entre celdas | Borde vertical `1px` · `color/brand/gray/200` · sin gap |
| Padding de celda | `16px` |
| Título de celda | Manrope `12px` · caja `16px` |
| Monto | Manrope Bold `28px` · caja `38px` |
| Chip de participación | `39 × 14px`, sin ícono, a `12px` del monto |
| Enlace | `Ver detalle` + chevron `16px`, alineado a la derecha |
| Botón del encabezado | `button/secondary` · `180 × 35px`, alineado a la derecha |

El monto de esta celda es `28px`: el número más grande del sistema después del valor central de la dona.

### 11.3 Reglas

- Siempre **tres** celdas. Si una categoría no tiene entidades, se muestra en `0` — no se oculta.
- El chip comunica participación sobre el total que requiere acción, no delta contra el periodo anterior.
- `Ver detalle` navega al listado filtrado por esa causa.
- El botón del encabezado **desaparece en mobile**; el acceso queda solo por `Ver detalle`. Ver § 19-07.

### 11.4 Implementación

| Propiedad | Desktop | Mobile |
|---|---|---|
| Ancho de panel | `1131px` | `328px` |
| Alto de panel | `222px` | `458px` |
| Celda | `366.33 × 139px` | `296 × 129px` |
| Disposición | 3 columnas | 3 filas apiladas |
| Separador | Vertical | Horizontal |

En producción: `Requiere acción` (En tiempo real, span 12).

---

## 12. Tabla de cohortes

Matriz de retención tipo heatmap. Siempre span 12.

> **Estado: definida, no implementada.** No aparece en ninguna vista en producción. Se conserva la especificación de 2.4.0 sin cambios; los pendientes de § 12.2 siguen abiertos.

### 12.1 Estructura

| Zona | Tipografía | Color |
|---|---|---|
| Encabezado | Manrope Bold `12px` | `color/brand/gray/600` |
| Alto de encabezado | `41px` | — |
| Columna de etiqueta | Manrope Medium `12px` | `color/brand/base/oxford` |
| Celda de dato | Manrope Medium `12px`, centrada | `color/brand/base/oxford` |
| Padding vertical de celda | `12px` | — |

### 12.2 Escala de intensidad

La escala base es la misma del mapa de calor (§ 9.3, tokens `color/dataviz/map/{1..5}`): es la misma necesidad —intensidad sobre una matriz— y no justifica una segunda escala. Esto cierra el pendiente de dos niveles que 2.4.0 dejaba abierto.

**Queda un pendiente nuevo:** la celda de cohortes lleva el valor **dentro** del relleno, y a partir de `map/3` ningún color de texto del sistema alcanza 4.5:1 (§ 16.1). Antes de implementar hay que elegir una de tres:

| Opción | Consecuencia |
|---|---|
| Limitar la escala a `map/1`–`map/2` | Solo dos niveles de intensidad — el problema original |
| Sacar el valor del relleno (chip blanco dentro de la celda) | Cinco niveles, pero cambia la anatomía de la celda |
| Celda sin valor, dato solo en tooltip | Cinco niveles, pero la matriz deja de leerse de un vistazo |

Ver § 19-08.

---

## 13. Elementos compartidos

### 13.1 Tooltip de comparación

Único tooltip del sistema. Se usa en § 4 y § 5.

```
┌──────────────────────────┐
│ Semana 2                 │
│ ● 9 jun 2026  1,002  35% │
│ ● 9 may 2026    802  22% │
└──────────────────────────┘
```

| Propiedad | Valor |
|---|---|
| Ancho | Se ajusta al contenido (`196–218px` observado) |
| Alto | `84px` |
| Padding | `12px` |
| Encabezado | `12px` · caja `16px` · `y: 12` |
| Filas | `2` · caja `14px` · paso `22px` |
| Indicador | `8 × 8px` redondeado |
| Gap indicador → fecha | `18px` |
| Columnas de valor y porcentaje | Alineadas a la derecha |
| Background | `color/brand/base/white` |
| Shadow | `shadow_card` |
| Radius | `10px` |

- El encabezado nombra el punto del eje X en lenguaje de negocio: `Semana 2`, `2 Días`. Nunca la fecha cruda.
- Las fechas de fila **sí** llevan año (`9 jun 2026`), a diferencia del eje X.

### 13.2 Leyenda de series

| Propiedad | Valor |
|---|---|
| Indicador | `8 × 8px` redondeado |
| Gap indicador → texto | `11px` |
| Gap entre items | `16px` |
| Texto | Manrope `10px` · caja `14px` |
| Posición | Centrada horizontalmente en el panel |
| Separación respecto de la gráfica | `8px` |

Etiquetas aprobadas: `Envíos` / `Periodo anterior` · `Incidencias` / `Periodo anterior`.

**La leyenda es obligatoria en toda gráfica de dos o más series.** Es el canal redundante que exige `accesibility/A11Y.md`: las series del sistema son todas rojas y no se distinguen por color bajo deuteranopia.

### 13.3 Barra de filtros

Va entre el título de página y el primer panel.

| Propiedad | Valor |
|---|---|
| Alto del control | `30px` |
| Padding lateral | `10px` |
| Chevron | `16 × 16px` |
| Texto | Manrope `12px` · caja `15px` |
| Gap entre controles | `12px` |
| Separador tras el rango de fechas | Línea vertical `1px` · alto `19px` |

Controles por vista:

| Vista | Filtros | Ancho total |
|---|---|---|
| Con periodo | Rango de fechas · Paquetería · Tipo de servicio | `437px` |
| Sin periodo (tiempo real) | Paquetería · Tipo de servicio | `256px` |

Una vista de tiempo real **no lleva filtro de fechas**. En su lugar, el título muestra el indicador `Ahora mismo` con un punto de estado (`icon-info/dot`, `10 × 10px`).

**En mobile la barra debe adaptarse: los controles a ancho de desktop suman `421–439px` sobre un contenedor de `328px`.** El comportamiento está sin definir. Ver § 19-09.

---

## 14. Comportamiento responsive

| Componente | Desktop | Mobile | Regla |
|---|---|---|---|
| Card Data (§ 3) | 4–5 en una fila | 1 hero + 2 × 2 | El KPI principal ocupa el ancho completo |
| Línea (§ 4) | span 6 o 12 | ancho completo | El alto del plot **no cambia** (`185px`) |
| Barras verticales (§ 5) | span 6 | ancho completo | Mismo número de barras; se comprime el gap |
| Barras horizontales (§ 6) | 1 línea por fila | 2 líneas por fila | La etiqueta sube a su propia línea |
| Lista de estatus (§ 7) | span 6 | ancho completo | Estructura idéntica, solo cambia el ancho de columna |
| Dona (§ 8) | dona + leyenda a la derecha | dona + leyenda abajo | Diámetro `180px` → `134px` |
| Mapa (§ 9) | mapa + tabla lado a lado | mapa arriba, tabla abajo | La tabla se pagina en mobile |
| Línea de tiempo (§ 10) | flujo horizontal con conectores | grid 2 × 2 sin conectores | Único elemento que se elimina |
| Acción requerida (§ 11) | 3 columnas | 3 filas | El botón del encabezado desaparece |
| Barra de filtros (§ 13.3) | en línea | **sin definir** | Ver § 19-09 |

### 14.1 Reglas transversales

- **Ninguna gráfica scrollea horizontalmente.** Cuando el contenido no cabe, cambia de disposición.
- **Ninguna gráfica se recorta.** El número de barras, filas y segmentos es el mismo en ambos breakpoints.
- El alto del plot es constante entre breakpoints. Solo el ancho es fluido.
- Ningún texto cambia entre breakpoints. Una misma métrica se llama igual en desktop y en mobile.

---

## 15. Estados

### 15.1 Vacío

Cuando no hay datos en el periodo consultado, la vista **conserva su estructura completa**. No se reemplaza por una ilustración.

| Elemento | Comportamiento en vacío |
|---|---|
| Card Data — monto | `0` |
| Card Data — chip | Texto `Sin comparación`, sin ícono ni color |
| Card Data inline | `0%` + su leyenda fija |
| Gráfica de línea | Ejes, guías y leyenda visibles, sin curvas |
| Barras verticales | Ejes y guías visibles, sin barras |
| Barras horizontales | Track visible al 100%, valor `0`, chip `0%` |
| Lista de estatus | Todas las filas presentes con valor `0` y chip `0%` |
| Dona | Círculo completo en `color/brand/gray/200`, centro en `0%` |
| Mapa de calor | Todos los estados en blanco con borde; tabla con `Total` en `0` |
| Línea de tiempo | Todos los nodos en `0`, conectores e íconos visibles |
| Acción requerida | Las 3 celdas en `0`; `Ver detalle` deshabilitado |
| Tabla de cohortes | Celdas en `0%` con background `color/dataviz/track` |

**Razón:** mantener el esqueleto comunica que la consulta funcionó y no arrojó resultados, en vez de sugerir un error de carga. Esto difiere del patrón general de `patterns/EMPTY-STATES.md`, que sí usa ilustración + CTA — ese patrón aplica a vistas sin configurar, no a periodos sin datos.

### 15.2 Carga

**Skeleton, nunca spinner.** El panel conserva su altura exacta para evitar el salto de layout. Se enmascaran los datos, no el contenedor: el título del panel, los ejes y las etiquetas permanecen visibles.

### 15.3 Hover

| Elemento | Comportamiento |
|---|---|
| Card Data | Border `red/200` |
| Punto de gráfica de línea | Línea guía vertical + marcadores + tooltip (§ 4.4) |
| Barra vertical | Marcadores + tooltip (§ 5.5) |
| Barra horizontal | **Sin definir** — § 19-10 |
| Fila de lista de estatus | **Sin definir**; la etiqueta es un link — § 19-10 |
| Segmento de dona | **Sin definir** — § 19-10 |
| Estado del mapa | Resalte del estado + tooltip (§ 9.5) |
| Nodo de línea de tiempo | **Sin definir**; la etiqueta es un link — § 19-10 |

Transición: `150ms ease`. Ningún elemento se atenúa al hacer hover sobre otro.

### 15.4 Error

**Sin definir.** Ninguna vista en producción documenta el estado de error de carga. Es un hueco abierto, no una omisión deliberada. Ver § 19-11.

---

## 16. Tokens de data visualization

**Bloque a agregar en `foundation/COLORS.md`.** Mientras no se agregue, este archivo es la declaración de los tokens `color/dataviz/*`: no existen en ningún otro lado del sistema.

| Token | Referencia | Hex | Uso |
|---|---|---|---|
| `color/dataviz/series/1` | `red/400` | `#E26153` | Serie principal: línea de periodo actual, barras, primera categoría |
| `color/dataviz/series/2` | `blue/500` | `#2180FF` | Segunda categoría |
| `color/dataviz/series/3` | `yellow/500` | `#EDBD55` | Tercera categoría |
| `color/dataviz/series/4` | — | `#4F6EE0` | Cuarta categoría |
| `color/dataviz/series/5` | `red/200` | `#F1B0A9` | Serie de comparación (periodo anterior), quinta categoría |
| `color/dataviz/positive` | `green/500` | `#4FC153` | Estado sano, deltas al alza |
| `color/dataviz/negative` | `red/700` | `#CC0000` | Deltas a la baja |
| `color/dataviz/track` | `gray/50` | `#F8F8F8` | Base de barra, celda sin valor, fila alterna |
| `color/dataviz/accent` | `red/200` | `#F1B0A9` | Border de Card Data seleccionada / hover |

### 16.1 Escala de intensidad

Para mapa de calor (§ 9) y tabla de cohortes (§ 12). Cinco pasos tomados **sin alterar** de la escala Brand Red de `foundation/COLORS.md`.

| Token | Referencia | Hex |
|---|---|---|
| `color/dataviz/map/empty` | `base/white` | `#FFFFFF` · borde `gray/200` |
| `color/dataviz/map/1` | `red/100` | `#F9D2D2` |
| `color/dataviz/map/2` | `red/200` | `#F1B0A9` |
| `color/dataviz/map/3` | `red/300` | `#E9897E` |
| `color/dataviz/map/4` | `red/400` | `#E26153` |
| `color/dataviz/map/5` | `red/500` | `#DB3B2B` |

**La escala no admite texto encima a partir de `map/3`.** Contraste medido contra los dos únicos colores de texto disponibles:

| Paso | vs `oxford` | vs `white` | Mejor | WCAG AA (4.5:1) |
|---|---|---|---|---|
| `map/1` | `6.21` | `1.38` | oxford | ✅ |
| `map/2` | `4.71` | `1.82` | oxford | ✅ |
| `map/3` | `3.41` | `2.52` | oxford | ❌ |
| `map/4` | `2.48` | `3.46` | white | ❌ |
| `map/5` | `1.91` | `4.49` | white | ❌ |

**Regla:** un relleno de `map/3` o superior **no puede llevar texto dentro**. En el mapa de calor no es problema —las celdas no llevan texto, el dato vive en el tooltip y en la tabla de ranking—. En la tabla de cohortes sí lo es, y por eso § 12.2 queda abierta.

### 16.2 Excepción semántica

Estos tokens **rompen deliberadamente** la regla de `COLORS.md` que prohíbe usar colores semánticos como decoración.

En data visualization, el amarillo **no significa** precaución y el azul **no significa** información: son categorías sin carga semántica. La única excepción dentro de la excepción es `positive` / `negative`, donde el verde y el rojo sí conservan su significado.

Fuera de gráficas, la regla original sigue vigente sin cambios.

### 16.3 `series/4` — token sin escala base

`#4F6EE0` es el único token de la paleta que **no referencia un color de la escala de marca**. Es un azul violáceo exclusivo de data visualization. No debe usarse en ningún otro contexto ni agregarse a la escala Blue.

### 16.4 Advertencia de accesibilidad

`series/1` (`#E26153`) y `series/5` (`#F1B0A9`) son ambos rojos. En segmentos pequeños de dona la diferencia se reduce a luminosidad, y bajo deuteranopia son difíciles de separar. Lo mismo aplica a los pasos `map/2` a `map/5`.

**Mitigación obligatoria:**

1. Toda gráfica de dos o más series lleva leyenda con etiqueta de texto (§ 13.2).
2. La serie de comparación se distingue además por **trazo punteado**, no solo por color.
3. El mapa de calor se acompaña de la tabla de ranking (§ 9.6), que da el mismo dato en texto.

El color nunca es el único canal de información. Ver `accesibility/A11Y.md`.

### 16.5 Colores en uso sin token

Detectados en el Figma de T1envíos. Todos deben migrarse.

| Hex | Dónde | Resolución |
|---|---|---|
| `#EB5757` (variable `Red`, legacy) | Segmento de incidencias en la dona | → `color/dataviz/series/1`. **Cambia visualmente.** |
| Verde sin bindear | Segmento sin incidencias en la dona | → `color/dataviz/positive`. **Cambia visualmente.** |
| `#51AF70` (`state indicators/success`) | Presente en el nodo, no aplicada | Retirar |
| `#FE4D61` (`text/chips/red`) | Texto de chips | → `color/brand/red/700` |
| `#828282` (variable `Gray 3`) | Texto secundario | → `color/brand/gray/600` |
| Degradado del mapa | Escala de calor | → `color/dataviz/map/{1..5}` |

---

## 17. Reglas de implementación

- **Manrope siempre.** Sora e Inter no existen en dashboard.
- **Rojo en data-viz es color de serie, no error.** Es la única zona del dashboard donde el rojo no significa error ni CTA. Fuera de un panel de métricas, el rojo mantiene su significado original.
- **Máximo cinco series por gráfica.** La paleta no tiene un sexto color y no debe inventarse.
- **En comparación de periodos, máximo dos series.** Actual y anterior. Una tercera serie de comparación es un componente nuevo, no una variante.
- **Leyenda obligatoria en toda gráfica de dos o más series.** Ver § 16.4.
- **La serie de comparación siempre va punteada.** El color no basta.
- **Sin count-up.** Los números aparecen en su valor final. Las animaciones de conteo son exclusivas de landing.
- **Transiciones funcionales.** Solo hover (`150ms ease`) y carga. Nada decorativo.
- **Skeleton durante carga**, nunca spinner.
- **El track de barra siempre se dibuja completo**, incluso con valor `0`.
- **La estructura sobrevive al vacío.** Ejes, guías, filas y leyenda permanecen cuando no hay datos.
- **Un panel, una métrica.** La única excepción es el mapa de calor, que combina mapa y tabla porque son la misma métrica en dos representaciones.
- **El alto del plot es constante entre breakpoints.** Solo el ancho es fluido.
- **Las etiquetas subrayadas son navegables.** En § 7 y § 10 llevan a listados filtrados. El subrayado no es decorativo.
- **Ningún hex directo.** Todo color entra por token de `foundation/COLORS.md`.
- **La librería de charting sigue sin confirmarse.** Estas specs son agnósticas de librería a propósito. Pendiente de Franco / Mario.

---

## 18. Cobertura de implementación

Estado de cada componente al cierre de esta versión.

| § | Componente | Estado | Dónde |
|---|---|---|---|
| 3 | Card Data | ✅ En producción | T1envíos › Reportes › General · Incidencias y retornos |
| 4 | Gráfica de línea | ✅ En producción | General (span 6) · Incidencias y retornos (span 12) |
| 5 | Barras verticales | ✅ En producción | General |
| 6 | Barras horizontales | ✅ En producción | Incidencias y retornos (× 2) |
| 7 | Lista de estatus | ✅ En producción | General |
| 8 | Dona | ✅ En producción | General |
| 9 | Mapa de calor | ✅ En producción | General |
| 10 | Línea de tiempo | ✅ En producción | En tiempo real |
| 11 | Acción requerida | ✅ En producción | En tiempo real |
| 12 | Tabla de cohortes | ⬜ Definida, no implementada | — |
| 13.1 | Tooltip | ✅ En producción | General · Incidencias y retornos |
| 13.2 | Leyenda | ✅ En producción | Todas las gráficas de dos series |
| 13.3 | Barra de filtros | ⚠️ En producción, mobile sin resolver | Las tres vistas |

### 18.1 Frames de origen

| Vista | Breakpoint | Node ID |
|---|---|---|
| General | Desktop | `18785:231813` |
| General | Mobile | `18785:234469` |
| En tiempo real | Desktop | `18785:232595` |
| En tiempo real | Mobile | `18785:235785` |
| Incidencias y retornos | Desktop | `18785:232888` |
| Incidencias y retornos | Mobile | `18785:235883` |

Archivo: `T1 Envíos 2026` (`DILjiDu55I7arqzmLmeXxS`).

---

## 19. Discrepancias detectadas

Hallazgos de `Componentes-DB` y `T1 Envíos 2026` contra NEXUS.
Categorías: **(a)** error de implementación · **(b)** Figma contradice el MD · **(c)** no documentado.

### 19.1 Abiertas — requieren decisión

| # | Hallazgo | Ubicación | Cat. | Resolución |
|---|---|---|---|---|
| 01 | El ancho de contenido `1134px` deriva del sidebar de `241px`, no del canónico `184px`. Con el sidebar vigente el ancho útil sería `1208px` y la columna `82.33px` | § 1.1 · todos los frames | (b) | **Bloquea todo el grid.** Decidir si el grid se recalcula al sidebar canónico o si `1134` se congela como token independiente |
| 02 | Fila de 5 KPIs de `210.8px`: no corresponde a ningún span del grid de 12 columnas | § 1.3 · General | (b) | Admitir la partición en quintos (§ 1.3) o reducir a 4 cards de span 3 |
| 03 | Título de panel en `16px` SemiBold en los seis frames; el MD fija `14px` Bold | § 2.2 | (b) | Elegir uno y aplicarlo a los dos archivos de Figma |
| 04 | `MOLECULES.md` no contiene el puntero al Card Data que este archivo declara. La § 13.2 citada es `Catálogo de estructuras` | § 3 · `components/MOLECULES.md` | (a) | Agregar el puntero en MOLECULES.md o retirar la referencia |
| 05 | Reclasificación: la evolución temporal se resuelve con línea, no con barras verticales | § 4, § 5 | (c) | Aplicada en esta versión. Confirmar con desarrollo |
| 06 | Orden de segmentos de dona: la primera categoría pasa de `series/2` a `series/1` | § 8.2 | (c) | Aplicada en esta versión. **Cambia visualmente** cualquier dona existente de 3+ segmentos |
| 07 | El botón `Ir a incidencias` desaparece en mobile sin sustituto | § 11.3 | (b) | Confirmar que `Ver detalle` basta, o agregar el botón al pie del panel |
| 08 | Escala de cohortes con solo dos niveles de intensidad | § 12.2 | (c) | Escala resuelta (`map/{1..5}`), pero a partir de `map/3` el texto dentro de la celda no alcanza 4.5:1. Elegir una de las tres opciones de § 12.2 |
| 09 | La barra de filtros mide `421–439px` en mobile sobre un contenedor de `328px` | § 13.3 · los 3 frames mobile | (a) | **Desborda el viewport.** Definir: scroll horizontal, dos filas, o bottom sheet |
| 10 | Sin hover definido para barra horizontal, fila de lista de estatus, segmento de dona y nodo de línea de tiempo | § 15.3 | (c) | Definir. Los elementos navegables necesitan afordancia además del subrayado |
| 11 | Sin estado de error de carga en ninguna vista | § 15.4 | (c) | Definir |
| 12 | El bloque `color/dataviz/` sigue sin agregarse a `foundation/COLORS.md` desde que 2.4.0 lo anunció. Los tokens solo existen en § 16 de este archivo | § 16 | (a) | Publicar el bloque en COLORS.md, o aceptar que METRICS.md sea su declaración y decirlo ahí |
| 12b | La variable de Figma `state indicators/error` vale `#DB362B`, que es `red/600` (variante oscura), no el rojo de error | Archivo de variables | (b) | Revisar si el rol `error` debe apuntar a `red/700` (`#CC0000`). El hex en sí es válido |
| 13 | Personalización de paneles no definida | Sistema | (c) | Decidir antes de implementar |
| 14 | Librería de charting sin confirmar | Sistema | (c) | Pendiente de Franco / Mario |

### 19.2 Corrección directa en Figma

| # | Hallazgo | Ubicación | Cat. |
|---|---|---|---|
| 15 | Escala de variables desplazada: `red-400`=`#F1B0A9`, `red-600`=`#E9897E`, `red-800`=`#E26153`, `gray-100`=`#F8F8F8`, `gray-400`=`#E7E7E7` | Ambos archivos | (b) |
| 16 | Namespace `color/neutral/` en vez de `color/brand/` | Grises | (b) |
| 17 | Radius de panel `12px` | `Componentes-DB` | (a) |
| 18 | Sidebar `241px` / header `60px` | Todos los frames | (a) |
| 19 | Gap vertical entre paneles: `24px` desktop, `20px` mobile | T1envíos | (a) |
| 20 | Gutter horizontal: `24px` en Incidencias y retornos, `20px` en General | T1envíos | (a) |
| 21 | Anchos de panel fuera del grid: `1131`, `566`, `558.5`, `555.5`, `555px` | T1envíos | (a) |
| 22 | La fila Dona + Barras verticales suma `1141.5px` sobre un contenedor de `1134px` — desborda `7.5px` | General / Desktop | (a) |
| 23 | Líneas guía no equidistantes: `51/41/46/46px` en línea, `61/51/56/56px` en barras | § 4.2, § 5.2 | (a) |
| 24 | Separación gráfica → leyenda con tres valores distintos: `8`, `16` y `26px` | § 13.2 | (a) |
| 25 | Gap interno del Card Data `12px` en producción; el MD fija `4px` | § 3.2 | (a) |
| 26 | Caja del título del Card Data: `19px` en desktop y hero, `16px` en cards pareadas de mobile | § 3.4 | (a) |
| 27 | Indicador de leyenda `10 × 10px` en la dona, `8 × 8px` en el resto | § 8.3 | (a) |
| 28 | `Cancelado` usa `check-circle-fill`, el mismo ícono que `Entregado` | § 10.2 | (a) |
| 29 | Etiquetas distintas entre breakpoints: `Por recolectar`/`Guías generadas`, `Entregado`/`Entregados hoy` | § 10.4 | (a) |
| 30 | `Barra creciente` de `Dirección incorrecta` mide `503px` sobre un track de `250px` | `18785:233270` | (a) |
| 31 | `Base` de la primera fila de Retornos mide `136px`; el resto `250px` | `18785:233269` | (a) |
| 32 | Nombres de frame incorrectos: `18785:232888` = `En tiempo real / Desktop` siendo Incidencias y retornos; `18785:235883` = `Step three - summary hidden [360]` | Frames raíz | (a) |
| 33 | Nombres de capa incorrectos: paneles de barras horizontales llamados `Días de entrega promedio`; panel de barras verticales llamado `Evolucion por semana` | T1envíos | (a) |
| 34 | Cinco segmentos de dona nombrados `Rojo`, `Verde 02–05`; ninguno corresponde a su nombre | `68:4817`–`68:4821` | (a) |
| 35 | `#828282`, `#111827`, `#4A4A4A`, `#F3F4F6` hardcodeados | `Componentes-DB` · Cohortes y Días de entrega | (a) |
| 36 | `#FE4D61` usado sólido como color de serie y de texto | Ambos archivos | (b) |
| 37 | Segmentos de dona sin token: `#EB5757` y un verde no bindeado | § 16.5 | (a) |

---

## Referencias cruzadas

Rutas verificadas contra el repo. Las carpetas `accesibility/` y `plataform/` están escritas como existen hoy, con su typo, para que los enlaces resuelvan.

| Archivo | Relación |
|---|---|
| `foundation/COLORS.md` | Tokens base y escala Brand Red · el bloque `color/dataviz/` vive en § 16 de este archivo (§ 19-12) |
| `foundation/TYPOGRAPHY.md` | Escala Manrope |
| `foundation/ELEVATION.md` | `shadow_card` |
| `foundation/LAYOUT.md` | Grid, breakpoints, contenedores |
| `components/MOLECULES.md` | Card Data — **pendiente:** puntero a este archivo (§ 19-04) |
| `components/ORGANISMS.md` | Layout del dashboard, sidebar y header — § 1.1 |
| `components/TABLES.md` | Tabla de ranking del mapa (§ 9.6) y tablas de datos generales |
| `components/STATES.md` | Estados obligatorios |
| `patterns/DASHBOARD-LAYOUTS.md` | Composición de vistas — § 2 Dashboard home |
| `patterns/EMPTY-STATES.md` | Patrón general de vacío — § 15.1 documenta la excepción |
| `plataform/DASHBOARD.md` | Reglas de plataforma |
| `accesibility/A11Y.md` | Contraste y canales redundantes — § 16.4 |
| `workflows/RESPONSIVE.md` | Cómo colapsa cada patrón por breakpoint — § 14 |

---

## Notas para Claude

- Este archivo es la **fuente única** del Card Data. No tomar su definición de `MOLECULES.md`.
- Nunca asignar un color de serie fuera del orden establecido en § 8.2.
- El rojo dentro de un panel de métricas es color de serie. Fuera del panel, sigue significando error o CTA primario.
- Ante cualquier duda de valor, **manda el bloque de Tokens de cada sección**, no el de Implementación. El bloque de Implementación documenta lo que se construyó; las diferencias entre ambos están en § 19.
- Los tamaños marcados **(der.)** son derivados de la caja de línea. Verificar contra Figma antes de codificar.
- No completar por inferencia las secciones marcadas como sin definir: hover faltantes (§ 15.3), estado de error (§ 15.4), barra de filtros en mobile (§ 13.3).
- Los tokens `color/dataviz/*` están declarados en § 16 de este archivo, no en `COLORS.md`. Tomarlos de aquí.
- Ninguna gráfica de comparación de periodos admite una tercera serie. Si un requerimiento la pide, es un componente nuevo.
