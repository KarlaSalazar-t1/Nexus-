# Erratas detectadas en el archivo de Figma

**Archivo:** [Nexus V2](https://www.figma.com/design/agWwqm17qIvfveD8CQwSRz/Nexus-V2?node-id=244-12451) · frame `Icons-logos` (`244:12451`)
**Librería de componentes:** `SD T1_1`
**Fecha de la revisión:** 3 de septiembre de 2026
**Alcance:** 92 componentes y 205 variantes del frame `Icons-logos`, más los `icon-*` y `flag/*` de la librería.

> Este documento **no propone cambios al canon**. Recoge lo que hay que corregir **en el archivo de
> Figma**, porque el canon documenta el estado correcto y Figma se ha desviado de él.
> Cada punto está verificado contra el archivo, no inferido.

---

## Estado general

La correspondencia entre Figma y el canon es alta:

| Medida | Resultado |
|---|---|
| Componentes en `Icons-logos` | 92 |
| Assets documentados en `ICONOGRAPHY.md §4–§6` | 93 |
| **Coinciden por nombre exacto** | **82 (89 %)** |
| **Variantes idénticas** (de 73 comparables) | **69 (95 %)** |

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
Están tan extendidos (18 componentes) que conviene documentarlos en vez de renombrarlos.

**Caracteres problemáticos:** `j&texpress-iso` y `fb&IG-iso` usan `&`; el `filePath` de la librería
ya lo transforma en `_` (`fb_IG-iso`), lo que rompe la correspondencia entre nombre y ruta.

**Mayúsculas inconsistentes:** `Telmex-iso` frente a `telmex-iso-marketplace`;
`TikTok-logo` frente a `tiktok-isotipo` y `tiktokshop`.

---

## 5. Documentado en el canon, ausente en Figma

La sección **SOCIAL MEDIA** de `ICONOGRAPHY.md §4` lista siete componentes que no se encontraron
ni en el frame `Icons-logos` ni al buscarlos en la librería `SD T1_1`:

```
x-isotipo · reddit-isotipo · linkedin-isotipo · facebook-isotipo · google-isotipo · Insta · Whatsapp
```

Sí existen, en la sección MARKETING: `fb&IG-iso`, `meta-iso` y `whatsapp-iso`.

Además:

| Documentado | Situación en Figma |
|---|---|
| `aplazo-logo` | solo existe como variante dentro de `payment card`, no como componente propio |
| `logo-kometia` · `logo-mercadoshop` · `logo-spincommerce` | no encontrados |

> `Insta` y `Whatsapp` rompen además la convención `{marca}-{tipo}` que el propio canon define.

**Decisión pendiente:** o se crean en Figma, o se retiran del canon. Hoy la documentación
promete assets que quien la lee no va a encontrar.

---

## 6. Nombre de la librería

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
| 7 | Decidir sobre los 7 componentes de SOCIAL MEDIA | Figma **o** canon |
| 8 | Documentar `-iso-plataforma` y `-iso-marketplace` en §8 | canon |

Las acciones 1–6 no pueden resolverse con un pull request: requieren editar el archivo de diseño.
