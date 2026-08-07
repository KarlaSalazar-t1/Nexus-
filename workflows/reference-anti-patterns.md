# reference-anti-patterns.md

> Guardrails de NEXUS V2.0. Lo que nunca hacer y qué hacer en su lugar.  
> Versión condensada para context window de Claude.  
> Fuentes: todos los MDs del repo — anti-patrones consolidados en un solo lugar.

---

## Regla cardinal — contextos

| ❌ Nunca | ✅ Siempre |
|---|---|
| Manrope en landing | Sora (headings) + Inter (cuerpo) en landing |
| Sora o Inter en dashboard | Manrope en dashboard para todo |
| `#DB3B2B` (Red 500) en landing | `#E26153` (Red 600) en landing |
| `#E26153` (Red 600) en dashboard | `#DB3B2B` (Red 500) en dashboard |
| Rojo en texto de dashboard | Oxford `#4C4C4C` — el rojo se lee como error |
| `max-w-[1600px]` en landing | `max-w-[1018px]` en landing |
| `max-w-[1018px]` en dashboard | `max-w-[1600px]` en dashboard |
| Asumir contexto sin confirmación | Preguntar si no está claro si es landing o dashboard |

---

## Tipografía

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| Sora Bold 700 o SemiBold 600 en headings landing | H0: Sora Light 300 · H1–H4: Sora Regular 400 |
| Inter Bold 700 en landing | Inter máximo SemiBold 600 |
| Span de acento rojo con peso diferente al padre | El `<span>` siempre hereda el peso del título |
| Links en azul | Links en Oxford `#4C4C4C` |
| Links con underline por default | Sin underline en estado normal |
| 3+ tamaños de texto en una misma línea | Máximo 2 niveles por línea |
| `text-[36px]` / `text-[40px]` / `text-[48px]` en h2 de sección | Solo `text-[32px] tablet:text-[44px]` |
| Tamaños fuera de escala (22px, 18px en dashboard) | Escala fija: 20 / 16 / 14 / 12px en dashboard |
| Line-height distinto al de la familia | 1.366em Manrope · 1.2em Sora · 1.5em Inter |
| Eyebrow centrado | Eyebrow left-aligned, `text-[11px] font-semibold uppercase tracking-[0.15em]` |

---

## Colores

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| Paleta default de Tailwind (indigo, blue, sky) | Tokens de NEXUS definidos en `reference-foundation.md` |
| Colores arbitrarios inventados | Solo tokens del sistema |
| Texto blanco en el hero claro (landing principal) | Texto `text-gray-900` — el hero del landing principal es claro. (En sublandings el hero es oscuro: blanco es correcto — ver LANDING.md §16) |
| Texto `text-gray-900` sobre fondos oscuros | `text-white` o `text-gray-400` |
| Números/métricas en rojo sobre fondos de color | `text-white` para métricas sobre fondos de color |
| Íconos en azul, verde o violeta en landing | Íconos solo en rojo `#E26153` o gris |

---

## Sombras y elevación

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| `shadow-md` / `shadow-lg` de Tailwind | Tokens del sistema: `shadow-button`, `shadow-card-selected`, `shadow-landing-*` |
| Sombra en dropdowns o sidebar de dashboard | Flat — sin sombra |
| Border-radius de landing (24px) en dashboard | 10px estándar, 20px cards grandes |
| Border-radius de dashboard (10px) en landing | 24px cards, 18px botones |
| Valores de radius inventados (6px, 8px, 13px, 15px en dashboard) | Solo 10px y 20px en dashboard |
| Sombras con opacidad alta (>0.2) | Sombras sutiles, siempre <0.2 de opacidad |
| Z-index arbitrarios (999, 9999) | Escala del sistema: 0/10/20/30/40/50/60/70/80/90/100 |

---

## Spacing

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| Valores fuera de escala (10px, 15px, 18px, 22px, 30px) | Múltiplos de 4px — escala del sistema |
| `p-[17px]` cuando existe un token equivalente | `p-4` (16px) o el token más cercano |
| Mezclar rem y px en un mismo componente | Solo px |
| 128px (`py-32`) como gap entre elementos | 128px solo para section padding, nunca como gap |

---

## Layout y estructura

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| Mismo layout en secciones consecutivas | Alternar: 2col → grid 3col → bento → dark → carrusel |
| Hero 50/50 genérico | Dashboard inmersivo + floating badges + glows |
| Títulos centrados | Left-aligned por defecto |
| `bg-gray-900` plano en secciones oscuras | Mesh gradient + noise overlay obligatorio |
| Screenshot plano sin contenedor | Siempre en browser mockup o phone mockup |
| Glassmorphism sobre fondo blanco | Solo sobre degradado, screenshot o sección oscura |
| Sidebar siempre visible en mobile | Colapsa a drawer desde hamburguesa |
| Diseño desktop-first | Mobile-first desde 360px |
| Botones o touch targets <44px en mobile | Mínimo 44×44px |
| Tablas que se cortan en mobile | Transformar en cards apiladas en mobile |
| Contenedor centrado sin `mx-auto` | Siempre `mx-auto` en contenedores |

---

## Animaciones

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| `transition-all` | Especificar propiedades exactas |
| Animar `height`, `width`, `top`, `left` | Solo `transform` y `opacity` |
| Transicionar `transform` o `scale` en carruseles | Solo `opacity` en carruseles |
| Floating badges con la misma animación | Cada badge usa un keyframe diferente |
| Más de 3 floating badges por sección | Máximo 3 |
| Stagger con más de 6 elementos o delay >500ms total | Máximo 6 elementos, delay acumulado ≤500ms |
| Auto-rotación sin pause on hover | Siempre pausar en hover |
| Scroll animations sin IntersectionObserver | Siempre con IntersectionObserver + `data-animate` |
| Ignorar `prefers-reduced-motion` | Siempre implementar el fallback |
| Transitions >700ms | Máximo 700ms — más lento se siente pesado |
| Keyframes custom en dashboard | Solo transitions CSS simples en dashboard |

---

## Componentes e implementación

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| Contenido hardcodeado en componentes | Todo en `constants.ts` |
| Nombres sin prefijo `T1` | `T1` + PascalCase obligatorio |
| `"use client"` en componentes estáticos | Solo si usa hooks, handlers o APIs del browser |
| `<img>` directo | `<Image>` de Next.js |
| Íconos sueltos en cards | Dentro de contenedor `52×52px rounded-[14px]` |
| Componente interactivo con menos de 10 estados | Default/Hover/Active/Focus/Disabled/Loading/Error/Success/Selected/Empty |
| `:focus` genérico para focus state | `:focus-visible` — solo activado por teclado |
| Mejorar o agregar al replicar una referencia | Replicar exacto — sin mejorar unilateralmente |
| Parar QA tras un solo screenshot | Mínimo 2 rondas de comparación |

---

## Fondos decorativos (landing)

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| `bg-gray-900` plano en sección oscura | Mesh gradient: radiales de rojo+azul sobre `#0f1219` |
| Sin noise overlay en secciones con degradado | `.bg-noise` al 3% encima del mesh gradient |
| Sin glow blob por sección | Al menos 1 glow blob `absolute pointer-events-none` por sección |
| Accordion FAQ simple | 2 columnas: lista de preguntas izq + panel respuesta der |
| Logo wall estático | Marquee animado con fades laterales |
| Header con fondo blanco sólido | `bg-white/90 backdrop-blur-md` |
| Footer con fondo distinto a negro | Footer siempre `#000000` |

---

## Dark mode (solo dashboard)

| ❌ Anti-patrón | ✅ Correcto |
|---|---|
| `bg-white` o `bg-[#FFFFFF]` hardcodeado | `bg-surface` para adaptarse a dark mode |
| `text-[#4C4C4C]` hardcodeado para texto | `text-on-surface` para adaptabilidad |
| Invertir el botón primario en dark mode | Absoluto — siempre `bg-[#DB3B2B] text-white` en ambos modos |
| Asumir que colores contextuales cambian en dark | Success/Warning/Error/Info no cambian entre modos |
| Shades claros (100) en dark sin mappear equivalente oscuro | BG dark usa `#242937` en lugar de shades 100 |
| Implementar modo oscuro toggleable en landing/sublanding | El modo toggleable solo aplica a dashboard. Secciones/heroes oscuros autorales de landing/sublanding sí son válidos (LANDING.md §16) |
