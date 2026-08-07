# Landing Sections — NEXUS V2.0

> Catálogo de secciones para landing pages públicas del ecosistema T1. Documenta qué secciones existen, cómo se estructuran, qué elementos requieren y cómo se ensamblan en una landing completa.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (`SD---Migration-V2`) · **Owner:** Karla Salazar — Lead UX/UI

> **Tokens de landing** (tipografía, colores, contenedores, botones, sombras) → `platforms/LANDING.md`  
> **Elementos decorativos y animaciones** → `platforms/LANDING.md` §9, §10

---

## Secuencia típica de secciones

| # | Sección | Fondo | Obligatoria |
|---|---|---|---|
| — | Header | Glass (`rgba(255,255,255,0.9)`) | Sí |
| 1 | Hero | Degradado rosa `#FDF0EF → #F2B5AE → #FFFFFF` | Sí |
| 2 | Beneficios | Blanco o `#FFFAFA` | Sí |
| 3 | Plataforma / Features | Blanco o `#FFFAFA` | Recomendada |
| 4 | Métricas / Stats | Blanco | Recomendada |
| 5 | Social proof | Blanco o gris muy claro | Recomendada |
| 6 | Pasos / Cómo funciona | `#FFFAFA` o sección oscura | Recomendada |
| 7 | Pricing / Formas de pago | Blanco | Según producto |
| 8 | Ecosistema T1 | Oscuro (`#0f1219`) | Recomendada |
| 9 | FAQ | Blanco | Recomendada |
| 10 | CTA Final | Oscuro (`bg-gray-900`) | Sí |
| — | Footer | `#000000` | Sí |

**Regla de ritmo visual (landing principal):** No repetir el mismo fondo en secciones consecutivas. Incluir al menos 2 secciones con fondo oscuro en toda la landing.

**Naming de componentes:** `T1` + PascalCase → `T1Hero`, `T1Beneficios`, `T1Plataforma`, `T1Metricas`, `T1SocialProof`, `T1Pasos`, `T1Pricing`, `T1Ecosistema`, `T1FAQ`, `T1CTAFinal`.

---

## Secuencia de sublanding (páginas de producto)

Las **sublandings** (T1tienda, T1pagos, T1envíos, T1score, T1marketing) usan las mismas secciones del catálogo, pero con dos diferencias de composición:

1. **Hero oscuro de apertura** (no el degradado rosa claro del landing principal).
2. **Ritmo por bloques**, no alternancia sección a sección. El fondo cambia en bloques de 2–3 secciones para evitar el zigzag claro/oscuro/claro/oscuro, que se siente pesado y fragmentado.

| Bloque | Secciones | Fondo |
|---|---|---|
| **A — Apertura** | Hero (oscuro) + opcional 1 sección de refuerzo | Oscuro `#0F1419` |
| **B — Cuerpo** | Beneficios + Plataforma + Métricas + Social proof | Claro (`#FFFFFF` / `#FFFAFA`) |
| **C — Profundidad** | Ecosistema / Casos + opcional FAQ | Oscuro `#0f1219` |
| **D — Cierre** | CTA Final → Footer | `bg-gray-900` → `#000000` |

**Regla de ritmo (sublanding):** máximo ~3 transiciones de fondo en toda la página; cada bloque agrupa mínimo 2 secciones del mismo tono. Dentro de un bloque claro se mantiene la variedad de *layouts* aunque el fondo no cambie.

> Tokens y tratamiento del hero oscuro → `platforms/LANDING.md` §16. Aquí solo se documenta la secuencia.

---

## Estructura base de toda sección

```tsx
"use client"; // solo si tiene interactividad
import SectionWrapper from "./ui/SectionWrapper";
import { DATOS_SECCION } from "@/lib/constants";

export default function T1NombreSeccion() {
  return (
    <SectionWrapper id="seccion-id" className="py-20 tablet:py-28">
      {/* Elementos decorativos (absolute, z-0, pointer-events-none) */}
      <div className="pointer-events-none absolute -top-24 -right-24 h-[400px] w-[400px] animate-pulse-soft rounded-full bg-[#E59086]/20 blur-[120px]" />

      <div className="relative z-10">
        <div data-animate>
          <p className="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">
            Eyebrow
          </p>
          <h2 className="font-sora text-[32px] font-normal text-gray-900 tablet:text-[44px]">
            Texto normal <span className="text-[#E26153]">acento</span>
          </h2>
        </div>
        <div data-animate>
          {/* contenido de la sección */}
        </div>
      </div>
    </SectionWrapper>
  );
}
```

**Reglas universales:**
- Todo contenido hardcodeado va en `src/lib/constants.ts` — nunca inline en el componente
- `data-animate` en cada bloque para activar scroll animations
- Elementos decorativos: `absolute pointer-events-none z-0`
- Contenido: `relative z-10`
- Padding mínimo: `py-20 tablet:py-28`
- Contenedor: `max-w-[1018px] mx-auto px-6`

---

## Header

**Posición:** `fixed top-0 z-50`, altura `70px` desktop / `60px` mobile.

### Desktop

```
[Logo 42px]    [Ecosistema] [¿Qué es T1?] [Contacto]    [Iniciar sesión]  [Comenzar →]
```

- Fondo: `rgba(255,255,255,0.9) backdrop-blur-md` — **nunca blanco sólido**
- Shadow on scroll: `shadow-[0px_0px_25px_2px_rgba(0,0,0,0.06)]`
- "Iniciar sesión": `<a>` link, Inter SemiBold Oxford — **nunca botón**
- "Comenzar": único `<Button>` del header — cambia a "Ir a Admin" cuando el usuario está autenticado

### Mobile

```
Barra:   [Logo 36px]                    [☰]

Panel:   [Ecosistema         ]
         [¿Qué es T1?        ]
         [Contacto           ]
         [Iniciar sesión     ]
         [═══ Comenzar → ═══]
```

- El CTA **no aparece en la barra** — solo en el panel expandido, full-width, al final del menú.

---

## 1. Hero

**Propósito:** Primera impresión. Comunica la propuesta de valor del producto con el elemento visual central.

### Layout (desktop)

```
[eyebrow badge glass]
[H0 — Título con acento rojo]
[Subtítulo — Inter Regular 16px, negro]
[CTA primario]  [CTA secundario]

                    [Elemento visual: browser mockup / video / ilustración]
                    [Floating badge 1]  [Floating badge 2]  [Floating badge 3]
```

Layout 2 columnas asimétrico: texto izquierda (~45%), elemento visual derecha (~55%).

### Fondo

El hero acepta dos variantes de degradado. La regla crítica en ambas: **la zona superior — donde el header glass se superpone — debe ser lo suficientemente clara para que el rojo del acento no choque con el fondo.**

| Variante | CSS | Cuándo usar |
|---|---|---|
| **Linear** | `linear-gradient(to bottom, #FDF0EF, #F2B5AE, #FFFFFF)` | Estándar — inicia muy claro arriba, se intensifica hacia el centro y regresa a blanco abajo |
| **Radial** | `radial-gradient(ellipse at top center, #FDF0EF 0%, #F2B5AE 50%, #FFFFFF 100%)` | Alternativa — mismo principio, el pico de color está en el centro, no en los bordes |

En ambas variantes el valor inicial es `#FDF0EF` (casi blanco) para que el header glass y el acento rojo `#E26153` sean legibles en la parte superior. Si se necesita un degradado más intenso, asegurarse de que la zona de los primeros `70px` (altura del header) permanezca por debajo de Red 300 (`#F1B0A9`) para evitar que el rojo del acento se pierda contra el fondo.

### Elemento visual

El elemento visual del hero varía según el producto, pero siempre sigue una de estas formas:

| Variante | Cuándo usar |
|---|---|
| Browser mockup + floating badges | Dashboard / admin (T1tienda, T1pagos) |
| Phone mockup | Features de usuario final (checkout, link de pago) |
| Video en loop | Cuando hay un demo funcional disponible |
| Ilustración isométrica | Cuando no hay screenshot o video disponible |

**Browser mockup:** screenshot nunca va plano — siempre dentro del contenedor de browser. Ver snippet completo en `platforms/LANDING.md` §11.

**Floating badges:** máximo 3, con animaciones diferentes (`float`, `float-slow`, `float-reverse`). Ocultar 1–2 en mobile. Glassmorphism: `bg-white/90 backdrop-blur-xl border border-white/60`.

### Colores de texto en el hero

**Landing principal (hero claro):**

| Elemento | Color |
|---|---|
| H0 / H1 | Negro `#000000` |
| Acento en heading | Red 600 `#E26153` |
| Subtítulo | Negro `#000000` |
| Eyebrow | Gray 400 `#A3A3A3` |

> ❌ Nunca texto blanco en el hero claro del landing principal — el fondo es claro, el contraste sería insuficiente.

**Sublanding (hero oscuro):** el hero arranca con fondo oscuro `#0F1419`, heading en blanco, subtítulo `text-gray-400` y acento `#E26153` solo en texto grande. Tokens completos en `platforms/LANDING.md` §16. En este caso el texto blanco es correcto — el fondo es oscuro.

### Elementos decorativos obligatorios

2 glow blobs posicionados en esquinas opuestas + eyebrow badge glass.

---

## 2. Beneficios

**Propósito:** Explicar el valor diferencial del producto con puntos concretos.

### Layout

Grid de 3 o 4 cards. Evitar 2 columnas — se ve escaso.

```
[Eyebrow]
[H1 — Título de sección]
[Descripción opcional]

[Card 1]  [Card 2]  [Card 3]  [Card 4]
```

### Anatomía de cada card

```
[Ícono en contenedor 52×52px]
[Título de beneficio — H3]
[Descripción — Inter Regular 16px gray-600]
```

**Ícono:** siempre dentro de contenedor de color, nunca suelto.

| Variante | Fondo contenedor | Color ícono |
|---|---|---|
| Rojo | `#FEF4F4` | `#E26153` |
| Gris | `#F8F8F8` | `#4C4C4C` |

> ❌ Prohibidos: azul, verde, violeta, naranja — solo rojo o gris.

**Card:** `rounded-[24px] bg-white shadow-[0_0_25px_2px_rgba(0,0,0,0.06)]` con hover glow rojo sutil al pasar el cursor.

### Elementos decorativos

1 glow blob lateral. Hover glow en cards al pasar el cursor.

---

## 3. Plataforma / Features

**Propósito:** Mostrar las funcionalidades del producto con screenshots reales de la plataforma.

### Layout — Tabs con screenshot

```
[Eyebrow]
[H1 — Título]

[Tab 1]  [Tab 2]  [Tab 3]  [Tab 4]

[Screenshot en browser mockup — activo según tab seleccionado]
[Floating badge contextual]
```

- Tabs: pills `rounded-full`, activo `bg-[#E26153] text-white`, inactivo Oxford hover rojo
- Transición de screenshot: `transition-opacity duration-500` (solo opacidad, nunca `transition-all`)
- Fade del screenshot activo: `opacity-100`, inactivo: `opacity-0 absolute`
- Screenshot en browser mockup + glow radial detrás

### Alternativa — Layout 2 columnas (feature por feature)

Para features que requieren más descripción textual:

```
[Screenshot / ilustración]    [Eyebrow + Título + Descripción + CTA]
[Descripción + CTA]    [Screenshot / ilustración]    ← alternando lado
```

### Elementos decorativos

Dot pattern en fondo `#FFFAFA` + glow radial detrás del mockup.

---

## 4. Métricas / Stats

**Propósito:** Demostrar escala e impacto con números reales.

### Layout

Grid de 3–4 stat cards centradas, o 2×2.

```
[Eyebrow]
[H1 — Título]

[Stat 1]  [Stat 2]  [Stat 3]
```

### Anatomía de cada stat card

```
[Número grande — H0 o display]
[Label descriptivo — Inter Regular gray-600]
[Descripción adicional opcional — Inter Regular 14px gray-500]
```

- Números: `useCountUp` con `IntersectionObserver` para animar al entrar al viewport
- Separador visual entre stats: borde derecho `border-r border-gray-100` (opcional)

### Elementos decorativos

1 glow blob centrado sutil. Hover glow en stat cards.

---

## 5. Social Proof

**Propósito:** Credibilidad mediante logos de clientes o socios.

### Variante A — Marquee de logos

```
[Eyebrow]
[H1 — "Empresas que confían en T1"]

← [Logo] [Logo] [Logo] [Logo] [Logo] [Logo] → (loop infinito)
```

- Logos: `grayscale opacity-40`, hover: `grayscale-0 opacity-80`, transición `duration-300`
- Fades laterales con `mask-image` degradado en ambos extremos
- Duplicar array para loop sin corte visible
- Velocidad: `30s` para 6–8 logos

### Variante B — Grid estático

Para cuando hay pocos logos (3–6) y se prefiere mostrarlos fijos.

```
[Logo 1]  [Logo 2]  [Logo 3]
[Logo 4]  [Logo 5]  [Logo 6]
```

- Mismo tratamiento: `grayscale opacity-40`, hover `grayscale-0 opacity-80`

### Variante C — Testimonios

Cards con quote + nombre + empresa + avatar. Grid de 2–3 columnas o carrusel.

---

## 6. Pasos / Cómo funciona

**Propósito:** Simplificar el proceso de adopción mostrando 3–4 pasos concretos.

### Layout — Horizontal (desktop)

```
[Eyebrow]
[H1 — "Empieza en minutos"]

[① Paso 1]  ──  [② Paso 2]  ──  [③ Paso 3]
```

Pasos conectados por línea horizontal divisora. Cada paso:
```
[Número en círculo — rojo]
[Título del paso — H3]
[Descripción — Inter Regular 14px gray-600]
```

### Layout — Vertical (mobile)

Los pasos colapsan en lista vertical con línea conectora izquierda.

### Alternativa — 2 columnas texto + visual

```
[Texto: Eyebrow + H1 + descripción + pasos numerados]    [Screenshot o ilustración]
```

---

## 7. Pricing / Formas de pago

**Propósito:** Comunicar el modelo de precios o los métodos de pago aceptados.

### Variante A — Cards de planes

```
[Eyebrow]
[H1 — Título de precios]

[Plan Básico]  [Plan Pro — destacado]  [Plan Enterprise]
```

**Card destacada** (plan recomendado): gradient border rojo, glow interno sutil. Ver snippet en `platforms/LANDING.md` §11.

**Cards normales:** `rounded-[24px] bg-white shadow-[0_0_25px_2px_rgba(0,0,0,0.06)]`.

### Variante B — Formas de pago aceptadas

Para T1pagos o T1tienda: grid o marquee de logos de métodos de pago (Visa, Mastercard, SPEI, etc.) con descripción de cada uno.

---

## 8. Ecosistema T1

**Propósito:** Mostrar los 5 productos del ecosistema y su integración. Refuerza el valor de la plataforma completa.

### Layout

Sección oscura con cards de los productos:

```
[fondo oscuro mesh gradient]

[Eyebrow]
[H1 — "Un ecosistema completo"]
[Descripción]

[T1tienda]  [T1envíos]  [T1pagos]  [T1score]  [T1marketing]
  card        card       card —     card        card
                        activa
```

**Cards normales:** `bg-white/[0.04] border border-white/[0.08] backdrop-blur-sm`
**Card activa** (producto actual de la landing): `bg-[#E26153]/[0.06] border-[#E26153]/40`
**Hover:** `hover:bg-white/[0.08] hover:border-white/[0.16]`

### Fondo obligatorio

Nunca `bg-gray-900` plano. Siempre mesh gradient:
```css
background:
  radial-gradient(ellipse at 25% 35%, rgba(226,97,83,0.07), transparent 50%),
  radial-gradient(ellipse at 75% 80%, rgba(33,128,255,0.04), transparent 50%),
  #0f1219;
```
Con overlay de noise al 3%.

---

## 9. FAQ

**Propósito:** Resolver dudas frecuentes y reducir fricción antes de la conversión.

### Layout — 2 columnas (recomendado)

```
[Eyebrow]
[H1 — Preguntas frecuentes]

[Lista de preguntas]    [Panel de respuesta activa]
  → P1 (activa)          [Respuesta visible aquí]
    P2
    P3
    P4
```

### Layout — Accordion (alternativo)

```
[Pregunta 1]  [+]
────────────────────
  Respuesta expandida...
────────────────────
[Pregunta 2]  [+]
[Pregunta 3]  [+]
```

Animación de apertura: `grid-rows-[1fr]` / `grid-rows-[0fr]` + `transition-all duration-300`.
Hover en pregunta: ligero scale up (`hover:scale-[1.01] transition-transform duration-200`) — sin cambio de color.
Contenedor: `max-w-[721px]` centrado (estrecho).

---

## 10. CTA Final

**Propósito:** Cierre de la landing con llamada a la acción principal. Siempre antes del footer.

### Layout

```
[bg-gray-900 rounded-[32px]]

    [Eyebrow]
    [H1 — Mensaje de cierre]
    [Descripción breve]
    
    [CTA primario]  [CTA secundario]
```

- Contenedor: `bg-gray-900` — fondo oscuro full-width, sin border-radius
- Glow interno: `bg-[#E26153]/10 blur-[80px] animate-pulse-soft`
- CTA primario: Red 600 `#E26153`
- CTA secundario: borde blanco, fondo transparente, texto blanco

---

## Footer

**Fondo:** `#000000`

### Desktop

```
[Logo T1]                    | Soluciones        | T1
Descripción breve            | T1tienda          | ¿Qué es T1?
[🔗] [🔗] [🔗] redes        | T1pagos           | Contacto
                              | T1envíos          | Blog
                              | T1score           | Soporte
──────────────────────────────────────────────────────────
[🇲🇽 México (Español)]      [Términos | Privacidad]    [© 2026 T1]
```

- Títulos de columna: Inter SemiBold 11px uppercase `tracking-wider` blanco
- Links: Inter Regular 13px `#9CA3AF` → hover blanco
- Número de columnas: 2 o 3 según el producto (más secciones = 3 columnas)
- WhatsApp FAB: `#25D366 h-14 w-14 rounded-full fixed bottom-6 right-6 z-50`

### Mobile

Stack vertical: Logo → Descripción → Redes → Soluciones → T1 → Legal.
Links: Inter Regular 14px (mayor tap target). Padding: `40px 20px`.

---

## Secciones avanzadas opcionales

Estas secciones aplican en landings más elaboradas o cuando el producto lo requiere.

### Carrusel de casos de uso / testimonios

Para mostrar múltiples casos de negocio con screenshot + copy.

- Altura fija del carrusel — el contenido no debe cambiar el alto del componente al transicionar
- Transición: solo opacidad (`transition-opacity duration-500`), nunca slide
- Auto-rotación: `setInterval` con pausa al hover
- Indicadores: dots o pills de navegación

### Tabs multimedia

Tabs que alternan entre diferentes tipos de contenido: video, screenshot, ilustración.

- Mismas reglas de tabs que la sección Plataforma
- Fade cross entre contenidos, nunca slide

### Demo interactiva / Calculadora

Para productos con ROI demostrable (T1envíos con cotizador, T1pagos con simulador de comisiones).

- Inputs controlados, resultado en tiempo real
- Siempre dentro de card `rounded-[24px] shadow-[0_0_25px_2px_rgba(0,0,0,0.06)]`

### Sticky scroll (horizontal)

Para explicar un proceso con pasos que se revelan en scroll.

- Pin de la sección mientras el usuario scrollea horizontalmente por los pasos
- Solo para desktop — en mobile colapsar a lista vertical

---

## Anti-patrones de layout

| ❌ Anti-patrón | ✅ Alternativa |
|---|---|
| Mismo layout en 3+ secciones consecutivas | Alternar: 2 col → grid 3col → bento → dark → carrusel |
| Hero 50/50 genérico | Dashboard inmersivo + floating badges + glows |
| Screenshot plano sin contenedor | Siempre en browser mockup (dashboard) o phone mockup (mobile) |
| Accordion FAQ simple | 2 col: lista preguntas izq + panel respuesta der |
| Pricing table simétrica | Precio como statement gigante + planes asimétricos |
| Logo wall estático centrado | Marquee animado con fades laterales |
| Badge pill centrado + título centrado | Eyebrow text left-aligned + título left-aligned |
| Fondo oscuro plano (`bg-gray-900`) | Mesh gradient + noise obligatorio |
| Íconos sueltos en cards | Siempre dentro de contenedor de color `52×52px rounded-[14px]` |
| Texto blanco en el hero claro (landing principal) | El hero del landing principal es claro — texto negro, acento rojo. (En sublandings el hero es oscuro: texto blanco es correcto) |
| Glassmorphism sobre fondo blanco | Solo sobre degradado, screenshot o sección oscura |

---

## Checklist QA — Pre-deployment

**Tipografía**
- [ ] H0: Sora Light 300 — únicamente este nivel usa Light
- [ ] H1–H4: Sora Regular 400
- [ ] H5 en adelante: Inter (nunca Sora)
- [ ] Eyebrow: Inter SemiBold 11px uppercase tracking-[0.15em]
- [ ] Acento rojo hereda el peso del título padre
- [ ] Sin Manrope en ninguna parte de la landing

**Colores**
- [ ] Rojo de landing es `#E26153` (Red 600), no `#DB3B2B` (Red 500)
- [ ] Texto en hero es negro, nunca blanco
- [ ] Íconos solo en rojo o gris — sin azul, verde, violeta
- [ ] Texto sobre fondos oscuros: `text-white` o `text-gray-400`

**Layout**
- [ ] Contenedor: `max-w-[1018px]` — nunca `max-w-[1600px]`
- [ ] Al menos 2 secciones con fondo oscuro
- [ ] Layouts visualmente distintos entre secciones consecutivas
- [ ] Títulos left-aligned (no centrados)
- [ ] Padding mínimo por sección: `py-20 tablet:py-28`

**Elementos visuales**
- [ ] Screenshots en browser mockup, nunca planos
- [ ] Floating badges: máximo 3 por sección
- [ ] Glow blob en cada sección
- [ ] `data-animate` en todos los bloques de contenido

**Header y footer**
- [ ] Header: `bg-white/90 backdrop-blur-md`, nunca blanco sólido
- [ ] CTA del header no aparece en la barra mobile, solo en el panel desplegado
- [ ] Footer: fondo `#000000`

**Interactividad**
- [ ] Carruseles: altura fija + transición solo opacidad
- [ ] Tabs: fade, nunca slide
- [ ] Números estadísticos: `useCountUp` con IntersectionObserver
- [ ] Auto-rotación con pause on hover en carruseles

**Performance**
- [ ] `npm run build` sin errores TypeScript
- [ ] Imágenes con `<Image>` de Next.js
- [ ] Logos como SVG inline
- [ ] Sin imports huérfanos
- [ ] Todo contenido en `constants.ts`, nunca hardcodeado en componentes

---

## Referencias cruzadas

- **Tokens de landing** (tipografía, colores, contenedores, botones, sombras, degradados, animaciones) → `platforms/LANDING.md`
- **Diferencias landing vs dashboard** → `platforms/LANDING.md` §Diferencias clave
- **Componentes base** (botones, inputs, badges) → `components/ATOMS.md`
- **Iconografía** → `assets/ICONOGRAPHY.md`
- **Logos de productos T1** → `assets/BRAND-ASSETS.md`
