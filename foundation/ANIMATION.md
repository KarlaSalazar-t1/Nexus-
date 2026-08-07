# Animaciones — NEXUS V2.0

> Solo animar `transform` y `opacity`. Nunca `transition-all`. Las animaciones son decorativas en landing y funcionales en dashboard.

**Última actualización:** Mayo 2026 · **Versión:** 2.2.0 · **Fuente de verdad:** Figma + código de producción + t1landing.vercel.app · **Owner:** Karla Salazar — Head of UX/UI

---

## ⚠️ Cambios v2.2.0 (mayo 2026)

Ajustes derivados del refactor a filosofía catálogo de landing:

- **`useCountUp` ahora es OPCIONAL en Stats Counter.** La sección en producción muestra valores fijos (`+25 mil / +$25 B / +40 M`) sin animación de conteo. La animación queda como mejora opcional según preferencia del producto. Los keyframes `count-tick` y el hook siguen disponibles para quien quiera usarlos. Ver `LANDING-SECTIONS.md §5` para criterios de cuándo usar cada variante.
- **Video loop multi-escena** sigue siendo válido pero como **variante A.2 del hero**, no como única variante obligatoria. La landing principal en producción usa video único (variante A.1). Patrón técnico documentado abajo en §Video loop crossfade.
- **Carrusel paginado** añadido como patrón formal (Section Stack producto variante A, Bento IA variante A): auto-play 6-10s, transición solo opacidad `transition-opacity duration-500` entre slides (nunca slide horizontal), pause on hover, click manual en dot rompe auto-play permanente.
- Resto de keyframes y patrones (de v2.1.0) siguen vigentes: `progress`, `count-tick`, `shimmer`, Sticky Scroll Stack, Card Stack flotante, Tabs verticales auto-play, Marquee multi-velocidad.

---

## Cambios v2.1.0 (referencia histórica)

Keyframes y patrones agregados originalmente con el rediseño de landing — todos siguen vigentes en v2.2.0:

- `progress` — barra de progreso para tabs verticales con auto-play 5s
- `count-tick` — pulso sutil al cambiar de dígito en stats counter
- `shimmer` — placeholder de carga para inputs de IA
- Patrón **Sticky Scroll Stack** — cards apiladas con `position: sticky` + z-index incremental
- Patrón **Card Stack flotante** — 2-4 cards flotantes con animaciones desfasadas alrededor de phone mockup
- Patrón **Video loop crossfade** — videos hero alternándose con `transition-opacity duration-700`
- Patrón **Tabs verticales auto-play** — interval 5s con pause on hover y break permanente al click manual
- Marquee multi-velocidad: `30s` para 6-8 logos, `40s` para 9+, `35s` para casos de éxito sobre fondo oscuro

---

## Regla fundamental

Solo se animan dos propiedades CSS: **transform** y **opacity**. Esto garantiza rendimiento (GPU-accelerated) y evita reflows costosos.

```css
/* ✅ Correcto */
transition: opacity 0.5s ease, transform 0.5s ease;

/* ❌ Prohibido */
transition: all 0.3s ease;
transition: height 0.3s ease;
transition: width 0.3s ease;
```

---

## Dashboard vs Landing

| Aspecto | Dashboard | Landing |
|---|---|---|
| **Filosofía** | Funcional — transitions rápidas para feedback | Decorativa — animaciones que crean impacto visual |
| **Keyframes** | No usa keyframes custom | 5 keyframes obligatorios |
| **Scroll animations** | No | Sí, con `data-animate` |
| **Hover en cards** | Cambio de sombra/border sutil | `-translate-y-1.5` + sombra + glow |
| **Durations** | 150–300ms | 300–700ms |
| **Easing** | `ease` estándar | `cubic-bezier(0.16, 1, 0.3, 1)` (spring) |

---

## Keyframes del sistema (landing)

Agregar al CSS global:

```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-12px); }
}

@keyframes float-slow {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}

@keyframes float-reverse {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(10px); }
}

@keyframes pulse-soft {
  0%, 100% { opacity: 0.35; transform: scale(1); }
  50% { opacity: 0.55; transform: scale(1.05); }
}

@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* === v2.1.0 — keyframes para tabs verticales, stats y placeholders IA === */

@keyframes progress {
  0% { transform: scaleX(0); transform-origin: left; }
  100% { transform: scaleX(1); transform-origin: left; }
}

@keyframes count-tick {
  0%, 100% { transform: translateY(0); opacity: 1; }
  50% { transform: translateY(-2px); opacity: 0.85; }
}

@keyframes shimmer {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}
```

### Tokens de animación

| Clase Tailwind | Keyframe | Duración | Uso |
|---|---|---|---|
| `animate-float` | float | `6s ease-in-out infinite` | Floating badges primarios + cards flotantes en Section Stack |
| `animate-float-slow` | float-slow | `8s ease-in-out infinite` | Floating badges secundarios + cards en Section Stack |
| `animate-float-reverse` | float-reverse | `7s ease-in-out infinite` | Floating badges terciarios (dirección inversa) + cards en Section Stack |
| `animate-pulse-soft` | pulse-soft | `4s ease-in-out infinite` | Glow blobs que "respiran" |
| `animate-marquee` | marquee | `30s linear infinite` | Logo wall / social proof — 6-8 logos |
| `animate-marquee-slow` | marquee | `40s linear infinite` | Logo wall denso — 9+ logos |
| `animate-progress` | progress | `5s linear forwards` | Barra de progreso bajo tab activo en Tabs Verticales |
| `animate-count-tick` | count-tick | `200ms ease-out` | Pulso al cambiar dígito en useCountUp |
| `animate-shimmer` | shimmer | `2s linear infinite` | Placeholder de carga en input IA del bento |

> **Regla:** Cada floating badge en una sección debe usar una animación diferente (float, float-slow, float-reverse) para evitar movimiento sincronizado. Lo mismo aplica para las 3-4 cards flotantes alrededor del phone mockup en Section Stack — cada una con un keyframe distinto.

---

## Scroll animations (landing)

Todos los bloques de contenido en landing se animan al entrar al viewport usando Intersection Observer.

### Implementación

```html
<div data-animate>contenido que aparece al hacer scroll</div>
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

### Variantes

| Atributo | Efecto | Uso |
|---|---|---|
| `data-animate` (default) | Fade up desde 28px abajo | Bloques de contenido estándar |
| `data-animate="slide-right"` | Fade in desde la derecha | Elementos que entran lateralmente |
| `data-animate="scale"` | Fade in desde más pequeño | Screenshots, mockups |

### Stagger (aparición escalonada)

Para grids de cards, cada card aparece con un delay incremental:

```tsx
{items.map((item, i) => (
  <div
    data-animate
    style={{ transitionDelay: `${i * 80}ms` }}
  >
    {/* card content */}
  </div>
))}
```

Delay recomendado: **80ms** entre elementos. Máximo 5-6 elementos con stagger antes de que se sienta lento.

---

## CSS transitions

### Durations estándar

| Duration | Uso | Contexto |
|---|---|---|
| **150ms** | Hover de botones, toggles | Dashboard |
| **300ms** | Transiciones de estado, accordion, tabs | Ambos |
| **500ms** | Hover de cards, fade entre slides | Landing |
| **700ms** | Scroll animations, aparición de secciones | Landing |

### Easing curves

| Easing | Valor | Uso |
|---|---|---|
| **Default** | `ease` | Transitions básicas de dashboard |
| **Spring** | `cubic-bezier(0.16, 1, 0.3, 1)` | Scroll animations, apariciones landing |
| **Ease-out cubic** | `1 - Math.pow(1 - progress, 3)` | useCountUp, números animados (JS) |
| **Linear** | `linear` | Marquee, rotaciones continuas |

---

## Micro-interacciones

### Hover en cards (landing)

```html
<div class="group relative overflow-hidden rounded-[24px] bg-white p-8
            shadow-[0_0_25px_2px_rgba(0,0,0,0.06)]
            transition-all duration-500
            hover:-translate-y-1.5
            hover:shadow-[0_20px_50px_rgba(0,0,0,0.08)]">
  <!-- Glow decorativo -->
  <div class="pointer-events-none absolute -top-10 -right-10 h-24 w-24
              rounded-full opacity-0 blur-[30px]
              transition-opacity duration-500 group-hover:opacity-100"
       style="background: rgba(226,97,83,0.08);">
  </div>
  <div class="relative z-10"><!-- contenido --></div>
</div>
```

### Accordion FAQ (landing)

Usa `grid-template-rows` para una animación suave de apertura/cierre:

```css
/* Cerrado */
.accordion-content {
  display: grid;
  grid-template-rows: 0fr;
  transition: grid-template-rows 300ms ease;
}

/* Abierto */
.accordion-content.open {
  grid-template-rows: 1fr;
}

.accordion-content > div {
  overflow: hidden;
}
```

### Tabs / fade transition (landing)

Los paneles de tabs se apilan con `absolute` y transicionan solo opacidad:

```html
<div class="relative h-[400px]">
  {panels.map((panel, i) => (
    <div
      key={i}
      class={`absolute inset-0 transition-opacity duration-500
              ${i === active ? 'opacity-100 z-10' : 'opacity-0 z-0'}`}
    >
      {panel}
    </div>
  ))}
</div>
```

---

## Carruseles estables (landing)

Los carruseles con contenido de altura variable son propensos a "flash" o colapso durante transiciones. Patrón obligatorio:

1. Contenedor exterior con **altura fija** (`h-[360px]` o similar)
2. Todos los slides se apilan con `absolute inset-0`
3. Transición es **solo opacity** (`transition-opacity duration-500`)
4. NUNCA transicionar `transform`, `scale` o `height` en carruseles
5. Fondos/gradientes en divs separados con `absolute inset-0 -z-10`

### Auto-rotación con pause on hover

```tsx
useEffect(() => {
  if (isPaused) return;
  const interval = setInterval(goNext, 6000);
  return () => clearInterval(interval);
}, [isPaused, goNext]);

// En el contenedor:
<div
  onMouseEnter={() => setIsPaused(true)}
  onMouseLeave={() => setIsPaused(false)}
>
```

### Intervalos recomendados según tipo de carrusel

| Tipo de carrusel | Intervalo | Por qué |
|---|---|---|
| Tabs verticales con auto-play | **5s** | Cada tab tiene poco contenido, lectura rápida |
| Carrusel paginado Section Stack producto (v2.2.0 A) | **8-10s** | Mockup desktop + mobile + descripción, requiere asimilación |
| Carrusel paginado Bento IA features (v2.2.0 A) | **6-8s** | Componente interactivo por slide, necesita tiempo de apreciación |
| Carrusel testimonios / casos éxito | **6s** | Quote + atribución, lectura media |
| Logos marquee (continuo, no paginado) | N/A — loop infinito 30-40s | No es carrusel paginado, es scroll continuo |

### Reglas para carruseles paginados (v2.2.0)

Aplican a **Section Stack producto variante A** y **Bento IA variante A**:

- Paginación visible: dots, pills numerados, o contador `N / M` minimalista
- Click manual en dot rompe auto-play **permanentemente** (no se reactiva)
- Pause on hover **obligatorio**
- Transición entre slides: **solo opacidad**, nunca slide horizontal
- Indicador del slide activo: peso o color distinto, no solo opacidad de dot
- En mobile: paginación se mantiene visible, pero el contenido del slide colapsa a stack vertical

---

## Números animados — useCountUp (landing)

> **v2.2.0:** `useCountUp` es **opcional**, no obligatorio. La landing principal en producción muestra valores fijos sin animación de conteo. Ver `LANDING-SECTIONS.md §5` para criterios de cuándo usar cada variante (sin animación recomendado para números aspiracionales redondos; con animación para números ultra-precisos donde la magnitud merece énfasis).

Cuando se decide usar la animación: los números en secciones de métricas se animan de 0 al valor final al entrar en viewport.

```tsx
function useCountUp(target, duration = 2000) {
  const [count, setCount] = useState(0);
  const [hasTriggered, setHasTriggered] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting && !hasTriggered) {
        setHasTriggered(true);
        const start = performance.now();
        const animate = (now) => {
          const progress = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
          setCount(Math.round(eased * target));
          if (progress < 1) requestAnimationFrame(animate);
        };
        requestAnimationFrame(animate);
      }
    }, { threshold: 0.5 });

    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, [target, duration, hasTriggered]);

  return { count, ref };
}
```

Formatos soportados: enteros con separador de miles (`25,000`), decimales (`99.9%`), moneda (`$25.4B`), prefijo + (`+85%`).

---

## Marquee de logos (landing)

Logo wall animado con scroll continuo:

| Propiedad | Valor |
|---|---|
| Velocidad estándar | `30s` para 6-8 logos |
| Velocidad densa | `40s` para 9+ logos |
| Velocidad casos éxito (oscuro) | `35s` |
| Dirección | `translateX(0)` → `translateX(-50%)` |
| Loop | Duplicar los logos para seamless loop |
| Fades | Gradientes laterales `mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent)` |
| Logos sobre claro | `grayscale opacity-40`, hover: `grayscale-0 opacity-80` |
| Logos sobre oscuro (casos éxito) | `text-white opacidad 60`, hover: `text-white opacidad 100` |

---

## v2.1.0 — Patrones avanzados de landing

### Sticky Scroll Stack

Cards apiladas que se quedan pegadas al scroll mientras la siguiente card aparece desde abajo. Crea sensación de acumulación visual.

```jsx
<section className="relative">
  {cards.map((card, i) => (
    <div
      key={i}
      className="lg:sticky"
      style={{
        top: `${80 + i * 16}px`,    // 80px base + 16px offset acumulado
        zIndex: i + 10,               // z-index incremental para apilamiento correcto
        marginBottom: '20vh',
      }}
    >
      <Card data={card} />
    </div>
  ))}
</section>
```

**Reglas:**
- Mínimo 3, máximo 4 cards
- `position: sticky` solo desde `lg:` — en mobile colapsa a stack normal (el sticky en pantalla chica satura)
- `top` con offset `80 + i * 16` para que cada card se vea ligeramente bajo la anterior
- `z-index` incremental — la card más reciente queda encima
- Animación interna de cada card al entrar al viewport con `data-animate` y stagger

### Card Stack flotante (Section Stack)

Phone mockup central + 2-4 cards flotantes alrededor, cada una con un keyframe de flotación distinto para evitar movimiento sincronizado.

```jsx
<div className="relative">
  <PhoneMockup className="mx-auto" />

  <div className="absolute top-[10%] left-[8%] animate-float">
    <FloatingCard variant="order" />
  </div>
  <div className="absolute top-[35%] right-[5%] animate-float-slow rotate-[3deg]">
    <FloatingCard variant="package" />
  </div>
  <div className="absolute bottom-[20%] left-[12%] animate-float-reverse rotate-[-2deg]">
    <FloatingCard variant="payment" />
  </div>
  <div className="absolute bottom-[8%] right-[10%] animate-float">
    <FloatingCard variant="badge" />
  </div>
</div>
```

**Reglas:**
- Mínimo 2, máximo 4 cards flotantes — más se vuelve caótico
- Rotaciones leves entre `-3deg` y `+3deg` para diagonal natural
- Cada card con `animate-float`, `animate-float-slow`, o `animate-float-reverse` — nunca repetir
- Glow Red 200 detrás del mockup (nunca encima): `bg-[#F1B0A9]/40 blur-[120px]`
- En mobile: cards pasan a stack vertical bajo el mockup, mantener animate-float

### Video loop crossfade (hero — variante A.2)

> **v2.2.0:** este patrón corresponde a la **variante A.2 del hero** documentada en `LANDING-SECTIONS.md §1`. No es la única variante de hero. La landing principal en producción usa **variante A.1 — Hero con video único** (un solo `/img/hero.mp4`), que no requiere crossfade. Usa este patrón solo cuando elijas explícitamente la variante multi-escena.

Cuando se decide usar la variante A.2: 4 videos que cician cada ~5s con crossfade suave. **Solo opacidad** se anima — nunca scale/transform.

```jsx
const videos = ['/img/hero-1.mp4', '/img/hero-2.mp4', '/img/hero-3.mp4', '/img/hero-4.mp4'];
const preheaders = ['Vende online', 'Cobra al instante', 'Gestiona envíos', 'Crece con datos'];

const [active, setActive] = useState(0);

useEffect(() => {
  const interval = setInterval(() => {
    setActive((prev) => (prev + 1) % videos.length);
  }, 5000);
  return () => clearInterval(interval);
}, []);

return (
  <div className="relative aspect-[4/3] overflow-hidden rounded-[24px]">
    {videos.map((src, i) => (
      <video
        key={src}
        src={src}
        autoPlay
        muted
        loop
        playsInline
        className={`absolute inset-0 h-full w-full object-cover transition-opacity duration-700
                    ${i === active ? 'opacity-100' : 'opacity-0'}`}
      />
    ))}
  </div>
);
```

**Reglas:**
- `transition-opacity duration-700` — nunca `transition-all`, nunca scale, nunca translate
- Comprimir cada video <2MB con ffmpeg (`-crf 28 -preset slow`)
- `playsInline muted autoPlay loop` obligatorios
- Preheader sincronizado con índice activo (mismo índice = misma copy)
- Aspect ratio fijo (`4/3` o `16/9`) — el contenedor no debe cambiar de tamaño entre videos

### Tabs verticales con auto-play + barra de progreso

Auto-rotación cada 5s con barra de progreso visible, pause on hover, break permanente al click manual.

```jsx
const [activeTab, setActiveTab] = useState(0);
const [isPaused, setIsPaused] = useState(false);
const [userInteracted, setUserInteracted] = useState(false);

useEffect(() => {
  if (isPaused || userInteracted) return;
  const interval = setInterval(() => {
    setActiveTab((prev) => (prev + 1) % tabs.length);
  }, 5000);
  return () => clearInterval(interval);
}, [isPaused, userInteracted]);

const handleTabClick = (i) => {
  setActiveTab(i);
  setUserInteracted(true); // rompe el auto-play permanentemente
};

return (
  <div
    onMouseEnter={() => setIsPaused(true)}
    onMouseLeave={() => setIsPaused(false)}
  >
    {tabs.map((tab, i) => (
      <button onClick={() => handleTabClick(i)}>
        <span>{tab.title}</span>
        {i === activeTab && (
          <div
            key={`progress-${activeTab}`}  // KEY cambia → animación se reinicia
            className="h-[2px] bg-[#E26153] origin-left animate-progress"
          />
        )}
      </button>
    ))}
  </div>
);
```

**Reglas:**
- Interval de 5000ms — más rápido se siente atropellado, más lento aburre
- Pause on hover obligatorio (`onMouseEnter` / `onMouseLeave`)
- **Click manual rompe auto-play permanente** — UX pattern: si el usuario interactuó, no le quites control. Algunos diseñadores prefieren reanudar tras 30s; aquí se queda detenido.
- La barra de progreso usa `key` que cambia con `activeTab` para que React la remonte y reinicie la animación
- `animate-progress` con `animation-duration: 5s linear forwards` (mismo tiempo que el interval)

### Card Stack on Scroll (entrada secuencial)

Cards de bento o lifestyle entran al viewport con stagger:

```jsx
{cards.map((card, i) => (
  <div
    key={i}
    data-animate
    style={{ transitionDelay: `${i * 100}ms` }}
  >
    <Card data={card} />
  </div>
))}
```

Stagger de 100ms entre cards — el ojo percibe el orden sin sentir lentitud.

---

## Dashboard — Transitions básicas

El dashboard usa transitions CSS simples sin keyframes custom.

| Interacción | Transition | Duración |
|---|---|---|
| Hover de botón | `background-color` | `150ms ease` |
| Hover de row en tabla | `background-color` | `150ms ease` |
| Apertura de sidebar | `width` | `300ms ease` |
| Toggle switch | `transform` (translate) | `150ms ease` |
| Dropdown apertura | `opacity` + `transform` (scale) | `200ms ease` |
| Loading skeleton | Shimmer gradient animado | `1.5s linear infinite` |
| Focus ring | `box-shadow` | `150ms ease` |

---

## Reducción de movimiento

Respetar `prefers-reduced-motion: reduce` del sistema operativo.

| Animación | Normal | Con reduce |
|---|---|---|
| Fade de sección | Opacity 0→1, 300ms | Mostrar directamente |
| Slide de modal/drawer | Translate + fade, 250ms | Mostrar directamente |
| Spinner de carga | Rotación continua | Spinner estático o texto "Cargando..." |
| Carrusel autoplay | Transición cada 6s | Detener autoplay, solo navegación manual |
| Smooth scroll | Desplazamiento animado | Scroll instantáneo |
| Skeleton shimmer | Animación wave | Fondo estático |
| Hover scale en cards | `scale(1.02)` | Solo cambio de sombra/borde |
| `data-animate` en landing | Slide + fade al viewport | Mostrar directamente |
| Floating badges | Float continuo | Estáticos en posición |

**Pueden mantenerse activas:** barras de progreso con valor real, cambio de estado de toggles, aparición de mensajes de error/éxito inline (son informativas, no decorativas).

```css
@media (prefers-reduced-motion: reduce) {
  [data-animate] {
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }

  .animate-float,
  .animate-float-slow,
  .animate-float-reverse,
  .animate-pulse-soft {
    animation: none !important;
  }

  .animate-marquee {
    animation: none !important;
  }
}
```

---

## Anti-patrones

- ❌ Usar `transition-all` — siempre especificar las propiedades exactas.
- ❌ Animar `height`, `width`, `top`, `left` — solo `transform` y `opacity`.
- ❌ Transicionar `transform` o `scale` en carruseles — solo `opacity`.
- ❌ Floating badges con la misma animación — cada uno debe usar un keyframe diferente.
- ❌ Más de 4 floating badges por sección (incluye cards flotantes en Section Stack).
- ❌ Stagger con más de 6 elementos o delay mayor a 500ms total.
- ❌ Auto-rotación de carrusel o tabs sin pause on hover.
- ❌ Scroll animations sin Intersection Observer (no animar con scroll position directamente).
- ❌ Ignorar `prefers-reduced-motion` — siempre implementar el fallback.
- ❌ Durations mayores a 700ms para transitions — se sienten lentas.
- ❌ Keyframes custom en dashboard — usar transitions CSS simples.
- ❌ **(v2.1.0)** Sticky scroll en mobile sin desactivar — usar `lg:sticky` para que solo aplique desde 1024px.
- ❌ **(v2.1.0)** Video loop con scale, translate o blur — solo crossfade de opacidad.
- ❌ **(v2.1.0)** Tabs verticales sin barra de progreso visible — el usuario necesita ver el avance del auto-play.
- ❌ **(v2.1.0)** Tabs verticales que reanudan auto-play tras click manual — una vez que el usuario interactuó, el control queda con él.
- ❌ **(v2.1.0)** Cards flotantes en Section Stack todas con la misma animación — desfasarlas siempre.
- ❌ **(v2.1.0)** Sticky Scroll Stack con cards idénticas — cada card debe tener acento o glow distinto.

---

## Referencias

- [ELEVATION.md](./ELEVATION.md) — Sombras que participan en hover transitions
- [COLORS.md](./COLORS.md) — Colores de glow blobs y overlays
- [../accessibility/A11Y.md](../accessibility/A11Y.md) — Reducción de movimiento (detalle completo)
- [../platforms/LANDING.md](../platforms/LANDING.md) — Contexto de uso de cada animación
