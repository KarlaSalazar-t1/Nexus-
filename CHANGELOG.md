# Changelog — NEXUS V2.0

Todos los cambios relevantes al sistema de diseño se documentan aquí. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

---

## [2.2.0] — 2026-05-06

### Refactor a filosofía catálogo

Cambio de paradigma en la documentación de landing pages tras revisión del estado real de `t1landing.vercel.app`. La versión 2.1.0 documentaba una "secuencia obligatoria" de secciones donde toda landing T1 debía tener hero video loop multi-escena + Section Stack con cards flotantes + Bento grid asimétrico + storytelling explícito + sticky scroll, en ese orden. Esta filosofía producía landings monolíticas que se sentían como copias unas de otras.

**v2.2.0 reformula:** las landings T1 son un **catálogo de componentes y patrones**, no una receta fija. **La cohesión viene de los tokens y estilo** (Sora+Inter, rojo `#E26153`, border-radius 24/18, header glass, footer negro, sin eyebrows, texto blanco opacidad 100 sobre oscuros), **no de tener los mismos elementos en el mismo orden**. Dos landings T1 pueden verse muy diferentes en composición y aún así sentirse familia.

**Owner:** Karla Salazar — Head of UX/UI

**Archivos afectados:**
- `platforms/LANDING.md` — refactor de filosofía + nuevas variantes de hero
- `patterns/LANDING-SECTIONS.md` — nuevo bloque inicial "Filosofía catálogo" + reglas de cohesión + tabla de componentes con variantes + ejemplos de composición + variantes de Hero, Section Stack, Bento IA, Pricing
- `references/reference-landing.md` — versión condensada actualizada
- `references/reference-anti-patterns.md` — anti-patrón crítico nuevo (#1: receta fija prohibida)

#### Añadido

- **Filosofía "Catálogo + Cohesión"** documentada en bloque inicial de `LANDING.md` y `LANDING-SECTIONS.md`. Define qué es obligatorio (tokens, mínimos de calidad) y qué es flexible (composición, número de secciones, énfasis narrativo).
- **4 variantes de Hero documentadas** en lugar de una sola obligatoria:
  - **A.1 — Hero con video único** (default en producción `t1landing.vercel.app`): un solo `/img/hero.mp4` + preheader fijo. La opción más liviana y suficiente para la mayoría de landings.
  - **A.2 — Hero con video loop multi-escena**: 4 videos que cician cada 5s con preheader sincronizado. Para lanzamientos y campañas especiales.
  - **A.3 — Hero con preheader animado** (sin video): visual estático + preheader que rota entre términos. Más sostenible que A.2.
  - **A.4 — Hero estático con visual rico**: sin animación. El interés visual lo carga el mockup, ilustración o foto humana. Para sublandings deep dive o enterprise.
- **2 variantes de Section Stack producto documentadas:**
  - **Variante A — Carrusel paginado** (en producción): título + descripción + CTA en columna izquierda, mockup desktop + mobile superpuesto en columna derecha, paginación 1/N entre productos. Más sostenible para producción.
  - **Variante B — Phone mockup + cards flotantes**: phone central + 2-4 cards flotantes con `animate-float` desfasadas. Más rico visualmente, más caro de mantener.
- **2 variantes de Bento IA documentadas:**
  - **Variante A — Carrusel paginado** (en producción `t1landing.vercel.app`): 1 card hero por slide con feature interactivo + paginación `1 / 5`. Documentadas las 5 cards verificadas en producción (input "Cuéntame qué vendes", color picker tienda, foto + texto IA, logos paqueterías en órbita, donut chart riesgo).
  - **Variante B — Grid asimétrico tipo bento**: 5-6 celdas con `col-span-5/7`, `col-span-7/5`, `col-span-12` y componentes simultáneamente visibles. Para sublandings donde la IA es el producto principal (ej: `/productos/t1tienda/tienda-con-ia`).
- **Variante C de Pricing — Layout 2+2 cards** (verificada en producción): 2 cards principales en fila superior (T1tienda Integrador GRATIS + Tienda en línea $399/mes) + 2 cards secundarias en fila inferior (T1pagos + T1envíos). Sirve para landing principal que comunica múltiples productos sin tabla simétrica.
- **Sticky Scroll Stack — secuencia documentada explícitamente:** Vende → Cobra → Envía → **Todo en uno (cierre)**. La última card es estructuralmente distinta — muestra los 4 íconos de productos + statement "Activa todo el ecosistema en minutos" + CTA "Crear cuenta gratis". No es solo otra capability al mismo nivel sino el cierre narrativo.
- **Formato de atribución de testimoniales documentado:** `Nombre · CARGO | EMPRESA` (middle dot entre nombre y cargo, pipe entre cargo y empresa). Verificado en producción: `"Mario Muñoz · CHIEF DIGITAL OFFICER | SEARS"`.
- **Tabla de catálogo de secciones por categoría** en `LANDING-SECTIONS.md`: 12 categorías (Hero / Social proof / Beneficios / Producto / IA-tech / Métricas / Lifestyle / Storytelling / Pricing / FAQ / Cierre / CTA Final) con todas las variantes disponibles por categoría.
- **3 ejemplos de composición real** documentados: landing principal `t1landing.vercel.app`, sublanding "Tienda con IA", y sublanding mínima de feature (hipotética). Demuestra que landings T1 pueden tener composición muy distinta y aún sentirse familia.
- **Reglas de cohesión explícitas** separadas de reglas de composición. Distingue claramente entre lo que toda landing debe tener (tokens) y lo que cada landing decide (componentes).

#### Cambiado

- **Stats counter — animación `useCountUp` ahora es opcional**, no obligatoria. La sección en producción muestra valores fijos (`+25 mil / +$25 B / +40 M`). Documentado que la animación es **mejora opcional** según preferencia del producto: sin animación es más sostenible y suficiente cuando los números son aspiracionales redondos; con animación es recomendable cuando los números son ultra-precisos (ej: 12,743 negocios) y la animación enfatiza la magnitud.
- **Stats counter header** documentado como `H3 "Nuestros números:"` (verificado en producción), permitiendo también H2 más fuerte si la sección lleva más peso narrativo.
- **Stats counter label** documentado en formato descriptivo no-uppercase: `Negocios`, `procesados en pagos`, `de envíos gestionados` (antes documentado como Inter SemiBold uppercase tracking).
- **Mínimo de fondos oscuros bajado de 2 a 1.** El requisito anterior de "mínimo 2 secciones con fondo oscuro" era prescriptivo en exceso para sublandings pequeñas.
- **Storytelling explícito ya no es obligatorio en toda landing.** Mantenido como recomendación fuerte para sublandings principales (`/productos/t1tienda/tienda-con-ia` usa Antes/Hoy completo); sublandings deep dive de un solo feature pueden prescindir.
- **Sección Lifestyle obligatoria con excepción explícita:** aplica a landing principal y sublandings principales; sublandings deep dive de un solo feature pueden prescindir.
- **"Secuencia recomendada" reformulada como "Composición orientativa"** en `LANDING.md` §16. Incluye esqueleto mínimo (Header → Hero → ... → CTA → Footer), reglas de selección, y 2 ejemplos de composición real distinta.
- **Atribución de testimoniales en código de ejemplo de LANDING.md** actualizada: `Mario Muñoz · CHIEF DIGITAL OFFICER | SEARS` (era `· SEARS`).

#### Eliminado

- **"Toda landing T1 debe tener exactamente las mismas secciones en el mismo orden"** — eliminado como filosofía. Es ahora un anti-patrón explícito en `reference-anti-patterns.md`.
- **Section Stack producto ×3 obligatorio** (uno por producto) — eliminado como obligatorio. La landing principal puede usar 1 Section Stack carrusel paginado para los 3 productos, o 3 Section Stack flotantes individuales, según preferencia.
- **Hero con video loop multi-escena como variante única** — ahora es 1 de 4 variantes disponibles.
- **Bento IA grid asimétrico como única opción** — ahora es 1 de 2 variantes disponibles (la otra es carrusel paginado).
- **"Mínimo 2 secciones con fondo oscuro"** — bajado a mínimo 1.
- **Eyebrow / chip / pill sobre títulos de sección** — sigue PROHIBIDO (regla v2.1.0 mantenida).

#### Corregido

- **Atribución de testimoniales:** producción usa `Nombre · CARGO | EMPRESA`, no `· EMPRESA`. Documentación actualizada en `LANDING-SECTIONS.md §11 Casos de éxito` y `LANDING.md §3 Texto sobre fondos oscuros`.
- **Stats counter:** label en formato descriptivo no-uppercase (verificado en producción). Antes documentado como uppercase con tracking.

#### Reglas v2.1.0 que se mantienen

- ❌ Eyebrow / chip / pill / tag sobre H1 o H2 de sección **PROHIBIDO**. Solo tags pequeños DENTRO de cards.
- ✅ Texto sobre fondos oscuros: `text-white` opacidad 100 obligatoria. Sin `text-white/X` ni `text-gray-300/400` para texto leíble.
- ✅ Mega menu de productos en header (4 cols + panel lateral 3 bloques).
- ✅ Footer `#000000` con texto blanco opacidad 100.
- ✅ Hero gradient `linear-gradient(180deg, #FDF0EF 0%, #FFFFFF 60%, #FFFFFF 100%)`.
- ✅ No repetir mismo layout en 3+ secciones consecutivas.
- ✅ No repetir mismo fondo en secciones consecutivas.

---

## [2.1.0] — 2026-05-05

### Rediseño de landing — t1landing.vercel.app

Versión refactorizada de toda la documentación de landing pages a partir del rediseño en producción de `t1landing.vercel.app` y la sublanding `t1landing.vercel.app/productos/t1tienda/tienda-con-ia`. El objetivo es que con los `.md` se puedan crear landings modernas, tech, interactivas, no planas — incorporando línea lifestyle (foto humana real, no solo paneles UI) y storytelling explícito.

**Owner:** Karla Salazar — Head of UX/UI

**Archivos afectados:**
- `platforms/LANDING.md` — reescrito completo
- `patterns/LANDING-SECTIONS.md` — reescrito completo (template base + 13 secciones + footer + anti-patrones + checklist QA)
- `foundation/ANIMATION.md` — keyframes nuevos + 4 patrones avanzados
- `references/reference-landing.md` — versión condensada actualizada
- `references/reference-anti-patterns.md` — anti-patrones críticos v2.1.0

#### Añadido

- **Hero con video loop crossfade (4 escenas):** documentado componente con 4 videos `/img/hero-1.mp4` a `hero-4.mp4` que cician cada 5s con `transition-opacity duration-700`. Preheader sincronizado con índice activo. Comprimir <2MB cada uno.
- **Header con Mega Menu de Productos:** 4 columnas (T1tienda / T1envíos / T1pagos / T1score) con features cada uno + panel lateral derecho con 3 bloques (Casos de éxito, Novedades recientes, ¿Cómo quieres empezar?). Documentado anatomía completa con HTML/JSX.
- **Section Stack — Producto (Tienda / Envíos / Pagos):** patrón nuevo con phone mockup central + 2-4 cards flotantes alrededor representando eventos del producto (orden #112, FedEx, VISA aprobado). Cada card flotante con `animate-float`, `animate-float-slow` o `animate-float-reverse` desfasadas + rotaciones leves `±3deg`.
- **Bento Grid IA asimétrico:** 6 cards con `col-span-5/7`, `col-span-7/5`, `col-span-12`. Cada celda con componente visual distinto (color picker, logos paqueterías en órbita, input chat, foto + texto IA, donut chart 78). Reglas de asimetría obligatoria.
- **Stats Counter:** 3 stats centradas con `useCountUp` + IntersectionObserver. Variante con fondo oscuro mesh + texto blanco opacidad 100. Sin eyebrow.
- **Lifestyle Cards — "¿Para quién es T1?":** patrón nuevo con 3 cards full-bleed `aspect-[4/5]` con foto humana real (Emprendedor / PyME / Enterprise) + gradient overlay inferior + texto blanco opacidad 100. Carrusel horizontal con snap en mobile. Casting con apariencia local (México), iluminación natural.
- **Tabs Verticales con auto-play:** layout 2 columnas (lista 40% / preview 60%). Auto-rotación 5s con barra de progreso `animate-progress` visible bajo tab activo. Pause on hover. **Click manual rompe auto-play permanentemente** (UX pattern: si el usuario interactuó, no le quites control).
- **Storytelling — Antes / Hoy:** patrón narrativo con 3 cards de problema (Antes) en gris apagado + bloque de solución (Hoy) con input grande interactivo + chips de ejemplo. Variante completa para sublanding, reducida para landing principal.
- **Pasos numerados 1→4:** números gigantes Sora Light 300 `clamp(56px, 8vw, 88px)` color rojo como visual hero. Sin línea conectora horizontal — la tipografía es el ritmo. Stagger de 150ms entre pasos.
- **Pricing transparente — variantes asimétricas:**
  - Variante A (T1tienda): statement gigante "GRATIS" Sora Light 300 `clamp(72px, 12vw, 144px)` + bullets
  - Variante B (T1pagos premium): cards asimétricas con plan destacado 10% más alto
  - Variante C (T1pagos métodos): marquee de logos de pago
- **Casos de éxito — sección oscura mesh:** marquee de logos blancos arriba + video card principal `aspect-[16/9]` con quote, nombre, cargo todos `text-white` opacidad 100 + thumbnails clicables con fade.
- **Sticky Scroll Stack final:** 4 cards apiladas con `position: sticky; top: 80+i*16px; z-index: i+10;`. Cada card con acento/glow distinto. Desactivado en mobile con `lg:sticky`.
- **CTA Final con avatares humanos:** 5 avatares circulares `h-12 w-12 rounded-full ring-2 ring-white -ml-3` superpuestos. Personas reales con diversidad visible. Variante Dark con texto blanco opacidad 100 + glow Red 600.
- **Logos marquee bajo el hero:** verificado en producción con 9 logos clientes (Sears, Círculo de Crédito, Mercado Libre, Telcel, Pirma, Makora, Sanborns, PASE, Claro). Velocidad 30s para 6-8 logos, 40s para 9+.
- **Keyframes nuevos en `ANIMATION.md`:**
  - `progress` — barra de progreso para tabs verticales (5s linear forwards)
  - `count-tick` — pulso sutil al cambiar de dígito en stats counter
  - `shimmer` — placeholder de carga para inputs de IA
- **Beneficios con ilustración rica:** variante recomendada — 3 cards con imagen `aspect-[4/3]` arriba de la card (VENDE / COBRA / ENVÍA), no ícono plano. Ícono plano queda como variante alternativa solo cuando no hay budget de ilustración.

#### Cambiado

- **Template base de sección elimina el eyebrow.** Antes:
  ```html
  <p class="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">Eyebrow</p>
  <h2>...</h2>
  ```
  Ahora: directo al H2 con descripción opcional debajo. Sin pill, badge ni tag sobre el título de sección.
- **Secuencia típica de secciones expandida de 10 a 16 secciones** con las nuevas: Section Stack ×3 (uno por producto), Bento IA, Stats Counter, Lifestyle Cards, Tabs Verticales, Casos de éxito, Sticky Scroll Stack, CTA con avatares.
- **Hero gradient ajustado:** `linear-gradient(180deg, #FDF0EF 0%, #FFFFFF 60%, #FFFFFF 100%)` — inicia en `#FDF0EF` (más cercano a blanco) para no chocar visualmente con el header glass.
- **Contenedor por sección diferenciado:**
  - `max-w-[1018px]` — secciones generales (era el único)
  - `max-w-[1280px]` — Hero, Casos de éxito, Sticky Scroll Stack
  - `max-w-[721px]` — Hero text, CTA final, FAQ
  - `max-w-[850px]` — Browser mockups
- **Reglas obligatorias por landing:**
  - Mínimo 1 sección con foto humana real (Lifestyle Cards o CTA con avatares)
  - Mínimo 1 sección con storytelling explícito (Antes/Hoy)
  - Mínimo 1 sección interactiva animada (Bento, Tabs verticales, Sticky Scroll, Hero video loop)
  - Mínimo 2 secciones con fondo oscuro
- **Footer texto:** todos los links pasan de `#9CA3AF` a `text-white` opacidad 100. El gris sobre `#000000` falla contraste WCAG AA.
- **Marquee multi-velocidad:** `30s` para 6-8 logos, `40s` para 9+ logos, `35s` para casos de éxito sobre fondo oscuro.

#### Eliminado

- **Eyebrow / chip / pill / tag sobre H1 o H2 de sección — PROHIBIDO.** Solo se permite tag pequeño DENTRO de cards (bento, lifestyle, beneficios), nunca sobre el título de sección.
- **Badge glass como eyebrow** (`bg-white/75 backdrop-blur-lg border border-white/50 rounded-full`): eliminado del catálogo de glassmorphism. El badge glass queda solo para floating badges contextuales (no encima de títulos).
- **Línea conectora horizontal** entre pasos numerados: eliminada. Los números gigantes son el ritmo visual.
- **Tabla simétrica de pricing 3 planes idénticos:** patrón eliminado. Usar statement gigante o asimetría.

#### Corregido

- **Texto blanco sobre fondos oscuros:** `text-white/80`, `text-white/90`, `text-white/[0.7]`, `text-gray-300`, `text-gray-400` para descripciones sobre fondo oscuro **prohibidos**. Sobre `#0f1219`, `#000000`, mesh dark, footer y secciones oscuras: `text-white` opacidad 100 obligatoria. La opacidad menor a 100 falla contraste WCAG AA y se ve descolorida cuando el fondo tiene textura mesh.
- **Quote, nombre, cargo en sección de Casos de éxito:** todos `text-white` opacidad 100 (antes a veces se documentaban en `text-gray-400`).
- **Header contenedor:** ampliado a `max-w-[1280px]` para acomodar el mega menu de productos.

#### Anti-patrones nuevos críticos (v2.1.0)

1. Eyebrow / chip / pill / tag sobre títulos de sección
2. `text-white/X` con opacidad menor a 100 sobre fondos oscuros
3. Landing solo con paneles UI sin sección lifestyle
4. Landing sin storytelling explícito
5. Pricing como tabla simétrica
6. Section Stack sin cards flotantes desfasadas
7. Tabs verticales sin barra de progreso
8. Tabs verticales que reanudan auto-play tras click manual
9. Sticky Scroll Stack activo en mobile
10. Sticky Scroll Stack con cards idénticas
11. Hero sin video loop ni interactividad
12. Pasos con línea conectora horizontal
13. CTA Final sin avatares humanos
14. Casos de éxito sobre fondo claro

---

## [2.0.0] — 2026-01-01

### Lanzamiento inicial del repositorio

**Añadido:**
- Estructura modular del repositorio con 37 archivos organizados por dominio
- `README.md` como entry point con índice, principios y guía por rol
- `GLOSSARY.md` en root como referencia transversal de terminología
- Arquitectura definida: `foundation/`, `components/`, `patterns/`, `content/`, `assets/`, `accessibility/`, `platforms/`, `workflows/`

**Decisiones de arquitectura:**
- `SPACING.md` y `LAYOUT.md` separados (tokens puros vs decisiones estructurales)
- `TABLES.md` como archivo propio en `components/` (core del admin, 80% del dashboard son tablas)
- `THEMES.md` en `foundation/` como placeholder para tokens semánticos y dark mode
- `EMPTY-STATES.md` y `NOTIFICATIONS.md` como patrones propios en `patterns/`
- `skill/` consolidado dentro de `workflows/` como `CLAUDE-CONTROLLER.md` + `references/`
- `GLOSSARY.md` movido a root (transversal a todas las áreas, no solo content)
- `ANIMATION.md` diferido a P1 (nice-to-have, animaciones documentadas inline donde se usan)

**Contexto:**
NEXUS V2.0 existía como documentación consolidada en archivos monolíticos (`CLAUDE.md`, `LANDING.md`). Esta versión del repositorio reorganiza todo el contenido en archivos modulares, autocontenidos y orientados por tema, para mejorar la mantenibilidad y permitir que cada área del equipo encuentre lo que necesita sin leer todo.

---

<!-- 
Formato para nuevas entradas:

## [2.X.Y] — YYYY-MM-DD

### Categoría del cambio
Usar las siguientes categorías según aplique:
- **Añadido** — Funcionalidad o documentación nueva
- **Cambiado** — Cambios en documentación o tokens existentes
- **Corregido** — Correcciones de errores o inconsistencias
- **Eliminado** — Documentación o tokens deprecados/removidos
- **Deprecado** — Algo que se mantendrá temporalmente pero será removido
-->
