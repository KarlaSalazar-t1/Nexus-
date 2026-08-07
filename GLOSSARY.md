# Glosario — Ecosistema T1

Referencia transversal de terminología usada en el ecosistema T1 y en e-commerce para el mercado mexicano. Este documento es para **todas las áreas** del equipo — si un término aparece en cualquier otro archivo de este repositorio, debería estar definido aquí.

> **Convención:** Cuando un término en inglés se usa tal cual en la plataforma (sin traducir), aparece marcado como *EN*. Cuando existe confusión frecuente entre español e inglés, se incluye la traducción.

---

## Productos del Ecosistema T1

| Término | Definición |
|---|---|
| **T1 Tienda** | Producto para creación y gestión de tiendas en línea. Permite a los comerciantes configurar su catálogo, personalizar su tienda y gestionar ventas. |
| **T1 Envíos** | Producto de gestión logística. Conecta con múltiples paqueterías nacionales e internacionales para cotizar, generar guías y rastrear envíos. |
| **T1 Pagos** | Producto de procesamiento de pagos. Integra múltiples métodos de pago (tarjetas, SPEI, OXXO, etc.), facturación y gestión financiera. |
| **T1 Score** | Producto de analytics y métricas. Proporciona dashboards con indicadores de rendimiento del negocio en tiempo real. |
| **T1 Marketing** | Producto de campañas y canales de venta. Herramientas para gestionar presencia en marketplaces, redes sociales y campañas publicitarias. |
| **T1 POS** | Marca del producto de punto de venta. Se usa en títulos, CTAs de producto, navegación de productos y logotipos. Su categoría descriptiva es "punto de venta". |
| **T1 Cuenta** | Cuenta única que da acceso a todos los productos del ecosistema con un solo registro. |
| **NEXUS** | Nombre del sistema de diseño del ecosistema T1. La versión actual es V2.0. Define tokens, componentes, patrones y reglas visuales para todos los productos. |
| **Ecosistema T1** | El conjunto completo de productos T1 que funcionan de forma integrada. Un comerciante puede usar uno o varios productos según sus necesidades. |

---

## Terminología de Negocio (E-commerce MX)

### Comercio y ventas

| Término | Definición | Nota |
|---|---|---|
| **Negocio** | La entidad a la que se dirige todo el copy de T1. El sistema nombra al **negocio** y a la **tienda**, nunca a la persona. Se escribe en segunda persona: `tu negocio`, `tu tienda`, `tus pedidos`. | Evitar `seller`, `merchant`, `comerciante`, `vendedor` y `usuario` |
| **Tienda** | Unidad operativa de venta que pertenece a un negocio. Un negocio puede tener más de una tienda. | No confundir con `sucursal` (ubicación física de inventario) |
| **Perfil de cliente** | La cuenta del comprador final en T1 Tienda: seguimiento de pedidos, métodos de pago, direcciones y datos de facturación. Forma canónica del término. | Evitar `storefront` (anglicismo) |
| **Listado de productos** | Conjunto completo de productos que un comerciante tiene registrados en la plataforma. Incluye productos, variantes, precios e inventario. | No confundir con "catálogo" |
| **Catálogo** | Agrupación específica de productos creada por el comerciante para un propósito particular: carruseles, páginas temáticas, colecciones destacadas, etc. Un comerciante puede tener múltiples catálogos a partir de su listado de productos. | |
| **SKU** | *Stock Keeping Unit.* Código único que identifica una variante específica de producto (ej: "Playera Roja Talla M"). | *EN* — Siempre se usa en inglés |
| **Variante** | Versión específica de un producto diferenciada por atributos como talla, color o material. Un producto puede tener múltiples variantes, cada una con su propio SKU. | |
| **Inventario** | Cantidad disponible de cada SKU. El sistema puede manejar inventario por ubicación (almacén, tienda física). | |
| **Pedido** | Solicitud de compra realizada por un cliente. Contiene productos, montos, datos de envío y estado de fulfillment. | *Order* en inglés — no confundir con "orden" (que en MX se usa coloquialmente pero "pedido" es el término formal en la plataforma) |
| **Checkout** | Proceso de compra desde el carrito hasta la confirmación de pago. Incluye datos de envío, selección de método de pago y confirmación. | *EN* — Se usa en inglés en la plataforma |
| **Carrito** | Conjunto temporal de productos que un comprador ha seleccionado antes de iniciar el checkout. | *Cart* en inglés |
| **Fulfillment** | Servicio integral 360° que incluye almacenamiento de productos, pick & pack y envío de pedidos. En T1, fulfillment se refiere específicamente a este servicio completo, no solo al proceso de envío. | *EN* — Se usa en inglés en la plataforma |
| **Canal de venta** | Plataforma donde un comerciante publica y vende sus productos: tienda propia, Amazon, MercadoLibre, Claroshop, TikTok Shop, etc. | *Sales channel* en inglés |
| **Marketplace** | Plataforma de terceros donde múltiples vendedores ofrecen productos (ej: Amazon, MercadoLibre, Liverpool). T1 permite conectar y sincronizar inventario con estos canales. | *EN* — Se usa en inglés |
| **Punto de venta** | Categoría descriptiva de T1 POS, análoga a "tienda en línea" frente a T1 Tienda. Se usa en textos explicativos, breadcrumbs y navegación de footer, y cuando el lector aún no sabe qué es T1 POS. | Las dos formas conviven; lo que las separa es el rol, no la preferencia |
| **Estatus del servicio** | Página pública de disponibilidad de la plataforma. Forma canónica del label. | Evitar `página de estatus`, `estado de la plataforma` |

### Pagos y finanzas

| Término | Definición | Nota |
|---|---|---|
| **TPV** | *Terminal Punto de Venta.* Dispositivo físico o virtual para procesar pagos con tarjeta. En T1, se refiere principalmente al procesamiento virtual. | |
| **SPEI** | *Sistema de Pagos Electrónicos Interbancarios.* Sistema de transferencias bancarias en tiempo real del Banco de México. Método de pago muy común en MX. | |
| **CLABE** | *Clave Bancaria Estandarizada.* Número de 18 dígitos que identifica una cuenta bancaria en México. Se usa para transferencias SPEI. | |
| **Reclamación** | Solicitud de un tarjetahabiente a su banco para que le devuelvan un cobro. Término único en todas las superficies de T1, porque es el que usa la interfaz de T1 Pagos. El negocio debe demostrar que la transacción fue legítima. | Evitar `contracargo` (salvo en metadata pública), `chargeback`, `disputa`, `CB` |
| **Devolución** | Entrega física del producto por parte del comprador, con el reembolso correspondiente. **No es lo mismo que una reclamación**: la reclamación es bancaria, la devolución es logística. | *Return* en inglés |
| **Dispersión** | Proceso de transferir los fondos cobrados a la cuenta bancaria del comerciante, descontando comisiones. | *Payout* en inglés — en MX se usa "dispersión" formalmente |
| **Pasarela de pago** | Servicio que procesa transacciones con tarjeta entre el comprador, el banco emisor y el banco del comerciante. Ejemplos: Conekta, Stripe, OpenPay. | *Payment gateway* en inglés |
| **Conciliación** | Proceso de verificar que los montos cobrados, las comisiones y los depósitos al comerciante cuadren correctamente. | *Reconciliation* en inglés |
| **Tasa de aprobación** | Porcentaje de transacciones con tarjeta que son aprobadas exitosamente por el banco emisor. | *Approval rate* en inglés |

### Logística y envíos

| Término | Definición | Nota |
|---|---|---|
| **Guía** | Documento/código de rastreo que identifica un envío ante la paquetería. Contiene número de tracking, origen, destino y servicio. | *Shipping label* en inglés — en MX siempre se dice "guía" |
| **Paquetería** | Empresa de transporte y entrega de paquetes (ej: DHL, FedEx, Estafeta, Redpack, 99 Minutos). | *Carrier* en inglés |
| **Cotización** | Estimación del costo de envío según peso, dimensiones, origen, destino y servicio seleccionado. | *Shipping rate/quote* en inglés |
| **Última milla** | Tramo final de entrega desde el centro de distribución hasta la puerta del cliente. Es la parte más costosa y compleja de la logística. | *Last mile* en inglés |
| **Recolección** | Servicio donde la paquetería recoge los paquetes en la ubicación del comerciante en lugar de que este los lleve a una sucursal. | *Pickup* en inglés |
| **Tracking** | Seguimiento en tiempo real del estado de un envío desde su origen hasta la entrega. | *EN* — Se usa en inglés en la plataforma |

### Analytics y métricas

| Término | Definición | Nota |
|---|---|---|
| **KPI** | *Key Performance Indicator.* Métrica clave que mide el rendimiento de un aspecto del negocio (ej: tasa de conversión, ticket promedio, pedidos por día). | *EN* — Siempre se usa en inglés |
| **Ticket promedio** | Monto promedio de cada pedido. Se calcula dividiendo el ingreso total entre el número de pedidos. | *AOV (Average Order Value)* en inglés |
| **Tasa de conversión** | Porcentaje de visitantes que completan una compra respecto al total de visitantes de la tienda. | *Conversion rate* en inglés |
| **GMV** | *Gross Merchandise Value.* Valor total de mercancía vendida en un período, antes de descontar devoluciones y comisiones. | *EN* — Siempre se usa en inglés |
| **Churn** | Tasa de abandono. Porcentaje de comerciantes que dejan de usar la plataforma en un período determinado. | *EN* — Se usa en inglés internamente |
| **MRR** | *Monthly Recurring Revenue.* Ingreso recurrente mensual por suscripciones activas. | *EN* — Siempre se usa en inglés |

---

## Terminología Técnica

### Arquitectura y desarrollo

| Término | Definición |
|---|---|
| **App Router** | Sistema de routing de Next.js 14+ basado en el filesystem. Usa carpetas dentro de `app/` para definir rutas. Es el estándar obligatorio en T1. |
| **Tailwind v4** | Versión del framework CSS utilizado en T1. A diferencia de v3, la configuración se hace en `globals.css` con `@theme inline` en lugar de `tailwind.config.js`. |
| **Token** | Valor de diseño reutilizable (color, tamaño, spacing, shadow) definido como variable. Los tokens son la base del sistema de diseño y se documentan en `foundation/`. |
| **Token semántico** | Token que describe su *función* en lugar de su valor visual (ej: `color-primary` en vez de `red-500`). Permite que el mismo componente se adapte a diferentes contextos. Ver `foundation/THEMES.md`. |
| **Componente** | Pieza de UI reutilizable con props, estados y variantes definidas. Clasificados en atoms, molecules y organisms según su complejidad. |
| **Atom** | Componente mínimo e indivisible: botón, input, badge, avatar, loader. No contiene otros componentes dentro. |
| **Molecule** | Componente compuesto por varios atoms: modal, tabs, timeline, upload zone. Tiene lógica de interacción propia. |
| **Organism** | Componente complejo que combina molecules y atoms para formar una sección completa de la interfaz: sidebar, header, footer, formulario compuesto. |
| **Breakpoint** | Punto de quiebre en el viewport donde el layout cambia su comportamiento. En T1: mobile (360px), tablet (768px), desktop (1920px). |
| **Skeleton** | Placeholder visual que simula la estructura del contenido mientras carga. Usa formas grises animadas que replican el layout final. |

### Patrones y estados

| Término | Definición |
|---|---|
| **Empty state** | Estado de una vista cuando no hay datos que mostrar. Incluye ilustración, mensaje de ayuda y CTA para guiar al usuario. Documentado en `patterns/EMPTY-STATES.md`. |
| **Loading state** | Estado visual durante la carga de datos. Puede ser spinner, skeleton o barra de progreso según el contexto. |
| **Error state** | Estado que comunica un problema al usuario. Puede ser inline (en el campo), toast (notificación temporal) o modal (requiere acción). |
| **Toast** | Notificación temporal que aparece brevemente en pantalla para confirmar una acción o reportar un error leve. Desaparece automáticamente. |
| **CRUD** | *Create, Read, Update, Delete.* Las cuatro operaciones básicas sobre datos. La mayoría de las vistas del dashboard siguen flujos CRUD. |
| **Wizard** | Flujo multi-paso guiado donde el usuario avanza secuencialmente (ej: onboarding, configuración de pagos). Cada paso valida antes de continuar. |
| **Master-detail** | Patrón de layout donde una lista (master) a la izquierda controla el contenido detallado (detail) a la derecha. Común en vistas de pedidos y productos. |
| **Drawer** | Panel lateral que se desliza desde el borde de la pantalla. En mobile, reemplaza al sidebar fijo del dashboard. |

### Design system

| Término | Definición |
|---|---|
| **Landing** | Página pública orientada a conversión (marketing, producto, pricing). Usa tipografía Sora+Inter, contenedor 1018px y border-radius 24px. Ver `platforms/LANDING.md`. |
| **Dashboard** | Interfaz administrativa interna del producto. Usa tipografía Manrope, contenedor 1600px y sidebar de 284px. Ver `platforms/DASHBOARD.md`. |
| **Brand Red** | Color primario de T1 (`#DB3B2B` en dashboard, `#E26153` en landing). Se usa en CTAs, acentos y elementos de marca. |
| **Oxford** | Color de texto principal (`#4C4C4C`). Nombre interno para el gris oscuro usado en cuerpo de texto en todo el ecosistema. |
| **Acento rojo** | Patrón tipográfico donde una o dos palabras clave de un título se colorean en Brand Red para crear jerarquía visual. |
| **Glass effect** | Efecto visual de transparencia con blur (`bg-white/90 backdrop-blur-md`). Usado en el header fijo de landing pages. |
| **References** | Versiones condensadas de la documentación del design system, optimizadas para el context window de Claude. Viven en `workflows/references/`. |

---

## Abreviaturas

| Abreviatura | Significado |
|---|---|
| **CTA** | *Call to Action.* Botón o elemento que invita al usuario a realizar una acción específica. |
| **UX** | *User Experience.* Experiencia del usuario al interactuar con el producto. |
| **UI** | *User Interface.* La interfaz visual con la que el usuario interactúa. |
| **A11Y** | Abreviatura de *accessibility* (a + 11 letras + y). Prácticas para hacer la interfaz usable por personas con discapacidades. |
| **QA** | *Quality Assurance.* Proceso de verificación de calidad antes de entregar o publicar. |
| **PR** | *Pull Request.* Solicitud de revisión de código antes de fusionar cambios en el repositorio. |
| **MX** | México. Usado como sufijo para indicar contexto del mercado mexicano. |
| **SVG** | *Scalable Vector Graphics.* Formato de imagen vectorial preferido para íconos y logos en T1. |
| **API** | *Application Programming Interface.* Interfaz para comunicación entre sistemas. |
| **SSR** | *Server-Side Rendering.* Renderizado en el servidor, habilitado por defecto en Next.js App Router. |
| **CSR** | *Client-Side Rendering.* Renderizado en el navegador. En T1 se usa con la directiva `"use client"` en componentes interactivos. |

---

## Convenciones de Nombres en la Plataforma

Estas son las convenciones usadas en la UI visible para el usuario final:

| Contexto | Convención | Ejemplo |
|---|---|---|
| **Nombres de producto** | Prefijo "T1" + espacio + nombre con inicial mayúscula | T1 Tienda, T1 Envíos, T1 Pagos, T1 Score, T1 POS |
| **Acciones principales** | Verbo en infinitivo | "Crear envío", "Agregar producto", "Configurar pagos" |
| **Estados de pedido** | Participio o sustantivo descriptivo | "Pendiente", "En tránsito", "Entregado", "Cancelado" |
| **Moneda** | Formato MXN con símbolo $ y separador de miles con coma | $1,250.00 MXN |
| **Fechas** | Formato relativo cuando aplica, descriptivo corto para el año en curso, con año solo si es diferente al actual | "Hoy", "Ayer", "12 de jun", "12 de jun 2023" |
| **Horas** | Formato 24 horas con sufijo "hrs" | 17:34 hrs |
| **Porcentajes** | Número + símbolo % sin espacio | 3.6%, 98% |

---

*Este glosario es un documento vivo. Si encuentras un término usado en el ecosistema T1 que no está aquí, proponlo en Slack para que se agregue.*
