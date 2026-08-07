# Responsive — NEXUS V2.0

> Cómo colapsa cada patrón del sistema por breakpoint. Este archivo es la referencia de implementación responsive — documenta comportamientos específicos, no tokens base.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (`SD---Migration-V2`) · **Owner:** Karla Salazar — Head of UX/UI

> **Breakpoints y contenedores** → `foundation/LAYOUT.md`  
> **Touch targets y spacing** → `foundation/LAYOUT.md` §Touch targets · `foundation/SPACING.md`

---

## Breakpoints del sistema

| Nombre | Viewport | Prefijo Tailwind | Nota |
|---|---|---|---|
| **Mobile** | 360px+ | base (sin prefijo) | Viewport mínimo soportado |
| **Tablet** | 768px+ | `tablet:` | Tablets y pantallas intermedias |
| **Desktop** | 1280px+ | `desktop:` | Laptops estándar en adelante |
| **Wide** | 1920px+ | `wide:` | Opcional — monitores grandes |

**Mobile-first:** los estilos base aplican a mobile, se sobreescriben con `tablet:` y `desktop:`.

---

## Dashboard

### Shell — Header

| Elemento | Desktop | Mobile |
|---|---|---|
| Logo del producto | ✅ visible | ❌ oculto |
| Hamburger | Toggle sidebar | Abre drawer |
| Selector de tienda | Avatar + texto + chevron | Solo avatar + chevron |
| Búsqueda | Input visible en header | Ícono lupa (expande al tap) |
| Saldo (`$`) | ✅ visible | ❌ oculto |
| Notificaciones | ✅ ícono visible | ❌ oculto |
| Ayuda `?` | ✅ ícono visible | ❌ oculto |
| Switch productos `⊞` | ✅ visible | ✅ visible |
| Avatar usuario | ✅ visible | ✅ visible |

**Mobile:** altura `55px` + status bar OS `32px` en `white`. Sin borde inferior. Solo hamburger, switch de productos, avatar de tienda y avatar de usuario.

**Desktop:** altura `48px`, borde inferior `gray-200`, fondo blanco sólido.

### Shell — Sidebar

| Breakpoint | Comportamiento |
|---|---|
| Desktop (≥1280px) | Sidebar fijo expandido `184px` |
| Tablet (768–1279px) | Sidebar colapsado solo íconos `48px` |
| Mobile (<768px) | Sidebar oculto → drawer desde hamburguesa con overlay |

**Drawer mobile:**
- Ancho: `280px` máximo o `85%` del viewport, lo que sea menor
- Contenido: logo del producto en la parte superior + items de navegación completos con ícono y label (igual que sidebar desktop expandido)
- Overlay: `rgba(0,0,0,0.5)` detrás del drawer
- Animación: slide desde la izquierda `duration-200`
- Cierre: tap en overlay o botón X dentro del drawer
- Status bar: `white` — nunca `red-500`

```tsx
{/* Overlay */}
<div
  className={`fixed inset-0 z-40 bg-black/50 transition-opacity duration-200 ${
    drawerOpen ? 'opacity-100' : 'opacity-0 pointer-events-none'
  }`}
  onClick={() => setDrawerOpen(false)}
/>

{/* Drawer — logo del producto + nav completo con íconos y labels */}
<aside className={`fixed left-0 top-0 z-50 h-full w-[280px] bg-white shadow-xl transition-transform duration-200 ${
  drawerOpen ? 'translate-x-0' : '-translate-x-full'
}`}>
  {/* Status bar — siempre blanca en mobile */}
  <div className="h-[32px] bg-white" />
  {/* Logo del producto */}
  <div className="px-4 py-3">
    <T1Logo product={product} />
  </div>
  {/* Navegación completa con íconos y labels */}
  <T1Sidebar />
</aside>
```

### Page Header — Listados

| Elemento | Desktop | Mobile |
|---|---|---|
| Título | Manrope Bold 20px | Manrope Bold 20px |
| CTA primario | Esquina superior derecha | Junto al título (misma fila) |
| Búsqueda | Input `max-w-[400px]` izquierda | Input `flex-1` + botón `···` derecha |
| Filtros | Pills/dropdowns en fila | Fila horizontal scrolleable |
| Exportar/Importar | Botones secundarios visibles | Dentro del botón `···` (meatballs) |

### Tablas → Cards

En mobile las tablas de datos se transforman en cards apiladas. Cada fila de la tabla se convierte en una card con los datos reorganizados verticalmente.

```
Desktop — tabla:                    Mobile — card:
┌────┬────────────┬───────┐        ┌─────────────────────────┐
│ □  │ Nombre     │ SKU   │        │ Nombre del producto      │
├────┼────────────┼───────┤        │ SKU: 123456   Activo ●  │
│ □  │ Prod. A    │ 12345 │   →    │ $1,200 MXN              │
└────┴────────────┴───────┘        │ [Editar]  [···]         │
                                   └─────────────────────────┘
```

**Reglas de la transformación:**
- Los campos más importantes van en la línea superior de la card (nombre, ID)
- Status badge siempre visible
- Precio/valor numérico en línea dedicada
- Acciones (editar, eliminar) como botones al fondo de la card
- Checkbox de selección arriba a la izquierda de la card
- Card: `rounded-[10px] border border-gray-200 p-3 bg-white`

### Grids del dashboard

| Layout | Desktop | Tablet | Mobile |
|---|---|---|---|
| KPI cards home | `grid-cols-4` | `grid-cols-2` | `grid-cols-2` |
| Cards de resumen | `grid-cols-3` | `grid-cols-2` | `grid-cols-1` |
| Gráfica + panel lateral | `grid-cols-3` (2+1) | `grid-cols-1` (apilado) | `grid-cols-1` |
| Master-detail | 2 paneles lado a lado | Panel lista full-width → tap → detalle | Full-screen lista → full-screen detalle |
| Settings tabs | Tabs verticales + contenido | Tabs horizontales arriba + contenido | Tabs horizontales scroll + contenido |
| Formularios CRUD | 2 columnas | 1 columna | 1 columna |

### Wizard / flujo multi-paso

| Elemento | Desktop | Mobile |
|---|---|---|
| Layout | Sidebar dashboard + contenido centrado | Full-screen sin sidebar |
| Indicador de pasos | "Paso N de M" textual | "Paso N de M" textual |
| Panel de resumen | Columna lateral fija derecha | Panel colapsable en bottom bar sticky |
| CTA principal | Posición fija en panel derecho | Sticky bottom full-width |
| Formulario | 2 columnas para campos relacionados | 1 columna |

---

## Landing

### Header

| Elemento | Desktop | Mobile |
|---|---|---|
| Altura | `70px` | `60px` |
| Contenido visible | Logo + nav completo + CTA | Solo logo + hamburger `☰` |
| CTA "Comenzar" | En la barra | **Solo** dentro del panel desplegado, full-width |
| Panel desplegado | No aplica | Links verticales full-width + CTA al fondo |

> El botón CTA **nunca** aparece en la barra mobile. Únicamente dentro del panel expandido como botón full-width.

### Secciones y contenedores

| Elemento | Desktop | Mobile |
|---|---|---|
| Contenedor principal | `max-w-[1018px] px-6` | Full-width `px-5` |
| Contenedor estrecho | `max-w-[721px] px-6` | Full-width `px-5` |
| Section padding vertical | `py-20` a `py-32` | `py-12` a `py-16` |
| Degradado con `rounded` | `rounded-[24px]` con márgenes | `rounded-none` full-width |

**Contenedor con degradado mobile:**
```tsx
<div className="overflow-hidden rounded-none tablet:mx-auto tablet:max-w-[1018px] tablet:rounded-[24px] tablet:px-6"
     style="background: linear-gradient(...)">
  <div className="px-5 py-12 tablet:p-16">
    {/* contenido */}
  </div>
</div>
```

### Secciones específicas

#### Hero

| Elemento | Desktop | Mobile |
|---|---|---|
| Layout | 2 columnas (texto izq + visual der) | 1 columna (texto arriba, visual abajo) |
| Elemento visual | Browser/phone mockup a tamaño completo | Mockup reducido o simplificado |
| Floating badges | 2–3 visibles | Ocultar todos (`hidden tablet:block`) |
| H0 | `54px` | `44px` |

#### Beneficios

| Desktop | Tablet | Mobile |
|---|---|---|
| `grid-cols-3` o `grid-cols-4` | `grid-cols-2` | `grid-cols-1` |

#### Plataforma / Tabs con screenshot

| Elemento | Desktop | Mobile |
|---|---|---|
| Tabs | Fila horizontal | Scroll horizontal o dropdown |
| Screenshot | Tamaño completo con mockup | Reducido, sin floating badges |

#### Métricas / Stats

| Desktop | Tablet | Mobile |
|---|---|---|
| `grid-cols-3` o fila horizontal | `grid-cols-2` | `grid-cols-2` |
| Separador visual entre stats | ✅ | ❌ |

#### Social proof — Marquee

El marquee de logos funciona igual en todos los breakpoints. En mobile reducir la velocidad ligeramente (`35s` vs `30s`) para que sea legible.

#### Pasos / Cómo funciona

| Desktop | Mobile |
|---|---|
| Pasos horizontales conectados | Pasos verticales apilados, línea conectora izquierda |

#### FAQ

| Desktop | Mobile |
|---|---|
| 2 columnas: lista preguntas + panel respuesta | Accordion full-width |

#### Ecosistema T1

| Desktop | Mobile |
|---|---|
| Grid de 5 cards en fila | Grid `2×3` o carrusel horizontal |

#### CTA Final

| Elemento | Desktop | Mobile |
|---|---|---|
| Layout | Centrado con max-width | Full-width con padding lateral |
| Botones | Fila horizontal | Stack vertical full-width |

### Footer (landing)

| Desktop | Mobile |
|---|---|
| 3 columnas lado a lado | Stack vertical (1 columna) |
| Links Inter 13px | Links Inter 14px (mayor tap target) |
| Fila legal horizontal | Stack vertical |

---

## Reglas universales

### Touch targets

Todo elemento interactivo en mobile debe tener área mínima de toque **44×44px**. Aplica a:

- Botones e íconos de acción
- Links de navegación
- Items del sidebar/drawer
- Checkboxes y radio buttons
- Rows de tabla (convertidas a cards)
- Pills de filtro (altura mínima `44px` en mobile, aunque visualmente sean `30px` — usar padding)

```tsx
// Ícono pequeño con touch target adecuado
<button className="flex h-[44px] w-[44px] items-center justify-center">
  <ChevronDownIcon className="h-4 w-4 text-oxford" />
</button>
```

### Filtros horizontales en mobile

Los filtros en listados mobile van en una fila con scroll horizontal. Sin wrap.

```tsx
<div className="flex items-center gap-2 overflow-x-auto pb-1 [-webkit-overflow-scrolling:touch]">
  {filters.map(filter => (
    <button key={filter.id} className="shrink-0 ...">
      {filter.label}
    </button>
  ))}
</div>
```

### Imágenes y screenshots responsive

```tsx
// Screenshot siempre con Next.js Image
<Image
  src="/screenshot.png"
  alt="Dashboard T1tienda"
  width={800}
  height={500}
  className="w-full h-auto rounded-[10px]"
  priority={isAboveFold}
/>
```

### Animaciones en mobile

- Reducir o eliminar `animate-float` en floating badges en mobile para evitar distracción en pantallas pequeñas
- `data-animate` scroll animations: mantener en mobile, reducir `translateY` de `28px` a `16px`
- Carruseles: misma lógica, pero considerar swipe touch además de los dots/flechas

### Tipografía responsive — Dashboard

El dashboard usa Manrope en todos los breakpoints. No hay cambios de tamaño tipográfico entre desktop y mobile en el dashboard — el layout cambia, la escala tipográfica no.

### Tipografía responsive — Landing

Los headings de landing sí cambian de tamaño entre breakpoints:

| Nivel | Mobile | Desktop |
|---|---|---|
| H0 | `44px` | `54px` |
| H1 | `28px` | `40px` |
| H2 | `26px` | `35px` |
| H3 | `20px` | `24px` |
| H4 | `16px` | `20px` |
| Body | `14px` | `16px` |

---

## Anti-patrones

| ❌ Evitar | ✅ En cambio |
|---|---|
| Sidebar visible en mobile | Drawer con overlay y hamburger |
| Tabla horizontal con scroll en mobile | Transformar filas en cards apiladas |
| Touch targets menores a 44px | Padding invisible para aumentar el área |
| CTA del header visible en barra mobile | Solo en panel desplegado |
| Floating badges visibles en mobile | `hidden tablet:block` |
| `rounded-[24px]` en contenedores full-width mobile | `rounded-none` en mobile, `rounded-[24px]` en `tablet:` |
| Grids de 3–4 columnas en mobile | Colapsar a 1–2 columnas |
| Botones en fila en mobile para CTA final | Stack vertical full-width |
| Imágenes sin `<Image>` de Next.js | Siempre `<Image>` con `width` y `height` definidos |
| Diseñar solo desktop y ajustar mobile después | Mobile-first: base styles para mobile, sobreescribir con `tablet:` |

---

## Referencias cruzadas

- **Breakpoints y contenedores** → `foundation/LAYOUT.md`
- **Spacing y touch targets** → `foundation/SPACING.md`
- **Shell del dashboard (header + sidebar)** → `components/ORGANISMS.md` §1–7, §10–11
- **Tablas → cards en mobile** → `components/TABLES.md`
- **Secciones de landing** → `patterns/LANDING-SECTIONS.md`
- **Layouts del dashboard** → `patterns/DASHBOARD-LAYOUTS.md`
- **Tokens de landing** → `platforms/LANDING.md`
- **Tokens de dashboard** → `platforms/DASHBOARD.md`
