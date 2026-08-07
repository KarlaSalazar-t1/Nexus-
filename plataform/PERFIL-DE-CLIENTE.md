# PERFIL-DE-CLIENTE.md — Contexto de plataforma: Perfil de cliente

> Este archivo documenta los tokens, reglas y componentes exclusivos del **perfil de cliente** del ecosistema T1 — la experiencia que ve el **comprador final**, no el comerciante.
> Cubre el perfil de cliente: inicio, historial de pedidos, detalle de pedido, métodos de pago, direcciones de envío y datos de facturación.
> **No aplica** en landing pages públicas ni en el admin/backoffice del comerciante.
> Para los contextos opuestos, ver [`platforms/LANDING.md`](./LANDING.md) y [`platforms/DASHBOARD.md`](./DASHBOARD.md).

**Última actualización:** Jun 2026 (historial `2341:19451` · estatus `2350:19452` · Inicio/Home `593`/`633` · métodos de pago `1979:19440` · direcciones `1979:19441` · configuraciones `1979:19442`) · **Fuente de verdad:** Figma (`Perfil-de-cliente` · `tviQYwF8Odft6l5FZEP6rm`) · **Owner:** Karla Salazar, Head of UX/UI

---

## ¿Qué es el perfil de cliente?

El **perfil de cliente** es la cuenta del comprador final en T1 Tienda: el lado público donde una persona da seguimiento a sus pedidos y administra sus métodos de pago, direcciones y datos de facturación. Es un tercer contexto de plataforma, distinto de los otros dos:

| Contexto | Usuario | Propósito |
|---|---|---|
| **Landing** | Visitante / prospecto | Convencer a un comerciante de usar T1 |
| **Dashboard** | Negocio | Operar el negocio (vender, enviar, cobrar) |
| **Perfil de cliente** | Comprador final | Comprar y dar seguimiento a sus pedidos |

> Este archivo documenta el **perfil de cliente**: las pantallas de cuenta del comprador. El escaparate de venta y el checkout se documentan en [`patterns/FLOWS.md`](../patterns/FLOWS.md) §4.

---

## Relación con Dashboard

El perfil de cliente **comparte la base visual del Dashboard**, no la de Landing. Usa los mismos tokens de fundación: Manrope como única familia tipográfica, Red 500 (`#DB3B2B`) como primario, la misma paleta semántica y los mismos radios. La diferencia no está en los tokens sino en el **layout, la densidad y el tono**.

| Propiedad | Perfil de cliente | Dashboard |
|---|---|---|
| Tipografía | Manrope (única familia) | Manrope (única familia) |
| Color primario | `#DB3B2B` (Red 500) | `#DB3B2B` (Red 500) |
| Border radius cards | `10px` | `10px`–`20px` |
| Border radius botones | `10px` | `8px`–`10px` |
| Contenedor de contenido | `~672px` (columna central angosta) | `1600px` (ancho completo) |
| Densidad | Baja — cómoda, espaciada | Alta — orientada a datos |
| Patrón dominante | Cards apiladas verticalmente | Tablas, grids, paneles |
| Sidebar | `284px`, navegación de cuenta del comprador | `284px`, navegación del producto |
| Tono | Cercano, de servicio al comprador | Funcional, operativo |

> ❌ **No usar** la tipografía Sora/Inter ni los radios de `24px`/`18px` de Landing. El perfil de cliente es un contexto Manrope.
> El perfil de cliente es Dashboard "en modo comprador": misma fundación, layout más simple y centrado.

---

## 1. Tipografía

El perfil de cliente usa **Manrope** como única familia tipográfica. Sora e Inter están **prohibidas** en este contexto, igual que en Dashboard — incluyendo el bloque de "Ayuda" y los links del sidebar.

> ✅ **EXCEPCIÓN DECLARADA (Inter en la tarjeta del historial).** Por decisión de la owner (Mayo 2026), la **tarjeta de pedido del historial (§9.17)** usa **Inter Bold `17px`** (line-height `25.5px`, tracking `-0.4316px`) en exactamente **tres roles**: **nombre de tienda**, **monto Total** y el **encabezado "N artículos totales"**. Es la única excepción sancionada al principio "Manrope única familia" en el perfil de cliente. Fuera de esos tres roles —y fuera de §9.17— **Inter sigue prohibida**. Esta excepción debe replicarse en `foundation/TYPOGRAPHY.md`.

### Escala en uso

| Rol | Tamaño | Peso | Uso |
|---|---|---|---|
| Page title | `24px` | Bold 700 | Título de página ("Historial de pedidos", "Pedido #1001") |
| Monto destacado | `30px` | Bold 700 | Total del pedido en el detalle (`MX$330.00`) |
| Section heading | `16px` | Bold 700 | Encabezados de bloque ("Pago", "Enviado a", "Datos de facturación") — siempre **fuera** de la card |
| Card title | `16px` | SemiBold 600 / Bold 700 | Nombre de la tienda, nombre del comprador |
| Logo de tienda (letra) | `20px` | ExtraBold 800 | Inicial de la tienda dentro del cuadro de logo (ver §9.13) |
| Body | `14px` | Regular 400 / Medium 500 | Texto general, valores, datos de dirección y facturación |
| Body small | `12px` | Medium 500 | Labels de campo, fechas, metadata de envío |
| Hint / caption | `10px`–`12px` | Medium 500 / Regular 400 | Desglose de pago, helper text, contadores |
| Nav item | `14px` | Medium 500 | Ítems del sidebar |
| Badge contador | `10px` | Bold 700 | Contador de notificaciones, badges numéricos |

**Line-height:** `1.366em` para toda la escala Manrope.

### Color de texto

Todo el texto usa tokens del sistema — nunca hex crudo.

| Rol | Token | Hex | Uso |
|---|---|---|---|
| Primary (Oxford) | `color/base/black-oxford` | `#4C4C4C` | Texto principal, body, títulos, valores |
| Secondary | `Gray 3` | `#828282` | Texto secundario, labels, metadata, **narrativa de envío** |
| Disabled | Gray 400 | `#A3A3A3` | Texto deshabilitado, placeholders |
| Inverse | `color/base/white` | `#FFFFFF` | Texto sobre fondos primarios u oscuros |
| Link | Blue 500 | `#2180FF` | Links interactivos *(de uso restringido — la convención del perfil de cliente es texto significativo en Oxford con `underline` para interactividad; este azul se reserva para enlaces externos o casos específicos)* |

### Anti-patrones tipográficos

- ❌ Sora o Inter en cualquier elemento del perfil de cliente, incluido el sidebar
- ❌ Pesos fuera de los válidos (400/500/600/700/800)
- ❌ Hex crudo de texto — siempre token (`black-oxford`, `Gray 3`)
- ❌ Texto en rojo para acentos decorativos — el rojo comunica error o CTA primario, igual que en Dashboard
- ❌ Section headings dentro de cards — siempre arriba como hermano anterior (ver §5 y §8.3)

---

## 2. Layout y contenedor

El perfil de cliente usa un **layout de columna central angosta** dentro de la estructura header + sidebar + contenido. A diferencia del Dashboard, el contenido no ocupa el ancho completo: se centra en una columna de lectura cómoda.

### Estructura base de página

```
┌──────────────────────────────────────────────────────────┐
│  Header (logo T1 Tienda + notificaciones + avatar)         │
├───────────────┬──────────────────────────────────────────┤
│               │                                          │
│   Sidebar     │        Columna central de contenido      │
│   284px       │        ~672px, centrada                  │
│               │                                          │
│   Inicio      │        [ Título de página ]              │
│   Historial   │        [ Card ]                          │
│   Métodos     │        [ Card ]                          │
│   Direcciones │        [ Card ]                          │
│   Config.     │                                          │
│               │                                          │
│   Ayuda       │                                          │
└───────────────┴──────────────────────────────────────────┘
```

### Contenedor

| Breakpoint | Sidebar | Contenido | Notas |
|---|---|---|---|
| Mobile `360px` | Oculto / drawer | `100% - 32px`, padding `16px` | Header simplificado |
| Tablet `768px` | Colapsado | Columna fluida centrada | |
| Desktop `1280px`+ | `284px` visible | Columna `~672px` centrada | El contenido **no** se estira al ancho completo |

> El canvas de Figma es `1440px`. La columna de contenido se mantiene angosta (`~672px`) y centrada dentro del área disponible para mantener legibilidad — el perfil de cliente es un contexto de lectura, no de operación densa.

### Estructura base de código

```tsx
<div className="flex min-h-screen flex-col bg-white">
  {/* Header */}
  <header className="flex h-[63px] items-center justify-between border-b border-gray-100 px-5">
    {/* logo + notificaciones + avatar */}
  </header>

  <div className="flex flex-1">
    {/* Sidebar */}
    <aside className="w-[284px] shrink-0 border-r border-gray-100 bg-white p-6">
      {/* navegación */}
    </aside>

    {/* Main content */}
    <main className="flex-1">
      <div className="mx-auto w-[672px] py-8">
        {/* título + cards */}
      </div>
    </main>
  </div>
</div>
```

---

## 3. Header

Barra superior fija, blanca, full-width.

| Propiedad | Valor |
|---|---|
| Altura | `63px` |
| Background | `#FFFFFF` |
| Borde inferior | `1px solid #F3F4F6` |
| Logo (izquierda) | `t1-logotipo` — solo el logotipo T1, **sin** texto "tienda" |
| Acciones (derecha) | Botón de notificaciones + avatar de usuario |

### Botón de notificaciones

Ícono de campana `36×36`, radius `10px`, fondo blanco. Cuando hay notificaciones sin leer, muestra un badge contador `14×12` con fondo Red 500 (`#DB3B2B`), texto blanco Bold `10px`, posicionado sobre la esquina superior derecha (`top: 12px, left: 20px` respecto del botón). El contador se trunca con `+` cuando excede 9: `1`, `2`…`9`, `+9`.

### Avatar de usuario

Circular `44×44`, `border-radius: 56px` (circular completo). Dos variantes:
- **Con foto:** `<img>` con `object-fit: cover`, sin borde.
- **Sin foto (iniciales):** fondo Red 500 (`color/background/avatar/user_red #DB3B2B`), iniciales Manrope ExtraBold 800, blanco.

> El avatar **siempre** está presente — sin foto, el fallback son las iniciales, no un placeholder genérico.

---

## 4. Sidebar — Navegación del comprador

El sidebar del perfil de cliente es la navegación de la **cuenta del comprador**, no del producto. Es plano y corto.

| Propiedad | Valor |
|---|---|
| Ancho | `284px` |
| Background | `#FFFFFF` |
| Borde derecho | `1px solid #F3F4F6` |
| Padding | `24px` |
| Fuente nav items | Manrope Medium 500, `14px` |
| Ítems | Inicio · Historial de pedidos · Métodos de pago · Direcciones de envío · Configuraciones |
| Bloque inferior | "Ayuda" + links: Términos y Condiciones · Política de privacidad · Pagar con T1 |

### Estados de ítem de menú

| Estado | Background | Texto | Ícono |
|---|---|---|---|
| Default | Transparente | `#4C4C4C` | Outline, `#4C4C4C` |
| Hover | `#F3F3F3` (Gray 200) | `#4C4C4C` | `#4C4C4C` |
| Selected | `#F3F3F3` (Gray 200), radius `10px` (píldora) | `#4C4C4C` | `#4C4C4C` |

### Glifos por ítem (obligatorios)

Cada ítem del sidebar usa un glifo específico — no son intercambiables. Todos `20×20`, outline, color Oxford `#4C4C4C` en cualquier estado.

| Ítem | Glifo | Asset / referencia |
|---|---|---|
| Inicio | Casa | `icons8-home` |
| Historial de pedidos | **Carrito de compras** | `icons8-shopping-cart` |
| Métodos de pago | Tarjetas bancarias | `icons8-bank-cards` |
| Direcciones de envío | **Mapa plegado con pin** | `icons8-map` |
| Configuraciones | **Engrane (settings)** | `Icon/settings` |

> ❌ **No usar** glifos genéricos como "documento" o "clipboard" para Historial de pedidos. Debe ser carrito. Para Direcciones debe ser **mapa con pin**, no pin solo. Para Configuraciones es un **engrane** (corrección Jun 2026: el MD documentaba "camión" por error — el nodo usa `Icon/settings`).

```tsx
{/* Ítem activo */}
<a className="flex items-center gap-2.5 rounded-[10px] bg-gray-200 px-3 py-1.5">
  <Icon className="h-5 w-5 text-oxford" />
  <span className="font-manrope text-[14px] font-medium text-oxford">
    Historial de pedidos
  </span>
</a>

{/* Ítem default */}
<a className="flex items-center gap-2.5 px-3 py-1.5 hover:rounded-[10px] hover:bg-gray-200">
  <Icon className="h-5 w-5 text-oxford" />
  <span className="font-manrope text-[14px] font-medium text-oxford">
    Inicio
  </span>
</a>
```

> A diferencia del Dashboard, el ítem seleccionado se marca con una **píldora gris de fondo completo** (radius `10px`), no con borde izquierdo rojo. El sidebar del perfil de cliente es navegación plana de un solo nivel — sin submenús anidados ni flyouts.

### Bloque "Ayuda"

Anclado al fondo del sidebar, **centrado horizontalmente** en su contenedor (`flex flex-col items-center`). El texto "Ayuda" (Manrope Medium, `14px`, Oxford) sobre tres links de pie centrados en Manrope Medium, `10px`, color `#99A1AF` — Términos y Condiciones, Política de privacidad, Pagar con T1. Gap entre "Ayuda" y los links: `16px`. Gap entre links: `8px`.

```tsx
<div className="mt-auto flex flex-col items-center gap-4">
  <span className="font-manrope text-[14px] font-medium text-oxford">Ayuda</span>
  <div className="flex flex-col items-center gap-2">
    <a className="font-manrope text-[10px] font-medium text-[#99A1AF]">Términos y Condiciones</a>
    <a className="font-manrope text-[10px] font-medium text-[#99A1AF]">Política de privacidad</a>
    <a className="font-manrope text-[10px] font-medium text-[#99A1AF]">Pagar con T1</a>
  </div>
</div>
```

> ❌ **No alinear** "Ayuda" ni los links a la izquierda. El bloque entero va centrado.

---

## 5. Cards

La card es el componente estructural dominante del perfil de cliente. Toda la información se organiza en cards apiladas verticalmente dentro de la columna central.

> ⚠ **Regla crítica de composición:** los **section headings** ("Pago", "Envío #1001", "Enviado a", "Datos de facturación") viven **fuera y arriba** de la card, no dentro de ella. La card contiene solo los datos; el título precede a la card como hermano anterior. Ver §8.3 para el patrón completo.

```tsx
{/* ✓ Correcto */}
<section>
  <h3 className="mb-3 font-manrope text-[16px] font-bold text-oxford">Pago</h3>
  <div className="rounded-[10px] border border-[#e7e7e7] bg-white p-4">
    {/* datos */}
  </div>
</section>

{/* ✗ Incorrecto — título dentro de la card */}
<div className="rounded-[10px] border border-[#e7e7e7] bg-white p-4">
  <h3>Pago</h3>
  {/* datos */}
</div>
```

| Propiedad | Valor |
|---|---|
| Background | `#FFFFFF` |
| Border | `1px solid #E7E7E7` (`color/neutral/gray-400`) |
| Border radius | `10px` |
| Padding interno | `16px` (`margins/m`) |
| Gap interno | `12px` (`margins/s`) |
| Separación entre cards | `24px` (`margins/xl`) |
| Sombra | Sin sombra — la card se delimita con borde |

### Tipos de card en el perfil de cliente

| Card | Uso | Contenido |
|---|---|---|
| Card de pago | Detalle de pedido | Fecha, método de pago, desglose (subtotal, envío, impuestos, total) |
| Card de envío | Detalle de pedido | Fechas, número de guía, tabla de productos |
| Card de dirección | "Enviado a" / Direcciones | Nombre, contacto, dirección completa |
| Card de facturación | "Datos de facturación" | RFC, régimen, uso de CFDI, CP |
| Card de método de pago | Métodos de pago | Ilustración de tarjeta, dígitos, vigencia, kebab, badge "Principal" |
| Card de dirección | Direcciones de envío | Ícono de pin, nombre del lugar, dirección, kebab, badge "Principal" |
| Card de acceso | Accesos a sub-vistas | Ícono + label + chevron derecho |

```tsx
<div className="rounded-[10px] border border-[#e7e7e7] bg-white p-4">
  <h3 className="mb-3 font-manrope text-[16px] font-bold text-oxford">
    Pago
  </h3>
  {/* contenido */}
</div>
```

> ❌ **No usar** la sombra de las cards de Landing (`0 0 25px...`). El perfil de cliente delimita cards con **borde** `#E7E7E7`, no con sombra.

---

## 6. Botones

El perfil de cliente usa los botones del Dashboard. Hay **tres variantes**: primario, secundario y enlace (text link). Todas comparten `border-radius: 10px` y texto Manrope `12px` (token `text/size/body`).

### 6.1 Primario y secundario

| Propiedad | Primario (`button/primary`) | Secundario (`button/secondary`) |
|---|---|---|
| Background | `#DB3B2B` (Red 500) — `color/background/button/primary_default` | `#FFFFFF` — `color/background/button/secondary_default` |
| Texto | `#FFFFFF` — `color/text/button/primary_default` | `#4C4C4C` (Oxford) — `button/secondary/default_text` |
| Borde | ninguno | `1px solid #E7E7E7` — `color/border/button/secondary_default` |
| Fuente | Manrope **Bold 700**, `12px` | Manrope **Medium 500**, `12px` |
| Border radius | `10px` | `10px` |
| Padding | `10px` | `10px` |
| Altura | `35px` | `35px` |
| Gap interno (ícono↔label) | `8px` | `8px` |

> El peso es el discriminador tipográfico: **primario = Bold 700**, **secundario = Medium 500**. Mismo tamaño (`12px`), mismo radius (`10px`), misma altura (`35px`). No usar SemiBold en estos botones.

**Estados** (heredados del Dashboard, ver `components/STATES.md`): primario deshabilitado = Red 200; secundario hover = fondo `#F8F8F8`; foco visible = anillo `#2180FF` (`:focus-visible`).

### 6.2 Botón de enlace / text link (`button/link`)

Botón sin fondo ni borde, para acciones de navegación de baja jerarquía (encabezados de sección, empties).

| Propiedad | Valor |
|---|---|
| Background / borde | ninguno (transparente) |
| Texto | Manrope **Bold 700**, `12px`, color `#4C4C4C` — `color/text/button/link_default` |
| Padding | `4px` vertical / `9px` horizontal |
| Border radius | `10px` |
| Ícono opcional | a la derecha, `18×18`, gap `9px` (flecha/chevron) |

Usos confirmados: **"Ver todo"** (encabezado de "Pedidos activos", §8.1) y **"Ver historial de pedidos"** (empty de sección, §8.1 — con flecha `18px`). No confundir con "Ver seguimiento", que es **primario** (rojo), no enlace.

### 6.3 Variante con ícono (secundario)

Botón secundario con ícono a la izquierda — p. ej. "Añadir tarjeta". Ícono `18×18` + gap `8px` + label.

### 6.4 Grupo de acciones en pedido

Las tarjetas de pedido y el header del detalle cierran con un grupo de hasta **3 botones** de `160px` de ancho, altura `35px`, radius `10px`, **gap `8px`**, alineados a la derecha (`justify-end`):

```
[ Contactar tienda ]  [ Volver a comprar ]  [ Ver seguimiento ]
   secundario             secundario            primario
```

> "Ver seguimiento" es el CTA **primario** (rojo) y, según annotation del Figma, **abre el modal de seguimiento**. "Contactar tienda" y "Volver a comprar" son **secundarios**.

### 6.5 Composición del grupo según contexto

**Qué botones aparecen no es fijo: depende del estatus del pedido (historial, §9.18) o del contexto (Home, §8.1).** Reglas:

- **Primario "Ver seguimiento"** → solo cuando el pedido es rastreable (En camino, Entregado, Enviado parcialmente, Parcialmente entregado).
- **3er secundario "Cancelar pedido"** → solo en estados cancelables (Pendiente de pago, En preparación, Parcialmente reembolsado).
- **Terminales** (Cancelado, Reembolsado) → solo 2 secundarios (Contactar tienda · Volver a comprar).
- **Tarjeta compacta/mini** (Home "Otros pedidos") → **sin botones**.

La matriz completa por estatus está en §9.18; las densidades de tarjeta en §9.19.

---

## 7. Badges de estado del pedido

El estado del pedido se comunica con un badge (chip). El perfil de cliente maneja un sistema amplio de estados con código de color.

| Propiedad | Valor |
|---|---|
| Fuente | Manrope Bold 700, `11px` |
| Border radius | `11px` |
| Padding | `4px 10px` |

### Mapa de estados

| Familia | Estados | Background | Texto |
|---|---|---|---|
| **Neutral** | En camino · En preparación · Pendiente de pago · Enviado parcialmente · Parcialmente entregado · Parcialmente cancelado · Parcialmente reembolsado | `chip_gray` `rgba(195,195,195,0.2)` | Oxford `#4C4C4C` |
| **Éxito** | Entregado | `overlay/turquoise` `rgba(82,245,176,0.1)` | `#008073` |
| **Informativo** | Reembolsado | `rgba(33,128,255,0.1)` (Blue overlay) | Blue 500 `#2180FF` |
| **Negativo** | Cancelado | `overlay/red` `rgba(254,77,97,0.1)` | `#FE4D61` |

> Los estados "parciales" (entregado/cancelado/reembolsado/enviado) usan el chip **neutral gris** — el matiz parcial se comunica en el texto, no en el color.
> En el detalle de pedido el badge aparece bajo el monto y también junto al título de cada envío ("Envío #1001 · 1 producto · En camino").
> En la **tarjeta del historial**, el estatus además **determina la fila de envío y el grupo de botones**: ver §9.18.

---

## 8. Estructura de pantallas

### 8.1 Inicio (Home)

Pantalla de entrada del perfil de cliente. Encabeza con un **saludo personalizado** y la sección **"Pedidos activos"**. Fuente: nodos Figma `593:173058` (con activos) y `633:179260` (sección vacía).

**Saludo personalizado** (siempre que el cliente tiene nombre configurado):
- Título **"Hola {nombre}, bienvenido"** — Manrope **SemiBold `24px`**, color Oxford `#4C4C4C`, line-height `32px`, tracking `0.0703px`.
- Subtítulo **"Administra tus pedidos, direcciones y métodos de pago"** — Manrope **Regular `14px`**, Oxford.
- Gap título↔subtítulo `4px`. El bloque `Main Content` usa padding `32px` h / `24px` v y gap `48px` entre saludo y secciones.

**Encabezado de sección con enlace:**
- **"Pedidos activos"** — Manrope **Bold `18px`**, Oxford — con **text link "Ver todo"** (§6.2) alineado a la derecha (`justify-between`).
- **"Otros pedidos"** — Manrope **Medium `14px`**, Oxford (sin enlace).

#### Estados de la pantalla

| Estado | Cuándo (regla de ruteo) | Contenido |
|---|---|---|
| **A. Con pedidos activos** (`593`) | Cliente con nombre configurado **y** ≥1 pedido activo | Saludo + "Pedidos activos" (1 tarjeta **destacada** + sección "Otros pedidos") |
| **B. Sin pedidos activos** (`633`) | No es primer pedido, solo tiene archivados/inactivos | Saludo + "Pedidos activos" con **empty de sección** (§8.1.1) |

> El primer ingreso absoluto (sin pedidos de ningún tipo) usa el empty de página completa del historial (§8.2 Estado B); el empty de **sección** (B) es distinto y se describe abajo.

Las dos densidades de tarjeta usadas aquí (destacada y compacta/mini) se especifican en **§9.19**.

#### Regla de negocio — "Pedidos activos"

> Annotation embebida en el Figma (`605:174471`). Es la lógica que llena la sección.

1. **Definición.** Un pedido es **activo** cuando su estatus ∈ { **Pendiente de pago**, **En preparación**, **En camino** }.
2. **Ordenamiento** (mayor → menor prioridad):
   1. Fecha de llegada estimada **ascendente** (el que llega primero, primero).
   2. Empate → fecha de creación **descendente** (más reciente primero).
   3. Empate → ID de pedido **descendente**.
   - Especial: ETA = **hoy** → máxima prioridad; ETA **null/desconocida** → al final del grupo de activos.
3. **Estructura y límites de visualización:**

| Pedidos activos | Qué se muestra |
|---|---|
| **0** | Empty de sección (§8.1.1) |
| **1** | Solo tarjeta **destacada**, sin sección "Otros pedidos" |
| **2–5** | 1 **destacada** + el resto (2º–5º) como **mini-tarjetas** en "Otros pedidos" |
| **6+** | 1 **destacada** + 4 **mini** en "Otros pedidos" + "Ver todo" lleva al historial completo |

#### 8.1.1 Empty de sección "Sin pedidos activos"

Empty **inline** dentro de la sección "Pedidos activos" (no es el empty de página completa del §8.2). Centrado, gap `24px`:
- Título **"Sin pedidos activos"** — Manrope **ExtraBold `24px`**, color `#0F172B`, line-height `32px`, tracking `0.0703px`.
- Texto **"Tus pedidos en tránsito aparecerán aquí"** — Manrope **Regular `16px`**, color `#62748E`, line-height `24px`, ancho máx `400px`, centrado.
- **Text link "Ver historial de pedidos"** (§6.2) — Manrope Bold `12px` `#4C4C4C` + flecha `18px`.

> Diferencia clave con §8.2: el empty de página completa del historial **no lleva CTA**; este empty de sección **sí** (el text link). Son dos componentes distintos.

### 8.2 Historial de pedidos

> ✅ **Estado canónico (actualizado Mayo 2026):** esta pantalla tiene **dos estados canónicos**: (1) el **empty state** documentado abajo, y (2) el **listado con tarjetas de pedido**, ahora canonizado a partir del nodo Figma `2341:19451` ("Variables de tarjetas"). La anatomía, variantes y comportamientos de la tarjeta viven en **§9.17**. El stack de miniaturas asociado se canonizó en **§9.4**. Pendientes aún (no en este nodo): filtros/orden (§9.7) y toggle lista/grid (§9.8).

**Estado A — Listado con pedidos:** columna `672px`; las tarjetas se apilan verticalmente con separación `24px`. Cada tarjeta es el componente de **§9.17**. La tarjeta ocupa el ancho de la columna (`~672px`; el nodo de Figma la muestra a `686px` de ancho aislada). Sin filtros ni toggle hasta que §9.7/§9.8 se canonicen.

**Estado B — Empty:**

Empty state centrado, sin CTA. El comprador no crea pedidos desde su perfil — el empty es informativo.

| Elemento | Especificación |
|---|---|
| Título | "Aún no tienes pedidos realizados" — Manrope **ExtraBold 800**, `24px`, color `#0F172B`, line-height `32px`, tracking `0.0703px` |
| Texto de apoyo | "Cuando compres en cualquier tienda de T1 Tienda, tus pedidos y su seguimiento aparecerán aquí." — Manrope Regular 400, `16px`, color `#62748E`, line-height `24px`, centrado, max-width `400px` |
| Gap título↔texto | `24px` |
| Posición | Centrado vertical y horizontalmente en la columna de contenido (`672px`, padding `16px 32px`) |

```tsx
<div className="mx-auto flex w-[672px] flex-col items-center justify-center gap-6 px-8 pt-4">
  <h2 className="font-manrope text-[24px] font-extrabold leading-8 tracking-[0.07px] text-[#0F172B]">
    Aún no tienes pedidos realizados
  </h2>
  <p className="max-w-[400px] text-center font-manrope text-[16px] font-normal leading-6 tracking-[-0.31px] text-[#62748E]">
    Cuando compres en cualquier tienda de T1 Tienda, tus pedidos y su seguimiento aparecerán aquí.
  </p>
</div>
```

> ✅ **La card de pedido ya está canonizada** (§9.17). El bloque histórico que prohibía implementarla queda superado por el nodo `2341:19451`. Lo único que sigue pendiente de canonización en esta pantalla es la **barra de filtros/orden** (§9.7) y el **toggle lista/grid** (§9.8): para esos, si se requieren antes de que existan en Figma, levantar ticket de diseño — no inferir.

### 8.3 Detalle de pedido

Vista de un solo pedido. **Layout en columna centrada de `672px`** con padding `pt-16px px-32px`. El back link queda fuera de la columna (absolute, izquierda). Estructura:

```
[← back]               (botón circular 32×32, ver §9.16)

        ───── Encabezado central ─────
        Pedido #1001                   ← title 18px SemiBold, sin copiar
        [logo tienda]                  ← cuadro 40×40 rojo, ver §9.13
        MX$330.00                      ← Manrope Bold 30px, #101828
        Nuki                           ← Medium 16px, #6A7282
        [ En camino ]                  ← chip neutral

   [Contactar] [Volver a comprar] [Ver seguimiento]
   ↑ los 3 botones de 160px de ancho, gap 8px


   Pago                                ← section heading FUERA de card
   ┌─ card ─────────────────────────────────────┐
   │ Jul 14, 12:39 PM                           │
   │ [ícono marca] tdc                          │
   │              •••• 8599                      │
   │ Subtotal              $215.52              │
   │ Envío (Express)        $80.00              │
   │ Impuestos (incluidos)  $34.48              │
   │ Total                 $330.00  ← Bold      │
   └────────────────────────────────────────────┘

   Envío #1001          1 producto  [En camino]   ← header fuera, 3 elementos
   ┌─ card ─────────────────────────────────────┐
   │ Pedido realizado el 17 de julio del 2025.  │ ← narrativa, no labels
   │ Tu pedido está en camino, salió el 19 de…  │ ← Medium 12px Gray 3
   │ [DHL] 1234567654545                        │ ← link 12px Bold underline
   │ ──── tabla productos ───────────────────── │
   │ Producto      Precio   Cantidad    Total   │ ← header Bold 12px Gray 3
   │ [img] Peluche  $250.00     1     $250.00  │
   └────────────────────────────────────────────┘

   Enviado a
   ┌─ card ─────────────────────────────────────┐
   │ Adrián Rodríguez                           │ ← Medium 12px Oxford
   │ adrian@gmail.com                           │
   │ 55 12 34 56 78                             │
   │                                            │
   │ Dirección de envío           ← Bold 12px   │
   │ C. Lago Zurich 245, Amp Granada…           │ ← Medium 12px
   └────────────────────────────────────────────┘

   Datos de facturación
   ┌─ card ─────────────────────────────────────┐
   │ Persona física                             │ ← ordensiempre fijo
   │ PAPJ850215HDF                              │
   │ Pedro Pascal Jiménez                       │
   │ Régimen de Servicios Profesionales (616)   │
   │ G03 - Gastos en general                    │
   │ 06100                                      │
   └────────────────────────────────────────────┘

   [🏪 Datos de contacto de la empresa      >]   ← card de acceso §9.6
```

**Reglas estructurales obligatorias:**

1. **Section headings fuera de la card** (gap `12px` entre heading y card). Se aplica a "Pago", "Envío #N", "Enviado a", "Datos de facturación". Ver §5.
2. **Encabezado central** del detalle es un componente propio — orden estricto: `título → logo → monto → tienda → chip`. Ver §9.14.
3. **El título "Pedido #1001" NO lleva botón de copiar** en el detalle.
4. **El back link es solo flecha** dentro de botón circular `32×32` — no texto "Volver". Ver §9.16.
5. **La card de Pago NO tiene divider** entre método y desglose.
6. **La card de Envío usa narrativa** ("Pedido realizado el…", "Tu pedido está en camino…"), NO el patrón "Label: valor".
7. **NO incluir labels tipo "Enviado por:" o "Llegada estimada:"** en el detalle — la card de envío usa oraciones completas, no pares label/valor.
8. **Sub-encabezado "Dirección de envío"** Bold `12px` precede al texto de dirección dentro de la card "Enviado a".
9. **Tabla de productos**, no lista. Ver §9.3.
10. **Datos de facturación: orden fijo** — `Persona física → RFC → Nombre fiscal → Régimen → Uso CFDI → CP`, todos Medium `12px` apilados sin labels.
11. **Header de la card de Envío** — los 3 elementos (`Envío #N` · `N productos` · chip de estado) se distribuyen con `flex justify-between`: título a la izquierda, contador en el centro-derecha, chip pegado a la derecha. NO se agrupan a la izquierda con un `gap` pequeño.

```tsx
{/* ✓ Correcto */}
<div className="flex items-center justify-between">
  <h3 className="font-manrope text-[16px] font-bold text-oxford">Envío #1001</h3>
  <div className="flex items-center gap-3">
    <span className="font-manrope text-[12px] text-oxford">1 producto</span>
    <Chip>En camino</Chip>
  </div>
</div>

{/* ✗ Incorrecto — los 3 agrupados a la izquierda */}
<div className="flex items-center gap-3">
  <h3>Envío #1001</h3>
  <span>1 producto</span>
  <Chip>En camino</Chip>
</div>
```

> Un pedido puede contener **varios envíos** (pantalla "Varios productos"). Cada envío es su propia card con su número de guía, estado y tabla de productos.

### 8.4 Métodos de pago

Gestión de tarjetas del comprador (débito o crédito). Sigue el patrón CRUD genérico de [`patterns/FLOWS.md`](../patterns/FLOWS.md) §6. Fuente canónica: nodo `1979:19440`.

**Estados de la pantalla:**

| Estado | Contenido | CTA |
|---|---|---|
| **Vacío** (0 tarjetas) | Texto centrado: título "Aún no cuentas con métodos de pago" (Manrope **Bold `20px`**, Oxford) + cuerpo "Agrega una tarjeta para pagar más rápido en cualquier tienda de T1. Puedes cambiarla o eliminarla cuando quieras." (Manrope Regular `14px`, Oxford, ancho `455px`, centrado) | Botón **primario** "Agregar nueva tarjeta" (`236px`, Manrope Bold `12px`) |
| **Con tarjetas** (1+) | Grid de cards de método de pago (§9.5) — `362px`, `flex-wrap`, gap `24px` (2 columnas en desktop) | Botón **secundario** "Añadir tarjeta" con ícono `+` (`18px`), ancho completo de columna (`362px`), debajo del grid |
| **Agregar / Editar** | Abre el modal de formulario de tarjeta (§9.20) | — |
| **Acciones por tarjeta** | Submenú kebab (§9.5): Establecer como principal · Editar · Eliminar | — |

> Dos tratamientos de botón distintos por contexto: el **empty usa primario** (es la acción principal de una pantalla vacía); la **lista usa secundario** (la acción principal ya es ver/gestionar las tarjetas). Mismo criterio que el empty con CTA del §11.

### 8.5 Direcciones de envío

Gestión de las direcciones guardadas del comprador. Mismo patrón de estados que Métodos de pago (§8.4). Fuente canónica: nodo `1979:19441`.

| Estado | Contenido | CTA |
|---|---|---|
| **Vacío** | Título "Aún no tienes direcciones de envío agregadas" (Manrope **Bold `20px`**) + cuerpo "Te ayudará a completar tus compras más rápido y a dar seguimiento a tus entregas." (Regular `14px`, centrado) | Botón **primario** "Agregar nueva dirección" (`236px`) |
| **Con direcciones** | Grid de cards de dirección (§9.10) — `362px`, `flex-wrap`, gap `24px` | Botón **secundario** "Añadir dirección" con `+` debajo |
| **Agregar / Editar** | Modal de formulario de dirección (§9.11) | — |
| **Acciones** | Submenú kebab (§9.5): Establecer como principal · Editar · Eliminar | — |

> El título de página aparece **centrado** en estas pantallas (en pagos está a la izquierda — inconsistencia menor pendiente de unificar). El **toast** de éxito (§9.9) usa la voz reflexiva: "Se agregó la dirección".
> ⚠ **D6:** en el Figma el botón de la lista dice "Añadir tarjeta" (bug de contenido). El label correcto es **"Añadir dirección"** — ver §15 · D6.

| Estado | Contenido |
|---|---|
| **Vacío** | Empty state centrado: título + texto de apoyo + **CTA primario** "Agregar nueva dirección" (`236px`). Al entrar sin direcciones, el modal de formulario se abre automáticamente. |
| **Con direcciones** | Grid de cards de dirección + botón "Agregar dirección" |

> A diferencia del empty del historial de pedidos, el empty de direcciones **sí lleva CTA** — aquí el comprador sí crea contenido.

Acciones por dirección (vía menú kebab): Establecer como principal · Editar · Eliminar. Crear y editar abren el **modal de formulario de dirección** (§9.11); eliminar abre el **modal de confirmación destructiva** (§9.12). Al guardar se muestra un toast de éxito (§9.9).

### 8.6 Datos de facturación

Datos fiscales del comprador para CFDI. La card de facturación presenta los datos en **orden fijo, sin labels**, todos Manrope Medium `12px` Oxford apilados con gap `4px`:

| Orden | Campo | Ejemplo |
|---|---|---|
| 1 | Tipo de persona | `Persona física` / `Persona moral` |
| 2 | RFC | `PAPJ850215HDF` |
| 3 | Nombre fiscal completo | `Pedro Pascal Jiménez` |
| 4 | Régimen fiscal | `Régimen de Servicios Profesionales (616)` |
| 5 | Uso de CFDI | `G03 - Gastos en general` |
| 6 | Código postal | `06100` |

> ❌ **No usar** el patrón "Label: valor" (ej. "RFC: PAPJ850215HDF"). Los datos se presentan como texto plano apilado — el orden los identifica.

### 8.7 Configuraciones (menú principal)

Pantalla de entrada de los ajustes del comprador. Fuente canónica: nodo `1979:19442`. Título **"Configuraciones"** centrado; debajo, **cuatro grupos**, cada uno con su encabezado y una card-tabla con filas navegables (§9.23). Columna de contenido `672px` centrada, gap `24px` entre grupos.

| Grupo (heading Bold `18px`) | Filas | Tipo de fila |
|---|---|---|
| **Cuenta** | Nombre · Correo electrónico · Teléfono | con valor (§9.23) — abren modal de edición (§9.24) |
| **Facturación** | Datos de facturación | solo-label — abre §8.6 |
| **Seguridad** | Actividad de inicio de sesión | solo-label — abre el detalle de actividad |
| **Soporte** | Centro de ayuda | solo-label — abre el centro de ayuda |

**Valores de la sección Cuenta:** Nombre → nombre completo; Correo → email; Teléfono → enmascarado `••• ••• ••32`.

> Las filas de **Cuenta** abren un **modal de edición** (§9.24). Cambiar correo o teléfono dispara además la **verificación por código** (§9.25). Las filas de Facturación/Seguridad/Soporte navegan a su sub-vista.
> ⚠ **Capas de fondo en el Figma:** los artboards de este nodo arrastran capas **ocultas** del dashboard de comerciante (nav Ventas/Inventario/Pagos, "Selecciona tu tienda", bloques SAT/Bank/Industry). **No son parte del perfil de cliente** y no deben implementarse aquí — ver §15 · nota de capas. Los nombres internos de las filas ("Industry/SAT/Bank block") son solo el nombre del componente reutilizado, no contenido fiscal.

---

## 9. Componentes específicos del perfil de cliente

### 9.1 Línea de desglose de pago

```
Subtotal              $215.52
Envío (Express)        $80.00
Impuestos (incluidos)  $34.48
Total                 $330.00
```

Label a la izquierda (Manrope Medium, `10px`, Oxford), valor a la derecha alineado en columna fija `88px`. La línea "Total" en Manrope Bold `12px`. Gap entre líneas `4px`.

### 9.2 Número de guía con paquetería

```
[ícono paquetería 20×20]  1234567654545
```

| Elemento | Especificación |
|---|---|
| Número | Manrope **Bold 700**, `12px`, color Oxford `#4C4C4C`, `underline` con `decoration-skip-ink: none` |
| Ícono | `20×20`, radius `5px`. Identifica la paquetería (DHL, FedEx, Estafeta…) |
| Gap ícono↔número | `3px` |
| Ancho del bloque | `112px` (acomoda 13 dígitos típicos de guía) |
| Border-radius del bloque | `10px` (área clickeable) |

> ⚠ **El número de guía NO es azul** (`#2180FF`). Es **Oxford `#4C4C4C` Bold subrayado** — sigue la convención del perfil de cliente de que el texto significativo es Oxford, no link-style. El subrayado señala la interactividad sin recurrir al azul.

> El Figma del detalle de pedido **no** muestra ícono de copiar junto al número de guía — solo el ícono de paquetería + el número. Si tu implementación necesita copiar, agrégalo fuera del bloque del link (no dentro), respetando el patrón de ícono+número como un solo componente.

Ver logos de paquetería en [`assets/BRAND-ASSETS.md`](../assets/BRAND-ASSETS.md).

### 9.3 Tabla de productos del envío

Dentro de la card de envío del detalle. **Es una tabla real**, no una lista — el implementador debe usar columnas alineadas, no `<ul>`.

| Elemento | Especificación |
|---|---|
| Header | Manrope **Bold** `12px`, color Gray 3 `#828282`, border-bottom `1px solid #E7E7E7`, padding-bottom `4px`, padding-right `16px` |
| Columnas | Producto (`flex-1`) · Precio (`120px`, center) · Cantidad (`120px`, center) · Total (`120px`, right) |
| Gap entre columnas | `20px` |
| Fila de producto | Padding `16px 16px 16px 0`, gap `20px` |
| Miniatura de producto | `40×40`, `border-radius: 4.667px`, borde `1px #E7E7E7` |
| Texto de producto | Manrope Medium `12px`, Oxford |
| Texto de valores | Manrope Medium `12px`, Oxford |

```tsx
<table className="w-full">
  <thead>
    <tr className="border-b border-[#e7e7e7] pb-1 pr-4 text-[#828282]">
      <th className="text-left font-manrope text-[12px] font-bold">Producto</th>
      <th className="w-[120px] text-center font-manrope text-[12px] font-bold">Precio</th>
      <th className="w-[120px] text-center font-manrope text-[12px] font-bold">Cantidad</th>
      <th className="w-[120px] text-right font-manrope text-[12px] font-bold">Total</th>
    </tr>
  </thead>
  {/* … filas */}
</table>
```

> ❌ **No usar** lista vertical con "Cantidad: N" + precio inline. La tabla con columnas es obligatoria.

### 9.4 Stack de miniaturas de producto

> ✅ **Canonizado** desde el nodo `2341:19451` (§9.17). Usado en la tarjeta de pedido del historial cuando el pedido tiene varios productos.

| Propiedad | Valor |
|---|---|
| Miniatura | `40×40`, radius `8px`, borde **blanco `1px`** (destaca el overlap) |
| Layout | Overlap horizontal `-8px` (margin-right negativo), sin gap |
| Visibles | Hasta **4** miniaturas; la 5ª posición es el contador de overflow |
| Contador de overflow | Cuadro `40×40`, radius `8px`, **fondo negro `#000000`**, texto `+N` Manrope **Bold `13px`** blanco. Ej. `+45` |
| Comportamiento (en tarjeta abierta) | Click en el contador `+N` **cierra la extensión** de la tarjeta (colapsa la lista de productos) |

> En la **tarjeta de un solo producto** no hay stack: se muestra una sola miniatura `40×40` (borde `#EDEDED`). Ver §9.17.

### 9.5 Card de método de pago

```
┌──────────────────────────────────────────┐
│  [VISA]   •••• 1234            [ ⋯ ]       │
│           Vigencia 07/27                   │
│                          [ ★ Principal ]  │
└──────────────────────────────────────────┘
```

| Elemento | Especificación |
|---|---|
| Card | `362×122`, radius `10px`, borde `#E7E7E7`, padding `16px`, contenido `justify-between` |
| Ilustración de tarjeta | `70×45` (aspecto 70/45), radius `10px`, contiene el **logo de la red**. Visa/Mastercard/Carnet: caja blanca con borde `0.857px #E7E7E7`. **Amex: fondo `#006FCF`** con el logo en blanco |
| Dígitos | `•••• 1234` — Manrope **Bold `16px`** (`text/size/section-description`), Oxford |
| Vigencia | "Vigencia MM/YY" — Manrope Medium `12px`, Oxford |
| Menú de acciones | Ícono kebab `⋯` `24×24`, abre el submenú flotante (ver abajo) |
| Badge "Principal" | **Solo en la tarjeta predeterminada.** Fondo `overlay/yellow` `rgba(237,189,85,0.1)`, texto `#F5A623` Manrope SemiBold `11px` (capitalize), ícono de estrella `16px`, radius `7px`, padding `2px 8px` |

> El badge **"Principal"** aparece únicamente en la tarjeta predeterminada; las demás solo muestran el kebab.

**Submenú de acciones (kebab) — componente compartido con §9.10:** Panel flotante, fondo `#FEFEFE` (`background/modal`), radius `10px`, ancho `216px`, sombra `0 0 2.5px rgba(0,0,0,0.1)`, padding vertical `8px`. Opciones en orden (Manrope Medium `14px`, ítems de `40px` de alto):
1. **Establecer como principal** — Oxford `#4C4C4C`
2. **Editar** — Oxford `#4C4C4C`
3. **Eliminar** — **rojo `#DB362B`** (`text/input/hint_error`), única acción destructiva

> Esta es la **única sombra** del perfil de cliente, exclusiva de submenús flotantes. Las cards no llevan sombra. Fuente canónica del flujo de métodos de pago: nodo `1979:19440`.

### 9.6 Card de acceso con chevron

```
┌────────────────────────────────────────────────┐
│  🏪  Datos de contacto de la empresa         >  │
└────────────────────────────────────────────────┘
```

Fondo `#F9FAFB`, radius `10px`, altura `44px`, padding `16px`. Ícono `20×20` + label (Manrope Medium `14px`) + `icon-nav/chevron-right` `16×16`. Navega a una sub-vista.

### 9.7 Filtros y orden del historial

> ⚠ **Aparece en nodo canónico, specs pendientes de análisis.** La barra (buscador + dropdowns **Estatus · Fecha · Canal de venta** + botón **"Filtrar"**) **sí está** en la pantalla canónica "Actividad con pedidos" (`2350:19452`). Falta analizar el componente de filtro a fondo antes de canonizar medidas; las de abajo siguen siendo **provisionales** — no implementar como definitivas todavía.

Sobre la lista de pedidos: barra de búsqueda + un grupo de filtros dropdown (Estado · Fecha · Tienda) + selector de orden.

- **Dropdown de filtro:** caja blanca, borde `#E7E7E7`, radius `7px`, altura `35px`, label Manrope `12px` + chevron-down `16×16`.
- **Filtro de orden:** botón segmentado de dos partes — "Nombre" (label) + ícono de orden ascendente/descendente — bordes `#E7E7E7`, radius `8px`.

### 9.8 Toggle lista / grid

> ⚠ **Componente pendiente de canonización.** Aplica solo a la pantalla "Historial de pedidos — con pedidos" que aún no es canónica v1 (§8.2). No implementar hasta migración del Figma.

Switch de dos íconos para alternar la visualización del historial:

| Estado | Background | Ícono |
|---|---|---|
| Opción activa | `#DB3B2B` (Red 500) | Blanco |
| Opción inactiva | Blanco, borde `#E7E7E7` | Oxford |

Radius `6px` en los extremos del par. La opción seleccionada se rellena con Red 500.

### 9.9 Toast de confirmación

Notificación temporal de éxito tras una acción del comprador (guardar/actualizar tarjeta o dirección, establecer principal, eliminar, etc.). Fuente canónica: nodo `536:126448`.

| Propiedad | Valor |
|---|---|
| Background | `#51AF70` (Success) |
| Texto | Manrope Bold `14px`, blanco, line-height `20px`, tracking `-0.1504px` |
| Border radius | `25px` (pill) |
| Padding | `8px 14px` (v/h) |
| Estructura | **Texto + ícono a la derecha**, gap `2px`, contenido ajustado al texto (sin ancho fijo) |
| Ícono | `check-circle-fill` `30×30`, blanco (a la derecha del texto) |
| Posición | Centrado en la parte superior del área de contenido |

**Mensaje:** una sola línea afirmativa, específica de la acción. Conviven **dos convenciones de copy** según el flujo (pendiente unificar con contenido):
- **Métodos de pago** — voz pasiva "ha sido": "La tarjeta ha sido actualizada", "La tarjeta ha sido agregada".
- **Direcciones** — voz reflexiva "se": "Se agregó la dirección", "Se actualizó la dirección", "Se cambió la dirección principal".
- **Configuraciones** — al enviar el código de verificación: "Se envió un código. Revisa tu teléfono." (y la variante de correo).

> ⚠ **D7 (bug de contenido):** en el nodo de Configuraciones el toast dice "Se envió **en** código" (debe ser "**un**"). No replicar — ver §15.

> El toast es efímero — aparece, se mantiene unos segundos y desaparece. El ícono va **después** del texto (a la derecha), no antes. ⚠ La inconsistencia de voz entre flujos (pagos "ha sido X" vs direcciones "se X") está marcada para unificación de copy. Para banners persistentes del sistema ver [`patterns/NOTIFICATIONS.md`](../patterns/NOTIFICATIONS.md).

### 9.10 Card de dirección

```
┌──────────────────────────────────────────┐
│  [📍]   Almacén central        [ ⋯ ]      │
│         El calvario 2, 20249 San           │
│         Cristóbal de las Casas, Chis; MX   │
│                          [ ★ Principal ]  │
└──────────────────────────────────────────┘
```

| Elemento | Especificación |
|---|---|
| Card | `362px`, altura `122px`, radius `10px`, borde `#E7E7E7`, padding `16px` |
| Ícono de ubicación | `icon-nav/pin-2` `24×24` dentro de contenedor `40×40`, borde Oxford `#4C4C4C`, radius `10px` |
| Nombre del lugar | Manrope Bold `16px`, Oxford — truncado con elipsis si excede |
| Dirección | Manrope Medium `12px`, Oxford |
| Menú de acciones | Ícono kebab `⋯` `24×24`, abre submenú flotante |
| Badge "Principal" | Componente compartido — fondo `overlay/yellow` `rgba(237,189,85,0.1)`, texto `#F5A623` Manrope SemiBold `11px`, ícono de estrella, radius `7px` |

**Submenú de acciones de dirección:** Panel flotante, fondo `#FEFEFE`, radius `10px`, ancho `216px`, sombra `0 0 2.5px rgba(0,0,0,0.1)`, padding vertical `8px`. Opciones (Manrope Medium `14px`): Establecer como principal · Editar · **Eliminar** (en rojo de error `#DB362B`).

> La opción "Eliminar" es la única en rojo del submenú — señala una acción destructiva. Mismo patrón de submenú que la card de método de pago (§9.5).

### 9.11 Modal de formulario de dirección

Modal centrado para crear o editar una dirección. El título cambia según el modo ("Agregar dirección" / "Actualizar dirección").

| Propiedad | Valor |
|---|---|
| Ancho | `600px` |
| Alto | Fijo, `~80%` de la pantalla — con scroll interno |
| Background | `#FFFFFF` |
| Border radius | `10px` |
| Padding | `20px` (`semantic/padding/relaxed`) |
| Estructura | TOP (título + cerrar) · MIDDLE (formulario, scrolleable) · BOTTOM (CTA) |

**TOP:** Título a la izquierda + ícono de cerrar `icon-nav/x-lg` `24×24` a la derecha.

**MIDDLE — campos del formulario** (inputs `57px` de alto, gap `6px` label/campo):

| Bloque | Campos |
|---|---|
| Identificación | Nombre del lugar |
| Contacto | Nombre de contacto · Correo electrónico · Número de contacto (input con selector de bandera MX) · Compañía (opcional) |
| Dirección | Calle · fila [Número exterior · Número interior (opcional)] · fila [Código Postal · Colonia (dropdown)] · fila [Estado · Ciudad] · Referencia (textarea multiline con contador `0/100`) |
| Opciones | Checkbox "Establecer como dirección predeterminada para mis envíos" · Checkbox "Establecer como dirección de devolución" |

**BOTTOM:** Botón primario de ancho fijo (`200px`) alineado a la derecha — "Agregar dirección" / "Actualizar dirección".

> Los campos marcados "(opcional)" lo indican en el propio label. El asterisco de requerido sigue la regla de [`components/ATOMS.md`](../components/ATOMS.md): solo en formularios largos con mezcla de campos requeridos y opcionales — este formulario califica.

### 9.12 Modal de confirmación destructiva

Modal compacto para confirmar acciones irreversibles (eliminar dirección, eliminar método de pago). Es distinto del modal de formulario: más pequeño, centrado, sin scroll.

| Propiedad | Valor |
|---|---|
| Ancho | `398px` |
| Background | `#FFFFFF` |
| Border | `1px solid rgba(0,0,0,0.1)` |
| Border radius | `16px` |
| Padding | `18px 25px` |
| Sombra | `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)` |
| Overlay | `rgba(0,0,0,0.45)` |

**Estructura:**
- **Cerrar:** ícono `icon-nav/x-lg` `24×24` alineado a la derecha.
- **Título:** Manrope Bold `24px`, centrado — pregunta directa ("¿Quieres eliminar la dirección?").
- **Descripción:** Manrope Medium `16px`, gris, centrada — consecuencia de la acción ("Esta dirección se eliminará de tu cuenta de T1.").
- **Botones:** dos botones de igual ancho (`flex-1`), gap `16px`, radius `10px`, padding `12px`:
  - Izquierda — "Cancelar": fondo `#F6F6F5`, texto Oxford.
  - Derecha — acción destructiva ("Eliminala"): fondo Red 500 `#DB3B2B`, texto blanco.

> Este modal usa **overlay más opaco** (`rgba(0,0,0,0.45)`), radius `16px` y doble sombra — distinto del modal de formulario (radius `10px`). Reservado para confirmaciones destructivas.

### 9.13 Logo de tienda

Representación visual de una tienda dentro del ecosistema T1. Aparece en el encabezado central del detalle (§9.14) y en cualquier listado donde se identifique la tienda.

| Propiedad | Valor |
|---|---|
| Forma | Cuadro `40×40` |
| Border radius | `8px` |
| Fondo | Red 500 — token `color/background/avatar/user_red` `#DB3B2B` |
| Contenido | Inicial mayúscula de la tienda |
| Tipografía | Manrope **ExtraBold 800**, `20px`, blanco, `line-height: 16px` |
| Alineación | center / center |

```tsx
<div
  className="flex size-10 items-center justify-center rounded-[8px]"
  style={{ background: "var(--color-background-avatar-user-red)" }}
>
  <span className="font-manrope text-[20px] font-extrabold leading-4 text-white">
    N
  </span>
</div>
```

**Variantes futuras:** cuando la tienda tenga logo subido (imagen), el cuadro contiene `<img>` con `object-fit: cover` — el fallback son siempre las iniciales sobre rojo.

> ❌ **No usar** círculo gris con letra oscura — el logo de tienda **siempre** va sobre rojo. Tampoco usar otra forma de letra (Bold, SemiBold): el peso correcto es **ExtraBold 800**.

### 9.14 Encabezado central del detalle de pedido

Bloque de resumen que abre el detalle de pedido. Es un componente fijo con orden estricto, centrado en la columna de `672px`.

```
        Pedido #1001                    ← line 1
        [logo tienda]                   ← line 2 (componente §9.13)
        MX$330.00                       ← line 3
        Nuki                            ← line 4
        [ En camino ]                   ← line 5
```

| Línea | Contenido | Tipografía | Color |
|---|---|---|---|
| 1 | Título del pedido | Manrope SemiBold 600, `18px`, line-height `28px`, tracking `-0.44px` | `#101828` |
| 2 | Logo de tienda (§9.13) | — | — |
| 3 | Monto total con divisa | Manrope **Bold 700**, `30px`, line-height `36px`, tracking `0.40px` | `#101828` |
| 4 | Nombre de la tienda | Manrope Medium 500, `16px`, line-height `24px`, tracking `-0.31px` | `#6A7282` (Gray 500) |
| 5 | Chip de estado | Ver §7 | — |

**Layout:** `flex flex-col items-center gap-[23px]`. La línea 4 (nombre de tienda) está a `4px` de la línea 3 (monto) — se renderizan como un par visual.

> El monto es `30px`, no `36px`. El título "Pedido #1001" no lleva botón de copiar.

### 9.15 Método de pago en card de Pago

Bloque que identifica la tarjeta usada en un pedido, dentro de la card de Pago del detalle. Es un componente compacto distinto de la card de método de pago de §9.5.

```
┌──────────────────────────┐
│ Jul 14, 12:39 PM          │
│ [ícono]  tdc              │
│          •••• 8599        │
│ ─── desglose abajo ─────  │
└──────────────────────────┘
```

| Elemento | Especificación |
|---|---|
| Fecha del pago | Manrope Medium `14px`, `#101828`, line-height `20px`, tracking `-0.15px`. Formato literal `Jul 14, 12:39 PM` |
| Ícono de marca | `32×20`, radius `4px`. Custom por marca (ver abajo) |
| Tipo de tarjeta | Manrope Medium `14px`, `#101828` — valores: `tdc` (crédito), `tdd` (débito) |
| Máscara | Manrope **Regular 400**, `12px`, color `#6A7282`, formato `•••• NNNN` |
| Layout interno del bloque tipo+máscara | `flex-col gap-2px`, posicionado a `44px` del ícono |

**Íconos de marca de tarjeta** (`32×20`, radius `4px`):

| Marca | Spec |
|---|---|
| Mastercard | Fondo negro `#000000`, dos círculos `10×10` — rojo `#EB001B` (izq, `left:8px top:5px`) y naranja `#F79E1B` (der, `left:14px top:5px`) |
| Visa | Fondo blanco con borde `#E7E7E7`, logo Visa centrado |
| Amex | Fondo azul `#006FCF`, logo Amex centrado |

> ⚠ La **fecha del método de pago se documenta con su formato literal `Jul 14, 12:39 PM`**, distinto del formato relativo-primero del resto del perfil de cliente (§10). Es una excepción aceptada por compatibilidad con el comprobante de pago del procesador.

> ❌ **No usar** label "Fecha del pedido:" ni texto "Método de pago:". El bloque se autodescribe visualmente.

### 9.16 Back link circular

Botón de retorno usado en el detalle de pedido y en cualquier vista hijo. Es un botón circular, **solo ícono — sin texto "Volver"**.

| Propiedad | Valor |
|---|---|
| Forma | Círculo `32×32`, `border-radius: 16777200px` (circular) |
| Fondo | Transparente (`bg-transparent`) |
| Ícono | Flecha izquierda `16×16`, Oxford |
| Posición | Absoluta a la izquierda del bloque principal, alineada con el inicio del encabezado central |
| Hover | Fondo `#F3F3F3` (Gray 200) |

```tsx
<button
  type="button"
  aria-label="Volver"
  className="flex size-8 items-center justify-center rounded-full hover:bg-gray-200"
>
  <ChevronLeftIcon className="size-4 text-oxford" />
</button>
```

> ❌ **No incluir texto "Volver"** junto a la flecha. La accesibilidad se cubre con `aria-label`.

### 9.17 Tarjeta de pedido del historial

> ✅ **Canonizado** desde el nodo Figma `2341:19451` ("Variables de tarjetas"). Es la tarjeta que lista cada pedido en **Historial de pedidos** (§8.2, estado con pedidos) y en "Actividad". **No confundir con el detalle de pedido (§8.3):** son componentes distintos y con reglas opuestas en varios puntos (ver "Diferencias clave" abajo).

Cada pedido se representa con una tarjeta clicable que resume tienda, estado, envío, productos y total, y cierra con un grupo de acciones. Tiene dos **estados de expansión** (Cerrada / Abierta) y variantes por **tipo de envío** y por **cantidad de productos**.

#### Contenedor

| Propiedad | Valor (Figma) | Nota |
|---|---|---|
| Ancho | `~672px` (columna); `686px` aislada en Figma | Ocupa el ancho de la columna del historial |
| Padding interno | `25px` | Excepción canónica de esta tarjeta (la card estándar §5 usa `16px`) |
| Border radius | `16px` | Excepción canónica de esta tarjeta (la card estándar §5 usa `10px`) |
| Borde | `1px solid #E7E7E7` (token `Gray-400`) | El export del Figma muestra `#E5E7EB` en la abierta; usar el token `#E7E7E7` |
| Fondo | `#FFFFFF` | Sin sombra |
| Gap entre bloques mayores | `24px` | Header-resumen ↔ lista ↔ divider ↔ botones |
| Dividers internos | `1px`, color `#F3F4F6` | Separan resumen / lista / acciones |

> ✅ **Excepción canónica (radius/padding):** esta "tarjeta de actividad" —más grande y clicable— usa `16px`/`25px` por decisión de la owner (Mayo 2026). Las cards del **detalle** y demás cards estándar siguen en `10px`/`16px` (§5).

#### Anatomía (estado Cerrada)

```
┌─ tarjeta (radius 16px, padding 25px) ──────────────────────────┐
│ [logo 40] Office Depot              [chip estado]   ·   3 ene   │ ← fila header (clicable)
│           Pedido #1001 [copy]                                   │
│ ─────────────────────────────────────────────────────────────  │
│ [iso] Enviado por:      Llegada estimada:      Número de guía:  │ ← fila de envío: icono 39×39 + label/valor
│       T1enviós          18-20 ene              12345 [copy]     │
│ ─────────────────────────────────────────────────────────────  │
│ [▢▢▢▢ +45]   580 artículos                              Total   │ ← fila resumen
│              50 Productos diferentes               $450,300.00   │
│ ─────────────────────────────────────────────────────────────  │
│        [Contactar tienda] [Volver a comprar] [Ver seguimiento]  │ ← 2 secundarios + 1 primario
└─────────────────────────────────────────────────────────────────┘
```

**Fila header** (contenedor clicable, fondo hover `#F8F8F8`, radius `8px`, padding `4px`):
- **Logo de tienda** `40×40` radius `8px` (imagen de la tienda; fallback = inicial sobre rojo, §9.13).
- **Nombre de tienda** — **Inter Bold `17px`** (excepción declarada §1), line-height `25.5px`, tracking `-0.4316px`, color negro.
- **"Pedido #NNNN"** — Manrope **Regular `13px`**, color `#99A1AF`, line-height `19.5px`, tracking `-0.0762px` + **ícono copiar `14×14`** a la derecha.
- A la derecha, apilados y alineados a la derecha: **chip de estado** (§7) y **fecha relativa** ("3 ene") en Manrope Regular `12px`, color `#6A7282`.

> ⚠ **Aquí "Pedido #NNNN" SÍ lleva ícono de copiar** y es texto secundario gris `13px`. En el **detalle** (§9.14) es el título `18px` SemiBold y **NO** lleva copiar. Son roles distintos.

**Fila de envío** (varía por tipo de envío y por estatus — ver §9.18). Empieza con un **icono de paquetería** y luego usa el patrón **label / valor**:
- **Icono de paquetería al inicio de la fila** — `39×39`, radius `5px`. `t1-logotipo` (T1 Envíos) o `dhl-iso` (paquetería). *(Resuelto Mayo 2026 a favor del nodo `2350:19452`: la fila de envío **sí** lleva este icono inicial. El nodo anterior `2341` no lo mostraba; gana `2350`.)*
- Label: Manrope **SemiBold `12px`**, negro, line-height `25.5px`, tracking `-0.4316px` ("Enviado por:", "Llegada estimada:", "Entregado:", "Número de guía").
- Valor: Manrope **Bold `12px`** (Medium `13px` en algunas variantes), color `#4C4C4C`, line-height `19.5px`, tracking `-0.0762px`.

> ⚠ El patrón **label/valor** ("Enviado por:", "Llegada estimada:") es **propio de esta tarjeta del historial**. El **detalle** (§8.3 reglas 6–7) usa **narrativa** y prohíbe esos labels. Esto resuelve y precisa la anti-regla del §12: los labels viven aquí, no en el detalle.
> Qué labels y qué botones aparecen depende del **estatus del pedido**: ver §9.18.

**Fila resumen:**
- **Stack de miniaturas** (§9.4) a la izquierda: hasta 4 miniaturas + contador `+N` en negro.
- **"N artículos"** Manrope **SemiBold `13px`** `#4C4C4C` + **"N Productos diferentes"** Manrope **Regular `13px`** `#99A1AF`.
- A la derecha: **"Total"** Manrope SemiBold `13px` `#4C4C4C` sobre el **monto** — **Inter Bold `17px`** (excepción declarada §1) negro, formato peso (`$450,300.00`).

**Grupo de acciones:** 3 botones de `160px`, alto `35px`, radius `10px`, gap `8px`, alineados a la derecha (`justify-end`): **Contactar tienda** (secundario) · **Volver a comprar** (secundario) · **Ver seguimiento** (primario, Red 500). El componente trae variantes ocultas de ancho `205px` para layouts de 2 botones y un secundario contextual extra (ej. "Cancelar pedido", §6) según estado.

#### Anatomía (estado Abierta)

Idéntica a la Cerrada hasta el resumen; entre el resumen y los botones se inserta la **lista de productos expandida**:

- Sub-encabezado: **"N artículos totales"** — **Inter Bold `17px`** (excepción declarada §1) negro — sobre **"N productos diferentes"** Manrope SemiBold `13px` `#4C4C4C`.
- **Lista scrolleable**, altura fija `322px`, `overflow` interno. Muestra ~**5 productos** visibles y luego hace scroll (annotation Figma). Gap entre filas `12px`.
- **Fila de producto** (radius `8px`, padding `6px`, gap `14px`): miniatura `40×40` radius `8px` borde `#EDEDED` + nombre de producto (Manrope **SemiBold `13px`** `#4C4C4C`) sobre **"Cantidad: N"** (Manrope **Regular `13px`** `#99A1AF`). La última fila puede llevar fondo `#F8F8F8` (Gray-100).
- **Scrollbar custom** (no nativo): riel `4px` radius `3px` color `#E7E7E7` (Gray-400); pulgar `2px` radius `3px` color `#C3C3C3` (Gray), altura proporcional al contenido.

**Comportamientos (annotations del Figma):**
1. La **fila header** tiene hover suave; al hacer click, **navega al detalle del pedido** (§8.3).
2. En la tarjeta Abierta, click en el contador **`+N`** del stack **cierra la extensión** (colapsa a Cerrada).
3. La lista expandida muestra ~5 productos y el resto por scroll interno.

#### Variantes

**Por tipo de envío** (cambia la fila de envío):

| Variante | "Enviado por" | "Llegada estimada" | "Número de guía" |
|---|---|---|---|
| **T1 Envíos** | `T1enviós` | `18-20 ene` | — (no se muestra guía) |
| **Paquetería** (DHL, etc.) | `DHL express` | `18-20 ene` | ícono iso de paquetería `20×20` + número + ícono copiar `16×16` |
| **Manual** | `Paquetería X` | — (sin ETA) | ícono `truck 24×24` + número + ícono copiar `16×16` |

> ⚠ En esta tarjeta el número de guía **sí** lleva ícono de copiar (`16×16`). En el detalle (§9.2) **no**. El número sigue siendo Oxford bold subrayado, no azul.
> 🐞 **Bug de contenido en Figma (no replicar):** en las variantes Paquetería el slot "Número de guía" muestra el texto `$245.50 - $390.00` (un rango de precio) en lugar de un número de guía. Es placeholder mal pegado; el slot corresponde al **número de guía**.

**Por cantidad de productos** (cambia la fila resumen y la lista):

| Variante | Miniaturas | Línea 1 | Línea 2 |
|---|---|---|---|
| **Varios productos (+5)** | stack hasta 4 + `+N` | `580 artículos` (SemiBold) | `50 Productos diferentes` (Regular gris) |
| **Un solo producto** | 1 miniatura | `10 artículos` | `Silla madera especial X 10` (nombre del producto · cantidad) |

#### Diferencias clave vs. el detalle de pedido (§8.3) — no confundir

| Aspecto | Tarjeta historial (§9.17) | Detalle de pedido (§8.3) |
|---|---|---|
| "Pedido #NNNN" | Texto gris `13px` **con** ícono copiar | Título `18px` SemiBold **sin** copiar |
| Datos de envío | **Label/valor** ("Enviado por:", "Llegada estimada:") | **Narrativa** ("Pedido realizado el…") |
| Número de guía | Con ícono copiar `16×16` | **Sin** copiar |
| Radius / padding | `16px` / `25px` | `10px` / `16px` |
| Productos | Stack de miniaturas + lista scrolleable | **Tabla** de 4 columnas (§9.3) |

#### Tokens (resueltos del Figma)

`Color/Base/Black-oxford #4C4C4C` · `Chip_Gray rgba(195,195,195,0.2)` · `Gray-400 #E7E7E7` (borde/riel scroll) · `Gray #C3C3C3` (pulgar scroll) · `#F8F8F8` (hover header / fila resumen / Gray-100 en Figma) · `#F3F4F6` (dividers) · `#99A1AF` (texto terciario) · `#6A7282` (fecha) · `#EDEDED` (borde miniatura en lista) · botón primario `#DB3B2B` / texto `#FFFFFF`; botón secundario fondo `#FFFFFF` / borde `#E7E7E7` / texto `#4C4C4C`. Radius botón `10px`, padding `10px`, gap `8px`/`10px`.

### 9.18 Comportamiento de la tarjeta por estatus de pedido

> ✅ **Canonizado** desde el nodo Figma `2350:19452` ("Todos los estatus"). Complementa a §9.17: §9.17 define la anatomía; §9.18 define **qué cambia por estatus**. Los colores de chip son los del §7 (aquí se confirman con tokens exactos).

**Solo tres cosas cambian según el estatus: el chip (§7), la fila de envío y el grupo de botones.** El resto de la tarjeta (header, resumen, total) es constante.

| Estatus | Chip (familia §7) | Fila de envío | Botones |
|---|---|---|---|
| **En camino** | Neutral gris `#4C4C4C` | Sí: icono paquetería + "Enviado por" + **"Llegada estimada: 18-20 ene"** (+ nº de guía si paquetería) | 2 sec + **primario "Ver seguimiento"** |
| **Entregado** | Éxito turquesa, texto `#008073`, bg `rgba(82,245,176,0.1)` | Sí: icono + "Enviado por" + **"Entregado: 20 ene"** (fecha real, no rango) | 2 sec + **primario "Ver seguimiento"** |
| **Enviado parcialmente** | Neutral gris | Sí: icono + "Enviado por" + "Llegada estimada" + nº de guía | 2 sec + **primario "Ver seguimiento"** |
| **Parcialmente entregado** | Neutral gris | Sí: icono + "Enviado por" + "Llegada estimada" + nº de guía | 2 sec + **primario "Ver seguimiento"** |
| **Pendiente de pago** | Neutral gris | **No** | 3 sec: Contactar tienda · Volver a comprar · **Cancelar pedido** |
| **En preparación** | Neutral gris | **No** | 3 sec: Contactar tienda · Volver a comprar · **Cancelar pedido** |
| **Parcialmente reembolsado** | Neutral gris | **No** | 3 sec: Contactar tienda · Volver a comprar · **Cancelar pedido** |
| **Cancelado** | Negativo, texto `#FE4D61`, bg `rgba(254,77,97,0.1)` | **No** | 2 sec: Contactar tienda · Volver a comprar |
| **Reembolsado** | Informativo, texto `Blue #2180FF`, bg `rgba(33,128,255,0.1)` | **No** | 2 sec: Contactar tienda · Volver a comprar |

**Reglas de comportamiento (la lógica que rige la tabla):**

1. El **CTA primario "Ver seguimiento"** aparece **solo si el pedido tiene logística rastreable**: En camino, Entregado, Enviado parcialmente, Parcialmente entregado.
2. **"Cancelar pedido"** (3er botón, secundario) aparece **solo en estados aún cancelables**: Pendiente de pago, En preparación, Parcialmente reembolsado.
3. Estados **terminales no rastreables** (Cancelado, Reembolsado) → **solo 2 secundarios** (Contactar tienda · Volver a comprar).
4. La **fila de envío existe solo cuando ya hay logística** (enviado/entregado/parcial-enviado). Estados pre-envío y terminales-no-enviados **no** la muestran.

**Variaciones de la fila de envío** (cuando existe; anatomía base en §9.17):
- Etiqueta de fecha: **"Llegada estimada: [rango]"** en tránsito vs **"Entregado: [fecha única]"** cuando el estatus es Entregado. El "Número de guía" aparece solo en envíos por paquetería.

> ⚠ **No ejemplificado en el nodo:** el estatus **"Parcialmente cancelado"** (listado en §7) no tiene tarjeta de muestra en `2350:19452`. Comportamiento **por confirmar** (presumible: terminal, 2 secundarios). No inferir hasta confirmar con diseño.

### 9.19 Variantes de densidad de la tarjeta de pedido

> ✅ **Canonizado** desde el nodo `593:173058` (Inicio con activos). La tarjeta de pedido tiene **tres densidades**. Todas comparten la misma caja: fondo blanco, borde `#E7E7E7`, `border-radius: 16px` (excepción de "tarjeta de actividad", D2). Cambia el contenido y el padding vertical.

| Densidad | Dónde se usa | Contenido | Padding |
|---|---|---|---|
| **Completa** | Historial (§9.17) | header + envío + **resumen (productos + total)** + acciones | `25px` |
| **Destacada / reducida** | Home → "Pedidos activos" (el pedido destacado) | header + envío + acciones — **sin** resumen ni total | `25px` |
| **Compacta / mini** | Home → "Otros pedidos" (2º–5º) | **solo header** (logo + tienda + "Pedido #N" + copy + chip + fecha) | `25px` h / **`12px` v** |

**Tarjeta destacada (reducida):**
- Anatomía: header (idéntico a §9.17) → divisor → fila de envío → divisor → grupo de botones. **Omite** la fila de resumen y el total.
- Botones según §6.5 (la destacada de Home con estatus rastreable trae 2 secundarios + primario "Ver seguimiento", que abre el modal de seguimiento).

**Tarjeta compacta / mini:**
- Solo la fila header. **Sin** fila de envío, **sin** resumen, **sin botones** (sin CTAs — regla de negocio §8.1).
- Padding `25px` horizontal / `12px` vertical (más baja que la completa).

> ⚠ **Variante por contexto de la fila de envío (D5):** en la tarjeta **destacada de Home** (`593`) la fila de envío **NO** lleva icono de paquetería al inicio; en el historial/estatus (§9.18, `2350`) **sí**. Documentado como diferencia por contexto, no como error. Ver §15 · D5.

### 9.20 Modal de formulario de tarjeta (agregar / editar método de pago)

> ✅ **Canonizado** desde el nodo `1979:19440`. Modal análogo al de dirección (§9.11) pero con campos específicos de tarjeta. Estructura TOP · MIDDLE (scroll) · BOTTOM. **Los campos usan placeholder como etiqueta** (no hay label arriba); el error se comunica con borde rojo + hint abajo (§9.22).

**TOP:** Título **"Añadir nueva tarjeta"** + ícono de cerrar `24×24` a la derecha. En modo edición el título cambia ("Editar tarjeta").

**MIDDLE — dos secciones con su encabezado** (Manrope SemiBold, Oxford):

**1) "Datos de tarjeta"**
- **Número de tarjeta** — placeholder `0000 0000 0000 0000`, con **logos de marca** a la derecha (Visa, Mastercard, Amex, Carnet; ver §9.21).
- Fila [**Fecha de vencimiento** placeholder `MM/AA` · **CVV** placeholder `CVV` con ícono de tarjeta a la derecha].

**2) "Dirección asociada a la tarjeta"** (es la **dirección de facturación**; la etiqueta visible es "Dirección asociada a la tarjeta"):
- Fila [**Nombre** · **Apellidos**]
- **Número celular (opcional)** — input con selector de **bandera MX** a la izquierda.
- **Calle** (ancho completo)
- Fila [**Número exterior** · **Número interior (opcional)**]
- Fila [**Código postal** · **Seleccionar colonia** (dropdown)]
- Fila [**Estado** · **Ciudad**]
- **Referencia (opcional)** — textarea con contador `0/100`.

Placeholders confirmados: "Introduce un número de tarjeta", "MM/AA", "CVV", "Nombre", "Apellidos", "Número celular (opcional)", "Calle", "Número exterior", "Número interior (opcional)", "Código postal", "Seleccionar colonia", "Estado", "Ciudad", "Referencia (opcional)".

Hints de error (estado validación, en rojo `#DB362B` debajo del campo): "Introduce un número de tarjeta", "Introduce una fecha de vencimiento válida", "Introduce el código de seguridad (CVV) de tu tarjeta", "Introduce un nombre", "Introduce un apellido", "Introduce una calle", "Introduce un número exterior", "Introduce un código postal", "Selecciona una colonia", "Introduce un Estado", "Introduce una ciudad".

**BOTTOM:** dos botones alineados a la derecha — **"Cancelar"** (secundario) + **"Guardar tarjeta"** (primario).

> ⚠ **El botón "Guardar tarjeta" inicia DESHABILITADO** (fondo `#F1B0A9` = `background/button/primary_disabled`, texto blanco) y se habilita (Red 500) solo cuando el formulario es válido.

### 9.21 Campo de número de tarjeta con logos de marca

Input de número de tarjeta (placeholder `0000 0000 0000 0000`) que muestra, alineados a la derecha dentro del propio campo, los **logos de las redes aceptadas** (`creditcard`): cuatro íconos de `~25×16` (Visa, Mastercard, Amex, Carnet). Conforme el usuario teclea, la red detectada se resalta y las demás se atenúan (detección de BIN). El **CVV** lleva un ícono de tarjeta (`24×16`) que ilustra dónde encontrar el código.

### 9.22 Campo de formulario (input de texto)

Átomo base de los formularios del perfil de cliente (§9.11, §9.20). Hereda de [`components/ATOMS.md`](../components/ATOMS.md); tokens en uso:

| Propiedad | Token / valor |
|---|---|
| Borde (default) | `color/border/input/default` `#E7E7E7` |
| Borde (error) | rojo `#DB362B` |
| Radius | `10px` |
| Placeholder (= etiqueta del campo) | `color/text/input/text_placeholder` `#C3C3C3` |
| Texto de error / hint | `color/text/input/hint_error` `#DB362B`, debajo del campo |
| Textarea con contador | Contador `n/100` (p. ej. "Referencia") |

> **Patrón placeholder-as-label:** en el formulario de tarjeta los campos no llevan label arriba; el placeholder identifica el campo y el sufijo "(opcional)" marca los no requeridos. El error se muestra como borde rojo + hint en rojo debajo.

### 9.23 Fila de ajuste (settings row)

> ✅ **Canonizado** desde `1979:19442` (§8.7). Fila navegable dentro de una card-tabla de Configuraciones.

| Elemento | Especificación |
|---|---|
| Card-tabla contenedora | Borde `#E7E7E7`, radius `10px`, ancho completo (`608px` en la columna de `672`). Agrupa 1+ filas |
| Divisor entre filas | Línea `#EDEDED` (`HR`), ancho completo |
| Padding de fila | `20px` |
| Label | Manrope **SemiBold `16px`**, Oxford `#4C4C4C` |
| Valor (opcional) | Manrope **Regular `12px`**, Oxford — debajo del label, gap `8px` |
| Chevron | `icon-nav/chevron-right` `16×16`, a la derecha |
| Alto | `~86px` con valor · `~62px` solo-label |

Dos variantes: **con valor** (Cuenta: Nombre, Correo, Teléfono) y **solo-label** (Datos de facturación, Actividad de inicio de sesión, Centro de ayuda). Se diferencia del §9.6 "Card de acceso con chevron" en que la fila de ajuste **no lleva ícono inicial**.

### 9.24 Modal de edición de campo

> ✅ Canonizado desde `1979:19442`. Modal simple para editar un campo de Cuenta.

| Propiedad | Valor |
|---|---|
| Ancho | `400px` |
| Estructura | Título + cerrar (×) · un campo · botón primario |
| Título | "Actualiza el {campo}" — Manrope Bold `20px` |
| Campo | Label + input (§9.22) |
| Botón | Primario ancho completo — "Actualizar el {campo}" |

Variantes: **nombre** (1 paso, campo "Nombre completo"), **correo** y **teléfono** (disparan verificación, §9.25). En el flujo de correo, un paso previo muestra "Primero, vamos a verificar tu correo electrónico actual." + botón "Verificar el correo electrónico".

> ⚠ **D8 (bug de contenido):** en el modal de correo, el label dice "Nombre completo" sobre un campo de email. Debe decir "Correo electrónico". No replicar — ver §15.

### 9.25 Modal de verificación por código (OTP)

> ✅ Canonizado desde `1979:19442`. Modal de confirmación por código de un solo uso tras cambiar correo o teléfono.

| Elemento | Especificación |
|---|---|
| Ancho | `398px` (mismo que el modal destructivo §9.12) |
| Barra superior | `icon-nav/chevron-left` `24×24` (volver) a la izquierda + `icon-nav/x-lg` `24×24` (cerrar) a la derecha |
| Ícono | Ilustración `Icon/Mobile` `44×44`, centrada |
| Título | "Confirma el {teléfono/correo}" — Manrope Bold `~24px`, centrado |
| Subtítulo | "Introduce el código que se envió a {destino enmascarado}" (ej. `••••••47`), centrado |
| **Input OTP** | **6 casillas** de `40×48`, borde `#E7E7E7`, radius `10px`, centradas con gap |
| Reenviar | Text link "Volver a enviar el código" (§6.2), centrado abajo |

Al abrir el modal se dispara el **toast** (§9.9) "Se envió un código…". La barra superior permite **volver** (‹) al paso anterior o **cerrar** (×).

---

## 10. Formato de datos

El perfil de cliente sigue las convenciones de [`content/UX-WRITING.md`](../content/UX-WRITING.md):

| Dato | Formato | Ejemplo |
|---|---|---|
| Fecha relativa | Relativo primero | "Hoy", "Ayer", "3 ene", "12 de jun 2023" |
| Fecha de evento | Día + mes + año en español | "Pedido realizado el 17 de julio del 2025" |
| Fecha en tabla | Día abreviado | "25 oct 2025" |
| **Fecha del pago** (excepción) | Inglés, 12h | `Jul 14, 12:39 PM` |
| Hora | 24 horas | "11 may 05:43 hrs" |
| Monto | Peso mexicano | `$450,300.00` · `MX$330.00` |
| Rango de entrega | Días con guion | "18-20 ene" |
| ETA relativa | Relativo cuando aplica | "Llega hoy" (en tarjeta destacada de Home, §9.19) |
| Tarjeta | Dígitos enmascarados | `•••• 1234` |
| Vigencia de tarjeta | "Vigencia MM/YY" | "Vigencia 07/27" |
| Tipo de tarjeta | Abreviatura minúscula | `tdc` (crédito), `tdd` (débito) |

> ⚠ La **fecha del método de pago** (línea superior de la card de Pago, §9.15) usa formato literal en inglés con AM/PM por compatibilidad con el comprobante del procesador. Es la única excepción al formato relativo-primero/24h del resto del perfil de cliente.

---

## 11. Estados

El perfil de cliente debe cubrir todos los estados obligatorios de [`components/STATES.md`](../components/STATES.md). Los más relevantes:

| Estado | Aplicación en perfil de cliente |
|---|---|
| **Empty** | **Página completa:** "Aún no tienes pedidos realizados" (§8.2, sin CTA). **De sección:** "Sin pedidos activos" (§8.1.1, con text link). **Métodos de pago / Direcciones:** título Bold `20px` + cuerpo Regular `14px` + **CTA primario** "Agregar nueva tarjeta" `236px` (§8.4) |
| **Loading** | Skeleton mientras carga datos del perfil |
| **Filtrado sin resultados** | Pendiente — aplicará cuando la pantalla de historial con cards sea canónica |
| **Error** | Fallo al cargar el perfil / al guardar un método de pago o dirección |

**Empty state — dos variantes según si el comprador puede crear ese contenido:**

| Tipo | Tipografía título | Color título | CTA | Aplica a |
|---|---|---|---|---|
| **Informativo** (sin CTA) | Manrope **ExtraBold 800**, `24px` | `#0F172B` | — | Historial de pedidos |
| **Con CTA primario** | Manrope **Bold 700**, `24px` | Oxford | Botón primario | Direcciones, métodos de pago |

En ambos casos el texto de apoyo va en Manrope Regular `16px`, color `#62748E`, centrado, max-width `400px`. Gap título↔texto `24px`. Contenedor centrado vertical y horizontalmente en la columna de `672px`.

**Loading:** Skeleton — bloques grises con el shape del contenido esperado, no spinner. Confirmado en el nodo `2350:19452`: filas de skeleton con miniatura `45×45` + dos líneas (`200×16` y `100×12`) + monto (`52×16`) a la derecha, repetidas mientras carga el historial.

---

## 12. Anti-patrones del perfil de cliente

| Anti-patrón | Corrección |
|---|---|
| Usar Sora o Inter | El perfil de cliente es contexto Manrope, igual que Dashboard — incluido el sidebar |
| Hex crudo de color | Usar siempre tokens del sistema |
| Radius `24px` en cards | Cards de perfil de cliente: `10px` |
| Sombra en cards | El perfil de cliente delimita cards con borde `#E7E7E7`; la única sombra (`0 0 2.5px...`) es para submenús flotantes |
| Estirar el contenido al ancho completo | La columna de contenido se mantiene angosta (`~672px`) y centrada |
| Sidebar con borde izquierdo rojo en ítem activo | El perfil de cliente marca el activo con píldora gris (`#F3F3F3`, radius `10px`) |
| Rojo decorativo | El rojo es CTA primario o error — nunca decoración |
| Empty state del historial con CTA | El historial es informativo, sin botón. (Direcciones y métodos de pago **sí** llevan CTA — el comprador crea ese contenido) |
| Tablas densas para listar pedidos | El perfil de cliente lista pedidos como cards, no como filas de tabla |
| Submenús anidados / flyouts en el sidebar | El sidebar del comprador es navegación plana de un nivel |
| Chips de estado de pedido en un solo color | Cada familia de estado tiene su color: neutral, éxito, informativo, negativo |
| **Section headings dentro de la card** | Los títulos "Pago", "Envío #N", "Enviado a", "Datos de facturación" viven **arriba** de la card como hermano anterior. Ver §5 y §8.3 |
| **Lista vertical para productos del pedido** | Es una **tabla** con 4 columnas alineadas. Ver §9.3 |
| **Patrón "Label: valor"** en facturación o "Enviado a" | Los datos van apilados sin labels en orden fijo. Ver §8.6 y §8.3 |
| **Importar labels tipo "Enviado por:" / "Llegada estimada:" al detalle** | La card de Envío del detalle usa narrativa, no pares label/valor |
| **Botón "copiar" en el título del detalle** | El título del detalle no lleva ícono de copiar |
| **Texto "Volver" junto al back link** | El back link es solo flecha dentro de botón circular `32×32` (§9.16) |
| **Logo de tienda gris/blanco con letra oscura** | Siempre cuadro rojo `#DB3B2B` con letra blanca ExtraBold 800 (§9.13) |
| **Monto del detalle a `36px`** | El monto del encabezado central es `30px` Bold (§9.14) |
| **Divider entre método de pago y desglose** | La card de Pago no lleva `<hr>`; los bloques se separan por gap interno |
| **"Fecha del pedido:" con label antes de la fecha** | La fecha del pago se renderiza sola en formato literal `Jul 14, 12:39 PM` (§9.15) |

---

## 13. Checklist de QA — Pre-deployment

**Tipografía**
- [ ] Toda la interfaz usa Manrope (nunca Sora ni Inter), sidebar incluido
- [ ] Pesos solo: Regular 400, Medium 500, SemiBold 600, Bold 700
- [ ] Título de página: Bold 700, `24px`
- [ ] Nav items: Medium 500, `14px`
- [ ] Color de texto siempre por token (`black-oxford`, `Gray 3`), nunca hex crudo

**Colores**
- [ ] Botón primario y CTA: `#DB3B2B` (Red 500)
- [ ] Rojo solo en CTA primario o estados de error
- [ ] Texto principal Oxford `#4C4C4C`, secundario `#828282`
- [ ] Borde de card: `#E7E7E7`
- [ ] Chips de estado con el color correcto por familia

**Layout**
- [ ] Header `63px`, blanco, borde inferior `#F3F4F6`, logo **solo T1** (sin texto "tienda")
- [ ] Columna de contenido angosta (`~672px`) y centrada — no a ancho completo
- [ ] Sidebar `284px`, navegación plana de un nivel
- [ ] Ítem de sidebar activo: píldora gris `#F3F3F3`, radius `10px`
- [ ] Sidebar: glifos correctos por ítem (Inicio=casa · Historial=**carrito** · Métodos=tarjetas · Direcciones=**mapa con pin** · Configuraciones=**engrane**)
- [ ] Bloque "Ayuda" + 3 links **centrados** horizontalmente, no a la izquierda
- [ ] Header de "Envío #N" en detalle: `flex justify-between` — título a la izquierda, contador + chip a la derecha (NO agrupados todos a la izquierda con gap)

**Componentes**
- [ ] Cards: borde `#E7E7E7`, radius `10px`, sin sombra
- [ ] Botones: radius `10px`, altura `35px`
- [ ] Badges de estado: radius `11px`, texto Bold `11px`
- [ ] Grupo de acciones en pedido: 2 secundarios + 1 primario
- [ ] Número de guía: Manrope Bold `12px`, Oxford `#4C4C4C`, `underline` (NO azul), ícono de paquetería `20×20`
- [ ] Card de método de pago: `362×122`, dígitos Bold `16px`, "Vigencia MM/YY" Medium `12px`, chip de marca `70×45` (Amex `#006FCF`), badge "Principal" solo en la predeterminada (§9.5)
- [ ] Submenú kebab: orden `Establecer como principal → Editar → Eliminar`; "Eliminar" en rojo `#DB362B`; ancho `216px`, sombra `0 0 2.5px rgba(0,0,0,0.1)` (§9.5)
- [ ] Empty de métodos de pago / direcciones: título Bold `20px` + CTA **primario** `236px`; la lista usa botón **secundario** "Añadir tarjeta" con `+` (§8.4)
- [ ] Modal de formulario de tarjeta: número con logos de marca, vencimiento + CVV, nombre/apellido, sección de dirección; **"Guardar tarjeta" inicia deshabilitado** (`#F1B0A9`) (§9.20)
- [ ] Card de dirección con ícono de pin + badge "Principal" compartido
- [ ] Submenú flotante con sombra `0 0 2.5px rgba(0,0,0,0.1)`; opción "Eliminar" en rojo
- [ ] Modal de formulario de dirección: `600px`, header/middle/bottom, scroll interno
- [ ] Configuraciones: título centrado; grupos Cuenta/Facturación/Seguridad/Soporte (heading Bold `18px`); filas en card-tabla borde `#E7E7E7` r10, divisores `#EDEDED` (§8.7)
- [ ] Fila de ajuste: label SemiBold `16px` + valor opcional Regular `12px` + chevron `16` (sin ícono inicial); `86px` con valor / `62px` solo-label (§9.23)
- [ ] Modal de edición de campo `400px`; modal OTP `398px` con 6 casillas `40×48` + "Volver a enviar el código" (§9.24–9.25)
- [ ] Sidebar: Configuraciones usa **engrane** (`Icon/settings`), NO camión
- [ ] No implementar capas de dashboard ocultas (Ventas/Inventario, SAT/Bank/Industry) del nodo de Configuraciones (§15)
- [ ] Modal de confirmación destructiva: `398px`, radius `16px`, overlay `rgba(0,0,0,0.45)`, botón destructivo en Red 500
- [ ] Toast de éxito: pill verde `#51AF70`, radius `25px`, con check-circle
- [ ] Logo de tienda: cuadro `40×40` radius `8px` fondo Red 500, letra ExtraBold 800 `20px` blanca (§9.13)
- [ ] Encabezado central del detalle: orden estricto `título → logo → monto 30px → tienda gris → chip` (§9.14)
- [ ] Card de Pago: método de pago con ícono de marca + `tdc/tdd` + `•••• NNNN`, sin label "Fecha del pedido:", sin divider (§9.15)
- [ ] Back link: solo flecha en círculo `32×32`, sin texto "Volver" (§9.16)
- [ ] Section headings ("Pago", "Envío #N", "Enviado a", "Datos de facturación") **fuera** de la card (§5)
- [ ] Tabla de productos: real `<table>` con 4 columnas alineadas, no lista (§9.3)
- [ ] Card de envío en detalle: narrativa "Pedido realizado el…" / "Tu pedido está en camino…", sin labels "Enviado por:" (§8.3)
- [ ] Card "Enviado a": sub-encabezado Bold `12px` "Dirección de envío" antes del texto de dirección
- [ ] Card de facturación: orden fijo `Persona → RFC → Nombre fiscal → Régimen → Uso CFDI → CP`, sin labels (§8.6)
- [ ] Header: campana con badge contador (`+9` cuando excede 9), avatar `44×44` con foto o iniciales ExtraBold sobre Red 500 (§3)

**Estados**
- [ ] Empty del historial: título Manrope ExtraBold 800 `24px` color `#0F172B`, texto Regular `16px` color `#62748E`, centrado, sin CTA (§8.2)
- [ ] Loading con skeleton (no spinner)
- [ ] Estado de búsqueda sin resultados cubierto

**Datos**
- [ ] Fechas en formato relativo-primero
- [ ] Horas en formato 24h ("hrs")
- [ ] Montos en formato peso mexicano
- [ ] Tarjetas con dígitos enmascarados `•••• NNNN`

**Accesibilidad**
- [ ] Focus visible en todos los elementos interactivos
- [ ] Touch targets mínimo `44×44px` en mobile
- [ ] Contraste suficiente en todos los textos (ver `accessibility/A11Y.md`)

---

## 14. Estructura de componente estándar

```tsx
"use client"; // solo si tiene interactividad

import { DATOS } from "@/lib/constants";

export default function T1OrderCard() {
  return (
    <div className="rounded-[10px] border border-[#e7e7e7] bg-white p-4">
      <h3 className="font-manrope text-[16px] font-bold text-oxford">
        Título
      </h3>
      {/* contenido */}
    </div>
  );
}
```

**Naming:** `T1` + PascalCase — ej. `T1OrderCard`, `T1OrderDetail`, `T1PaymentMethodCard`, `T1CustomerSidebar`.
**Contenido:** Todo texto va en `src/lib/constants.ts`. Nunca hardcodear contenido en el componente.

---

## 15. Estado de canonización y componentes restringidos

Esta sección es la **fuente única** del estado de cada componente del perfil de cliente. Si un componente está marcado 🛑 **PROHIBIDO IMPLEMENTAR**, no se implementa ni se infiere su anatomía: se levanta ticket de diseño. Un componente solo pasa a ✅ cuando existe un nodo Figma canónico que lo respalde.

| Componente | Estado | Respaldo / nota |
|---|---|---|
| Detalle de pedido (§8.3, §9.13–9.16) | ✅ Canónico | Figma `Perfil-de-cliente` |
| **Tarjeta de pedido del historial (§9.17)** | ✅ **Canónico (Mayo 2026)** | Nodo `2341:19451` "Variables de tarjetas" |
| **Comportamiento por estatus (§9.18)** | ✅ **Canónico (Mayo 2026)** | Nodo `2350:19452` "Todos los estatus" |
| **Inicio / Home (§8.1) + regla de "pedido activo"** | ✅ **Canónico (Mayo 2026)** | Nodos `593:173058` (con activos) y `633:179260` (sección vacía) |
| **Densidades de tarjeta: destacada y compacta (§9.19)** | ✅ **Canónico (Mayo 2026)** | Nodo `593:173058` |
| **Empty de sección "Sin pedidos activos" (§8.1.1)** | ✅ **Canónico (Mayo 2026)** | Nodo `633:179260` |
| **Botón de enlace / text link (§6.2)** | ✅ **Canónico (Mayo 2026)** | Nodos `593`/`633` ("Ver todo" / "Ver historial de pedidos") |
| Stack de miniaturas (§9.4) | ✅ Canónico | Nodo `2341:19451` |
| Empty state del historial (§8.2 Estado B) | ✅ Canónico | Figma |
| Loading del historial (skeleton, §11) | ✅ Canónico | Nodo `2350:19452` (3 filas skeleton) |
| Métodos de pago y direcciones — flujo completo (§8.4–8.5, §9.5, §9.9–9.12, §9.20–9.22) | ✅ **Canónico (Jun 2026)** | Nodos `1979:19440` (pagos) y `1979:19441` (direcciones): empty · formulario · agregado+toast · varios · acciones |
| Configuraciones — menú + edición + OTP (§8.7, §9.23–9.25) | ✅ **Canónico (Jun 2026)** | Nodo `1979:19442`: menú · modales de edición · verificación por código |
| **Filtros y orden del historial (§9.7)** | ⚠ **Aparece en nodo canónico; specs por analizar** | Visible en `2350:19452` (buscador + Estatus/Fecha/Canal + "Filtrar"). Pendiente analizar el componente antes de canonizar medidas. |
| **Toggle lista / grid (§9.8)** | 🛑 **PROHIBIDO IMPLEMENTAR** | Sin nodo canónico. |

**Decisiones resueltas (Mayo 2026, owner Karla Salazar):**

| # | Tema | Sección | Resolución |
|---|---|---|---|
| D1 | Inter en nombre de tienda, Total y "N artículos totales" | §1, §9.17 | ✅ **Excepción declarada.** Inter Bold `17px` permitido solo en esos 3 roles de §9.17. Replicar en `TYPOGRAPHY.md`. |
| D2 | Radius `16px` / padding `25px` de la tarjeta | §5, §9.17 | ✅ **Canonizado** como excepción de "tarjeta de actividad". Cards estándar siguen en `10px`/`16px`. |
| D3 | Slot "Número de guía" muestra rango de precio `$245.50 - $390.00` en variantes Paquetería | §9.17 | ⚠ **Bug de contenido en Figma — no replicar.** El slot es el número de guía. Pendiente corregir el placeholder en el archivo de Figma. |
| D4 | La fila de envío de §9.17 (`2341`) no llevaba icono inicial; la de §9.18 (`2350`) sí | §9.17 | ✅ **Resuelto a favor de `2350`.** La fila de envío **lleva icono de paquetería `39×39` radius `5px`** al inicio (`t1-logotipo`/`dhl-iso`). §9.17 ya actualizado. |
| D5 | La tarjeta **destacada de Home** (`593`) no lleva icono en la fila de envío; el historial/estatus (`2350`) sí | §9.19 | ✅ **Variante por contexto.** Historial/estatus → con icono (D4); tarjeta destacada de Home → sin icono. No es error; documentado en §9.19. |
| D6 | En la lista de direcciones (`468:95280`), el botón de agregar dice **"Añadir tarjeta"** | §8.5 | ⚠ **Bug de contenido en Figma — no replicar.** Debe decir **"Añadir dirección"** (paralelo a "Añadir tarjeta" de pagos). Pendiente corregir el label en el archivo de Figma. |
| D7 | Toast de Configuraciones dice "Se envió **en** código" | §9.9 | ⚠ **Bug de contenido — no replicar.** Debe ser "Se envió **un** código". |
| D8 | Modal de edición de correo: el label dice "Nombre completo" sobre un campo de email | §9.24 | ⚠ **Bug de contenido — no replicar.** Debe ser "Correo electrónico". |
| Capas | Los artboards de Configuraciones (`1979:19442`) arrastran capas **ocultas** del dashboard de comerciante (nav Ventas/Inventario/Pagos, "Selecciona tu tienda", bloques SAT/Bank/Industry) | §8.7 | ℹ️ **Fuera de alcance del perfil de cliente.** No documentar ni implementar; los nombres "SAT/Bank/Industry block" son solo el nombre del componente de fila reutilizado. |

> §9.17 ya documenta los valores reales canonizados. El único punto abierto es **D3** (corrección de contenido en Figma); no afecta la implementación, que usa el número de guía real.

**Flag abierto (a) — logotipo del header.** El §3 fija el asset `t1-logotipo` ("solo T1"), pero los nodos canónicos del header (`2350`, `593`, `633`) referencian **`t1store-imagotipo`** (logo + "tienda", `117×38`). Además, en validaciones visuales el logotipo aparece **sólido en rojo**, lo que contradice `assets/BRAND-ASSETS.md` §1 (negro `#1A1A1A` + acento rojo `#DB3B2B`). **Pendiente decidir** cuál es el asset correcto del header del perfil de cliente antes de fijarlo en §3. No resuelto.

---

## Referencias

- [`foundation/COLORS.md`](../foundation/COLORS.md) — Paleta completa y tokens semánticos
- [`foundation/TYPOGRAPHY.md`](../foundation/TYPOGRAPHY.md) — Escala tipográfica del sistema
- [`foundation/SPACING.md`](../foundation/SPACING.md) — Escala de spacing
- [`foundation/ELEVATION.md`](../foundation/ELEVATION.md) — Sombras y border-radius
- [`foundation/LAYOUT.md`](../foundation/LAYOUT.md) — Grid, breakpoints, responsive
- [`components/ATOMS.md`](../components/ATOMS.md) — Botones, inputs, badges
- [`components/STATES.md`](../components/STATES.md) — Estados obligatorios
- [`patterns/FLOWS.md`](../patterns/FLOWS.md) — Checkout (§4) y CRUD genérico (§6)
- [`patterns/EMPTY-STATES.md`](../patterns/EMPTY-STATES.md) — Patrones de estado vacío
- [`patterns/NOTIFICATIONS.md`](../patterns/NOTIFICATIONS.md) — Toasts y banners del sistema
- [`content/UX-WRITING.md`](../content/UX-WRITING.md) — Formato de fechas, montos y mensajes
- [`assets/BRAND-ASSETS.md`](../assets/BRAND-ASSETS.md) — Logos de paqueterías y terceros
- [`accessibility/A11Y.md`](../accessibility/A11Y.md) — WCAG AA, contraste, ARIA
- [`platforms/DASHBOARD.md`](./DASHBOARD.md) — Contexto del comerciante (base visual compartida)
- [`platforms/LANDING.md`](./LANDING.md) — Contexto de landing pages públicas
- [`workflows/CLAUDE-CONTROLLER.md`](../workflows/CLAUDE-CONTROLLER.md) — Entry point para Claude
