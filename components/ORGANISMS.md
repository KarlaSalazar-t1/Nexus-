# ORGANISMS — NEXUS V2.0 Design System

> **Categoría:** components  
> **Nivel:** Organismo (combinación de moléculas y átomos que forman secciones de UI completas)  
> **Contexto:** Dashboard — todos los organismos de este archivo son de contexto admin  
> **Fuente:** Figma `SD - Migration V2` · frame `MENU` (node `232:7239`)  
> **Última actualización:** 2025  
> **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Layout base del dashboard](#1-layout-base-del-dashboard)
2. [Header](#2-header)
3. [Sidebar — estructura común](#3-sidebar--estructura-común)
4. [Sidebar — variantes por producto](#4-sidebar--variantes-por-producto)
5. [Estados del sidebar](#5-estados-del-sidebar)
6. [Nav item — molécula base](#6-nav-item--molécula-base)
7. [Reglas de implementación](#7-reglas-de-implementación)

---

## 1. Layout base del dashboard

Todo dashboard del ecosistema T1 sigue el mismo layout de dos columnas: sidebar fijo a la izquierda + área de contenido a la derecha.

```
┌──────────────────────────────────────────────────────────┐
│  Header (100% ancho · fixed top · h-[48px])              │
├────────────────────┬─────────────────────────────────────┤
│                    │                                     │
│  Sidebar           │  Área de contenido                  │
│  (fixed left)      │  (scroll vertical)                  │
│                    │                                     │
│  Expandido: 184px  │  Con sidebar expandido:             │
│  Colapsado:  48px  │  padding-left: 184px                │
│                    │  Con sidebar colapsado:             │
│                    │  padding-left: 48px                 │
│                    │                                     │
└────────────────────┴─────────────────────────────────────┘
```

### 1.1 Tokens de layout

| Elemento | Valor |
|---|---|
| Header height | `48px` |
| Sidebar width expandido | `184px` |
| Sidebar width colapsado | `48px` |
| Contenido max-width | `1600px` |
| Contenido padding | `24px` |
| BG global | `white` |

### 1.2 Snippet de layout

```tsx
// app/layout.tsx — Layout base del dashboard
export default function DashboardLayout({ children }) {
  const [collapsed, setCollapsed] = useState(false)

  return (
    <div className="min-h-screen bg-white">
      {/* Header — fixed top, full width */}
      <T1Header collapsed={collapsed} onToggle={() => setCollapsed(!collapsed)} />

      {/* Sidebar — fixed left, below header */}
      <T1Sidebar
        collapsed={collapsed}
        className="fixed left-0 top-[48px] h-[calc(100vh-48px)]"
      />

      {/* Contenido — margen izquierdo dinámico */}
      <main className={`pt-[48px] transition-all duration-200 ${
        collapsed ? 'pl-[48px]' : 'pl-[184px]'
      }`}>
        <div className="mx-auto max-w-[1600px] p-6">
          {children}
        </div>
      </main>
    </div>
  )
}
```

---

## 2. Header

El header es consistente en todos los productos del ecosistema. Sus elementos varían levemente por producto.

**Figma node:** `232:7298` (T1 Envíos full) — referencia del header

### 2.1 Anatomía

```
┌──────────────────────────────────────────────────────────────────┐
│ [≡] [Logo producto]  [Selector tienda ∨]  [Búsqueda___] [Q]    │  [Saldo $] [›] [⊞] [?] [🔔] [AE] │
└──────────────────────────────────────────────────────────────────┘
```

### 2.2 Elementos del header

| Elemento | Descripción | Aparece en |
|---|---|---|
| **Toggle sidebar** | Ícono `≡` — colapsa/expande el sidebar | Todos los productos |
| **Logo producto** | Logotipo del producto activo (T1 Tienda, T1 Envíos, T1 Pagos…) | Todos |
| **Selector de tienda** | Avatar color + nombre de tienda + chevron `∨` — abre dropdown para cambiar tienda | T1 Tienda, T1 Envíos |
| **Búsqueda** | Input centrado con placeholder contextual (ej: "Número de rastreo") | T1 Envíos |
| **Saldo** | `$` + monto + `›` — abre panel de saldo/recarga | T1 Envíos |
| **Switch de productos** | Ícono `⊞` — abre selector de productos del ecosistema | Todos |
| **Ayuda** | Ícono `?` | Todos |
| **Notificaciones** | Ícono `🔔` con badge rojo de contador | Todos |
| **Avatar usuario** | Foto de perfil circular o iniciales — abre submenu de cuenta | Todos |

### 2.3 Tokens de estilo

```css
/* Header */
height: 48px;
background: white;
border-bottom: 1px solid var(--color-gray-200);
position: fixed;
top: 0;
left: 0;
right: 0;
z-index: 50;
padding: 0 16px;
```

### 2.4 Selector de tienda

- Avatar: `32×32px` · círculo · BG color asignado a la tienda · iniciales en `white`
- Nombre de tienda: Manrope Medium 14px · `oxford`
- Chevron `∨`: `gray-600`
- Click → dropdown de tiendas disponibles para cambiar contexto

### 2.5 Badge de notificaciones

- Círculo `red-500` · `16×16px` · posición absolute top-right del ícono
- Número en `white` · Manrope SemiBold 10px
- Máximo muestra `99` — si hay más: `99+`

### 2.6 Diferencias por producto

| Producto | Búsqueda | Saldo | Selector tienda |
|---|---|---|---|
| **T1 Tienda** | — | — | ✅ |
| **T1 Envíos** | ✅ "Número de rastreo" | ✅ | ✅ |
| **T1 Pagos** | — | — | ✅ |
| **T1 Cuenta** | — | — | ❌ (es config de cuenta) |

### 2.7 Snippet

```tsx
<header className="fixed left-0 right-0 top-0 z-50 flex h-[48px] items-center justify-between border-b border-gray-200 bg-white px-4">
  {/* Lado izquierdo */}
  <div className="flex items-center gap-3">
    {/* Toggle sidebar */}
    <button
      onClick={onToggle}
      className="flex h-8 w-8 items-center justify-center rounded-[8px] hover:bg-gray-50"
    >
      <Bars3Icon className="h-4 w-4 text-oxford" />
    </button>

    {/* Logo del producto */}
    <T1Logo product="enviос" />

    {/* Selector de tienda */}
    <button className="flex items-center gap-2 rounded-[8px] px-2 py-1 hover:bg-gray-50">
      <div className="flex h-[28px] w-[28px] items-center justify-center rounded-full bg-green-500 font-manrope text-[11px] font-semibold text-white">
        CO
      </div>
      <span className="font-manrope text-[14px] font-medium text-oxford">Chicos Ole</span>
      <ChevronDownIcon className="h-3 w-3 text-gray-600" />
    </button>
  </div>

  {/* Centro — búsqueda (solo T1 Envíos) */}
  <div className="flex max-w-[400px] flex-1 mx-8">
    <T1Search placeholder="Número de rastreo" className="w-full" />
  </div>

  {/* Lado derecho */}
  <div className="flex items-center gap-2">
    {/* Saldo (solo T1 Envíos) */}
    <button className="flex items-center gap-1 rounded-[8px] border border-gray-200 px-3 py-1 hover:bg-gray-50">
      <CurrencyDollarIcon className="h-4 w-4 text-oxford" />
      <span className="font-manrope text-[13px] font-medium text-oxford">$9,456.00</span>
      <ChevronRightIcon className="h-3 w-3 text-gray-600" />
    </button>

    {/* Switch de productos */}
    <button className="flex h-8 w-8 items-center justify-center rounded-[8px] hover:bg-gray-50">
      <Squares2X2Icon className="h-4 w-4 text-oxford" />
    </button>

    {/* Ayuda */}
    <button className="flex h-8 w-8 items-center justify-center rounded-[8px] hover:bg-gray-50">
      <QuestionMarkCircleIcon className="h-4 w-4 text-oxford" />
    </button>

    {/* Notificaciones */}
    <button className="relative flex h-8 w-8 items-center justify-center rounded-[8px] hover:bg-gray-50">
      <BellIcon className="h-4 w-4 text-oxford" />
      <span className="absolute right-0.5 top-0.5 flex h-4 w-4 items-center justify-center rounded-full bg-red-500 font-manrope text-[10px] font-semibold text-white">
        4
      </span>
    </button>

    {/* Avatar usuario */}
    <button className="h-8 w-8 overflow-hidden rounded-full">
      <img src={user.avatar} alt={user.name} className="h-full w-full object-cover" />
    </button>
  </div>
</header>
```

---

## 3. Sidebar — estructura común

Todos los sidebars del ecosistema comparten la misma estructura base, variando solo en su contenido de navegación.

### 3.1 Anatomía (expandido)

```
┌─────────────────────────┐
│  [CTA primario]          │  ← button/primary · w-full · solo productos con acción principal
├─────────────────────────┤
│  [ícono] Item nivel 1   │  ← nav item sin hijos
│  [ícono] Sección    ∧   │  ← nav item con hijos expandido
│    Subitem              │  ← nav subitem (indentado)
│    Subitem activo       │  ← nav subitem seleccionado
│  [ícono] Sección    ∨   │  ← nav item colapsado
├─────────────────────────┤
│  [«]                    │  ← toggle de colapso (esquina inferior)
└─────────────────────────┘
```

### 3.2 Tokens de estilo

```css
/* Sidebar */
width: 184px;             /* expandido */
width: 48px;              /* colapsado */
background: white;
border-right: 1px solid var(--color-gray-200);
height: calc(100vh - 48px);
position: fixed;
top: 48px;
left: 0;
overflow-y: auto;
overflow-x: hidden;
transition: width 200ms ease;
padding-top: 12px;
padding-bottom: 24px;
```

### 3.3 Nav item — estados

| Estado | BG | Text/Icon | Descripción |
|---|---|---|---|
| **Default** | `white` | `oxford` | Reposo |
| **Hover** | `gray-50` | `oxford` | Cursor sobre el item |
| **Activo** | `gray-50` | `oxford` | Página actual — subitem resaltado |
| **Activo con hijos** | `white` | `oxford` | Sección expandida — el subitem activo tiene `gray-50` |

### 3.4 Tipografía del sidebar

| Elemento | Font | Size | Weight | Color |
|---|---|---|---|---|
| Item nivel 1 (con ícono) | Manrope | `14px` | Regular (400) | `oxford` |
| Subitem nivel 2 | Manrope | `14px` | Regular (400) | `oxford` |
| Subitem activo | Manrope | `14px` | Regular (400) | `oxford` · BG `gray-50` |
| Label de grupo (T1 Cuenta) | Manrope | `10px` | SemiBold (600) | `gray-600` · uppercase |

### 3.5 Toggle de colapso

- Ícono `«` (chevron doble izquierda) — posición bottom del sidebar
- Click → colapsa a `48px` mostrando solo íconos
- En estado colapsado el ícono cambia a `»` (chevron doble derecha)
- Transición suave `200ms ease`

---

## 4. Sidebar — variantes por producto

### 4.1 T1 Envíos — Expandido

**Figma node:** `232:7298`

CTA primario: `+ Crear envío` · `button/primary` · `w-full` · `border-radius: 10px`

Estructura de navegación:
```
Inicio
Envíos ∧
  Cotizador
  Recolecciones
  Rastreo de guías
  Mis envíos
Mis Pedidos
Clientes
Canales de Venta
Control de calidad ∧
  Incidencias
  Sobrepesos
HUB logístico ∧
  Reglas
  Logs
Reportes
Configuración ∧
  Direcciones guardadas
  Plantillas de paquetes
  Paqueterías
  Zonas
```

### 4.2 T1 Envíos — Colapsado

**Figma node:** `232:7759`

- Solo íconos · sin texto · sin CTA
- CTA se convierte en botón `+` cuadrado `red-500` · `36×36px` · `border-radius: 10px`
- Íconos: `24×24px` · color `oxford`
- Hover: BG `gray-50` en el área del ícono
- Al hacer hover sobre un item → tooltip con el nombre (ver `components/MOLECULES.md`)

### 4.3 T1 Tienda — Expandido

**Figma node:** `232:8205`

Sin CTA primario en el sidebar.

```
Inicio
Mis Pedidos
Mis Productos ∧
  Listado de productos
  Inventario
  Precio
  Catálogos
  Sucursales
Clientes
Canales de Venta
Descuentos
Tienda en línea ∧
  Personalizar diseño
  Enlaces de redes sociales
  Configuración
Reportes
Mis pagos
```

### 4.4 T1 Tienda — Colapsado

**Figma node:** `232:9042`

- Solo íconos · sin texto · sin CTA
- Íconos: `24×24px` · color `oxford`
- Mismo comportamiento de hover y tooltip que T1 Envíos colapsado

### 4.5 T1 Pagos — Expandido

**Figma node:** `232:8112`

Sin CTA primario en el sidebar.

```
Inicio
Transacciones ∧
  Listado de transacciones
  Reclamaciones
Link de pago
Liquidaciones
Pedidos
Métodos de pago
Desarrolladores
```

### 4.6 T1 Pagos — Colapsado

**Figma node:** `232:8014`

Variante visual diferente: los íconos se muestran en **círculos con BG `red-50`** y ícono en `red-500`. Esto diferencia visualmente T1 Pagos del resto cuando está colapsado.

```css
/* Ícono colapsado T1 Pagos */
background: var(--color-red-50);
border-radius: 50%;
width: 36px;
height: 36px;
color: var(--color-red-500);
```

### 4.7 T1 Cuenta — Expandido

**Figma node:** `232:8321`

Sidebar especial — diferente estructura visual. Sin íconos en los items, organizado por grupos con labels de sección en uppercase.

**Sin CTA primario.**

Estructura:
```
MI PERFIL          ← label de grupo · 10px SemiBold · gray-600 · uppercase
  Mi perfil
  Seguridad
  Mis accesos

TIENDA
  [Avatar] Chicos Ole ∨   ← selector de tienda inline

FINANZAS
  Saldos y movimientos
  Facturación
  Métodos de pago

ADMINISTRACIÓN
  Datos de tienda
  Roles y permisos
  Sucursales
  Planes
```

> ⚠️ **T1 Cuenta** no tiene estado colapsado — es una sección de configuración, no un dashboard de trabajo. No implementar toggle de colapso en T1 Cuenta.

---

## 5. Estados del sidebar

### 5.1 Item nivel 1 — con y sin hijos

```tsx
// Item sin hijos
<a
  href={item.href}
  className={`flex h-[36px] items-center gap-2.5 rounded-[8px] px-3 font-manrope text-[14px] text-oxford transition-colors ${
    isActive ? 'bg-gray-50' : 'hover:bg-gray-50'
  }`}
>
  <item.icon className="h-5 w-5 shrink-0 text-oxford" />
  {!collapsed && <span>{item.label}</span>}
</a>

// Item con hijos (expandible)
<button
  onClick={() => toggleSection(item.id)}
  className="flex h-[36px] w-full items-center gap-2.5 rounded-[8px] px-3 font-manrope text-[14px] text-oxford hover:bg-gray-50 transition-colors"
>
  <item.icon className="h-5 w-5 shrink-0 text-oxford" />
  {!collapsed && (
    <>
      <span className="flex-1 text-left">{item.label}</span>
      <ChevronUpIcon className={`h-4 w-4 text-gray-600 transition-transform ${
        !expanded ? 'rotate-180' : ''
      }`} />
    </>
  )}
</button>
```

### 5.2 Subitem nivel 2

```tsx
// Subitem (visible solo cuando la sección está expandida)
{expanded && (
  <div className="ml-7 flex flex-col">
    {item.children.map(child => (
      <a
        key={child.href}
        href={child.href}
        className={`flex h-[34px] items-center rounded-[8px] px-3 font-manrope text-[14px] text-oxford transition-colors ${
          isActive(child.href) ? 'bg-gray-50' : 'hover:bg-gray-50'
        }`}
      >
        {child.label}
      </a>
    ))}
  </div>
)}
```

### 5.3 CTA primario en sidebar

Solo en productos con acción principal frecuente (T1 Envíos → "Crear envío").

```tsx
// Expandido
<T1Button variant="primary" className="mx-3 w-[calc(100%-24px)]">
  + Crear envío
</T1Button>

// Colapsado — solo ícono
<button className="mx-auto flex h-[36px] w-[36px] items-center justify-center rounded-[10px] bg-red-500 text-white hover:bg-red-700">
  <PlusIcon className="h-4 w-4" />
</button>
```

### 5.4 Labels de grupo (T1 Cuenta)

```tsx
<div className="px-3 pb-1 pt-4">
  <p className="font-manrope text-[10px] font-semibold uppercase tracking-wider text-gray-600">
    {group.label}
  </p>
</div>
```

### 5.5 Toggle de colapso

```tsx
<button
  onClick={onToggle}
  className="flex h-[28px] w-full items-center justify-end px-3 font-manrope text-[12px] text-gray-600 hover:text-oxford"
>
  {collapsed
    ? <ChevronDoubleRightIcon className="h-4 w-4" />
    : <ChevronDoubleLeftIcon className="h-4 w-4" />
  }
</button>
```

---

## 6. Nav item — molécula base

El nav item es la unidad mínima del sidebar. Está documentado en `components/MOLECULES.md` — aquí se referencia cómo se ensambla en el organismo.

| Propiedad | Valor |
|---|---|
| Height | `36px` |
| Padding horizontal | `12px` |
| Gap ícono–texto | `10px` |
| Border-radius | `8px` |
| Ícono | `20×20px` · color `oxford` |
| Indentación subitems | `28px` (margen izquierdo) |

---

## 7. Reglas de implementación — Dashboard

- **El sidebar nunca tiene shadow** — solo borde derecho `gray-200`.
- **El header nunca tiene shadow** — solo borde inferior `gray-200`.
- **La transición de colapso** es `200ms ease` en width — el contenido desaparece con `overflow: hidden`.
- **T1 Cuenta no tiene estado colapsado** — no implementar el toggle.
- **T1 Pagos colapsado** usa íconos en círculo `red-50` — diferente a los demás productos que usan ícono directo sobre `white`.
- **Los subitems no tienen ícono** — solo indentación y texto.
- **El item activo** resalta el subitem (si hay subitems), no el item padre — el padre se mantiene expandido pero sin BG propio.
- **Tooltip en colapsado** — al hover sobre un ícono colapsado, mostrar el label del item. Ver `components/MOLECULES.md → Tooltip`.
- **Sin scroll horizontal** en el sidebar — `overflow-x: hidden` siempre.
- **El sidebar es `position: fixed`** — no interfiere con el scroll del contenido.

---

## 8. Header — Landing

**Figma node:** `1:8059` · Archivo: `Landing-T1-versión-lanzamiento` (`LtyvOqWvByid8aObEwNp7K`)

### 8.1 Visual

```
[T1 Tienda logo]    Ecosistema ∨    ¿Qué es T1?    Iniciar sesión →    [Empieza gratis]
```

### 8.2 Anatomía

| Elemento | Descripción |
|---|---|
| **Logo producto** | Imagotipo del producto (ej: T1 Tienda) — izquierda · `126×42px` |
| **Navegación central** | Links: "Ecosistema ∨" (con dropdown) · "¿Qué es T1?" |
| **Iniciar sesión** | Link con chevron `→` — abre flujo de login |
| **CTA primario** | `button/primary` · texto: "Empieza gratis" · `156×45px` |

### 8.3 Tokens de estilo

```css
/* Header landing */
height: 70px;
background: white;          /* o transparente en variantes dark */
padding: 10px 0;
position: sticky;
top: 0;
z-index: 50;

/* Contenedor interior */
max-width: 1018px;
margin: 0 auto;
padding: 0 0;               /* el contenedor maneja el centrado */
```

### 8.4 Tipografía

| Elemento | Font | Size | Weight | Color |
|---|---|---|---|---|
| Links de nav | Sora | `16px` | Regular (400) | `oxford` |
| "Iniciar sesión" | Inter | `16px` | Regular (400) | `oxford` |
| CTA "Empieza gratis" | Inter | `16px` | SemiBold (600) | `white` |

### 8.5 Snippet

```tsx
<header className="sticky top-0 z-50 bg-white">
  <div className="mx-auto flex h-[70px] max-w-[1018px] items-center justify-between px-0">
    {/* Logo */}
    <T1Logo product="tienda" className="h-[42px]" />

    {/* Navegación */}
    <nav className="flex items-center gap-8">
      <button className="flex items-center gap-1 font-sora text-[16px] text-oxford hover:text-black">
        Ecosistema <ChevronDownIcon className="h-3.5 w-3.5" />
      </button>
      <a href="/que-es-t1" className="font-sora text-[16px] text-oxford hover:text-black">
        ¿Qué es T1?
      </a>
    </nav>

    {/* Acciones */}
    <div className="flex items-center gap-3">
      <a href="/login" className="flex items-center gap-1 font-inter text-[16px] text-oxford hover:text-black">
        Iniciar sesión <ChevronRightIcon className="h-2.5 w-2.5" />
      </a>
      <T1Button variant="primary" className="h-[45px] px-6 font-inter text-[16px]">
        Empieza gratis
      </T1Button>
    </div>
  </div>
</header>
```

### 8.6 Reglas

- El header de landing usa **Sora** para los links de navegación — diferente al dashboard que usa Manrope.
- El CTA "Empieza gratis" usa **Inter SemiBold** — mismo que los botones del sistema en landing.
- El logo varía según el producto de la landing: T1 Tienda, T1 Pagos, T1 Envíos.
- Sin borde inferior visible — el header flota sobre el contenido de la landing.
- En mobile → menú hamburguesa que despliega los links en vertical.

---

## 9. Footer — Landing

**Figma node:** `1:8002` · Archivo: `Landing-T1-versión-lanzamiento`

### 9.1 Visual

Footer oscuro de 3 columnas + barra legal inferior.

```
┌─────────────────────────────────────────────────────────────────┐
│  [T1 logo blanco]          Soluciones   T1          Planes      │
│  [Li][In][X][Fb][TikTok]  T1 Tienda     ¿Qué es T1? Precios     │
│                             T1 Pagos     Únete a T1  Enterprise  │
│                             T1 Envíos    Historias                │
│                             T1 Score     Contacto                 │
├─────────────────────────────────────────────────────────────────┤
│  🇲🇽 México (Español) ∨    Términos | Privacidad  © 2025 T1.   │
└─────────────────────────────────────────────────────────────────┘
```

### 9.2 Tokens de estilo

```css
/* Footer */
background: #000000;         /* Negro — color/brand/base/black */
color: #FFFFFF;              /* Blanco */
padding-top: 80px;
padding-bottom: 32px;

/* Contenedor interior */
max-width: 1016px;
margin: 0 auto;
```

### 9.3 Columnas de navegación

| Columna | Encabezado | Links |
|---|---|---|
| **1** | Soluciones | T1 Tienda · T1 Pagos · T1 Envíos · T1 Score |
| **2** | T1 | ¿Qué es T1? · Únete a T1 · Historias e éxito · Contacto |
| **3** | Planes | Precios · Enterprise |

### 9.4 Tipografía del footer

| Elemento | Font | Size | Weight | Color |
|---|---|---|---|---|
| Encabezado de columna | Inter | `16px` | SemiBold (600) | `white` |
| Links de nav | Inter | `14px` | Regular (400) | `gray-600` (`#9CA3AF`) |
| Links hover | Inter | `14px` | Regular (400) | `white` |
| Links legales | Inter | `12px` | Regular (400) | `gray-600` |
| Copyright | Inter | `12px` | Regular (400) | `gray-600` |

### 9.5 Redes sociales

Íconos de `24×24px` en blanco. Orden: LinkedIn · Instagram · X (Twitter) · Facebook · TikTok.

### 9.6 Barra legal

Tres elementos en fila justificados:
- **Izquierda:** Selector de idioma `🇲🇽 México (Español) ∨`
- **Centro:** `Términos y condiciones | Privacidad`
- **Derecha:** `© 2025 T1. Todos los derechos reservados.`

### 9.7 Snippet

```tsx
<footer className="bg-black text-white">
  {/* Columnas */}
  <div className="mx-auto max-w-[1016px] px-0 pb-16 pt-20">
    <div className="grid grid-cols-4 gap-8">
      {/* Logo + redes */}
      <div className="flex flex-col gap-8">
        <T1Logo product="t1" variant="white" className="h-8" />
        <div className="flex items-center gap-6">
          {socialLinks.map(social => (
            <a key={social.id} href={social.href} className="text-white hover:opacity-70">
              <social.icon className="h-6 w-6" />
            </a>
          ))}
        </div>
      </div>

      {/* Soluciones */}
      <div className="flex flex-col gap-4">
        <p className="font-inter text-[16px] font-semibold text-white">Soluciones</p>
        {['T1 Tienda', 'T1 Pagos', 'T1 Envíos', 'T1 Score'].map(item => (
          <a key={item} href={`/${item.toLowerCase()}`}
            className="font-inter text-[14px] text-gray-600 hover:text-white transition-colors">
            {item}
          </a>
        ))}
      </div>

      {/* T1 */}
      <div className="flex flex-col gap-4">
        <p className="font-inter text-[16px] font-semibold text-white">T1</p>
        {['¿Qué es T1?', 'Únete a T1', 'Historias e éxito', 'Contacto'].map(item => (
          <a key={item} href="#"
            className="font-inter text-[14px] text-gray-600 hover:text-white transition-colors">
            {item}
          </a>
        ))}
      </div>

      {/* Planes */}
      <div className="flex flex-col gap-4">
        <p className="font-inter text-[16px] font-semibold text-white">Planes</p>
        {['Precios', 'Enterprise'].map(item => (
          <a key={item} href="#"
            className="font-inter text-[14px] text-gray-600 hover:text-white transition-colors">
            {item}
          </a>
        ))}
      </div>
    </div>
  </div>

  {/* Barra legal */}
  <div className="mx-auto max-w-[1016px] border-t border-white/10 px-0 py-8">
    <div className="flex items-center justify-between">
      <button className="flex items-center gap-1 font-inter text-[12px] text-gray-600 hover:text-white">
        🇲🇽 México (Español) <ChevronDownIcon className="h-3 w-3" />
      </button>
      <div className="flex items-center gap-2 font-inter text-[12px] text-gray-600">
        <a href="/terminos" className="hover:text-white">Términos y condiciones</a>
        <span>|</span>
        <a href="/privacidad" className="hover:text-white">Privacidad</a>
      </div>
      <p className="font-inter text-[12px] text-gray-600">
        © 2025 T1. Todos los derechos reservados.
      </p>
    </div>
  </div>
</footer>
```

### 9.8 Reglas

- El footer **siempre es negro** — nunca gris oscuro ni variantes.
- Los links usan `gray-600` (`#9CA3AF`) en reposo → `white` en hover.
- El logo T1 en el footer es la versión **white** del logotipo (sin el color rojo del imagotipo).
- El separador de la barra legal usa `border-white/10` — borde sutil sobre fondo negro.
- En mobile el grid de columnas colapsa a 2 columnas, luego a 1 columna en pantallas muy pequeñas.

---

---

## 10. Header mobile — Dashboard

**Figma node:** `2:5161` · Archivo: `Tablas - taxonomia`

El header mobile del dashboard es una barra superior delgada sobre fondo `red-500` (status bar del OS) seguida del header propiamente dicho en `white`.

### 10.1 Anatomía

```
┌─────────────────────────────────────────────┐
│  ≡   [switch ⊞]  [Avatar tienda ∨]  [Foto] │
└─────────────────────────────────────────────┘
```

| Elemento | Descripción |
|---|---|
| **Hamburger `≡`** | Abre el sidebar como drawer desde la izquierda |
| **Switch de productos `⊞`** | Ícono `16×16px` — abre selector de productos del ecosistema |
| **Avatar + chevron** | Avatar circular de la tienda activa (`24×24px`) + chevron `∨` para cambiar tienda |
| **Foto de perfil** | Avatar circular del usuario (`32×32px`) — abre submenu de cuenta |

### 10.2 Tokens de estilo

```css
/* Header mobile */
height: 55px;
background: white;
border-bottom: none;      /* sin borde en mobile */
padding: 0 13px;

/* Status bar del OS — sobre el header */
height: 32px;
background: red-500;      /* #DB3B2B */
```

### 10.3 Diferencias vs header desktop

| Elemento | Desktop | Mobile |
|---|---|---|
| Logo producto | ✅ visible | ❌ oculto |
| Hamburger | ✅ toggle sidebar | ✅ abre drawer |
| Selector de tienda | Texto + avatar | Solo avatar + chevron |
| Búsqueda | Input visible | Ícono de lupa (expande al tap) |
| Saldo | ✅ visible | ❌ oculto |
| Notificaciones | ✅ ícono visible | ❌ oculto |
| Ayuda | ✅ ícono visible | ❌ oculto |

### 10.4 Snippet

```tsx
<header className="bg-white">
  {/* Status bar del OS */}
  <div className="h-[32px] bg-red-500" />

  {/* Header */}
  <div className="flex h-[55px] items-center justify-between px-[13px]">
    {/* Hamburger */}
    <button className="flex h-10 w-10 items-center justify-center">
      <Bars3Icon className="h-6 w-6 text-oxford" />
    </button>

    {/* Lado derecho */}
    <div className="flex items-center gap-2">
      {/* Switch de productos */}
      <button className="flex h-8 w-8 items-center justify-center">
        <Squares2X2Icon className="h-4 w-4 text-oxford" />
      </button>

      {/* Avatar tienda + chevron */}
      <button className="flex items-center gap-1">
        <div className="h-6 w-6 overflow-hidden rounded-full">
          <img src={store.avatar} alt={store.name} className="h-full w-full object-cover" />
        </div>
        <ChevronDownIcon className="h-3 w-3 text-oxford" />
      </button>

      {/* Avatar usuario */}
      <button className="h-8 w-8 overflow-hidden rounded-full">
        <img src={user.avatar} alt={user.name} className="h-full w-full object-cover" />
      </button>
    </div>
  </div>
</header>
```

---

## 11. Page Header — Mobile

El page header mobile es el área que aparece debajo del header principal, dentro del contenido de la página. Tiene dos variantes.

### 11.1 Variante A — Título + CTA

Usada en listados principales (Mis pedidos, Mis productos, etc.).

```
┌──────────────────────────────────────────────┐
│  Mis pedidos              [Crear pedido]      │
│  Todos los canales ∨                         │
├──────────────────────────────────────────────┤
│  [Buscar_____________] [🔍]     [···]         │
├──────────────────────────────────────────────┤
│  [Filtrar ⌃⌄]  [Nombre ∨]  [↑↓]             │
└──────────────────────────────────────────────┘
```

**Especificaciones:**
- Título: Manrope Bold 20px · `oxford`
- Subtítulo/filtro activo: Manrope Regular 14px · `oxford` + chevron `∨`
- CTA: `button/primary` · `h-[35px]`
- Búsqueda: input `w-[278px]` + botón meatballs `35×35px` a la derecha
- Filtros: pills de `30px` alto — mismos que desktop

### 11.2 Variante B — Flecha atrás + Título (navegación anidada)

Usada en vistas de detalle, flows de creación multi-paso y sub-secciones. Visible en el flujo "Crear envío" de T1 Envíos.

**Figma node:** `76:80387` · Archivo: `T1envios - Crear envio`

```
┌──────────────────────────────────────────────┐
│  ← Detalles de tu paquete                    │
│  Paso 2 de 3                                 │
└──────────────────────────────────────────────┘
```

**Especificaciones:**
- Flecha `←` izquierda `24×24px` · color `oxford` · tap regresa a la vista anterior
- Título: Manrope SemiBold 20px · `oxford`
- Subtítulo de progreso (opcional): Manrope Regular 12px · `gray-600` — ej: "Paso 2 de 3"
- Sin CTA en el header — el botón de avance va al fondo de la pantalla ("Siguiente")
- BG: `white` · sin borde

### 11.3 Snippet Variante B

```tsx
<div className="px-4 py-3">
  <div className="flex items-center gap-3">
    <button
      onClick={onBack}
      className="flex h-8 w-8 items-center justify-center"
    >
      <ArrowLeftIcon className="h-5 w-5 text-oxford" />
    </button>
    <div>
      <h1 className="font-manrope text-[20px] font-semibold text-oxford">
        {title}
      </h1>
      {stepLabel && (
        <p className="font-manrope text-[12px] text-gray-600">{stepLabel}</p>
      )}
    </div>
  </div>
</div>
```

### 11.3 Snippet Variante A

```tsx
<div className="px-4 py-3">
  {/* Título + CTA */}
  <div className="mb-1 flex items-center justify-between">
    <h1 className="font-manrope text-[20px] font-bold text-oxford">Mis pedidos</h1>
    <T1Button variant="primary" className="h-[35px] text-[13px]">
      Crear pedido
    </T1Button>
  </div>

  {/* Filtro activo / subtítulo */}
  <button className="mb-3 flex items-center gap-1 font-manrope text-[14px] text-oxford">
    Todos los canales <ChevronDownIcon className="h-3 w-3" />
  </button>

  {/* Búsqueda + meatballs */}
  <div className="mb-3 flex items-center gap-2">
    <T1Search placeholder="Buscar..." className="flex-1 h-[40px]" />
    <button className="flex h-[35px] w-[35px] items-center justify-center rounded-[10px] border border-gray-200 bg-white">
      <EllipsisHorizontalIcon className="h-4 w-4 text-oxford" />
    </button>
  </div>

  {/* Filtros — mismos tokens que desktop, h-[30px] */}
  <div className="flex items-center gap-2 overflow-x-auto pb-1">
    <button className="flex h-[30px] shrink-0 items-center gap-1 rounded-[10px] border border-gray-200 bg-white px-3 font-manrope text-[12px] font-medium text-oxford">
      Filtrar <AdjustmentsHorizontalIcon className="h-3.5 w-3.5" />
    </button>
    <button className="flex h-[30px] shrink-0 items-center gap-1 rounded-[10px] border border-gray-200 bg-white px-3 font-manrope text-[12px] font-medium text-oxford">
      Nombre <ChevronDownIcon className="h-3 w-3" />
    </button>
    <button className="flex h-[30px] w-[30px] shrink-0 items-center justify-center rounded-[10px] border border-gray-200 bg-white">
      <ChevronUpDownIcon className="h-3.5 w-3.5 text-oxford" />
    </button>
  </div>
</div>
```

---

## 10. Wizard — Flujo multi-paso

**Archivo:** `T1envios - Crear envio` (`emoT2euO10CyyOQPnuLAbJ`)  
**Figma nodes:** `2:4211` (Step 1) · `8:41155` (Step 2) · `18:38862` (Step 3) · `76:80387` (Step 2 mobile con IA)  
**Contexto:** Dashboard · Mobile-first (existe versión desktop y mobile)

El Wizard es el organismo que estructura flujos de creación que requieren múltiples pasos secuenciales. El caso canónico es "Crear envío" en T1 Envíos, pero el patrón aplica a cualquier flujo guiado del ecosistema.

### 10.1 Anatomía

```
┌─────────────────────────────┐
│  Bar top (header mobile)     │
├─────────────────────────────┤
│  ← Título del paso           │
│  Paso N de M                 │
├─────────────────────────────┤
│  Sección A                   │
│  ─────────────────────────   │
│  Sección B                   │
├─────────────────────────────┤
│  Ver resumen de envío  ∧/∨   │
│  [      Siguiente      ]     │
└─────────────────────────────┘
```

### 10.2 Estructura de pasos — Crear envío

**Paso 1 de 3 — Dirección**
- Dirección de origen: selector de dirección guardada o formulario nuevo
- Dirección de destino: selector o formulario nuevo

**Paso 2 de 3 — Detalles del paquete**
- Dimensiones: Nombre de plantilla + Largo/Alto/Ancho/Peso (inputs con subfix `cm`/`kg`)
- Resumen de pesos: Peso físico · Peso volumétrico · Peso a cotizar (read only)
- Checkbox: "Guardar como plantilla para futuros envíos"
- Detalle del envío: Cantidad · Descripción del contenido · Tipo de producto SAT (con sugerencia IA) · Checkbox seguro de envío

**Paso 3 de 3 — Cotización**
- Lista de carriers con precio (ver `components/TABLES.md → 8.7`)
- Badge "RECOMENDADA" en la opción sugerida
- Selección de carrier activa el CTA "Crear envío"

### 10.3 Tokens de estilo

```css
background: white;
min-height: 100vh;

/* Header del paso */
border-bottom: 1px solid var(--color-gray-200);
padding: 12px 16px;

/* Separadores de sección */
border-top: 1px solid var(--color-gray-200);
padding: 16px;

/* Bottom bar — sticky */
position: sticky;
bottom: 0;
background: white;
border-top: 1px solid var(--color-gray-200);
padding: 10px 15px 24px;
```

### 10.4 Snippet

```tsx
export default function WizardLayout({ steps, currentStep, children }) {
  const [summaryOpen, setSummaryOpen] = useState(false)

  return (
    <div className="flex min-h-screen flex-col bg-white">
      <T1BarTop />

      {/* Header del paso */}
      <div className="border-b border-gray-200 px-4 py-3">
        <div className="flex items-center gap-2">
          <button onClick={goBack}>
            <ArrowLeftIcon className="h-6 w-6 text-oxford" />
          </button>
          <h1 className="font-manrope text-[20px] font-semibold text-oxford">
            {steps[currentStep].title}
          </h1>
        </div>
        <p className="mt-1 pl-8 font-manrope text-[12px] text-gray-600">
          Paso {currentStep + 1} de {steps.length}
        </p>
      </div>

      {/* Contenido scrollable */}
      <div className="flex-1 overflow-y-auto">{children}</div>

      {/* Bottom bar sticky */}
      <div className="sticky bottom-0 border-t border-gray-200 bg-white px-4 pb-6 pt-2">
        <button
          onClick={() => setSummaryOpen(!summaryOpen)}
          className="flex w-full items-center justify-between py-2 font-manrope text-[14px] text-oxford"
        >
          Ver resumen de envío
          <ChevronUpIcon className={`h-4 w-4 transition-transform ${!summaryOpen ? 'rotate-180' : ''}`} />
        </button>
        {summaryOpen && <T1ShippingSummary />}
        <T1Button variant="primary" className="mt-2 w-full" disabled={!isStepComplete}>
          {currentStep < steps.length - 1 ? 'Siguiente' : 'Crear envío'}
        </T1Button>
      </div>
    </div>
  )
}
```

### 10.5 Sugerencia IA inline

El campo "Tipo de producto - SAT" muestra una etiqueta cuando el valor fue seleccionado por IA:

```tsx
<div className="flex items-center justify-between">
  <label className="font-manrope text-[14px] font-medium text-oxford">
    Tipo de producto - SAT
  </label>
  <span className="flex items-center gap-1 font-manrope text-[12px] text-purple-500">
    Seleccionado con IA <SparklesIcon className="h-3 w-3" />
  </span>
</div>
```

### 10.6 Desktop vs Mobile

| Elemento | Mobile | Desktop |
|---|---|---|
| Layout | Full width · scroll vertical | Sidebar izquierdo + panel derecho |
| Header | Bar top + título con back | Header dashboard estándar |
| Progreso | "Paso N de M" textual | Steps visuales horizontales |
| Resumen | Panel colapsable en bottom bar | Panel fijo lateral derecho |
| CTA | Sticky bottom · w-full | Posición fija en panel |

### 10.7 Reglas

- **El CTA siempre es sticky** al fondo — nunca se pierde en el scroll.
- **El resumen es colapsable** — no ocupa espacio por defecto.
- **Navegación lineal** — solo se puede ir al paso anterior, no saltar.
- **Validación progresiva** — CTA deshabilitado (`red-200`) hasta completar campos requeridos del paso.
- **Sugerencias IA** se marcan con label "Seleccionado con IA" + ícono sparkles en `purple-500`.

---

---

## 12. Header mobile — Landing

**Figma node:** `16:20783` · Archivo: `Landing-T1-versión-lanzamiento`

### 12.1 Visual

```
[T1 logo]                                    [≡]
```

Extremadamente minimalista — solo logo y hamburger. Sin navegación visible, sin CTA.

### 12.2 Especificaciones

| Elemento | Valor |
|---|---|
| Height | `51px` |
| BG | `white` (o transparente sobre hero) |
| Logo | Imagotipo T1 · `105×35px` · izquierda · `margin-left: 16px` |
| Hamburger `≡` | `24×24px` · derecha · `margin-right: 16px` · color `oxford` |

### 12.3 Comportamiento del hamburger

Al tap → abre drawer desde la derecha (o menú overlay) con los links de navegación completos:
- Ecosistema
- ¿Qué es T1?
- Iniciar sesión →
- CTA "Empieza gratis" · `button/primary` · `w-full`

### 12.4 Snippet

```tsx
<header className="sticky top-0 z-50 bg-white">
  <div className="flex h-[51px] items-center justify-between px-4">
    {/* Logo */}
    <T1Logo product="t1" className="h-[35px]" />

    {/* Hamburger */}
    <button
      onClick={() => setMenuOpen(true)}
      className="flex h-10 w-10 items-center justify-center"
    >
      <Bars3Icon className="h-6 w-6 text-oxford" />
    </button>
  </div>

  {/* Drawer de navegación */}
  {menuOpen && (
    <div className="fixed inset-0 z-50 bg-white">
      <div className="flex h-[51px] items-center justify-between px-4">
        <T1Logo product="t1" className="h-[35px]" />
        <button onClick={() => setMenuOpen(false)}>
          <XMarkIcon className="h-6 w-6 text-oxford" />
        </button>
      </div>
      <nav className="flex flex-col gap-6 px-6 pt-8">
        <button className="flex items-center gap-1 font-sora text-[18px] text-oxford">
          Ecosistema <ChevronDownIcon className="h-4 w-4" />
        </button>
        <a href="/que-es-t1" className="font-sora text-[18px] text-oxford">¿Qué es T1?</a>
        <a href="/login" className="flex items-center gap-1 font-inter text-[18px] text-oxford">
          Iniciar sesión <ChevronRightIcon className="h-3 w-3" />
        </a>
        <T1Button variant="primary" className="mt-4 w-full h-[48px]">
          Empieza gratis
        </T1Button>
      </nav>
    </div>
  )}
</header>
```

---

## 13. Footer mobile — Landing

**Figma node:** `16:20730` · Archivo: `Landing-T1-versión-lanzamiento`

### 13.1 Visual

El footer mobile apila las columnas verticalmente en lugar del grid horizontal de desktop.

```
┌─────────────────────────────────┐
│  T1 (logo)                      │
│  [Li][In][X][Fb][TikTok]        │
│                                  │
│  Soluciones                      │
│  T1 Tienda                        │
│  T1 Pagos                         │
│  T1 Envíos                        │
│  T1 Score                         │
│                                  │
│  T1                              │
│  ¿Qué es T1?                     │
│  Únete a T1                      │
│  Historias e éxito               │
│  Contacto                        │
│                                  │
│  🇲🇽 México (Español) ∨          │
│  Términos y condiciones           │
│  Privacidad                      │
│  © 2025 T1. Todos los derechos   │
└─────────────────────────────────┘
```

### 13.2 Diferencias vs footer desktop

| Elemento | Desktop | Mobile |
|---|---|---|
| Layout columnas | Grid 4 columnas | Apilado vertical |
| Columna "Planes" | ✅ visible | ❌ oculta |
| Links legales | Una fila horizontal | Apilados en vertical |
| Copyright | Misma fila que legales | Línea separada debajo |
| Padding | `px-0` (contenedor centrado) | `px-[20px]` |

### 13.3 Tokens de estilo

Idénticos al footer desktop — `bg-black`, texto `white`, links `gray-600` → hover `white`. Ver sección 9 de este archivo.

### 13.4 Snippet

```tsx
<footer className="bg-black text-white px-5">
  {/* Logo + redes */}
  <div className="pt-12 pb-8">
    <T1Logo product="t1" variant="white" className="mb-8 h-8" />
    <div className="flex items-center gap-6">
      {socialLinks.map(social => (
        <a key={social.id} href={social.href} className="text-white hover:opacity-70">
          <social.icon className="h-6 w-6" />
        </a>
      ))}
    </div>
  </div>

  {/* Soluciones */}
  <div className="border-t border-white/10 py-8">
    <p className="mb-4 font-inter text-[16px] font-semibold text-white">Soluciones</p>
    <div className="flex flex-col gap-3">
      {['T1 Tienda', 'T1 Pagos', 'T1 Envíos', 'T1 Score'].map(item => (
        <a key={item} href="#"
          className="font-inter text-[14px] text-gray-600 hover:text-white">
          {item}
        </a>
      ))}
    </div>
  </div>

  {/* T1 */}
  <div className="border-t border-white/10 py-8">
    <p className="mb-4 font-inter text-[16px] font-semibold text-white">T1</p>
    <div className="flex flex-col gap-3">
      {['¿Qué es T1?', 'Únete a T1', 'Historias e éxito', 'Contacto'].map(item => (
        <a key={item} href="#"
          className="font-inter text-[14px] text-gray-600 hover:text-white">
          {item}
        </a>
      ))}
    </div>
  </div>

  {/* Barra legal — apilada en mobile */}
  <div className="border-t border-white/10 py-8 flex flex-col gap-3">
    <button className="flex items-center gap-1 font-inter text-[12px] text-gray-600 hover:text-white w-fit">
      🇲🇽 México (Español) <ChevronDownIcon className="h-3 w-3" />
    </button>
    <a href="/terminos" className="font-inter text-[12px] text-gray-600 hover:text-white">
      Términos y condiciones
    </a>
    <a href="/privacidad" className="font-inter text-[12px] text-gray-600 hover:text-white">
      Privacidad
    </a>
    <p className="font-inter text-[12px] text-gray-600">
      © 2025 T1. Todos los derechos reservados.
    </p>
  </div>
</footer>
```



---

## 14. Dropdowns del header — Dashboard

**Figma node:** `1585:1827` · Archivo: `Menu` (`6Bhx11Vjje6OCVEbwrxEcF`)

El header del dashboard tiene 3 dropdowns. Todos comparten el mismo contenedor base.

```css
/* Base de todos los dropdowns */
background: white;
border-radius: 10px;
border: 1px solid var(--color-gray-200);
box-shadow: 0 0 5px 1px rgba(0, 0, 0, 0.1);
position: absolute;
z-index: 100;
```

### 14.1 Dropdown de Perfil de usuario

**Figma node:** `1469:1584` (versión actual) · Abre al click en avatar (esquina derecha del header)

**2 variantes de avatar:** con foto · con iniciales sobre `red-500`

```
┌──────────────────────────────┐
│ [AR]  Alonso Ruiz            │
│       aruiz@correo.com       │
├──────────────────────────────┤
│ Mi perfil                    │
├──────────────────────────────┤
│ Saldos y movimientos         │
│ Facturación                  │
│ Métodos de pago              │
│ Roles y permisos             │
├──────────────────────────────┤
│ Cerrar sesión                │
└──────────────────────────────┘
```

| Elemento | Especificación |
|---|---|
| Ancho | `~224px` |
| Avatar | `40×40px` · circular · iniciales o foto |
| Nombre | Manrope SemiBold 14px · `oxford` |
| Email | Manrope Regular 12px · `gray-600` |
| Links | Manrope Regular 14px · `oxford` · hover `gray-50` |
| Separadores | `gray-200` · `1px` — 3 grupos |

**Grupos de links:**
1. **Perfil:** Mi perfil
2. **Finanzas/Admin:** Saldos y movimientos · Facturación · Métodos de pago · Roles y permisos
3. **Sesión:** Cerrar sesión

> Los links del grupo 2 varían por producto — pueden aparecer más o menos opciones según el contexto.

```tsx
{profileOpen && (
  <div className="absolute right-0 top-[48px] z-50 w-[224px] rounded-[10px] border border-gray-200 bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
    {/* Cabecera */}
    <div className="flex items-center gap-3 p-4">
      <div className="h-[40px] w-[40px] shrink-0 overflow-hidden rounded-full">
        {user.avatar
          ? <img src={user.avatar} className="h-full w-full object-cover" />
          : <div className="flex h-full w-full items-center justify-center bg-red-500 font-manrope text-[14px] font-semibold text-white">{user.initials}</div>
        }
      </div>
      <div>
        <p className="font-manrope text-[14px] font-semibold text-oxford">{user.name}</p>
        <p className="font-manrope text-[12px] text-gray-600">{user.email}</p>
      </div>
    </div>
    {/* Grupo 1 — Perfil */}
    <div className="border-t border-gray-200 p-1">
      <a href="/perfil" className="block rounded-[8px] px-3 py-2 font-manrope text-[14px] text-oxford hover:bg-gray-50">Mi perfil</a>
    </div>
    {/* Grupo 2 — Finanzas y admin */}
    <div className="border-t border-gray-200 p-1">
      {[
        { label: 'Saldos y movimientos', href: '/saldos' },
        { label: 'Facturación', href: '/facturacion' },
        { label: 'Métodos de pago', href: '/metodos-pago' },
        { label: 'Roles y permisos', href: '/roles' },
      ].map(link => (
        <a key={link.href} href={link.href}
          className="block rounded-[8px] px-3 py-2 font-manrope text-[14px] text-oxford hover:bg-gray-50">
          {link.label}
        </a>
      ))}
    </div>
    {/* Grupo 3 — Sesión */}
    <div className="border-t border-gray-200 p-1">
      <button onClick={logout}
        className="block w-full rounded-[8px] px-3 py-2 text-left font-manrope text-[14px] text-oxford hover:bg-gray-50">
        Cerrar sesión
      </button>
    </div>
  </div>
)}
```

### 14.2 Dropdown de Ecosistema

**Figma node:** `1430:10195` · Abre al click en ícono `⊞` del header

```
┌─────────────────────────────────┐
│         Ecosistema  T1          │
├─────────────────────────────────┤
│  [🏪]        [✈]        [💰]   │
│  Tienda     Envíos      Pagos   │
└─────────────────────────────────┘
```

| Elemento | Especificación |
|---|---|
| Ancho | `320px` |
| Header | "Ecosistema" + logotipo T1 · centrado |
| Grid | 3 columnas · `95×105px` por producto |
| Ícono producto | `32×32px` |
| Label | Manrope Regular 12px · `oxford` |
| Hover | BG `gray-50` · `border-radius: 8px` |
| Productos | Tienda · Envíos · Pagos |

```tsx
{ecosystemOpen && (
  <div className="absolute right-8 top-[48px] z-50 w-[320px] rounded-[10px] border border-gray-200 bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
    <div className="flex items-center justify-center gap-2 py-3">
      <span className="font-manrope text-[16px] text-oxford">Ecosistema</span>
      <T1Logo product="t1" className="h-6" />
    </div>
    <div className="border-t border-gray-200" />
    <div className="grid grid-cols-3 gap-1 p-2">
      {products.map(product => (
        <a key={product.id} href={product.url}
          className="flex flex-col items-center gap-2 rounded-[8px] px-3 py-4 hover:bg-gray-50">
          <product.icon className="h-8 w-8" />
          <span className="font-manrope text-[12px] text-oxford">{product.label}</span>
        </a>
      ))}
    </div>
  </div>
)}
```

### 14.3 Dropdown de Tiendas

**Figma node:** `1430:10241` · Abre al click en el selector de tienda del header

```
┌──────────────────────────┐
│  Mis tiendas             │
│  [🔍 Búsqueda...]        │
├──────────────────────────┤
│  [Nt] Chicos Ole    ✓   │  ← Tienda activa + check green-500
│  [Nt] Chicos Ole         │
│  ... (scroll si >7)      │
├──────────────────────────┤
│  + Nueva tienda          │
└──────────────────────────┘
```

| Elemento | Especificación |
|---|---|
| Ancho | `255px` |
| Header | "Mis tiendas" · Manrope Regular 14px · `oxford` |
| Búsqueda | Input `232px` · `h-[35px]` · ícono lupa |
| Items | `40px` alto · avatar `22×22px` + nombre + check activo |
| Check activo | `green-500` |
| Scroll | Si hay más de 7 tiendas |
| Link inferior | "+ Nueva tienda" · Manrope Regular 12px · `oxford` |

```tsx
{storeOpen && (
  <div className="absolute left-0 top-[48px] z-50 w-[255px] rounded-[10px] border border-gray-200 bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]">
    <div className="px-3 pt-3 pb-2">
      <p className="font-manrope text-[14px] text-oxford">Mis tiendas</p>
    </div>
    <div className="px-3 pb-2">
      <T1Search placeholder="" className="h-[35px] w-full" />
    </div>
    <div className="max-h-[280px] overflow-y-auto">
      {stores.map(store => (
        <button key={store.id} onClick={() => switchStore(store)}
          className="flex h-[40px] w-full items-center gap-2 px-3 hover:bg-gray-50">
          <div className="flex h-[22px] w-[22px] items-center justify-center rounded-[6px] font-manrope text-[11px] font-semibold text-white"
            style={{ backgroundColor: store.color }}>
            {store.initials}
          </div>
          <span className="flex-1 text-left font-manrope text-[14px] text-oxford">{store.name}</span>
          {store.active && <CheckIcon className="h-4 w-4 text-green-500" />}
        </button>
      ))}
    </div>
    <div className="border-t border-gray-200 px-3 py-2">
      <button className="font-manrope text-[12px] text-oxford hover:underline">+ Nueva tienda</button>
    </div>
  </div>
)}
```

---

## 15. Sidebar colapsado — Panel flotante de subitems

**Figma node:** `1430:10107` · Archivo: `Menu`

Cuando el sidebar está colapsado (`48px`), los ítems con subitems muestran un **panel flotante** al hacer hover — no un tooltip simple.

### 15.1 Comportamiento

- **Ítem sin hijos** → tooltip simple con el nombre del ítem (ver `MOLECULES.md → Tooltip`)
- **Ítem con hijos** → panel flotante con label del padre + lista de subitems

```
Sidebar colapsado + hover en ítem con hijos:

┌────┐  ┌──────────────────┐
│ 📦 │  │ Pedidos          │  ← label padre · gray-600 · no clickeable
│    │  ├──────────────────┤
└────┘  │ Listado de ped.  │  ← subitem activo · BG gray-50
        │ Cotizador        │  ← subitem
        └──────────────────┘
```

### 15.2 Especificaciones

| Elemento | Valor |
|---|---|
| Posición | `left: 48px` · `top` alineado al ítem |
| Ancho | `167px` |
| BG | `white` · `border-radius: 10px` · `shadow_card` |
| Label padre | Manrope Regular 12px · `gray-600` · no clickeable |
| Subitems | Manrope Regular 14px · `oxford` · hover `gray-50` |
| Subitem activo | BG `gray-50` |

### 15.3 Snippet

```tsx
{collapsed && hoveredItem?.children && (
  <div
    className="fixed z-50 w-[167px] rounded-[10px] border border-gray-200 bg-white shadow-[0_0_5px_1px_rgba(0,0,0,0.1)]"
    style={{ top: itemTop, left: 48 }}
  >
    {/* Label padre — no clickeable */}
    <p className="px-3 py-2 font-manrope text-[12px] text-gray-600">
      {hoveredItem.label}
    </p>
    {/* Subitems */}
    <div className="pb-1">
      {hoveredItem.children.map(child => (
        <a key={child.href} href={child.href}
          className={`block mx-1 rounded-[8px] px-3 py-2 font-manrope text-[14px] text-oxford hover:bg-gray-50 ${
            isActive(child.href) ? 'bg-gray-50' : ''
          }`}>
          {child.label}
        </a>
      ))}
    </div>
  </div>
)}
```



## Referencias cruzadas

| Archivo | Relación |
|---|---|
| `components/ATOMS.md` | Buttons (CTA sidebar y landing), íconos, avatares |
| `components/MOLECULES.md` | Tooltip (sidebar colapsado), Submenu de acciones |
| `components/STATES.md` | Estados del nav item (default, hover, activo) |
| `foundation/COLORS.md` | `oxford`, `gray-50`, `gray-200`, `red-500` |
| `foundation/TYPOGRAPHY.md` | Sora (landing nav), Inter (landing body/footer), Manrope (dashboard) |
| `platforms/DASHBOARD.md` | Tokens específicos del contexto admin |
| `platforms/LANDING.md` | Tokens específicos de landing — contenedor 1018px, tipografía Sora+Inter |
| `assets/BRAND-ASSETS.md` | Logotipos de cada producto y variante white para footer |
