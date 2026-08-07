# Layout — NEXUS V2.0

> Decisiones estructurales: breakpoints, contenedores, grid, sidebar y comportamiento responsive. Para valores de spacing puros (escala, padding, gap, margin) ver [SPACING.md](./SPACING.md).

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma · **Owner:** Karla Salazar — Head of UX/UI

---

## Breakpoints

| Nombre | Viewport | Tailwind | Nota |
|---|---|---|---|
| **Mobile** | 360px | `mobile:` | Viewport mínimo soportado |
| **Tablet** | 768px | `tablet:` | Tablets y pantallas intermedias |
| **Desktop** | 1280px | `desktop:` | Laptops estándar en adelante |
| **Wide** *(opcional)* | 1920px | `wide:` | Monitores grandes, optimización futura |

Diseño **mobile-first**: los estilos base aplican a mobile, se sobreescriben con `tablet:` y `desktop:`.

> **Nota:** El canvas de diseño en Figma es 1440px, pero el breakpoint de desktop arranca en 1280px para cubrir laptops de usuarios con pantallas más pequeñas (1366px es muy común entre comerciantes).

```js
// Tailwind v4 (@theme inline en globals.css)
screens: {
  mobile: '360px',
  tablet: '768px',
  desktop: '1280px',
  wide: '1920px',  // opcional, para optimizaciones futuras
},
```

---

## Contenedores

### Dashboard

| Propiedad | Desktop | Tablet | Mobile |
|---|---|---|---|
| **Contenedor máximo** | `1600px` | fluid | fluid |
| **Page padding lateral** | `28px` | `24px` | `16px` |
| **Page padding top** | `28px` | `16px` | `16px` |
| **Content gap** (entre bloques) | `28px` | `24px` | `24px` |
| **Altura de title bar** (título + acciones) | `35px` | `35px` | `35px` |

### Landing

| Contenedor | Ancho máximo | Clase Tailwind | Uso |
|---|---|---|---|
| **Principal** | `1018px` | `max-w-[1018px]` | Contenedor por defecto de todas las secciones |
| **Estrecho** | `721px` | `max-w-[721px]` | Hero text, CTA final, FAQ, contenido centrado |
| **Screenshot** | `850px` | `max-w-[850px]` | Capturas/mockups de la plataforma |

Todos centrados con `mx-auto`. Container padding horizontal: `24px` en desktop/tablet, `20px` en mobile.

| Propiedad | Desktop | Tablet | Mobile |
|---|---|---|---|
| **Section padding vertical** | 80–128px (py-20 a py-32) | 64–96px | 48–64px |
| **Content gap** | 24–32px | 20–24px | 16px |

---

## Estructura de página — Dashboard

La página del dashboard se compone de 3 zonas fijas:

```
┌─────────────────────────────────────────────────┐
│                  Header (64px)                   │
├──────────┬──────────────────────────────────────┤
│          │                                      │
│ Sidebar  │          Content Area                │
│ (284px)  │      (resto del viewport)            │
│          │                                      │
│          │                                      │
└──────────┴──────────────────────────────────────┘
```

### Header top bar

Barra fija en la parte superior, siempre visible.

| Propiedad | Valor |
|---|---|
| **Altura** | 64px |
| **Posición** | Fijo en top, full-width |
| **Background** | `#FFFFFF` |
| **Contenido izquierdo** | Logo T1 + producto (T1tienda, T1envíos, etc.) |
| **Contenido centro** | Selector de tienda (avatar + nombre + chevron) |
| **Contenido derecho** | Íconos de acción (grid, ayuda, notificaciones) + avatar de usuario |

> **Detalle del componente:** Ver [../components/ORGANISMS.md](../components/ORGANISMS.md) para estados, responsive y variantes.

---

## Sidebar (dashboard)

| Estado | Ancho | Comportamiento |
|---|---|---|
| **Expandido** | `284px` | Navegación completa con labels |
| **Colapsado** | ~64px | Solo íconos, sin labels |
| **Mobile drawer** | 100% overlay | Aparece desde la izquierda con overlay |

```js
// Token Tailwind
spacing: {
  'sidebar-width': '284px',
},
```

El área de contenido ocupa el espacio restante: `calc(100% - 284px)` en desktop con sidebar expandido.

---

## Grid system

### Dashboard

El dashboard no usa un grid de columnas fijo. Los layouts se construyen con flexbox y CSS grid según la vista:

| Layout | Estructura | Uso |
|---|---|---|
| **Sidebar + Content** | Sidebar fijo + contenido fluid | Layout principal de toda la app |
| **Tabla full-width** | 1 columna, tabla ocupa todo el ancho | Listados de productos, pedidos, envíos |
| **Cards grid** | 2–4 columnas responsive | Dashboard home, métricas, resumen |
| **Master-detail** | 2 columnas (lista + detalle) | Vista de pedido, producto individual |
| **Form layout** | 1–2 columnas | Formularios de creación/edición |

### Landing

Los layouts de landing usan grids variados para crear ritmo visual. Regla: **secciones consecutivas nunca repiten el mismo layout**.

| Tipo | Columnas | Uso |
|---|---|---|
| **Full-width** | 1 col | Hero, CTA final, FAQ |
| **2 columnas** | texto + media | Beneficios, features con screenshot |
| **3 columnas** | 3 cards iguales | Features, pricing, beneficios simples |
| **Grid asimétrico** | 2+1, 1+2, bento | Variedad visual entre secciones |
| **Bento grid** | celdas de diferentes tamaños | Features avanzadas, min 3 max 6-8 celdas |

> **Regla landing:** Al menos 1 celda `col-span-2` en bento grids. No todos `grid-cols-3` simétricos.

---

## Comportamiento responsive

### Sidebar → Drawer

| Breakpoint | Comportamiento |
|---|---|
| Desktop (≥1280px) | Sidebar expandido 284px |
| Tablet (768–1279px) | Sidebar colapsado (solo íconos) |
| Mobile (<768px) | Sidebar oculto → drawer desde hamburguesa |

### Tablas → Cards

En mobile, las tablas de datos se transforman en cards apiladas. Cada fila se convierte en una card con los datos reorganizados verticalmente. Ver [../components/TABLES.md](../components/TABLES.md).

### Grids → Stack

| Desktop | Tablet | Mobile |
|---|---|---|
| 3–4 columnas | 2 columnas | 1 columna (stack) |

### Header (landing)

| Breakpoint | Comportamiento |
|---|---|
| Desktop | Fixed, 70px, `bg-white/90 backdrop-blur-md`, nav completo + botón CTA |
| Mobile | Solo logo + hamburguesa en barra, CTA full-width dentro del panel desplegado |

### Footer (landing)

| Breakpoint | Comportamiento |
|---|---|
| Desktop | 3 columnas sobre `#000000` |
| Mobile | Stack vertical, links 14px para tap targets |

### Landing contenedores con gradiente

En desktop los contenedores con degradado tienen `rounded-[24px]` con márgenes laterales. En mobile (<768px) pierden el border-radius y se vuelven full-width.

```html
<!-- Responsive: rounded en desktop, full-width en mobile -->
<div class="overflow-hidden rounded-none tablet:mx-auto tablet:max-w-[1018px] tablet:rounded-[24px] tablet:px-6"
     style="background: linear-gradient(to bottom, #FFFAFA, #F2B5AE);">
  <div class="px-5 py-10 tablet:p-16"><!-- contenido --></div>
</div>
```

---

## Touch targets

Todos los elementos interactivos en mobile deben tener un área mínima de toque de **44×44px**. Esto incluye botones, links, ítems de sidebar, checkboxes y rows de tabla.

---

## Configuración Tailwind CSS

```js
screens: {
  mobile: '360px',
  tablet: '768px',
  desktop: '1280px',
  wide: '1920px',
},
spacing: {
  'content-gap': '28px',
  'page-padding-desktop': '28px',
  'page-padding-tablet': '24px',
  'page-padding-mobile': '16px',
  'sidebar-width': '284px',
  'header-height': '64px',
},
```

---

## Anti-patrones

- ❌ Usar `max-w-[1600px]` en landing — el contenedor de landing es `1018px`.
- ❌ Usar `max-w-[1018px]` en dashboard — el contenedor de dashboard es `1600px`.
- ❌ Sidebar siempre visible en mobile — debe colapsar a drawer.
- ❌ Diseñar solo para desktop y ajustar mobile después (siempre mobile-first).
- ❌ Botones o áreas tocables menores a 44px en mobile.
- ❌ Tablas que se cortan horizontalmente en mobile sin transformación.
- ❌ Repetir el mismo layout en secciones consecutivas de landing.
- ❌ Usar contenedores centrados sin `mx-auto`.

---

## Referencias

- [SPACING.md](./SPACING.md) — Escala de spacing, tokens de padding/gap/margin
- [ELEVATION.md](./ELEVATION.md) — Shadows y border-radius por componente
- [THEMES.md](./THEMES.md) — Diferencias visuales landing vs dashboard
- [PRINCIPLES.md](./PRINCIPLES.md) — Principio de Adaptabilidad
- [../platforms/LANDING.md](../platforms/LANDING.md) — Layout completo de landing
- [../platforms/DASHBOARD.md](../platforms/DASHBOARD.md) — Layout completo de dashboard
- [../patterns/RESPONSIVE.md](../patterns/RESPONSIVE.md) — Detalle de cómo colapsa cada patrón
