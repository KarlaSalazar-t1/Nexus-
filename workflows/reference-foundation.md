# reference-foundation.md

> Tokens compartidos de NEXUS V2.0. Versión condensada para context window de Claude.  
> Fuente completa: `foundation/COLORS.md`, `TYPOGRAPHY.md`, `SPACING.md`, `LAYOUT.md`, `ELEVATION.md`.  
> **Figma es la fuente de verdad.** Ante cualquier discrepancia, Figma gana.

---

## Colores — Paleta completa

### Brand Red (primario)

| Token | Hex | Uso |
|---|---|---|
| Red 50 | `#FEF4F4` | Backgrounds de alertas error, hover suave |
| Red 100 | `#F9D2D2` | — |
| Red 200 | `#F1B0A9` | Shadow card-selected dashboard |
| Red 400 | `#E9897E` | — |
| Red 500 | `#DB3B2B` | **Botón primario dashboard**, hover `#CC0000` |
| Red 600 | `#E26153` | **Botón primario landing**, acentos en texto landing |
| Red 900 | `#CC0000` | Error/destructivo, hover de botones |

> ⚠️ `#DB3B2B` (Red 500) = dashboard · `#E26153` (Red 600) = landing. **No intercambiar.**  
> ⚠️ El logotipo T1 usa `#000000` y `#DB3B2B` — valores de marca, no tokens del sistema.

### Gray

| Shade | Hex | Uso principal |
|---|---|---|
| 50 | `#F8F8F8` | Backgrounds alternativos |
| 100 | `#F2F2F2` | Disabled background |
| 200 | `#E5E5E5` | Borders secundarios |
| 300 | `#D4D4D4` | — |
| 400 | `#A3A3A3` | Texto disabled |
| 500 | `#737373` | — |
| 600 | `#525252` | — |
| 700 | `#404040` | — |
| 800 | `#262626` | — |
| 900 | `#1F2937` | — |

Texto Oxford: `#4C4C4C` (no está en la escala, es token base independiente).  
Borders: `#E7E7E7`. Table header bg: `#F4F8FF`.

### Colores semánticos

| Rol | Hex | Uso |
|---|---|---|
| Success | `#51AF70` | Confirmaciones, pagos, stock disponible |
| Success BG | `#F0FDF4` | Background alertas éxito |
| Warning | `#FF6700` | Acciones que requieren atención |
| Warning BG | `#FFF0E5` | Background alertas warning |
| Caution | `#EDBD55` | Estados pendientes |
| Caution BG | `#FFF4BF` | Background alertas caution |
| Error | `#CC0000` | Errores, eliminaciones, estados críticos |
| Error BG | `#FEF4F4` | Background alertas error |
| Info | `#2180FF` | Links, selección activa, focus state |
| Info BG | `#F0F8FF` | Background informativo, table header |
| Premium/Gold | `#EDBD55` | Badges premium |
| Overlay modal | `rgba(0,0,0,0.6)` | Overlay de modales |

### Otras escalas de color

| Escala | Base (500) | Uso en T1 |
|---|---|---|
| Blue | `#2180FF` | Info, links, focus, selección activa |
| Green | `#51AF70` | Success |
| Orange | `#FF6700` | Warning |
| Yellow | `#EDBD55` | Caution, premium |
| Violet | `#8B5CF6` | IA, funciones avanzadas |
| Turquoise | `#14B8A6` | Reportes, datos |
| Brown/Gold | `#B8860B` | Premium, planes avanzados |

---

## Tipografía

### Familias por contexto

| Familia | Contexto | Rol | Line-height |
|---|---|---|---|
| **Manrope** | Dashboard únicamente | Todo: headings, body, labels | `1.366em` |
| **Sora** | Landing únicamente | Headings H0–H4 | `1.2em` |
| **Inter** | Landing únicamente | Body, botones, labels, H5+ | `1.5em` |

> ❌ Manrope NUNCA en landing. ❌ Sora/Inter NUNCA en dashboard.

### Escala dashboard (Manrope)

**Display (peso fijo):**

| Token | Tamaño | Peso |
|---|---|---|
| display-2xl | 72px | Bold 700 |
| display-xl | 60px | Bold 700 |
| display-lg | 48px | Bold 700 |
| medium-lg | 36px | SemiBold 600 |
| semi-md | 28px | SemiBold 600 |
| title-base | 24px | Bold 700 |

**Contenido (peso variable según jerarquía):**

| Tamaño | Regular 400 | Medium 500 | SemiBold 600 | Bold 700 |
|---|---|---|---|---|
| 20px | Descripciones largas | Table headers, nav | Subtítulos enfáticos | Labels destacados |
| 16px | Cuerpo | Labels de form | Subtítulos de card | Títulos internos |
| 14px | Body, inputs | Labels, placeholders | Botones, tabs activos | Valores destacados |
| 12px | Captions, helper | Badges | Tags enfáticos | Contadores, KPIs |

### Escala landing (Sora + Inter)

**Headings Sora:**

| Nivel | Peso | Mobile → Desktop | Clase Tailwind |
|---|---|---|---|
| H0 Display | Light 300 | 44px → 54px | `font-sora font-light text-[44px] tablet:text-[54px]` |
| H1 Section | Regular 400 | 28px → 40px | `font-sora font-normal text-[28px] tablet:text-[40px]` |
| H2 Subsection | Regular 400 | 26px → 35px | `font-sora font-normal text-[26px] tablet:text-[35px]` |
| H3 Card | Regular 400 | 20px → 24px | `font-sora font-normal text-[20px] tablet:text-[24px]` |
| H4 Small | Regular 400 | 16px → 20px | `font-sora font-normal text-[16px] tablet:text-[20px]` |

> H0 es el ÚNICO nivel con Sora Light 300. H1–H4 todos usan Sora Regular 400.

**H2 estándar de sección (consistencia obligatoria):**

```html
<!-- Fondo claro -->
<h2 class="font-sora text-[32px] font-light text-gray-900 tablet:text-[44px]">
<!-- Fondo oscuro -->
<h2 class="font-sora text-[32px] font-light text-white tablet:text-[44px]">
```
❌ No usar `text-[36px]`, `text-[40px]`, `text-[48px]` en h2 de sección. Solo 32/44px.

**Texto Inter:**

| Nivel | Peso | Tamaño | Clase Tailwind |
|---|---|---|---|
| H5 Mini | Medium 500 | 16px → 20px | `font-inter font-medium text-[16px] tablet:text-[20px]` |
| Body | Regular 400 | 14px → 16px | `font-inter font-normal text-[14px] tablet:text-[16px]` |
| Botones/CTA | SemiBold 600 | 14px | `font-inter font-semibold text-[14px]` |
| Eyebrow | SemiBold 600 | 11px | `font-inter font-semibold text-[11px] uppercase tracking-[0.15em]` |
| Micro/Caption | Regular 400 | 12px | `font-inter font-normal text-[12px]` |

### Colores de texto

| Rol | Hex | Contexto |
|---|---|---|
| Primary (Oxford) | `#4C4C4C` | Ambos — texto principal |
| Dark | `#1F2937` | Ambos — headings, labels enfáticos |
| Secondary | `#6B7280` | Ambos — texto secundario |
| Tertiary | `#9CA3AF` | Ambos — placeholders, eyebrow |
| Inverse | `#FFFFFF` | Ambos — sobre fondos oscuros |
| Accent rojo | `#E26153` | **Solo landing** — acentos en títulos |

> ❌ Rojo en texto dashboard = se interpreta como error. Nunca usar.

---

## Spacing

**Unidad base: 4px.** Escala de múltiplos de 4.

| Alias | Valor | Tailwind | Uso típico |
|---|---|---|---|
| 2xs | 4px | `p-1 / gap-1 / m-1` | Ícono + texto inline, badges |
| xs | 8px | `p-2 / gap-2 / m-2` | Espaciado compacto, chips |
| sm | 12px | `p-3 / gap-3 / m-3` | Botones, cells de tabla |
| md | 16px | `p-4 / gap-4 / m-4` | Estándar de componentes |
| lg | 20px | `p-5 / gap-5 / m-5` | Secciones internas |
| xl | 24px | `p-6 / gap-6 / m-6` | Panels, áreas amplias |
| 2xl | 32px | `p-8 / gap-8 / m-8` | Cards grandes, bloques |
| 3xl | 40px | `p-10 / gap-10 / m-10` | Secciones de página |
| 4xl | 48px | `p-12 / gap-12 / m-12` | Hero, áreas mayores |

**Valores extendidos (section padding landing):**

| Valor | Tailwind |
|---|---|
| 64px | `py-16` |
| 80px | `py-20` |
| 96px | `py-24` |
| 128px | `py-32` |

---

## Layout y breakpoints

### Breakpoints

| Nombre | Viewport | Tailwind |
|---|---|---|
| Mobile | 360px | `mobile:` |
| Tablet | 768px | `tablet:` |
| Desktop | 1280px | `desktop:` |
| Wide *(opcional)* | 1920px | `wide:` |

Mobile-first. Canvas Figma es 1440px pero el breakpoint target es 1280px.

### Contenedores

| Contexto | Contenedor | Clase |
|---|---|---|
| Dashboard | 1600px | `max-w-[1600px]` |
| Landing principal | 1018px | `max-w-[1018px]` |
| Landing estrecho | 721px | `max-w-[721px]` |
| Landing screenshot | 850px | `max-w-[850px]` |

### Dashboard shell

```
┌─────────────────────────────────────┐
│           Header (64px)             │
├──────────┬──────────────────────────┤
│ Sidebar  │      Content Area        │
│ (284px)  │   calc(100% - 284px)     │
└──────────┴──────────────────────────┘
```

| Zona | Valor |
|---|---|
| Header altura | 64px |
| Sidebar expandido | 284px |
| Sidebar colapsado | ~64px (solo íconos) |
| Page padding desktop | 28px |
| Page padding tablet | 24px |
| Page padding mobile | 16px |
| Content gap | 28px |

---

## Elevación — Sombras

### Dashboard (solo 2 sombras)

| Token | Valor CSS | Uso |
|---|---|---|
| `shadow/button` | `0 0 4px 0 rgba(0,0,0,0.14)` | Botones con elevación |
| `shadow/card-selected` | `0 0 4.5px 0.9px #F1B0A9` | Card seleccionada activamente |

> Dropdowns, sidebar y menús: **sin sombra, completamente flat**.

### Landing

| Token | Valor CSS | Uso |
|---|---|---|
| `shadow/landing-card` | `0 0 25px 2px rgba(0,0,0,0.06)` | Cards, features, pricing |
| `shadow/landing-card-hover` | `0 20px 50px rgba(0,0,0,0.08)` | Cards en hover |
| `shadow/landing-badge` | `0 12px 40px rgba(0,0,0,0.1)` | Floating badges en hero |
| `shadow/landing-mockup` | `0 25px 80px -15px rgba(0,0,0,0.18), 0 0 0 1px rgba(0,0,0,0.04)` | Browser mockups |
| `shadow/landing-header` | `0 0 25px 2px rgba(0,0,0,0.06)` | Header on scroll |
| `shadow/landing-screenshot` | `0 0 40px 8px rgba(0,0,0,0.08)` | Screenshots de plataforma |

---

## Elevación — Border radius

### Dashboard

| Valor | Componentes |
|---|---|
| `20px` | Cards grandes, contenedores principales |
| `10px` | Todo lo demás: botones, inputs, selects, badges, cards estándar, modales, bottom sheet |

### Landing

| Componente | Valor |
|---|---|
| Cards | `24px` |
| CTA final card | `32px` |
| Botones | `18px` |
| Icon containers (52×52) | `14px` |
| Tabs / Pills | `rounded-full` |
| Browser mockup | `24px` |
| Contenedores con gradiente | `24px` desktop · `0px` mobile (full-width) |

### Comparativa rápida

| Componente | Dashboard | Landing |
|---|---|---|
| Cards | `10px` / `20px` grandes | `24px` |
| Botones | `10px` | `18px` |
| Inputs | `10px` | `18px` |

---

## Elevación — Z-index

| Token | Valor | Uso |
|---|---|---|
| base | 0 | Contenido normal |
| elevated | 10 | Cards con hover |
| sticky | 20 | Headers sticky, tabs fijos |
| sidebar | 30 | Sidebar dashboard |
| dropdown | 40 | Dropdowns, popovers |
| header | 50 | Header fijo |
| modal | 60 | Modales, dialogs |
| toast | 70 | Notificaciones toast |
| tooltip | 80 | Tooltips |
| overlay | 90 | Overlay de modales |
| max | 100 | Loaders full-screen |

> ❌ Nunca z-index arbitrarios (999, 9999). Usar siempre esta escala.

---

## Nota — Pendientes

- **`RESPONSIVE.md`** — en desarrollo. Para comportamiento de colapso detallado por componente ver `LAYOUT.md`.
- **Dark mode** — el modo oscuro toggleable solo aplica a dashboard. Tokens semánticos y absolutos en `THEMES.md`. Landing/sublanding no tienen modo toggleable, pero sí usan secciones y heroes oscuros autorales (landing: Ecosistema/CTA/footer; sublanding: hero oscuro + ritmo por bloques — ver `LANDING.md` §16).
