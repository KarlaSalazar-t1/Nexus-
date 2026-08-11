# Landing Sections — NEXUS V2.0

> **Capa de ensamblaje de página.** Documenta cómo se **componen** las landing pages del ecosistema T1: qué secuencia siguen, cómo se agrupan los fondos y qué reglas de layout aplican al armar una página completa.
>
> **No documenta componentes** (esos viven en `components/LANDING-COMPONENTS.md`) **ni tokens** (esos viven en `plataform/LANDING.md`). Este archivo es solo la capa de composición.

**Última actualización:** Agosto 2026 · **Fuente de verdad:** repo `T1landing` (código) · **Owner:** Karla Salazar — Head of UX/UI

> - **Componentes y variantes** (heros, cards, carruseles, paneles, tabs…) → `components/LANDING-COMPONENTS.md`
> - **Tokens** (tipografía, color, contenedores, botones, sombras, degradados, animaciones) → `plataform/LANDING.md`

---

## Filosofía: catálogo, no receta

Una landing T1 es un **catálogo de componentes y patrones**, no una secuencia obligatoria. La cohesión viene de los **tokens y el estilo** (Sora + Inter, botón Red 500, hero oscuro, header con dropdowns, footer negro), **no** de tener los mismos elementos en el mismo orden. Dos landings T1 pueden verse muy distintas en composición y aun así sentirse familia.

Las secuencias de abajo son **referencia del estado actual**, no una plantilla fija.

---

## Secuencia típica — Landing principal

Orden actual en `src/app/page.tsx` (referencia, no obligatorio):

| # | Sección | Componente | Fondo |
|---|---|---|---|
| — | Header | `T1Navbar` (dropdowns Productos + Recursos) | Glass |
| 1 | Hero oscuro | `T1Hero` (degradado + input IA) | Oscuro (degradado) |
| 2 | Problema → solución | `T1Problema` | Claro |
| 3 | Vende / Cobra / Envía | `T1FeatureIntro` (glass + glow + imagen) | Oscuro |
| 4 | Capacidades | `T1Features` (tabs) | Claro |
| 5 | Métricas | `T1Metrics` (count-up) | Oscuro |
| 6 | Para cada etapa | `T1AudienceRotator` (tabs auto-rotación) | Oscuro |
| 7 | Casos de éxito | `T1EnterpriseCarousel` | Oscuro |
| 8 | Soluciones | `T1Solutions` (stack cards 1/N) | Claro |
| 9 | Vende / Cobra / Envía (sticky) | `T1ScrollShowcase` | Oscuro |
| 10 | Cierre | CTA final → `T1Footer` | Oscuro |

**Ritmo de fondos (principal):** base predominantemente **oscura** (hero + varias secciones) con **respiros claros** intercalados. Cierre oscuro.

---

## Secuencia típica — Sublanding (páginas de producto)

Esqueleto canónico, consistente entre las 16 rutas de producto (bloques opcionales marcados):

| # | Bloque | Componente(s) (catálogo) |
|---|---|---|
| 1 | **Hero oscuro dividido** (+ CTA) | 1.3 / 1.4 / 1.6 |
| 2 | Statement / problema | 2.3 pain cards *o* 6.2 mini-stats |
| 3 | Transición a solución | — |
| 4 | **Feature blocks con panel de UI simulada** (2–4) | 4.1 |
| 5 | "Cómo funciona / en N pasos" | 5.1 / 5.2 |
| 6 | Grid de features image-led | 2.2 |
| 7 | *(opcional)* Números / count-up | 6.1 |
| 8 | *(opcional)* Pricing | 2.5 |
| 9 | *(opcional)* App download | 9.2 |
| 10 | *(opcional)* Ecosistema cross-sell | 9.3 |
| 11 | FAQ | — |
| 12 | CTA final + footer | 9.4 / 8.3 |

**Ritmo de fondos (sublanding):** **hero oscuro** + **cuerpo mayormente claro** (blanco / `#FFFAFA` con paneles) + **cierre oscuro** (CTA + footer). Las secciones oscuras dentro del cuerpo son puntuales (statement, casos). No hay "ritmo por bloques oscuro→claro→oscuro" — ese modelo se retiró.

> Hero: siempre oscuro (negro o degradado similar al del hero principal), texto blanco. Detalle → `plataform/LANDING.md` §6 y §16.

---

## Estructura base de toda sección

```tsx
"use client"; // solo si tiene interactividad
import SectionWrapper from "./ui/SectionWrapper";
import { DATOS_SECCION } from "@/lib/constants";

export default function T1NombreSeccion() {
  return (
    <SectionWrapper id="seccion-id" className="px-5 py-[100px] tablet:px-10 tablet:py-[128px]">
      {/* Decorativos: absolute, z-0, pointer-events-none */}
      <div className="relative z-10 mx-auto max-w-[var(--max-w)]">
        <div data-animate>{/* título + contenido */}</div>
      </div>
    </SectionWrapper>
  );
}
```

**Reglas universales:**
- Contenido hardcodeado → `src/lib/constants.ts`, nunca inline.
- `data-animate` en cada bloque para las scroll animations.
- Decorativos: `absolute pointer-events-none z-0`; contenido: `relative z-10`.
- Contenedor: cota `max-w-[var(--max-w)]` (1220px) + `mx-auto`.
- Espaciados (padding/margin/gap) en **múltiplos de 4px**.
- Padding de sección típico: `py-[100px] tablet:py-[128px]`.

> Tokens exactos (radios, sombras, degradados) → `plataform/LANDING.md`.

---

## Anti-patrones de layout

| ❌ Anti-patrón | ✅ Alternativa |
|---|---|
| Mismo layout en 3+ secciones consecutivas | Alternar: 2 col → grid → oscuro → carrusel → sticky |
| Screenshot plano sin contenedor | Réplica de UI simulada (4.1) o phone mockup |
| Logo wall estático centrado | Marquee animado con fades laterales |
| Fondo oscuro plano | + glows radiales / mesh |
| Glassmorphism sobre fondo blanco | Solo sobre oscuro, degradado o imagen |
| Título centrado | Título **left-aligned** |
| Texto negro sobre hero | El hero es oscuro → texto **blanco** |

---

## Checklist QA — Composición de página

*(Las validaciones de tokens —tipografía, color— viven en el checklist de `plataform/LANDING.md`.)*

**Composición**
- [ ] Landing principal: base oscura + respiros claros. Sublanding: cuerpo claro + hero y cierre oscuros.
- [ ] Hero oscuro (negro o degradado) con texto blanco.
- [ ] Cierre: CTA final + footer oscuro.
- [ ] Layouts visualmente distintos entre secciones consecutivas.

**Layout**
- [ ] Contenedor: cota `1220px` (nunca `1600px`).
- [ ] Títulos left-aligned.
- [ ] Espaciados en múltiplos de 4px; padding de sección `py-[100px] tablet:py-[128px]`.

**Interactividad**
- [ ] Carruseles: altura fija + transición solo opacidad.
- [ ] Tabs: fade, nunca slide.
- [ ] Stats: count-up con IntersectionObserver.
- [ ] Auto-rotación (tabs/accordion) con pausa on hover.

**Performance**
- [ ] `npm run build` sin errores TypeScript.
- [ ] Imágenes con `<Image>` de Next.js; logos SVG.
- [ ] Todo el contenido en `constants.ts`; sin imports huérfanos.

---

## Referencias cruzadas

- **Componentes de landing** (variantes, tokens, responsive) → `components/LANDING-COMPONENTS.md`
- **Tokens de landing** → `plataform/LANDING.md`
- **Diferencias landing vs dashboard** → `plataform/LANDING.md` §Diferencias clave
- **Componentes base** (botones, inputs, badges) → `components/ATOMS.md`
- **Iconografía / logos** → `assets/ICONOGRAPHY.md`, `assets/BRAND-ASSETS.md`
