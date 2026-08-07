# BRAND-ASSETS.md — Assets de Marca

**Repositorio:** `t1-design-system`  
**Ruta:** `assets/BRAND-ASSETS.md`  
**Audiencia:** Diseñadores · Desarrolladores · Marketing · Claude instances  
**Relacionado con:** [`assets/ICONOGRAPHY.md`](./ICONOGRAPHY.md) · [`components/ICON-COMPONENT.md`](../components/ICON-COMPONENT.md) · [`foundation/COLORS.md`](../foundation/COLORS.md)

---

## Índice

1. [Logotipo T1](#1-logotipo-t1)
2. [Imagotipos de plataforma T1](#2-imagotipos-de-plataforma-t1)
3. [Reglas generales de uso de marca](#3-reglas-generales-de-uso-de-marca)
4. [Logos de terceros — Pagos](#4-logos-de-terceros--pagos)
5. [Logos de terceros — Carriers](#5-logos-de-terceros--carriers)
6. [Logos de terceros — Canales de venta](#6-logos-de-terceros--canales-de-venta)
7. [Logos de terceros — Plataformas](#7-logos-de-terceros--plataformas)
8. [Logos de terceros — Social Media](#8-logos-de-terceros--social-media)
9. [Logos de terceros — Marketing](#9-logos-de-terceros--marketing)
10. [Uso en código](#10-uso-en-código)
11. [Proceso de actualización](#11-proceso-de-actualización)

---

## 1. Logotipo T1

El logotipo T1 es el isotipo (símbolo de la "N" estilizada con la barra roja). Es el elemento de identidad más básico del ecosistema — aparece en headers, favicons y combinado con los nombres de plataforma en los imagotipos.

### Variantes

| Variante | Nombre de archivo | Uso |
|----------|------------------|-----|
| Color (default) | `t1-logotipo-color.svg` | Sobre fondos blancos o claros. Negro `#1A1A1A` + acento rojo `#DB3B2B` |
| Gris | `t1-logotipo-gray.svg` | Cuando el logo debe tener menor jerarquía visual o en contextos monocromáticos |

### Colores del logotipo T1

El logotipo es una máscara SVG — el color lo controla el contexto donde se usa:

| Elemento | Color | Token / Valor |
|----------|-------|---------------|
| Símbolo principal (N) | Negro | `#1A1A1A` |
| Acento / barra diagonal | Brand Red | `#DB3B2B` (`color/brand/red/500`) |
| Variante gris | Gris medio | `#4C4C4C` |
| Sobre fondo oscuro | Blanco | `#FFFFFF` (`Color/Base/White`) |

> ⚠️ **Nunca alterar** los colores del logotipo fuera de estas combinaciones oficiales. No usar el rojo 600 (`#E26153`) ni ningún otro tono de la paleta para el acento del logo — solo `#DB3B2B`.

### Tamaños mínimos

| Contexto | Tamaño mínimo |
|----------|--------------|
| Digital (header, app) | 24×24px |
| Favicon | 16×16px |
| Impresión | 10mm |

### Espacio de protección

Mantener un espacio libre equivalente a **la altura de la barra diagonal** alrededor del logotipo en todos los lados.

---

## 2. Imagotipos de plataforma T1

Cada plataforma del ecosistema T1 tiene su imagotipo: la combinación del isotipo (N) + el nombre de la plataforma. Todos siguen el mismo sistema de variantes.

### Catálogo de imagotipos

| Plataforma | Nombre de archivo base | Variantes disponibles |
|------------|----------------------|----------------------|
| T1 Pagos | `t1pagos-default.svg` | Default (color) · White |
| T1 Envíos | `t1envios-default.svg` | Default · Variant2 (alternativa tipográfica) |
| T1partners | `t1partners-default.svg` | Default · Variant2 |
| T1 Score | `t1score-default.svg` | Default · White |
| T1pos | `t1pos-default.svg` | Default · White |
| T1ai | `t1ai-default.svg` | Default · White |
| T1 Cuenta | `t1cuenta-default.svg` | Default · White |
| T1store | `t1store-default.svg` | Default · White |

### Sistema de variantes

**Default (color):** Sobre fondos blancos o claros. El isotipo mantiene negro + rojo brand, el nombre de la plataforma en negro.

**White:** Sobre fondos oscuros, fondos de color intenso o sobre el brand red. Todo el imagotipo en blanco `#FFFFFF`.

**Variant2 (T1 Envíos y T1partners):** Alternativa tipográfica para contextos específicos — consultar con el equipo de diseño antes de usar.

### Convención de naming en `/public/assets/logos/t1/`

```
t1pagos-default.svg
t1pagos-white.svg
t1envios-default.svg
t1envios-white.svg
t1partners-default.svg
t1partners-white.svg
t1score-default.svg
t1score-white.svg
t1pos-default.svg
t1pos-white.svg
t1ai-default.svg
t1ai-white.svg
t1cuenta-default.svg
t1cuenta-white.svg
t1store-default.svg
t1store-white.svg
t1-logotipo-color.svg
t1-logotipo-gray.svg
```

---

## 3. Reglas generales de uso de marca

### Cuándo usar Default vs White

| Fondo | Variante a usar |
|-------|----------------|
| Blanco `#FFFFFF` | Default |
| Gris claro (`gray-50` a `gray-100`) | Default |
| Brand red (`#DB3B2B`, `#E26153`) | White |
| Oscuro (`gray-800` a `gray-900`, `#1A1A1A`) | White |
| Foto o imagen de fondo | Preferir White sobre área oscura; Default sobre área clara |

### Fondos permitidos para los imagotipos T1

Los imagotipos **no tienen espacio de color propio** — siempre se muestran sobre el fondo del contenedor donde viven. Fondos recomendados:

- Blanco puro `#FFFFFF`
- Gris muy claro `#F8F8F8`
- Brand red `#DB3B2B` (solo con variante White)
- Negro `#1A1A1A` (solo con variante White)

### Anti-patrones de marca

❌ No recrear ni rediseñar el logotipo o imagotipos — usar siempre los SVGs del design system.  
❌ No cambiar los colores del isotipo fuera de las combinaciones documentadas.  
❌ No distorsionar, rotar ni aplicar efectos (sombras, gradientes, opacidades parciales) sobre los logos T1.  
❌ No usar el logotipo sobre fondos con poco contraste.  
❌ No combinar el isotipo de T1 con otro logotipo en una misma composición sin jerarquía clara.  
❌ No escalar por debajo del tamaño mínimo (24px digital / 10mm impresión).

---

## 4. Logos de terceros — Pagos

Procesadores y métodos de pago integrados en T1 Pagos. Usar siempre en sus versiones oficiales.

### Procesadores principales

| Marca | Nombre de archivo base | Variantes en Figma | Tipo |
|-------|----------------------|-------------------|------|
| Visa | `visa.svg` | Default · White · Black | Logotipo |
| Mastercard | `mastercard.svg` | Default · B/N | Isotipo |
| American Express | `amex.svg` | Square · Rectangle | Logotipo |
| SPEI | `spei.svg` | Default · B/N | Imagotipo |
| Conekta | `conekta.svg` | Default · B/N · Isologo | Imagotipo |
| Stripe | `stripe.svg` | Color · Black · White | Logotipo |
| OpenPay | `openpay.svg` | Default · B/N · Isologo | Imagotipo |
| Getnet | `getnet.svg` | Default · Black · Isologo | Imagotipo |

### Métodos de pago en efectivo / BNPL

| Marca | Nombre de archivo | Variantes | Tipo |
|-------|-----------------|-----------|------|
| OXXO | `oxxo.svg` | Default · B/N | Isotipo |
| 7-Eleven | `7-eleven.svg` | Default · B/N | Imagotipo |
| Kueski Pay | `kueski.svg` | Default · B/N · Isologo | Imagotipo |
| Aplazo | `aplazo.svg` | Default | Logo |
| PayPal | `paypal.svg` | Default | Logo |

### Componente `payment card`

Figma incluye un componente `payment card` con las siguientes variantes de logo en formato **40.5×30px** (aspecto ratio de tarjeta de crédito):

`visa` · `mastercard` · `amex` · `vcarnet` · `spei` · `kueski` · `oxxo` · `7-eleven` · `paypal` · `aplazo`

Usar este componente para los selectores de método de pago en formularios de checkout — garantiza tamaños y alineaciones consistentes.

### Card brands (grupo de bancos)

Existe un componente `grupo-bancos` con los logos de las principales redes de tarjetas agrupados. Usar en pantallas de onboarding de comerciante y páginas de "métodos de pago aceptados".

---

## 5. Logos de terceros — Carriers

Paqueterías y operadores logísticos integrados en T1 Envíos.

### Carriers principales

| Marca | Nombre de archivo | Variantes | Notas |
|-------|-----------------|-----------|-------|
| DHL | `dhl.svg` | Color · Black · Sin BG · App (user) | Isotipo |
| FedEx | `fedex.svg` | Color · Black · App | Logo horizontal |
| Estafeta | `estafeta.svg` | Color · Black · App | Logo |
| UPS | `ups.svg` | Color · Black · Sin envolvente · App | Isotipo |
| Redpack | `redpack.svg` | Color · Black | Logo |
| 99 Minutos | `99min.svg` | Color · Black · Isologo · Isologo+ · Sin envolvente · App | Imagotipo — más variantes |
| iVoy | `ivoy.svg` | Color · Black | Logo |
| Skydrop | `skydrop.svg` | Color · Black | Isotipo |
| Enviaya | `envia-ya.svg` | Color · Black | Isotipo |
| Manuable | `manuable.svg` | Color · Black | Isotipo |
| Melonn | `melonn.svg` | Color · Black | Isotipo |
| Envia.com | `envia.svg` | Color · Black | Isotipo |
| Envío Click | `envio-click.svg` | Color · Black | Isotipo |
| Cubbo | `cubbo.svg` | Color · Black | Isotipo |
| Paquetexpress | `paquetexpress.svg` | Color · Black · App | Logo |
| J&T Express | `jt-express.svg` | Color · App | Isotipo |
| Moova | `moova.svg` | Color · Black | Logo |
| Kometia | `kometia.svg` | Color | Isotipo |
| Cargamos | `cargamos.svg` | Color · Black | Isotipo |
| iMile | `imile.svg` | Color | Isotipo |
| Logify | `logify.svg` | Color | Isotipo |
| Tookan | `tookan.svg` | Color | Isotipo |
| Grupo Am/Pm | `grupo-ampm.svg` | Color · App | Logo |

### Variante `App` en carriers

Varios carriers tienen una variante `App` (ícono cuadrado redondeado, 60×60px) para uso en contextos de selección de paquetería, tracking cards y notificaciones. Usar esta variante en lugar del logo horizontal cuando el espacio sea cuadrado o pequeño.

---

## 6. Logos de terceros — Canales de venta

Marketplaces y canales donde los sellers de T1 venden sus productos.

### Canales en formato isotipo (30×30px)

Para uso en selectors, tags de canal en órdenes y listas compactas:

| Marca | Nombre de archivo | Variantes |
|-------|-----------------|-----------|
| Amazon | `amazon-iso.svg` | Color · Off (grayscale) |
| Mercado Libre | `meli-iso.svg` | ML · Off |
| Total Play | `total-iso.svg` | Color · Variant2 |
| Shein | `shein-iso.svg` | Color · Off |
| Telmex | `telmex-iso.svg` | Color · Off |
| Shopify | `shopify-iso.svg` | Default · Variant2 |
| AliExpress | `aliexpress-iso.svg` | Color · Off |
| Stripe (canal) | `stripe-iso.svg` | Default · B/N |
| Salesforce | `salesforce-iso.svg` | Default · Black |

### Canales en formato marketplace (64×64px)

Para uso en cards de canal, configuración de integraciones y pantallas de onboarding:

| Marca | Nombre de archivo | Variantes |
|-------|-----------------|-----------|
| Amazon | `amazon-marketplace.svg` | Color · Black |
| Mercado Libre | `meli-marketplace.svg` | Color · Black |
| Shein | `shein-marketplace.svg` | Color · Black |
| Telmex | `telmex-marketplace.svg` | Color · Black |
| Shopify | `shopify-marketplace.svg` | Color · Black |
| Elektra | `elektra-marketplace.svg` | Color · Black |
| Linio | `linio-marketplace.svg` | Color · Black |
| Walmart | `walmart-marketplace.svg` | Default · Black |
| Coppel | `coppel-marketplace.svg` | Color · Black |
| Liverpool | `liverpool-marketplace.svg` | Color · Black |
| Mercado Shops | `mercado-shops.svg` | Default |
| TikTok Shop | `tiktokshop-marketplace.svg` | Default · Off |

### Canales departamentales (en formato imagotipo)

Para uso en landing pages y páginas de partners — incluyen el nombre de la marca:

| Marca | Nombre de archivo | Variantes |
|-------|-----------------|-----------|
| Claroshop | `claroshop-imagotipo.svg` | Color · Off · Imagotipo |
| Sears | `sears-imagotipo.svg` | Color · Off · Isotipo |
| Sanborns | `sanborns-imagotipo.svg` | Color · Off · Isotipo |

### Variante `Off` (grayscale)

La variante `off` aplica grayscale al logo. Se usa en:
- Marquees de "Integra con tus canales de venta" en landing pages (junto con opacidad reducida)
- Estados no conectados en la configuración de canales del dashboard
- Contextos donde el canal aún no está activo para el seller

---

## 7. Logos de terceros — Plataformas

ERPs, plataformas de e-commerce y herramientas de gestión con integración a T1.

| Marca | Nombre de archivo | Variantes | Categoría |
|-------|-----------------|-----------|-----------|
| Magento | `magento.svg` | Color · Black | E-commerce |
| VTex | `vtex.svg` | Color · Black | E-commerce |
| Prestashop | `prestashop.svg` | Color · Black | E-commerce |
| Woocommerce | `woocommerce.svg` | Color · Black | E-commerce |
| Shopify (plataforma) | `shopify-platform.svg` | Color · Black | E-commerce |
| Tienda Nube | `tienda-nube.svg` | Color · Fill · Black | E-commerce |
| TikTok Shop | `tiktokshop.svg` | Default · Off | Social Commerce |
| TikTok (logo horizontal) | `tiktok-logo.svg` | Default · Off | Social Commerce |
| Wix | `wix.svg` | Color · Black | Website builder |
| Aspel | `aspel.svg` | Color · Black | ERP / Facturación |
| Siigo | `siigo.svg` | Color · Black | ERP / Contabilidad |
| Clip | `clip.svg` | Color · Black | Pagos / POS |
| Epos | `epos.svg` | Color · Black | POS |
| Pulpos | `pulpos.svg` | Color · Black | Gestión de inventario |
| Sicar | `sicar.svg` | Color · Black | Facturación |
| Spin Commerce | `spincommerce.svg` | Default | E-commerce |

---

## 8. Logos de terceros — Social Media

Redes sociales para integración en T1 Marketing y perfiles de seller.

| Marca | Nombre de archivo | Variantes |
|-------|-----------------|-----------|
| X (Twitter) | `x-iso.svg` | Color |
| Facebook | `facebook-iso.svg` | Color |
| Instagram | `instagram-iso.svg` | Color |
| LinkedIn | `linkedin-iso.svg` | Color |
| Reddit | `reddit-iso.svg` | Color |
| Pinterest | `pinterest-iso.svg` | Color |
| Google | `google-iso.svg` | Color |
| WhatsApp | `whatsapp-iso.svg` | Color |
| TikTok | `tiktok-iso.svg` | Color · Gray |
| Facebook (v2) | `facebook-iso-2.svg` | Color |

> Todos los isotipos de social media tienen tamaño base **30×30px**.

---

## 9. Logos de terceros — Marketing

Herramientas de marketing y publicidad integradas con T1 Marketing.

| Marca | Nombre de archivo | Descripción |
|-------|-----------------|-------------|
| Google Ads | `googleads-iso.svg` | Google Ads |
| Google Shopping | `googleshopping-iso.svg` | Google Shopping |
| Google Analytics | `analytics-iso.svg` | Google Analytics |
| Google Tag Manager | `tagmanager-iso.svg` | Google Tag Manager |
| Meta | `meta-iso.svg` | Meta (Facebook + Instagram Ads) |
| WhatsApp Business | `whatsapp-iso.svg` | WhatsApp Business API |
| FB & IG | `fb-ig-iso.svg` | Facebook e Instagram combinados |

---

## 10. Uso en código

### Componente `<BrandLogo />`

Ver **[ICON-COMPONENT.md — sección 5](../components/ICON-COMPONENT.md#5-componente-brandlogo-)** para la implementación completa. Resumen de uso:

```tsx
import { BrandLogo } from '@/components/Icon/BrandLogo'

// Imagotipo T1 Pagos — sobre fondo claro
<BrandLogo name="t1pagos-default" category="t1" width={120} height={32} alt="T1 Pagos" />

// Imagotipo sobre fondo oscuro o rojo
<BrandLogo name="t1pagos-white" category="t1" width={120} height={32} alt="T1 Pagos" />

// Logo de pago en checkout
<BrandLogo name="visa" category="payments" width={40} height={30} alt="Visa" />
<BrandLogo name="mastercard" category="payments" width={40} height={30} alt="Mastercard" />

// Carrier en selector de envío
<BrandLogo name="dhl" category="carriers" width={64} height={40} alt="DHL" />

// Canal de venta — tamaño marketplace
<BrandLogo name="meli-marketplace" category="channels" width={64} height={64} alt="Mercado Libre" />

// Marquee de "Integra con" — grayscale + hover
<BrandLogo name="amazon-iso" category="channels" width={30} height={30} grayscale alt="Amazon" />

// Logo sobre fondo oscuro (sección Ecosistema en landing)
<BrandLogo name="shopify-iso" category="channels" width={30} height={30} onDark alt="Shopify" />
```

### Ruta de archivos en `/public/assets/`

```
/public/assets/logos/
├── t1/                   ← Logos marca T1
├── payments/             ← Procesadores y métodos de pago
├── carriers/             ← Paqueterías
├── channels/             ← Canales de venta (isotipos + marketplace)
├── platforms/            ← ERPs, e-commerce platforms
├── social/               ← Redes sociales
└── marketing/            ← Herramientas de marketing
```

### Regla de uso sobre fondos

| Fondo del contenedor | Prop a usar | Resultado |
|---------------------|-------------|-----------|
| Blanco / Claro | (ninguna) | Logo en colores propios |
| Oscuro / Brand red | `onDark` | `brightness-0 invert` — logo en blanco |
| Marquee / inactivo | `grayscale` | `grayscale opacity-40`, hover activa color |

---

## 11. Proceso de actualización

### Agregar un nuevo logo de tercero

1. Obtener el SVG oficial del proveedor (nunca recrear).
2. Optimizar con SVGO: `npx svgo logo.svg --output logo.svg`
3. Verificar que los colores originales se preserven (no convertir a currentColor).
4. Guardar en la subcarpeta correcta de `/public/assets/logos/`.
5. Documentar en este archivo y en `assets/ICONOGRAPHY.md`.

### Actualizar un logo T1

Cambios en identidad de marca T1 deben coordinarse con el equipo de diseño. El proceso es:
1. Exportar nuevas variantes desde Figma (artboard `Icons-logos`, frame `t1{plataforma}-imagotipo`).
2. Reemplazar los SVGs en `/public/assets/logos/t1/`.
3. Verificar que todas las instancias en el producto usen el componente `<BrandLogo />` — no SVGs embebidos hardcodeados.
4. Actualizar versión en `CHANGELOG.md`.

---

## Referencias cruzadas

- **[assets/ICONOGRAPHY.md](./ICONOGRAPHY.md)** — Catálogo completo incluyendo íconos del sistema, con naming conventions y reglas de uso visual.
- **[components/ICON-COMPONENT.md](../components/ICON-COMPONENT.md)** — Implementación de `<BrandLogo />` y `<Flag />` en código.
- **[foundation/COLORS.md](../foundation/COLORS.md)** — Tokens de color del ecosistema T1 (brand red `#DB3B2B`, paleta completa).
- **[patterns/LANDING.md](../platforms/LANDING.md)** / **[LANDING_new.md]** — Marquees de logos, sección Ecosistema y reglas de uso en landing pages.
