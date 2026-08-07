# reference-landing.md

> Tokens y patrones exclusivos de **landing pages públicas** T1 / NEXUS V2.0.  
> Versión condensada para context window de Claude.  
> Fuente completa: `platforms/LANDING.md`, `patterns/LANDING-SECTIONS.md`.  
> ❌ Nada de este archivo aplica en dashboard.

---

## Regla cardinal

| Token | Landing | Dashboard |
|---|---|---|
| Tipografía headings | Sora Light 300 (H0) / Regular 400 (H1–H4) | Manrope |
| Tipografía cuerpo | Inter | Manrope |
| Rojo primario | `#E26153` (Red 600) | `#DB3B2B` (Red 500) |
| Contenedor | `max-w-[1018px]` | `max-w-[1600px]` |
| Border radius cards | `24px` | `10px` / `20px` |
| Border radius botones | `18px` | `10px` |
| Altura botones | `45px` | `35px` |
| Sombra cards | `0 0 25px 2px rgba(0,0,0,0.06)` | `0 0 5px 1px rgba(0,0,0,0.1)` |
| Header BG | `rgba(255,255,255,0.9)` + blur | Blanco sólido |
| Footer BG | `#000000` | No aplica |

---

## Tipografía

**Familias:** Sora (headings) + Inter (todo lo demás). Manrope **prohibida**.

### Headings (Sora)

| Nivel | Peso | Mobile → Desktop | Clase |
|---|---|---|---|
| H0 Display | Light 300 | 44px → 54px | `font-sora font-light text-[44px] tablet:text-[54px]` |
| H1 Section | Regular 400 | 28px → 40px | `font-sora font-normal text-[28px] tablet:text-[40px]` |
| H2 Subsection | Regular 400 | 26px → 35px | `font-sora font-normal text-[26px] tablet:text-[35px]` |
| H3 Card | Regular 400 | 20px → 24px | `font-sora font-normal text-[20px] tablet:text-[24px]` |
| H4 Small | Regular 400 | 16px → 20px | `font-sora font-normal text-[16px] tablet:text-[20px]` |

> H0 es el ÚNICO nivel Sora Light 300. H1–H4: Sora Regular 400. ❌ Sora Bold/SemiBold prohibido.

**H2 estándar de sección (aplicar consistentemente en toda la landing):**
```html
<!-- Fondo claro -->
<h2 class="font-sora text-[32px] font-normal text-gray-900 tablet:text-[44px]">
<!-- Fondo oscuro -->
<h2 class="font-sora text-[32px] font-normal text-white tablet:text-[44px]">
```
❌ `text-[36px]`, `text-[40px]`, `text-[48px]` en h2 de sección — solo 32/44px.

### Texto (Inter)

| Nivel | Peso | Tamaño | Clase |
|---|---|---|---|
| H5 Mini | Medium 500 | 16px → 20px | `font-inter font-medium text-[16px] tablet:text-[20px]` |
| Body | Regular 400 | 14px → 16px | `font-inter font-normal text-[14px] tablet:text-[16px]` |
| CTA / Botones | SemiBold 600 | 14px | `font-inter font-semibold text-[14px]` |
| Eyebrow | SemiBold 600 | 11px | `font-inter font-semibold text-[11px] uppercase tracking-[0.15em]` |
| Caption | Regular 400 | 12px | `font-inter font-normal text-[12px]` |

### Patrones de código frecuentes

```html
<!-- Título con acento rojo — span hereda el peso del padre -->
<h2 class="font-sora font-normal text-gray-900 text-[32px] tablet:text-[44px]">
  Texto normal <span class="text-[#E26153]">acento rojo</span>
</h2>

<!-- Eyebrow badge -->
<p class="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">
  Eyebrow label
</p>

<!-- Link con chevron -->
<a class="font-inter text-sm font-semibold text-oxford hover:text-[#E26153] transition-colors">
  Probar gratis <ChevronRight class="h-4 w-4 inline" />
</a>
```

**Texto en el hero:** en el landing principal (hero claro) heading y descripción siempre en negro `#000000`. ❌ Nunca texto blanco sobre el hero claro. **En sublandings el hero es oscuro** (`#0F1419`): heading en blanco, acento `#E26153` solo en texto grande.

---

## Contenedores

| Tipo | Ancho | Clase | Uso |
|---|---|---|---|
| Principal | 1018px | `max-w-[1018px] mx-auto px-6` | Todas las secciones |
| Estrecho | 721px | `max-w-[721px] mx-auto` | Hero text, CTA final, FAQ |
| Screenshot | 850px | `max-w-[850px] mx-auto` | Browser mockups |

**Contenedor con degradado — responsive:**
```html
<div class="overflow-hidden rounded-none tablet:mx-auto tablet:max-w-[1018px] tablet:rounded-[24px] tablet:px-6"
     style="background: linear-gradient(to bottom, #FFFAFA, #F2B5AE);">
  <div class="px-5 py-10 tablet:p-16"><!-- contenido --></div>
</div>
```
> Mobile: `rounded-none`, full-width. Desktop: `rounded-[24px]` con márgenes.

---

## Botones

| Propiedad | Primario | Secundario |
|---|---|---|
| BG | `#E26153` | `#FFFFFF` |
| Texto | `#FFFFFF` | Oxford `#4C4C4C` |
| Border | ninguno | `1px solid #D9D9D9` |
| Border radius | `18px` | `18px` |
| Altura | `45px` | `45px` |
| Font | Inter SemiBold 600 | Inter SemiBold 600 |
| Hover BG | `#DB3B2B` | Gray 50 `#F8F8F8` |

**Botón sobre fondo oscuro:** usar `<a>` con borde semitransparente, no `secondary`:
```html
<a class="border border-white/50 text-white bg-transparent hover:bg-white/10 rounded-[18px] h-[45px] px-6 font-inter font-semibold text-[14px] inline-flex items-center">
  Texto
</a>
```

---

## Cards

```css
border-radius: 24px;
box-shadow: 0 0 25px 2px rgba(0,0,0,0.06);
padding: 32px; /* p-8 */
```

**Hover:** `hover:-translate-y-1.5 hover:shadow-[0_20px_50px_rgba(0,0,0,0.08)] duration-500`

**Con glow en hover:**
```html
<div class="group relative overflow-hidden rounded-[24px] bg-white p-8 shadow-[0_0_25px_2px_rgba(0,0,0,0.06)] transition-all duration-500 hover:-translate-y-1.5 hover:shadow-[0_20px_50px_rgba(0,0,0,0.08)]">
  <div class="pointer-events-none absolute -top-10 -right-10 h-24 w-24 rounded-full opacity-0 blur-[30px] transition-opacity duration-500 group-hover:opacity-100"
       style="background: rgba(226,97,83,0.08);"></div>
  <div class="relative z-10"><!-- contenido --></div>
</div>
```

**Cards sobre fondo oscuro:**
```html
<!-- Normal -->  class="bg-white/[0.04] border border-white/[0.08] backdrop-blur-sm hover:bg-white/[0.08]"
<!-- Activa -->  class="bg-[#E26153]/[0.06] border-[#E26153]/40 backdrop-blur-sm"
```

---

## Degradados y fondos

| Tipo | Valor | Uso |
|---|---|---|
| Hero linear | `linear-gradient(to bottom, #FDF0EF, #F2B5AE, #FFFFFF)` | Hero |
| CTA | `linear-gradient(to bottom-right, #E59086, #F2B5AE)` | CTA cards |
| Mesh dark | ver snippet abajo | Secciones oscuras |

**Fondos de sección:** Blanco `#FFFFFF` · Rosa suave `#FFFAFA` · Negro `#000000` (footer) · Oscuro `#0f1219` (secciones oscuras)

**Mesh gradient (secciones oscuras — nunca `bg-gray-900` plano):**
```css
background:
  radial-gradient(ellipse at 25% 35%, rgba(226,97,83,0.07), transparent 50%),
  radial-gradient(ellipse at 75% 80%, rgba(33,128,255,0.04), transparent 50%),
  radial-gradient(ellipse at 50% 50%, rgba(226,97,83,0.03), transparent 60%),
  #0f1219;
```
Siempre agregar overlay `.bg-noise` al 3%.

---

## Elementos decorativos (obligatorios)

Cada sección incluye al menos un elemento decorativo. Son parte del lenguaje visual, no opcionales.

### Glow blobs

```html
<div class="pointer-events-none absolute -top-24 -right-24 h-[400px] w-[400px] animate-pulse-soft rounded-full bg-[#E59086]/20 blur-[120px]"></div>
```

| Color | Tamaño | Blur | Uso |
|---|---|---|---|
| `rgba(229,144,134,0.2)` | 400–500px | `blur-[120px]` | Rosa principal |
| `rgba(249,210,210,0.35)` | 250–350px | `blur-[80px]` | Rojo suave |
| `rgba(226,97,83,0.06)` | 400–600px | `blur-[100px]` | Sobre fondos oscuros |

**Regla de estructura:** padre `relative overflow-hidden` · blobs `absolute pointer-events-none z-0 animate-pulse-soft` · contenido `relative z-10`

### Dot pattern (sobre `#FFFAFA`)

```html
<div class="pointer-events-none absolute inset-0 z-0 opacity-40"
     style="background-image: radial-gradient(circle, #D4D4D4 0.8px, transparent 0.8px); background-size: 24px 24px;"></div>
```

### Íconos en cards — siempre dentro de contenedor

```html
<div class="flex h-[52px] w-[52px] items-center justify-center rounded-[14px] bg-[#FEF4F4]">
  <Icon class="h-6 w-6 text-[#E26153]" />
</div>
```

| Variante | BG | Ícono | 
|---|---|---|
| Rojo | `#FEF4F4` (Red 50) | `#E26153` (Red 600) |
| Gris | `#F8F8F8` (Gray 50) | `#4C4C4C` (Oxford) |

❌ Sin azul, verde, violeta, naranja — solo rojo o gris.

---

## Componentes clave

### Browser mockup (screenshots nunca planos)

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
  <img src="screenshot.png" class="w-full" alt="..." />
</div>
```

### Floating badges (máx. 3 por sección)

```html
<div class="absolute [posición] z-20 animate-float rounded-2xl border border-white/60 bg-white/90 p-3 px-4 shadow-[0_12px_40px_rgba(0,0,0,0.1)] backdrop-blur-xl">
  <div class="flex items-center gap-3">
    <div class="flex h-9 w-9 items-center justify-center rounded-[10px] bg-green-100">
      <CheckIcon class="h-[18px] w-[18px] text-green-500" />
    </div>
    <div>
      <p class="font-sora text-[12px] font-semibold text-gray-900">Pago aprobado</p>
      <p class="font-inter text-[11px] text-gray-500">$1,250.00 MXN</p>
    </div>
  </div>
</div>
```

Cada badge usa animación diferente: `animate-float` · `animate-float-slow` · `animate-float-reverse`. Ocultar 1–2 en mobile.

### Glassmorphism

| Componente | Clases |
|---|---|
| Badge flotante | `bg-white/90 backdrop-blur-xl border border-white/60 shadow-[0_12px_40px_rgba(0,0,0,0.1)] rounded-2xl` |
| Eyebrow badge | `bg-white/75 backdrop-blur-lg border border-white/50 rounded-full` |
| Card glass (dark) | `bg-white/[0.04] backdrop-blur-sm border border-white/[0.08] rounded-[24px]` |
| Header on scroll | `bg-white/90 backdrop-blur-md` |

> Solo sobre contenido visual (screenshot, degradado, sección oscura). ❌ Nunca sobre fondo blanco plano.

---

## Header

| Propiedad | Desktop | Mobile |
|---|---|---|
| Altura | `70px` | `60px` |
| BG | `rgba(255,255,255,0.9) backdrop-blur-md` | `rgba(255,255,255,0.92) backdrop-blur` |
| Posición | `fixed top-0 z-50` | `fixed top-0 z-50` |
| Contenedor | `max-w-[1018px]` | full-width |
| "Iniciar sesión" | `<a>` link Oxford — ❌ nunca botón | visible en panel |
| CTA "Comenzar" | Botón primario en barra | Solo en panel expandido |

❌ Header con fondo blanco sólido — siempre semitransparente con blur.

---

## Footer

BG `#000000` · contenedor `max-w-[1018px]`  
Desktop: Logo + redes + 2–3 columnas links · Mobile: stack vertical  
WhatsApp FAB: `#25D366 · h-14 w-14 · fixed bottom-6 right-6 z-50`

---

## Animaciones

```css
@keyframes float        { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-12px)} }
@keyframes float-slow   { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
@keyframes float-reverse{ 0%,100%{transform:translateY(0)} 50%{transform:translateY(10px)} }
@keyframes pulse-soft   { 0%,100%{opacity:0.35;transform:scale(1)} 50%{opacity:0.55;transform:scale(1.05)} }
@keyframes marquee      { 0%{transform:translateX(0)} 100%{transform:translateX(-50%)} }
```

**Scroll animations (`data-animate`):**
```css
[data-animate] { opacity:0; transform:translateY(28px); transition: opacity 0.7s cubic-bezier(0.16,1,0.3,1), transform 0.7s cubic-bezier(0.16,1,0.3,1); }
[data-animate].visible { opacity:1; transform:translateY(0); }
```

**Patrones:**

| Patrón | Implementación |
|---|---|
| Fade entre tabs/carrusel | `transition-opacity duration-500` — solo opacidad, nunca slide |
| Hover en cards | `-translate-y-1.5` + shadow hover + `duration-500` |
| Stagger | `transitionDelay: ${i * 80}ms` |
| Auto-rotación | `setInterval` + pause on hover — siempre |
| Números animados | `useCountUp` + IntersectionObserver |

---

## Estructura de sección — plantilla base

```tsx
"use client"; // solo si tiene interactividad
import SectionWrapper from "./ui/SectionWrapper";
import { DATOS } from "@/lib/constants";

export default function T1NombreSeccion() {
  return (
    <SectionWrapper id="seccion-id" className="py-20 tablet:py-28">
      {/* Decorativos — absolute z-0 pointer-events-none */}
      <div className="pointer-events-none absolute -top-24 -right-24 h-[400px] w-[400px] animate-pulse-soft rounded-full bg-[#E59086]/20 blur-[120px]" />

      <div className="relative z-10 mx-auto max-w-[1018px] px-6">
        <div data-animate>
          <p className="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">Eyebrow</p>
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

---

## Secuencia típica de secciones

| # | Sección | Fondo |
|---|---|---|
| — | Header | Glass `rgba(255,255,255,0.9)` |
| 1 | Hero | Degradado `#FDF0EF → #F2B5AE → #FFFFFF` |
| 2 | Beneficios | `#FFFFFF` o `#FFFAFA` |
| 3 | Plataforma / Features | `#FFFFFF` |
| 4 | Métricas / Stats | `#FFFFFF` |
| 5 | Social proof | `#FFFFFF` o gris muy claro |
| 6 | Pasos | `#FFFAFA` o sección oscura |
| 7 | Pricing | `#FFFFFF` |
| 8 | Ecosistema | Oscuro `#0f1219` |
| 9 | FAQ | `#FFFFFF` |
| 10 | CTA Final | Oscuro `bg-gray-900` |
| — | Footer | `#000000` |

> **Landing principal:** no repetir mismo fondo en secciones consecutivas. Mínimo 2 secciones oscuras en toda la landing.
> **Sublanding:** hero oscuro de apertura + ritmo por bloques (oscuro → claro → oscuro), fondo cambia cada 2–3 secciones, no sección a sección. Ver `platforms/LANDING.md` §16.
