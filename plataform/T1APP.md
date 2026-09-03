# T1app — Flujos y pantallas (NEXUS V2.0)

> ⚠️ **Este no es el punto de entrada.** Para diseñar a fidelidad 90-100% sin necesitar el detalle completo, empieza por [`APP.md`](./APP.md) (fundamentos: tipografía, color, spacing, radios, botones) y [`../patterns/APP-FLOWS.md`](../patterns/APP-FLOWS.md) (mapas de flujo y patrones, nivel de implementación). **Este archivo es la referencia profunda**: hallazgos de auditoría, drift de tokens y trazabilidad pantalla-por-pantalla a Figma — útil para investigar un caso puntual, no para arrancar un diseño nuevo.

> Documento **único** que concentra todos los flujos y pantallas de la app **móvil nativa** de T1. Se separa **internamente por flujo** (no un archivo por flujo). Los fundamentos de plataforma (tipografía, color, spacing, radios, botones) viven en [APP.md](./APP.md) y se referencian aquí sin duplicar.

**Última actualización:** Junio 2026 · **Fuente de verdad:** Figma — `T1-App---ESP` (`viFhO18oodfFqrvyDznrA9`) · **Plataforma:** App (Inter) · **Owner:** Karla Salazar — Head of UX/UI

---

## Índice de flujos

| # | Flujo | Sección Figma | Estado |
|---|---|---|---|
| 1 | Login / Signup / Onboarding | `107:22340` | ✅ Documentado |
| 2 | Home — Pantalla principal | `1532:69077` | ✅ Documentado (7 variantes) |
| 3 | Crear tienda (con IA / Nova) | `590:24176` | ✅ Documentado |
| 4 | Agregar producto (manual / con IA) | `601:26477` · `601:26478` | ✅ Documentado |
| 5 | Conectar canales de venta (Shein) | `171:16434` | ✅ Documentado |
| 6 | Agregar dirección de origen | `590:22183` | ✅ Documentado |
| 7 | Configurar tarifas de envío | `602:31005` | ✅ Documentado |
| 8 | Activar T1 pagos | `602:31723` | ✅ Documentado |
| 9 | Nombre de la tienda (sugerencias IA) | `601:26479` | ✅ Documentado |
| 10 | Dominio personalizado (paywall de planes) | `601:27991` | ✅ Documentado |
| 11 | Conectar redes sociales | `601:28233` | ✅ Documentado |
| 12 | Configurar políticas de la tienda | `601:30287` | ✅ Documentado |
| 13 | Pedidos (Orders) — lista, filtros, búsqueda, acciones | `290:20528` | ✅ Documentado |
| 14 | **Detalle de pedido** — ciclo completo (10 estados + 5 parciales + 6 sub-flujos) | `290:21918` | ✅ Documentado (62 pantallas) |
| 15 | **Crear pedido** — asistente de 2 pasos (productos → cliente/cobro) | `312:20348` | ✅ Documentado (11 pantallas) |
| 16 | **Carrito abandonado** — listado (KPIs, filtros) + detalle (recuperación) | `4183:109497` | ✅ Documentado (15 pantallas) |
| 17 | **Productos — Listado** (inicio del dominio de Productos) | `320:23825` | ✅ Documentado (11 pantallas) |
| 18 | **Agregar producto — Paso 1** (sin variantes) | `366:16829` | ✅ Documentado (form + sheet + ayuda) |
| 18 | **Agregar producto — Paso 2** (Precio e inventario) | `366:16828` | ✅ Documentado (3 bloques + tooltips + sheet) |
| 18 | **Agregar producto — Paso 2 CON variantes** (§PC) | `366:17295` | ✅ Documentado (~19 pantallas: asistente, valores, sheets, validación, modal) |
| 18 | **Agregar producto — Paso 3: SEO** (§PD) | `367:18786` | ✅ Documentado (form SEO + vista previa buscador + escenario SIN PLAN) |
| 18 | **Agregar producto — Paso 4: Canales de venta** (§PE) | `4181:94782` | ✅ Documentado (acordeones de marketplace + mini-form por canal) · **cierra Flujo 18** |
| 18 | **Agregar producto — Confirmación: Producto creado** (§PF) | `4269:110500` | ✅ Documentado (toast "Producto creado" + retorno al listado) |
| 19 | **Agregar producto con IA** (§PG) | `4269:108999` | ✅ Documentado (cámara → IA → formulario prellenado → crear) |
| 20 | **Inventario** (§PH) | `369:29099` | ✅ Documentado (tarjeta de desglose + modificación masiva + no vendible) |
| 21 | **Precios** (§PI) | `375:16216` | ✅ Documentado (modificación masiva % / monto + editor de precios por canal + variantes) |
| 22 | **Catálogo** (§PJ) | `404:28696` | ✅ Documentado (listado + Nuevo/Editar con modos Manual/Avanzado + constructor de reglas + admin canales) |
| 23 | **Sucursales** (§PK) | `421:21749` | ✅ Documentado (listado + alta dirección MX + detalle con métricas + modales de estado/transferencia) |
| 24 | **Envíos** (§EN) | `4298:44178` | ✅ Documentado (listado 4 tabs + tarjeta de envío + menús + timeline de rastreo) |
| 24b | **Crear envío** (§EN.9) | `465:48968` | ✅ Documentado (wizard 3 pasos + agregar dirección + plantillas + SAT IA + resumen + éxito) |
| 24c | **Cotizar** (§EN.10) | `467:14391` | ✅ Documentado (cotizador 8 casos + validación CP + seleccionar paquetería + popups desglose) |
| 24d | **Tracking de guías** (§EN.11) | `470:45363` | ✅ Documentado (listado + filtros activos + detalle de guía + historial de actividad timeline) |
| 24e | **Recolecciones** (§EN.12) | `483:15741` | ✅ Documentado (listado + vacíos + wizard acordeón 4 secciones + éxito con política de ausencia) |
| 25 | **Configuración de envíos** (§CE) | `5183:168845` | ✅ Documentado (menú config + Reglas de prioridad: 4 modos, drag-and-drop, modal selección) |
| 26 | **Control de calidad — Incidencias (base)** (§CC) | `947:60630` | 🟡 En progreso (vacío + listado + estados + KPIs + filtros + detalle; Sobrepesos y flujos de acción pendientes) |
| — | **Loaders y Skeletons** (transversal) | `185:18667` | ✅ Documentado |
| — | **Error de sincronización** (transversal) | `434:40991` | ✅ Documentado |
| — | **Banners y estados globales** (transversal) | `603:34724` | ✅ Documentado |
| — | **Nova AI — Chat** (transversal) | `605:38095` | ✅ Documentado |
| — | **Nova AI — Integración con Pedidos** (transversal) | `435:41638` | ✅ Documentado (3 pantallas) |
| — | **Nova AI — Integración con Productos** (transversal) | `433:25412` | ✅ Documentado (8 pantallas, §N.15) |
| — | **Canales de venta** (§CV, transversal) | `4292:28699` | ✅ Documentado (7 plantillas + acceso) |
| — | **Estados de la sección de alertas** (transversal) | `1399:69897` | ✅ Documentado |
| — | **Estados del checklist de configuración** (transversal) | `1336:103820` | ✅ Documentado |
| — | **Estados del bloque de métricas** (transversal) | `1366:50557` | ✅ Documentado |
| — | *(próximas secciones se agregan abajo)* | | |

---

## Convenciones compartidas (móvil nativo)

Aplican a todos los flujos salvo que una sección indique lo contrario.

- **Mockup base:** `360×780`, con **Status Bar de iPhone** (50px) arriba y **Home Indicator** abajo. Contenido entre ambas *safe areas*.
- **Margen lateral de contenido:** `16px` (ancho útil 328px).
- **Áreas táctiles:** mínimo 44px. Tarjetas de opción 64px, botones 48px, contenedores de ícono 40px.
- **Tipografía:** Inter (ver [APP.md](./APP.md) §2).
- **Botón primario:** `#DB3B2B`, alto 48px, radio 16px; *pressed* `#CC0000`; *disabled* fondo `#F3F3F3` / texto `#9CA3AF`.
- **Teclado:** en captura de texto, contenido y botón se reacomodan sobre el teclado nativo.
- **Navegación:** avance/retroceso entre pasos como transición horizontal; el back conserva las selecciones.
- 🔴 **Haptics:** patrón de retroalimentación háptica (selección, error, éxito) pendiente de definición global.

---

# Flujo 1 — Login / Signup / Onboarding

**Figma:** sección *Login Signup/Onboarding* (`107:22340`) · **Prueba interactiva:** `AppT1OnboardingFlow.jsx`

## 1.1 Resumen

El flujo arranca en un **Splash** y desemboca en una **Welcome de autenticación** con: *Continuar con Google*, *Continuar con correo* (registro/entrada) e *Inicia sesión* (login). A partir de ahí se separan dos caminos:

- **Login:** Welcome → autenticación web (navegador del sistema) → Pantalla principal.
- **Signup:** Welcome → Onboarding (6 pasos) → Loader de configuración → Pantalla principal.

El onboarding **personaliza la configuración inicial** de la cuenta (qué hará el negocio, su etapa, nombre, canales de venta y volumen) para precargar costos, precios y módulos relevantes antes de entrar.

## 1.2 Mapa del flujo

```
Splash
  └─(espera ~2s)→ Welcome (autenticación)
                    ├─ "Inicia sesión"                 → Autenticación web → Pantalla principal
                    └─ "Continuar con Google/correo"   → Onboarding
                                          1. ¿Qué te gustaría hacer con T1?      (multi-select)
                                          2. ¿En qué etapa está tu negocio?      (single-select) ─┐ BIFURCACIÓN
                                          3. ¿Cómo se llama tu negocio?          (input + IA)      │
                                          4a. ¿Dónde te gustaría vender?  ◄── etapa = "Apenas empezando"
                                          4b. ¿Dónde vendes actualmente? ◄── etapa = "Ya está operando"
                                          5. ¿Cuánto vendes al año?              (single-select)
                                          └→ Loader (configurando) → Pantalla principal
```

**Indicador de progreso:** stepper de **6 puntos** en la cabecera de cada paso. Activo en rojo `#CC0000`; resto en gris `#F3F3F3`.

> **Bifurcación (paso 4):** el contenido del paso 4 depende de la respuesta del paso 2. Negocio **nuevo** → se pregunta dónde *querría* vender (intención). Negocio **existente** → se pregunta dónde vende *hoy* (canales actuales). Misma posición en el stepper, distinto copy y propósito.

## 1.3 Pantallas

### Splash (`107:28047`)
Logotipo T1 (98×96) centrado sobre fondo blanco. Sin interacción; transición automática a Welcome tras una breve espera.

### Welcome — autenticación (`1770:85884`)
Pantalla de entrada. Fondo blanco con **degradado rojo al 20%** arriba (`linear-gradient(rgba(219,59,43,0.2) → transparente)`, ~542px). Hexágonos concéntricos redondeados (gris claro) con el **logo T1** y un **círculo** (`Ellipse`, 33px, negro) centrados.
- **Acciones:** dos botones gris `#F8F8F8` / borde `#F3F3F3` (radio 16, alto ~51px): *Continuar con Google* (logo Google) y *Continuar con correo* (`mail-01`). Texto Inter SemiBold 14px `#010B08`.
- **Login:** "¿Ya tienes una cuenta? **Inicia sesión**" (Inter 14px; "Inicia sesión" SemiBold).

### Cabecera de onboarding (común a los pasos)
- **Back:** flecha izquierda 24px en `left:16 top:66`.
- **Stepper:** 6 puntos `16×6` radio full, `gap 3px`, centrados. Activo `#CC0000`, inactivo `#F3F3F3`.
- **Encabezado:** título `T1 SemiBold 24px` + subtítulo `B2 Regular 14px` `#4C4C4C`, **centrados**. `gap 16px`.
- **Footer:** botón primario fijo abajo. En multi-select se antepone el **contador** "*X de N seleccionadas*".

### Paso 1 — ¿Qué te gustaría hacer con T1? (`1523:27148` · seleccionado `1523:27227`)
Multi-select. "Selecciona todas las que apliquen". Tarjetas (ver §1.4.1):
- Crear mi tienda en línea (`store-01`)
- Cotizar y enviar mis paquetes (`shipping-truck-01`)
- Vender en marketplaces — *(Mercado Libre, Amazon, etc.)*
- Cobrar con tarjeta o transferencia (`credit-card-pos`)

**Validación:** *Continuar* se habilita al seleccionar **al menos una** opción.

### Paso 2 — ¿En qué etapa está tu negocio? (`1523:27314`)
Single-select (radio). "Selecciona una de las opciones". Opciones de dos líneas:
- **Apenas estoy empezando** — *Empresa nueva*
- **Ya está operando** — *Empresa existente*

Determina la bifurcación del paso 4.

### Paso 3 — ¿Cómo se llama tu negocio? (`1523:27369` · con sugerencias `1523:27413`)
- Label *Nombre del negocio* (`B2 SemiBold 14px`) + **Input** (radio 20px, alto 55px, borde `#F3F3F3`).
- Botón **Sugerencias de IA** (text-link morado `#7C3AED`, ícono *ai-magic*) → abre el bottom sheet.
- Tras generar, aparecen **chips de sugerencia**: el primero (IA) morado (`#F5EFFF`/`#7C3AED`), el resto gris (`#F8F8F8`/negro), radio 11px.
- Subtítulo "Puedes cambiarlo después."

### Bottom sheet — Cuéntanos sobre tu tienda (`1523:27750` / `1523:27844`)
Hoja inferior sobre fondo atenuado. Header con *cerrar* (`cancel-01`) + título. **Textarea** *Descripción* (~181px) + teclado nativo + botón. Genera la sugerencia de nombre con IA a partir de la descripción.

### Paso 4 — Canales de venta (bifurcado)
- **4a · ¿Dónde te gustaría vender?** (`1523:27468`) — negocio nuevo. Multi-select: Tienda en línea propia · Tienda física · Redes sociales *(Instagram, Facebook)* · Vender en marketplaces *(Mercado Libre, Amazon)* · Aún no lo decido. Contador "*3 de 5 seleccionadas*".
- **4b · ¿Dónde vendes actualmente?** (`1523:27628`) — negocio existente. Mismas 5 opciones, subtítulo "Selecciona todos los canales que usas hoy."

### Paso 5 — ¿Cuánto vendes aproximadamente al año? (`1523:27570`)
Single-select (radio). "Cifras en pesos mexicanos". Opciones: Menos de $250,000 · $250,000 – $1,000,000 · Más de $1,000,000.

### Loader (`1523:27730`)
Spinner rojo (`loader` 44px) + texto de estado **"Recopilando tu información"** (puede ciclar mensajes, p. ej. "Costos y precios (MX)…"). Verifica y precarga la configuración por unos segundos y redirige a la **Pantalla principal**.

## 1.4 Patrones introducidos

### 1.4.1 Tarjeta de opción seleccionable

| Propiedad | Default | Seleccionada |
|---|---|---|
| Fondo | `#FFFFFF` | `#FFF0EF` (Primary/100) |
| Borde | `#F3F3F3` (1px) | `#DB3B2B` (1px) |
| Radio | `16px` | `16px` |
| Alto | `64px` | `64px` |
| Indicador | — | `checkmark-circle-02` (20px, derecha) |

Estructura interna: contenedor de ícono `40×40` `#F8F8F8` radio 12px (ícono 20px) + `gap 12px` + label `B2 SemiBold 14px` negro. Línea secundaria opcional `B3 Medium 12px` `#4C4C4C`.

### 1.4.2 Selección única (radio)
Control circular `16×16` a la izquierda + texto (una o dos líneas). Una sola opción activa a la vez.

### 1.4.3 Stepper de progreso
6 puntos `16×6` radio full, `gap 3px`. Activo `#CC0000`, inactivo `#F3F3F3`. En la bifurcación 4a/4b ocupa la misma posición.

### 1.4.4 Chip de sugerencia
`px 12 · py 8`, radio 11px. Variante IA: `bg #F5EFFF`, texto `#7C3AED SemiBold 12px`. Variante normal: `bg #F8F8F8`, texto negro `Regular 12px`.

### 1.4.5 Input / Textarea
Radio 20px, borde `#F3F3F3`, `padding 16/18px`. Input alto 55px; textarea ~181px. Texto `Inter Regular ~13–14px`.

### 1.4.6 Bottom sheet
Hoja inferior con fondo atenuado, header (título + cerrar), contenido y botón de acción. Acompaña al teclado nativo en captura de texto.

### 1.4.7 Loader de proceso
Spinner 44px + texto de estado. Bloquea la pantalla mientras procesa; transición automática al terminar.

## 1.5 Reglas de interacción y validación

- **Multi-select:** botón deshabilitado hasta seleccionar **≥1**; con selección aparece el contador "*X de N seleccionadas*".
- **Single-select:** elegir una opción deselecciona la anterior y habilita el avance.
- **Bifurcación:** la respuesta del paso 2 enruta a 4a (nuevo) o 4b (existente).
- **IA de nombre:** requiere descripción (bottom sheet) → genera chips; tocar un chip rellena el input.
- **Back:** regresa al paso anterior conservando selecciones.
- **Login:** *Iniciar sesión* delega en autenticación web; al volver, entra a la Pantalla principal.

## 1.6 Consideraciones nativas específicas

- Cada paso cabe en una pantalla (sin scroll largo); el stepper es la única señal de progreso.
- En captura de texto (nombre, descripción) el bottom sheet sube con el teclado.

## 1.7 Tokens detectados (capa componente)

Valores nuevos que aparecen en este flujo y conviene consolidar en el sistema de la App:

| Token / uso | Valor |
|---|---|
| Tarjeta seleccionada — fondo (Primary/100) | `#FFF0EF` |
| Contenedor de ícono — fondo (Greys/900) | `#F8F8F8` |
| Stepper activo (Primary/700) | `#CC0000` |
| Chip IA — fondo / texto | `#F5EFFF` / `#7C3AED` |
| `color/background/chips/green` | `rgba(81,175,112,0.1)` |
| `color/background/state-indicators/success` | `#51AF70` |
| `color/base/black-oxford` | `#4C4C4C` |
| Radio de input / textarea | `20px` |
| Radio de chip | `11px` |
| Sombra de card flotante | `0 3.66px 21.88px rgba(0,0,0,0.1)` |

> El morado `#7C3AED` corresponde a `purple/700` del sistema de la App. Confirmar nomenclatura — en este archivo Figma aparece etiquetado de forma inconsistente.

## 1.8 Pendientes (🔴)

1. Patrón de **haptics** (selección, error, éxito).
2. Estados de **error/validación** del input de nombre.
3. Variantes del **bottom sheet** (vacío vs. con descripción) y estado de carga de la IA.
4. Texto/estados del **Loader** (lista de pasos que muestra).
5. Consolidar los tokens de §1.7 en el sistema de la App.

## 1.10 Referencias

- Figma — sección *Login Signup/Onboarding* (`107:22340`): Splash `107:28047` · Welcome `1523:24251` · Onboarding `1523:27148/27314/27369/27413/27468/27628/27570` · Bottom sheet `1523:27750` · Loader `1523:27730`
- [APP.md](./APP.md) — fundamentos de la plataforma App
- Prueba interactiva: `AppT1OnboardingFlow.jsx`

---

# Home — Pantalla principal

> Pantalla principal de la App tras autenticarse. Es **una sola plantilla** con **variantes por tipo de usuario y estado**. La anatomía y los componentes son comunes; lo que cambia es el **contenido de las tarjetas y los datos**.

**Figma:** sección *Home* (`1532:69077`). Variantes: Envíos `1990:79652` · Pagos `1532:67566` · Tienda/premium `1532:67782` · Tienda sin premium `1683:52896` · All services `1532:68546` · Sin onboarding `1683:54299`.

## H.1 Anatomía

Pantalla de **360px** de ancho, scroll vertical, fondo `#F8F8F8`. De arriba a abajo:

1. **Status bar** (iPhone, 54px).
2. **Top bar / header** fijo (116px, borde inferior `#F3F3F3`).
3. **Configurar cuenta** — tarjetas de setup en carril horizontal *(o banner "Personaliza tu experiencia" en el estado sin onboarding)*.
4. **Métricas** — tarjetas de métrica en carril horizontal + botón "Ver reporte detallado".
5. **Acciones rápidas** — 3 tarjetas.
6. **Nova Insights** — tarjetas de insight en carril horizontal.
7. **Promo (cross-sell)** — card oscura *(ausente cuando el usuario ya usa todos los servicios)*.
8. **Tab bar** inferior (86px) con **FAB "+"**.

Cada bloque (3–7) es una sección blanca con: header (ícono 20px + título `Inter Medium 14px` negro) + control opcional a la derecha, y contenido con `gap 8px`. Padding de sección: `left 16 · top 20`.

## H.2 Variantes

Qué dispara cada variante y en qué se diferencia (detalle de datos en §H.4):

| Variante | Setup cards | Métricas (primeras) | Acciones rápidas | Promo |
|---|---|---|---|---|
| **Envíos** | Recarga saldo · Dirección origen · Plantilla envío · Notif. rastreo | Envíos creados, En tránsito, Entregados, Incidencias, Costo, Saldo | Resumen semanal · Cotizar envío · Rastrear envío | Carrusel: T1pagos / T1tienda |
| **Pagos** | Info fiscal · Cuenta bancaria · Link de pago · Notif. pago | Pagos procesados, Transacciones, Dispersión pendiente, Última dispersión, Links activos | Resumen semanal · Ver transacciones · Ver dispersiones | T1tienda |
| **Tienda / premium** | Primer producto · Métodos de pago | Ventas totales, Pedidos … | Preparar pedidos · Ver pedido · Editar tienda | T1 Payments (Premium) |
| **Tienda sin premium** | **Crear tu tienda con IA** (badge IA) · Primer producto | Ventas totales, Pedidos … | Preparar pedidos · Ver pedido · Editar tienda | T1 Payments (Premium) |
| **Seller sin tienda** | **Tarjeta destacada "Crea tu tienda con IA"** (badge premium) + carril largo (8 tareas) | Ventas totales, Pedidos, Ticket promedio, Conversión, Productos vendidos | Preparar pedidos · Ver pedido · Editar tienda | T1pagos (Premium) |
| **All services** | Primer producto · Métodos de pago | Ventas totales, Pedidos … | Resumen semanal · Cotizar envío · Rastrear envío | **Ninguna** (sin cross-sell) |
| **Sin onboarding** | **Banner "Personaliza tu experiencia"** (reemplaza el carril de setup) | Envíos creados, En tránsito (conteos) | Resumen semanal · Cotizar envío · Rastrear envío | Carrusel: T1pagos |

> **Reglas de variante:** el contenido se deriva del producto principal del usuario; la promo es cross-sell del **siguiente** producto a adoptar y **desaparece** cuando ya usa todo (*All services*); sin datos de onboarding se muestra el banner de encuesta en lugar del setup.

## H.3 Componentes (componente por componente)

### H.3.1 Header / top bar
Barra fija de 116px, fondo blanco, borde inferior `#F3F3F3`. Contenido alineado abajo (`bottom 15`), ancho 328:
- **Izquierda:** selector de tienda (§H.3.2).
- **Derecha:** campana de notificaciones (`notification-02`, 24px) + avatar del usuario (32px, circular), `gap 16px`.

### H.3.2 Selector de tienda
Chip `bg #F8F8F8`, radio 10, `padding 4`, `gap 4`: avatar de iniciales (`24px`, radio 6, fondo de color — ej. `#51AF70` "EC") + nombre (`Inter Medium 12px` negro) + chevron abajo (16px). Abre el cambio de tienda.

### H.3.3 Tarjeta de setup ("Essential Setup")
Tarjeta `160px`, `bg white`, borde `#F3F3F3`, radio **12**, `padding 12/15`, `gap 13`:
- Contenedor de ícono: `40px`, `bg #F8F8F8`, radio full, ícono 20px.
- Título: `Inter Medium 16px` negro (hasta 2 líneas).
- Botón (32px, radio **8**): **rojo** `#DB3B2B`/texto blanco para tareas prioritarias; **gris** `#F8F8F8`/borde `#F3F3F3`/texto negro para secundarias.
- **Badge de IA** opcional (sparkle, esquina) para tareas asistidas — ej. *"Crear tu tienda con IA"*.

El header de la sección lleva un **chip de progreso** "X de N completados" (`Inter Bold 12px` `#4C4C4C`, `bg #F8F8F8`, radio 6).

### H.3.3c Comportamiento al completar una tarea (pantalla de éxito)
Al completar una tarea de setup, el flujo regresa al **Home completo** — no a una versión compacta. La pantalla de éxito conserva todas las secciones del Home: setup → métricas + **"Ver reporte detallado"** → **Acciones rápidas** → **Nova Insights** → promo → **tab bar**, más la **animación de confeti** como única señal universal de éxito (**no** hay banner verde de confirmación).

El estado de la **tarjeta completada varía por flujo** (inconsistencia a resolver):

| Flujo | Comportamiento de la tarjeta al completar |
|---|---|
| Agregar dirección de origen (F6) | **Desaparece** de la lista (las demás suben) |
| Agregar producto (F4) | **Se mueve al final** de la lista |
| Conectar canal (F5) | Botón → **tag "Conectado"** y **se mueve al final** |
| Configurar tarifas de envío (F7) | **Se queda** igual (el mock no la cambia) |
| Activar T1 pagos (F8) | **Se queda** igual (aunque la anotación dice "mover al final") |

> 🔴 **Definir la regla canónica** de este comportamiento — hoy hay 4 variantes distintas entre flujos. El confeti y el Home completo (con Nova Insights) sí son consistentes.

### H.3.3b Tarjeta destacada — Crear tienda (con IA)
Variante **full-width** de la tarjeta de setup que encabeza la sección cuando el usuario aún no tiene tienda (*Seller sin tienda*). Card gris (`bg #F8F8F8`, radio 22 → contenedor interno radio 12, `padding 16`):
- Fila: contenedor de ícono blanco (40px, `store-add`) + título "Crea tu tienda con IA" (`Inter Medium 16px`) + **badge premium**: cuadro 24px, radio 7, `bg #FFEEC9`, ícono **`menu/crown`** (corona, 18px).
- Botón rojo full-width "Create store" con ícono `ai-magic`.

> 🔴 El ícono **`menu/crown`** aparece aquí — exportarlo de Figma a `icons.ts` (es el último gap pendiente de Components).

### H.3.4 Banner "Personaliza tu experiencia" (estado sin onboarding)
Reemplaza el carril de setup. Título "Personaliza tu experiencia" + dos botones: **Después** (secundario) y **Iniciar encuesta →** (primario rojo).

### H.3.5 Tarjeta de métrica
Tarjeta `176×92`, `bg white`, borde `#F3F3F3`, radio 12, `padding 11/15`:
- **Label:** `Inter Medium 12px` `#4C4C4C`.
- **Valor:** `Inter SemiBold 24px` negro (`T1`), tracking −2%. Formato conteo (`234`) o dinero (`$55K`).
- **Delta (opcional):** chip `Inter SemiBold 12px` + flecha 16px (`auto-conversations`, espejada según dirección). Color **semántico** (ver §H.4): verde `#4FC153` (Green/300) o `#16A34A` (Green/200), rojo `#DB3B2B`.
- **Ícono de categoría:** 20px, arriba-derecha.

Header de sección con filtro **"Hoy"** (ícono `filter-mail` 16px + `Inter Medium 12px` `#4C4C4C`). Debajo del carril: botón **"Ver reporte detallado →"** (rojo, 40px, radio 12, `Inter SemiBold 14px` + flecha).

### H.3.6 Tarjeta de acción rápida
Tarjeta `104×100`, `bg white`, borde `#F3F3F3`, radio 12: ícono 20px + label (`Inter Medium 12px` negro, centrado). **3 por variante** (la 1ª suele ser "Ver resumen semanal", común). Header de sección con ícono `customize` a la derecha.

### H.3.7 Tarjeta de insight (Nova Insights)
Tarjeta `bg white`, borde `#F3F3F3`, radio **16**, `padding 16/12`, `gap 8`: fila superior (ícono 24px izquierda + chevron-right 24px derecha) + texto (`Inter Regular 14px` negro). Carril horizontal de 4. **Contenido compartido** entre variantes (costo promedio, SLA DHL, hito de pedidos, retrasos).

### H.3.8 Card promo (cross-sell)
Card oscura `bg #1F2937`, radio 13.32, `328×212`, con elipse + ilustración decorativa:
- **Eyebrow:** `Inter Regular 12px` `rgba(255,255,255,.6)` — ej. "Siguiente paso recomendado".
- **Título:** `Inter SemiBold 24px` blanco.
- **Botón:** blanco, 40px, radio 12, borde `#F3F3F3`, texto negro + flecha.
- Puede ser **carrusel** (2 slides + dots) o card única. **Se omite** cuando el usuario usa todos los servicios.

### H.3.9 Tab bar
Barra inferior (86px): nav tipo **píldora** (`bg white`, borde `#F3F3F3`, radio 64, `260×56`, sombra `0 4 10 rgba(0,0,0,.05)`) con 5 íconos de 48px (radio full): **home** (activo, `bg #FFF0EF`), orders, product, shipping, more-horizontal. + **FAB** (§H.3.10). Cierra con el **iPhone indicator** (`#C3C3C3`).

### H.3.10 FAB + menú de creación rápida
Botón **"+"** (56px, `bg white`, borde `#F3F3F3`, radio 72, ícono `add-01` 24px). Al tocarlo despliega un **grid de 6 accesos** (2×3) con badge de ícono + label: **Nuevos envíos · Ver métricas · Agregar dirección · Recargar · Pedidos · Nova IA**.

## H.4 Reglas de datos (métricas)

1. **Conteo sin delta vs monto con delta** — las métricas de **conteo operativo** (Envíos creados, En tránsito, Entregados, Links activos) **no** llevan delta; las **financieras o de calidad** (Costo, Saldo, Pagos, Incidencias) **sí**.
2. **El color del delta es semántico (bueno/malo), NO el signo.** Ej.: *Incidencias −8%* → **verde** (menos incidencias = bueno); *Costo +8%* → **rojo** (más costo = malo).
3. **Formato de valor:** dinero (`$55K`, `$180K`, `$889`) o conteo (`234`, `53`).
4. **Carril scrollable**, no número fijo de métricas (envíos 6, pagos 5, tienda 2+…).

**Datos por variante (referencia de Figma):**

| Métrica | Valor | Delta |
|---|---|---|
| *Envíos* — Envíos creados | 234 | — |
| *Envíos* — En tránsito | 35 | — |
| *Envíos* — Entregados | 154 | — |
| *Envíos* — Incidencias | 5 | −8% (verde `#4FC153`) |
| *Envíos* — Costo de envío | $30 | +8% (rojo `#DB3B2B`) |
| *Envíos* — Saldo disponible | $180K | +12% (verde `#16A34A`) |
| *Pagos* — Pagos procesados | $55K | +8% (verde) |
| *Pagos* — Transacciones | 53 | −3% (rojo) |
| *Pagos* — Dispersión pendiente | $3K | +2% (rojo) |
| *Pagos* — Última dispersión | $889 | +2% (rojo) |
| *Pagos* — Links activos | 30 | — |
| *Tienda* — Ventas totales | $55K | +8% (verde) |
| *Tienda* — Pedidos | 53 | −3% (rojo) |
| *Seller* — Ventas totales | $55K | +8% (verde `#51AF70`) |
| *Seller* — Pedidos | 53 | −3% (rojo) |
| *Seller* — Ticket promedio | $3K | +2% (rojo) |
| *Seller* — Conversión | 45% | +8% (verde `#51AF70`) |
| *Seller* — Productos vendidos | 118 | +8% (verde `#51AF70`) |

## H.5 Pendientes (🔴)

1. Confirmar hex de los **badges del FAB** (en captura se ven rojos; en código aparecían en morado `#7C3AED` a escala reducida).
2. Estados de **carga/vacío** de cada carril (métricas sin datos, sin insights).
3. 🔴 **Dos verdes** para delta positivo: `#4FC153` (Green/300, envíos/pagos) vs `#51AF70` (Green/400, seller/tienda). Definir el token oficial de "tendencia positiva".
4. 🔴 Exportar el ícono **`menu/crown`** (badge premium) a `icons.ts`.

## H.6 Referencias

- Figma — sección *Home* (`1532:69077`): Envíos `1990:79652` · Pagos `1532:67566` · Tienda/premium `1532:67782` · Tienda sin premium `1683:52896` · Seller sin tienda `1990:103034` · All services `1532:68546` · Sin onboarding `1683:54299`
- [APP.md](./APP.md) — fundamentos (Inter, color, spacing, radios)

---

# Flujo 3 — Crear tienda (con IA / Nova)

> Flujo para que un *seller sin tienda* genere su tienda con IA (Nova). Entra desde el botón **Create store** de la tarjeta destacada del Home *Seller sin tienda* (§H.3.3b).

**Figma:** sección *Create Store* (`590:24176`). Anotaciones del flujo: *"User taps on Create Store Button" → "User either writes a prompt or selects a predefined option; once submitted, AI starts creating the store" → "After delay, store will be created" → "Tapping Visit Store opens the web store"*.

## 3.1 Mapa del flujo

```
Home seller sin tienda (1990:103034) ──[Create store]──▶
  Nova AI · "Crea tu tienda en segundos" (1571:24199)
     estados: Default · Typed · Multilínea+teclado · Voz 0:00 · Voz grabando 0:04 · Límite de caracteres
        │  (escribe prompt / elige categoría / dicta por voz) → enviar
        ▼
  Loader "Nova AI" (591:26182) — spinner + status cíclico ("Costos y precios (MX)…")
        │  (delay; la IA genera la tienda)
        ▼
  Preview "Mi tienda" (591:26599) ──[Visit Store]──▶ Storefront web "DenimLux" (591:26746)
        │  (Done, Go to home)
        ▼
  Home con tienda creada + 🎉 confeti (1990:110570)
```

## 3.2 Pantallas

### Input Nova AI — "Crea tu tienda en segundos" (`1571:24199`)
Pantalla de entrada. Fondo blanco con **degradado rojo al 30%** arriba (`linear-gradient(rgba(219,59,43,0.3) → transparente)`, 542px). Back arrow (`majesticons:arrow-up` rotado = flecha izquierda) en (16, 67).
- **Badge Nova AI** (centrado, top 154): `bg rgba(255,255,255,0.4)`, radio 59, `px12 py6`; punto de 12px con **glow morado** (`shadow 0 0 145.7px #b830ff`) + texto "Nova AI" (`Inter Regular 12px`, **`#6537AE`**).
- **Título:** "Crea tu tienda en segundos" — `Inter Medium 24px` `#1F2937`, centrado.
- **Input de prompt** (top 279, 328×119, white, borde `#F3F3F3`, radio 16): placeholder "Pídele a Nova que cree tu tienda…" (`Inter Regular 14px` `#9CA3AF`) + **botón enviar** abajo-derecha (30px, `bg #DB3B2B`, radio 40, ícono `tabler:arrow-up` 16px blanco).
- **Chips de categoría** (top 414, wrap, gap 8): 6 chips white/borde `#F3F3F3`/radio 16/`h40`/`px12 py6` con ícono 16 + label (`Inter Regular 12px`): **Moda** (`shirt-01`), **Deportes** (`american-football`), **Belleza** (`ai-beautify`), **Joyería** (`necklace`), **Electrónica** (`bulb`), **Hogar** (`oven`).

**Estados** (`Group 1321314563`):
- **Default** (`1766:42535`) — placeholder.
- **Typed** (`1766:42675`) — texto escrito.
- **Multilínea + teclado** (`1766:42902`) — input multilínea con teclado iOS.
- **Voz 0:00** (`1766:43518`) — sheet (344×302): timer "0:00" + "Empieza a grabar" + botón de grabar (52px) + drag handle (48×5).
- **Voz grabando 0:04** (`1766:43595`) — sheet con timer "0:04" + **waveform** (líneas verticales de alturas variables) + botón grabar.
- **Límite de caracteres** (`1766:44016`) — prompt largo + highlight de límite + mensaje de aviso (`Messages`) + teclado.

### Loader (`591:26182`)
Top: back arrow + "Nova AI". Centro: **spinner** (`loader` 44px) + **status cíclico** (ej. "Costos y precios (MX)…"). Tras el delay redirige a la preview/tienda.

### Preview "Mi tienda" (`591:26599`, scroll largo `591:26666`)
Vista **in-app** de la tienda recién generada. Header: back + **"Mi tienda"** (centrado) + botón **"Visit Store"** (ghost, texto rojo). Debajo, **selector de página** "Home Page" (dropdown full-width con chevron). **Hero** (foto del catálogo generado). Sección **"Explora nuestras categorías"** con cards de producto (foto + label, ej. "Jeans") en scroll horizontal. **FAB Nova** (orbe morado flotante). **Mensaje informativo** (azul, ícono info): "Store editing is only available on desktop. To customise your store, log in through the web version." Botón inferior **"Done, Go to home"** (rojo). La versión con scroll largo agrega **paginación 1–5**.

### Storefront web "DenimLux" (`591:26746`) — destino de *Visit Store*
Vista de la tienda como la ve el comprador. Header: back **"Regresar"** + línea. Topbar: `menu-02` + **"DENIMLUX"** | `search-01` · `user` · `shopping-basket-01`. **Banner de plan**: "Elige un plan y desbloquea todas las funciones de tu tienda." + botón **"Upgrade Plan"** con ícono **corona** (`menu/crown`). **Hero** (foto). Sección **"Explora nuestras categorías"** con grid de productos. **FAB Nova** + mismo **mensaje informativo** azul.

### Cierre — Home con tienda creada + **confeti** (`1990:110570`)
El flujo cierra volviendo al **Home con la tienda ya creada** con una **lluvia de confeti** (`image 333`, overlay 360×360) celebrando la creación. El contenido del Home es la variante *Seller con tienda* (documentada en §H): setup arranca en "Crea tu primer producto" (ya **sin** la tarjeta destacada de crear tienda); métricas Ventas $55K / Pedidos 53 / Ticket $3K / Conversión 45% / Productos 118; promo Premium. Es decir: la pantalla de Home pertenece a la base (§H); lo propio de este flujo es **el confeti de celebración** sobre ella.

## 3.3 Componentes nuevos (vs. ya documentados)

- **Badge Nova AI** — pill translúcido con punto glow morado + label `#6537AE`. Acento de IA = **morado** (`#6537AE` / glow `#b830ff`).
- **Input de prompt** — caja 328×119, radio 16, con botón enviar circular rojo (30px, radio 40).
- **Chip de categoría** — pill white/borde `#F3F3F3`/radio 16/h40 con ícono 16 + label 12.
- **Sheet de grabación de voz** — timer (`m:ss`) + waveform de líneas + botón grabar 52px + drag handle.
- **FAB Nova (orbe)** — botón circular flotante con degradado morado (asistente Nova) en preview/storefront.
- **Card de producto (storefront)** — foto + label (ej. "Jeans") / nombre + precio en el grid largo.
- **Banner de plan** — copy "Elige un plan…" + botón **"Upgrade Plan"** con ícono corona.
- **Mensaje informativo** — caja azul con ícono info ("Store editing is only available on desktop…").
- **Confeti de celebración** — overlay sobre el Home al cerrar el flujo.

## 3.4 Pendientes (🔴)

1. 🔴 **Token de acento IA (Nova):** definir oficialmente el **morado** (`#6537AE` texto / `#b830ff` glow) en `COLORS.md`/foundation; hoy sólo aparece en este flujo.
2. Definir la **duración** real del status cíclico del loader.
3. Estados de error de la generación IA (timeout, prompt inválido; el límite de caracteres ya está diseñado).

## 3.5 Caso — Crear **otra** tienda (cuando ya existe una)

> Figma: sección *Create Store (When already 1 store is created)* (`615:41280`).

Es el **mismo flujo** que el Flujo 3, con las **mismas pantallas y componentes** (input Nova → loader → preview "Mi tienda" → storefront "DenimLux" → cierre Home + confeti). **No introduce componentes nuevos.** Cambian dos cosas: el **punto de entrada** y el **copy**.

**Punto de entrada — Selector de tiendas.** En vez de la tarjeta destacada "Create store" (Home *seller sin tienda*), aquí se dispara con el **botón "Crear tienda"** desde el **selector de tiendas**, estando ya con ≥1 tienda (anotación: *"El usuario da clic en el botón Crear tienda"*).

El selector se abre desde el **chip de tienda** del header del Home (ej. "EC · Eco Clothing ▾"). Patrón (reconstruido sobre el chip ya documentado en §H.3.1; ⚠️ **pendiente de confirmar contra su nodo de Figma**, no aparece en esta sección):
- Panel desplegable (white, radio ~14, borde `#F3F3F3`, sombra) anclado bajo el chip.
- Encabezado "TUS TIENDAS" (`Inter SemiBold 12px`, `#9CA3AF`).
- **Filas de tienda:** tile de inicial (28px, radio 7, color de marca) + nombre (`Inter Medium 14px`) + ✓ en la activa (`#51AF70`).
- **Fila "Crear tienda"** (CTA): tile rojo claro `#FFF0EF` con ícono `+` + label "Crear tienda" (`Inter SemiBold 14px`, `#DB3B2B`) → entra al flujo de creación (input Nova).

> 🔴 El nodo canónico del selector no está en `615:41280`. Confirmar con Figma: ¿es dropdown anclado o bottom-sheet?, copy del encabezado, orden/estado de las tiendas, y si "Crear tienda" vive aquí o en otro punto.

### Pendientes del caso (🔴)

1. 🔴 **Confirmar el selector de tiendas contra Figma**: el nodo canónico (chip → lista de tiendas + "Crear tienda") no está en esta sección; la documentación actual es una reconstrucción del patrón. Verificar tipo (dropdown vs bottom-sheet) y comportamiento.

### Referencias del caso

- Sección `615:41280`: Input `1995:136549` · Loader `615:41503` · Preview "Mi tienda" `615:41518` / paginación `615:41586` · Storefront "DenimLux" `615:41667` · Cierre Home + confeti `1990:111039`

## 3.6 Referencias

- Figma — sección *Create Store* (`590:24176`): Input `1571:24199` (+ estados `1766:42535/42675/42902/43518/43595/44016`) · Loader `591:26182` · Preview `591:26599` / `591:26666` · Storefront `591:26746` · Home con tienda `1990:110570`
- Figma — sección *Create Store (When already 1 store is created)* (`615:41280`)

---

# Flujo 4 — Agregar producto (manual / con IA)

> Dos variantes que **convergen en el mismo formulario "Crear producto"** y el mismo cierre (Home + confeti). Entra desde la tarjeta de setup **"Crear primer producto"** del Home.
> **Figma:** *Add Product Manually* (`601:26477`) · *Add Product With AI* (`601:26478`).

## 4.1 Mapa de los flujos

```
Home (tarjeta "Crear primer producto")
   │ tap
   ▼
Modal "Crea tu primer producto"  ──[Crear manualmente]──▶ Formulario "Crear producto" (vacío) ─┐
   │                                                                                            │
   └──[Crear con IA]──▶ Cámara vision.ai → Loader/Sparks (IA procesa) → Formulario (pre-llenado)┤
                              │ (error: foto borrosa → tomar otra)                              │
                                                                                                ▼
                                                                          Agregar producto → Home + 🎉 confeti
```

- Anotación: *"When user taps 'Add first product' card we'll show a popup to select the Manual or AI process."* Tocar fuera del popup lo cierra.
- El botón **"Agregar producto"** está **deshabilitado** hasta llenar todos los campos obligatorios.
- Al agregar, la tarjeta "Crear primer producto" **se anima y pasa al final** de la lista de setup.

## 4.2 Modal de selección (`153:41333` / `1532:78390`)
Popup sobre el Home atenuado (`image 337`). Card (328 ancho): ícono `tags` (32px en círculo 64px) + título **"Crea tu primer producto"** + subtítulo "Ya tienes algunos productos, sigue agregando más." + **2 botones** (299×40): **Crear manualmente** (rojo, con ícono `+`) y **Crear con IA** (texto oscuro + ícono sparkle, no morado).

## 4.3 Formulario "Crear producto" (compartido) — `152:40348` (vacío) / `153:40826` (lleno)
Header: back + "Crear producto" + línea. Campos (input `Inactive/Default Input` 328×55, label arriba `Inter Medium`, placeholder `#9CA3AF`):
1. **Nombre del producto** — input.
2. **Descripción del producto** — textarea (112h) + acción **"Mejorar con IA"** (ícono `ai-magic` + texto, acento **morado Nova `#6537AE`**).
3. **Subir imagen** — dropzone (borde sólido, `upload-square-02` 32px en cuadro blanco + "Sube aquí las imágenes de tu producto") + hint "Formato: JPG, PNG, WEBP, HEIC y GIF. Tamaño máximo 20 MB".
4. **Categoría** — select ("Seleccionar" → "Camisas") + chevron down.
5. **Variantes del producto** — toggle (`Control` 36×20, **por defecto activado/verde**) + "Activa esta opción si vendes el mismo producto en diferentes tallas, colores, estilos, etc."
6. *(divisor)* **Inventario y precio** — Unidades disponibles (Ej. 10), Precio base ($), Precio de venta ($).
7. *(divisor)* **Identificadores del producto** — SKU (Ej. POL78912344), Código de barras (EAN, ISBN, UPC, GTIN).
- Footer: **"Agregar producto"** (primario, deshabilitado hasta requeridos) + **"Cancelar"** (secundario, sin borde, 328×48). FAB Nova flotante.

### 4.3.1 Estado de campo — "Mejorar con IA" (`548:48930`)
3 estados: **"Mejorar con IA"** (default, texto oscuro) → al tocar, **borde animado morado** + campo deshabilitado y texto **"Mejorando con IA"** → al terminar, vuelve a normal y debajo dice **"Descripción mejorada con IA"**.

### 4.3.2 Estados del campo "Subir imagen" (`548:48980`)
- **Default** — dropzone.
- **Subiendo** — "Subiendo N archivos" + 4 miniaturas (56×56) + barra de progreso + "18% completado" + botón cancelar (X 32px).
- **Subidos** — lista "Archivos subidos": miniatura 56 + nombre ("Playera 1") + peso ("5 MB") + botón eliminar (X).
- **Error** — banner `Messages` (error) + lista.

## 4.4 Variante con IA — Cámara vision.ai (`601:26478`)
La cámara es **full-bleed 393×852** (más ancha que 360). 
- **Barra superior:** flash (`ion:flash`) + cerrar (`basil:cross-solid` 35) + logo **"vision ai"** (114×25, con espacio, texto blanco) + texto de instrucción ("Toma una buena foto para que podamos identificar y crear tu producto.").
- **Captura (abajo):** botón de captura "Click" (77px) + miniatura de galería (40px).
- **Estados:** 
  - *Default* (`153:41437`/`153:42707`) — apuntando al producto.
  - *Procesando* — **loader** "Costos y precios (MX…" (`153:42803`) y/o animación **Sparks** con ícono IA (`153:42868`).
  - *Resultado* (`153:42812`) — 2 botones: **Crear producto** (morado, ícono sparkle) / **Tomar otra foto**.
  - *Error* (`153:42944`) — banner `Messages`: imagen borrosa → pedir otra foto.
- Anotaciones: *"Cuando el usuario selecciona IA, se abre la cámara"* · *"carga un momento para obtener los detalles"* · *"Create Product → procesa con IA y anima con ícono IA"* · *"la IA llena los campos; el usuario revisa"* · *"Por defecto sólo se agrega 1 imagen (la foto tomada); desde aquí puede agregar más"*.
- El **formulario con IA** (`153:43002`) llega **pre-llenado** y con un banner `Messages` arriba (revisar detalles).

## 4.5 Cierre — Home con producto + **confeti** (`1990:118223` / `1990:118692`)
Vuelve al Home con **confeti** (`image 333`) como única señal de éxito. La tarjeta **"Crear primer producto" se anima y pasa al final** de la lista de setup (puedes seguir agregando productos). **No** hay banner verde de éxito.

## 4.6 Componentes nuevos (vs. ya documentados)
- **Modal de selección** (popup con ícono + título + subtítulo + 2 botones; cierra al tocar fuera).
- **Campo de input con label** (`Inactive/Default Input` 328×55; variante textarea 112h).
- **Acción inline "Mejorar con IA"** (3 estados; borde animado morado).
- **Dropzone de subida** + **estados** (subiendo con barra/%, subidos con lista, error).
- **Fila de archivo subido** (miniatura + nombre + peso + eliminar).
- **Select de categoría** (placeholder + chevron).
- **Toggle "Variantes del producto"**.
- **Cámara vision.ai** (barra superior flash/cerrar/logo, captura, galería) + **Sparks** (animación de procesamiento IA).

## 4.7 Pendientes (🔴)
1. 🔴 **Tokens exactos del formulario** (radio/borde/tipografía de inputs, toggle, dropzone) — heredados de los tokens de input de la App; confirmar contra Figma.
2. Definir **estados de error** de la IA (borrosa, sin producto detectado).

## 4.9 Referencias
- *Add Product Manually* (`601:26477`): Home `1990:109165` · Modal `153:41333` · Form vacío `152:40348` · Form lleno `153:40826` · Home+confeti `1990:118223` · Estados IA-texto `548:48930` · Estados subida `548:48980`
- *Add Product With AI* (`601:26478`): Modal `1532:78390` · Cámara `153:41437`/`153:42707`/`153:42812`/`153:42868` · Loader `153:42803` · Error `153:42944` · Form pre-llenado `153:43002` · Home+confeti `1990:118692`

---

# Flujo 5 — Conectar canales de venta (caso Shein)

> Conectar un canal externo (marketplace o tienda en línea) a T1tienda. Entra desde la tarjeta de setup **"Conectar canal de ventas"** del Home.
> **Figma:** *Connect Sales Channels* (`171:16434`) → subsección *Shein Channel* (`597:43220`).

## 5.1 Mapa del flujo

```
Home (tarjeta "Conectar canal de ventas")
   ▼
Lista de canales (907:63714) — search + Marketplace / Tiendas en línea / Próximamente
   │ tap "Conectar canal" (ej. Shein)
   ▼
Detalle del canal — Shein (269:20513): descripción + video + "¿Cómo me conecto?" (pasos 1–4) + capacidades + banner
   │ "Conectar canal"
   ▼
Modal "Importante" (596:24998) — aviso de importación de datos
   ▼
Auth web Shein (597:25076 / 597:25091) — login fuera de la app
   ▼
¿La cuenta ya está vinculada a otra tienda T1tienda?
   ├─ Sí → Error de autenticación (597:42720)
   └─ No ▼
Sincronización (271:21451) — toggle activar + Pedidos / Productos / Activación masiva / Reglas de inventario
   ▼
Conectado (271:21881) — toggle ON
   │ "Listo, ir al inicio"
   ▼
Home + 🎉 confeti (1990:114826)
```

Anotaciones: *"El usuario da clic en conectar canal de ventas"* · *"User taps any channel card… ej. Shein"* · *"In this step we'll sync all of the things of the Shein account"* · *"La cuenta de Shein quedará conectada y podrás activarla o desactivarla cuando el usuario lo desee"* · *"Once user completes… taps 'Done go to home' → home con animación de éxito; la tarjeta completada se convierte en tag 'Connected' y pasa al final"*.

## 5.2 Lista de canales (`907:63714`)
Header back + **"Conectar canales de ventas"**. **Search** "Buscar canales, tiendas en línea". Tres secciones, cada una grid 2-col de **cards de canal** (logo 56px en tile redondeado de marca + nombre + botón):
- **Marketplace:** Shein · Walmart · Mercado Libre · Tiktok shop · Totalplay · Amazon · Sanborns · Sears → botón **"Conectar canal"** + "Ver todos ⌄".
- **Tiendas en línea:** Shopify · Woocommerce → "Conectar canal".
- **Próximamente:** Wix · Prestashop · Vtex · Magento → botón **"Me interesa →"** (en vez de conectar).

## 5.3 Detalle del canal — Shein (`269:20513`)
Header "Conectar Shein". Logo + nombre + descripción ("…simplifica la gestión de pedidos… **leer más**"). **Video** (card con play). **"¿Cómo me conecto?"** — stepper vertical **1–4** (números rojos + línea):
1. Da clic en "Conectar canal" — saldrás brevemente a la página de Shein.
2. Ingresa tu ID de usuario y contraseña de Shein.
3. Confirma la autorización a la aplicación.
4. ¡Listo! — gestiona tus pedidos y métricas.

Segundo bloque **"¿Cómo me conecto?"** = grid 2×2 de capacidades (Importación de pedidos · Generación de guías · Actualizaciones en tiempo real · Reportes). **Banner** (info naranja): "Importaremos la información de tus pedidos a partir del 1 de enero de 2022." Botón **"Conectar canal"** (rojo).

## 5.4 Modal "Importante" (`596:24998`)
Popup: **"Importante"** + "Recuerda que importaremos la información de pedidos a partir del 1 de enero de 2022… Podrás ver reflejada la información en ~24 horas." + botón.

## 5.5 Auth web Shein (`597:25076` / `597:25091`)
Login **fuera de la app** (web view de Shein; representado con screenshots/bitmaps). El usuario inicia sesión y autoriza.

## 5.6 Error de autenticación (`597:42720`)
Si **la cuenta ya está vinculada a otra tienda T1tienda** → modal (ícono `alert-02`): **"Error de autenticación"** + "Tu cuenta de {sales channel} ya está vinculada a otra tienda de T1tienda." + 2 botones.

## 5.7 Sincronización (`271:21451`) y Conectado (`271:21881`)
Header "Conectar Shein". **Fila de canal:** logo + nombre + **chip de estado** + **toggle** (Control). Tarjetas de acción para **Pedidos** y **Productos** (Sincroniza pedidos · Sincroniza productos · Activación masiva · Reglas de inventario), cada una con el visual **origen → T1**. Botón final **"Listo, ir al inicio"**.

### 5.7.1 Estados de pedidos y productos (sincronización)
Las acciones de sincronización tienen estado, y el canal cambia de inactivo a activo:

| Elemento | Estado inicial (`271:21451`) | Estado conectado (`271:21881`) |
|---|---|---|
| **Canal** | chip **INACTIVO** (gris) + toggle **off** | chip **ACTIVO** (verde) + toggle **on** (verde) |
| **Sincronizar pedidos** | botón "Sincronizar pedidos ⟳" (gris, accionable) | **"Sincronizado"** (verde, confirmación, sin botón) |
| **Sincronizar productos** | botón "Sincronizar productos ⟳" | (sigue **pendiente** en el ejemplo: botón gris) |
| **Activación masiva** | botón "Activar de forma masiva" | **"Activado"** (verde) |
| **Reglas de inventario** | botón "Establecer reglas" | botón **"Actualizar reglas"** (ya configuradas) |

Patrón de estados de cada acción: **Pendiente** (botón gris con ícono de acción) → *Sincronizando…* (transición) → **Hecho** (texto verde "Sincronizado"/"Activado"). Las **Reglas** no tienen estado "verde": cambian de label "Establecer" → "Actualizar". El **chip + toggle** del canal reflejan ACTIVO/INACTIVO de forma independiente a cada acción.

## 5.8 Cierre — Home + confeti (`1990:114826`)
Vuelve al Home con **confeti** como única señal de éxito. La tarjeta "Conectar canal de ventas" cambia su botón por un **tag "Connected"/"Conectado"** y **se mueve al final** de la lista de setup. **No** hay banner verde de éxito.

## 5.9 Componentes nuevos
- **Card de canal** (logo de marca 56px + nombre + botón "Conectar canal" / "Me interesa →").
- **Search bar** de canales.
- **Stepper numerado vertical** (pasos 1–4 con línea conectora).
- **Card de capacidad** (ícono + texto, grid 2×2).
- **Video card** (thumbnail + play).
- **Modal informativo** ("Importante").
- **Fila de canal con chip de estado (INACTIVO/ACTIVO) + toggle**.
- **Card de sincronización** (logo origen → T1 + descripción + botón con ícono de acción).
- **Modal de error de autenticación**.

## 5.10 Pendientes (🔴)
1. 🔴 **Logos de marca** (Shein, Walmart, Mercado Libre, etc.): se recrean como tiles; los reales no se pueden descargar de Figma. Confirmar set y uso.

## 5.11 Referencias
- *Connect Sales Channels* (`171:16434`) → *Shein Channel* (`597:43220`): Home `1990:105745` · Lista `907:63714` · Detalle `269:20513` · Modal Importante `596:24998` · Auth `597:25076`/`597:25091` · Error `597:42720` · Sincronización `271:21451` · Conectado `271:21881` · Home+confeti `1990:114826`

---

# Flujo 6 — Agregar dirección de origen

> Capturar la dirección de origen (sucursal) para envíos. Entra desde la tarjeta de setup **"Agregar dirección de origen"** del Home de **Envíos**.
> **Figma:** *Add Source Address* (`590:22183`).

## 6.1 Mapa del flujo

```
Home Envíos (tarjeta "Agregar dirección de origen")
   │ tap
   ▼
Formulario "Dirección de origen" (590:22348) — 11 campos
   │ "Guardar" (requiere datos completos)   └─ "Descartar" → vuelve al Home
   ▼
Home Envíos + 🎉 confeti (1990:122492) — animación de tarea completada
```

Anotaciones: *"El usuario toca la tarjeta de dirección de origen"* · *"El usuario completa todos los datos"* · *"…toca el botón guardar para guardar la dirección de origen"* · *"Aparecerá una animación de tarea completada con éxito"* · *"Descartar regresa al usuario a la pantalla de inicio"*.

## 6.2 Contexto — Home de Envíos (T1envíos) `1990:121606`
Esta es la **variante de Home para Envíos** (ya listada en §H.2). Detalle:
- **Métricas:** Envíos creados (234) · En tránsito (35) · Entregados (154) · Incidencias (5, −8%) · Costo de envío ($30, +8%) · Saldo disponible ($180K, +12%).
- **Acciones rápidas:** Ver resumen semanal · Cotizar envío · Rastrear envío.
- **Setup:** Hacer primera recarga de saldo · **Agregar dirección de origen** · Crear plantilla de envío · Configurar notificaciones de rastreo.
> Referencia cruzada con §H.2 (variante Envíos).

## 6.3 Formulario "Dirección de origen" (`590:22348` vacío / `590:22400` lleno)
Header back + **"Dirección de origen"**. Campos (input con label arriba, `Inactive/Default Input` 328×55):
1. **Nombre de sucursal** — input.
2. **País** — select con **bandera** + "México" + chevron.
3. **Calle** — input.
4. **Número exterior** — input.
5. **Número interior** — input.
6. **Código postal** — input.
7. **Colonia** — select ("Selecciona una opción" → ej. "Del Valle") + chevron.
8. **Ciudad** — input.
9. **Estado** — input.
10. **Número de teléfono** — input.
11. **Referencias** — textarea (152h).
- Footer: 2 botones (328×48) — **"Guardar"** (primario) + **"Descartar"** (secundario). FAB Nova.

## 6.4 Cierre — Home Envíos + confeti (`1990:122492`)
Guardar → vuelve al Home de Envíos con **confeti** (única animación de "tarea completada"). La tarjeta **"Agregar dirección de origen" simplemente desaparece** de la lista de setup (las demás tarjetas suben para ocupar su lugar). **No** hay estado "Listo"/verde en la tarjeta ni banner de éxito; el contador de "Configurar cuenta" avanza (ej. "2 de 5 completados").

## 6.5 Componentes
- **Campo input con label** (reutiliza §4.3; aquí variante select con **bandera de país** y select de colonia).
- **Botonera Guardar / Descartar**.
- *(reutilizados)* FAB Nova, confeti, tarjeta de setup.

## 6.6 Pendientes (🔴)
1. 🔴 Documentar la **variante Envíos del Home** en §H.
2. Confirmar el asset de la **bandera de país**.

## 6.7 Referencias
- *Add Source Address* (`590:22183`): Home Envíos `1990:121606` · Form vacío `590:22348` · Form lleno `590:22400` · Home+confeti `1990:122492`

---

# Flujo 7 — Configurar tarifas de envío (Review Shipping Rates)

> La app **sugiere tarifas de envío con IA** según la industria; el usuario las acepta y guarda, o las edita en web. Entra desde la tarjeta de setup **"Configurar tarifas de envío"** del Home de Tienda.
> **Figma:** *Review Shipping Rates* (`602:31005`).

## 7.1 Mapa del flujo

```
Home Tienda (tarjeta "Configurar tarifas de envío")
   │ tap  ("User taps on Review Shipping Rates")
   ▼
Pantalla "Tarifas de envío" (681:29701) — sugerencia de IA por industria
   │ "Guardar" (guarda las tarifas)   └─ "Descartar" → vuelve al Home
   ▼
Home Tienda + 🎉 confeti (1990:124696)
```

Anotaciones: *"User taps on 'Review Shipping Rates'"* · *"La app sugerirá las tarifas según la información de la industria usando IA. El usuario puede aceptarlas y guardar para continuar, o editarlas en web."* · *"Guardar guardará las tarifas de envío."* · *"Descartar regresará al usuario al inicio."*

## 7.2 Pantalla "Tarifas de envío" (`681:29701`)
Header back + **"Tarifas de envío"**. 
- **Texto guía:** "Según la información de tu industria, te sugerimos ofrecer a tus clientes".
- **Card de tarifa sugerida** (`681:29782`): chip **"Creado con IA"** (gris, ícono sparkle) + fila con **bandera 🇲🇽** + **"Envío gratis en todo México en compras mayores a $230.00"** + botón **"✎ Editar"** (bordeado, full-width).
- **Footer:** 2 botones (328×48) — **"Guardar"** (rojo) + **"Descartar"** (bordeado). FAB Nova.
- La **edición fina** de las tarifas se hace **en web** (según anotación).

## 7.3 Cierre — Home Tienda + confeti (`1990:124696`)
Guardar → vuelve al Home de Tienda con **confeti**. **Confirmado por captura:** la lista de setup **se mantiene igual** (la tarjeta "Configurar tarifas de envío" sigue presente con su botón "Configurar" y el contador sigue en "2 de 5"); la única señal de éxito es el confeti. *(Comportamiento distinto al de agregar dirección/producto/canal — aquí la tarjeta no desaparece ni cambia de estado.)*

## 7.4 Componentes nuevos
- **Card de tarifa sugerida por IA** (chip + regla con bandera de país + acción de edición).
- *(reutilizados)* input/botones, FAB Nova, confeti, tarjeta de setup, Home de Tienda.

## 7.5 Pendientes (🔴)
1. 🔴 **Inconsistencia de comportamiento**: al completar, esta tarjeta de setup **no cambia** (se mantiene) mientras que en dirección/producto/canal desaparece o se marca. Definir el patrón canónico.

## 7.6 Referencias
- *Review Shipping Rates* (`602:31005`): Home `1990:123758` · Tarifas de envío `681:29701` · Home+confeti `1990:124696`

## 7.7 Validación de tipografía (App) — hallazgo global
Al validar los `font-weight` reales contra Figma (nodo `681:29701`) surgió el **token scale del App** y correcciones que aplican a **todos los flujos**:

**Escala (Inter):**
| Token | Familia/Peso | Tamaño | LH | Tracking |
|---|---|---|---|---|
| `T3 M` / `B1 M` | Inter **Medium 500** | 16px | 100% | −2% (≈ −0.32px) |
| `B1 R` | Inter **Regular 400** | 16px | 100% | −2% |
| `B3 M` | Inter **Medium 500** | 12px | 100% | 0 |
| `.base/Button` | Inter **Medium 500** | 16px | — | −0.32px |

**Regla:** en el App, **títulos de pantalla, labels y botones = Inter Medium 500** (no SemiBold 600). Body = Regular 400. Colores: texto oscuro `#000`, texto claro `#4C4C4C`, borde de card `#E7E7E7` (gray-400), stroke `#F3F3F3`.

**🔴 Correcciones pendientes en los demos:** varios demos usan **600** en títulos/botones donde debe ser **500** — hacer sweep global.
**🔴 Anomalía:** el texto "Envío gratis…" (`681:29761`) está en **Manrope SemiBold 600 14px** dentro del App (que debería ser Inter). Confirmar si es intencional o error.
**🔴 `TYPOGRAPHY.md`** no incluye la escala del App (T/B tokens, Inter) — agregarla; y corregir el owner a "Head of UX/UI".

---

# Flujo 8 — Activar T1 pagos (Activate T1 Payments)

> Activar el procesamiento de pagos (T1pagos). Entra desde la tarjeta de setup **"Activar T1 pagos"** del Home de Pagos.
> **Figma:** *Activate T1 Payments* (`602:31723`).

## 8.1 Mapa del flujo

```
Home Pagos (tarjeta "Activar T1 pagos")
   │ tap  → se abre el popup
   ▼
Modal "Activar T1 pagos" (794:73222) — beneficios + nota de depósito + aceptar T&C
   │ "Activar" → carga un momento    └─ "Cancelar" → cierra el popup
   ▼
Loading
   ▼
Modal éxito "¡T1 pagos está activo!" (794:73264) — ilustración + subir documentación
   │ cerrar
   ▼
Home Pagos + 🎉 confeti (1990:126964) — la tarjeta completada se mueve al final
```

Anotaciones: *"Al tocar la tarjeta para activar T1 pagos se abrirá el popup"* · *"Cancelar cerrará el popup"* · *"Al tocar el botón de activar cargará un momento"* · *"Después de cargar, T1 pagos quedará activado"* · *"El usuario cierra el popup y la pantalla de inicio se animará; la tarjeta del paso completado se moverá al final."*

## 8.2 Contexto — Home de Pagos (T1pagos) `1990:126121`
Variante de Home para **Pagos** (ya listada en §H.2). Detalle:
- **Métricas:** Pagos procesados ($55K +8%) · Transacciones (53 −3%) · Dispersión pendiente ($3K +2%) · Última dispersión ($889 +2%) · Links activos (30).
- **Acciones rápidas:** Ver resumen semanal · Ver transacciones · Ver dispersiones.
- **Setup:** **Activar T1 pagos** · Completar información fiscal · Agregar cuenta bancaria · Crear primer link de pago · Configurar notificaciones de pago.
- **Promo:** "Haz crecer tu negocio / Empieza a vender con T1tienda".
> Referencia cruzada con §H.2 (variante Pagos).

## 8.3 Modal "Activar T1 pagos" (`794:73222`)
Popup (card blanca redondeada) sobre el Home atenuado. Contenido:
- **Título** "Activar T1 pagos" + **subtítulo** "Empieza a cobrar en minutos con tarjetas de crédito/débito, SPEI y otros métodos, todo en un solo lugar."
- **Check (beneficio, pre-marcado rojo):** "Empieza a vender hoy y ofrece múltiples opciones de pago a tus clientes."
- **Nota (info):** "Las ganancias de tus ventas se depositarán en tu cuenta bancaria una vez que tu documentación sea validada."
- **Check (sin marcar):** "Acepta los Términos y Condiciones de T1 pagos." *(texto normal, NO link rojo)*.
- **Botones** (296×40): **"Activar"** (rojo, **siempre habilitado** — no depende de los checks) + **"Cancelar"**.

## 8.4 Loading (in-modal) + Modal de éxito (`794:73264`)
Al tocar **Activar**, el **botón muestra un spinner** (el modal se mantiene abierto) — no es pantalla aparte. Al terminar → **Modal éxito**: ilustración (*Payment Information-bro*: manos con teléfono "PAYMENTS", tono coral) + **"¡T1 pagos está activo!"** + subtítulo "Ya puedes empezar a cobrar con tarjetas y SPEI. Sube tu documentación…" + botón **"Cerrar"** (bordeado/blanco, no rojo).

## 8.5 Cierre — Home Pagos + confeti (`1990:126964`)
Cerrar → vuelve al Home de Pagos con **confeti**. **Confirmado por captura:** la tarjeta "Activar T1 pagos" **se mantiene en su lugar** (sigue primera, contador "2 de 5"), igual que el inicio.
> 🔴 **Discrepancia:** la anotación dice "la tarjeta del paso completado se moverá al final", pero el **mock de cierre no lo refleja** (la tarjeta no se mueve ni cambia de estado). Definir el comportamiento canónico.

## 8.6 Componentes nuevos
- **Modal de activación** (título + subtítulo + checks + nota informativa + 2 botones).
- **Check / Control** (checkbox de beneficio y de T&C).
- **Modal de éxito con ilustración**.
- *(reutilizados)* FAB Nova, confeti, Home de Pagos, tarjeta de setup.

## 8.7 Pendientes (🔴)
1. Variante Pagos del Home: ya en §H.2 (referencia cruzada).
2. Asset de la **ilustración** de éxito (no descargable de Figma).
3. Flujo posterior de **subir documentación** (KYC) referido en el modal de éxito.

## 8.8 Referencias
- *Activate T1 Payments* (`602:31723`): Home Pagos `1990:126121` · Modal activar `794:73222` · Modal éxito `794:73264` · Home+confeti `1990:126964`

---

# Flujo 9 — Nombre de la tienda (Set the store name)

> Capturar el **nombre de la tienda**, con **sugerencias por IA** y **límite de 40 caracteres**. Entra desde la tarjeta de setup **"Añade el nombre de tu tienda"** del Home de Tienda.
> **Figma:** *Set the store name* (`601:26479`).

## 9.1 Mapa del flujo

```
Home Tienda (tarjeta "Añade el nombre de tu tienda")
   │ tap
   ▼
Nombre de la tienda — vacío (674:63552): input + contador 0/40 + botón "Sugerir con IA"
   │ "Sugerir con IA" → la IA sugiere nombres
   ▼
Con sugerencias (674:64265): label "Sugerido con IA" + 5 chips
   │ seleccionar un chip  ó  escribir a mano
   ▼
Con selección (674:64321): input lleno (ej. "EcoClothing", 11/40) + chip marcado
   │ (si >40 → error "Límite de caracteres alcanzado", 41/40 · 743:62234)
   │ "Guardar"                              └─ "Descartar" → vuelve al Home
   ▼
Home Tienda + 🎉 confeti (1990:129256) — la tarjeta "Añade el nombre…" desaparece
```

Anotaciones: *"El usuario toca sugerir con IA y la IA sugerirá el nombre de la tienda"* · *"El usuario puede seleccionar cualquiera de los nombres sugeridos o escribir su propio nombre de tienda."*

## 9.2 Pantalla "Nombre de la tienda" (`674:63552` vacío · `674:64265` sugerencias · `674:64321` selección · `743:62234` error)
Header back + **"Nombre de la tienda"**. Contenido (ancho 328):
- **Label** "Nombre de la tienda" (`Inter SemiBold 600` 14px).
- **Input** (h55, borde `#F3F3F3`, **radio 20**) con texto `Inter Regular 400` ~12px.
- **Contador** "N/40" alineado a la derecha (`Manrope Regular` ~13px). Límite **40**.
- **Botón "Sugerir con IA"** (`ai-magic`, 187px) — solo en el estado inicial; dispara la sugerencia.
- **"Sugerido con IA"** (label con `ai-magic`, `Inter SemiBold 600` 14px `#4C4C4C`) + **chips de sugerencia** (bg `#F8F8F8`, **radio 11**, padding 12/8):
  - **No seleccionado:** `Inter Regular 400` 12px negro.
  - **Seleccionado:** `Inter SemiBold 600` 12px `#4C4C4C`.
  - Sugerencias del mock: **EcoClothing · Natural Green · Live thread · EcoNatura · Café Punto**.
- **Estado de error** (`743:62234`): al superar 40 → contador **"41/40"** + mensaje **"Límite de caracteres alcanzado"** (rojo).
- **Footer:** 2 botones (328×48) **"Guardar"** (rojo, `Inter Medium 500`) + **"Descartar"** (bordeado 1.5px `#4C4C4C`). FAB Nova.

## 9.3 Cierre — Home Tienda + confeti (`1990:129256`)
Guardar → vuelve al Home de Tienda con **confeti**. La tarjeta **"Añade el nombre de tu tienda" desaparece** de la lista de setup (comportamiento tipo "desaparece", como Agregar dirección — ver §H.3.3c).

## 9.4 Componentes nuevos
- **Input con contador de caracteres** (N/40) + **estado de error de límite** ("Límite de caracteres alcanzado").
- **Botón "Sugerir con IA"** (ai-magic).
- **Chips de sugerencia seleccionables** (estado seleccionado = SemiBold + oxford).
- *(reutilizados)* label "Sugerido con IA", FAB Nova, confeti, Home Tienda completo.

> **Relación:** mismo patrón que el **Paso 3 del Onboarding** ("¿Cómo se llama tu negocio?", sugerencias) y el **Flujo 3** (Crear tienda con IA). Unificar el componente "input + sugerencias IA".

## 9.5 Validación de tipografía (App) — hallazgos
- **Inconsistencia de peso en títulos de pantalla:** aquí "Nombre de la tienda" es **`Inter SemiBold 600`** (token `T3 S`), pero en el Flujo 7 "Tarifas de envío" es **`Inter Medium 500`** (`T3 M`). Definir el peso canónico del título de pantalla.
- **Anomalía Manrope:** el **contador "N/40"** usa **`Manrope Regular`** dentro del App (debería ser Inter) — igual que el texto "Envío gratis…" del Flujo 7. Confirmar/corregir.
- Tokens del App vistos aquí: `T3 S` (Inter SemiBold 16), `B2 S` (SemiBold 14), `B3 S` (SemiBold 12), `B3 R` (Regular 12), `B1 M` (Medium 16). Input radio 20, chip radio 11, stroke `#F3F3F3`, bg chip `#F8F8F8`.

## 9.6 Pendientes (🔴)
1. 🔴 Peso canónico del **título de pantalla** (500 vs 600 — inconsistente entre flujos).
2. 🔴 Anomalía **Manrope** en el contador (unificar a Inter).
3. Reglas del **límite de 40** (¿se bloquea el tecleo o solo se marca error?).
4. Cuántas **sugerencias de IA** se muestran en el carril de chips.
5. Unificar el **componente input + sugerencias IA** con Onboarding Paso 3 y Flujo 3.

## 9.7 Referencias
- *Set the store name* (`601:26479`): Home `1990:128293` · Vacío `674:63552` · Sugerencias `674:64265` · Selección `674:64321` · Error `743:62234` · Home+confeti `1990:129256`

---

# Flujo 10 — Dominio personalizado (Use Custom domain)

> Conectar un **dominio propio** a la tienda. **Feature de pago:** si el usuario no tiene plan de suscripción, el flujo lo lleva al **paywall de planes**. Entra desde la tarjeta de setup **"Conectar tu dominio"** del Home de Tienda.
> **Figma:** *Use Custom domain* (`601:27991`).

## 10.1 Mapa del flujo (bifurcado)

```
Home Tienda (tarjeta "Conectar tu dominio")
   │ tap
   ▼
Dominio personalizado — "Conectar dominio existente" + input
   │
   ├─ CON plan (682:30122 → 682:30298): llenar → "Guardar"
   │      ▼
   │   Dominio conectado → Home Tienda + 🎉 confeti (1990:131180) · la tarjeta desaparece
   │
   └─ SIN plan (682:30380 → 683:30894): llenar → (botón en card)
          ▼
       Modal de planes / paywall (683:30674) — Gratis · Básico · Avanzado
          → seleccionar plan para desbloquear "Dominio propio"
```

Anotaciones: *"El usuario toca la tarjeta de dominio personalizado"* · *"Con/Sin plan de suscripción"* · *"El usuario llena el campo"* · *"El usuario guarda y el dominio queda conectado a la tienda"* · *"Cuando el usuario llena el campo, necesita adquirir el plan para conectar el dominio personalizado."*

## 10.2 Pantalla "Dominio personalizado" (`682:30122` con plan · `682:30380` sin plan)
Header back + **"Dominio personalizado"**. **Card** (`Frame 2147239724`, 296 de ancho):
- **Título** "Conectar dominio existente" + **descripción** "Ingresa el dominio que quieres conectar a tu cuenta de T1tienda."
- **Input** (296×55) para el dominio.
- **Sin plan:** la card agrega un **botón** (296×32) debajo del input (acción que dispara el paywall). *(el rol exacto del botón queda por confirmar visualmente)*.
- **Footer:** 2 botones (328×48) **"Guardar"** + **"Descartar"**. FAB Nova.

## 10.3 Modal de planes / paywall (`683:30674`)
**Modal flotante** (tarjeta con esquinas redondeadas y fondo atenuado **arriba y abajo** — no es un drawer pegado al borde inferior). **Componente en Manrope** (no Inter) — probablemente compartido con Dashboard/Storefront. Header **"Accede a todas las funciones seleccionando un plan"** (Manrope) + botón **cerrar** (X). Contenido scrolleable con **3 planes**:

| Plan | Precio | Badge subtítulo (verde) | Créditos IA | Botón |
|---|---|---|---|---|
| **Gratis** | **FREE** + "Plan actual" | "Para nuevos vendedores en línea" | **50 créditos de IA** (gris) | — |
| **Básico** | **$399 MXN/mes** + toggle Anual | "Para nuevos vendedores en línea" | **500 créditos de IA por mes** (morado) | **"Mejorar plan"** (rojo) |
| **Avanzado** | **$1,499 MXN/mes** + toggle Anual | "Para equipos en crecimiento" | **1,000 créditos de IA por mes** (morado) | **"Mejorar plan"** (rojo) |

**Anatomía de la plan card** (borde `#F3F3F3`, radio **~22**):
- **Badge de nombre** (bg `#F8F8F8`, Manrope SemiBold 10px `#101928`) + **badge verde de subtítulo** (bg `#51AF70`, blanco, Manrope SemiBold 10px, derecha).
- **Precio** Manrope Bold ~36px `#101928` + "MXN / mes" Manrope Medium `#485162`.
- **"Plan actual"** (Gratis) o **toggle "Anual"** (pagados).
- **Botón "Mejorar plan"** (rojo `#DB3B2B`, **Inter** SemiBold 14, radio 12) — solo planes de pago.
- **Chip "N créditos de IA"** (bg `#F8F8F8`, borde `#F3F3F3`, ícono `ai-magic` + **Inter** Medium 12px; texto **gris `#4C4C4C`** en Gratis, **morado `#7C3AED`** en pagados).
- **Features** con `tick-02` (Manrope Medium 12px `#101928`): incluye **"Dominio propio"** en Básico+ (motivo del flujo). Bloque **"Comisión por tarjeta desde"** en pagados.
- Cierre de la lista: link **"Ver comparación de planes aquí"** (Manrope). **No hay CTA de footer fijo**; la acción de cada plan vive en su propia card (chip "N créditos de IA" + botón "Mejorar plan").
- **"Dominio propio"** aparece como feature del plan **Básico** (y superiores) → por eso el flujo sin plan lleva aquí.

> **Colores del componente:** texto oscuro `#101928`, texto claro `#485162` (distintos a los del resto del App `#000`/`#4C4C4C`), lo que refuerza que es un **componente compartido con Dashboard** (Manrope).

## 10.4 Cierre (con plan) — Home Tienda + confeti (`1990:131180`)
Guardar → dominio conectado → Home + **confeti**; la tarjeta **"Conectar tu dominio" desaparece** de la lista de setup (comportamiento tipo "desaparece" — §H.3.3c).

## 10.5 Componentes nuevos
- **Paywall / hoja de planes** (**modal flotante** con 3 planes; esquinas redondeadas, fondo atenuado arriba y abajo).
- **Plan card** (badge + subtítulo + precio + toggle Anual + botón + lista de features con `tick-02` + bloque de comisiones).
- **Toggle "Anual"** (Control/switch).
- **Card "Conectar dominio existente"** (título + descripción + input, con botón extra en estado sin plan).
- *(reutilizados)* FAB Nova, confeti, Home Tienda completo.

## 10.6 Pendientes (🔴)
1. 🔴 Confirmar visualmente el **rol del botón extra** en la card sin plan (¿"Conectar dominio" / "Adquirir plan"?) y sus tokens.
2. ✅ **Paywall validado** contra Figma (Manrope, badges verdes, chips de créditos IA, "Mejorar plan" por plan, colores `#101928`/`#485162`, **modal flotante** sin CTA de footer fijo).
3. 🔴 El paywall es un **componente en Manrope** (probable reúso de Dashboard) — confirmar y, si aplica, documentarlo en el design system compartido en vez de solo en App.

## 10.7 Referencias
- *Use Custom domain* (`601:27991`): Home `1990:130215` · Dominio con plan `682:30122`/`682:30298` · Dominio sin plan `682:30380`/`683:30894` · Paywall `683:30674` · Home+confeti `1990:131180`

---

# Flujo 11 — Conectar redes sociales (Connect Social media)

> Agregar usuarios/enlaces de redes sociales a la tienda + activar la **burbuja de WhatsApp** (feature de pago). Entra desde la tarjeta de setup **"Conectar redes sociales"** del Home.
> **Figma:** *Connect Social media* (`601:28233`).

## 11.1 Mapa del flujo

```
Home (All Services) — tarjeta "Conectar redes sociales"
   │ tap
   ▼
Conectar redes sociales (158:44757 vacío → 158:45202 lleno)
   · 7 inputs de redes (TikTok, Instagram, Facebook, X, YouTube, Pinterest, Threads)
   · input WhatsApp + toggle "Mostrar burbuja de WhatsApp en tu tienda"  ← feature de pago
   │ "Guardar"  (animación de éxito)         └─ "Descartar" → Home
   ▼
Home + 🎉 confeti (1990:133050) — la tarjeta desaparece

  · Si NO hay plan / la prueba gratis terminó al usar la burbuja de WhatsApp:
       → Paywall de planes (674:60887 sin plan · 674:60606 "prueba gratis terminada")
```

Anotaciones: *"El usuario da clic en la tarjeta de conectar redes sociales"* · *"Agrega los enlaces de las cuentas de redes sociales que quiere conectar"* · *"Animación de éxito después de que el usuario da clic en Guardar"* · *"La burbuja de WhatsApp estará en el plan de pago"*.

## 11.2 Pantalla "Conectar redes sociales" (`158:44757`)
Header back + **"Conectar redes sociales"**. Contenido (ancho 328):
- **Descripción:** "Agrega tus usuarios o enlaces para mostrar tus redes sociales en tu tienda y conectar con más clientes."
- **7 inputs de red social** (h55): cada uno con un **prefijo de ícono de marca** (54px, izquierda) + placeholder **"@"** (o la URL cuando está lleno, ej. `tiktok.com/@lumen.create23`). Orden: **TikTok · Instagram · Facebook · X · YouTube · Pinterest · Threads**.
- **Divisor** (Line 728).
- **Segunda sección** (misma descripción): **1 input de WhatsApp** + **toggle "Mostrar burbuja de WhatsApp en tu tienda"** (Control switch).
- **Footer:** 2 botones (328×48) **"Guardar"** + **"Descartar"**. FAB Nova.

## 11.3 Burbuja de WhatsApp = feature de pago (paywall reutilizado)
La **burbuja de WhatsApp** solo está disponible con plan. Sin plan → al intentar activarla se abre el **paywall de planes** (el mismo componente del Flujo 10, §10.3). Dos variantes de header:
- **Sin plan:** "Accede a todas las funciones seleccionando un plan".
- **Prueba gratis terminada:** **"¡Tu prueba gratuita de la tienda en línea ha terminado! Conserva tu tienda suscribiéndote a un plan"**.
> 🔴 **Nueva variante de header del paywall** ("prueba gratis terminada") — agregarla al componente de planes documentado en §10.3.

## 11.4 Cierre — Home + confeti (`1990:133050`)
Guardar → **animación de éxito** → Home con **confeti**; la tarjeta **"Conectar redes sociales" desaparece** de la lista de setup (§H.3.3c).

## 11.5 Componentes nuevos
- **Input con prefijo de ícono de red social** (icono de marca 54px + campo con placeholder "@"/URL).
- **Toggle "Mostrar burbuja de WhatsApp"** (feature de pago, dispara paywall).
- *(reutilizados)* Paywall de planes (§10.3) + **nueva variante de header** "prueba gratis terminada", FAB Nova, confeti, Home (All Services).

## 11.6 Pendientes (🔴)
1. 🔴 **Íconos de marca** (TikTok, Instagram, Facebook, X, YouTube, Pinterest, Threads, WhatsApp) — no descargables de Figma; en el demo se recrean de forma simplificada. Exportar los oficiales a `icons.ts`.
2. 🔴 Agregar la **variante de header "prueba gratis terminada"** al paywall (§10.3).
3. Comportamiento exacto de la **burbuja de WhatsApp** en la tienda (posición).

## 11.7 Referencias
- *Connect Social media* (`601:28233`): Home `1990:132125` · Vacío `158:44757` · Lleno `158:45202` · Home+confeti `1990:133050` · SIN PLAN `674:60220` + paywall `674:60887` · PRUEBA GRATIS `674:60554` + paywall `674:60606`

---

# Flujo 12 — Configurar políticas de la tienda (Configure Store Policies)

> Configurar **reglas de devolución** y **políticas legales** (devoluciones, privacidad, T&C, envíos), con **generación por IA** y **personalización avanzada en escritorio**. Entra desde la tarjeta de setup **"Configurar políticas"** del Home.
> **Figma:** *Configure Store Policies* (`601:30287`). Flujo largo con varias sub-pantallas.

## 12.1 Mapa del flujo

```
Home (tarjeta "Configurar políticas")
   │ tap
   ▼
Políticas de la tienda (689:31269) — 2 bloques
   ├─ REGLAS DE DEVOLUCIÓN
   │    · botón "Creado con IA basado en la información de tu industria"
   │    · card Resumen (14 días / envío cubierto por cliente / 2 productos venta final)
   │    · botón "Configurar" → Reglas de devolución (683:51727)
   │
   └─ PERSONALIZA TUS POLÍTICAS
        · botón "Generar con IA" → Aviso de IA (689:31218) → loading (689:30993) → generadas (689:31628)
        · lista de 4 políticas con chip de estado + flecha:
             Política de devoluciones · Aviso de privacidad · Términos y condiciones · Política de envíos
        · tap en una política (personalizar) → Modal "sólo escritorio" (700:35123)
   ▼
Guardar → Home + 🎉 confeti (1990:137803) — la tarjeta "Configurar políticas" desaparece
```

## 12.2 Pantalla principal "Políticas de la tienda" (`689:31269`)
Header back + **"Políticas de la tienda"**.

**Bloque 1 — Reglas de devolución:**
- Título "Reglas de devolución" (Inter Medium 16) + descripción "Activa tus políticas de devolución para simplificar el proceso, ajustar costos o envíos, y marcar los artículos que no aceptan devolución."
- **Botón** (gris `#F8F8F8`, ai-magic): **"Creado con IA basado en la información de tu industria"**.
- **Card "Resumen"** (bg `#F8F8F8`, radio 16): "• Devoluciones aceptadas dentro de 14 días • El envío de devolución es cubierto por el cliente • Artículos de venta final: 2 productos no pueden devolverse".
- **Botón "Configurar"** (bordeado) → pantalla de Reglas de devolución.

**Divisor.**

**Bloque 2 — Personaliza tus políticas:**
- Título "Personaliza tus políticas" + descripción "Las políticas que actives se muestran en el pie de página de tu tienda y durante el proceso de checkout."
- **Botón "Generar con IA"** (bordeado `#E7E7E7`, ai-magic).
- **Lista de 4 políticas** (etiqueta en **Manrope SemiBold 14**, chip + `arrow-right`):
  | Política | Chip |
  |---|---|
  | Política de devoluciones | **No generada** (gris) |
  | Aviso de privacidad | **Activar** (verde) |
  | Términos y condiciones | **No generada** (gris) |
  | Política de envíos | **No generada** (gris) |

**Estados del chip:** `No generada` (gris `#F3F3F3`/`#4B5563`) · `Activar` (verde `#F0FDF4`/`#51AF70`) · **loader** (generando con IA). Footer: Guardar + Descartar.

## 12.3 Reglas de devolución (`683:51727`)
Pantalla dedicada (larga). Header "Reglas de devolución".
- **Toggle "Reglas de devolución"** + "Habilita solicitudes de devolución para tus clientes en pedidos que hayan sido entregados."
- **"Configura tus devoluciones":**
  1. **Límite del período de devolución** — "Selecciona cuántos días tienen tus clientes para validar una devolución." + **Select** "Selecciona los días" → **"14 días"** (con chevron).
  2. **Costo de envío de devolución** — "Selecciona cómo se cobrará el envío de devolución." + **radios** (opciones "Categoría 1 › Subcat").
  3. **Catálogos y productos sin devolución** — "Selecciona los catálogos y productos que no son elegibles para devolución." + **checkboxes** + **buscador "Buscar catálogos"** + **"Catálogos seleccionados"** (Bautizo · Niña · Niño · Primera comunión, cada uno "13 productos" con imagen + quitar `X`).
- Footer: Guardar + Descartar.

## 12.4 Generación con IA (aviso → loading → generadas)
1. **Aviso sobre el uso de IA** (`689:31218`, bottom sheet): ícono `ai-magic` (64) + **"Aviso sobre el uso de IA"** + "La información generada por nuestra IA no constituye asesoría legal. Al usarla, aceptas el deslinde de responsabilidad de T1." + 2 botones (aceptar / cancelar).
2. **Loading** (`689:30993` / `4098:27805`): cada fila de política muestra un **loader** en lugar del chip (loader inline — ver §L.3 *Estados de carga*).
3. **Generadas** (`689:31628`): cada fila lleva **ícono `ai-magic`** como prefijo + chip **"Activar"** (verde) + flecha.

## 12.5 Personalización avanzada = sólo escritorio (`700:35123`)
Al tocar una política para editarla a fondo → **modal** (bottom sheet): ícono `google-doc` (64) + **"Personalización de políticas disponible en escritorio"** + "Usa la versión de escritorio para actualizar o personalizar las políticas de tu tienda." + botón (Entendido).
> Consistente con el patrón "la edición fina se hace en web" (visto también en Tarifas de envío, Flujo 7).

## 12.6 Cierre — Home + confeti (`1990:137803`)
Guardar → Home con **confeti**; la tarjeta **"Configurar políticas" desaparece** de la lista de setup (§H.3.3c).

## 12.7 Componentes nuevos
- **Fila de política** (etiqueta Manrope + **chip de estado** [No generada / Activar / loader] + `arrow-right`).
- **Card "Resumen"** de reglas (bg `#F8F8F8`, radio 16, bullets).
- **Botones "Creado con IA…" / "Generar con IA"** (ai-magic).
- **Config de reglas de devolución**: toggle, select de días, radios de costo, checkboxes, **buscador + lista de catálogos seleccionados** (item con imagen + quitar).
- **Modal "Aviso sobre el uso de IA"** (deslinde legal).
- **Modal "sólo escritorio"** (google-doc).
- *(reutilizados)* FAB Nova, confeti, Home (All Services).

## 12.8 Notas de tipografía
- **Etiquetas de política en `Manrope SemiBold 14`** (`#000`, tracking −0.5, lh 22) — nueva anomalía Manrope dentro del App (van 4: F7 tarifas, F9 contador, F10 paywall, y estas etiquetas). Probable componente compartido.
- Botones/títulos en **Inter Medium 500**; descripciones **Inter Regular 14 `#4C4C4C`**; chips **Inter Medium 12**.

## 12.9 Pendientes (🔴)
1. 🔴 Consolidar las **anomalías Manrope** dentro del App (¿componentes compartidos con Dashboard o inconsistencias a corregir?).
2. 🔴 Estados completos del **chip de política** (¿existe "Activada"/"Desactivar" tras activar?).
3. Fuente de las **imágenes de catálogo** (placeholder) — recreadas en el demo.
4. Íconos `ai-magic`, `google-doc`, `loader`, `arrow-right-01-sharp` — exportar a `icons.ts`.

## 12.10 Referencias
- *Configure Store Policies* (`601:30287`): Home `1990:135879` · Políticas `689:31269` · Reglas de devolución `683:51727` · Aviso IA `689:31218` · Loading `689:30993` · Generadas `689:31628` · Sólo escritorio `700:35123` · Home+confeti `1990:137803`

---

# Flujo 13 — Pedidos (Orders)

> Sección **"Orders"** (`290:20528`): listado y gestión de pedidos del merchant (contexto multicanal T1). Cubre estados de lista (vacío / con pedidos / carga diferida), búsqueda, UI de filtros, menú por pedido (duplicar / cancelar) y el paywall al crear pedido sin plan. La sección incluye varias **notas de desarrollo en inglés**.
> **Figma:** *Orders* (`290:20528`).

## 13.1 Mapa del flujo

La sección agrupa las pantallas bajo 9 rótulos:

| Rótulo Figma | Pantallas | Contenido |
|---|---|---|
| Estado vacío de mis pedidos | `731:26144` | Empty state (sin pedidos) |
| Variante con pedidos | `731:26521` | Lista poblada de tarjetas de pedido |
| Opciones de menú | `795:63501` | Menú de la barra superior (overflow) |
| UI de filtros | `795:67660` · `731:27302` · `733:28160` · `733:28530` · `4183:101130` · `733:28907` · `733:29169` | Panel de filtros, multiselección y resultados |
| Variante de búsqueda | `733:29479` | Lista filtrada por búsqueda |
| Opciones de menú del pedido | `733:29874` · **Duplicate** `290:21765` · **Cancel** `290:21849` | Menú "···" por pedido + acciones |
| Carga diferida | `434:39740` · `434:39767` | Lazy load / skeleton (ver §L) |
| Crear pedido - SIN PLAN | `733:30827` · `674:55489` | Paywall al crear sin plan |
| Crear pedido - PRUEBA GRATUITA | `733:31596` · `674:58702` | Variante prueba gratuita del paywall |

**Recorrido base:** *Mis pedidos* (lista) → buscar / filtrar → abrir menú "···" de un pedido → **Duplicar** o **Cancelar** (modal de confirmación). En paralelo, crear pedido sin plan activo abre el **paywall de planes** (§10.3).

## 13.2 Chrome de la pantalla (común)

- **Status bar** iPhone (50) + **barra inferior con FAB** (86; ver §H.3.9 / §H.3.10).
- **Título** "Mis pedidos" — token **`T2 S`** (Inter **SemiBold 20**, lh 1.3, tracking −0.4). *(Resuelto contra Figma `731:26682`.)*
- **Buscador** (`Frame 2147239909`): campo `bg #F8F8F8`, **radio 12**, `px8 py10` — ícono `search-01` (20) + placeholder **"Buscar por ID de pedido, SKU, cliente"** (Inter Regular 14, **`#9CA3AF`** Greys/300) + **2 botones 40×40** (`bg #F8F8F8`, radio 12): **ordenar** (`filter-horizontal`, descrito en Figma como *sorting*) y **overflow** (`more-vertical`).
- **Tabs (subrayado)** — contenedor con borde inferior `1px #F3F3F3`:
  - **"Listado de pedidos"** (activo): Inter **SemiBold 14** `#000`, tracking −0.28, **subrayado 1.5px `#DB3B2B`**, padding `8/16/12`.
  - **"Carrito abandonado"** e **"Sucursales"** (inactivos): Inter Medium 14 `#4C4C4C`. "Sucursales" va **separado a la derecha** (left 391).

## 13.3 Tarjeta de pedido (átomo) — `731:26810`

Tarjeta `328` de ancho (contenido 296), **bg white**, borde `1px #F3F3F3`, radio 12, `padding 15`, columna `gap 16`.

- **Cabecera** (fila, space-between):
  - **Izquierda:** avatar (`Avatars-Size-Component` 48×48) + **nombre del cliente** (Inter **Medium 16**, `#000`, tracking −0.32) + **# de pedido** "#394030" (Inter **Regular 12**, `#4C4C4C`). *(Algunas tarjetas incluyen un ícono `x` 12px junto al nombre.)*
  - **Derecha:** **chip de estado** + `more-horizontal` (20px, rotado 90° = 3 puntos verticales) → menú del pedido.
- **Divisor** (`Line 711`).
- **Detalle** (gap 16):
  - "Producto" (label Inter Regular 12 `#4C4C4C`) → **"3 productos"** (valor Inter Medium 14 `#000`, tracking −0.28, derecha).
  - *(opcional)* ícono `cash-01` (20) + "Monto" → **"$12,383.00"**.
  - *(opcional)* ícono `store-03` (20) + "Pedido vía" → **chip de canal** (nombre + logo, ej. "Amazon" + `amazon-iso`).
- **Divisor** (`Line 712`).
- **Pie:** `calendar-03` (20) + **"14:24 - 23 de oct, 2025"** (Inter Medium 12 `#000`) + *(opcional)* **"3 envíos"** (Inter Medium 12 `#1F2937`, derecha).

**Chips de la tarjeta:** ambos (estado y canal) usan el mismo molde — bg `#F8F8F8`, radio 6, `px6 py4`, texto Inter Medium 12. El **estado** ("En camino") va en `#4C4C4C`; el **canal** ("Amazon") en `#000` + logo 12px.

> **Dos densidades de tarjeta:** una **simple** (filas sin ícono, solo label→valor) y otra **rica** (filas Monto/Pedido vía con ícono a la izquierda + pie con "N envíos"). Confirmar cuándo aplica cada una.

> 🔴 **Jerarquía de cabecera inconsistente:** hay tarjetas con **nombre 16 / #id 12** (esta) y otras con **#id ~19 (bold) / nombre 15**. Definir cuál es canónica.

## 13.4 Estado vacío (`731:26144`)

- Ilustración `Usability testing-pana 1` (220×220, Freepik).
- **Título** "Aún no tienes pedidos" (Inter SemiBold ~22).
- **Subtítulo** "Una vez que recibas un pedido, aparecerá aquí." (Inter Regular 14 `#4C4C4C`).
- **Botón primario** (162×40, `bg #DB3B2B`, radio 12, Inter SemiBold 14 blanco): **"Crear pedido"**. *(Resuelto contra Figma `731:26315`.)* A diferencia del empty de Métricas (§M.3, CTA **secundario**), aquí el CTA es **primario**.
- Tabs y buscador presentes (el bloque vacío ocupa el área de la lista, **no** se oculta la pantalla).

## 13.5 Variante con pedidos (`731:26521`)

Lista vertical de **tarjetas de pedido** (§13.3). Datos de ejemplo en Figma: clientes *Javari Mena / Zain Vetrovs*, `#394030`, "3 productos", "$12,383.00", canal, "14:24 - 23 de oct, 2025", "3 envíos".

## 13.6 Búsqueda (`733:29479`)

Buscador activo → lista filtrada por *query* (mismo layout de tarjetas). Placeholder: "Buscar por ID de pedido, SKU, cliente".

## 13.7 UI de filtros (`795:67660` + 6 pantallas)

Flujo (según notas de dev en Figma):
1. El usuario toca el **ícono de filtro** en la barra de búsqueda.
2. Se abre el **panel de filtros**: categorías + **selección de fecha**; se pueden elegir **múltiples filtros dentro de una misma categoría**.
3. Botón **"Mostrar resultados"** → se muestran los resultados según los filtros.
4. Al aplicar filtros, el **chip de filtro** muestra el **nombre de la categoría + número** de filtros aplicados en ella.

Pantallas del grupo: `795:67660` · `731:27302` · `733:28160` · `733:28530` · `4183:101130` · `733:28907` · `733:29169` (incluye listas largas 360×1165 con filtros aplicados).

## 13.8 Menú del pedido — acciones (Duplicar / Cancelar)

Desde el `more-horizontal` de cada tarjeta se abren las acciones. Ambas usan el **mismo patrón de modal de confirmación**.

**Modal de confirmación** (`290:21766`): tarjeta blanca **radio 16**, contenido centrado `w299`, `gap 24`.
- **Ícono** en círculo `#F8F8F8` (64, radio full) + glifo 32px.
- **Título** Inter **SemiBold 20** (`T2 S`, `#000`, tracking −0.4, line-height 1.3).
- **Cuerpo** Inter Regular 14 (`#4C4C4C`, tracking −0.28), centrado.
- **2 botones** (fila, `gap 5`, cada uno flex-1, h40, radio 12): **"Cerrar"** secundario (blanco, borde 1.25px `#F3F3F3`, Inter Medium 14 `#000`) + **confirmación primaria** (bg `#DB3B2B`, Inter **SemiBold 14** blanco).

| Acción | Nodo | Ícono | Título | Cuerpo | Botón primario |
|---|---|---|---|---|---|
| Duplicar | `290:21765` | `copy-01` | Duplicar pedido | "¿Estás seguro de que quieres duplicar este pedido? Esto creará otro pedido similar." | **"Sí, duplicar"** |
| Cancelar | `290:21849` | `cancel-circle` | Cancelar pedido | "¿Estás seguro de que quieres cancelar este pedido? Esta acción no se puede deshacer." | **"Sí, cancelar"** (bg `#DB3B2B` — **mismo rojo que el primario**, sin color *danger* propio) |

*(El rótulo "Opciones de menú" `795:63501` corresponde al menú de la barra superior; "Opciones de menú del pedido" a este menú por tarjeta.)*

## 13.9 Crear pedido sin plan / prueba gratuita (paywall)

Al crear un pedido **sin plan activo** se abre el **paywall de planes reutilizado** (mismo componente de §10.3 / F10–F11):
- **Crear pedido - SIN PLAN** (`674:55489`) y **- PRUEBA GRATUITA** (`674:58702`).
- Título **"Accede a todas las funciones seleccionando un plan"**, cierre `cancel-01` (16).
- Planes en scroll (298 de ancho): **Gratis** (`FREE`, "Para nuevos vendedores en línea", badge **"Plan actual"**), **Básico** (**$399 MXN / mes**, toggle **"Anual"**), y planes superiores (Avanzado / Enterprise). Features con `tick-02` (ej. "Gestión de pedidos en +10 canales", "Reportes de ventas", "Hasta 3 sucursales").

> No se re-documenta el paywall aquí: es el mismo de §10.3 (ver también §B.2 para la variante "suscripción terminada" + Enterprise).

## 13.10 Componentes nuevos (vs. ya documentados)

- **Tarjeta de pedido** (§13.3) — avatar + cliente/#id + chip de estado + detalle + pie.
- **Tabs con subrayado rojo** (segmented underline; activo `SemiBold 14` + `1.5px #DB3B2B`).
- **Chip de estado** (neutral gris) y **chip de canal** (con logo) — mismo molde `#F8F8F8` radio 6.
- **Buscador con acciones** (search-01 + placeholder + 2 botones 40×40).
- **Panel de filtros** multicategoría + **chip de conteo** por categoría.
- **Modal de confirmación** (ícono en círculo + título + cuerpo + 2 botones) — patrón reutilizable (duplicar/cancelar).
- **Carga diferida** (Lazy Load) → §L.

## 13.11 Pendientes (🔴)

1. 🔴 **Jerarquía de cabecera de tarjeta** inconsistente (nombre 16 / #id 12 vs #id 19 / nombre 15). Definir canónica.
2. 🔴 **Estado del pedido sin color semántico:** el chip de estado es **gris `#F8F8F8`** para todos ("En camino", …). Confirmar si los estados (En camino, Entregado, Cancelado, etc.) deben tener color o se mantienen neutrales.
3. ✅ ~~Label del botón del estado vacío y label primario del modal Cancelar~~ → **"Crear pedido"** / **"Sí, cancelar"** (resueltos contra Figma).
4. ✅ ~~Tamaño px del título "Mis pedidos"~~ → **`T2 S` (SemiBold 20)** (resuelto).
5. 🔴 **Sin color destructivo propio:** "Sí, cancelar" (destructivo) usa el **mismo rojo `#DB3B2B`** que "Sí, duplicar" y que el primario. Definir variante *danger*. *(Ver también §D.9·1.)*
6. **Variante enmascarada (locked)** (`733:31596`): el nombre del cliente se sustituye por el **# de pedido** bajo *gating* de plan. Confirmar qué campos se ocultan.
7. Íconos a `icons.ts`: `search-01`, `filter-horizontal`, `more-vertical`, `more-horizontal`, `cash-01`, `store-03`, `calendar-03`, `copy-01`, `cancel-circle`, `amazon-iso`, `x`.

## 13.13 Referencias

- *Orders* (`290:20528`): Vacío `731:26144` · Con pedidos `731:26521` · Opciones de menú (barra) `795:63501` · Búsqueda `733:29479` · Menú del pedido `733:29874` · **Duplicar** `290:21765` · **Cancelar** `290:21849` · Carga diferida `434:39740`/`434:39767` · Crear sin plan `674:55489` · Prueba gratuita `674:58702`.
- UI de filtros: `795:67660` · `731:27302` · `733:28160` · `733:28530` · `4183:101130` · `733:28907` · `733:29169`.
- Reutiliza: paywall §10.3 · barra inferior/FAB §H.3.9–H.3.10 · loaders §L.
- [APP.md](./APP.md) — fundamentos (Inter, color, spacing, radios).

---

# Estados de carga — Loaders y Skeletons (transversal)

> Patrones de carga del App. Aplican a cualquier flujo, no a uno en particular.
> **Figma:** *Loader Screens* (`185:18667`).

## L.1 Skeleton (Lazy Load) — `50:723`
Placeholder que **replica la estructura real** del contenido mientras carga (no un spinner genérico). Bloques color **`#F2F2F2`**, **radio 2px** en líneas de texto.

**Anatomía (mimetiza el Home):**
- **Header:** línea 160×13 + línea 98×10 (gap 4) + **círculo avatar 34×34**.
- **Tabs/filtros:** 4 bloques 96×34 en fila (scroll horizontal).
- **Grid de cards:** 4 bloques 160×145 en **2×2** (tarjetas de setup).
- **Lista:** título 107×23 + **5 filas 328×56**.

**Uso:** carga inicial de pantallas con **layout conocido** (home, listas, grids). Es el patrón **preferido** sobre el spinner cuando se conoce la estructura, porque reduce la percepción de espera y evita saltos de layout.

## L.2 Spinner (Lazy Load) — `69:9908`
`tabler:loader` **32×32**, **centrado** en pantalla vacía. **Uso:** carga **indeterminada** o de pantalla completa cuando **no** se conoce la estructura del contenido.

## L.3 Loaders inline (dentro de componentes)
- **Fila con loader:** en la lista de políticas (Flujo 12), cada fila muestra un **loader (24px)** en lugar del chip mientras la IA genera las políticas.
- **Botón con spinner:** el CTA muestra un **spinner in-place** sin abrir otra pantalla (ej. "Activar" en Flujo 8). El resto de la UI se mantiene visible.

## L.4 Reglas de uso
1. **Skeleton** cuando el layout es conocido; **spinner** cuando no.
2. Color de skeleton `#F2F2F2`; radio 2px para líneas; el skeleton **respeta las dimensiones** del contenido real para evitar reflow.
3. Los **loaders inline no bloquean** el resto de la pantalla; solo el elemento afectado.
4. El **botón** que dispara una acción muestra su propio spinner (no una pantalla de carga aparte).

## L.5 Pendientes (🔴)
1. 🔴 Definir la **animación** del skeleton (shimmer vs pulse) y su timing/easing.
2. 🔴 Umbral para elegir **skeleton vs spinner** (¿a partir de cuántos elementos/qué pantallas?).
3. Exportar `tabler:loader` (spinner) y el `loader` inline a `icons.ts`.
4. Confirmar el color del skeleton (`#F2F2F2`) como token en `COLORS`/foundations.

## L.6 Referencias
- *Loader Screens* (`185:18667`): Skeleton `50:723` · Spinner `69:9908`

---

# Estado — Error de sincronización (Sync Error, transversal)

> Estado de error cuando falla la sincronización de datos por conexión. Aplica de forma transversal (no a un flujo específico).
> **Figma:** *Syncing Screens* (`434:40991`) → *Sync Error* (`434:41043`).

## S.1 Anatomía (`434:41047`)
**Card centrada** (bg blanco, **sombra suave** `0 4 16 rgba(0,0,0,.02)`, **radio 20**, padding 16, gap 32):
- **Ícono** `wifi-error-01` (32px, **naranja `#FF6700`**) dentro de un **círculo 64** con fondo **`#FFF5F0`** (peach).
- **Título** "Error de sincronización detectado" — **Inter SemiBold 600** 16px, negro, tracking −0.32, lh 1.3 (token `T3 S`).
- **Descripción** "No pudimos sincronizar tus datos más recientes por un problema de conexión. Revisa tu conexión a internet o intenta reconectar más abajo." — Inter Regular 400 14px `#4C4C4C`.
- **Botón "Reconectar"** (48h, **rojo `#DB3B2B`**, radio 16, ícono `refresh` + Inter Medium 500 16px blanco).
- **Texto informativo** "Última sincronización exitosa: 10:42 a.m." (40h, transparente, Inter Regular 14 `#4C4C4C`) — **no es botón de acción**, solo muestra el último sync exitoso.

## S.2 Semántica de color
- Usa **acento naranja** (`#FF6700` ícono / `#FFF5F0` fondo del círculo) para señalar el **estado de error de sincronización**, distinto del **rojo** de error/CTA.
- El **rojo `#DB3B2B`** se reserva para la **acción** ("Reconectar").
> 🔴 Confirmar tokens **Orange/300 `#FF6700`** y **Orange/500 `#FFF5F0`** en `COLORS`/foundations (nomenclatura invertida vs. intensidad: el "500" es el claro).

## S.3 Patrón de estado (reutilizable)
Estructura genérica **ícono en círculo de color + título + descripción + acción**, centrada verticalmente. Es el mismo molde de otros estados (éxito de activación en F8, empty states). Candidato a **componente de estado** parametrizable (color de acento, ícono, título, descripción, acción primaria, texto secundario).

## S.4 Relación con otros flujos
- El **Flujo 5** (Canales/Shein) tiene su propio error de sync (`597:42720`); **este** (`434:41043`) es el **estado genérico** de error de sincronización.
- El estado **exitoso/loading** de reconexión no está en esta sección (solo el error). En el demo se extrapola un estado "Sincronización exitosa" para mostrar la interacción del botón (spinner in-place → éxito), marcado como demo.

## S.5 Pendientes (🔴)
1. 🔴 Confirmar tokens naranja (`#FF6700` / `#FFF5F0`) en `COLORS`.
2. Definir el **resultado de "Reconectar"** (loading → éxito / reintento fallido) — no hay pantalla de resultado en esta sección.
3. Exportar `wifi-error-01` y `refresh` a `icons.ts`.
4. Evaluar unificar como **componente de estado** con los demás (éxito/empty/error).

## S.6 Referencias
- *Syncing Screens* (`434:40991`): Sync Error `434:41043`

---

# Banners y estados globales (Banner Use Cases, transversal)

> Sistema de **banners/alertas del Home** (3 severidades, carrusel) + pantallas globales (suscripción terminada, sin conexión, mantenimiento). Transversal.
> **Figma:** *Banner Use Cases* (`603:34724`).

## B.1 Sistema de banners/alertas del Home
**Carrusel horizontal** de banners (cada uno **328×104**, radio **16**, gap 12) ubicado **arriba del contenido del Home** (bajo el header), con **dots de paginación** debajo (círculos iguales ~7px; **activo oscuro**, inactivos gris claro). El banner va **encapsulado en una tarjeta gris** (`#F5F5F5`) sobre el **home blanco** — el gris de la tarjeta es del mismo tono que las **bandas separadoras** entre secciones (el resto de secciones van en blanco). Cada banner:
- **Ícono** (~28px, izquierda) + **título** (`Inter` Bold ~16, tracking −0.32) + **descripción** (`Inter Regular ~13`, **siempre visible**) en columna (x48) + **chevron derecho** (`tabler:chevron-up` rotado → **navegación al detalle**, centrado verticalmente a la derecha).

**3 tipos (severidad):**
| Tipo | Fondo | Ícono | Título / Descripción |
|---|---|---|---|
| **Critical Alert** | `#F8F8F8` (gris) | `passport-expired` (rojo) | negro / `#4C4C4C` |
| **High Alert** | `#FFF5F0` (peach) | `alarm-clock` (naranja) | negro / `#4C4C4C` |
| **Info** | `#FFFFFF` + borde `#E7E7E7` | `transaction` (azul) | `#1F2937` / `#6B7280` |

**Casos de uso documentados:**
| Caso | Tipo sugerido | Copy (descripción) |
|---|---|---|
| **Pago de plan rechazado** | Critical | "Un pago de plan ha fallado. Se requiere acción inmediata para evitar la interrupción del servicio." |
| **Pedidos pendientes por más de 24 horas** | High | "Uno o más pedidos llevan más de 24 horas esperando ser preparados. Revísalos y procésalos para evitar problemas de SLA." |
| **Disputas por vencer pronto** | High | "Una o más disputas vencerán en las próximas 48 horas. Responde ahora para evitar una pérdida automática." |
| **Advertencia de inventario bajo** | High/Info | "Algunos productos están por debajo del nivel mínimo de inventario. Considera reponer existencias pronto." |
| **Disputas pendientes** | Info | "Tienes disputas sin resolver que esperan una respuesta. Revísalas y actúa antes de que venza el plazo." |
| **Transacción de alto valor** | Info | "Se detectó una transacción por encima de tu límite configurado. Revísala para verificar su exactitud o evaluar el riesgo." |

> 🔴 Confirmar el **color de ícono por tipo** (rojo/naranja/azul).

## B.2 Paywall "suscripción terminada" + plan Enterprise (`668:30874`)
Reutiliza el **paywall de planes** (§10.3) con:
- **Header** (variante): **"¡Tu prueba gratuita de la tienda en línea ha terminado! Conserva tu tienda suscribiéndote a un plan"** · alterno: "Accede a todas las funcionalidades seleccionando un plan".
- **NUEVO 4º plan — Enterprise:** "**Personalizado para adaptarse a las necesidades y capacidades de tu negocio**" · features: **Hecho a tu medida**, **Escalable**, **Integraciones avanzadas** (íconos `building` / `trending-up` / `zap`). Sin precio fijo (a la medida).
> 🔴 Agregar al componente de paywall (§10.3): la **variante de header "prueba terminada"** (ya señalada en F11) y el **plan Enterprise**.

## B.3 Pantalla "Sin conexión" (`603:36118`)
Estado global: ilustración *No connection-bro* + **"¡Sin conexión a internet!"** + cuerpo + acción (reintentar).

## B.4 Pantalla "Mantenimiento" (`603:36185`)
Estado global: ilustración *Phone maintenance-pana* + **"We're currently undergoing maintenance"** + "Our team is performing some routine updates to keep things running smoothly. We'll be back online shortly — thanks for your patience."

## B.5 Componentes / patrones
- **Banner/alerta** (3 tipos por severidad) — componente nuevo.
- **Carrusel de banners + dots** de paginación (arriba del Home).
- **Estado global full-screen** (ilustración + título + descripción + acción) — mismo molde que *Sync Error* (§S.3) y éxito de activación; refuerza el **componente de estado** parametrizable.

## B.6 Pendientes (🔴)
1. 🔴 Color de ícono por severidad.
2. 🔴 Sumar **Enterprise** + header "prueba terminada" al paywall (§10.3).
3. Comportamiento del **chevron** del banner (navega al detalle) y del **carrusel** (auto-rotación / prioridad por severidad).
4. Ilustraciones (*No connection-bro*, *Phone maintenance-pana*) — placeholders en el demo.
5. Íconos `passport-expired`, `alarm-clock`, `transaction`, `building`, `trending-up`, `zap` → `icons.ts`.

## B.7 Referencias
- *Banner Use Cases* (`603:34724`): Banners Home `1990:141592` · Suscripción terminada `668:30874` / Select plan `668:31867` · Sin conexión `603:36118` · Mantenimiento `603:36185`

---

# Nova AI — Chat ("Preguntarle a Nova", transversal)

> Chat con el asistente **Nova AI**. Se abre desde el **FAB de Nova** (orbe morado) del Home. Modal a pantalla (bg blanco, esquinas superiores redondeadas 12) sobre el home atenuado.
> **Figma:** *Nova AI* (`605:38095`).

## N.1 Estructura de la pantalla
- **Header** (56h): título **"Preguntarle a Nova"** (`Inter Medium 16`, centrado) + **X cerrar** (`icon/action/close`, derecha).
- **Área de mensajes** (scroll, x16):
  - **Burbuja de usuario** (pregunta): bg `#F8F8F8`, **pill radio 37**, `Manrope Medium 14` negro, **alineada a la derecha**, sin avatar.
  - **Respuesta de Nova**: **avatar** (`image 218`, círculo 28) + **burbuja** bg `#F8F8F8` **radio 19** (pt10/pb16/px12), `Manrope Medium 14` + **link CTA subrayado** (`Manrope SemiBold 12` `#4C4C4C`). Alineada a la izquierda.
- **Barra de input** (330w, abajo):
  - **Campo** pill bg `#F8F8F8` **radio 61** (50h) + placeholder **"Escribe lo que quieras..."** (`Manrope Medium 12`, opacidad 60) + **mic** (círculo blanco 32, `mic-02`) dentro del campo a la derecha.
  - **Botón enviar**: círculo rojo `#DB3B2B` (50) con `material-symbols:send-outline` (blanco).

## N.2 Estados
1. **Un intercambio** (`43:2009`): 1 pregunta + 1 respuesta.
2. **Envíos** (`435:44674`): respuesta con datos multilínea.
3. **Conversación multi-turno** (`43:2057`): varias preguntas/respuestas scrolleadas.
4. **Grabación de voz** (`43:5519`): al tocar el **mic**, la barra cambia a → **X cancelar** + **waveform** + **timer "00:33"** + **enviar**.
5. **Mensaje de voz enviado** (`43:5930`): burbuja con **play ▶** (`iconoir:play-solid`) + **duración "0:04"** + **waveform**.
6. **Teclado abierto / escribiendo** (`43:2130`, `43:2185`): teclado iPhone + input con texto; **el mic se oculta** (solo texto + enviar).

## N.3 Prompts y respuestas de ejemplo
| Pregunta (usuario) | Respuesta de Nova | Link CTA |
|---|---|---|
| ¿Cómo va mi rendimiento hoy? | Tus ventas totales de hoy son $12,400, con 28 pedidos procesados. | Ver reporte detallado |
| ¿Cómo van mis envíos? | Aquí están los datos de tus envíos en todos los canales: Envíos totales — 88 · Envíos cancelados — 13 · Envíos T1 — 48 | Ver reporte detallado |
| Muéstrame mis productos más vendidos. | Estos son tus 3 productos más vendidos hoy: Smart Thermo Pro — 52 · Air Purifier Mini — 34 · Eco Water Bottle — 28 (unidades vendidas) | Ver todos los productos |
| ¿Cuántos pedidos pendientes tengo? | Actualmente tienes 7 pedidos pendientes. 4 están esperando pago y 3 están listos para envío. | Abrir página de pedidos |

## N.4 Componentes nuevos
- **Burbuja de chat** (usuario pill / Nova con avatar + link CTA subrayado).
- **Avatar de Nova** (círculo 28).
- **Barra de input de chat** (campo pill + mic + enviar).
- **Grabador de voz** (X + waveform + timer + enviar).
- **Mensaje de voz** (play + duración + waveform).

## N.5 Notas de tipografía
- **Header** en `Inter Medium 16`.
- **Mensajes y placeholder en `Manrope Medium 14/12`** — nueva anomalía Manrope dentro del App (van 5: F7 tarifas, F9 contador, F10 paywall, F12 etiquetas de política, y **el chat de Nova**). Probable **componente de chat compartido**.
- Link CTA `Manrope SemiBold 12`, subrayado — **`#4C4C4C` aquí, pero `#DB3B2B` en la integración con Pedidos** (§N.10).

## N.6 Pendientes (🔴)
1. 🔴 Confirmar si el chat es **Manrope intencional** (componente compartido) o debe migrar a Inter (App = Inter-only).
2. Avatar real de Nova (`image 218`).
3. Estado **"Nova está escribiendo"** (typing) — no visto en Figma, confirmar si existe.
4. Comportamiento del **mic** al escribir (se oculta).
5. Íconos `mic-02`, `material-symbols:send-outline`, `iconoir:play-solid`, `icon/action/close` → `icons.ts`.

## N.7 Referencias
- *Nova AI* (`605:38095`): 1 intercambio `43:2009` · Envíos `435:44674` · Multi-turno `43:2057`/`43:5678` · Grabación `43:5519` · Mensaje de voz `43:5930` · Teclado `43:2130`/`43:2185`

---

## N.8 Integración con Pedidos (Nova Integration — Orders)

> Sección **"Nova Integration (Orders)"** (`435:41638`) — **3 pantallas**. Extiende el chat de Nova (§N.1) con **resultados enriquecidos**: Nova responde con **tarjetas de pedido reales** embebidas en la conversación, no sólo texto.

### N.8.1 Anatomía de la respuesta con resultados

Orden fijo dentro de la columna de chat (`x16`, `w328`, `gap 12`):

```
[Burbuja de usuario]                    ← derecha, pill
[Avatar + burbuja de Nova]              ← izquierda, con link CTA
[Tarjeta de pedido compacta]  ┐
[Tarjeta de pedido compacta]  ├─ Frame de resultados (328×292, gap 4)
[Botón "Mostrar 25 más"]      ┘
```

### N.8.2 Tarjeta de pedido compacta — `435:41839`
Variante **reducida** de la tarjeta del listado (§13.3): **`bg #F8F8F8`** (gris, no blanca), radio 12, **alto fijo 126**, contenido `296` a `16px`, `gap 16`.
- **Cabecera:** nombre (**`B1 S`** — Inter SemiBold 16) + **`#394030`** (**`B3 S`** — Inter SemiBold 12, `#4C4C4C`) | **chip** de estado + **kebab** (`more-horizontal` rotado, 20).
- **Divisor** → **pie:** `calendar-03` (20) + fecha (`B3 M` 12 negro) + **"3 envíos"** (`B3 M` 12, `#1F2937`).

> **Las filas Producto / Monto / Pedido vía están OCULTAS** en Figma (`hidden=true` en `435:41854`), igual que el avatar. La tarjeta es una versión **compacta a propósito**: sólo identidad + estado + fecha.

> 🔴 **Tres jerarquías distintas para el mismo par "identificador + subtítulo":**
> | Superficie | Nombre / ID | Subtítulo |
> |---|---|---|
> | Tarjeta del listado (§13.3, §CA.3.6) | `B1 M` (Medium 16) | `B3 R` (Regular 12) |
> | Header del detalle (`171:16844`) | `B1 S` (SemiBold 16) | `B3 R` (Regular 12) |
> | **Tarjeta de Nova** (`435:41844`) | **`B1 S`** | **`B3 S`** (SemiBold 12) |
>
> Definir una sola regla.
> 🔴 **Fondo gris (`#F8F8F8`) en vez de blanco** — la tarjeta del listado es blanca con borde `#F3F3F3`. Aquí no hay borde.
> 🔴 **El alto fijo de 126px rompe el padding:** en `435:41824` el nombre "Javari Mena" **envuelve a dos líneas** y el contenido crece a 109px → el padding inferior queda en **1px** (debería ser 16). Con nombres largos, la tarjeta se desborda.

### N.8.3 Botón "Mostrar 25 más" — `435:41941`
Ancho completo, **h32**, radio 8, texto **Inter SemiBold 12** `#DB3B2B` **subrayado**, centrado.

> 🔴 **Relleno fantasma:** `bg rgba(244,244,244,0)` — un color con **alfa 0** en vez de "sin relleno". Limpiar.

### N.9 Las 3 pantallas (prompts y respuestas)

| # | Nodo | Pregunta (usuario) | Respuesta de Nova | Chip de las tarjetas |
|---|---|---|---|---|
| 1 | `435:41824` | Filtrar pedidos de Amazon | "Claro, aquí está la lista de tus pedidos de Amazon." | **Pago pendiente** |
| 2 | `435:41958` | Buscar el pedido de María | "Claro, aquí está la lista de pedidos a nombre de María:" | Pago pendiente |
| 3 | `435:42092` | Pedidos cancelados esta semana | "Aquí está la lista de todos los pedidos cancelados esta semana:<br>Total de pedidos cancelados — 52" | **Cancelado** |

Las tres usan el mismo link CTA: **"Ir a la página de pedidos"**.

> ⚠️ **Pantalla 1 — incoherencia de datos:** el usuario pide *pedidos de Amazon*, pero las tarjetas **no muestran el canal** (la fila "Pedido vía" está oculta). El resultado no evidencia por qué esos pedidos responden al filtro.

## N.10 🔴 Divergencias con el chat de Nova base (§N.1)

Misma pantalla, dos secciones de Figma que **no coinciden**:

| Elemento | Nova AI base (`43:2009`) | Nova Integration — Orders (`435:41824`) |
|---|---|---|
| **Título del header** | `T3 M` — Inter **Medium** 16 | **`T3 S`** — Inter **SemiBold** 16 |
| **Link CTA de la burbuja** | `#4C4C4C` (gris) | **`#DB3B2B`** (rojo) |
| Burbuja de usuario | posición **absoluta** (`left: 101`) | **alineada a la derecha** (`right: 0`) ✅ correcto |
| Inicio de la columna de chat | `top: 72` | `top: 75` |

**Iguales en ambas:** panel blanco `h728` anclado abajo con **radio superior 12**, scrim **`rgba(0,0,0,0.7)`** sobre la captura de fondo (`image 334`), burbujas en **Manrope**, barra de input (campo pill radio 61 + mic 32 + enviar `#DB3B2B` 50).

**Cuál es el canónico (verificado):**
- **Título → `T3 S`.** El resto de la App usa `T3 S` en los headers: detalle de pedido (`171:16856`), asistente Crear pedido (`4179:22826`) y esta sección. **El outlier es el Nova base** (`T3 M`) — hay que corregirlo ahí, no aquí.
- **Link CTA → `#DB3B2B`.** Coherente con el sistema: las acciones y los links son rojos. El gris `#4C4C4C` del Nova base se lee como texto inerte.
- **Burbuja de usuario → alineada a la derecha** (la posición absoluta del Nova base es frágil).

## N.11 Componentes nuevos (vs. §N.4)
- **Tarjeta de pedido compacta en chat** (`bg #F8F8F8`, sin borde, filas de detalle ocultas).
- **Bloque de resultados** dentro de la burbuja de conversación (tarjetas + botón de paginación).
- **Botón de texto subrayado** ("Mostrar 25 más") — `h32`, radio 8, sin relleno.

## N.12 Pendientes (🔴)
1. 🔴 **Corregir el Nova base (`43:2009`), no esta sección:** su título debe pasar a **`T3 S`** y su link CTA a **`#DB3B2B`** — §N.10.
2. 🔴 **Pesos de la tarjeta** distintos a los del listado (`B1 S`/`B3 S` vs `B1 M`/`B3 R`) y **fondo gris sin borde**.
3. 🔴 **Alto fijo de 126px:** con nombre de dos líneas el padding inferior colapsa a 1px.
4. 🔴 **Relleno `rgba(244,244,244,0)`** (alfa 0) en el botón "Mostrar 25 más".
5. ⚠️ **El filtro de Amazon no muestra el canal** en las tarjetas (la fila "Pedido vía" está oculta), lo que no evidencia por qué esos pedidos responden al filtro.
6. ⚠️ **El kebab de la tarjeta en el chat no tiene menú** (mismo hueco que §D y §CA).
7. **Sin estados** de carga ("Nova está escribiendo"), de **sin resultados**, ni de error de la consulta.
8. **Sin definir** qué pasa al tocar una tarjeta (¿abre el detalle §D? ¿cierra el chat?).

## N.14 Referencias — Integración con Pedidos
- *Nova Integration (Orders)* (`435:41638`) — 3 pantallas: Amazon `435:41824` · María `435:41958` · Cancelados `435:42092`.
- Reutiliza: shell del chat §N.1 · tarjeta de pedido §13.3 (compacta) · chips §D.3.

---

## N.15 Integración con Productos (Nova Integration — Products)

> **Sección "Nova Integration (Products)"** (`433:25412`). Es el conjunto de **capacidades de Nova aplicadas al área de Productos**: consultar pedidos pendientes, productos con poco inventario, más vendidos, y disparar acciones (crear producto con foto, conectar canal). **8 pantallas** que muestran la conversación acumulándose turno a turno. Reutiliza el shell del chat de Nova (§N.1).
> **Figma:** `433:25412`. **Owner:** Karla Salazar — Head of UX/UI.

### N.15.1 Shell (confirmado `433:35019`)
Nova es un **bottom sheet modal** (bg blanco, esquinas superiores r12, 728h) sobre el contenido **atenuado al 70%** (`rgba(0,0,0,0.7)`). Header **"Preguntarle a Nova"** (`Inter SemiBold 16`, centrado) + **X** (`icon/action/close`). Barra de input abajo (§N.1). Igual que el chat base.

### N.15.2 Capacidades documentadas (una por pantalla)
| # | Prompt (chip usuario) | Respuesta de Nova | CTA | Respuesta enriquecida |
|---|---|---|---|---|
| 1 | **Ver pedidos pendientes** (`433:35019`) | "Claro, aquí está la lista de tus pedidos pendientes." | **Ir a la página de pedidos** | 3 **tarjetas de pedido** + "Ver 15 más" |
| 2 | **Productos con poco inventario** (`435:41158`) | "Claro, aquí está la lista de productos con poco inventario." | **Ir a productos** | **tarjeta de producto** con "Inventario total: 12/28" |
| 3 | **Producto más vendido** (`435:44613`) | "Aquí están tus productos más vendidos esta semana: …" | **Ir a productos** | lista de ranking (Smart Thermo Pro 52 · Air Purifier Mini 34 · Eco Water Bottle 28) |
| 4 | **¿Qué producto se vendió más hoy?** (`434:36333`) | "Aquí están tus productos más vendidos hoy: …" | **Ver todos los productos** | ranking del día |
| 5 | **Ver productos con poco inventario** (`434:36744`) | "Aquí está la lista de productos con poco inventario:" | **Ir a inventario** | tarjeta de producto |
| 6 | **Crear producto con foto** (`434:37326`) | "Sure, Let's create a product with photo." | — | [nota diseñador] *"Redirigir al usuario al flujo de agregar producto con IA"* (§PG) |
| 7 | **Conectar canal de Amazon** (`434:37794`) | "Sure, Let's connect your Amazon channel" | — | [nota diseñador] *"Redirigir a agregar canal"* |

> Las pantallas 4–8 muestran la **conversación acumulada** (todos los turnos anteriores + el nuevo), no pantallas aisladas — es el historial creciendo. Los prompts se ofrecen como **chips sugeridos** (pill `#FFF0EF` rosa claro, `Manrope Medium 14`, alineados a la derecha como burbuja de usuario).

### N.15.3 Tarjeta de pedido en el chat (`433:35670`)
Card `#F8F8F8` r12 (132h): **nombre** ("Javari Mena", `Inter SemiBold 16`) + **folio** ("#394030", `#6B7280` 12) + **chip "Pago pendiente"** (`#E7E7E7`/`#6B7280`) + **more-horizontal** (rotado 90°) + divisor + **fecha** (`calendar-03` + "14:24 - 23 de oct, 2025") + **"3 envíos"** (rojo `#DB3B2B`, derecha). Cierra con **"Ver 15 más"** (link rojo subrayado).

### N.15.4 Tarjeta de producto en el chat (`435:44590` / `435:44601`)
**Una tarjeta por producto** (no una combinada). Card `#F8F8F8` r12 (123h): **thumbnail** (40px, borde `#F3F3F3` r8) + **nombre** (2 líneas, `Inter SemiBold 14`, ellipsis) + divisor + **"Inventario total:"** + **cifra** (`Inter SemiBold 14`). En el ejemplo, dos tarjetas con **12** y **28** respectivamente. Cierra con CTA **"Mostrar 25 más"** (link rojo subrayado).

> 🔴 **Corrección:** son tarjetas **separadas** por producto (cada una con su inventario), no una tarjeta con "12/28".

### N.15.5 CTA de acción (redirección)
Las capacidades 6 y 7 no muestran datos: Nova **confirma y redirige** a un flujo existente de la App:
- **Crear producto con foto** → flujo de **agregar producto con IA** (§PG).
- **Conectar canal de Amazon** → flujo de **agregar canal de venta** (§PE / admin canales §PJ.5).

> ✅ **Nova como orquestador:** no solo responde consultas, también **lanza flujos** de la App (crear producto, conectar canal). Es el hilo que conecta Nova con Productos, Inventario, Pedidos y Canales.

### N.15.6 Hallazgos (🔴)
1. 🔴 **Chip de pedido "Pago pendiente"** usa gris `#E7E7E7`/`#6B7280` (no el chip de estado de Pedidos §D.3) — confirmar consistencia con el sistema de chips de estado de pedido.
2. 🔴 **Manrope** en burbujas y chips sugeridos (`#FFF0EF`) — misma anomalía del chat de Nova (§N.5). El chat es un componente Manrope.
3. ⚠️ **Prompts sugeridos**: confirmar si son chips fijos de onboarding o sugerencias dinámicas.

### N.15.7 Componentes nuevos (vs §N.4/§N.11)
- **Chip de prompt sugerido** (pill `#FFF0EF` rosa claro) — N.15.2.
- **Tarjeta de pedido en chat** (compacta, con "Ver N más") — N.15.3.
- **Tarjeta de producto en chat** (con inventario) — N.15.4.
- **CTA de redirección a flujo** (crear producto / conectar canal) — N.15.5.

### N.15.9 Referencias — Integración con Productos
- *Nova Integration (Products)* (`433:25412`) — 8 pantallas Nova AI: `433:35019` · `435:41158` · `435:44613` · `434:35933` · `434:36333` · `434:36744` · `434:37326` · `434:37794`.
- Reutiliza: shell del chat §N.1 · tarjeta de pedido §N.15.3 · chips §D.3. Redirige a: agregar producto IA §PG · canales §PE/§PJ.5.

---

# Estados de la sección de alertas (Alert Section States, transversal)

> Estados de la **sección de alertas del Home** (el carrusel de banners de §B.1). Contexto: Home de **T1envíos** (Shipping). Incluye notas de desarrollo del diseño.
> **Figma:** *Alert Section States* (`1399:69897`).

## AS.1 Con alertas (default)
Carrusel de banners (Critical/High/Info, §B.1) + dots + nota **"Última actualización: hace 2 horas. Actualizar ahora"** debajo. Casos de uso en contexto de **envíos**:

> **Color del Critical Alert aquí = `#FFF0EF` (Primary/100, rosado)** — título Inter SemiBold 14 negro, desc Regular 12 `#4C4C4C`, ícono rojo. 🔴 **Inconsistencia:** en *Banner Use Cases* (§B.1) el Critical Alert aparece con fondo `#F8F8F8` (gris); aquí es `#FFF0EF` (rosado). El rosado (Primary/100) es el que corresponde a la semántica crítica/error y el confirmado en pantalla — definir como canónico y alinear §B.1.
| Severidad | Ícono | Título | Descripción |
|---|---|---|---|
| **Critical** | `package-process-01` | Sobrepesos sin responder | Hay casos de sobrepeso que deben responderse en 24h. De lo contrario, serán cancelados. |
| **High** | `money-receive-01` | Saldo bajo | Se detectó saldo bajo. Tu saldo está por debajo de 2× tu gasto diario promedio. |
| **Info** | `calendar-03` | Recolección programada para hoy | La recolección está programada para hoy. Asegúrate de que todo esté listo para ser recolectado. |

## AS.2 Cargando (skeleton)
Los banners se muestran como **skeleton** (bloques vacíos 328×109/93) + dots. Ver §L (Loaders y Skeletons).

## AS.3 Error
Bloque **centrado**: `information-circle` (24) + **"No pudimos cargar tus alertas"** (Inter Regular 14 `#4C4C4C`) + botón **"Reintentar"** (bordeado `#F3F3F3`, radio 8, h32, ícono `refresh` 12 + Inter Medium 12 **texto rojo `#DB3B2B`**).
> **Nota dev:** si **falla 3 veces** → mostrar un mensaje de reintento y **ocultar el bloque**.

## AS.4 Sin conexión (offline)
Bloque **centrado**: `cellular-network-offline` (24) + **"Sin conexión - Las alertas se actualizarán cuando te reconectes"** + botón **"Reintentar"**. Es un estado **cross-section**; además:
- **Métricas**: nota **"Última actualización: hace 2 horas. Actualizar ahora"**.
- **Nova Insights**: chip de estado + **"Información de tu última conexión"** (datos en caché).

## AS.5 Vacío (sin alertas)
El **bloque NO aparece** — **no** se muestra un mensaje tipo "no tienes alertas"; el **espacio se recupera** para las demás secciones (el Home arranca directo en "Configurar cuenta").
> 🔴 **Nota dev:** *"The block does NOT appear (don't show 'You have no alerts') Space is recovered for other blocks"*.

## AS.6 Componentes / patrones
- **Bloque de estado de sección** (ícono centrado + texto `#4C4C4C` + botón **"Reintentar"** con texto rojo) — reutilizable para **error** y **offline**.
- **Skeleton de banners** (§L).
- **Nota de frescura** "Última actualización … · Actualizar ahora" (dato + link de refresco).
- **Regla de espacio recuperado**: cuando la sección está vacía, se **oculta** (no empty-state con copy).

## AS.7 Pendientes (🔴)
1. 🔴 Estilo/color del link **"Actualizar ahora"** y de **"Información de tu última conexión"**.
2. Confirmar si estos estados (error/offline/loading/empty) aplican también a **Métricas** y **Nova Insights** o solo a Alertas.
3. Íconos `information-circle`, `cellular-network-offline`, `package-process-01`, `money-receive-01`, `calendar-03` → `icons.ts`.

## AS.8 Referencias
- *Alert Section States* (`1399:69897`): Con alertas `1991:160450` · Cargando `1991:157713` · Error `1991:158618` · Offline `1991:161433` · Vacío `1991:159517`

---

# Estados del checklist de configuración (Setup Checklist States, transversal)

> Estados de la sección **"Configurar cuenta"** del Home (contexto T1envíos). Figma nombra 5 estados + el normal. Incluye notas de desarrollo.
> **Figma:** *Setup Checklist States* (`1336:103820`).

## CL.1 Normal (con items)
Sección "Configurar cuenta" con chip **"N de 5 completados"** + tarjetas de setup (ícono en círculo peach + título + botón contextual). Ver §H / flujos.

## CL.2 Estado de carga (Loading) — `1991:162385`
**Skeleton**: cada tarjeta muestra placeholder de ícono (40×40) + **2 líneas skeleton** (51×15 y 120×15) + botón; chip también skeleton. Ver §L.

## CL.3 Estado vacío (Empty) — `1991:163234`
El **bloque no aparece**; el Home arranca directo en **Métricas**. **Espacio recuperado** (consistente con AS.5). Sin mensaje "no tienes tareas".

## CL.4 Estado de completado (Completed) = pantalla de éxito — `1366:49767` / `1332:19020`
Al completar el checklist:
- **Celebración efímera (3 s):** modal **"¡Listo! Tu negocio está configurado"** + **`checkmark-badge-02`** (150px, verde) + **confeti** + botón **"Empezar a vender"** (bordeado `#F3F3F3`, radio 12, con flecha `arrow-right-02-round`).
- Luego **el bloque desaparece** y **ya no vuelve a aparecer**.
- **Tokens:** título Inter **SemiBold 18** negro centrado (tracking −0.36); cuerpo Inter Regular 14 `#4C4C4C`; modal blanco **radio 24** (328×418) sobre fondo atenuado (`rgba(0,0,0,.4)`).
- **Nota dev:** *"Block disappears · First time completing: Ephemeral celebration (3 seconds) · Message 'All set! Your business is configured' · Then block doesn't appear anymore"*.

## CL.5 Estado de error (Error) — `1991:164410`
Bloque **centrado**: `information-circle` (24) + **"No pudimos cargar tu progreso"** (Inter Regular 14 `#4C4C4C`) + botón **"Reintentar"** (bordeado, texto rojo `#DB3B2B`).
- **Nota dev:** *"If fails: Temporarily hide and show on refresh"*.

## CL.6 Estado sin conexión (Offline) — `1991:176072` / `1991:176921`
- Muestra el **último estado conocido (caché)** + **badge "Offline"** (chip junto al título).
- Al **intentar completar un paso** → mensaje **"You need connection to save your progress"**.
- **Nota dev:** *"Show last known state (from cache) · Badge: 'Offline' · When trying to complete step: Message 'You need connection to save your progress'"*.

## CL.7 Componentes / patrones
- **Skeleton de tarjeta de checklist** (ícono + 2 líneas + botón).
- **Bloque de estado** reutilizado (ícono + texto + "Reintentar") — mismo molde que AS.3.
- **Pantalla de éxito / celebración efímera** (checkmark-badge + confeti + CTA).
- **Badge "Offline"** + **mensaje inline** al intentar completar sin conexión.
- **Regla de espacio recuperado** (vacío y completado ocultan el bloque).

## CL.8 Pendientes (🔴)
1. Duración/animación exacta de la **celebración efímera** (3 s) y su transición al ocultar el bloque.
2. Íconos `checkmark-badge-02`, `information-circle`, `cellular-network-offline`, `arrow-right-02-round` → `icons.ts`.
3. Confirmar si "completado" y "vacío" comparten la misma regla de ocultar/recuperar espacio.

## CL.9 Referencias
- *Setup Checklist States* (`1336:103820`): Carga `1991:162385` · Vacío `1991:163234` · Completado `1366:49767`/`1366:49779` · Error `1991:164410` · Sin conexión `1991:176072`/`1991:176921`
- Pantalla de éxito también en `1332:19020`.

---

# Estados del bloque de métricas (Metrics Block States, transversal)

> Estados del **bloque de Métricas** del Home (contexto T1envíos / Shipping). Reutiliza la **tarjeta de métrica** (§H.3.5) y las **reglas de datos** (§H.4); aquí se documenta su **máquina de estados**. Resuelve el pendiente §H.5·5.
> **Figma:** *Metrics Block States* (`1366:50557`).

## M.1 Con datos (Cache Data) — `1991:170465`
Header **"Métricas / Hoy"** + carril de 6 tarjetas pobladas (§H.4) con sus deltas. Debajo del carril:
- **Nota de frescura:** **"Datos de hace 2 horas. Cargar ahora"** (Inter Medium 12 `#4C4C4C`, centrado; *"Cargar ahora"* = refrescar).
- **Botón secundario full-width:** **"Ver reporte detallado →"** (§H.3.5).
- **Nota dev (@devs):** *"Show cached data if available with badge 'Data from X ago'"* — hoy se resuelve como nota de texto, no como chip.

## M.2 Cargando (skeleton) — `1991:167471`
Header y botón inferior en skeleton. Cada una de las 6 tarjetas muestra placeholders en **Greys/900 `#F8F8F8`**: barra de label (15px, radio 3), placeholder de valor (71×32, radio 8) y placeholder de ícono (26×26, radio 6). Ver §L.
> **Nota dev (@devs):** *"Skeleton cards with large number + label shape · Maintain grid layout · Maximum duration: 5 seconds"*.

## M.3 Vacío (empty / no activity) — `1991:168503`
**Diverge del patrón §AS.5 / §CL.3:** el bloque **no se oculta**; muestra un **empty-state de onboarding**:
- **Ilustración** `Logistics-rafiki 1` (150×123, Freepik).
- **Título:** "Aún no tienes envíos" (Inter SemiBold 16 negro, tracking −0.32).
- **Subtítulo:** "Crea tu primera guía para ver tus estadísticas" (Inter Regular 14 `#4C4C4C`).
- **CTA:** secundario full-width **"Cotizar envío →"** (mismo botón que "Ver reporte detallado").

Sin header "Métricas / Hoy" ni carril.

## M.4 Error — `1991:169631`
Conserva el header "Métricas / Hoy". Usa el **bloque de estado reutilizable** (§AS.6): `information-circle` (24) + **"No pudimos cargar tus métricas"** (Inter Regular 14 `#4C4C4C`, centrado) + botón **"Reintentar"** (bordeado `#F3F3F3`, radio 8, h32, ícono `refresh` 12 + Inter Medium 12 **texto rojo `#DB3B2B`**).

## M.5 Sin conexión (offline) — `1991:177349`
Estado **cross-section** (mismo evento que §AS.4 y §CL.6), a **pantalla completa**:
- **Bloque superior** (reemplaza a alertas): `cellular-network-offline` (24) + **"Sin conexión - Las alertas se actualizarán cuando te reconectes"** + botón **"Reconectar"** (mismo molde que "Reintentar"; sólo cambia el label).
- **Métricas:** carril poblado (caché) + nota **"Última actualización: hace 2 horas. Actualizar ahora"**.
- **Configurar cuenta** y **Nova Insights:** chip de estado (~86px, badge offline); Nova añade **"Información de tu última conexión"**.

## M.6 Componentes / patrones
- **Tarjeta de métrica** (§H.3.5) + **reglas de datos** (§H.4) — sin cambios.
- **Skeleton de tarjeta de métrica** (label + valor + ícono) — variante de §L.
- **Bloque de estado** reutilizado (ícono + texto `#4C4C4C` + botón "Reintentar"/"Reconectar" con texto rojo) — mismo molde que §AS.6 / §CL.7.
- **Nota de frescura** (dato + link de refresco).
- **Empty-state de onboarding** (ilustración + título + subtítulo + CTA) — **no** recupera espacio (a diferencia de §AS.5 / §CL.3).

## M.7 Pendientes (🔴)
1. 🔴 **Badge "Data from X ago":** la nota dev pide un **badge**; hoy es nota de texto. Definir si se estandariza a chip.
2. 🔴 **Verde de delta positivo:** dentro de *Envíos* conviven **dos verdes** — `#4FC153` (Incidencias) y `#16A34A` (Saldo) — que se suman al `#51AF70` de otras variantes. **Amplía §H.5·7:** el token de "tendencia positiva" tiene **3 hex** en uso.
3. Confirmar que el **empty-state con CTA** (no ocultar) es intencional y no colisiona con la regla de espacio recuperado de §AS.5 / §CL.3.
4. Íconos a `icons.ts`: `analytics-01`, `information-circle`, `cellular-network-offline`, `refresh`, `arrow-right-02-round`, `shipping-loading`, `truck-delivery`, `package-delivered`, `alert-02`, `container-truck-01`, `dollar-circle`, `auto-conversations`.

## M.8 Referencias
- *Metrics Block States* (`1366:50557`): Carga `1991:167471` · Vacío `1991:168503` · Error `1991:169631` · Cache Data `1991:170465` · Sin conexión `1991:177349`.
- Reutiliza: tarjeta de métrica §H.3.5 · reglas de datos §H.4 · loaders §L · offline cross-section §AS.4 / §CL.6.


---

# Flujo 14 — Detalle de pedido (Order Details)

> Sección **"Orders Details (userflow)"** (`290:21918`): la pantalla de detalle de un pedido y **todo su ciclo de vida**. Es el flujo más grande de la App: **62 pantallas** agrupadas en **10 estados principales**, **5 estados parciales** y **6 sub-flujos de acción**.
> **Figma:** `290:21918`. **Owner:** Karla Salazar — Head of UX/UI.
> **Entrada:** desde la tarjeta de pedido del listado (§13.3).

## D.1 Mapa del flujo

```
Detalle de pedido (#3146535)
│
├── CICLO PRINCIPAL (el estado define chip + CTA)
│   Pendiente de pago → Por preparar → Por enviar → En camino / Por recolectar
│                                                  → Entregado → Completado
│   (ramas terminales: Cancelado · Devuelto · Reembolsado)
│
├── ESTADOS PARCIALES (el pedido se divide en grupos/envíos)
│   Parcialmente preparado · enviado · entregado · cancelado · reembolsado
│
└── SUB-FLUJOS DE ACCIÓN
    ├── Preparar productos ──► Dividir pedido (multi-paquete)
    ├── Generar guía ────────► Cotizar → resumen → (sin cobertura)
    ├── Cancelar pedido / Cancelar artículo
    ├── Devolver productos
    ├── Reembolsar ─────────► modales (éxito / método vencido / +6 meses)
    ├── Notas, etiquetas y comentarios
    └── Editar contacto y direcciones
```

**Sub-secciones Figma:** Pending Payment `291:25455` · To prepare `291:25456` · To Ship `291:25866` / `4177:23610` · On the way `291:26948` / `4177:25990` · To Collect `292:36880` / `4177:25412` · Delivered `292:36025` / `4177:26602` · Completed `292:36337` · Cancel `4177:27236` · Return `4177:27765` · Refunded `4177:28153` · Partially Prepared `291:27407` · Partially Shipped `293:40481` · Partially Delivered `293:41697` · Partially Cancelled `293:42904` · Partially Refunded `293:44055` · Refund `381:34105` · Return `896:73678` · Cancel Order `896:73696` · Cancel Product (Before Shipping) `343:14994` · Add Label/Notes/Comment `381:30672` · Editar info de contacto y direcciones `4179:79155`.

## D.2 Anatomía de la pantalla (común a todos los estados)

Scroll vertical único. **La estructura no cambia entre estados; cambian el chip, el bloque de productos y la CTA.**

| Orden | Bloque | Nodo (Pendiente de pago) |
|---|---|---|
| 0 | **Header de pedido** | `171:16842` |
| 1 | **PRODUCTOS** (o bloque de envío `SH01`) | `171:16858` |
| 2 | **RESUMEN DE COBRO** (+ CTA principal) | `4098:50595` |
| 3 | **INFO DEL CLIENTE** | `4098:50614` |
| 4 | **NOTAS DEL PEDIDO** | `4098:50645` |
| 5 | **ETIQUETAS** | `4098:50653` |
| 6 | **HISTORIAL DE ACTIVIDAD** | `4098:50661` |

*(Variantes recientes añaden **INFO DEL PEDIDO** entre 1 y 2 — ver §D.4.6.)*

### D.2.1 Header de pedido — `171:16842`
- **# de pedido** `#3146535` — `B1 S` (Inter SemiBold 16, `#000`, tracking −0.32).
- **Meta:** "Creado el 29 de oct, 2024 a las 05:43 AM en `store-04` tienda en línea" — `B3 R` (Inter Regular 12, `#4C4C4C`), con ícono `store-04` (12px) **inline** antes del canal.
- **Derecha:** **chip de estado** (§D.3) + **kebab** (`more-horizontal` rotado 90°, 20px) → acciones del pedido.
- Título de pantalla: **"Detalles del pedido"** + flecha de regreso.

### D.2.2 Encabezado de bloque (patrón repetido)
`bg #F8F8F8`, `px16 py8`. Título en **`Tag S`** (Inter **SemiBold 10**, mayúsculas). Puede incluir una **línea meta** (`B3 R` `#4C4C4C`): *"Creado el 29 de oct | Sucursal: Polanco - Gestionado por vendedor"*, y (en parciales) un **chip de estado del grupo** a la derecha.

> 🔴 **Color inconsistente en los títulos de bloque:** `PRODUCTOS`, `RESUMEN DE COBRO` e `INFO DEL PEDIDO` usan **`#4C4C4C`**; `INFO DEL CLIENTE`, `ETIQUETAS` e `HISTORIAL DE ACTIVIDAD` usan **`#4B5563`** (Greys/100). Unificar.

### D.2.3 Fila de producto — `171:16862`
Miniatura **44×44** (radio 12) + columna (w186, `gap 8`) + precio a la derecha (w57).
- **Nombre** `B2 M` (Inter Medium 14, `#000`, tracking −0.28).
- **Cantidad** "1unidad" `B3 M` `#4C4C4C`.
- **Chip de variante** (opcional): `bg rgba(33,128,255,0.1)` (Overlay/Blue), texto **`#2180FF`** (Complementary/Blue), `B3 M`, radio 6 — ej. "Rosa / Niño".
- **SKU** `B3 M` `#4C4C4C`.
- **Precio** `B2 S` (Inter SemiBold 14) `#000`, derecha.

Filas separadas por divisor hairline `#F3F3F3`.

## D.3 Chip de estado — taxonomía completa

Único componente `Chips` (radio 6, `px6 py4`, `B3 M` Inter Medium 12) con **6 variantes de color** verificadas:

| Variante | Fondo | Texto | Borde | Se usa en |
|---|---|---|---|---|
| **Neutral** | `#F8F8F8` | `#4C4C4C` | — | Pendiente de pago · Por preparar · Por enviar · En camino · Por recolectar |
| **Éxito** | `#F0FDF4` (Green/500) | `#51AF70` (success) | — | **Entregado** · **Completado** |
| **Destructivo** | `#F8F8F8` | `#DB3B2B` (Primary/600) | — | "Cancelados (3)" (en INFO DEL PEDIDO) |
| **Parcial** | `#F3F3F3` | `#4B5563` | **`1px dashed #4B5563`** | Parcialmente entregado / cancelado / enviado / preparado |
| **Bordeado** | `#F8F8F8` | `#4C4C4C` | `1px #DBDBDB` | Estado **por grupo** en parciales ("Por preparar") |
| **Info / variante** | `rgba(33,128,255,.1)` | `#2180FF` | — | Variante de producto ("Rosa / Niño") |

**Tabla de estados (chip de header + CTA principal):**

| Estado | Nodo | Chip | Color | CTA principal |
|---|---|---|---|---|
| Pendiente de pago | `171:16835` | "Pendiente de pago" | neutral | **Marcar como pagado** |
| Por preparar | `171:17009` | "Por preparar" | neutral | **Preparar envío** |
| Por enviar | `171:17194` | "Por enviar" | neutral | **Generar guía** |
| En camino | `171:17392` | "En camino" | neutral | — *(sin CTA)* |
| En camino (b) | `895:69184` | "En camino" | neutral | **Marcar como entregado** |
| Por recolectar | `312:11520` | "Por recolectar" | neutral | **Imprimir guía de envío** |
| Entregado | `292:36338` | "Entregado" | **verde** | — |
| Completado | `292:36610` | "Completado" | **verde** | — |
| Parcialmente preparado | `4166:113772` | "Parcialmente preparado" | punteado | 2 CTAs (una por grupo) |
| Parcialmente enviado | `4167:115279` | "Parcialmente enviado" | punteado | 2 CTAs |
| Parcialmente entregado | `4167:115550` | "Parcialmente entregado" | punteado | 1 CTA |
| Parcialmente cancelado | `293:46928` | "Parcialmente cancelado" | punteado | — |
| Parcialmente reembolsado | `293:44056` | — | — | — |
| Cancelado | `4177:27541` | — | — | — |
| Devuelto | `4177:27766` | — | — | — |
| Reembolsado | `4177:28154` | — | — | — |

> 🔴 **Contradice §13.11·2:** en el **listado** el chip de estado es siempre gris; en el **detalle** sí hay color semántico (verde/rojo/punteado). Alinear ambas superficies.

## D.4 Bloques

### D.4.1 PRODUCTOS → bloque de envío (SH01)
En "Pendiente de pago" y "Por preparar" el título es **PRODUCTOS**. En cuanto el pedido se prepara, el bloque pasa a titularse **`#3146535 - SH01`** y su meta cambia a *"Preparado el 29 de oct | Sucursal…"*. Cada envío es un bloque; **las devoluciones usan el prefijo `RE01`**.

**Multi-sucursal** (`4166:113119`): el pedido se parte en **dos bloques PRODUCTOS**, uno por sucursal (Polanco / Centro).

### D.4.2 RESUMEN DE COBRO — `4098:50595`
- **Banner de alerta** (`Messages`): `bg #FFFCE5` (Yellow/500), ícono `icon/status/alert` (24, Yellow/300 `#EDBD55`), texto `B3 M` `#1F2937`, radio 10, sombra `0 4 7 rgba(0,0,0,.05)` — *"Pago pendiente por SPEI. Vence el 23 de abril, 2025"*.
- **Filas:** label `B2 R` `#4C4C4C` ··· valor `B2 S` `#000` (w90, derecha). Subtotal · Impuestos (IVA) · Tarifa de envío · **Total**.
- **CTA principal** (§D.5).

### D.4.3 INFO DEL CLIENTE — `4098:50614`
Nombre `B2 S` + "2 pedidos" `B3 R`. Divisores entre sub-bloques:
- **Información de contacto** + link **"Editar"** (`B2 S` **negro**, no rojo) → email `B2 M`, teléfono `B3 R`.
- **Dirección de envío** + "Editar" → dirección `B3 R`.
- **Dirección de facturación** → "Igual que la dirección de envío" *(sin "Editar")*.

### D.4.4 NOTAS DEL PEDIDO — `4098:50645`
Título + nota ("Envío urgente") + link **"Editar"**. Estado vacío → input.

### D.4.5 ETIQUETAS — `4098:50653`
**Input** (h48, radio **20**, borde `0.916px #F3F3F3`) + **chips removibles** (`B3 S` Inter SemiBold 12 + `x` 12px): "Regalo", "Urgente".

### D.4.6 INFO DEL PEDIDO — `4177:27596` *(bloque nuevo)*
Aparece en variantes recientes (cancelado, editar contacto). Filas label `B2 R` ··· valor `B2 S`, con divisores: **Fecha de creación** · **Sucursal** · **Gestionado por** · **Estado** (→ **chip**, ej. "Cancelados (3)" en rojo) · **Pedido a través de**.

### D.4.7 HISTORIAL DE ACTIVIDAD — `4098:50661`
- **Input de comentario** (h48, radio 20, borde `0.916px`, placeholder "Agregar un comentario" `#C3C3C3` **13.43px**).
- **Chip de día** ("Hoy"): `bg #F3F3F3`, texto `#4B5563`.
- **Entradas:** ícono en cuadro 40×40 (radio 12, `bg #F3F3F3`) + título `B2 M` + monto `B1 R` `#4C4C4C` + hora `B2 R` `#4C4C4C`. Ej.: *"Creaste un pedido desde POS · $2,629.36 · 17:34 hrs"*, *"Pedido confirmado — $2,629.36 - Pago (por SPEI en efectivo)"* con link **"Ver comprobante de pago"**.

> 🔴 **Valores fuera de token** en los inputs de Etiquetas/Historial: borde `0.916px`, tipografía `13.43px`, radio `20`. Parece un componente **escalado** (≈0.916×). Corregir a tokens.

## D.5 CTA principal (botón grande)
`bg #DB3B2B`, **h48**, **radio 16**, `px32 py12`, label **`B1 M`** (Inter **Medium 16**, blanco, tracking −0.32), ancho completo. Vive **dentro del bloque** (RESUMEN DE COBRO o el grupo de productos), **no** en una barra fija inferior.

> ⚠️ **Difiere del botón primario del listado** (h40, radio 12, SemiBold 14). Son dos escalas distintas del mismo botón: **grande (detalle)** vs **compacto (listado/modales)**.

## D.6 Sub-flujo: Preparar productos — `171:18394` / `291:25729`
- Título **"Preparar productos"** + `#3146535`.
- **PRODUCTOS:** cada fila con **selector de cantidad** ("0/1") y **peso** ("0 kg").
- **DIRECCIÓN DE ENVÍO:** nombre + dirección + link **"Ver mapa"** + "Editar".
- **NOTAS DEL PEDIDO.**
- **RESUMEN:** "Preparando desde Polanco" · "0 de 3 artículos".

**Dividir pedido** (`4177:25091` / `4177:25189`): variante con título **"Dividir pedido"** y bajada *"Selecciona los productos que quieres que contenga este paquete."* → genera múltiples paquetes (origen de los estados parciales).

## D.7 Sub-flujo: Generar guía (Manual Guide) — 7 pantallas
1. **Generar guía** (`344:16020` / `346:15534`): **Direcciones** (Origen / Destino + "Editar") · **"Selecciona el tipo de guía"** → **Guía T1** / **Guía propia** · dimensiones **Largo/Ancho/Alto** (cm) + **Peso** (Kg) · cálculo **Peso físico / Peso volumétrico / Peso a cotizar** · **Valor del producto**.
2. **Cotizar — lista de paqueterías** (`344:24852`): tarjetas por carrier (**FedEx**, **Redpack**, **UPS**) con servicio ("Mismo día / 24H", "Servicio express"), **Entrega estimada**, **Precio** ($143.00-MXN) y *"Incluye seguro y zona extendida"*.
3. **Cotizar — resumen** (`344:29466`): Precio de envío · Cantidad de paquetes · Costo de seguro · **Monto total** + aviso *"Para programar una recolección, hazlo en la sección de recolecciones"*.
4. **Sin cobertura** (`344:24424`): *"No encontramos cobertura para tu envío."* + *"Ninguna de nuestras paqueterías tiene cobertura en la dirección…"*.
5. Variantes: `345:16217` · `346:15661` (guía propia / campos).

## D.8 Sub-flujos: cancelar, devolver, reembolsar

### D.8.1 Cancelar pedido — `896:73712` / `4177:31637` / `4177:31702`
Sheet: **"Motivo de cancelación *"** → **select** (h46, radio 12, borde `#F3F3F3`, placeholder "Selecciona un motivo" `B3 M` `#4C4C4C`, `arrow-down-01` 20px) + **checkbox** "Reponer inventario" (16px, radio 4, `bg #DB3B2B` activo).
- Aviso condicional (**anotación Figma: "solo se muestra en caso de pedido pagado"**): *"Al cancelar este pedido, el reembolso se procesará automáticamente al método de pago original. Para pagos realizados con SPEI, deberás completar el reembolso manualmente desde los detalles del pedido."*

### D.8.2 Cancelar envío — `795:68062`
Modal: *"Cancelar envío"* — *"Al cancelar envío tu pedido regresara a estatus "Por preparar""*. Ícono `cancel-circle`.

🔴 **Dos inconsistencias del propio modal** (vs. el patrón de §13.8):
- **Scrim `rgba(0,0,0,0.4)`** — todos los demás modales usan **`0.2`**.
- **Botón secundario "Cancelar"** — los demás usan **"Cerrar"**. Aquí además genera ambigüedad: "Cancelar" (cerrar el modal) junto a "Sí, cancelar" (ejecutar la cancelación).

### D.8.3 Cancelar artículo (antes de enviar) — `343:15661` / `343:15718`
- **"Selecciona el producto a cancelar"** → filas con selector "0/1" → "1/1".
- **Motivo de cancelación *** (select) → ej. "El cliente canceló el pedido".
- **RESUMEN:** vacío → *"No hay productos seleccionados"*; con selección → "Productos cancelados (2)" · $1198.00 · **IVA** $65.00 · **Reembolso esperado** $00.00.
- Modal `4177:31606`: *"Cancelar productos — Al cancelar, el reembolso se procesará automáticamente al método de pago…"*

### D.8.4 Devolver productos — `896:73100` / `896:73371` / `896:73499`
Filas con precio + selector ("0/1"). Al seleccionar aparece **"Motivo de devolución *"**.
**RESUMEN DE COBRO:** "Productos devueltos (1)" · $650.00 · **VAT** $65.00 · **Reembolso esperado** $00.00 · *"Sin envío requerido"*.

### D.8.5 Reembolso — `905:41311` / `905:41423` / `4112:35436` / `4177:29997`
- Filas de producto + **"Reponer en:"** (sucursal: Polanco / CDMX).
- **RESUMEN:** "Subtotal del producto (1)" · **Reembolso total**.
- **Monto del reembolso:** modo **Manual** + *"$1,797.00 disponibles para reembolso"*.
- **Validación** (`4177:29997`): *"No se puede reembolsar más del monto disponible"*.
- **Checkbox:** *"Notificar al cliente una vez que se procese el reembolso"*.
- Estado vacío: *"No se han seleccionado productos"*.

**Modales de reembolso** (mismo componente que §13.8, radio 16, ícono en círculo 64):

| Nodo | Título | Cuerpo | Botones |
|---|---|---|---|
| `4177:31471` | Reembolsar | "¿Estás seguro de que quieres reembolsar? Contacta a tu cliente para…" | Cerrar + primario |
| `4177:31510` | Reembolsar | "¿Estás seguro de que quieres reembolsar? El reembolso se efectuará…" | Cerrar + primario |
| `4177:31533` | Reembolsar | "No se **puedo** procesar el reembolso porque el método de pago ha vencido." | **1 botón "Aceptar"** (ícono `redo`) |
| `4177:31556` | Reembolsar | "No se pudo procesar el reembolso porque han pasado más **e** 6 meses desde la fecha de pago." | **1 botón "Aceptar"** (ícono `redo`) |
| `4177:31587` | **Reembolso realizado** | "Tu cliente recibirá el monto en su método de pago los próximos días." | **1 botón "Aceptar"** (rojo, full-width, h40, radio 12) |

## D.9 Sub-flujos: notas/etiquetas y edición

- **Add Label/Notes/Comment** (`381:29767` · `381:30096` · `381:30417` · `381:30673` · `381:30913`): 5 variantes del detalle mostrando los estados **vacío → con contenido** de NOTAS, ETIQUETAS y el comentario del HISTORIAL.
- **Editar info de contacto y direcciones** (`4179:80257` · `4179:80471`): formulario de dirección — **Direcciones guardadas** · Calle · Número exterior · Número interior (opcional) · Código postal · Colonia · Estado.

## D.10 Pendientes (🔴)

1. 🔴 **Sin color destructivo propio** — el CTA destructivo reutiliza `#DB3B2B` (ver §13.11·6). *Aquí se agrava:* el mismo rojo marca "Cancelados (3)" (estado) y las CTAs primarias.
2. 🔴 **Chip de estado: listado vs detalle.** El listado los pinta siempre gris (§13.11·2); el detalle usa verde/rojo/punteado. **Definir la paleta de estados única** y aplicarla en ambas superficies.
3. 🔴 **Títulos de bloque con dos grises** (`#4C4C4C` vs `#4B5563`).
4. 🔴 **Valores fuera de token** en inputs (borde `0.916px`, texto `13.43px`, radio 20) — componente escalado.
5. 🔴 **Modal "Cancelar envío" fuera de patrón** (§D.8.2): scrim `0.4` (vs `0.2`) y secundario **"Cancelar"** (vs "Cerrar"), que además choca con "Sí, cancelar".
6. **"En camino" sin CTA** (`171:17392`) vs la variante con "Marcar como entregado" (`895:69184`). ¿Cuál es canónica?
7. **Menú kebab del detalle:** no hay pantalla del menú desplegado.
8. **Estados terminales** (Cancelado / Devuelto / Reembolsado) **no tienen chip de header** en Figma. Confirmar.
9. Íconos a `icons.ts`: `store-04`, `shopping-cart-02`, `arrow-down-01`, `redo`, `icon/status/alert`, `copy-01`, `cancel-circle`, `more-horizontal`.

## D.12 Referencias
- *Orders Details (userflow)* (`290:21918`) — 62 pantallas.
- **Estados:** Pendiente `171:16835` · Por preparar `171:17009` (multi-sucursal `4166:113119`) · Por enviar `171:17194` · En camino `171:17392` / `895:69184` · Por recolectar `312:11520` · Entregado `292:36338` · Completado `292:36610` · Cancelado `4177:27541` · Devuelto `4177:27766` · Reembolsado `4177:28154`.
- **Parciales:** preparado `4166:113772` · enviado `4167:115279` · entregado `4167:115550` · cancelado `293:46928` · reembolsado `293:44056`.
- **Acciones:** Preparar `171:18394` · Dividir `4177:25091` · Guía `344:16020`/`344:24852`/`344:29466`/`344:24424` · Cancelar `896:73712` · Cancelar envío `795:68062` · Cancelar artículo `343:15661` · Devolver `896:73100` · Reembolso `905:41311` · Modales `4177:31471`–`4177:31606` · Notas/etiquetas `381:29767` · Editar dirección `4179:80471`.
- Reutiliza: tarjeta de pedido §13.3 · modal de confirmación §13.8 · loaders §L.

---

# Flujo 15 — Crear pedido (Create Order)

> Sección **"Create Order"** (`312:20348`): creación manual de un pedido desde la App (uso típico: venta en mostrador / POS). **11 pantallas** en un asistente de **2 pasos**: `1/2` selección de productos → `2/2` cliente, cobro y confirmación.
> **Figma:** `312:20348`. **Owner:** Karla Salazar — Head of UX/UI.
> **Entrada:** CTA "Crear pedido" del listado vacío (§13.4) y del FAB.

## CP.1 Mapa del flujo

```
Paso 1/2 — Productos
├── Catálogo (grid 2 col) + buscar + [+] crear producto
├── Búsqueda activa ("Smartwatch") → resultados
├── Stepper por producto (− 1 +)
├── Sheet "Selecciona la variante" (talla → color, 2 niveles)
└── Barra inferior: acordeón "Productos seleccionados (2)" + [Continuar]
        │
        ▼
Paso 2/2 — Cliente y cobro
├── Resumen: PRODUCTOS · RESUMEN DE COBRO · INFO DEL CLIENTE · NOTAS · ETIQUETAS
├── INFO DEL CLIENTE = buscador "Buscar cliente"
│     ├── Sheet de clientes (lista + "＋ Nuevo cliente")
│     └── Form "Agregar nuevo cliente" (Información básica + Dirección)
├── Cliente seleccionado → tarjeta con contacto + dirección
└── [Crear pedido]
        ├── Modal 1: confirmación
        ├── Modal 2: estatus de pago (pagado / pendiente)
        └── ✅ "¡Pedido creado!" → [Ver detalle] · [Crear otro pedido]
```

## CP.2 Chrome del asistente

**Header** (`4179:22826`): flecha atrás (12×14) + **"Crear pedido"** centrado (**`T3 S`** — Inter SemiBold 16, lh 1.3, tracking −0.32) + **indicador de paso** a la derecha (**"1/2"** / **"2/2"**, mismo `T3 S`). Debajo, divisor `Line 716` a todo el ancho.

> **Token nuevo:** `T3 S` (Inter SemiBold 16 / lh 1.3) — no aparecía en el resto de la App.

**Barra inferior fija** (`312:22298`): `bg white`, sombra `0 0 2.35px rgba(0,0,0,.1)`, `pt8 pb24 px16`. Contiene el acordeón de selección (§CP.3.4) + el CTA.

> ⚠️ El CTA aquí es de **escala compacta** (h40 / radio 12 / `B2 S`), no la escala grande del detalle (h48 / radio 16 / `B1 M`, §D.5).

## CP.3 Paso 1/2 — Selección de productos

### CP.3.1 Buscador + crear producto — `312:21388`
- **Input:** `bg #F8F8F8`, radio 12, h40 — `search-01` (20) + placeholder **"Buscar productos"** (`B2 R`, `#9CA3AF`).
- **Botón [+]** (40×40, `bg #F8F8F8`, radio 12, `add-01` 20px): crear producto nuevo.
- **Búsqueda activa** (`312:21952`): el texto escrito ("Smartwatch") sustituye al placeholder y aparece **`cancel-01`** (20px) para limpiar. El grid muestra sólo los resultados.

### CP.3.2 Tarjeta de producto (catálogo) — `312:21836`
Grid de **2 columnas**, tarjeta `160×143`. `bg white`, **radio 16**, `padding 12`, sombra **`shadow_button`** (`0 0 4px rgba(0,0,0,.14)`).
- **Imagen** 56×56, centrada.
- **Nombre:** `B2 S` (Inter SemiBold 14), centrado, truncado ("Audífonos inalám…").
- **Stock:** "22 unidades" — `B3 M` `#4C4C4C`.
- **Precio:** "$129" — **`B3 B`** (Inter **Bold** 12), negro, centrado.

> **Token nuevo:** `B3 B` (Inter Bold 12) — único uso de Bold en la App.

### CP.3.3 Stepper de cantidad — `4179:22950`
Aparece bajo la tarjeta al seleccionar. `bg white`, borde `1px #F3F3F3`, **radio 9px**, h32, `px8 py6`, ancho completo.
- Botones **−** / **+**: 16×16, `bg #F8F8F8`, **radio 6**, glifos `minus-sign` / `add-01` (12px).
- **Valor** al centro: `B3 M` (Inter Medium 12) negro.

> 🔴 **Radio 9px fuera de escala** (la App usa 6/8/10/12/16/20).
> 🔴 **La segunda línea de la tarjeta cambia de dato:** en el catálogo muestra **stock** ("22 unidades"); en el modo con stepper (`4179:22931`) muestra **SKU** ("SKU 5678906775"). Definir cuál corresponde.

### CP.3.4 Acordeón "Productos seleccionados" — `312:22298` / `4179:23127`
**Colapsado:** panel `bg #F8F8F8`, radio 16, `px12 py16` — **"Productos seleccionados (2)"** (`B2 S`) + `chevron-down` (16).
**Expandido** (`4179:23133`): lista de tarjetas `bg white`, radio 16, `p12`:
- **Nombre** `B3 S` (Inter SemiBold 12) + **chip de variante** (azul `#2180FF`, mismo de §D.2.3) + **precio** `B3 B`.
- **Stepper** (§CP.3.3, w89.5) + **`cancel-01`** (16px, descripción Figma: *delete, remove*) para quitar el producto.

### CP.3.5 Sheet "Selecciona la variante" — `4179:24008` / `4179:24133`
Bottom sheet: **radio 20**, sombra `shadow_card` (`0 0 5px spread 1`), filas de **h72** con borde inferior `#F3F3F3`.
- **Nivel 1** (`4179:24008`): header **"Selecciona la variante"** (`B2 M`) → opciones **Grande** / **Chico** con `arrow-right-01-sharp` (24).
- **Nivel 2** (`4179:24133`): header con **`arrow-left`** + "Selecciona la variante" → **Azul** (234 unidades) / **Rosa** (6 unidades), con stock bajo el nombre (`B3 R`).

Las variantes son **jerárquicas** (talla → color). El resultado se refleja como chip azul en el acordeón.

## CP.4 Paso 2/2 — Cliente, cobro y confirmación

Reutiliza la **estructura de bloques del detalle de pedido** (§D.2): `PRODUCTOS` → `RESUMEN DE COBRO` → `INFO DEL CLIENTE` → `NOTAS DEL PEDIDO` → `ETIQUETAS`. Barra inferior con **dos botones de 160px** (secundario + primario).

### CP.4.0 ⚠️ RESUMEN DE COBRO — dos variantes conviviendo

| Variante | Dónde | Divisores | Total |
|---|---|---|---|
| **A** (§D.4.2) | Detalle de pedido · paso 2/2 principal (`4179:77741`) | no | `B2 S` (14px) |
| **B** | Resumen compacto de Crear pedido (`4179:23293`, `4179:77168`) | **sí** (`Line 728` / `Line 729`) | **`B1 S` (16px)** |

Además, la variante **B** omite la fila "Tarifa de envío". Definir cuál es canónica.

### CP.4.1 INFO DEL CLIENTE — estado vacío (`4179:77758`)
El bloque contiene **un buscador** (`bg #F8F8F8`, radio 12, h40): `search-01` + placeholder **"Buscar cliente"**.

### CP.4.2 Sheet de selección de cliente — `4179:77942`
Mismo componente que el sheet de variantes (radio 20, filas h72):
- **Cliente:** nombre (`B2 M`) + email (`B3 R` `#4C4C4C`).
- **Última fila:** **`add-01`** (20) + **"Nuevo cliente"** (`B2 M`).

### CP.4.3 Form "Agregar nuevo cliente" — `4179:23270`
Pantalla propia (h1453) con back + título **"Agregar nuevo cliente"**. Dos secciones colapsables (`arrow-down-01-sharp`):

**Información básica** — inputs `Inactive/Default Input`: h55, **radio 20**, borde `1px #F3F3F3`, `px20 py18`; label `B2 S`, placeholder `B2 R` `#C3C3C3`.
| Campo | Placeholder |
|---|---|
| Nombre | Ej. María |
| Apellido | Ej. González |
| Correo electrónico | Ej. maria.gonzalez@ejemplo.com |
| Número de teléfono | — |

- **Aviso** (`information-circle` 16): *"Recuerda pedir permiso a tus clientes para activar las notificaciones de marketing."*
- **Checkboxes:** "Acepta recibir email marketing" · "Acepta recibir notificaciones al celular".

**Dirección** — Calle · Número exterior · Número interior (opcional) · Código postal · Colonia (select) · Estado · Ciudad · **Referencia** (textarea h141).
- **Checkboxes:** "Establecer como dirección predeterminada para mis envíos." · "Establecer como dirección de devolución".
- CTA final: botón h48.

> 🔴 **Medidas fraccionarias** en todo el form (`gap 7.328`, alto de campo `79.328`) — mismo patrón de **componente escalado** que §D.4.7. Corregir a tokens.

### CP.4.4 Cliente seleccionado — `4179:77134`
Tarjeta con **nombre** (`B2 M`) + **`cancel-01`** (quitar cliente), y dos bloques con link **"Editar"** (`B2 S` negro):
- **INFORMACIÓN DE CONTACTO** (label 10px Regular, `uppercase`) → email + teléfono (`B3 R`).
- **DIRECCIÓN DE ENVÍO** → dirección completa.

> ⚠️ Estos labels usan **10px Regular**, mientras los encabezados de bloque del detalle usan **`Tag S` (SemiBold 10)** (§D.2.2). Unificar.

### CP.4.5 Modales de confirmación
Mismo componente de §13.8 (radio 16, ícono en círculo `#F8F8F8` 64px, `shopping-bag-03` 35px).

| # | Nodo | Título | Cuerpo | Botones |
|---|---|---|---|---|
| 1 | `4179:77126` | Crear pedido | *"Esto **creara** un pedido gratuito. ¿**Estas** seguro que deseas crear este pedido?"* | **Cancelar** + **Crear pedido** |
| 2 | `4179:77243` | Crear pedido | *"Selecciona **la el** estatus de pago:"* — **radios**: "Marcar como pagado" / "Marcar como pendiente de pago" | **Cancelar** + **Crear pedido** |

> ⚠️ En Figma **los dos radios se ven activos** al mismo tiempo (ambas instancias con `state=on`).

### CP.4.6 Éxito — "¡Pedido creado!" — `317:23273`
Sin header de asistente; **`cancel-01`** (20) arriba a la derecha para cerrar.
- **Ícono:** círculo `#F0FDF4` (Green/500, 72px) + `tick-02` (32px) en `#51AF70` (Contextual_success).
- **Título:** "¡Pedido creado!" (`T2 S`) · **Subtítulo:** "Se generó el link de pago" (`B2 R` `#4C4C4C`).
- **Tarjeta de resumen** (`bg #F8F8F8`, radio 16, `px12 py16`): "Detalles del pedido" (`B2 S`) + filas **ID de pedido** `#394031` · **Cliente** Javari Mena · **Monto** $1888.00 (label `B2 R` `#4C4C4C` ··· valor `B2 S` negro).
- **Botones** (barra inferior fija): **"Ver detalle"** primario + **"Crear otro pedido"** secundario.

## CP.5 Componentes nuevos (vs. ya documentados)
- **Header de asistente con indicador de paso** (`1/2` · `2/2`) — token `T3 S`.
- **Tarjeta de producto de catálogo** (grid 2 col, `shadow_button`, precio `B3 B`).
- **Stepper de cantidad** (− valor +, radio 9).
- **Acordeón de selección** en barra inferior fija.
- **Bottom sheet de lista** (radio 20, filas h72) — reutilizado para **variantes** y **clientes**.
- **Buscador de cliente** dentro del bloque INFO DEL CLIENTE.
- **Pantalla de éxito** con ícono verde + tarjeta de resumen.

## CP.6 Pendientes (🔴)

1. 🔴 **Radio 9px** del stepper, fuera de escala.
2. 🔴 **Medidas fraccionarias** en el form de nuevo cliente (componente escalado).
3. ⚠️ **Los dos radios de estatus de pago aparecen activos** simultáneamente.
4. ⚠️ **Dato inconsistente en la tarjeta de producto:** stock ("22 unidades") en catálogo vs SKU en modo stepper.
5. ⚠️ **Fila de cliente sin nombre** (sólo email) en el sheet.
6. ⚠️ **Labels de 10px Regular** vs `Tag S` (SemiBold 10) del detalle.
7. ⚠️ **Dos variantes del RESUMEN DE COBRO** (§CP.4.0): Total en 14px sin divisores vs 16px con divisores, y una omite "Tarifa de envío".
8. **Sin estados de error/vacío:** no hay pantalla de "sin productos", "sin resultados de búsqueda", "sin clientes" ni error al crear. Faltan.
9. **Sin estado de carga** al crear el pedido (entre el modal y el éxito).
10. Íconos a `icons.ts`: `add-01`, `minus-sign`, `cancel-01`, `chevron-down`, `arrow-right-01-sharp`, `arrow-left`, `arrow-down-01-sharp`, `shopping-bag-03`, `tick-02`, `information-circle`, `search-01`.

## CP.8 Referencias
- *Create Order* (`312:20348`) — 11 pantallas.
- **Paso 1/2:** catálogo `312:21370` · búsqueda `312:21952` · seleccionados `312:22187` · steppers + panel `4179:22931` · variante N1 `4179:23799` · variante N2 `4179:24031`.
- **Paso 2/2:** resumen `4179:77700` · sheet de clientes `4179:77821` · nuevo cliente `4179:23270` · cliente seleccionado `4179:23201` · modal confirmación `4179:77126` · modal estatus de pago `4179:77243` · éxito `317:23273`.
- Reutiliza: bloques del detalle §D.2 · modal de confirmación §13.8 · chip de variante §D.2.3.

---

# Flujo 16 — Carrito abandonado (Cart)

> Sección **"Cart"** (`4183:109497`), con la sub-sección **"Detail"** (`4184:116418`) **anidada dentro**: son un solo flujo, no dos.
> Corresponde a la **pestaña "Carrito abandonado"** de *Mis pedidos* (§13.2) — cierra el pendiente §13.11·8.
> **15 pantallas:** 10 en el listado + 5 en el detalle.
> **Figma:** `4183:109497`. **Owner:** Karla Salazar — Head of UX/UI.

## CA.1 Mapa del flujo

```
Mis pedidos › pestaña "Carrito abandonado"
│
├── LISTADO
│   ├── Vacío
│   ├── Con datos: selector de rango (30 días) + 2 KPIs (Pendiente · Monto)
│   │   ├── Popover de desglose (% carrito / % compra)
│   │   ├── Buscador + botón de filtro
│   │   ├── Chips de filtro aplicados (Tipo · Estado)
│   │   └── Tarjetas: Carrito (CRT-) / Compra (CHK-)
│   ├── Lazy load (skeleton) ×2
│   └── 3 frames VACÍOS (placeholders sin contenido)
│
└── DETALLE (CRT-100000718)
    ├── Header: ID + fecha + chip "No recuperado" + kebab
    ├── 4 tarjetas: Cliente · Cantidad de productos · Monto · Estado de correo
    ├── PRODUCTOS + RESUMEN
    ├── Toast "Link copiado"
    └── Sheet "Detalle de recuperación" (timeline de automatización)
        ├── variante Carrito abandonado
        └── variante Compra (checkout)
```

## CA.2 Dos entidades en una misma lista

El flujo maneja **dos tipos de abandono**, distinguidos por prefijo de ID y por el chip **"Tipo"**:

| Tipo | Prefijo | Subtítulo de la tarjeta | Chip "Tipo" |
|---|---|---|---|
| **Carrito** abandonado | `CRT-` | **nombre** del cliente ("Javari Mena") | "Carrito" |
| **Compra** abandonada (checkout) | `CHK-` | **email** ("correo@correo.com") | "Compra" |

## CA.3 Listado

### CA.3.1 Chrome
- **Título** "Mis pedidos" (`T2 S`) — misma pantalla que §13.2.
- **Tabs** (`4192:170221`): mismo componente; ahora **"Carrito abandonado"** activo (`B2 S` + subrayado `1.5px #DB3B2B`); "Listado de pedidos" y "Sucursales" inactivos (`B2 M` `#4C4C4C`).
- **Barra inferior con FAB** (§H.3.9): es un **overlay flotante** (`y: 694`, `360×86`), no ocupa flujo — las tarjetas de la lista **pasan por debajo**.

> 🔴 **El tab "Sucursales" está en `left: 391`** — fuera de la pantalla de 360px. Se arrastra desde §13.2. Definir scroll horizontal de tabs o recortar.

### CA.3.2 Bloque de KPIs — `4184:115777`
- **Selector de rango:** botón secundario `329×35`, radio 12, borde `1.25px #F3F3F3`, label **"30 días"** (`B3 M` 12px) + `chevron-down` (24).
- **2 tarjetas KPI:** `bg white`, borde `1px #F3F3F3`, radio 12, **h106**. Label (`B1 M` 16) → divisor → valor (`B1 M` 16) + `chevron-down` (16).
  - **Pendiente** → `2`
  - **Monto** → `$ 3,456.00`

> 🔴 **El bloque de KPIs se desborda:** el contenedor mide **622px de ancho dentro de un contenedor de 328px**. Las tarjetas son de 200px y **402px** (asimétricas). La tarjeta **Monto queda cortada por el borde de la pantalla** — no hay scroll horizontal ni carrusel definido. Es un error de layout: confirmar si debía ser un carrusel de KPIs o dos tarjetas simétricas de 154px.

### CA.3.3 Popover de desglose — `4184:115758`
Se abre desde el `chevron-down` de la tarjeta **Pendiente** (la izquierda). Es un **overlay absoluto sobre la pantalla**, no un hijo de la tarjeta: posición **`x: 27` · `y: 292`**, tamaño **`203 × 60`**. Queda **por encima del buscador**, que tapa parcialmente.
`bg white`, radio 10, `p10`, sombra `shadow_card`, dos líneas (`B3 M` 12):
- "50.00% de carrito abandonado"
- "50.00% de compra abandonado"

### CA.3.4 Buscador — `4183:109632`
Campo `bg #F8F8F8`, radio 12, `w283` + **un solo botón 40×40** (`filter-horizontal`, radio 12).

> ⚠️ **Difiere del buscador de pedidos** (§13.2), que tiene **dos** botones (ordenar + overflow) y ancho completo. Aquí solo hay uno.

### CA.3.5 Chips de filtro aplicados — `4184:116400`
Mismo patrón de §13.7: chip `bg #F8F8F8`, radio 6, `p6` — label (`B3 M` negro) + **badge de conteo** (`bg #000`, radio 8, `Tag S` 10 blanco) + `x` (12).
**Categorías:** **Tipo** y **Estado**.

### CA.3.6 Tarjeta de carrito — `4183:109500` / `4184:115290`
`bg white`, borde `1px #F3F3F3`, radio 12, contenido `w296` a `15px` de los bordes, `gap 16`.
- **Cabecera:** **ID** (`B1 M` 16, ej. `CRT-100000718`) + **subtítulo** (`B3 R` 12 `#4C4C4C`) | **chip de estado** ("No recuperado", neutral).
- **Divisor** → filas label (`B3 R` `#4C4C4C`) ··· valor (`B2 M` 14):
  - Producto → "3 productos"
  - Monto → "$12,383.00"
  - **Tipo** → **chip** ("Carrito" / "Compra")
- **Divisor** → pie: `calendar-03` (20) + "14:24 - 23 de oct, 2025" (`B3 M` 12 negro).

> **Sin kebab** — a diferencia de la tarjeta de pedido (§13.3). Las acciones viven en el detalle.

> 🔴 **Hay una tarjeta de PEDIDO dentro del listado de carritos** (`4183:109576`): "Zain Vetrovs / #394030", chip "En camino", kebab, filas con íconos (`cash-01`, `store-03`), chip de canal "Amazon" y pie "3 envíos". Es la tarjeta de §13.3 pegada por error; **aparece en 3 pantallas** (`4183:109498`, `4184:115449`, `4183:110296`). Eliminar.

### CA.3.7 Estado vacío — `4183:111228`
Reutiliza el empty de §13.4: ilustración Freepik (220px), título **"Aún no tienes carritos abandonados"** (`T2 S`), subtítulo **"Una vez que tengas uno, aparecerá aquí."** (`B2 R`, opacidad 70%), botón primario `162×40`.

### CA.3.8 Lazy load — `4183:111204` / `4183:111220`
Skeleton de la lista (rectángulos: título `160×22`, avatar circular 34, tarjetas `328×161`). Mismo patrón que §L.

### CA.3.9 🔴 Tres frames vacíos
`4183:111418` (360×614) · `4184:116063` (360×614) · `4183:111622` (360×780) **no tienen ninguna capa dentro**. Son placeholders sin contenido — presumiblemente el **sheet de filtros** (Tipo / Estado) y el selector de rango, que quedaron sin diseñar. Mismo hueco que los filtros de Pedidos (§13.11).

## CA.4 Detalle del carrito

Scroll único. **5 pantallas**, todas sobre la misma base.

### CA.4.1 Header — `4184:116726`
Mismo patrón que §D.2.1: **ID** `CRT-100000718` (`B1 S` 16) + **fecha** "9 de oct, 2024 a las 05:43 AM" (`B3 R` 12 `#4C4C4C`) + **chip** "No recuperado" (neutral) + **kebab** (`more-horizontal` rotado, 20).

> 🔴 **El kebab no tiene pantalla de menú.** La acción de copiar link (que produce el toast §CA.4.4) no está diseñada.

### CA.4.2 Tarjetas de información — `4184:116666`
Cuatro tarjetas apiladas (`gap 20`, `px16`), mismo molde que los KPIs (§CA.3.2): `bg white`, borde `1px #F3F3F3`, radio 12.

| Tarjeta | Alto | Contenido |
|---|---|---|
| **Cliente** | 106 | `corroeo@correo.com` (`B2 R` 14) |
| **Cantidad de productos** | 106 | `2` (`B1 M`) + `chevron-down` |
| **Monto** | 106 | `$ 3,456.00` (`B1 M`) + `chevron-down` |
| **Estado de correo** | 126 | **chip verde "Enviado"** (`#F0FDF4` / `#51AF70`) + texto: *"Se envío a tu cliente un correo de productos pendientes de compra."* |

> ⚠️ La tarjeta **Cliente** muestra solo el email; la tarjeta del listado muestra nombre (carrito) o email (compra). Inconsistente.

### CA.4.3 PRODUCTOS y RESUMEN
- **PRODUCTOS** (`4184:116442`): mismas filas que §D.2.3 (thumb 44/r12, nombre `B2 M`, "1unidad", SKU, precio `B2 S`).
- **RESUMEN** (`4184:117741`): el encabezado dice "RESUMEN". Filas: Subtotal · Impuestos (VA) · Tarifa de envío · Total.

### CA.4.4 Toast "Link copiado" — `4184:118033`
`bg #51AF70` (Green/400), borde `1px #F3F3F3`, radio 12, `px12 py8`, texto `B3 M` **blanco**.

> 🔴 **Sombra roja en un toast verde:** `drop-shadow(0 4px 6.75px rgba(255,0,0,0.05))`. El valor `rgba(255,0,0,…)` está copiado de otro componente. Corregir.
> ⚠️ **Primer toast documentado en la App.** No existe un componente de toast en el sistema — hay que crearlo (variantes éxito / error / info, posición, duración).

### CA.4.5 Sheet "Detalle de recuperación" — `4203:85178` / `4203:84873`
Bottom sheet: `bg white`, **radio superior 20**, `px16 py24`, sombra `0 0 2.35px rgba(0,0,0,.1)`.
- **Título** (`B2 S` 14) · **descripción** (`B2 R` 14 negro) · **"Proceso:"** (`B2 S` `#4C4C4C`).
- **Timeline vertical:** íconos `24×24` (`bg #F8F8F8`, **radio 10**, glifo 16) unidos por **líneas verticales punteadas**.
  - Cada paso: **label** (`B3 M` 12, **`#4F4F4F`**) + **descripción** (`B2 R` 14 negro).
- **CTA** "Continuar" (primario, **`328×40`**, radio 12, `B2 S`): **fijo al pie del sheet**, fuera del área scrolleable.

**Dos variantes:**

| | **Carrito abandonado** (`4203:85059`) | **Compra / checkout** (`4203:84735`) |
|---|---|---|
| Pasos | `person` → `clock` → 3× `clipboard-list-check` → `mail` | igual |

> 🔴 **Tercer gris fuera de paleta:** los labels del timeline usan **`#4F4F4F`** (Gray 2), sumándose a `#4C4C4C` y `#4B5563` (§D.10·3). **Ya son tres grises de texto secundario.**

## CA.5 Componentes nuevos (vs. ya documentados)
- **Tarjeta KPI con desglose** (label + valor + chevron → popover).
- **Popover de desglose** (radio 10, `shadow_card`).
- **Selector de rango temporal** ("30 días", botón secundario + chevron).
- **Tarjeta de carrito** (sin kebab, con chip de Tipo).
- **Toast** (`bg #51AF70`, radio 12) — **primero en la App**.
- **Timeline de proceso** (íconos 24 en `#F8F8F8` radio 10 + conectores verticales).

## CA.6 Pendientes (🔴)

1. 🔴 **Bloque de KPIs desbordado:** 622px dentro de 328px, tarjetas asimétricas (200 / 402).
2. 🔴 **Tarjeta de pedido dentro del listado de carritos** (`4183:109576`, en 3 pantallas). Eliminar.
3. 🔴 **Tres frames vacíos** (`4183:111418`, `4184:116063`, `4183:111622`): el **sheet de filtros** (Tipo / Estado) y el selector de rango no están diseñados.
4. 🔴 **Sombra roja en el toast verde** (`rgba(255,0,0,.05)`).
5. 🔴 **No existe componente de toast** en el sistema. Definir variantes, posición y duración.
6. 🔴 **Tercer gris de texto:** `#4F4F4F` (timeline) junto a `#4C4C4C` y `#4B5563`.
7. ⚠️ **Kebab del detalle sin menú diseñado** (de ahí sale "copiar link").
8. ⚠️ **Tab "Sucursales" fuera de pantalla** (`left: 391` en 360px).
9. ⚠️ **Buscador con 1 botón** aquí vs **2** en pedidos (§13.2).
10. **Sin estados** de error ni de "sin resultados de búsqueda".
11. Íconos a `icons.ts`: `calendar-03`, `filter-horizontal`, `chevron-down`, `more-horizontal`, `person`, `icon-info/clock`, `icon-info/clipboard-list-check`, `icon-nav/mail`, `search-01`, `x`.

## CA.8 Referencias
- *Cart* (`4183:109497`) → *Detail* (`4184:116418`) anidada. 15 pantallas.
- **Listado:** vacío `4183:111228` · lista `4183:109498` · popover `4184:115449` · variante `4183:109647` · filtros aplicados `4183:110296` · lazy load `4183:111204` / `4183:111220` · frames vacíos `4183:111418` / `4184:116063` / `4183:111622`.
- **Detalle:** base `4184:116419` · variante `4184:117759` · toast `4184:117896` · sheet compra `4203:84735` · sheet carrito `4203:85059`.
- Reutiliza: tabs y empty §13.2/§13.4 · fila de producto §D.2.3 · chips §D.3 · loaders §L.

---

# Flujo 17 — Productos · Listado (Product List)

> **Sección "Product List"** (`320:23825`). **Punto de entrada del dominio de Productos** — todo lo que venga después (detalle de producto, inventario, precios, catálogo, variantes) cuelga de aquí.
> **11 pantallas** + sub-sección *Product Card Variants* (4 variantes de tarjeta) + **3 menús**.
> **Figma:** `320:23825`. **Owner:** Karla Salazar — Head of UX/UI.
> **Entrada:** ícono *Product* de la tab bar (§H.3.9).

## P.1 Mapa del flujo

```
Productos  (5 tabs: Listado de productos · Inventario · Precio · Catálogo · Sucursales)
│
├── Buscador ("Busca por código, nombre, SKU…") + [ordenar] + [overflow]
│
├── LISTADO
│   ├── Vacío ("Aún no tienes productos")
│   ├── Con productos → tarjeta de producto
│   │     ├── kebab → Menú: Editar · Desactivar
│   │     └── checkbox → modo selección
│   ├── Selección múltiple → "2 seleccionados" + [Acciones ▾]
│   │     └── Menú: Eliminar seleccionados
│   ├── Filtros aplicados → chips (Estado · Canal de ventas · Inventario · Categoría · Gestionado por)
│   └── Botón "+" → Menú: Agregar producto · Crear con IA
│
├── Lazy load (skeleton) · Lazy load (spinner)
└── Error de sincronización
```

## P.2 Chrome de la sección

- **Título:** "Productos" (`T2 S` — Inter SemiBold 20), centrado.
- **Tabs** (`712:55312`) — **5 pestañas**: **Listado de productos** (activa: `B2 S` + subrayado `1.5px #DB3B2B`) · Inventario · Precio · Catálogo · Sucursales (inactivas: `B2 M` `#4C4C4C`).
- **Buscador** (`4183:114783`): campo flexible `bg #F8F8F8` radio 12 h40, `search-01` + placeholder **"Busca por código, nombre, SKU…"** (`B2 R` `#9CA3AF`), más **dos botones 40×40**: `filter-horizontal` (*sorting*) y `more-vertical` (overflow). **Idéntico al buscador de Pedidos (§13.2).** ✅
- **Tab bar con FAB** (§H.3.9), overlay flotante.

> 🔴 **La barra de tabs está rota, y de forma distinta en cada pantalla.** Los tabs están posicionados en **absoluto**, con **cuatro layouts diferentes** y solapes en tres de ellos:
>
> | Pantalla | Solapes medidos | "Sucursales" |
> |---|---|---|
> | `712:55299` (listado) | Precio↔Inventario **2px** · Catálogo↔Precio **7px** · **Sucursales↔Catálogo 70px** | termina en **495** |
> | `712:54799` (vacío) | **Sucursales↔Catálogo 41px** | termina en **511** |
> | `712:66158` | **Inventario↔Listado 58px** · Precio **2px** · Catálogo **7px** | termina en **495** |
> | `712:55819` (selección) | **Catálogo↔Precio 71px** | termina en **495** |
>
> 🔴 **"Sucursales" siempre queda fuera de la pantalla** (termina entre 495 y 511px, sobre un ancho de 360).
> 🔴 **En las pantallas de selección el tab "Catálogo" está VACÍO:** el frame existe (`712:55969` / `4167:116506`, `32×37`) pero **no tiene texto dentro**. El tab desaparece.
> 🔴 **Dos implementaciones de la barra:** en el empty los tabs viven en un contenedor de auto-layout (`4100:51331`, w432); en el resto están sueltos en absoluto. Unificar y definir **scroll horizontal** — 5 tabs no caben en 360px.

## P.3 🔴 Tarjeta de producto — DOS anatomías conviviendo

**El hallazgo central de este flujo.** En la **misma lista**, las tarjetas 1–2 y la tarjeta 3 son componentes **distintos**:

| | **Tarjeta A** (`1864:49243`) | **Tarjeta B** (`1864:49364`) |
|---|---|---|
| **Checkbox** | ✅ arriba a la izquierda | ❌ **no tiene** |
| **Chip de estado** | arriba a la derecha | **abajo a la derecha** |
| **Kebab** | arriba, junto al chip | **arriba, junto al nombre** |
| **Íconos en las filas** | no | ✅ `store-verified-02` · `store-03` · `dollar-02` |
| **Labels de las filas** | Inventario · Precio · **Canales** | **Stock** · **Activo** · Precio |
| **Valor de stock** | "3,102 unidades \| 2 variantes" | **"(T1) 3,102 unidades"** |
| **Dato "1/3"** | fila **Canales** | fila **Activo** |
| **Layout** | auto-layout `p16` | **absoluto** (`left/top: 15`) |
| **Divisores** | 1 | 2 |

> 🔴 **"Activo" significa dos cosas distintas dentro de la misma tarjeta B:** es el **chip de estado** del producto *y* el **label de la fila** que muestra "1/3" (canales activos). Misma palabra, dos semánticas, a 60px de distancia.
> 🔴 **El mismo dato "1/3" tiene dos labels:** "Canales" (A) y "Activo" (B).
> 🔴 **Los labels cambian entre pantallas, no sólo entre tarjetas:** en el listado (`712:55299`) la tarjeta A dice *Inventario / Precio / Canales*; en la pantalla de selección (`712:55819`) la misma tarjeta dice *Stock / Activo / Precio*.

### P.3.1 Anatomía canónica propuesta (Tarjeta A)
`bg white`, borde `1px #F3F3F3`, **radio 12**, `p16`, contenido `w296`, `gap 16`.
- **Fila de control:** `Control` (checkbox 16px; *On* = `bg #DB3B2B` radio 4) ··· **chip de estado** + **kebab** (`more-horizontal` rotado, 20).
- **Identidad:** **thumb 40×40** (`bg white`, borde `#F3F3F3`, **radio 8**, imagen 32 centrada) + **nombre** (`B2 M` 14, 2 líneas, `text-ellipsis`, w248).
- **Divisor** (`#F3F3F3`).
- **Filas de datos** (`gap 12`): label `B3 R` 12 `#4C4C4C` ··· valor `B2 M` 14.

> 🔴 **El valor de "Inventario" va en `#4C4C4C`** mientras Precio y Canales van en **negro**. En la misma tabla, un valor gris y dos negros sin razón semántica.

### P.3.2 Chip de estado — 🔴 cuarto verde
El chip "Activo" usa `bg #F0FDF4` (Green/500) + texto **`#4FC153`** (**Green/300**).

> 🔴 El chip de éxito del detalle de pedido (§D.3) usa **`#51AF70`**. Ya van **tres verdes** de "positivo" (`#4FC153`, `#16A34A`, `#51AF70`) y este flujo **confirma el tercero como token nombrado** (Green/300 vs Green/400). Hay que fijar uno.

## P.4 Variantes de tarjeta (*Product Card Variants*, `434:39384`)

Cuatro variantes documentadas en su propia sub-sección:

| Variante | Nodo | Inventario | Precio | Chips |
|---|---|---|---|---|
| **Simple** | `4181:81673` | "3,102 unidades" | "$1,234.99" | 1 |
| **Dos chips** | `4181:81794` | "3,102 unidades" | "$1,234.99" | **2** |
| **Con variantes** | `4181:81503` | "3,102 unidades \| 2 variantes" | **rango** "$1,234.99 - $1,300.90" | 1 |
| **Con variantes (bis)** | `4181:81540` | igual que la anterior | igual | 1 |

**Reglas que se deducen:**
- Si el producto **tiene variantes**, el inventario agrega **"\| N variantes"** y el precio se muestra como **rango**.
- El bloque de chips admite **más de uno** (segundo chip de 91px, sin contenido documentado).

> ⚠️ `4181:81503` y `4181:81540` son **idénticas** — duplicado sin diferencia aparente. Confirmar cuál sobra.

## P.5 Selección múltiple

**Barra de selección** (`4183:114839`, aparece bajo el buscador):
- **Checkbox maestro** (`Control`, estado **`Multiselection`** = indeterminado).
- **Contador:** "2 seleccionados" (`B2 M` 14).
- **Botón "Acciones"** (secundario, `118×35`, radio 12, borde `1.25px #F3F3F3`, `B3 M` 12 + `chevron-down` 24).

> ⚠️ **El botón "Acciones" cambia de tamaño de texto entre pantallas:** `B2 M` (14px) en `712:56113` vs `B3 M` (12px) en `4183:114839`.

## P.6 Menús — **los primeros menús kebab diseñados en toda la App**

Los tres comparten componente: `bg white`, borde `1px #F8F8F8`, **radio 16**, `p16`, `gap 16`, sombra `0 4px 6.3px rgba(0,0,0,.1)`. Ítems: ícono 16 + label `B3 M` 12 negro.

| Menú | Nodo | Ítems |
|---|---|---|
| **De tarjeta** (kebab) | `326:37722` | `pencil-edit-02` **Editar** · `toggle-off` **Desactivar** |
| **De creación** (botón +) | `712:55749` | `add-01` **Agregar producto** · `ai-magic` **Crear con IA** |
| **De selección** ("Acciones") | `4167:116689` | `delete-02` **Eliminar seleccionados** |

> ✅ **Esto cierra un hueco abierto en todos los flujos anteriores.** El kebab no tenía menú en Pedidos (§13), Detalle (§D), Carrito (§CA) ni Nova (§N). **Este es el patrón a reutilizar en todos ellos.**
> ⚠️ **"Crear con IA"** (`ai-magic`) es una entrada a Nova desde Productos. Su flujo no está en esta sección — documentar aparte.

## P.7 Filtros aplicados — `4167:117409`

**5 categorías**, cada una como chip con conteo: `bg #F8F8F8`, radio 6, `p6` — label **`B3 S`** (SemiBold 12) + **badge** (`bg #000`, radio 8, `Tag S` 10 blanco) + `x` (12).

| Chip | Conteo |
|---|---|
| Estado | 1 |
| **Canal de ventas** | 3 |
| Inventario | 1 |
| Categoría | 1 |
| Gestionado por | 1 |

El contenedor mide **594px** en una pantalla de 360 → **scroll horizontal**.

> ⚠️ El label del chip aquí es **`B3 S`** (SemiBold); en Carrito abandonado (§CA.3.5) el mismo chip usa **`B3 M`** (Medium). Unificar.
> 🔴 **El sheet de filtros no existe.** Tres frames **vacíos, sin una sola capa**: `712:53944` (360×**1286**) · `4183:101517` (360×**1286**) · `712:56795` (360×780). Por el alto (1286px) es claramente el **sheet de filtros** con sus 5 categorías. **Tercera vez** que pasa (Pedidos §13.11, Carrito §CA.3.9).

## P.8 Estados

### P.8.1 Vacío — `712:54799`
Ilustración (*Online wishes list-pana*, 220px) + título **"Aún no tienes productos"** (`T2 S`) + subtítulo + botón primario `162×40`.

### P.8.2 Error de sincronización — `434:39252`
Tarjeta blanca, **radio 20**, `p16`, `gap 32`, sombra `0 4px 16px rgba(0,0,0,.02)`.
- **Ícono:** círculo **`#FFF5F0`** (Orange/500) 64px + `wifi-error-01` (32px, **`#FF6700`** Orange/300).
- **Título:** "Error de sincronización detectado" (`T3 S`).
- **Cuerpo:** *"No pudimos sincronizar tus datos más recientes por un problema de conexión. Revisa tu conexión a internet o intenta reconectar más abajo."* (`B2 R` `#4C4C4C`).
- **CTA primario:** h48 / radio 16 / ícono `refresh` + **"Reconectar"** (`B1 M`).
- **Pie:** "Última sincronización exitosa: 10:42 a.m."

> 🔴 **Naranja nuevo en la App:** `#FF6700` (Orange/300) / `#FFF5F0` (Orange/500). Ya existe el **amarillo** de alerta (`#EDBD55` / `#FFFCE5`, §D.4.2). **Dos escalas para el mismo rol semántico** — definir cuál es *warning* y cuál *error de conexión*.
> 🔴 **El pie está construido como BOTÓN** (`434:39264`, h40, radio 12) con relleno `rgba(244,244,244,0)`. Es **texto informativo, no una acción**. Mismo relleno fantasma alfa-0 que el botón de Nova (§N.8.3).

### P.8.3 Lazy load — `434:40300` / `434:40322`
- **Skeleton** (`434:40300`): título `110×22`, avatar circular 34, **4 pastillas de tab** (`96×34`), buscador (`280×40` + `40×40`) y **5 tarjetas** (`328×161`).
- **Spinner** (`434:40322`): `tabler:loader` (32px) centrado, pantalla en blanco.

> ⚠️ **Dos loaders distintos para la misma lista.** Definir cuándo va skeleton y cuándo spinner.
> ⚠️ El skeleton dibuja tarjetas de **161px**, pero las tarjetas reales miden **216–251px**. El salto de layout al cargar será visible.

## P.10 Componentes nuevos
- **Tarjeta de producto** (thumb + nombre + checkbox + chip + kebab + filas de datos).
- **Menú desplegable** (`radio 16`, sombra) — **primer menú kebab de la App**; patrón reutilizable en §13, §D, §CA y §N.
- **Barra de selección múltiple** (checkbox indeterminado + contador + botón "Acciones").
- **Checkbox `Control`** con 3 estados: `Off` · `On` (`#DB3B2B`) · `Multiselection`.
- **Tarjeta de error de sincronización** (ícono naranja + reconectar + timestamp).
- **Skeleton de listado** con tabs.

## P.11 Pendientes (🔴)

1. 🔴 **Dos anatomías de tarjeta de producto** en la misma lista (§P.3). Elegir una.
2. 🔴 **"Activo" tiene dos significados** en la tarjeta B: chip de estado y label de canales activos.
3. 🔴 **El dato "1/3" tiene dos labels**: "Canales" y "Activo".
4. 🔴 **Los labels de las filas cambian entre pantallas** (Inventario/Precio/Canales vs Stock/Activo/Precio).
5. 🔴 **Barra de tabs rota:** 4 layouts distintos, solapes de 2 a 71px, "Sucursales" siempre fuera de pantalla, y el tab **"Catálogo" vacío** (sin texto) en las pantallas de selección (§P.2).
6. 🔴 **Cuarto verde:** el chip "Activo" usa `#4FC153` (Green/300) vs `#51AF70` del chip de éxito (§D.3).
7. 🔴 **Valor de "Inventario" en `#4C4C4C`** mientras Precio y Canales van en negro.
8. 🔴 **Naranja nuevo** (`#FF6700` / `#FFF5F0`) conviviendo con el amarillo de alerta (`#EDBD55` / `#FFFCE5`).
9. ⚠️ **El botón "Acciones" usa 14px en una pantalla y 12px en otra** (`712:56113` vs `4183:114839`).
10. 🔴 **Sheet de filtros sin diseñar:** 3 frames vacíos (`712:53944`, `4183:101517`, `712:56795`).
11. 🔴 **Pie del error de sync construido como botón** con relleno alfa-0 (`434:39264`).
12. ⚠️ **Dos loaders** (skeleton y spinner) sin regla de uso; el skeleton usa alturas (161px) que no coinciden con las tarjetas reales (216–251px).
13. ⚠️ **Variantes de tarjeta `4181:81503` y `4181:81540` idénticas** — duplicado.
14. ⚠️ **"Crear con IA"** sin flujo documentado.
15. **Sin estados**: sin resultados de búsqueda, error de carga de la lista, ni confirmación de "Desactivar"/"Eliminar".
16. **Las 4 pestañas restantes** (Inventario · Precio · Catálogo · Sucursales) no están en esta sección — son documentos aparte.
17. Íconos a `icons.ts`: `pencil-edit-02`, `toggle-off`, `delete-02`, `ai-magic`, `store-verified-02`, `store-03`, `dollar-02`, `wifi-error-01`, `refresh`, `more-horizontal`, `more-vertical`, `filter-horizontal`, `search-01`, `add-01`, `x`, `tabler:loader`.

## P.13 Referencias
- *Product List* (`320:23825`) — 11 pantallas + *Product Card Variants* (`434:39384`).
- **Listado:** vacío `712:54799` · con productos `712:55299` · variante `4167:116760` · filtros aplicados `4167:117396` · menú de tarjeta `712:65861` · tarjeta de variante completa `712:66158`.
- **Selección:** `712:55819` · con menú `4167:116389`.
- **Estados:** error de sync `434:39248` · lazy load `434:40300` / `434:40322`.
- **Menús:** tarjeta `326:37722` · creación `712:55749` · selección `4167:116689`.
- **Sin diseñar:** `712:53944`, `4183:101517`, `712:56795` (sheet de filtros).
- Reutiliza: buscador §13.2 · chips de filtro §13.7/§CA.3.5 · tab bar §H.3.9 · loaders §L.

---

# Flujo 18 — Agregar producto · Paso 1 (sin variantes)

> **Sección "Step 1: If product don't have variants"** (`366:16829`). Primer paso del asistente de alta de producto **cuando el producto NO tiene variantes**. Se llega desde el menú de creación de §P.6 ("Agregar producto").
> Es un **formulario largo** (una sola pantalla scrolleable de **3773px**) organizado en 8 bloques colapsables, bajo 5 sub-tabs. El paso 1 cubre el tab **"Información general"**.
> **Figma:** `366:16829`. **Owner:** Karla Salazar — Head of UX/UI.

## PA.1 Mapa del paso

```
Nuevo producto  (sub-tabs: Información general · Precio e inventario · SEO · Catálogo · Sucursales)
│  ← el paso 1 es "Información general"
│
├── Información básica         Nombre · Descripción · Marca ▾ · Categoría ▾
├── Identificadores            SKU · Código de barras (EAN, ISBN, UPC, GTIN)
├── Variantes del producto     switch "Producto con variantes" (OFF en este paso)
├── Multimedia                 grid 2-col de imágenes (portada, drag, borrar, +) + badge de recomendaciones
├── Especificaciones           Color/Tono con chips + catálogo de especificaciones + "Agregar especificación"
│     └── sheet "Añadir opción" (Nombre · Color · Valor base)
├── Clasificación              Tipo · Proveedor · Etiquetas (chips) · Catálogo (chips)
├── Publicar en                checklist de canales (Tienda en línea, PDV, Sears, Sanborns, Shein, TikTok, Amazon)
│
└── [Descartar]  [Continuar]   ← barra inferior fija
```

## PA.2 Chrome

- **Header:** back (`arrow-up` rotado) + **"Nuevo producto"** + divisor.
- **Sub-tabs:** **Información general** (activa: `B2 S` + subrayado `1.5px #DB3B2B`) · Precio e inventario · SEO · Catálogo · Sucursales (inactivas `B2 M` `#4C4C4C`).
- **Barra inferior fija:** `bg white`, sombra `0 0 2.35px rgba(0,0,0,.1)`, `pt8 pb24 px16` — **Descartar** (secundario, h40/r12/`B2 M`) + **Continuar** (primario `#DB3B2B`, h40/r12/`B2 S`), ambos al 50%.

> 🔴 **Los mismos tabs rotos que en el Listado (§P.2).** Aquí: "Catálogo" en `left: 370` (ancho ~91 → llega a 461) y "Sucursales" en `left: 391` → **se solapan** y ambos quedan **fuera de la pantalla de 360**. Es el mismo componente defectuoso, reutilizado.

## PA.3 Encabezados de bloque

Todos los bloques comparten patrón: título **`Manrope SemiBold 12`, `#4B5563`, UPPERCASE** + `arrow-down-01-sharp` (colapsar). Contenido con `gap 24`.

> 🔴 **Anomalía Manrope, de nuevo — y aquí es masiva.** Los **8 encabezados de bloque** de este formulario (Información básica, Identificadores, Variantes, Multimedia, Especificaciones, Clasificación, Publicar en) usan **Manrope SemiBold**, no Inter. La App es Inter-only salvo Nova. Este form, siendo Inter en todos sus campos, pone los **títulos de sección en Manrope**. Suma a las instancias ya rastreadas (§N, §D).
> 🔴 Los encabezados usan `#4B5563` (Greys/100), el tercer gris ya señalado (§D.10).

## PA.4 Bloque: Información básica — `366:15021`
Campos (todos input `Inactive/Default`, h55, radio 20, borde `1px #F3F3F3`, label `B2 S`, `gap 7.328`):
| Campo | Control | Placeholder |
|---|---|---|
| Nombre del producto | texto | ej. Playera polo de manga corta (`#C3C3C3`) |
| Descripción | **textarea h196** | "Descripción aquí" |
| Marca | select (`arrow-down-01-sharp`) | ej. Polo (`#4C4C4C`) |
| Categoría | select | Camisas en Ropa y accesorios (`#4C4C4C`) |

> 🔴 **El textarea "Descripción" usa Manrope y medidas rotas:** placeholder en **`Manrope Regular 12.824px`**, borde **`0.916px`**, radio **`18.321px`**, padding **`18.321`**. Todo el resto de inputs es Inter / borde 1 / radio 20. Este textarea es un componente escalado y en otra tipografía.
> ⚠️ **Dos colores de placeholder:** Nombre/SKU/Código en `#C3C3C3` (Greys/400) vs Marca/Categoría/Tipo/Proveedor en `#4C4C4C` (texto real, no placeholder — son valores de ejemplo pre-llenados).

## PA.5 Bloque: Identificadores del producto — `366:15052`
Dos campos: **SKU** (placeholder "Ej. POL78912344") y **Código de barras (EAN, ISBN, UPC, GTIN)** (placeholder "Ej. 12345678912344"). Mismos inputs h55/r20.

## PA.6 Bloque: Variantes del producto — `366:15083`
Tarjeta `bg #F8F8F8`, radio 16, `px12 py16`: fila con **"Producto con variantes"** (`B2 S`) + **switch** (`36×20`) + subtítulo *"Agrega tus variantes desde la sección de Precio y variantes."* (`B3 R` `#4C4C4C`).

> **En el paso 1 el switch está OFF** (producto sin variantes). Al activarlo se entra al flujo del paso 1-con-variantes (documentar aparte).

## PA.7 Bloque: Multimedia — `366:15313`
- Subtítulo *"Sube fotos o videos de tu producto."* (`B2 R` `#4C4C4C`).
- **Badge** (`bg #F0F8FF` Blue/500, radio 8, `bulb` 12 + `B3 M` `#2180FF`): *"Recomendaciones para optimizar tus imágenes"* → abre la pantalla **Recommendations** (§PA.11).
- **Grid 2-col** de celdas `159.9×163.5`, radio `14.537`:
  - Cada imagen: botón **borrar** (círculo `#F3F3F3` 29, `delete-02`) + handle **drag** (`qlementine-icons:drag`, rotado).
  - La primera lleva chip **"Foto de portada"** (`bg #F0F8FF`, texto `#005EDC` Blue/200, `B3 S`).
  - Última celda: **"+"** (borde punteado `1.363px #C3C3C3`, botón circular rojo `#DB3B2B` con `Plus`).

> 🔴 **Todo el bloque en medidas fraccionarias:** celdas `159.911×163.546`, radio `14.537`, gap `8/7.269`, círculos `29.075`, iconos `14.537/21.806`, borde punteado `1.363`. Es un **componente escalado** (factor ~0.909). Reconstruir a la escala base.
> 🔴 **Dos azules para el mismo rol:** el chip "Foto de portada" usa texto `#005EDC` (Blue/200) mientras el badge y los chips de especificación usan `#2180FF` (Blue/300). Definir el azul de acento.

## PA.8 Bloque: Especificaciones — `366:15114`
- Filas **Color:** / **Tono:** (label `B3 S`) con **botón "Seleccionar color"** (`bg #F8F8F8`, radio 8, h32) + **chips** de valores elegidos (`bg #F0F8FF`, texto `#2180FF`, `x` para quitar).
- **"Agregar más especificaciones"** (`B1 S` 16).
- **Chip punteado "Agregar especificación +"** (borde dashed `#4C4C4C`) + **catálogo de especificaciones disponibles** como chips grises (`bg #F8F8F8`, `#1F2937`): Grupo de edad · Actividad · Color · Instrucciones de cuidado · Tipo de cierre · Material del calzado · Tipo de altura del tacón · Estampado · Características del calzado · Ajuste del calzado · Talla de calzado · Género objetivo · Estilo de puntera.

> 🔴 El botón dice "Seleccionar **color**" incluso en la fila **Tono** — label sin parametrizar.

### PA.8.1 Estados progresivos del bloque (sección "Specification" `907:34708`)

La sección **"Specification"** documenta el bloque de especificaciones en **estados incrementales** — no es contenido nuevo, es el mismo bloque §PA.8 en sus fases de llenado. Verificado nodo por nodo:

| Estado | Nodo | Contenido del bloque |
|---|---|---|
| Vacío | `907:28940` | solo "Agregar más especificaciones" + catálogo de chips |
| 1 spec (Color) | `907:29690` | fila **Color:** + catálogo |
| 2 specs (Color+Tono) | `907:30205` | filas **Color:** y **Tono:** |
| Con valores | `907:33606` | specs como **select + chips** (ver §PA.8.2) |
| Dropdown de valores | `907:33606` | menú desplegado con opción **"+ Añadir {valor}"** (§PA.8.3) |

> 🔴 **El encabezado del bloque cambia de gris entre secciones:** en el form principal (§PA.3) es **`#4B5563`** (Greys/100); aquí en "Specification" el mismo encabezado es **`#9CA3AF`** (Greys/300). Dos grises para el mismo encabezado según la pantalla.

### PA.8.2 🔴 Especificación agregada — dos anatomías distintas

**Hallazgo importante:** una especificación ya agregada se representa de **dos formas incompatibles** en la misma sección:

| | **Forma A** (Color/Tono, `366:15114`) | **Forma B** (Marca/Manga, `907:33745`) |
|---|---|---|
| Label | "Color:" / "Tono:" (con dos puntos) | "Marca" / "Manga" (sin dos puntos) |
| Control | **botón "Seleccionar color"** (`bg #F8F8F8`, h32, r8) | **input select** "Ej. Polo" (h55, r20, `arrow-down-01-sharp`) |
| Valores | chips debajo del botón | **chip debajo del select** (`Polo`, azul `#2180FF`) |
| Layout | label a la izquierda, control a la derecha | label arriba, select+chip apilados |

Son **dos componentes de "fila de especificación" que no coinciden**. Definir uno canónico.

### PA.8.3 Dropdown de valores — crear nuevo — `907:33900`
Al abrir el select de valores de una spec, aparece un **menú desplegable** (`280×135`) con las opciones existentes (ej. "Amarillo") y, al final, una acción **"+ Añadir {texto buscado}"** (`B2 S` negro) para **crear un valor nuevo** con el término tecleado.

> ✅ Patrón útil (crear-al-vuelo desde el buscador). Documentar como componente reutilizable de select con creación.

### PA.8.4 Dos sheets distintos de especificación

Hay **dos** bottom sheets, no uno. Ambos: scrim `rgba(0,0,0,0.2)`, panel blanco radio-top 16, título **`B1 B` (Inter Bold 16)** 🔴 *(segundo Bold de la App)*, input **Nombre** con contador **"0/30 caracteres"** (`#6B7280` 🔴 *quinto gris*), botones Cerrar (sec 160) + Agregar (pri 160).

| Sheet | Nodo | Alto | Campos |
|---|---|---|---|
| **"Añadir opción"** | `4181:94276` | h467 | Nombre · **Color** (`#000000`) · **Valor base** (select "Selecciona") |
| **"Agregar especificaciones"** | `907:34136` | h248 | **solo** Nombre |

> 🔴 **Dos títulos, dos alturas, mismo propósito aparente.** "Añadir opción" pide Color + Valor base; "Agregar especificaciones" solo el nombre. Definir cuándo se usa cada uno, o unificar.
> 🔴 **Input del sheet con medidas rotas:** borde `0.916px`, tipografía `13.43px`, `tracking -0.2686`, padding `16.489`. Mismo componente escalado que el textarea (§PA.4) y que §D.4.7.
> 🔴 **Quinto gris de texto:** `#6B7280` (Greys/200) en el contador, junto a `#4C4C4C`, `#4B5563`, `#4F4F4F`.

## PA.9 Bloque: Clasificación del producto — `366:15145`
Campos: **Tipo de producto** (ej. Polo) · **Proveedor** (ej. Polo) · **Etiquetas** (select "Seleccionar" + chips *Camisas · Unisex · Polo*) · **Catálogo** (select + chips *Descuento · Camisas*).

## PA.10 Bloque: Publicar en — `366:15207`
Checklist de **7 canales** con checkbox `Control` (radio 4, `On`=`#DB3B2B`):
| Canal | Estado | Logo |
|---|---|---|
| Tienda en línea | ✅ On | — |
| Punto de venta | ✅ On | — |
| Sears | ✅ On | logo 22px |
| Sanborns | ⬜ Off | logo |
| Shein | ⬜ Off | logo |
| TikTok | ⬜ Off | logo |
| Amazon | ⬜ Off | logo |

Los dos primeros (Tienda en línea, PDV) sin logo y con **divisor** antes de Sears (separación canales propios vs marketplaces).

> ⚠️ **"Publicar en" reusa el mismo dato "1/3 canales"** que la tarjeta de producto (§P.3). Aquí se ve el detalle: 3 de 7 activos. Confirmar que el "1/3" de la tarjeta cuenta **canales propios** (Tienda/PDV/Sears) y no el total.

## PA.11 Pantalla: Recommendations — `367:28307`
Pantalla de ayuda (se abre desde el badge de Multimedia). Lista de recomendaciones para imágenes con valor destacado + descripción:
`>1000px` resolución · `1:1 / 3:4` proporción · `70-80%` producto en foco · fondo claro · `3 a 10` imágenes · `<5MB` `JPG`/`PNG` formato.

## PA.12 Componentes nuevos
- **Input de formulario largo** (`Inactive/Default`, h55, radio 20) — select, textarea y texto.
- **Switch** (36×20) — primer switch documentado en la App.
- **Uploader multimedia** (grid, portada, drag, borrar, celda +).
- **Selector de especificaciones** (chips catálogo + chip punteado "agregar").
- **Checklist de canales** con logos de marketplace.
- **Sheet "Añadir opción"** (form corto en bottom sheet).
- **Badge informativo** (`bulb` + texto azul).

## PA.13 Pendientes (🔴)

1. 🔴 **8 encabezados de bloque en Manrope** (Inter-only salvo Nova) — anomalía masiva en un solo form (§PA.3).
2. 🔴 **Tabs rotos/solapados** (Catálogo 370, Sucursales 391) — mismo componente defectuoso del listado (§PA.2).
3. 🔴 **Textarea "Descripción" en Manrope 12.824px** + borde `0.916` + radio `18.321` (§PA.4).
4. 🔴 **Bloque Multimedia completo en medidas fraccionarias** (factor ~0.909) (§PA.7).
5. 🔴 **Sheet "Añadir opción": input escalado** (borde `0.916`, texto `13.43`) (§PA.8.1).
6. 🔴 **Dos azules de acento:** `#005EDC` (Blue/200) vs `#2180FF` (Blue/300) (§PA.7).
7. 🔴 **Quinto gris de texto:** `#6B7280` en el contador de caracteres (§PA.8.1).
8. 🔴 **`#4B5563` (tercer gris) en los 8 encabezados** (§PA.3).
9. 🔴 **Label sin parametrizar:** botón "Seleccionar color" reutilizado en la fila Tono (§PA.8).
9b. 🔴 **Dos anatomías de "fila de especificación"** (Color/Tono con botón vs Marca/Manga con select+chip) — §PA.8.2.
9c. 🔴 **Dos sheets de especificación** ("Añadir opción" h467 con Color/Valor base vs "Agregar especificaciones" h248 solo Nombre) — §PA.8.4.
9d. 🔴 **Encabezado del bloque en dos grises** según la pantalla: `#4B5563` (form) vs `#9CA3AF` ("Specification") — §PA.8.1.
10. 🔴 **`B1 B` (Inter Bold)** en el título del sheet — segundo Bold de la App (§PA.8.1).
14. ⚠️ **Dos colores de placeholder** (`#C3C3C3` vs `#4C4C4C`) sin criterio claro (§PA.4).
15. **Sin estados:** sin validación de campos, sin error de carga de imagen, sin confirmación al descartar (los campos requeridos no están marcados).
16. Íconos a `icons.ts`: `arrow-down-01-sharp`, `delete-02`, `qlementine-icons:drag`, `plus`, `bulb`, `x`, switch.

## PA.15 Referencias
- *Step 1: If product don't have variants* (`366:16829`).
- **Form completo:** `366:15007` (3773px). Bloques: básica `366:15021` · identificadores `366:15052` · variantes `366:15083` · multimedia `366:15313` · especificaciones `366:15114` · clasificación `366:15145` · publicar en `366:15207`.
- **Colapsados/expandidos:** `364:13857`, `366:15814`.
- **Sección "Specification"** (`907:34708`): estados del bloque `907:28940` (vacío) · `907:29690` (1) · `907:30205` (2) · `907:33606` (valores + dropdown).
- **Sheets:** "Añadir opción" `4181:94276` (h467) · "Agregar especificaciones" `907:34136` (h248). Dropdown de valores `907:33900`.
- **Ayuda:** Recommendations `367:28307`.
- **Footer:** `366:15013`. **Sub-tabs:** `4181:94232`.
- Reutiliza: input de form §CP.4.3 · chips §D.3 · sub-tabs (defectuosos) §P.2.

---

# Flujo 18 — Agregar producto · Paso 2 (Precio e inventario)

> **Sección "Step 2: If product don't have variants"** (`366:16828`). Segundo paso del alta **sin variantes** — corresponde al sub-tab **"Precio e inventario"**.
> **Nota sobre el nombre en Figma:** la sección se titula "Step 2: If product **don't** have variants" (igual que el paso 1). El contenido es el tab de precio/inventario que sigue a "Información general".
> Es un **formulario scrolleable de 1629px** (más corto que el paso 1) con **3 bloques colapsables**: Precio · Inventario · Envíos. Incluye tooltips y un sheet "Editar sucursales".
> **Figma:** `366:16828`. **Owner:** Karla Salazar — Head of UX/UI.

## PB.1 Mapa del paso

```
Nuevo producto  (sub-tabs: Información general · Precio e inventario ← activo · SEO · Catálogo · Sucursales)
│
├── Precio        Precio base · Precio de oferta (ⓘ) · Costo del producto (ⓘ)
│                 Ganancia (ⓘ, calculado) · Margen (ⓘ, calculado)
│                 ☑ Mi producto cobra IVA. (ⓘ)
├── Inventario    [Editar sucursales] · Sucursal 1/2/3 (Unidades disponibles)
│                 Stock de seguridad (ⓘ) · ☐ Continuar vendiendo en línea cuando no haya stock.
│                 └── sheet "Editar sucursales" (checklist + Cerrar/Guardar)
├── Envíos        Largo · Ancho · Alto · Peso (grid 2col) · Días de envío (ⓘ)
│
└── [Descartar]  [Continuar]
```

> **Los 3 bloques se muestran colapsados por defecto** (`hidden=true` en Figma para el contenido). La pantalla expandida (1629px) es el estado **todo expandido**.

## PB.2 Chrome
Idéntico al paso 1: header "Nuevo producto" + back, sub-tabs (ahora **"Precio e inventario"** activo), footer Descartar + Continuar.

> 🔴 **Sub-tabs aún más rotos que en el paso 1.** El contenedor de tabs mide **620px** (vs 360 de pantalla) y aparece **"SEO" DUPLICADO**: dos frames consecutivos con el mismo texto "SEO" (`x:305` y `x:365`). Además Catálogo (`x:425`) y Sucursales (`x:516`) quedan muy fuera de pantalla. Es el mismo componente de tabs defectuoso (§P.2/§PA.2) **y encima con un tab repetido**.

## PB.3 Encabezados de bloque
Mismo patrón del paso 1 pero con una diferencia: aquí los títulos (Precio, Inventario, Envíos) son **`text 16 / #000` (no Manrope, no uppercase)** — usan un estilo distinto al `Manrope SemiBold #4B5563 uppercase` del paso 1.

> 🔴 **Inconsistencia entre pasos:** los encabezados de bloque del paso 1 son Manrope uppercase gris; los del paso 2 son texto normal 16px negro. Mismo asistente, dos estilos de encabezado de bloque.

## PB.4 Bloque: Precio — `366:16410`
Grid flexible (`gap 16/8`) de campos, todos input h55/r20:
| Campo | Ancho | Tipo | Placeholder / valor |
|---|---|---|---|
| Precio base | 160 | input | ej. $1,000,000 |
| Precio de oferta | 160 | input + **ⓘ** | ej. $1,000,000 |
| Costo del producto | 328 | input + **ⓘ** | ej. $1,000,000 |
| **Ganancia** | 160 | **botón calculado** | **$122,345.00** |
| **Margen** | 160 | **botón calculado** | **90%** |

- **Ganancia y Margen** son **valores calculados**, no inputs: botón `bg #F0FDF4` (Green/500), texto **`#4FC153`** (Green/300), `B2 S`.
- **Checkbox "Mi producto cobra IVA."** (marcado ON) + **ⓘ** → tooltip: *"Al activarlo, se agregará el 16% al precio configurado en T1 para el cliente final."*

> 🔴 **El cuarto verde otra vez, y ahora como fondo de campo:** Ganancia/Margen usan `#4FC153`/`#F0FDF4` — el mismo par del chip "Activo" de la tarjeta de producto (§P.3.2). Aquí significa "valor calculado positivo", allá "estado activo". Mismo verde, dos semánticas.

## PB.5 Bloque: Inventario — `366:16584`
- **Botón "Editar sucursales"** (secundario h32/r8, `pencil-edit-02` + `B3 M`) → abre el sheet (§PB.7).
- **Sucursal 1/2/3 (Unidades disponibles)** — 3 inputs h55, placeholder "ej. 30".
- **Stock de seguridad** + **ⓘ** — input, placeholder "ej. 25".
- **Checkbox "Continuar vendiendo en línea cuando no haya stock."** (**OFF**).

## PB.6 Bloque: Envíos — `366:16472`
- Texto intro: *"Ingresa la información de tu producto empaquetado para el envío."*
- Grid 2col: **Largo (cm)** "Ej. 10" · **Ancho (cm)** "ej. 15" · **Alto (cm)** "ej. 25" · **Peso (kg)** "ej. 1".
- **Días de envío** + **ⓘ** — input, placeholder "ej. 2".

## PB.7 Sheet: Editar sucursales — `907:62849`
Bottom sheet (h248, radio-top 16): **título "Editar sucursales"** (`B1 B` Inter Bold 16), **checklist**:
- ☑ Sucursal 1 (ON) · ☑ Sucursal 2 (ON) — checkbox `Control` + `B2 M` `#4C4C4C`.
- Botones **Cerrar** (secundario 160) + **Guardar** (primario 160).

## PB.8 Tooltips (ⓘ) — `907:63360`
Los `information-circle` abren tooltips (caja + cola/polígono). Textos verificados:
| Campo | Tooltip |
|---|---|
| Precio de oferta | "Precio con descuento o promocional. Se mostrará a los clientes en lugar del precio base." |
| Costo del producto | "Costo de adquisición o fabricación. Ayuda a calcular la ganancia y el margen." |
| Ganancia | "Diferencia en monto y porcentaje entre el precio de venta y el costo del producto. Se calcula automáticamente." |
| Margen | "Es el porcentaje de ganancia sobre el precio total." |
| Mi producto cobra IVA | "Al activarlo, se agregará el 16% al precio configurado en T1 para el cliente final." |
| Stock de seguridad | "Cantidad mínima de producto para evitar quedarte sin inventario por imprevistos o picos de demanda." |
| Días de envío | *(no capturado en el frame de tooltips; confirmar)* |

> ✅ **Primer sistema de tooltips documentado de la App.** Componente verificado: caja blanca, borde `1px #F3F3F3`, **radio 12**, sombra `0 4px 5.3px rgba(0,0,0,.1)`, texto `B3 R #4C4C4C` **ancho 220**, **cola superior centrada** (polígono `10×9`). El "242" es el frame contenedor, no la caja.

## PB.9 Componentes nuevos
- **Campo calculado** (botón verde no editable: Ganancia, Margen).
- **Tooltip** (`information-circle` + caja con cola).
- **Botón "Editar sucursales"** (secundario compacto h32).
- **Sheet de checklist** (Editar sucursales).
- **Grid de dimensiones** (Largo/Ancho/Alto/Peso).

## PB.10 Pendientes (🔴)

1. 🔴 **"SEO" DUPLICADO** en los sub-tabs — **confirmado como texto real** (ambos `B2 M`), no nombre de capa (§PB.2).
2. 🔴 **Sub-tabs en contenedor de 620px**, muy fuera de la pantalla de 360 (§PB.2).
3. 🔴 **Encabezados de bloque en estilo distinto al paso 1** (texto 16 negro vs Manrope uppercase gris) (§PB.3).
4. 🔴 **Cuarto verde `#4FC153`** como fondo de Ganancia/Margen, misma pareja que el chip "Activo" (§PB.4).
7. 🔴 **Medidas fraccionarias** heredadas en todos los inputs (`gap 7.328`, `y 24.328`, campos `514.313`, etc.).
9. **Sin estados:** sin validación (precio de oferta > base, margen negativo), sin error, campos requeridos sin marcar.
10. Íconos a `icons.ts`: `information-circle`, `pencil-edit-02`.

## PB.12 Referencias
- *Step 2: If product don't have variants* (`366:16828`).
- **Colapsado:** `366:16107`. **Expandido:** `366:16396` (1629px). **Variante:** `366:16683`.
- **Bloques:** Precio `366:16410` · Inventario `366:16584` · Envíos `366:16472`.
- **Sheet:** Editar sucursales `907:62849` (contenedor `907:63132`).
- **Tooltips:** `907:63360`.
- Reutiliza: input de form §PA.4 · footer §PA.2 · sub-tabs (defectuosos) §PA.2.

---

# Flujo 18 — Agregar producto · Paso 2 CON variantes (§PC)

> **Sección "Step 2: If product have variants"** (`366:17295`). Es el paso 2 cuando el producto **sí tiene variantes** — reemplaza el sub-tab "Precio e inventario" (§PB) por **"Precio y variante"** y despliega un **sub-flujo completo** de creación/edición de variantes (~19 pantallas: asistente, selectores de valores, sheets, menús y modal de borrado).
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `366:17295`.

## PC.1 Mapa del flujo

```
Tab "Precio y variante"  (366:17296 colapsado inicial · 403:22672 con datos)
│  Tarjeta producto ("Polo de mujer" · subtítulo "Sin variantes" 🔴)
│  ├── VARIANTES (lista de tipos, cada uno colapsable)
│  │     Color → Azul, Rojo, Verde
│  │     Estampado → Floral, Animal print, Puntos
│  │     Talla → S, M, L        [+ Agregar variante]
│  └── Inventario y precio (combinaciones)
│        Azul / Floral / S · 23 unidades | $3,456.99   (×3 idénticas 🔴)
│
├─▶ "Variantes"  (401:36393 / 401:36539 / 403:21847)
│     Lista de tipos + [Agregar variante]
│     └─▶ "Agregar variante" (401:32965) — 6 categorías (Categoria 1 > Subcat)
│
├─▶ "Valores de color"  (401:33453 base / 401:34043 con sheet / 401:34217 con chips)
│     15 colores (swatch + check) · "Agregar color personalizado"
│     └─▶ sheet "Añadir color personalizado" (4181:94472 / 4181:94530)
│           Nombre 0/30 · Color #000000 · Valor base "Selecciona"
│
├─▶ "Valores de talla"  (401:35473 / 401:35669 / 401:35799 / 403:21229)
│     Agrupada Adultos (XXXS…XXL) / Niños (0 a 3 meses…) · "Agregar talla personalizada"
│     └─▶ "Editar talla" (403:21229) con more-vertical → menú "Eliminar variante" (403:21942)
│
├─▶ "Variante personalizada"  (401:36117 vacía / 401:36305 con chips)
│     Nombre de variante "Ej. Camisa" · Crear valores (chips + "Añadir")
│
├─▶ Edición inventario/precio por combinación  (403:22849 / 403:23303)
│     Chips de filtro (Color/Estampado/Talla) · lista por combinación
│     Unidades disponibles · Precio base · Precio oferta
│     └── validación: "Precio oferta debe ser menor al precio base" 🔴
│
└─▶ Modal "Eliminar variante"  (403:21477) — confirmación destructiva
```

## PC.2 Tab "Precio y variante" — `403:22672`

Núcleo del paso. Tres zonas apiladas (`gap 32`):

**a) Tarjeta de producto** (`bg #F8F8F8` r16, h84): thumbnail 64 (r**14.537** 🔴 fraccionario) + **"Polo de mujer"** (`B1 S`) + subtítulo **"Sin variantes"** (`B2 R #4C4C4C`).

**b) Sección VARIANTES**: encabezado **"VARIANTES"** (Manrope SemiBold `#4B5563` uppercase 🔴 *Manrope fuera de Nova*) + card blanca r12 con filas divididas:
| Tipo | Valores (ejemplo) | Control |
|---|---|---|
| Color | Azul, Rojo, Verde | chevron (rotado -90°) |
| Estampado | Floral, Animal print, Puntos | chevron |
| Talla | S, M, L | chevron |
- Cada fila: label `B2 S` + valores `B3 R #4C4C4C` + `arrow-down-01-sharp` rotado. Debajo, botón **"Agregar variante"**.

**c) Sección "Inventario y precio"**: encabezado Manrope + card con combinaciones. Cada fila: combinación `B2 S` (ej. "Azul / Floral / S") + detalle `B3 R` "23 unidades | $3,456.99".

> 🔴 **Las 3 combinaciones son idénticas:** "Azul / Floral / S · 23 unidades | $3,456.99" repetida literal 3 veces. En el estado vacío sí varían (Azul/Floral/S, Azul/Animal print/S, Azul/Puntos/S) con detalle **"-- --"**. Datos de ejemplo sin variar en el estado "con datos".

**Estados del tab:**
| Estado | Nodo | Diferencia |
|---|---|---|
| Colapsado inicial | `366:17296` | solo tarjeta + botón "Agregar tu primer variante" |
| 2 variantes, combinaciones vacías | `401:32739` | Color+Estampado · combinaciones "-- --" |
| 3 variantes, combinaciones vacías | `401:32850` | Color+Estampado+Talla · combinaciones "-- --" |
| Con datos | `403:22672` | combinaciones "23 unidades \| $3,456.99" |

## PC.3 Sub-flujo "Variantes" (lista de tipos)
Pantalla **"Variantes"** (`401:36393` / `401:36539` / `403:21847`): lista los tipos de variante creados (Color, Talla, Estampado) como filas colapsables (label + valores) + botón **"Agregar variante"**. Es la versión de página completa de la sección VARIANTES del tab.

- **"Agregar variante"**: 6 filas de categoría **"Categoria 1 > Subcat"** (`Frame 2147224742`) con chevron — plantillas/placeholder de categorías.

## PC.4 Selector "Valores de color" — `401:34042`
Lista scrolleable de **15 colores**, cada fila: **checkbox** `Check` (ON = `#DB3B2B` r4) + **swatch** de color (r4, 15px) + nombre (`B2 M`). Primera fila fija: **"Agregar color personalizado"** con `plus-sign-square`.

**Colores con hex reales verificados:**
| Color | Hex | Color | Hex |
|---|---|---|---|
| Azul | `#2F80ED` | Café | `#963D00` |
| Azul claro | `#56CCF2` | Morado | `#6537AE` |
| Amarillo | `#F2C94C` | Rojo | `#DB3B2B` |
| Blanco | `#FFF` (borde `#E7E7E7`) | Rosa | `#FFC0C7` |
| Gris | `#ADADAD` | Turquesa | `#2BEEBD` |
| Negro | `#333` | Verde | `#51AF70` |
| Magenta | `#CD2BEE` | Lavanda | `#D1E5FF` |

- **Estados:** base, con sheet abierto, con chips de selección arriba (chips de colores elegidos).

> 🔴 **Rojo del swatch = `#DB3B2B`** (marca) y **Verde = `#51AF70`** (Green/400): confirman los valores ya rastreados. El swatch reутiliza el token de marca como "color de producto", no como acento de UI.

### PC.4.1 Sheet "Añadir color personalizado" — `4181:94472` / `4181:94530`
Bottom sheet (scrim `.2`, panel r-top, h467): título **"Añadir color personalizado"** + **Nombre** (input + "0/30 caracteres") + **Color** (`#000000`) + **Valor base** (select "Selecciona") + botones Cerrar/—. Mismo sheet que el de especificaciones del paso 1 (§PA.8.4) pero con campo **Color**.

## PC.5 Selector "Valores de talla" — `401:35486`
Lista **agrupada** por encabezado de sección:
- **Adultos:** XXXS, XXS, XS, S, M, L, XL, XXL.
- **Niños:** 0 a 3 meses, 3 a 6 meses, 6 a 9 meses…
- Cada talla: checkbox `Check` + nombre. Primera fila: **"Agregar talla personalizada"** (`plus-sign-square`).
- Estados: base, con input "Agregar valor personalizado" + `delete-02`, con chips de selección.

### PC.5.1 "Editar talla" + menú kebab — `403:21229` / `403:21942`
La pantalla "Editar talla" agrega un **`more-vertical`** en el header → abre menú **"Eliminar variante"** (`delete-02` + label, 161×48). El menú tiene 6 filas "Opción" ocultas (plantilla de menú reutilizable).

## PC.6 "Variante personalizada" — `401:36320`
Para crear un tipo de variante nuevo (no Color/Talla/Estampado):
- **Nombre de variante** — input, placeholder **"Ej. Camisa"**.
- Divisor.
- **"Crear valores para tu variante"** — **chips** de valores ya creados (Floral, Animal print, Puntos; `bg #F8F8F8` r6, texto negro `B3 S`, x de borrar) + campo **"Agregar valor personalizado"** con acción **"Añadir"** a la derecha.
- Estados: vacía sin chips y con chips.

> Nota: el chip aquí es **gris `#F8F8F8` con texto negro** — distinto del chip azul `#F0F8FF`/`#2180FF` de las especificaciones (§PA.8). Dos estilos de chip en el mismo asistente de alta.

## PC.7 Edición inventario/precio por combinación — `403:23303`
Al tocar una combinación se abre una pantalla **"Precio e inventario"** (título propio) con:
- **Chips de filtro** arriba: Color / Estampado / Talla o valores concretos (Azul, Puntos, L) con `cancel-01` para quitar.
- **Lista larga por combinación** (h832): cada combinación es un bloque con label (Manrope `#4B5563`, ej. "Azul / Floral / Niña") + **Unidades disponibles** + **Precio base** + **Precio oferta**.
- Botón único **"Guardar"** full-width.

### PC.7.1 🔴 Primer estado de validación/error de la App — `403:23330`
En la combinación "Azul / Floral / Niña" con datos (Unidades "23", Precio base "$98.99", Precio oferta "$99.99"):
- El input **Precio oferta** tiene **borde rojo `#DB362B`** y debajo el mensaje **"Precio oferta debe ser menor al precio base"** (`B3 R` rojo).

> 🔴 **Primer patrón de validación de campo documentado en toda la App.** Definir el componente de input en estado error (borde + mensaje) como átomo reutilizable.
> 🔴 **SEXTO ROJO — `#DB362B`** (token `background/state-indicators/error`), **distinto** del `#DB3B2B` de marca por un dígito. Confirmar si es intencional (rojo de error vs rojo de marca) o si es una desviación. Se suma a la lista de rojos ya rastreada.

## PC.8 Modal "Eliminar variante" — `403:21477`
**Primer modal de confirmación destructiva de la App.** Scrim `rgba(0,0,0,.2)`, card blanca 328 r16 h255, centrada:
- Ícono **`delete-02`** (32) en círculo **`#FFF0EF`** (Primary/100) de 64.
- Título **"Eliminar variante"** (`T2 S`, Inter SemiBold **20**, line-height 1.3) 🔴 *primer uso de T2/20px en la App*.
- Cuerpo: *"Al eliminar esta variante, dejará de estar disponible en tu catálogo."* (`B2 R #4C4C4C`).
- Botones: **Cancelar** (secundario, flex) + **Eliminar** (primario `#DB3B2B`, flex). Ancho 147 c/u.

> ✅ Establece el patrón de **modal destructivo** (ícono en círculo suave + título + cuerpo + Cancelar/acción). Reutilizable para otras confirmaciones (Desactivar, Eliminar producto §P).

## PC.9 Componentes nuevos (primeros de la App)
- **Input en estado error** (borde `#DB362B` + mensaje) — §PC.7.1.
- **Modal de confirmación destructiva** — §PC.8.
- **Selector de valores con lista larga + swatch** (colores) y **agrupada** (tallas) — §PC.4/PC.5.
- **Fila de tipo de variante colapsable** (label + valores + chevron) — §PC.2.
- **Fila de combinación** (combinación + "N unidades | $precio") — §PC.2.
- **Chips de filtro** con `cancel-01` — §PC.7.
- **Chip gris** (variante personalizada, `#F8F8F8`/negro) — §PC.6.

## PC.10 Pendientes (🔴)

2. 🔴 **3 combinaciones idénticas** "Azul / Floral / S · 23 unidades | $3,456.99" en el estado con datos (§PC.2).
3. 🔴 **Sexto rojo `#DB362B`** (error) distinto del `#DB3B2B` de marca (§PC.7.1). Confirmar intención.
4. 🔴 **Primer estado de validación** sin documentar como átomo (input error + mensaje) (§PC.7.1).
6. 🔴 **Manrope** en los encabezados VARIANTES / Inventario y precio / labels de combinación (§PC.2, §PC.7) — suma a la anomalía Manrope.
7. 🔴 **Medidas fraccionarias** omnipresentes (`14.537`, `7.328`, `24.328`, `79.328`, `832.298`).
8. ⚠️ **Dos estilos de chip** en el mismo asistente: azul (especificaciones §PA.8) vs gris (variante personalizada §PC.6).
11. Íconos a `icons.ts`: `plus-sign-square`, `cancel-01`, `delete-02`, `more-vertical`, `checkmark-square-02`.

## PC.12 Referencias
- *Step 2: If product have variants* (`366:17295`).
- **Tab:** colapsado `366:17296` · 2 var `401:32739` · 3 var `401:32850` · con datos `403:22672`.
- **Variantes:** `401:36393`/`401:36539`/`403:21847` · Agregar variante `401:32965`.
- **Valores color:** `401:33453`/`401:34043`/`401:34217` · sheet `4181:94472`/`4181:94530`.
- **Valores talla:** `401:35473`/`401:35669`/`401:35799` · Editar talla `403:21229` · menú `403:21942`.
- **Variante personalizada:** `401:36117`/`401:36305`.
- **Edición combinación:** `403:22849`/`403:23303` · validación `403:23330`.
- **Modal:** Eliminar variante `403:21477`.

---

# Flujo 18 — Agregar producto · Paso 3: SEO (§PD)

> **Sección "Step 3: SEO"** (`367:18786`). Tercer sub-tab del alta. Es el **más simple** del asistente. Tiene **dos escenarios** según si el comercio ya tiene tienda en línea:
> - **CON tienda / CON plan:** formulario SEO (Meta título · Descripción · URL) + vista previa en el buscador.
> - **SIN PLAN:** en lugar del formulario, una **tarjeta de upsell** para crear tienda con IA.
>
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `367:18786`.

## PD.1 Mapa del paso

```
Nuevo producto  (sub-tabs)
│
├── [CON tienda]                              ├── [SIN PLAN]  (674:60106)
│   SEO (form)                                │   Barra de progreso "PASO 3/3 · SEO"
│   ├── texto ayuda                           │   Tarjeta upsell (imagen + glass card)
│   ├── Meta título        (input)            │   ├── "Crea tu tienda en línea
│   ├── Descripción        (textarea)         │   │    en segundos con IA"
│   ├── URL                (input)            │   └── [+ Crear tienda]  (CTA IA)
│   └── Vista previa en el buscador
│       (favicon + tienda + URL + título + desc)
│
└── [Descartar] [Continuar]
```

> Dos layouts de estado del bloque SEO: **expandido inline** (sin encabezado colapsable, form directo) y **colapsable** (encabezado "SEO" con chevron, contenido `hidden`). Igual patrón mixto que en los pasos anteriores.

## PD.2 Chrome
Header "Nuevo producto" + back, footer Descartar + Continuar.

> 🔴 **Los sub-tabs CAMBIARON respecto a los pasos 1-2.** Aquí el contenedor de tabs mide **344px** (más cercano a 360) y lista: Información general · **Precio y variante** · **SEO** (un solo tab, **ya no duplicado**) · **Canales de venta**. Comparar con los pasos 1-2 donde había "SEO" ×2 + "Catálogo" + "Sucursales". **Dos juegos de sub-tabs distintos conviven en el mismo asistente:**
> | | Pasos 1-2 | Paso 3 (SEO) |
> |---|---|---|
> | Tabs | Info · Precio · **SEO · SEO** · Catálogo · Sucursales | Info · Precio · **SEO** · **Canales de venta** |
> | Ancho contenedor | 611-620px | 344px |
> Definir el juego de tabs canónico. El 4º tab "Canales de venta" sugiere que "Catálogo/Sucursales" de los pasos 1-2 eran placeholders.
> **Confirmado:** no es solo cuestión de ancho — es **otro componente de tabs**. El del paso 3 usa **auto-layout** (`justify-end`, 4 tabs limpios: Información general · Precio y variante · **SEO** activo `border-b #DB3B2B` · Canales de venta); el de los pasos 1-2 usa **posiciones absolutas** solapadas con el tab repetido. Dos implementaciones distintas del mismo control.

## PD.3 Escenario CON tienda — Formulario SEO — `367:19460`
- Texto de ayuda: *"Ayuda a lograr un mejor posicionamiento en los resultados de búsqueda"* (`B2 R #4C4C4C`).
- **Meta título** — input h55, placeholder "Ej. Playera polo manga corta".
- **Descripción** — **textarea** h196, placeholder "Descripción aquí".
- **URL** — input h55, valor "https://domain/store/" (`#4C4C4C`, no placeholder gris).

> 🔴 **El textarea "Descripción" repite la deuda del paso 1:** está en **Manrope** (`font-['Manrope:Regular']`) con medidas fraccionarias — borde `0.916px`, texto `12.824px`, radio `18.321`, padding `18.321`. Es el **mismo componente escalado** que el textarea de §PA.4. La App es Inter-only salvo Nova.
> ⚠️ **URL con valor precargado, no placeholder:** "https://domain/store/" va en `#4C4C4C` (texto real), mientras Meta título va en `#C3C3C3` (placeholder).

## PD.4 Vista previa en el buscador — `367:19513`
Simula un **resultado de motor de búsqueda** (estilo Google). Card `bg #F8F8F8` r12, p16/13:
- **Fila superior:** favicon 40 (`Group 769`) + **"Nombre de la tienda"** (`B2 S`) + **"https://domain/store/collection"** (`B3 R #4C4C4C`).
- Divisor.
- **Bloque resultado:** **"Nombre del producto"** (`B1 S` 16) + descripción larga de ejemplo (*"La camiseta de manga larga acanalada es perfecta para quienes buscan comodidad sin sacrificar el estilo…"*, `B3 R #4C4C4C`).

> ✅ **Primer componente de "vista previa de SERP" de la App.** Útil como patrón reutilizable (favicon + título + URL + snippet). Los datos son de ejemplo (placeholder de preview).

## PD.5 Escenario SIN PLAN — Tarjeta de upsell — `674:60174`
Cuando el comercio **no tiene plan/tienda**, el paso 3 no muestra el form SEO. En su lugar:
- **Barra de progreso**: **"PASO 3/3"** (`B3`) + **"SEO"** (título 19) + barra `270×3` (progreso ~parcial).

> 🔴 **Indicador de paso "PASO 3/3" solo aparece en el escenario SIN PLAN.** En los pasos 1-2 y en el SEO con tienda no hay barra "PASO n/3". Inconsistencia: o el asistente es de 3 pasos con indicador siempre, o no. Definir.

- **Tarjeta de upsell** (`bg #FFF0EF` Primary/100, r16, h446): imagen de fondo + **glass card** (`backdrop-blur 15.6px`, `bg rgba(0,0,0,.2)`, r20) con:
  - Título **"Crea tu tienda en línea en segundos con IA"** (`T2 S` 20, blanco).
  - Cuerpo *"Obtén tu tienda y empieza a vender en línea de forma fácil, rápida y sin intermediarios."* (`B2 R` blanco).
  - **CTA "Crear tienda"** (botón primario `#DB3B2B`, h48 r16, ícono `add-01`/IA + `B1 M` 16).

> ✅ **Segundo uso del patrón "glass card sobre imagen" con IA** (relacionado con "Crear con IA" del menú de Productos §P.6). Vincular como sistema de upsell/IA.

## PD.6 Componentes nuevos
- **Vista previa de resultado de búsqueda (SERP)** — §PD.4.
- **Tarjeta de upsell con glass card sobre imagen** + CTA IA — §PD.5.
- **Barra de progreso "PASO n/3"** — §PD.5 (solo SIN PLAN).

## PD.7 Pendientes (🔴)

1. 🔴 **Dos juegos de sub-tabs distintos** en el mismo asistente: pasos 1-2 (SEO×2 + Catálogo + Sucursales, 611px) vs paso 3 (SEO + Canales de venta, 344px) (§PD.2). Definir el canónico.
2. 🔴 **Textarea "Descripción" en Manrope** + medidas fraccionarias — misma deuda del paso 1 (§PD.3).
3. 🔴 **Indicador "PASO 3/3" solo en el escenario SIN PLAN**, ausente en el resto del asistente (§PD.5).
4. ⚠️ **URL con valor precargado** ("https://domain/store/") vs placeholder gris del resto (§PD.3).
6. ✅ **La vista previa SERP y la tarjeta de upsell IA** son patrones reutilizables — registrarlos como componentes.

## PD.9 Referencias
- *Step 3: SEO* (`367:18786`).
- **CON tienda:** form expandido `367:19406` (`367:19460`) · colapsable `367:19527` · vista previa `367:19513`.
- **SIN PLAN:** `674:60106` · barra progreso `674:60115` · tarjeta upsell `674:60174` · CTA `674:60183`.
- Reutiliza: input/textarea §PA.4 · footer §PA.2.

---

# Flujo 18 — Agregar producto · Paso 4: Canales de venta (§PE)

> **Sección "Step 4: Sales Channels"** (`4181:94782`). Cuarto y último sub-tab del alta. Cierra el Flujo 18.
> **Concepto:** lista los marketplaces donde se puede publicar el producto (Sears, Sanborns, Shein…), cada uno como un **acordeón**. Cada canal pide **completar los datos que ese marketplace específico requiere** (multimedia, especificaciones, identificadores, precio, envíos), porque cada marketplace tiene requisitos propios.
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `4181:94782`.

## PE.1 Mapa del paso

```
Nuevo producto  (sub-tabs: Información general · Precio y variante · SEO · Canales de venta ← activo)
│
├── Lista de canales (acordeones)
│   ├── ▸ Sears      · logo + "Detalles no agregados" / "Detalles agregados"
│   ├── ▸ Sanborns   · logo + estado
│   ├── ▸ Shein      · logo + estado
│   └── … (los canales activados en "Publicar en" del paso 1)
│
└── Canal expandido (▾) → mini-formulario específico del marketplace:
    ESTADO (Activo) · Información básica · Multimedia · Categoría / especificaciones
    · Identificadores · Precio (Ganancia/Margen) · Envíos
```

> **Estados de la pantalla:** lista con canales colapsados (h780), uno o varios expandidos (h1298), y todos expandidos (h**5258** — la pantalla más alta del alta).

## PE.2 Chrome
Header "Nuevo producto" + back, sub-tabs (**"Canales de venta"** activo — el mismo componente de 4 tabs con auto-layout del paso SEO, §PD.2), footer Descartar + Continuar.

> ✅ **Confirma el juego de tabs canónico:** Información general · Precio y variante · SEO · Canales de venta. Coincide con el paso 3 (§PD) y **descarta** el "Catálogo/Sucursales" duplicado de los pasos 1-2.

## PE.3 Fila de canal (colapsada) — `4181:94798`
Cada marketplace es una fila acordeón (h84, borde inferior `#F8F8F8`):
- **Logo del canal** (40×40, r7) — Sears, Sanborns, Shein (logos reales enmascarados).
- **Nombre** (`B1 S` 16, ej. "Sears") + **estado** (`B2 R #4C4C4C`): **"Detalles no agregados"** o **"Detalles agregados"**.
- **Chevron** `arrow-right-01-sharp` rotado 90° (apunta abajo).

> **El estado es el indicador de completitud del canal:** "Detalles no agregados" (pendiente) → "Detalles agregados" (listo). No hay chip de color, es solo texto gris — a diferencia del chip "Activo"/"Inactivo" de la tarjeta de producto (§P.3).

## PE.4 Canal expandido — mini-formulario del marketplace — `4181:98185`
Al expandir un canal se despliega un **formulario propio del marketplace**. **Son 11 bloques colapsables** (no 7 — revisión completa de la pantalla alta, h5258), en este orden:

| # | Bloque | Contenido verificado |
|---|---|---|
| 1 | **ESTADO** | valor "Activo" |
| 2 | **Información básica** | **Nombre del producto\*** · Descripción |
| 3 | **Multimedia** | "Sube fotos o videos de tu producto." |
| 4 | **Categoría** | "Camisas en Ropa y accesorios" |
| 5 | **Precio** | Precio base · Precio de oferta · Costo · **Ganancia · Margen** (calculados) · ☑ "Mi producto cobra IVA." |
| 6 | **Inventario** | "Unidades disponibles: 3" + 2 textos guía: *"Edita el inventario desde la pestaña «Precio e inv…»"* y *"Si tu producto tiene variantes, actívalas en «Infor…»"* |
| 7 | **Envíos** | intro "Dimensiones de tu producto empaquetado…" · Largo/Ancho/Alto/Peso · Días de envío |
| 8 | **Atributos** | **14 campos, orden real:** Marca\* · Color · Talla · Modelo · **Marca** · Manga · Material · **Instrucciones de lavado y limpieza** (textarea) · Corte de ropa · Estilo · Lavado · Estampado · Corte de cintura · Corte |
| 9 | **Garantía** | 3 filas **"Categoria 1 > Subcat"** (selects de categoría) |
| 10 | **Inventario y reglas de precio** | intro "Define el stock de seguridad y las reglas…" · **Stock de seguridad** (ej. 3) · **Regla de precio** (Seleccionar) · **Valor** (ej. $119.99) · **Redondear** (Seleccionar) |
| 11 | *(Identificadores)* | SKU · Código de barras (EAN, ISBN, UPC, GTIN) — aparece en las variantes h1298 |

> 🔴 **Duplicación estructural masiva — y peor de lo que parecía.** El canal expandido no solo repite los bloques del alta general, sino que suma **dos bloques nuevos exclusivos del canal**: **Atributos** (14 campos de ficha textil, varios sin correspondencia en el alta general) e **Inventario y reglas de precio** (Stock de seguridad + Regla de precio + Valor + Redondear). Con 11 bloques por canal × N canales, la pantalla llega a **5258px de alto** — la más larga de toda la App.

### PE.4.1 🔴 Bloque "Atributos" — ficha de producto por canal — `4181:96933`
Lista de ~14 atributos textiles, cada uno label + input "Ej. Polo" (o textarea en "Instrucciones de lavado"). **Dos campos con asterisco de requerido** (Nombre del producto\* en Info básica, **Marca\*** aquí). El resto sin marcar.
> ⚠️ **"Marca" aparece dos veces con textos distintos:** **"Marca\*"** (con asterisco/requerido, posición 1) y **"Marca"** (sin asterisco, posición 5). No son idénticos — uno es requerido y el otro no. Confirmar si son dos campos reales o un error de duplicación.

### PE.4.2 🔴 Bloque "Inventario y reglas de precio" — nuevo en la App — `4181:96995`
Bloque **sin equivalente** en el alta general. Campos: **Stock de seguridad** (input, "ej. 3") · **Regla de precio** (select "Seleccionar") · **Valor** (input "ej. $119.99") · **Redondear** (select "Seleccionar"). Es el primer lugar donde aparece el concepto de **reglas de precio automáticas por canal**.

### PE.4.3 Bloque "Garantía" — `4181:96964`
3 filas **"Categoria 1 > Subcat"** (selects de categoría) — mismo componente de placeholder que en "Agregar variante" (§PC.3).

> 🔴 **"Nombre del producto\*" y "Marca\*" con asterisco** — los **únicos campos marcados como requeridos** en todo el alta. En los pasos 1-3 ningún campo obligatorio está marcado. Inconsistencia: o se marcan en todos lados o en ninguno.
> 🔴 **Encabezados de bloque en DOS colores dentro del mismo canal:** "ESTADO" e "Inventario y reglas de precio" son Manrope `#4B5563`; **"Envíos" es Manrope `#000` (negro)**. Inconsistencia de color en los propios encabezados.
> 🔴 **Manrope** en todos los encabezados + campos calculados verde `#4FC153` (§PB.4). Hereda ambas deudas.

## PE.5 Estados vacío vs con datos
- **"Detalles no agregados"**: el canal aún no tiene datos capturados.
- **"Detalles agregados"**: el canal ya fue completado. La diferencia visible es solo el texto de estado; el resto de la fila es idéntico.

## PE.6 Componentes nuevos
- **Fila de canal / marketplace** (logo + nombre + estado de completitud + chevron) — §PE.3.
- **Mini-formulario por marketplace** de **11 bloques** replicado dentro de un acordeón de canal — §PE.4.
- **Bloque "Atributos"** (ficha textil de ~14 campos) — §PE.4.1.
- **Bloque "Inventario y reglas de precio"** (Stock de seguridad · Regla de precio · Valor · Redondear) — nuevo en la App — §PE.4.2.
- **Estado de completitud textual** ("Detalles no agregados / agregados") — §PE.3.

## PE.7 Pendientes (🔴)

1. 🔴 **Duplicación del formulario de alta dentro de cada canal** (§PE.4).
2. 🔴 **"Nombre del producto\*" y "Marca\*"** son los únicos campos con asterisco de requerido en todo el alta (§PE.4). Unificar el marcado de campos obligatorios.
2b. 🔴 **Bloque "Atributos" (§PE.4.1):** ~14 campos textiles; "Marca" aparece dos veces (una requerida, otra no).
2e. 🔴 **Encabezados de bloque en dos colores** dentro del canal: `#4B5563` (ESTADO) vs `#000` (Envíos) (§PE.4.3).
3. 🔴 **Manrope** en los encabezados de bloque del canal + **campos calculados verde `#4FC153`** — hereda las deudas de §PA/§PB (§PE.4).
4. 🔴 **Medidas fraccionarias** heredadas de los inputs del alta.
5. ⚠️ **Estado textual sin chip de color:** "Detalles no agregados/agregados" es solo texto gris; el resto del sistema usa chips de estado (§P.3). Evaluar consistencia.
7. Íconos a `icons.ts`: `arrow-right-01-sharp` (ya usado como chevron).

## PE.9 Referencias
- *Step 4: Sales Channels* (`4181:94782`).
- **Canales colapsados:** `4181:94783` (no agregados) · `4181:95430`/`4181:96077` (agregados).
- **Expandidos:** `4181:96722`/`4181:97447` (h1298) · `4181:98172` (h5258, todos).
- **Fila de canal:** `4181:94798` (Sears) · `4181:95008` (Sanborns) · `4181:95218` (Shein).
- **Canal expandido (bloques):** `4181:98185` · ESTADO `4181:98198`.
- Reutiliza: bloques del alta §PA/§PB · sub-tabs §PD.2 · footer §PA.2.

---

# Flujo 18 — Confirmación: Producto creado (§PF)

> **Sección "OK"** (`4269:110500`). Es la **confirmación de que el producto se creó** al terminar el alta.
> **Hallazgo de partida:** NO es una pantalla de éxito dedicada. Es un **toast "Producto creado"** que aparece sobre el **listado de Productos** (§P) — el usuario regresa a la lista y ve el nuevo producto ya integrado, con un toast temporal de confirmación.
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `4269:110500`.

## PF.1 Patrón de confirmación
Al completar el alta (los 4 tabs), la app **navega de vuelta al listado de Productos** (la misma pantalla de §P) y muestra:
- El **producto recién creado** ya presente en la lista (ej. "Tommy Hilfiger Casual Mini Dress for Women").
- Un **toast "Producto creado"** flotante sobre la barra inferior.

> ✅ **Confirmación por retorno + toast, no por pantalla dedicada.** Es coherente con crear-y-continuar: no interrumpe con una pantalla de éxito a pantalla completa (a diferencia de "Crear pedido" §CP, que sí tiene pantalla de éxito). Definir cuál es el patrón canónico de confirmación (toast vs pantalla) según la acción.

## PF.2 Toast "Producto creado" — `4269:110976`
Píldora centrada sobre la barra inferior:
- **Fondo verde `#51AF70`** (Green/400), borde `#F3F3F3`, radio 12, padding `12/8`.
- Texto **"Producto creado"** (`B3 M` 12, blanco), centrado.

> 🔴 **La sombra del toast es ROJA:** `drop-shadow(0px 4px 6.75px rgba(255,0,0,0.05))`. Un toast de éxito verde con sombra roja es casi con seguridad un **error de diseño** (probablemente un token de sombra copiado de un componente destructivo). Corregir a una sombra neutra o verde.
> 🔴 **Quinto verde en la familia — `#51AF70` (Green/400):** el toast de éxito usa Green/400, mientras los campos calculados (§PB.4) usan `#4FC153` (Green/300) y el chip "Activo" también `#4FC153`. Dos verdes para dos "éxitos" distintos. Consolidar la familia de verdes con semántica clara.

## PF.3 El listado tras crear — variantes de tarjeta
La pantalla de retorno muestra el listado de §P con las **mismas tres anatomías de tarjeta** ya documentadas (§P.3), aquí con el producto nuevo:
- **Tarjeta A**: checkbox + chip + kebab arriba · Inventario "3,102 unidades | 2 variantes" · Precio "$1,234.99 - $1,300.90" (rango) · Canales "1/3".
- **Tarjeta B**: checkbox + chip + kebab · Inventario "3,102 unidades" · Canales "1/3" · Precio "$1,234.99".
- **Tarjeta C**: sin checkbox · kebab · íconos (`store-verified-02` Stock "(T1) 3,102 unidades" · `store-03` Activo "1/3" · `dollar-02` Precio) + chip abajo.

> Confirma lo documentado en §P.3: **el orden de los labels cambia entre tarjetas** (A: Inventario·Precio·Canales; B: Inventario·Canales·Precio) y **"Activo" tiene doble significado** (aquí como label de estado de canal con ícono `store-03`). Sin novedad respecto a §P.3, pero refuerza el hallazgo.

## PF.4 Chrome del listado
Header "Productos" + buscador "Busca por código, nombre, SKU…" + 2 botones (filtro/orden) + tabs (Listado de productos · Inventario · Precio · Catálogo · Sucursales) + barra inferior.

> 🔴 **Los tabs del listado siguen rotos** (los mismos de §P.2): "Catálogo" en `x:370` y "Sucursales" en `x:391` — solapados, fuera de 360. Sin cambio respecto a §P.2.

## PF.5 Componentes nuevos
- **Toast de confirmación** (píldora verde centrada sobre barra inferior) — §PF.2. **Primer toast de éxito documentado del dominio Productos.**

## PF.6 Pendientes (🔴)

1. 🔴 **Sombra roja en toast verde** (`rgba(255,0,0,0.05)`) — error de token de sombra (§PF.2).
2. 🔴 **Quinto verde `#51AF70`** (Green/400) en el toast, distinto del `#4FC153` (Green/300) de campos calculados y chip "Activo" (§PF.2). Consolidar familia de verdes.
3. 🔴 **Patrón de confirmación no unificado:** toast + retorno aquí, vs pantalla de éxito dedicada en Crear pedido (§CP). Definir cuándo se usa cada uno (§PF.1).
4. 🔴 **Tabs del listado rotos** (heredado de §P.2) (§PF.4).
5. ⚠️ **Duración/comportamiento del toast sin especificar** (auto-dismiss, tap para cerrar).

## PF.8 Referencias
- *OK* (`4269:110500`) · listado de retorno `4269:110708`.
- **Toast:** `4269:110976` (`4269:110977` texto).
- **Tarjetas:** A `4269:110710` · B `4269:110739` · C `4269:110768`.
- Reutiliza: listado y tarjetas §P · tabs §P.2 · barra inferior.

---

# Flujo 19 — Agregar producto con IA (§PG)

> **Sección "Add Product With AI"** (`4269:108999`). Flujo alternativo de alta: en vez de llenar el formulario a mano, el usuario **captura una foto** del producto y la **IA prellena** todos los campos. Se accede desde el menú "Crear con IA" del listado (§P.6).
> **El userflow trae notas del diseñador** que explican la intención de cada paso — se documentan como fuente autoritativa.
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `4269:108999`.

## PG.1 Mapa del flujo (según notas del diseñador)

```
Menú "Crear con IA" (§P.6)
│  [nota: "el usuario selecciona el proceso con IA para agregar un producto"]
│
├─▶ 1. Cámara  (4269:109453)
│     [nota: "Cuando el usuario selecciona IA, se abre la cámara para capturar el producto"]
│     · Flash on/off (nota: "Flash encendido/apagado") · botón capturar · cerrar (x)
│
├─▶ 2. Foto capturada  (4269:109542)
│     [nota: "el usuario puede tocar crear producto o tomar otra foto"]
│     · [Crear producto] [Tomar otra foto]
│
├─▶ 3. Procesamiento IA  (4269:109592 loader "Costos y precios (MX…)")
│     [nota: "carga un momento para obtener todos los detalles del producto"]
│     [nota: "When user tap 'Create Product' it will process the image with ai and animate it"]
│     └── ⚠️ Excepción (4269:109519): [nota: "If there's any error in the image like it blurry…
│         Ai will ask user to retake the photo"]  → volver a cámara
│
├─▶ 4. Formulario prellenado por IA  (4269:109263 / 4269:109343 maximizada)
│     [nota: "la IA llena todos los campos requeridos y el usuario puede revisar…"]
│     Nombre · Descripción (+ "Mejorar con IA") · Subir imagen (uploader + progreso)
│     · Categoría · Variantes (switch) · Inventario y precio · Identificadores
│     [Crear producto] [Tomar otra foto]
│
└─▶ 5. Producto creado  (4269:110979) → listado + toast "Producto creado" (= §PF)
```

## PG.2 Pantalla: Cámara — `4269:109453`
Vista de cámara a pantalla completa (**393px**, no 360). Fondo **`#03071E`** (Background, azul casi negro) con la **foto del producto en vivo** cubriendo la pantalla, más **gradientes** negros arriba (255px) y abajo (187px):
- **Barra superior:** flash (`ion:flash`) izq + cerrar (`basil:cross-solid` 35) der.
- **Encabezado (top 55):** **wordmark "vision ai"** (`Group1321314556`, 114×25) + texto **"Toma una buena foto para que podamos identificar y crear tu producto."** (`B2 R` blanco, w245).
- **Zona de captura** inferior: botón de disparo (`Click`, 77) centrado + **thumbnail lateral** (40, r3) a la derecha.

> ✅ **Primera cámara + primer branding "vision ai" de la App.** El wordmark "vision ai" (con el **sparkle como acento sobre la "i"**) es la marca del feature de IA. Documentar como asset. La cámara es **fullscreen inmersivo** (sin barra de estado visible).

## PG.3 Pantalla: Foto capturada — `4269:109542`
Mismo fondo `#03071E` + foto + wordmark "vision ai". Dos acciones apiladas (botones 328×48, r16):
- **Crear producto** — **botón MORADO `#7C3AED`** (Purple/300) + ícono `add-01`/ai-magic + `B1 M` blanco.
- **Tomar otra foto** — botón blanco borde `#F3F3F3`.

> 🔴 **PRIMER MORADO DE LA APP — `#7C3AED` (Purple/300).** El CTA de IA "Crear producto" usa **morado**, no el rojo de marca. Es un color nuevo, exclusivo del feature de IA. Registrar en COLORS.md y definir su semántica (¿morado = IA en todo el sistema?).
> 🔴 **Inconsistencia de color de CTA dentro del mismo flujo:** en la foto capturada el CTA es **morado**; en el formulario prellenado (§PG.5) es **rojo**. Dos colores distintos para avanzar el mismo flujo.
> [nota diseñador `4269:109858`]: *"When user tap on 'Retake Photo' it will take user back to retake the photo."* — "Tomar otra foto" regresa a la cámara.

## PG.4 Pantalla: Procesamiento IA — `4269:109592`
Estado de carga mientras la IA analiza la imagen:
- **Foto del producto de fondo** + **overlay `rgba(0,0,0,0.4)` con `backdrop-blur 10.8px`**.
- Al centro: **loader circular** (44px) + texto **"Capturando imagen"** (`T2 B` Inter **Bold 20**, blanco).

> [nota `4269:109854`]: *"Cuando el usuario captura la imagen, carga un momento para obtener todos los detalles del producto."*
> **Variante con fases:** existe otro estado del procesamiento con texto rotativo, ej. **"Costos y precios (MX…)"** + efecto **"Sparks"**. El loader **cicla por distintas fases** con transición de texto.

### PG.4.1 🔴 Excepción: imagen borrosa — `4269:109519`
[nota `4269:109872`]: *"If there's any error in the image like it blurry or anything else Ai will ask user to retake the photo."* Si la imagen no sirve, la IA pide **retomar la foto**. Pantalla de error del flujo IA (mensaje + volver a cámara).

> 🔴 **Caso de excepción sin diseño terminado:** la nota describe el comportamiento pero la pantalla de error está en estado mínimo. Diseñar el mensaje de error real de "imagen borrosa / no reconocida".

## PG.5 Pantalla: Formulario prellenado — `4269:109263`
El corazón del flujo. Título **"Crear producto"**. La IA llena los campos y el usuario revisa. Bloques:

| Bloque | Contenido |
|---|---|
| **Nombre del producto** | input |
| **Descripción del producto** | textarea + acción **"Mejorar con IA"** (`Icon_der` + texto) |
| **Subir imagen** | uploader dashed "Sube aquí las imágenes de tu producto" + formato/límite + **"Archivos subidos"** (thumbnail 56 + nombre "Playera 1" + peso "5 MB" + borrar) |
| **Categoría** | select "Camisas" |
| **Variantes del producto** | **switch** + texto guía "Activa esta opción si vendes el mismo producto en diferentes tallas, colores…" |
| **Inventario y precio** | Unidades disponibles "55" · Precio base "$25" · **Precio de venta** "$50" |
| **Identificadores del producto** | SKU "POL78912344" · Código de barras "12345678912344" |

- Footer: **Agregar producto** (primario **rojo `#DB3B2B`**) + **Cancelar** (secundario blanco), botones 328×48 apilados.

> [nota `4269:109862`]: *"Cuando la IA procesa el producto correctamente, llena todos los campos requeridos y el usuario puede revisar que todos los detalles sean correctos."*

### PG.5.0 Elementos del formulario prellenado (verificados en pantalla real)
- 🔴 **Banner de revisión (arriba del formulario):** ⓘ **"Revisa todos los detalles del producto."** sobre fondo crema/amarillo (`bg #FFFBEB`, texto ámbar `#B45309`, ícono `#F59E0B`). Refuerza la nota del diseñador: la IA prellena pero el usuario debe validar. **Primer banner de advertencia informativa del alta.**
- 🔴 **Orbe de IA flotante:** burbuja **`56×56` negra** (`rounded-72`) con un **núcleo (28) de glow morado** `shadow 0 0 35.1px #6D01A5` + imagen. Flota abajo-derecha sobre el footer. Es el **acceso flotante al asistente IA** dentro del formulario. **Sexto morado/color nuevo — `#6D01A5`** (glow), distinto del `#7C3AED` del CTA. Relacionar con Nova (§N).
- **Toggle "Variantes del producto" en ON** (verde `#51AF70`) por defecto en el ejemplo prellenado.
- Valores prellenados reales: Nombre "Playera unisex básica" · Descripción "Playera unisex de algodón con corte clásico…" · Categoría "Camisas" · Unidades "55" · Precio base "$25" · Precio de venta "$50" · SKU "POL78912344".
> 🔴 **"Mejorar con IA"** — segunda entrada de IA dentro del propio formulario, para reescribir la descripción. Documentar como acción reutilizable (aparece también en el alta manual).
> ⚠️ **"Inventario y precio"** como encabezado de bloque (T-size 22/26, no Manrope uppercase) — otro estilo de encabezado distinto a los pasos manuales.

### PG.5.1 Estado de carga de imágenes — `4269:109369`
Cuando se suben varias fotos, el uploader muestra progreso:
- **"Subiendo 4 archivos"** + fila de 4 thumbnails (56) + **barra de progreso** (`bg #F0FDF4`, relleno **`#51AF70`** Green/400) + **"18% completado"** + botón cancelar (`cancel-circle`).

> 🔴 **Texto vs visual de la barra inconsistente:** dice "18% completado" pero la barra está renderizada casi vacía (`inset 0 98.17% 0 0` ≈ 1.8%). Corregir el ancho de relleno o el texto.
> 🔴 **Verde `#51AF70` (Green/400)** en la barra — el mismo quinto verde del toast (§PF.2). Consolidar con la familia de verdes.

### PG.5.2 Versión maximizada — `4269:109343`
[nota `4269:109868`]: *"Versión maximizada"* — variante del formulario con el bloque de imágenes expandido (muestra el estado de carga §PG.5.1 y la lista de "Archivos subidos" con 3 ítems). Por defecto solo hay 1 imagen (la foto tomada); desde aquí se agregan más.
> [nota `4269:109866`]: *"Por defecto solo se agrega 1 imagen, ya que el usuario solo ha tomado 1 foto. Desde aquí puede agregar más imágenes del producto."*

## PG.6 Componentes nuevos
- **Vista de cámara** (flash + disparo + thumbnail) — §PG.2. **Primera cámara de la App.**
- **Estado de procesamiento IA** (loader + fase rotativa + sparks) — §PG.4.
- **Uploader con estado de carga** (barra de progreso + thumbnails + cancelar) — §PG.5.1.
- **Fila de archivo subido** (thumbnail 56 + nombre + peso + borrar) — §PG.5.
- **Acción "Mejorar con IA"** (inline en textarea) — §PG.5.

## PG.7 Pendientes (🔴)

0. 🔴 **PRIMER MORADO `#7C3AED` (Purple/300)** en el CTA "Crear producto" de IA — color nuevo de la App, exclusivo del feature IA. Registrar en COLORS.md (§PG.3).
0b. 🔴 **CTA de color inconsistente en el mismo flujo:** morado (foto) vs rojo (formulario §PG.5). Unificar color.
1. 🔴 **Caso de excepción (imagen borrosa) sin diseño terminado** (§PG.4.1).
2. 🔴 **Barra de progreso: texto "18%" no coincide con el relleno visual (~1.8%)** (§PG.5.1).
3. 🔴 **Verde `#51AF70`** en la barra de carga — quinto verde, consolidar (§PG.5.1).
4. 🔴 **Cámara usa 393px** (ancho de dispositivo distinto al 360 del resto). Confirmar breakpoint (§PG.2).
5. 🔴 **Banner "Revisa todos los detalles del producto"** (ámbar) — primer banner de advertencia del alta, documentar como componente (§PG.5.0).
5b. 🔴 **Orbe de IA flotante** (morado/azul) en el formulario — acceso al asistente IA, relacionar con Nova §N y el morado `#7C3AED` (§PG.5.0).
6. ⚠️ **Encabezado "Inventario y precio"** en estilo distinto (T22) a los pasos manuales (§PG.5).
10. Íconos a `icons.ts`: `upload-square-02`, `cancel-circle`, `ion:flash`, `basil:cross-solid`, `Sparks`.

## PG.9 Referencias
- *Add Product With AI* (`4269:108999`).
- **Cámara:** `4269:109453` · foto `4269:109542` · procesamiento `4269:109592` · excepción `4269:109519`.
- **Formulario:** `4269:109263` · maximizada `4269:109343` · uploader carga `4269:109369`.
- **Producto creado:** `4269:110979` (= §PF).
- **Notas del diseñador:** `4269:109848`–`4269:109873`.

---

# Productos — Sub-tab: Inventario (§PH)

> **Sección "Inventory"** (`369:29099`). Es el sub-tab **"Inventario"** del listado de Productos (§P.2) — la segunda pestaña, junto a "Listado de productos", "Precio", "Catálogo" y "Sucursales".
> Muestra el inventario de cada producto desglosado en **Disponible para venta / Reservado / No vendible / Inventario total**, con acciones de **modificar inventario** (masivo) y desglose de **inventario no vendible**.
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `369:29099`.

## PH.1 Mapa del sub-tab

```
Productos › tab "Inventario"
│
├── Estado VACÍO (733:32252)
│     ilustración + "Aún no tienes inventario" + cuerpo + CTA
├── Estado CON DATOS (733:32435)
│     tarjetas de inventario por producto (Disponible/Reservado/No vendible/Total)
├── Con FILTROS aplicados (733:35244)
│     chips: Inventario 2 · Canal de ventas 1 · Categoría 1 · Otros filtros 1
├── Menú Exportar/Importar (733:33571) — desde el botón de acciones
├── Modo SELECCIÓN (733:33824)
│     barra superior (checkbox + "Title" + botón) + menú "Modificar inventario disponible"
│
├─▶ Sheet "Modificar inventario de {X} productos" (429:33900 / 429:33901)
│     toggle: Agregar inventario | Establecer cantidad  → dos textos distintos
│     input cantidad + Cancelar / Guardar
│
└─▶ Popover "Inventario no vendible" (429:33208)
      Dañado · Defectuoso · Stock de seguridad · Otro (inputs) + "Guardar" · "Pausar"
```

## PH.2 Chrome
Header "Productos" + buscador "Busca por código, nombre, SKU…" + 2 botones + tabs (Listado de productos · **Inventario** activo · Precio · Catálogo · Sucursales) + barra inferior.

> 🔴 **Los tabs siguen rotos** (los mismos de §P.2): "Catálogo" en `x:340` y "Sucursales" en `x:391` — solapados y fuera de 360. Sin cambio.

## PH.3 Estado vacío — `733:32252`
- Ilustración ("Memory storage" 220×220).
- Título **"Aún no tienes inventario"** (`T` grande).
- Cuerpo: *"No tienes productos en tu inventario en este momento. Una vez que agregues un producto, aparecerá aquí."*
- **CTA** (botón 162×40).

## PH.4 Tarjeta de inventario — `4181:99643`
Card blanca (borde `#F3F3F3`, r12, p16). Estructura verificada:
- **Encabezado:** checkbox (`Control`, OFF por defecto) + thumbnail 40 (r8) + **nombre** (`B2 M`, 2 líneas máx, ellipsis) + **chip de variante** (`bg rgba(33,128,255,0.1)`, texto `#2180FF`, ej. **"Rosa / Niño"**).
- Divisor.
- **Fila "Disponible para venta"** (`B3 R #4C4C4C`) + valor en **caja con borde** (`#F3F3F3`, r9, 82×35, ej. "28") — editable.
- **Fila "Reservado"** + valor en **texto plano** (`B2 M`, "28") — no editable.
- **Fila "No vendible"** + valor en **caja con borde** (82×35, "28") — editable/tappable → abre popover §PH.7.
- Divisor.
- **Fila "Inventario total:"** (`B2 M` negro) + valor ("28").

> 🔴 **Dos tratamientos visuales para valores en la misma tarjeta:** "Disponible" y "No vendible" van en **caja con borde** (parecen editables); "Reservado" e "Inventario total" van en **texto plano** (solo lectura). El patrón de "qué es editable" no es obvio — definir affordance.
> 🔴 **Chip de variante "Rosa / Niño"** usa el **overlay azul** (`rgba(33,128,255,0.1)` / `#2180FF`) — mismo azul de las especificaciones (§PA.8). Consistente con el chip de variante del alta.

## PH.5 Filtros aplicados — `733:35244`
Fila de chips de filtro activos (cada uno con contador + `x` para quitar):
- **Inventario** (2) · **Canal de ventas** (1) · **Categoría** (1) · **Otros filtros** (1).

> Los chips de filtro tienen un **badge de conteo** (`Frame 2147239697` con número) — patrón reutilizable de "filtro con N valores activos". Documentar.
> 🔴 **La sheet de filtros sigue sin diseñarse** (como en Pedidos §13.11, Carrito §CA.3.9, Productos §P.7). Aquí ya se ven los chips resultantes, pero no la superficie que los genera.

## PH.6 Sheet "Modificar inventario de {X} productos" — `429:33900` / `429:33901`
Bottom sheet (blanco, r16). Acción masiva sobre los productos seleccionados:
- **Título** "Modificar inventario de {X} productos" (`B1 S`, con placeholder `{X}`).
- **Toggle segmentado** (píldora `#F8F8F8` r50): **"Agregar inventario"** | **"Establecer cantidad"** — texto **Manrope Medium 12** 🔴.
- **Input** "Ingresa la cantidad a establecer" (label `B2 S`) + placeholder "ej. 1".
- **Texto de ayuda dinámico** (`#6B7280` 🔴 quinto gris) que cambia según el modo:
  - Agregar: *"Se agregarán {N} artículos al inventario de tus productos seleccionados."*
  - Establecer: *"{N} se establecerá como el inventario de tus productos seleccionados."*
- **Botones:** Cancelar (secundario 144) + **Guardar** (primario 144, **`#E9897E`** Primary/400).

> 🔴 **Botón "Guardar" en `#E9897E` (Primary/400 — rosa/coral claro):** es el **estado deshabilitado** del botón primario (sin cantidad ingresada aún). Documentar el estado disabled del botón como átomo — es la primera vez que se ve explícito.
> 🔴 **Toggle en Manrope** dentro de una superficie Inter — suma a la anomalía Manrope.

## PH.7 Popover "Inventario no vendible" — `429:33208`
Popover blanco (r16) que **desglosa el "No vendible"** en categorías:
- Título **"Inventario no vendible"** (`B2 S`).
- 4 filas label + input pequeño (61×40, r12, valor "0"):
  - **Dañado** · **Defectuoso** · **Stock de seguridad** · **Otro**.
- **"Guardar"** (`#DB3B2B` rojo, `B2 S`, alineado a la derecha) sobre un divisor.
- En el frame contenedor aparece también **"Pausar"** como acción secundaria.

> 🔴 **Inputs del popover con medidas fraccionarias** (`0.916px` borde, `13.43px` texto, `16.489` padding) — el mismo componente escalado recurrente (§D.4.7, §PA.4).

## PH.8 Menús contextuales
- **Menú Exportar / Importar:** **Exportar** (`file-export`) + **Importar** (`file-import`) — desde el botón de acciones del header.
- **Menú "Modificar inventario disponible":** opción con `edit-01` → abre el sheet §PH.6.

## PH.9 Modo selección — `733:33824`
Barra superior de selección (checkbox + texto **"N seleccionados"** + botón 118) sobre las tarjetas. Igual patrón que la barra de selección del listado (§P.3), aquí para acciones masivas de inventario.

## PH.10 Componentes nuevos
- **Tarjeta de inventario** (desglose Disponible/Reservado/No vendible/Total) — §PH.4.
- **Sheet de modificación masiva** con toggle Agregar/Establecer — §PH.6.
- **Popover de inventario no vendible** (Dañado/Defectuoso/Stock seg./Otro) — §PH.7.
- **Chip de filtro con badge de conteo** — §PH.5.
- **Estado disabled del botón primario** (`#E9897E`) — §PH.6.

## PH.11 Pendientes (🔴)

1. 🔴 **Dos tratamientos de valor en la tarjeta** (caja con borde vs texto plano) sin affordance clara de editabilidad (§PH.4).
2. 🔴 **Botón Guardar en `#E9897E`** (disabled) — formalizar el estado deshabilitado del botón primario (§PH.6).
3. 🔴 **Toggle "Agregar/Establecer" en Manrope** (§PH.6).
4. 🔴 **Medidas fraccionarias** en los inputs del popover (§PH.7).
5. 🔴 **Sheet de filtros sin diseñar** (recurrente) (§PH.5).
6. 🔴 **Tabs rotos** (heredado de §P.2) (§PH.2).
8. ⚠️ **Quinto gris `#6B7280`** en el texto de ayuda del sheet (§PH.6).
9. Íconos a `icons.ts`: `file-export`, `file-import`, `edit-01`.

## PH.13 Referencias
- *Inventory* (`369:29099`).
- **Estados:** vacío `733:32252` · con datos `733:32435` · filtros `733:35244` · selección `733:33824`.
- **Tarjeta:** `4181:99643`.
- **Sheets:** Modificar (Agregar) `429:33900` · Modificar (Establecer) `429:33901` · No vendible `429:33208`.
- **Menús:** Exportar/Importar `733:33571` · Modificar disponible `733:34097`.
- Reutiliza: tabs §P.2 · barra de selección §P.3 · chip azul §PA.8.

---

# Flujo 20 — Inventario (§PH)

> **Sección "Inventory"** (`369:29099`). Es el **tab "Inventario"** del listado de Productos (§P.2) — la segunda pestaña. Gestiona el stock de cada producto con un desglose por estado (disponible / reservado / no vendible).
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `369:29099`.

## PH.1 Mapa del tab

```
Productos › tab "Inventario"
│
├── Vacío (733:32252)
│   ilustración + "Aún no tienes inventario" + botón
│
├── Listado (733:32435)
│   tarjetas de inventario (Disponible/Reservado/No vendible/Total)
│
├── Con filtros aplicados (733:35244)
│   chips: Inventario 2 · Canal de ventas 1 · Categoría 1 · Otros filtros 1
│
├── Con selección múltiple (733:33824)
│   barra superior (checkbox "Title" + botón) + menú "Modificar inventario disponible"
│
├── Menús
│   ├── Exportar / Importar (733:33759)
│   └── Modificar inventario disponible (733:34097)
│
└── Sheets / popovers
    ├── "Modificar inventario de {X} productos" (429:33292 / 429:33936)
    │     tabs: Agregar inventario · Establecer cantidad
    └── "Inventario no vendible" (429:33208)
          Dañado · Defectuoso · Stock de seguridad · Otro · Pausar
```

## PH.2 Estado vacío — `733:32252`
- Ilustración (`Memory storage-cuate`, 220×220).
- **"Aún no tienes inventario"** (`T-size` 20) + cuerpo *"No tienes productos en tu inventario en este momento. Una vez que agregues un producto, aparecerá aquí."* (`B2 R`, w280).
- Botón (162×40).

## PH.3 Tarjeta de inventario — `4181:99643` ⭐ componente central
Card blanca r12 borde `#F3F3F3` p16. Estructura:
- **Header:** checkbox (`Control`, ON = `#DB3B2B` r4) + thumbnail 40 (r8) + nombre (`B2 M`, 2 líneas, ellipsis) + **chip** "Rosa / Niño" (`B3 M #2180FF` sobre overlay azul `rgba(33,128,255,0.1)` r6).
- Divisor.
- **Desglose de stock** (4 filas, label `B3 R #4C4C4C` izq + valor der):
  | Fila | Valor | Formato del valor (componente base) |
  |---|---|---|
  | **Disponible para venta** | 28 | **caja con borde** (w82 h35 r9, `B2 M`) |
  | **Reservado** | 28 | **texto plano** (`B2 M`, w83) |
  | **No vendible** | 28 | **caja con borde** (w82 h35 r9) |
  | *(divisor)* | | |
  | **Inventario total:** | 28 | texto plano (`B2 M` negro) |

> **Formato mixto (confirmado en design context):** "Disponible para venta" y "No vendible" muestran su valor en una **caja con borde** (w82 r9), mientras "Reservado" e "Inventario total" son **texto plano**. La caja sugiere editabilidad; el texto plano, valores derivados.
> 🔴 **Estado stepper observado en pantalla, nodo por localizar:** en un screenshot del modal de modificación, las filas "Disponible para venta" y "No vendible" aparecen como **stepper** (`−` gris + caja + `+` rojo `#DB3B2B`). **No aparece en los design contexts base**, donde son cajas simples. Confirmar si el stepper es un **estado interactivo** (edición inline al entrar al modal) o una variante distinta de la tarjeta, y mapear su nodo antes de darlo por canónico.
> **Semántica:** Disponible para venta + Reservado + No vendible = Inventario total. Disponible y No vendible son los capturables; Reservado y Total se derivan.

## PH.4 Filtros aplicados — `733:35244`
Fila de **chips de filtro activos** (r con contador + `x`):
- **Inventario 2** · **Canal de ventas 1** · **Categoría 1** · **Otros filtros 1**.
- Cada chip: label + badge numérico (cantidad de valores seleccionados) + `x` para quitar.

> Confirma el patrón de **filtros con contador** (cuántos valores hay activos por categoría). Reutilizable en el resto de listados (Pedidos §13, Productos §P).

## PH.5 Selección múltiple — `733:33824` / `4181:100084`
Al entrar en modo selección aparece una **barra superior**: checkbox en estado **Multiselection** (`Control`, ícono de guión/indeterminado) + texto **"2 seleccionados"** (`B2 M`) + botón desplegable **"Acciones ▾"** (118×35, blanco borde `#F3F3F3`, `chevron-down`).

> ✅ **Confirmado (design context):** el texto real es **"2 seleccionados"** y el botón dice **"Acciones"** en español (no "Actions"). El checkbox usa un tercer estado **"Multiselection"** (indeterminado), además de On/Off.
> ⚠️ **Variante visual observada en screenshot:** existe un estado de la barra con **botón cuadrado + `x` rojo (`#FDECEA`)** en vez del botón desplegable "Acciones ▾" — mapear su nodo y confirmar si es un estado distinto del componente.

## PH.6 Menús

### PH.6.1 Menú Exportar / Importar — `733:33759`
- **Exportar** (`file-export` + label) · **Importar** (`file-import` + label). (+ 7 filas "Opción" ocultas, plantilla de menú.)

### PH.6.2 Menú "Modificar inventario disponible" — `733:34097`
- **Modificar inventario disponible** (`edit-01` + label). Abre el sheet §PH.7.

## PH.7 Modal "Modificar inventario de {X} productos" — `429:33292`
**Modal centrado** (no bottom sheet): overlay **`rgba(0,0,0,0.4)`** sobre el listado, y card blanca **328×324 r16** centrada (`translate -50%,-50%`, `top: calc(50% - 12px)`). Modifica el stock de **varios productos** seleccionados a la vez:
- **Título** *"Modificar inventario de {X} productos"* (`B1 S`, con placeholder `{X}`).
- **Segmented control (pill)** con dos modos:
  - **Agregar inventario** (suma al stock actual).
  - **Establecer cantidad** (fija el stock a un valor).
- **Campo** "Ingresa la cantidad a establecer" (input h55, "ej. 1").
- **Texto dinámico según el modo:**
  - Agregar: *"Se agregarán {N} artículos al inventario de tus productos seleccionados."* (`#6B7280`)
  - Establecer: *"{N} se establecerá como el inventario de tus productos seleccionados."*
- Botones **Cancelar** (secundario) + **Guardar** (primario).

> 🔴 **Los tabs del segmented control van en Manrope** (`Manrope Medium 12`) — anomalía Manrope dentro de un sheet de la App.
> 🔴 **Botón "Guardar" en `#E9897E` (Primary/400):** un rojo/coral **más claro** que el `#DB3B2B` de marca. Parece el **estado disabled** del botón primario (sin cantidad ingresada aún). Documentar el estado disabled del botón como token.
> 🔴 **Quinto gris `#6B7280`** en el texto de ayuda — el mismo de §PA.8.4.

## PH.8 Modal "Inventario no vendible" — `429:33208`
**Modal centrado** (mismo patrón que §PH.7: overlay `rgba(0,0,0,0.4)` + card centrada), blanco r16, 243 ancho. Desglosa el **"No vendible"** de un producto en sus causas:
- **Título "Inventario no vendible"** (`B2 S`).
- 4 filas (label izq + input w61 h40 r12): **Dañado** · **Defectuoso** · **Stock de seguridad** · **Otro**.
- **"Guardar"** (`B2 S` **`#DB3B2B`**, alineado derecha) sobre un divisor superior.

> 🔴 **Inputs con medidas fraccionarias** (`0.916px` borde, `13.43px` texto, `16.489` padding) — la deuda recurrente del componente escalado (§D.4.7, §PA).

## PH.9 Chrome del tab
Header "Productos" + buscador "Busca por código, nombre, SKU…" + 2 botones + tabs (Listado de productos · **Inventario** activo · Precio · Catálogo · Sucursales) + barra inferior.

> 🔴 **Los mismos tabs rotos** de §P.2 (Catálogo `340`/Sucursales `391`, solapados). En este tab el orden y anchos varían ligeramente respecto al listado — otro estado del mismo componente defectuoso.

## PH.10 Componentes nuevos
- **Tarjeta de inventario** (desglose Disponible/Reservado/No vendible/Total) — §PH.3.
- **Checkbox de 3 estados** (On/Off/**Multiselection**) en la barra de selección — §PH.5.
- **Modal centrado** (overlay `rgba(0,0,0,0.4)` + card) para modificar inventario y desglose no vendible — §PH.7/§PH.8.
- **Barra de acciones "Actions"** (desplegable + cuadro + x rojo) — §PH.5.
- **Chips de filtro con contador** — §PH.4.
- **Segmented control (pill) Agregar/Establecer** — §PH.7.
- **Sheet de modificación masiva de inventario** — §PH.7.
- **Popover de desglose "No vendible"** (Dañado/Defectuoso/Stock seg./Otro) — §PH.8.
- **Menú Exportar/Importar** — §PH.6.1.

## PH.11 Pendientes (🔴)

1. 🔴 **Estado stepper del desglose sin nodo localizado:** aparece en screenshot (`−`/`+`) pero no en los design contexts base (cajas simples). Mapear su nodo y confirmar si es edición inline o variante (§PH.3).
1b. ⚠️ **Variante visual de la barra de selección** (botón cuadrado + `x` rojo `#FDECEA`) observada en screenshot — mapear su nodo y confirmar si es un estado distinto del botón "Acciones ▾" (§PH.5).
2. 🔴 **"Title" sin resolver** en la barra de selección (§PH.5).
3. 🔴 **Tabs del segmented control en Manrope** (§PH.7).
4. 🔴 **Botón "Guardar" en `#E9897E`** (Primary/400) — documentar como estado disabled del primario (§PH.7).
6. 🔴 **Medidas fraccionarias** en los inputs del popover (§PH.8).
7. 🔴 **Quinto gris `#6B7280`** en texto de ayuda (§PH.7).
8. 🔴 **Tabs rotos** heredados de §P.2 (§PH.9).
9. Íconos a `icons.ts`: `file-export`, `file-import`, `edit-01`.

## PH.13 Referencias
- *Inventory* (`369:29099`).
- **Vacío:** `733:32252`. **Listado:** `733:32435`. **Filtros:** `733:35244`. **Selección:** `733:33824`.
- **Tarjeta:** `4181:99643`. **Menús:** Export/Import `733:33759` · Modificar `733:34097`.
- **Sheets:** Modificar inventario `429:33292` (Agregar) / `429:33936` (Establecer) · No vendible `429:33208`.
- Reutiliza: listado y tabs §P · barra inferior · chips de filtro.

---

# Flujo 21 — Precios (§PI)

> **Sección "Price"** (`375:16216`). Es el **tab "Precio"** del listado de Productos (§P.2) — la tercera pestaña. Gestiona los precios de cada producto: modificación **masiva por porcentaje/monto** (aumentar/reducir) y un **editor de precios por canal de venta** con soporte de variantes. Es un flujo amplio (múltiples modales + editor multicanal).
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `375:16216`.

## PI.1 Mapa del flujo

```
Productos › tab "Precio"
│
├── Vacío (733:36284)
│   ilustración "Online wishes list" + "Aún no tienes productos" + botón
│
├── Listado (733:36652)
│   tarjetas de producto (checkbox + thumbnail + nombre + "2 variantes" + botón)
│
├── Con filtros aplicados (733:38695)
│   chips: Canal de ventas 1 · Categoría 1 · Otros filtros 1
│
├── Con selección múltiple (733:37132)
│   barra "Title" + botón + menú (Modificar precio / Eliminar seleccionados)
│
├── Modal "Modificar precio para X productos" (455:40274 …)
│   ├── Aumentar precio / Reducir precio (segmented control)
│   ├── campo porcentaje (%) + campo "Aplicar a" (canales)
│   ├── menú Porcentaje / Monto (455:40769)
│   └── sub-popover "Monto" (Rango / Cifra) (414:27093)
│
├── Toast "Precios modificados" (733:37964)
│
└── Editor de precios por canal (376:28142 / 376:28842)
    ├── por canal: T1tienda · Claro Shop · Shein · Mercado Libre · Amazon
    │     cada uno: logo + Precio base + Precio de oferta + "Ver variantes"
    └── acordeón de variantes (376:29043): tarjeta por variante con su precio
```

## PI.2 Estado vacío — `733:36284`
- Ilustración **"Online wishes list-pana"** (220×220).
- **"Aún no tienes productos"** (`T-size` 26) + cuerpo.
- Botón (162×40).

## PI.3 Listado de precios — `733:36652`
Tarjetas de producto (h126). Cada una:
- **Checkbox** (`Control`) + **thumbnail** 40 (r8) + **nombre** (`B2 M`, w224).
- Divisor + fila inferior: **"2 variantes"** (`B2 M`) izq + botón **"Ver precios ›"** (88×32, con chevron derecho) der.
- La última tarjeta del ejemplo va **sin checkbox** (variante del componente).

> ✅ **Botón "Ver precios ›"** (validado en Figma) — `B3 M` gris `#4C4C4C` + ícono `arrow-right-01-sharp`, fondo transparente. Abre el editor de precios por canal (§PI.8). En el screenshot aparece en rojo en la fila inferior: es el **estado activo/pressed** de la fila, no el color base.

## PI.4 Filtros aplicados — `733:38695`
Fila de **chips de filtro** con contador + `x`: **Canal de ventas 1** · **Categoría 1** · **Otros filtros 1**. (Aquí NO aparece el chip "Inventario" que sí está en §PH — el set de filtros varía por tab.) Buscador con `filter-horizontal`.

## PI.5 Selección múltiple + menú — `733:37132`
- Barra superior: checkbox + **"Title"** 🔴 (placeholder) + botón (118×35).
- **Menú de acciones:** **Modificar precio** (`edit-01`, texto negro `#000`) + **Eliminar seleccionados** (`delete-02`, **texto en rojo `#DB3B2B`** — validado en Figma, acción destructiva).
- La barra real (verificada en pantalla) muestra checkbox **Multiselection** (rojo, guión) + **"2 seleccionados"** + botón **"Acciones ▾"** (español), igual que §PH.5.

> ✅ **"Eliminar seleccionados" en rojo** confirma el patrón: en la App, rojo = acción destructiva en menús (consistente con el modal "Eliminar variante" §PC).
> 🔴 **"Title" sin resolver** en el nodo base, aunque la pantalla real renderiza "2 seleccionados".

## PI.5b Drawer de filtros "Filtrar" — (nodo por localizar)
Bottom sheet/drawer que abre el botón de filtro (`filter-horizontal`). Verificado en pantalla; es un **componente de filtros compartido** entre tabs. Estructura:
- **Header:** **"Filtrar"** (centrado) + **"Restablecer"** (derecha).
- **"Odenar por"** 🔴 (typo: falta la "r" → debe ser **"Ordenar por"**) — select **"Nombre (A-Z)"** + chevron.
- **Sección "Canales de venta (1)"** (colapsable, chevron arriba) — lista de checkbox + logo + nombre, **11 canales**: **Tienda en línea** (checked) · Punto de venta · Amazon · Shein · Walmart · Sanborns · Sears · Aliexpress · Shopify · Mercado Libre · Woocommerce.
- **Sección "Categoría (1)"** (colapsable) — **Camisas** (checked) · Pantalones · Accesorios · Relojes.
- **Sección "Precio"** (colapsable) — segmented control **Rango / Cifra** + inputs **"$ desde" — "$ hasta"** (en modo Rango).
- **Botón "Mostrar resultados"** (rojo `#DB3B2B`, ancho completo, sticky abajo).

> 🔴 **Typo "Odenar por" → "Ordenar por"** en el encabezado del sort.
> ✅ **El patrón Rango/Cifra se reutiliza:** aparece en el filtro de Precio (aquí) y en el sub-popover "Monto" del modal (§PI.6.2). Mismo componente segmented + inputs.
> **Nodo por localizar:** este drawer no está en el metadata de la sección Price; es un componente compartido. Mapear su node id para documentarlo formalmente (posible sección global de Filtros).

## PI.6 Modal "Modificar precio para X productos" — `455:40274` ⭐
**Modal centrado** (overlay `rgba(0,0,0,0.4)` + card 328×421 r16 centrada, confirmado en Figma). Modifica el precio de **varios productos** por porcentaje o monto:
- **Título** *"Modificar precio para X productos"* (`B1 S`; nota: usa `X` literal, no `{X}`).
- **Segmented control (pill):** **Aumentar precio** / **Reducir precio** (Manrope 🔴).
- **Campo porcentaje:** label dinámico *"Ingresa el porcentaje a aumentar"* / *"...a reducir"* + input con **"%"** + selector (chevron) + valor (ej. "30").
- **Campo "Aplicar a":** select con **"Todos los canales"** o **"4 canales"** + chevron.
- **Texto de ayuda:** *"Al guardar, verás el precio actualizado en el editor masivo"* (`#6B7280`).
- **Botones:** **Cancelar** (secundario) + **Aplicar** (rojo **`#DB3B2B`** pleno).

### PI.6.1 Menú Porcentaje / Monto — `455:40769`
Menú desplegable dentro del modal: **Porcentaje** (`percent`) / **Monto** (`dollar-01`). Cambia el modo de cálculo del ajuste de precio.

### PI.6.2 Sub-popover "Monto" — `414:27093`
Al elegir "Monto" aparece un popover: título **"Monto"** + **"Limpiar"** (`line-md:chevron-up`) + segmented control **Rango / Cifra** + input con **"$"**. Permite ajustar por un monto fijo (cifra) o un rango.

### PI.6.3 Selector "Aplicar a" (canales) — `455:40496`
Al tocar el campo "Aplicar a" se despliega un **dropdown de canales** (card blanca r16, sombra) con **checkbox cuadrado + logo + nombre** por fila. Los **11 canales** (mismo catálogo que el filtro §PI.5b): **Tienda en línea** (checked, `store-04`) · **Punto de venta** (`sale-tag-02`) · **Amazon** · **Shein** · **Walmart** · **Sanborns** · **Sears** · **Aliexpress** · **Shopify** · **Mercado Libre** · **Woocommerce**.

> ✅ **"Aplicar a" es multi-selección de canales**, no un simple "Todos/N". Por eso el campo muestra "Todos los canales" o "4 canales" (el conteo de los marcados). El checkbox marcado usa rojo `#DB3B2B`.

> ✅ **Modelo de modificación de precio de dos ejes:** dirección (Aumentar/Reducir) × tipo (Porcentaje/Monto), y el Monto a su vez por Rango/Cifra. Documentar la matriz completa.
> 🔴 **Segmented control en Manrope** — anomalía Manrope, igual que en §PH.7.

## PI.7 Toast "Precios modificados" — `733:37964`
Tras aplicar, píldora **"Precios modificados"** (141×31) sobre el listado. Mismo patrón de toast que §PF ("Producto creado").

## PI.8 Editor de precios por canal — `376:28142` (corto) / `376:28842` (con variantes) ⭐⭐
Pantalla dedicada (no modal). Header: flecha atrás (`majesticons:arrow-up`) + **"Precios"** + divisor. Debajo, la tarjeta del producto (thumbnail 48 + nombre). Luego, **un bloque por canal de venta**, cada uno con:
- **Logo + nombre del canal:** **T1tienda** (`t1-logotipo-2`) · **Claro Shop** (`logo CS`) · **Shein** (`logo shein`) · **Mercado Libre** (`logo ML`) · **Amazon** (`logo amazon`).
- **Precio base** (input 160, "$3,456.99") + **Precio de oferta** (input 160, "$1,456.99").
- Botón **"Ver variantes"** (con chevron) que despliega el acordeón (§PI.8.1).
- Separados por divisores.
- **Footer:** 2 botones (160 c/u) — Cancelar + Guardar.

### PI.8.1 Acordeón de variantes por canal — `376:29043`
Al tocar **"Ver variantes"** (chevron gira ↑), el bloque del canal se expande (h519) y muestra **una tarjeta por variante** (`#F8F8F8` r12 p12):
- **Chip de variante** (overlay azul `rgba(33,128,255,0.1)`, `#2180FF`): **"Rosa / Niño"** · **"Azul / Niño"** · **"Negro / Niño"**.
- **Precio base** + **Precio de oferta** por variante (inputs 136 c/u).

> ✅ **Editor de precios multicanal — componente más rico del flujo.** Permite precio base + precio de oferta **por canal de venta** (5 marketplaces) y **por variante dentro de cada canal**. Es la contraparte de precios del alta multicanal (§PE).
> **Dos longitudes de la pantalla:** h1374 (todos los canales colapsados) y h1601 (T1tienda con variantes expandidas). Documentar como estados colapsado/expandido del mismo editor.

## PI.9 Chrome del tab
Header "Productos" + buscador (aquí **sin** el segundo botón de filtro en algunas pantallas, solo 288px de search + 1 botón) + tabs (Listado · Inventario · **Precio** activo · Catálogo · Sucursales) + barra inferior.

> 🔴 **Tabs rotos (peor que en otros tabs):** el contenedor de tabs arranca en **`x:-74`** con **431px de ancho** — desbordado fuera del viewport de 360. Catálogo/Sucursales quedan cortados. Es el mismo componente defectuoso de §P.2/§PH.9 pero aquí con offset negativo explícito.

## PI.10 Componentes nuevos
- **Modal "Modificar precio"** (Aumentar/Reducir × Porcentaje/Monto) — §PI.6.
- **Sub-popover "Monto"** (Rango/Cifra) — §PI.6.2.
- **Editor de precios por canal** (Precio base + oferta por marketplace) — §PI.8.
- **Acordeón de variantes por canal** (precio por variante) — §PI.8.1.
- **Toast "Precios modificados"** — §PI.7.
- **Selector "Aplicar a"** (multi-selección de 11 canales con logos) — §PI.6.3.
- **Drawer de filtros "Filtrar"** (Ordenar por · Canales · Categoría · Precio Rango/Cifra) — §PI.5b.

## PI.11 Pendientes (🔴)

1. 🔴 **"Title" sin resolver** en la barra de selección (§PI.5).
2. 🔴 **Segmented control en Manrope** (Aumentar/Reducir) (§PI.6).
3. 🔴 **Tabs desbordados** (`x:-74`, 431px) — el peor caso del componente de tabs (§PI.9).
4. 🔴 **Medidas fraccionarias** omnipresentes en inputs (`24.328`, `7.328`, `0.916`…) (§PI.6/§PI.8).
5. ✅ **Botón por tarjeta = "Ver precios ›"** (verificado en pantalla) (§PI.3).
6. 🔴 **Typo "Odenar por" → "Ordenar por"** en el drawer de filtros (§PI.5b).
7. 🔴 **Drawer de filtros sin node id localizado** — componente compartido, mapear (§PI.5b).
8. Íconos/logos a `icons.ts`: `percent`, `dollar-01`, `edit-01`, `delete-02`, `majesticons:arrow-up`, `filter-horizontal`, `store-04`, `sale-tag-02`, y logos de canal (Amazon, Shein, Walmart, Sanborns, Sears, Aliexpress, Shopify, Mercado Libre, Woocommerce, Claro Shop, t1-logotipo-2).

## PI.13 Referencias
- *Price* (`375:16216`).
- **Vacío:** `733:36284`. **Listado:** `733:36652`. **Filtros:** `733:38695`. **Selección:** `733:37132` (+ menú `733:37426`).
- **Modal Modificar precio:** `455:40274` (Aumentar) · `455:40970` (Reducir) · `455:40841` (con valor "30"/"4 canales") · menú `455:40769` · sub-popover Monto `414:27093`.
- **Toast:** `733:37964`.
- **Editor por canal:** `376:28142` (colapsado) · `376:28842` (variantes) · acordeón `376:29043`.
- Reutiliza: listado y tabs §P · barra inferior · chips de filtro · patrón de toast §PF.

---

# Flujo 22 — Catálogo (§PJ)

> **Sección "Catalog"** (`404:28696`). Es el **tab "Catálogo"** del listado de Productos (§P.2) — la cuarta pestaña. Es el flujo más amplio de la App hasta ahora (**33 pantallas, 931 frames** en Figma). Permite agrupar productos en **catálogos** que se publican a canales de venta, con **dos modos de armado**: **Manual** (seleccionas productos) y **Avanzado/Automático** (defines reglas y los productos que cumplen se agregan solos).
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `404:28696`.

## PJ.1 Mapa del flujo

```
Productos › tab "Catálogo"
│
├── A. LISTADO
│   ├── Vacío (733:39844) — "Aún no tienes catálogos" + cuerpo
│   ├── Con catálogos (733:40369) — tarjetas expandibles (Ropa de verano, Pantalones…)
│   ├── Con chips de filtro (733:42158) — Inteligente 1 · Canal 3
│   ├── Selección múltiple (733:41283) — "Title" + Eliminar seleccionados
│   ├── Menú crear (733:40567) — "Crear catálogo"
│   ├── Menú por catálogo (733:41834) — Editar / Administrar canales de venta / Eliminar
│   └── Modales destructivos
│       ├── Eliminar catálogo (410:20124)
│       └── Eliminar catálogos seleccionados (733:41809)
│
├── B. NUEVO CATÁLOGO (formulario, 2 modos)
│   ├── Base / vacío (410:20337)
│   ├── Manual — buscar/seleccionar productos (410:36786 / 4183:104283 / 410:37740 / 421:21302)
│   └── Avanzado — reglas (411:19945 / 414:28451 / 4183:107012)
│
├── C. EDITAR CATÁLOGO (414:27114) — mismo form, precargado
│
├── D. ADMINISTRAR CANALES DE VENTA (410:19814) — 11 canales + variantes
│
└── E. MENÚ ORDENAR (421:21302) — 8 opciones de orden
```

## PJ.2 A · Listado

### PJ.2.1 Vacío — `733:39844`
- Ilustración + **"Aún no tienes catálogos"** (título es) + cuerpo.

### PJ.2.2 Con catálogos — `733:40369` ⭐ tarjeta de catálogo
Tarjeta expandible (328 ancho) por catálogo. Estructura:
- **Header:** imagen 32/40 + **nombre** ("Ropa de verano", "Pantalones") + menú **`more-horizontal`**.
- **Fila "Tipo"** (`search-list-02` + "Tipo" + valor **"Manual"** o **"Avanzado"**) + chevron.
- **Fila "Productos"** (`product-loading` + "Productos" + count **"31"**).
- **Fila "Canal de ventas:"** + **"1/8"** (canales activos/total) + chevron.

> ✅ **La tarjeta resume el catálogo:** tipo de armado (Manual/Avanzado), nº de productos y cobertura de canales (X/8).

### PJ.2.3 Chips de filtro — `733:42158`
Chips: **Inteligente 1** · **Canal 3**.

### PJ.2.4 Selección múltiple — `733:41283`
Barra **"Title"** 🔴 (placeholder) + menú con **"Eliminar seleccionados"**.

### PJ.2.5 Menús
- **Crear:** **"Crear catálogo"**.
- **Por catálogo:** **Editar catálogo** · **Administrar canales de venta** · **Eliminar** (rojo, destructivo).

### PJ.2.6 Modales destructivos
- **Eliminar catálogo:** *"Esta acción solo eliminará el catálogo. Los productos seguirán publicados en los marketplaces donde están activos."*
- **Eliminar catálogos seleccionados:** *"Esta acción solo eliminará los catálogos seleccionados. Los productos seguirán publicados…"*

> ✅ **Copy de borrado muy claro:** aclara que eliminar el catálogo NO despublica los productos. Buen patrón de mensaje destructivo, replicar en otros borrados.

## PJ.3 B · Nuevo catálogo (formulario)
Título **"Nuevo catálogo"**. Secciones:

> **Footer del formulario:** botones **"Descartar"** (secundario) + **"Guardar"** (rojo `#DB3B2B`) — no "Cancelar/Crear catálogo".

### PJ.3.1 Información del catálogo — `410:20337`
- **Subir imagen** (uploader "Sube aquí las imágenes de tu producto") → con archivo: "Playera 1 · 5 MB".
- **Nombre del catálogo** (input "Ej. Playera polo manga corta").
- **Descripción** (textarea "Descripción aquí" — 🔴 en **Manrope** `#C3C3C3` 12.8px, anomalía Manrope como en el alta §PB).

> 🔴 **Encabezados de sección en Manrope uppercase `#4B5563`** ("INFORMACIÓN DEL CATÁLOGO", "SELECCIÓN DE PRODUCTOS", "REGLAS", "PRODUCTOS", etc.) — misma anomalía Manrope de los encabezados del alta de producto (§PA/§PE). Cada sección es **colapsable** (chevron `arrow-down-01-sharp`).

### PJ.3.2 Selección de productos — selector de modo (radios)
Dos tarjetas `#F8F8F8` r16, cada una con **radio** (`Control`, no segmented) + título + descripción:
- **Manual:** *"Selecciona o busca productos para agregar al catálogo"*.
- **Avanzado:** *"Los productos que cumplan tus reglas se agregarán automáticamente al catálogo"*.

> 🔴 **Es un grupo de radios, no un segmented control** (corrección de análisis). El radio ON usa el estilo `Radio/state On`.

### PJ.3.3 Modo Manual
- **Vacío:** buscador "Busca por código, nombre, SKU…" + **"Busca tu producto para comenzar tu catálogo"** + **"Aún no tienes productos en este catálogo"**.
- **Resultados de búsqueda:** categoría "Jerseys" + **"Seleccionar todo"** + lista de productos con checkbox (jerseys de selecciones ADIDAS).
- **Sin coincidencias:** **"No hay coincidencias con tu busqueda"** 🔴 (typo: "busqueda" sin tilde).
- **Con productos agregados:** tarjeta de producto (thumbnail + nombre + **"Identificador: 123456777"** + **"$1,900.00"**).

### PJ.3.4 Modo Avanzado (reglas) — `414:28451` / `4183:107012` ⭐⭐ (validado en design context)
Constructor de reglas. Estructura real:
- Sección **"REGLAS"** (encabezado Manrope `#4B5563` uppercase) + texto **"Los productos deben cumplir con:"** (`B2 R #4C4C4C`).
- **Lógica AND/OR:** dos radios — **"Todas las reglas"** (ON, AND) / **"Cualquier regla"** (OR). 🔴 No lo tenía documentado.
- **Tarjeta de regla** (`#F8F8F8` r12), una por regla, con **3 inputs apilados** (55px, r20) + **botón borrar** (`delete-02`, arriba a la derecha):
  - **Regla 1:** input **"Tipo"** (con chevron `arrow-down-01-sharp`) → **"es igual a"** → **"Camiseta"**.
  - **Regla 2:** input **"Color"** (chevron) → **"es igual a"** → **"Azul"** con **swatch de color azul `#2F80ED`** (cuadro 15px) junto al texto.
- Botón **"Agregar regla"** (`add-01`, borde **dashed** `#C3C3C3`).
- Sección **"PRODUCTOS"** (preview de los que cumplen): buscador + sort + **tarjetas de producto** con:
  - thumbnail 40 + nombre + **chip de estado** (**"Activo"** verde `#4FC153`/`#F0FDF4` o **"Inactivo"** gris `#F8F8F8`/`#4C4C4C`) + **botón borrar** (`delete-02`).
  - "Identificador: 123456777" + "$1,900.00".
  - Botón **"Ver más productos"** al final.

> ✅ **Constructor de reglas completo (validado en design context):** lógica AND/OR ("Todas las reglas"/"Cualquier regla") + N reglas de **campo → operador → valor** (cada una borrable) + botón "Agregar regla" + preview en vivo de productos que cumplen (con chip Activo/Inactivo). Es el componente más complejo de toda la App.
> 🔴 **Chip "Activo/Inactivo"** en el preview: cuarto/quinto uso del verde `#4FC153` (Green/300) — consistente con el chip de estado de otros listados.
> 🔴 **El valor de color muestra un swatch `#2F80ED`** — un azul NUEVO (`#2F80ED`), distinto de `#2180FF` (Blue/300) y `#005EDC` (Blue/200). Sexto azul, registrar.

## PJ.4 C · Editar catálogo — `414:27114`
Mismo formulario que Nuevo, con título **"Editar catálogo"** y datos precargados: nombre **"Colección de verano"**, descripción **"Esta es la descripción del catálogo"**, productos ya agregados.

## PJ.5 D · Administrar canales de venta — `410:19814`
Pantalla (título **"Administrar canales de venta"**) con **"Agregar variante"** + la lista de **11 canales**: Tienda en línea · Punto de venta · Amazon · Shein · Walmart · Sanborns · Sears · Aliexpress · Shopify · Mercado Libre · Woocommerce. Más valores de variante (Rosa · Turquesa · Verde).

## PJ.6 E · Menú Ordenar — `421:21302`
Menú con **8 opciones**: Más vendidos · Nombre del producto (A-Z) · Nombre del producto (Z-A) · Precio (Mayor a menor) · Precio (Menor a mayor) · Más recientes · Más antiguos · Manualmente.

> Es el mismo sort del drawer de filtros (§PI.5b "Ordenar por") pero desplegado como menú con las 8 opciones completas. Documentar como componente de ordenamiento reutilizable.

## PJ.7 Componentes nuevos
- **Tarjeta de catálogo** (Tipo · Productos · Canal X/8) — §PJ.2.2.
- **Formulario Nuevo/Editar catálogo** (Info + Selección de productos con 2 modos) — §PJ.3/§PJ.4.
- **Toggle de modo Manual/Avanzado** — §PJ.3.2.
- **Constructor de reglas** (campo → operador → valor) — §PJ.3.4.
- **Menú Ordenar** (8 opciones) — §PJ.6.
- **Modales destructivos con copy "los productos siguen publicados"** — §PJ.2.6.

## PJ.8 Pendientes (🔴)

1. 🔴 **"Title" sin resolver** en selección múltiple (§PJ.2.4).
2. 🔴 **Typo "busqueda"** sin tilde en el estado sin coincidencias (§PJ.3.3).
3. 🔴 **"Categoria 1 > Subcat"** placeholder (§PJ.3.4).
4. 🔴 **Encabezados de sección en Manrope** uppercase `#4B5563` + **textarea Descripción en Manrope** (§PJ.3.1) — anomalía Manrope.
5. 🔴 **Azul NUEVO `#2F80ED`** en el swatch de valor de color (§PJ.3.4) — sexto azul, distinto de `#2180FF` y `#005EDC`. Registrar.
6. 🔴 **Botones del footer "Descartar / Guardar"**, no "Cancelar/Crear" (§PJ.3).
7. Íconos a `icons.ts`: `search-list-02`, `product-loading`, `more-horizontal`, `arrow-down-01-sharp`, `arrow-data-transfer-vertical-round`.

## PJ.10 Referencias
- *Catalog* (`404:28696`).
- **Listado:** vacío `733:39844` · con catálogos `733:40369` · chips `733:42158` · selección `733:41283` · menú crear `733:40567` · menú catálogo `733:41834`.
- **Modales:** eliminar catálogo `410:20124` · eliminar seleccionados `733:41809`.
- **Nuevo catálogo:** base `410:20337` · Manual `410:36786`/`4183:104283`/`410:37740`/`421:21302` · Avanzado `411:19945`/`414:28451`/`4183:107012`.
- **Editar:** `414:27114`. **Admin canales:** `410:19814`. **Menú Ordenar:** `421:21302`.

---

# Flujo 23 — Sucursales (§PK)

> **Sección "Branches"** (`421:21749`). Es el **tab "Sucursales"** del listado de Productos (§P.2) — la quinta y última pestaña. Gestiona las **sucursales/almacenes** físicos del negocio: alta, detalle con métricas, activación/desactivación (con transferencia de inventario), sucursal principal y límite por plan. Junto con Catálogo es el flujo más amplio de la App.
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `421:21749`.

## PK.1 Mapa del flujo

```
Productos › tab "Sucursales"
│
├── A. LISTADO
│   ├── Sucursal principal (card destacada: Almacén + dirección + badge "Principal")
│   ├── Todas las sucursales (buscador "…nombre, dirección…" + cards con chips)
│   ├── Variantes:
│   │   ├── Base (733:42938 / 733:43209)
│   │   ├── Con filtros (4183:109155 / 4183:108641) — Ordenar por 1 · Estado 3 · Plan POS 1
│   │   ├── Búsqueda activa (4183:107930) — "Almacén" + cancel-01
│   │   └── Límite alcanzado (736:26841) — banner "{X} sucursales"
│   └── Menú "Nueva sucursal" (733:43356, add-01)
│
├── B. NUEVA SUCURSAL (form largo, 4278:114384)
│   Nombre · País · Calle · Núm ext · Núm int · CP · Colonia · Estado · Ciudad · Referencia · Teléfono
│   + Encargado de sucursal (Nombre · Correo)
│
├── C. DETALLE DE SUCURSAL
│   ├── Branch New (448:32546) / Branch Main (448:33025 / 4279:118691) / Sucursal 1 (4279:117631)
│   ├── stats: Ventas totales $1,234.00 · SKU's 3 · Valor de inventario $1,200.70
│   ├── Datos de la tienda (chips + dirección + tel + encargado)
│   └── Preparación de pedidos (chip + "Envío a domicilio")
│
├── D. MODALES DE ESTADO
│   ├── Eliminar sucursal (4279:117687)
│   ├── Desactivar sin inventario (4279:117704)
│   ├── Desactivar con inventario → transferir (4279:117719 / 4279:117741)
│   ├── Cambiar sucursal y desactivar (4279:117762)
│   └── Cambiar sucursal principal (736:27325)
│
└── E. ENVÍOS A DOMICILIO / Store Setting (4279:149531)
    lista de sucursales con more-horizontal + Estado + chip
```

## PK.2 A · Listado

### PK.2.1 Estructura
Dos bloques:
- **"Sucursal principal"**: **card contenedora** (borde `#F3F3F3` r12, `B1 M`) con título "Sucursal principal" + subtítulo *"Usamos esta sucursal para descontar inventario de tus ventas en línea."* + **card interna gris** (`#F8F8F8` r12) con **"Almacén"** (`B2 S`) + dirección (`B3 R #4C4C4C`) + columna derecha con **badge "Principal"** y, debajo, la acción **"⟳ Cambiar"** (rojo `#DB3B2B` + ícono refresh) que abre el modal "Cambiar sucursal principal" (§PK.5.5).
- **"Todas las sucursales"**: buscador **"Busca por código, nombre, dirección…"** (nota: incluye *dirección*, distinto de otros tabs) + 2 botones + lista de cards de sucursal.

### PK.2.2 Card de sucursal
Cada card (borde r12): **nombre** ("Almacén", "Sucursal 2") + **badge "Principal"** (ámbar, si aplica) + **dirección** (con ellipsis "…") + divisor + **2 chips**: **"Activo"** (verde `#4FC153`/`#F0FDF4`) + **"POS básico"** (azul `#2180FF`/`#F0F8FF`, plan POS de la sucursal).

### PK.2.3 Variantes del listado
- **Con filtros aplicados**: chips **"Ordenar por ①"** · **"Estado ③"** · **"Plan POS ①"**, cada uno con **badge circular negro** (contador blanco) + `x`. Chip tipo pill con borde. Introduce el filtro **"Plan POS"** (específico de sucursales).

### PK.2.3b Drawer de filtros "Filtrar"
Sheet de filtros (mismo patrón que Precios §PI.5b): **"Filtrar"** + **"Restablecer"** · **"Odenar por"** 🔴 (mismo typo "Odenar") con select "Nombre (A-Z)" · sección **"Estado"** (checkbox **Activo**/**Inactivo**) · sección **"Plan POS"** ("POS Basic"/"POS Pro") · botón **"Mostrar resultados"**.

- **Búsqueda activa**: el buscador muestra "Almacén" + ícono **cancel-01** para limpiar.
- **Límite alcanzado**: **banner amarillo** (`Yellow/500 #FFFCE5` r16) con título **"Límite de sucursales alcanzado"** (**Manrope SemiBold** 16) + cuerpo *"Alcanzaste el límite de {X} sucursales activas en tu plan. Mejora tu plan para agregar más sucursales."* (**Manrope Regular**, opacity 70%) 🔴 (placeholder `{X}`) + botón **"Mejorar plan"** ancho completo **amarillo `Yellow/300 #EDBD55`** texto blanco + `x` cerrar (`icon/action/close`) arriba-derecha.

### PK.2.4 Menú "Nueva sucursal" — `733:43356`
Menú con **"Nueva sucursal"** (`add-01`). Punto de entrada al formulario §PK.3.

## PK.3 B · Nueva sucursal (formulario) — `4278:114384`
Título **"Nueva sucursal"**. Formulario largo (h1585). Campos de dirección:
| Campo | Placeholder |
|---|---|
| **Nombre de sucursal** | Ej. Sucursal Polanco |
| **País** | México (con bandera/ícono izq + chevron) |
| **Calle** | Ej. Sucursal Polanco |
| **Número exterior** | Ej. 39 |
| **Número interior** | Ej. 12 |
| **Código postal** | (vacío) |
| **Colonia** | Buenavista |
| **Estado** | Avenida Francisco I. Madero |
| **Ciudad** | Avenida Francisco I. Madero |
| **Referencia** | Avenida Francisco I. Madero (textarea, h141) |
| **Número de teléfono** | (input) |

Sección colapsable **"Encargado de sucursal"**:
- **Nombre** (Ej. Juan Pérez) · **Correo electrónico** (Ej. juan@tucorreo.com).

Footer: 2 botones (Descartar/Guardar, 160 c/u).

> ✅ **Dirección estructurada mexicana completa:** País, Calle, Núm ext/int, CP, Colonia, Estado, Ciudad, Referencia. Buen modelo de dirección MX.

## PK.4 C · Detalle de sucursal — `448:33025` (Branch Main) / `448:32546` (Branch New) / `4279:117631` (Sucursal 1)
Título = nombre ("Almacén"). Contenido:

### PK.4.1 Métricas (stats, `4278:113932`)
Tres tarjetas: **Ventas totales `$1,234.00`** · **SKU's `3`** · **Valor de inventario `$1,200.70`**.

### PK.4.2 Datos de la tienda (`4278:113954`)
Sección colapsable con: **chips** (Activo `#4FC153` + tipo) + **badge "Principal"** (ámbar **`#EDBD55`/`#FFFCE5`** con ícono **estrella**, `Yellow/300` sobre `Yellow/500`) + dirección + teléfono (`+52 55 6784 7623`) + **Encargado de sucursal** ("James Jones · james@mail.com").

### PK.4.3 Preparación de pedidos (`4278:113974`)
Sección colapsable: **chip** + **"Envío a domicilio"** + *"Habilita esta sucursal para que pueda procesar y envíar pedidos."* 🔴 (typo "envíar" → "enviar").

### PK.4.4 Elementos adicionales del detalle (verificados en pantalla)
- **Botón "Ver inventario"** arriba (`B2 M`, blanco borde) — acceso al inventario de esa sucursal.
- **Selector de periodo "30 días"** (dropdown) que filtra las métricas.
- **Orden real de chips en Datos de la tienda:** **"POS básico"** (azul) + **"Activo"** (verde) + **"Principal"** (ámbar estrella) — los tres juntos.
- **Teléfono con bandera** de México + `+52 55 6784 7623`.
- **Encargado** con label en mayúsculas "ENCARGADO DE SUCURSAL" + "James Jones / james@mail.com".
- **Footer:** **Eliminar** (secundario) + **Guardar** (primario; en el ejemplo aparece **disabled** `#F1B0A9`).

### PK.4.5 Detalle de sucursal INACTIVA — `4279:118691`
Cuando la sucursal está desactivada, el detalle añade:
- **Banner azul** (`#F0F8FF`/`#2180FF`, ícono info): **"Sucursal inactiva"** + *"Desactivaste esta sucursal el {fecha}."* (ej. "el 2 de abril de 2020").
- **Botón "Activar"** ancho completo **rojo `#DB3B2B`**, `B2 S` blanco, reactiva la sucursal.
  > 🔴 **Discrepancia token vs render:** el design context reporta `rounded-[12px]`, pero en pantalla el botón se ve como **pill** (bordes tipo cápsula, radio ~100px). Igual el botón "Ver inventario". Confirmar si el radio real de estos botones es pill o si es un desajuste de token. El demo replica el render (pill).
- El resto igual (periodo, métricas, datos, preparación).

> ✅ **El detalle combina métricas de negocio + datos + preparación de pedidos** en secciones colapsables, con un **selector de periodo** para las métricas y un **botón de inventario**. Estado activo/inactivo cambia el header (banner azul + botón Activar).
> Variantes: **Branch New** (recién creada, sin badge Principal), **Branch Main** (con badge Principal), **Sucursal 1** (con acciones), **inactiva** (banner + Activar).

## PK.5 D · Modales de estado (reglas de negocio)
El flujo tiene **notas del diseñador embebidas** que documentan las reglas. **Patrón de modal:** card centrada 328 r16 + overlay `rgba(0,0,0,0.4)` + **ícono en círculo `#F8F8F8` r61 (64px)** + título **`T2 S` (20)** + cuerpo `B2 R #4C4C4C` + **botones h40**: en modales de confirmación van **lado a lado** (Cancelar blanco + primario rojo, ej. "Sí, desactivar"/"Sí, cambiar"); cuando hay contenido extra (selector) o el CTA es largo van **apilados** (primario arriba). 🔴 **Los botones se renderizan como PILL** (radio cápsula) aunque el token diga `r12` — desajuste transversal a revisar. Cinco modales:

### PK.5.1 Eliminar sucursal — `4279:117687`
Ícono `delete-02` + **"Eliminar sucursal"** + *"Esta acción no se puede deshacer. ¿Estás seguro de que quieres eliminar esta sucursal?"* + Cancelar/Eliminar.

### PK.5.2 Desactivar sin inventario — `4279:117704`
`toggle-off` + **"Desactivar sucursal"** + *"¿Estás seguro de que quieres desactivar esta sucursal? Puedes reactivarla cuando quieras."*
> [nota diseñador]: *"Si la sucursal no tiene inventario, puede desactivarse de esta forma."*

### PK.5.3 Desactivar CON inventario → transferir (paso 2) — `4279:117719` / `4279:117741`
**Flujo de 2 pasos:** primero aparece la confirmación §PK.5.2 ("¿Estás seguro…? Puedes reactivarla") con **"Cancelar / Sí, desactivar"** lado a lado; **si la sucursal tiene inventario**, al confirmar pasa a este segundo modal: `toggle-off` + **"Desactivar sucursal"** + *"Para desactivar esta sucursal, debes seleccionar otra para transferir el inventario: Inventario surtido en esta sucursal / Pedidos sin preparar asignados a esta sucursal"* + **selector "Sucursal"** ("Seleccionar" → "Polanco") con dropdown + botón **"Desactivar"** (deshabilitado hasta elegir).
> [nota diseñador]: *"Si la sucursal tiene inventario, el usuario debe seleccionar otra sucursal para mover todo el inventario y luego podrá eliminarla."*
> [nota]: *"BOTÓN 'DESACTIVAR': Deshabilitado hasta que se seleccione una sucursal."*

### PK.5.4 Cambiar sucursal y desactivar — `4279:117762`
`toggle-off` (círculo gris `#F8F8F8`) + **"Cambiar sucursal y desactivar"** (`T2 S` 20) + *"Usaremos esta sucursal para descontar inventario de tus ventas en línea. ¿Estás seguro de que quieres usar esta sucursal?"* + **botones apilados full**: **"Sí, cambiar y desactivar"** (rojo **arriba**) + **Cancelar** (blanco abajo), h40 gap 5. Los botones se renderizan como **pill** (radio tipo cápsula, igual que "Activar" §PK.4.5). 🔴 Nota: hay screenshots con el orden invertido (Cancelar arriba); confirmar el orden canónico.

### PK.5.5 Cambiar sucursal principal — `736:27325`
`toggle-off` + **"Cambiar sucursal principal"** (`T2 S` 20) + *"Usaremos esta sucursal para descontar inventario de tus ventas en línea. ¿Estás seguro de que quieres establecerla como tu sucursal principal?"* + botones **lado a lado**: **Cancelar** (blanco) + **"Sí, cambiar"** (rojo). (Nota: existe también una variante con botones apilados "Confirmar/Cancelar" — confirmar cuál es la canónica.)

> ✅ **Lógica de estado bien modelada:** desactivar depende de si hay inventario (si lo hay, obliga a transferir a otra sucursal primero, con el botón deshabilitado hasta elegir destino). El botón "Activar" no se muestra si se alcanzó el límite del plan. Documentar estas **reglas de negocio** como parte del sistema.

## PK.6 E · Envíos a domicilio / Store Setting — `4279:149531`
Título **"Envíos a domicilio"**. Lista de sucursales, cada una con: **nombre** (Centro · Lake Zurich · Moneda · Plaza Carso) + **dirección** + **more-horizontal** (menú) + fila **"Estado"** + **chip**. Lake Zurich trae **badge** extra. Buscador **"Buscar por nombre"**.

> Es la pantalla de configuración de qué sucursales hacen envío a domicilio. Se conecta con la sección "Preparación de pedidos" del detalle (§PK.4.3).

## PK.7 Componentes nuevos
- **Card de sucursal** (nombre + badge Principal + dirección + chips) — §PK.2.2.
- **Badge "Principal"** (ámbar `#EDBD55`/`#FFFCE5` con estrella) — §PK.4.2.
- **Chip "POS básico"** (azul `#2180FF`/`#F0F8FF`, plan POS) — §PK.2.2.
- **Formulario de dirección MX** (11 campos + encargado) — §PK.3.
- **Ficha de detalle de sucursal** (métricas + datos + preparación) — §PK.4.
- **Métricas de sucursal** (Ventas/SKU's/Valor de inventario) + **selector de periodo "30 días"** — §PK.4.1/§PK.4.4.
- **Banner "Sucursal inactiva"** (azul) + botón "Activar" — §PK.4.5.
- **Botón "Ver inventario"** — §PK.4.4.
- **Acción "Cambiar" (sucursal principal)** — §PK.2.1.
- **Banner de límite de plan** (amarillo `Yellow/500`, botón `Yellow/300`) — §PK.2.3.
- **Modales de estado con transferencia de inventario** — §PK.5.
- **Filtro "Plan POS"** — §PK.2.3.
- **Pantalla "Envíos a domicilio"** — §PK.6.

## PK.8 Pendientes (🔴)

2. 🔴 **Typo "envíar"** → "enviar" en Preparación de pedidos (§PK.4.3).
3. 🔴 **Placeholder `{X}`** en el banner de límite de sucursales (§PK.2.3).
3b. 🔴 **Banner de límite en Manrope** (título SemiBold + cuerpo Regular) — anomalía Manrope (§PK.2.3).
4. 🔴 **"Title" sin resolver** en el botón de una variante de detalle (§PK.4).
5. 🔴 **Tabs desbordados** (`x:-20`/`x:-109`, 360→desborde) — mismo componente roto de los otros tabs (§PK.2).
6. ✅ **Badge "Principal" identificado:** ámbar `#EDBD55`/`#FFFCE5` (`Yellow/300`/`Yellow/500`) con ícono estrella. Registrar `Yellow/300`+`Yellow/500` en COLORS.md (§PK.4.2).
7. 🔴 **Medidas fraccionarias** omnipresentes (`24.328`, `79.328`, `1.7763e-15`…) (§PK.3).
8c. 🔴 **Chips de filtro con badge negro** (no rojo) — actualizado (§PK.2.3).
8d. 🔴 **Botones se renderizan como PILL** (modales + "Activar" + "Ver inventario") pese al `rounded-[12px]` del token — desajuste transversal, revisar el radio real del componente Button (§PK.4.5/§PK.5).
8f. 🔴 **Orden de botones apilados inconsistente** en screenshots del modal "Cambiar y desactivar" (primario arriba vs Cancelar arriba) — confirmar canónico (§PK.5.4).
9. Íconos a `icons.ts`: `toggle-off`, `cancel-01`, `more-horizontal`, `add-01`, `icon/action/close`, `status`.

## PK.10 Referencias
- *Branches* (`421:21749`).
- **Listado:** `733:42938` · `733:43209` · con filtros `4183:109155`/`4183:108641` · búsqueda `4183:107930` · límite `736:26841` · menú `733:43356`.
- **Nueva sucursal:** `4278:114384` (form) · `423:28209` (sección).
- **Detalle:** Branch Main `448:33025`/`4279:118691` · Branch New `448:32546` · Sucursal 1 `4279:117631`.
- **Modales:** eliminar `4279:117687` · desactivar s/inv `4279:117704` · desactivar c/inv `4279:117719`/`4279:117741` · cambiar y desactivar `4279:117762` · cambiar principal `736:27325`.
- **Envíos a domicilio:** `4279:149531`. **Menú sucursales (base):** `423:49559`.

---

# Canales de venta (Sales Channels, §CV)

> **Sección "Section 5"** (`4292:28699`). Flujo de **Canales de venta** de la App: conectar la tienda a marketplaces (Mercado Libre, Shein, Amazon…), tiendas en línea (Shopify, WooCommerce) y ver los "próximamente". Se accede desde **Más › OTROS › Canales de venta**.
> **El flujo se repite por canal** — solo cambia el logo, el nombre y el contenido. Se documentan las **pantallas plantilla**, no cada canal.
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `4292:28699`.

## CV.1 Mapa del flujo

```
Más › Canales de venta
│
├── PLANTILLA 1 · LISTADO (434:38699)
│   Header "Canales de venta" + more-vertical
│   Buscador "Buscar canales, tiendas en línea"
│   Tabs: Todos · Activo · Próximamente
│   ├── Marketplace: Mercado Libre · Shein · Sanborns · Sears · Walmart · AliExpress · Amazon
│   ├── Tiendas en línea: Shopify · WooCommerce
│   └── Próximamente: Wix · Prestashop · Vtex · Magento · Liverpool · Elektra · Coppel · Tiktok shop · Totalplay
│   (cada tile: logo 56 + nombre + botón "Conectar" [+ chip "Activo" si conectado])
│   Variantes: 429:47210 (meli activo) · 429:46019 (varios activos) · 429:46505 (solo próximamente)
│
├── PLANTILLA 2 · CONECTAR CANAL / onboarding (429:45091)
│   logo + nombre + descripción + video + "¿Cómo me conecto?" (4 pasos) + 4 tarjetas de recursos
│
├── PLANTILLA 3 · DETALLES DEL CANAL / credenciales (448:31918)
│   ID de cuenta · Contraseña de cuenta · Correo electrónico (Opcional)
│
├── PLANTILLA 4 · CANAL PRÓXIMAMENTE (429:45172)
│   logo + nombre + descripción + video (sin conectar, "Próximamente")
│
├── PLANTILLA 5 · CANAL CONECTADO / sincronización (4184:167202)
│   header + chip estado + toggle
│   Pedidos · Productos · Activación masiva · Reglas de inventario (tarjetas de sync)
│
├── PLANTILLA 6 · ERROR DE SINCRONIZACIÓN (434:39116)
│   wifi-error + "Error de sincronización detectado" + 2 botones
│
└── PLANTILLA 7 · CARGA / lazy load (434:40639 skeletons · 434:40668 spinner)
```

## CV.2 Plantilla 1 · Listado de canales — `434:38699`
- **Header:** "Canales de venta" + **more-vertical** (menú).
- **Buscador:** "Buscar canales, tiendas en línea".
- **Tabs:** **Todos · Activo · Próximamente**.
- **Tres secciones**, cada una una grilla de 2 columnas de tiles:
  - **Marketplace:** Mercado Libre · Shein · Sanborns · Sears · Walmart · AliExpress · Amazon.
  - **Tiendas en línea:** Shopify · WooCommerce.
  - **Próximamente (9):** Wix · Prestashop · Vtex · Magento · **Liverpool** · **Elektra** · Coppel · **Tiktok shop** · **Totalplay**.
- **Tile de canal**: **card `#F8F8F8` r16** con **logo** (isotipo 56, en tarjeta blanca) + nombre (`B2 S` 14) + **botón "Conectar canal"** (blanco borde `#F3F3F3` r8, 32h, `B3 M` 12 — **no rojo**). En "Próximamente" el botón es **"Me interesa →"** (con flecha). Canal conectado muestra **chip "Activo"** (verde).
- Cada sección cierra con **"Ver menos ⌃"** (expandir/colapsar).

### CV.2.1 Variantes del listado
- **Tab "Activo"**: muestra **solo los canales conectados**, agrupados por sección (Marketplace, Tiendas en línea — sin "Próximamente"). El tile activo tiene: **chip "Activo"** (verde `#4FC153`/`#F0FDF4`) bajo el nombre + botón **"Configuración →"** (blanco borde, con flecha), en vez de "Conectar canal".
- **Con canal(es) activo(s) en "Todos"**: los tiles conectados muestran el **chip "Activo"** dentro de la vista completa.
- **Tab "Próximamente"**: muestra **solo la sección "Próximamente"** — grilla de tiles card gris con logo + nombre + botón **"Me interesa →"** (sin chip, sin "Conectar canal"). En el screenshot se ven 7 (Wix, Prestashop, Vtex, Magento, Liverpool, Elektra, Coppel); Tiktok shop y Totalplay quedan bajo el scroll.
- **Búsqueda activa**: buscador con texto ("Mercado") + `cancel-01`.

> **Tres estados del botón del tile:** **"Conectar canal"** (no conectado) · **"Configuración →"** (conectado/activo) · **"Me interesa →"** (próximamente).

## CV.3 Plantilla 2 · Conectar canal (onboarding) — `429:45091`
Header **"Conectar canal de {Canal}"** (ej. "Conectar canal de Shein"). Contenido:
1. **Encabezado del canal:** logo (48) + nombre + **descripción** *"Conecta tu tienda de {Canal} con T1tienda y simplifica la gestión de pedidos, ahorra tiempo en administración y asegura tu… leer más"* (truncada con "leer más").
2. **Video/preview:** rectángulo (328×180) con **botón play** circular (56).
3. **"¿Cómo me conecto?"** — **4 pasos numerados** (1–4) con línea vertical conectora, cada uno con título + descripción.
4. **Segunda sección "¿Cómo me conecto?"** — **4 tarjetas de recursos** (íconos: `file-text`, `clipboard-list-check`, `pin`, `reportes`) con texto de apoyo.
5. **Footer:** componente **Messages** (aviso) + **Button** (48h) "Conectar".

## CV.4 Plantilla 3 · Detalles del canal / credenciales — `448:31918`
Header **"Detalles del canal"**. Formulario:
- **ID de cuenta** · **Contraseña de cuenta** · **Correo electrónico (Opcional)**.
- Footer: **Button** (48h).

## CV.5 Plantilla 4 · Canal "Próximamente" — `429:45172`
Header **"{Canal} Próximamente"** (ej. "Wix Próximamente"). logo + nombre + **descripción** *"Conecta fácilmente tu tienda de {Canal} con T1tienda… ver más"* + **video/play** + footer Messages + Button. Es la variante de un canal aún no disponible: muestra la info pero no permite conectar.

## CV.6 Plantilla 5 · Canal conectado / sincronización — `4184:167202`
Header **"Conectar {Canal}"** (ej. "Conectar Shein"). Estructura (validada por design context):
- **Encabezado:** logo (40) + nombre ("Shein", `B1 S`) + **chip de estado** ("INACTIVO", `#F3F3F3`/`#9CA3AF`) + **Control (toggle)** a la derecha.
- **Cuatro tarjetas de sincronización** (borde `#E7E7E7` r16), cada una con el diagrama **{Canal} → T1com** (isotipo + flecha + T1com) + descripción + botón:
  | Tarjeta | Descripción | Botón |
  |---|---|---|
  | **Sincronizar tus pedidos** | "Sincroniza tus pedidos anteriores de Shein a T1tienda" | Sincronizar pedidos (`recycle-03`) |
  | **Sincronizar tus productos** | "Sincroniza tus productos de Shein al catálogo de T1tienda" | Sincronizar productos (`recycle-03`) |
  | **Activación masiva** | "Activa masivamente tus productos de cualquier canal de ventas a Shein" | Activar de forma masiva (`workflow-square-06`) |
  | **Reglas de inventario** | "Define el inventario mínimo para que un producto esté activo" | Establecer reglas |
- **Footer:** Button (48h).

## CV.7 Plantilla 6 · Error de sincronización — `434:39116`
Ícono **wifi-error** (círculo 64) + **"Error de sincronización detectado"** + *"No pudimos sincronizar tus datos más recientes por un problema de conexión. Revisa tu conexión a internet o intenta reconectar más abajo."* + **2 botones** (Button 48 + Button 40).

## CV.8 Plantilla 7 · Carga (lazy load) — `434:40639` / `434:40668`
- **Skeletons**: rectángulos placeholder (título, tabs, tiles) mientras carga.
- **Spinner**: `tabler:loader` centrado.

## CV.9 Acceso · Más / Settings — `1961:76003`
Pantalla **"Más"** con secciones: **PAGOS** (Transacciones · Disputas · Links de pago · Liquidaciones · Configuración de T1pagos), **MI TIENDA** (Mi tienda · Descuentos), **OTROS** (**Canales de venta** · Marketing · Control de calidad · Clientes · Reportes y análisis). El acceso a Canales de venta está en **OTROS**.

## CV.10 Componentes nuevos
- **Tile de canal** (logo + nombre + botón Conectar + chip estado) — §CV.2.
- **Pasos numerados "¿Cómo me conecto?"** (1–4 con línea conectora) — §CV.3.
- **Tarjeta de recurso** (ícono + texto) — §CV.3.
- **Formulario de credenciales de canal** — §CV.4.
- **Tarjeta de sincronización** (diagrama {Canal}→T1com + botón) — §CV.6.
- **Encabezado de canal con toggle de estado** — §CV.6.
- **Estado de error de sincronización** — §CV.7.
- **Skeletons / spinner de carga** — §CV.8.

## CV.11 Pendientes (🔴)
1b. ✅ **Tile validado:** card `#F8F8F8` r16, botón **"Conectar canal"** blanco (no rojo) / **"Me interesa →"** en Próximamente (§CV.2).
7. Íconos a `icons.ts`: `more-vertical`, `cancel-01`, `wifi-error-01`, `tabler:loader`, `recycle-03`, `workflow-square-06`, `sales channel`, y logos de canales.

## CV.13 Referencias
- *Section 5* (`4292:28699`).
- **Listado:** `434:38699` · variantes `429:47210`/`429:46019`/`429:46505`/`1961:76419` · búsqueda `429:46859`.
- **Onboarding:** `429:45091`. **Credenciales:** `448:31918`. **Próximamente:** `429:45172`/`429:47160`.
- **Canal conectado:** `4184:167202`. **Error sync:** `434:39116`. **Lazy load:** `434:40639`/`434:40668`.
- **Acceso (Más):** `1961:76003`. **Nota diseñador:** `1708:99269`.

---

# Flujo 24 — Envíos (§EN)

> **Sección "Section 2"** (`4298:44178`). Flujo de **Envíos** de la App: gestiona los envíos del negocio a través de múltiples paqueterías (FedEx, DHL, Grupo ampm, 99 Minutos, Amazon), con listado por estado, tarjetas de envío, menús de acciones, y un **timeline de rastreo** detallado. Se apoya en **T1envíos** (el producto de logística de T1).
> **Owner:** Karla Salazar — Head of UX/UI. **Figma:** `4298:44178`.

## EN.1 Mapa del flujo

```
Envíos
│
├── A. LISTADO (Shipments)
│   Header "Envíos" + tabs: Cotizar · Mis envíos · Guías de rastreo · Recolecciones
│   ├── Estado vacío (822:57994): "Aún no tienes envíos"
│   ├── Con envíos (822:58177): buscador + tarjetas de envío
│   ├── Con filtros (823:61568): Fecha 1 · Origen
│   ├── Menú "Crear" (823:62071): Crear envío · Crear guías masivas · Exportar
│   └── Menú por envío (823:62672): Rastrear envío · Descargar guía · Reportar incidencia · Imprimir guía · Cancelar guía
│
├── B. TARJETA DE ENVÍO
│   transportista (logo) + guía + precio + canal de ventas + fecha + cliente
│
└── C. RASTREO (Track Shipment, 523:36361)
    header transportista + guía + "Llega el {fecha}"
    Origen / Destino (sucursal → cliente)
    Timeline de eventos (entregado → en camino → guía generada → preparado → confirmado → creado)
    footer: Descargar guía + Ver detalles del envío
```

## EN.2 A · Listado de envíos

### EN.2.1 Estructura
- **Header:** "Envíos".
- **Tabs** (4): **Cotizar · Mis envíos · Guías de rastreo · Recolecciones**.
- **Buscador:** "Buscar".
- Contenido: lista de **tarjetas de envío** o estado vacío.

### EN.2.2 Estado vacío — `822:57994`
Ilustración (camión de reparto rojo) + **"Aún no tienes envíos"** (`T3 S` 20) + *"Una vez que crees uno, aparecerán aquí."* + **botón "Crear envío"** (rojo `#DB3B2B`, 48h).

### EN.2.3 Con envíos — `822:58177`
Buscador + lista de tarjetas de envío (§EN.3). Cada tarjeta muestra un envío con su paquetería, guía, precio, canal y cliente.

### EN.2.4 Con filtros — `823:61568`
Chips de filtro: **Fecha** (con contador **1**) · **Origen**. Filtran la lista por fecha de creación y sucursal de origen.

### EN.2.7 Drawer de filtros "Filtrar"
Sheet de filtros (mismo patrón que Precios §PI.5b y Sucursales §PK.2.3b): **"Filtrar"** + **"Restablecer"**. Secciones acordeón (cada una con contador y colapsable):
- **Odenar por** 🔴 (mismo typo "Odenar") — select "Fecha de creación (Más recientes primero)".
- **Paquetería:** FedEx · DHL · Grupo ampm · **UPS** · 99 Minutos (checkboxes con logo).
- **Estado (estados reales del envío):** **Por recolectar · Recolectado · En camino · Entregados · Excepción de entrega**. → Este es el **ciclo de vida del envío** (resuelve el pendiente del chip de estado §EN.3).
- **Fecha:** Hoy · Últimos 7 días · Últimos 30 días · Fecha personalizada.
- **Origen:** buscador "Buscar sucursal" + checkboxes (Almacén Polanco, Sucursal Norte).
- Footer: **"Mostrar resultados"** (rojo, ancho completo).

Vista **colapsada:** acordeones cerrados con contador — Paquetería (1) · Estado (1) · Fecha · Origen.

> ✅ **Estados del envío identificados:** Por recolectar → Recolectado → En camino → Entregados (+ Excepción de entrega). Es el ciclo de vida que va en el chip de estado de la tarjeta (§EN.3).

### EN.2.5 Menú "Crear" (opciones superiores) — `823:62071`
Menú desde el header ("Opción"):
- **Crear envío** — alta de un envío individual.
- **Crear guías masivas** — generación en lote.
- **Exportar** — exportar la lista de envíos.

### EN.2.6 Menú por envío (acciones de tarjeta) — `823:62672`
Menú contextual de cada envío ("Opción"):
- **Rastrear envío** (→ §EN.4).
- **Descargar guía de envío**.
- **Reportar incidencia**.
- **Imprimir guía**.
- **Cancelar guía**.

## EN.3 B · Tarjeta de envío (validada `822:58177`)
Card blanca **borde `#F3F3F3` r12** (216h), tres filas separadas por divisores:
- **Fila 1:** **logo** del transportista (40, r13) + **nombre** (`B2 S` 14) + **guía** (`B3 R #4C4C4C`, ej. "43567890082") + **precio** (`B2 S`, derecha, ej. "$87.45" / "$449.00") + **more-horizontal** (rotado 90°, menú §EN.2.6).
- **Fila 2:** "Canal de ventas" (`B3 R #4C4C4C`) → valor (`B2 M`: T1envíos / Shopify / Amazon) · "Fecha" → "26 de enero - 2:24 hrs".
- **Fila 3:** "Cliente:" + nombre (`B2 S`, "Javier Mena") + chevron + **chip de estado** (derecha).

### EN.3.1 Chip de estado del envío (colores validados)
El chip refleja el **estado del envío** con estos colores:
| Estado | Fondo | Texto | Familia |
|---|---|---|---|
| **Por recolectar** | `#F3F3F3` | `#4B5563` | Gris (neutro) |
| **Recolectado** | `#FFFCE5` | `#EDBD55` | **Amarillo** (Yellow/500·300) |
| **En camino** | `#F3F3F3` | `#4B5563` | Gris (neutro) |
| **Entregado / Entregados** | `#F0FDF4` | `#4FC153` | **Verde** (Green/500·300) |

> ✅ **Chip de estado resuelto** (pendiente §EN.3 cerrado). Reutiliza el componente **Chips** con las familias del sistema: **verde = entregado**, **amarillo = recolectado (en proceso)**, **gris = por recolectar/en camino (neutro)**. 🔴 Nota: "En camino" en gris (neutro) es cuestionable — normalmente un estado activo llevaría color; confirmar si debería tener su propia familia (¿azul informativo?).

> **Paqueterías soportadas:** FedEx, DHL, Grupo ampm, 99 Minutos, Amazon (tarjetas) + **UPS** (aparece en el filtro §EN.2.7). Documentar los logos como assets.

## EN.4 C · Rastreo del envío (Track Shipment) — `523:36361`
La pantalla más rica del flujo (validada por design context). Estructura:

### EN.4.1 Encabezado
- Header **"Rastrear envío"** (`T3 B` 16, back-arrow).
- **Transportista** (logo 40) + nombre ("DHL", `B2 S`) + **guía** ("3456788909765445676", `B3 R #4C4C4C`) + **"Llega el 26 de enero"** (`B3 M #4C4C4C`, derecha).

### EN.4.2 Origen / Destino
Card (r16) con dos bloques (cada uno `location-05` + label + dirección):
- **Origen:** "Sucursal Polanco" + "Lago Zurich 25, 55110, CDMX, México."
- **Destino:** "Maria Fernanda Baz Carrillo" + "Socrates 25, 55110, CDMX, México."

### EN.4.3 Timeline "Rastrear envío"
Línea de tiempo de eventos, cada uno con **ícono de estado** (círculo `#F8F8F8` r12 40px con `checkmark-circle-02`) + título + hora + (a veces) acción. **Chips de fecha** (`#F3F3F3`/`#4B5563` r6, "16 de junio") separan los días. Eventos (de más reciente a más antiguo):
| Evento | Detalle | Acción |
|---|---|---|
| **Paquete entregado #101 - SH01** | 17:34 hrs | (expandible ⌃) |
| **Paquete en camino #101 - SH01** | 17:34 hrs | **Ver rastreo** (link) |
| **Generaste la guía - #101** | logo DHL + "3245456435434324" + 17:34 hrs | **Ver / Imprimir guía** (link) |
| **Preparaste 3 productos de (Sucursal)** | 17:34 hrs | (expandible ⌃) |
| **Pedido confirmado** | "$2,629.36 - Pago (por SPEI en efectivo)" + 17:34 hrs | **Ver comprobante de pago** (link) |
| **Pedido creado - pago pendiente** | "$2,629.36" + "17:34 hrs - 12 oct 2025" | — |

### EN.4.4 Footer
`#F8F8F8` con 2 botones: **"Descargar guía"** (rojo `#DB3B2B`, `B2 S` blanco) + **"Ver detalles del envío"** (blanco borde `#F3F3F3`).

> ✅ **El timeline conecta todo el ciclo del pedido→envío:** desde "Pedido creado" (pago pendiente) → confirmado → preparado → guía generada → en camino → entregado. Es la **traza completa** que une Pedidos (§13), Preparación (§PK.4.3) y Envíos. Vincula al comprobante de pago, a la guía y al rastreo del transportista.

## EN.5 Componentes nuevos
- **Tabs de Envíos** (Cotizar/Mis envíos/Guías de rastreo/Recolecciones) — §EN.2.1.
- **Tarjeta de envío** (transportista + guía + precio + canal + cliente + chip de estado) — §EN.3.
- **Chip de estado de envío** (Por recolectar/Recolectado/En camino/Entregado) — §EN.3.1.
- **Menú "Crear"** (envío / guías masivas / exportar) — §EN.2.5.
- **Menú de acciones de envío** (rastrear/descargar/reportar/imprimir/cancelar) — §EN.2.6.
- **Chips de filtro** (Fecha/Origen) — §EN.2.4.
- **Timeline de rastreo** (eventos + chips de fecha + acciones) — §EN.4.3.
- **Bloque Origen/Destino** — §EN.4.2.
- **Logos de paqueterías** (FedEx/DHL/Grupo ampm/99 Minutos/Amazon) — §EN.3.

## EN.6 Pendientes (🔴)
2. 🔴 **3 pantallas sin texto en metadata** (`822:60086`, `4184:168235`, `822:60492`, 1055h) — son variantes que necesitan design context/screenshot para documentar (¿detalle de envío? ¿cotizar?) (§EN.2).
3. 🔴 **Tabs "Cotizar" y "Recolecciones"** aún sin pantalla propia documentada — solo aparecen como tabs. Confirmar su contenido (§EN.2.1).
4. ✅ **Estados del envío identificados** (del filtro §EN.2.7): Por recolectar · Recolectado · En camino · Entregados · Excepción de entrega. Confirmar cómo se renderiza el chip en la tarjeta (§EN.3).
5. 🔴 **"Reportar incidencia"** y **"Cancelar guía"** — flujos destino sin documentar (§EN.2.6).
6. Íconos a `icons.ts`: `location-05`, `checkmark-circle-02`, `line-md:chevron-up`, `majesticons:arrow-up`, `cbi:dhl`, logos de paqueterías.

## EN.8 Referencias
- *Section 2* (`4298:44178`).
- **Listado:** vacío `822:57994` · con envíos `822:58177`/`823:63738`/`823:63270` · filtros `823:61568` · menú crear `823:62071` · menú envío `823:62672`.
- **Variantes 1055h (por documentar):** `822:60086` · `4184:168235` · `822:60492`.
- **Rastreo:** `523:36361` (+ footer `523:36910`).

---

## EN.9 Crear envío — wizard (desde "sin dirección guardada")

> **Sección "Create Shipment When no address is created"** (`465:48968`). El flujo completo para **crear un envío**, arrancando desde el caso en que el negocio **aún no tiene una dirección de origen guardada**. Es un **wizard de 3 pasos** (PASO 1/3 → 2/3 → 3/3) + resumen + éxito. 51 pantallas en Figma (muchas son estados del mismo paso).
> **Figma:** `465:48968`. **Owner:** Karla Salazar — Head of UX/UI.

### EN.9.1 Mapa del flujo

```
Crear envío
│
├── 0. SIN DIRECCIÓN (455:42910)
│   "Aún no tienes una dirección de envío" → obliga a agregar dirección de origen
│
├── AGREGAR DIRECCIÓN (455:44001) — form largo
│   Nombre del lugar · Contacto · Correo · Teléfono · Compañía (opc)
│   Dirección: Calle · Núm ext · Núm int · CP · Colonia · Estado · Ciudad · Referencia
│   ☑ Establecer como predeterminada · ☑ Establecer como dirección de devolución
│
├── PASO 1/3 · DIRECCIONES (455:44464)
│   Dirección de origen (Almacén CDMX + Cambiar)
│   Dirección de destino (form de contacto + dirección)
│   ☑ Guardar este cliente en T1 para futuros envíos
│
├── PASO 2/3 · DETALLES DEL PAQUETE (455:44804 / 465:49928)
│   Dimensiones (plantilla): Largo · Ancho · Alto · Peso → Peso volumétrico
│   ☑ Guardar como plantilla · plantillas disponibles (buscar/seleccionar)
│   Detalles del envío: Número de paquetes · Descripción del contenido
│   Tipo de producto - SAT (Seleccionando con IA…) · ☑ Incluir seguro de envío
│
├── PASO 3/3 · SELECCIONAR PAQUETERÍA (455:44464 / 532:36426)
│   lista de paqueterías con tarifa/tiempo · estado "No se pudieron obtener las tarifas"
│
├── RESUMEN DEL ENVÍO (465:51476 / 465:51148)
│   Direcciones · Dimensiones · Paquetería · Total → botón "Crear envío"
│
└── ÉXITO (455:47149)
    "¡Tu envío fue creado con éxito!" + guía + pasos siguientes + sucursales/recolección
```

### EN.9.2 Paso 0 · Sin dirección de envío — `455:42910`
Header **"Crear envío"**. Estado vacío: **"Aún no tienes una dirección de envío"** + *"Antes de hacer tu primer envío, necesitamos saber desde dónde se enviarán tus paquetes."* Obliga a **agregar una dirección de origen** antes de continuar.

### EN.9.3 Agregar dirección — `455:44001`
Header **"Agregar dirección"**. Formulario largo (1696h):
| Campo | Placeholder |
|---|---|
| **Nombre del lugar** | Ej. Bodega Central |
| **Nombre de contacto** | Ej. María González López |
| **Correo electrónico** | Ej. maria.gonzalez@ejemplo.com |
| **Número de teléfono** | — |
| **Conpañia (opcional)** 🔴 (typo "Conpañia" → "Compañía") | Ej. 232 |
| **Dirección › Calle** | Avenida Francisco I. Madero |
| **Número exterior** | 140 |
| **Número interior (opcional)** | Depto 5A |
| **Código postal** | 06000 |
| **Colonia** | Buenavista |
| **Estado / Ciudad / Referencia** | — |

Toggles: **☑ Establecer como dirección predeterminada para mis envíos** · **☑ Establecer como dirección de devolución**.

> 🔴 **Typo "Conpañia"** (aparece dos veces) → "Compañía". Este mismo form de dirección aparece en el destino (§EN.9.4).

### EN.9.4 Paso 1/3 · Direcciones — `455:44464`
Header "Crear envío" + **"PASO 1/3"**. Dos bloques:
- **Dirección de origen:** card con **"Almacén CDMX"** + dirección ("Avenida Francisco I. Madero, 140, 18, Centro, Ciudad de México, CDMX") + botón **"Cambiar"**.
- **Dirección de destino:** form de contacto (Nombre · Correo · Número · Compañía opc) + dirección (Calle · Núm ext/int · CP · Colonia · Estado · Ciudad · Referencia).
- **☑ Guardar este cliente en T1 para futuros envíos.**

### EN.9.5 Paso 2/3 · Detalles del paquete — `455:44804` (sin plantilla) / `465:49927` (con plantilla, 6 variantes)
Header "Crear envío" + subtítulo **"Detalles del paquete"** + **"PASO 2/3"** (con barra de progreso 244/360). Indicador de progreso avanza 2/3. Dos secciones colapsables:

**A. Dimensiones del paquete**
- **Chip de plantilla activa**: "Caja para botas" con **`cancel-01`** (removible) — cuando ya hay una plantilla aplicada.
- **Nombre de la plantilla** (input, "Caja para botas" / placeholder "ej. Caja para botas").
- **Grilla 2×2:** **Largo (cm)** "10" · **Ancho (cm)** "15" · **Alto (cm)** "25" · **Peso (kg)** "1" (placeholders "Ej. 10 / ej. 15 / ej. 25 / ej. 1").
- **Resumen cotizador**: **"Peso volumetrico: 1k"** 🔴 (typo "volumetrico"→"volumétrico", "1k"→"1kg") calculado de las dimensiones.
- **Toggles de plantilla:** **"Guardar cambios en esta plantilla"** + **"Guardar como nueva plantilla"**. En la variante sin plantilla: **"Guardar como plantilla para envíos futuros"**.

**Variante "Buscar plantilla"**: buscador **"Buscar plantilla"** + separador **"ó"** + campos vacíos para crear una nueva plantilla desde cero. Incluye un **Dropdown** de selección.

**B. Detalles del envío**
- **Número de paquetes** (input, "1").
- **Descripción del contenido** (textarea, "Zapatos de piel" / "ej. Zapatos de piel").
- **Tipo de producto - SAT** (clave fiscal mexicana), con **tres estados**:
  - **Sin resolver:** placeholder "Seleccionar" (input con dropdown).
  - **Cargando:** **"Seleccionando con IA…"** con spinner (`loader`).
  - **Resuelto:** badge **"Seleccionado por IA"** (arriba-derecha, `Icon_der`) + valor real **"53111502: Botas para mujer"** (clave SAT de 8 dígitos + descripción).
- **"Guardar dirección de"** (label — posible sección de dirección de recolección).
- **☑ Incluir seguro de envío.**
- **Valor del contenido** (input, "$100.00") — para seguro/aduana; aparece en la variante extendida.

> ✅ **Clasificación SAT con IA (estado completo):** el campo "Tipo de producto - SAT" pasa de "Seleccionando con IA…" (cargando) a **"Seleccionado por IA" + clave real** (ej. "53111502: Botas para mujer"). Es la clave de producto/servicio del SAT (requisito fiscal MX) resuelta automáticamente por IA, con opción de editar manualmente (dropdown). Segunda integración de IA en un flujo operativo (además de Nova).
> ✅ **Sistema de plantillas de paquete completo:** chip de plantilla activa (removible), buscar plantilla existente, crear nueva ("ó"/"or"), y guardar (cambios en la actual / como nueva). Acelera envíos recurrentes con dimensiones predefinidas (Caja para botas, Caja de pino…).
> ✅ **Peso volumétrico** calculado de las dimensiones (largo×ancho×alto) — documentar la fórmula exacta y su unidad.
> ✅ **Valor del contenido** — base para el cálculo del seguro y trámites aduanales.

### EN.9.6 Paso 3/3 · Seleccionar paquetería — `455:44464` / `532:36426`
Header "Crear envío" + **"Seleccionar paquetería"** + **"PASO 3/3"**. Lista de paqueterías (FedEx Estandar, DHL Económico/Día siguiente/Semanal…) con tarifa y tiempo de entrega.
- **Estado de error:** **"No se pudieron obtener las tarifas."** — cuando la API de tarifas falla.

### EN.9.7 Resumen del envío — `465:51476` (validado) / `465:51148`
Header **"Resumen del envío"** (`T3 S` 16). Secciones colapsables, cada una con botón **"Editar"** (blanco borde `#F3F3F3` r12):
- **Direcciones:** origen ("Sucursal Polanco" + dirección) → destino ("Maria Fernanda Baz Carrillo" + dirección), con **línea conectora** (`location-04` en cada una).
- **Dimensiones del paquete:** "Caja de pino • 23 x 23 x 23 cm | 3 kg" + "3 paquetes".
- **Paquetería:** logo DHL (40, r5) + "DHL" (`B2 S`) + "Económico / Día siguiente / Semanal" + "Llega el 26 de ene".
- **Total:** **"$214.00"** (`B1 S` 16) + *"Incluye seguro y zona extendida"* (`B3 R #4C4C4C`).
- **Footer fijo** (sombra): botón **"Crear envío →"** (rojo `#DB3B2B`, `B2 S`, con `arrow-right-01-sharp`).

### EN.9.8 Éxito — `455:47149` (validado)
Header con **X** (cerrar, arriba-derecha; no back-arrow) + **ícono check** en círculo verde `#F0FDF4`/`#4FC153` + **"¡Tu envío fue creado con éxito!"** (`T2 S`). Estructura:

**A. Card de resumen del envío** (gris `#F8F8F8`):
- DHL (logo) + guía ("3456788909765445676") + "Llega el 26 de enero".
- **Origen** (sub-card blanca): `location` + "Sucursal Polanco" + "Lago Zurich 25, 55110, CDMX, México."
- **Destino** (sub-card blanca): "Maria Fernanda Baz Carrillo" + "Socrates 25, 55110, CDMX, México."
- **Dos botones:** **"Descargar guía"** (rojo `#DB3B2B`) + **"Ver detalles del envío"** (blanco borde).

**B. "¿Cómo preparar tu envío?"** — 3 bullets: *"Descarga e imprime tu guía."* · *"Empaca tu envío; consulta nuestra guía de sugerencias de empaque…"* · *"Lleva tu paquete a tu sucursal preferida o solicita una recolección en tu domicilio."*

**C. Card "HORARIOS DE SUCURSALES DHL"** (gris): "Lunes a viernes 09:00 a 19:00 hrs / Sábado 10:00 a 14:00 hrs" + botón **"Ver sucursales"** (→ §EN.9.8.1).

**D. Card "RECOLECCIÓN"** (gris): "Solicítala desde nuestro módulo de recolección." + botón **"Programar recolección"** (→ modal §EN.9.8.2).

> 🔴 **Truncamiento:** "HORARIOS DE SUCURSALES DHL" se corta a "HORARIOS DE SUCU…" en el card — revisar ancho/ellipsis.

### EN.9.8.1 Modal "Sucursales" — (al tocar "Ver sucursales")
**Modal** (bottom sheet, no pantalla aparte) que se abre sobre la pantalla de éxito. Contiene un **mapa** interactivo (pines de los puntos DHL + botón **"Abrir en Mapas"** + controles de zoom/ubicación) seguido de la lista **"Sucursales"**. Cada punto:
- **Nombre:** "DHL Express Service Point (AEROPUERTO)" / "(LERMA)" / "EMPAKATODO TOLLOCAN (Centro de envíos DHL autorizado)".
- **Dirección** completa.
- **"Distancia: 2.5 km"** / "3.8 km".
- **"Horario: Lunes a viernes de 10:00 a 18:00 hrs"**.

### EN.9.8.2 Modal "Programar recolección" — (al tocar "Programar recolección")
**Patrón de modal transversal** (mismo que Sucursales §PK.5): círculo gris `#F8F8F8` + ícono (pin de recolección) + título **"Programar recolección"** (`T2 S`) + cuerpo *"Estás a punto de ir al módulo de recolección. Antes de programar una recolección, ten en cuenta:"* + **3 bullets**: *"Revisa nuestra guía para empacar correctamente tus envíos."* · *"Los horarios de recolección pueden variar según la paquetería, el día de la semana y la temporada."* · *"Asegúrate de tener todo listo antes de la visita del mensajero."* + **botones lado a lado**: **Cancelar** (blanco) + **Programar** (rojo).

> ✅ **La pantalla de éxito es un centro de acción post-envío:** guía (descargar / ver detalles), instrucciones de empaque, **sucursales cercanas con mapa/distancia/horarios**, y **módulo de recolección** (con modal de advertencia). No es solo confirmación — orienta los siguientes pasos físicos del envío. El modal reutiliza el patrón de la App (círculo gris + título 20 + botones lado a lado), confirmando su carácter transversal.

### EN.9.13 Variante · Crear envío con direcciones guardadas — `465:55797`
Sección **"Create Shipment When Origin is saved and has destination address"**. Es el **mismo wizard de 3 pasos**, pero cuando el negocio **ya tiene dirección de origen guardada** y **puede seleccionar el destino de sus clientes guardados**. Solo cambia el **Paso 1/3**; los pasos 2/3 y 3/3 son idénticos a §EN.9 (nota del diseñador `465:56273`: *"El resto del proceso es igual al anterior"*).

**Diferencias vs §EN.9 (sin dirección):**

**A. Dirección de origen ya establecida**: card con **"Almacén CDMX"** + **badge** (predeterminada) + dirección + botón **"Cambiar"**. No hay que crear la dirección — ya existe.

**B. Dirección de destino seleccionable**: en vez de un form vacío, arranca con un **buscador "Buscar por cliente o dirección"** + separador **"or"** 🔴 + label **"AÑADE NUEVA Dirección de destino"** sobre el form (contacto + dirección). Puedes **buscar un cliente guardado** o escribir uno nuevo.

**C. Estados del destino:**
- **Cliente seleccionado**: **chip removible** "María López Ruiz | maria.lopez@gmail.com" (`cancel-01`) + tarjeta con datos del contacto ("Fabian Hernández Hernández 55 1234 5678" + dirección) + "Cambiar".
- **Cliente + dirección elegida**: tarjeta con "Fabián Hernandez ! Avenida Francisco I Madero" + dirección + teléfono, con opción "or" para otra.
- **Agregar nueva dirección a cliente existente**: chip de cliente + "Agregar nueva dirección" + divisor + **"Nueva dirección"** + form.

**D. Modal "Cambiar dirección de origen"**: bottom sheet con **"Cambiar dirección de origen"** + buscador "Buscar por nombre del lugar o dirección" + **lista de sucursales** (Bodega CDMX · Sucursal 2 · Bodega centro · Sucursal Polanco) + **"+ Agregar nueva dirección"** (`plus-sign`).

**E. Modal "Cambiar dirección de destino"**: bottom sheet con **"Cambiar dirección de destino"** + buscador + **lista de direcciones de clientes** (con nombre + dirección completa: "Graciela López 140 Avenida Francisco I. Madero…" / "María López Ruiz 435 Lago Zurich…") + **"+ Agregar nueva dirección"**.

**F. Dropdown de selección de cliente**: al buscar, despliega dos grupos:
- **Clientes frecuentes:** Juan Pérez García (55 5123 4567 • Col. Roma Norte) · Ana García Silva (ana.garcia@hotmail.com • dirección).
- **Todos los clientes (A-Z):** Carmen Rodríguez (55 5678 9012 • **4 direcciones**) · José Luis Martínez · María López Ruiz (maria.lopez@gmail.com • Col. Condesa) · Miguel Ángel Torres. Cada uno con `tick-02` (selección). Nota: un cliente puede tener **varias direcciones** ("4 direcciones").

> ✅ **Selección de cliente guardado:** cuando ya hay clientes en T1, el destino se elige de una **libreta de direcciones** (clientes frecuentes + todos A-Z) con buscador y dropdown, en vez de teclear todo. Un cliente puede tener múltiples direcciones. Esto conecta con **"Guardar este cliente en T1 para futuros envíos"** (§EN.9.4): los clientes guardados aquí alimentan esta libreta.
> ✅ **Origen desde sucursales guardadas:** el modal de cambiar origen lista las **sucursales** del negocio (§PK) — el origen de un envío es una de las sucursales/almacenes registrados.

### EN.9.14 Errores de input y validaciones — `4205:105239`
Sección **"Errors validation"**. Estados de validación de los campos del wizard de crear envío. Son estados de sistema reutilizables (aplican al patrón de input de toda la App).

**A. Mensajes de validación de formato** (texto de ayuda bajo el input, gris → rojo en error):
| Campo | Mensaje | Regla |
|---|---|---|
| **Número de teléfono / contacto** | "Debe contener 10 dígitos" | exactamente 10 dígitos (MX) |
| **Código postal** | "Debe contener 5 dígitos" | exactamente 5 dígitos (MX) |
| **Referencia** (textarea) | "Alcanzaste el límite máximo de caracteres" | límite de caracteres alcanzado |

**B. Dropdown/búsqueda sin resultados:**
- **"No hay resultados para tu búsqueda"** — aparece en el dropdown de **cliente** (al buscar, ej. "Tere") y en el de **plantilla** (al buscar, ej. "Caja"). Estado vacío del dropdown.

**C. Alerta de artículo prohibido** (validada) — componente **Messages** que aparece bajo "Descripción del contenido" cuando el contenido puede estar restringido (ej. "Aleta de tiburon"):
- **Fondo `Brown/500 #FAF8F3`** + ícono `alert` + texto **`Yellow/200 #A96A00`**, r10, con sombra.
- Texto (en **Manrope** 🔴): *"Este artículo puede estar prohibido. Revisa las **restricciones** antes de enviarlo; podría generar una multa de $X,XXX."* — con **"restricciones"** como enlace (bold subrayado) y **"$X,XXX"** como placeholder del monto de multa.
- **Semántica:** advertencia (warning), no error bloqueante — informa un riesgo legal/aduanal sin impedir continuar.

> ✅ **Sistema de validación de campos:** el patrón de input soporta **texto de ayuda/error** bajo el campo (formato de teléfono, CP, límite de caracteres), **estado vacío** en dropdowns ("No hay resultados"), y **alertas contextuales** (artículo prohibido). Documentar el estado visual de error del input en sí (borde rojo) además del mensaje.
> 🔴 **Manrope en la alerta de artículo prohibido** — nueva instancia de Manrope fuera de Nova (el componente Messages usa Manrope). Sumar al rastreo de la anomalía Manrope.
> 🔴 **Nueva familia de color "Brown"** (`Brown/500 #FAF8F3`) + **`Yellow/200 #A96A00`** para advertencias de restricción — registrar en COLORS.md.
> 🔴 **"$X,XXX" placeholder** del monto de multa — confirmar si se rellena dinámicamente con el monto real.

### EN.9.9 Componentes nuevos
- **Estado "sin dirección de origen"** — §EN.9.2.
- **Formulario de dirección con toggles** (predeterminada/devolución) — §EN.9.3.
- **Wizard de 3 pasos** (indicador PASO N/3) — §EN.9.1.
- **Card de dirección origen con "Cambiar"** — §EN.9.4.
- **Editor de dimensiones + plantillas de paquete** (chip activo removible + buscar + crear + guardar) — §EN.9.5.
- **Campo "Tipo SAT" con clasificación por IA** (3 estados: seleccionar → cargando → "Seleccionado por IA" + clave real) — §EN.9.5.
- **Resumen cotizador** (peso volumétrico) — §EN.9.5.
- **Campo "Valor del contenido"** (seguro/aduana) — §EN.9.5.
- **Mensajes de validación de campo** (formato teléfono/CP, límite de caracteres) — §EN.9.14.
- **Estado vacío de dropdown** ("No hay resultados para tu búsqueda") — §EN.9.14.
- **Alerta de artículo prohibido** (Messages, Brown/Yellow, Manrope) — §EN.9.14.
- **Selector de paquetería con tarifas** (+ estado de error) — §EN.9.6.
- **Resumen del envío con secciones editables** — §EN.9.7.
- **Selector de dirección de destino** (buscador + chip de cliente removible) — §EN.9.13.
- **Modal "Cambiar dirección de origen"** (lista de sucursales) — §EN.9.13.
- **Modal "Cambiar dirección de destino"** (lista de direcciones de clientes) — §EN.9.13.
- **Dropdown de clientes** (frecuentes + todos A-Z, con múltiples direcciones) — §EN.9.13.
- **Pantalla de éxito** (card resumen + Descargar guía / Ver detalles + cards horarios/recolección) — §EN.9.8.
- **Modal de sucursales cercanas** (mapa + lista con distancia/horario) — §EN.9.8.1.
- **Modal "Programar recolección"** (patrón transversal) — §EN.9.8.2.

### EN.9.10 Pendientes (🔴)
1. 🔴 **Typo "Conpañia"** → "Compañía" (2 veces) (§EN.9.3).
2. 🔴 **Estado "Seleccionando con IA…"** del tipo SAT — documentar el estado final (éxito/error) y qué pasa si la IA no clasifica (§EN.9.5).
3. 🔴 **Fórmula del peso volumétrico** — documentar cómo se calcula ("Peso volumetrico: 1k") + typo "volumetrico"→"volumétrico" y "1k"→"1kg" (§EN.9.5).
4. 🔴 **Estado "No se pudieron obtener las tarifas"** — documentar el fallback/retry del paso 3 (§EN.9.6).
4c. 🔴 **Truncamiento "HORARIOS DE SUCU…"** — el título del card se corta (§EN.9.8).
5. 🔴 **"Estandar"** → "Estándar" (§EN.9.6).
5c. 🔴 **Clave SAT real** "53111502: Botas para mujer" — documentar el formato (8 dígitos + descripción) y qué pasa si la IA no encuentra clave (§EN.9.5).
6. 🔴 **Manrope en la alerta de artículo prohibido** (§EN.9.14) — otra instancia de Manrope fuera de Nova.
7. 🔴 **Colores nuevos** `Brown/500 #FAF8F3` + `Yellow/200 #A96A00` (advertencia de restricción) — registrar en COLORS.md (§EN.9.14).
8. 🔴 **Estado visual de error del input** (borde rojo) — documentar además de los mensajes (§EN.9.14).
6. 🔴 **"Title"** sin resolver en el botón de origen del Resumen (§EN.9.7).
7. ⚠️ **Consistencia del form de dirección:** el de origen (§EN.9.3), destino (§EN.9.4) y el de Sucursales (§PK.3) comparten estructura — unificar como un solo componente de dirección MX.

### EN.9.12 Referencias
- *Create Shipment When no address is created* (`465:48968`).
- **Sin dirección:** `455:42910`. **Agregar dirección:** `455:44001`/`465:49152`/`465:49382`.
- **Paso 1/3:** `455:44464`/`465:48971`. **Paso 2/3:** `455:44804`/`465:49565`/`465:49928` (plantillas: `465:50060`/`465:50178`/`465:50314`/`465:50608`/`465:50911`).
- **Paso 3/3:** `532:36426`. **Resumen:** `465:51476`/`465:51148`. **Éxito:** `455:47149` (+ `465:51698`/`465:51807`).
- **Variante con direcciones guardadas** (`465:55797`): Paso 1/3 origen guardado `465:55798` · cliente seleccionado `465:57167` · cliente+dirección `465:57361` · nueva dirección a cliente `465:57617` · dropdown clientes `465:56793` · modal cambiar origen `4194:39050` · modal cambiar destino `4194:39159` · nota diseñador `465:56273`.
- **Errores y validaciones** (`4205:105239`): teléfono "Debe contener 10 dígitos" `4205:106371` · CP "Debe contener 5 dígitos" `4205:107147` · límite caracteres `4205:107173` · dropdown sin resultados `4205:106540` · alerta artículo prohibido `4205:106781`.

---

## EN.10 Cotizar — cotizador de envíos (§EN, tab "Cotizar")

> **Sección "Quote"** (`467:14391`). El **cotizador rápido de envíos**: se accede desde la **tab "Cotizar"** del listado de Envíos (§EN.2.1) — resuelve el pendiente de esa tab, que no tenía pantalla propia documentada. A diferencia de Crear envío (§EN.9), Cotizar es **anónimo y ligero**: solo pide **CP de origen/destino + dimensiones** (sin direcciones completas, sin cliente, sin clave SAT) y devuelve un **estimado de precios por paquetería**. Es la puerta de entrada antes de crear el envío formal.
> **Figma:** `467:14391`. **Owner:** Karla Salazar — Head of UX/UI.

### EN.10.1 Mapa del flujo

```
Envíos › tab "Cotizar"
│
├── FORMULARIO DEL COTIZADOR (8 casos/estados)
│   CP origen (Ej. 06700) · CP destino · Largo/Ancho/Alto/Peso · Incluir seguro
│   [+ Valor del contenido cuando el seguro está activo]
│   → Resumen cotizador (Peso volumétrico) → 2 botones
│
└── SELECCIONAR PAQUETERÍA (resultados)
    Filtros: Paquete · Tipo de servicio · Ventaja
    Tarjetas de opción (radio + logo + carrier + tipo + chip ventaja + precio + fecha)
    ├── Filtro de paqueterías (checkboxes con logos)
    └── Popups de desglose: Insurance / Insurance & Extended Area
```

### EN.10.2 Los 8 casos del cotizador (etiquetados por el diseñador)
El formulario del cotizador se documenta en **8 estados** (los frames "Caso N:" son etiquetas del diseñador):

| # | Caso | Figma | Qué muestra |
|---|---|---|---|
| **1** | **Cotizador vacío** | `824:65838` | Form base: CP origen "Ej. 06700" + CP destino + Largo/Ancho/Alto/Peso + ☑ Incluir seguro de envío + 2 botones |
| **2** | **Cotización completa sin seguro** | `824:66369` | CP origen "11529" + CP destino "06700" (ambos con **checkmark-circle-02** ✓) + dimensiones llenas + **Resumen cotizador** (Peso volumétrico) |
| **3** | **Cotización completa con seguro** | `824:66612` | Igual + campo **"Valor del contenido"** ("$100.00") que aparece al activar el seguro |
| **4** | **C.P. en proceso de validación** | `824:66932` | CP origen "115" con **loader** (spinner) mientras valida el código postal |
| **5** | **C.P. correcto** | `824:67168` | CP con **checkmark-circle-02** verde (validado) |
| **6** | **Campos incorrectos** | `824:67371` | **Error Input:** CP origen "11529" + "**Código postal no disponible**", CP destino "55635" + "Código postal no disponible", Largo/Ancho/Alto/Peso "0" + "**Debe ser mayor que 0**" |
| **7** | **Resultados** | `824:67617` | Cotización completa con seguro + Valor del contenido "$100.00" (estado listo para cotizar) |
| **8** | **Seguro activo sin Valor del contenido** | `824:67892` | Seguro activado pero "Valor del contenido" en "$0.00" (validación pendiente antes de cotizar) |

**Botones del cotizador** (validado screenshot): dos botones apilados al pie del form — **"Borrar datos"** (arriba, blanco con borde) + **"Cotizar"** (abajo, rojo). El botón **"Cotizar" está deshabilitado** (rojo atenuado `~#EBA9A0`) mientras el formulario no esté completo/válido; se habilita a rojo pleno cuando CP origen/destino son válidos y hay dimensiones. 🔴 Antes documenté "Limpiar" — el texto real es **"Borrar datos"**.

**Checkbox "Incluir seguro de envío"** (validado): es un **checkbox cuadrado** (`Control`), no un toggle switch.

**Barra de navegación inferior:** el cotizador vive dentro del contenedor de la App con la **tab bar** visible (home · carrito · etiqueta · **camión activo en rojo** · "…" · botón "+"). Confirma que Cotizar/Envíos es una sección de nivel superior de la App (ícono camión).

**Estados de validación del CP** (progresión): vacío → **escribiendo/validando** (loader, caso 4) → **válido** (**checkmark-circle-02 sólido** — círculo verde relleno con palomita blanca, no outline; caso 5) → **inválido** ("Código postal no disponible", caso 6). El CP se valida contra cobertura de paqueterías en tiempo real.

**Resumen cotizador** (validado design context) — **tres líneas** en **Manrope** 🔴 (SemiBold):
- **Peso físico:** "6 kg" (peso real declarado).
- **Peso volumétrico:** "10.8 kg" (calculado de largo×ancho×alto; label con **subrayado punteado** → tiene tooltip explicativo).
- **Peso a cotizar:** "10.8 kg" (el **mayor** entre físico y volumétrico — es sobre el que se cobra; también con subrayado punteado/tooltip).

> ✅ **Peso a cotizar = max(físico, volumétrico)** — así cobran las paqueterías. El subrayado punteado en volumétrico y a cotizar indica tooltips que explican el cálculo.
> 🔴 **Manrope** — el Resumen cotizador usa Manrope (SemiBold), otra instancia fuera de Nova. Sumar a la anomalía Manrope.

**Campo "Valor del contenido"**: aparece condicionalmente cuando **"Incluir seguro de envío"** está activo. Necesario para calcular la prima del seguro. Caso 8 valida que no quede en "$0.00".

### EN.10.3 Seleccionar paquetería — `522:16912` / `4198:68188`
Header **"Seleccionar paquetería"**. Es la pantalla de **resultados** de la cotización. Estructura:

**Filtros/orden** (fila superior, cada uno con chevron): **Paquete** · **Tipo de servicio** · **Ventaja**.

**Tarjetas de opción de paquetería** (validadas por screenshot). Card blanco r12, borde `#F3F3F3`, padding 16. Anatomía:
- **Fila superior:** **radio** (`Control`; seleccionado = **círculo rojo relleno** `#DB3B2B`) + **logo 40** (r13, borde) + nombre carrier (`B2 S` 14) + tipo de servicio (`B3 R` 12, `#4C4C4C`) + **chip de ventaja** opcional (arriba-derecha).
- **Divisor** (`Line 711`, `#F3F3F3`).
- **Fila "Precio":** label "Precio" (`B3 M` 12, gris) a la izquierda + columna derecha con **precio "$158.00"** (`B2 S` 14, negro, **sin "MXN"**) + nota **"*incluye seguro de $23.00"** (`B3 R` 12, `#4C4C4C`, **subrayada**).
- **Fila "Fecha estimada":** label gris + **"26 de ene"** (`B2 M` 14, gris).

| Carrier | Tipo de servicio | Precio | Nota | Chip |
|---|---|---|---|---|
| **FedEx** | Estandar 🔴 | $158.00 | *incluye seguro de $23.00 | **Recomendado** |
| **FedEx** | Mismo día / 24H | $158.00 | *incluye seguro de $23.00 | — |
| **UPS** | Mismo día / 24H | $158.00 | *incluye seguro de $23.00 y zona extendida de $54.00 | — |
| **Grupo ampm** | Mismo día / 24H | $158.00 | *incluye seguro de $23.00 | — |
| **DHL** | Económico / 2 días | $158.00 | *incluye seguro de $23.00 | — |

**Chip de ventaja "Recomendado"** (validado): fondo **`#DB3B2B` (Primary/600)** + texto **`#FFF0EF` (Primary/100)**, r6, `B3 S` 12. Marca la opción recomendada (típicamente la más barata o mejor balance).

**Footer — dos botones** (validado screenshot): **"Ver más opciones"** (blanco con borde) + **"Créar envío"** 🔴 (rojo, **deshabilitado** hasta seleccionar una paquetería; typo "Créar"→"Crear"). Antes documenté un solo botón "Seleccionar paquetería" — el real es este par.

> 🔴 **Precio "$158.00" sin "MXN"** en la tarjeta (el "MXN" solo aparece en los popups de desglose §EN.10.5). Corregido de "$218.00 MXN".
> 🔴 **Typos:** "Estandar"→"Estándar", "Créar envío"→"Crear envío", "*incluye seguro **e** $23.00"→"de".

### EN.10.4 Filtro de paqueterías — `468:44983`
Lista de **checkboxes con logos** (`checkmark-square-02` + iso del carrier) para filtrar por paquetería: **99 minutos · DHL · FedEx · Grupo AMPM · Paquetexpress · UPS** (visibles) + ocultos en el componente (Sears, Aliexpress, Shopify, Mercado Libre, Woocommerce). Coincide con el set de paqueterías del drawer de filtros de Envíos (§EN.2.7).

### EN.10.5 Popups de desglose de costo (validados)
Al tocar la nota "*incluye seguro…" o el precio, se abre un **popup de desglose** del costo. Dos variantes:

**Insurance** (validado): card blanco r16, borde `#F3F3F3`, sombra fuerte:
| Concepto | Monto |
|---|---|
| Precio de guía | $122.00 MXN |
| **Seguro ($856.00)** | $72.00 MXN |
| **Total** | **$194.00 MXN** |

**Insurance & Extended Area** (validado): añade la fila de zona extendida:
| Concepto | Monto |
|---|---|
| Precio de guía | $122.00 MXN |
| Seguro ($856.00) | $72.00 MXN |
| **Zona extendida** | $45.00 MXN |
| **Total** | **$214.00 MXN** |

> ✅ **Transparencia de costo:** el popup desglosa precio de guía + seguro (con el valor asegurado entre paréntesis) + zona extendida → total. Explica de dónde sale cada peso de la tarifa.

### EN.10.6 Componentes nuevos
- **Formulario de cotizador** (CP origen/destino + dimensiones + checkbox seguro condicional) — §EN.10.2.
- **Botón "Cotizar" con estado deshabilitado** (rojo atenuado hasta que el form es válido) + "Borrar datos" — §EN.10.2.
- **Resumen cotizador** (Peso físico / volumétrico / a cotizar, con tooltips) — §EN.10.2.
- **Indicador de CP válido** (checkmark-circle-02 sólido verde) — §EN.10.2.
- **Validación de CP en tiempo real** (loader → checkmark-circle-02 → error) — §EN.10.2.
- **Error Input con "Código postal no disponible" / "Debe ser mayor que 0"** — §EN.10.2 (estado de error del input, complementa §EN.9.14).
- **Tarjeta de opción de paquetería** (radio rojo + logo + tipo + chip "Recomendado" + precio $158.00 + nota subrayada + fecha) — §EN.10.3.
- **Chip "Recomendado"** (Primary/600 fondo + Primary/100 texto) — §EN.10.3.
- **Footer "Ver más opciones" + "Créar envío"** (deshabilitado) — §EN.10.3.
- **Filtros Paquete/Tipo de servicio/Ventaja** — §EN.10.3.
- **Filtro de paqueterías** (checkboxes con logos) — §EN.10.4.
- **Popup de desglose de costo** (Insurance / Insurance & Extended Area) — §EN.10.5.

### EN.10.7 Pendientes (🔴)
1. 🔴 **"*incluye seguro e $23.00"** → "de". **"Estandar"** → "Estándar" (§EN.10.3).
2. 🔴 **Resumen cotizador en Manrope** — otra instancia de Manrope fuera de Nova (§EN.10.2).
3. 🔴 **"Title"** del botón de Seleccionar paquetería sin resolver (§EN.10.3).
3b. ✅ **Corregido:** el botón secundario es **"Borrar datos"** (no "Limpiar") y "Cotizar" tiene **estado deshabilitado**; el seguro es **checkbox** (no toggle) — validado por screenshot (§EN.10.2).
5. ⚠️ **Estado de error de input reutilizable:** "Código postal no disponible" y "Debe ser mayor que 0" usan el componente **Error Input** con "Info Text" — el mismo patrón de §EN.9.14; unificar la doc del componente Error Input.

### EN.10.9 Referencias
- *Quote* (`467:14391`).
- **8 casos:** vacío `824:65838` · sin seguro `824:66369` · con seguro `824:66612` · CP validando `824:66932` · CP correcto `824:67168` · incorrectos `824:67371` · resultados `824:67617` · seguro sin valor `824:67892`.
- **Seleccionar paquetería:** `522:16912` / `4198:68188`. **Filtro paqueterías:** `468:44983`. **Popups:** Insurance `4198:68365` · Insurance & Extended Area `4198:68378` / `4198:68527`.

---

## EN.11 Tracking de guías — rastreo (§EN, tab "Guías de rastreo")

> **Sección "Tracking Guides"** (`470:45363`). El **rastreo de guías**: se accede desde la **tab "Guías de rastreo"** del listado de Envíos (§EN.2.1) — resuelve el pendiente de esa tab. Tiene dos niveles: un **listado de guías** (tarjetas por guía) y un **Detalle de guía** a pantalla completa con el **historial de actividad** (timeline de eventos de la paquetería, agrupado por día).
> **Figma:** `470:45363`. **Owner:** Karla Salazar — Head of UX/UI.

### EN.11.1 Mapa del flujo

```
Envíos › tab "Guías de rastreo"
│
├── LISTADO DE GUÍAS (827:69754)
│   Header "Envíos" + tabs + buscador + botón filtro
│   Tarjetas de guía: logo + carrier + tracking + chip estado
│                     + Fecha + Cliente (colapsable, chevron)
│   ├── Variante con filtros activos (827:72872): chips Envíos/Estado/Fecha/Cliente (contador + X)
│   └── tap en tarjeta → Detalle de guía
│
└── DETALLE DE GUÍA (471:57459) — pantalla completa
    Header "Detalles de guía" (back) + carrier + tracking + tipo servicio
    ├── INFO DE GUÍA: No. de pedido · Paquete · Fecha estimada de entrega · Última actualización
    ├── INFO DE DIRECCIÓN: Origen · Destino
    └── HISTORIAL DE ACTIVIDAD: timeline agrupado por día (Hoy / Ayer)
        cada evento: título + ubicación + chevron (expandible)
        último evento expandido → "Detalles de guía" + guía DHL + hora + "Ver / Imprimir guía"
```

### EN.11.2 Listado de guías — `827:69754`
Header **"Envíos"** + las 4 tabs (tab activa **"Guías de rastreo"**) + **buscador "Buscar"** (con `search-01`) + **botón de filtro** (40×40, a la derecha del buscador). Debajo, la lista de **tarjetas de guía**.

**Tarjeta de guía** (validada estructura, mismo patrón que la tarjeta de envío §EN.3 pero orientada a rastreo):
- **Fila superior:** logo del carrier (40, iso: `fedex-logo`/`dhl-iso`/`grupoAmPm`) + **nombre** (`B2 S`) + **número de tracking** ("43567890082", `B3` gris) + **chip de estado** (arriba-derecha).
- **Divisor** (`Line 711`).
- **Fila "Fecha":** ícono `calendar-02` + label "Fecha" + **"26 de enero - 2:24 hrs"**.
- **Divisor** (`Line 712`).
- **Fila "Cliente":** "Cliente:" + **"Javier Mena"** + **chevron** (`line-md:chevron-up`, colapsable — expande más info del cliente/envío).

**Estados de las tarjetas** (validado screenshot): el chip reutiliza el sistema de estados del envío (§EN.3): **Por recolectar** (gris), **Recolectado** (gris/amarillo), **En camino** (gris), **Entregados** (verde `#F0FDF4`/`#4FC153`, en **plural**), **Excepción de entrega** (5º estado, visto en el drawer). Cada carrier (FedEx/DHL/Grupo ampm) aparece con su iso.

### EN.11.3 Drawer de filtros — `827:72872` (validado screenshot)
El botón de filtro (junto al buscador) abre el **drawer "Filtrar"** (bottom sheet, mismo patrón transversal que Envíos §EN.2.7, Precios §PI.5b y Sucursales §PK.2.3b). Header **"Filtrar"** + **"Restablecer"**. Secciones en **acordeón colapsable** (chevron), cada una con **contador entre paréntesis** cuando tiene selección ("Paqueterías (1)", "Fecha (1)"):

- **Paqueterías** (checkboxes con logo): **FedEx · DHL · Grupo ampm · UPS · 99 Minutos**.
- **Estado** (checkboxes; "Por recolectar" seleccionado = check rojo): **Por recolectar · Recolectado · En camino · Entregados · Excepción de entrega**.
- **Fecha** (checkboxes): **Hoy · Últimos 7 días · Últimos 30 días · Fecha personalizada**.
- **Cliente**: buscador **"Buscar nombres"** + lista de clientes con checkbox (Joel Pérez · Miguel Hernandez · Mario Vasquez…).

**Footer fijo:** botón **"Mostrar resultados"** (rojo, ancho completo).

> ✅ **Es el mismo organismo de drawer de filtros** de toda la App — confirma el patrón transversal. Set de **Estado** completo aquí: incluye **"Excepción de entrega"** (no visto en el chip de la tarjeta) — es el 5º estado del envío.
> 🔴 Antes documenté esto como "chips activos en el listado"; el screenshot confirma que es el **drawer de filtros** con secciones-acordeón + contador, no chips.

### EN.11.4 Detalle de guía — `471:57459` (validado design context)
Pantalla completa. Header: **back** (`majesticons:arrow-up` rotado -90°) + título **"Detalles de guía"** (`T3 S` 16, centrado) + divisor. Contenido:

**Encabezado del carrier:** logo (40, r13) + **"FedEx: 77452320977452"** (`B1 S` 16) + **"Mismo día / 24H"** (`B2 R` 14, `#4C4C4C`) + **chip de estado** ("En camino", gris `#F3F3F3`/`#4B5563`) debajo del tipo de servicio.

**Bloque "INFO DE GUÍA"** (título en banda gris `#F8F8F8`, `Tag S` 10, `#6B7280`; filas separadas por `Line 719`):
| Campo | Valor |
|---|---|
| No. de pedido: | **774523209** |
| Paquete: | **1 pieza - 0.5 kg** |
| Fecha estimada de entrega | **9 de sep** |
| Última actualización: | **2 hrs** |

Cada fila: label izquierda (`B2 R`, negro) + valor derecha (`B2 S`, negro).

**Bloque "INFO DE DIRECCIÓN"** (banda gris, título `#9CA3AF`):
- **Origen:** (`B2 S`) → "Sucursal Polanco / Lago Zurich 234, C.P. 11530, Ampliación Granada, Polanco, Miguel Hidalgo, CDMX." (`B3 R`, `#4C4C4C`).
- **Destino:** → "Maria Fernanda Baz Carrillo / Sócrates 25, 55110, CDMX, México."

**Bloque "HISTORIAL DE ACTIVIDAD"** — el **timeline de rastreo**, agrupado por día con una **línea vertical conectora** (`Line 724`) a la izquierda:
- **Chip de día** (fondo `#F3F3F3` r6, texto `#4B5563` `B3 M`): **"Hoy"** / **"Ayer"**.
- Bajo cada chip, los **eventos** de ese día. Cada evento: **nodo** (cuadro gris `#F8F8F8` redondeado 40×40 con **punto negro relleno** al centro, sobre la línea) + **título** (`B2 M` 14, negro) + **chevron** (`line-md:chevron-up`, expandible) + **ubicación/fuente** (`B2 R` 14, `#4C4C4C`).

**Eventos del ejemplo** (de más reciente a más antiguo):
| Día | Evento | Ubicación/Fuente |
|---|---|---|
| **Hoy** | El envío salió de una sucursal DHL | Ciudad de México, México |
| **Hoy** | Procesado en el hub de Ciudad de México, México | Ciudad de México, México |
| **Ayer** | El envío salió de una sucursal DHL | Querétaro, México |
| **Ayer** | Envío procesado en Querétaro, México | Querétaro, México |
| **Ayer** | Envío recolectado | Guadalajara, Jalisco |
| **Ayer** | Información de envío recibida | T1envíos System |

**Evento expandido** (último, "Información de envío recibida"): al expandir muestra un sub-bloque **"Detalles de guía"** con:
- Ícono **`cbi:dhl`** + número de guía **"3245456435434324"** (`B2 M`).
- **"17:34 hrs"** (`B2 R`, `#4C4C4C`).
- **"Ver / Imprimir guía"** (`B2 S` 14, negro, **subrayado** — enlace a la guía PDF).

> ✅ **Cierra el ciclo de rastreo:** el historial de actividad muestra el recorrido físico completo del paquete (recolección → hubs → sucursales → salida a entrega) con ubicación por evento, agrupado por día. Cada evento es expandible; el evento raíz enlaza a **"Ver / Imprimir guía"**. Es la vista granular que complementa el timeline resumido de Envíos (§EN.8) — ese es del pedido, este es de la paquetería.
> ✅ **"T1envíos System"** como fuente del primer evento — marca el origen del tracking dentro de la plataforma, antes de que el carrier tome el paquete.

### EN.11.5 Componentes nuevos
- **Tarjeta de guía de rastreo** (logo + carrier + tracking + chip estado + Fecha + Cliente colapsable) — §EN.11.2.
- **Chips de filtro activos** (contador + X) — §EN.11.3.
- **Bloques de info con banda gris** (INFO DE GUÍA / INFO DE DIRECCIÓN) — §EN.11.4.
- **Timeline de historial de actividad** (agrupado por día, eventos expandibles, línea conectora) — §EN.11.4.
- **Evento expandido con "Ver / Imprimir guía"** — §EN.11.4.

### EN.11.6 Pendientes (🔴)
2. 🔴 **"INFO DE GUÍA" usa `#6B7280`** pero "INFO DE DIRECCIÓN"/"HISTORIAL" usan `#9CA3AF` — mismo estilo de banda, dos grises distintos. Unificar el token del título de banda (§EN.11.4).
3b. ✅ **Corregido (screenshot):** el botón de filtro abre el **drawer "Filtrar"** (no chips en el listado); estado "Entregados" en plural; chip de estado también en el encabezado del detalle; nodo del timeline = punto negro en cuadro gris (§EN.11.3/§EN.11.4).
4. ⚠️ **Los eventos son todos colapsables (chevron)** pero solo se documenta un estado expandido — confirmar qué muestra cada evento al expandir (§EN.11.4).

### EN.11.8 Referencias
- *Tracking Guides* (`470:45363`).
- **Listado:** `827:69754`. **Con filtros activos:** `827:72872` (chips `827:73169`/`827:73174`/`827:73179`/`827:73184`).
- **Detalle de guía:** `471:57459` (versión completa) / `471:56728` (versión corta). INFO DE GUÍA `471:57473` · INFO DE DIRECCIÓN `471:57493` · HISTORIAL `471:57505` · evento expandido `471:57615` · Ver/Imprimir guía `471:57624`.
- **Estados vacíos/lazy:** `827:71116` / `827:71419` (frames sin contenido).

---

## EN.12 Recolecciones — programar recolección (§EN, tab "Recolecciones")

> **Sección "Pick-up"** (`483:15741`). El flujo de **recolecciones**: se accede desde la **tab "Recolecciones"** del listado de Envíos (§EN.2.1) — resuelve el último pendiente de las 4 tabs. Permite **programar que la paquetería pase por los paquetes** al domicilio/almacén, en vez de llevarlos a sucursal. Tiene un **listado de recolecciones** y un **wizard de creación** (acordeón de 4 secciones) que cierra con una pantalla de éxito.
> **Figma:** `483:15741`. **Owner:** Karla Salazar — Head of UX/UI.

### EN.12.1 Mapa del flujo

```
Envíos › tab "Recolecciones"
│
├── LISTADO DE RECOLECCIONES (827:73506)
│   Header "Envíos" + tabs + buscador + 2 botones (filtro + more)
│   Tarjetas: logo carrier + tracking + more-horizontal
│             + Fecha programada + Paquetes + Dirección
│   ├── Vacío A (827:74046): "Aún no tienes recolecciones programadas"
│   └── Vacío B (827:74682): "Aún no tienes envíos" (necesitas envíos primero)
│
├── CREAR RECOLECCIÓN — wizard acordeón (4199:81107 → …)
│   1. Dirección de recolección (Selecciona/Editar + form)
│   2. Elige la paquetería (Seleccionar paquetería)
│   3. Programar la recolección (Fecha + Horario)
│   4. Detalles del paquete (Número de paquetes + dimensiones)
│   → Crear recolección
│
└── ÉXITO (487:81431)
    "¡Tu recolección fue creada con éxito!" + resumen + advertencia de presencia
```

### EN.12.2 Listado de recolecciones — `827:73506` (validado design context)
Header **"Envíos"** + las 4 tabs (activa **"Recolecciones"**) + buscador **"Buscar"** + **dos botones** a la derecha (`filter-horizontal` = filtro/orden, `more-vertical` = más acciones). Debajo, la lista de **tarjetas de recolección**.

**Tarjeta de recolección** (card blanco r12, borde `#F3F3F3`, 242h):
- **Fila superior:** logo carrier (40, iso: `fedex-logo`/`dhl-iso`/`99min-iso`) + nombre (`B2 S`) + tracking ("43567890082", `B3 R` gris) + **`more-horizontal`** (rotado 90°, menú de acciones).
- **Divisor** (`Line 711`).
- **Fila "Fecha programada":** ícono `calendar-02` + label + **"26 de enero / 8:00 - 10:00 AM"** (`B2 M`, dos líneas — el día y la **ventana horaria**).
- **Fila "Paquetes":** ícono `package` + label + **"12"** (`B2 M`).
- **Divisor.**
- **Dirección:** **"Dirección: Lago Zurich 25, C.P. 55110, Ampliación Granada, CDMX, México."** (`B3 S`).

Cada carrier aparece con su iso (FedEx, DHL, 99 Minutos en el ejemplo). La **ventana horaria** ("8:00 - 10:00 AM") es lo que distingue la recolección del envío: no es una fecha de entrega, es el rango en que pasará el mensajero.

### EN.12.3 Estados vacíos
Dos estados vacíos distintos:
- **Sin recolecciones** (`827:74046`): **"Aún no tienes recolecciones programadas"** + *"Programa y administra la recolección de tus paquetes."*
- **Sin envíos** (`827:74682`): **"Aún no tienes envíos"** + *"Para solicitar una recolección, primero necesitas crear envíos."* — **dependencia dura:** no puedes programar una recolección sin envíos creados. La recolección recoge envíos existentes.

> ✅ **La recolección depende de envíos previos:** el estado vacío B lo hace explícito — primero se crean los envíos (§EN.9), luego se programa que los recojan. Es un paso posterior en el ciclo logístico.

### EN.12.4 Wizard de crear recolección — acordeón de 4 secciones (validado screenshot)
Header **"Crear recolección"** (back). Wizard tipo **acordeón** de 4 secciones que se completan en orden. Cada sección tiene:
- **Ícono circular gris** con el ícono real de cada sección: **`checkmark-circle-02`** (dirección, ya viene con estrella) / **`building-05`** (paquetería) / **`calendar-02`** (programar) / **`package-moving`** (detalles).
- **Título** (`B2 S`) + **descripción** (`B3 R` gris).
- **"Editar"** a la derecha (aparece cuando la sección tiene contenido o está activa).
- **Estados visuales:** sección **activa** = ícono/textos en negro pleno + input visible; secciones **pendientes** = todo **atenuado** (gris claro); sección **completada** = **colapsa** (oculta descripción e input) mostrando solo el valor elegido, y el ícono se vuelve **`checkmark-circle-02`** (círculo verde con palomita, `#4FC153`/`#F0FDF4`).

El botón **"Crear recolección"** (footer) está **deshabilitado** (rojo atenuado) hasta completar las 4 secciones — mismo patrón que Cotizar (§EN.10).

**1. Dirección de recolección** (`4199:81107`):
- Descripción *"Selecciona o agrega una nueva dirección."* + **"Editar"**.
- **Dropdown "Selecciona"** (chevron). Debajo, la dirección + contacto elegidos ("Avenida Francisco I. Madero, 140, 18, Centro, Ciudad de México, CDMX" / "Fabian Hernandez Hernández • 55 1234 5678").
- **Dropdown abierto** (`4200:82230`, validado): **badge estrella amarillo** (`Yellow/300` — dirección predeterminada/favorita) + buscador **"Buscar por nombre del lugar o dirección"** + **lista de almacenes/sucursales** (Almacén CDMX · Almacén Norte · Almacén Monterrey · Sucursal Polanco · Almacén central) + **"+ Agregar nueva dirección"**.
- **Completada** (validado): ícono **check verde** + **"Almacén CDMX"** con **estrella amarilla** (predeterminada) + dirección + contacto.
- **Agregar dirección** (`827:78732`, validado design context + screenshots): pantalla completa **"Agregar dirección"**. Es el **cuarto lugar** donde aparece este form (origen §EN.9.3, destino §EN.9.4, Sucursales §PK.3) — aquí queda **completamente especificado**:
  - **Datos de contacto:** Nombre del lugar ("Ej. Bodega Central") · Nombre de contacto ("Ej. Juan Pérez") · Correo electrónico ("ej. jamesjones@gmail.com") · **Número de teléfono** (con **selector de país con bandera** — placeholder "+90 (124) 111 222 33" 🔴 default Turquía) · Empresa (opcional) ("ej. Commer 101").
  - **Sección colapsable "DIRECCIÓN"** (chevron): Calle · Número exterior ("ej. 140") · Número interior (opcional) ("ej. Depto 5A") · Código postal ("ej. 06000") · **Colonia** (dropdown) · Estado · Ciudad · **Referencia** (textarea multilínea).
  - **Autocompletado de Calle** (`827:79630`, validado): al escribir sugiere direcciones (Av. Prado Norte / Av. Presidente Masaryk / Av. Francisco I. Madero / Av. Constituyentes…) + **"Ingresar manualmente"** al pie. Autocompletado de direcciones tipo Google Places.
  - **Dos checkboxes:** *"Establecer como dirección predeterminada para mis envíos."* + *"Establecer como dirección de devolución."*
  - **Footer:** **"Cancelar"** (blanco) + **"Guardar"** (rojo, deshabilitado hasta llenar los requeridos → habilitado con datos completos).

> 🔴 **Selector de teléfono default Turquía (+90):** el placeholder muestra bandera y código de Turquía en una app **mexicana** — debería ser México (+52). Bug de configuración del componente de teléfono (mismo componente que reaparece en todos los forms de contacto).
> ✅ **Autocompletado de direcciones:** el campo Calle sugiere direcciones reales mientras escribes, con escape "Ingresar manualmente". Reduce errores de captura — documentar la fuente (Google Places o similar).
> 🔴 **Este es el form de dirección MX definitivo** — con contacto + teléfono internacional + DIRECCIÓN colapsable + autocompletado + 2 flags (predeterminada/devolución). Al aparecer por 4ª vez, unificarlo como **un solo componente** es deuda urgente.

**2. Elige la paquetería** (`487:81538`, validado design context):
- Ícono **`building-05`** + descripción *"Compara las opciones disponibles para tu ubicación"* + **"Editar"**.
- **Dropdown "Seleccionar paquetería"** (`arrow-down-01-sharp`). Se activa (negro) al completar la sección 1.
- **Dropdown abierto** (`4200:81710`, validado): lista de paqueterías, cada opción con **logo (30) + nombre + horario de atención en dos líneas** + `tick-02` (selección):
  | Carrier | Horario |
  |---|---|
  | **DHL** | Lun-Vie: 9:00-20:00 / Sábado: 9:00-14:00 |
  | **FedEx** | Lun-Vie: 9:00-20:00 / Sábado: 9:00-14:00 |
  | **UPS** | Lun-Vie: 9:00-20:00 / Sábado: 9:00-14:00 |
  | **Ampm** | Lun-Vie: 9:00-20:00 / Sábado: 9:00-14:00 |
- **Completado** (validado): la sección **colapsa** — ícono se vuelve **`checkmark-circle-02`** (check verde) y muestra solo **logo (30) + "FedEx"** (sin la descripción). El resto de secciones pendientes siguen atenuadas.

> ✅ **El dropdown de paquetería muestra el horario de atención** de cada carrier (Lun-Vie / Sábado) — relevante porque la recolección debe caer dentro de esos horarios. No es solo elegir carrier, es ver su ventana de operación.

**Estado de error — recolección no disponible** (`827:75857` / `827:80120`, validado screenshot): si la ubicación no tiene servicio de recolección, la sección 2 muestra un **componente Messages en advertencia** (amarillo/café): *"Recolección no disponible en esta ubicación. Lleva tus paquetes a la sucursal más cercana."* El dropdown de paquetería queda con la opción elegida (DHL) pero el botón "Crear recolección" **deshabilitado** (gris). Es la ruta de fallo: no todas las direcciones admiten recolección, y el copy redirige a llevar a sucursal.

> ✅ **Fallback de cobertura:** la recolección no está disponible en todas las ubicaciones. Cuando falla, el sistema lo comunica con un Messages de advertencia y **redirige a la sucursal más cercana** (conecta con el modal de Sucursales §EN.9.8.1). Es un buen manejo del caso sin cobertura.

**3. Programar la recolección** (`487:81539`, validado design context + screenshots):
- Ícono **`calendar-02`** + descripción *"Elige el día y la hora en que pasarán por tus paquetes"* + **"Editar"**.
- **Fecha de recolección** (dropdown "Selecciona el día de recolección"). **Abierto** (`4200:82598`): lista de **días hábiles predefinidos** — "Mañana, 8 de octubre" / "Jueves, 9 de octubre" / "Viernes, 10 de octubre" / "Lunes, 12 de octubre" / "Martes, 13 de octubre" + **"+ Seleccionar del calendario"** (en **rojo**, abre un date picker completo).
- **Horario de recolección** (dropdown "Seleccionar horario"). **Atenuado/deshabilitado hasta elegir la fecha** (dependencia entre campos). **Abierto** (`4201:83127`): ventanas de **3 horas con incrementos de 1 hora** — "9:00 - 12:00 hrs" / "10:00 - 13:00 hrs" / "11:00 - 14:00 hrs" / "12:00 - 15:00 hrs" / "13:00 - 16:00 hrs" / "14:00 - 17:00 hrs" / "15:00 - 18:00 hrs".
- **Completada** (`4201:83730`, validado): colapsa a **"Mañana, 8 de octubre | 10:00 - 13:00"** con check verde + sub-label **"Dirección de origen"**.

> ✅ **Fecha con días hábiles predefinidos + calendario:** el dropdown ofrece los próximos días laborables (salta fin de semana: de "Viernes 10" a "Lunes 12") como atajo, más "Seleccionar del calendario" para cualquier fecha. Los sábados/domingos no aparecen en la lista rápida.
> ✅ **Ventanas horarias de 3h, deslizantes cada hora:** los horarios son rangos de 3 horas que avanzan de hora en hora (9-12, 10-13, 11-14…hasta 15-18). Cubren el horario laboral del carrier (§EN.12.4, paso 2).
> ✅ **Dependencia fecha → horario:** el selector de horario permanece deshabilitado hasta elegir el día — no puedes elegir horario sin fecha.

**4. Detalles del paquete** (`4201:83693`, validado design context + screenshot):
- Ícono **`package-moving`** + descripción *"Indica cuántos paquetes recolectaremos y sus dimensiones"* + **"Editar"**.
- **Componente Messages informativo** (`4201:83751`, banner azul): *"Ingresa las dimensiones y el peso promedio si los paquetes son diferentes."* — instrucción para cuando el lote de paquetes no es homogéneo.
- **Número de paquetes** ("Ej. 12").
- **Grilla 2×2 de dimensiones:** **Largo (cm)** "Ej. 10" / **Ancho (cm)** "ej. 15" / **Alto (cm)** "ej. 25" / **Peso (kg)** "ej. 1" — mismas dimensiones que Crear envío/Cotizar, pero aquí son el **promedio** del lote a recolectar.
- Cuando la sección 3 (Programar) se completa, aparece el sub-label **"Dirección de origen"** sobre esta sección — encabezado que agrupa los detalles del paquete bajo la dirección de origen ya elegida.

> ✅ **Peso/dimensiones promedio para lotes heterogéneos:** el banner informativo aclara que si los paquetes son distintos, se ingresa el promedio. La recolección trata el lote como un conjunto, no paquete por paquete (a diferencia de Crear envío, que es por envío).

**Validación de campos obligatorios** (`4205:92465`, validado screenshot): si se intenta continuar sin llenar las dimensiones, los inputs Largo/Ancho/Alto/Peso pasan a **estado de error** (borde rojo) con el texto **"Campo obligatorio"** (`Hint` bajo cada campo, en rojo). Las 4 dimensiones son obligatorias.

**Detalles del paquete completado** (validado screenshot): la sección colapsa a un resumen inline: **"Número de paquetes: 12 | Largo: 23 cm | Alto: 45 cm | Ancho: 33 cm | Peso: 2 kg"** (`B3 R` gris). Con las 4 secciones completas, el botón **"Crear recolección" se habilita** (rojo pleno `#DB3B2B`).

> ✅ **Wizard acordeón (no pasos numerados):** a diferencia de Crear envío (§EN.9, PASO N/3) y Cotizar, la recolección usa un **acordeón** de secciones con **ícono + Editar**, no un badge numerado. Cada sección progresa: **atenuada** (pendiente) → **activa** (negro) → **check verde** (completada). El botón se habilita solo al completar todo.
> ✅ **Selección de dirección con favorita:** el dropdown de dirección marca la **predeterminada con estrella amarilla** (`Yellow/300`) y permite buscar entre almacenes/sucursales o agregar una nueva. Conecta con Sucursales (§PK) — las direcciones son las sucursales/almacenes del negocio.

### EN.12.5 Éxito — `487:81431` (validado design context)
**X para cerrar** (`cancel-01`) arriba-derecha. Contenido centrado:
- **Ícono de éxito:** círculo verde `#F0FDF4` (Green/500) + `tick-02` verde `#4FC153` (Green/300), 72px.
- **Título "¡Tu recolección fue creada con éxito!"** (`T2 S` 20, centrado).

**Card de resumen** (fondo gris `#F8F8F8` r16, sub-cards blancas dentro):
- **Encabezado:** logo carrier (**DHL**, 40) + nombre + guía ("3456788909765445676") + **"12 paquetes"** (`B3 M`, derecha). Divisor.
- **Sub-card "Fecha de recolección"** (blanca r12, ícono `calendar-minus-02`): **"Mañana, 8 de octubre"** + **"10:00 - 13:00"** (`B3 R` gris).
- **Sub-card "Lugar de recolección"** (blanca r12, ícono `location-05`): **"Almacén CDMX"** + "Lago Zurich 25, C.P. 55110, Ampliación Granada, CDMX, México."
- **Botón "Ir a recolecciones"** (`#DB3B2B`, r8, dentro de la card) — lleva al listado de recolecciones (§EN.12.2).

**Sección "¿Cómo preparo mi recolección?"** (`T3 S` 16) con 2 bullets (`B2 R` 14, ambos en **negro**):
- *"Empaca y ten tus envíos listos al menos 30 minutos antes de la hora de recolección."*
- **Política de ausencia:** *"Es indispensable que estés presente al momento de la recolección. Tu ausencia generará un reporte y podría impedirte solicitar recolecciones en el futuro."*

> ✅ **Advertencia con peso informativo alto:** la pantalla de éxito advierte que no estar presente genera un reporte y puede bloquear futuras recolecciones. En Figma va en negro como el otro bullet, no destacada en rojo — considerar darle más peso visual (color/ícono de advertencia) dado su impacto para el usuario.

### EN.12.5b Cancelar recolección (validado screenshot)
Desde el **menú de la tarjeta** de recolección (ícono `more`, 3 puntos):
- **Popover de acciones** (`827:75467`): opción **"Cancelar recolección"** (con ícono **X en círculo**, `cancel-01`).
- Al tocarla → **modal destructivo** (patrón transversal de la App): círculo **rojo suave** `#FFF0EF` + ícono **X** rojo + título **"Cancelar recolección"** (`T2 S`) + cuerpo *"Esta acción no se puede deshacer, tu recolección será cancelada permanentemente. ¿Estás seguro de que quieres cancelar?"* + **botones lado a lado**: **"Cancelar"** (blanco) + **"Sí, cancelar"** (rojo).

**Menú "more-vertical" del header** (`4199:78034`): despliega **"Crear recolección"** (con `plus-sign`) — acceso alterno a crear, además del botón del estado vacío.

**Drawer de filtros aplicados** (validado screenshot `4199:78033`): tras aplicar filtros, aparecen **chips activos** bajo el buscador — **Fecha (1)** · **Origen (1)** (contador negro + X para quitar). El botón `filter-horizontal` abre el drawer de filtros; estos chips reflejan lo aplicado.

> ✅ **Modal destructivo reutiliza el patrón de la App** (círculo rojo suave + X + T2 + "Cancelar"/"Sí, cancelar"), el mismo de eliminar catálogo (§PJ) y otros destructivos. La cancelación es **permanente e irreversible** — coherente con la política de ausencia (§EN.12.5): las recolecciones son compromisos con la paquetería.

### EN.12.6 Componentes nuevos
- **Tarjeta de recolección** (logo + tracking + fecha programada con ventana horaria + paquetes + dirección) — §EN.12.2.
- **Dos estados vacíos** (sin recolecciones / sin envíos, con dependencia) — §EN.12.3.
- **Wizard acordeón de 4 secciones** (dirección/paquetería/programación/detalles) — §EN.12.4.
- **Selector de fecha + ventana horaria de recolección** — §EN.12.4.
- **Sección de acordeón con ícono + Editar + estados (atenuado/activo/check)** — §EN.12.4.
- **Dropdown de dirección con favorita (estrella) + buscador + lista** — §EN.12.4.
- **Menú de tarjeta "Cancelar recolección" + modal destructivo** — §EN.12.5b.
- **Chips de filtro aplicados** (Fecha/Origen, contador + X) — §EN.12.5b.
- **Pantalla de éxito con política de ausencia** — §EN.12.5.

### EN.12.7 Pendientes (🔴)
1. 🔴 **Form de dirección MX — cuarta aparición** (§EN.12.4): origen §EN.9.3, destino §EN.9.4, Sucursales §PK.3, recolección aquí. Unificar como componente único es cada vez más urgente.
2. 🔴 **Peso visual de la advertencia de ausencia** — el mensaje de consecuencia ("generará un reporte y podría impedirte solicitar recolecciones") va en el mismo estilo que el resto del texto; evaluar si merece un tratamiento visual de advertencia (§EN.12.5).
3. ⚠️ **Ventana horaria** ("8:00 - 10:00 AM" / "10:00 - 13:00") — documentar los rangos disponibles y de dónde salen (por paquetería/zona) (§EN.12.4).
4. ✅ **Validado (screenshots):** wizard con ícono+Editar (no badge numerado), estados atenuado/activo/check verde (`checkmark-circle-02`), completada **colapsa** a solo el valor; botón deshabilitado hasta completar; dropdown de dirección con estrella de favorita + lista de almacenes; dropdown de paquetería con **horario de atención** (Lun-Vie/Sábado); cancelación con modal destructivo permanente; chips de filtro Fecha/Origen (§EN.12.4/§EN.12.5b).
5. ✅ **Paso 3 validado:** fecha con días hábiles predefinidos + "Seleccionar del calendario" (rojo); horario en ventanas de 3h deslizantes cada hora (9-12…15-18); dependencia fecha→horario; completada colapsa a "día | rango" + sub-label "Dirección de origen" (§EN.12.4).
6. ✅ **Paso 4 validado:** componente **Messages informativo** azul ("peso promedio si los paquetes son diferentes") + Número de paquetes + grilla Largo/Ancho/Alto/Peso (promedio del lote). **Campos obligatorios** con error "Campo obligatorio" (borde rojo) (§EN.12.4).
7. 🔴 **Selector de teléfono default Turquía (+90)** en Agregar dirección — debería ser México (+52). Bug del componente de teléfono (§EN.12.4).
8. ✅ **Autocompletado de Calle** (sugerencias + "Ingresar manualmente") — documentar fuente (Google Places) (§EN.12.4).
9. ✅ **Fallback sin cobertura:** Messages de advertencia "Recolección no disponible… Lleva tus paquetes a la sucursal más cercana" cuando la ubicación no admite recolección (§EN.12.4).

### EN.12.9 Referencias
- *Pick-up* (`483:15741`).
- **Listado:** `827:73506` / `827:75467` / `1810:20272`. **Vacíos:** sin recolecciones `827:74046` · sin envíos `827:74682`.
- **Wizard:** dirección `4199:81107` · paquetería `486:79592` · programar `486:79435`/`4200:82230` · detalles `4201:83693`/`4205:92465` · agregar dirección `827:78732`.
- **Éxito:** `487:81431`.

---

## CE Configuración de envíos — Reglas de prioridad (§CE)

> **Sección "Configuracion prioridad"** (`5183:168845`). Área nueva de **configuración del módulo de Envíos**, a la que se accede desde el **ícono de engrane** (`setting-02`) en el header de Envíos. Agrupa tres ajustes: **Plantillas**, **Direcciones de origen** y **Reglas de prioridad**. Esta entrada documenta el flujo completo de **Reglas de prioridad** (cómo el sistema elige qué paquetería usar), validado con screenshots.
> **Figma:** `5183:168845`. **Owner:** Karla Salazar — Head of UX/UI.

### CE.1 Mapa del flujo

```
Envíos (header con ⚙ setting-02)
│
├── ⚙ → CONFIGURACIÓN DE ENVÍOS (menú)
│   ├── Plantillas            (nota)      → [pendiente documentar]
│   ├── Direcciones de origen (camión)    → [pendiente documentar]
│   └── Reglas de prioridad   (sort)      → §CE.3
│
└── REGLAS DE PRIORIDAD (5184:53889+)
    ├── Card regla activa + "Cambiar"
    ├── Lista de paqueterías (chip Activa)
    │
    ├── Modal "Regla de prioridad" (5184:54323) — 4 opciones:
    │   ├── Prioridad T1     (logo T1)          "Eligiremos la mejor opción para ti"
    │   ├── Por prioridad    (sort-by-down-01)  "Tú eliges el orden de las paqueterías"
    │   ├── Más económico    (dollar-receive-02)"Se elige la tarifa más baja"
    │   └── Más rápido       (timer-02)         "Se prioriza el menor tiempo de entrega"
    │
    └── Estados por modo:
        ├── Prioridad T1 / Por prioridad → card + LISTA de paqueterías
        │   └── Por prioridad: con handle drag-and-drop (reordenable)
        └── Más económico / Más rápido   → solo card (sin lista)
```

### CE.2 Acceso — engrane + tab "Plantillas" nueva
En el **header de Envíos** (`5183:169196`) aparece el título "Envíos" + **ícono de engrane `setting-02`** (arriba-derecha) que abre **Configuración de envíos**. Además, el tab bar de Envíos ahora incluye una **tab "Plantillas"** nueva (`5183:171505`) junto a Cotizar / Mis envíos / Guías de rastreo / Recolecciones.

> 🔴 **Tab bar de Envíos desordenado en Figma** (`5183:169206`): la metadata muestra tabs duplicados y stale ("Guias de rastreo" sin tilde, "Guías de rastreo" repetida) mezclados con las posiciones reales. El set correcto de tabs es: **Cotizar · Mis envíos · Guías de rastreo · Recolecciones · Plantillas**. Confirmar el orden final y limpiar los frames duplicados.

### CE.3 Configuración de envíos (menú) — validado screenshot
Pantalla **"Configuración de envíos"** (back). Tres filas de menú (ícono + label + chevron `>`):
- **Plantillas** (ícono nota `sticky-note`).
- **Direcciones de origen** (ícono camión `truck`).
- **Reglas de prioridad** (ícono `sort-by-down`).

Cada fila navega a su submódulo. (Variante con tabs `5184:54111`: "Plantillas / Dirección de origen / Prioridad de paqueteria" — hay dos patrones de navegación posibles para esta config: **menú de filas** vs **tabs**. Confirmar cuál es el definitivo.)

> 🔴 **Dos patrones de navegación para la config:** el screenshot muestra un **menú de filas** (Plantillas / Direcciones de origen / Reglas de prioridad); la metadata de la variante con **tabs** muestra ("Plantillas / Dirección de origen / Prioridad de paqueteria"). Además "Direcciones de origen" (plural, menú) vs "Dirección de origen" (singular, tabs) y "Reglas de prioridad" vs "Prioridad de paqueteria". Unificar nomenclatura y patrón.

### CE.4 Reglas de prioridad — listado — `5184:53889` (validado screenshot)
Header **"Reglas de prioridad"** (back). Estructura:

**Card superior = regla activa** (`5184:53889`): ícono de la regla + **nombre** (`B1 S`) + **descripción** (`B3 R` gris) + **"Cambiar"** (a la derecha, abre el modal de selección). En el ejemplo: **Prioridad T1** (ícono **`t1-logotipo-2`** + flecha `sort-by-down-01`) / "Eligiremos la mejor opción para ti".

**Lista de paqueterías** debajo (solo en modos Prioridad T1 / Por prioridad): cada tarjeta con logo (40) + nombre + **tipo de servicio** + **chip de estado**:
| Paquetería | Servicio | Chip |
|---|---|---|
| **DHL** | Día siguiente | Activa (verde) |
| **DHL** | Económico / Dos días | Activa |
| **FedEx** | Mismo día / 24H /SO24NRS | Activa |
| **FedEx** | Económico / Día siguiente / semanal/XS-ECONOMY | Activa |
| **Grupo ampm** | Día siguiente | Activa (en screenshot img3 aparece "Recolectado" 🔴 — chip stale) |

Cada fila es una **combinación paquetería + servicio** (no solo el carrier): DHL aparece dos veces (Día siguiente / Económico), FedEx dos veces (Mismo día / Económico). El chip **"Activa"** (verde `#F0FDF4`) indica que esa combinación participa en la selección automática.

### CE.5 Modal de selección "Regla de prioridad" — `5184:54323` (validado screenshot)
Al tocar **"Cambiar"** se abre un **bottom sheet** "Regla de prioridad":
- Título **"Regla de prioridad"** + botón (`5184:54325`) + descripción *"Selecciona la regla para determinar la paquetería que predominará"*.
- **4 opciones** (cada una card con ícono + título + descripción):

| Regla | Ícono | Descripción |
|---|---|---|
| **Prioridad T1** | `t1-logotipo-2` (marca T1) | Eligiremos la mejor opción para ti |
| **Por prioridad** | `sort-by-down-01` | Tú eliges el orden de las paqueterías |
| **Más económico** | `dollar-receive-02` | Se elige la tarifa más baja |
| **Más rápido** | `timer-02` | Se prioriza el menor tiempo de entrega |

> ✅ **Cuatro estrategias de selección automática de paquetería:** T1 decide (recomendado) · el usuario ordena manualmente (Por prioridad) · optimiza costo (Más económico) · optimiza tiempo (Más rápido). Es la lógica que resuelve qué carrier se usa cuando hay varios disponibles — clave para el negocio.

### CE.6 Modo "Por prioridad" (drag-and-drop) — `5184:104316` (validado screenshot)
Cuando la regla activa es **"Por prioridad"**, la card superior muestra "Por prioridad / Tu eliges el orden de las paqueterías" + "Cambiar", y la lista de paqueterías gana un **handle de arrastre** (`vertical-drag-&-drop`, ícono de 6 puntos a la izquierda de cada fila) para **reordenar manualmente** por drag-and-drop. El orden de la lista = la prioridad con que se intenta cada paquetería. Todas las filas conservan su chip "Activa".

> ✅ **Reordenamiento por drag-and-drop:** único modo donde el usuario controla el orden de preferencia arrastrando. Los demás modos (T1/económico/rápido) calculan el orden automáticamente y no muestran handle.

### CE.7 Modos "Más económico" y "Más rápido" (colapsados) — `5188:144741` / `5188:145057` (validado screenshot)
Cuando la regla activa es **"Más económico"** (`5188:144741`) o **"Más rápido"** (`5188:145057`), la pantalla muestra **solo la card superior** (ícono + nombre + descripción + "Cambiar"), **sin lista de paqueterías reordenables** — el criterio (tarifa más baja / menor tiempo) se aplica automáticamente sobre todas las opciones disponibles, así que no hay orden manual que mostrar.

> ✅ **Diferencia estructural por modo:** Prioridad T1 y Por prioridad muestran la lista de combinaciones paquetería+servicio; Más económico y Más rápido solo muestran la card de la regla (el sistema decide sin intervención). Es coherente: solo tiene sentido ver/ordenar la lista cuando el modo depende de ella.

### CE.8 Componentes nuevos
- **Header de Envíos con engrane** (`setting-02`) → Configuración de envíos — §CE.2.
- **Tab "Plantillas"** nueva en el tab bar de Envíos — §CE.2.
- **Menú Configuración de envíos** (Plantillas / Direcciones de origen / Reglas de prioridad) — §CE.3.
- **Card de regla activa + "Cambiar"** — §CE.4.
- **Fila paquetería+servicio con chip de estado** — §CE.4.
- **Modal de selección de regla** (4 estrategias) — §CE.5.
- **Lista reordenable con handle drag-and-drop** (`vertical-drag-&-drop`) — §CE.6.
- **Íconos nuevos:** `setting-02`, `sort-by-down-01`, `dollar-receive-02`, `timer-02`, `vertical-drag-&-drop`, `t1-logotipo-2`.

### CE.9 Pendientes (🔴)
1. 🔴 **Plantillas** y **Direcciones de origen** son áreas nuevas del menú **aún sin documentar** — cobertura faltante (§CE.3).
2. 🔴 **Dos patrones de navegación** para la config (menú de filas vs tabs `5184:54111`) + nomenclatura divergente ("Direcciones de origen" vs "Dirección de origen"; "Reglas de prioridad" vs "Prioridad de paqueteria"). Unificar (§CE.3).
3. 🔴 **Tab bar de Envíos con frames duplicados/stale** ("Guias de rastreo" sin tilde repetida). Limpiar y confirmar orden final con "Plantillas" (§CE.2).
4. 🔴 **Chip "Recolectado" en Grupo ampm** (screenshot img3) donde el resto dice "Activa" — parece stale; el set de chips de esta lista debería ser solo estado de la regla (Activa/Inactiva), no estados de envío (§CE.4).
5. ⚠️ **Combinación paquetería+servicio** como unidad: documentar de dónde salen los servicios (Día siguiente / Económico / Mismo día / XS-ECONOMY…) y cómo se activan/desactivan individualmente (§CE.4).

### CE.11 Referencias
- *Configuracion prioridad* (`5183:168845`).
- **Header con engrane:** `5183:169196` (`setting-02` `5184:53834`). **Tab Plantillas:** `5183:171505`.
- **Config menú (tabs):** `5184:54111`. **Reglas listado (T1):** `5184:53889`. **Modal selección:** `5184:54323`.
- **Por prioridad (drag):** `5184:104316` (`vertical-drag-&-drop`). **Más económico:** `5188:144741`. **Más rápido:** `5188:145057`.

---

## CC Control de calidad — Gestión de incidencias (base) (§CC)

> **Módulo "Incident Management"** (`947:60630`). Área grande de **Control de calidad**, accesible desde el menú **"Más"** (sección OTROS). Tiene dos tabs: **Gestión de incidencias** y **Sobrepesos**. Una **incidencia** es un problema en la entrega de un envío (dirección incorrecta, acceso restringido, paquete dañado…) que requiere seguimiento y una acción de resolución.
> Esta entrada documenta **la base**: acceso, estado vacío, KPIs, listado, sistema de estados, filtros y detalle. **Pendientes para siguientes partes:** tab Sobrepesos, flujo de reportar incidencia, y los flujos de acción (Cambiar dirección, Enviar a sucursal, Retornar al origen, Reprogramar entrega, Recolección en sucursal, Solicitar búsqueda, Intentar nueva entrega, Agregar detalles de acceso).
> **Figma:** `947:60630`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.1 Mapa del flujo (base)

```
Más › OTROS › Control de calidad
│
├── Tabs: [Gestión de incidencias] · [Sobrepesos → pendiente]
│
├── ESTADO VACÍO (852:48784): ilustración + "Sin incidencias" + "Reportar incidencia"
│
└── LISTADO CON DATOS (4205:109247)
    ├── KPIs: "Requiere acción 04 +12%" · "Tasa de incidencias 1.02% +2.1%"
    ├── Buscador ("Busca por código, nombre, SKU…") + filtro + more-vertical
    │   └── more-vertical → "Reportar incidencia"
    ├── Tarjetas de incidencia (INC-XXXXX)
    │   INC + chip estado · Guía · Estado del envío · Solución estimada · Fecha
    │
    ├── DRAWER DE FILTROS (Filtrar): Ordenar por / Paquetería / Fecha / Estado incidencia / Estado del envío
    │   └── colapsado: chips activos (Entrega de paquete, Fecha, Estado…)
    │
    └── DETALLE (4206:37050): Estado / Situación / DETALLE DE ENVÍO / DIRECCIONES / HISTORIAL
```

### CC.2 Acceso — desde "Más"
Control de calidad vive en el menú **"Más"** (`...` del tab bar), sección **OTROS**, junto a Canales de venta y Marketing. Ícono `delivery-truck-clock` (camión con "24"). Al entrar, header **"Control de calidad"** (back) + tabs **Gestión de incidencias** (activa) / **Sobrepesos**.

### CC.3 Estado vacío — `852:48784` (validado screenshot)
Cuando no hay incidencias: **ilustración** (personas de almacén con checkmark) + título **"Sin incidencias"** + cuerpo descriptivo + botón **"Reportar incidencia"** (rojo).

### CC.4 KPIs — `4205:109252` (validado design context)
Dos tarjetas métricas (blancas r12, `shadow_card`, **títulos en Manrope**):
- **"Requiere acción"** (Manrope SemiBold 14, `#4C4C4C`) + **"04"** (`T1 M` 24) + chip **"+12%"** (verde `rgba(79,193,83,.1)` / `#4FC153`).
- **"Tasa de incidencias"** + **"1.02%"** + chip **"+2.1%"** (rojo `#F9D2D2` / `#DB3B2B`).

> 🔴 **Manrope en KPIs de incidencias** — los títulos y los chips de porcentaje usan **Manrope**, no Inter. Nueva instancia de la anomalía Manrope fuera de Nova (ver hallazgos de sistema). El número grande sí es Inter (`T1 M`).
> ✅ **Semántica de color en los deltas:** "+12%" en verde (más incidencias que requieren acción — el verde aquí es "subió", no "bueno") y "+2.1%" en rojo (tasa subió — malo). Ojo: en KPIs el color del delta puede confundir; documentar el criterio (¿verde = subió, rojo = empeoró?).

### CC.5 Buscador + acciones — `4205:109266`
- **Buscador** "Busca por código, nombre, SKU…" (`search-01`, placeholder `#9CA3AF`).
- **Botón filtro** (`filter-horizontal`, `#F8F8F8` r12) → abre el drawer de filtros (§CC.7).
- **Botón more-vertical** (`#F8F8F8` r12) → despliega **"Reportar incidencia"** (con `plus-sign`).

### CC.6 Tarjeta de incidencia — `4206:36096` (validado design context)
Card blanco r12 (borde `#F3F3F3`, 233h):
- **Fila superior:** **"INC-00103"** (`B1 S` 16) + **chip de estado** (der.) + **`more-horizontal`** (rotado 90°, menú de acciones).
- **Divisor.**
- **Guía:** label + **"FedEx - 43567890082"** (`B2 M`, carrier + tracking).
- **Estado del envío:** label + el **motivo** (Dirección incompleta o incorrecta / Acceso restringido / etc.).
- **Solución estimada:** label + **"10 días hábiles"**.
- **Divisor.**
- **Fecha de creación:** ícono `calendar-02` + **"15 ago - 2:24 hrs"**.

### CC.7 Sistema de estados de incidencia (chips)
El chip de la tarjeta (y del detalle) reutiliza el sistema de estados, con **tres familias de color** (validado design context):

| Estado | Fondo | Texto | Notas |
|---|---|---|---|
| **Requiere acción** / **Acción requerida** | `#FFF0EF` (Primary/100) | `#DB3B2B` (Primary/600) | Variante con **borde punteado rojo** ("Acción requerida" en screenshots) |
| **En revisión** | `#F3F3F3` | `#4B5563` (Greys/100) | Gris |
| **Envío en proceso** / **En proceso** | `#F3F3F3` | `#4B5563` | Gris, variante con **borde punteado gris** |
| **En revisión** | `#F3F3F3` | `#4B5563` | Gris |
| **Finalizada** | `#F0FDF4` (Green/500) | `#51AF70` (Green/400) | Verde |

> 🔴 **Variantes con borde punteado** (rojo/gris) en los chips de estado de incidencia — parecen indicar un sub-estado o énfasis distinto del color de fondo; confirmar el criterio visual que las distingue.

**Estados del envío (motivos de incidencia)** — el "Estado del envío" de cada tarjeta es la **causa**: Dirección incompleta o incorrecta · Acceso restringido · Paquete sin movimiento · Destinatario no localizado · Paquete rechazado · Paquete dañado. (Cada motivo habilita distintos flujos de acción — se documentan en la siguiente parte.)

### CC.8 Drawer de filtros — `852:50303` (validado screenshot)
El botón de filtro abre el **drawer "Filtrar"** (patrón transversal). Header "Filtrar" + "Restablecer". Secciones:
- **Ordenar por** 🔴 ("Odenar por" typo en Figma) — dropdown con 4 opciones: Fecha de creación (Más recientes primero) · Fecha de creación (Más antiguos primero) · Fecha de actualización (Más recientes primero) · Fecha de actualización (Más antiguos primero).
- **Paquetería** (checkboxes con logo): FedEx · DHL · Grupo ampm · UPS · 99 Minutos.
- **Fecha** (radios): Hoy · Últimos 7 días · Últimos 30 días · **Rango personalizado** (con Fecha de inicio / Fecha de fin, "DD/MM/AAAA").
- **Estado de incidencia** (checkboxes): Envío en proceso · Requiere acción.
- **Estado del envío** (colapsado en la vista compacta).

**Footer:** "Mostrar resultados" (rojo). **Colapsado** (`852:50709`): secciones-acordeón con contador — "Entrega de paquete (1)", "Fecha (1)", "Estado de incidencia", "Estado del envío".

**Chips de filtro aplicados** (`4205:108843`, validado): tras filtrar, chips bajo el buscador con **contador negro** + X — "Entrega de paquete (2)", "Fecha (1)", "Requiere acción"…

> 🔴 **Typo "Odenar por"** → "Ordenar por" (§CC.8).
> ✅ **Drawer de filtros = mismo organismo transversal** (Envíos, Precios, Sucursales, Tracking, y ahora Incidencias). Aquí suma **"Ordenar por"** (sort) que no estaba en los otros — variante enriquecida del drawer.

### CC.9 Detalle de incidencia — `4206:37050` (validado screenshot)
Header **"INC-00103"** (back + `more-vertical`). Estructura:
- **Encabezado:** "28 feb, 12:33 hrs" + **chip de estado** ("Requiere acción").
- **Bloque de estado** (labels + valores): **Estado** (Requiere acción) · **Situación actual** (Requiere acción) · **Fecha de última actualización** (28 feb 12:45 hrs) · **Solución estimada** (10 días hábiles).
- **DETALLE DE ENVÍO** (banda gris): logo carrier (DHL) + guía "774523209" + "Mismo día / 24H" + "1 paquete" · **Costo** ($158.00) · **Fecha de creación** (26 de ene) · **Fecha estimada de entrega** (26 de ene) · **Dimensiones** (45 × 30 × 25 cm) · **Peso** (6kg).
- **DIRECCIÓN DE DESTINO** (banda gris): nombre (Zain Vetrovs) · Información de contacto (correo + tel) · Dirección de envío.
- **DIRECCIÓN DE ORIGEN** (banda gris): nombre · contacto · **Compañía** (Mi empresa) · Dirección de envío.
- **HISTORIAL DE ACTIVIDAD** (banda gris): timeline agrupado por día (Hoy / Hace 1 día / Hace 2 días), **nodo activo = punto negro** en cuadro gris, **nodos pasados = check** en cuadro gris. Eventos: "En espera de una acción" · "Paquete en ruta" · "Notificación enviada al destinatario/remitente" (Sistema automático) · "Incidencia creada" · "Intento de entrega fallido" — cada uno con ubicación (CDMX - Unidad de reparto / Centro de distribución) + fecha/hora.

> ✅ **El detalle reutiliza patrones ya documentados:** bloques con banda gris (como Tracking §EN.11.4) y timeline agrupado por día con nodos (activo=punto, pasado=check). Coherencia con el detalle de guía.

### CC.10 Componentes nuevos (base)
- **Header Control de calidad + tabs** (Gestión de incidencias / Sobrepesos) — §CC.2.
- **KPI card** (título Manrope + número grande + chip delta) — §CC.4.
- **Tarjeta de incidencia** (INC + estado + Guía + motivo + solución + fecha) — §CC.6.
- **Sistema de estados de incidencia** (3 familias + variantes punteadas) — §CC.7.
- **Drawer de filtros con "Ordenar por"** — §CC.8.
- **Detalle de incidencia** (estado + detalle envío + direcciones + historial) — §CC.9.
- **Menú de acciones de tarjeta** (`more-horizontal`) — motivo-dependiente, se documenta en la siguiente parte.

### CC.11 Pendientes (🔴) y cobertura faltante
1. 🔴 **Tab "Sobrepesos"** sin documentar (§CC.2).
2. 🔴 **Flujo "Reportar incidencia"** sin documentar.
3. 🔴 **Flujos de acción por motivo** (menús de la imagen 10-13): Cambiar dirección / Enviar a sucursal / Retornar al origen · Reprogramar entrega / Recolección en sucursal · Solicitar búsqueda / Intentar nueva entrega · Agregar detalles de acceso — cada motivo habilita un set distinto. Documentar en la siguiente parte.
4. 🔴 **Variantes de borde punteado** en los chips de estado por aclarar su significado (§CC.7).
5. 🔴 **Typo "Odenar por"** en el drawer de filtros (§CC.8).
6. ⚠️ **Manrope en KPIs** — nueva instancia de la anomalía (§CC.4).
7. ⚠️ **Semántica del color de los deltas** en KPIs (verde/rojo = subió/bajó vs bueno/malo) — documentar (§CC.4).

### CC.13 Referencias
- *Incident Management* (`947:60630`).
- **Vacío:** `852:48784`. **Listado:** `4205:109247` (tarjetas `4206:36096`+). **KPIs:** `4205:109252`.
- **Chip filtro aplicado:** `4205:108843`. **Drawer filtros:** `852:50303` / colapsado `852:50709`.
- **Detalle:** `4206:37050` (estado `4206:37064`, historial `4206:37151`).

---

## CC.14 Control de calidad — Acción "Cambiar dirección" (§CC.14)

> **Sección "Change address"** (`614:38097`). **Primer flujo de acción** de los pendientes en §CC.11 (punto 3). Se dispara desde el menú `more-horizontal` de la tarjeta de incidencia (§CC.6) o desde el `more-vertical` del detalle (§CC.9), y es la acción de resolución asociada al motivo **"Dirección incompleta o incorrecta"** (§CC.7). Permite capturar una dirección de destino nueva y confirmarla antes de aplicarla al envío.
> 4 pantallas: formulario vacío → campos llenos → validación con error → modal de confirmación.
> **Figma:** `614:38097`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.14.1 Mapa del flujo

```
Incidencia (motivo: Dirección incompleta o incorrecta)
│  menú more-horizontal (tarjeta §CC.6) / more-vertical (detalle §CC.9)
│  └── "Cambiar dirección"
│
├── 1. FORMULARIO VACÍO (606:66173)
│   Card "Dirección actual" (read-only) + botón "Replicar"
│   "Nueva dirección": 8 campos con placeholders
│   CTA "Cambiar" DESHABILITADO (Primary/300)
│
├── 2. CAMPOS LLENOS (606:66923)
│   Valores capturados · CTA "Cambiar" HABILITADO (Primary/600)
│
├── 3. CAMPOS CON ERROR (606:66995)
│   Bordes de error + "Este campo es obligatorio" / "Selecciona una opción"
│   CTA vuelve a deshabilitado
│
└── 4. MODAL DE CONFIRMACIÓN (606:67161)
    "¿Estás seguro de que esta es la dirección correcta?"
    Dirección + botón copiar · [Cancelar] [Sí, confirmar]
```

Los labels de anotación del diseñador en la sección ("Campos llenos", "Campos con error", "Da clic en Cambiar dirección") confirman las transiciones.

### CC.14.2 Chrome de la pantalla (común 1–3)

Status bar iPhone + **header** con back (`majesticons:arrow-up` rotado −90°, 24px, `left 16`) + título **"Cambiar dirección"** centrado (`T3 S` 16 SemiBold, `-0.32px`) + divisor `#F3F3F3` a `y=106`. Home indicator `#9CA3AF` (135×5, r100).

Contenedor: `left 16` · `top 122` · `w 328` · **gap 20** entre bloques. CTA fijo al fondo (`w 328`, h 48).

### CC.14.3 Card "Dirección actual" + Replicar — `606:66637`

Card blanco r12, borde `#F3F3F3`, 130h, padding 12, gap 12:
- **"Dirección actual"** (`B2 S` 14 SemiBold, `-0.28px`, negro).
- **Dirección** (`B3 R` 12 Regular, `#4C4C4C`): "Av. Insurgentes Nte. S/N, San Simón Tolnahuac, Cuauhtémoc, 06920 Ciudad de México, CDMX".
- **Botón "Replicar"** (`606:66642`) — secundario blanco, borde `#F3F3F3`, **r8**, h32, `px16/py12`, label `B3 M` 12 Medium negro. Autocompleta el formulario con la dirección actual.

### CC.14.4 Formulario "Nueva dirección" — `606:66180`

Encabezado de sección **"Nueva dirección"** (`T3 S` 16 SemiBold). Ocho campos, cada uno label + input con **gap 7.328px**; label en `B2 S` 14 SemiBold `-0.28px`.

| # | Campo | Tipo | Placeholder | Nodo (vacío) |
|---|---|---|---|---|
| 1 | Calle | texto | `Av. Reforma` | `606:66193` |
| 2 | Número exterior | texto | `123` | `606:66196` |
| 3 | Número interior | texto | `Depto 5A` | `606:66199` |
| 4 | Código postal | texto | `12345` | `606:66202` |
| 5 | **Colonia** | **select** | `Selecciona una opción` | `606:66205` |
| 6 | Estado | texto | `CDMX` | `606:66213` |
| 7 | Ciudad | texto | `Ciudad de México` | `606:66210` |
| 8 | Referencias | textarea | `Agrega referencias o instrucciones para asegurar la entrega (códigos de acceso, contacto, horarios, etc.).` | `606:66219` |

**Input de texto** (`Inactive/Default Input`): borde `0.916px #F3F3F3`, **r20**, h55, `px18.321 / py16.489`. Placeholder `#C3C3C3` Inter Regular **11.75** `-0.235px`.
**Textarea Referencias:** mismo borde y r20, **h152**, padding 12, texto en 2 líneas.
**Select Colonia:** mismo borde y alto pero **r18.321** y `justify-between`, con `icon/nav/chevron/down` (24px) a la derecha.

> 🔴 **Radio inconsistente:** los inputs de texto usan **r20** y el select Colonia **r18.321**. Unificar a un solo token de radio de input.
> 🔴 **Manrope en el select Colonia** — tanto el placeholder ("Selecciona una opción", `606:66206`) como el valor seleccionado ("San Simón Tolnahuac", `606:66952`) usan **Manrope Regular 12.824px** en negro, mientras todos los demás inputs son Inter 11.75 `#C3C3C3`. **Nueva instancia de la anomalía Manrope** fuera de Nova — se suma a la de los KPIs (§CC.4). Además el select rompe el tratamiento visual del placeholder (negro en vez de gris `#C3C3C3`).

### CC.14.5 Estados de validación — `606:66995`

Al intentar continuar con campos incompletos, el input entra en error: **borde `#DB362B`** y **mensaje debajo** en `B2 R` 14 Regular `-0.28px` color `#DB3B2B`, con gap 7.328px.

| Campo | Mensaje |
|---|---|
| Calle · Número exterior · Número interior · Código postal | **"Este campo es obligatorio"** |
| Colonia (select) | **"Selecciona una opción"** |

Estado y Ciudad **no** muestran error en esta pantalla (se infieren del CP — confirmar si son read-only derivados).

> 🔴 **Drift de token de error:** el borde resuelve a `background/state-indicators/error` = **`#DB362B`**, pero el texto del mensaje y `Primary/600` son **`#DB3B2B`**. Dos rojos casi idénticos conviviendo. Confirmar si el token semántico debe apuntar a Primary/600.
> ⚠️ En la pantalla de error los campos con error conservan **el placeholder** (no el valor capturado), lo que sugiere que el error se dispara con campos vacíos. Colonia sí muestra valor ("San Simón Tolnahuac") **y** error "Selecciona una opción" — contradicción a validar.

### CC.14.6 CTA "Cambiar" — `606:66221`

Botón full-width (328×48), **r16**, label `B1 M` 16 Medium `-0.32px` blanco.

| Estado | Fondo | Cuándo |
|---|---|---|
| **Deshabilitado** | `#F1B0A9` (Primary/300) | Formulario vacío (pant. 1) y con errores (pant. 3) |
| **Habilitado** | `#DB3B2B` (Primary/600) | Todos los campos requeridos llenos (pant. 2) |

### CC.14.7 Modal de confirmación — `606:67161` / `606:67162`

Modal blanco **r16**, centrado, gap 24. Estructura:
- **Ícono** `refresh-01` (32px) en círculo `#F8F8F8` de 64px (r61).
- **Título** "¿Estás seguro de que esta es la dirección correcta?" — `T2 S` **20** SemiBold, `lh 1.3`, `-0.4px`, centrado.
- **Cuerpo** "Tu envío será enviado a la siguiente dirección:" — `B2 R` 14, `#4C4C4C`, centrado (gap 8 respecto al título).
- **Card de dirección** (`606:67172`) — blanco r12, borde `#F3F3F3`, h73, padding 12/11: dirección en `B3 R` 12 `#4C4C4C` + **botón copiar** (`copy-01` 12px) `#F3F3F3` r8 32×32.
- **Acciones** (gap 5, ambos h40 r12, `px32/py12`):
  - **"Cancelar"** — blanco, borde **1.25px** `#F3F3F3`, label `B2 M` 14 Medium negro.
  - **"Sí, confirmar"** — `#DB3B2B`, label `B2 S` 14 SemiBold blanco.

> 🔴 **Backdrop del modal en inglés.** La pantalla usa una **imagen estática** (`image 347`, `606:67159`, 360×780) como fondo atenuado, y ese asset está renderizado **en inglés**: "Change address", "Current address", "**Mexico City**", "Postal Code", "Change". El modal encima sí está correcto en es-MX. → Re-exportar el backdrop desde una pantalla es-MX. Se suma al patrón de copy EN en pantallas es-MX (§CC.3, §B.3, §B.4).
> ✅ **Patrón de confirmación destructiva/irreversible** coherente con los modales ya documentados (§PC.8 "Eliminar variante", §PK.5): ícono en círculo gris + título pregunta + body + par de botones con la acción primaria en rojo.

### CC.14.8 Componentes nuevos (vs. ya documentados)

- **Card "dirección actual" + Replicar** — patrón de *copiar dato existente al formulario*. Es la primera vez que aparece un botón "Replicar" en la App; funcionalmente equivale al checkbox "Establecer como…" de §EN.9 pero en modo acción.
- **Card de dirección con botón copiar** (`copy-01`) dentro de modal — nuevo en la App.
- **Modal de confirmación con dato citado** (muestra el valor a confirmar dentro de una card) — variante enriquecida del modal de confirmación estándar.

Reutiliza sin cambios: input de texto/textarea, select con chevron, CTA full-width, header con back.

### CC.14.9 Pendientes (🔴)

1. 🔴 **Backdrop del modal en inglés** (`image 347`) — re-exportar en es-MX (§CC.14.7).
2. 🔴 **Manrope en el select Colonia** (placeholder y valor, 12.824px) — nueva instancia de la anomalía; además placeholder en negro en vez de `#C3C3C3` (§CC.14.4).
3. 🔴 **Radio inconsistente** entre inputs de texto (r20) y select (r18.321) (§CC.14.4).
4. 🔴 **Drift de token de error**: borde `#DB362B` vs. texto/Primary/600 `#DB3B2B` (§CC.14.5).
5. ⚠️ **Colonia con valor seleccionado Y error "Selecciona una opción"** — contradicción de estado a validar (§CC.14.5).
6. 🔴 **Sin pantalla de éxito documentada** — el flujo termina en "Sí, confirmar"; falta el estado posterior (¿toast? ¿retorno al detalle de incidencia con estado actualizado?). Localizar en Figma.
7. 🔴 **Menú de acciones origen sin documentar** — el `more-horizontal` de la tarjeta (§CC.6) que contiene "Cambiar dirección" y las demás acciones sigue pendiente (§CC.11 punto 3).
8. ⚠️ **Estado y Ciudad** — confirmar si son campos editables o derivados del CP (§CC.14.5).

### CC.14.11 Referencias

- *Change address* (`614:38097`).
- **Vacío:** `606:66173` · **Lleno:** `606:66923` · **Error:** `606:66995` · **Modal:** `606:67161` (contenido `606:67162`).
- **Card dirección actual:** `606:66637` (botón Replicar `606:66642`).
- **Select Colonia:** `606:66205` (placeholder `606:66206`) / lleno `606:66951` (valor `606:66952`).
- **CTA "Cambiar":** `606:66221` (off) / `606:67035` (en pantalla de error).
- **Backdrop EN (bug):** `606:67159` (`image 347`).
- **Anotaciones del diseñador:** `615:40260` · `615:40262` · `615:40265`.

---

## CC.15 Control de calidad — Acción "Enviar a sucursal" (§CC.15)

> **Sección "Send to Branch"** (`614:38098`). **Segundo flujo de acción** de los pendientes en §CC.11 (punto 3). Redirige el paquete a una **sucursal de paquetería** para que el destinatario lo recoja, en lugar de reintentar la entrega a domicilio. Se dispara desde el menú de acciones de la incidencia y aplica a motivos como *Destinatario no localizado* o *Acceso restringido* (confirmar binding exacto).
> 4 pantallas: selección de sucursal (mapa + radios) → modal de confirmación · y dos estados de un **popup de error** cuando no hay sucursales para el CP.
> **Figma:** `614:38098`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.15.1 Mapa del flujo

```
Incidencia › menú de acciones › "Enviar a sucursal"
│
├── 1. SELECCIÓN DE SUCURSAL (608:18087)
│   Header "Enviar a sucursal de [logo DHL]"
│   Mapa (328×238, r12) + "Abrir en Mapas" + controles GPS/zoom
│   Copy explicativo (título + subtítulo)
│   Radio-cards de sucursal (nombre · dirección · distancia · horario)
│   CTA "Confirmar"
│   │
│   ├── tap "Confirmar" ──▶ 2. MODAL DE CONFIRMACIÓN (609:18357)
│   │       "¿Estás seguro de que prefieres recogerlo en la sucursal?"
│   │       [Cancelar] [Sí, confirmar]
│   │
│   └── sin sucursales para el CP ──▶ 3. POPUP DE ERROR
│           3a. CP vacío  (614:37834) — "Validar" DESHABILITADO
│           3b. CP escrito (614:38029) — "Validar" HABILITADO
│           Salidas: Validar · Cambiar dirección · Devolver al origen · Cancelar
```

Las anotaciones del diseñador "Error Popup" confirman que 3a/3b son dos estados del mismo popup, no dos pantallas distintas.

### CC.15.2 Header con logo de paquetería — `608:18167`

Header con back + título compuesto: **"Enviar a sucursal de"** (`B?` 16, ver nota) + **logo DHL como imagen** (`608:18164`, grupo de 75.4×10.77px) inline al final del texto.

> ⚠️ **Primer header con marca de tercero embebida en la App.** El título no es puro texto: concatena copy + asset de logo. Esto obliga a que el header sea **dinámico por paquetería** (DHL, FedEx, UPS, 99 Minutos, Grupo ampm — el catálogo de §CC.8). Documentar como componente parametrizable y definir el fallback cuando no haya logo disponible.
> 🔴 **El logo es un asset plano**, no un componente de marca versionado. Si cambia el logo de una paquetería hay que reemplazarlo en cada pantalla. Considerar un componente `carrier-logo` con variantes.

### CC.15.3 Mapa — `608:18168`

Contenedor 328×238, **r12**, imagen de mapa (Google Maps) con pines de sucursales. Controles superpuestos:
- **"Abrir en Mapas"** (`608:18187`) — píldora **r57**, fondo `rgba(0,0,0,.4)` + **backdrop-blur 2.8px**, `px8/py6`, logo `logos:google-maps` (10×14) + label `B3 M` 12 blanco. Esquina superior derecha (`top 8`, `right 8`).
- **Control GPS** (`608:18171`) — botón 32×32, **r40**, `rgba(0,0,0,.4)` + **backdrop-blur 3.85px**, ícono `gps-off-02` 20px.
- **Zoom +/−** (`608:18179`) — par apilado 32×64, r40, mismo fondo y blur; divisor interno `border-b rgba(255,255,255,.2)`; íconos `add-01` / `minus-sign` 20px.

> ✅ **Primer mapa embebido documentado en la App.** Aporta un patrón nuevo: *superficie de mapa con controles flotantes glassmorphism* (`rgba(0,0,0,.4)` + backdrop-blur). Reutilizable en Envíos (§EN) y Recolecciones (§EN.12).
> 🔴 **El mapa es una imagen estática en Figma** — definir con dev el proveedor real (Google Maps SDK), el comportamiento de los pines, el centrado inicial y qué pasa sin permiso de ubicación (el ícono `gps-off-02` sugiere estado "GPS apagado" — ¿es el default?).

### CC.15.4 Copy explicativo — `608:18198`

Bloque de dos textos, gap 8:
- **Título:** "El paquete será enviado a una sucursal de paquetería para su recolección." — `T3 S` 16 SemiBold, `lh 1.3`, `-0.32px`, negro.
- **Subtítulo:** "Selecciona la sucursal más conveniente para completar el proceso." — `B2 R` 14 Regular, `-0.28px`, `#4C4C4C`.

### CC.15.5 Radio-card de sucursal — `608:18200` / `608:18205` / `608:18210`

Lista con gap 8. Cada card: blanco, **r16**, `px12/py16`, contenido con gap 12.

| Estado | Borde |
|---|---|
| **Seleccionada** | `1px #DB3B2B` (Primary/600) |
| **No seleccionada** | `1px #F3F3F3` (Greys/800) |

- **Fila superior** (gap 8): **radio `Control`** 16×16 (variantes `Radio`/state on ↔ `Radi`/state off) + **nombre de la sucursal** en `B2 S` 14 SemiBold `-0.28px` negro, con `text-ellipsis` a una línea.
- **Bloque de datos** — un **único nodo de texto** en `B3 M` 12 Medium `#4C4C4C`, con líneas separadas por párrafos vacíos:
  - Dirección completa
  - `Distancia: 2.5 km`
  - `Horario: Lunes a viernes de 10:00 a 18:00 hrs`

> 🔴 **Nombre truncado a una línea.** "EMPAKATODO TOLLOCAN (Centro de envíos DHL autorizado)" se corta con elipsis en la pantalla (`608:18212`). Los nombres de sucursal con calificador entre paréntesis son largos por naturaleza — definir si se permiten 2 líneas o si el calificador va en una línea secundaria.
> 🔴 **Distancia y horario son texto libre dentro de un solo nodo**, no campos estructurados. Para dev conviene separarlos (dirección / distancia / horario) y definir formato de distancia (¿km con 1 decimal? ¿qué pasa a <1 km?) y de horario (¿rangos múltiples? ¿sábados? ¿cerrado?).
> ⚠️ **El radio va a la izquierda del nombre** — coherente con los patrones de selección ya documentados.

### CC.15.6 CTA "Confirmar" — `608:18127`

Botón full-width 328×48 al fondo. En el screenshot validado aparece **habilitado en `#DB3B2B`** porque ya hay una sucursal seleccionada por defecto (la primera).

> ⚠️ **Hay preselección por defecto** (AEROPUERTO viene marcado). Confirmar si es intencional — implica que el CTA nunca arranca deshabilitado, a diferencia de "Cambiar dirección" (§CC.14.6).

### CC.15.7 Modal de confirmación — `609:18357` / `609:18359`

Mismo componente que §CC.14.7, con contenido distinto. Modal blanco **r16**, gap 24:
- **Ícono** `refresh-01` 32px en círculo `#F8F8F8` 64px (r61).
- **Título:** "¿Estás seguro de que prefieres recogerlo en la sucursal?" — `T2 S` 20 SemiBold `lh 1.3` `-0.4px`, centrado.
- **Cuerpo:** "Tu envío será enviado a la siguiente sucursal" — `B2 R` 14, `#4C4C4C`, centrado. *(Sin punto final.)*
- **Card de dato citado** (`609:18368`) — blanco r12, borde `#F3F3F3`, **h119** (vs. h73 en §CC.14), `B3 R` 12 `#4C4C4C` en 3 líneas: nombre de sucursal · dirección · horario. Con **botón copiar** `copy-01` 12px sobre `#F3F3F3` r8 32×32.
- **Acciones** (gap 5, h40, r12): **"Cancelar"** blanco borde 1.25px `#F3F3F3` `B2 M`; **"Sí, confirmar"** `#DB3B2B` `B2 S` blanco.

> ✅ **Confirma el patrón "modal de confirmación con dato citado"** introducido en §CC.14.8. Segunda instancia → es un componente real del sistema, no un one-off. La card crece en alto según el dato (73 ↔ 119); documentar como contenedor flexible.
> 🔴 **Backdrop del modal en inglés** — igual que §CC.14.7. El fondo atenuado (`image 348`, `609:18355`) está en EN: "Send to branch of", "Open in Maps", "Distance: 3.8 km", "Hours: Monday to Friday from 10:00 am - 6:00 pm". El modal encima sí está en es-MX. **Mismo bug, mismo origen** (imagen estática exportada de una pantalla EN).

### CC.15.8 Popup de error "sin sucursales" — `614:37834` (3a) / `614:38029` (3b)

Popup blanco **r16**, ancho 296, gap 24. **No** usa el patrón de modal con ícono circular — es un **contenedor con header propio**:

- **Header** (`614:37899`): título **"Enviar a sucursal de"** + **logo DHL** (`T2 S` 20 SemiBold `-0.4px`) + **`cancel-01`** 24px a la derecha.
- **Card interior** (`614:37904`) — blanco r12, borde `#F3F3F3`, `p11/12`, gap 12:
  - **Mensaje:** "No encontramos sucursales cercanas para el código postal **[#####]**" — `B2 M` 14 Medium `-0.28px` negro.
  - **Ayuda:** "Puedes ingresar un código postal diferente o elegir otra opción para gestionar la entrega." — `B3 R` 12 Regular `#4C4C4C`.
  - **Input de CP** (`614:37937`) — borde `0.916px #F3F3F3`, **r20**, h55, `px18.321/py16.489`. Placeholder "Ingresa un código postal" `#C3C3C3` 11.75. En 3b muestra el valor `55520` en **negro**.
  - **Botón "Validar"** (h32, **r8**, full-width):

| Estado | Fondo | Texto | Nodo |
|---|---|---|---|
| **Deshabilitado** (3a, CP vacío) | `#F3F3F3` | `#9CA3AF` | `614:37909` |
| **Habilitado** (3b, CP escrito) | `#DB3B2B` | `#FFFFFF` | `614:38050` |

  - **Divisor** (`Line 735`) full-width.
  - **Fila de escapes** (gap 12, ambos h32 r8, fondo `rgba(244,244,244,0)` = transparente, label `B3 M` 12 negro), separados por un **divisor vertical de 22px** (`Line 736`, rotado 90°):
    - **"Cambiar dirección"** → deriva a §CC.14
    - **"Devolver al origen"** → deriva al flujo de retorno (pendiente)
- **Botón "Cancelar"** (`614:37910`) fuera de la card — blanco, borde **1.25px** `#F3F3F3`, h40, **r12**, `B2 M` 14.

> ✅ **Patrón nuevo: "callejón sin salida con rutas de escape".** Cuando la acción elegida no es viable, el popup no solo informa: ofrece **reintentar** (otro CP), **derivar a otra acción** (Cambiar dirección / Devolver al origen) o **abortar**. Este es el patrón a reutilizar en los demás flujos de acción cuando fallen sus precondiciones. Vale la pena elevarlo a componente transversal.
> 🔴 **Placeholder literal `[#####]` sin resolver** en el copy del mensaje (`614:37907`). Debe ser una variable con el CP real. Está así en **ambos** estados, incluso en 3b donde ya hay CP escrito (55520) — el mensaje debería reflejarlo.
> 🔴 **Fondo transparente en los botones de escape** (`rgba(244,244,244,0)`, alpha 0). Parece un `#F4F4F4` al que le bajaron la opacidad a 0 en vez de quitar el fill. Limpiar: o es transparente de verdad o es `#F4F4F4`.
> 🔴 **Inconsistencia de radio** — el input del popup usa **r20** (igual que §CC.14.4) pero los botones internos usan **r8** y el "Cancelar" exterior **r12**. Tres radios de botón en un mismo popup. Revisar contra la escala de radios de `APP.md`.
> ⚠️ El popup **no tiene estado de error de validación** del CP (CP inválido / inexistente). Falta esa pantalla.

### CC.15.9 Componentes nuevos (vs. ya documentados)

- **Header con logo de paquetería** (copy + asset de marca inline) — §CC.15.2. Debe ser parametrizable por carrier.
- **Mapa embebido con controles flotantes glassmorphism** (`rgba(0,0,0,.4)` + backdrop-blur, r40/r57) — §CC.15.3. **Primero en la App.**
- **Radio-card de sucursal** (radio + nombre + dirección/distancia/horario, borde rojo al seleccionar) — §CC.15.5.
- **Popup "callejón sin salida" con rutas de escape** (mensaje + reintento + 2 derivaciones + cancelar) — §CC.15.8. **Candidato a componente transversal.**

Reutiliza: **modal de confirmación con dato citado** (§CC.14.7, segunda instancia), input de texto r20, botón `Cancelar` outline, CTA full-width.

### CC.15.10 Pendientes (🔴)

1. 🔴 **Backdrop del popup/modal en inglés** (`image 348`, `609:18355` y las de `614:37835` / `614:38030`) — mismo bug que §CC.14.7. Re-exportar en es-MX.
2. 🔴 **Placeholder `[#####]` sin resolver** en el mensaje de error, en ambos estados (§CC.15.8).
3. 🔴 **Logo de paquetería como asset plano** — crear componente `carrier-logo` con variantes y definir fallback (§CC.15.2).
4. 🔴 **Mapa sin especificación técnica** — proveedor, pines, centrado, permiso de ubicación denegado (§CC.15.3).
5. 🔴 **Nombre de sucursal truncado** a una línea (§CC.15.5).
6. 🔴 **Distancia/horario como texto libre** en un solo nodo — estructurar y definir formatos (§CC.15.5).
7. 🔴 **Fondo `rgba(244,244,244,0)`** (alpha 0) en botones de escape — limpiar (§CC.15.8).
8. 🔴 **Tres radios de botón** en el mismo popup (r8 / r12) + input r20 (§CC.15.8).
9. 🔴 **Falta estado de CP inválido** tras "Validar" (§CC.15.8).
10. 🔴 **Sin pantalla de éxito** — igual que §CC.14, el flujo corta en "Sí, confirmar".
11. ⚠️ **Preselección de la primera sucursal** — confirmar si es intencional (§CC.15.6).
12. ⚠️ **Motivos que habilitan esta acción** sin confirmar (§CC.7).

### CC.15.12 Referencias

- *Send to Branch* (`614:38098`).
- **Selección:** `608:18087` (contenido `608:18093`) · **Modal:** `609:18357` (contenido `609:18359`).
- **Popup error CP vacío:** `614:37834` (contenido `614:37895`) · **CP escrito:** `614:38029` (contenido `614:38044`).
- **Header + logo DHL:** `608:18167` (logo `608:18164`) · popup `614:37934` (logo `614:37930`).
- **Mapa:** `608:18168` (Abrir en Mapas `608:18187`, GPS `608:18171`, zoom `608:18179`).
- **Radio-cards:** `608:18200` (seleccionada) · `608:18205` · `608:18210`.
- **Botón Validar:** `614:37909` (off) / `614:38050` (on) · **escapes:** `614:37969` / `614:37955`.
- **Backdrops EN (bug):** `609:18355` · `614:37835` · `614:38030` (`image 348`).
- **Anotaciones del diseñador:** `615:40586` · `615:40588` (Error Popup).

---

## CC.16 Control de calidad — Acción "Devolver al origen" (§CC.16)

> **Sección "Return to origin"** (`614:38096`). **Tercer flujo de acción** de los pendientes en §CC.11 (punto 3). Cancela la entrega y regresa el paquete a la dirección de origen del negocio. Es la ruta de escape a la que derivan otros flujos cuando su acción no es viable (§CC.15.8).
> Solo **2 pantallas**: bottom sheet de confirmación → modal de confirmación. **Es el flujo de acción más corto documentado** y el **primero que usa el arquetipo bottom sheet**.
> **Figma:** `614:38096`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.16.1 Mapa del flujo

```
Incidencia › menú de acciones › "Devolver al origen"
│  (o derivado desde el popup "sin sucursales" de §CC.15.8)
│
├── 1. BOTTOM SHEET (606:66078)
│   "Devolver al origen" + cancel-01
│   "¿Confirmas que el paquete debe devolverse al origen?"
│   Card "Dirección de destino" + botón "Cambiar"
│   CTA "Sí, devolver"
│   │
│   ├── tap cancel-01 ──▶ regresa al listado
│   └── tap "Sí, devolver" ──▶
│
└── 2. MODAL DE CONFIRMACIÓN (606:66114)
    "¿Estás seguro de que quieres devolver al origen?"
    Dirección + copiar · [Cancelar] [Sí, confirmar]
```

Las anotaciones del diseñador confirman las transiciones: **"Da clic en sí, devolver"** del sheet al modal, y **"Da clic en el botón cancelar para regresar"**.

### CC.16.2 Bottom sheet — `606:66078` / `606:66080`

**Primer bottom sheet de los flujos de acción.** Ancla al fondo de la pantalla (`y=468` sobre un frame de 780, ocupa los 312px inferiores), ancho completo 360.

- **Contenedor:** blanco, **radio superior 16px** (`rounded-tl-16 rounded-tr-16`, esquinas inferiores rectas), `px16 / py17`, gap 24.
- **Header** (`606:66084`): título **"Devolver al origen"** (`T2 S` 20 SemiBold `lh 1.3` `-0.4px`, ancho 200) + **`cancel-01`** 24px alineado a la derecha, con `items-start` (alineados arriba, no centrados).
- **Pregunta** (`606:66088`): "¿Confirmas que el paquete debe devolverse al origen?" — `B2 R` 14 Regular `-0.28px` `#4C4C4C`. Gap 8 respecto al header.
- **Card de dirección** (`606:66103`) — blanco r12, borde `#F3F3F3`, **h130**, contenido en `left 11 / top 11`, ancho 272, gap 12:
  - **"Dirección de destino"** — `B2 S` 14 SemiBold `-0.28px` negro.
  - Dirección — `B3 R` 12 Regular `#4C4C4C`.
  - **Botón "Cambiar"** (`606:66108`) — blanco, borde `#F3F3F3`, **r8**, h32, w101, `px16/py12`, label `B3 M` 12 Medium negro.
- **CTA "Sí, devolver"** (`606:66094`) — full-width, h40, **r12**, `#DB3B2B`, label `B2 S` 14 SemiBold blanco.

> ✅ **Arquetipo nuevo en los flujos de acción: bottom sheet.** Hasta ahora §CC.14 usó pantalla completa y §CC.15 pantalla completa + popup centrado. Este es el tercero: **sheet anclado al fondo con radio superior 16 y esquinas inferiores rectas**. Con esto ya son **tres arquetipos de UI** conviviendo en las acciones de incidencias — conviene documentar el criterio de cuándo usar cada uno.
> 🔴 **Sin handle (grabber).** El sheet no tiene el indicador de arrastre típico de iOS/Android. Definir si es descartable por gesto (swipe down) o solo por `cancel-01`. Si es arrastrable, falta el handle; si no lo es, documentarlo explícitamente.
> ⚠️ **Card idéntica a la de §CC.14.3** (misma estructura: título + dirección + botón secundario, r12, h130, borde `#F3F3F3`, botón r8 h32 w101). Cambian solo el título y el label del botón ("Dirección actual"/"Replicar" ↔ "Dirección de destino"/"Cambiar"). **Es el mismo componente parametrizable** — documentar como tal en lugar de dos cards distintas.

### CC.16.4 Modal de confirmación — `606:66114` / `606:66117`

Idéntico en estructura a §CC.14.7 (misma card h73, mismos gaps):
- **Ícono** `refresh-01` 32px en círculo `#F8F8F8` 64px (r61).
- **Título:** "¿Estás seguro de que quieres devolver al origen?" — `T2 S` 20 SemiBold `lh 1.3` `-0.4px`, centrado.
- **Cuerpo:** "Tu envío será enviado a la siguiente dirección" — `B2 R` 14 `#4C4C4C`, centrado, en 2 líneas. *(Sin punto final.)*
- **Card de dato citado** (`606:66137`) — blanco r12, borde `#F3F3F3`, **h73**, dirección en `B3 R` 12 `#4C4C4C` + botón copiar `copy-01` 12px sobre `#F3F3F3` r8 32×32.
- **Acciones** (gap 5, h40, r12): **"Cancelar"** blanco borde 1.25px `B2 M`; **"Sí, confirmar"** `#DB3B2B` `B2 S` blanco.

> ✅ **Tercera instancia del "modal de confirmación con dato citado"** (§CC.14.7, §CC.15.7, aquí). Queda confirmado como **componente estable del sistema**. Las tres instancias comparten ícono, gaps, tipografía y par de botones; solo varían el título, el cuerpo y el alto de la card (h73 / h119 / h73).
> 🔴 **Espacio inicial en el copy** — el segundo renglón del cuerpo empieza con un espacio (`" siguiente dirección"`, `606:66125`). Limpiar.

### CC.16.5 🔴 Backdrop en inglés — tercera instancia, ahora del listado

Ambas pantallas usan la imagen estática **`image 346`** (`606:66079`, `606:66115`) como fondo atenuado, y está **completamente en inglés**. A diferencia de §CC.14 y §CC.15 —donde el backdrop era la pantalla del propio flujo— aquí el backdrop es **el listado de incidencias**, es decir la base ya documentada en §CC.4–§CC.6, lo que indica que existe una versión EN completa de esas pantallas en el archivo, no solo backdrops sueltos.

> 🔴 Re-exportar los backdrops desde las pantallas es-MX correspondientes — mismo bug de origen que §CC.14.7/§CC.15.7.

### CC.16.6 🟡 Elementos del backdrop no cubiertos por §CC (base)

El backdrop expone **dos elementos del listado que no están en la documentación base**:

1. **Texto introductorio** bajo el header — *"Resolve delivery issues fast and manage all shipment reports in one place."* No aparece en §CC.2 ni §CC.4. ¿Es nuevo, o se omitió al documentar la base?
2. **CTA "Report incident →"** prominente (rojo, full-width, con flecha) entre el intro y los KPIs. En §CC.3 "Reportar incidencia" aparece solo en el **estado vacío**, y en §CC.5 dentro del menú `more-vertical`. **Aquí está como CTA permanente del listado con datos** — es una tercera ubicación.
3. **Filtros como dropdowns inline** (`Package delivery ⌄` · `Date ⌄` · `Incident status ⌄`) en fila bajo el buscador, en vez del **drawer "Filtrar"** documentado en §CC.8.

> 🟡 **No accionar todavía.** Estos elementos vienen de una imagen de backdrop, no de nodos vivos — pueden ser una versión anterior o posterior del listado. **Verificar contra el nodo real del listado** (`4205:109247`) antes de corregir §CC.4–§CC.8. Si el listado vivo ya cambió, la base necesita actualización; si no, el backdrop está desactualizado.

### CC.16.7 Componentes nuevos (vs. ya documentados)

- **Bottom sheet de confirmación** (radio superior 16, `px16/py17`, header con título + `cancel-01`, gap 24) — §CC.16.2. **Primero de los flujos de acción**; tercer arquetipo de UI del módulo.

Reutiliza: **card dirección + botón secundario** (§CC.14.3, misma geometría), **modal de confirmación con dato citado** (§CC.14.7, tercera instancia), botón `Cancelar` outline, CTA r12.

### CC.16.8 Pendientes (🔴)

1. 🔴 **Backdrop en inglés — 3ª instancia, ahora del listado completo** (§CC.16.5). Re-exportar desde las pantallas es-MX correspondientes.
2. 🔴 **Espacio inicial** en el copy del modal (`606:66125`) (§CC.16.4).
3. 🔴 **Sheet sin handle** — definir si es descartable por gesto (§CC.16.2).
4. 🔴 **Sin pantalla de éxito** — igual que §CC.14 y §CC.15. **Ya son 3 flujos sin cierre documentado**; conviene resolverlo como patrón único, no flujo por flujo.
5. 🟡 **Elementos del listado no documentados** en la base: intro, CTA permanente "Reportar incidencia", filtros inline vs. drawer (§CC.16.6). **Verificar contra `4205:109247` antes de corregir §CC.4–§CC.8.**
6. ⚠️ **Card de dirección duplicada como componente** — unificar §CC.14.3 y §CC.16.2 en un solo componente parametrizable.

### CC.16.10 Referencias

- *Return to origin* (`614:38096`).
- **Bottom sheet:** `606:66078` (contenido `606:66080`; header `606:66084`, pregunta `606:66088`, card `606:66103`, botón "Cambiar" `606:66108`, CTA `606:66094`).
- **Modal:** `606:66114` (contenido `606:66117`; título `606:66124`, cuerpo `606:66125`, card `606:66137`, copiar `606:66142`, acciones `606:66127` / `606:66128`).
- **Backdrops EN (bug):** `606:66079` · `606:66115` (`image 346`).
- **Anotaciones del diseñador:** `615:39810` ("Da clic en sí, devolver") · `615:39808` ("Da clic en el botón cancelar para regresar").

---

## CC.17 Control de calidad — Acción "Reagendar entrega" (§CC.17)

> **Sección "Reschedule Delivery"** (`614:38094`). **Cuarto flujo de acción** de los pendientes en §CC.11 (punto 3). Reprograma la entrega a una nueva fecha sin cambiar el destino. Aplica a motivos como *Destinatario no localizado* (confirmar binding).
> 4 pantallas: bottom sheet (fecha vacía) → date picker → sheet (fecha capturada) → modal de confirmación.
> **Primer flujo con selección de fecha** y **primer modal con ícono distinto** al `refresh-01`.
> **Figma:** `614:38094`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.17.1 Mapa del flujo

```
Incidencia › menú de acciones › "Reagendar entrega"
│
├── 1. BOTTOM SHEET — fecha vacía (606:65878)
│   "Reagendar entrega" + cancel-01
│   Card "Dirección de destino" + botón "Cambiar" ──▶ deriva a §CC.14
│   "Selecciona una nueva fecha de entrega." + select "Seleccionar fecha"
│   CTA "Continuar" DESHABILITADO
│   │
│   └── tap select ──▶ 2. DATE PICKER (615:38459 · picker 615:38492)
│           Mes ‹ Nov › · Año 2024 ⌄ · grilla 7×6
│           [Cancelar] [Seleccionar]
│           │
│           └── tap "Seleccionar" ──▶
│
├── 3. BOTTOM SHEET — fecha capturada (615:38725)
│   Select muestra "12 de nov 2024" · CTA "Continuar" HABILITADO
│   │
│   └── tap "Continuar" ──▶
│
└── 4. MODAL DE CONFIRMACIÓN (606:65979)
    Ícono calendar-03 · "¿Confirmas la nueva fecha entrega?" · "14/02/2025"
    [Cancelar] [Sí, reprogramar]
```

Anotaciones del diseñador: **"Selecciona fecha"**, **"Da clic en continuar"** y —la más importante— la que documenta el destino del botón "Cambiar" (§CC.17.3).

### CC.17.2 Bottom sheet — `606:65878` / `615:38725`

Reutiliza **exactamente** el arquetipo de §CC.16.2 (bottom sheet anclado al fondo, radio superior 16, gap 24), con un bloque de fecha añadido:

- **Header:** título **"Reagendar entrega"** (`T2 S` 20 SemiBold `-0.4px`, ancho 200) + **`cancel-01`** 24px, `items-start`.
- **Card de dirección** (`615:38734`) — **idéntica a §CC.16.2**: r12, h130, borde `#F3F3F3`, título **"Dirección de destino"** (`B2 S` 14) + dirección (`B3 R` 12 `#4C4C4C`) + botón **"Cambiar"** (blanco, borde `#F3F3F3`, r8, h32, w101, `B3 M` 12).
- **Bloque de fecha** (`615:38740`, gap 7.328):
  - **Label:** "Selecciona una nueva fecha de entrega." — `B2 S` 14 SemiBold `-0.28px` negro.
  - **Select de fecha** (`615:38742`) — borde `1px #F3F3F3`, **r20**, h55, `px20/py18`, `justify-between`, con `icon/nav/chevron/down` 24px.
    - **Vacío:** "Seleccionar fecha"
    - **Lleno:** "12 de nov 2024" en `B2 M` 14 Medium `-0.28px` **negro**
- **CTA "Continuar"** (`615:38746`) — full-width, h40, **r12**, `B2 S` 14 SemiBold blanco.

| Estado CTA | Fondo | Cuándo |
|---|---|---|
| **Deshabilitado** | `#F1B0A9` (Primary/300) | Sin fecha seleccionada |
| **Habilitado** | `#DB3B2B` (Primary/600) | Con fecha seleccionada |

> ⚠️ **El select de fecha usa `border 1px` y `px20/py18`**, mientras los inputs de §CC.14.4 usan `border 0.916px` y `px18.321/py16.489`. Mismo radio (r20) y alto (55) pero métricas distintas — el de §CC.14 tiene escalado horneado (§ patrón de valores no redondos), este está limpio. **Este es el correcto**; usarlo como referencia al unificar.
> ✅ **Sin anomalía Manrope en el sheet** — todo Inter, a diferencia del select Colonia de §CC.14.4.

### CC.17.3 Destino del botón "Cambiar"

La anotación del diseñador `615:39623` dice literalmente:

> *"Cuando el usuario da clic en cambiar dirección, se le lleva a la pantalla de cambio de dirección que se encuentra a la derecha de las secciones"*

**El botón "Cambiar" de la card deriva al flujo §CC.14 "Cambiar dirección".** En este flujo tiene sentido pleno: al reprogramar una entrega, corregir también la dirección es un caso de uso real. Queda establecido el patrón: *card de dirección + botón "Cambiar" → §CC.14*.

### CC.17.4 Date picker — `615:38492` (instancia de `Frame 2147224763`)

**Componente compartido** (es una *instance*, no un frame local). Popup centrado 328×380 superpuesto sobre el sheet.

- **Contenedor:** blanco, borde `1px #F8F8F8`, **r16**, `p16`, gap 24, **sombra `0 4px 7.45px rgba(0,0,0,.15)`**.
- **Navegación superior** (`justify-between`):
  - **Selector de mes** (`I…108:29883`) — pill blanco, borde `1px #E7E7E7`, **r10**, `px15/py4`, w209, con chevrons ‹ › a los lados y **"Nov"** al centro.
  - **Selector de año** (`I…108:29875`) — pill blanco, borde `1px #E7E7E7`, **r10**, `px10/py4`, **"2024"** + chevron down 16px.
- **Grilla** 7 columnas × 6 filas, gap 11, 273×238:
  - **Encabezados de día:** `D L M M J V S` — `B2 M` 14 Medium `-0.28px`, color `#C3C3C3` (Greys/400).
  - **Días del mes:** `B2 M` 14 Medium, color `#242C2E`, celdas `p6` **r10** fondo blanco.
  - **Día seleccionado:** fondo `#DB3B2B` (brand/red), texto blanco, **r60** (círculo).
  - **Días de mes contiguo:** color `#C3C3C3` (ej. el "1" de diciembre en la última fila).
- **Acciones** (gap 8, ambos h32 w133 **r8**):
  - **"Cancelar"** — blanco, borde `#F3F3F3`, `B3 M` 12 negro.
  - **"Seleccionar"** — `#DB3B2B`, `B3 M` 12 blanco.

> 🔴 **Manrope en el date picker.** Los selectores de **mes ("Nov")** y **año ("2024")** usan **Manrope SemiBold 16**, mientras la grilla de días usa Inter. **Nueva instancia de la anomalía Manrope** — se suma a los KPIs de incidencias (§CC.4) y al select Colonia (§CC.14.4). Como es un **componente compartido**, esta anomalía se propaga a todas las pantallas que usen el date picker.
> 🔴 **Color `#242C2E` fuera de la paleta de la App.** Los días de la grilla y los selectores de mes/año usan `#242C2E`, un gris azulado que **no existe en los tokens documentados** (la App usa `Text/Text Dark #000000`). Igual que Manrope, viene del componente compartido. Mapear a `#000000` o registrar el token si es intencional.
> 🔴 **Borde `#E7E7E7` fuera de la paleta.** Los pills de mes/año usan `#E7E7E7` (`neutral/gray-400`), cuando el borde estándar de la App es `#F3F3F3` (Greys/800). Tercera fuga de tokens del mismo componente.
> ⚠️ **Radio del día seleccionado = r60** (círculo) vs. **r10** de las celdas normales. Es intencional visualmente, pero documentarlo como estado, no como valor suelto.
> ⚠️ **Semana inicia en domingo (D L M M J V S).** Correcto para MX. Confirmar que el componente no cambie a lunes en otro contexto.
> 🔴 **Sin restricción de fechas visible.** No hay días deshabilitados en la grilla — falta el estado visual de "día no disponible" (fondo/color atenuado) para fechas pasadas u otras que deban excluirse.

### CC.17.5 Modal de confirmación — `606:65979` / `606:66015`

**Cuarta instancia** del modal de confirmación, pero con **dos diferencias estructurales**:

- **Ícono `calendar-03`** 32px en círculo `#F8F8F8` 64px (r61) — **primer modal que NO usa `refresh-01`**.
- **Sin card de dato citado.** El dato va como **texto plano** bajo el título: "14/02/2025" en `B1 R` **16** Regular `-0.32px` `#4C4C4C`. Las instancias anteriores (§CC.14.7, §CC.15.7, §CC.16.4) usan card r12 con botón copiar.
- **Título:** "¿Confirmas la nueva fecha entrega?" — `T2 S` 20 SemiBold `lh 1.3` `-0.4px`, centrado.
- **Acciones** (gap 5, h40, r12): **"Cancelar"** blanco borde 1.25px `B2 M`; **"Sí, reprogramar"** `#DB3B2B` `B2 S` blanco.

> ✅ **Confirma que el modal de confirmación es parametrizable en ícono y cuerpo.** Cuatro instancias, dos ejes de variación: **ícono** (`refresh-01` ×3, `calendar-03` ×1) y **tipo de cuerpo** (card con dato citado ×3, texto plano ×1). Documentar como componente con props `icon`, `title`, `body` (texto | card), `confirmLabel`.
> 🔴 **Typo en el título: "¿Confirmas la nueva fecha entrega?"** — falta la preposición. Debe ser **"¿Confirmas la nueva fecha de entrega?"** (`606:66022`).

### CC.17.6 🔴 Inconsistencias de datos y copy entre pantallas

Las pantallas del flujo no usan un formato de fecha consistente:

| Elemento | Pantalla 3 | Pantalla 4 (modal) |
|---|---|---|
| **Formato** | `12 de nov 2024` | `14/02/2025` 🔴 |

> 🔴 **Dos formatos de fecha conviviendo:** `12 de nov 2024` (largo, es-MX) en el select y `14/02/2025` (numérico DD/MM/AAAA) en el modal. **Definir el formato canónico** de fecha de la App y aplicarlo. Nota: §CC.8 documenta "DD/MM/AAAA" como placeholder en el drawer de filtros, y §CC.6 usa "15 ago - 2:24 hrs" en las tarjetas — ya hay al menos **tres formatos** en el módulo.

### CC.17.7 Componentes nuevos (vs. ya documentados)

- **Date picker** (`Frame 2147224763`) — popup centrado con navegación mes/año, grilla 7×6, día seleccionado en círculo rojo, acciones Cancelar/Seleccionar. **Componente compartido** (instancia), primero documentado en la App. ⚠️ Arrastra tres fugas de token (Manrope, `#242C2E`, `#E7E7E7`).
- **Select de fecha** (input r20 con chevron que abre el picker) — §CC.17.2.

Reutiliza: **bottom sheet** (§CC.16.2, idéntico), **card dirección + botón "Cambiar"** (§CC.16.2, idéntica), **modal de confirmación** (§CC.14.7, cuarta instancia — ahora con ícono y cuerpo parametrizados).

### CC.17.8 Pendientes (🔴)

1. 🔴 **Dos formatos de fecha** (`12 de nov 2024` vs `14/02/2025`) — definir formato canónico de la App (§CC.17.6).
2. 🔴 **Typo "la nueva fecha entrega"** → "la nueva fecha **de** entrega" (`606:66022`) (§CC.17.5).
3. 🔴 **Manrope en el date picker** (mes y año) — nueva instancia, y **se propaga** por ser componente compartido (§CC.17.4).
4. 🔴 **`#242C2E` fuera de paleta** en días y selectores del picker (§CC.17.4).
5. 🔴 **`#E7E7E7` fuera de paleta** en los pills de mes/año (§CC.17.4).
6. 🔴 **Sin restricción de fechas** en el picker — falta el estado visual de "día no disponible" (§CC.17.4).
7. 🔴 **Backdrop en inglés — 4ª instancia** (`image 346`, mismo asset que §CC.16). Confirma el set EN del módulo (§CC.16.5).
8. 🔴 **Sin pantalla de éxito** — **4 de 4 flujos** sin cierre documentado.
9. ⚠️ **Métricas del select** (`border 1px`, `px20/py18`) difieren de los inputs de §CC.14.4 (`0.916px`, `px18.321`). Este está limpio; usarlo como referencia al unificar (§CC.17.2).
10. ⚠️ **Motivos que habilitan esta acción** sin confirmar (§CC.7).

### CC.17.10 Referencias

- *Reschedule Delivery* (`614:38094`).
- **Sheet vacío:** `606:65878` (contenido `606:65901`) · **con picker:** `615:38459` · **fecha capturada:** `615:38725` (contenido `615:38728`).
- **Date picker:** `615:38492` (instancia de `Frame 2147224763`; mes `I615:38492;108:29883`, año `I615:38492;108:29875`, día seleccionado `I615:38492;108:29911`).
- **Select de fecha:** `606:65913` (vacío) / `615:38742` (lleno, valor `615:38744`).
- **Card dirección:** `615:38734` (botón "Cambiar" `615:38739`).
- **Modal:** `606:65979` (contenido `606:66015`; ícono `606:66167`, título `606:66022`, fecha `606:66023`, acciones `606:66025` / `606:66026`).
- **Backdrops EN (bug):** `606:65876` · `615:38460` · `615:38726` · `606:65980` (`image 346`).
- **Anotaciones del diseñador:** `615:39623` (destino de "Cambiar") · `615:39238` ("Selecciona fecha") · `615:39240` ("Da clic en continuar").

---

## CC.18 Control de calidad — Acción "Recolección en sucursal" + **Menú de acciones** (§CC.18)

> **Sección "Pickup at Branch"** (`615:38102`). **Quinto flujo de acción** de los pendientes en §CC.11 (punto 3). Envía el paquete a una sucursal para que el destinatario lo recoja.
> **Esta sección cierra además el hueco mayor de §CC.11: contiene el menú de acciones** que origina todos los flujos, y **el detalle de incidencia con su estado final** tras ejecutar una acción.
> 6 pantallas: detalle con menú abierto · selección de sucursal · modal · 2 estados de popup de error · detalle en estado final.
> **Figma:** `615:38102`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.18.1 Mapa del flujo

```
Detalle de incidencia INC-00103 (1060:20289)
│  tap more-horizontal (1060:20355)
│
├── MENÚ DE ACCIONES (1060:20359) ⭐
│   📍 location-04  · Cambiar dirección       ──▶ §CC.14
│   🏪 store-03     · Recolección en sucursal ──▶ este flujo
│   ↻  refresh-01   · Devolver al remitente   ──▶ §CC.16
│
├── SELECCIÓN DE SUCURSAL (1060:20151)
│   Header "Recolección en sucursal [DHL]"
│   Mapa + copy + radio-cards + CTA "Confirmar"
│   │
│   ├── tap "Confirmar" ──▶ MODAL (1060:20214)
│   │       "¿Estás seguro de que prefieres recogerlo en la sucursal?"
│   │       [Cancelar] [Sí, confirmar]
│   │
│   └── sin sucursales ──▶ POPUP DE ERROR
│           CP vacío (1060:20233) · CP escrito (1060:20261)
│
└── DETALLE — ESTADO FINAL (1060:20426)
    Chip de motivo reemplazado por chip de acción: "Enviar a sucursal" (morado)
```

### CC.18.2 ⭐ Menú de acciones — `1060:20359`

**Cierra el pendiente §CC.11 punto 3 y §CC.16.8 #8.** Es el menú que despliega el `more-horizontal` del detalle, esquina superior derecha del header `INC-00103`.

- **Contenedor:** blanco, borde `1px #F8F8F8` (Greys/900), **r16**, `p16`, **gap 16**, sombra `0 4px 6.3px rgba(0,0,0,.1)`. Ancho 183, alto 140.
- **Ítems** (gap 8): ícono 16px + label `B3 M` 12 Medium negro.

| # | Ícono | Label | Deriva a |
|---|---|---|---|
| 1 | `location-04` | **Cambiar dirección** | §CC.14 |
| 2 | `store-03` | **Recolección en sucursal** | §CC.18 (este) |
| 3 | `refresh-01` | **Devolver al remitente** | §CC.16 |

> ✅ **Es exactamente el mismo componente de menú kebab documentado en §P.6** (Productos): `bg white`, borde `1px #F8F8F8`, **r16**, `p16`, `gap 16`, sombra `0 4px 6.3px rgba(0,0,0,.1)`, ítems con ícono 16 + `B3 M` 12. **Confirma que §P.6 es el patrón transversal de menú kebab de la App**, tal como se anticipó ahí. No es un componente nuevo.

### CC.18.3 ⭐ Detalle de incidencia — variante "Resumen de envío" — `1060:20289` / `1060:20426`

**Esta pantalla no coincide con el detalle documentado en §CC.9.** Son dos estructuras distintas:

| | §CC.9 (`4206:37050`) | §CC.18 (`1060:20289`) |
|---|---|---|
| **Bloques** | Estado · Situación actual · Fecha última actualización · Solución estimada · DETALLE DE ENVÍO · DIRECCIONES origen/destino · HISTORIAL timeline | **Resumen de envío** (colapsable) · Estado · Tipo de incidencia · Solución estimada · Servicio · Fechas · Paquetes · Dimensiones · Peso · Costo · Seguro |
| **Direcciones** | Sí (origen y destino) | **No** |
| **Historial** | Sí (timeline agrupado) | **No** |
| **Colapsable** | No | **Sí** (`arrow-down-01-sharp` `1060:20297`) |
| **Chip carrier** | — | **Sí** (motivo / acción) |

Estructura de esta variante:
- **Header:** back + **"INC-00103"** + **`more-horizontal`** (abre §CC.18.2).
- **"Resumen de envío"** con chevron colapsable.
- **Fila de carrier:** `dhl-iso` 40×40 (r5) + guía **"774523209"** (`B2 S` 14) + **chip** + **"1 paquete"** (`B3 M` 12 `#4C4C4C`, derecha).
- **Divisor**, luego **Estado** + chip "Envío en proceso".
- **Pares label/valor** (label `B2 S`-ish 14, valor 12 gris, gap 21, bloques de 66px): Tipo de incidencia (*Cambio de dirección*) · Solución estimada (*10 días hábiles*) · Servicio: (*Económico / 2 días*) · Fecha de creación (*08/02/2025*) · Fecha estimada de entrega (*09/02/2025*) · Número de paquetes: (*1*) · Paquete (*45 x 30 x 25 cm*) · Peso total: (*6 kg*) · Costo (*$345.00*) · Seguro: (*No contratado*).

### CC.18.4 🔴 Sistema de chips ampliado — dos familias nuevas

El detalle usa **dos chips que no están en el catálogo de §CC.7** (que solo cubría Requiere acción rojo / En proceso gris / Finalizada verde). Ambos comparten geometría: **r6**, `px6/py4`, label `B3 M` 12 Medium.

| Chip | Rol | Fondo | Texto | Nodo |
|---|---|---|---|---|
| **"Dirección incorrecta o incompleta"** | **Motivo** de la incidencia | `#FFF5F0` (Orange/500) | `#FF6700` (Orange/300) | `1060:20304` |
| **"Enviar a sucursal"** | **Acción** de resolución aplicada | `#F5EFFF` (Purple/500) | `#7C3AED` (Purple/300) | `1060:20441` |

**El chip cambia de motivo a acción tras ejecutar el flujo**: es el indicador de que la acción se aplicó.

> ✅ **Esto responde parcialmente el pendiente "sin pantalla de éxito"** que arrastran §CC.14–§CC.17. **No hay pantalla de éxito: el cierre es el retorno al detalle con el chip de acción actualizado.** Actualizar el pendiente en los cuatro flujos anteriores.
> 🔴 **Catálogo de estados de §CC.7 incompleto.** Faltan las familias **naranja (motivo)** y **morada (acción)**. Son ejes distintos del estado de incidencia: un mismo INC tiene *estado* (Envío en proceso), *motivo* (naranja) y *acción aplicada* (morado). Documentar los tres ejes por separado.
> 🔴 **Escala de tokens invertida.** `Orange/300 = #FF6700` (oscuro) y `Orange/500 = #FFF5F0` (claro); igual `Purple/300 = #7C3AED` oscuro y `Purple/500 = #F5EFFF` claro. Es **al revés** de la convención de la App, donde el número mayor es más oscuro (`Primary/600 = #DB3B2B` oscuro, `Primary/100 = #FFF0EF` claro). Corregir la nomenclatura en las variables de Figma o documentar la excepción.

### CC.18.5 Selección de sucursal — `1060:20151`

**Idéntica a §CC.15.2–§CC.15.6** salvo el título: mapa 328×238 r12 con controles glassmorphism y "Abrir en Mapas", copy explicativo, tres radio-cards de sucursal (borde `#DB3B2B` la seleccionada), CTA "Confirmar" full-width.

- **Header** (`1060:20209`): **"Recolección en sucursal"** + logo DHL inline. A diferencia de §CC.15.2, el título ocupa **dos líneas** (h42 vs h19) porque es más largo.

> ⚠️ **El título a dos líneas desplaza el layout** del header respecto a §CC.15. Confirmar que el componente de header soporte 1 y 2 líneas sin romper el centrado.

### CC.18.7 Modal de confirmación — `1060:20214`

**Quinta instancia**, y aporta una variación nueva:

- **Círculo del ícono en `#FFF0EF` (Primary/100) con `refresh-01` en rojo** — las cuatro instancias anteriores (§CC.14.7, §CC.15.7, §CC.16.4, §CC.17.5) usan círculo **gris `#F8F8F8`** con ícono oscuro.
- Título "¿Estás seguro de que prefieres recogerlo en la sucursal?" · cuerpo "Tu envío será enviado a la siguiente sucursal" · card r12 **h119** con dirección + horario + botón copiar · **[Cancelar] [Sí, confirmar]**.

> ✅ **Tercer eje de parametrización del modal confirmado: el color del círculo del ícono** (gris `#F8F8F8` ×4 · rojo `#FFF0EF` ×1), además de ícono y tipo de cuerpo (§CC.17.5). Props sugeridas: `icon`, `iconTone` (neutral | danger), `title`, `body` (texto | card), `confirmLabel`.
> 🔴 **Pero no hay criterio visible para el tono.** §CC.15.7 es el **mismo modal, mismo copy**, y usa círculo gris; este usa rojo. Definir cuándo aplica cada tono (¿acción destructiva vs. reversible?) o unificar.

### CC.18.8 Popup de error — `1060:20233` / `1060:20261`

Idéntico a §CC.15.8 (mensaje + input CP r20 + "Validar" en dos estados + divisor + escapes "Cambiar dirección" / "Devolver al origen" + "Cancelar"), con una diferencia: el **título ocupa dos líneas** (h52 vs h26).

> 🔴 Arrastra los mismos bugs de §CC.15.8: placeholder `[#####]` sin resolver, fondo `rgba(244,244,244,0)` en los escapes, tres radios de botón (r20/r8/r12).

### CC.18.9 Componentes nuevos (vs. ya documentados)

- **Chip de motivo** (naranja `#FFF5F0`/`#FF6700`) y **chip de acción** (morado `#F5EFFF`/`#7C3AED`) — §CC.18.4. Amplían el catálogo de §CC.7.
- **Detalle de incidencia variante "Resumen de envío"** (colapsable, con chip de carrier y pares label/valor) — §CC.18.3. **Puede reemplazar a §CC.9.**

Reutiliza: **menú kebab de §P.6** (idéntico, no es nuevo), mapa + radio-cards + CTA de §CC.15, modal de confirmación (5ª instancia), popup de error de §CC.15.8.

### CC.18.10 Pendientes (🔴)

1. 🔴 **Catálogo de chips de §CC.7 incompleto** — faltan familias naranja (motivo) y morada (acción); son tres ejes distintos, no uno (§CC.18.4).
2. 🔴 **Escala de tokens invertida** en Orange y Purple (300 = oscuro, 500 = claro) vs. la convención de la App (§CC.18.4).
3. 🔴 **Sin criterio para el tono del círculo del modal** (gris vs. rojo) con copy idéntico (§CC.18.7).
4. 🔴 Arrastra los bugs de §CC.15.8: `[#####]`, `rgba(244,244,244,0)`, tres radios (§CC.18.8).
5. ⚠️ **Header a dos líneas** — confirmar que el componente lo soporte (§CC.18.5).

### CC.18.11 ✅ Resuelto en esta sección

| Pendiente | Origen | Resolución |
|---|---|---|
| **Menú de acciones sin documentar** | §CC.11 #3, §CC.16.8 #8 | ✅ `1060:20359` — es el componente de §P.6, con 3 ítems motivo-dependientes (§CC.18.2) |
| **Sin pantalla de éxito** | §CC.14.9 #7, §CC.15.10 #10, §CC.16.8 #7, §CC.17.8 #11 | ✅ **No existe pantalla de éxito**: el cierre es el retorno al detalle con el **chip de acción** actualizado (§CC.18.4). Confirmar si además hay toast |

### CC.18.13 Referencias

- *Pickup at Branch* (`615:38102`).
- **Detalle con menú:** `1060:20289` (header `1060:20351`, kebab `1060:20355`) · **Menú:** `1060:20359` (ítems `1060:20360` / `1060:20366` / `1060:20372`; ocultos `1060:20377`–`1060:20419`).
- **Detalle estado final:** `1060:20426` · fila carrier `1060:20436`.
- **Chips:** motivo `1060:20304` (Orange) · acción `1060:20441` (Purple) · estado `1060:20447`.
- **Selección de sucursal:** `1060:20151` (header `1060:20209`, mapa `1060:20157`, radio-cards `1060:20188` / `1060:20194` / `1060:20200`).
- **Modal:** `1060:20214` (contenido `1060:20218`; círculo `1060:20219` `#FFF0EF`).
- **Popup error:** `1060:20233` (CP vacío) · `1060:20261` (CP escrito).
- **Backdrops EN (bug):** `1060:20215` · `1060:20234` · `1060:20262` (`image 348`).
- **Anotaciones del diseñador:** `1060:20498` · `1060:20500` ("Error Popup").

---

## CC.19 Control de calidad — Acción "Solicitar búsqueda" (§CC.19)

> **Sección "Request Search"** (`614:38099`). **Sexto flujo de acción** de los pendientes en §CC.11 (punto 3). Abre una **investigación formal** con la paquetería cuando el paquete se extravía o deja de reportar movimiento.
> 5 pantallas: formulario vacío → lleno (scroll con footer fijo) → validación con error → dropdown de moneda → modal de confirmación.
> **Es el formulario más largo de los flujos de acción** (6 campos, 3 de ellos textarea) y el primero con **selector de moneda** y **footer con degradado**.
> **Figma:** `614:38099`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.19.1 Mapa del flujo

```
Incidencia › menú de acciones › "Solicitar búsqueda"
│
├── 1. FORMULARIO VACÍO (614:37395) — alto 1086
│   Header "Solicitar búsqueda"
│   Descripción del problema (textarea)
│   Descripción del empaque (textarea)
│   Descripción exacta del producto (textarea)
│   Costo · Moneda (select) · Número de piezas
│   CTA "Solicitar búsqueda" DESHABILITADO
│   │
│   ├── tap select Moneda ──▶ 4. DROPDOWN (614:37520 · dropdown 959:54222)
│   │       MXN · USD · EUR · GBP
│   │
│   ├── validación fallida ──▶ 3. ERROR (614:37608) — alto 1260
│   │       "Ingresa la información requerida" (textareas)
│   │       "Este campo es obligatorio" (Costo, Número de piezas)
│   │
│   └── campos completos ──▶ 2. LLENO (614:37473) — alto 804 + degradado
│           CTA HABILITADO
│           │
│           └── tap CTA ──▶
│
└── 5. MODAL DE CONFIRMACIÓN (614:37724)
    Ícono calendar-03 · "¿Estás seguro de que quieres iniciar una búsqueda?"
    "Se iniciará una investigación que puede tardar hasta 20 días hábiles."
    [Cancelar] [Sí, iniciar búsqueda]
```

### CC.19.2 Chrome y estructura

Pantalla completa (arquetipo de §CC.14, no sheet). Status bar + header con back (`majesticons:arrow-up` 24px) + título **"Solicitar búsqueda"** centrado (`T3 S`-ish 16, ancho 140) + divisor a `y=106`. Contenedor `left 16 / top 122 / w 328`, gap 20 entre bloques. CTA full-width 328×48 al fondo.

### CC.19.3 Campos del formulario — `614:37401`

Seis campos, cada uno label (`B2 S` 14 SemiBold `-0.28px` negro) + control, gap **7.328px**.

| # | Campo | Tipo | Alto | Placeholder / valor | Nodo (vacío) |
|---|---|---|---|---|---|
| 1 | Descripción del problema | **textarea** | 152 | *"Describe la situación con detalle. Ejemplo: 'El paquete no ha mostrado actualizaciones en el tracking durante las últimas 24 horas.'"* | `614:37434` |
| 2 | Descripción del empaque | **textarea** | 152 | *"Describe el tipo y estado del empaque externo e interno, por ejemplo: 'Caja de cartón con protección de plástico burbuja, tiene abolladuras en las esquinas.'"* | `614:37465` |
| 3 | Descripción exacta del producto | **textarea** | 152 | *"Especifica la marca, modelo, color y otras características del producto. Ejemplo: 'Smartphone marca XYZ, modelo ABC123, color negro, 128GB.'"* | `614:37470` |
| 4 | Costo | texto | 55 | `$` | `614:37592` |
| 5 | **Moneda** | **select** | 55 | `MXN` | `614:37595` |
| 6 | Número de piezas | texto | 55 | `Ingresa la cantidad` | `614:37600` |

**Textarea:** borde `0.916px #F3F3F3`, **r20**, h152, `p12`.
**Input de texto:** borde `0.916px #F3F3F3`, **r20**, h55, `px18.321/py16.489`, placeholder `#C3C3C3` 11.75 `-0.235px`.
**Select Moneda:** mismo borde y alto, `justify-between`, valor "MXN" a `x=18.32` + `icon/nav/chevron/down` 24px.

> ✅ **Placeholders con ejemplo concreto.** Los tres textareas no solo describen qué escribir, sino que dan un ejemplo entrecomillado. Es el mejor patrón de placeholder del módulo — vale la pena elevarlo a guía de UX writing para campos de texto libre.
> ⚠️ **El select Moneda no usa Manrope** (a diferencia del select Colonia de §CC.14.4). Está en Inter, correcto. Refuerza que la anomalía de §CC.14.4 es un caso puntual, no el comportamiento del componente select.
> ⚠️ **Costo y Moneda son campos separados.** Considerar si conviene un input compuesto (monto + moneda en una fila) para reducir altura del formulario, que ya es de 1086px.

### CC.19.4 Estado de error del formulario — `614:37608`

En el estado de error, el borde pasa a `#DB362B` y aparece el mensaje en `B2 R` 14 Regular `-0.28px` color `#DB3B2B`, gap 7.328.

> ⚠️ **Moneda no muestra error** porque trae "MXN" precargado. Coherente con el resto del formulario.
> ⚠️ **En el estado de error los textareas muestran el placeholder en negro**, no en `#C3C3C3` (`I614:37617;52:7736`). Mismo comportamiento que §CC.14.5 — el texto de ejemplo se ve como valor capturado. Definir el tratamiento del placeholder en estado de error.
> 🔴 **Arrastra el drift de token de §CC.14.5:** borde de error `#DB362B` vs. texto de error y `Primary/600` `#DB3B2B`.

### CC.19.5 Dropdown de moneda — `959:54222`

Popup blanco, borde `1px #F3F3F3`, **r16**, sombra `0 4px 26.2px rgba(0,0,0,.1)`, ancho 328. Se ancla **debajo** del select (a `y=888`, el select está a `y≈810`).

Cada opción: `px16/py12`, divisor inferior `1px #F3F3F3`, con dos líneas:
- **Código** — `B2 M` 14 Medium `-0.28px` negro (`MXN`, `USD`, `EUR`, `GBP`).
- **Nombre** — `B3 M` 12 Medium `#4C4C4C` (`Peso mexicano`, `Dólar estadounidense`, `Euro`, `Libra esterlina`).

> 🔴 **Anchos fijos rompen el texto.** El código tiene `w-[111px]` y el nombre `w-[87px]`, dentro de un contenedor de **296px**. Por eso *"Dólar estadounidense"* se parte en **tres renglones** ("Dólar / estadounide / nse") con corte a media palabra. Ambos deben ser ancho automático o full. **Es el bug más visible del flujo.**
> 🔴 **Cuatro monedas ocultas** (`hidden="true"`): **CAD**, **JPY**, **AUD**, **CNY**. Están apiladas en la misma posición `y=252`. Si el catálogo es dinámico, el dropdown necesita scroll.
> 🔴 **`tick-02` oculto en todas las opciones.** **No hay indicador visual de la opción seleccionada** — el usuario abre el dropdown y no ve cuál está activa. Mostrar el tick en la opción vigente.
> ⚠️ **Sin scroll ni altura máxima.** Con 4 opciones mide 270px; con 8 mediría ~540px y no cabría. Definir `max-height` + scroll.
> ⚠️ **El dropdown no es un componente compartido** (es un frame local), a diferencia del date picker de §CC.17.4. Considerar componentizarlo.

### CC.19.6 Footer con degradado — `614:37606`

En la pantalla de formulario lleno aparece un **rectángulo de 360×100 a `y=704`** justo detrás del CTA, que no existe en las demás pantallas. Es el **degradado de desvanecido** que indica contenido scrolleable bajo el footer fijo.

> ✅ **Primer footer con degradado documentado en los flujos de acción.** Patrón correcto para formularios largos con CTA fijo: el contenido se desvanece al pasar bajo el botón en vez de cortarse en seco. Reutilizable en §CC.14 (que tiene el mismo problema de formulario largo con CTA fijo y **no** lo trae).
> 🔴 **Inconsistente entre pantallas del mismo flujo.** Solo la pantalla 2 lo tiene; las pantallas 1, 3 y 4 no, aunque también tienen contenido bajo el CTA. Aplicarlo en todas o en ninguna.
> 🔴 **Sin especificación de gradiente.** El nodo es un `rounded-rectangle` sin fill documentado en el design context. Definir los stops (probablemente `transparent → #FFFFFF`) y la altura canónica.

### CC.19.7 Modal de confirmación — `614:37724`

**Sexta instancia.** Círculo `#F8F8F8` (gris) con **`calendar-03`** 32px:
- **Título:** "¿Estás seguro de que quieres iniciar una búsqueda?" — `T2 S` 20 SemiBold `lh 1.3` `-0.4px`, centrado, en 2 líneas explícitas.
- **Cuerpo:** "Se iniciará una investigación que puede tardar hasta **20 días hábiles**." — `B2 R` 14 `#4C4C4C`, centrado. **Con punto final** (a diferencia de §CC.15.7 y §CC.16.4, que no lo llevan).
- **Sin card de dato citado** — como §CC.17.5, el cuerpo es texto plano.
- **Acciones** (gap 5, h40, r12): **"Cancelar"** blanco borde 1.25px `B2 M`; **"Sí, iniciar búsqueda"** `#DB3B2B` `B2 S` blanco.

> 🔴 **Ícono semánticamente incorrecto.** `calendar-03` es un calendario, y aquí se usa para *iniciar una búsqueda*. Tiene sentido en §CC.17 (reagendar, que sí es una fecha), pero no aquí — probablemente se copió de ahí. Debería ser un ícono de búsqueda/investigación (`search-01`, `file-search`) o de alerta. **Segundo modal con `calendar-03`, primero donde no aplica.**
> ✅ **Buen copy de expectativa.** Es el único modal del módulo que **advierte del costo temporal** de la acción antes de confirmarla. Patrón a replicar en acciones de plazo largo.

### CC.19.8 Componentes nuevos (vs. ya documentados)

- **Dropdown de selección con código + descripción** (`959:54222`) — lista de opciones en dos líneas con divisores, r16 y sombra `0 4px 26.2px`. Distinto del date picker (§CC.17.4) y del drawer de filtros (§CC.8). **Frame local, conviene componentizar.**
- **Footer con degradado de desvanecido** (`614:37606`) — §CC.19.6.

Reutiliza: pantalla completa con header + CTA fijo (§CC.14), textarea/input r20, modal de confirmación (6ª instancia).

### CC.19.9 Pendientes (🔴)

1. 🔴 **Anchos fijos rompen el texto del dropdown** (`w-[111px]` / `w-[87px]` en contenedor de 296px) — "Dólar estadounidense" se parte en 3 renglones con corte a media palabra (§CC.19.5).
2. 🔴 **`tick-02` oculto en todas las opciones** — no hay indicador de selección en el dropdown (§CC.19.5).
3. 🔴 **Ícono `calendar-03` en un modal de búsqueda** — semánticamente incorrecto, probablemente copiado de §CC.17 (§CC.19.7).
4. 🔴 **Degradado del footer solo en 1 de 4 pantallas** y sin especificación de gradiente (§CC.19.6).
5. 🔴 **Placeholder en negro en estado de error** — se lee como valor capturado (§CC.19.4).
6. 🔴 Arrastra el **drift del token de error** (`#DB362B` borde vs. `#DB3B2B` texto) de §CC.14.5.
7. 🔴 **Backdrop en inglés — 5ª instancia** (`image 349`, `614:37722`).
8. ⚠️ **Dropdown sin `max-height` ni scroll** — con 8 monedas no cabría (§CC.19.5).
9. ⚠️ **Costo y Moneda como campos separados** — considerar input compuesto (§CC.19.3).

### CC.19.11 Referencias

- *Request Search* (`614:38099`).
- **Vacío:** `614:37395` (contenedor `614:37401`, CTA `614:37435`) · **Lleno:** `614:37473` (degradado `614:37606`, CTA `614:37489`).
- **Error:** `614:37608` (mensajes `614:37658` / `614:37660` / `614:37657` / `614:37661` / `614:37659`).
- **Dropdown moneda:** `614:37520` (dropdown `959:54222`; opciones `959:54224` MXN · `959:54340` USD · `959:54348` EUR · `959:54356` GBP; ocultas `959:54364` CAD · `959:54332` JPY · `959:54380` AUD · `959:54372` CNY; ticks ocultos `959:54228` / `959:54344` / `959:54352` / `959:54360`).
- **Modal:** `614:37724` (contenido `614:37726`; ícono `614:37729`, título `614:37735`, cuerpo `614:37736`, acciones `614:37738` / `614:37739`).
- **Backdrop EN (bug):** `614:37722` (`image 349`).

---

## CC.20 Control de calidad — Acción "Intentar nueva entrega" (§CC.20)

> **Frame "Attempt New Delivery"** (`614:37749`). **Séptimo flujo de acción** de los pendientes en §CC.11 (punto 3). Pide a la paquetería que reintente la entrega en la misma dirección.
> **Una sola pantalla: un modal.** Es el flujo más corto del módulo — no hay formulario, selección ni paso intermedio.
> ⚠️ A diferencia de las demás acciones, **no es una `<section>` sino un `<frame>` suelto** en el canvas.
> **Figma:** `614:37749`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.20.1 Mapa del flujo

```
Incidencia › menú de acciones › "Intentar nueva entrega"
│
└── MODAL ÚNICO (614:37749)
    Ícono container-truck-01
    Título "Intentar nueva entrega"
    "¿Confirmas que el paquete debe enviarse de nuevo a tu dirección de entrega?"
    Card "Dirección de destino" + botón "Cambiar" ──▶ §CC.14
    [Cancelar] [Sí, reintentar]
```

Sin anotaciones del diseñador en este frame.

### CC.20.2 Modal — `614:37749` / `614:37752`

**Séptima instancia** del modal de confirmación, con dos variaciones estructurales nuevas.

- **Contenedor:** blanco r16, gap 24, ancho 328, contenido 299, bloque interno 278.
- **Ícono:** **`container-truck-01`** 32px en círculo `#F8F8F8` (Greys/900) de 64px (r61).
- **Título:** **"Intentar nueva entrega"** — `T2 S` 20 SemiBold `lh 1.3` `-0.4px`, centrado.
- **Cuerpo:** "¿Confirmas que el paquete debe enviarse de nuevo a tu dirección de entrega?" — `B2 R` 14 Regular `-0.28px` `#4C4C4C`, centrado.
- **Card de dirección** (`614:37817`) — blanco r12, borde `#F3F3F3`, **h130**, `overflow-clip`:
  - **"Dirección de destino"** — 14 negro `-0.28px`, **peso Bold (700)** ⚠️ ver §CC.20.4.
  - Dirección — `B3 R` 12 Regular `#4C4C4C`.
  - **Botón "Cambiar"** — blanco, borde `#F3F3F3`, **r8**, h32, w101, `B3 M` 12 negro. Deriva a §CC.14 (patrón confirmado en §CC.17.3).
- **Acciones** (gap 5, h40, **r12**): **"Cancelar"** blanco borde 1.25px `B2 M` 14; **"Sí, reintentar"** `#DB3B2B` `B2 S` 14 SemiBold blanco.

> ✅ **Tercer ícono distinto del modal.** Van `refresh-01` (§CC.14, §CC.15, §CC.16, §CC.18), `calendar-03` (§CC.17, §CC.19) y ahora `container-truck-01`. Aquí **sí es semánticamente correcto** — camión para reintento de entrega. Refuerza que el ícono debe ser prop del componente (§CC.17.5).
> ✅ **Nueva variante de cuerpo: card con botón de acción.** Las instancias previas usaban card con **botón copiar** (dato citado, §CC.14.7) o texto plano (§CC.17.5, §CC.19.7). Esta usa la **card editable de §CC.16.2** (título + dirección + "Cambiar") dentro de un modal centrado. Ya son **tres tipos de cuerpo**: `texto` · `card-dato` (copiar) · `card-editable` ("Cambiar").

### CC.20.3 🔴 Título afirmativo + pregunta en el cuerpo — estructura distinta

Este modal invierte la estructura de todos los demás:

| Instancia | Título | Cuerpo |
|---|---|---|
| §CC.14.7 | ¿Estás seguro de que esta es la dirección correcta? | Tu envío será enviado a la siguiente dirección: |
| §CC.15.7 | ¿Estás seguro de que prefieres recogerlo en la sucursal? | Tu envío será enviado a la siguiente sucursal |
| §CC.16.4 | ¿Estás seguro de que quieres devolver al origen? | Tu envío será enviado a la siguiente dirección |
| §CC.17.5 | ¿Confirmas la nueva fecha entrega? | 14/02/2025 |
| §CC.19.7 | ¿Estás seguro de que quieres iniciar una búsqueda? | Se iniciará una investigación… |
| **§CC.20** | **Intentar nueva entrega** *(afirmativo)* | **¿Confirmas que el paquete debe enviarse de nuevo…?** *(pregunta)* |

> 🔴 **Es el único modal cuyo título no es la pregunta.** El título repite el nombre de la acción y la pregunta baja al cuerpo. Nota: **es la misma estructura del bottom sheet de §CC.16.2** ("Devolver al origen" + "¿Confirmas que el paquete debe devolverse al origen?"), lo que sugiere que este modal se construyó a partir de un sheet convertido a modal centrado.
> **Decisión de sistema pendiente:** ¿el título del confirmador es la pregunta o el nombre de la acción? Unificar; hoy conviven ambos patrones.

### CC.20.4 🔴 Bugs de la card

**1 — Contenido desbordado y recortado.**
La card mide **278px** de ancho (`w-full` del contenedor de 278), pero su contenido interno está en `left: 11px` con `width: 272px` → **11 + 272 = 283px**, es decir **5px de desbordamiento**. Como la card tiene `overflow-clip`, **el texto se recorta a la derecha**: en la captura se ve *"San Simón Tolnahuac"* y *"Cuauhtémoc,"* cortados al borde.

> 🔴 **Causa:** es la **misma card de §CC.16.2 y §CC.17.2**, donde el contenedor mide **328px** (11 + 272 = 283 < 328 ✓). Al reutilizarla en un contenedor de 278px no se ajustó el ancho interno. **Corregir:** contenido a `width: 100%` con padding, o reducir a 256px.
> Es el mismo tipo de fallo que el dropdown de §CC.19.5 (anchos fijos que no se adaptan al contenedor). **Segundo caso del mismo patrón** — vale la pena revisar todos los componentes con anchos absolutos.

**2 — Peso tipográfico inconsistente.**
El título "Dirección de destino" usa **Inter Bold (700)** — token `B2/B2 B` — mientras que la **misma card** en §CC.16.2 (`606:66106`) y §CC.17.2 (`615:38737`) usa **Inter SemiBold (600)** — token `B2 S`.

> 🔴 Un mismo componente con dos pesos según dónde se instancie. Unificar a `B2 S` (600), que es el usado en las otras dos instancias y el estándar de títulos de card en el módulo.

### CC.20.5 Componentes nuevos (vs. ya documentados)

Ninguno. Este flujo **solo recombina** piezas existentes: modal de confirmación (7ª instancia), card de dirección editable de §CC.16.2, botones `Cancelar` / afirmativo.

Aporta dos variaciones del modal ya documentado: **ícono `container-truck-01`** y **cuerpo tipo card-editable**.

### CC.20.6 Pendientes (🔴)

1. 🔴 **Contenido de la card desbordado 5px y recortado** (w272 + left11 en card de 278) — el texto de dirección se corta a la derecha (§CC.20.4).
2. 🔴 **Peso Bold (700) en el título de la card** vs. SemiBold (600) en §CC.16.2 y §CC.17.2 (§CC.20.4).
3. 🔴 **Título afirmativo con pregunta en el cuerpo** — único caso; decidir el patrón del confirmador (§CC.20.3).
4. 🔴 **Backdrop en inglés — 6ª instancia** (`image 346`, `614:37750`; mismo asset que §CC.16 y §CC.17).
5. 🔴 **Sin estado de carga ni confirmación posterior.** Es un modal único: al confirmar no hay más pantallas documentadas.
6. ⚠️ **Es un frame suelto, no una `<section>`** como los demás flujos (§CC.14–§CC.19). Normalizar la organización del archivo.
7. ⚠️ **Sin anotaciones del diseñador** en el frame, a diferencia de §CC.16 y §CC.17.

### CC.20.8 Referencias

- *Attempt New Delivery* (`614:37749`) — frame suelto, no `<section>`.
- **Modal:** contenedor `614:37751` · contenido `614:37752` · bloque `614:37753`.
- **Ícono:** `614:37828` (`container-truck-01`) en círculo `614:37754`.
- **Título:** `614:37759` · **Cuerpo:** `614:37760`.
- **Card:** `614:37817` (contenido `614:37818`; título `614:37820`, dirección `614:37821`, botón "Cambiar" `614:37822`).
- **Acciones:** `614:37766` (Cancelar) · `614:37767` (Sí, reintentar).
- **Backdrop EN (bug):** `614:37750` (`image 346`).

---

## CC.21 Control de calidad — Acción "Agregar detalles de acceso" (§CC.21)

> **Sección "Add Access Details"** (`614:38095`). **Octavo y último flujo de acción** de los pendientes en §CC.11 (punto 3). Permite añadir instrucciones de acceso al domicilio (códigos, contacto de portería, horarios) para que la paquetería complete la entrega.
> **2 pantallas: bottom sheet vacío → sheet con referencia capturada.** Sin modal de confirmación.
> **Con esta sección se completan las 8 acciones de §CC.11 punto 3** — ver el cierre consolidado en §CC.21.6.
> **Figma:** `614:38095`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.21.1 Mapa del flujo

```
Incidencia › menú de acciones › "Agregar detalles de acceso"
│
├── 1. BOTTOM SHEET — vacío (606:66036)
│   "Agregar detalles de acceso" + cancel-01
│   "Agrega referencias o instrucciones para facilitar el acceso
│    (códigos, contacto, horarios, etc.)."
│   Referencia (textarea con placeholder ejemplificado)
│   CTA "Guardar" DESHABILITADO (#F1B0A9)
│   │
│   └── captura de texto ──▶
│
└── 2. BOTTOM SHEET — con referencia (615:39577)
    Textarea con valor · CTA "Guardar" HABILITADO (#DB3B2B)
```

> ✅ **Es el único flujo sin modal de confirmación.** Coherente: agregar una referencia es una acción **no destructiva y reversible**, a diferencia de devolver al origen o iniciar una investigación de 20 días. **Este es el criterio que faltaba** para el pendiente "¿cuándo lleva confirmación?" — vale la pena documentarlo como regla: *acciones reversibles guardan directo; acciones irreversibles o de plazo largo confirman*.

### CC.21.2 Bottom sheet — `606:66036` / `606:66038`

Mismo arquetipo de §CC.16.2 y §CC.17.2, anclado al fondo (`y=471` sobre 780, ocupa los 307px inferiores):

- **Contenedor:** blanco, **radio superior 16px** (esquinas inferiores rectas), `p16`, gap 24, ancho completo 360 (contenido 328).
- **Header** (`606:66041`): título **"Agregar detalles de acceso"** — `T2 S` 20 SemiBold `lh 1.3` `-0.4px`, ancho 265 — + **`cancel-01`** 24px, `items-start`.
- **Descripción** (`606:66075`): "Agrega referencias o instrucciones para facilitar el acceso (códigos, contacto, horarios, etc.)." — `B2 R` 14 Regular `-0.28px` `#4C4C4C`. Gap 8 respecto al header.
- **Campo Referencia** (`606:66051`, gap **7.328px**):
  - **Label** "Referencia" — `B2 S` 14 SemiBold `-0.28px` negro.
  - **Textarea** (`606:66053`) — borde **`1px #F3F3F3`**, **r20**, **h103**, `p12`.
    - **Placeholder:** *"Ej. Entrada por la calle lateral, código 1234#, llamar a recepción al 555-123-4567."* — `B2 R` **14** `-0.28px` `#C3C3C3`.
    - **Valor:** *"Entrada por la calle lateral, código 1234#, llamar a recepción al 555-123-4567."* — `B2 R` **14** `-0.28px` **negro**.
- **CTA "Guardar"** (`606:66057`) — full-width, h40, **r12**, label `B2 S` 14 SemiBold blanco.

| Estado CTA | Fondo | Cuándo |
|---|---|---|
| **Deshabilitado** | `#F1B0A9` (Primary/300) | Sin referencia capturada |
| **Habilitado** | `#DB3B2B` (Primary/600) | Con referencia capturada |

### CC.21.3 🔴 Métricas del textarea inconsistentes con el resto del módulo

Este textarea difiere de todos los demás documentados:

| Propiedad | §CC.14.4 (Referencias) | §CC.19.3 (descripciones) | **§CC.21** |
|---|---|---|---|
| Borde | `0.916px` | `0.916px` | **`1px`** |
| Radio | 20 | 20 | 20 ✓ |
| Alto | 152 | 152 | **103** |
| Padding | 12 | 12 | 12 ✓ |
| Tamaño de texto | **11.75px** | **11.75px** | **14px** |
| Tracking | `-0.235px` | `-0.235px` | **`-0.28px`** |

> ✅ **Este es el correcto.** Borde `1px` y texto `B2 R` 14 `-0.28px` son valores limpios de token; los `0.916px` / `11.75px` / `-0.235px` de §CC.14 y §CC.19 son **escalado horneado** de instancias con transform (patrón ya identificado en el módulo). **Usar §CC.21 como referencia canónica del textarea** al unificar.
> ⚠️ **Alto 103 vs. 152.** Aquí el campo es más bajo porque el sheet tiene espacio limitado. Definir si el textarea tiene altura fija por contexto o si debe crecer con el contenido.
> ⚠️ **El contenido interno tiene ancho fijo 267px** (`606:66054` / `4206:37296`) dentro de un textarea de 328 con `p12` (área útil 304). No recorta —267 < 304— pero es el **mismo patrón de ancho absoluto** de §CC.19.5 y §CC.20.4. Cambiar a ancho automático por consistencia.

### CC.21.4 Componentes nuevos (vs. ya documentados)

Ninguno. Recombina: **bottom sheet** (§CC.16.2, idéntico), **textarea r20**, **CTA full-width r12** con estados Primary/300 ↔ Primary/600.

Aporta el **textarea con métricas limpias** (§CC.21.3) como referencia canónica.

### CC.21.5 Pendientes (🔴)

1. 🔴 **Sin estado de validación.** No hay pantalla ni mensaje de error definido para el campo Referencia (§CC.21.1).
2. 🔴 **Sin límite de caracteres.** Un textarea de instrucciones de acceso necesita `maxlength` y contador visual.
3. 🔴 **Sin confirmación de guardado.** El flujo termina en "Guardar" sin toast ni pantalla de retorno documentada.
4. 🔴 **Backdrop en inglés — 7ª instancia** (`image 346`, `606:66037` y `615:39578`; mismo asset que §CC.16, §CC.17 y §CC.20).
5. ⚠️ **Ancho fijo 267px** en el contenido del textarea — mismo patrón de §CC.19.5 y §CC.20.4 (§CC.21.3).
6. ⚠️ **Alto del textarea 103 vs. 152** en otros flujos — definir criterio (§CC.21.3).
7. ⚠️ **Sheet sin handle**, igual que §CC.16.2 (§CC.16.8 #6).

### CC.21.6 ✅ Cierre del catálogo de acciones (§CC.11 punto 3)

Con esta sección quedan documentadas **las ocho acciones** listadas en §CC.11 punto 3:

| # | Acción (§CC.11) | Sección | Nombre real en pantalla | Arquetipo | Pantallas | Confirma |
|---|---|---|---|---|---|---|
| 1 | Cambiar dirección | §CC.14 | Cambiar dirección | Pantalla completa | 4 | Modal |
| 2 | Enviar a sucursal | §CC.15 | Enviar a sucursal de [carrier] | Pantalla + popup | 4 | Modal |
| 3 | Retornar al origen | §CC.16 | Devolver al origen | Bottom sheet | 2 | Modal (doble) |
| 4 | Reprogramar entrega | §CC.17 | Reagendar entrega | Bottom sheet + picker | 4 | Modal |
| 5 | Recolección en sucursal | §CC.18 | Recolección en sucursal | Pantalla + popup | 6 | Modal |
| 6 | Solicitar búsqueda | §CC.19 | Solicitar búsqueda | Pantalla completa | 5 | Modal |
| 7 | Intentar nueva entrega | §CC.20 | Intentar nueva entrega | Modal único | 1 | — |
| 8 | Agregar detalles de acceso | §CC.21 | Agregar detalles de acceso | Bottom sheet | 2 | **Ninguna** |

**Cuatro arquetipos de UI** conviven en el módulo: pantalla completa (§CC.14, §CC.19), pantalla + popup de error (§CC.15, §CC.18), bottom sheet (§CC.16, §CC.17, §CC.21) y modal único (§CC.20). **Falta documentar el criterio de cuándo usar cada uno.**

**Pendientes transversales de sistema** (afectan a varias secciones, conviene resolverlos de una vez):

- **Modal de confirmación parametrizable** (7 instancias): props `icon` (`refresh-01` ×4 · `calendar-03` ×2 · `container-truck-01` ×1), `iconTone` (gris `#F8F8F8` ×6 · rojo `#FFF0EF` ×1), `title`, `body` (`texto` · `card-dato` · `card-editable`), `confirmLabel`.
- **Anchos absolutos que no se adaptan:** §CC.19.5 (dropdown), §CC.20.4 (card recortada), §CC.21.3 (textarea). **Auditar el conjunto.**
- **Métricas de input/textarea:** conviven `0.916px`/`11.75px`/`-0.235px` (escalado horneado) y `1px`/`14px`/`-0.28px` (limpio). **§CC.21 es la referencia correcta.**
- **Catálogo de chips en tres ejes** (estado · motivo · acción) con escalas Orange/Purple invertidas (§CC.18.4).
- **Criterio de confirmación:** §CC.21 establece que las acciones **reversibles** guardan directo y las **irreversibles o de plazo largo** confirman. Validar y documentar como regla.

### CC.21.8 Referencias

- *Add Access Details* (`614:38095`).
- **Sheet vacío:** `606:66036` (contenido `606:66038`; header `606:66041`, título `606:66042`, descripción `606:66075`, campo `606:66051`, textarea `606:66053`, placeholder `606:66055`, CTA `606:66057`).
- **Sheet con referencia:** `615:39577` (contenido `4206:37284`; campo `4206:37293`, textarea `4206:37295`, valor `4206:37297`, CTA `4206:37298`).
- **Backdrops EN (bug):** `606:66037` · `615:39578` (`image 346`).

---

## CC.22 Control de calidad — Flujo "Reportar incidencia" · Paso 1/2 (§CC.22)

> **Sección "Report Incident"** (`504:18064`). Cubre el **punto 2 de §CC.11**: el flujo de alta de incidencias, la contraparte de los flujos de resolución (§CC.14–§CC.21). El usuario elige un envío, indica el tipo de problema y continúa a un paso 2.
> 4 pantallas: **selector de envío** → **Paso 1/2 colapsado** → **Paso 1/2 con dropdown de tipos** → **Paso 1/2 expandido**.
> ⚠️ **Documenta solo el Paso 1/2.** El indicador dice `PASO 1/2` pero **el paso 2 no está en esta sección** — ver §CC.22.7.
> **Figma:** `504:18064`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.22.1 Mapa del flujo

```
Incidencias › "Reportar incidencia"
│  (entradas: estado vacío §CC.3 · menú more-vertical §CC.5 · CTA del listado §CC.16.6)
│
├── 1. SELECTOR DE ENVÍO (504:36872)
│   Header "Reportar incidencia" + cancel-01 (X, no back)
│   Buscador · Filtro "Período: Mes actual"
│   Lista de tarjetas de envío con radio (selección única)
│   CTA "Reportar incidencia"
│   │
│   └── tap CTA ──▶
│
├── 2. PASO 1/2 — COLAPSADO (504:37912)
│   Header "Reportar incidencia" + back
│   Tab "Tipo de incidencia" · PASO 1/2 · barra de progreso
│   Resumen del envío (carrier + guía + servicio + paquetes) + "Ver más"
│   Select "Tipo de incidencia" · CTA "Continuar" DESHABILITADO
│   │
│   ├── tap select ──▶ 3. DROPDOWN DE TIPOS (4230:37621 · dropdown 4230:37679)
│   │       7 opciones
│   │
│   └── tap "Ver más" ──▶ 4. EXPANDIDO (4230:37545)
│           Costo · Fecha de creación · Fecha estimada · Dimensiones · Peso
│           "Ver menos"
│
└── PASO 2/2 ──▶ 🔴 no documentado (§CC.22.7)
```

### CC.22.2 Pantalla 1 · Selector de envío — `504:36872`

Pantalla completa. Header con título **"Reportar incidencia"** + **`cancel-01`** (X) a la derecha — **no lleva back**, coherente con un flujo modal que se abandona, no se retrocede.

- **Buscador** (`504:37188`) — `search-01` 20px + placeholder "Buscar", alto 40.
- **Filtro de período** (`504:37194`) — label "Período" + control de 246×32 con `calendar-03` 16px + **"Mes actual"** + chevron.
- **Lista de tarjetas** (`504:37718`) — selección única por radio.
- **CTA "Reportar incidencia"** en footer fijo (`4230:37321`, franja de 360×72 con botón 328×40).

#### Tarjeta de envío seleccionable — `504:37719`

Card blanca **r12**, `p16`, **sombra `shadow_card`** (`0 0 5px 1px rgba(0,0,0,.1)`), contenido 296, gap 16:
- **Fila superior:** **radio** `Control` 16px + **logo del carrier** 40×40 (`fedex-logo` r13 `#29007C` · `dhl-iso` r5) + **guía** (`B2 S` 14 SemiBold `-0.28px`) + **chip de estado** + a la derecha `calendar-02` 16px + **fecha** (`B3 M` 12 `#4C4C4C`).
- **Divisor** (`Line 711`).
- **Bloque destinatario:** label **"Destinatario"** (`B3 M` 12 `#4C4C4C`) + **nombre y dirección** en `B3 S` **12 SemiBold** `-0.24px` negro, 2 líneas, alto 48 con `text-ellipsis`.

**Chip "Recolección pendiente"** — `#FFF5F0` (Orange/500) / `#FF6700` (Orange/300), r6, `px6/py4`, `B3 M` 12. **Mismo componente de chip de motivo de §CC.18.4.**

> 🔴 **El chip naranja se usa aquí con otra semántica.** En §CC.18.4 el chip naranja es el **motivo de la incidencia**; aquí es el **estado logístico del envío** ("Recolección pendiente"). Mismo color, dos significados. Se suma al problema de ejes de chip (§CC.18.4): ahora son **cuatro** — estado de incidencia, motivo, acción aplicada y **estado del envío**.
> 🔴 **Dirección del destinatario en SemiBold.** El nombre y la dirección van en `B3 S` 12 **SemiBold**, cuando en todas las demás pantallas del módulo la dirección es `B3 R` 12 **Regular** `#4C4C4C` (§CC.14.3, §CC.16.2, §CC.18.3). Aquí además es **negro**, no gris. Unificar.
> ⚠️ **Cuarta tarjeta con anatomía distinta** (`504:37785`): **sin radio**, con ícono `user-list` junto a "Destinatario", divisor extra (`Line 712`) y un **botón** (`504:37807`). Es una variante que no aparece en el screenshot; confirmar si es un estado alternativo.

### CC.22.3 Pantalla 2 · Paso 1/2 — chrome del wizard — `504:37912`

Header con **back** (`majesticons:arrow-up`) + **"Reportar incidencia"**.

**Indicador de paso** (`4241:13106`) — patrón nuevo en el módulo:
- Fila de 328×40: **"Tipo de incidencia"** (título del paso, 19px de alto) a la izquierda + **"PASO 1/2"** a la derecha (15px).
- **Barra de progreso** (`Rectangle 42477`) — **180×3** sobre un ancho de 360, es decir **50%**, coherente con 1 de 2 pasos.

> ✅ **Primer indicador de paso con barra de progreso** de los flujos de incidencias. §CC.17 y §CC.19 son de un solo paso; el wizard de §EN.9 usa "PASO 1/3" textual. **Aquí la barra da feedback visual del avance** — buen patrón, conviene unificarlo con §EN.9.
> ⚠️ **La barra mide 180 sobre 360** (mitad exacta). Confirmar que en el paso 2 llegue a 360 y que el ancho sea proporcional, no fijo.

### CC.22.4 Resumen del envío colapsable — `4230:37379` / `4230:37555`

Bloque bajo el indicador de paso, con dos estados.

**Colapsado** (`4230:37379`, alto 96):
- **Fila:** `dhl-iso` 40×40 + **guía** "774523209" (`B2 S` 14) + **servicio** "Mismo día / 24H" (`B3 R` 12 `#4C4C4C`) + a la derecha **"1 paquete"** (`B3 M` 12 `#4C4C4C`).
- **Divisor** (`Line 720`, **329px** ⚠️).
- **Toggle "Ver más"** (`4230:37537`) centrado — label `B2 S` 14 SemiBold `#4C4C4C` + `arrow-down-01-sharp` 24px.

**Expandido** (`4230:37555`, alto 261): entre el divisor y el toggle aparecen **cinco pares label/valor** (gap 16, `B2 R` 14 `-0.28px`; label `#4C4C4C`, valor **negro** alineado a la derecha):

| Label | Valor |
|---|---|
| Costo | `$158.00` |
| Fecha de creación | `26 de ene` |
| Fecha estimada de entrega | `26 de ene` |
| Dimensiones | `45 x 30 x 25 cm` |
| Peso | `6kg` |

El toggle cambia a **"Ver menos"** (`4230:37570`).

> ✅ **Patrón "resumen colapsable" bien resuelto** — mantiene el contexto del envío visible sin ocupar toda la pantalla. Reutilizable en otros wizards.
> 🔴 **Divisor de 329px en un contenedor de 328** (`4230:37566`) — desborda 1px. Corregir a 328 o `width: 100%`. Tercer caso del patrón de anchos absolutos (tras §CC.19.5, §CC.20.4).
> 🔴 **"Dimensiones" y "Peso" tienen el label en negro**, mientras "Costo", "Fecha de creación" y "Fecha estimada" lo tienen en `#4C4C4C`. Inconsistencia dentro del mismo bloque (`4230:37614`, `4230:37617` vs. los demás).
> ⚠️ **El toggle usa el componente `Inactive/Default Input`** (`4230:37537`) aunque es un botón de acción, no un campo. Componente mal aplicado; usar un botón de texto.

### CC.22.5 Catálogo de tipos de incidencia — `4230:37679`

Dropdown **componente compartido** (es una *instance*), blanco, borde **`1px #E7E7E7`** (Greys/700), **r16**, sombra `0 4px 26.2px rgba(0,0,0,.1)`, ancho 328, alto 287. Opciones de una sola línea, `px16/py12`, divisor `1px #F3F3F3`, texto `B2 R` **14 Regular** `-0.28px` negro.

**Siete tipos:**

| # | Tipo de incidencia |
|---|---|
| 1 | Cambio de dirección |
| 2 | Paquete sin movimiento |
| 3 | Recolecciones fallidas |
| 4 | Retraso en la entrega |
| 5 | Paquete dañado |
| 6 | Paquete perdido |
| 7 | Paquete abierto o alterado |

> ⚠️ **Borde `#E7E7E7`** aquí vs. **`#F3F3F3`** en el dropdown de moneda de §CC.19.5. **Dos dropdowns con bordes distintos** — y este es componente compartido, aquel es frame local. Unificar y componentizar el de §CC.19.
> ⚠️ **Sin indicador de selección** (no hay tick), igual que §CC.19.5.
> ⚠️ **Sin `max-height` ni scroll** — con 7 opciones mide 287px; si el catálogo crece no cabrá.

### CC.22.6 Select y CTA

**Select "Tipo de incidencia"** (`504:38282`) — label `B2 S`-ish 14 + control r-estándar h55, `px20`, con "Selecciona una opción" y `arrow-down-01-sharp` 24px. Gap 7.328.

> ⚠️ **Usa `arrow-down-01-sharp`** mientras los selects de §CC.14.4 y §CC.17.2 usan `icon/nav/chevron/down`. **Dos íconos de chevron distintos** para el mismo control. Unificar.
> ⚠️ **Ícono izquierdo oculto** (`504:38284`, `4230:37539`, `hidden="true"`) — el componente soporta ícono a la izquierda y aquí no se usa. Normal, pero registrar.

**CTA "Continuar"** (`504:38290`) — full-width 328×40, `#F1B0A9` deshabilitado hasta seleccionar tipo.

### CC.22.7 🔴 El Paso 2/2 no está en esta sección

El indicador dice **PASO 1/2** en las cuatro pantallas, pero **la sección no contiene el paso 2**. No hay pantalla de descripción del problema, adjuntos, resumen ni confirmación.

> 🔴 **Falta localizar y documentar el Paso 2/2.** Presumiblemente pide la descripción del problema (y quizá evidencia fotográfica, dado que hay tipos como *Paquete dañado* y *Paquete abierto o alterado*). Sin él, el flujo de alta queda incompleto y **§CC.11 punto 2 no puede cerrarse**.
> 🔴 **Sin pantalla de éxito** — igual que los flujos de acción (§CC.18.4 estableció que el cierre es el retorno con chip; aquí debería ser la creación del INC-XXXXX).
> ⚠️ **Sin estado vacío del selector.** ¿Qué pasa si no hay envíos en el período elegido? Falta esa pantalla.
> ⚠️ **Sin validación.** No hay estado de error si se intenta continuar sin seleccionar envío o tipo (el CTA deshabilitado lo previene, pero conviene confirmar).

### CC.22.8 Componentes nuevos (vs. ya documentados)

- **Tarjeta de envío seleccionable** (`504:37719`) — radio + carrier + guía + chip + fecha + destinatario, r12 con `shadow_card`. Distinta de la tarjeta de incidencia de §CC.6 y de la radio-card de sucursal de §CC.15.5.
- **Indicador de paso con barra de progreso** (`4241:13106`) — título + "PASO n/m" + barra. **Primero en el módulo.**
- **Resumen de envío colapsable** (`4230:37379` ↔ `4230:37555`) — "Ver más" / "Ver menos".
- **Dropdown de opción simple** (`4230:37679`) — **componente compartido**, una línea por opción. Distinto del de §CC.19.5 (código + descripción, frame local).
- **Filtro de período** (`504:37194`) — control con `calendar-03` + valor + chevron.

Reutiliza: chip Orange (§CC.18.4), `Control` radio (§CC.15.5), CTA full-width.

### CC.22.9 Pendientes (🔴)

1. 🔴 **Paso 2/2 sin localizar ni documentar** — bloquea el cierre de §CC.11 punto 2 (§CC.22.7).
2. 🔴 **Chip naranja con dos semánticas** — estado del envío aquí, motivo en §CC.18.4. Ya son **cuatro ejes de chip** (§CC.22.2).
3. 🔴 **Dirección del destinatario en SemiBold negro** vs. Regular gris en el resto del módulo (§CC.22.2).
4. 🔴 **Divisor de 329px** en contenedor de 328 (`4230:37566`) — tercer caso de ancho absoluto (§CC.22.4).
5. 🔴 **Labels con dos colores** en el mismo bloque de detalles — "Dimensiones" y "Peso" en negro, los demás en `#4C4C4C` (§CC.22.4).
6. 🔴 **Dos dropdowns con bordes distintos** — `#E7E7E7` aquí (compartido) vs. `#F3F3F3` en §CC.19.5 (local). Unificar y componentizar (§CC.22.5).
7. 🔴 **Sin estado vacío del selector** de envíos (§CC.22.7).
8. 🔴 **Sin pantalla de éxito** ni confirmación de creación del INC (§CC.22.7).
9. ⚠️ **Dos íconos de chevron** en selects — `arrow-down-01-sharp` aquí vs. `icon/nav/chevron/down` en §CC.14.4 y §CC.17.2 (§CC.22.6).
10. ⚠️ **Toggle "Ver más" usa el componente `Inactive/Default Input`** en vez de un botón (§CC.22.4).
11. ⚠️ **Cuarta tarjeta con anatomía distinta** (sin radio, con `user-list` y botón) — ¿estado alternativo? (§CC.22.2).
12. ⚠️ **Dropdown sin tick ni `max-height`** (§CC.22.5).

### CC.22.11 Referencias

- *Report Incident* (`504:18064`).
- **Selector:** `504:36872` (buscador `504:37188`, período `504:37194`, lista `504:37718`, footer `4230:37321`).
- **Tarjetas:** `504:37719` (FedEx, seleccionada) · `504:37741` · `504:37763` · `504:37785` (variante sin radio).
- **Paso 1/2 colapsado:** `504:37912` (indicador `4241:13106`, resumen `4230:37379`, toggle `4230:37537`, select `504:38282`, CTA `504:38290`).
- **Paso 1/2 con dropdown:** `4230:37621` (dropdown `4230:37679`).
- **Paso 1/2 expandido:** `4230:37545` (resumen `4230:37555`, detalles `4230:37603`, toggle `4230:37567`).
- **Paso 2/2:** 🔴 no localizado.

---

## CC.23 Control de calidad — Consolidación de hallazgos y plan de resolución (§CC.23)

> Sección transversal. Consolida **todos** los hallazgos de §CC.14–§CC.22 (181 marcadores 🔴 y 80 ⚠️ en el bloque) y los reduce a **54 hallazgos únicos**, eliminando las repeticiones entre secciones.
> **Owner:** Karla Salazar — Head of UX/UI.

### CC.23.1 Método y alcance

Los hallazgos se clasifican por **quién puede resolverlos**:

| Tipo | Qué significa | Cantidad | Estado |
|---|---|---|---|
| ✅ **Resuelto** | Tiene respuesta objetiva derivable del propio sistema (token existente, convención ya documentada, o valor correcto evidente por comparación). Se indica el valor corregido y su fundamento. | **34** | Listo para aplicar |
| 🟠 **Requiere decisión** | Depende de producto o del owner. Se presentan opciones, recomendación e impacto. **No se decide aquí.** | **13** | Listo para decidir |
| ⬜ **Contenido faltante** | No es un error: son pantallas o definiciones que no existen en Figma. | **7** | Requiere diseño |

> ⚠️ **Nada de esta sección se aplicó al diseño.** Es un plan de remediación documental; los cambios en Figma y código los ejecutan sus owners.

---

### CC.23.2 ✅ Resueltos — Tokens y estilos

| # | Hallazgo | Valor actual | **Valor correcto** | Fundamento | Origen |
|---|---|---|---|---|---|
| T1 | Drift del token de error | Borde `#DB362B` · texto `#DB3B2B` | **`#DB3B2B`** (Primary/600) en ambos | El texto de error y `Primary/600` ya son `#DB3B2B`. `#DB362B` solo aparece en el token semántico `background/state-indicators/error`, sin uso propio. Apuntar el token a Primary/600. | §CC.14.5, §CC.19.4 |
| T2 | Métricas de input/textarea | `0.916px` / `11.75px` / `-0.235px` | **`1px` / `14px` / `-0.28px`** | Principio ya documentado: los valores no redondos indican **escalado horneado** en instancias con transform, no tokens intencionales. §CC.21.3 tiene las métricas limpias. | §CC.14.4, §CC.19.3, §CC.21.3 |
| T3 | Radio del select Colonia | `18.321px` | **`20px`** | `18.321 = 20 × 0.916` — es el mismo escalado horneado de T2. | §CC.14.4 |
| T4 | Manrope fuera de Nova | Manrope en KPIs, select Colonia, mes/año del date picker | **Inter** | Principio ya documentado: la App usa Inter exclusivamente fuera de Nova. Tres instancias confirmadas; la del date picker **se propaga** por ser componente compartido. | §CC.4, §CC.14.4, §CC.17.4 |
| T5 | Color fuera de paleta (date picker) | `#242C2E` en días y selectores | **`#000000`** (Text/Text Dark) | `#242C2E` no existe en los tokens de la App. | §CC.17.4 |
| T6 | Borde fuera de paleta (date picker) | `#E7E7E7` en pills mes/año | **`#F3F3F3`** (Greys/800) | Greys/800 es el borde estándar de la App. | §CC.17.4 |
| T7 | Bordes de dropdown divergentes | `#E7E7E7` (§CC.22) vs `#F3F3F3` (§CC.19) | **`#F3F3F3`** (Greys/800) | Mismo fundamento que T6. | §CC.19.5, §CC.22.5 |
| T8 | Fill con alpha 0 | `rgba(244,244,244,0)` en botones de escape | **`transparent`** | Es un `#F4F4F4` al que se le bajó la opacidad a 0 en vez de eliminar el fill. | §CC.15.8 |
| T9 | Peso del título de card | Bold (700) en §CC.20 · SemiBold (600) en §CC.16 y §CC.17 | **SemiBold (600)** — `B2 S` | 2 de 3 instancias del mismo componente usan 600, y 600 es el estándar de títulos de card del módulo. | §CC.20.4 |
| T10 | Peso de la dirección del destinatario | `B3 S` 12 SemiBold **negro** | **`B3 R` 12 Regular `#4C4C4C`** | Es el tratamiento de dirección en §CC.14.3, §CC.16.2 y §CC.18.3. | §CC.22.2 |
| T11 | Placeholder en estado de error | Negro | **`#C3C3C3`** (Greys/400) | El placeholder no cambia de color por el estado del campo; hoy se lee como valor capturado. | §CC.14.5, §CC.19.4 |
| T12 | Placeholder del select Colonia | Negro | **`#C3C3C3`** (Greys/400) | Mismo fundamento que T11. | §CC.14.4 |
| T13 | Anchos absolutos que rompen texto | `w-111px`/`w-87px` (dropdown) · `w-272px` en card de 278 · divisor `329px` en 328 | **`width: 100%`** con padding | Tres casos del mismo patrón. Ver regla **R2** (§CC.23.5). | §CC.19.5, §CC.20.4, §CC.22.4 |
| T14 | Labels con dos colores en el mismo bloque | "Dimensiones" y "Peso" en negro; el resto en `#4C4C4C` | **`#4C4C4C`** en todos los labels | En un par label/valor, el label es siempre secundario. | §CC.22.4 |
| T15 | Dos chevrons para el mismo control | `arrow-down-01-sharp` vs `icon/nav/chevron/down` | **`icon/nav/chevron/down`** | Es el usado en los selects de §CC.14.4 y §CC.17.2 y pertenece al set `icon/nav`. | §CC.22.6 |
| T16 | Componente mal aplicado | Toggle "Ver más" usa `Inactive/Default Input` | **Botón de texto** | Es una acción, no un campo de entrada. | §CC.22.4 |
| T17 | Ícono no semántico en modal | `calendar-03` en "Solicitar búsqueda" | **Ícono de búsqueda/investigación** | Copiado de §CC.17 (reagendar), donde sí corresponde a una fecha. Ver regla **R8**. | §CC.19.7 |
| T18 | Radio del día seleccionado sin documentar | `r60` suelto vs `r10` de celdas | **`r60` como estado**, no valor suelto | Es intencional visualmente; falta declararlo como estado del componente. | §CC.17.4 |

### CC.23.3 ✅ Resueltos — Copy

| # | Hallazgo | Actual | **Correcto** | Origen |
|---|---|---|---|---|
| C1 | Typo | "¿Confirmas la nueva fecha entrega?" | **"¿Confirmas la nueva fecha de entrega?"** | §CC.17.5 |
| C2 | Typo | "Odenar por" | **"Ordenar por"** | §CC.8 |
| C3 | Espacio inicial | `" siguiente dirección"` | `"siguiente dirección"` | §CC.16.4 |
| C4 | Placeholder sin resolver | `"...código postal [#####]"` | **Variable con el CP real**; en el estado con CP capturado debe reflejarlo | §CC.15.8, §CC.18.8 |
| C5 | Dos mensajes para la misma condición | "Ingresa la información requerida" (textareas) vs "Este campo es obligatorio" (inputs) | **"Este campo es obligatorio"** en ambos | §CC.19.4 |
| C6 | Orden de palabras del motivo | "Dirección incorrecta o incompleta" vs "Dirección incompleta o incorrecta" | **Una sola redacción** (redacción final pendiente de decisión de producto, fuera de esta guía) | §CC.7, §CC.18.4 |
| C7 | Dos convenciones de placeholder ejemplificado | `Ej. <texto>` vs `Ejemplo: '<texto>'` | **`Ejemplo: '<texto>'`** | §CC.19.3, §CC.21.2 |
| C8 | Puntuación inconsistente en labels | "Servicio:", "Peso total:", "Seguro:" con dos puntos; "Costo", "Paquete" sin ellos | **Sin dos puntos** en todos | §CC.18.3 |

> **C7 — fundamento:** `Ejemplo: '<texto>'` deja el ejemplo entrecomillado, lo que lo separa visualmente de la instrucción y evita que se confunda con contenido a escribir. `Ej.` abrevia sin marcar el límite del ejemplo.

### CC.23.4 ✅ Resueltos — Higiene de Figma

| # | Hallazgo | Acción | Origen |
|---|---|---|---|
| F1 | 7 ítems ocultos residuales en el menú de acciones (`1060:20377`–`1060:20419`), con `checkmark-square-02` + "Opción" | **Eliminar** — restos de una variante con checkboxes | §CC.18.2 |
| F3 | `tick-02` oculto en todas las opciones del dropdown | **Mostrar** en la opción seleccionada | §CC.19.5, §CC.22.5 |
| F4 | Chevrons ocultos en las tarjetas del selector | **Eliminar** si la tarjeta no es expandible | §CC.22.2 |
| F5 | Datos dummy repetidos (mismo destinatario, misma fecha, guía duplicada; LERMA y EMPAKATODO con la misma dirección; 3 fechas distintas en §CC.17) | **Diferenciar** para no confundir a dev | §CC.15.5, §CC.17.6, §CC.22.2 |
| F7 | `Attempt New Delivery` es un frame suelto, no una `<section>` | **Normalizar** a `<section>` como las demás acciones | §CC.20.6 |
| F8 | Dropdown de moneda es frame local; el de tipos es componente compartido | **Componentizar** el de §CC.19.5 | §CC.19.5, §CC.22.5 |

### CC.23.5 ✅ Reglas de sistema derivadas

Ocho reglas que **resuelven familias completas** de hallazgos y previenen su reaparición. Candidatas a `APP.md` y `reference-anti-patterns.md`.

| Regla | Enunciado | Resuelve |
|---|---|---|
| **R1 — Valores no redondos** | Todo valor con decimales no intencionales (`0.916px`, `11.75px`, `18.321px`, `-0.235px`, `12.824px`) es **escalado horneado** de una instancia con transform, **nunca un token**. Al documentar, redondear al token de origen. | T2, T3 |
| **R2 — Prohibido el ancho absoluto en contenido de texto** | Ningún nodo que contenga texto variable lleva ancho fijo. Usar `width: 100%` + padding del contenedor. | T13 (3 casos) |
| **R3 — Inter exclusivo** | La App usa **Inter** en todo contexto fuera de Nova. Manrope en la App es siempre anomalía, incluso si viene de un componente compartido. **Auditar el componente en origen, no la pantalla.** | T4 |
| **R4 — Criterio de confirmación** | Las acciones **reversibles** guardan directo (sin modal). Las **irreversibles o de plazo largo** requieren confirmación. Derivada de §CC.21, único flujo sin confirmación. | — |
| **R5 — CTA afirmativo** | El botón afirmativo **nombra la acción**: "Sí, devolver", "Sí, reprogramar", "Sí, reintentar", "Sí, iniciar búsqueda". `"Sí, confirmar"` queda reservado a confirmaciones sin verbo propio. | — |
| **R6 — Escala de color** | En toda familia, **número mayor = más oscuro** (`Primary/600` oscuro, `Primary/100` claro). Orange y Purple están invertidos. | — |
| **R7 — Un mensaje por condición** | Una condición de validación tiene **un solo** mensaje, independientemente del tipo de control. | C5 |
| **R8 — Ícono semántico** | El ícono del modal de confirmación debe corresponder a **la acción**, no heredarse de otro flujo. | T17 |

### CC.23.7 ⬜ Contenido faltante (requiere diseño)

| # | Qué falta | Nota | Origen |
|---|---|---|---|
| M1 | **Paso 2/2 de "Reportar incidencia"** | El indicador lo anuncia; no hay pantallas. Presumiblemente descripción + evidencia fotográfica | §CC.22.7 |
| M2 | **Tab "Sobrepesos"** | §CC.11 punto 1, sin tocar | §CC.2 |
| M3 | **Mapa motivo → acciones** | El menú muestra 3 de 8 acciones | §CC.18.2 |
| M4 | **Estado vacío del selector de envíos** | ¿Qué pasa si no hay envíos en el período? | §CC.22.7 |
| M5 | **Estado de CP inválido** tras "Validar" | El popup solo tiene "sin sucursales" | §CC.15.8 |
| M6 | **Reglas del date picker** | ¿Fechas pasadas? ¿domingos? ¿festivos? Sin días deshabilitados | §CC.17.4 |
| M7 | **Especificación del mapa y del degradado** | Proveedor, pines, permiso de ubicación denegado · stops del gradiente del footer | §CC.15.3, §CC.19.6 |

> ✅ **"Pantalla de éxito" ya no está en esta lista.** §CC.18.4 lo resolvió: **no existe**. El cierre de cada acción es el retorno al detalle con el **chip de acción** reemplazando al de motivo. Falta definir **qué chip corresponde a cada acción** (si además hay toast queda fuera de esta guía, es decisión de producto).

### CC.23.8 Orden de ejecución sugerido

| Fase | Contenido | Depende de |
|---|---|---|
| **1 — Reglas** | Publicar R1–R8 en `APP.md` y `reference-anti-patterns.md` | — |
| **2 — Auditar en origen** | Componentes compartidos: date picker (T4, T5, T6), dropdowns (T7, F8), card de dirección (T9, T13) | Fase 1 |
| **3 — Aplicar tokens y copy** | T1–T18, C1–C8 | Fases 1 y 2 |
| **4 — Higiene** | F1–F8 | — |
| **5 — Diseñar faltantes** | M1–M7 | — |

> **La fase 2 es la de mayor rendimiento:** tres componentes compartidos concentran nueve hallazgos, y corregirlos en origen los elimina de todas las pantallas que los instancian.

### CC.23.9 Estado de §CC tras la consolidación

| Punto de §CC.11 | Contenido | Estado |
|---|---|---|
| 1 | Tab "Sobrepesos" | 🔴 Sin documentar (M2) |
| 2 | Flujo "Reportar incidencia" | 🟡 Paso 1/2 documentado (§CC.22); falta Paso 2/2 (M1) |
| 3 | Flujos de acción por motivo | ✅ Cerrado (§CC.14–§CC.21) |
| 4 | Catálogo de estados con duplicidad | 🟡 Ampliado a **cuatro ejes** (estado · motivo · acción · estado del envío); catalogación final pendiente de decisión de producto (fuera de esta guía) |
| 5 | Localización | 🟡 Diagnóstico reclasificado: no son assets sueltos sino un **set EN del módulo**; alcance final pendiente de decisión de producto (fuera de esta guía) |
| 6 | Manrope en KPIs | ✅ Resuelto por R3 y T4 (3 instancias) |
| 7 | Semántica del color de los deltas | 🔴 Sin resolver — no reapareció en §CC.14–§CC.22 |

**Resumen:** §CC.23 consolida los **181 marcadores 🔴 y 80 ⚠️** de §CC.14–§CC.22 en **54 hallazgos únicos**, clasificados por quién puede resolverlos. **34 quedan resueltos** con valor corregido y fundamento (detalle en §CC.23.2–§CC.23.3), más **ocho reglas de sistema** (R1–R8) que resuelven familias completas y previenen su reaparición; la más rentable es **R3 + auditoría en origen**, porque tres componentes compartidos concentran nueve hallazgos. Los **siete restantes** son contenido que no existe en Figma y requiere diseño (§CC.23.7).

### CC.23.10 Referencias

- Consolida: §CC.14 · §CC.15 · §CC.16 · §CC.17 · §CC.18 · §CC.19 · §CC.20 · §CC.21 · §CC.22.
- Reglas derivadas propuestas para: `APP.md` (R1, R3, R6), `reference-anti-patterns.md` (R2, R8). El resto de R1–R8 son reglas de interacción/copy de UI que también quedan en esta guía; las decisiones de producto asociadas a hallazgos anteriores no viven aquí.
- Sin cambios en el **Índice de flujos** ni en **§CC.11** — pendientes de decisión del owner.

---

## CC.24 Control de calidad — "Reportar incidencia" · Paso 2/2 · Cambio de dirección (§CC.24)

> **Sección "Section 1"** (`4230:37750`). **Cierra el Paso 2/2** que faltaba en §CC.22.7 (pendiente **M1** de §CC.23.7), en su variante para el tipo **"Cambio de dirección"**.
> 5 pantallas: formulario vacío → lleno → modal de confirmación → modal de éxito → modal de error "Dirección duplicada".
> ⚠️ **Es la variante de un solo tipo.** Los otros seis tipos de §CC.22.5 tendrán su propio Paso 2/2 — ver §CC.24.8.
> **Figma:** `4230:37750`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.24.1 Mapa del flujo

```
Paso 1/2 (§CC.22) · tipo = "Cambio de dirección"
│
├── PASO 2/2 — VACÍO (504:38692) · alto 1559
│   Header "Reportar incidencia" + back
│   Tab "Cambio de dirección" · PASO 2/2 · barra al 100%
│   Motivo del cambio (textarea)
│   Card "Dirección actual" + acción "Replicar"
│   ▾ Nueva dirección (colapsable): 8 campos
│   CTA "Enviar incidencia" DESHABILITADO
│   │
│   └── captura ──▶ LLENO (504:38922) · CTA HABILITADO
│           │
│           └── tap "Enviar incidencia" ──▶
│
├── MODAL DE CONFIRMACIÓN (504:39241)
│   alert-circle · "Confirmación de creación de incidente"
│   [Cancelar] [Sí, confirmar]
│   │
│   ├── éxito ──▶ MODAL DE ÉXITO (504:39300)
│   │       tick-02 verde · "Tu incidente se envió con éxito."
│   │       [Entendido]
│   │
│   └── dirección igual a la actual ──▶ MODAL DE ERROR (504:39273)
│           copy-01 · "Dirección duplicada"
│           [Entendido]
```

### CC.24.2 ✅ Resuelve M1 — y **corrige** el hallazgo "no existe pantalla de éxito"

> ✅ **El Paso 2/2 existe.** Cierra el pendiente **M1** de §CC.23.7 y el punto 1 de §CC.22.9 — para este tipo de incidencia.
> 🔴 **Corrección a §CC.18.4 y §CC.23.7.** Ahí se concluyó que *"no existe pantalla de éxito: el cierre es el retorno al detalle con el chip de acción"*. Eso sigue siendo cierto para los **flujos de acción** (§CC.14–§CC.21), pero **no** para el flujo de alta: aquí **sí hay modal de éxito explícito**. Son dos patrones de cierre distintos:

| Flujo | Cierre |
|---|---|
| **Acción** (§CC.14–§CC.21, resolución) | Retorno al detalle con **chip de acción** actualizado. Sin modal. |
| **Alta** (§CC.22 + §CC.24, reporte) | **Modal de éxito** con seguimiento y plazo estimado. |

> **La distinción tiene sentido:** al resolver, el usuario ya está en el detalle y ve el cambio de estado; al reportar, viene de un wizard y necesita confirmación explícita de que se creó el registro.
> **Acción documental:** actualizar la redacción de §CC.18.4 y de §CC.23.7 para acotar el hallazgo a los flujos de acción.

### CC.24.3 Chrome y barra de progreso

Header con back + **"Reportar incidencia"** (se mantiene el título del wizard, no cambia por tipo).

**Indicador de paso** (`4241:13142`): **"Cambio de dirección"** (el tipo elegido en el paso 1) + **"PASO 2/2"** + barra `Rectangle 42477` de **360×3** — **ancho completo**, frente a los 180 del paso 1/2.

> ✅ **La barra es proporcional y correcta:** 180/360 = 50% en el paso 1, 360/360 = 100% en el paso 2. Resuelve la duda planteada en §CC.22.3.
> ✅ **El título del tab cambia al tipo elegido**, no repite "Tipo de incidencia". Buen patrón de wizard contextual.

### CC.24.4 Formulario — `504:38700`

- **Motivo del cambio** (`504:38886`) — label + **textarea h141**, `p12`, placeholder *"Describe el motivo del cambio (p. ej., número incorrecto, destinatario cambió de domicilio, etc.)."*
- **Card "Dirección actual"** (`504:38893`) — ver §CC.24.5.
- **Divisor** (`Line 711`).
- **Bloque "Nueva dirección"** (`504:38827`) — **colapsable**: título (16px) + `arrow-down-01-sharp` 20px. Contiene 8 campos:

| # | Campo | Tipo | Valor de ejemplo | Nodo |
|---|---|---|---|---|
| 1 | Calle | texto | `Avenida Francisco I. Madero` | `504:38834` |
| 2 | Número exterior | texto | `140` | `504:38840` |
| 3 | **Número interior (opcional)** | texto | `Depto 5A` | `504:38846` |
| 4 | Código postal | texto | `06000` | `504:38852` |
| 5 | Colonia | **select** | `Buenavista` | `504:38858` |
| 6 | Estado | texto | `Avenida Francisco I. Madero` | `504:38865` |
| 7 | Ciudad | texto | `Avenida Francisco I. Madero` | `504:38871` |
| 8 | Referencia | textarea h141 | `Avenida Francisco I. Madero` | `504:38877` |

- **CTA "Enviar incidencia"** (`504:38708`) — full-width 328×40, `#F1B0A9` off / `#DB3B2B` on.

> ✅ **"Nueva dirección" colapsable** — buen patrón para un formulario de 1,559px de alto. §CC.14 no lo tiene y lo necesitaría.
> ⚠️ **Es el mismo formulario de §CC.14.4** (mismos 8 campos), pero aquí precedido por "Motivo del cambio" y con el bloque colapsable. **Confirmar si son el mismo componente**: uno se usa al *reportar* y otro al *resolver*. Si lo son, unificar; si no, documentar por qué difieren.
> ⚠️ **El select Colonia aquí NO usa Manrope** (a diferencia de §CC.14.4). Refuerza que aquella instancia era la anómala (T4 de §CC.23.2).

### CC.24.5 🔴 Card "Dirección actual" — tercera anatomía del mismo bloque

Card **`#F8F8F8`** (Greys/900, **fondo gris, sin borde**), **r12**, `p12`, gap 12:
- **Fila:** **"Dirección actual"** (`B2 S` 14 SemiBold negro) + **"Replicar"** a la derecha (`B2 S` 14 SemiBold **negro**) — es **texto, no botón**.
- **Dirección** — `B3 R` 12 Regular `#4C4C4C`.

Comparación con las otras dos instancias del mismo bloque:

| | §CC.14.3 | §CC.16.2 / §CC.17.2 | **§CC.24.5** |
|---|---|---|---|
| Fondo | blanco | blanco | **`#F8F8F8`** |
| Borde | `1px #F3F3F3` | `1px #F3F3F3` | **ninguno** |
| Alto | 130 | 130 | **83** |
| Acción | **botón** "Replicar" (r8, h32, w101) | **botón** "Cambiar" (r8, h32, w101) | **texto** "Replicar" |
| Posición de la acción | debajo, izquierda | debajo, izquierda | **misma fila, derecha** |

> 🔴 **Tres anatomías para el mismo bloque conceptual** ("dirección de referencia + acción"). La de §CC.24 es la más compacta pero la que peor comunica la acción: **"Replicar" es texto plano en negro, sin afordancia de botón** — no se distingue del título "Dirección actual", que tiene exactamente el mismo estilo (`B2 S` 14 SemiBold negro).
> **Recomendación:** unificar en un componente con prop `action` (botón secundario) y `density` (normal / compacta). Como mínimo, **diferenciar visualmente "Replicar"** del título — es un control, no una etiqueta.
> ⚠️ Se suma al patrón ya detectado en §CC.20.4 y §CC.23.2 T9/T13: **la card de dirección es el componente más divergente del módulo**.

### CC.24.6 Modales — tres nuevos

Los tres comparten estructura del confirmador (círculo 64px r61 + título `T2 S` 20 + cuerpo `B2 R` 14 `#4C4C4C` + acciones h40 r12, gap 24/10/8), y **amplían el componente a dos ejes nuevos**.

| | Confirmación `504:39241` | **Éxito** `504:39300` | Error `504:39273` |
|---|---|---|---|
| Ícono | `alert-circle` | **`tick-02`** | `copy-01` |
| Círculo | `#F8F8F8` | **`#F0FDF4`** (Green/500) | `#F8F8F8` |
| Tono del ícono | neutro | **`#4FC153`** (Green/300) | neutro |
| Título | Confirmación de creación de incidente | **Tu incidente se envió con éxito.** | Dirección duplicada |
| Cuerpo | Estás a punto de crear un incidente para el envío con número de rastreo **[Tracking Number]**. ¿Deseas continuar con esta acción? | Puedes darle seguimiento en la sección de incidentes. El tiempo estimado de respuesta de **[Courier Name]** es de hasta **XX días hábiles**. | La dirección ingresada coincide con la actual. Ingresa una dirección diferente para continuar. |
| Acciones | `Cancelar` + `Sí, confirmar` | **`Entendido`** (única) | **`Entendido`** (única) |

> ✅ **Primer tono verde del módulo** — `#F0FDF4` / `#4FC153` (Green/500 y Green/300). Coherente con el estado "Finalizada" de §CC.7, que usa `#F0FDF4` / `#51AF70`.
> 🔴 **Dos verdes distintos para éxito:** `#4FC153` aquí vs. `#51AF70` en el chip "Finalizada" (§CC.7). Y `#4FC153` es también el del delta positivo de los KPIs (§CC.4). Unificar el verde semántico de éxito.
> ✅ **Tercer eje de parametrización del modal confirmado.** Con §CC.18.7 (`iconTone`) y §CC.17.5 (`icon`, `body`), ahora se añade **`actions`**: par (Cancelar + afirmativo) o **única** (Entendido). Props finales sugeridas: `icon`, `iconTone` (neutral | danger | success), `title`, `body` (texto | card-dato | card-editable), `actions` (par | única), `confirmLabel`.
> ✅ **Modal de error de negocio bien planteado** — "Dirección duplicada" no es una validación de campo sino una regla (la nueva dirección no puede ser igual a la actual), y se comunica como modal bloqueante con salida única. Patrón correcto y **nuevo en el módulo**.
> ⚠️ **`copy-01` para "Dirección duplicada"** es semánticamente aceptable (duplicar/copiar) pero débil: el usuario no copió nada, escribió lo mismo. Considerar un ícono de advertencia. Ver **R8** (§CC.23.5).

### CC.24.8 Componentes nuevos (vs. ya documentados)

- **Modal de éxito** (`504:39300`) — círculo verde `#F0FDF4` + `tick-02` + acción única "Entendido". **Primero del módulo.**
- **Modal de error de negocio** (`504:39273`) — regla incumplida, no validación de campo, con salida única.
- **Bloque de formulario colapsable** (`504:38827`) — "Nueva dirección" con chevron. §CC.14 lo necesitaría.
- **Card de dirección compacta** (`504:38893`) — fondo `#F8F8F8` sin borde, acción en la misma fila. ⚠️ Tercera anatomía (§CC.24.5).

Reutiliza: chrome del wizard e indicador de paso (§CC.22.3), inputs y textareas r20, modal de confirmación (8ª instancia).

### CC.24.9 Pendientes (🔴)

1. 🔴 **Tercera anatomía de la card de dirección**, con "Replicar" como **texto sin afordancia de botón**, idéntico en estilo al título (§CC.24.5).
2. 🔴 **Dos verdes de éxito** — `#4FC153` aquí vs. `#51AF70` en el chip "Finalizada" (§CC.7) (§CC.24.6).
3. 🔴 **Faltan los Paso 2/2 de los otros seis tipos** — Paquete sin movimiento, Recolecciones fallidas, Retraso en la entrega, Paquete dañado, Paquete perdido, Paquete abierto o alterado (§CC.22.5). Los tipos con daño probablemente requieran **carga de evidencia fotográfica**, que no aparece en ninguna pantalla documentada.
4. 🔴 **Sin estado de validación de campo** — no hay pantalla de error con bordes rojos, a diferencia de §CC.14.5 y §CC.19.4.
5. ⚠️ **¿Es el mismo formulario de §CC.14.4?** Mismos 8 campos; confirmar si es un componente compartido (§CC.24.4).
6. ⚠️ **`copy-01` para "Dirección duplicada"** — ícono débil; considerar advertencia (§CC.24.6).

### CC.24.10 ✅ Correcciones a secciones previas

Esta sección **corrige o cierra** puntos documentados antes:

| Punto | Sección afectada | Corrección |
|---|---|---|
| "No existe pantalla de éxito" | §CC.18.4, §CC.23.7 | ✅ **Acotar a los flujos de acción.** El flujo de alta **sí** tiene modal de éxito (§CC.24.2) |
| M1 — Paso 2/2 sin localizar | §CC.22.7, §CC.23.7 | ✅ **Cerrado parcialmente** — existe para "Cambio de dirección"; faltan los otros 6 tipos |
| Barra de progreso proporcional | §CC.22.3 | ✅ **Confirmado:** 180/360 (50%) → 360/360 (100%) |

### CC.24.12 Referencias

- *Section 1* (`4230:37750`).
- **Paso 2/2 vacío:** `504:38692` (indicador `4241:13142`, motivo `504:38886`, card `504:38893`, bloque colapsable `504:38827`, CTA `504:38708`).
- **Paso 2/2 lleno:** `504:38922` (card `504:38945`, campos `504:38955`, CTA `4254:13180`).
- **Modal confirmación:** `504:39241` (ícono `504:39269` `alert-circle`, título `504:39250`, cuerpo `504:39251`).
- **Modal éxito:** `504:39300` (contenido `504:39303`; círculo `504:39305` `#F0FDF4`, ícono `504:39330` `tick-02`, título `504:39311`, cuerpo `504:39312`, CTA `504:39324`).
- **Modal "Dirección duplicada":** `504:39273` (contenido `504:39276`; ícono `504:39297` `copy-01`, título `504:39284`, cuerpo `504:39285`, CTA `504:39288`).

---

## CC.25 Control de calidad — "Reportar incidencia" · Paso 2/2 · Paquete sin movimiento (§CC.25)

> **Sección "Package without movement"** (`504:50784`). **Segunda variante** del Paso 2/2 (§CC.11 punto 2), tras §CC.24 (*Cambio de dirección*). Avanza **M1** a 2 de 7 tipos.
> 4 pantallas: formulario vacío → lleno → modal de confirmación → modal de éxito.
> **Aporta el primer banner informativo del módulo** y **confirma que el Paso 2/2 es un formulario distinto por tipo**.
> **Figma:** `504:50784`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.25.1 Mapa del flujo

```
Paso 1/2 (§CC.22) · tipo = "Paquete sin movimiento"
│
├── PASO 2/2 — VACÍO (504:50212) · alto 1245
│   Tab "Paquete sin movimiento" · PASO 2/2 · barra al 100%
│   🔵 Banner informativo: "…se iniciará una investigación que puede durar hasta 20 días hábiles."
│   Descripción del problema (textarea h141)
│   Descripción del empaque (textarea h141)
│   Descripción exacta del producto (textarea h141)
│   Costo [226px] + Moneda [93px]  ← en una sola fila
│   Número de piezas
│   CTA "Enviar incidencia" DESHABILITADO
│   │
│   └── captura ──▶ LLENO (504:50470) · CTA HABILITADO
│           │
│           └── tap "Enviar incidencia" ──▶
│
├── MODAL DE CONFIRMACIÓN (504:50744) — idéntico a §CC.24.6
│
└── MODAL DE ÉXITO (504:50768) — idéntico a §CC.24.6
```

> ⚠️ **No hay modal de error de negocio** (como el "Dirección duplicada" de §CC.24.6). Coherente: aquí no hay regla de unicidad que validar.

### CC.25.2 🔴 Confirmado: el Paso 2/2 es un formulario distinto por tipo

Comparación con §CC.24 (*Cambio de dirección*):

| | §CC.24 · Cambio de dirección | **§CC.25 · Paquete sin movimiento** |
|---|---|---|
| Banner | — | 🔵 **Informativo (20 días hábiles)** |
| Campos | Motivo + card dirección actual + 8 campos de nueva dirección | **3 textareas + Costo + Moneda + Número de piezas** |
| Bloque colapsable | Sí ("Nueva dirección") | No |
| Alto | 1,559px | 1,245px |
| Modal de error de negocio | Sí ("Dirección duplicada") | No |

> 🔴 **Cada tipo tiene su propio formulario.** No es un formulario común con campos condicionales: son estructuras distintas. **Faltan los cinco restantes** (Recolecciones fallidas, Retraso en la entrega, Paquete dañado, Paquete perdido, Paquete abierto o alterado), y no se pueden inferir de los dos documentados.
> **Implicación para dev:** el Paso 2/2 debe modelarse como **un formulario por tipo**, no como un formulario único parametrizado.

### CC.25.4 ✅ Banner informativo — `4256:13495` (componente `Messages`)

**Primer banner informativo documentado en el módulo**, y **primera familia azul**.

- **Contenedor:** `#F0F8FF` (Blue/500), **r10**, `p10`, gap 12, sombra `0 4px 7px rgba(0,0,0,.05)`, ancho 328, alto 65.
- **Ícono:** `icon/status/info` 24px (vector 17px).
- **Texto:** `B3 R` **12 Regular**, color `#2180FF` (Blue/300): *"Al seleccionar este incidente, se iniciará una investigación que puede durar hasta 20 días hábiles."*

> ✅ **Es un componente compartido** (`Messages`), no un frame local. Buena señal: el sistema ya tiene un componente de mensajería que este flujo instancia correctamente.
> ✅ **Excelente patrón de expectativa.** Advierte del costo temporal **antes** de que el usuario llene el formulario, no después. Es superior al modal de §CC.19.7, que avisa al confirmar —cuando ya invirtió el esfuerzo—. **Recomendación: replicar el banner en §CC.19.**
> 🔴 **Escala Blue invertida, igual que Orange y Purple.** `Blue/300 = #2180FF` (oscuro) y `Blue/500 = #F0F8FF` (claro), al revés de la convención de la App (`Primary/600` oscuro / `Primary/100` claro). **Tercera familia con el mismo problema** — refuerza **R6** de §CC.23.
> ⚠️ **Contraste a verificar.** `#2180FF` sobre `#F0F8FF` a 12px Regular: conviene medirlo contra WCAG AA (4.5:1 para texto pequeño). Ver `A11Y.md`.

### CC.25.5 ✅ Costo + Moneda en una sola fila — `4256:13698`

Fila de 327px con dos inputs (`justify-between`):

| Campo | Ancho | Padding | Contenido |
|---|---|---|---|
| **Costo** | **226px** | `px20/py18` | `$` / `$ 587.00` |
| **Moneda** | **93px** | `pl16 / pr8 / py18` | `MXN` + `arrow-down-01-sharp` 24px |

Ambos: borde `1px #F3F3F3`, **r20**, h55, texto `B2 R` 14 `-0.28px`. Label "Costo" único para la fila, gap **7px**.

> ✅ **Resuelve la sugerencia de §CC.19.3.** Ahí propuse considerar un input compuesto para reducir la altura del formulario; aquí **ya existe** y funciona. 226 + 8 + 93 = 327.
> 🔴 **Inconsistencia con §CC.19.3:** en "Solicitar búsqueda" los mismos dos campos están **apilados** (dos filas completas de 328px), y aquí **en una fila**. Mismo par de campos, dos layouts. **Unificar al de §CC.25**, que es el correcto: la moneda es un calificador del monto, no un campo independiente.
> ⚠️ **Gap del label = 7px** aquí vs. **7.328px** en el resto del formulario. Diferencia mínima pero es el mismo síntoma de **R1** (§CC.23.5): 7.328 es escalado horneado, **7 es el valor limpio**. Confirma que el token correcto es **8px** o **7px**, no 7.328.
> ⚠️ **`arrow-down-01-sharp`** en el select de Moneda, mientras §CC.14.4 y §CC.17.2 usan `icon/nav/chevron/down`. Se suma a **T15** de §CC.23.2.
> ⚠️ **Ancho 327 vs. 328** del resto de campos. Diferencia de 1px sin razón; ver **R2**.

### CC.25.6 Modales

Los dos modales son **idénticos a los de §CC.24.6** — mismo ícono, tono, copy y acciones:

| | Confirmación `504:50744` | Éxito `504:50768` |
|---|---|---|
| Ícono / círculo | `alert-circle` / `#F8F8F8` | `tick-02` / `#F0FDF4` |
| Título | Confirmación de creación de **incidente** | Tu **incidente** se envió con éxito. |
| Cuerpo | …número de rastreo **[Tracking Number]**… | …sección de **incidentes**. …de **[Courier Name]** es de hasta **XX días hábiles**. |
| Acciones | `Cancelar` + `Sí, confirmar` | `Entendido` |

> ✅ **Confirma que los modales de cierre son transversales al flujo de alta**, no específicos por tipo. Documentar una sola vez y referenciar.

### CC.25.8 Componentes nuevos (vs. ya documentados)

- **Banner informativo** (`Messages`, `4256:13495`) — `#F0F8FF` / `#2180FF`, r10, ícono `icon/status/info`. **Componente compartido**; primera familia azul del módulo.
- **Fila compuesta Costo + Moneda** (`4256:13701`) — 226 + 93 con label único. Resuelve la sugerencia de §CC.19.3.

Reutiliza: chrome del wizard e indicador de paso (§CC.22.3, §CC.24.3), textareas h141, modales de confirmación y éxito (§CC.24.6).

### CC.25.9 Pendientes (🔴)

1. 🔴 **Costo + Moneda apilados en §CC.19 y en fila aquí** — unificar al layout de §CC.25 (§CC.25.5).
2. 🔴 **Escala Blue invertida** (`Blue/300` oscuro / `Blue/500` claro) — **tercera familia** con el problema de **R6** (§CC.25.4).
3. 🔴 **Faltan cinco Paso 2/2**: Recolecciones fallidas, Retraso en la entrega, Paquete dañado, Paquete perdido, Paquete abierto o alterado. **No se pueden inferir** — cada tipo tiene su propio formulario (§CC.25.2).
4. 🔴 **Sin estado de validación de campo** — tampoco aquí, como en §CC.24.
5. ⚠️ **Gap 7px vs 7.328px** — confirma que 7.328 es escalado horneado (R1) (§CC.25.5).
6. ⚠️ **Ancho 327 vs 328** en la fila de Costo (§CC.25.5).
7. ⚠️ **`arrow-down-01-sharp`** en Moneda — se suma a T15 (§CC.25.5).
8. ⚠️ **Contraste `#2180FF` sobre `#F0F8FF`** a 12px — verificar WCAG AA (§CC.25.4).

### CC.25.10 ✅ Aportes a secciones previas

| Punto | Sección afectada | Aporte |
|---|---|---|
| Input compuesto Costo + Moneda | §CC.19.3 (sugerencia) | ✅ **Ya existe** aquí y funciona. Unificar §CC.19 a este layout |
| Aviso de plazo antes vs. después | §CC.19.7 | ✅ El **banner** avisa antes de llenar el formulario; el modal de §CC.19 avisa al confirmar. **Replicar el banner en §CC.19** |
| R1 — valores no redondos | §CC.23.5 | ✅ **Nueva evidencia:** gap **7px** aquí vs **7.328px** en el mismo formulario |
| R6 — escala de color | §CC.23.5 | 🔴 **Tercera familia afectada** (Blue, tras Orange y Purple) |
| M1 — Paso 2/2 | §CC.23.7 | 🟡 **2 de 7 tipos** documentados |

### CC.25.12 Referencias

- *Package without movement* (`504:50784`).
- **Paso 2/2 vacío:** `504:50212` (indicador `4256:13486`, banner `4256:13495`, campos `4256:13496`/`13502`/`13508`, fila Costo `4256:13514`, CTA `4256:13536`).
- **Paso 2/2 lleno:** `504:50470` (banner `4256:13679`, fila Costo `4256:13698`, CTA `4256:13720`).
- **Banner:** `4256:13495` (componente `Messages`; ícono `I4256:13495;98:16214`, texto `I4256:13495;98:16215`).
- **Fila Costo + Moneda:** `4256:13701` (Costo `4256:13702` w226 · Moneda `4256:13707` w93).
- **Modal confirmación:** `504:50744` (ícono `504:50750`, título `504:50755`, cuerpo `504:50756`).
- **Modal éxito:** `504:50768` (ícono `504:50774`, título `504:50777`, cuerpo `504:50778`, CTA `504:50779`).

---

## CC.26 Control de calidad — "Reportar incidencia" · Paso 2/2 · Recolección fallida (§CC.26)

> **Sección "Failed Pick-up"** (`504:54218`). **Tercera variante** del Paso 2/2 (§CC.11 punto 2), tras §CC.24 (*Cambio de dirección*) y §CC.25 (*Paquete sin movimiento*). Avanza **M1** a **3 de 7** tipos.
> 4 pantallas: formulario vacío → "lleno" → modal de confirmación → modal de éxito.
> **Es la variante más simple: un solo campo.** Y la que mejor evidencia que el Paso 2/2 escala por complejidad del tipo.
> **Figma:** `504:54218`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.26.1 Mapa del flujo

```
Paso 1/2 (§CC.22) · tipo = "Recolecciones fallidas"
│
├── PASO 2/2 (504:54247) · alto 780 — sin scroll
│   Tab "Recolección fallida" · PASO 2/2 · barra al 100%
│   Descripción del problema (textarea h141) ← ÚNICO campo
│   CTA "Enviar incidencia" DESHABILITADO
│   │
│   └── captura ──▶ "LLENO" (504:54533) · CTA HABILITADO
│           │
│           └── tap "Enviar incidencia" ──▶
│
├── MODAL DE CONFIRMACIÓN (504:54231) — idéntico a §CC.24 y §CC.25
│
└── MODAL DE ÉXITO (504:54219) — idéntico a §CC.24 y §CC.25
```

> ✅ **Sin banner informativo** (a diferencia de §CC.25) y **sin modal de error de negocio** (a diferencia de §CC.24). Coherente: no hay plazo largo que advertir ni regla de unicidad que validar.

### CC.26.2 Formulario — `4256:13818`

Un solo bloque, gap 20:

- **Label** "Descripción del problema" — `B2 S` 14 SemiBold `-0.28px` negro.
- **Textarea** (`4256:13868`) — borde **`1px #F3F3F3`**, **r20**, **h141**, `p12`, gap del label **7.328px**.
  - **Placeholder:** *"Describe la situación que provocó la recolección fallida. Ejemplo: "El mensajero no se presentó en la fecha y hora programadas para la recolección.""* — `B2 R` 14 Regular `-0.28px`.
- **CTA "Enviar incidencia"** (`4256:13826` / `4256:13872`) — full-width 328×40, **r12**, `B2 S` 14 SemiBold blanco. `#F1B0A9` off / `#DB3B2B` on.

> ✅ **Métricas limpias**, coherentes con §CC.21.3 y §CC.24: borde `1px`, texto 14, tracking `-0.28px`. Confirma la referencia canónica de **T2** (§CC.23.2).
> ⚠️ **Persiste el gap 7.328px**, mientras §CC.25.5 usa 7px en la fila de Costo. Sigue siendo la misma evidencia de **R1**.

### CC.26.3 🔴 El estado "lleno" no tiene contenido capturado

Los nodos de texto de las dos pantallas son **idénticos**:

| Pantalla | Nodo | Contenido | Color |
|---|---|---|---|
| Vacío | `4256:13825` | *"Describe la situación que provocó la recolección fallida. Ejemplo: …"* | gris (placeholder) |
| **"Lleno"** | `4256:13871` | **el mismo texto, palabra por palabra** | **negro** |

> 🔴 **La maqueta del estado lleno solo cambió el color del placeholder a negro**, sin escribir un valor real. Es distinto de §CC.24 y §CC.25, donde el estado lleno sí tiene contenido capturado (*"Error en el número."*, *"El paquete no ha mostrado actualizaciones…"*).
> **Corregir en Figma:** poner un ejemplo de captura real, p. ej. *"El mensajero no llegó en la ventana de 9:00 a 14:00 del 12 de nov."* Hoy la pantalla sugiere —incorrectamente— que el usuario debe transcribir el placeholder.
> ⚠️ **Es el mismo síntoma que T11 de §CC.23.2** (placeholder en negro en estado de error). Ahí el diagnóstico era "el placeholder no debe cambiar de color"; aquí se confirma que **el patrón de maqueta es reutilizar el placeholder como si fuera valor**. Vale la pena revisarlo en todas las pantallas de estado lleno del módulo.

### CC.26.5 🔴 Chrome del header sin normalizar

Esta variante estructura el header **distinto** a §CC.24 y §CC.25:

| | §CC.24 / §CC.25 | **§CC.26** |
|---|---|---|
| Estructura | Frame `2147239830` con back + título | **Nodos sueltos** |
| Back | dentro del frame, `x=0` | `504:54251`, `x=16 y=90` |
| Título | `x=24 w=304` | `504:54253`, **`x=77 w=207`** |
| Divisor | `y=106` | **`y=104`** |

> 🔴 **Mismo header, tres geometrías distintas.** El título arranca en x=77 en vez de x=24, el divisor está 2px más arriba y no hay frame contenedor. Normalizar al patrón de §CC.24/§CC.25.
> ⚠️ **El contenedor del paso arranca en `x=1`** en la pantalla vacía y en `x=0` en la llena. Desplazamiento de 1px sin razón.

### CC.26.6 Modales

Idénticos a §CC.24.6 y §CC.25.6 — mismo ícono, tono, copy y acciones.

| | Confirmación `504:54231` | Éxito `504:54219` |
|---|---|---|
| Ícono / círculo | `alert-circle` / `#F8F8F8` | `tick-02` / `#F0FDF4` |
| Título | Confirmación de creación de **incidente** | Tu **incidente** se envió con éxito. |
| Cuerpo | …**[Tracking Number]**… | …sección de **incidentes**. …**[Courier Name]**… **XX días hábiles**. |
| Acciones | `Cancelar` + `Sí, confirmar` | `Entendido` |

> ✅ **Tercera confirmación de que los modales de cierre son transversales**, no específicos por tipo. Documentar una sola vez.

### CC.26.7 ✅ El Paso 2/2 escala por complejidad del tipo

Con tres variantes documentadas, el patrón es claro:

| Tipo | Campos | Alto | Banner | Error de negocio |
|---|---|---|---|---|
| **Recolección fallida** (§CC.26) | **1** textarea | **780** (sin scroll) | — | — |
| **Paquete sin movimiento** (§CC.25) | 3 textareas + Costo + Moneda + Piezas | 1,245 | 🔵 Sí | — |
| **Cambio de dirección** (§CC.24) | Motivo + card + 8 campos | 1,559 | — | Sí |

> ✅ **La complejidad del formulario es proporcional a lo que la paquetería necesita para investigar.** Una recolección fallida se resuelve con una descripción; un paquete extraviado requiere valor declarado y detalle del producto; un cambio de dirección requiere la dirección completa.
> ✅ **Confirma §CC.25.2:** no es un formulario parametrizado sino uno por tipo. Y ahora se ve **por qué**.
> ⚠️ **§CC.26 cabe sin scroll (780px)** — es la única de las tres. Su CTA queda a media pantalla, no anclado al fondo. Definir si el CTA debe fijarse al fondo cuando el contenido no llena la pantalla.

### CC.26.8 Componentes nuevos (vs. ya documentados)

Ninguno. Recombina: chrome del wizard e indicador de paso (§CC.22.3), textarea h141 r20 (§CC.24, §CC.25), CTA full-width r12, modales de confirmación y éxito (§CC.24.6).

### CC.26.9 Pendientes (🔴)

1. 🔴 **Estado "lleno" sin contenido capturado** — es el placeholder en negro, palabra por palabra (§CC.26.3).
2. 🔴 **Header con geometría distinta** a §CC.24 y §CC.25 — título en `x=77` vs `x=24`, divisor en `y=104` vs `y=106`, sin frame contenedor (§CC.26.5).
3. 🔴 **Faltan cuatro Paso 2/2**: Retraso en la entrega, Paquete dañado, Paquete perdido, Paquete abierto o alterado (§CC.26.7).
4. 🔴 **Sin estado de validación de campo** — tercera variante sin él.
5. ⚠️ **Gap 7.328px** — persiste la evidencia de R1 (§CC.26.2).
6. ⚠️ **Contenedor en `x=1` vs `x=0`** entre las dos pantallas (§CC.26.5).
7. ⚠️ **CTA no anclado al fondo** en la única pantalla que cabe sin scroll (§CC.26.7).

### CC.26.11 Referencias

- *Failed Pick-up* (`504:54218`).
- **Paso 2/2 vacío:** `504:54247` (header `504:54251` / `504:54253`, indicador `4256:13813`, campo `4256:13820`, placeholder `4256:13825`, CTA `4256:13826`).
- **Paso 2/2 "lleno":** `504:54533` (contenido `4256:13865`; texto `4256:13871`, CTA `4256:13872`).
- **Modal confirmación:** `504:54231` (ícono `504:54237`, título `504:54242`, cuerpo `504:54243`).
- **Modal éxito:** `504:54219` (ícono `504:54225`, título `504:54228`, cuerpo `504:54229`, CTA `504:54230`).

## CC.27 Control de calidad — "Reportar incidencia" · Paso 2/2 · Retraso en la entrega (§CC.27)

> **Sección "Delivery Delay"** (`504:58879`). **Cuarta variante** del Paso 2/2 (§CC.11 punto 2), tras §CC.24 (*Cambio de dirección*), §CC.25 (*Paquete sin movimiento*) y §CC.26 (*Recolección fallida*). Avanza **M1** a **4 de 7** tipos.
> 4 pantallas: formulario vacío (dirección **expandida**) → lleno (dirección **colapsada**) → modal de confirmación → modal de éxito.
> **Es la variante más compleja y la más alta del conjunto:** recombina los textareas de §CC.25 con el bloque de dirección de §CC.24. Aporta un hallazgo nuevo: **dos campos con la misma etiqueta**.
> **Figma:** `504:58879`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.27.1 Mapa del flujo

```
Paso 1/2 (§CC.22) · tipo = "Retraso en la entrega"
│
├── PASO 2/2 — VACÍO (504:59110) · dirección EXPANDIDA · alto 2,143 (con scroll)
│   Tab "Retraso en entrega" · PASO 2/2 · barra al 100%
│   1. "Descripción del problema"  (textarea h141) ← placeholder de EMPAQUE
│   2. "Descripción exacta del producto" (textarea h141)
│   3. Costo [226px] + Moneda [93px]  ← en una sola fila
│   4. "Descripción del problema"  (textarea h141) ← placeholder de SITUACIÓN
│   ── divisor ──
│   5. "Dirección de entrega" (colapsable, EXPANDIDA) → 8 campos:
│        Calle · Núm. exterior · Núm. interior (opcional) · Código postal ·
│        Colonia (select) · Estado · Ciudad · Referencia (textarea)
│   CTA "Enviar incidencia" DESHABILITADO
│   │
│   └── captura ──▶ LLENO (504:59927) · dirección COLAPSADA · alto 1,115 · CTA HABILITADO
│           │
│           └── tap "Enviar incidencia" ──▶
│
├── MODAL DE CONFIRMACIÓN (504:58892) — idéntico a §CC.24 / §CC.25 / §CC.26
│
└── MODAL DE ÉXITO (504:58880) — idéntico a §CC.24 / §CC.25 / §CC.26
```

> ✅ **Sin banner informativo** (a diferencia de §CC.25) y **sin modal de error de negocio** (a diferencia de §CC.24). No hay plazo largo que advertir ni regla de unicidad que validar.
> ⚠️ **Única variante con sección colapsable** (§CC.24 también, pero ahí era el cuerpo entero). Aquí el bloque de dirección se puede plegar; su alto depende del estado (2,143 expandida / 1,115 colapsada).

### CC.27.2 Formulario — `4256:14009` (vacío) / `4256:14441` (lleno)

Cinco bloques con gap 20; cada campo con gap label→control **7.328px** (Costo usa **7px**).

| # | Label | Nodo label | Control | Placeholder (vacío) → Valor (lleno) |
|---|---|---|---|---|
| 1 | Descripción del problema | `4256:14012` | textarea h141 | *"Describe el tipo y condición del **empaque**…"* → *"Caja de cartón sellada con cinta transparente."* |
| 2 | Descripción exacta del producto | `4256:14018` | textarea h141 | *"Especifica la marca, modelo, color…"* → *"Smartphone marca XYZ, modelo ABC123, color negro, 128GB."* |
| 3 | Costo + Moneda | `4256:14025` | input 226px + select 93px | `$` / `MXN` → `$ 587.00` / `MXN` |
| 4 | Descripción del problema | `4256:14039` | textarea h141 | *"Describe la situación con detalle…"* → *"El paquete no ha mostrado actualizaciones en el rastreo desde el 03/03/2025…"* |
| 5 | Dirección de entrega | `4256:14047` | colapsable → 8 campos | ver §CC.27.5 |

- **Textareas** (`Inactive/Default Input`) — borde **`1px #F3F3F3`** (Greys/800), **r20**, **h141**, `p12`. Métricas limpias.
- **Costo** (`4256:14027`, w226) + **Moneda** (`4256:14032`, w93, con chevron) — borde `1px #F3F3F3`, **r20**, **h55**, `px20/py18`. Confirmado por design context — **idéntico a §CC.25.5**.
- **Label / valor:** `B2 S` 14 SemiBold `-0.28px` negro / `B2 R` 14 Regular `-0.28px` negro.
- **CTA "Enviar incidencia"** (`4256:14099` / `4256:14531`) — full-width 328×40, **r12**, blanco. `#F1B0A9` off / `#DB3B2B` on.

### CC.27.4 ✅ El formulario recombina componentes de §CC.25 + §CC.24

Ningún campo es nuevo. **Retraso en la entrega recombina campos ya documentados:**

| Bloque | Origen | Cambio en §CC.27 |
|---|---|---|
| Empaque + Producto + Costo + Moneda | §CC.25 (*Paquete sin movimiento*) / §CC.19 | Se **elimina "Número de piezas"** |
| Descripción del problema (situación) | §CC.25 | Se **reubica después de Costo** (en §CC.25 va primero) |
| Bloque de 8 campos de dirección | §CC.24 (*Cambio de dirección*) | Se rotula **"Dirección de entrega"** (en §CC.24 es "Nueva dirección"), y aquí es **colapsable** |

> ✅ **Confirma §CC.25.2 y lo extiende:** los Paso 2/2 no solo son un formulario por tipo, sino que **se ensamblan recombinando grupos de campos**. Con cuatro variantes ya se ven los grupos reutilizables: *textareas de detalle* (empaque, producto, problema), *valor declarado* (Costo + Moneda), *cantidad* (Piezas) y *dirección* (8 campos).
> **Implicación para dev:** modelar el Paso 2/2 como composición de **grupos de campos reutilizables**, no como formularios independientes por tipo ni como uno solo parametrizado.

### CC.27.5 Bloque de dirección

Bloque colapsable "Dirección de entrega" (`4256:14045`), **expandido** en la pantalla vacía y **colapsado** en la llena (`4256:14481` `hidden=true`).

| Campo | Nodo valor | Contenido |
|---|---|---|
| Calle | `4256:14055` | Avenida Francisco I. Madero |
| Número exterior | `4256:14061` | 140 |
| Número interior (opcional) | `4256:14067` | Depto 5A |
| Código postal | `4256:14073` | 06000 |
| Colonia (select, con chevron) | `4256:14079` | Buenavista |
| Estado | `4256:14086` | Avenida Francisco I. Madero |
| Ciudad | `4256:14092` | Avenida Francisco I. Madero |
| Referencia (textarea h141) | `4256:14098` | Avenida Francisco I. Madero |

> ⚠️ **"Número interior (opcional)"** está bien marcado como opcional — coherente con §CC.24.4.
> ⚠️ **Mismo bloque de 8 campos que en §CC.24** ("Nueva dirección"), aquí bajo el rótulo "Dirección de entrega". Confirmar si es un componente compartido.

### CC.27.6 Modales

Idénticos a §CC.24.6 / §CC.25.6 / §CC.26.6 — mismo ícono, tono, copy y acciones.

| | Confirmación `504:58892` | Éxito `504:58880` |
|---|---|---|
| Ícono / círculo | `alert-circle` / `#F8F8F8` | `tick-02` / `#F0FDF4` |
| Título | Confirmación de creación de **incidente** | Tu **incidente** se envió con éxito. |
| Cuerpo | …**[Tracking Number]**… | …sección de **incidentes**. …**[Courier Name]**… **XX días hábiles**. |
| Acciones | `Cancelar` + `Sí, confirmar` | `Entendido` |

> ✅ **Cuarta confirmación de que los modales de cierre son transversales**, no específicos por tipo. Ya documentados una sola vez (§CC.24.6); aquí solo se referencian.

### CC.27.7 ✅ El Paso 2/2 escala por complejidad — cuatro variantes

Con la cuarta variante, el patrón de §CC.26.7 se confirma y **Retraso en la entrega marca el techo**:

| Tipo | Campos | Alto | Banner | Error de negocio | Colapsable |
|---|---|---|---|---|---|
| **Retraso en la entrega** (§CC.27) | 3 textareas + Costo + Moneda + **8 campos dirección** | **2,143 / 1,115** | — | — | ✅ |
| Cambio de dirección (§CC.24) | Motivo + card + 8 campos | 1,559 | — | Sí | ✅ |
| Paquete sin movimiento (§CC.25) | 3 textareas + Costo + Moneda + Piezas | 1,245 | 🔵 Sí | — | — |
| Recolección fallida (§CC.26) | 1 textarea | 780 (sin scroll) | — | — | — |

> ✅ **La complejidad sigue siendo proporcional a lo que la paquetería necesita para investigar.** Un retraso requiere el detalle del empaque y el producto (para valorar), el valor declarado y **la dirección de entrega completa** (para reubicar la entrega) — de ahí que sea el formulario más largo.
> ⚠️ **Es la variante que más scroll exige** (2,143 con dirección expandida). El colapsable es la mitigación: plegar la dirección baja el alto a 1,115. Documentar el estado por defecto (¿expandida o colapsada al entrar?): la maqueta muestra **expandida** en vacío y **colapsada** en lleno.

### CC.27.8 Componentes nuevos (vs. ya documentados)

Ninguno. Recombina: chrome del wizard e indicador de paso (§CC.22.3), textarea h141 r20 y bloque de dirección de 8 campos (§CC.24.4), fila Costo + Moneda (§CC.25.5), CTA full-width r12 y modales de confirmación y éxito (§CC.24.6). **El aporte es de composición, no de componentes.**

### CC.27.9 Pendientes (🔴)

1. 🔴 **Faltan tres Paso 2/2**: Paquete dañado, Paquete perdido, Paquete abierto o alterado (§CC.27.7). Los de daño probablemente requieran carga de evidencia fotográfica.
2. 🔴 **Sin estado de validación de campo** — cuarta variante consecutiva sin él.
3. ⚠️ **Contenedor del paso en `x=1`** (lleno) vs `x=0` (vacío). Mismo desplazamiento de 1px de §CC.26.5.
4. ⚠️ **Gap 7.328px** en textareas vs 7px en Costo — persiste la evidencia de **R1** (§CC.27.2).
5. ⚠️ **Header con la misma geometría no normalizada** que §CC.26: título en `x=77 w=207`, divisor en `y=106`, sin frame contenedor. Se suma a §CC.26.5.
6. ⚠️ **CTA no anclado** — en un formulario de 2,143px el CTA queda al final del contenido, sin fijarse al fondo. Misma decisión pendiente que §CC.26.7.

### CC.27.11 Referencias

- *Delivery Delay* (`504:58879`).
- **Paso 2/2 vacío (dir. expandida):** `504:59110` (header back `504:59114` / título `504:59116`, divisor `504:59117`; indicador `4256:14006` + `4256:14007`, barra `4256:14008`; contenido `4256:14009`; CTA `4256:14099`).
  - Campo 1 empaque: label `4256:14012`, textarea `4256:14013`, placeholder `4256:14016`.
  - Campo 2 producto: label `4256:14018`, placeholder `4256:14022`.
  - Costo/Moneda: `4256:14023` (`$` `4256:14030` / `MXN` `4256:14035`).
  - Campo 4 problema: label `4256:14039`, placeholder `4256:14043`.
  - Dirección: bloque `4256:14045`, header `4256:14047` + chevron `4256:14048`; campos `4256:14051`→`4256:14098`.
- **Paso 2/2 lleno (dir. colapsada):** `504:59927` (contenido `4256:14435`, x=1; valores `4256:14448` · `4256:14454` · `4256:14462` · `4256:14475`; dirección colapsada `4256:14479`; CTA `4256:14531`).
- **Modal confirmación:** `504:58892` (ícono `504:58898`, título `504:58903`, cuerpo `504:58904`, botones `504:58906` / `504:58907`).
- **Modal éxito:** `504:58880` (ícono `504:58886`, título `504:58889`, cuerpo `504:58890`, CTA `504:58891`).

## CC.28 Control de calidad — "Reportar incidencia" · Paso 2/2 · Paquete dañado (§CC.28)

> **Sección "Damaged Package"** (`504:60111`). **Quinta variante** del Paso 2/2 (§CC.11 punto 2). Avanza **M1** a **5 de 7** tipos.
> 4 pantallas: formulario vacío → lleno → modal de confirmación → modal de éxito.
> **Es la variante más rica en tipos de campo:** introduce **dos componentes nuevos** —el **radio Sí/No** y la **carga de evidencia fotográfica**—, esta última resolviendo la predicción abierta desde §CC.24.9 #6.
> **Figma:** `504:60111`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.28.1 Mapa del flujo

```
Paso 1/2 (§CC.22) · tipo = "Paquete dañado"
│
├── PASO 2/2 — VACÍO (504:64469) · alto 1,579
│   Tab "Paquete dañado" · PASO 2/2 · barra al 100%
│   🔵 Banner informativo (20 días hábiles) ← 2ª aparición (§CC.25.4)
│   1. Descripción del empaque       (textarea h141)
│   2. Contenido                      (input h93)
│   3. Número de piezas dañadas       (input h93)
│   4. Número de artículos en buen estado (input h93)
│   5. Número de artículos en buen estado (radio Sí/No)
│   6. Descripción del problema       (textarea h141)
│   7. Evidencia → 📷 dropzone "Subir fotos" (hasta 4, JPG/PNG, 5 MB)  ← NUEVO
│   CTA "Enviar incidencia" DESHABILITADO
│   │
│   └── captura + fotos ──▶ LLENO (504:64735) · alto 1,724 · CTA HABILITADO
│           Evidencia → grid 2×2: 3 fotos (con borrar) + 1 tile "añadir"
│           │
│           └── tap "Enviar incidencia" ──▶
│
├── MODAL DE CONFIRMACIÓN (504:60124) — idéntico a §CC.24 / §CC.25 / §CC.26 / §CC.27
│
└── MODAL DE ÉXITO (504:60112) — idéntico a §CC.24 / §CC.25 / §CC.26 / §CC.27
```

> ⚠️ **Primera variante donde el estado lleno es más alto que el vacío** (1,724 vs 1,579): las fotos cargadas expanden el grid. En §CC.24–§CC.27 el alto era estable entre estados.
> ✅ **Sin modal de error de negocio.** Coherente: no hay regla de unicidad que validar.

### CC.28.2 🔴 NUEVO: carga de evidencia fotográfica — `4256:14782` (vacío) / `4256:15046` (lleno)

**Primer componente de subida de archivos del módulo.** Resuelve la predicción de §CC.24.9 #6, §CC.26.9 #6 y §CC.27.9 #6: los tipos de daño requieren evidencia fotográfica.

**Estado vacío — dropzone (`4256:14782`):**
- Contenedor: fondo blanco, **borde punteado `1.25px #C3C3C3`** (Greys/400), **r20**, **h196**, w328. (Confirmado por design context.)
- Ícono `upload-square-02` 32px, centrado; gap 16 al texto.
- **"Subir fotos"** — `B2 S` 14 SemiBold `-0.28px` negro.
- **Ayuda** — `B3 R` **12 Regular** `#4C4C4C`: *"Sube hasta 4 imágenes claras que muestren el daño en el empaque y el contenido. Formatos permitidos: JPG, PNG. Tamaño máximo por archivo: 5 MB."*

**Estado lleno — grid (`4256:15046`, h335):**
- **Grid 2×2**, gap ~7px, tiles de **159.91×163.55** (r por confirmar).
- **3 fotos cargadas** (`4256:15047` · `4256:15055` · `4256:15063`), cada una con botón **borrar** (`delete-02` ~14.5px en círculo 29px, esquina superior derecha).
- **4º tile = "añadir"** (`4256:15071`): ícono `Plus` centrado, sin foto. No es una cuarta foto.

> ✅ **Componente bien resuelto:** dropzone → grid con borrado individual y tile de añadir. Cubre el caso de 1–4 fotos.
> 🔴 **Especificar el comportamiento al llegar a 4 fotos:** ¿desaparece el tile "añadir"? El límite (4) está en el copy, pero la maqueta solo muestra 3 + añadir. Definir el estado de 4/4.
> 🔴 **Faltan estados:** subiendo (progreso), error (formato/tamaño inválido), y el mensaje cuando se excede 5 MB o un formato no permitido. Solo hay vacío y lleno.
> ⚠️ **Radio de los tiles (159.91×163.55) es un valor no redondo** — instancia con escalado horneado (R1). Al normalizar, cuadrar a un tamaño entero.

### CC.28.3 ✅ NUEVO: radio Sí/No — `4256:14765`

Segundo componente nuevo: un **grupo de radio de dos opciones**.

- Dos opciones de **81×47** cada una, gap 8 entre control y label.
- **Control** `Radio` 16px (`4256:15032` / `4256:15036`); seleccionado = relleno **Primary/600 `#DB3B2B`** (screenshot: "Sí" activo).
- **Labels** `B2 R` 14 Regular `-0.28px` negro: **"Sí"** (`4256:15033`) · **"No"** (`4256:15037`) — confirmado por design context.

### CC.28.5 🔵 Banner informativo — 2ª aparición

El **mismo banner de §CC.25.4** (`Messages`, `4256:14735`): `#F0F8FF` (Blue/500), r10, texto `B3 R` 12 `#2180FF` (Blue/300): *"Al seleccionar este incidente, se iniciará una investigación que puede durar hasta 20 días hábiles."*

> ✅ **Confirma que el banner es un componente compartido y transversal**, no específico de "Paquete sin movimiento". Un paquete dañado también abre investigación de 20 días.
> 🔴 **Escala Blue invertida** — mismo hallazgo R6 de §CC.25.4.

### CC.28.6 Campos de detalle

Cinco campos de captura de texto/número, gap label→control **7.328px**:

| # | Label | Nodo | Control | Placeholder (vacío) → Valor (lleno) |
|---|---|---|---|---|
| 1 | Descripción del empaque | `4256:14737` | textarea **h141** | *"Describe el tipo y estado del empaque externo e interno…"* → *"Caja de cartón con protección de plástico burbuja; presenta abolladuras y rasgaduras en las esquinas."* |
| 2 | Contenido | `4256:14743` | input **h93** | *"Detalla los artículos contenidos en el paquete. Ejemplo: 'Dos tazas de cerámica'"* → *"Dos tazas de cerámica modelo ABC123."* |
| 3 | Número de piezas dañadas | `4256:14750` | input h93 | *"Ingresa la cantidad de artículos dañados"* → `2` |
| 4 | Número de artículos en buen estado | `4256:14757` | input h93 | *"Ingresa la cantidad de artículos en buen estado."* → `3` |
| 6 | Descripción del problema | `4256:14775` | textarea h141 | *"Describe con detalle el problema encontrado. Ejemplo: 'El paquete llegó mojado y las cajas internas estaban dañadas.'"* → *"Al abrir el paquete, se observó que una de las tazas tenía el asa rota…"* |

- Todos borde `1px #F3F3F3`, r20, `p12`. Textareas h141 · inputs de una línea h93.
- **CTA "Enviar incidencia"** (`4256:14788` / `4256:15078`) — full-width 328×40, r12. `#F1B0A9` off / `#DB3B2B` on.

### CC.28.7 Modales

Idénticos a §CC.24.6 / §CC.25.6 / §CC.26.6 / §CC.27.6.

| | Confirmación `504:60124` | Éxito `504:60112` |
|---|---|---|
| Ícono / círculo | `alert-circle` / `#F8F8F8` | `tick-02` / `#F0FDF4` |
| Título | Confirmación de creación de **incidente** | Tu **incidente** se envió con éxito. |
| Cuerpo | …**[Tracking Number]**… | …sección de **incidentes**. …**[Courier Name]**… **XX días hábiles**. |
| Acciones | `Cancelar` + `Sí, confirmar` | `Entendido` |

### CC.28.8 ✅ El Paso 2/2 escala por complejidad — cinco variantes

| Tipo | Campos | Alto | Banner | Evidencia | Componentes nuevos |
|---|---|---|---|---|---|
| Retraso en la entrega (§CC.27) | 3 textareas + Costo + Moneda + 8 campos dirección | **2,143 / 1,115** | — | — | — |
| **Paquete dañado** (§CC.28) | 5 campos + radio Sí/No | **1,579 / 1,724** | 🔵 Sí | 📷 **Sí** | radio + subida de fotos |
| Cambio de dirección (§CC.24) | Motivo + card + 8 campos | 1,559 | — | — | — |
| Paquete sin movimiento (§CC.25) | 3 textareas + Costo + Moneda + Piezas | 1,245 | 🔵 Sí | — | banner |
| Recolección fallida (§CC.26) | 1 textarea | 780 | — | — | — |

> ✅ **La complejidad sigue siendo proporcional a la investigación:** un paquete dañado requiere describir empaque y contenido, contar piezas dañadas y en buen estado, **y aportar fotos del daño**. Es la única con evidencia visual porque es la única donde el daño es demostrable.
> ✅ **Confirma que los tipos de daño suman evidencia fotográfica** (predicho en §CC.24/§CC.26/§CC.27). Presumiblemente *Paquete abierto o alterado* (§CC.29 pendiente) también.

### CC.28.9 Componentes nuevos (vs. ya documentados)

**Dos nuevos:**
1. **Subida de evidencia fotográfica** (`4256:14782` dropzone / `4256:15046` grid) — dashed 1.25px, r20; grid 2×2 con borrar + añadir (§CC.28.2).
2. **Radio Sí/No** (`4256:14765`) — control 16px, Primary/600 al seleccionar (§CC.28.3).

Recombina: chrome del wizard e indicador de paso (§CC.22.3), banner `Messages` (§CC.25.4), textareas h141 e inputs h93 r20 (§CC.24/§CC.25), CTA r12 y modales (§CC.24.6).

### CC.28.10 Pendientes (🔴)

1. 🔴 **Componente de evidencia sin estados completos** — falta 4/4 (¿desaparece "añadir"?), subiendo, y error de formato/tamaño (§CC.28.2).
2. 🔴 **Faltan dos Paso 2/2**: Paquete perdido y Paquete abierto o alterado (§CC.28.8).
3. 🔴 **Sin estado de validación de campo** — quinta variante consecutiva sin él.
4. ⚠️ **Estado lleno más alto que el vacío** (1,724 vs 1,579) por las fotos — definir alto de referencia (§CC.28.1).
5. ⚠️ **Radio de tiles de foto 159.91×163.55** — valor no redondo (escalado horneado, R1) (§CC.28.2).
6. ⚠️ **Header con la misma geometría no normalizada** (título `x=77`, divisor `y=106`) que §CC.26/§CC.27.

### CC.28.12 Referencias

- *Damaged Package* (`504:60111`).
- **Paso 2/2 vacío:** `504:64469` (header `504:64473` / `504:64475`, divisor `504:64476`; indicador `4256:14730` + `4256:14731`, barra `4256:14732`; contenido `4256:14734`; CTA `4256:14788`).
  - Banner: `4256:14735`. Empaque: label `4256:14737`, ph `4256:14741`. Contenido: `4256:14743` / `4256:14747`. Piezas dañadas: `4256:14750` / `4256:14754`. Artículos buen estado (input): `4256:14757` / `4256:14761`. Radio: label `4256:14764`, grupo `4256:14765` (Sí `4256:14769`... render, No). Problema: `4256:14775` / `4256:14779`. Evidencia: label `4256:14781`, dropzone `4256:14782` (icono `4256:14784`, "Subir fotos" `4256:14786`, ayuda `4256:14787`).
- **Paso 2/2 lleno:** `504:64735` (contenido `4256:14998`; valores `4256:15005` · `4256:15011` · `4256:15018` · `4256:15025` · radio `4256:15029` · `4256:15043`; evidencia grid `4256:15046` → fotos `4256:15047`/`4256:15055`/`4256:15063`, añadir `4256:15071`; CTA `4256:15078`).
- **Modal confirmación:** `504:60124` (ícono `504:60130`, título `504:60135`, cuerpo `504:60136`, botones `504:60138` / `504:60139`).
- **Modal éxito:** `504:60112` (ícono `504:60118`, título `504:60121`, cuerpo `504:60122`, CTA `504:60123`).

## CC.29 Control de calidad — "Reportar incidencia" · Paso 2/2 · Paquete perdido (§CC.29)

> **Sección "Lost Package"** (`504:68781`). **Sexta variante** del Paso 2/2 (§CC.11 punto 2). Avanza **M1** a **6 de 7** tipos — falta solo *Paquete abierto o alterado*.
> 4 pantallas: formulario vacío → lleno → modal de confirmación → modal de éxito.
> **Recombinación más limpia hasta ahora:** los 6 campos exactos de §CC.25 + **dos adjuntos de documento (PDF)**. Introduce el **segundo modo de subida**: archivo único (factura, guía), distinto del grid de fotos de §CC.28.
> **Figma:** `504:68781`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.29.1 Mapa del flujo

```
Paso 1/2 (§CC.22) · tipo = "Paquete perdido"
│
├── PASO 2/2 — VACÍO (504:69156) · alto 1,661
│   Tab "Paquete perdido" · PASO 2/2 · barra al 100%
│   🔵 Banner informativo (20 días hábiles) ← 3ª aparición
│   1. Descripción del problema         (textarea h141)
│   2. Descripción del empaque          (textarea h118)
│   3. Descripción exacta del producto  (textarea h110)
│   4. Costo [226px] + Moneda [93px]
│   5. Número de piezas                 (input h55)
│   6. Adjuntar factura → 📄 dropzone PDF (máximo 5 MB)  ← NUEVO modo: archivo único
│   7. Adjuntar guía    → 📄 dropzone PDF (máximo 5 MB)
│   CTA "Enviar incidencia" DESHABILITADO
│   │
│   └── captura + PDFs ──▶ LLENO (504:69347) · alto 1,661 · CTA HABILITADO
│           Factura → thumbnail PDF con borrar · Guía → thumbnail PDF con borrar
│           │
│           └── tap "Enviar incidencia" ──▶
│
├── MODAL DE CONFIRMACIÓN (504:68794) — idéntico a §CC.24 … §CC.28
│
└── MODAL DE ÉXITO (504:68782) — idéntico a §CC.24 … §CC.28
```

> ✅ **Sin modal de error de negocio.** Coherente.

### CC.29.2 ✅ Recombinación limpia: el formulario de §CC.25 + dos adjuntos

Los seis campos de captura **coinciden exactamente** con §CC.25 (*Paquete sin movimiento*), que a su vez era el de §CC.19 (§CC.25.3):

| Campo | §CC.25 / §CC.19 | §CC.29 |
|---|---|---|
| Descripción del problema | ✅ | ✅ (placeholder de "paquete perdido") |
| Descripción del empaque | ✅ | ✅ |
| Descripción exacta del producto | ✅ | ✅ |
| Costo + Moneda | ✅ | ✅ |
| Número de piezas | ✅ `Ingresa la cantidad de artículos` | ✅ mismo |
| **Adjuntar factura + Adjuntar guía** | — | 🆕 **dos adjuntos PDF** |

> ✅ **A diferencia de §CC.27 y §CC.28, aquí no hay colisión de etiquetas ni campos mal rotulados.** Es la recombinación mejor ejecutada del bloque: reutiliza el grupo de §CC.25 intacto y le suma los adjuntos. Confirma **§CC.27.4** (los Paso 2/2 se componen de grupos de campos) mostrando el caso limpio.
> ⚠️ **Alturas de textarea inconsistentes en vacío:** problema `h141`, empaque `h118`, producto `h110`. En §CC.25 los tres eran uniformes. Definir un `min-height` común; hoy parecen auto-ajustados al contenido de la maqueta.

### CC.29.3 🔴 NUEVO modo de subida: archivo único (PDF)

Segundo modo del componente de subida, **distinto del grid de fotos de §CC.28**:

| | §CC.28 · Evidencia | **§CC.29 · Adjuntar factura / guía** |
|---|---|---|
| Cardinalidad | **múltiple** (hasta 4) | **única** (1 archivo por adjunto) |
| Formato | JPG, PNG | **PDF** |
| Lleno | grid 2×2 (fotos + tile "añadir") | **un thumbnail** con borrar (sin grid, sin "añadir") |
| Instancias | 1 | **2** (factura `4256:15321`, guía `4256:15329`) |

- **Vacío:** mismo shell que §CC.28 — dropzone punteado, `upload-square-02` 32px, h196.
  - Factura (`4256:15326`): *"Sube una copia de la factura que respalde el valor del contenido del envío. PDF, máximo 5 MB."*
  - Guía (`4256:15334`): *"Sube una copia de la guía de envío o recibo que contenga el número de tracking. PDF, máximo 5 MB."*
- **Lleno:** un solo tile 159.91×163.55 con `delete-02` (`4256:15582` factura, `4256:15592` guía) — el mismo tile de §CC.28 pero sin grid ni tile de añadir.

> 🔴 **Un mismo componente, dos modos, copy hardcodeado.** El shell de subida es el mismo (§CC.28 y §CC.29), pero el CTA del dropzone queda fijo incluso en el modo de adjuntar PDF, contradiciendo su propio texto de ayuda ("PDF, máximo 5 MB") dentro del mismo componente. Al parametrizar el componente, el CTA y el formato aceptado deben ser props (`fotos`/`archivo`, `image/*`/`application/pdf`).
> 🔴 **Falta el estado de error** (formato no PDF, >5 MB) y el de subiendo — igual que §CC.28.2.

### CC.29.4 🔵 Banner informativo — 3ª aparición

Mismo banner de §CC.25.4 / §CC.28.5 (`Messages`, `4256:15277`): *"Al seleccionar este incidente, se iniciará una investigación que puede durar hasta 20 días hábiles."*

> ✅ **Tercera aparición** — confirma definitivamente que el banner es transversal a los tipos que abren investigación (sin movimiento, dañado, perdido).

### CC.29.5 Campos de captura

Gap label→control **7.328px**; Costo usa **7px**.

| # | Label | Nodo | Placeholder (vacío) → Valor (lleno) |
|---|---|---|---|
| 1 | Descripción del problema | `4256:15279` | *"Describe la situación. Ejemplo: 'El paquete no ha tenido actualizaciones en el tracking desde el 03/05/2025…'"* → *"El paquete no ha tenido actualizaciones en el tracking desde el 03/05/2025 y la paquetería no puede localizarlo."* |
| 2 | Descripción del empaque | `4256:15285` | *"Describe el tipo y estado del empaque utilizado para el envío…"* → *"Caja de cartón de doble pared con relleno de espuma, sin etiquetas de fragilidad."* |
| 3 | Descripción exacta del producto | `4256:15292` | *"Especifica la marca, modelo, color…"* → *"Smartphone marca XYZ, modelo ABC123, color negro, 128 GB."* |
| 4 | Costo + Moneda | `4256:15300` | `$` / `MXN` → `$ 13,587.00` / `MXN` |
| 5 | Número de piezas | `4256:15314` | *"Ingresa la cantidad de artículos"* → `2` |

- Borde `1px #F3F3F3`, r20, `p12`. CTA `4256:15335` / `4256:15600` — r12, `#F1B0A9` off / `#DB3B2B` on.

### CC.29.6 Modales

Idénticos a §CC.24.6 … §CC.28.7.

| | Confirmación `504:68794` | Éxito `504:68782` |
|---|---|---|
| Ícono / círculo | `alert-circle` / `#F8F8F8` | `tick-02` / `#F0FDF4` |
| Título | Confirmación de creación de **incidente** | Tu **incidente** se envió con éxito. |
| Cuerpo | …**[Tracking Number]**… | …sección de **incidentes**. …**[Courier Name]**… **XX días hábiles**. |
| Acciones | `Cancelar` + `Sí, confirmar` | `Entendido` |

### CC.29.7 ✅ Los dos modos de subida del módulo — resumen

Con §CC.28 y §CC.29 quedan documentados **los dos modos** del componente de subida:

| Modo | Tipo | Formato | Cardinalidad | Estado lleno | Sección |
|---|---|---|---|---|---|
| **Fotos** | Evidencia | JPG, PNG | hasta 4 | grid 2×2 + "añadir" | §CC.28 |
| **Archivo** | Factura, Guía | PDF | 1 c/u | thumbnail + borrar | §CC.29 |

> ✅ **Es el mismo componente base** (dropzone punteado + tile 159.91×163.55 con `delete-02`) en dos configuraciones. **Documentar como un componente con props** (`accept`, `multiple`, `maxFiles`, `ctaLabel`) resuelve el copy "Subir fotos" y unifica ambos usos.

### CC.29.8 Componentes nuevos (vs. ya documentados)

**Uno nuevo (modo):** subida de **archivo único (PDF)** — reconfiguración del componente de §CC.28 (§CC.29.3). Recombina: chrome del wizard (§CC.22.3), banner `Messages` (§CC.25.4), grupo de 6 campos de §CC.25/§CC.19, CTA r12 y modales (§CC.24.6).

### CC.29.9 Pendientes (🔴)

1. 🔴 **Componente de subida con copy hardcodeado** — el CTA "Subir fotos" queda fijo incluso en el modo de adjuntar PDF; parametrizar CTA y formato aceptado como props (§CC.29.3, §CC.29.7).
2. 🔴 **Sin estados de subiendo/error** en los dos modos de subida — se arrastra desde §CC.28.2.
3. 🔴 **Falta un Paso 2/2**: Paquete abierto o alterado — **último para cerrar M1** (§CC.29.1).
4. 🔴 **Sin estado de validación de campo** — sexta variante consecutiva sin él.
5. ⚠️ **Alturas de textarea inconsistentes** en vacío (141 / 118 / 110) — definir `min-height` común (§CC.29.2).
6. ⚠️ **Gap 7.328px** en campos vs 7px en Costo — persiste R1.
7. ⚠️ **Header con la misma geometría no normalizada** (título `x=77`, divisor `y=106`) que §CC.26–§CC.28.

### CC.29.11 Referencias

- *Lost Package* (`504:68781`).
- **Paso 2/2 vacío:** `504:69156` (header `504:69160` / `504:69162`, divisor `504:69163`; indicador `4256:15265` + `4256:15266`, barra `4256:15267`; contenido `4256:15269`; CTA `4256:15335`).
  - Banner: `4256:15277`. Problema: `4256:15279` / ph `4256:15283`. Empaque: `4256:15285` / `4256:15289`. Producto: `4256:15292` / `4256:15296`. Costo/Moneda: `4256:15298` (`$` `4256:15305` / `MXN` `4256:15310`). Piezas: `4256:15314` / `4256:15318`.
  - Adjuntar factura: label `4256:15320`, dropzone `4256:15321` (icono `4256:15323`, "Subir fotos" `4256:15325`, ayuda `4256:15326`).
  - Adjuntar guía: label `4256:15328`, dropzone `4256:15329` ("Subir fotos" `4256:15333`, ayuda `4256:15334`).
- **Paso 2/2 lleno:** `504:69347` (contenido `4256:15537`; valores `4256:15544` · `4256:15550` · `4256:15557` · `4256:15566` · `4256:15579`; factura thumbnail `4256:15582` (borrar `4256:15585`), guía thumbnail `4256:15592` (borrar `4256:15595`); CTA `4256:15600`).
- **Modal confirmación:** `504:68794` (ícono `504:68800`, título `504:68805`, cuerpo `504:68806`, botones `504:68808` / `504:68809`).
- **Modal éxito:** `504:68782` (ícono `504:68788`, título `504:68791`, cuerpo `504:68792`, CTA `504:68793`).

## CC.30 Control de calidad — "Reportar incidencia" · Paso 2/2 · Paquete abierto o manipulado (§CC.30)

> **Sección "Opened or Tampered Package"** (`504:73261`). **Séptima y última variante** del Paso 2/2 (§CC.11 punto 2). **Cierra M1: 7 de 7.**
> 4 pantallas: formulario vacío → lleno → modal de confirmación → modal de éxito.
> **No aporta componentes nuevos:** 4 textareas + el grid de evidencia fotográfica de §CC.28 (segundo uso, segunda confirmación del componente de subida).
> **Figma:** `504:73261`. **Owner:** Karla Salazar — Head of UX/UI.

### CC.30.1 Mapa del flujo

```
Paso 1/2 (§CC.22) · tipo = "Paquete abierto o alterado"
│
├── PASO 2/2 — VACÍO (504:73968) · alto 1,371
│   Tab "Paquete abierto o manipulado" · PASO 2/2 · barra al 100%
│   🔵 Banner informativo (20 días hábiles) ← 4ª aparición
│   1. Descripción del empaque              (textarea h141)
│   2. Descripción exacta del producto      (textarea h118)  ← placeholder "producto faltante"
│   3. Contenido declarado del paquete      (textarea h110)  ← label nuevo
│   4. Descripción del problema             (textarea h110)
│   5. Evidencia → 📷 grid de fotos (hasta 4, JPG/PNG, 5 MB) ← modo §CC.28
│   CTA "Enviar incidencia" DESHABILITADO
│   │
│   └── captura + fotos ──▶ LLENO (504:74068) · alto 1,490 · CTA HABILITADO
│           Evidencia → grid 2×2: 3 fotos (con borrar) + 1 tile "añadir"
│           │
│           └── tap "Enviar incidencia" ──▶
│
├── MODAL DE CONFIRMACIÓN (504:73274) — idéntico a §CC.24 … §CC.29
│
└── MODAL DE ÉXITO (504:73262) — idéntico a §CC.24 … §CC.29
```

> ⚠️ **Estado lleno más alto que el vacío** (1,490 vs 1,371) por las fotos — como §CC.28.

### CC.30.3 Campos de captura — cuatro textareas

Gap label→control **7.328px**; alturas de textarea en vacío **141 / 118 / 110 / 110** (misma inconsistencia de §CC.29.2).

| # | Label | Nodo | Placeholder (vacío) → Valor (lleno) |
|---|---|---|---|
| 1 | Descripción del empaque | `4257:15944` | *"Describe el estado y tipo de empaque al recibir el paquete…"* → *"Caja de cartón sellada con cinta transparente; muestra signos de apertura en una esquina y el sello de seguridad está roto."* |
| 2 | Descripción exacta del producto | `4257:15950` | *"Especifica marca, modelo, color y otras características del **producto faltante**…"* → *"Laptop marca XYZ, modelo UltraBook 15, color plata, 16GB RAM, 512GB SSD"* |
| 3 | **Contenido declarado del paquete** 🆕 | `4257:15957` | *"Lista todos los artículos que debían estar en el paquete según el pedido original…"* → *"1 laptop XYZ UltraBook 15, 1 cargador, 1 manual de usuario."* |
| 4 | Descripción del problema | `4257:15964` | *"Detalla la situación observada al recibir el paquete…"* → *"Al recibir el paquete, se observó que la caja mostraba signos de manipulación. Al abrirla, la laptop no estaba…"* |

> ✅ **"Contenido declarado del paquete" es un label nuevo bien pensado** para este tipo: pide el contenido *esperado* (según el pedido) para contrastarlo con lo recibido — clave cuando falta producto. Es la variante del grupo "detalle de texto" adaptada al caso de manipulación.

### CC.30.4 Evidencia — segundo uso del grid de fotos (§CC.28)

Idéntico al de §CC.28.2: dropzone punteado "Subir fotos" (`4257:15972`) → grid 2×2 (`4257:16177`) con 3 fotos + tile de añadir.

> ✅ **Segundo uso del modo "fotos"** (el 1º fue §CC.28) — confirma que los tipos con daño/manipulación comparten el mismo componente de evidencia. Aquí el CTA "Subir fotos" **sí es correcto** (son fotos), a diferencia del bug de §CC.29.3 (PDF).
> 🔴 **Mismos pendientes del componente:** faltan estados 4/4, subiendo y error (§CC.28.2).

### CC.30.5 🔵 Banner informativo — 4ª aparición

Mismo `Messages` (`4257:15942`): investigación de 20 días hábiles.

> ✅ **Cuarta aparición** (sin movimiento, dañado, perdido, abierto) — banner transversal, definitivamente confirmado.

### CC.30.6 Modales

Idénticos a §CC.24.6 … §CC.29.6.

| | Confirmación `504:73274` | Éxito `504:73262` |
|---|---|---|
| Ícono / círculo | `alert-circle` / `#F8F8F8` | `tick-02` / `#F0FDF4` |
| Título | Confirmación de creación de **incidente** | Tu **incidente** se envió con éxito. |
| Cuerpo | …**[Tracking Number]**… | …sección de **incidentes**. …**[Courier Name]**… **XX días hábiles**. |
| Acciones | `Cancelar` + `Sí, confirmar` | `Entendido` |

### CC.30.7 ✅ M1 CERRADO — las siete variantes del Paso 2/2

Con §CC.30 se documentan **los siete Paso 2/2** de "Reportar incidencia" (§CC.11 punto 2). **Pendiente M1 de §CC.23.7: cerrado.**

| # | Tipo | §CC | Composición | Alto (vacío/lleno) | Banner | Evidencia |
|---|---|---|---|---|---|---|
| 1 | Cambio de dirección | §CC.24 | Motivo + card actual + 8 campos dirección | 1,559 | — | — |
| 2 | Paquete sin movimiento | §CC.25 | 3 textareas + Costo + Moneda + Piezas | 1,245 | 🔵 | — |
| 3 | Recolección fallida | §CC.26 | 1 textarea | 780 | — | — |
| 4 | Retraso en la entrega | §CC.27 | 3 textareas + Costo + Moneda + 8 campos dirección | 2,143 / 1,115 | — | — |
| 5 | Paquete dañado | §CC.28 | 5 campos + radio Sí/No | 1,579 / 1,724 | 🔵 | 📷 fotos |
| 6 | Paquete perdido | §CC.29 | 6 campos (=§CC.25) | 1,661 | 🔵 | 📄 PDF ×2 |
| 7 | Paquete abierto o manipulado | §CC.30 | 4 textareas | 1,371 / 1,490 | 🔵 | 📷 fotos |

**Biblioteca de grupos de campos** (composición confirmada tras las 7 variantes — entregable para dev):

| Grupo | Componentes | Usado en |
|---|---|---|
| **G1 · Detalle de texto** | textareas (empaque, producto, contenido, contenido declarado, problema) | todas |
| **G2 · Valor declarado** | Costo [226] + Moneda [93] | §CC.25, §CC.27, §CC.29 |
| **G3 · Cantidad** | input numérico (piezas / dañadas / buen estado) | §CC.25, §CC.28, §CC.29 |
| **G4 · Dirección** | 8 campos (colapsable) | §CC.24, §CC.27 |
| **G5 · Card dirección actual + acción** | card compacta | §CC.24 |
| **G6 · Subida** | fotos (multi, JPG/PNG) · archivo (single, PDF) | §CC.28, §CC.29, §CC.30 |
| **G7 · Radio Sí/No** | radio 16px | §CC.28 |
| **G8 · Banner investigación** | `Messages` azul, 20 días | §CC.25, §CC.28, §CC.29, §CC.30 |
| **Cierre** | modal confirmación + éxito (+ error de negocio en §CC.24) | todas |

> ✅ **Confirmado: el Paso 2/2 es composición de ~9 grupos reutilizables, no 7 formularios independientes ni uno parametrizado.** **Recomendación para dev:** implementar los grupos G1–G8 + cierre como bloques, y cada tipo como una lista ordenada de grupos. Esto evita inconsistencias de etiquetado entre campos y centraliza el copy hoy hardcodeado del componente de subida (§CC.29.3).

### CC.30.8 🔴 Defectos transversales de las 7 variantes (para §CC.23)

Estos hallazgos **se repiten en casi todas** y deben resolverse **una sola vez en el componente/patrón**, no variante por variante:

| Defecto | Apariciones | Corrección |
|---|---|---|
| Subida: CTA "Subir fotos" hardcodeado | §CC.28–30 (bug real en §CC.29) | Parametrizar `ctaLabel` / `accept` |
| Header no normalizado (título `x=77`, divisor `y=106`) | §CC.26–30 | Normalizar al patrón §CC.24 |
| Sin estado de validación de campo | **7** | Definir estados de error de input |
| Gap 7.328px vs 7px (Costo) — R1 | todas | Cuadrar a entero |

### CC.30.9 Componentes nuevos (vs. ya documentados)

Ninguno. Recombina: chrome del wizard (§CC.22.3), banner `Messages` (§CC.25.4), textareas h141/h118/h110 (§CC.29), grid de evidencia (§CC.28.2), CTA r12 y modales (§CC.24.6).

### CC.30.10 Pendientes (🔴)

1. 🔴 **Componente de evidencia sin estados** 4/4, subiendo, error (§CC.30.4, hereda §CC.28.2).
2. ⚠️ **Alturas de textarea inconsistentes** (141/118/110/110) — definir `min-height` común (§CC.30.3).
3. ⚠️ **Header no normalizado** (título `x=77`, divisor `y=106`) — §CC.26–30.

### CC.30.12 Referencias

- *Opened or Tampered Package* (`504:73261`).
- **Paso 2/2 vacío:** `504:73968` (header `504:73972` / `504:73974`, divisor `504:73975`; indicador `4257:15930` + `4257:15931`, barra `4257:15932`; contenido `4257:15934`; CTA `4257:15978`).
  - Banner: `4257:15942`. Empaque: `4257:15944` / ph `4257:15948`. Producto: `4257:15950` / `4257:15954`. Contenido declarado: `4257:15957` / `4257:15961`. Problema: `4257:15964` / `4257:15968`. Evidencia: label `4257:15971`, dropzone `4257:15972` ("Subir fotos" `4257:15976`, ayuda `4257:15977`).
- **Paso 2/2 lleno:** `504:74068` (contenido `4257:16146`; valores `4257:16153` · `4257:16159` · `4257:16166` · `4257:16173`; evidencia grid `4257:16177` → fotos `4257:16178`/`4257:16186`/`4257:16194`, añadir `4257:16202`; CTA `4257:16209`).
- **Modal confirmación:** `504:73274` (ícono `504:73280`, título `504:73285`, cuerpo `504:73286`, botones `504:73288` / `504:73289`).
- **Modal éxito:** `504:73262` (ícono `504:73268`, título `504:73271`, cuerpo `504:73272`, CTA `504:73273`).
