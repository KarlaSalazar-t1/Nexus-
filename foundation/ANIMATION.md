# Animaciones — NEXUS V2.0

> Solo animar `transform` y `opacity`. Nunca `transition-all`. Las animaciones son decorativas en landing y funcionales en dashboard.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma + código de producción · **Owner:** Karla Salazar — Head of UX/UI

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
```

### Tokens de animación

| Clase Tailwind | Keyframe | Duración | Uso |
|---|---|---|---|
| `animate-float` | float | `6s ease-in-out infinite` | Floating badges primarios |
| `animate-float-slow` | float-slow | `8s ease-in-out infinite` | Floating badges secundarios |
| `animate-float-reverse` | float-reverse | `7s ease-in-out infinite` | Floating badges terciarios (dirección inversa) |
| `animate-pulse-soft` | pulse-soft | `4s ease-in-out infinite` | Glow blobs que "respiran" |
| `animate-marquee` | marquee | `30s linear infinite` | Logo wall / social proof marquee |

> **Regla:** Cada floating badge en una sección debe usar una animación diferente (float, float-slow, float-reverse) para evitar movimiento sincronizado.

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

Intervalo recomendado: **6 segundos** entre slides.

---

## Números animados — useCountUp (landing)

Los números en secciones de métricas se animan de 0 al valor final al entrar en viewport.

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
| Velocidad | `30s` para 6-8 logos |
| Dirección | `translateX(0)` → `translateX(-50%)` |
| Loop | Duplicar los logos para seamless loop |
| Fades | Gradientes laterales `from-white via-transparent to-white` |
| Logos | `grayscale opacity-40`, hover: `grayscale-0 opacity-80` |

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
- ❌ Más de 3 floating badges por sección.
- ❌ Stagger con más de 6 elementos o delay mayor a 500ms total.
- ❌ Auto-rotación de carrusel sin pause on hover.
- ❌ Scroll animations sin Intersection Observer (no animar con scroll position directamente).
- ❌ Ignorar `prefers-reduced-motion` — siempre implementar el fallback.
- ❌ Durations mayores a 700ms para transitions — se sienten lentas.
- ❌ Keyframes custom en dashboard — usar transitions CSS simples.

---

## Referencias

- [ELEVATION.md](./ELEVATION.md) — Sombras que participan en hover transitions
- [COLORS.md](./COLORS.md) — Colores de glow blobs y overlays
- [../accessibility/A11Y.md](../accessibility/A11Y.md) — Reducción de movimiento (detalle completo)
- [../platforms/LANDING.md](../platforms/LANDING.md) — Contexto de uso de cada animación
