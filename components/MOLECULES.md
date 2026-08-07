# MOLECULES — NEXUS V2.0 Design System

> **Categoría:** components  
> **Nivel:** Molécula (2+ átomos combinados con función propia)  
> **Fuente:** Figma `SD - Migration V2` · frames `MOLECULES` (5:3591) · `MOLECULES 2` (69:4133) · `MOLECULES 3` (244:17077) · `MOLECULES 4` (224:9054) · `MOLECULES 5` (1134:8526)  
> **Contexto:** Dashboard — todas las moléculas de este archivo son de contexto admin salvo indicación explícita  
> **Última actualización:** 2025  
> **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Forms](#1-forms)
2. [Search / Buscador](#2-search--buscador)
3. [Color Picker](#3-color-picker)
4. [Calendar / Date Picker](#4-calendar--date-picker)
5. [Upload](#5-upload)
6. [Modal](#6-modal)
7. [Tooltip](#7-tooltip)
8. [Submenu](#8-submenu)
9. [Timeline](#9-timeline)
10. [Messages](#10-messages)
11. [Steps / Onboarding](#11-steps--onboarding)
12. [Tabs](#12-tabs)
13. [Cards](#13-cards)

---

## Convenciones de este archivo

- Todos los colores se referencian por token de `foundation/COLORS.md`.
- Los átomos usados dentro de cada molécula referencian `components/ATOMS.md`.
- Variantes mobile documentadas bajo `📱 Mobile` en cada componente.
- `border-radius` base de contenedores: `10px`. Cards: `10px` estándar, `20px` cards grandes.
- Shadow estándar de cards: `shadow_card` → `0 0 5px 1px rgba(0,0,0,0.1)` (`color/overlay/Light Black`).

---

## 1. Forms

**Figma nodes:** `67:5123` (Default) · `67:5135` (Required) · `67:5149` (Error)

Los Forms son la combinación de múltiples átomos de entrada (inputs, dropdowns, multiline) con botones de acción. Son el patrón base para cualquier flujo de creación o edición en el dashboard.

### 1.1 Variantes

| Variante | Descripción | Figma node |
|---|---|---|
| **Default** | Campos sin marcar como requeridos | `67:5123` |
| **Required** | Muestra `*Campos requeridos` en la parte superior derecha | `67:5135` |
| **Error** | Estado de validación fallida — inputs en estado error | `67:5149` |

### 1.2 Estructura

Un Form se compone de:
- **Título de sección** (opcional) — Manrope SemiBold 14px · `oxford`
- **Grid de campos** — combinación libre de: `input`, `dropdown`, `input prefix`, `input split`, `input subfix`, `input multiline`
- **Indicador de campos requeridos** — `*Campos requeridos` · Manrope Regular 12px · `oxford` · alineado a la derecha del header
- **Área de acciones** — siempre al final, alineada a la derecha: `button/secondary` + `button/primary`

### 1.3 Reglas de uso

- El botón destructivo (Cancelar/Cerrar) siempre va a la izquierda del CTA principal.
- Los campos requeridos **solo se marcan con `*`** en formularios largos donde hay campos opcionales mezclados — y únicamente en el label del campo específico, nunca como indicador global con `*Campos requeridos`. En formularios cortos donde todos los campos son obligatorios, no se marca ninguno.
- La validación de error se muestra inline bajo cada campo, no como toast.
- Un form nunca tiene más de un botón Primary.

### 1.4 Snippet

```tsx
<form className="flex flex-col gap-6">
  {/* Header de sección */}
  <h3 className="font-manrope text-[14px] font-semibold text-oxford">Datos del producto</h3>

  {/* Grid de campos — * solo cuando hay mezcla de obligatorios y opcionales */}
  <div className="grid grid-cols-2 gap-4">
    <T1Input label="Nombre *" placeholder="Nombre del producto" />
    <T1Dropdown label="Categoría *" options={categorias} />
    <T1Input label="Precio" type="prefix" prefix="$" />
    <T1Input label="SKU" />
    <T1Multiline label="Descripción" className="col-span-2" />
  </div>

  {/* Acciones */}
  <div className="flex justify-end gap-3">
    <T1Button variant="secondary" onClick={onCancel}>Cancelar</T1Button>
    <T1Button variant="primary" type="submit">Guardar producto</T1Button>
  </div>
</form>
```

### 📱 Mobile

En mobile los campos pasan a una sola columna (`grid-cols-1`). Los botones de acción son `w-full` apilados verticalmente, con el Primary primero.

---

## 2. Search / Buscador

**Figma nodes:** `87:3934` (buscador_desktop) · `99:3932` (con resultados)

### 2.1 Variantes

| Variante | Descripción | Figma node |
|---|---|---|
| **Empty** | Campo vacío, placeholder visible | `87:3930` |
| **Fill** | Con texto ingresado | `87:3935` |
| **Con resultados** | Panel de resultados desplegado bajo el input | `99:3924` |
| **Con resultados (Variant2)** | Panel de resultados con estructura alternativa | `99:3925` |

### 2.2 Estructura

- Input de búsqueda — height `40px` · `border-radius: 10px` · ícono lupa a la izquierda
- Panel de resultados — aparece con shadow card, `border-radius: 10px`, BG `white`
- Resultados agrupados por categoría cuando aplica

### 2.3 Snippet

```tsx
<div className="relative">
  {/* Input */}
  <div className="flex h-[40px] items-center gap-2 rounded-[10px] border border-gray-200 bg-white px-3 focus-within:border-gray-400">
    <MagnifyingGlassIcon className="h-4 w-4 shrink-0 text-gray-500" />
    <input
      className="flex-1 font-manrope text-[14px] text-black placeholder:text-gray-500 focus:outline-none"
      placeholder="Buscar..."
      value={query}
      onChange={e => setQuery(e.target.value)}
    />
    {query && (
      <button onClick={clearQuery}>
        <XMarkIcon className="h-4 w-4 text-gray-500" />
      </button>
    )}
  </div>

  {/* Panel de resultados */}
  {results.length > 0 && (
    <div className="absolute top-[44px] z-50 w-full rounded-[10px] border border-gray-200 bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
      {results.map(result => (
        <button key={result.id} className="flex w-full items-center gap-3 px-3 py-2 text-left hover:bg-gray-50">
          <span className="font-manrope text-[14px] text-oxford">{result.label}</span>
        </button>
      ))}
    </div>
  )}
</div>
```

### 📱 Mobile

El buscador ocupa `w-full`. El panel de resultados se extiende al ancho completo de la pantalla.

---

## 3. Color Picker

**Figma node:** `99:4011`

Selector visual de color. Combina: paleta de colores, slider de tono, slider de opacidad (opcional), e input de valor hex.

### 3.1 Estructura

- **Paleta principal** — área de selección de saturación/luminosidad
- **Slider de tono** (hue) — barra horizontal con gradiente del espectro
- **Input hex** — campo de texto con validación de formato `#RRGGBB`
- **Muestra de color** — preview del color seleccionado

Dimensiones: `264×380px`

### 3.2 Snippet

```tsx
// Wrapper del color picker
<div className="w-[264px] rounded-[10px] border border-gray-200 bg-white p-4 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
  <T1ColorPickerCanvas color={color} onChange={setColor} />
  <T1HueSlider hue={hue} onChange={setHue} className="mt-3" />
  <div className="mt-3 flex items-center gap-2">
    <div className="h-8 w-8 rounded-[4px] border border-gray-200" style={{ backgroundColor: color }} />
    <input
      className="flex-1 rounded-[10px] border border-gray-200 px-2 py-1 font-manrope text-[12px] focus:border-gray-400 focus:outline-none"
      value={color}
      onChange={e => setColor(e.target.value)}
      placeholder="#000000"
    />
  </div>
</div>
```

---

## 4. Calendar / Date Picker

**Figma nodes:** `532:9168` (Advanced — date range) · `67:5366` (Small — un mes) · `67:5227` (Number-calendar — átomo de celda)

> ⚠️ El átomo `Number-calendar` (celda individual de día) está documentado en `components/ATOMS.md`. Este componente es la molécula completa.

### 4.1 Variantes

| Variante | Descripción | Meses visibles | Figma node |
|---|---|---|---|
| **Advanced** | Selector de rango de fechas — dos inputs de fecha + dos meses en paralelo | 2 | `532:9168` |
| **Small** | Selector de fecha única — un mes | 1 | `67:5366` |

### 4.2 Estructura (Advanced)

- **Header de inputs** — 2 campos de fecha (inicio / fin) · height `57px`
- **Grid de días** — 7 columnas (D L M M J V S) × 6 filas · celda `30×30px` (átomo `Number-calendar`)
- **Header de mes** — nombre del mes + año + flechas de navegación `‹` `›`
- **Botones de acción** — `button/secondary` (Cancelar) + `button/primary` (Aplicar)

Dimensiones Advanced: `635×491px`

### 4.3 Snippet

```tsx
// Calendar Small
<div className="w-[344px] rounded-[10px] border border-gray-200 bg-white p-4 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
  {/* Header mes */}
  <div className="mb-4 flex items-center justify-between">
    <button className="text-gray-600 hover:text-oxford"><ChevronLeftIcon className="h-4 w-4" /></button>
    <div className="flex gap-2">
      <button className="flex items-center gap-1 font-manrope text-[14px] font-semibold text-oxford">
        Mayo 2024 <ChevronDownIcon className="h-3 w-3" />
      </button>
    </div>
    <button className="text-gray-600 hover:text-oxford"><ChevronRightIcon className="h-4 w-4" /></button>
  </div>

  {/* Días de la semana */}
  <div className="mb-2 grid grid-cols-7 text-center">
    {['D','L','M','M','J','V','S'].map(d => (
      <span key={d} className="font-manrope text-[12px] text-gray-500">{d}</span>
    ))}
  </div>

  {/* Grid de días — cada celda es el átomo Number-calendar */}
  <div className="grid grid-cols-7 gap-0">
    {days.map(day => (
      <T1NumberCalendar key={day.date} day={day} onSelect={setDate} />
    ))}
  </div>
</div>
```

### 📱 Mobile

El Calendar Advanced en mobile se transforma en un único mes (Small) presentado como bottom sheet.

---

## 5. Upload

**Figma node:** `123:4151`

Zona de carga de archivos con drag & drop y variante de IA para procesamiento inteligente.

### 5.1 Variantes

| Variante | Descripción | Figma node |
|---|---|---|
| **Default** | Zona de drop inactiva · ícono + texto instructivo | `123:4149` |
| **Hover** | Zona de drop con archivo sobre ella · borde activo | `123:4267` |
| **Pressed** | Click activo en la zona | `123:4295` |
| **Disabled** | No interactivo · opacidad reducida | `123:4257` |
| **IA** | Variante con procesamiento IA · ícono diferenciado | `123:4202` |
| **Loading** | Archivo cargando · barra de progreso | `123:4220` |
| **Fill** | Archivo cargado · nombre + opción de eliminar | `123:4244` |

### 5.2 Tokens de estilo

| Estado | Border | BG | Figma node |
|---|---|---|---|
| **Default** | `gray-200` · dashed | `white` | `123:4149` |
| **Hover** | `red-500` · dashed | `red-50` | `123:4267` |
| **Disabled** | `gray-200` · dashed | `gray-50` | `123:4257` |
| **Fill** | `gray-200` · solid | `white` | `123:4244` |

Dimensiones: `677×100px` (compacto) · `677×80px` (IA/Loading/Fill)

### 5.3 Snippet

```tsx
<div
  onDragOver={handleDragOver}
  onDrop={handleDrop}
  className={`flex h-[100px] w-full cursor-pointer items-center justify-center rounded-[10px] border-2 border-dashed transition-colors ${
    isDragging
      ? 'border-red-500 bg-red-50'
      : 'border-gray-200 bg-white hover:border-gray-400 hover:bg-gray-50'
  }`}
>
  {!file ? (
    <div className="flex flex-col items-center gap-1 text-center">
      <ArrowUpTrayIcon className="h-6 w-6 text-gray-500" />
      <p className="font-manrope text-[14px] text-oxford">
        Arrastra tu archivo o <span className="text-red-500 underline">selecciona uno</span>
      </p>
      <p className="font-manrope text-[12px] text-gray-500">PNG, JPG, PDF · Máx 10MB</p>
    </div>
  ) : (
    <div className="flex w-full items-center justify-between px-4">
      <div className="flex items-center gap-3">
        <DocumentIcon className="h-6 w-6 text-oxford" />
        <span className="font-manrope text-[14px] text-oxford">{file.name}</span>
      </div>
      <button onClick={clearFile}>
        <XMarkIcon className="h-4 w-4 text-gray-500 hover:text-oxford" />
      </button>
    </div>
  )}
</div>
```

### 📱 Mobile

El Upload en mobile reduce su altura a `80px`. El drag & drop se deshabilita — solo queda el tap para seleccionar archivo desde galería o archivos del sistema.

---

## 6. Modal

**Figma node:** `86:3930` (Modal base) · `412:9145` (Modal instancia con slots)

El Modal es un contenedor de diálogo con slots intercambiables. No tiene un contenido fijo — sus slots se combinan según el caso de uso.

### 6.1 Slots disponibles

| Slot | Descripción | Figma node |
|---|---|---|
| `Slot/modal/empty` | Contenedor vacío — punto de partida | `86:3876` |
| `Slot/modal/Top` | Header del modal — título + botón cerrar | `86:3891` |
| `Slot/modal/Text` | Cuerpo de texto — párrafo o descripción | `86:3893` |
| `Slot/modal/button` | Área de acciones — botones CTA | `138:4262` |
| `Slot/modal/Map` | Slot de mapa embebido | `86:3928` |
| `Slot/modal/Toma+logo` | Slot con screenshot de la app + logo | `97:3920` |

### 6.2 Tokens de estilo

```css
border-radius: 10px;
background: white;
box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.1); /* shadow_card */
overlay: rgba(0, 0, 0, 0.6);               /* color/overlay/black 60% */
```

Dimensiones: Modal pequeño `309×235px` · Modal estándar `505×315px` · Modal grande (con Map) hasta `940×470px` para el slot de mapa.

### 6.3 Composición estándar

La combinación más común es: `Top` + `Text` + `button`.

```tsx
{/* Overlay */}
<div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60">
  {/* Modal */}
  <div className="w-[505px] rounded-[10px] bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">

    {/* Slot/modal/Top */}
    <div className="flex items-center justify-between border-b border-gray-200 px-6 py-4">
      <h2 className="font-manrope text-[14px] font-semibold text-oxford">Confirmar acción</h2>
      <button onClick={onClose}>
        <XMarkIcon className="h-4 w-4 text-gray-500 hover:text-oxford" />
      </button>
    </div>

    {/* Slot/modal/Text */}
    <div className="px-6 py-4">
      <p className="font-manrope text-[14px] text-oxford">
        ¿Estás seguro de que deseas continuar? Esta acción no se puede deshacer.
      </p>
    </div>

    {/* Slot/modal/button */}
    <div className="flex justify-end gap-3 border-t border-gray-200 px-6 py-4">
      <T1Button variant="secondary" onClick={onClose}>Cancelar</T1Button>
      <T1Button variant="primary" onClick={onConfirm}>Confirmar</T1Button>
    </div>

  </div>
</div>
```

### 6.4 Reglas de uso

- El overlay siempre es `rgba(0,0,0,0.6)` — nunca más claro ni más oscuro.
- El modal siempre tiene `Slot/modal/Top` con botón de cierre (X).
- El scroll interno aplica al slot de contenido, nunca al modal completo.
- Máximo un modal visible a la vez — no apilar modales.
- En mobile el modal ocupa el ancho completo como bottom sheet con `border-radius: 10px 10px 0 0`.

### 📱 Mobile

El Modal se presenta como **bottom sheet** en mobile: ocupa el ancho completo, aparece desde abajo, `border-radius: 10px 10px 0 0`, con handle indicador en la parte superior.

---

## 7. Tooltip

**Figma node:** dentro de `MOLECULES 2` (69:4133) · sección `TOOLTIP`

Texto contextual que aparece al hover sobre un elemento. Informativo, no interactivo.

### 7.1 Especificaciones

- BG: `oxford` (`#4C4C4C`)
- Text: `white` · Manrope Regular 12px
- `border-radius: 4px`
- Padding: `4px 8px`
- Flecha direccional según posición (top/bottom/left/right)
- Aparece con delay de ~200ms · desaparece al quitar el hover

### 7.2 Snippet

```tsx
<div className="relative inline-block">
  <button
    onMouseEnter={() => setVisible(true)}
    onMouseLeave={() => setVisible(false)}
    className="..."
  >
    <InformationCircleIcon className="h-4 w-4 text-gray-500" />
  </button>

  {visible && (
    <div className="absolute bottom-full left-1/2 mb-2 -translate-x-1/2 whitespace-nowrap rounded-[4px] bg-oxford px-2 py-1 font-manrope text-[12px] text-white shadow-sm">
      Texto explicativo
      {/* Flecha */}
      <div className="absolute left-1/2 top-full -translate-x-1/2 border-4 border-transparent border-t-oxford" />
    </div>
  )}
</div>
```

### 📱 Mobile

Los tooltips no aplican en mobile — se reemplazan por texto de ayuda visible directamente o por modales de información al tap.

---

## 8. Submenu

**Figma node:** `1134:8371` (Submenú instancia)

Menú contextual que aparece al hacer click en un elemento. Contiene acciones específicas para ese elemento.

### 8.1 Especificaciones

- BG: `white`
- Border: `gray-200`
- `border-radius: 10px`
- Shadow: `shadow_card` → `0 0 5px 1px rgba(0,0,0,0.1)`
- Sin shadow según reglas de dashboard — **excepción:** el submenu sí usa shadow porque es flotante
- Ancho: `161px` · Items: height `~48px` por item
- Tipografía items: Manrope Regular 14px · `oxford`

### 8.2 Snippet

```tsx
{open && (
  <div className="absolute right-0 top-full z-50 mt-1 w-[161px] rounded-[10px] border border-gray-200 bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
    {items.map(item => (
      <button
        key={item.id}
        onClick={item.action}
        className={`flex w-full items-center gap-2 px-4 py-3 font-manrope text-[14px] hover:bg-gray-50 first:rounded-t-[10px] last:rounded-b-[10px] ${
          item.destructive ? 'text-red-700' : 'text-oxford'
        }`}
      >
        {item.icon && <item.icon className="h-4 w-4" />}
        {item.label}
      </button>
    ))}
  </div>
)}
```

### 📱 Mobile

El Submenu en mobile se presenta como bottom sheet con la lista de acciones.

---

## 9. Timeline

**Figma node:** `172:6917` · Indicadores: `178:7126`

Componente de línea de tiempo para tracking de pedidos y eventos. Usado principalmente en T1 Envíos y T1 Tienda.

### 9.1 Variantes de item

| Variante | Descripción | Figma node |
|---|---|---|
| **Simple** | Evento con ícono + título + fecha | `172:6904` |
| **Collapsed** | Evento colapsado — solo título + fecha | `172:6918` |
| **Open** | Evento expandido con detalle adicional | `172:6945` |
| **Comment** | Item con comentario/nota adjunta | `179:5490` |
| **Date** | Separador de fecha entre grupos de eventos | `182:5387` |

### 9.2 Indicadores de evento

Íconos que marcan el tipo de evento en la línea de tiempo:

| Ícono | Significado | Figma node |
|---|---|---|
| `dot` | Evento genérico | `178:7125` |
| `check` | Completado / entregado | `178:7149` |
| `cart` | Pedido / compra | `178:7150` |
| `car` | En camino / envío | `178:7202` |
| `alert` | Alerta / problema | `179:5320` |
| `user` | Acción de usuario | `179:5359` |

### 9.3 Slots de contenido

| Slot | Descripción |
|---|---|
| `Slot/timeline/empty` | Punto de partida vacío |
| `Slot/timeline/products` | Lista de productos del pedido |
| `Slot/timeline/customer info` | Datos del cliente |
| `Slot/timeline/address` | Dirección de entrega |

### 9.4 Tokens de estilo

- Línea conectora: `gray-200` · `2px` de ancho
- Indicador completado: `green-500`
- Indicador pendiente: `gray-200`
- Indicador alerta: `red-500`
- Texto título evento: Manrope SemiBold 14px · `oxford`
- Texto fecha/hora: Manrope Regular 12px · `gray-600`

### 9.5 Snippet

```tsx
<div className="flex flex-col">
  {events.map((event, i) => (
    <div key={event.id} className="flex gap-4">
      {/* Indicador + línea */}
      <div className="flex flex-col items-center">
        <div className={`flex h-6 w-6 items-center justify-center rounded-full ${
          event.done ? 'bg-green-500' : 'bg-gray-200'
        }`}>
          <CheckIcon className="h-3 w-3 text-white" />
        </div>
        {i < events.length - 1 && (
          <div className="w-[2px] flex-1 bg-gray-200" />
        )}
      </div>

      {/* Contenido */}
      <div className="pb-6">
        <p className="font-manrope text-[14px] font-semibold text-oxford">{event.title}</p>
        <p className="font-manrope text-[12px] text-gray-600">{event.date}</p>
        {event.open && (
          <p className="mt-1 font-manrope text-[14px] text-oxford">{event.detail}</p>
        )}
      </div>
    </div>
  ))}
</div>
```

### 📱 Mobile

El Timeline no cambia estructuralmente en mobile — ya es una lista vertical. El ancho de la columna de contenido se ajusta al viewport.

---

## 10. Messages

**Figma node:** `72:4598`

Banners de mensaje informativo inline — no son toasts flotantes, son mensajes dentro del flujo de contenido.

### 10.1 Variantes

| Variante | Token BG | Token border/ícono | Cuándo usar | Figma node |
|---|---|---|---|---|
| **Info** | `blue-100` | `blue-500` | Información neutral, tips, instrucciones | `72:4599` |
| **Caution** | `orange-100` | `orange-500` | Advertencia no bloqueante, acciones que requieren atención | `72:4604` |
| **Danger** | `red-50` | `red-700` | Error, acción destructiva, bloqueo | `72:4609` |

> **Nota:** Para el sistema completo de notificaciones (toasts, banners persistentes, notificaciones push) ver `patterns/NOTIFICATIONS.md`.

### 10.2 Especificaciones

- Height: variable según contenido · mínimo `44px`
- `border-radius: 10px`
- Padding: `12px 16px`
- Ícono a la izquierda: `30×30px` (átomo indicador de estado)
- Tipografía: Manrope Regular 14px · `oxford`
- Ancho: `688px` desktop · `w-full` mobile

### 10.3 Snippet

```tsx
const messageStyles = {
  info:    { bg: 'bg-blue-100',   icon: 'text-blue-500',   border: 'border-blue-500' },
  caution: { bg: 'bg-orange-100', icon: 'text-orange-500', border: 'border-orange-500' },
  danger:  { bg: 'bg-red-50',     icon: 'text-red-700',    border: 'border-red-700' },
}

<div className={`flex items-start gap-3 rounded-[10px] border p-3 ${messageStyles[type].bg} ${messageStyles[type].border}`}>
  <div className={`mt-0.5 shrink-0 ${messageStyles[type].icon}`}>
    {type === 'info' && <InformationCircleIcon className="h-5 w-5" />}
    {type === 'caution' && <ExclamationTriangleIcon className="h-5 w-5" />}
    {type === 'danger' && <XCircleIcon className="h-5 w-5" />}
  </div>
  <p className="font-manrope text-[14px] text-oxford">{message}</p>
</div>
```

### 📱 Mobile

Los Messages son `w-full` en mobile. No cambian de estructura.

---

## 11. Steps / Onboarding

**Figma node:** `224:5753` (Steps container) · `224:6011` (Slot/steps/row) · `224:6092` (Carga)

Módulo de pasos para onboarding en el home del dashboard. Guía al usuario en los pasos iniciales de configuración.

### 11.1 Variantes

| Variante | Plataforma | Descripción | Figma node |
|---|---|---|---|
| **Default** | Desktop | Lista de pasos con íconos y estado | `224:5754` |
| **Default móvil** | Mobile | Misma lista adaptada a mobile | `224:5860` |
| **Card** | Desktop | Pasos presentados como cards horizontales | `224:5935` |
| **Card móvil** | Mobile | Cards de pasos adaptadas a mobile | `224:5948` |

### 11.2 Slots de fila

| Slot | Descripción | Figma node |
|---|---|---|
| `Icons` | Fila de pasos con íconos grandes — desktop | `224:6034` |
| `Icons móvil` | Fila de pasos con íconos — mobile | `224:6052` |

### 11.3 Barra de progreso de carga

Indicador de progreso porcentual de 0 a 90% en incrementos de 10. Figma node: `224:6092`.

- Componente: `Barra-Progreso B` (átomo) con valor dinámico
- Tokens: relleno `red-500` · fondo `gray-100`

### 11.4 Tokens de estilo (Steps)

- Step completado: ícono `green-500` · texto `oxford`
- Step activo: ícono `red-500` · texto `oxford` · highlighted
- Step pendiente: ícono `gray-200` · texto `gray-600`
- BG del módulo: `white` · `border-radius: 10px` · shadow `shadow_card`
- Separador entre pasos: `gray-200`

### 11.5 Snippet

```tsx
<div className="rounded-[10px] bg-white p-6 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
  <h3 className="mb-2 font-manrope text-[14px] font-semibold text-oxford">
    Configura tu tienda
  </h3>

  {/* Barra de progreso */}
  <div className="mb-6 h-[8px] w-full overflow-hidden rounded-full bg-gray-100">
    <div
      className="h-full rounded-full bg-red-500 transition-all duration-300"
      style={{ width: `${progress}%` }}
    />
  </div>

  {/* Lista de pasos */}
  <div className="flex flex-col divide-y divide-gray-200">
    {steps.map(step => (
      <div key={step.id} className="flex items-center gap-4 py-3">
        <div className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-full ${
          step.done ? 'bg-green-500' : step.active ? 'bg-red-500' : 'bg-gray-100'
        }`}>
          {step.done
            ? <CheckIcon className="h-4 w-4 text-white" />
            : <step.icon className={`h-4 w-4 ${step.active ? 'text-white' : 'text-gray-500'}`} />
          }
        </div>
        <div className="flex-1">
          <p className={`font-manrope text-[14px] font-semibold ${step.done || step.active ? 'text-oxford' : 'text-gray-600'}`}>
            {step.title}
          </p>
          {step.description && (
            <p className="font-manrope text-[12px] text-gray-600">{step.description}</p>
          )}
        </div>
        {!step.done && (
          <T1Button variant={step.active ? 'primary' : 'secondary'} size="sm">
            {step.active ? 'Completar' : 'Ver'}
          </T1Button>
        )}
      </div>
    ))}
  </div>
</div>
```

### 📱 Mobile

Las variantes `Default móvil` y `Card móvil` están explícitamente diseñadas en Figma. En mobile el módulo ocupa `w-full` y los pasos se presentan en una sola columna con menor padding.

---

## 12. Tabs

**Figma node:** `119:4183` (Tab item) · `119:4218` (Item pestañas) · `119:4182` (Pestañas — barra horizontal) · `119:4181` (Tabs — pill/capsule)

Existen **dos variantes** visuales con comportamiento idéntico pero apariencia distinta:

### 12.1 Variante 1 — Pestañas (navegación horizontal)

Fila de tabs con indicador inferior rojo en el tab activo. Usada para navegación principal dentro de una sección.

| Estado | Visual | Token | Figma node |
|---|---|---|---|
| **Select (activo)** | Texto `oxford` SemiBold + línea inferior `2px red-500` | `red-500` | `119:4184` |
| **Off (inactivo)** | Texto `oxford` SemiBold sin línea · hover BG `gray-50` | `gray-50` | `119:4187` |

```tsx
// Variante Pestañas — indicador inferior rojo
<div className="border-b border-gray-200">
  <nav className="flex">
    {tabs.map(tab => (
      <button
        key={tab.id}
        onClick={() => setActive(tab.id)}
        className={`flex items-center gap-2 px-4 pb-3 pt-2 font-manrope text-[14px] font-semibold transition-colors hover:bg-gray-50 ${
          active === tab.id
            ? 'border-b-2 border-red-500 text-oxford'
            : 'border-b-2 border-transparent text-oxford'
        }`}
      >
        {tab.icon && <tab.icon className="h-4 w-4" />}
        {tab.label}
      </button>
    ))}
  </nav>
</div>
```

### 12.2 Variante 2 — Tabs (pill / capsule)

Grupo de tabs con BG contenedor redondeado en `gray-50`. Tab activo con BG `white` y borde `gray-200`. Usada para filtros o sub-navegación dentro de una card o sección compacta.

| Estado | Visual | Token | Figma node |
|---|---|---|---|
| **Select (activo)** | BG `white` · borde `gray-200` · texto `oxford` SemiBold | `white`, `gray-200` | `119:4219` |
| **Off (inactivo)** | Sin BG · texto `oxford` SemiBold | — | `119:4224` |

```tsx
// Variante Tabs — pill con BG contenedor
<div className="inline-flex rounded-[10px] bg-gray-50 p-1">
  {tabs.map(tab => (
    <button
      key={tab.id}
      onClick={() => setActive(tab.id)}
      className={`flex items-center gap-2 rounded-[8px] px-3 py-1.5 font-manrope text-[14px] font-semibold transition-colors ${
        active === tab.id
          ? 'border border-gray-200 bg-white text-oxford shadow-sm'
          : 'text-oxford hover:bg-white/50'
      }`}
    >
      {tab.icon && <tab.icon className="h-4 w-4" />}
      {tab.label}
    </button>
  ))}
</div>
```

### 12.3 Cuándo usar cada variante

| Situación | Variante |
|---|---|
| Navegación principal de una vista o sección amplia | **Pestañas** (indicador rojo) |
| Filtro compacto dentro de una card o panel | **Tabs** (pill) |
| Más de 5 opciones | **Pestañas** (scrollable horizontal) |
| 2–4 opciones en espacio reducido | **Tabs** (pill) |

### 📱 Mobile

Ambas variantes son scrollables horizontalmente en mobile (`overflow-x: auto`, sin scrollbar visible). La variante Tabs pill mantiene su BG contenedor.

---

## 13. Cards

**Figma node:** `1134:8526` (MOLECULES 5)

Las Cards son **contenedores estáticos de dashboard** con estructura fija pero contenido variable. No tienen estados de interacción (hover/selected) salvo el **Card Selector** que se documenta por separado.

> **Card Selector** (encuestas, selección de plan, opciones visuales): tiene estado selected con border `red-500` y shadow `Red 200`. Ver `components/STATES.md` para su implementación.

### 13.1 Token base de todas las cards

```css
border-radius: 10px;          /* estándar — 20px para cards grandes */
background: white;
border: 1px solid #E7E7E7;    /* gray-200 */
box-shadow: 0 0 5px 1px rgba(0,0,0,0.1); /* shadow_card */
padding: 16px 20px;            /* base — variable según contenido */
```

### 13.2 Catálogo de estructuras

**Card Métrica** — `1134:9256`
Número grande + label descriptivo + delta de cambio. Usada en dashboards de analytics.

```
┌─────────────────────────┐
│ Total de miembros        │
│ 30                [+3]  │
│ este mes                 │
└─────────────────────────┘
```

**Card Resumen (Summary)** — `1134:9976`
Múltiples métricas en fila separadas por divisores verticales. Para resúmenes de pedidos, ventas, etc.

```
┌──────────────────────────────────────────────────┐
│ Pedidos │ Importe gastado │ Ticket promedio │ ... │
│    4    │    $37,035.00   │    $320.00      │ ... │
└──────────────────────────────────────────────────┘
```

**Card de Integración** — `1134:9762`
Logo del proveedor + nombre + chip de estado + link de configuración.

```
┌──────────────────┐
│ [Logo] Nombre    │
│        [Chip]    │
│ Configuración →  │
└──────────────────┘
```

**Card de Canal** — `1134:9797`
Logo + nombre + switch de activación + chip de estado. Para gestión de canales de venta.

```
┌────────────────────────────────┐
│ Canales de venta               │
│ [Logo] Nombre    [Switch][Chip]│
└────────────────────────────────┘
```

**Card de Sincronización** — `1134:9810`
Estado de última sincronización + botón de acción + indicador de fuente → destino.

**Card de Dirección** — `1134:9997`
Label + datos de dirección + badge de tipo + link de edición.

**Card Fiscal** — `1134:10022`
RFC + dirección fiscal + link de edición.

**Card de Notas** — `1134:10042`
Título + contenido de nota + link de edición.

**Card de Tags** — `1134:10033`
Título + input + chips de tags aplicados.

**Card de Lista** — `1134:10006`
Título + datos en fila + indicadores de estado.

**Card de Recarga de Saldo** — `1134:9109`
Instrucciones + logos de métodos de pago + botón de acción.

**Card de Cargos Adicionales** — `1134:9097`
Monto grande + descripción + texto link de detalle.

**Card de Perfil (Submenu)** — `1134:9498`
Avatar + nombre + email + lista de acciones de navegación. Se comporta como submenú desplegable.

### 13.3 Snippet base

```tsx
// Card base — aplica a la mayoría de estructuras
<div className="rounded-[10px] border border-gray-200 bg-white p-5 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
  {/* Header */}
  <div className="mb-4 flex items-center justify-between">
    <h3 className="font-manrope text-[14px] font-semibold text-oxford">Título de la card</h3>
    <T1Button variant="link">Editar</T1Button>
  </div>

  {/* Contenido — variable según tipo */}
  <div>{/* slots de contenido */}</div>
</div>

// Card Métrica
<div className="rounded-[10px] border border-gray-200 bg-white p-5 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
  <p className="font-manrope text-[12px] text-gray-600">Total de miembros</p>
  <div className="mt-1 flex items-end gap-2">
    <span className="font-manrope text-[32px] font-bold text-oxford">30</span>
    <span className="mb-1 font-manrope text-[12px] text-green-500">+3 este mes</span>
  </div>
</div>
```

### 📱 Mobile

Las cards en mobile ocupan `w-full`. Las cards de Summary colapsan su layout horizontal a vertical (cada métrica en su propia fila). Las cards de Integración y Canal mantienen su estructura pero con padding reducido.

---

## Notas para Claude

- Las moléculas **siempre referencian átomos** de `components/ATOMS.md` — no redefinir estilos de átomos dentro de una molécula.
- El **Modal en mobile** es siempre bottom sheet — nunca modal centrado en pantalla pequeña.
- Los **Tooltips** no aplican en mobile — siempre proveer alternativa táctil.
- Las **Cards** no tienen hover ni selected salvo el Card Selector (encuestas/planes) que usa border `red-500`.
- El **shadow_card** (`0 0 5px 1px rgba(0,0,0,0.1)`) aplica a todas las cards y componentes flotantes (submenú, dropdown de resultados).
- Header y Sidebar son **Organisms** — no están en este archivo. Ver `components/ORGANISMS.md`.

---

## Referencias cruzadas

| Archivo | Relación |
|---|---|
| `components/ATOMS.md` | Átomos usados en todas las moléculas |
| `components/ORGANISMS.md` | Header, Sidebar — usan moléculas como building blocks |
| `components/TABLES.md` | Tablas de datos — componente propio, no duplicado aquí |
| `components/STATES.md` | Card Selector (estado selected con Red 200) |
| `patterns/NOTIFICATIONS.md` | Sistema completo: toasts, banners persistentes, push |
| `foundation/COLORS.md` | Tokens de color referenciados en este archivo |
| `foundation/ELEVATION.md` | Shadow tokens — `shadow_card` definido aquí |
