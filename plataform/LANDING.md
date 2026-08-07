# LANDING.md — Contexto de plataforma: Landing Pages Públicas

> Este archivo documenta los tokens, reglas y componentes exclusivos de **landing pages públicas** del ecosistema T1.  
> **No aplica** en dashboard, admin ni backoffice.  
> Para el contexto opuesto, ver [`platforms/DASHBOARD.md`](./DASHBOARD.md).

---

## Diferencias clave vs Dashboard

| Propiedad | Landing | Dashboard |
|---|---|---|
| Tipografía headings | Sora Light 300 / Regular 400 | Manrope SemiBold / Bold |
| Tipografía cuerpo | Inter Regular / Medium | Manrope Regular |
| Contenedor principal | `1018px` | `1600px` |
| Border radius cards | `24px` | `10px`–`20px` |
| Border radius botones | `18px` | `8px` |
| Altura botones | `45px` | variable |
| Color botón primario | `#E26153` (Red 600) | `#DB3B2B` (Red 500) |
| Sombra cards | `0 0 25px 2px rgba(0,0,0,0.06)` | `0 0 5px 1px rgba(0,0,0,0.1)` |
| Fondo header | `rgba(255,255,255,0.9)` + blur (glass) | Blanco sólido |
| Fondo footer | `#000000` | No aplica |

---

## 1. Tipografía

Landing usa **Sora + Inter**. Manrope está **prohibida** en este contexto.

### Escala completa

| Nivel | Familia | Peso | Mobile | Desktop |
|---|---|---|---|---|
| **H0** — Display | Sora | Light 300 | `44px` | `54px` |
| **H1** — Section Title | Sora | Regular 400 | `28px` | `40px` |
| **H2** — Subsection | Sora | Regular 400 | `26px` | `35px` |
| **H3** — Card Heading | Sora | Regular 400 | `20px` | `24px` |
| **H4** — Small Heading | Sora | Regular 400 | `16px` | `20px` |
| **H5** — Mini Heading | Inter | Medium 500 | `16px` | `20px` |
| **Body** | Inter | Regular 400 | `14px` | `16px` |
| **Body Light** | Inter | Light 300 | `14px` | `14px` |
| **Nav / Tabs** | Inter | Medium 500 | `14px` | `14px` |
| **CTA / Botones** | Inter | SemiBold 600 | `14px` | `14px` |
| **Links** | Inter | SemiBold 600 | Oxford `#4C4C4C` · Sin underline · Hover: Red 600 | — |
| **Eyebrow** | Inter | SemiBold 600 | `11px` · uppercase · `tracking-[0.15em]` | — |
| **Micro / Caption** | Inter | Regular 400 | `12px` | `12px` |

> **H0 es el ÚNICO nivel Sora Light 300.** H1–H4 usan Sora Regular 400. H5 en adelante: Inter.

### Pesos permitidos

| Familia | Pesos válidos | Prohibidos |
|---|---|---|
| **Sora** | Light 300 (solo H0), Regular 400 (H1–H4) | SemiBold 600, Bold 700 en headings |
| **Inter** | Light 300, Regular 400, Medium 500, SemiBold 600 | Bold 700, ExtraBold 800 |

### Patrones de código frecuentes

**Título con acento rojo**
```html
<h2 class="font-sora font-normal text-gray-900">
  Texto normal <span class="text-[#E26153]">texto rojo</span>
</h2>
```
> El `<span>` hereda el peso del padre. Si H0 es Light, el span es Light. **Nunca cambiar el peso del acento.**

**Eyebrow badge**
```html
<p class="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">
  Texto del eyebrow
</p>
```

**Link con chevron**
```html
<a class="font-inter text-sm font-semibold text-oxford hover:text-[#E26153] transition-colors">
  Probar gratis <ChevronRight class="h-4 w-4 inline" />
</a>
```

### Anti-patrones tipográficos

- ❌ Sora Bold / SemiBold en headings
- ❌ Peso del acento rojo diferente al del título padre
- ❌ Inter Bold 700 o pesos fuera de 300/400/500/600
- ❌ Manrope en cualquier elemento de landing
- ❌ Underline en links en estado normal
- ❌ Texto en rojo (`#E26153`) en estados de error — el rojo de acento es exclusivo de landing; en dashboard puede confundirse con error
- ❌ Texto blanco en el hero — el fondo es claro, usar negro `#000000` tanto en headings como en descripciones

---

## 2. Contenedores

| Contenedor | Ancho máximo | Clase Tailwind | Uso |
|---|---|---|---|
| Principal | `1018px` | `max-w-[1018px]` | Todas las secciones |
| Estrecho | `721px` | `max-w-[721px]` | Hero text, CTA final, FAQ |
| Screenshot | `850px` | `max-w-[850px]` | Browser mockups |

Siempre centrados con `mx-auto`.

> ❌ **Nunca** usar `max-w-[1600px]` en landing. Ese es el contenedor de dashboard.

---

## 3. Botones

| Propiedad | Primario | Secundario |
|---|---|---|
| Background | `#E26153` | `#FFFFFF` |
| Texto | `#FFFFFF` | `#4C4C4C` (Oxford) |
| Border | ninguno | `1px solid #D9D9D9` |
| Border Radius | `18px` | `18px` |
| Altura | `45px` | `45px` |
| Fuente | Inter SemiBold 600 | Inter SemiBold 600 |
| Hover bg | `#DB3B2B` (Red 500) | `#F8F8F8` (Gray 50) |

**Botón sobre fondo oscuro o degradado:** No usar variant `secondary`. Usar `<a>` inline con borde semitransparente:
```html
<a class="border border-white/50 text-white bg-transparent hover:bg-white/10 rounded-[18px] h-[45px] ...">
  Texto
</a>
```

---

## 4. Cards

| Propiedad | Valor |
|---|---|
| Border Radius | `24px` |
| Box Shadow | `0px 0px 25px 2px rgba(0, 0, 0, 0.06)` |
| Padding | `32px` (`p-8`) |
| Hover transform | `translateY(-4px)` |
| Hover shadow | `0 20px 50px rgba(0,0,0,0.08)` |

---

## 5. Sombras del sistema

| Elemento | Valor CSS |
|---|---|
| Card default | `0 0 25px 2px rgba(0,0,0,0.06)` |
| Card hover | `0 20px 50px rgba(0,0,0,0.08)` |
| Floating badge | `0 12px 40px rgba(0,0,0,0.1)` |
| Browser mockup | `0 25px 80px -15px rgba(0,0,0,0.18), 0 0 0 1px rgba(0,0,0,0.04)` |
| Header on scroll | `0 0 25px 2px rgba(0,0,0,0.06)` |

---

## 6. Degradados y fondos

### Degradados principales

| Tipo | Valor CSS | Uso |
|---|---|---|
| Hero linear | `linear-gradient(to bottom, #FDF0EF, #F2B5AE, #FFFFFF)` | Hero — inicia casi blanco para no chocar con el header glass |
| Hero radial | `radial-gradient(ellipse at top center, #FDF0EF 0%, #F2B5AE 50%, #FFFFFF 100%)` | Alternativa radial para hero |
| CTA | `linear-gradient(to bottom-right, #E59086, #F2B5AE)` | CTA cards, banners |
| Radial decorativo | `radial-gradient(ellipse at top, #E59086, #FFFFFF)` | Fondos decorativos secundarios |

### Texto en el hero (landing principal)

En el **landing principal** el hero es claro (degradado rosa) y sigue las mismas reglas de color que el resto del landing. No hay variantes especiales por estar en degradado.

| Elemento | Color | Hex |
|---|---|---|
| Heading (H0 / H1) | Negro | `#000000` |
| Acento en heading | Red 600 | `#E26153` |
| Subtítulo / descripción | Negro | `#000000` |
| Eyebrow | Gray 400 | `#A3A3A3` |

> ❌ **Nunca usar texto blanco en el hero claro del landing principal.** El fondo es claro (rosa pastel → blanco) — el contraste sería insuficiente.  
> ❌ **El acento rojo (`#E26153`) en el título no debe caer sobre la zona más saturada del degradado.** El degradado inicia en `#FDF0EF` (casi blanco) precisamente para garantizar legibilidad del texto negro y del acento rojo en la parte superior, donde está el heading.

> ℹ️ **En sublandings el hero arranca oscuro** (texto blanco), no claro. Esa es una variante intencional, no una violación de la regla anterior. Ver §16 — Variante Sublanding.

### Fondos de sección

| Color | Hex | Uso |
|---|---|---|
| Blanco | `#FFFFFF` | Mayoría de secciones |
| Rosa suave | `#FFFAFA` | Alternativo |
| Degradado rosa | `#E59086 → #FFFFFF` | Hero |
| Negro | `#000000` | Footer |
| Gris 900 | `#1F2937` / `#0f1219` | Secciones oscuras |

**Landing principal:** alternar fondos entre secciones para mantener ritmo visual. No repetir el mismo fondo en secciones consecutivas.

**Sublanding:** el cambio de fondo ocurre por **bloques de 2–3 secciones**, no sección a sección, y el hero arranca oscuro. Ver §16 — Variante Sublanding.

### Contenedor con degradado (desktop vs mobile)

```html
<!-- Desktop: card con rounded -->
<div class="mx-auto max-w-[1018px] px-6">
  <div class="overflow-hidden rounded-[24px]"
       style="background: linear-gradient(to bottom, #FFFAFA, #F2B5AE);">
    <div class="p-10 tablet:p-16"><!-- contenido --></div>
  </div>
</div>

<!-- Mobile: full-width, sin radius -->
<div class="overflow-hidden rounded-none tablet:mx-auto tablet:max-w-[1018px] tablet:rounded-[24px] tablet:px-6"
     style="background: linear-gradient(to bottom, #FFFAFA, #F2B5AE);">
  <div class="px-5 py-10 tablet:p-16"><!-- contenido --></div>
</div>
```

> En mobile (`< 768px`): `rounded-none`, full-width, sin márgenes laterales. En desktop: `rounded-[24px]` con padding y contenedor centrado.

---

## 7. Header / Navegación

### Desktop

| Propiedad | Valor |
|---|---|
| Posición | `fixed`, `z-50` |
| Altura | `70px` |
| Background | `rgba(255,255,255,0.9)` — **Semitransparente, nunca blanco sólido** |
| Blur | `backdrop-blur-md` (12px) |
| Contenedor | `max-w-[1018px]` |
| Logo | `h-[42px]` |
| Links nav | Inter Medium 500, 14px, Oxford |
| "Iniciar sesión" | Inter SemiBold 600, Oxford — `<a>` link, **nunca botón** |
| "Comenzar" / "Ir a Admin" | Único `<Button>` del header — cambia a **"Ir a Admin"** cuando el usuario está autenticado |
| Shadow on scroll | `shadow-[0px_0px_25px_2px_rgba(0,0,0,0.06)]` |

```
[Logo 42px]    [Ecosistema] [¿Qué es T1?] [Contacto] [Iniciar sesión] [Comenzar →]
```

### Mobile

| Propiedad | Valor |
|---|---|
| Altura barra | `60px` |
| Background | `rgba(255,255,255,0.92)` + `backdrop-blur` |
| Barra visible | Solo logo + icono hamburguesa. Sin CTA en barra. |
| Logo | `h-[36px]` |
| Panel desplegado | Full-width, links verticales, Inter Medium 16px |
| CTA en panel | Botón "Comenzar" full-width al final del menú |

```
Barra: [Logo 36px]                    [☰]

Panel desplegado:
  [Ecosistema         ]
  [¿Qué es T1?        ]
  [Contacto           ]
  [Iniciar sesión     ]
  [═══ Comenzar → ═══]
```

> El botón CTA **no aparece en la barra**. Solo en el panel expandido como elemento full-width.

---

## 8. Footer

### Desktop

| Propiedad | Valor |
|---|---|
| Background | `#000000` |
| Contenedor | `max-w-[1018px]` |
| Estructura | Logo + redes sociales · 2 o 3 columnas de links (según el producto) |
| Títulos columna | Inter SemiBold 11px, uppercase, `tracking-wider`, blanco |
| Links | Inter Regular 13px, `#9CA3AF` → hover: `white` |
| Fila inferior | País+idioma · Términos · Privacidad · © Copyright |
| WhatsApp FAB | `#25D366`, `h-14 w-14`, `fixed bottom-6 right-6 z-50` |

> El número de columnas de links varía por producto. Un producto con más secciones puede necesitar 3 columnas; uno más simple, 2. Definir según el mapa de contenido de cada landing.

```
[Logo T1]                    | Soluciones        | T1
Descripción breve            | T1tienda          | ¿Qué es T1?
[🔗] [🔗] [🔗]              | T1pagos           | Contacto
                              | T1envíos          | Blog
                              | T1score           | Soporte
                              | T1marketing       |
─────────────────────────────────────────────────────────
[🇲🇽 México (Español)]    [Términos | Privacidad]    [© 2026 T1]
```

### Mobile

| Propiedad | Valor |
|---|---|
| Layout | Stack vertical (1 columna) |
| Orden | Logo → Descripción → Redes → Soluciones → T1 → Legal |
| Links | Inter Regular 14px (mayor tap target) |
| Padding | `40px 20px` |

> Iconos de redes: contenedor `32×32px`, `rounded-lg`, `bg-white/8`.

---

## 9. Elementos decorativos

Cada sección debe incluir al menos un elemento decorativo. Son parte del lenguaje visual de landing, no opcionales.

### Glow Blobs

| Elemento | Tamaño | Color | Blur |
|---|---|---|---|
| Rosa principal | `400px–500px` | `rgba(229,144,134,0.2)` | `blur-[120px]` |
| Rojo suave | `250px–350px` | `rgba(249,210,210,0.35)` | `blur-[80px]` |
| Sobre fondo oscuro | `400px–600px` | `rgba(226,97,83,0.06)` | `blur-[100px]` |

**Regla de estructura:** Padre: `relative overflow-hidden`. Blobs: `absolute pointer-events-none z-0 animate-pulse-soft`. Contenido: `relative z-10`.

```html
<section class="relative overflow-hidden py-24">
  <div class="pointer-events-none absolute -top-24 -right-24 h-[400px] w-[400px] animate-pulse-soft rounded-full bg-[#E59086]/20 blur-[120px]"></div>
  <div class="relative z-10 mx-auto max-w-[1018px] px-6"><!-- contenido --></div>
</section>
```

### Dot Pattern

Para secciones con fondo `#FFFAFA`:
```html
<div class="pointer-events-none absolute inset-0 z-0 opacity-40"
     style="background-image: radial-gradient(circle, #D4D4D4 0.8px, transparent 0.8px); background-size: 24px 24px;"></div>
```

### Secciones oscuras — Mesh Gradient

Nunca `bg-gray-900` plano en secciones oscuras. Siempre con mesh gradient:
```css
background:
  radial-gradient(ellipse at 25% 35%, rgba(226,97,83,0.07), transparent 50%),
  radial-gradient(ellipse at 75% 80%, rgba(33,128,255,0.04), transparent 50%),
  radial-gradient(ellipse at 50% 50%, rgba(226,97,83,0.03), transparent 60%),
  #0f1219;
```
Agregar overlay `.bg-noise` al 3%.

### Decoración obligatoria por sección

| Sección | Elementos |
|---|---|
| **Hero** | Patrón de referencia: 2 glow blobs + browser mockup + 2–3 floating badges + eyebrow badge glass. Sustituible por video, ilustración u otro elemento visual según el producto. |
| Beneficios | 1 glow blob lateral + íconos en contenedor de color + hover glow en cards |
| Plataforma | Dot pattern + browser mockup + glow radial + tabs con shadow |
| Métricas | Glow blob centrado + hover glow en stat cards |
| Social proof | Marquee con fades laterales + logos grayscale |
| **Ecosistema** | Patrón de referencia: fondo oscuro mesh + glow superior + cards glass + card activa con border rojo. La configuración puede variar según el producto. |
| FAQ | Accordion animado + hover rojo |
| CTA Final | `bg-gray-900` + `rounded-[32px]` + glow rojo interno |

---

## 10. Animaciones

```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-12px); }
}
@keyframes float-slow {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(-8px); }
}
@keyframes float-reverse {
  0%, 100% { transform: translateY(0px); }
  50%       { transform: translateY(10px); }
}
@keyframes pulse-soft {
  0%, 100% { opacity: 0.35; transform: scale(1); }
  50%       { opacity: 0.55; transform: scale(1.05); }
}
@keyframes marquee {
  0%   { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
```

### Scroll Animations (Intersection Observer)

```html
<div data-animate>contenido</div>
```
```css
[data-animate] {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.7s cubic-bezier(0.16, 1, 0.3, 1);
}
[data-animate].visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Patrones de interacción

| Patrón | Implementación |
|---|---|
| Tabs / Pills activos | `rounded-full`, color `#E26153`, texto blanco |
| Fade transition | `transition-opacity duration-500` + `absolute inset-0 opacity-0` |
| Hover en cards | `-translate-y-1.5` + shadow hover + `duration-500` |
| Accordion FAQ | `grid-rows-[1fr]` / `grid-rows-[0fr]` + `transition-all duration-300` |
| Stagger animation | `transitionDelay: ${i * 80}ms` |
| Auto-rotación carrusel | `setInterval` + pause on hover |

---

## 11. Componentes de landing

### Browser Mockup

Screenshots nunca van planas. Siempre en browser mockup:

```html
<div class="overflow-hidden rounded-[16px] border border-gray-200/50 bg-white"
     style="box-shadow: 0 25px 80px -15px rgba(0,0,0,0.18), 0 0 0 1px rgba(0,0,0,0.04);">
  <div class="flex items-center gap-2.5 border-b border-gray-200 bg-[#F6F6F8] px-4 py-3">
    <div class="flex gap-1.5">
      <div class="h-[10px] w-[10px] rounded-full bg-[#FF5F57]"></div>
      <div class="h-[10px] w-[10px] rounded-full bg-[#FFBD2E]"></div>
      <div class="h-[10px] w-[10px] rounded-full bg-[#27C93F]"></div>
    </div>
    <div class="ml-2 flex-1 rounded-md border border-gray-200 bg-white px-3 py-1.5 text-[11px] text-gray-400">
      app.t1pagos.com/dashboard
    </div>
  </div>
  <div class="bg-gradient-to-br from-[#fafafa] to-[#f0f0f0]">
    <img src="screenshot.png" class="w-full" alt="..." />
  </div>
</div>
```

Siempre colocar glow radial detrás del browser mockup.

### Floating Badges

Máximo 3 por sección. En mobile ocultar 1–2. Cada badge con animación diferente (`float`, `float-slow`, `float-reverse`).

```html
<div class="absolute [posición] z-20 animate-float rounded-2xl border border-white/60 bg-white/90 p-3 px-4 shadow-[0_12px_40px_rgba(0,0,0,0.1)] backdrop-blur-xl">
  <div class="flex items-center gap-3">
    <div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-[10px] bg-green-100">
      <CheckIcon class="h-[18px] w-[18px] text-green-500" />
    </div>
    <div>
      <p class="font-sora text-[12px] font-semibold text-gray-900">Pago aprobado</p>
      <p class="font-inter text-[11px] text-gray-500">$1,250.00 MXN</p>
    </div>
  </div>
</div>
```

### Glassmorphism

| Componente | Clases Tailwind |
|---|---|
| Badge flotante | `bg-white/90 backdrop-blur-xl border border-white/60 shadow-[0_12px_40px_rgba(0,0,0,0.1)] rounded-2xl` |
| Eyebrow badge | `bg-white/75 backdrop-blur-lg border border-white/50 rounded-full` |
| Card glass (dark) | `bg-white/[0.04] backdrop-blur-sm border border-white/[0.08] rounded-[24px]` |
| Header on scroll | `bg-white/90 backdrop-blur-md` |

> Solo usar glassmorphism sobre contenido visual (screenshot, degradado, sección oscura). Nunca sobre fondo blanco plano.

### Íconos en cards de beneficios

Siempre dentro de contenedor de color. Nunca sueltos.

```html
<div class="flex h-[52px] w-[52px] items-center justify-center rounded-[14px] bg-[#FEF4F4]">
  <Icon class="h-6 w-6 text-[#E26153]" />
</div>
```

| Variante | Fondo | Icono |
|---|---|---|
| Rojo | `#FEF4F4` (Red 50) | `#E26153` (Red 600) |
| Gris | `#F8F8F8` (Gray 50) | `#4C4C4C` (Oxford) |

> ❌ **Prohibidos:** Azul, Verde, Violeta, Naranja, Turquesa o cualquier otro color fuera de estas dos variantes.

### Hover Glow en cards

```html
<div class="group relative overflow-hidden rounded-[24px] bg-white p-8 shadow-[0_0_25px_2px_rgba(0,0,0,0.06)] transition-all duration-500 hover:-translate-y-1.5 hover:shadow-[0_20px_50px_rgba(0,0,0,0.08)]">
  <div class="pointer-events-none absolute -top-10 -right-10 h-24 w-24 rounded-full opacity-0 blur-[30px] transition-opacity duration-500 group-hover:opacity-100"
       style="background: rgba(226,97,83,0.08);"></div>
  <div class="relative z-10"><!-- contenido --></div>
</div>
```

### Gradient Border Cards

Para pricing destacada o card activa:
```html
<div class="rounded-[24px] bg-gradient-to-br from-[#E26153]/25 via-transparent to-[#E59086]/15 p-[1.5px]">
  <div class="relative overflow-hidden rounded-[23px] bg-white p-8">
    <div class="pointer-events-none absolute -top-8 -right-8 h-24 w-24 rounded-full bg-[#E26153]/5 blur-[30px]"></div>
    <div class="relative z-10"><!-- contenido --></div>
  </div>
</div>
```

### Cards sobre fondo oscuro

| Estado | Clases |
|---|---|
| Normal | `bg-white/[0.04] border border-white/[0.08] backdrop-blur-sm hover:bg-white/[0.08] hover:border-white/[0.16]` |
| Activa | `bg-[#E26153]/[0.06] border-[#E26153]/40 backdrop-blur-sm` |

### Marquee de logos

Logos en `grayscale opacity-40`. Hover: `grayscale-0 opacity-80`. Fades laterales. Duplicar array para loop. Velocidad: `30s` para 6–8 logos.

### Phone Mockup

Para features visibles en mobile por el usuario final (checkout, links de pago, tracking):
```html
<div class="mx-auto w-[280px]">
  <div class="overflow-hidden rounded-[32px] border-[6px] border-gray-800 bg-white shadow-[0_20px_60px_rgba(0,0,0,0.15)]">
    <!-- Status bar + Notch + Contenido + Bottom bar -->
  </div>
</div>
```

> Usar **browser mockup** para screenshots de dashboard. Usar **phone mockup** para features de usuario final en mobile.

### CTA Final (Dark variant)

`bg-gray-900`, `rounded-[32px]`, glow interno: `bg-[#E26153]/10 blur-[80px] animate-pulse-soft`.

---

## 12. Estructura de sección estándar

```tsx
"use client"; // solo si tiene interactividad
import SectionWrapper from "./ui/SectionWrapper";
import { DATOS } from "@/lib/constants";

export default function T1NombreSeccion() {
  return (
    <SectionWrapper id="seccion-id" className="py-20 tablet:py-28">
      {/* Elementos decorativos (absolute, z-0) */}
      <div className="pointer-events-none absolute -top-24 -right-24 h-[400px] w-[400px] animate-pulse-soft rounded-full bg-[#E59086]/20 blur-[120px]" />

      <div className="relative z-10">
        <div data-animate>
          <p className="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">
            Eyebrow
          </p>
          <h2 className="font-sora text-[32px] font-normal text-gray-900 tablet:text-[44px]">
            Texto <span className="text-[#E26153]">acento</span>
          </h2>
        </div>
        <div data-animate>
          {/* contenido */}
        </div>
      </div>
    </SectionWrapper>
  );
}
```

**Naming:** `T1` + PascalCase — ej. `T1Hero`, `T1Pricing`, `T1ProofWall`.  
**Contenido:** Todo texto va en `src/lib/constants.ts`. Nunca hardcodear contenido en el componente.

---

## 13. Secuencia típica de secciones

| # | Sección | Notas |
|---|---|---|
| 1 | Header | Nav fijo, glass effect |
| 2 | Hero | Degradado rosa (inicia claro `#FDF0EF`), CTAs · El elemento visual (screenshot, video, ilustración) varía por producto |
| 3 | Beneficios | Grid cards con íconos de color |
| 4 | Plataforma | Tabs con screenshots + fade |
| 5 | Métricas | Stat cards con datos duros |
| 6 | Social proof | Marquee de logos |
| 7 | Pasos | Pasos en línea horizontal |
| 8 | Pricing | Cards de precios o formas de pago |
| 9 | Ecosistema | Fondo oscuro, cards de otros productos T1 |
| 10 | FAQ | Accordion, contenedor `721px` |
| 11 | CTA Final | Card con degradado rosa, 2 botones |
| 12 | Footer | Fondo negro · Logo + redes + 2 o 3 columnas de links según el producto |

> No hay una secuencia obligatoria fija. Lo que sí es obligatorio: variedad de layouts entre secciones consecutivas y al menos 2 secciones con fondo oscuro.
>
> Esta secuencia describe el **landing principal**. Para páginas de producto individuales (sublandings), ver §16 — Variante Sublanding, donde el hero arranca oscuro y los fondos se agrupan en bloques.

---

## 14. Anti-patrones de layout

| Anti-patrón | Alternativa |
|---|---|
| Mismo layout repetido en 3+ secciones | Alternar: 2 col → 3 col → bento → dark → carrusel |
| Hero 50/50 split genérico | Dashboard inmersivo + floating badges + glows |
| Accordion FAQ simple | 2 col: preguntas izq + panel respuesta der |
| Pricing table simétrica | Precio como statement gigante + planes asimétricos |
| Logo wall estático centrado | Marquee animado con fades laterales |
| Badge pill centrado + título centrado | Título left-aligned con eyebrow text (no pill) |
| Fondo plano en sección oscura | Mesh gradient + noise obligatorio |

> La regla no es "nunca uses X layout". Es **nunca repitas el mismo layout en secciones consecutivas**. Una landing que alterna Hero 2col → Grid 3col → Bento → Dark → Carrusel se siente dinámica.

---

## 15. Checklist de QA — Pre-deployment

**Tipografía**
- [ ] H0: Sora Light 300, `44px` mobile → `54px` desktop
- [ ] H1–H4: Sora Regular 400, tamaños correctos por nivel
- [ ] H5 en adelante: Inter (nunca Sora)
- [ ] Body: Inter Regular, `14px` → `16px`
- [ ] Links: Inter SemiBold, Oxford, sin underline
- [ ] Inter solo usa pesos 300/400/500/600
- [ ] Acento rojo hereda peso del título padre
- [ ] Eyebrow con formato estándar: 11px · semibold · uppercase · tracking

**Colores y sombras**
- [ ] Rojo primario es `#E26153`, no `#DB3B2B`
- [ ] Hero (landing principal): texto heading y descripción en negro `#000000` — nunca blanco
- [ ] Hero (sublanding): fondo oscuro `#0F1419`, heading en blanco, acento rojo `#E26153` solo en texto grande
- [ ] Hero: acento rojo posicionado sobre la zona más clara del degradado (inicio `#FDF0EF`)
- [ ] Texto sobre fondos oscuros: `text-white` o `text-gray-400`
- [ ] Íconos solo en variantes rojo o gris (sin azul, verde, etc.)
- [ ] Sombra card: `0 0 25px 2px rgba(0,0,0,0.06)`
- [ ] Botón secundario: fondo blanco sólido (no transparente)

**Layout**
- [ ] Contenedor: `max-w-[1018px]` (nunca `1600px`)
- [ ] Layouts visualmente distintos entre secciones consecutivas
- [ ] Al menos 2 secciones con fondo oscuro
- [ ] Títulos left-aligned
- [ ] Padding de sección: `py-20 tablet:py-28` como mínimo

**Header**
- [ ] `bg-white/90 backdrop-blur-md` (nunca blanco sólido)
- [ ] `fixed`, altura `70px` desktop / `60px` mobile
- [ ] Mobile: solo logo + hamburguesa en barra
- [ ] CTA "Comenzar" solo dentro del panel expandido en mobile

**Footer**
- [ ] Fondo `#000000`
- [ ] 3 columnas desktop, stack vertical mobile
- [ ] Links mobile: `14px` para tap targets

**Interactividad**
- [ ] Carruseles: altura fija + transición solo opacidad
- [ ] `data-animate` en todos los bloques de contenido
- [ ] Auto-rotación con pause on hover
- [ ] `useCountUp` con IntersectionObserver para números animados

**Performance**
- [ ] `npm run build` sin errores TypeScript
- [ ] Imágenes con `<Image>` de Next.js
- [ ] Logos como SVG inline
- [ ] Sin imports huérfanos

---

## 16. Variante Sublanding

Las **sublandings** son páginas de producto individuales del ecosistema (T1tienda, T1pagos, T1envíos, T1score, T1marketing). Comparten el 100% del ADN del landing principal — misma tipografía (Sora + Inter), mismo rojo `#E26153`, mismos radios (`24px` card / `18px` botón), mismos blobs decorativos, mismas animaciones. **Solo cambian dos cosas:** el hero arranca oscuro y el ritmo de fondos se agrupa en bloques.

> Todo lo no documentado aquí se hereda de las secciones §1–§15. Esta sección solo describe los *deltas*.

### Hero oscuro (prioridad)

A diferencia del landing principal, el hero de un sublanding **arranca oscuro**. Es la primera decisión de composición y la que marca el tono de toda la página.

| Elemento | Valor |
|---|---|
| Fondo | Superficie oscura `#0F1419` (token base oscuro del sistema — ver `foundation/THEMES.md`). Equivalentes válidos ya en uso: `#0f1219` (Ecosistema), `bg-gray-900` |
| Heading (H0 / H1) | Blanco `#FFFFFF` |
| Acento en heading | Red 600 `#E26153` — **solo en texto grande** (heading), nunca en cuerpo pequeño sobre oscuro |
| Subtítulo / descripción | `text-gray-400` |
| Eyebrow | `text-gray-400` uppercase |
| Decorativos | Glow blobs rojos suaves: `rgba(226,97,83,0.06)` con `blur-[100px]` — los blobs rosas claros se pierden sobre negro |
| Mesh + noise | Obligatorio sobre el fondo oscuro plano (misma regla que cualquier sección oscura) |

```html
<section class="relative overflow-hidden bg-[#0F1419] py-24 tablet:py-32">
  <div class="pointer-events-none absolute -top-32 -left-32 h-[500px] w-[500px] rounded-full bg-[#E26153]/[0.06] blur-[100px] animate-pulse-soft" />
  <div class="relative z-10 mx-auto max-w-[1018px] px-6">
    <p class="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">Eyebrow</p>
    <h1 class="font-sora font-light text-white">
      Texto <span class="text-[#E26153]">acento</span>
    </h1>
    <p class="mt-4 font-inter text-gray-400">Subtítulo</p>
  </div>
</section>
```

> ⚠️ Verificar contraste AA del acento `#E26153` sobre `#0F1419` — válido para texto grande (heading), no para cuerpo. Ver `accessibility/A11Y.md`.

### Ritmo por bloques (no alternancia)

El landing principal alterna fondos sección a sección. **En sublandings eso se siente pesado y fragmentado** (claro / oscuro / claro / oscuro). En su lugar, el fondo cambia por **bloques de 2–3 secciones**: varias secciones del mismo fondo seguidas antes de transicionar.

**Regla:** máximo ~3 transiciones de fondo en todo el sublanding. Cada bloque agrupa mínimo 2 secciones del mismo tono (excepción: el hero puede ir solo como apertura del primer bloque oscuro).

**Estructura de bloques recomendada:**

| Bloque | Secciones | Fondo |
|---|---|---|
| **A — Apertura oscura** | Hero + (opcional 1 sección de refuerzo) | Oscuro `#0F1419` |
| **B — Cuerpo claro** | Beneficios + Plataforma + Métricas + Social proof | Claro (`#FFFFFF` / `#FFFAFA`) |
| **C — Profundidad oscura** | Ecosistema / Casos de uso + (opcional FAQ) | Oscuro `#0f1219` |
| **D — Cierre oscuro** | CTA Final → Footer | `bg-gray-900` → `#000000` |

> El resultado es un ritmo deliberado **oscuro → claro → oscuro**, con peso en cada bloque, en lugar del zigzag del landing principal. Dentro de un bloque claro se mantiene la regla de variedad de *layouts* (§14) aunque el fondo no cambie.

### Qué NO cambia respecto al landing principal

- Tipografía, escala, pesos (§1)
- Contenedor `1018px` (§2)
- Botones, cards, sombras, radios (§3–§5)
- Header glass y footer negro (§7–§8)
- Blobs, animaciones, estructura de sección (§9–§12)
- Catálogo de secciones y anti-patrones (`patterns/LANDING-SECTIONS.md`)

---

## Referencias

- [`foundation/COLORS.md`](../foundation/COLORS.md) — Paleta completa y tokens de color
- [`foundation/TYPOGRAPHY.md`](../foundation/TYPOGRAPHY.md) — Escala tipográfica del sistema
- [`foundation/SPACING.md`](../foundation/SPACING.md) — Escala de spacing, padding, gap
- [`foundation/ELEVATION.md`](../foundation/ELEVATION.md) — Sombras y border-radius completos
- [`foundation/ANIMATION.md`](../foundation/ANIMATION.md) — Keyframes y transiciones del sistema
- [`foundation/LAYOUT.md`](../foundation/LAYOUT.md) — Grid, breakpoints, responsive
- [`components/ATOMS.md`](../components/ATOMS.md) — Botones, inputs, badges
- [`platforms/DASHBOARD.md`](./DASHBOARD.md) — Contexto opuesto: dashboard/admin
- [`workflows/CLAUDE-CONTROLLER.md`](../workflows/CLAUDE-CONTROLLER.md) — Entry point para Claude
