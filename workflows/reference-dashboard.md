# reference-dashboard.md

> Tokens y patrones exclusivos del **dashboard / admin** T1 / NEXUS V2.0.  
> Versión condensada para context window de Claude.  
> Fuente completa: `components/ORGANISMS.md`, `patterns/DASHBOARD-LAYOUTS.md`.  
> ❌ Nada de este archivo aplica en landing pages.

---

## Regla cardinal

| Token | Dashboard | Landing |
|---|---|---|
| Tipografía | Manrope (todo) | Sora + Inter |
| Rojo primario | `#DB3B2B` (Red 500) | `#E26153` (Red 600) |
| Contenedor | `max-w-[1600px]` | `max-w-[1018px]` |
| Border radius cards | `10px` / `20px` grandes | `24px` |
| Border radius botones | `10px` | `18px` |
| Altura botones | `35px` | `45px` |
| Sombra cards | Flat — sin sombra | `0 0 25px 2px rgba(0,0,0,0.06)` |
| Header BG | Blanco sólido | Glass + blur |
| Fondo global | `white` | `white` + secciones alternadas |
| Rojo en texto | ❌ Se interpreta como error | ✅ Acento decorativo |

---

## Tipografía (Manrope — exclusiva)

**Familia única: Manrope.** Sora e Inter **prohibidas**.  
Line-height: `1.366em` en todos los tamaños.

### Escala de contenido (peso variable)

| Tamaño | Regular 400 | Medium 500 | SemiBold 600 | Bold 700 |
|---|---|---|---|---|
| 20px | Descripciones largas | Table headers, nav | Subtítulos enfáticos | Labels destacados |
| 16px | Cuerpo de texto | Labels de form | Subtítulos de card | Títulos internos |
| 14px | Body, inputs | Labels, placeholders | Botones, tabs activos | Valores destacados |
| 12px | Captions, helper | Badges | Tags enfáticos | Contadores, KPIs |

### Jerarquía de página estándar

```
Título de página:    Manrope Bold 20px      text-oxford
Título de card:      Manrope SemiBold 14px  text-oxford
Labels y metadata:   Manrope Regular 12px   text-gray-500
Body / inputs:       Manrope Regular 14px   text-oxford
Botones:             Manrope SemiBold 14px  text-white / text-oxford
```

### Colores de texto

| Rol | Hex | Uso |
|---|---|---|
| Primary (Oxford) | `#4C4C4C` | Texto principal, body copy |
| Secondary | `#6B7280` | Texto secundario, descripciones |
| Tertiary | `#9CA3AF` | Placeholders, disabled, labels de grupo |
| Inverse | `#FFFFFF` | Sobre fondos de color |

> ❌ Rojo en texto dashboard — se interpreta como error. Usar Oxford para links también.

---

## Shell del dashboard

```
┌──────────────────────────────────────────────────────┐
│  Header (fixed · 100% ancho · h-[48px])              │
├──────────────────┬───────────────────────────────────┤
│                  │                                    │
│  Sidebar         │  Área de contenido                 │
│  (fixed left)    │  max-w-[1600px] · p-6              │
│                  │  scroll vertical                   │
│  Expandido: 184px│                                    │
│  Colapsado:  48px│                                    │
│                  │                                    │
└──────────────────┴───────────────────────────────────┘
```

| Token | Valor |
|---|---|
| Header height | `48px` |
| Sidebar expandido | `184px` |
| Sidebar colapsado | `48px` |
| Contenido max-width | `1600px` |
| Contenido padding | `24px` |
| BG global | `white` |

**Snippet layout base:**

```tsx
export default function DashboardLayout({ children }) {
  const [collapsed, setCollapsed] = useState(false)
  return (
    <div className="min-h-screen bg-white">
      <T1Header collapsed={collapsed} onToggle={() => setCollapsed(!collapsed)} />
      <T1Sidebar collapsed={collapsed} className="fixed left-0 top-[48px] h-[calc(100vh-48px)]" />
      <main className={`pt-[48px] transition-all duration-200 ${collapsed ? 'pl-[48px]' : 'pl-[184px]'}`}>
        <div className="mx-auto max-w-[1600px] p-6">
          {children}
        </div>
      </main>
    </div>
  )
}
```

---

## Header

```
[≡] [Logo producto]  [Selector tienda ∨]  [Búsqueda]  [Saldo $] [⊞] [?] [🔔] [Avatar]
```

- Altura `48px` · BG `white` · borde inferior `gray-200` · **sin sombra**
- Ícono hamburguesa: activa toggle de sidebar
- Selector de tienda: avatar + nombre + chevron (centro)
- Botones de acción (derecha): grid productos, ayuda, notificaciones, avatar usuario

---

## Sidebar

- BG `white` · borde derecho `gray-200` · **sin sombra** · `position: fixed`
- `overflow-x: hidden` siempre
- Transición colapso: `200ms ease` en width

**Estados de nav item:**

| Estado | BG | Text | Indicador |
|---|---|---|---|
| Default | Transparente | Oxford `#4C4C4C` | — |
| Hover | `gray-50` | Oxford | — |
| Active (item con hijos) | Expandido, sin BG propio | Oxford | — |
| Selected (subitem) | `gray-50` | Oxford Bold | — |
| Selected (item sin hijos) | `gray-50` | `red-500` | Borde izq `red-500` 2px |

**Nav item tokens:**

```
Height: 36px  ·  Padding: 12px  ·  Gap ícono–texto: 10px
Border-radius: 8px  ·  Ícono: 20×20px oxford
Subitems: ml-7 (28px), sin ícono
```

**Snippets:**

```tsx
// Item activo
<a className="flex h-[36px] items-center gap-2.5 rounded-[8px] px-3 font-manrope text-[14px] bg-gray-50 border-l-2 border-red-500 text-red-500">
  <Icon className="h-5 w-5 text-red-500" /><span>Inicio</span>
</a>

// Item hover/default
<a className="flex h-[36px] items-center gap-2.5 rounded-[8px] px-3 font-manrope text-[14px] text-oxford hover:bg-gray-50 transition-colors">
  <Icon className="h-5 w-5 text-oxford" /><span>Envíos</span>
</a>

// Subitem activo
<a className="flex h-[34px] items-center rounded-[8px] px-3 ml-7 font-manrope text-[14px] bg-gray-50 text-oxford font-bold">
  Mis envíos
</a>
```

**CTA en sidebar** (solo productos con acción frecuente, ej. T1envíos):
```tsx
// Expandido
<T1Button variant="primary" className="mx-3 w-[calc(100%-24px)]">+ Crear envío</T1Button>
// Colapsado
<button className="mx-auto flex h-[36px] w-[36px] items-center justify-center rounded-[10px] bg-red-500 text-white hover:bg-red-700">
  <PlusIcon className="h-4 w-4" />
</button>
```

**T1pagos colapsado** — excepción visual: íconos en círculo `bg-red-50` con ícono `red-500` (no sobre white).

**T1cuenta** — sin estado colapsado. Sin íconos en items. Labels de grupo en `10px SemiBold uppercase gray-400 tracking-wider`.

---

## Cards

```css
border-radius: 10px;           /* 20px cards grandes */
background: white;
border: 1px solid #E7E7E7;     /* gray-200 */
/* Sin sombra — solo borde */
padding: 16px 20px;            /* p-4 compacto · p-6 detalle */
```

> ❌ No agregar sombra a cards de dashboard — son flat, solo borde.  
> **Excepción: Card Selector** (selected) → `border: 2px red-500` + `shadow: 0 0 4.5px 0.9px #F1B0A9`

---

## Layouts de página

### 1. Dashboard home (KPIs + gráficas)

```tsx
{/* KPIs — grid 4 cols */}
<div className="grid grid-cols-4 gap-4 mb-6">
  {kpis.map(kpi => <T1KPICard key={kpi.id} {...kpi} />)}
</div>

{/* Gráfica 2/3 + panel 1/3 */}
<div className="grid grid-cols-3 gap-4 mb-6">
  <div className="col-span-2"><T1Chart /></div>
  <div className="col-span-1"><T1ActivityPanel /></div>
</div>

{/* Tabla actividad reciente */}
<T1RecentTable />
```

KPI card: label 12px gray-500 · valor 24px Bold oxford · delta verde/rojo 12px · `border border-gray-200 p-4 bg-white rounded-[10px]` · sin sombra.

### 2. Listado con tabla y filtros

```
[Título H1]                              [CTA primario]
[Búsqueda_________] [Filtro ∨] [Filtro ∨] [Filtro ∨]
[Tabla completa]
[Paginación]
```

```tsx
<div className="mb-6 flex items-center justify-between">
  <h1 className="font-manrope text-[24px] font-bold text-oxford">{titulo}</h1>
  <div className="flex items-center gap-2">
    <T1Button variant="secondary">Exportar</T1Button>
    <T1Button variant="primary">Agregar {entidad}</T1Button>
  </div>
</div>
<div className="mb-4 flex items-center gap-2">
  <T1Search className="max-w-[400px]" />
  <div className="ml-auto flex items-center gap-2">
    <T1FilterDropdown label="Estatus" />
    <T1FilterDropdown label="Canal" />
  </div>
</div>
```

### 3. Master-detail

```
┌───────────────────┬──────────────────────────────────┐
│  Lista (w-[320px])│  Detalle del item activo          │
│  [Búsqueda]       │  [Breadcrumb]                     │
│  [Item 1] ←activo │  [Contenido]                      │
│  [Item 2]         │  [Acciones]                       │
└───────────────────┴──────────────────────────────────┘
```

Item activo en lista: `bg-gray-50 border-l-2 border-red-500`  
Transición al cambiar item: fade `opacity duration-200`  
Mobile: lista full-screen → tap → detalle full-screen (no split)

### 4. Detalle de entidad

```
[← Volver a Listado]
[Título H1]                     [Editar · ···]
[Tab 1] [Tab 2] [Tab 3]
────────────────────────────────────────────
[Columna principal 2/3]   [Columna lateral 1/3]
```

```tsx
<div className="grid grid-cols-3 gap-6">
  <div className="col-span-2 flex flex-col gap-4">
    <T1Card>Sección A</T1Card>
    <T1Timeline />
  </div>
  <div className="col-span-1 flex flex-col gap-4">
    <T1Card>Resumen</T1Card>
    <T1Card>Acciones rápidas</T1Card>
  </div>
</div>
```

Tabs: activo `border-b-2 border-red-500 text-oxford font-semibold` · inactivo `text-gray-500 hover:text-oxford`

### 5. Settings — tabs verticales

```
┌───────────────┬───────────────────────────────────────┐
│ Tabs (w-200px)│ Contenido del tab activo               │
│ Mi perfil     │ [Card con formulario]                  │
│ Seguridad     │ [Guardar cambios → derecha]            │
│ Mi tienda ▾   │                                        │
│   · Datos     │                                        │
└───────────────┴───────────────────────────────────────┘
```

Tab activo: `bg-red-50 text-red-500 rounded-[8px] font-semibold`  
Tab inactivo: `text-oxford hover:bg-gray-50 rounded-[8px]`  
Contenido: cards `rounded-[10px] border border-gray-200 p-6 bg-white`

### 6. Wizard multi-paso

```
[← Título]   [Steps: ①──②──③]
┌─────────────────────────┬──────────────────┐
│ Formulario paso actual  │ Resumen (sticky) │
│                         │ Campo: valor     │
│                [Sig →]  │ Total: $XXX      │
└─────────────────────────┴──────────────────┘
```

Steps: completado `bg-red-500 text-white` · activo `border-2 border-red-500 text-red-500` · pendiente `border-2 border-gray-200 text-gray-400`  
CTA siempre sticky al fondo. Validación progresiva: CTA `opacity-50 pointer-events-none` hasta completar campos.

### 7. Página con empty state

```
[Título H1]

[Ilustración opcional]
[Título del empty state]
[Descripción accionable]
[CTA primario centrado]
```

Sin card ni borde — hereda fondo blanco del área de contenido. Ver `patterns/EMPTY-STATES.md`.

---

## Reglas generales del área de contenido

| Regla | Valor |
|---|---|
| Cards — shadow | ❌ Ninguna — solo borde `gray-200` |
| Cards — border-radius | `10px` estándar · `20px` grandes |
| Gap entre cards (grid denso) | `16px` (`gap-4`) |
| Gap entre columnas | `24px` (`gap-6`) |
| Padding card pequeña | `p-4` |
| Padding card detalle | `p-6` |
| Título de página | Manrope Bold 24px oxford |
| Subtítulo dentro de card | Manrope SemiBold 14px oxford |
| Labels y metadata | Manrope Regular 12px gray-500 |
| Contenido y bordes | `p-6` en contenedor — nunca toca el viewport |
