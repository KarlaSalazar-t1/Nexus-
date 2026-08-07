# ATOMS — NEXUS V2.0 Design System

> **Categoría:** components  
> **Nivel:** Átomo (unidad mínima no divisible del sistema)  
> **Fuente:** Figma `SD - Migration V2` · frame `ATOMS` (node `1:652`)  
> **Última actualización:** 2025  
> **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Buttons](#1-buttons)
2. [Links](#2-links)
3. [Inputs & Text Fields](#3-inputs--text-fields)
4. [Select & Dropdowns](#4-select--dropdowns)
5. [Controls de Selección](#5-controls-de-selección)
6. [Badges & Chips](#6-badges--chips)
7. [Avatars](#7-avatars)
8. [Indicadores & Loaders](#8-indicadores--loaders)

---

## Convenciones de este archivo

- **Desktop first.** Las especificaciones base corresponden a viewport ≥ 1024px.
- **Variantes mobile** se documentan dentro de cada componente bajo el encabezado `📱 Mobile`.
- **Los colores se referencian siempre por token** definido en `foundation/COLORS.md` — nunca por hex directo. Si un valor hex cambia en COLORS.md, automáticamente aplica aquí.
- Todo snippet usa las **clases Tailwind del sistema** (ej: `text-oxford`, `bg-red-500`) configuradas en `globals.css` — no valores arbitrarios `[#hex]`.
- Naming de componentes: prefijo `T1` + PascalCase. Ej: `T1Button`, `T1Input`.

---

## Mapa de tokens usados en este archivo

Referencia rápida de los tokens de `foundation/COLORS.md` que aparecen en ATOMS:

| Token | Nombre | Valor |
|---|---|---|
| `color/brand/base/oxford` | Oxford | `#4C4C4C` |
| `color/brand/base/black` | Black | `#000000` |
| `color/brand/base/white` | White | `#FFFFFF` |
| `color/brand/red/500` | Red 500 | `#DB3B2B` |
| `color/brand/red/200` | Red 200 | `#F1B0A9` |
| `color/brand/red/700` | Red 700 | `#CC0000` |
| `color/brand/gray/50` | Gray 50 | `#F8F8F8` |
| `color/brand/gray/100` | Gray 100 | `#F3F3F3` |
| `color/brand/gray/200` | Gray 200 | `#E7E7E7` |
| `color/brand/gray/300` | Gray 300 | `#DBDBDB` |
| `color/brand/gray/400` | Gray 400 | `#CFCFCF` |
| `color/brand/gray/500` | Gray 500 | `#C3C3C3` |
| `color/brand/gray/600` | Gray 600 | `#9CA3AF` |
| `color/brand/blue/500` | Blue 500 | `#2180FF` |
| `color/brand/green/500` | Green 500 | `#4FC153` |
| `color/brand/green/100` | Green 100 | `#F0FDF4` |
| `color/brand/yellow/500` | Yellow 500 | `#EDBD55` |
| `color/brand/red/50` | Red 50 | `#FEF4F4` |

> Si un valor cambia en `foundation/COLORS.md`, actualiza solo ese archivo — los tokens referenciados aquí se actualizan automáticamente en la implementación.

---

## 1. Buttons

**Figma node:** `1:669` (Button) · `1:760` (Action 1 / Split) · `328:9117` (button/ia) · `667:7717` (Social)

Los botones son la acción primaria del sistema. Existen **8 variantes** con sus respectivos estados.

### 1.1 Variantes

| Variante | Descripción | Cuándo usar |
|---|---|---|
| **Primary** | BG rojo sólido, texto blanco | CTA principal — una sola acción primaria por vista |
| **Secondary** | Borde gris, fondo transparente | Acciones secundarias, cancelar, alternativas |
| **Link** | Sin borde/fondo, texto oxford | Acciones terciarias, navegación inline |
| **Split** | Botón dividido con chevron dropdown | Acciones con múltiples variantes (ej: "Exportar" → CSV / PDF) |
| **Icon** | Solo icono, sin texto | Acciones compactas en toolbars, tablas |
| **IA** | Estilo diferenciado con gradiente/ícono | Acciones de inteligencia artificial |
| **Social** | Logo de proveedor + texto | Autenticación con Google, Facebook, etc. |
| **Disclosure** | Texto + chevron expandible | Mostrar/ocultar secciones de contenido |

### 1.2 Estados por variante

**Primary / Secondary / Link**

| Estado | Primary | Secondary | Link |
|---|---|---|---|
| **Default** | BG: `red-500` · Text: `white` | Border: `gray-200` · BG: `white` · Text: `oxford` | Text: `oxford` |
| **Hover** | BG: `red-700` | BG: `gray-50` · Border: `gray-200` | Text: `black` · underline |
| **Pressed** | BG: `red-700` · opacity `0.9` | BG: `gray-100` | Text: `black` · opacity `0.8` · underline |
| **Disabled** | BG: `red-200` · Text: `white` | Border: `gray-200` · BG: `white` · Text: `gray-500` | Text: `gray-500` |
| **Loading** | Solo spinner (acción rápida) · Spinner + texto descriptivo (proceso activo, ej: "Analizando…") | Solo spinner | — |

> **Tokens Figma verificados:** `color/background/button/primary_disabled` → `red-200` · `color/border/button/secondary_default` → `gray-200` · `color/background/button/secondary_hover` → `gray-50` · `color/text/button/secondary_disabled` → `gray-500` · `color/text/link/enlace_default` → `oxford` · `color/text/link/enlace_hover` → `black` · `color/text/link/enlace_disabled` → `gray-500`

**Split** — Figma nodes `5:3939` (instancia base) · `1:760` (Action 1 — parte texto) · `1:777` (action2 — parte ícono/chevron)

El Split es un único componente dividido en **dos instancias independientes** para que cada parte tenga sus propios estados de interacción.

| Estado | Parte texto (Action 1) | Parte chevron (action2) | Figma node |
|---|---|---|---|
| **Default** | BG: `white` · Border: `gray-200` | BG: `white` · Border: `gray-200` | `1:761` · `1:778` |
| **Hover** | BG: `gray-50` | BG: `gray-50` | `1:765` · `1:790` |
| **Pressed** | BG: `gray-100` | BG: `gray-100` | `1:769` · `1:802` |
| **Disabled** | Border: `gray-200` · Text: `gray-500` | Border: `gray-200` · ícono `gray-500` | `1:773` · `1:814` |

**Icon** — Figma node `1:897`–`1:906`

Botón de solo ícono. Dimensiones: `24×24px`. Sin texto.

| Estado | Visual | Figma node |
|---|---|---|
| **Default** | Ícono `oxford` · sin fondo | `1:897` |
| **Hover** | Ícono `black` · BG `gray-50` | `1:900` |
| **Pressed** | Ícono `black` · BG `gray-100` | `1:903` |
| **Disabled** | Ícono `gray-500` · no interactivo | `1:906` |

**IA** — Figma node `328:9117`

Estilo visual diferenciado para señalar acciones con inteligencia artificial. Ver `foundation/COLORS.md` → Purple para los tokens de color.

| Estado | Figma node |
|---|---|
| **Default** | `328:9118` |
| **Hover** | `328:9135` |
| **Pressed** | `328:9142` |
| **Variant5** (estado alternativo activo) | `328:9125` |
| **Loading** | `328:9132` — solo spinner |

**Social** — Figma node `667:7717`

Botón de autenticación con proveedor externo. Incluye logo del proveedor + texto "Continuar con [Proveedor]".

| Estado | Figma node |
|---|---|
| **Default** | `667:7714` |
| **Hover** | `667:7781` |
| **Focus** | `667:7866` |
| **Disabled** | `667:7804` |
| **Error** | `667:7827` — muestra mensaje de error bajo el botón |

### 1.3 Tokens de estilo

```css
/* Tipografía */
font-family: Manrope, sans-serif;
font-size: 14px;
font-weight: 600; /* SemiBold */
line-height: 1;

/* Dimensiones base (dashboard) */
height: 35px;
padding: 0 16px;
border-radius: 10px;

/* Primary → color/brand/red/500 */
background-color: var(--color-red-500);
color: var(--color-white);

/* Secondary → color/brand/gray/200 */
background-color: transparent;
border: 1px solid var(--color-gray-200);
color: var(--color-oxford);
```

### 1.4 Props configurables

```tsx
type ButtonProps = {
  variant: 'primary' | 'secondary' | 'link' | 'split' | 'icon' | 'ia' | 'social' | 'disclosure'
  status?: 'default' | 'hover' | 'pressed' | 'disabled' | 'loading'
  showLeftIcon?: boolean
  showRightIcon?: boolean
  icon?: React.ReactNode
  fullWidth?: boolean
  children: React.ReactNode
  onClick?: () => void
}
```

### 1.5 Snippet

```tsx
// Primary Button
<button className="h-[35px] rounded-[10px] bg-red-500 px-4 font-manrope text-[14px] font-semibold text-white hover:bg-red-700 disabled:bg-red-200 disabled:cursor-not-allowed transition-colors">
  Guardar cambios
</button>

// Secondary Button
<button className="h-[35px] rounded-[10px] border border-gray-200 bg-white px-4 font-manrope text-[14px] font-semibold text-oxford hover:bg-gray-50 disabled:text-gray-500 disabled:cursor-not-allowed transition-colors">
  Cancelar
</button>

// Link Button
<button className="font-manrope text-[14px] font-medium text-oxford hover:text-black hover:underline disabled:text-gray-500 disabled:cursor-not-allowed transition-colors">
  Ver detalle
</button>

// Icon Button
<button className="flex h-[35px] w-[35px] items-center justify-center rounded-[10px] border border-gray-200 bg-white hover:bg-gray-50 disabled:text-gray-500 disabled:cursor-not-allowed transition-colors">
  <IconName className="h-4 w-4 text-oxford" />
</button>
```

### 1.6 Reglas de uso

- **Máximo un Primary** por sección o pantalla. Dos Primary juntos generan ambigüedad.
- El botón **Split** siempre tiene una acción default visible y un dropdown para variantes.
- El botón **IA** usa diferenciación visual explícita (gradiente, ícono especial) para señalar que la acción involucra inteligencia artificial.
- El botón **Social** incluye el logo oficial del proveedor (Google, Facebook, Instagram, etc.) seguido del texto "Continuar con [Proveedor]".
- **Loading:** dos comportamientos según el contexto:
  - **Solo spinner** → acción rápida, cambio de paso/pantalla (no requiere texto).
  - **Spinner + texto descriptivo** → proceso activo que toma tiempo (ej: "Analizando…", "Creando producto…"). El ancho del botón no cambia en ningún caso.

### 📱 Mobile

Los botones **no cambian de variante** en mobile. Los ajustes son de tamaño y táctil:

| Propiedad | Desktop | Mobile |
|---|---|---|
| Height | `35px` | `44px` (mínimo touch target) |
| Border radius | `8px` | `8px` |
| Font size | `14px` | `14px` |
| Full width | Opcional | Frecuente en CTAs de pantallas completas |

---

## 2. Links

**Figma node:** `1:909` (text-link) — subtipos: Text, Disclosure, Multiline

### 2.1 Variantes

| Variante | Descripción |
|---|---|
| **Text** | Link inline simple — una línea |
| **Disclosure** | Link + chevron (›) para expandir/colapsar |
| **Multiline** | Link que ocupa múltiples líneas con texto largo |

### 2.2 Estados

| Estado | Token | Decoración | Figma node |
|---|---|---|---|
| **Default** | `oxford` (`color/brand/base/oxford`) | Sin underline | `1:910` |
| **Hover** | `black` (`color/brand/base/black`) | Underline | `1:914` |
| **Pressed** | `black` · opacity `0.8` | Underline | `1:918` |
| **Disabled** | `gray-500` (`color/brand/gray/500`) | Sin underline · no interactivo | `1:922` |

### 2.3 Snippet

```tsx
// Link texto
<a
  href="/ruta"
  className="font-manrope text-[14px] font-medium text-oxford hover:text-black hover:underline transition-colors"
>
  Ver detalle
</a>

// Disclosure link
<button className="flex items-center gap-1 font-manrope text-[14px] font-medium text-oxford hover:text-black hover:underline disabled:text-gray-500 disabled:pointer-events-none">
  Más información
  <ChevronRightIcon className="h-3 w-3" />
</button>
```

### 📱 Mobile

Los links no cambian visualmente en mobile. El área táctil mínima debe ser `44×44px`.

---

## 3. Inputs & Text Fields

**Figma node:** `1:961` (TextField) · `1:1195`/`1:1216` (Input A/B) · `81:4700` (Number)

### 3.1 Variantes

| Variante | Descripción | Figma node |
|---|---|---|
| **Input** | Campo de texto estándar | `1:961` |
| **Prefix** | Con prefijo de texto (ej: `$`, `/`) | `1:998` |
| **Subfix** | Con sufijo de texto o ícono (ej: `kg`, ícono ojo) | `1:1025` |
| **Multiline** | Área de texto multilínea (textarea) | `1:1052` |
| **Number** | Input numérico con controles +/− | `81:4689` |
| **Split (Input A + B)** | Dos campos unidos: selector (A) + valor (B). Ej: selector `%`/`$` + campo numérico. | `1:1149` |
| **Teléfono** | Bandera del país + lada + campo de número. La bandera cambia según la lada seleccionada. | `1:1233`–`1:1258` |
| **Social** | Input con ícono de red social para ingresar link o @usuario. | — |

> ⚠️ **Input Split:** los frames `input a` e `input b` no son variantes independientes — forman un único componente Split. El campo A es el selector (ej: `%` o `$`) y el campo B es el valor numérico. Siempre van juntos.

> ⚠️ **Teléfono vs Prefix:** el input de teléfono **no es** el mismo que el input con prefix de texto. El de teléfono tiene bandera del país interactiva que cambia según la lada seleccionada.

### 3.2 Estados

| Estado | Border | Background | Label | Nota | Figma node |
|---|---|---|---|---|---|
| **Default** | `gray-200` | `white` | `oxford` | — | `1:962` |
| **Hover** | `gray-200` | `gray-50` | `oxford` | BG cambia, border igual | `1:969` |
| **Focus** | `gray-400` | `white` | `oxford` | Solo borde cambia | `1:990` |
| **Error** | `red-700` | `white` | `red-700` | Solo borde y label cambian | `1:976` |
| **Disabled** | `gray-200` | `white` | `gray-500` | BG sigue blanco | `1:983` |
| **Success** | `gray-200` | `white` | `oxford` | Solo se agrega ícono check `green-500` | — |
| **Read Only** | `gray-200` | `gray-50` | `gray-600` | No interactivo | — |

> ⚠️ **BG siempre blanco:** los estados Error, Disabled y Success mantienen `bg-white`. El color solo cambia en border y label. La excepción es Hover y Read Only que usan `gray-50`.

### 3.3 Tipografía interna

| Elemento | Font | Size | Weight | Token color |
|---|---|---|---|---|
| Label | Manrope | `14px` | Medium (500) | `oxford` |
| Value / texto ingresado | Manrope | `14px` | Regular (400) | `black` |
| Placeholder | Manrope | `14px` | Regular (400) | `gray-500` |
| Helper text / error msg | Manrope | `12px` | Regular (400) | según estado |
| Prefix / Subfix | Manrope | `14px` | Regular (400) | `gray-600` |

### 3.4 Snippet

```tsx
// Input estándar
<div className="flex flex-col gap-1">
  <label className="font-manrope text-[14px] font-medium text-oxford">
    Nombre
  </label>
  <input
    type="text"
    placeholder="Escribe tu nombre"
    className="h-[48px] rounded-[10px] border border-gray-200 bg-white px-3 font-manrope text-[14px] text-black placeholder:text-gray-500 hover:bg-gray-50 focus:border-gray-400 focus:outline-none disabled:text-gray-500 disabled:cursor-not-allowed transition-colors"
  />
</div>

// Input Split (selector % / $ + valor)
<div className="flex h-[48px] overflow-hidden rounded-[10px] border border-gray-200 hover:bg-gray-50 focus-within:border-gray-400">
  <select className="w-[72px] border-r border-gray-200 bg-gray-50 px-2 font-manrope text-[14px] text-oxford focus:outline-none">
    <option>%</option>
    <option>$</option>
  </select>
  <input
    type="number"
    className="flex-1 bg-white px-3 font-manrope text-[14px] text-black focus:outline-none"
    placeholder="0"
  />
</div>

// Input teléfono con bandera
<div className="flex h-[48px] overflow-hidden rounded-[10px] border border-gray-200 focus-within:border-gray-400">
  <button className="flex items-center gap-1.5 border-r border-gray-200 bg-gray-50 px-3 font-manrope text-[14px] text-oxford">
    🇲🇽 <span>+52</span> <ChevronDownIcon className="h-3 w-3" />
  </button>
  <input
    type="tel"
    className="flex-1 bg-white px-3 font-manrope text-[14px] focus:outline-none"
    placeholder="55 0000 0000"
  />
</div>

// Input social (link o @usuario)
<div className="flex h-[48px] overflow-hidden rounded-[10px] border border-gray-200 focus-within:border-gray-400">
  <span className="flex items-center border-r border-gray-200 bg-gray-50 px-3">
    <InstagramIcon className="h-4 w-4 text-gray-600" />
  </span>
  <input
    type="text"
    className="flex-1 bg-white px-3 font-manrope text-[14px] text-black focus:outline-none"
    placeholder="@usuario o link"
  />
</div>

// Input error (BG sigue blanco, solo borde y label cambian)
<div className="flex flex-col gap-1">
  <input
    className="h-[48px] rounded-[10px] border border-red-700 bg-white px-3 font-manrope text-[14px] focus:outline-none"
  />
  <p className="font-manrope text-[12px] text-red-700">Este campo es obligatorio</p>
</div>

// Input success (BG blanco + ícono check)
<div className="relative">
  <input
    className="h-[48px] w-full rounded-[10px] border border-gray-200 bg-white px-3 pr-10 font-manrope text-[14px] focus:outline-none"
  />
  <CheckCircleIcon className="absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-green-500" />
</div>
```

### 📱 Mobile

| Propiedad | Desktop | Mobile |
|---|---|---|
| Height | `48px` | `48px` |
| Font size | `14px` | `16px` mínimo (evita zoom automático en iOS) |
| Full width | Según layout | Siempre `w-full` |

> ⚠️ **Crítico mobile:** usar `font-size: 16px` en inputs móviles para prevenir el zoom automático de iOS Safari.

---

## 4. Select & Dropdowns

**Figma node:** `1:1351` (Dropdown) · `1:1534` (Select — Radio/Check) · `1:1559` (Image-radio)

### 4.1 Variantes

| Variante | Descripción | Figma node |
|---|---|---|
| **Dropdown** | Select nativo estilizado — una opción | `1:1351` |
| **Selector (Radio)** | Lista de opciones con radio button | `1:1535` |
| **Selector (Check)** | Lista de opciones con checkbox (múltiple selección) | `1:1341` |
| **Selector Múltiple** | Multi-select con chips para seleccionados | `1:718` |
| **Image Select / Image Radio** | Opciones con imagen o thumbnail | `1:1559` |

### 4.2 Estados del Dropdown

| Estado | Border | Background | Figma node |
|---|---|---|---|
| **Default** | `gray-200` | `white` | `1:1352` |
| **Hover** | `gray-200` | `gray-50` | `1:1371` |
| **Focus** | `gray-400` | `white` | `1:1365` |
| **Error** | `red-700` | `white` | `1:1358` |

### 4.3 Snippet

```tsx
<div className="relative">
  <select className="h-[48px] w-full appearance-none rounded-[10px] border border-gray-200 bg-white px-3 pr-8 font-manrope text-[14px] text-oxford hover:bg-gray-50 focus:border-gray-400 focus:outline-none">
    <option value="">Seleccionar categoría</option>
    <option value="ropa">Ropa</option>
  </select>
  <ChevronDownIcon className="pointer-events-none absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-600" />
</div>
```

### 📱 Mobile

El Dropdown usa el selector nativo del OS en mobile. Los selectores complejos (Image Select, Múltiple) pueden presentarse como bottom sheets en mobile.

---

## 5. Controls de Selección

**Figma node:** `1:1089` (Control — Switch/Radio/Check/Select)

### 5.1 Switch

| Estado | Track | Thumb | Figma node |
|---|---|---|---|
| **On** | `green-500` | `white` | `1:1090` |
| **Off** | `gray-200` | `white` | `1:1097` |
| **Disabled** | `gray-200` | `gray-50` · no interactivo | `1:1101` |

Dimensiones: `36×20px`.

```tsx
<button
  role="switch"
  aria-checked={isOn}
  className={`relative inline-flex h-[20px] w-[36px] items-center rounded-full transition-colors ${
    isOn ? 'bg-green-500' : 'bg-gray-200'
  } disabled:cursor-not-allowed`}
>
  <span className={`inline-block h-[16px] w-[16px] transform rounded-full transition-transform ${
    isOn ? 'translate-x-[18px] bg-white' : 'translate-x-[2px] bg-white'
  } disabled:bg-gray-50`} />
</button>
```

### 5.2 Radio Button

| Estado | Visual | Figma node |
|---|---|---|
| **On** | Círculo relleno `red-500` | `1:1115` |
| **Off** | Círculo borde `gray-200` · BG `white` | `1:1109` |
| **Hover** | Borde `gray-200` · BG `gray-50` | `1:1112` |
| **Disabled** | Borde `gray-200` · BG `white` · no interactivo | `1:1106` |

Dimensiones: `16×16px`.

### 5.3 Checkbox

| Estado | Visual | Figma node |
|---|---|---|
| **On** | Fondo `red-500` · checkmark `white` | `1:1139` |
| **Off** | Borde `gray-200` · fondo `white` | `1:1129` |
| **Hover** | Borde `gray-200` · BG `gray-50` | `1:1134` |
| **Indeterminate** | Línea horizontal en `red-500` | `1:1122` |
| **DisabledOn** | Fondo `gray-100` · checkmark `gray-500` | `1:1125` |
| **DisabledOff** | Borde `gray-200` · fondo `white` | `1:1145` |

Dimensiones: `16×16px`.

### 5.4 Favorite

| Estado | Visual | Figma node |
|---|---|---|
| **On** | Corazón relleno `red-500` | `1:1528` |
| **Off** | Corazón contorno `gray-200` | `1:1531` |

Dimensiones: `20×20px`.

### 5.5 Premium

| Estado | Visual | Figma node |
|---|---|---|
| **Default** | Ícono corona `gray-500` | `1:1568` |
| **Active** | Ícono corona `yellow-500` | `1:1570` |

### 📱 Mobile

El área táctil mínima debe ser `44×44px` — usar padding exterior para compensar el tamaño visual de `16px`.

```tsx
<label className="flex cursor-pointer items-center gap-2 min-h-[44px]">
  <input type="checkbox" className="sr-only" />
  <span className="flex h-[16px] w-[16px] ..." />
  <span className="font-manrope text-[14px] text-oxford">Opción</span>
</label>
```

---

## 6. Badges & Chips

**Figma node:** `1:1433` (Chips) · `1:1423` (Badges) · `1:1503` (Recomendado) · `1:1567` (Premium)

### 6.1 Chips

Etiquetas seleccionables y/o removibles. **5 variantes de color:**

| Variante | Token BG | Token Text | Uso | Figma node |
|---|---|---|---|---|
| **Violet** | `purple-100` | `purple-700` | Categorías premium, IA | `1:1467` |
| **Gray** | `gray-100` | `gray-700` | Tags neutrales, filtros | `1:1461` |
| **Blue** | `blue-100` | `blue-500` | Info, conectividad | `1:1443` |
| **Green** | `green-100` | `green-700` | Activo, éxito, positivo | `1:1446` |
| **Red** | `red-50` | `red-700` | Error, alerta, negativo | `1:1449` |

Dimensiones: `24px` alto · `border-radius: 4px` · padding `4px 8px`

```tsx
// Chip removible (variante blue)
<span className="inline-flex items-center gap-1 rounded-[4px] bg-blue-100 px-2 py-1 font-manrope text-[12px] font-medium text-blue-500">
  Conectado
  <button onClick={onRemove} className="ml-1 hover:opacity-70">
    <XMarkIcon className="h-3 w-3" />
  </button>
</span>
```

### 6.2 Badges de Estado

| Tipo | Token BG | Token Text | Cuándo usar |
|---|---|---|---|
| **Success** | `green-100` | `green-700` | Activo, completado, aprobado, pagado |
| **Warning** | `orange-100` | `orange-700` | Pendiente, en proceso, requiere atención |
| **Error** | `red-50` | `red-700` | Rechazado, error, fallido |
| **Info** | `blue-100` | `blue-500` | Informativo, neutral positivo |
| **Neutral** | `gray-100` | `gray-700` | Inactivo, sin estado, borrador |

### 6.3 Badges de Tendencia

| Tipo | Token BG | Token Text | Ícono | Figma node |
|---|---|---|---|---|
| **Positiva** | `green-100` | `green-700` | `↑` | `1:728` |
| **Negativa** | `red-50` | `red-700` | `↓` | `1:728` |
| **Neutra** | `gray-100` | `gray-700` | `—` | `1:728` |

### 6.4 Badges de Prioridad

Figma node: `1:729`.

| Nivel | Token BG | Token Text |
|---|---|---|
| **Alta** | `red-50` | `red-700` |
| **Media** | `orange-100` | `orange-700` |
| **Baja** | `green-100` | `green-700` |

### 6.5 Badge IA

Badge especial para señalar funcionalidades con IA. Figma node: `666:7648`. Dimensiones: `128×32px`. Usa tokens de `purple` — ver `foundation/COLORS.md`.

### 6.6 Badge Recomendado

Figma node: `1:503`. Dimensiones: `91×25px`.

### 6.7 Badge Premium

Ícono de corona. Token color: `yellow-500`. Figma node: `1:1567`.

### 📱 Mobile

Chips y badges no cambian en mobile. En listas largas los chips deben ser scrollables horizontalmente, no hacer wrap infinito.

---

## 7. Avatars

**Figma node:** `1:1470` (user-letter)

### 7.1 Tipos

| Tipo | Descripción | Figma node |
|---|---|---|
| **User (letra)** | Iniciales del usuario sobre fondo de color | `1:1471` |
| **Photo** | Foto de perfil circular | `1:1577` |
| **Store** | Logo o inicial de la tienda — forma cuadrada redondeada | `1:1490` |

### 7.2 Tamaños

| Tamaño | Dimensión | Uso |
|---|---|---|
| **SM** | `28×28px` | Tablas, listas compactas, comentarios inline |
| **MD** | `56×56px` | Cards de perfil, headers de sección, modales |

### 7.3 Estados

| Estado | Visual | Figma nodes |
|---|---|---|
| **Default** | Estático | `1:1471`, `1:1474` |
| **Hover** | Ring o overlay sutil | `1:1483`, `1:1486` |
| **Pressed** | Ring más marcado | `1:1477`, `1:1480` |

### 7.4 Snippet

```tsx
// Avatar letra - SM (color asignado algorítmicamente por nombre)
<div className="flex h-[28px] w-[28px] items-center justify-center rounded-full bg-red-500 font-manrope text-[11px] font-semibold text-white">
  KS
</div>

// Avatar foto - MD
<div className="h-[56px] w-[56px] overflow-hidden rounded-full">
  <img src="/foto.jpg" alt="Nombre usuario" className="h-full w-full object-cover" />
</div>

// Avatar store - MD
<div className="flex h-[36px] w-[36px] items-center justify-center rounded-[8px] bg-blue-100 font-manrope text-[14px] font-bold text-blue-500">
  T
</div>
```

### 7.5 Reglas

- El avatar **User** muestra máximo **2 iniciales** (nombre + apellido).
- El color de fondo del avatar con iniciales se asigna algorítmicamente por nombre para consistencia.
- El tipo **Store** usa `border-radius: 8px` (no circular) para diferenciarse del avatar de persona.

### 📱 Mobile

SM puede reducirse a `24px` en contextos muy compactos (notificaciones push, listas de alta densidad).

---

## 8. Indicadores & Loaders

**Figma nodes:** `1:1381` (Barra-Progreso A) · `526:9195` (Barra-Progreso B) · `1:1506` (progress vertical) · `1:1522` (progress select) · `1:1585` (iconos de estado)

### 8.1 Barra de Progreso

| Variante | Orientación | Alto | Figma node |
|---|---|---|---|
| **Barra-Progreso A** | Horizontal | `6px` | `1:1381` |
| **Barra-Progreso B** | Horizontal | `8px` | `526:9195` |
| **Vertical** | Vertical | — | `1:1506` |

Tokens: Relleno `red-500` · Fondo `gray-100`

```tsx
<div className="h-[6px] w-full overflow-hidden rounded-full bg-gray-100">
  <div
    className="h-full rounded-full bg-red-500 transition-all duration-300"
    style={{ width: `${progress}%` }}
  />
</div>
```

### 8.2 Indicadores de Estado (íconos circulares)

**5 tipos · 2 estilos (Default relleno / Line outline):**

| Tipo | Token color | Token BG (Default) | Cuándo usar | Figma node |
|---|---|---|---|---|
| **Success** | `green-500` | `green-100` | Completado, aprobado, activo | `1:1394` |
| **Error** | `red-700` | `red-50` | Fallo, rechazado | `24:3539` |
| **Warning** | `yellow-500` | `orange-100` | Atención requerida | `24:3541` |
| **Info** | `blue-500` | `blue-100` | Informativo neutro | `24:3540` |
| **Alert** | `red-500` | `red-50` | Alerta crítica | `1:1586` |

Dimensiones: `30×30px`.

```tsx
// Indicador success - Default
<div className="flex h-[30px] w-[30px] items-center justify-center rounded-full bg-green-100">
  <CheckCircleIcon className="h-5 w-5 text-green-500" />
</div>

// Indicador error - Line
<ExclamationCircleIcon className="h-[30px] w-[30px] text-red-700" />
```

### 8.3 Steps (Progreso de pasos)

Para wizards y flujos multi-etapa. Figma node: `1:731`.

| Estado | Visual |
|---|---|
| **Completado** | Círculo relleno `red-500` · checkmark `white` |
| **Activo** | Círculo borde `red-500` · número `red-500` |
| **Pendiente** | Círculo borde `gray-200` · número `gray-600` |

### 8.4 Cronología (Timeline)

Figma node: `1:732`.

- Línea vertical conectora: `gray-200`
- Punto completado: `red-500` · Punto pendiente: `gray-200`
- Texto del evento: Manrope Medium 14px · token `oxford`
- Tiempo/fecha: Manrope Regular 12px · token `gray-600`

### 8.5 Loader Spinner

```tsx
<svg className="animate-spin h-5 w-5 text-red-500" fill="none" viewBox="0 0 24 24">
  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
</svg>
```

### 8.6 Skeleton Loading

```tsx
// Skeleton línea
<div className="h-4 w-full animate-pulse rounded-[4px] bg-gray-100" />

// Skeleton card
<div className="rounded-[10px] border border-gray-100 bg-white p-4 space-y-3">
  <div className="h-4 w-3/4 animate-pulse rounded bg-gray-100" />
  <div className="h-4 w-1/2 animate-pulse rounded bg-gray-100" />
</div>
```

### 📱 Mobile

Los loaders no cambian en mobile. El skeleton se adapta al layout de cards (no tabla) en mobile.

---

## Notas para Claude

- **Siempre usar tokens, nunca hex directo.** Si un color no está en el mapa de tokens de este archivo, consultar `foundation/COLORS.md` antes de usar un valor arbitrario.
- Los **estados disabled** nunca disparan eventos: usar `pointer-events-none` + cambio de color por token.
- **Focus visible** es obligatorio: `focus-visible:ring-2 focus-visible:ring-blue-500` en todos los elementos interactivos.
- Los **touch targets** mínimos en mobile son `44×44px`.
- Ver `components/STATES.md` para el sistema completo de 10 estados obligatorios.
- Ver `accessibility/A11Y.md` para reglas de contraste, ARIA y keyboard navigation.

---

## Referencias cruzadas

| Archivo | Relación |
|---|---|
| `foundation/COLORS.md` | **Fuente de verdad de todos los tokens de color** usados en este archivo |
| `foundation/TYPOGRAPHY.md` | Escalas Manrope/Inter aplicadas en inputs, buttons, labels |
| `foundation/SPACING.md` | Padding y gaps internos |
| `components/STATES.md` | Sistema completo de estados de interacción |
| `components/MOLECULES.md` | Átomos combinados — Color Picker y Calendar viven aquí |
| `components/TABLES.md` | Documentación completa de tablas de datos |
| `accessibility/A11Y.md` | Contraste mínimo, touch targets, ARIA roles |
