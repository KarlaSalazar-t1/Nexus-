# Sistema Cromático — NEXUS V2.0

> Todas las escalas van de 50/100 a 900. El valor **500 es el base**. Variantes claras (100-300) para backgrounds, medias (400-500) para elementos principales, oscuras (700-900) para texto y acentos.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (variables) · **Owner:** Karla Salazar — Lead UX/UI

---

## Filosofía del color

El sistema cromático de T1 se organiza en tres capas: **brand** (identidad), **semántico** (significado) y **extendido** (diferenciación por producto/contexto). Cada color tiene una escala de shades con roles claros — nunca se usa un shade arbitrario.

| Rango de shade | Rol | Ejemplo |
|---|---|---|
| 50–100 | Backgrounds suaves, alertas | `bg-[#FEF4F4]` para alerta de error |
| 200–300 | Borders, estados hover suaves, íconos ligeros | `border-[#F1B0A9]` |
| 400–500 | Elementos principales, botones, íconos | `bg-[#DB3B2B]` botón primario dashboard |
| 600–700 | Hover intenso, variantes oscuras, acentos | `bg-[#CC0000]` hover destructivo |
| 900 | Texto de alto contraste, fondos oscuros | `text-[#1F2937]` |

---

## Colores base

| Token | Nombre | Hex |
|---|---|---|
| `color/brand/base/white` | White | `#FFFFFF` |
| `color/brand/base/oxford` | Oxford | `#4C4C4C` |
| `color/brand/base/black` | Black | `#000000` |

Oxford (`#4C4C4C`) es el color de texto principal en toda la plataforma.

---

## Brand Red — Color primario

El rojo T1 es el color insignia. Se usa en CTAs, elementos de marca y acentos principales.

| Token | Shade | Hex | Uso principal |
|---|---|---|---|
| `color/brand/red/50` | 50 | `#FEF4F4` | Background de alertas de error, hover suave |
| `color/brand/red/100` | 100 | `#F9D2D2` | Borders suaves, backgrounds decorativos |
| `color/brand/red/200` | 200 | `#F1B0A9` | Borders intermedios, íconos ligeros |
| `color/brand/red/300` | 300 | `#E9897E` | Estados intermedios, gráficos secundarios |
| `color/brand/red/400` | 400 | `#E26153` | **Botón primario landing**, acentos en títulos landing |
| `color/brand/red/500` | 500 (base) | `#DB3B2B` | **Botón primario dashboard**, CTAs admin, status bar |
| `color/brand/red/600` | 600 | `#DB362B` | Variante oscura, hover de botón dashboard |
| `color/brand/red/700` | 700 | `#CC0000` | Hover destructivo, alertas de error, eliminaciones |

**Rosa decorativo (landing):**

| Hex | Uso |
|---|---|
| `#E59086` | Degradados hero, CTAs, glow blobs |
| `#F2B5AE` | Degradados secundarios, transición a blanco |

> **Nota:** El rojo primario cambia entre plataformas. Dashboard usa Red 500 (`#DB3B2B`), landing usa Red 400 (`#E26153`). Ver [THEMES.md](./THEMES.md) para todas las variaciones.

---

## Gray Scale

| Token | Shade | Hex | Uso principal |
|---|---|---|---|
| `color/brand/gray/50` | 50 (más claro) | `#F8F8F8` | Background de página, hover suave |
| `color/brand/gray/100` | 100 | `#F3F3F3` | Background disabled, separadores |
| `color/brand/gray/200` | 200 | `#E7E7E7` | Borders, dividers |
| `color/brand/gray/300` | 300 | `#DBDBDB` | Borders secundarios |
| `color/brand/gray/400` | 400 | `#CFCFCF` | Borders suaves, placeholders ligeros |
| `color/brand/gray/500` | 500 (base) | `#C3C3C3` | Borders intermedios |
| `color/brand/gray/600` | 600 | `#9CA3AF` | Texto secundario, placeholders, eyebrow badges |
| `color/brand/gray/700` | 700 | `#6B7280` | Texto medio, descripciones |
| `color/brand/gray/800` | 800 | `#4B5563` | Texto enfático |
| `color/brand/gray/900` | 900 (más oscuro) | `#1F2937` | Headings dark, fondos oscuros de secciones |

---

## Colores semánticos

Los colores semánticos comunican significado. Cada uno tiene un shade principal (500) para el elemento activo y un shade claro (100) para backgrounds de alertas.

### Green — Success

| Token | Shade | Hex | Uso |
|---|---|---|---|
| `color/brand/green/100` | 100 | `#F0FDF4` | Background de alertas de éxito |
| `color/brand/green/300` | 300 | `#6FCF97` | Íconos secundarios, gráficos |
| `color/brand/green/500` | 500 (base) | `#4FC153` | Confirmaciones, pagos exitosos, stock disponible |
| `color/brand/green/700` | 700 | `#16A34A` | Texto de éxito sobre fondo claro, badges |
| `color/brand/green/900` | 900 | `#14532D` | Texto de éxito de alto contraste |

### Orange — Warning

| Token | Shade | Hex | Uso |
|---|---|---|---|
| `color/brand/orange/100` | 100 | `#FFF0E5` | Background de alertas de advertencia |
| `color/brand/orange/300` | 300 | `#FFB380` | Íconos secundarios, progress bars |
| `color/brand/orange/500` | 500 (base) | `#FF6700` | Acciones que requieren atención, alertas |
| `color/brand/orange/700` | 700 | `#CC5200` | Texto de advertencia sobre fondo claro |
| `color/brand/orange/900` | 900 | `#8A3600` | Texto de advertencia de alto contraste |

### Yellow — Caution / Premium

| Token | Shade | Hex | Uso |
|---|---|---|---|
| `color/brand/yellow/100` | 100 | `#FFF4BF` | Background de alertas de precaución |
| `color/brand/yellow/300` | 300 | `#FEF08A` | Badges premium ligeros, highlights |
| `color/brand/yellow/500` | 500 (base) | `#EDBD55` | Estados pendientes, badges premium, planes avanzados |
| `color/brand/yellow/700` | 700 | `#A96A00` | Texto de precaución sobre fondo claro |
| `color/brand/yellow/900` | 900 | `#713F12` | Texto de precaución de alto contraste |

### Blue — Info / Links

| Token | Shade | Hex | Uso |
|---|---|---|---|
| `color/brand/blue/100` | 100 | `#F0F8FF` | Background informativo, table headers |
| `color/brand/blue/300` | 300 | `#7DB3FF` | Íconos secundarios, estados hover |
| `color/brand/blue/500` | 500 (base) | `#2180FF` | Links, selección activa, badges info |
| `color/brand/blue/700` | 700 | `#005EDC` | Link hover |
| `color/brand/blue/900` | 900 | `#0F3D7A` | Link visitado |

---

## Colores extendidos

Usados para diferenciación por producto, categoría o contexto funcional.

### Brown / Gold — Premium

| Token | Shade | Hex | Uso |
|---|---|---|---|
| `color/brand/brown/100` | 100 | `#FAF8F3` | Background premium suave |
| `color/brand/brown/300` | 300 | `#F0E6B8` | Borders premium, íconos ligeros |
| `color/brand/brown/500` | 500 (base) | `#976905` | Badges gold, planes premium |
| `color/brand/brown/700` | 700 | `#6B4A04` | Texto premium sobre fondo claro |
| `color/brand/brown/900` | 900 | `#4A3202` | Texto premium de alto contraste |

### Purple — IA / Avanzado

| Token | Shade | Hex | Uso |
|---|---|---|---|
| `color/brand/purple/100` | 100 | `#FAF7FF` | Background de funciones IA, facturación |
| `color/brand/purple/300` | 300 | `#D0B3FF` | Íconos secundarios, gráficos |
| `color/brand/purple/500` | 500 (base) | `#A064FF` | Badges IA, features avanzadas, facturación |
| `color/brand/purple/700` | 700 | `#6537AE` | Texto purple sobre fondo claro |
| `color/brand/purple/900` | 900 | `#3C1361` | Texto purple de alto contraste |

> **Nota:** En Figma el token es `color/brand/purple`, no `violet`. Usar `purple` como nombre canónico.

### Turquoise — Reportes / Datos

| Token | Shade | Hex | Uso |
|---|---|---|---|
| `color/brand/turquoise/100` | 100 | `#F0FDFA` | Background de reportes, analytics |
| `color/brand/turquoise/300` | 300 | `#ADFFDC` | Gráficos, progress bars |
| `color/brand/turquoise/500` | 500 (base) | `#52F5B0` | Badges de reportes, analytics, retiros |
| `color/brand/turquoise/700` | 700 | `#0F766E` | Texto turquoise sobre fondo claro |
| `color/brand/turquoise/900` | 900 | `#134E4A` | Texto turquoise de alto contraste |

---

## Tabla de colores semánticos por rol

Referencia rápida para implementación:

| Rol | Color | Hex | Uso |
|---|---|---|---|
| **Success** | Green 500 | `#4FC153` | Confirmaciones, pagos exitosos, stock disponible |
| **Success BG** | Green 100 | `#F0FDF4` | Background de alertas de éxito |
| **Warning** | Orange 500 | `#FF6700` | Acciones que requieren atención |
| **Warning BG** | Orange 100 | `#FFF0E5` | Background de alertas de advertencia |
| **Caution** | Yellow 500 | `#EDBD55` | Estados pendientes, precaución |
| **Caution BG** | Yellow 100 | `#FFF4BF` | Background de alertas de precaución |
| **Error / Destructive** | Red 700 | `#CC0000` | Errores, eliminaciones, estados críticos |
| **Error BG** | Red 50 | `#FEF4F4` | Background de alertas de error |
| **Info** | Blue 500 | `#2180FF` | Información, links, selección activa |
| **Info BG** | Blue 100 | `#F0F8FF` | Background informativo, table headers |
| **Disabled Text** | Gray 600 | `#9CA3AF` | Texto deshabilitado |
| **Disabled BG** | Gray 100 | `#F3F3F3` | Background deshabilitado |
| **Overlay** | Black 60% | `rgba(0,0,0,0.6)` | Overlays de modales |
| **Premium/Gold** | Yellow 500 | `#EDBD55` | Badges premium, planes avanzados |

---

## Colores de texto

| Rol | Hex | Token | Uso |
|---|---|---|---|
| **Primary (Oxford)** | `#4C4C4C` | `color/brand/base/oxford` | Texto principal, body copy |
| **Dark** | `#1F2937` | `color/brand/gray/900` | Headings, labels enfáticos |
| **Secondary** | `#6B7280` | `color/brand/gray/700` | Texto secundario, descripciones |
| **Tertiary** | `#9CA3AF` | `color/brand/gray/600` | Placeholders, texto disabled, eyebrow badges |
| **Inverse** | `#FFFFFF` | `color/brand/base/white` | Texto sobre fondos oscuros/primarios |
| **Link** | `#4C4C4C` | `color/brand/base/oxford` | Links — mismo color que texto, sin underline |
| **Link Hover** | `#4C4C4C` | `color/brand/base/oxford` | Links en hover — mismo color |

---

## Overlays por color

Sistema de overlays semitransparentes para backgrounds suaves en cards, badges y contenedores.

| Token | Color base | Hex | Alfa | Uso |
|---|---|---|---|---|
| `color/overlay/green` | Green | `#51AF70` | 10% | Badges de éxito, cards de confirmación |
| `color/overlay/turquoise` | Turquoise | `#52F5B0` | 10% | Cards de reportes, analytics |
| `color/overlay/blue` | Blue | `#2180FF` | 10% | Cards de info, selección |
| `color/overlay/violet` | Violet | `#AD7CFA` | 10% | Cards de IA, facturación |
| `color/overlay/yellow` | Yellow | `#EDBD55` | 10% | Cards de precaución, premium |
| `color/overlay/orange` | Orange | `#FF6700` | 10% | Cards de advertencia |
| `color/overlay/red` | Red | `#FE4D61` | 10% | Cards de error, hover glow |
| `color/overlay/black` | Black | `#000000` | 10% | Sombras suaves, separadores |
| `color/overlay/light-black` | Black | `#000000` | 25% | Overlays más intensos, modales ligeros |

---

## Opacidades funcionales (landing)

| Uso | Valor | Contexto |
|---|---|---|
| **Modal overlay** | `rgba(0,0,0,0.6)` | Overlay detrás de modales |
| **Glow blob rojo** | `rgba(226,97,83,0.08)` | Hover glow en cards landing |
| **Card glass (dark)** | `rgba(255,255,255,0.04)` | Cards sobre fondo oscuro |
| **Border glass (dark)** | `rgba(255,255,255,0.08)` | Borders sobre fondo oscuro |
| **Card activa (dark)** | `rgba(226,97,83,0.06)` | Card seleccionada en sección oscura |
| **Border activa (dark)** | `rgba(226,97,83,0.15)` | Border de card activa oscura |

---

## Degradados

### Degradados de landing

| Nombre | Valor CSS | Uso |
|---|---|---|
| **Hero (3 pasos)** | `linear-gradient(to bottom, #E59086, #F2B5AE, #FFFFFF)` | Hero section |
| **CTA** | `linear-gradient(to bottom-right, #E59086, #F2B5AE)` | CTA cards, banners |
| **Radial** | `radial-gradient(ellipse at top, #E59086, #FFFFFF)` | Fondos decorativos |
| **Contenedor rosa** | `linear-gradient(to bottom, #FFFAFA, #F2B5AE)` | Secciones alternativas |
| **Gradient container** | `linear-gradient(135deg, #FFFAFA 0%, #FFFFFF 40%, #F0F8FF 70%, #FFF5F3 100%)` | Contenedores de plataforma |

### Fondos de sección (landing)

Landing principal: alternar para crear ritmo visual. Sublanding: agrupar en bloques (ver `LANDING.md` §16).

| Color | Hex | Uso |
|---|---|---|
| Blanco | `#FFFFFF` | Mayoría de secciones |
| Rosa muy suave | `#FFFAFA` | Alternativo |
| Degradado rosa | `#E59086 → #FFFFFF` | Hero section |
| Negro | `#000000` | Footer |
| Gris 900 | `#1F2937` | Secciones oscuras (ecosistema, etc.) |
| Superficie oscura | `#0F1419` / `#0f1219` | Hero oscuro de sublanding y secciones oscuras profundas |

### Fondos de sección (dashboard)

| Color | Hex | Uso |
|---|---|---|
| Blanco | `#FFFFFF` | **Fondo por defecto** — siempre blanco |
| Gray 50 | `#F8F8F8` | Uso mínimo — solo en bloques puntuales que necesiten diferenciarse |
| Gray 100 | `#F3F3F3` | Uso mínimo — separadores o áreas secundarias excepcionales |

> **Regla:** El fondo del dashboard es blanco. Gray 50/100 se usa ocasionalmente en bloques específicos, pero se busca mantenerlo al mínimo.

---

## Configuración Tailwind CSS

Extensión obligatoria para todos los proyectos T1:

```js
// tailwind.config.js (o dentro de globals.css con @theme inline en Tailwind v4)
module.exports = {
  theme: {
    extend: {
      colors: {
        brand: {
          red: {
            50: '#FEF4F4',
            100: '#F9D2D2',
            200: '#F1B0A9',
            300: '#E9897E',
            400: '#E26153',
            500: '#DB3B2B',
            600: '#DB362B',
            700: '#CC0000',
          },
        },
        blue: {
          100: '#F0F8FF',
          300: '#7DB3FF',
          500: '#2180FF',
          700: '#005EDC',
          900: '#0F3D7A',
        },
        green: {
          100: '#F0FDF4',
          300: '#6FCF97',
          500: '#4FC153',
          700: '#16A34A',
          900: '#14532D',
        },
        orange: {
          100: '#FFF0E5',
          300: '#FFB380',
          500: '#FF6700',
          700: '#CC5200',
          900: '#8A3600',
        },
        yellow: {
          100: '#FFF4BF',
          300: '#FEF08A',
          500: '#EDBD55',
          700: '#A96A00',
          900: '#713F12',
        },
        gray: {
          50: '#F8F8F8',
          100: '#F3F3F3',
          200: '#E7E7E7',
          300: '#DBDBDB',
          400: '#CFCFCF',
          500: '#C3C3C3',
          600: '#9CA3AF',
          700: '#6B7280',
          800: '#4B5563',
          900: '#1F2937',
        },
        brown: {
          100: '#FAF8F3',
          300: '#F0E6B8',
          500: '#976905',
          700: '#6B4A04',
          900: '#4A3202',
        },
        purple: {
          100: '#FAF7FF',
          300: '#D0B3FF',
          500: '#A064FF',
          700: '#6537AE',
          900: '#3C1361',
        },
        turquoise: {
          100: '#F0FDFA',
          300: '#ADFFDC',
          500: '#52F5B0',
          700: '#0F766E',
          900: '#134E4A',
        },
        oxford: '#4C4C4C',
      },
    },
  },
};
```

---

## Anti-patrones

- ❌ Usar colores del palette default de Tailwind (indigo-500, blue-600, etc.) en lugar de los tokens NEXUS.
- ❌ Inventar shades intermedios que no existen en la escala (ej: Red 350, Gray 550).
- ❌ Usar Red 500 (`#DB3B2B`) como primario en landing — es Red 400 (`#E26153`).
- ❌ Usar Red 400 (`#E26153`) como primario en dashboard — es Red 500 (`#DB3B2B`).
- ❌ Usar colores semánticos para decoración (verde para un borde decorativo, azul como background de card).
- ❌ Hardcodear hex en componentes sin referenciar el token correspondiente.
- ❌ Usar `text-gray-900` sobre fondos oscuros — usar `text-white` o `text-gray-600`.
- ❌ Usar `violet` como nombre de token — el nombre canónico es `purple`.

---

## Referencias

- [THEMES.md](./THEMES.md) — Variaciones de color por plataforma (landing vs dashboard) y dark mode
- [TYPOGRAPHY.md](./TYPOGRAPHY.md) — Colores de texto por rol tipográfico
- [PRINCIPLES.md](./PRINCIPLES.md) — Principio de Consistencia (uso correcto de tokens)
- [../platforms/LANDING.md](../platforms/LANDING.md) — Restricciones de color específicas de landing
- [../platforms/DASHBOARD.md](../platforms/DASHBOARD.md) — Restricciones de color específicas de dashboard
