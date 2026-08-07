# Tipografía — NEXUS V2.0

> Tres familias tipográficas, dos contextos visuales. **Manrope** para dashboard, **Sora + Inter** para landing pages. Nunca se mezclan entre contextos.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (variables) · **Owner:** Karla Salazar — Head of UX/UI

---

## Familias tipográficas

| Familia | Contexto | Rol | Line-height |
|---|---|---|---|
| **Manrope** | Dashboard / Admin | Tipografía única: headings, body, labels, todo | `1.366em` |
| **Sora** | Landing pages | Headings H0–H4 | `1.2em` |
| **Inter** | Landing pages | Body, botones, links, labels, H5+, todo excepto headings | `1.5em` |

**Regla fundamental:** Manrope NUNCA aparece en landing pages. Sora e Inter NUNCA aparecen en el dashboard.

---

## Pesos permitidos por familia

| Familia | Pesos válidos | Prohibidos |
|---|---|---|
| **Manrope** | Regular 400, Medium 500, SemiBold 600, Bold 700 | ~~Light 300~~, ~~ExtraBold 800~~ |
| **Sora** (landing headings) | Light 300 (solo H0), Regular 400 (H1–H4) | ~~SemiBold 600~~, ~~Bold 700~~ en headings |
| **Inter** (landing body) | Light 300, Regular 400, Medium 500, SemiBold 600 | ~~Bold 700~~, ~~ExtraBold 800~~ |

---

## Escala tipográfica — Dashboard (Manrope)

Toda la escala usa Manrope con line-height `1.366em`.

### Tamaños display (peso fijo)

| Token | Tamaño | Peso | Uso |
|---|---|---|---|
| `display-2xl` | 72px | Bold 700 | Hero sections de admin (raro) |
| `display-xl` | 60px | Bold 700 | Títulos de sección principales |
| `display-lg` | 48px | Bold 700 | Títulos de página |
| `medium-lg` | 36px | SemiBold 600 | Subtítulos prominentes |
| `semi-md` | 28px | SemiBold 600 | Encabezados de card |
| `title-base` | 24px | Bold 700 | Títulos de sección |

### Tamaños de contenido (peso variable según jerarquía)

Los tamaños de 20px a 12px se combinan con diferentes pesos para crear jerarquía dentro del mismo tamaño. No tienen un peso "default" fijo — el peso depende del rol del texto.

| Tamaño | Regular 400 | Medium 500 | SemiBold 600 | Bold 700 |
|---|---|---|---|---|
| **20px** | Descripciones largas | Table headers, nav items | Subtítulos enfáticos | Labels destacados |
| **16px** | Cuerpo de texto | Labels de formulario | Subtítulos de card | Títulos internos |
| **14px** | Body text, inputs | Labels, placeholders | Botones, tabs activos | Valores destacados |
| **12px** | Captions, helper text | Badges | Tags enfáticos | Contadores, KPIs mini |

---

## Escala tipográfica — Landing (Sora + Inter)

Las landing pages usan una escala diferente con tamaños responsive (mobile → desktop).

### Headings (Sora)

| Nivel | Peso | Mobile | Desktop | Clase Tailwind |
|---|---|---|---|---|
| **H0** — Display | Light 300 | `44px` | `54px` | `font-sora font-light text-[44px] tablet:text-[54px]` |
| **H1** — Section Title | Regular 400 | `28px` | `40px` | `font-sora font-normal text-[28px] tablet:text-[40px]` |
| **H2** — Subsection | Regular 400 | `26px` | `35px` | `font-sora font-normal text-[26px] tablet:text-[35px]` |
| **H3** — Card Heading | Regular 400 | `20px` | `24px` | `font-sora font-normal text-[20px] tablet:text-[24px]` |
| **H4** — Small Heading | Regular 400 | `16px` | `20px` | `font-sora font-normal text-[16px] tablet:text-[20px]` |

> **H0 es el ÚNICO nivel que usa Sora Light 300.** H1–H4 todos usan Sora Regular 400.

### Texto (Inter)

| Nivel | Peso | Mobile | Desktop | Clase Tailwind |
|---|---|---|---|---|
| **H5** — Mini Heading | Medium 500 | `16px` | `20px` | `font-inter font-medium text-[16px] tablet:text-[20px]` |
| **Body** | Regular 400 | `14px` | `16px` | `font-inter font-normal text-[14px] tablet:text-[16px]` |
| **Body Light** | Light 300 | `14px` | `14px` | `font-inter font-light text-[14px]` |
| **Nav / Tabs** | Medium 500 | `14px` | `14px` | `font-inter font-medium text-[14px]` |
| **Botones / CTA** | SemiBold 600 | `14px` | `14px` | `font-inter font-semibold text-[14px]` |
| **Links** | SemiBold 600 | `14px` | `14px` | `font-inter font-semibold text-sm text-oxford` |
| **Eyebrow** | SemiBold 600 | `11px` | `11px` | `font-inter font-semibold text-[11px] uppercase tracking-[0.15em]` |
| **Micro / Caption** | Regular 400 | `12px` | `12px` | `font-inter font-normal text-[12px]` |

### Consistencia de h2 en secciones (landing)

Todas las secciones de una landing DEBEN usar la misma escala para h2. No se permite que cada sección invente su tamaño.

| Elemento | Mobile | Tablet | Clase completa |
|---|---|---|---|
| h2 de sección | `32px` | `44px` | `font-sora text-[32px] font-light text-gray-900 tablet:text-[44px]` |
| h2 sobre fondo oscuro | `32px` | `44px` | `font-sora text-[32px] font-light text-white tablet:text-[44px]` |
| h1 de hero | `38px` | `52px` | Excepcional — solo el hero puede ser mayor |

Errores comunes: usar `text-[36px]`, `text-[48px]` o `text-[40px]` en tablet. Los tamaños son fijos: 32/44px.

---

## Colores de texto

Los colores de texto son compartidos entre dashboard y landing. Referencia completa en [COLORS.md](./COLORS.md).

| Rol | Hex | Token | Uso |
|---|---|---|---|
| **Primary (Oxford)** | `#4C4C4C` | `color/brand/base/oxford` | Texto principal, body copy |
| **Dark** | `#1F2937` | `color/brand/gray/900` | Headings, labels enfáticos |
| **Secondary** | `#6B7280` | `color/brand/gray/700` | Texto secundario, descripciones |
| **Tertiary** | `#9CA3AF` | `color/brand/gray/600` | Placeholders, texto disabled, eyebrow badges |
| **Inverse** | `#FFFFFF` | `color/brand/base/white` | Texto sobre fondos oscuros/primarios |
| **Link** | `#4C4C4C` | `color/brand/base/oxford` | Links — mismo color que texto principal, sin underline |
| **Link Hover** | `#4C4C4C` | `color/brand/base/oxford` | Links en hover — mismo color, el hover se indica con underline u opacidad |
| **Accent (solo landing)** | `#E26153` | `color/brand/red/400` | Acentos rojos en títulos de landing |

> **Nota dashboard:** El acento rojo en texto se evita en dashboard porque puede confundirse con un estado de error. En dashboard los links también son Oxford, hover a rojo.

---

## Patrón de títulos con acento rojo (solo landing)

Los títulos de landing frecuentemente incluyen una o dos palabras en rojo para enfatizar. El acento **siempre hereda el peso del padre**. Este patrón es exclusivo de landing pages — en dashboard se evita porque el rojo en texto puede interpretarse como estado de error.

```html
<!-- H0: Light 300, el span hereda Light -->
<h1 class="font-sora font-light text-[44px] text-gray-900 tablet:text-[54px]">
  Simplifica tu <span class="text-[#E26153]">crecimiento digital</span>
</h1>

<!-- H2: Regular 400, el span hereda Regular -->
<h2 class="font-sora font-normal text-[32px] text-gray-900 tablet:text-[44px]">
  Todo lo que necesitas <span class="text-[#E26153]">en un solo lugar</span>
</h2>
```

**Regla:** El `<span>` con color rojo NUNCA cambia el peso. Si el título es `font-light`, el acento es `font-light`. Si es `font-normal`, el acento es `font-normal`.

### Subtítulo con dato destacado

Máximo DOS niveles de tamaño en una misma línea: el tamaño base + un nivel de de-emphasis.

```html
<p class="font-sora text-[32px] font-light text-gray-900 tablet:text-[44px]">
  Desde <span class="font-bold text-[#E26153]">$299</span>
  <span class="text-[18px] text-gray-600 tablet:text-[24px]">MXN / mes</span>
</p>
```

❌ NUNCA usar 3+ tamaños diferentes en una misma línea de texto.

---

## Eyebrow badges

Formato estándar para labels encima de títulos de sección:

```html
<p class="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-600">
  Texto del eyebrow
</p>
```

Siempre Inter SemiBold 600, 11px, uppercase, tracking `0.15em`, color Gray 600 (`#9CA3AF`).

---

## Links (landing)

```html
<a class="font-inter text-sm font-semibold text-oxford hover:underline transition-colors">
  Probar gratis <ChevronRight class="h-4 w-4 inline" />
</a>
```

Inter SemiBold 600, color Oxford (`#4C4C4C`), **sin underline por default**. Puede incluir ícono chevron → o flecha.

---

## Configuración Tailwind CSS

### Font families

```js
fontFamily: {
  manrope: ['Manrope', 'sans-serif'],
  sora: ['Sora', 'sans-serif'],
  inter: ['Inter', 'sans-serif'],
},
```

### Font size tokens (dashboard / Manrope)

```js
fontSize: {
  // Display sizes (peso fijo)
  'display-2xl': ['72px', { lineHeight: '1.366em', fontWeight: '700' }],
  'display-xl': ['60px', { lineHeight: '1.366em', fontWeight: '700' }],
  'display-lg': ['48px', { lineHeight: '1.366em', fontWeight: '700' }],
  'medium-lg': ['36px', { lineHeight: '1.366em', fontWeight: '600' }],
  'semi-md': ['28px', { lineHeight: '1.366em', fontWeight: '600' }],
  'title-base': ['24px', { lineHeight: '1.366em', fontWeight: '700' }],
  // Content sizes (sin fontWeight — se controla con clases font-normal/medium/semibold/bold)
  'content-lg': ['20px', { lineHeight: '1.366em' }],
  'content-md': ['16px', { lineHeight: '1.366em' }],
  'content-sm': ['14px', { lineHeight: '1.366em' }],
  'micro': ['12px', { lineHeight: '1.366em' }],
},
```

> **Nota:** Los tamaños de contenido (20px–12px) no definen fontWeight porque se usan con múltiples pesos según el rol. Usar clases de Tailwind (`font-normal`, `font-medium`, `font-semibold`, `font-bold`) para controlar la jerarquía.

---

## Anti-patrones

- ❌ Usar Manrope en landing pages.
- ❌ Usar Sora o Inter en el dashboard.
- ❌ Sora Bold (700) o SemiBold (600) en headings de landing — deben ser Light (H0) o Regular (H1-H4).
- ❌ Inter Bold 700 o cualquier peso fuera de 300/400/500/600.
- ❌ Cambiar el peso del acento rojo respecto al título padre.
- ❌ Usar acento rojo en texto de dashboard — puede confundirse con estado de error.
- ❌ Underline en links por default (sin subrayado en estado normal).
- ❌ Links en azul — los links son Oxford (`#4C4C4C`), no azules.
- ❌ Links con hover en rojo — el hover también es Oxford.
- ❌ Inventar tamaños tipográficos fuera de la escala definida (ej: 22px o 18px en dashboard).
- ❌ Mezclar 3+ tamaños de texto en una misma línea.
- ❌ Usar `text-[36px]`, `text-[48px]` o `text-[40px]` en h2 de sección landing (son 32/44px).
- ❌ Usar un line-height diferente al de la familia (1.366em Manrope, 1.2em Sora, 1.5em Inter).

---

## Referencias

- [COLORS.md](./COLORS.md) — Colores de texto y acentos
- [THEMES.md](./THEMES.md) — Variaciones tipográficas por plataforma
- [PRINCIPLES.md](./PRINCIPLES.md) — Principio de Claridad (jerarquía tipográfica)
- [../platforms/LANDING.md](../platforms/LANDING.md) — Reglas tipográficas completas de landing
- [../platforms/DASHBOARD.md](../platforms/DASHBOARD.md) — Reglas tipográficas completas de dashboard
