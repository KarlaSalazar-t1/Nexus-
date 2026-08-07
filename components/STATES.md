# STATES — NEXUS V2.0 Design System

> **Categoría:** components  
> **Propósito:** Referencia rápida del sistema de estados de interacción — consolida lo documentado en ATOMS.md y MOLECULES.md en un solo lugar para implementación consistente  
> **Última actualización:** 2025  
> **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Los 10 estados del sistema](#1-los-10-estados-del-sistema)
2. [Tokens de estado por categoría](#2-tokens-de-estado-por-categoría)
3. [Estados por componente — tabla de referencia](#3-estados-por-componente--tabla-de-referencia)
4. [Card Selector — estado selected](#4-card-selector--estado-selected)
5. [Reglas de implementación](#5-reglas-de-implementación)
6. [Accesibilidad de estados](#6-accesibilidad-de-estados)

---

## 1. Los 10 estados del sistema

Todo componente interactivo de NEXUS puede existir en alguno de estos 10 estados. No todos los componentes tienen todos los estados — cada componente implementa el subconjunto que aplica a su función.

| # | Estado | Cuándo ocurre | Señal visual obligatoria |
|---|---|---|---|
| 1 | **Default** | Estado base en reposo | Apariencia estándar del componente |
| 2 | **Hover** | Cursor sobre el elemento | Cambio de BG o color — señala interactividad |
| 3 | **Focus** | Navegación por teclado / click activo | Ring o borde visible — obligatorio para a11y |
| 4 | **Pressed / Active** | Durante el click o tap | BG más oscuro u opacidad reducida |
| 5 | **Loading** | Acción en proceso | Spinner — texto solo si el proceso tarda y necesita nombre |
| 6 | **Disabled** | No disponible en el contexto actual | Opacidad reducida · no interactivo · cursor `not-allowed` |
| 7 | **Error** | Validación fallida o error del sistema | Borde/texto `red-700` · mensaje de ayuda inline |
| 8 | **Success** | Acción completada correctamente | Ícono check `green-500` · sin cambio de BG |
| 9 | **Selected** | Elemento elegido en una selección | Indicador visual de selección activa |
| 10 | **Empty** | Sin contenido disponible | Mensaje contextual + CTA de recuperación |

---

## 2. Tokens de estado por categoría

Todos los valores referencian `foundation/COLORS.md`.

### 2.1 Estados de interacción (hover, focus, pressed)

| Estado | Token BG | Token border | Token text | Aplica a |
|---|---|---|---|---|
| **Hover** | `gray-50` | `gray-200` (sin cambio) | sin cambio | Botones, inputs, filas, tabs, controles |
| **Focus** | sin cambio | `gray-400` | sin cambio | Inputs, dropdowns, selects |
| **Pressed** | `gray-100` | sin cambio | sin cambio | Botones secondary, split, icon |
| **Focus visible (a11y)** | sin cambio | `blue-500` ring 2px | sin cambio | Todos los elementos interactivos |

### 2.2 Estados semánticos (error, success, loading, disabled)

| Estado | Token BG | Token border | Token text/icon | Aplica a |
|---|---|---|---|---|
| **Error** | `white` | `red-700` | `red-700` | Inputs, dropdowns, forms, Social button |
| **Success** | `white` | `gray-200` (sin cambio) | ícono `green-500` | Inputs |
| **Loading** | sin cambio | sin cambio | spinner `red-500` | Buttons, acciones async |
| **Disabled (button primary)** | `red-200` | — | `white` | Button primary |
| **Disabled (button secondary/link)** | `white` | `gray-200` | `gray-500` | Button secondary, link, icon, split |
| **Disabled (inputs/controls)** | `white` | `gray-200` | `gray-500` | Inputs, dropdowns, checkbox, radio |
| **Disabled (switch)** | `gray-200` | — | thumb `gray-50` | Switch |

### 2.3 Estado selected

| Componente | Token BG | Token border | Token indicador |
|---|---|---|---|
| **Tab activo (Pestañas)** | sin cambio | — | borde inferior `red-500` 2px |
| **Tab activo (pill)** | `white` | `gray-200` | — |
| **Radio / Checkbox on** | — | — | relleno `red-500` |
| **Switch on** | `green-500` (track) | — | thumb `white` |
| **Favorite on** | — | — | corazón `red-500` |
| **Card Selector selected** | `white` | `red-500` 2px | shadow `red-200` |
| **Fila de tabla seleccionada** | `gray-50` | — | — |
| **Steps activo** | `red-500` | — | número/ícono `white` |

---

## 3. Estados por componente — tabla de referencia

Tabla de qué estados implementa cada componente. ✅ = implementado · — = no aplica.

| Componente | Default | Hover | Focus | Pressed | Loading | Disabled | Error | Success | Selected | Empty |
|---|---|---|---|---|---|---|---|---|---|---|
| **Button Primary** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — | — |
| **Button Secondary** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — | — |
| **Button Link** | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | — | — | — |
| **Button Split** | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | — | — | — |
| **Button Icon** | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | — | — | — |
| **Button IA** | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — | — | — |
| **Button Social** | ✅ | ✅ | ✅ | — | — | ✅ | ✅ | — | — | — |

> ⚠️ **Los colores de estado varían por variante de botón.** Primary usa `red-500`/`red-700`/`red-200`. IA usa su propia paleta `purple`. Los tokens exactos por variante están en `components/ATOMS.md → 1.2 Estados por variante`.
| **Link (Text/Disclosure)** | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | — | — | — |
| **Input** | ✅ | ✅ | ✅ | — | — | ✅ | ✅ | ✅ | — | — |
| **Dropdown / Select** | ✅ | ✅ | ✅ | — | — | ✅ | ✅ | — | — | — |
| **Switch** | ✅ | — | ✅ | — | — | ✅ | — | — | ✅ | — |
| **Radio** | ✅ | ✅ | ✅ | — | — | ✅ | — | — | ✅ | — |
| **Checkbox** | ✅ | ✅ | ✅ | — | — | ✅ | — | — | ✅ | — |
| **Tabs (Pestañas)** | ✅ | ✅ | ✅ | — | — | — | — | — | ✅ | — |
| **Tabs (pill)** | ✅ | ✅ | ✅ | — | — | — | — | — | ✅ | — |
| **Card Selector** | ✅ | ✅ | ✅ | — | — | — | — | — | ✅ | — |
| **Fila de tabla** | ✅ | ✅ | — | — | — | — | — | — | ✅ | — |
| **Upload** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | ✅ | — | — |
| **Number-calendar** | ✅ | ✅ | ✅ | — | — | — | — | — | ✅ | — |
| **Steps** | ✅ | — | — | — | ✅ | — | — | ✅ | ✅ | — |
| **Tabla completa** | ✅ | — | — | — | ✅ | — | ✅ | — | — | ✅ |

> Para los tokens y especificaciones visuales detalladas de cada estado por componente, ver `components/ATOMS.md` y `components/MOLECULES.md`.

---

## 4. Card Selector — estado selected

Componente especial usado en flujos de selección visual: encuestas, selección de plan, elección de opción entre varias. Es el único tipo de card con estado interactivo.

### 4.1 Estados

| Estado | BG | Border | Shadow |
|---|---|---|---|
| **Default** | `white` | `gray-200` 1px | `shadow_card` estándar |
| **Hover** | `gray-50` | `gray-200` 1px | `shadow_card` estándar |
| **Selected** | `white` | `red-500` 2px | shadow `red-200` |
| **Disabled** | `white` | `gray-200` 1px | sin shadow · opacidad `0.5` |

### 4.2 Shadow selected

```css
/* Estado selected — shadow con Red 200 */
box-shadow: 0 0 0 2px var(--color-red-200);
border: 2px solid var(--color-red-500);
```

### 4.3 Snippet

```tsx
<button
  onClick={() => setSelected(option.id)}
  className={`rounded-[10px] border-2 bg-white p-4 text-left transition-all ${
    selected === option.id
      ? 'border-red-500 shadow-[0_0_0_2px_theme(colors.red.200)]'
      : 'border-gray-200 shadow-[0_0_5px_1px_rgba(0,0,0,0.1)] hover:bg-gray-50'
  }`}
>
  {/* contenido de la opción */}
  <p className="font-manrope text-[14px] font-semibold text-oxford">{option.label}</p>
  {option.description && (
    <p className="mt-1 font-manrope text-[12px] text-gray-600">{option.description}</p>
  )}
</button>
```

### 4.4 Uso en contexto

```tsx
// Grid de opciones tipo encuesta
<div className="grid grid-cols-2 gap-3 md:grid-cols-3">
  {options.map(option => (
    <T1CardSelector
      key={option.id}
      selected={selected === option.id}
      onClick={() => setSelected(option.id)}
    >
      {option.icon && <option.icon className="mb-2 h-6 w-6 text-oxford" />}
      <p className="font-manrope text-[14px] font-semibold text-oxford">{option.label}</p>
    </T1CardSelector>
  ))}
</div>
```

---

## 5. Reglas de implementación

### 5.1 Disabled

- Siempre `pointer-events-none` — nunca solo cambio de color
- Nunca disparar eventos de un elemento disabled
- El cursor debe ser `not-allowed` visualmente

```tsx
// Patrón correcto para disabled
<button
  disabled={isDisabled}
  className={`... ${isDisabled ? 'cursor-not-allowed opacity-50 pointer-events-none' : ''}`}
>
```

### 5.2 Loading

- El ancho del botón **no cambia** al entrar en loading
- **Solo spinner** → acción rápida o cambio de paso/pantalla
- **Spinner + texto** → proceso con nombre propio (ej: "Analizando…", "Creando envío…", "Generando reporte…")
- Mientras loading está activo el botón debe ser `disabled` — no permite doble click

```tsx
<button disabled={isLoading} className="h-[35px] min-w-[120px] ...">
  {isLoading ? (
    <div className="flex items-center justify-center gap-2">
      <svg className="animate-spin h-4 w-4 text-white" .../>
      {loadingText && <span>{loadingText}</span>}
    </div>
  ) : children}
</button>
```

### 5.3 Error

- El mensaje de error va **inline bajo el campo** — nunca como toast para errores de validación de formulario
- El borde y el label cambian a `red-700`
- El BG del input **no cambia** — siempre `white`
- El mensaje usa Manrope Regular 12px · `red-700`

```tsx
<div className="flex flex-col gap-1">
  <input className={`... ${hasError ? 'border-red-700' : 'border-gray-200'}`} />
  {hasError && (
    <p className="font-manrope text-[12px] text-red-700" role="alert">
      {errorMessage}
    </p>
  )}
</div>
```

### 5.4 Focus visible (accesibilidad)

Todo elemento interactivo debe tener un estado de focus visible para navegación por teclado. Es obligatorio — no se elimina con `outline-none` sin reemplazo.

```tsx
// Patrón correcto — focus-visible preserva a11y sin afectar usuarios de mouse
className="focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-1"
```

> `focus-visible` solo muestra el ring cuando el usuario navega por teclado — no aparece al hacer click con mouse. Ver `accessibility/A11Y.md` para reglas completas.

### 5.5 Transiciones

Los cambios de estado deben tener transición suave para no ser abruptos:

```css
transition: colors 150ms ease;   /* Para cambios de color — hover, focus */
transition: all 200ms ease;      /* Para cambios que incluyen transform o shadow */
```

En Tailwind: `transition-colors` para la mayoría · `transition-all duration-200` para card selector y elementos con shadow.

---

## 6. Accesibilidad de estados

Ver `accessibility/A11Y.md` para el sistema completo. Resumen de requisitos mínimos por estado:

| Estado | Requisito a11y |
|---|---|
| **Disabled** | `disabled` attr en HTML · `aria-disabled="true"` en elementos no nativos |
| **Loading** | `aria-busy="true"` · `aria-label` descriptivo (ej: "Guardando cambios…") |
| **Error** | `aria-invalid="true"` en el input · `aria-describedby` apuntando al mensaje de error |
| **Selected** | `aria-selected="true"` en tabs · `aria-checked="true"` en radio/checkbox/switch |
| **Focus** | `focus-visible` ring obligatorio — nunca `outline: none` sin alternativa visible |
| **Empty** | Mensaje de empty state legible por screen reader · CTA con label descriptivo |

---

## Referencias cruzadas

| Archivo | Relación |
|---|---|
| `components/ATOMS.md` | Especificaciones visuales detalladas de estados por átomo |
| `components/MOLECULES.md` | Estados de moléculas (Modal, Upload, Steps, etc.) |
| `components/TABLES.md` | Estados de filas y tabla (hover, seleccionada, empty, error de carga) |
| `foundation/COLORS.md` | Tokens de color de todos los estados |
| `accessibility/A11Y.md` | Requisitos ARIA, contraste y navegación por teclado |
