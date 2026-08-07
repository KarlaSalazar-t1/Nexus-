# ICON-COMPONENT.md — Componente de Íconos

**Repositorio:** `t1-design-system`  
**Ruta:** `components/ICON-COMPONENT.md`  
**Audiencia:** Desarrolladores · Claude instances  
**Relacionado con:** [`assets/ICONOGRAPHY.md`](../assets/ICONOGRAPHY.md) · [`foundation/COLORS.md`](../foundation/COLORS.md) · [`accessibility/A11Y.md`](../accessibility/A11Y.md)

---

## Índice

1. [Arquitectura — estrategia híbrida](#1-arquitectura--estrategia-híbrida)
2. [Estructura de carpetas](#2-estructura-de-carpetas)
3. [Componente `<Icon />`](#3-componente-icon-)
4. [Catálogo de íconos disponibles](#4-catálogo-de-íconos-disponibles)
5. [Componente `<BrandLogo />`](#5-componente-brandlogo-)
6. [Componente `<Flag />`](#6-componente-flag-)
7. [Reglas de uso](#7-reglas-de-uso)
8. [Accesibilidad](#8-accesibilidad)
9. [Proceso de actualización](#9-proceso-de-actualización)

---

## 1. Arquitectura — estrategia híbrida

El ecosistema T1 usa **dos mecanismos distintos** para íconos y logos, según el tipo de asset:

| Tipo | Mecanismo | Componente | Color |
|------|-----------|------------|-------|
| Íconos del sistema (~150) | Inline SVG via TypeScript | `<Icon />` | `currentColor` — hereda del texto |
| Íconos de menú sidebar (31) | Inline SVG via TypeScript | `<Icon name="menu/..." />` | `currentColor` |
| Logos de terceros (300+) | Archivo `.svg` en `/public/` | `<BrandLogo />` | Colores propios del logo |
| Banderas ISO (250+) | Archivo `.svg` en `/public/` | `<Flag />` | Colores propios |
| Logos T1 Brand | Archivo `.svg` en `/public/` | `<BrandLogo brand="t1" />` | Variantes documentadas |

### Por qué esta separación

**Íconos del sistema → inline SVG:**
- Son monocromáticos (stroke `#4C4C4C`, heredan `currentColor`)
- Necesitan cambiar de color en estados (hover, active, disabled, semántico)
- ~150 íconos caben bien en un bundle TypeScript sin impacto significativo en peso
- Elimina 150+ peticiones HTTP o configuración de sprite

**Logos y banderas → archivos en `/public/`:**
- Tienen colores propios (Visa azul, DHL amarillo, banderas multicolor)
- No deben cambiar de color en estados normales
- Son cientos de archivos — incluirlos en bundle sería ineficiente
- Se cargan bajo demanda según el contexto del seller

---

## 2. Estructura de carpetas

```
components/
└── Icon/
    ├── Icon.tsx              ← Componente principal <Icon />
    ├── icons.ts              ← Mapa de 153 SVG paths (sistema + menú)
    └── index.ts              ← Re-export limpio

public/
└── assets/
    ├── logos/
    │   ├── t1/               ← Logos de marca T1 (t1pagos-default.svg, etc.)
    │   ├── payments/         ← Procesadores de pago (visa.svg, mastercard.svg...)
    │   ├── carriers/         ← Paqueterías (dhl.svg, fedex.svg, estafeta.svg...)
    │   ├── channels/         ← Canales de venta (amazon.svg, mercadolibre.svg...)
    │   └── banks/            ← Bancos mexicanos (bbva.svg, banamex.svg...)
    └── flags/                ← Banderas ISO 3166-1 alpha-2 (MX.svg, US.svg...)
```

---

## 3. Componente `<Icon />`

### 3.1 Archivo `icons.ts`

El archivo `icons.ts` contiene el mapa completo de **153 íconos** organizados en dos grupos:

- **122 íconos del sistema** — extraídos del artboard `Icons` de Figma
- **31 íconos de menú** — extraídos del artboard `Icon-menu`, accesibles con prefijo `menu/`

```ts
// Estructura de cada entrada
export const icons: Record<string, { vb: string; p: string }> = {
  'arrow-left': {
    vb: "0 0 17.0 16.16",       // viewBox calculado del bounding box real
    p: "<path d=\"...\" fill=\"currentColor\"/>"  // SVG inner HTML normalizado
  },
  'menu/home': {
    vb: "0 0 24.23 55.5",
    p: "<path d=\"...\" fill=\"currentColor\"/>..."
  },
  // ...
}

export type IconName = keyof typeof icons
export const iconNames = Object.keys(icons) as IconName[]
export const menuIconNames = iconNames.filter(n => n.startsWith('menu/'))
export const systemIconNames = iconNames.filter(n => !n.startsWith('menu/'))
```

> **Nota técnica:** Los viewBoxes son los bounding boxes reales de cada ícono en Figma — no el canvas 24×24 estándar. El componente `<Icon />` escala correctamente vía `width`/`height` y preserva la proporción del diseño original.

### 3.2 Implementación `Icon.tsx`

```tsx
// components/Icon/Icon.tsx
import { icons } from './icons'
import type { IconName } from './icons'

interface IconProps {
  name: IconName
  size?: number
  className?: string
  'aria-label'?: string
  'aria-hidden'?: boolean | 'true' | 'false'
}

export function Icon({
  name,
  size = 24,
  className = '',
  'aria-label': ariaLabel,
  'aria-hidden': ariaHidden,
}: IconProps) {
  const icon = icons[name]

  if (!icon) {
    if (process.env.NODE_ENV === 'development') {
      console.warn(`[Icon] Ícono no encontrado: "${name}"`)
    }
    return null
  }

  return (
    <svg
      width={size}
      height={size}
      viewBox={icon.vb}
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
      className={className}
      aria-label={ariaLabel}
      aria-hidden={ariaHidden ?? (ariaLabel ? undefined : 'true')}
      dangerouslySetInnerHTML={{ __html: icon.p }}
    />
  )
}
```

### 3.3 Re-export `index.ts`

```ts
// components/Icon/index.ts
export { Icon } from './Icon'
export type { IconName } from './icons'
export { icons, iconNames, menuIconNames, systemIconNames } from './icons'
```

### 3.4 Ejemplos de uso

```tsx
import { Icon } from '@/components/Icon'

// Ícono básico — decorativo (aria-hidden automático)
<Icon name="trash" size={24} />

// Ícono con color via Tailwind (className en el SVG)
<Icon name="search" size={20} className="text-gray-500" />

// Ícono funcional en botón — el aria-label va en el botón, no en el ícono
<button aria-label="Eliminar producto">
  <Icon name="action-trash" size={20} aria-hidden="true" />
</button>

// Ícono semántico con color de estado
<Icon name="status-alert" size={20} className="text-orange-500" />
<Icon name="status-info"  size={20} className="text-blue-500" />

// Ícono de menú sidebar
<Icon name="menu/home"         size={24} className="text-gray-500" />
<Icon name="menu/orders"       size={24} className="text-brand-red-500" />  // estado activo

// Tamaños estándar del sistema
<Icon name="action-search" size={16} />   {/* small — dentro de badges, inputs */}
<Icon name="action-search" size={24} />   {/* base  — UI estándar */}
<Icon name="action-search" size={30} />   {/* large — nav principal */}
```

### 3.5 Uso con colores semánticos

Los íconos heredan `currentColor` del padre. Para colorear, aplicar `text-{color}` al `<Icon />` o a un wrapper:

```tsx
// ✅ Correcto — color en el ícono directamente
<Icon name="finance-wallet" size={24} className="text-green-500" />

// ✅ Correcto — color heredado del padre
<span className="text-orange-500">
  <Icon name="status-alert" size={20} />
  <span>Advertencia</span>
</span>

// ✅ Correcto — ícono en contenedor de feature card (landing)
<div className="flex h-[52px] w-[52px] items-center justify-center rounded-[14px] bg-[#FEF4F4]">
  <Icon name="action-search" size={24} className="text-[#E26153]" />
</div>

// ❌ Incorrecto — no modificar fill/stroke directamente con CSS
<Icon name="trash" style={{ fill: '#DB3B2B' }} />
```

### 3.6 Colores permitidos para íconos en feature cards

Solo en el contexto de **landing pages**:

| Variante | Fondo contenedor | Color ícono |
|----------|-----------------|-------------|
| Rojo (principal) | `bg-[#FEF4F4]` | `text-[#E26153]` |
| Gris | `bg-[#F8F8F8]` | `text-[#4C4C4C]` |

> ⚠️ En **dashboard**, los íconos usan paleta semántica estándar (ver `foundation/COLORS.md`). Los colores azul, verde, violeta, naranja y turquesa para contenedores de íconos son exclusivos de landing.

---

## 4. Catálogo de íconos disponibles

### Íconos del sistema (122)

Organizados por categoría. Tamaño base: **24×24px**. Stroke: **1.5px**.

| Categoría | Prefijo | Cantidad | Ejemplos |
|-----------|---------|----------|---------|
| NAVIGATION — Arrows | `arrow-` | 6 | `arrow-left`, `arrow-right`, `arrow-up`, `arrow-down`, `arrow-up-short`, `arrow-down-short` |
| NAVIGATION — Chevrons | `chevron-` | 5 | `chevron-up`, `chevron-down`, `chevron-left`, `chevron-right`, `chevron-up-down` |
| NAVIGATION — Menu | `menu-` | 3 | `menu-hamburger`, `menu-kebab`, `menu-drag` |
| TEXT | `align-`, `indent-`, `list-` | 9 | `align-left`, `align-center`, `list-dot`, `list-number`, `list-check` |
| FILE | `file-` | 7 | `file-bill`, `file-text`, `file-excel`, `file-pdf` |
| BUILDER | `builder-` | 10 | `builder-header`, `builder-form`, `builder-product`, `builder-table`, `builder-catalog-list` |
| MEDIA | `media-` | 3 | `media-camera`, `media-multimedia`, `media-image` |
| ACTION | `action-` | 11 | `action-trash`, `action-close`, `action-copy`, `action-search`, `action-download`, `action-upload` |
| COMMUNICATION | `comm-` | 5 | `comm-mail`, `comm-comment`, `comm-sms`, `comm-whatsapp` |
| COMMERCE | `commerce-` | 9 | `commerce-cart`, `commerce-product`, `commerce-store`, `commerce-refund` |
| FINANCE | `finance-` | 9 | `finance-wallet`, `finance-cash`, `finance-transfer`, `finance-ticket` |
| DATA | `data-` | 8 | `data-grid`, `data-list`, `data-filter`, `data-order` |
| TIME | `time-` | 3 | `time-calendar`, `time-calendar-switch`, `time-watch` |
| STATUS | `status-` | 6 | `status-visible`, `status-hide`, `status-info`, `status-alert`, `status-help`, `status-lock` |
| USER | `user-` | 2 | `user-profile`, `user-perfiles` |
| TRANSFORM | `transform-` | 5 | `transform-rotate-left`, `transform-rotate-right`, `transform-reply`, `transform-color` |
| SYSTEM | `system-` | 9 | `system-laptop`, `system-mobile`, `system-tablet`, `system-pos`, `system-qr`, `system-ai` |
| MATH & MISC | `math-`, `misc-` | 12 | `math-plus`, `math-minus`, `misc-star`, `misc-bookmark`, `misc-lightbulb`, `misc-cvv` |

### Íconos de menú sidebar (31)

Prefijo: `menu/`. Uso exclusivo en sidebar de navegación del dashboard.

| Nombre | Descripción |
|--------|-------------|
| `menu/home` | Inicio / dashboard principal |
| `menu/user` | Perfil de usuario |
| `menu/online-store` | T1tienda |
| `menu/marketing` | T1marketing |
| `menu/gallery` | Galería de productos |
| `menu/discount` | Descuentos y promociones |
| `menu/product` | Catálogo de productos |
| `menu/channel` | Canales de venta |
| `menu/orders` | Gestión de pedidos |
| `menu/shipping` | T1envíos — logística |
| `menu/analytics` | Reportes y analíticas |
| `menu/insumos` | Tienda de insumos |
| `menu/payments` | T1pagos |
| `menu/balance` | Balance y saldos |
| `menu/link` | Links de cobro |
| `menu/transactions` | Historial de transacciones |
| `menu/settings` | Configuración |
| `menu/antifraude` | Sistema antifraude |
| `menu/developers` | API / desarrolladores |
| `menu/payment-method` | Métodos de pago guardados |
| `menu/cash` | Efectivo / caja |
| `menu/billing` | Facturación electrónica |
| `menu/hub` | Centro de integraciones |
| `menu/liquidaciones` | Liquidaciones |
| `menu/locations` | Ubicaciones / sucursales |
| `menu/roles` | Roles y permisos |
| `menu/security` | Seguridad de cuenta |
| `menu/data` | Gestión de datos |
| `menu/access` | Control de acceso |
| `menu/plans` | Planes y suscripciones |
| `menu/quality-control` | Control de calidad |

> **Íconos pendientes:** `menu/crown` (line y color) no están en el artboard exportado. Agregar a `icons.ts` cuando se exporte desde Figma.

---

## 5. Componente `<BrandLogo />`

Para logos de terceros y marca T1 almacenados como SVG en `/public/assets/logos/`.

### 5.1 Implementación

```tsx
// components/Icon/BrandLogo.tsx
import Image from 'next/image'

type LogoCategory = 't1' | 'payments' | 'carriers' | 'channels' | 'banks'

interface BrandLogoProps {
  /** Nombre del archivo sin extensión. Ej: "visa", "t1pagos-default", "dhl-iso" */
  name: string
  category: LogoCategory
  /** Ancho en px. Default: 30 */
  width?: number
  /** Alto en px. Default: 30 */
  height?: number
  className?: string
  /** Texto alternativo para accesibilidad. Dejar vacío si es decorativo */
  alt?: string
  /** Aplica filtro grayscale (para marquees de "Confianza" en landing) */
  grayscale?: boolean
  /** Aplica brightness-0 invert (para logos sobre fondos oscuros) */
  onDark?: boolean
}

export function BrandLogo({
  name,
  category,
  width = 30,
  height = 30,
  className = '',
  alt = '',
  grayscale = false,
  onDark = false,
}: BrandLogoProps) {
  const src = `/assets/logos/${category}/${name}.svg`

  const filterClasses = [
    grayscale ? 'grayscale opacity-40 hover:grayscale-0 hover:opacity-80 transition-all duration-300' : '',
    onDark ? 'brightness-0 invert' : '',
    className,
  ].filter(Boolean).join(' ')

  return (
    <Image
      src={src}
      alt={alt}
      width={width}
      height={height}
      className={filterClasses}
    />
  )
}
```

### 5.2 Ejemplos de uso

```tsx
import { BrandLogo } from '@/components/Icon/BrandLogo'

// Logo de pago — tamaño estándar 30×30
<BrandLogo name="visa" category="payments" width={30} height={30} alt="Visa" />
<BrandLogo name="mastercard" category="payments" alt="Mastercard" />

// Logo T1 — isotipo en header
<BrandLogo name="t1pagos-default" category="t1" width={120} height={32} alt="T1pagos" />

// Logo paquetería
<BrandLogo name="dhl-iso" category="carriers" alt="DHL" />

// Logo sobre fondo oscuro (aplica brightness-0 invert)
<BrandLogo name="fedex-logo" category="carriers" onDark alt="FedEx" />

// Marquee de confianza en landing (grayscale + hover)
<BrandLogo name="amazon" category="channels" grayscale alt="Amazon" />

// Logo de banco mexicano
<BrandLogo name="bbva" category="banks" width={64} height={64} alt="BBVA" />
```

### 5.3 Variantes de logos T1

| Nombre de archivo | Uso |
|------------------|-----|
| `t1-logotipo` | Logotipo T1 — header landing principal |
| `t1pagos-default` | T1pagos — color, sobre fondo claro |
| `t1pagos-white` | T1pagos — blanco, sobre fondo oscuro o rojo |
| `t1envios-default` | T1envíos — color, sobre fondo claro |
| `t1score-default` | T1score — color, sobre fondo claro |
| `t1marketing-default` | T1marketing — color, sobre fondo claro |

> Para el listado completo de logos de terceros disponibles, ver **[ICONOGRAPHY.md — sección 4](../assets/ICONOGRAPHY.md#4-logos-de-terceros-icons-logos)**.

---

## 6. Componente `<Flag />`

Para banderas de países almacenadas como SVG en `/public/assets/flags/`. Naming según ISO 3166-1 alpha-2.

### 6.1 Implementación

```tsx
// components/Icon/Flag.tsx
import Image from 'next/image'

interface FlagProps {
  /** Código ISO 3166-1 alpha-2. Ej: "MX", "US", "BR" */
  country: string
  /** Ancho en px. Default: 24 */
  width?: number
  /** Alto se calcula en proporción 3:2 automáticamente */
  height?: number
  className?: string
}

export function Flag({
  country,
  width = 24,
  height,
  className = '',
}: FlagProps) {
  // Proporción estándar de banderas: 3:2
  const h = height ?? Math.round(width * (2 / 3))
  const code = country.toUpperCase()

  return (
    <Image
      src={`/assets/flags/${code}.svg`}
      alt={`Bandera ${code}`}
      width={width}
      height={h}
      className={`rounded-sm ${className}`}
    />
  )
}
```

### 6.2 Ejemplos de uso

```tsx
import { Flag } from '@/components/Icon/Flag'

// Bandera estándar (24×16px)
<Flag country="MX" />
<Flag country="US" />
<Flag country="BR" />

// Bandera en selector de país
<div className="flex items-center gap-2">
  <Flag country="MX" width={20} />
  <span>México (+52)</span>
</div>

// Bandera grande
<Flag country="MX" width={48} />
```

---

## 7. Reglas de uso

### Tamaños estándar

| Tamaño | Uso |
|--------|-----|
| **16px** | Dentro de badges, chips, inputs compactos, texto inline |
| **24px** | UI estándar — botones, listas, cards, navegación (default) |
| **30px** | Chevrons de navegación principal · Logos de terceros |

❌ No usar 20px, 28px, 32px u otros tamaños fuera de este sistema.

### Estados del sidebar

Los íconos de menú cambian de color según el estado del nav item:

```tsx
// Estado default
<Icon name="menu/orders" size={24} className="text-gray-500" />

// Estado activo / seleccionado
<Icon name="menu/orders" size={24} className="text-brand-red-500" />

// Estado hover
<Icon name="menu/orders" size={24} className="text-gray-700 group-hover:text-gray-900" />

// Estado disabled
<Icon name="menu/orders" size={24} className="text-gray-300" />
```

### Anti-patrones

❌ Usar íconos de Heroicons, Lucide, Phosphor u otras librerías externas sin aprobación del equipo de diseño.  
❌ Modificar `fill` o `stroke` directamente en CSS — solo usar `currentColor` vía `text-{color}`.  
❌ Escalar íconos fuera de los tamaños estándar (16 / 24 / 30px).  
❌ Usar logos de terceros con colores alterados fuera de las variantes `onDark` y `grayscale`.  
❌ Agregar íconos al sistema directamente — el proceso de actualización requiere exportar desde Figma (ver sección 9).  
❌ Usar `menu/crown` para usuarios no premium.

---

## 8. Accesibilidad

### Íconos decorativos

Cuando el ícono complementa texto visible, debe ocultarse para lectores de pantalla:

```tsx
// ✅ Ícono decorativo junto a texto
<button className="flex items-center gap-2">
  <Icon name="action-download" size={16} aria-hidden="true" />
  <span>Descargar reporte</span>
</button>
```

### Íconos funcionales (sin texto visible)

Cuando el ícono es el único elemento comunicativo, el contexto semántico va en el elemento interactivo:

```tsx
// ✅ Ícono funcional — aria-label en el botón
<button aria-label="Eliminar producto">
  <Icon name="action-trash" size={20} aria-hidden="true" />
</button>

// ✅ Ícono con tooltip — aria-label en el ícono
<Icon name="status-help" size={16} aria-label="¿Qué es el contracargo?" />
```

### Comportamiento por default del componente

El componente `<Icon />` aplica `aria-hidden="true"` automáticamente cuando no se pasa `aria-label`. Esto significa que en la mayoría de casos no necesitas declararlo explícitamente:

```tsx
// Equivalentes — ambos ocultan el ícono de lectores de pantalla
<Icon name="arrow-right" size={20} />
<Icon name="arrow-right" size={20} aria-hidden="true" />

// Ícono accesible — solo cuando el ícono comunica información sin texto visible
<Icon name="status-alert" size={20} aria-label="Advertencia: saldo insuficiente" />
```

### Contraste

El color de un ícono sobre su fondo debe cumplir mínimo **WCAG AA (4.5:1)**. Los tokens del sistema están calibrados para esto — no usar colores arbitrarios.

---

## 9. Proceso de actualización

### Agregar nuevos íconos del sistema

1. Diseñador exporta el artboard `Icons` o `Icon-menu` actualizado desde Figma como SVG plano.
2. Ejecutar el script de extracción (ver `scripts/extract-icons.py` en el repo).
3. El script genera entradas nuevas para agregar a `icons.ts`.
4. PR con el `icons.ts` actualizado + actualización de este archivo.

### Agregar logos de terceros

1. Obtener el SVG oficial de la marca (no recrear).
2. Optimizar con SVGO manteniendo los colores originales.
3. Guardar en la subcarpeta correspondiente de `/public/assets/logos/`.
4. Documentar en `assets/ICONOGRAPHY.md`.

### Agregar banderas

1. Fuente recomendada: [flag-icons](https://github.com/lipis/flag-icons) (SVG optimizados, licencia MIT).
2. Guardar como `{CÓDIGO-ISO}.svg` en `/public/assets/flags/`.
3. El componente `<Flag />` las resuelve automáticamente.

---

## Referencias cruzadas

- **[assets/ICONOGRAPHY.md](../assets/ICONOGRAPHY.md)** — Catálogo visual completo: qué íconos existen, naming de Figma, logos de terceros, reglas de uso.
- **[foundation/COLORS.md](../foundation/COLORS.md)** — Tokens de color para estados semánticos de íconos.
- **[accessibility/A11Y.md](../accessibility/A11Y.md)** — Requisitos completos de contraste, ARIA y touch targets.
- **[components/ATOMS.md](../components/ATOMS.md)** — Cómo se integran íconos dentro de botones, badges, chips e inputs.
