# Dashboard Layouts — NEXUS V2.0

> Patrones de composición de páginas para el área de contenido del dashboard. Documenta cómo se organiza el contenido dentro del shell (header + sidebar) según el tipo de vista.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (`SD---Migration-V2`) · **Owner:** Karla Salazar — Head of UX/UI

> **Shell del dashboard** (header, sidebar, layout base) → `components/ORGANISMS.md` §1–7  
> **Tokens de dashboard** (tipografía Manrope, colores, contenedor 1600px) → `platforms/DASHBOARD.md`

---

## Índice

1. [Shell base](#1-shell-base)
2. [Dashboard home — KPIs + gráficas](#2-dashboard-home--kpis--gráficas)
3. [Listado — tabla con filtros](#3-listado--tabla-con-filtros)
4. [Master-detail](#4-master-detail)
5. [Detalle de entidad](#5-detalle-de-entidad)
6. [Settings — tabs verticales](#6-settings--tabs-verticales)
7. [Wizard multi-paso](#7-wizard-multi-paso)
8. [Página con empty state](#8-página-con-empty-state)

---

## 1. Shell base

Todo el contenido del dashboard vive dentro del shell: header fijo en la parte superior + sidebar fijo a la izquierda. El área de contenido es lo único que scrollea.

```
┌──────────────────────────────────────────────────────────┐
│  Header (fixed · 100% ancho · h-[48px])                  │
├─────────────────┬────────────────────────────────────────┤
│                 │                                        │
│  Sidebar        │  Área de contenido                     │
│  (fixed left)   │  max-w-[1600px] · p-6                  │
│                 │  scroll vertical                        │
│  Expandido:     │                                        │
│  184px          │                                        │
│  Colapsado:     │                                        │
│  48px           │                                        │
│                 │                                        │
└─────────────────┴────────────────────────────────────────┘
```

| Token | Valor |
|---|---|
| Header height | `48px` |
| Sidebar expandido | `184px` |
| Sidebar colapsado | `48px` |
| Contenido `max-width` | `1600px` |
| Contenido `padding` | `24px` |
| Fondo global | `white` |

Ver estructura completa del shell → `components/ORGANISMS.md` §1–7.

---

## 2. Dashboard home — KPIs + gráficas

**Cuándo usar:** Página de inicio de cada producto. Vista general del estado del negocio.

### Estructura

```
[Page title — H1]

[KPI card 1]  [KPI card 2]  [KPI card 3]  [KPI card 4]
────────────────────────────────────────────────────────
[Gráfica principal — ancho completo o 2/3]   [Panel lateral 1/3]
────────────────────────────────────────────────────────
[Tabla de actividad reciente — ancho completo]
```

### KPI cards

Grid de 3–4 cards en la fila superior. Cada card:

```
[Label — Manrope Regular 12px gray-500]
[Valor principal — Manrope Bold 24px oxford]
[Delta vs período anterior — verde/rojo 12px]
```

- `rounded-[10px]` · `border border-gray-200` · `p-4` · `bg-white`
- Sin shadow — solo borde `gray-200`
- Delta positivo: `text-green-500` con flecha ↑ · Delta negativo: `text-red-700` con flecha ↓

### Gráfica principal

Ocupa 2/3 del ancho restante. Panel lateral (actividad, resumen, lista corta) ocupa 1/3.

- Contenedor: `rounded-[10px] border border-gray-200 p-4 bg-white`
- Título: Manrope SemiBold 14px oxford
- Sin shadow en el contenedor de la gráfica

### Tabla de actividad reciente

Versión simplificada de la tabla completa. 5–10 filas más recientes con link "Ver todo" que lleva al listado completo.

### Grid

```tsx
{/* KPIs */}
<div className="grid grid-cols-4 gap-4 mb-6">
  {kpis.map(kpi => <T1KPICard key={kpi.id} {...kpi} />)}
</div>

{/* Gráfica + panel */}
<div className="grid grid-cols-3 gap-4 mb-6">
  <div className="col-span-2">
    <T1Chart />
  </div>
  <div className="col-span-1">
    <T1ActivityPanel />
  </div>
</div>

{/* Tabla reciente */}
<T1RecentTable />
```

---

## 3. Listado — tabla con filtros

**Cuándo usar:** Cualquier módulo que muestra una colección de entidades (productos, pedidos, envíos, clientes, transacciones).

### Estructura

```
[Page title — H1]                    [CTA primario — Agregar entidad]

[Búsqueda___________] [Exportar] [Importar] [Más opciones ∨]

[Filtro 1 ∨]  [Filtro 2 ∨]  [Filtro 3 ∨]  [Filtro 4 ∨]

[Tabla de datos]
  [Header: checkbox | Col 1 | Col 2 | Col 3 | Col 4 | ···]
  [Fila 1]
  [Fila 2]
  [Fila N]

[Paginación: < 1 2 3 ... N > | Items por página: 25 ∨]
```

### Cabecera de página

```tsx
<div className="mb-6 flex items-center justify-between">
  <h1 className="font-manrope text-[20px] font-bold text-oxford">
    {titulo}
  </h1>
  <div className="flex items-center gap-2">
    {/* Botones secundarios opcionales */}
    <T1Button variant="secondary">Exportar</T1Button>
    <T1Button variant="secondary">Importar</T1Button>
    {/* CTA primario */}
    <T1Button variant="primary">Agregar {entidad}</T1Button>
  </div>
</div>
```

### Barra de búsqueda y filtros

```tsx
<div className="mb-4 flex items-center gap-2">
  <T1Search placeholder="Buscar por código, nombre..." className="max-w-[400px]" />
  <div className="ml-auto flex items-center gap-2">
    <T1FilterDropdown label="Estatus" options={...} />
    <T1FilterDropdown label="Canal de venta" options={...} />
    <T1FilterDropdown label="Categoría" options={...} />
  </div>
</div>
```

### Reglas

- El CTA primario siempre en la esquina superior derecha de la cabecera
- La búsqueda va a la izquierda de los filtros; los filtros a la derecha
- Filtros activos se muestran como pills con `×` para remover individualmente
- Cuando hay items seleccionados: aparece barra de selección con contador + acciones masivas
- Ver documentación completa de tablas → `components/TABLES.md`
- Ver patrones de búsqueda y filtrado → `patterns/FLOWS.md` §7

---

## 4. Master-detail

**Cuándo usar:** Cuando el usuario necesita explorar una lista y ver el detalle de cada item sin cambiar de página (ej: bandeja de mensajes, gestión de incidencias, lista de pedidos con preview).

### Estructura

```
┌───────────────────────┬─────────────────────────────────┐
│  Panel izquierdo      │  Panel derecho                   │
│  (lista)              │  (detalle del item activo)        │
│                       │                                   │
│  [Búsqueda]           │  [Breadcrumb o título]            │
│  [Item 1] ←activo     │  [Contenido del detalle]          │
│  [Item 2]             │                                   │
│  [Item 3]             │  [Acciones: Editar · Eliminar]   │
│  ...                  │                                   │
└───────────────────────┴─────────────────────────────────┘
```

### Proporciones

| Panel izquierdo | Panel derecho |
|---|---|
| `w-[320px]` fijo | Ocupa el resto del área de contenido |

### Comportamiento

- El panel izquierdo tiene scroll propio — el panel derecho también scrollea de forma independiente
- El item activo en la lista: `bg-gray-50 border-l-2 border-red-500`
- Transición al cambiar de item: fade `opacity` en el panel derecho (`duration-200`)
- En mobile: la lista ocupa toda la pantalla → tap en item → navega a vista de detalle full-screen (no split)

---

## 5. Detalle de entidad

**Cuándo usar:** Vista dedicada de un solo objeto (un pedido, un envío, un producto específico). El usuario llegó desde un listado o desde un link directo.

### Estructura

```
[← Volver a Listado]

[Título de la entidad — H1]    [Acciones: Editar · ··· ]

[Tab 1]  [Tab 2]  [Tab 3]  (cuando hay múltiples secciones)
──────────────────────────────────────────────────────────
[Contenido del tab activo]

  Columna principal (2/3)          Columna lateral (1/3)
  ─────────────────────            ──────────────────────
  Sección de datos A               Resumen / metadata
  Sección de datos B               Acciones rápidas
  Historial / Timeline             Estado actual
```

### Breadcrumb / navegación de regreso

```tsx
<div className="mb-4 flex items-center gap-2">
  <button
    onClick={router.back}
    className="flex items-center gap-1 font-manrope text-[13px] text-gray-500 hover:text-oxford"
  >
    <ArrowLeftIcon className="h-4 w-4" />
    Volver a {nombreListado}
  </button>
</div>
```

### Layout de columnas

```tsx
<div className="grid grid-cols-3 gap-6">
  {/* Columna principal */}
  <div className="col-span-2 flex flex-col gap-4">
    <T1Card>Sección A</T1Card>
    <T1Card>Sección B</T1Card>
    <T1Timeline />
  </div>
  {/* Columna lateral */}
  <div className="col-span-1 flex flex-col gap-4">
    <T1Card>Resumen</T1Card>
    <T1Card>Acciones rápidas</T1Card>
  </div>
</div>
```

### Tabs de detalle

Cuando la entidad tiene muchas secciones, usar tabs horizontales debajo del título:

- Tab activo: `border-b-2 border-red-500 text-oxford font-semibold`
- Tab inactivo: `text-gray-500 hover:text-oxford`
- Transición de contenido: fade `opacity` (`duration-200`)

---

## 6. Settings — tabs verticales

**Cuándo usar:** Módulos de configuración con múltiples categorías (T1 Cuenta, configuración de tienda, perfil de usuario).

### Estructura

```
[Page title — H1]

┌─────────────────┬────────────────────────────────────────┐
│  Tabs verticales│  Contenido del tab activo               │
│                 │                                         │
│  Mi perfil      │  [Subtítulo de sección]                 │
│  Región/idioma  │  [Formulario o contenido]               │
│  Seguridad      │                                         │
│  Mi tienda ▾    │  [CTA: Guardar cambios]                 │
│   · Datos       │                                         │
│   · Métodos     │                                         │
│   · Roles       │                                         │
│   · Sucursales  │                                         │
│  Planes ▾       │                                         │
└─────────────────┴────────────────────────────────────────┘
```

### Panel de tabs

- Ancho: `200px` fijo, sin shadow, sin borde derecho visible (el contenido activo define el límite visual)
- Tab activo: `bg-red-50 text-red-500 rounded-[8px] font-semibold`
- Tab inactivo: `text-oxford hover:bg-gray-50 rounded-[8px]`
- Grupos con subtítulo: label de sección en Manrope SemiBold 11px uppercase `gray-400 tracking-wider`
- Subitems: indentados `pl-4`, sin ícono, misma tipografía que tabs normales

### Panel de contenido

- `flex-1` — ocupa el espacio restante
- Cada sección de settings en su propia card: `rounded-[10px] border border-gray-200 p-6 bg-white`
- CTA "Guardar cambios" siempre al final del formulario, alineado a la derecha
- Cambios no guardados: banner de alerta `T1Message` variante `caution` en la parte superior del panel

### Grid

```tsx
<div className="flex gap-6">
  {/* Tabs verticales */}
  <nav className="w-[200px] shrink-0">
    <T1VerticalTabs sections={settingsSections} activeTab={activeTab} />
  </nav>
  {/* Contenido */}
  <div className="flex-1 min-w-0">
    {activeSection.component}
  </div>
</div>
```

---

## 7. Wizard multi-paso

**Cuándo usar:** Flujos de creación que requieren múltiples pasos secuenciales y/o validación progresiva (crear envío, configuración inicial de módulo, alta de integración).

### Estructura desktop

```
[Header dashboard estándar]
[Sidebar dashboard estándar]

Área de contenido:
┌────────────────────────────────────────────────────────┐
│  [← Título del wizard]                                 │
│  [Steps: ①──②──③]  o  "Paso N de M"                   │
├──────────────────────────────────┬─────────────────────┤
│  Formulario del paso actual      │  Panel de resumen    │
│                                  │  (sticky)            │
│  [Sección A]                     │                      │
│  ──────────────────              │  Origen:  ...        │
│  [Sección B]                     │  Destino: ...        │
│                                  │  Paquete: ...        │
│                          [Sig →] │  Total:   $XXX       │
└──────────────────────────────────┴─────────────────────┘
```

### Estructura mobile

Full-screen sin sidebar. Header simplificado con back + título + "Paso N de M". Panel de resumen colapsable en bottom bar sticky.

Ver documentación completa del Wizard → `components/ORGANISMS.md` §10.

### Reglas

- Navegación solo lineal — el usuario puede ir al paso anterior, no saltar pasos
- CTA siempre sticky al fondo — nunca se pierde en el scroll
- Panel de resumen: fijo en desktop, colapsable en mobile
- Validación progresiva: CTA deshabilitado (`opacity-50 pointer-events-none`) hasta completar todos los campos requeridos del paso actual
- Indicador de pasos: "Paso N de M" textual en desktop y mobile — no hay steps visuales horizontales

---

## 8. Página con empty state

**Cuándo usar:** Un módulo que el usuario aún no ha configurado o donde no hay datos disponibles.

### Estructura

```
[Page title — H1]
[Subtítulo o descripción opcional]

┌──────────────────────────────────────────────────────┐
│                                                      │
│                                                      │
│         [Ilustración contextual — opcional]          │
│                                                      │
│         [Título del empty state]                     │
│         [Descripción accionable]                     │
│                                                      │
│                  [CTA primario]                      │
│                                                      │
│                                                      │
└──────────────────────────────────────────────────────┘
```

El contenedor del empty state ocupa el área disponible de la página. No tiene card ni borde propio — hereda el fondo blanco del área de contenido.

Ver patrones completos de empty states → `patterns/EMPTY-STATES.md`.

---

## Reglas generales del área de contenido

- **Sin shadow en cards del dashboard** — solo borde `1px solid gray-200`
- **Border-radius de cards:** `10px` cards estándar · `20px` cards grandes (KPI prominente, card de saldo)
- **Gap entre cards:** `16px` (`gap-4`) para grids densos · `24px` (`gap-6`) para layouts de columnas
- **Padding de sección:** `p-4` cards pequeñas · `p-6` cards de detalle
- **Títulos de página:** Manrope Bold 20px `text-oxford`
- **Subtítulos de sección dentro de card:** Manrope SemiBold 14px `text-oxford`
- **Labels y metadata:** Manrope Regular 12px `text-gray-500`
- **El contenido nunca toca los bordes del viewport** — siempre `p-6` en el contenedor `max-w-[1600px]`

---

## Referencias cruzadas

- **Shell (header + sidebar)** → `components/ORGANISMS.md` §1–7
- **Tablas de datos con filtros** → `components/TABLES.md`
- **Empty states por módulo** → `patterns/EMPTY-STATES.md`
- **Flujos de wizard y CRUD** → `patterns/FLOWS.md`
- **Tokens de dashboard** → `platforms/DASHBOARD.md`
- **Notificaciones (banners en dashboard)** → `patterns/NOTIFICATIONS.md`
