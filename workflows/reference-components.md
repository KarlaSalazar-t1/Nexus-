# reference-components.md

> Catálogo condensado de componentes NEXUS V2.0 para context window de Claude.  
> Fuente completa: `components/ATOMS.md`, `MOLECULES.md`, `ORGANISMS.md`, `STATES.md`, `TABLES.md`.  
> Todos los componentes son de **dashboard** salvo indicación explícita.

---

## Convenciones globales

- Naming: prefijo `T1` + PascalCase — `T1Button`, `T1Input`, `T1DataTable`
- Tipografía: Manrope en todo el dashboard
- Todo contenido hardcodeado va en `constants.ts` — nunca inline en el componente
- Todo componente interactivo requiere los **10 estados** (ver sección 7)
- Touch targets mínimo `44×44px` en mobile
- Focus: `focus-visible:ring-2 focus-visible:ring-blue-500` en todos los elementos interactivos

---

## 1. Buttons

**8 variantes:** Primary · Secondary · Link · Split · Icon · IA · Social · Disclosure

| Variante | BG default | Cuándo usar |
|---|---|---|
| **Primary** | `red-500 #DB3B2B` | CTA principal — máximo uno por vista |
| **Secondary** | `white` + border `gray-200` | Acciones secundarias, cancelar |
| **Link** | Transparente | Acciones terciarias, navegación inline |
| **Split** | `white` + border `gray-200` | Acción default + dropdown de variantes |
| **Icon** | `white` + border `gray-200` | Acciones compactas en toolbars y tablas |
| **IA** | `white` + border purple | Acciones de inteligencia artificial |
| **Social** | `white` | Auth con Google, Facebook, etc. |
| **Disclosure** | Transparente | Mostrar/ocultar secciones |

**Tokens base:**

```css
height: 35px;          /* mobile: 44px */
padding: 0 16px;
border-radius: 10px;
font: Manrope SemiBold 14px;
```

**Snippets clave:**

```tsx
// Primary
<button className="h-[35px] rounded-[10px] bg-red-500 px-4 font-manrope text-[14px] font-semibold text-white hover:bg-red-700 disabled:bg-red-200 disabled:cursor-not-allowed transition-colors">
  Guardar
</button>

// Secondary
<button className="h-[35px] rounded-[10px] border border-gray-200 bg-white px-4 font-manrope text-[14px] font-semibold text-oxford hover:bg-gray-50 disabled:text-gray-500 disabled:cursor-not-allowed transition-colors">
  Cancelar
</button>

// Link
<button className="font-manrope text-[14px] font-medium text-oxford hover:text-black hover:underline disabled:text-gray-500 transition-colors">
  Ver detalle
</button>

// Icon
<button className="flex h-[35px] w-[35px] items-center justify-center rounded-[10px] border border-gray-200 bg-white hover:bg-gray-50 transition-colors">
  <IconName className="h-4 w-4 text-oxford" />
</button>
```

**Loading:** Solo spinner para acciones rápidas · Spinner + texto para procesos lentos (ancho del botón no cambia).

---

## 2. Inputs & Text Fields

**8 variantes:** Input · Prefix · Subfix · Multiline · Number · Split · Teléfono · Social

**Estados:**

| Estado | Border | BG | Nota |
|---|---|---|---|
| Default | `gray-200` | `white` | — |
| Hover | `gray-200` | `gray-50` | BG cambia, border igual |
| Focus | `gray-400` | `white` | Solo borde cambia |
| Error | `red-700` | `white` | BG siempre blanco |
| Disabled | `gray-200` | `white` | BG siempre blanco |
| Success | `gray-200` | `white` | Solo agrega ícono check `green-500` |
| Read Only | `gray-200` | `gray-50` | No interactivo |

> ⚠️ BG siempre `white` en Error, Disabled y Success. Solo Hover y Read Only usan `gray-50`.  
> ⚠️ Mobile: `font-size: 16px` obligatorio para evitar zoom automático en iOS Safari.

```tsx
// Input estándar
<div className="flex flex-col gap-1">
  <label className="font-manrope text-[14px] font-medium text-oxford">Label</label>
  <input
    className="h-[48px] rounded-[10px] border border-gray-200 bg-white px-3 font-manrope text-[14px] placeholder:text-gray-500 hover:bg-gray-50 focus:border-gray-400 focus:outline-none disabled:cursor-not-allowed transition-colors"
  />
</div>

// Input error
<input className="h-[48px] rounded-[10px] border border-red-700 bg-white px-3 font-manrope text-[14px] focus:outline-none" />
<p className="font-manrope text-[12px] text-red-700">Mensaje de error</p>
```

---

## 3. Select & Dropdowns

**5 variantes:** Dropdown · Selector Radio · Selector Check · Selector Múltiple · Image Select

```tsx
<div className="relative">
  <select className="h-[48px] w-full appearance-none rounded-[10px] border border-gray-200 bg-white px-3 pr-8 font-manrope text-[14px] text-oxford hover:bg-gray-50 focus:border-gray-400 focus:outline-none">
    <option>Seleccionar</option>
  </select>
  <ChevronDownIcon className="pointer-events-none absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-600" />
</div>
```

> Dropdowns son **flat** — sin sombra en dashboard.

---

## 4. Controls de Selección

**Variantes:** Checkbox · Radio · Switch · Favorite · Rating

| Control | On state | Off state |
|---|---|---|
| Checkbox | relleno `red-500` | border `gray-200` |
| Radio | relleno `red-500` | border `gray-200` |
| Switch | track `green-500` · thumb `white` | track `gray-200` · thumb `white` |
| Favorite | corazón `red-500` | corazón `gray-300` |

---

## 5. Badges & Chips

**Chips** — seleccionables/removibles, `border-radius: 4px`, height `24px`:

| Variante | BG | Text |
|---|---|---|
| Violet | `purple-100` | `purple-700` |
| Gray | `gray-100` | `gray-700` |
| Blue | `blue-100` | `blue-500` |
| Green | `green-100` | `green-700` |
| Red | `red-50` | `red-700` |

**Badges de estado** — height `24px`, `border-radius: 4px`:

| Tipo | BG | Text |
|---|---|---|
| Success | `green-100` | `green-700` |
| Warning | `orange-100` | `orange-700` |
| Error | `red-50` | `red-700` |
| Info | `blue-100` | `blue-500` |
| Neutral | `gray-100` | `gray-700` |

**Badges especiales:** IA (purple, `128×32px`) · Recomendado (`91×25px`) · Premium (corona `yellow-500`)

---

## 6. Avatars

| Tipo | Forma | Tamaños | Nota |
|---|---|---|---|
| User (letra) | Circular | SM `28×28px` · MD `56×56px` | Iniciales algorítmicas por nombre |
| Photo | Circular | SM · MD | `object-cover` |
| Store | `border-radius: 8px` | MD `36×36px` | Cuadrado redondeado — diferencia de persona |

---

## 7. Indicadores & Loaders

**Barra de progreso:** relleno `red-500` · fondo `gray-100` · `border-radius: full`

**Indicadores de estado** (`30×30px`): Success `green-500` · Error `red-700` · Warning `yellow-500` · Info `blue-500` · Alert `red-500`

**Steps:** Completado = círculo `red-500` + check · Activo = borde `red-500` + número · Pendiente = borde `gray-200`

**Spinner:**
```tsx
<svg className="animate-spin h-5 w-5 text-red-500" fill="none" viewBox="0 0 24 24">
  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
</svg>
```

**Skeleton:** `animate-pulse rounded bg-gray-100` — se adapta a cards en mobile.

---

## 8. Modal

Contenedor de diálogo con slots intercambiables.

**Slots:** `empty` · `Top` (título + cerrar) · `Text` (cuerpo) · `button` (CTAs) · `Map` · `Toma+logo`

```css
border-radius: 10px;
background: white;
box-shadow: 0 0 5px 1px rgba(0,0,0,0.1);
overlay: rgba(0,0,0,0.6);
```

**Tamaños:** pequeño `309×235px` · estándar `505×315px` · grande (con Map) hasta `940×470px`

```tsx
<div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
  <div className="w-[505px] rounded-[10px] bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
    {/* Top */}
    <div className="flex items-center justify-between border-b border-gray-200 px-6 py-4">
      <h2 className="font-manrope text-[14px] font-semibold text-oxford">Título</h2>
      <button onClick={onClose}><XMarkIcon className="h-4 w-4 text-gray-500" /></button>
    </div>
    {/* Text */}
    <div className="px-6 py-4">
      <p className="font-manrope text-[14px] text-oxford">Contenido</p>
    </div>
    {/* Buttons */}
    <div className="flex justify-end gap-3 border-t border-gray-200 px-6 py-4">
      <T1Button variant="secondary" onClick={onClose}>Cancelar</T1Button>
      <T1Button variant="primary" onClick={onConfirm}>Confirmar</T1Button>
    </div>
  </div>
</div>
```

> Mobile: bottom sheet — ancho completo, `border-radius: 10px 10px 0 0`, aparece desde abajo.  
> Máximo un modal visible a la vez — no apilar.

---

## 9. Cards (dashboard)

Token base de todas las cards:

```css
border-radius: 10px;       /* 20px para cards grandes */
background: white;
border: 1px solid #E7E7E7; /* gray-200 */
box-shadow: 0 0 5px 1px rgba(0,0,0,0.1);
padding: 16px 20px;
```

**Tipos principales:** Métrica · Resumen (Summary) · Integración · Canal · Sincronización · Dirección · Fiscal · Notas · Tags · Lista · Recarga de Saldo · Perfil (Submenu)

> Cards son estáticas — sin hover ni selected, salvo **Card Selector** que usa `border: 2px red-500` + `shadow red-200` en estado selected.

```tsx
<div className="rounded-[10px] border border-gray-200 bg-white p-5 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
  <div className="mb-4 flex items-center justify-between">
    <h3 className="font-manrope text-[14px] font-semibold text-oxford">Título</h3>
    <T1Button variant="link">Editar</T1Button>
  </div>
  {/* contenido */}
</div>
```

---

## 10. Tooltip & Submenu

**Tooltip:** BG `oxford` · text `white` · Manrope Regular 12px · `border-radius: 4px` · delay ~200ms  
No aplica en mobile — reemplazar por texto de ayuda visible o modal al tap.

**Submenu:** BG `white` · border `gray-200` · `border-radius: 10px` · `shadow_card` · ancho `161px`  
Ítems destructivos en `red-700`, el resto en `oxford`.

```tsx
{open && (
  <div className="absolute right-0 top-full z-50 mt-1 w-[161px] rounded-[10px] border border-gray-200 bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
    {items.map(item => (
      <button key={item.id}
        className={`flex w-full items-center gap-2 px-4 py-3 font-manrope text-[14px] hover:bg-gray-50 first:rounded-t-[10px] last:rounded-b-[10px] ${item.destructive ? 'text-red-700' : 'text-oxford'}`}>
        {item.label}
      </button>
    ))}
  </div>
)}
```

---

## 11. Los 10 estados obligatorios

Todo componente interactivo implementa el subconjunto que aplica a su función.

| # | Estado | Señal visual |
|---|---|---|
| 1 | **Default** | Apariencia base |
| 2 | **Hover** | BG `gray-50` — señala interactividad |
| 3 | **Focus** | Ring `blue-500` 2px con `:focus-visible` |
| 4 | **Pressed/Active** | BG `gray-100` u opacidad reducida |
| 5 | **Loading** | Spinner `red-500` |
| 6 | **Disabled** | Opacidad reducida · `cursor-not-allowed` · no interactivo |
| 7 | **Error** | Border + text `red-700` · mensaje inline |
| 8 | **Success** | Ícono check `green-500` · BG sin cambio |
| 9 | **Selected** | Indicador activo según componente |
| 10 | **Empty** | Mensaje contextual + CTA de recuperación |

**Tokens de estado clave:**

| Estado | BG | Border | Text/Icon |
|---|---|---|---|
| Hover | `gray-50` | sin cambio | sin cambio |
| Focus | sin cambio | `gray-400` | sin cambio |
| Focus a11y | sin cambio | `blue-500` ring 2px | sin cambio |
| Error | `white` | `red-700` | `red-700` |
| Success | `white` | `gray-200` | ícono `green-500` |
| Disabled primary | `red-200` | — | `white` |
| Disabled secondary/inputs | `white` | `gray-200` | `gray-500` |
| Card Selector selected | `white` | `red-500` 2px | shadow `red-200` |

---

## 12. Organisms — Shell del dashboard

**Header top bar:** altura `64px` · fijo · BG `white`  
- Izquierda: logo T1 + nombre del producto  
- Centro: selector de tienda (avatar + nombre + chevron)  
- Derecha: íconos de acción + avatar de usuario

**Sidebar:**
- Expandido: `284px` · solo íconos colapsado: `~64px` · mobile: drawer overlay
- `border-radius: 18px` · BG `white` · flat (sin sombra)

| Estado de item | BG | Text | Indicador |
|---|---|---|---|
| Default | Transparente | `#4C4C4C` | — |
| Hover | `gray-50` | `#4C4C4C` | — |
| Selected (main) | Highlight sutil | `red-500` | Borde izq `red-500` |
| Selected (sub) | Highlight sutil | `#4C4C4C` Bold | — |

---

## 13. Tables

Ver `components/TABLES.md` para documentación completa.

**Tokens base:**

```css
table header: bg #F4F8FF · Manrope SemiBold 14px · oxford
table row: bg white · Manrope Regular 14px · oxford
row hover: bg gray-50
row selected: bg gray-50
border: 1px solid gray-200
```

**Características obligatorias:** sorting por columna · paginación · filtros · estado empty · estado loading (skeleton) · transformación a cards en mobile.
