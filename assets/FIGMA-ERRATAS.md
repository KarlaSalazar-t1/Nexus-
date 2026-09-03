# Erratas detectadas en el archivo de Figma

**Archivo:** [Nexus V2](https://www.figma.com/design/agWwqm17qIvfveD8CQwSRz/Nexus-V2?node-id=244-12451) · frame `Icons-logos` (`244:12451`)
**Librería de componentes:** `SD T1_1`
**Fecha de la revisión:** 3 de septiembre de 2026
**Alcance:** 123 componentes e instancias del frame `Icons-logos` (196 variantes medidas),
más los `icon-*` y `flag/*` de la librería. Incluye revisión visual del frame renderizado.

> Este documento **no propone cambios al canon**. Recoge lo que hay que corregir **en el archivo de
> Figma**, porque el canon documenta el estado correcto y Figma se ha desviado de él.
> Cada punto está verificado contra el archivo, no inferido.

---

## Estado general

La correspondencia entre Figma y el canon es alta:

| Medida | Resultado |
|---|---|
| Componentes e instancias en `Icons-logos` | 123 |
| Assets documentados en `ICONOGRAPHY.md §4–§6` | 93 |
| **Documentados que existen en Figma** | **93 (100 %)** |
| **Variantes idénticas** (de 73 comparables) | **69 (95 %)** |

Todo lo que el canon documenta existe en el archivo de diseño. Lo que falta es al revés:
componentes que se crearon en Figma y no llegaron al canon.

Las erratas de abajo son, en su mayoría, acumulación de trabajo reciente sin pasar por el canon.

---

## 1. Typos en nombres publicados

| Nombre actual | Debería ser | Dónde |
|---|---|---|
| `emex` | `amex` | variante de `payment card` |
| `analitycs-iso` | `analytics-iso` | sección MARKETING |
| `icon-action//ia` | `icon-action/ia` | librería `SD T1_1` — doble slash |
| `icon envios` | `icon-nav/envios` (o la categoría que corresponda) | librería `SD T1_1` — espacio y sin prefijo |
| `Component` | *(pendiente de nombrar)* | `Icons-logos` — nombre por defecto de Figma, variantes `Color · app` |

`emex` es el más urgente: American Express aparece mal escrito en el set de tarjetas de pago.

### Dos hallazgos de la revisión visual del frame

- **`T1careers`** aparece dibujado en la fila BRAND del frame, pero **no existe ningún componente
  publicado con ese nombre** ni en `Icons-logos` ni en la librería `SD T1_1`. O se componentiza,
  o se retira del frame.
- **`t1store-imagotipo` se lee «T1tienda»** en el arte. El archivo va en inglés y el logo en
  español; el README del canon llama al producto «T1 Tienda». Conviene alinear el nombre del
  componente con el producto.

---

## 2. Componentes duplicados

| Caso | Detalle |
|---|---|
| `t1score-imagotipo` | **dos componentes con el mismo nombre**, uno con variantes `Default · White` y otro con `Default · Variant2` |
| `total-iso` / `total-iso-v2` | mismas variantes (`ml`, `Variant2`); el sufijo `-v2` no está en la convención |
| `t1-logotipo` / `t1-logotipo-2` | dos logotipos T1 sin criterio documentado de cuál usar |
| `amazon-iso` / `amazon-iso-marketplace` | mismo patrón en `meli`, `shein` y `telmex` |
| `shopify-iso` / `shopify-iso-plataforma` | |
| `tienda-nube-iso-plataforma` / `icono/plataforma/Tienda nube` | el segundo además rompe la convención de nombres |

---

## 3. Nomenclatura de variantes

`ICONOGRAPHY.md §1` define cuatro variantes: `Default`/`Line`, `Fill`/`Color`, `Black`/`b/n`, `White`.
En Figma conviven **seis formas de decir "negro"**:

```
Black · black · b/n · bn · iconoBlack · gray
```

Y tres para "sin fondo", dos de ellas el mismo concepto escrito distinto:

```
Sin BG · Sin envolvente · SinEnvolvente
```

### Variantes autogeneradas

`Variant2`, `Variant11` y `Variant12` aparecen en `payment card`, `t1envios-imagotipo`,
`t1partners-imagotipo`, `total-iso`, `shopify-iso` y `t1score-imagotipo`.
`BRAND-ASSETS.md §2` documenta `Variant2` como *"alternativa tipográfica"* — conviene que el nombre lo diga.

### La propiedad lleva el nombre de la marca

En 11 sets la propiedad de variante se llama como la marca en vez de tener un nombre semántico
compartido: `Aliexpress=color`, `Amazon=off`, `ML=ml`, `Sanborns=color`, `Sears=Isotipo`,
`Shein=color`, `Shopify=Default`, `Stripe=bn`, `Totalplay=ml`, `Claroshop=imagotipo`, `default=Default`.

### Una variante que debería llamarse Default

`t1pagos-imagotipo` tiene las variantes `T1 pagos · White`. El canon la documenta como `Default · White`.

---

## 4. Nombres fuera de la convención

`ICONOGRAPHY.md §8` define `{marca}-{tipo}`, con `{tipo}` ∈ `iso · logo · imagotipo · isotipo`.

**Sin sufijo de tipo (9):**
```
cargamos · imile · logify · moova · tookan · walmart · grupoAmPm · paquetexpress · tiktokshop
```

**Sufijos usados en Figma que el canon no define:** `-iso-plataforma`, `-iso-marketplace`.
Están tan extendidos (21 componentes) que conviene documentarlos en vez de renombrarlos.

**Caracteres problemáticos:** `j&texpress-iso` y `fb&IG-iso` usan `&`; el `filePath` de la librería
ya lo transforma en `_` (`fb_IG-iso`), lo que rompe la correspondencia entre nombre y ruta.

**Mayúsculas inconsistentes:** `Telmex-iso` frente a `telmex-iso-marketplace`;
`TikTok-logo` frente a `tiktok-isotipo` y `tiktokshop`.

---

## 5. Tamaños: el canon describe un sistema que Figma no sigue

`ICONOGRAPHY.md §1` define cuatro tamaños — 16, 24, 30 y 64 px — y presenta **30×30** como el
estándar de logos de terceros. Los tamaños medidos en las 196 variantes del frame dicen otra cosa:

| Tamaño real | Variantes |
|---|---|
| **64 × 64** | 79 |
| 30 × 30 | 29 |
| 64 × 40 | 16 |
| 137 × 42 | 11 |
| 60 × 60 | 11 |
| 40 × 30 | 11 |
| 40 × 40 · 64 × 24 · 24 × 24 · 58 × 24 · 55 × 55 · 122 × 42 · 64 × 42 … | resto |

**64×64 es el tamaño dominante**, no 30×30. Y aparecen medidas que el canon no menciona:
`40×40`, `55×55`, `58×24`, `60×60`, `60×42`, `64×42`, `122×42`, `137×42`, `181×101`.

La mayoría de los logos **no son cuadrados**, mientras el canon los describe con un solo valor.

### Variantes del mismo componente con tamaños distintos

24 componentes cambian de tamaño al cambiar de variante. Los casos más marcados:

| Componente | Tamaños entre sus variantes |
|---|---|
| `99min-iso` | 42×42 · 60×60 · 64×24 · 64×40 · 64×64 |
| `ups-iso` | 34×34 · 60×60 · 64×40 · 64×64 |
| `conekta-imagotipo` | 24×24 · 64×11 |
| `kueski-imagotipo` | 24×24 · 64×15 |
| `openpay-imagotipo` | 24×24 · 64×64 |
| `tienda-nube-iso-plataforma` | 30×30 · 64×64 |

Cambiar de variante mueve el layout de quien lo consume. Las variantes de un set deberían
compartir caja.

### Imagotipos T1

La altura sí es consistente (**42 px** en los ocho), el ancho no —y no tiene por qué serlo, son
logos de distinta longitud. La excepción es `t1ai-imagotipo`, de **64×42**, muy por debajo de los
**137×42** de `t1cuenta`, `t1envios`, `t1partners` y `t1score`.

**Decisión pendiente:** o `ICONOGRAPHY.md §1` documenta los tamaños reales por familia, o el
equipo de diseño normaliza los componentes a la escala declarada. Hoy la tabla del canon no
describe el archivo.

---

## 6. La clasificación de tipo no coincide con el arte

El tipo de logo se declara en dos sitios: la columna «Notas» de `BRAND-ASSETS.md §5` y el sufijo
del propio nombre (`-isotipo`, `-logotipo`, `-imagotipo`). Se comprobó abriendo el arte.

**Alcance: 17 de 93 assets** — las secciones CARRIER, PAYMENT y SOCIAL MEDIA renderizadas a
resolución completa. Los 76 restantes no se revisaron.

### Mal clasificados (5 confirmados)

| Componente | Dice | Muestra el arte |
|---|---|---|
| `dhl-iso` | Isotipo | **Logotipo** — las 4 variantes son la palabra «DHL», sin símbolo |
| `ups-iso` | Isotipo | **Isologo** — escudo con «ups» dentro; texto y símbolo indivisibles |
| `oxxo-isotipo` | Isotipo | **Logotipo** — la palabra «OXXO» en su recuadro rojo |
| `spei-imagotipo` | Imagotipo | **Logotipo** — solo la palabra «SPEI» |
| `getnet-imagotipo` | Imagotipo | **Logotipo** — solo la palabra «Getnet» |

Un *isotipo* es el símbolo **sin** texto; un *imagotipo* combina símbolo y texto separables.
En los cinco casos el arte es solo tipografía.

### Bien clasificados (11)

`visa-logotipo` · `mastercard-isotipo` · `conekta-imagotipo` · `7-eleven-imagotipo` ·
`openpay-imagotipo` · `kueski-imagotipo` · `stripe-logotipo` · `fedex-logo` · `estafeta-logo` ·
`redpack-logo` · y los `-isotipo` de SOCIAL MEDIA, que sí son símbolos sin texto.

### Un caso mixto

`99min-iso` — el canon lo llama Imagotipo. El set tiene ambas cosas: el círculo con «99»
(isotipo) y la versión «99minutos.com» (imagotipo). El nombre solo describe una.

---

## 6b. Iconos de acción dentro de la sección CARRIER

Entre los logos de paquetería del frame hay tres piezas etiquetadas **`incidencia`**,
**`transferir`** y **`flash`** que no son logos de marca: son iconos de acción del sistema.
O se mueven a la sección de iconos, o se documenta por qué viven entre los carriers.

---

## 7. Nombre de la librería

La librería de componentes se llama **`SD T1_1`**. El sufijo `_1` sugiere un duplicado, y el
nombre no menciona NEXUS. Conviene confirmar que es la librería vigente y, si lo es, renombrarla.

---

## Resumen de acciones

| # | Acción | Dónde se corrige |
|---|---|---|
| 1 | Renombrar `emex` → `amex` | Figma |
| 2 | Corregir `analitycs-iso`, `icon-action//ia`, `icon envios` | Figma |
| 3 | Nombrar el componente `Component` | Figma |
| 4 | Resolver el duplicado `t1score-imagotipo` | Figma |
| 5 | Unificar el vocabulario de variantes (negro, sin fondo) | Figma |
| 6 | Renombrar `Variant2/11/12` a algo descriptivo | Figma |
| 7 | Igualar la tabla de tamaños de §1 con las medidas reales | canon **o** Figma |
| 8 | Documentar `-iso-plataforma` y `-iso-marketplace` en §8 | canon |
| 9 | Unificar el tamaño de las variantes dentro de cada set | Figma |
| 10 | Corregir la clasificación de los 5 assets mal tipados | canon |
| 11 | Revisar los 76 assets cuyo arte no se comprobó | canon |
| 12 | Reubicar `incidencia`, `transferir` y `flash` fuera de CARRIER | Figma |

Las acciones 1–6 no pueden resolverse con un pull request: requieren editar el archivo de diseño.
