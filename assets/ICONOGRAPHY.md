# Iconografía — NEXUS V2.0

> Catálogo completo de íconos del ecosistema T1: reglas de uso, especificaciones técnicas, categorías y naming conventions. Los íconos son un lenguaje visual que refuerza la claridad y consistencia en todas las plataformas.

**Última actualización:** Marzo 2026 · **Owner:** Karla Salazar — Head of UX/UI  
**Fuente Figma:** `SD — Migration V2` — Artboards: Icon-menu, Icons, Icons-logos, Banks, Banderas

---

## Índice

1. [Especificaciones técnicas](#1-especificaciones-técnicas)
2. [Íconos de navegación / menú (Icon-menu)](#2-íconos-de-navegación--menú-icon-menu)
3. [Íconos del sistema (Icons)](#3-íconos-del-sistema-icons)
4. [Logos de terceros (Icons-logos)](#4-logos-de-terceros-icons-logos)
5. [Bancos mexicanos (Banks)](#5-bancos-mexicanos-banks)
6. [Banderas (Banderas)](#6-banderas-banderas)
7. [Reglas de uso](#7-reglas-de-uso)
8. [Naming conventions](#8-naming-conventions)

---

## 1. Especificaciones técnicas

### Tamaños estándar

| Tamaño | Uso |
|--------|-----|
| **24×24px** | Tamaño base — íconos de UI: acciones, estados, navegación inline |
| **16×16px** | Íconos pequeños — dentro de badges, chips, inputs compactos |
| **30×30px** | Logos de terceros (pagos, carriers, social media) |
| **64×64px** | Logos de terceros tamaño marketplace / plataforma |
| **30px** (xl nav) | Chevrons de navegación principal (tamaño alternativo) |

### Stroke y estilo visual

| Propiedad | Valor |
|-----------|-------|
| **Stroke weight** | 1.5px |
| **Estilo** | Line (outline) como default — Fill disponible en variantes seleccionadas |
| **Corner radius** | Consistente con el token del sistema |
| **Color base** | Hereda color del texto circundante o token semántico aplicado |

### Variantes disponibles por ícono

La mayoría de los íconos del sistema cuentan con una o más de estas variantes:

- `Default` / `Line` — versión outline estándar
- `Fill` / `Color` — versión rellena, usada en estados activos o énfasis
- `Black` / `b/n` — versión monocromática para fondos claros
- `White` — versión blanca para fondos oscuros o de color

---

## 2. Íconos de navegación / menú (Icon-menu)

Íconos exclusivos para el **sidebar de navegación principal** del dashboard. Cada plataforma T1 tiene su ícono de menú asociado.

### Plataformas T1

| Nombre | Slug Figma | Descripción |
|--------|-----------|-------------|
| Home | `Nuevo home` | Inicio / dashboard principal |
| User | `User nuevo` | Perfil de usuario / cuenta |
| Online Store | `Nuevo online store` | T1tienda — gestión de tienda en línea |
| Marketing | `marketing` | T1marketing — campañas y marketing |
| Gallery | `gallery` | Galería de productos / medios |
| Discount | `Nuevo descuento` | Descuentos y promociones |
| Product | `Nuevo producto` | Catálogo / listado de productos |
| Channel | `Nuevo canales` | Canales de venta |
| Orders | `Nuevo pedidos` | Gestión de pedidos |
| Shipping | `Nuevo envios` | T1envíos — logística |
| Online Store (T1) | `Nuevo online store` | Tienda virtual |
| Analytics | `Nuevo reportes` | Reportes y analíticas |
| Tienda de insumos | `insumos 3` | Insumos y materiales |
| Payments | `payments` | T1pagos — métodos de pago |
| Balance / Saldos | `Saldos nuevo` | Balance y saldos |
| Link de pago | `Nuevo link` | Links de cobro |
| Transactions | `Nuevo transacciones 2` | Historial de transacciones |
| Settings / Config | `Nuevo config` | Configuración |
| Antifraude | `antifraude 2` | Sistema antifraude |
| Developers | `Nuevo develop` | API / desarrolladores |
| Payment Method | `Nuevo card` | Métodos de pago guardados |
| Cash | `Nuevo money` | Efectivo / caja |
| Billing / Facturación | `Facturacion nuevo` | Facturación electrónica |
| Hub | `Nuevo Hub` | Centro de integraciones |
| Liquidaciones | `Nuevo liquidacion` | Liquidaciones |
| Locations | `Nuevo pin` | Ubicaciones / sucursales |
| Roles | `Nuevo permisos` | Roles y permisos |
| Security | `Nuevo seguridad` | Seguridad de cuenta |
| Data | `Nuevo datos` | Gestión de datos |
| Access | `Nuevo llave` | Control de acceso |
| Plans | `Nuevos planes` | Planes y suscripciones |
| Quality Control | `Nuevo control` | Control de calidad |
| Crown | `crown` | Usuario premium / plan Pro |

### Variantes de menú — Crown

El ícono Crown tiene dos variantes específicas documentadas para el menú:
- `Property 1=Line` — estado default
- `Property 1=Color` — estado activo / seleccionado

### Uso en sidebar

```jsx
// Ícono de menú — tamaño 24px, color hereda del estado del nav item
<Icon name="menu/home" size={24} />

// Estado activo (fill/color)
<Icon name="menu/home" size={24} variant="color" />
```

---

## 3. Íconos del sistema (Icons)

Catálogo completo de íconos para uso general en el dashboard y landing. Organizados por categoría.

### NAVIGATION

Íconos de dirección y navegación:

| Nombre | Slug Figma | Descripción |
|--------|-----------|-------------|
| arrow-left | `icon/nav/arrow/left` | Flecha izquierda |
| arrow-right | `icon/nav/arrow/right` | Flecha derecha |
| arrow-up | `icon/nav/arrow/up` | Flecha arriba |
| arrow-down | `icon/nav/arrow/down` | Flecha abajo |
| arrow-left-short | `icon/nav/arrow/left-short` | Flecha izquierda corta |
| arrow-right-short | `icon/nav/arrow/right-short` | Flecha derecha corta |
| arrow-up-short | `icon/nav/arrow/up-short` | Flecha arriba corta |
| arrow-down-short | `icon/nav/arrow/down-short` | Flecha abajo corta |
| arrow-bar-right | `icon/nav/arrow/bar-right` | Flecha con barra |
| chevron-down | `icon/nav/chevron/down` | Chevron abajo (sm y lg) |
| chevron-up | `icon/nav/chevron/up` | Chevron arriba (sm y lg) |
| chevron-right | `icon-nav/chevron/right` | Chevron derecha (sm y xl) |
| chevron-left | `icon-nav/chevron/left` | Chevron izquierda (sm y xl) |
| chevrons-left | `icon/nav/chevron/double-left` | Doble chevron izquierda |
| chevrons-right | `icon/nav/chevron/double-right` | Doble chevron derecha |
| chevron-up-down | `icon/nav/chevron/up&down` | Chevron bidireccional |
| menu-hamburger | `icon/nav/menu/hamburguer` | Menú hamburguesa |
| menu-kebab | `icon/nav/menu/kebab` | Menú kebab (vertical) |
| menu-kebab-2 | `icon/nav/menu/meatballs` | Menú meatballs (horizontal) |
| drag-move2 | `icon/nav/menu/drag` | Arrastrar / reordenar |
| waffle | `icon/nav/menu/waffle` | Waffle menu (grid de apps) |

### TEXT

Íconos para edición y formato de texto:

| Nombre | Slug Figma |
|--------|-----------|
| text-center | `icon/text/align/center` |
| text-justify | `icon/text/align/justify` |
| text-left | `icon/text/align/left` |
| text-right | `icon/text/align/right` |
| increase-indent | `icon/text/indent/increase` |
| decrease-indent | `icon/text/indent/decrease` |
| list-ul | `icon/text/list/dot` |
| list-ol | `icon/text/list/number` |
| list-check | `icon/text/list/check` |
| text-expanded | `icon/text/list/expanded` |
| text-pin | `icon/text/location` |

### FILE

Íconos para gestión de archivos:

| Nombre | Slug Figma |
|--------|-----------|
| file-money | `icon/file/bill` |
| file-text | `icon/file/text` |
| files | `icon/file/files` |
| file-excel | `icon/file/excel` |
| file-pdf | `icon/file/pdf` |

### BUILDER

Íconos para el constructor de contenido (landing builder):

| Nombre | Slug Figma |
|--------|-----------|
| header | `icon/builder/header` |
| footer | `icon/builder/footer` |
| form | `icon/builder/form` |
| image-text | `icon/builder/image+text` |
| image-prod | `icon-edit/image+prod` |
| image-banner | `icon/builder/image-banner` |
| image-columns | `icon/builder/image-column` |
| product-featured | `icon/builder/product` |
| product-list | `icon/builder/product-list` |
| table | `icon/builder/table` |
| catalog-list | `icon-info/catalog-list` |
| play | `icon/builder/video` |
| input-cursor-text | `icon/builder/input` |
| input-text | `icon/builder/text` |
| brand-list | `icon/builder/brand` |

### MEDIA

| Nombre | Slug Figma |
|--------|-----------|
| camera | `icon/media/camara` |
| multimedia | `icon/media/multimedia` |
| image | `icon/media/image` |

### ACTION

Íconos para acciones del usuario:

| Nombre | Slug Figma |
|--------|-----------|
| trash | `icon/action/trash` |
| close (md) | `icon/action/close` |
| copy | `icon/action/copy` |
| share | `icon/action/share` |
| paperclip | `icon/action/attach` |
| print | `icon/action/print` |
| backup | `icon/action/backup` |
| upload | `icon/action/upload` |
| download | `icon/action/download` |
| export | `icon/action/export` |
| search | `icon/action/search` |
| check-patch | `icon-action/check-patch` |

### COMMUNICATION

| Nombre | Slug Figma |
|--------|-----------|
| mail | `icon/communication/mail` |
| comments | `icon/communication/comment` |
| text-sms | `icon/communication/sms` |
| smiley | `icon/communication/emotion` |
| whatsapp | `icon/communication/whatsapp` |

### COMMERCE

| Nombre | Slug Figma |
|--------|-----------|
| add-cart | `icon/commerce/addcart` |
| cart.v2 | `icon/commerce/cart` |
| new products | `icon/commerce/products` |
| new product | `icon/commerce/product` |
| Mercado | `icon/commerce/market` |
| variante | `icon/commerce/variant` |
| rotate-coin | `icon/commerce/refund` |
| store | `icon/commerce/store` |
| envelope | `icon-info/envelope` |
| box-1 | `icon-info/box-1` |
| box-2 | `icon-info/box-2` |
| packaging-tape | `icon/commerce/tape` (line + fill) |
| envelope-2 | `icon/commerce/envelope` (line + fill) |
| bag | `icon/commerce/bag` (line + fill) |
| box-3 | `icon/commerce/box` (line + fill) |

### FINANCE

| Nombre | Slug Figma |
|--------|-----------|
| wallet | `icon/finance/wallet` |
| cash.v2 | `icon/finance/cash` |
| store-credito | `icon/finance/store-credit` |
| coin-transfer | `icon/finance/transfer` |
| currency | `icon/finance/currency` |
| receive-money | `icon/finance/collect` |
| ticket | `icon/finance/ticket` |
| calculator | `icon/finance/calculator` |
| cupon | `icon/finance/cupon` |
| comment-money | `icon/finance/money` |

### DATA

| Nombre | Slug Figma |
|--------|-----------|
| grid-2 | `icon/data/grid` |
| list-2 | `icon/data/list` |
| columns | `icon/data/column` |
| sliders | `icon/data/filter` |
| box-arrow-up-right | `icon/data/new-window` |
| full | `icon/data/full` |
| toggle vista | `icon/data/toggle-view` |
| a-to-z-order | `icon/data/name-order` (ascending/descending) |
| highest value-order | `icon/data/value-order` (decreasing/increasing) |
| arrow-down-up | `icon/data/order` (active/upward/downward) |
| arrow-left-right | `icon/data/order-horizontal` (left/right) |

### TIME

| Nombre | Slug Figma |
|--------|-----------|
| calendar | `icon/time/calendar` |
| calendar-rotate | `icon/time/calendar-switch` |
| clock | `icon/time/watch` |

### STATUS

| Nombre | Slug Figma |
|--------|-----------|
| eye | `icon/status/visible` |
| eye-off | `icon/status/hide` |
| info-circle | `icon/status/info` |
| alert-circle | `icon/status/alert` |
| help-circle | `icon/status/help` |
| lock | `icon/status/lock` |

### USER

| Nombre | Slug Figma |
|--------|-----------|
| users | `icon/t1pagos/user` |
| users-circle | `icon/t1pagos/perfiles` |
| top-badge | `top-badge` |
| card-ine | `icon-info/card-ine` |
| pos-profile | `pos-profile` |

### TRANSFORM

| Nombre | Slug Figma |
|--------|-----------|
| rotate-left | `icon/transform/rotate` (left) |
| rotate-right | `icon/transform/rotate` (right) |
| rotate (double) | `icon/transform/rotate` (double) |
| reply | `icon/transform/reply` |
| repeat-short | `icon/transform/repeat` |
| color | `icon/transform/color` |
| position | `icon/transform/position` (right/left/up/down/center/middle/row-down/row-up) |
| direction | `icon/transform/direction` (vertical/horizontal) |

### SYSTEM

| Nombre | Slug Figma |
|--------|-----------|
| laptop-code | `icon/system/laptop` |
| desktop | `icon/system/desktop` |
| cellphone | `icon/system/mobil` |
| tablet | `Icon/tablet` |
| POS | `pos` |
| qr | `icon/system/qr` |
| radio | `icon/system/radio` |
| atom | `icon/system/atom` |
| ia | `icon/system/ia` |

### MATH

| Nombre | Slug Figma |
|--------|-----------|
| plus (sm/md/lg/fill) | `icon/math/plus` |
| minus | `icon/math/minus` |
| hash | `icon/math/hashtag` |
| at-sign | `icon/math/at` |
| percent | `icon/math/percentage` |
| plus-circle | (circle variant) |
| plus-short | (short variant) |
| plus-xl | (extra large) |

### MISC

| Nombre | Slug Figma |
|--------|-----------|
| bookmark | `bookmark` |
| check | (check frame) |
| check-patch | `icon-action/check-patch` |
| star (line + fill) | `icon/t1envios/star` |
| flash (line + fill) | `icon-action/t1envios/flash` |
| hand (line + fill) | `icon/t1envios/hand` |
| loader (5 variantes) | `loader` — animated loading states |
| eclipse | `eclipse` |
| ruler | `icon-ruler` |
| lightbulb | `icon-info/lightbulb` |
| abacus | `icon-info/abacus` |
| CVV (default + AMEX) | `CVV` |
| clipboard-data | `icon/clipboard/data` |
| clipboard-list-check | `icon/clipboard/list` |

---

## 4. Logos de terceros (Icons-logos)

Logos de marcas externas organizados por categoría. Todos los logos de terceros deben usarse siempre en sus versiones oficiales del design system — nunca recrear ni alterar.

### BRAND — Logos T1

| Marca | Componente Figma | Variantes |
|-------|-----------------|-----------|
| T1 (logotipo) | `t1-logotipo` | color, gray |
| T1pagos | `t1pagos-imagotipo` | Default, White |
| T1envíos | `t1envios-imagotipo` | Default, Variant2 |
| T1partners | `t1partners-imagotipo` | Default, Variant2 |
| T1score | `t1score-imagotipo` | Default, White |
| T1pos | `t1pos-imagotipo` | Default, White |
| T1ai | `t1ai-imagotipo` | Default, White |
| T1cuenta | `t1cuenta-imagotipo` | Default, White |
| T1store | `t1store-imagotipo` | Default, White |

> **Nota de uso:** Los imagotipos T1 combinan el isotipo (N) con el nombre de la plataforma. Usar siempre la versión correcta según el fondo (Default = fondo blanco/claro, White = fondo oscuro/de color).

### PAYMENT — Procesadores de pago

| Marca | Componente Figma | Variantes |
|-------|-----------------|-----------|
| Visa | `visa-logotipo` | Default, white, black |
| Mastercard | `mastercard-isotipo` | Default, b/n |
| AMEX | `amex-logotipo` | square, rectangle |
| SPEI | `spei-imagotipo` | Default, b/n |
| Conekta | `conekta-imagotipo` | Default, b/n, isologo |
| Stripe | `stripe-logotipo` | Color, Black, White |
| Aplazo | `aplazo-logo` | Default |
| OXXO | `oxxo-isotipo` | Default, b/n |
| 7-Eleven | `7-eleven-imagotipo` | Default, bn |
| Kueski | `kueski-imagotipo` | Default, isologo, bn |
| OpenPay | `openpay-imagotipo` | Default, bn, isologo |
| GetNet | `getnet-imagotipo` | Default, black, isologo |
| Card brands (conjunto) | `payment card` | visa, mc, amex, vcarnet, spei, kueski, oxxo, seven, paypal, aplazo |

### SALES CHANNEL — Canales de venta

| Marca | Componente Figma | Variantes |
|-------|-----------------|-----------|
| Claroshop | `claroshop-imagotipo` | color, off, imagotipo |
| Sears | `sears-isotipo` | color, off, isotipo |
| Sanborns | `sanborns-isotipo` | color, off, isotipo |
| Amazon | `amazon-iso` | color, off |
| MercadoLibre | `meli-iso` | ml, off |
| Mercado Shops | `logo-mercadoshop` | — |
| AliExpress | `ali-express-iso` | color, off |
| Shein | `shein-iso` | color, off |
| Shopify | `shopify-iso` | Default, Variant2 |
| Stripe (marketplace) | `stripe-iso` | Default, bn |
| Salesforce | `salesforce-iso` | Default, black |
| Telmex | `Telmex-iso` | color, off |
| Elektra | `elektra-iso-marketplace` | color, black |
| Linio | `linio-iso-marketplace` | color, black |
| Walmart | `walmart` | Default, black |
| Coppel | `coppel-iso-marketplace` | color, black |
| Liverpool | `liverpool-iso-marketplace` | color, black |
| TikTok Shop | `tiktokshop` | Default, off |
| TikTok (logo completo) | `TikTok-logo` | Default, off |

### Plataformas e-commerce / ERP

| Marca | Componente Figma | Variantes |
|-------|-----------------|-----------|
| Magento | `magento-iso-plataforma` | Color, Black |
| VTEX | `vtex-iso-plataforma` | Color, Black |
| PrestaShop | `presta-shop-iso-plataforma` | Color, Black |
| Aspel | `aspel-iso-plataforma` | Color, Black |
| Clip | `clip-iso-plataforma` | Color, Black |
| Epos | `epos-iso-plataforma` | Color, Black |
| WooCommerce | `woocommerce-iso-plataforma` | Color, Black |
| Tienda Nube | `tienda-nube-iso-plataforma` | Color, Fill, Black |
| Wix | `wix-iso-plataforma` | Color, Black |
| Siigo | `siigo-iso-plataforma` | Color, Black |
| Pulpos | `pulpos-iso-plataforma` | Color, Black |
| Sicar | `sicar-iso-plataforma` | Color, Black |

### CARRIER — Paqueterías y logística

| Marca | Componente Figma | Variantes |
|-------|-----------------|-----------|
| DHL | `dhl-iso` | Color, Black, Sin BG, user (app) |
| Redpack | `redpack-logo` | Color, Black |
| FedEx | `fedex-logo` | Color, Black, app |
| Estafeta | `estafeta-logo` | Color, Black, app |
| UPS | `ups-iso` | Color, Black, Sin envolvente, APP |
| J&T Express | `j&texpress-iso` | Color, app |
| 99 Minutos | `99min-iso` | iconoColor, iconoBlack, Isologo, Isologo+, SinEnvolvente, app |
| Skydrop | `skydrop-iso` | Color, Black |
| Envía ya | `envia-ya-iso` | Color, Black |
| Manuable | `manuable-iso` | Color, Black |
| Melonn | `melonn-iso` | Color, Black |
| Envia | `envia-iso` | Color, Black |
| Envío Click | `envio-click-iso` | Color, Black |
| Cubbo | `cubbo-iso` | Color, Black |
| Moova | `moova` | Color, Black |
| Paquetexpress | `paquetexpress` | Color, Black, app |
| iVoy | `ivoy-iso` | Color, Black |
| Cargamos | `cargamos` | Color, Black |
| iMile | `imile` | Color |
| Grupo Am/Pm | `grupoAmPm` | Color, app |
| Logify | `logify` | Color |
| Tookan | `tookan` | Color |
| Kometia | `logo-kometia` | — |
| Spin Commerce | `logo-spincommerce` | — |

### SOCIAL MEDIA — Redes sociales y marketing

| Marca | Componente Figma | Variantes |
|-------|-----------------|-----------|
| X (Twitter) | `x-isotipo` | — |
| Reddit | `reddit-isotipo` | — |
| LinkedIn | `linkedin-isotipo` | — |
| Pinterest | `pinterest-isotipo` | — |
| Facebook | `facebook-isotipo` | — |
| Instagram | `Insta` | — |
| Google | `google-isotipo` | — |
| TikTok | `tiktok-isotipo` | color, gray |
| WhatsApp | `Whatsapp` | — |

### MARKETING — Herramientas de marketing digital

| Marca | Componente Figma |
|-------|-----------------|
| Google Shopping | `googleshopping-iso` |
| Meta | `meta-iso` |
| Google Tag Manager | `tagmanager-iso` |
| Google Analytics | `analitycs-iso` |
| Google Ads | `googleads-iso` |
| WhatsApp Business | `whatsapp-iso` |
| FB & IG (Meta) | `fb&IG-iso` |

---

## 5. Bancos mexicanos (Banks)

Catálogo de logos de instituciones bancarias mexicanas. Usados principalmente en flujos de transferencia, conciliación y T1pagos. Tamaño estándar: **30×30px**.

### Bancos principales

Banamex, BBVA, Santander, Banorte, HSBC, Inbursa, Scotiabank, Banregio, Bajío, Banjercito, Bancomext, Banobras, IXE, Mifel, Invex, Bansi, Afirme, The Royal Bank, American Express

### Bancos internacionales

Tokyo, JP Morgan, ING, Deutsche, Credit Suisse, Bamsa, VE Por Más, Azteca, Autofin, Bmonex, Barclays

### Casas de bolsa

Compartamos, Famsa, Bmultiva, Actinver, Wal-Mart, NAFIN, Interbanco, Bancoppel, ABC, UBS Bank, Masari, GBM, Hipotecaria Federal, Bansefi, Bbase, CIBanco, Volkswagen, Consubanco

### Otros / Seguros / Cambio

Tiber, Vector, Skandia, Zurich, Su Casita, CB Intercam, CI Bolsa, Bulltick, Sterling, Profuturo, Mapfre, Única, Valmex, Finamex, Merrill Lynch, Accival, B&B, STP, Telecomm, Evercore, Segmty, ASEA, Kuspit, Sofiexpress, Unagra, CLS, Fincomun, HDI, Order, Reforma, Indeval, Libertad

> **Total:** 70+ instituciones financieras mexicanas cubiertas.

### Uso en código

```jsx
// Logo de banco — siempre 30×30px dentro de contenedor estandarizado
<div className="h-9 w-14 rounded-lg border border-gray-200 bg-white shadow-sm flex items-center justify-center">
  <Image src="/assets/logos/banks/bbva.svg" alt="BBVA" className="h-5 w-auto object-contain" />
</div>

// Estado deshabilitado
<div className="h-9 w-14 rounded-lg border border-gray-100 bg-gray-100 opacity-40 flex items-center justify-center">
  <Image src="/assets/logos/banks/bbva.svg" alt="BBVA" className="h-5 w-auto object-contain" />
</div>
```

---

## 6. Banderas (Banderas)

250+ banderas de países usando el estándar **ISO 3166-1 alpha-2**. Aspect ratio: **3:2** (76.95×51.3px en Figma).

### Implementación

Las banderas se referencian por su código ISO:

```jsx
// Bandera de México
<Image src="/assets/flags/MX.svg" alt="México" width={20} height={14} />

// Patrón de uso en selector de país
<div className="flex items-center gap-2">
  <Image src={`/assets/flags/${countryCode}.svg`} alt={countryName} width={20} height={14} />
  <span>{countryName}</span>
</div>
```

### Países prioritarios para el mercado mexicano

México (MX), Estados Unidos (US), Canadá (CA), Brasil (BR), Argentina (AR), Colombia (CO), Chile (CL), España (ES), Alemania (DE), Francia (FR), Reino Unido (GB), China (CN), Japón (JP)

### Fuente de referencia

Estándar oficial: [ISO 3166-1 — Wikipedia](https://en.wikipedia.org/wiki/ISO_3166-1#Officially_assigned_code_elements)

---

## 7. Reglas de uso

### Reglas obligatorias

1. **Siempre usar los íconos del design system** — nunca crear íconos nuevos sin aprobarlos con el equipo de diseño.
2. **Nunca escalar íconos fuera de los tamaños definidos** (16, 24, 30px). Para necesidades especiales, consultar con el equipo.
3. **El color del ícono hereda del contexto** — usar `currentColor` en SVG para respetar el sistema de tokens.
4. **Logos de terceros: siempre usar la versión oficial** del design system. No recrear, no alterar proporciones, no cambiar colores.
5. **No mezclar estilos** — si una pantalla usa íconos line, no intercalar íconos fill sin una razón semántica clara (ej: estado activo).

### Cuándo usar `fill` vs `line`

| Situación | Variante |
|-----------|----------|
| Estado default / inactivo | `line` |
| Estado activo / seleccionado | `fill` o `color` |
| Ícono decorativo con énfasis | `fill` |
| Menú de navegación — ítem seleccionado | `color` |
| Dentro de badges o chips | `line` (por legibilidad a tamaño reducido) |

### Accesibilidad

- Todo ícono funcional (no decorativo) **debe tener `aria-label`** o estar acompañado de texto visible.
- Los íconos puramente decorativos deben usar `aria-hidden="true"`.
- El contraste mínimo de un ícono sobre su fondo debe cumplir **AA (4.5:1)**.

```jsx
// Ícono funcional — con aria-label
<button aria-label="Eliminar producto">
  <Icon name="trash" size={24} aria-hidden="true" />
</button>

// Ícono decorativo — oculto para lectores de pantalla
<Icon name="star" size={24} aria-hidden="true" />

// Ícono con texto visible — aria-hidden en el ícono
<button>
  <Icon name="download" size={16} aria-hidden="true" />
  <span>Descargar reporte</span>
</button>
```

### Anti-patrones

❌ Usar íconos de librerías externas (Heroicons, Lucide, etc.) sin aprobación del equipo de diseño.  
❌ Cambiar el color de logos de terceros (Visa, DHL, etc.) fuera de las variantes documentadas.  
❌ Usar un ícono a 20px o 32px — los tamaños estándar son 16, 24 y 30px.  
❌ Colocar íconos sin suficiente contraste sobre fondos de color.  
❌ Usar el ícono de `crown` para usuarios no premium.

---

## 8. Naming conventions

### Sistema de íconos internos

```
icon/{categoría}/{nombre}
icon-nav/{subcategoría}/{nombre}
icon-info/{nombre}
icon-action/{nombre}
icon-edit/{nombre}
```

**Ejemplos:**
- `icon/nav/arrow/left`
- `icon/action/trash`
- `icon/finance/wallet`
- `icon-info/catalog-list`
- `icon/builder/image+text`

### Logos de terceros

```
{marca}-{tipo}
```

Donde `{tipo}` puede ser: `iso` (isotipo), `logo` (logotipo), `imagotipo`, `isotipo`

**Ejemplos:**
- `dhl-iso`
- `fedex-logo`
- `t1envios-imagotipo`
- `visa-logotipo`

### Banderas

```
flag/{CÓDIGO-ISO}
```

**Ejemplos:**
- `flag/MX`
- `flag/US`
- `flag/BR`

### Rutas de assets en el proyecto

Los SVGs físicos **no viven en este repo de documentación** — viven en cada proyecto T1 bajo `/public/`:

```
/public/assets/icons/           ← SVGs del sistema de íconos (exportados de Figma)
/public/assets/logos/t1/        ← Logos de marca T1 (t1pagos-default.svg, etc.)
/public/assets/logos/payments/  ← Logos de procesadores de pago (visa.svg, etc.)
/public/assets/logos/carriers/  ← Logos de paqueterías (dhl.svg, fedex.svg, etc.)
/public/assets/logos/channels/  ← Logos de canales de venta (amazon.svg, etc.)
/public/assets/logos/banks/     ← Logos de bancos mexicanos (bbva.svg, etc.)
/public/assets/flags/           ← SVGs de banderas (ISO 3166-1 alpha-2: MX.svg, US.svg…)
```

> **Nota para implementación en código:** Los ~150 íconos del sistema (stroke/line) se consumen mediante el componente `<Icon />` con paths inline en TypeScript — sin necesidad de archivos SVG físicos. Los logos de terceros y banderas se consumen como archivos desde `/public/`. Ver **[ICON-COMPONENT.md](../components/ICON-COMPONENT.md)** para la implementación completa.

---

## Referencias cruzadas

- **[ICON-COMPONENT.md](../components/ICON-COMPONENT.md)** — Cómo implementar `<Icon />` en código: `icons.ts` con SVG paths, `<BrandLogo />`, `<Flag />` y configuración Tailwind.
- **[BRAND-ASSETS.md](./BRAND-ASSETS.md)** — Reglas de identidad de marca T1, uso del logotipo y restricciones.
- **[COLORS.md](../foundation/COLORS.md)** — Tokens de color para íconos semánticos.
- **[A11Y.md](../accessibility/A11Y.md)** — Requisitos de contraste y ARIA para íconos funcionales.
- **[COMPONENTS/ATOMS.md](../components/ATOMS.md)** — Implementación de íconos dentro de botones, badges y chips.
