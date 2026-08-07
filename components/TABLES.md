# TABLES — NEXUS V2.0 Design System

> **Categoría:** components  
> **Contexto:** Dashboard exclusivamente — las tablas no aplican en landing  
> **Fuente:** Figma `Tablas - taxonomia` (`hnhSOWk8b7k8KyeggJh6fS`)  
> **Última actualización:** 2025  
> **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Anatomía de la tabla base](#1-anatomía-de-la-tabla-base)
2. [Header de tabla](#2-header-de-tabla)
3. [Filas](#3-filas)
4. [Tipos de celda](#4-tipos-de-celda)
5. [Toolbar de tabla](#5-toolbar-de-tabla)
6. [Filtros](#6-filtros)
7. [Paginación](#7-paginación)
8. [Variantes especiales](#8-variantes-especiales)
9. [Mobile — Cards](#9-mobile--cards)
10. [Skeleton loading](#10-skeleton-loading)
11. [Empty state](#11-empty-state)

---

## Convenciones

- Todas las tablas son de **dashboard** — nunca en landing.
- Los colores se referencian por token de `foundation/COLORS.md`.
- Tipografía base de tablas: **Manrope Medium 12px** — nunca Inter.
- El archivo Figma `Tablas - taxonomia` contiene +25 tablas reales del ecosistema T1. Este MD documenta la estructura y los patrones compartidos — no cada tabla individualmente.

---

## 1. Anatomía de la tabla base

Toda tabla del sistema comparte esta estructura vertical:

```
┌─────────────────────────────────────────────┐
│  Toolbar (título + acciones + búsqueda)      │
├─────────────────────────────────────────────┤
│  Filtros (pills de estado, fecha, etc.)      │
├────────┬────────┬────────┬────────┬──────────┤
│ Col A  │ Col B  │ Col C  │ Col D  │  ...     │  ← Header
├────────┼────────┼────────┼────────┼──────────┤
│ dato   │ dato   │ dato   │ dato   │  ...     │  ← Fila
├────────┼────────┼────────┼────────┼──────────┤
│ dato   │ dato   │ dato   │ dato   │  ...     │
├────────┴────────┴────────┴────────┴──────────┤
│  Paginación                                  │
└─────────────────────────────────────────────┘
```

### Tokens base de la tabla

| Elemento | Token | Valor |
|---|---|---|
| BG tabla | `white` | `#FFFFFF` |
| BG header | `blue-100` | `#F0F8FF` |
| Border general | `gray-200` | `#E7E7E7` |
| BG fila hover | `gray-50` | `#F8F8F8` |
| BG fila seleccionada | `gray-50` | `#F8F8F8` |
| Texto header | `gray-600` | `#9CA3AF` |
| Texto celda principal | `oxford` | `#4C4C4C` |
| Texto celda secundario | `gray-600` | `#9CA3AF` |
| Separador entre filas | `gray-200` | `#E7E7E7` |

---

## 2. Header de tabla

El header identifica cada columna con su label y permite ordenamiento.

### 2.1 Especificaciones

```css
background-color: var(--color-blue-100);   /* #F0F8FF */
height: 40px;
padding: 0 12px;
font-family: Manrope;
font-size: 10px;
font-weight: 600;       /* SemiBold */
color: var(--color-gray-600);   /* #9CA3AF */
text-transform: uppercase;
letter-spacing: 0.05em;
border-bottom: 1px solid var(--color-gray-200);
```

### 2.2 Sorting

Las columnas ordenables siempre muestran el ícono de **dos chevrons apilados** (↑↓) junto al label — ambas flechas visibles en todo momento, no se muestran por separado. El estado activo se indica cambiando el color del ícono completo.

| Estado | Visual |
|---|---|
| **Sin ordenar** | `⌃⌄` (chevron arriba + abajo) en `gray-400` |
| **Activo (cualquier dirección)** | `⌃⌄` en `oxford` |

> ⚠️ **No** mostrar solo `↑` o solo `↓` según la dirección — siempre se muestran los dos chevrons juntos.

### 2.3 Snippet

```tsx
<thead>
  <tr className="bg-blue-100">
    {columns.map(col => (
      <th
        key={col.key}
        onClick={() => col.sortable && handleSort(col.key)}
        className={`px-3 py-2.5 text-left font-manrope text-[10px] font-semibold uppercase tracking-wider text-gray-600 ${
          col.sortable ? 'cursor-pointer select-none hover:text-oxford' : ''
        }`}
      >
        <div className="flex items-center gap-1">
          {col.label}
          {col.sortable && (
            // Siempre se muestran los dos chevrons juntos — nunca solo uno
            <ChevronUpDownIcon className={`h-3 w-3 ${
              sort.key === col.key ? 'text-oxford' : 'text-gray-400'
            }`} />
          )}
        </div>
      </th>
    ))}
  </tr>
</thead>
```

---

## 3. Filas

### 3.1 Fila estándar

| Estado | BG | Descripción |
|---|---|---|
| **Default** | `white` | Estado base |
| **Hover** | `gray-50` | Al pasar el cursor |
| **Seleccionada** | `gray-50` | Con checkbox activo — mismo BG que hover |

```css
/* Fila base */
height: 56px;
padding: 0 12px;
border-bottom: 1px solid var(--color-gray-200);
font-family: Manrope;
font-size: 12px;
font-weight: 500;
```

### 3.2 Fila expandible (acordeón)

Usada en **Productos** y **Pedidos** — la fila padre se puede expandir para mostrar subfilas de detalle.

**Toggle del acordeón:**
- `∧` (chevron arriba) → expandido — las subfilas están visibles
- `∨` (chevron abajo) → colapsado — las subfilas están ocultas

> ⚠️ El chevron **no apunta a la derecha** al estar colapsado — siempre apunta arriba (expandido) o abajo (colapsado).

**Fila padre:**
- Texto en `oxford` Medium 12px
- Chevron `∧/∨` en `gray-600`
- Label de variantes: `N variantes ∨` como texto + chevron inline

**Subfilas (filas hijas):**
- Indentación izquierda: `32px`
- BG: `gray-50` para diferenciarse de la fila padre
- Borde izquierdo: `2px solid gray-200`
- Mismo height que fila estándar (`56px`)

```tsx
{/* Fila padre expandible */}
<tr className="cursor-pointer hover:bg-gray-50 border-b border-gray-200">
  <td className="px-3 py-3">
    <div className="flex items-start gap-3">
      {/* contenido de fila */}
      <button
        onClick={() => toggleRow(row.id)}
        className="mt-1 flex items-center gap-1 font-manrope text-[11px] text-oxford hover:underline"
      >
        {row.variants} variantes
        {/* Chevron arriba si expandido, abajo si colapsado */}
        <ChevronUpIcon className={`h-3 w-3 transition-transform ${!expanded ? 'rotate-180' : ''}`} />
      </button>
    </div>
  </td>
</tr>

{/* Subfilas */}
{expanded && row.variants.map(variant => (
  <tr key={variant.id} className="bg-gray-50 border-b border-gray-200">
    <td className="py-2 pl-10 pr-3 border-l-2 border-gray-200">
      {/* contenido de variante */}
    </td>
  </tr>
))}
```

### 3.3 Checkbox de selección y barra de acciones masivas

Las tablas con selección múltiple tienen una primera columna con checkbox (`width: 40px`).

Cuando una o más filas están seleccionadas, el **header de columnas se reemplaza** por una barra de acciones masivas:

| Elemento | Descripción |
|---|---|
| **Ícono rojo** | Cuadrado `red-500` con guión — click deselecciona todo |
| **Contador** | "Seleccionados: N" · Manrope Medium 12px · `oxford` |
| **Acciones masivas** | `button/secondary` **h-[30px]** por cada acción disponible (ej: "Edición masiva") |
| **Meatballs `···`** | `button/icon` **h-[30px] w-[30px]** que agrupa acciones adicionales en un submenu cuando son muchas |

> **Tamaño de controles en barra masiva: 30px** — igual que los filtros, más pequeños que los botones estándar del sistema (35px).

```tsx
{selectedRows.length > 0 ? (
  // Barra de selección — reemplaza el header de columnas
  <div className="flex h-[40px] items-center justify-between bg-blue-100 px-3 border-b border-gray-200">
    <div className="flex items-center gap-3">
      <button
        onClick={clearSelection}
        className="flex h-4 w-4 items-center justify-center rounded-[2px] bg-red-500"
      >
        <MinusIcon className="h-2.5 w-2.5 text-white" />
      </button>
      <span className="font-manrope text-[12px] font-medium text-oxford">
        Seleccionados: {selectedRows.length}
      </span>
    </div>
    <div className="flex items-center gap-2">
      {/* Botones de acción masiva — altura 30px, más pequeños que controles estándar */}
      <T1Button variant="secondary" className="h-[30px] text-[12px]">Edición masiva</T1Button>
      <button className="flex h-[30px] w-[30px] items-center justify-center rounded-[10px] border border-gray-200 bg-white hover:bg-gray-50">
        <EllipsisHorizontalIcon className="h-4 w-4 text-oxford" />
      </button>
    </div>
  </div>
) : (
  // Header normal de columnas
  <thead>...</thead>
)}

---

## 4. Tipos de celda

Las celdas de la tabla no son texto plano — cada columna usa un tipo de celda específico.

### 4.1 Texto simple

Texto con una o dos líneas.

```tsx
<td className="px-3 py-3">
  <span className="font-manrope text-[12px] font-medium text-oxford">{value}</span>
</td>

// Con texto secundario debajo
<td className="px-3 py-3">
  <p className="font-manrope text-[12px] font-medium text-oxford">{primary}</p>
  <p className="font-manrope text-[11px] text-gray-600">{secondary}</p>
</td>
```

### 4.2 Producto (imagen + nombre + metadatos)

Celda compleja usada en tablas de productos y pedidos.

```tsx
<td className="px-3 py-3">
  <div className="flex items-start gap-3">
    <img src={img} className="h-10 w-10 rounded-[4px] object-cover" />
    <div className="flex flex-col gap-0.5">
      <span className="font-manrope text-[12px] font-medium text-oxford line-clamp-2">{name}</span>
      <span className="font-manrope text-[11px] text-gray-600">{sku}</span>
      {variants && (
        <button className="flex items-center gap-1 text-[11px] text-oxford hover:underline">
          {variants} variantes <ChevronDownIcon className="h-3 w-3" />
        </button>
      )}
    </div>
  </div>
</td>
```

### 4.3 Badge de estado

Chip de color que indica el estado del registro.

```tsx
// Estados comunes en tablas T1
const statusStyles = {
  'Activo':                 'bg-green-100 text-green-700',
  'En camino':              'bg-blue-100 text-blue-500',
  'Pendiente de pago':      'bg-orange-100 text-orange-700',
  'Por preparar':           'bg-orange-100 text-orange-700',
  'Por enviar':             'bg-orange-100 text-orange-700',
  'Parcialmente preparado': 'bg-orange-100 text-orange-700',
  'Entregado':              'bg-green-100 text-green-700',
  'Cancelado':              'bg-red-50 text-red-700',
  'Devolución':             'bg-purple-100 text-purple-700',
}

<td className="px-3 py-3">
  <span className={`inline-flex rounded-[4px] px-2 py-0.5 font-manrope text-[11px] font-medium ${statusStyles[status]}`}>
    {status}
  </span>
</td>
```

### 4.4 Canal de venta (logo + nombre)

Ícono del canal con su nombre. Cada canal tiene un logo/color propio.

```tsx
<td className="px-3 py-3">
  <div className="flex items-center gap-2">
    <img src={channel.logo} className="h-4 w-4 object-contain" />
    <span className="font-manrope text-[12px] text-oxford">{channel.name}</span>
  </div>
</td>
```

Canales soportados: T1 Tienda en línea, Punto de venta, Amazon, Mercado Libre, Shein, TikTok Shop, Shopify.

### 4.5 Precio / Monto

```tsx
// Precio simple
<td className="px-3 py-3 text-right">
  <span className="font-manrope text-[12px] font-medium text-oxford">${price}</span>
</td>

// Rango de precio (cuando hay variantes)
<td className="px-3 py-3 text-right">
  <span className="font-manrope text-[12px] text-oxford">${min} - ${max}</span>
</td>
```

### 4.6 Fecha / Tiempo relativo

```tsx
<td className="px-3 py-3">
  <p className="font-manrope text-[12px] font-medium text-oxford">{relativeTime}</p>
  <p className="font-manrope text-[11px] text-gray-600">{absoluteDate}</p>
</td>
```

Ejemplos: "Hoy · 2:24 hrs", "Ayer · 3:04 hrs", "01 jul · 5:34 hrs"

### 4.7 Seguimiento / Guías

Badge con número de guía de envío o chip de "N envíos".

```tsx
// Chip de guía
<td className="px-3 py-3">
  <span className="inline-flex items-center gap-1 rounded-[4px] bg-yellow-100 px-2 py-0.5 font-manrope text-[11px] font-medium text-oxford">
    📦 {trackingNumber}
  </span>
</td>

// Chip de envíos múltiples
<td className="px-3 py-3">
  <button className="flex items-center gap-1 font-manrope text-[12px] text-oxford hover:underline">
    {n} envíos <ChevronDownIcon className="h-3 w-3" />
  </button>
</td>
```

### 4.8 Inventario / Conteo con ratio

```tsx
<td className="px-3 py-3">
  <p className="font-manrope text-[12px] font-medium text-oxford">{qty} unidades</p>
  <p className="font-manrope text-[11px] text-gray-600">{available}/{total}</p>
  {isLow && (
    <p className="font-manrope text-[11px] text-red-700">⚠ {qty} unidades</p>
  )}
</td>
```

### 4.9 Celda editable (tabla Precios)

Celda de input inline para edición directa — exclusiva de la tabla de Precios.

```tsx
<td className={`relative px-3 py-3 ${isEditing ? 'bg-white ring-2 ring-inset ring-gray-400' : ''}`}>
  {isEditing ? (
    <input
      autoFocus
      value={value}
      onChange={e => setValue(e.target.value)}
      onBlur={handleSave}
      className="w-full bg-transparent font-manrope text-[12px] font-medium text-oxford focus:outline-none"
    />
  ) : (
    <button
      onClick={() => setEditing(true)}
      className="w-full text-left font-manrope text-[12px] font-medium text-oxford hover:text-black"
    >
      ${value}
    </button>
  )}
  {/* Drag handle para fill-down */}
  {isEditing && (
    <div
      className="absolute bottom-0 right-0 h-2 w-2 cursor-s-resize bg-red-500"
      onMouseDown={handleDragStart}
    />
  )}
</td>
```

### 4.10 Acciones (menú ···)

Última columna con botón de acciones contextuales.

```tsx
<td className="px-3 py-3 text-right">
  <div className="relative">
    <button
      onClick={() => setMenuOpen(true)}
      className="rounded-[4px] p-1 hover:bg-gray-100"
    >
      <EllipsisHorizontalIcon className="h-4 w-4 text-gray-600" />
    </button>
    {menuOpen && <T1Submenu items={rowActions} onClose={() => setMenuOpen(false)} />}
  </div>
</td>
```

---

## 5. Toolbar de tabla

Área superior que contiene el título de la sección, búsqueda y acciones principales.

### 5.1 Estructura

```
[Título]                    [Acción secundaria] [Acción primaria]
[Búsqueda___________] [Ordenar ▼] [↑↓]        [Más opciones ▼]
```

### 5.2 Elementos

| Elemento | Especificación |
|---|---|
| **Título** | Manrope Bold 24px · `oxford` |
| **Búsqueda** | Input estándar · placeholder "Búsqueda por código, nombre, SKU…" · ícono lupa |
| **Ordenar** | Dropdown con campo de ordenamiento + botón ↑↓ para dirección |
| **Acciones primarias** | `button/primary` (ej: "Agregar producto", "Crear pedido") |
| **Acciones secundarias** | `button/secondary` (ej: "Exportar", "Importar") |
| **Más opciones** | Dropdown con acciones adicionales (ej: "Personalizar vista", "Ver estadísticas") |

### 5.3 Snippet

```tsx
<div className="mb-4">
  {/* Fila de título + acciones */}
  <div className="mb-4 flex items-center justify-between">
    <h1 className="font-manrope text-[24px] font-bold text-oxford">{title}</h1>
    <div className="flex items-center gap-2">
      <T1Button variant="secondary">Exportar</T1Button>
      <T1Button variant="secondary">Importar</T1Button>
      <T1Button variant="primary">Agregar producto</T1Button>
    </div>
  </div>

  {/* Fila de búsqueda + ordenamiento */}
  <div className="flex items-center gap-3">
    <T1Search placeholder="Búsqueda por código, nombre, SKU…" className="flex-1" />
    <T1Dropdown label="Ordenar" options={sortOptions} />
    <button className="flex h-[35px] w-[35px] items-center justify-center rounded-[10px] border border-gray-200 hover:bg-gray-50">
      <ArrowsUpDownIcon className="h-4 w-4 text-oxford" />
    </button>
    <T1Button variant="secondary">Más opciones</T1Button>
  </div>
</div>
```

---

## 6. Filtros

Fila de pills/dropdowns debajo del toolbar para filtrar el contenido de la tabla.

> **Tamaño de controles:** Los pills de filtro y dropdowns de esta fila tienen **altura de 30px** — más pequeños que los controles estándar del sistema (35px). Aplica también a los botones de la barra de acciones masivas.

### 6.1 Tipos de filtro

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Pill dropdown** | Click abre menú de opciones con checkboxes | "Estado ∨", "Fecha ∨", "Categoría ∨" |
| **Pill seleccionado** | Pill con valor aplicado — borde `red-500` · BG `red-50` | "Estado: Activo ×" |
| **Añadir filtro** | Botón `+` para agregar más columnas de filtro | "Añadir filtro +" |
| **Eliminar filtros** | Link de limpieza al haber filtros aplicados | "Eliminar productos prueba 🗑" |

### 6.2 Snippet

```tsx
<div className="flex items-center gap-2 flex-wrap">
  {activeFilters.map(filter => (
    <button
      key={filter.key}
      // height 30px — más pequeño que controles estándar (35px)
      className="flex h-[30px] items-center gap-1 rounded-[10px] border border-red-500 bg-red-50 px-3 font-manrope text-[12px] font-medium text-oxford"
    >
      {filter.label}: {filter.value}
      <XMarkIcon className="h-3 w-3" onClick={() => removeFilter(filter.key)} />
    </button>
  ))}

  {availableFilters.map(filter => (
    <button
      key={filter.key}
      className="flex h-[30px] items-center gap-1 rounded-[10px] border border-gray-200 bg-white px-3 font-manrope text-[12px] font-medium text-oxford hover:bg-gray-50"
    >
      {filter.label} <ChevronDownIcon className="h-3 w-3" />
    </button>
  ))}

  <button className="flex h-[30px] items-center gap-1 font-manrope text-[12px] text-oxford hover:underline">
    <PlusIcon className="h-3 w-3" /> Añadir filtro
  </button>
</div>
```

---

## 7. Paginación

Solo se muestra cuando la tabla tiene **más de 50 registros**. Con 50 o menos, todos los registros se muestran en una sola página sin controles de paginación.

### 7.1 Estructura

```
En total 23,456 registro(s)  ‹  1  2  3  4  5  ...  68  ›   20 registros / página ▼   Saltar a página  [___]  ›
```

### 7.2 Especificaciones

| Elemento | Especificación |
|---|---|
| **Contador** | "En total N registro(s)" · Manrope Regular 12px · `oxford` |
| **Página activa** | Círculo relleno `red-500` · texto `white` · `24×24px` |
| **Páginas inactivas** | Texto `oxford` · hover BG `gray-50` |
| **Puntos suspensivos** | `...` en `gray-600` — cuando hay muchas páginas |
| **Flechas** | `‹` `›` — prev/next · disabled en primera/última página |
| **Registros por página** | Dropdown: 10 / 20 / 50 / 100 registros por página |
| **Saltar a página** | Input numérico + botón `›` |

### 7.3 Snippet

```tsx
<div className="flex items-center justify-between border-t border-gray-200 px-4 py-3">
  {/* Contador */}
  <span className="font-manrope text-[12px] text-oxford">
    En total {total.toLocaleString()} registro(s)
  </span>

  {/* Páginas */}
  <div className="flex items-center gap-1">
    <button
      onClick={() => setPage(p => Math.max(1, p - 1))}
      disabled={page === 1}
      className="flex h-6 w-6 items-center justify-center rounded-[4px] hover:bg-gray-50 disabled:text-gray-400"
    >‹</button>

    {pages.map(p => (
      <button
        key={p}
        onClick={() => setPage(p)}
        className={`flex h-6 w-6 items-center justify-center rounded-full font-manrope text-[12px] ${
          p === page
            ? 'bg-red-500 text-white'
            : 'text-oxford hover:bg-gray-50'
        }`}
      >
        {p}
      </button>
    ))}

    <button
      onClick={() => setPage(p => Math.min(totalPages, p + 1))}
      disabled={page === totalPages}
      className="flex h-6 w-6 items-center justify-center rounded-[4px] hover:bg-gray-50 disabled:text-gray-400"
    >›</button>
  </div>

  {/* Registros por página + saltar */}
  <div className="flex items-center gap-3">
    <T1Dropdown
      value={pageSize}
      options={[10, 20, 50, 100].map(n => ({ value: n, label: `${n} registros / página` }))}
      onChange={setPageSize}
    />
    <div className="flex items-center gap-1">
      <span className="font-manrope text-[12px] text-oxford">Saltar a página</span>
      <input
        type="number"
        className="h-[28px] w-[48px] rounded-[4px] border border-gray-200 px-2 font-manrope text-[12px] text-center focus:border-gray-400 focus:outline-none"
        onKeyDown={e => e.key === 'Enter' && setPage(Number(e.target.value))}
      />
      <button className="font-manrope text-[12px] text-oxford hover:underline">›</button>
    </div>
  </div>
</div>
```

---

## 8. Variantes especiales

### 8.1 Tabla de Productos — filas con variantes expandibles

**Figma node:** `2:13070`

La tabla de productos tiene dos niveles de fila:

**Nivel 1 — Producto padre:**
- Columnas: Detalle de producto · Estado de listado · Inventario · Canales · Identificador · Precio · Colección · Acciones
- El campo "Estado de listado" muestra badge + fecha de actualización + fecha de creación
- El campo "Canales" muestra ratio (ej: `4/4`, `2/4`) indicando canales activos vs totales
- El campo "Identificador" muestra SKU + UPC/EAN apilados
- El campo "Precio" muestra precio base + costo apilados
- Botón de variantes: `N variantes ▼` como chip expandible

**Nivel 2 — Variante (subfila):**
- Indentación `32px` respecto al padre
- Muestra: imagen variante · Color · Talla · SKU individual · Precio individual
- BG: `gray-50`
- No tiene columnas de Estado/Canales — hereda del padre

```tsx
// Fila de producto con variantes
<>
  <tr className="border-b border-gray-200 hover:bg-gray-50">
    <td className="px-3 py-3">
      <div className="flex items-start gap-3">
        <img src={product.img} className="h-10 w-10 rounded-[4px] object-cover" />
        <div>
          <p className="font-manrope text-[12px] font-medium text-oxford line-clamp-2">{product.name}</p>
          <p className="font-manrope text-[11px] text-gray-600">{product.category}</p>
          {product.variants > 0 && (
            <button
              onClick={() => toggleExpand(product.id)}
              className="mt-1 flex items-center gap-1 font-manrope text-[11px] text-oxford hover:underline"
            >
              {product.variants} variantes
              <ChevronUpIcon className={`h-3 w-3 transition-transform ${!expanded ? 'rotate-180' : ''}`} />
            </button>
          )}
        </div>
      </div>
    </td>
    {/* resto de columnas */}
  </tr>

  {expanded && product.variantList.map(variant => (
    <tr key={variant.id} className="border-b border-gray-200 bg-gray-50">
      <td className="py-2 pl-10 pr-3">
        <div className="flex items-center gap-2">
          <img src={variant.img} className="h-8 w-8 rounded-[4px] object-cover" />
          <div>
            <p className="font-manrope text-[11px] text-oxford">Color: {variant.color}</p>
            <p className="font-manrope text-[11px] text-oxford">Talla: {variant.size}</p>
          </div>
        </div>
      </td>
      {/* columnas de variante */}
    </tr>
  ))}
</>
```

### 8.2 Tabla de Pedidos — desglose de productos expandible

**Figma node:** `2:4179`

Similar a Productos pero el nivel 2 muestra el contenido del pedido.

**Nivel 1 — Pedido padre:**
- Columnas: ID · Fecha · Canal · Cliente · Productos · Total · Estado de pedido · Seguimiento · Acciones
- ID: `#N` en `oxford` Medium
- Fecha: tiempo relativo + absoluto
- Canal: logo + nombre del canal de venta
- Cliente: nombre con dropdown de selección
- Productos: `N productos ▼` expandible
- Estado: badge de color según estado del pedido
- Seguimiento: badge de guía o `N envíos ▼`

**Nivel 2 — Producto del pedido (subfila):**
- Indentación marcada
- Muestra: imagen · nombre · SKU · chip de variante (Color/Talla) · cantidad · subtotal
- Agrupado por sub-pedido si aplica (ej: "Por preparar:", "Por enviar: 1001-SH01")
- BG: `gray-50`

**Acciones extra en toolbar:**
- "Personalizar vista" y "Ver estadísticas" en dropdown "Más opciones"

### 8.3 Tabla de Precios — edición inline tipo spreadsheet

**Figma node:** `2:17765`

Tabla de edición masiva de precios por canal. Funciona como un spreadsheet embebido.

**Características especiales:**

| Feature | Descripción |
|---|---|
| **Celdas editables** | Click en celda → modo edición inline con borde `gray-400` |
| **Fill-down handle** | Punto azul `●` en la esquina inferior derecha de la celda activa — arrastrar hacia abajo copia el valor a las celdas siguientes |
| **Columnas por canal** | Agrupadas por canal: T1 (Precio base + Precio oferta) · Shein · Shopify · etc. Cada grupo tiene header con logo del canal |
| **Variantes expandibles** | Igual que Productos — producto padre con N variantes expandibles |
| **Guardar/Descartar** | Botones en la toolbar: `button/secondary` "Descartar cambios" + `button/primary` "Guardar cambios" · solo visibles cuando hay cambios pendientes |
| **Selección checkbox** | Permite aplicar cambio masivo a filas seleccionadas |

**Comportamiento del fill-down:**
1. Usuario hace click en celda → entra en modo edición
2. Aparece handle (punto rojo `●` de `4×4px`) en esquina inferior derecha
3. Usuario arrastra handle hacia abajo → el valor se copia a todas las celdas del rango arrastrado
4. Al soltar → las celdas se actualizan con el valor copiado
5. Los cambios quedan en estado "pendiente" hasta que el usuario presione "Guardar cambios"

```tsx
// Celda editable con fill-down
const EditableCell = ({ value, onChange, onFillStart }) => {
  const [editing, setEditing] = useState(false)
  const [localValue, setLocalValue] = useState(value)

  return (
    <td
      className={`relative border-r border-gray-200 px-3 py-3 ${
        editing ? 'ring-2 ring-inset ring-gray-400' : 'hover:bg-gray-50'
      }`}
      onClick={() => setEditing(true)}
    >
      {editing ? (
        <input
          autoFocus
          value={localValue}
          onChange={e => setLocalValue(e.target.value)}
          onBlur={() => { setEditing(false); onChange(localValue) }}
          className="w-full bg-transparent font-manrope text-[12px] font-medium text-oxford focus:outline-none"
        />
      ) : (
        <span className="font-manrope text-[12px] font-medium text-oxford">${localValue}</span>
      )}

      {/* Fill-down handle */}
      {editing && (
        <div
          className="absolute bottom-0.5 right-0.5 h-[6px] w-[6px] cursor-s-resize rounded-full bg-red-500"
          onMouseDown={onFillStart}
        />
      )}
    </td>
  )
}
```

---

## 8. Acomodos de columna

Las tablas del sistema usan diferentes layouts de celda según el tipo de dato. Estos son los patrones identificados en Figma:

### 8.1 Celda con dato principal + secundario apilados

El patrón más frecuente — dato principal en medium arriba, dato secundario en gris abajo.

```
┌─────────────────┐
│ Valor principal │  ← Manrope Medium 12px · oxford
│ Dato secundario │  ← Manrope Regular 11px · gray-600
└─────────────────┘
```

Ejemplos: Fecha (relativa + absoluta), Identificador (SKU + UPC/EAN), Precio (base + costo).

### 8.2 Celda con imagen + texto multilínea

Para registros con imagen (productos, variantes).

```
┌──────────────────────────────┐
│ [img] Nombre del producto    │  ← Medium 12px · oxford · line-clamp-2
│       Categoría / SKU        │  ← Regular 11px · gray-600
│       N variantes ∨          │  ← Regular 11px · oxford (si aplica)
└──────────────────────────────┘
```

### 8.3 Celda con logo + texto (canales / integraciones)

```
┌──────────────────┐
│ [logo] Nombre    │  ← logo 16×16px + Medium 12px · oxford
└──────────────────┘
```

### 8.4 Celda numérica con ratio

Para inventario, canales activos, envíos.

```
┌──────────────┐
│ 3,102 unids  │  ← Medium 12px · oxford
│ 2/4          │  ← Regular 11px · gray-600
└──────────────┘
```

### 8.5 Tabla de Precios mobile — inputs por canal (node `2:18287`)

En mobile la tabla de Precios **no se convierte en cards** — mantiene su estructura de edición pero adaptada a pantalla estrecha:

- Producto: imagen + nombre + SKU en la parte superior
- "Modificar por variante (N variantes) ›" como link expandible
- Por cada canal: logo + "Precio base" y "Precio oferta" como dos inputs uno debajo del otro
- "Ver todos los canales" como link al fondo cuando hay más canales de los que caben

```tsx
// Tabla precios mobile
<div className="border-b border-gray-200 py-3">
  {/* Producto */}
  <div className="mb-2 flex items-center gap-2 px-4">
    <img src={product.img} className="h-10 w-10 rounded-[4px] object-cover" />
    <div>
      <p className="font-manrope text-[12px] font-medium text-oxford line-clamp-1">{product.name}</p>
      <p className="font-manrope text-[11px] text-gray-600">{product.sku}</p>
    </div>
  </div>
  {/* Variantes */}
  <button className="mb-3 flex w-full items-center justify-between px-4 py-2 font-manrope text-[12px] text-oxford hover:bg-gray-50">
    Modificar por variante ({product.variants} variantes)
    <ChevronRightIcon className="h-4 w-4 text-gray-600" />
  </button>
  {/* Precios por canal */}
  {channels.map(channel => (
    <div key={channel.id} className="mb-3 px-4">
      <div className="mb-1 flex items-center gap-2">
        <img src={channel.logo} className="h-5 w-5 object-contain" />
      </div>
      <div className="grid grid-cols-2 gap-2">
        <div>
          <label className="font-manrope text-[11px] text-gray-600">Precio base</label>
          <input className="mt-1 h-[35px] w-full rounded-[10px] border border-gray-200 px-2 font-manrope text-[12px]" value={channel.base} />
        </div>
        <div>
          <label className="font-manrope text-[11px] text-gray-600">Precio oferta</label>
          <input className="mt-1 h-[35px] w-full rounded-[10px] border border-gray-200 px-2 font-manrope text-[12px]" value={channel.offer} />
        </div>
      </div>
    </div>
  ))}
  <button className="px-4 font-manrope text-[12px] text-oxford underline">Ver todos los canales</button>
</div>
```

### 8.6 Tabla de Clientes mobile — card sin imagen (node `2:30611`)

Card por cliente con datos de contacto. Sin imagen/avatar.

```
┌─────────────────────────────────┐
│ Gabriela Luna      [Suscrita]   │  ← nombre SemiBold 14px + badge
│ Ciudad de México - México       │  ← Regular 12px · gray-600
│ gabluor@gmail.com               │  ← Regular 12px · gray-600
│ $2,320.00          5511327490   │  ← monto + teléfono · Medium 12px
└─────────────────────────────────┘
```

```tsx
<div className="border-b border-gray-200 py-4 px-0">
  <div className="flex items-start justify-between">
    <p className="font-manrope text-[14px] font-semibold text-oxford">{client.name}</p>
    <span className={`rounded-[4px] px-2 py-0.5 font-manrope text-[11px] font-medium ${
      client.subscribed ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-600'
    }`}>
      {client.subscribed ? 'Suscrita' : 'No suscrito'}
    </span>
  </div>
  <p className="mt-0.5 font-manrope text-[12px] text-gray-600">{client.city} - {client.country}</p>
  <p className="font-manrope text-[12px] text-gray-600">{client.email}</p>
  <div className="mt-1 flex items-center justify-between">
    <span className="font-manrope text-[12px] font-medium text-oxford">{client.total}</span>
    <span className="font-manrope text-[12px] text-gray-600">{client.phone}</span>
  </div>
</div>
```

### 8.7 Cotizador de envíos mobile — lista de opciones (node `2:54285`)

Este patrón **no es una tabla** — es una lista de opciones de carrier tipo selector. Cada opción es una card con CTA propio.

```
┌─────────────────────────────────────┐
│ [logo] FedEx Estándar  [RECOMENDADA]│  ← logo + nombre + badge opcional
│ Entrega estimada:      Precio:      │
│ 26 de ene             $214.00 MXN   │
│ *Incluye seguro de $23.00           │
│ [     Crear envío    ]              │  ← button/primary w-full
└─────────────────────────────────────┘
```

```tsx
{carriers.map(carrier => (
  <div key={carrier.id} className="mb-3 rounded-[10px] border border-gray-200 bg-white p-4 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
    <div className="mb-3 flex items-center justify-between">
      <div className="flex items-center gap-2">
        <img src={carrier.logo} className="h-8 w-8 object-contain" />
        <div>
          <p className="font-manrope text-[13px] font-semibold text-oxford">{carrier.name}</p>
          <p className="font-manrope text-[11px] text-gray-600">{carrier.service}</p>
        </div>
      </div>
      {carrier.recommended && (
        <span className="rounded-[4px] bg-red-500 px-2 py-0.5 font-manrope text-[10px] font-semibold text-white">
          RECOMENDADA
        </span>
      )}
    </div>
    <div className="mb-3 flex items-start justify-between">
      <div>
        <p className="font-manrope text-[11px] text-gray-600">Entrega estimada:</p>
        <p className="font-manrope text-[12px] font-medium text-oxford">{carrier.deliveryDate}</p>
      </div>
      <div className="text-right">
        <p className="font-manrope text-[11px] text-gray-600">Precio:</p>
        <p className="font-manrope text-[12px] font-medium text-oxford">{carrier.price}</p>
        {carrier.note && <p className="font-manrope text-[10px] text-gray-600">{carrier.note}</p>}
      </div>
    </div>
    <T1Button variant="primary" className="w-full">Crear envío</T1Button>
  </div>
))}
```

En mobile **no existe tabla**. Cada fila se convierte en una card de ancho completo (`w-full`).

### 9.1 Principio

```
Desktop:
┌────┬────────┬────────┬────────┬────────┐
│ #  │ Campo1 │ Campo2 │ Campo3 │ Campo4 │
└────┴────────┴────────┴────────┴────────┘

Mobile:
┌────────────────────────┐
│ [img] Nombre principal │
│ Campo2: valor          │
│ Campo3: valor          │
│ [badge] [badge]        │
│ Campo4: valor   [···]  │
└────────────────────────┘
```

### 9.2 Especificaciones de la card

```css
/* Card de fila mobile */
border-radius: 10px;
border: 1px solid var(--color-gray-200);
background: white;
padding: 12px 16px;
margin-bottom: 8px;
width: 100%;
box-shadow: 0 0 5px 1px rgba(0,0,0,0.1);
```

### 9.3 Reglas de contenido

- **Siempre visible:** nombre/título principal + estado (badge) + acción principal
- **Colapsable opcional:** datos secundarios (SKU, fechas, IDs) bajo un "Ver más"
- **Acciones:** botón `···` en la esquina superior derecha de la card
- **Imágenes:** si la fila tiene imagen de producto, se muestra como thumbnail `40×40px` a la izquierda

### 9.4 Snippet

```tsx
// Card mobile de pedido
<div className="rounded-[10px] border border-gray-200 bg-white p-4 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
  {/* Header de card */}
  <div className="mb-3 flex items-start justify-between">
    <div>
      <p className="font-manrope text-[12px] font-semibold text-oxford">{order.id}</p>
      <p className="font-manrope text-[11px] text-gray-600">{order.relativeDate}</p>
    </div>
    <div className="flex items-center gap-2">
      <span className={`rounded-[4px] px-2 py-0.5 font-manrope text-[11px] font-medium ${statusStyle}`}>
        {order.status}
      </span>
      <button onClick={() => setMenuOpen(true)}>
        <EllipsisHorizontalIcon className="h-4 w-4 text-gray-600" />
      </button>
    </div>
  </div>

  {/* Datos */}
  <div className="flex flex-col gap-1.5">
    <div className="flex items-center gap-2">
      <img src={order.channel.logo} className="h-4 w-4 object-contain" />
      <span className="font-manrope text-[12px] text-oxford">{order.channel.name}</span>
    </div>
    <p className="font-manrope text-[12px] text-oxford">{order.client}</p>
    <p className="font-manrope text-[12px] font-semibold text-oxford">{order.total}</p>
  </div>
</div>
```

---

## 10. Skeleton loading

Mientras la tabla carga sus datos, se muestran filas skeleton que replican la estructura real.

```tsx
// Skeleton de tabla
<tbody>
  {Array.from({ length: pageSize }).map((_, i) => (
    <tr key={i} className="border-b border-gray-200">
      {columns.map((col, j) => (
        <td key={j} className="px-3 py-3">
          <div className="h-4 animate-pulse rounded-[4px] bg-gray-100"
            style={{ width: `${60 + Math.random() * 30}%` }}
          />
          {col.hasSecondLine && (
            <div className="mt-1.5 h-3 w-1/2 animate-pulse rounded-[4px] bg-gray-100" />
          )}
        </td>
      ))}
    </tr>
  ))}
</tbody>
```

---

## 11. Empty state y estados de tabla sin contenido

La tabla tiene **3 estados posibles** cuando no muestra datos:

### 11.1 Sin registros (tabla vacía)

Cuando el usuario aún no tiene datos — primera vez o sección en blanco. El toolbar se mantiene con sus acciones para que el usuario pueda agregar contenido.

**Visual:**
- Toolbar normal con título + acciones (Importar, Más opciones, CTA primario)
- Área de tabla: fondo `white` · sin header de columnas · sin filtros
- Centrado vertical y horizontal: título + descripción + CTA

**Especificaciones de texto:**
- Título: Manrope SemiBold 16px · `oxford` — ej: "Aún no tienes productos"
- Descripción: Manrope Regular 14px · `gray-600` — ej: "Empieza a cargar tus productos, puedes hacerlo de manera masiva o individual."
- CTA: `button/primary` con la misma acción que el botón principal del toolbar — ej: "Agregar producto"

```tsx
// Empty state — sin registros
<div className="flex flex-col items-center justify-center py-24 text-center">
  <h3 className="font-manrope text-[16px] font-semibold text-oxford">
    Aún no tienes productos
  </h3>
  <p className="mt-2 max-w-md font-manrope text-[14px] text-gray-600">
    Empieza a cargar tus productos, puedes hacerlo de manera masiva o individual.
  </p>
  <T1Button variant="primary" className="mt-6" onClick={onAdd}>
    Agregar producto
  </T1Button>
</div>
```

### 11.2 Sin resultados (filtros aplicados)

Cuando hay filtros activos pero ningún registro coincide. Los filtros se mantienen visibles para que el usuario pueda modificarlos.

**Visual:** igual que sin registros, pero el texto cambia:
- Título: "No encontramos resultados"
- Descripción: "Intenta ajustar los filtros o realiza una nueva búsqueda."
- CTA: `button/secondary` "Limpiar filtros"

### 11.3 Error de carga

Cuando hubo un problema al obtener los datos del servidor. La fila de filtros se mantiene visible pero el área de tabla muestra el error.

**Visual:**
- Área de tabla con borde `gray-200` · `border-radius: 10px` · BG `white`
- Sin header de columnas
- Centrado: solo título + descripción (sin CTA — el usuario debe recargar la página)

**Especificaciones de texto:**
- Título: Manrope SemiBold 16px · `oxford` — "Algo no salió como esperábamos"
- Descripción: Manrope Regular 14px · `gray-600` — "Hubo un problema al cargar la información. Por favor, recarga la página para continuar."

```tsx
// Error de carga
<div className="rounded-[10px] border border-gray-200 bg-white py-24">
  <div className="flex flex-col items-center justify-center text-center">
    <h3 className="font-manrope text-[16px] font-semibold text-oxford">
      Algo no salió como esperábamos
    </h3>
    <p className="mt-2 max-w-lg font-manrope text-[14px] text-gray-600">
      Hubo un problema al cargar la información. Por favor, recarga la página para continuar.
    </p>
  </div>
</div>
```

> **Diferencia clave entre los tres:** Sin registros → toolbar completo + CTA para crear. Sin resultados → filtros visibles + CTA para limpiarlos. Error → contenedor con borde + sin CTA (acción es recargar el browser).

---

## 12. Header sticky

El header de columnas se mantiene fijo al hacer scroll vertical cuando la tabla tiene muchos registros.

```css
thead tr {
  position: sticky;
  top: 0;
  z-index: 10;
  background-color: var(--color-blue-100);
}
```

```tsx
<div className="overflow-auto">
  <table className="w-full">
    <thead className="sticky top-0 z-10">
      <tr className="bg-blue-100">
        {/* columnas */}
      </tr>
    </thead>
    <tbody>
      {/* filas */}
    </tbody>
  </table>
</div>
```

> ⚠️ El contenedor padre debe tener `overflow-auto` y una altura máxima definida para que el sticky funcione correctamente.

---

## Notas para Claude

- **Nunca usar `<table>` nativa sin estilos** — todas las tablas usan las clases del sistema.
- **El header siempre usa `blue-100`** como BG — no `gray-50` ni `white`.
- **La tipografía base es Manrope 12px Medium** — no Inter, no 14px.
- **Las tablas en mobile son siempre cards** — nunca tabla horizontal con scroll.
- **La tabla de Precios** es el único lugar donde las celdas son editables inline.
- **Paginación solo con +50 registros** — con 50 o menos, todos los registros en una sola página.
- **Paginación:** página activa usa `red-500` como BG — nunca `blue-500`.
- **Sorting:** siempre dos chevrons juntos (↑↓) — nunca solo uno según dirección.
- **Selección:** fila seleccionada usa `gray-50` — mismo que hover, no `red-50`.
- **Barra masiva:** reemplaza el header de columnas cuando hay filas seleccionadas.
- **Header sticky:** siempre fijo en scroll vertical — contenedor padre necesita `overflow-auto` + altura máxima.
- **Empty state sin registros:** toolbar completo + CTA para crear. **Error:** contenedor con borde + sin CTA.
- **Personalizar vista** no está activo actualmente — no documentar ni implementar.

---

## Referencias cruzadas

| Archivo | Relación |
|---|---|
| `foundation/COLORS.md` | Tokens: `blue-100` header, `gray-50` hover/seleccionada, `red-500` paginación activa |
| `components/ATOMS.md` | Badges de estado, chips, botones de acción usados en celdas |
| `components/MOLECULES.md` | Search, Dropdown de filtros, Submenu de acciones (`···`) |
| `patterns/EMPTY-STATES.md` | Empty states por contexto de negocio (productos, pedidos, envíos) |
| `patterns/NOTIFICATIONS.md` | Toasts de confirmación tras acciones en tabla (guardar, eliminar) |
| `platforms/DASHBOARD.md` | Contexto de uso — las tablas solo existen en dashboard |
