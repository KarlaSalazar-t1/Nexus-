# App Flows — NEXUS V2.0

> Los flujos documentan cómo se ensamblan pantallas y componentes de la **app móvil nativa** de T1 para completar tareas de usuario de principio a fin. Son la referencia de implementación para secuencias de más de una pantalla — mismo nivel de detalle que [`FLOWS.md`](./FLOWS.md), aplicado a la App.
>
> Para tokens (tipografía, color, spacing, radios) ver [`../plataform/APP.md`](../plataform/APP.md). Para el detalle profundo pantalla-por-pantalla, hallazgos de auditoría y trazabilidad a Figma, ver [`../plataform/T1APP.md`](../plataform/T1APP.md).

**Última actualización:** Septiembre 2026 · **Fuente de verdad:** Figma — `T1-App---ESP` (`viFhO18oodfFqrvyDznrA9`) · **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Login, registro y onboarding](#1-login-registro-y-onboarding)
2. [Home — Pantalla principal](#2-home--pantalla-principal)
3. [Crear tienda con IA (Nova)](#3-crear-tienda-con-ia-nova)
4. [Agregar producto (manual / con IA)](#4-agregar-producto-manual--con-ia)
5. [Conectar canales de venta (caso Shein)](#5-conectar-canales-de-venta-caso-shein)
6. [Agregar dirección de origen](#6-agregar-dirección-de-origen)
7. [Configurar tarifas de envío](#7-configurar-tarifas-de-envío)
8. [Activar T1 pagos](#8-activar-t1-pagos)
9. [Nombre de la tienda](#9-nombre-de-la-tienda)
10. [Dominio personalizado](#10-dominio-personalizado)
11. [Conectar redes sociales](#11-conectar-redes-sociales)
12. [Configurar políticas de la tienda](#12-configurar-políticas-de-la-tienda)
13. [Pedidos — Listado](#13-pedidos--listado)
14. [Detalle de pedido — Ciclo completo](#14-detalle-de-pedido--ciclo-completo)
15. [Crear pedido](#15-crear-pedido)
16. [Carrito abandonado](#16-carrito-abandonado)
17. [Productos — Listado](#17-productos--listado)
18. [Agregar producto](#18-agregar-producto)
19. [Agregar producto con IA](#19-agregar-producto-con-ia)
20. [Inventario](#20-inventario)
21. [Precios](#21-precios)
22. [Catálogo](#22-catálogo)
23. [Sucursales](#23-sucursales)
24. [Envíos](#24-envíos)
25. [Configuración de envíos — Reglas de prioridad](#25-configuración-de-envíos--reglas-de-prioridad)
26. [Control de calidad — Incidencias](#26-control-de-calidad--incidencias)
27. [Reportar incidencia — Paso 2/2](#27-reportar-incidencia--paso-22)

---

## 1. Login, registro y onboarding

**Producto:** Ecosistema T1 (App móvil — login unificado)
**Figma:** `107:22340`

### Estructura del flujo

```
Splash
  └─(auto, ~2s)→ Welcome (autenticación)
                    ├─ Inicia sesión               → Autenticación web → Pantalla principal
                    └─ Continuar con Google/correo → Onboarding (6 pasos)
                                    1. ¿Qué te gustaría hacer con T1?     (multi-select)
                                    2. ¿En qué etapa está tu negocio?     (single-select) ─┐ bifurcación
                                    3. ¿Cómo se llama tu negocio?         (input + IA)      │
                                    4a. ¿Dónde te gustaría vender?  ← negocio nuevo ────────┘
                                    4b. ¿Dónde vendes actualmente? ← negocio existente
                                    5. ¿Cuánto vendes al año?             (single-select)
                                    └→ Loader (configurando cuenta) → Pantalla principal
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Tarjeta de opción seleccionable | Tarjeta con ícono y label; marca visualmente la opción activa con un check |
| Selección única (radio) | Control circular; una sola opción activa a la vez |
| Stepper de progreso | Indicador de pasos (dots) en la cabecera; conserva la misma posición aunque el paso 4 se bifurque |
| Chip de sugerencia | Chip tocable que rellena el input al seleccionarse; distingue sugerencia generada por IA de las genéricas |
| Input / Textarea | Campo de texto para nombre y descripción del negocio |
| Bottom sheet | Hoja inferior para capturar la descripción del negocio y generar sugerencias de nombre con IA |
| Loader de proceso | Pantalla de carga bloqueante con mensaje de estado cíclico mientras se configura la cuenta |

### Reglas de interacción y validación

- Multi-select: el botón "Continuar" se habilita con al menos una selección y muestra el contador "X de N seleccionadas".
- Single-select: elegir una opción deselecciona la anterior y habilita el avance.
- Bifurcación: la respuesta del paso 2 (negocio nuevo vs. existente) determina el contenido del paso 4 (intención de venta vs. canales actuales) sin cambiar su posición en el stepper.
- El asistente de IA para nombrar el negocio es opcional: requiere una descripción en el bottom sheet para generar sugerencias; tocar un chip rellena el input.
- "Atrás" conserva las selecciones ya hechas al volver a un paso anterior.
- Login de usuario existente delega la autenticación en un flujo web del sistema; al volver, entra directo a la pantalla principal.
- Cada paso ocupa una sola pantalla, sin scroll largo — el stepper es la única señal de progreso.

---

## 2. Home — Pantalla principal

**Producto:** Ecosistema T1 (App móvil)
**Figma:** `1532:69077`

### Estructura del flujo

Home no es un flujo lineal: es **una plantilla con variantes** según el producto principal del usuario y su estado de onboarding.

```
Home
├── Header (selector de tienda + notificaciones + avatar)
├── Configurar cuenta (carril de tarjetas de setup, o banner de encuesta si falta onboarding)
├── Métricas (carril de tarjetas + "Ver reporte detallado")
├── Acciones rápidas (3 tarjetas)
├── Nova Insights (carril de insights)
├── Promo cross-sell (card oscura; se omite si el usuario ya usa todos los servicios)
└── Tab bar + FAB "+" → grid de 6 accesos rápidos
```

### Variantes

| Variante | Qué la dispara | Diferencia principal |
|---|---|---|
| Envíos | Producto principal = T1 Envíos | Setup y métricas orientadas a envíos; promo cruza a Pagos/Tienda |
| Pagos | Producto principal = T1 Pagos | Setup y métricas orientadas a pagos; promo cruza a Tienda |
| Tienda / premium | Tienda con plan activo | Setup mínimo (producto, métodos de pago); promo cruza a Pagos premium |
| Tienda sin premium | Tienda sin plan activo | Igual a la anterior, con tarjeta destacada de IA para crear tienda |
| Seller sin tienda | Usuario sin tienda creada | Tarjeta destacada full-width "Crea tu tienda con IA" + carril largo de tareas de setup |
| All services | Usuario ya usa todos los productos | Sin card de promo (no hay siguiente producto que ofrecer) |
| Sin onboarding | Faltan datos de la encuesta inicial | El carril de setup se reemplaza por un banner "Personaliza tu experiencia" |

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Selector de tienda | Chip con avatar de iniciales + nombre + chevron; abre el cambio de tienda activa |
| Tarjeta de setup | Ícono + título + botón de acción (prioritaria o secundaria) + badge opcional de IA para tareas asistidas |
| Chip de progreso de setup | Indicador "X de N completados" en el header de la sección |
| Tarjeta destacada de creación con IA | Variante full-width de la tarjeta de setup, con badge premium, para cuando el usuario no tiene tienda |
| Banner de encuesta | Reemplaza el carril de setup cuando falta completar el onboarding; ofrece posponer o iniciar la encuesta |
| Tarjeta de métrica | Label + valor (conteo o monto) + delta opcional con color semántico + ícono de categoría |
| Tarjeta de acción rápida | Ícono + label, 3 por variante |
| Tarjeta de insight (Nova) | Ícono + texto + chevron; carril horizontal, contenido compartido entre variantes |
| Card promo (cross-sell) | Card oscura que invita a adoptar el siguiente producto del ecosistema; puede ser carrusel de 2 slides |
| Tab bar + FAB | Barra de navegación inferior tipo píldora con 5 accesos + botón flotante que despliega un menú de 6 accesos rápidos |

### Reglas de interacción y validación

- El contenido de cada sección se deriva del producto principal del usuario — la anatomía de la pantalla es la misma en todas las variantes, solo cambian los datos.
- La card promo es cross-sell del siguiente producto que el usuario no usa todavía, y desaparece por completo cuando ya usa todos los servicios del ecosistema.
- Sin datos de onboarding completos, el carril de setup se reemplaza por el banner de encuesta.
- Las métricas de conteo operativo (envíos creados, en tránsito, entregados) no llevan delta; las métricas financieras o de calidad (costo, saldo, incidencias) sí.
- El color del delta es semántico según si el cambio es bueno o malo para el negocio, no según si es positivo o negativo — ej. una baja en incidencias se muestra en verde aunque el número tenga signo negativo.
- Al completar una tarea de setup, el flujo siempre regresa al Home completo (no a una versión reducida) con animación de confeti como única señal de éxito.

---

## 3. Crear tienda con IA (Nova)

**Producto:** T1 Tienda (App móvil)
**Figma:** `590:24176`

### Estructura del flujo

```
Home (seller sin tienda) ─[Create store]→
  Nova AI — prompt de creación
     (escribe prompt / elige categoría / dicta por voz) → enviar
        ↓
  Loader Nova AI (genera la tienda, status cíclico)
        ↓
  Preview "Mi tienda" (in-app) ─[Visit Store]→ Storefront web (vista pública)
        ↓ (Done, ir al inicio)
  Home con tienda creada + confeti
```

> **Caso — crear otra tienda:** mismo flujo completo; solo cambia el punto de entrada (selector de tiendas en el header, en vez de la tarjeta destacada del home) cuando el usuario ya tiene al menos una tienda.

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Badge Nova AI | Indicador de que el asistente de IA (Nova) está activo; acento morado distintivo para toda la marca del asistente |
| Input de prompt | Campo de texto libre para pedirle a la IA que genere la tienda, con botón de enviar |
| Chip de categoría | Selección rápida de categoría de negocio como alternativa a escribir un prompt |
| Sheet de grabación de voz | Alternativa de captura por voz, con temporizador y forma de onda, para dictar el prompt |
| Loader de proceso | Pantalla de carga con mensaje de estado cíclico mientras la IA genera la tienda |
| Preview de tienda | Vista in-app de la tienda generada, con selector de página y acceso directo a la tienda pública |
| FAB Nova (orbe) | Acceso flotante al asistente Nova, disponible sobre la preview y el storefront |
| Banner de plan | Aviso para desbloquear funciones completas de la tienda (upgrade de plan) |
| Mensaje informativo | Aviso de que la edición de la tienda solo está disponible en escritorio |
| Selector de tiendas | Punto de entrada alterno para crear una tienda adicional cuando ya existe al menos una |
| Confeti de celebración | Señal de éxito al cerrar el flujo, superpuesta sobre la pantalla principal |

### Reglas de interacción y validación

- El usuario puede iniciar la generación de tres formas equivalentes: prompt libre, categoría predefinida o dictado por voz.
- Enviar el prompt dispara el loader; tras el delay de generación, la IA entrega una tienda lista para previsualizar.
- El prompt tiene un límite de caracteres, con aviso al alcanzarlo.
- "Visit Store" abre la tienda generada tal como la vería un comprador; "Done, ir al inicio" cierra el flujo y regresa a la pantalla principal.
- El cierre del flujo siempre muestra confeti sobre la pantalla principal como única señal de éxito — no hay banner de confirmación adicional.
- Crear una tienda adicional reutiliza el flujo completo sin componentes nuevos; solo cambia el punto de entrada.

---

## 4. Agregar producto (manual / con IA)

**Producto:** T1 Tienda (App móvil)
**Figma:** `601:26477` (manual) · `601:26478` (con IA)

Dos variantes de captura — manual y asistida por IA — que convergen en el mismo formulario "Crear producto" y en el mismo cierre.

### Estructura del flujo

```
Home (tarjeta "Crear primer producto")
   ↓
Modal de selección ─[Crear manualmente]→ Formulario "Crear producto" (vacío) ─┐
   │                                                                          │
   └─[Crear con IA]→ Cámara (vision.ai) → Procesando (IA) → Formulario (pre-llenado) ┤
        (error: foto borrosa → tomar otra)                                          │
                                                                                      ↓
                                                          Agregar producto → Home + confeti
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Modal de selección | Popup para elegir entre crear el producto manualmente o con ayuda de IA; se cierra al tocar fuera |
| Campo de input con label | Campo de texto estándar del formulario (nombre, descripción, etc.) |
| Acción inline "Mejorar con IA" | Mejora la descripción del producto con IA; el campo se bloquea mientras procesa y confirma al terminar |
| Dropzone de subida de imágenes | Zona para subir imágenes del producto, con estados de progreso, lista de subidos y error |
| Fila de archivo subido | Muestra miniatura, nombre y peso del archivo, con opción de eliminar |
| Select de categoría | Selector de categoría del producto |
| Toggle "Variantes del producto" | Activa o desactiva si el producto tiene variantes (talla, color, etc.) |
| Cámara vision.ai | Captura de foto del producto para que la IA lo identifique y prellene el formulario |
| Animación de procesamiento IA | Indica que la IA está analizando la foto capturada |
| Confeti de celebración | Señal de éxito al cerrar el flujo, superpuesta sobre la pantalla principal |

### Reglas de interacción y validación

- Ambas variantes (manual / con IA) convergen en el mismo formulario y en el mismo cierre.
- El botón "Agregar producto" permanece deshabilitado hasta llenar todos los campos obligatorios.
- En la variante con IA, la foto capturada prellena el formulario automáticamente; el usuario revisa y puede editar antes de guardar. Por defecto solo se agrega la foto tomada, pero se pueden sumar más.
- Si la foto capturada es de baja calidad, se muestra un error y se pide tomar otra.
- Al completar el flujo, la tarjeta de setup "Crear primer producto" se anima y pasa al final de la lista en la pantalla principal (el usuario puede seguir agregando productos).
- El cierre siempre muestra confeti como única señal de éxito, sin banner de confirmación adicional.

---

## 5. Conectar canales de venta (caso Shein)

**Producto:** T1 Tienda (App móvil)
**Figma:** `171:16434` (canal Shein: `597:43220`)

### Estructura del flujo

```
Home (tarjeta "Conectar canal de ventas")
   ↓
Lista de canales — búsqueda + Marketplace / Tiendas en línea / Próximamente
   │ tap "Conectar canal" (ej. Shein)
   ↓
Detalle del canal — descripción + video + pasos de conexión + capacidades + aviso
   │ "Conectar canal"
   ↓
Modal "Importante" — aviso de importación de datos
   ↓
Autenticación web del canal (fuera de la app)
   ↓
¿La cuenta ya está vinculada a otra tienda?
   ├─ Sí → Error de autenticación
   └─ No ↓
Sincronización — activar canal + sincronizar pedidos/productos + reglas de inventario
   ↓
Canal conectado (toggle activo)
   │ "Listo, ir al inicio"
   ↓
Home + confeti
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Card de canal | Tarjeta con logo, nombre y botón para conectar (o "Me interesa" si el canal aún no está disponible) |
| Search bar de canales | Búsqueda de canal o tienda en línea dentro del listado |
| Stepper numerado vertical | Guía paso a paso de cómo conectarse a un canal externo |
| Card de capacidad | Resumen visual de lo que habilita el canal (importación de pedidos, guías, reportes, etc.) |
| Video card | Miniatura reproducible con explicación del canal |
| Modal informativo | Aviso previo a la conexión sobre el alcance de la importación de datos |
| Autenticación externa | Login y autorización que ocurren fuera de la app, en el sitio del canal |
| Fila de canal con estado + toggle | Muestra si el canal está activo/inactivo y permite encenderlo o apagarlo |
| Card de sincronización | Acción de sincronizar pedidos o productos, con estado pendiente → en progreso → hecho |
| Modal de error de autenticación | Aviso cuando la cuenta del canal ya está vinculada a otra tienda |
| Confeti de celebración | Señal de éxito al cerrar el flujo, superpuesta sobre la pantalla principal |

### Reglas de interacción y validación

- Si la cuenta del canal externo ya está vinculada a otra tienda, el flujo se detiene con un modal de error y no avanza a sincronización.
- Cada acción de sincronización (pedidos, productos, activación masiva) tiene estado independiente: pendiente → sincronizando → hecho; las reglas de inventario no tienen estado "hecho", solo cambian su label de "Establecer" a "Actualizar" una vez configuradas.
- El estado del canal (activo/inactivo) es independiente del estado de cada acción de sincronización — se controla con su propio toggle.
- Los canales listados como "Próximamente" no ofrecen conexión, solo un CTA de interés ("Me interesa").
- Al completar la conexión, la tarjeta de setup "Conectar canal de ventas" cambia su botón por un tag "Conectado" y se mueve al final de la lista en la pantalla principal.
- El cierre siempre muestra confeti como única señal de éxito, sin banner de confirmación adicional.

---

## 6. Agregar dirección de origen

**Producto:** T1 Envíos
**Figma:** `590:22183`

### Estructura del flujo

```
[Home Envíos] (tarjeta "Agregar dirección de origen")
     ↓ tap
[Formulario "Dirección de origen"] — 11 campos
     │ "Guardar" (requiere datos completos)
     │ "Descartar" → vuelve al Home
     ↓
[Home Envíos + confeti] — tarjeta de setup desaparece de la lista
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Campo input con label | Label arriba + input; incluye variante select con bandera de país (campo País) y select de colonia (con opción "Selecciona una opción") |
| Botonera Guardar / Descartar | Guardar (primario) + Descartar (secundario), en el footer del formulario |
| Home de Envíos | Variante de Home con métricas propias de envíos y lista de tarjetas de setup |

### Reglas de interacción y validación

- "Guardar" requiere que el formulario esté completo (11 campos: nombre de sucursal, país, calle, número exterior, número interior, código postal, colonia, ciudad, estado, teléfono, referencias).
- "Descartar" regresa al Home sin guardar cambios.
- Al guardar exitosamente se muestra una animación de confeti como única señal de "tarea completada" (no hay banner de éxito adicional).
- La tarjeta de setup completada desaparece de la lista y las demás tarjetas suben para ocupar su lugar; el contador general de setup avanza (ej. "2 de 5 completados").

---

## 7. Configurar tarifas de envío

**Producto:** T1 Tienda
**Figma:** `602:31005`

### Estructura del flujo

```
[Home Tienda] (tarjeta "Configurar tarifas de envío")
     ↓ tap
[Pantalla "Tarifas de envío"] — sugerencia de IA según industria
     │ "Guardar" (guarda las tarifas)
     │ "Descartar" → vuelve al Home
     ↓
[Home Tienda + confeti]
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Card de tarifa sugerida por IA | Chip "Creado con IA" + regla de envío sugerida (con bandera de país) + acción "Editar" que remite a edición fina en la versión web |
| Botonera Guardar / Descartar | Igual que en otros formularios de setup |

### Reglas de interacción y validación

- Las tarifas se sugieren automáticamente según la información de industria del negocio, vía IA.
- El usuario puede aceptar la sugerencia y guardar, o editarla — la edición fina de tarifas se hace en la versión web, no en la app.
- Al guardar se muestra confeti en el Home, pero **a diferencia de otros flujos de setup, la tarjeta de la tarea completada permanece visible** en la lista (no desaparece ni cambia de estado); el confeti es la única señal de éxito.

---

## 8. Activar T1 pagos

**Producto:** T1 Pagos
**Figma:** `602:31723`

### Estructura del flujo

```
[Home Pagos] (tarjeta "Activar T1 pagos")
     ↓ tap
[Modal "Activar T1 pagos"] — beneficios + nota de depósito + aceptar T&C
     │ "Activar" → botón muestra spinner (modal permanece abierto)
     │ "Cancelar" → cierra el modal
     ↓
[Modal de éxito "¡T1 pagos está activo!"] — ilustración + aviso de subir documentación
     │ "Cerrar"
     ↓
[Home Pagos + confeti]
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Modal de activación | Título + subtítulo + checkbox de beneficio (premarcado) + nota informativa + checkbox de Términos y Condiciones + botones Activar/Cancelar |
| Checkbox / control | Usado para el beneficio destacado y para la aceptación de T&C |
| Modal de éxito con ilustración | Ilustración temática + mensaje de confirmación + indicación de subir documentación + botón Cerrar |

### Reglas de interacción y validación

- El botón "Activar" está **siempre habilitado**, independientemente del estado de los checkboxes.
- Al tocar "Activar", el loading ocurre dentro del propio modal (spinner en el botón); no hay pantalla de carga separada.
- Tras completar la activación se informa que las ganancias se depositarán una vez validada la documentación (flujo de subir documentación queda fuera de este alcance).
- Al cerrar el modal de éxito se vuelve al Home con confeti; la tarjeta de setup permanece en su lugar (mismo comportamiento que en Flujo 7 — no desaparece).

---

## 9. Nombre de la tienda

**Producto:** T1 Tienda
**Figma:** `601:26479`

### Estructura del flujo

```
[Home Tienda] (tarjeta "Añade el nombre de tu tienda")
     ↓ tap
[Nombre de la tienda — vacío] — input + contador 0/40 + botón "Sugerir con IA"
     │ "Sugerir con IA" → genera sugerencias
     ↓
[Con sugerencias] — label "Sugerido con IA" + chips de nombres sugeridos
     │ seleccionar un chip, o escribir a mano
     ↓
[Con selección] — input lleno + chip marcado
     │ (si excede 40 caracteres → estado de error "Límite de caracteres alcanzado")
     │ "Guardar"
     │ "Descartar" → vuelve al Home
     ↓
[Home Tienda + confeti] — tarjeta desaparece
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Input con contador de caracteres | Input de texto con contador "N/40" y estado de error al superar el límite |
| Botón "Sugerir con IA" | Dispara la generación de sugerencias de nombre; visible solo en el estado inicial (vacío) |
| Chips de sugerencia seleccionables | Lista de nombres sugeridos por IA; estado seleccionado se distingue visualmente del no seleccionado |

### Reglas de interacción y validación

- El límite de caracteres es 40; al superarlo se muestra el mensaje de error "Límite de caracteres alcanzado" junto al contador.
- El usuario puede elegir un nombre sugerido por IA o escribirlo manualmente — ambos caminos llevan al mismo estado "con selección".
- Este patrón (input + sugerencias de IA) se repite en el Paso 3 del Onboarding ("¿Cómo se llama tu negocio?") y en el flujo de Crear tienda con IA — es un componente candidato a unificación.
- Al guardar, la tarjeta de setup correspondiente desaparece de la lista (mismo comportamiento que Flujo 6).

---

## 10. Dominio personalizado

**Producto:** T1 Tienda
**Figma:** `601:27991`

### Estructura del flujo

```
[Home Tienda] (tarjeta "Conectar tu dominio")
     ↓ tap
[Dominio personalizado] — "Conectar dominio existente" + input
     │
     ├─ CON plan activo: llenar input → "Guardar"
     │        ↓
     │   [Dominio conectado] → [Home Tienda + confeti] — tarjeta desaparece
     │
     └─ SIN plan activo: llenar input → acción en la card
              ↓
         [Modal de planes / paywall] — Gratis · Básico · Avanzado
              → el usuario selecciona un plan de pago para desbloquear "Dominio propio"
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Card "Conectar dominio existente" | Título + descripción + input de dominio; en el estado sin plan agrega una acción adicional que dispara el paywall |
| Paywall / modal de planes | Modal flotante (no es un drawer de borde inferior) con 3 planes desplazables; header explica que se debe elegir un plan para acceder a la función |
| Plan card | Nombre del plan + subtítulo + precio (con toggle mensual/anual en planes de pago) + cantidad de créditos de IA incluidos + lista de features + CTA "Mejorar plan" en planes de pago; el plan Gratis muestra "Plan actual" en vez de CTA |
| Toggle Anual | Control para alternar la facturación entre mensual y anual en los planes de pago |

### Decisión de qué plan/paywall se muestra

- La función "Dominio propio" está disponible desde el plan **Básico** en adelante; el plan **Gratis** no la incluye.
- Si el usuario ya tiene un plan de pago activo, el flujo permite conectar el dominio directamente y guardar.
- Si no tiene plan (o su plan no incluye la función), al intentar guardar/usar la función se despliega el paywall para que elija un plan.

| Plan | Precio | Créditos de IA |
|---|---|---|
| Gratis | Gratis (plan actual por defecto) | 50 créditos/mes |
| Básico | $399 MXN/mes (con opción anual) | 500 créditos/mes |
| Avanzado | $1,499 MXN/mes (con opción anual) | 1,000 créditos/mes |

### Reglas de interacción y validación

- El paywall no tiene CTA de footer fijo: la acción de cada plan (créditos incluidos + botón "Mejorar plan") vive dentro de su propia card.
- El plan Gratis no tiene botón de acción, solo la etiqueta "Plan actual".
- Al conectar el dominio con éxito (con plan), la tarjeta de setup desaparece del Home y se muestra confeti.
- Este mismo componente de paywall se reutiliza en otros flujos (ver Flujo 11) para features exclusivas de plan de pago.

---

## 11. Conectar redes sociales

**Producto:** T1 Tienda
**Figma:** `601:28233`

### Estructura del flujo

```
[Home] (tarjeta "Conectar redes sociales")
     ↓ tap
[Conectar redes sociales]
   · 7 inputs de red social (TikTok, Instagram, Facebook, X, YouTube, Pinterest, Threads)
   · input de WhatsApp + toggle "Mostrar burbuja de WhatsApp en tu tienda"  ← feature de pago
     │ "Guardar" (con animación de éxito)
     │ "Descartar" → vuelve al Home
     ↓
[Home + confeti] — tarjeta desaparece

  · Si el usuario no tiene plan (o su prueba gratis terminó) e intenta activar la burbuja de WhatsApp:
       → [Paywall de planes] (mismo componente del Flujo 10, con variante de header según el caso)
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Input con prefijo de red social | Campo de texto con ícono de marca como prefijo y placeholder tipo "@" o URL; se repite para cada red social soportada |
| Toggle "Mostrar burbuja de WhatsApp" | Control que activa la burbuja de WhatsApp en la tienda; es una feature de pago y dispara el paywall si no hay plan habilitante |
| Paywall de planes (reutilizado) | Mismo modal del Flujo 10, con una variante adicional de header para el caso de "prueba gratis terminada" |

### Reglas de interacción y validación

- Los 7 campos de redes sociales son opcionales e independientes entre sí.
- La burbuja de WhatsApp en la tienda solo está disponible con un plan de pago activo.
- Si el usuario no tiene plan, al intentar activar la burbuja se abre el paywall con el header "Accede a todas las funciones seleccionando un plan".
- Si el usuario tenía una prueba gratuita y esta ya terminó, el paywall muestra en su lugar el header "¡Tu prueba gratuita de la tienda en línea ha terminado! Conserva tu tienda suscribiéndote a un plan".
- Al guardar exitosamente se reproduce una animación de éxito antes de volver al Home con confeti; la tarjeta de setup desaparece de la lista.

---

## 12. Configurar políticas de la tienda

**Producto:** T1 Tienda
**Figma:** `601:30287`

### Estructura del flujo

```
[Home] (tarjeta "Configurar políticas")
     ↓ tap
[Políticas de la tienda] — 2 bloques
   │
   ├─ Bloque "Reglas de devolución"
   │     · botón "Creado con IA basado en la información de tu industria"
   │     · card Resumen (período · costo de envío · productos de venta final)
   │     · botón "Configurar" → [Reglas de devolución] (pantalla dedicada)
   │
   └─ Bloque "Personaliza tus políticas"
         · botón "Generar con IA"
              → [Aviso sobre uso de IA] (bottom sheet, aceptar/cancelar)
              → [Loading] (loader por fila de política)
              → [Políticas generadas] (chip "Activar" + ícono IA por fila)
         · lista de 4 políticas (Devoluciones · Privacidad · Términos y condiciones · Envíos)
              con chip de estado y flecha
         · tap en una política → [Modal "personalización disponible en escritorio"]
     │ "Guardar" / "Descartar"
     ↓
[Home + confeti] — tarjeta desaparece
```

### Reglas de devolución (subpantalla)

- Toggle general para habilitar solicitudes de devolución de clientes en pedidos entregados.
- Configuración del período de devolución mediante selector de días (ej. "14 días").
- Configuración de quién cubre el costo de envío de devolución mediante opciones de selección única.
- Selección de catálogos/productos excluidos de devolución vía checkboxes con buscador y lista de "catálogos seleccionados" (cada uno removible individualmente).

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Fila de política | Etiqueta de la política + chip de estado (No generada / Activar / cargando) + flecha de navegación |
| Card "Resumen" de reglas | Resumen en bullets de las reglas de devolución configuradas actualmente |
| Botones "Creado con IA…" / "Generar con IA" | Disparan la generación automática de reglas o políticas según la industria del negocio |
| Bloque de configuración de reglas de devolución | Toggle + selector de días + opciones de costo de envío + selector de catálogos con buscador |
| Modal "Aviso sobre el uso de IA" | Bottom sheet de deslinde legal antes de generar políticas con IA; requiere aceptación explícita |
| Modal "personalización solo en escritorio" | Informa que la edición avanzada de una política individual solo está disponible en la versión web |

### Reglas de interacción y validación

- Las reglas de devolución pueden generarse automáticamente con IA basándose en la industria del negocio, o configurarse manualmente vía "Configurar".
- Generar políticas con IA requiere primero aceptar el aviso legal de deslinde de responsabilidad.
- Mientras se generan las políticas, cada fila muestra un estado de carga (loader) en lugar del chip de estado.
- Cada política individual (devoluciones, privacidad, términos, envíos) puede activarse desde la app, pero su personalización/edición fina solo está disponible en la versión de escritorio — mismo patrón que la edición de tarifas de envío (Flujo 7).
- Al guardar, la tarjeta de setup "Configurar políticas" desaparece del Home y se muestra confeti.

---

## 13. Pedidos — Listado

**Producto:** T1 Tienda (multicanal)
**Figma:** `290:20528`

### Estructura del flujo

```
[Mis pedidos] (lista)
├── Estado vacío → CTA "Crear pedido"
├── Estado con pedidos → tarjetas de pedido
├── Buscador → variante de búsqueda (lista filtrada)
├── Ícono de filtro → panel de filtros (multicategoría + fecha) → "Mostrar resultados"
├── Menú "···" por pedido
│   ├── Duplicar → modal de confirmación → "Sí, duplicar"
│   └── Cancelar → modal de confirmación → "Sí, cancelar"
├── Carga diferida (skeleton / lazy load)
└── Crear pedido sin plan activo → paywall de planes (reutilizado)
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Tarjeta de pedido | Avatar + nombre del cliente + # de pedido, chip de estado, detalle (productos, monto, canal), pie con fecha y número de envíos. Acceso al menú de acciones del pedido. |
| Chip de estado / chip de canal | Mismo molde de etiqueta compacta; el de estado indica la etapa del pedido, el de canal identifica el origen (ej. Amazon) con logo. |
| Tabs con subrayado | Navegación entre "Listado de pedidos", "Carrito abandonado" y "Sucursales"; el tab activo lleva subrayado. |
| Buscador con acciones | Campo de búsqueda por ID de pedido, SKU o cliente, con botones de ordenar y opciones adicionales. |
| Panel de filtros | Selección multicategoría (incluye rango de fecha), permite varias opciones por categoría; el chip de filtro aplicado muestra categoría + conteo. |
| Modal de confirmación | Ícono + título + cuerpo + dos botones (cerrar / confirmar); patrón reutilizable para duplicar y cancelar. |
| Carga diferida | Skeleton que replica la estructura del listado mientras carga. |
| Paywall de planes | Pantalla de selección de plan que interrumpe la creación de pedido cuando no hay plan activo o se está en prueba gratuita. |

### Reglas de interacción y validación

- El estado vacío muestra un CTA primario ("Crear pedido"); el estado con contenido muestra la lista de tarjetas. Tabs y buscador permanecen visibles en ambos casos.
- El buscador filtra en tiempo real por ID de pedido, SKU o nombre del cliente.
- Los filtros permiten múltiples selecciones dentro de una misma categoría y deben confirmarse con "Mostrar resultados" antes de aplicarse a la lista.
- El menú "···" de cada tarjeta ofrece Duplicar (crea un pedido similar) y Cancelar (acción irreversible); ambas acciones requieren confirmación en modal antes de ejecutarse.
- Intentar crear un pedido sin un plan activo interrumpe el flujo y muestra el paywall de planes en su lugar.

---

## 14. Detalle de pedido — Ciclo completo

**Producto:** T1 Tienda (multicanal)
**Figma:** `290:21918`

### Estructura del flujo

```
Detalle de pedido (entrada: tarjeta del listado, §13)
│
├── CICLO PRINCIPAL (el estado define chip + bloque de productos + CTA)
│   Pendiente de pago → Por preparar → Por enviar → En camino / Por recolectar
│                                                  → Entregado → Completado
│   (ramas terminales: Cancelado · Devuelto · Reembolsado)
│
├── ESTADOS PARCIALES (el pedido se divide en grupos/envíos)
│   Parcialmente preparado · enviado · entregado · cancelado · reembolsado
│
└── SUB-FLUJOS DE ACCIÓN
    ├── Preparar productos ──► Dividir pedido (multi-paquete → origina parciales)
    ├── Generar guía ────────► Cotizar entre paqueterías → resumen → (sin cobertura)
    ├── Cancelar pedido / Cancelar envío / Cancelar artículo
    ├── Devolver productos
    ├── Reembolsar ─────────► modal de éxito / método vencido / +6 meses
    ├── Notas, etiquetas y comentarios
    └── Editar contacto y direcciones
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Header de pedido | Número de pedido, metadatos de creación (fecha, canal), chip de estado y acceso al menú de acciones del pedido. |
| Bloque de sección (encabezado repetido) | Título de bloque en mayúsculas, con línea de metadatos opcional (fecha, sucursal, responsable) y, en estados parciales, un chip de estado del grupo. |
| Fila de producto | Miniatura, nombre, cantidad, chip de variante opcional, SKU y precio. |
| Chip de estado (taxonomía) | Componente único con variantes semánticas: neutral (estados en curso), éxito (entregado/completado), destructivo (cancelados), parcial (punteado, estados parciales), bordeado (estado por grupo) e informativo (variante de producto). |
| CTA principal | Botón de acción primaria embebido dentro del bloque relevante (no en barra fija), cuyo label cambia según el estado del pedido. |
| Banner de alerta | Aviso contextual dentro del resumen de cobro (ej. pago pendiente con fecha límite). |
| Selector de cantidad | Control "0/N" usado para asignar cantidades en preparar, cancelar o devolver productos. |
| Etiquetas removibles | Input con chips de etiqueta que se pueden quitar individualmente. |
| Historial de actividad | Timeline de eventos del pedido (ícono + título + monto + hora) con campo para agregar comentarios. |
| Comparador de paqueterías | Tarjetas por transportista con servicio, tiempo estimado y precio, usado en generar guía. |
| Modal de confirmación / resultado | Mismo patrón del listado (§13): ícono + título + cuerpo + botones; se reutiliza en cancelar y reembolsar. |

### Estados del pedido

| Estado | CTA / acción habilitada |
|---|---|
| Pendiente de pago | Marcar como pagado |
| Por preparar | Preparar envío |
| Por enviar | Generar guía |
| En camino | Sin CTA, o "Marcar como entregado" según variante |
| Por recolectar | Imprimir guía de envío |
| Entregado | Sin CTA (estado de éxito) |
| Completado | Sin CTA (cierre del ciclo) |
| Parcialmente preparado | Una CTA de preparación por grupo/envío |
| Parcialmente enviado | Una CTA de envío por grupo |
| Parcialmente entregado | Una CTA de confirmación |
| Parcialmente cancelado | Sin CTA, solo visualización |
| Parcialmente reembolsado | Sin CTA, solo visualización |
| Cancelado | Estado terminal, sin CTA |
| Devuelto | Estado terminal, sin CTA |
| Reembolsado | Estado terminal, sin CTA |

### Sub-flujos de acción

- **Preparar productos:** asigna cantidad y peso a cada producto antes de enviarlo; incluye la opción de dividir el pedido en varios paquetes, lo que origina los estados parciales.
- **Generar guía:** cotiza el envío entre paqueterías (carrier, servicio, tiempo, precio) a partir de dimensiones/peso/valor declarado y genera un resumen de costo total; contempla el caso de falta de cobertura en la dirección de destino.
- **Cancelar pedido / envío / artículo:** tres variantes de cancelación (todo el pedido, solo el envío, o un artículo antes de enviarse), cada una con motivo obligatorio y resumen del monto a reembolsar.
- **Devolver productos:** selecciona productos ya entregados para devolución, requiere motivo y calcula el reembolso esperado, sin generar una nueva guía de envío.
- **Reembolsar:** define el monto a reembolsar de forma manual (limitado al disponible), permite notificar al cliente al completarse, y contempla los casos de éxito, método de pago vencido, o plazo vencido (más de 6 meses desde el pago).
- **Notas, etiquetas y comentarios:** edición inline dentro de sus bloques respectivos — estado vacío muestra un input, estado con contenido muestra un link "Editar".
- **Editar contacto y direcciones:** formulario para actualizar datos de contacto, dirección de envío y de facturación, con opción de reutilizar direcciones guardadas.

### Reglas de interacción y validación

- La estructura de la pantalla es la misma en todos los estados del ciclo; lo que cambia es el chip de estado, el contenido del bloque de productos/envío y la CTA principal.
- El bloque de productos se retitula al bloque de envío correspondiente en cuanto el pedido se prepara; las devoluciones generan su propio bloque de envío diferenciado.
- Cuando el pedido involucra más de una sucursal, se genera un bloque de productos independiente por sucursal.
- El monto de un reembolso no puede exceder el monto disponible para reembolso.
- Cancelar un pedido ya pagado dispara el reembolso automáticamente al método de pago original, salvo pagos por SPEI, que requieren reembolso manual desde el detalle del pedido.

---

## 15. Crear pedido

**Producto:** T1 Tienda
**Figma:** `312:20348`

### Estructura del flujo

```
Entrada: CTA "Crear pedido" (listado vacío o FAB)
│
Paso 1/2 — Productos
├── Catálogo (grid 2 columnas) + buscador + botón crear producto
├── Búsqueda activa → resultados filtrados
├── Selección de producto → stepper de cantidad
├── Sheet "Selecciona la variante" (talla → color, jerárquico en 2 niveles)
└── Acordeón "Productos seleccionados (N)" en barra inferior fija → [Continuar]
        ↓
Paso 2/2 — Cliente y cobro
├── Resumen: Productos · Resumen de cobro · Info del cliente · Notas · Etiquetas
├── Info del cliente = buscador de cliente
│     ├── Sheet de clientes (lista + "Nuevo cliente")
│     └── Form "Agregar nuevo cliente" (información básica + dirección)
├── Cliente seleccionado → tarjeta con contacto + dirección (editable)
└── [Crear pedido]
        ├── Modal de confirmación
        ├── Modal de estatus de pago (pagado / pendiente)
        └── Pantalla de éxito → [Ver detalle] · [Crear otro pedido]
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Header de asistente | Título centrado + indicador de paso ("1/2" · "2/2"), flecha atrás. |
| Tarjeta de producto (catálogo) | Grid de 2 columnas: imagen, nombre truncado a 1 línea, dato secundario (stock o SKU según pantalla) y precio. |
| Stepper de cantidad | Control −/valor/+ que aparece bajo la tarjeta al seleccionar un producto. |
| Acordeón de selección | Panel colapsable en la barra inferior fija que resume los productos elegidos; expandido muestra tarjeta por producto con nombre, chip de variante, precio, stepper y opción de quitar. |
| Bottom sheet de lista | Componente reutilizado para selección de variante (2 niveles: talla → color, con stock por opción) y selección de cliente (lista + opción de crear nuevo). |
| Buscador de cliente | Campo de búsqueda dentro del bloque "Info del cliente" que abre el sheet de clientes. |
| Form "Agregar nuevo cliente" | Pantalla con dos secciones colapsables: información básica (nombre, apellido, correo, teléfono + checkboxes de consentimiento de marketing) y dirección (calle, números, CP, colonia, estado, ciudad, referencia + checkboxes de dirección predeterminada/devolución). |
| Modales de confirmación | Confirmación de creación del pedido y selección de estatus de pago (radios pagado/pendiente). |
| Pantalla de éxito | Ícono de confirmación + tarjeta de resumen (ID, cliente, monto) + botones "Ver detalle" y "Crear otro pedido". |

### Reglas de interacción y validación

- El asistente tiene exactamente 2 pasos; no se puede avanzar al paso 2 sin al menos un producto seleccionado.
- Las variantes de producto son jerárquicas: primero se elige talla, luego color; el resultado se refleja como chip en el acordeón de selección.
- El paso 2/2 reutiliza la misma estructura de bloques que el detalle de pedido (Productos → Resumen de cobro → Info del cliente → Notas → Etiquetas).
- Seleccionar un cliente existente reemplaza el buscador por una tarjeta de contacto + dirección, con opción de editar cada bloque o quitar el cliente.
- Crear un cliente nuevo es un flujo embebido (form propio) que retorna al paso 2/2 con el cliente ya seleccionado.
- "Crear pedido" dispara primero un modal de confirmación y después un modal para definir el estatus de pago (pagado / pendiente) antes de generar el pedido.
- La pantalla de éxito ofrece dos salidas: ir al detalle del pedido recién creado o iniciar un nuevo pedido sin salir del flujo.

---

## 16. Carrito abandonado

**Producto:** T1 Tienda
**Figma:** `4183:109497`

### Estructura del flujo

```
Mis pedidos › pestaña "Carrito abandonado"
│
├── LISTADO
│   ├── Vacío
│   ├── Con datos: selector de rango temporal + KPIs (Pendiente · Monto)
│   │     └── Popover de desglose (% carrito vs % compra) desde el KPI "Pendiente"
│   ├── Buscador + filtro
│   ├── Chips de filtro aplicados (Tipo · Estado)
│   ├── Tarjetas: Carrito (CRT-) / Compra abandonada (CHK-)
│   └── Lazy load (skeleton)
│
└── DETALLE (por carrito/compra)
    ├── Header: ID + fecha + chip de estado + menú
    ├── Tarjetas de información: Cliente · Cantidad de productos · Monto · Estado de correo
    ├── Bloques Productos + Resumen
    ├── Toast de confirmación (ej. "Link copiado")
    └── Sheet "Detalle de recuperación" (timeline del proceso de automatización)
        ├── Variante: Carrito abandonado
        └── Variante: Compra / checkout abandonado
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Selector de rango temporal | Control tipo botón que define la ventana de tiempo de los KPIs mostrados ("30 días" por defecto). |
| Tarjeta KPI con desglose | Muestra un valor agregado (ej. carritos pendientes, monto) y abre un popover con el desglose porcentual al interactuar. |
| Popover de desglose | Overlay que detalla la composición del KPI (ej. % carrito abandonado vs % compra abandonada). |
| Tarjeta de carrito/compra | Cabecera con ID + chip de estado; filas de datos (cantidad de productos, monto, tipo); pie con fecha. No incluye menú de acciones — las acciones viven en el detalle. |
| Chip de filtro aplicado | Etiqueta con contador que representa un filtro activo (Tipo, Estado), removible individualmente. |
| Tarjetas de información del detalle | Bloques apilados con datos del cliente, cantidad de productos, monto y estado del correo de recuperación enviado. |
| Toast de confirmación | Notificación breve para acciones puntuales (ej. copiar link de recuperación). |
| Timeline de proceso | Lista vertical de pasos con ícono + label + descripción, conectados entre sí, que narra el estado de la automatización de recuperación. |

### Reglas de interacción y validación

- El listado combina dos entidades distintas bajo una misma vista, diferenciadas por prefijo de ID y por el chip "Tipo": **Carrito** abandonado (identificado por nombre del cliente) y **Compra** abandonada / checkout (identificado por email).
- El KPI "Pendiente" es interactivo: al abrirlo se despliega el popover con el desglose porcentual entre carrito y compra abandonados.
- La tarjeta de carrito/compra no tiene menú de acciones propio; todas las acciones (ej. copiar link) se ejecutan desde la pantalla de detalle.
- El sheet "Detalle de recuperación" tiene dos variantes de contenido según el tipo de abandono (carrito vs compra/checkout), cada una con su propia secuencia de pasos en el timeline.
- El CTA del sheet queda fijo al pie, fuera del área con scroll, para mantenerse visible mientras se revisa el timeline.

---

## 17. Productos — Listado

**Producto:** T1 Tienda
**Figma:** `320:23825`

### Estructura del flujo

```
Productos (entrada: ícono "Product" de la tab bar)
Tabs: Listado de productos · Inventario · Precio · Catálogo · Sucursales
│
├── Buscador (por código, nombre o SKU) + ordenar + menú overflow
│
├── LISTADO
│   ├── Vacío
│   ├── Con productos → tarjeta de producto
│   │     ├── Menú (kebab): Editar · Desactivar
│   │     └── Checkbox → activa modo de selección múltiple
│   ├── Selección múltiple → contador "N seleccionados" + menú de Acciones
│   │     └── Menú: Eliminar seleccionados
│   ├── Filtros aplicados → chips (Estado · Canal de ventas · Inventario · Categoría · Gestionado por)
│   └── Botón "+" → menú: Agregar producto · Crear con IA
│
├── Error de sincronización (con reintento)
└── Lazy load (skeleton / spinner)
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Buscador de sección | Campo de búsqueda por código/nombre/SKU + botón de ordenar + menú overflow. Mismo componente reutilizado en Pedidos. |
| Tarjeta de producto | Muestra imagen, nombre, checkbox de selección, chip de estado (activo/inactivo), menú de acciones (kebab) y filas de datos: inventario/stock, precio, canales de venta activos. Si el producto tiene variantes, el inventario indica el número de variantes y el precio se muestra como rango en vez de valor único. |
| Menú de tarjeta | Editar · Desactivar. |
| Menú de creación | Agregar producto · Crear con IA (entrada al asistente de creación asistida). |
| Barra de selección múltiple | Aparece bajo el buscador al activar el modo selección: checkbox maestro (con estado indeterminado), contador de seleccionados y botón "Acciones". |
| Menú de selección | Eliminar seleccionados. |
| Chip de filtro aplicado | Etiqueta con contador por categoría de filtro (Estado, Canal de ventas, Inventario, Categoría, Gestionado por), removible individualmente. |
| Tarjeta de error de sincronización | Comunica una falla de conexión con mensaje explicativo, CTA "Reconectar" y timestamp de la última sincronización exitosa. |
| Loaders de listado | Skeleton (estructura de tabs, buscador y tarjetas) y spinner centrado como estados de carga alternativos. |

### Reglas de interacción y validación

- El listado de productos es el punto de entrada al dominio de Productos: inventario, precio, catálogo y sucursales son secciones hermanas bajo las mismas tabs.
- La tarjeta de producto muestra la fila de "Inventario/Stock" en dos formatos según si el producto tiene o no variantes: unidades simples, o unidades + conteo de variantes con precio como rango.
- El modo de selección múltiple se activa al marcar el checkbox de cualquier tarjeta; mientras está activo, la acción disponible en bloque es "Eliminar seleccionados".
- El botón "+" abre un menú con dos rutas de creación: manual (Agregar producto) o asistida (Crear con IA, que deriva a un flujo de generación con IA fuera de esta sección).
- Los menús contextuales (kebab de tarjeta, creación, selección) siguen un mismo componente base y son el patrón de referencia para menús de acciones en el resto de la app.
- El estado de error de sincronización ofrece una acción de reintento explícita ("Reconectar") en vez de fallar silenciosamente.

---

## 18. Agregar producto

**Producto:** T1 Tienda
**Figma:** `366:16829`

### Estructura del flujo

```
Nuevo producto  (wizard de 4 sub-tabs + confirmación)
│
├── Paso 1 — Información general
│     Información básica · Identificadores · Variantes del producto (switch) ·
│     Multimedia · Especificaciones · Clasificación · Publicar en (canales)
│     │
│     switch "Producto con variantes" ─┬─ OFF ──► Paso 2 (sin variantes)
│                                      └─ ON  ──► Paso 2 CON variantes
│
├── Paso 2 — Precio e inventario  (si el producto NO tiene variantes)
│     Precio · Inventario · Envíos
│
│   Paso 2 — Precio y variante  (si el producto SÍ tiene variantes)
│     Tipos de variante (Color · Talla · Estampado · personalizada)
│     → selectores de valores → combinaciones generadas
│     → edición de inventario/precio por combinación
│
├── Paso 3 — SEO
│     [con tienda/plan]  formulario SEO + vista previa en buscador
│     [sin plan]         tarjeta de upsell "Crear tienda con IA"
│
├── Paso 4 — Canales de venta
│     Lista de canales activados en "Publicar en" (Paso 1), cada uno
│     como acordeón → mini-formulario completo propio del marketplace
│
└── Confirmación
      Retorno al listado de Productos + toast "Producto creado"
```

### Paso 1 — Información general (detalle)

Formulario largo de una sola pantalla scrolleable, organizado en bloques colapsables: **Información básica** (nombre, descripción, marca, categoría), **Identificadores** (SKU, código de barras), **Variantes del producto** (switch que determina la bifurcación del Paso 2), **Multimedia** (grid de imágenes con portada, reordenar por drag, borrar y celda "+", más un badge de recomendaciones), **Especificaciones** (chips de valores + catálogo de especificaciones disponibles + creación de opción vía sheet corto), **Clasificación** (tipo, proveedor, etiquetas y catálogo como chips) y **Publicar en** (checklist de los canales de venta donde se publicará el producto — esta selección determina qué canales aparecen en el Paso 4).

### Paso 2 — Precio e inventario / Precio y variante (detalle)

**Sin variantes:** tres bloques — **Precio** (precio base, precio de oferta, costo, más Ganancia y Margen como campos calculados no editables, y un checkbox de IVA), **Inventario** (unidades disponibles por sucursal mediante un selector de sucursales activas, stock de seguridad, y un checkbox para seguir vendiendo sin stock) y **Envíos** (dimensiones del paquete y días de envío). Varios campos incluyen tooltips explicativos.

**Con variantes** (bifurcación cuando el switch del Paso 1 está en ON): el sub-tab pasa a llamarse "Precio y variante". Muestra los tipos de variante creados (Color, Talla, Estampado u otros personalizados) como filas colapsables con sus valores; cada tipo abre un selector propio (lista de colores con swatch, lista de tallas agrupada por Adultos/Niños, o un formulario de variante personalizada con chips), todos con opción de agregar un valor nuevo al vuelo. A partir de las combinaciones de valores se genera una lista de combinaciones (ej. "Azul / Floral / S") con su inventario y precio, editable por combinación — aquí vive el único caso de validación de campo documentado del flujo (precio de oferta debe ser menor al precio base). Eliminar un tipo de variante pasa por un modal de confirmación destructiva.

### Paso 3 — SEO (detalle)

El paso más simple del asistente, con dos escenarios según si el comercio ya tiene tienda en línea/plan activo. **Con tienda:** formulario corto (meta título, descripción, URL) acompañado de una vista previa del resultado de búsqueda (favicon, nombre de tienda, URL y snippet, al estilo de un resultado de Google). **Sin plan:** el formulario se reemplaza por una tarjeta de upsell con imagen de fondo y overlay tipo "glass card" que invita a crear una tienda en línea con IA.

### Paso 4 — Canales de venta (detalle)

Lista, como acordeones, los canales de venta activados en "Publicar en" (Paso 1) — cada fila muestra el logo del canal y un estado de completitud ("Detalles no agregados" / "Detalles agregados"). Al expandir un canal, el paso repite el formulario completo de alta de producto (información básica, multimedia, categoría, precio, inventario, envíos e identificadores) adaptado a ese marketplace específico, y suma dos bloques exclusivos por canal: **Atributos** (ficha de especificaciones textiles) e **Inventario y reglas de precio** (stock de seguridad, regla de precio automática, valor y redondeo).

### Confirmación

Al completar los 4 pasos, la app no muestra una pantalla de éxito dedicada: navega de vuelta al **listado de Productos**, donde el producto recién creado ya aparece integrado en la lista, y despliega un **toast "Producto creado"** (píldora verde) flotante sobre la barra inferior.

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Input de formulario largo | Campo base (texto, select o textarea) reutilizado en todos los pasos del alta. |
| Switch | Activa/desactiva "Producto con variantes"; determina la bifurcación del Paso 2. |
| Uploader multimedia | Grid de imágenes con portada, reordenar (drag), borrar y celda de agregar. |
| Selector de especificaciones | Chips de valores elegidos + catálogo de especificaciones disponibles + creación de opción al vuelo desde el buscador. |
| Sheet corto de creación | Bottom sheet con nombre + campo(s) extra (color, valor base) para crear una opción/color/especificación nueva sin salir del flujo. |
| Checklist de canales | Lista de marketplaces con checkbox, usada en "Publicar en" del Paso 1. |
| Badge informativo | Ícono + texto de ayuda que abre una pantalla de recomendaciones (ej. multimedia). |
| Campo calculado | Botón no editable que muestra un valor derivado (Ganancia, Margen). |
| Tooltip | Ícono de información junto a un campo que abre una explicación contextual. |
| Sheet de checklist | Bottom sheet para seleccionar sucursales activas del inventario. |
| Grid de dimensiones | Layout de 2 columnas para largo/ancho/alto/peso del paquete. |
| Selector de valores de variante | Lista de opciones con checkbox y swatch (colores) o agrupada por categoría (tallas), con opción de agregar valor personalizado. |
| Fila de tipo de variante | Fila colapsable con label + valores + chevron, dentro de la sección de variantes. |
| Fila de combinación | Muestra una combinación de variante con su inventario y precio; al tocarla abre la edición de esa combinación. |
| Chips de filtro | Filtran la lista de combinaciones por tipo/valor de variante, removibles con "x". |
| Input en estado de error | Borde y mensaje de validación bajo el campo (único caso documentado: precio de oferta vs. precio base). |
| Modal de confirmación destructiva | Ícono en círculo + título + cuerpo + acciones Cancelar/Eliminar, para eliminar una variante. |
| Vista previa de resultado de búsqueda (SERP) | Simula cómo se vería el producto en un buscador: favicon, tienda, URL, título y snippet. |
| Tarjeta de upsell con IA | Imagen de fondo + overlay tipo "glass card" con CTA para crear tienda con IA. |
| Barra de progreso "Paso n/3" | Indicador de avance, presente solo en el escenario sin plan del Paso 3. |
| Fila de canal/marketplace | Acordeón con logo, nombre y estado de completitud, usada en el Paso 4. |
| Toast de confirmación | Píldora flotante sobre la barra inferior que confirma la creación del producto. |

### Reglas de interacción y validación

- El switch "Producto con variantes" del Paso 1 es lo único que determina si el Paso 2 es el formulario simple de Precio e inventario o el sub-flujo de Precio y variante.
- Los campos Ganancia y Margen son siempre calculados a partir de precio y costo — nunca editables directamente.
- Los selectores de valores de variante (color, talla, especificación) permiten crear una opción nueva al vuelo desde el propio buscador, sin salir a otra pantalla.
- Toda confirmación destructiva (eliminar una variante) pasa por un modal — nunca es inline ni inmediata.
- La validación de campo (borde + mensaje de error) solo está documentada en la edición de precio por combinación de variante (precio de oferta menor al precio base); el resto del alta no marca campos requeridos ni valida en tiempo real.
- El Paso 3 cambia de contenido según el plan del comercio: formulario SEO si ya tiene tienda, tarjeta de upsell con IA si no tiene plan activo.
- El Paso 4 repite, por cada canal de venta activado en "Publicar en" del Paso 1, un formulario propio del marketplace con sus campos y reglas específicas (incluye atributos adicionales y reglas de precio automáticas que no existen en el alta general).
- El cierre del asistente es por retorno + toast (no hay pantalla de éxito dedicada), a diferencia de otros flujos de creación de la App que sí usan una pantalla de confirmación de página completa.

---

## 19. Agregar producto con IA

**Producto:** T1 Tienda
**Figma:** `4269:108999`

### Estructura del flujo

```
Menú "Crear con IA" (listado de productos)
    ↓
[1] Cámara
    Captura foto del producto (flash on/off · disparo · cerrar)
    ↓
[2] Foto capturada
    "Crear producto" | "Tomar otra foto"
    ↓
[3] Procesamiento IA
    Loader con fases rotativas ("Capturando imagen" → "Costos y precios...")
    └── Excepción: imagen borrosa/no reconocida → vuelve a Cámara
    ↓
[4] Formulario prellenado por IA
    Nombre · Descripción (+ "Mejorar con IA") · Imágenes · Categoría
    Variantes (switch) · Inventario y precio · Identificadores
    [Agregar producto]  [Cancelar]
    ↓
[5] Producto creado → listado + toast "Producto creado"
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Vista de cámara | Captura fullscreen con flash on/off, botón de disparo y thumbnail de la última foto tomada |
| Estado de procesamiento IA | Loader con texto que cicla por distintas fases mientras la IA analiza la imagen |
| Formulario prellenado | Mismo formulario del alta manual, con todos los campos completados por la IA para revisión del usuario |
| Uploader con progreso | Barra de progreso + miniaturas de archivos subidos, con opción de cancelar la carga |
| Fila de archivo subido | Miniatura + nombre + peso + acción de borrar |
| Acción "Mejorar con IA" | Botón inline en el campo de descripción que reescribe el texto con IA (reutilizable también en el alta manual) |
| Asistente IA flotante | Acceso flotante dentro del formulario para invocar ayuda de IA mientras se revisan los datos |
| Banner de revisión | Aviso informativo pidiendo al usuario validar que los datos generados por IA sean correctos |

### Reglas de interacción y validación

- El usuario accede desde el menú "Crear con IA" del listado de productos.
- Al capturar la foto, el usuario puede confirmar ("Crear producto") o repetir la toma ("Tomar otra foto").
- Al confirmar, la IA procesa la imagen y extrae automáticamente los detalles del producto (nombre, descripción, categoría, inventario, precio, identificadores).
- Si la imagen no es válida (borrosa u otro error), la IA solicita repetir la foto y regresa a la cámara.
- El formulario resultante es completamente editable: el usuario debe revisar y puede corregir cualquier campo antes de guardar.
- Por defecto se agrega solo la foto tomada en cámara; desde el formulario el usuario puede subir imágenes adicionales.
- El switch "Variantes del producto" habilita la gestión de variantes (tallas, colores, etc.), igual que en el alta manual.
- La acción "Mejorar con IA" en la descripción es opcional y puede invocarse en cualquier momento antes de guardar.
- Al guardar, el flujo confluye con el alta estándar: listado + toast de confirmación.

---

## 20. Inventario

**Producto:** T1 Tienda
**Figma:** `369:29099`

### Estructura del flujo

```
Productos › tab "Inventario"
├── Vacío
│   ilustración + "Aún no tienes inventario" + botón
├── Listado
│   tarjetas de inventario (Disponible / Reservado / No vendible / Total)
├── Con filtros aplicados
│   chips: Inventario · Canal de ventas · Categoría · Otros filtros
├── Selección múltiple
│   barra superior (checkbox + "N seleccionados" + botón "Acciones")
│   menú: Modificar inventario disponible
├── Menú Exportar / Importar
└── Modales (centrados)
    ├── "Modificar inventario de {X} productos" — Agregar inventario | Establecer cantidad
    └── "Inventario no vendible" — Dañado · Defectuoso · Stock de seguridad · Otro
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Tarjeta de inventario | Desglosa el stock de un producto en Disponible para venta / Reservado / No vendible / Inventario total |
| Checkbox de 3 estados | On / Off / Multiselection (indeterminado), usado en la barra de selección múltiple |
| Modal de modificación masiva | Ajusta el inventario de varios productos seleccionados a la vez, con dos modos de cálculo |
| Popover de desglose "No vendible" | Divide el inventario no vendible en sus causas, cada una editable por separado |
| Barra de acciones (selección) | Aparece al entrar en modo selección; agrupa acciones masivas sobre los productos marcados |
| Chip de filtro con contador | Indica cuántos valores están activos por categoría de filtro |
| Menú Exportar / Importar | Acción global de import/export de inventario desde el header |

### Reglas de interacción y validación

- Semántica del desglose: Disponible para venta + Reservado + No vendible = Inventario total. Disponible y No vendible son valores editables (capturables); Reservado y Total son derivados, de solo lectura.
- El modal de modificación masiva ofrece dos modos: "Agregar inventario" (suma al stock actual) y "Establecer cantidad" (fija el stock a un valor); el texto de ayuda cambia según el modo elegido.
- El botón de confirmar el modal permanece deshabilitado hasta que se ingresa una cantidad.
- El popover "Inventario no vendible" desglosa esa cifra en causas (Dañado, Defectuoso, Stock de seguridad, Otro), editables individualmente.
- El modo de selección múltiple habilita la acción de modificación masiva de inventario sobre los productos marcados.

---

## 21. Precios

**Producto:** T1 Tienda
**Figma:** `375:16216`

### Estructura del flujo

```
Productos › tab "Precio"
├── Vacío
├── Listado
│   tarjetas de producto (checkbox + thumbnail + nombre + "N variantes" + "Ver precios")
├── Con filtros aplicados
│   chips: Canal de ventas · Categoría · Otros filtros
├── Selección múltiple
│   menú: Modificar precio · Eliminar seleccionados
├── Modal "Modificar precio para X productos"
│   Aumentar precio / Reducir precio  ×  Porcentaje / Monto
│   Monto → Rango | Cifra
│   "Aplicar a" → selector multi-canal
├── Toast "Precios modificados"
└── Editor de precios por canal
    por canal (T1tienda, marketplaces): Precio base · Precio de oferta
    "Ver variantes" → acordeón con precio por variante
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Modal "Modificar precio" | Ajusta el precio de varios productos combinando dirección (Aumentar/Reducir) y tipo de cálculo (Porcentaje/Monto) |
| Sub-selector "Monto" | Cuando el tipo es Monto, permite definirlo como Rango o Cifra fija |
| Selector "Aplicar a" | Selección múltiple de canales de venta a los que se aplica el ajuste, con conteo de canales marcados |
| Editor de precios por canal | Pantalla dedicada para definir precio base y precio de oferta por cada canal de venta conectado |
| Acordeón de variantes por canal | Expande el bloque de un canal para fijar precio base/oferta por cada variante del producto |
| Drawer de filtros | Componente compartido (Ordenar por, Canales, Categoría, Precio en Rango/Cifra) |
| Toast de confirmación | Notifica que los precios se modificaron tras aplicar un cambio masivo |

### Reglas de interacción y validación

- El ajuste de precio masivo combina dos ejes: dirección (Aumentar/Reducir) y tipo de cálculo (Porcentaje/Monto); Monto admite a su vez Rango o Cifra fija.
- "Aplicar a" es una selección múltiple de canales, no un simple todos/ninguno — el campo refleja el conteo de canales marcados.
- El editor de precios por canal permite definir precio base y precio de oferta de forma independiente por canal de venta y, dentro de cada canal, por variante del producto.
- Al confirmar un cambio masivo, el resultado se refleja en el editor de precios antes de darlo por aplicado.
- "Eliminar seleccionados" en el menú de selección múltiple es una acción destructiva.

---

## 22. Catálogo

**Producto:** T1 Tienda
**Figma:** `404:28696`

### Estructura del flujo

```
Productos › tab "Catálogo"
├── Listado
│   tarjetas de catálogo (Tipo: Manual/Avanzado · Nº productos · Canales activos/total)
│   selección múltiple → Eliminar seleccionados
│   menú por catálogo: Editar · Administrar canales de venta · Eliminar
│
├── Nuevo / Editar catálogo (mismo formulario)
│   Información del catálogo (imagen · nombre · descripción)
│   Selección de productos → modo Manual | Avanzado
│       Manual:   buscar y seleccionar productos uno a uno
│       Avanzado: constructor de reglas → productos se agregan automáticamente
│
├── Administrar canales de venta (canales del catálogo + variantes)
└── Menú Ordenar (por más vendidos, nombre, precio, fecha, manual)
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Tarjeta de catálogo | Resume tipo de armado (Manual/Avanzado), número de productos y cobertura de canales |
| Selector de modo | Radios (no segmented) para elegir entre armar el catálogo Manual o Avanzado, cada uno con su descripción |
| Buscador de productos (modo Manual) | Búsqueda + selección individual o "Seleccionar todo" para agregar productos al catálogo |
| Constructor de reglas (modo Avanzado) | Cada regla = campo + operador + valor; una lista de reglas combinadas por lógica "Todas" (AND) o "Cualquiera" (OR), cada regla borrable, con botón para agregar más |
| Preview de productos que cumplen | Vista en vivo de los productos que satisfacen las reglas definidas, con su estado (Activo/Inactivo) |
| Menú Ordenar | Conjunto de criterios de orden reutilizable en los listados del módulo |
| Modal destructivo con copy aclaratorio | Al eliminar un catálogo, aclara que los productos siguen publicados en sus canales |

### Reglas de interacción y validación

- Un catálogo se arma en uno de dos modos, elegidos con radios: **Manual** (el usuario busca y selecciona productos) o **Avanzado** (el usuario define reglas y los productos que las cumplen se agregan automáticamente).
- El constructor de reglas combina una lógica global (AND/OR) con una lista de reglas individuales de la forma campo → operador → valor; cada regla se puede eliminar de forma independiente.
- En modo Avanzado, el sistema muestra en vivo los productos que cumplen las reglas configuradas, indicando si están Activos o Inactivos.
- Eliminar un catálogo solo remueve la agrupación: los productos permanecen publicados en los canales donde ya estaban activos.
- "Administrar canales de venta" define a qué canales se publica el catálogo, incluyendo sus variantes.

---

## 23. Sucursales

**Producto:** T1 Tienda
**Figma:** `421:21749`

### Estructura del flujo

```
Productos › tab "Sucursales"
├── Listado
│   Sucursal principal (card destacada + badge "Principal" + acción "Cambiar")
│   Todas las sucursales (buscador + cards con chips: Activo · Plan POS)
│   filtros: Ordenar por · Estado · Plan POS
│   banner de límite de plan alcanzado
│
├── Nueva sucursal (formulario: dirección MX completa + encargado)
│
├── Detalle de sucursal
│   métricas (Ventas totales · SKUs · Valor de inventario) + selector de periodo
│   Datos de la tienda (chips + dirección + teléfono + encargado)
│   Preparación de pedidos (envío a domicilio)
│   estado inactivo → banner + botón "Activar"
│
├── Modales de estado
│   Eliminar sucursal
│   Desactivar (sin inventario → directo | con inventario → elegir sucursal destino y transferir)
│   Cambiar sucursal principal
│
└── Envíos a domicilio (qué sucursales participan en entrega a domicilio)
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Card de sucursal | Nombre, badge de sucursal Principal, dirección y chips de estado/plan |
| Formulario de dirección MX | País, calle, números exterior/interior, CP, colonia, estado, ciudad, referencia, teléfono, más datos del encargado |
| Ficha de detalle de sucursal | Métricas de negocio, datos de la tienda y preparación de pedidos en secciones colapsables |
| Selector de periodo | Filtra el rango temporal de las métricas mostradas en el detalle |
| Banner de sucursal inactiva | Indica la fecha de desactivación y ofrece reactivar la sucursal |
| Banner de límite de plan | Aparece al alcanzar el número máximo de sucursales activas del plan, con CTA para mejorarlo |
| Modales de confirmación de estado | Confirman eliminar, desactivar o cambiar la sucursal principal; layout de botones lado a lado para confirmaciones simples y apilado cuando hay una selección adicional que hacer |
| Selector de sucursal destino | Elige a qué sucursal transferir inventario y pedidos pendientes al desactivar una sucursal con stock |

### Reglas de interacción y validación

- Solo puede existir una sucursal principal a la vez; cambiarla requiere confirmación explícita.
- Desactivar una sucursal sin inventario es una confirmación simple. Si la sucursal tiene inventario o pedidos sin preparar asignados, el sistema obliga a elegir otra sucursal destino para transferirlos antes de completar la desactivación; el botón de confirmar permanece deshabilitado hasta seleccionar el destino.
- Eliminar una sucursal es una acción irreversible y requiere confirmación explícita.
- El número de sucursales activas está limitado por el plan contratado; al llegar al límite se bloquea la activación de nuevas sucursales y se muestra un CTA para mejorar el plan.
- El detalle de una sucursal cambia según su estado: si está inactiva, muestra la fecha de desactivación y un botón para reactivarla.
- "Envíos a domicilio" configura, por sucursal, si participa en la preparación de pedidos con entrega a domicilio.

---

## 24. Envíos

**Producto:** T1 Envíos
**Figma:** `Section 2 (listado y rastreo) · Create Shipment · Quote · Tracking Guides · Pick-up`

### Estructura general del módulo

```
Envíos (header)
│
├── Tabs: Cotizar · Mis envíos · Guías de rastreo · Recolecciones
│
├── Mis envíos          → ver "Listado"
├── Cotizar              → ver "Cotizar"
├── Guías de rastreo     → ver "Tracking de guías"
└── Recolecciones        → ver "Recolecciones"

Desde el listado → "Crear envío" (wizard)
Desde una tarjeta de envío → "Rastrear envío" (timeline resumido del pedido→envío)
```

### Listado (Mis envíos)

```
[Listado]
├── Vacío: "Aún no tienes envíos" → CTA "Crear envío"
├── Con envíos: buscador + tarjetas de envío
├── Filtros (drawer): Ordenar · Paquetería · Estado · Fecha · Origen
├── Menú "Crear": Crear envío · Crear guías masivas · Exportar
└── Menú por envío: Rastrear envío · Descargar guía · Reportar incidencia · Imprimir guía · Cancelar guía
     ↓ (Rastrear envío)
[Rastreo del envío]
    Header transportista + guía + fecha de llegada
    Origen / Destino
    Timeline: pedido creado → confirmado → preparado → guía generada → en camino → entregado
    Footer: Descargar guía · Ver detalles del envío
```

**Patrones y componentes**

| Componente | Descripción |
|---|---|
| Tarjeta de envío | Transportista + guía + precio + canal de venta + fecha + cliente + chip de estado |
| Chip de estado de envío | Refleja el ciclo de vida del envío con colores del sistema de chips (neutro/amarillo/verde) |
| Drawer de filtros | Patrón transversal de la app: acordeones con contador, footer "Mostrar resultados" |
| Menú "Crear" | Envío individual / guías masivas / exportar listado |
| Menú de acciones de envío | Rastrear, descargar guía, reportar incidencia, imprimir, cancelar |
| Timeline de rastreo | Eventos con ícono de estado, chips de fecha, y links a comprobante/guía/rastreo del carrier |

**Reglas de interacción y validación**

- Ciclo de vida del envío: Por recolectar → Recolectado → En camino → Entregado (+ Excepción de entrega como estado de excepción).
- Paqueterías soportadas: FedEx, DHL, Grupo ampm, 99 Minutos, Amazon, UPS.
- El timeline de rastreo conecta todo el recorrido pedido→envío (creado, confirmado, preparado, guía generada, en camino, entregado), enlazando al comprobante de pago, a la guía descargable y al rastreo del transportista.
- Los filtros activos persisten durante la sesión; siempre debe existir salida a "limpiar/restablecer".

### Crear envío (wizard)

```
[Sin dirección de origen] (solo la primera vez)
    Empty state → obliga a agregar una dirección de origen
         ↓
[Agregar dirección] (si no existe origen guardado)
    Formulario de dirección MX: contacto + dirección + toggles (predeterminada / devolución)
         ↓
[Paso 1/3] Direcciones
    Origen: dirección guardada (selector + "Cambiar") o la recién creada
    Destino: buscar cliente guardado (libreta) o capturar uno nuevo
    ☑ Guardar cliente en T1 para futuros envíos
         ↓
[Paso 2/3] Detalles del paquete
    Dimensiones (plantilla): largo · ancho · alto · peso → peso volumétrico calculado
    Sistema de plantillas: usar existente / crear nueva / guardar cambios
    Número de paquetes · Descripción del contenido
    Tipo de producto (SAT) — clasificado automáticamente por un asistente de IA, editable
    ☑ Incluir seguro de envío → Valor del contenido
         ↓
[Paso 3/3] Seleccionar paquetería
    Lista de opciones con tarifa y tiempo de entrega (o error si falla la cotización)
         ↓
[Resumen del envío]
    Secciones editables: Direcciones · Dimensiones del paquete · Paquetería · Total
    CTA "Crear envío"
         ↓
[Éxito]
    Card de guía (transportista + tracking + fecha de llegada) + Origen/Destino
    "Cómo preparar tu envío" (instrucciones)
    Sucursales cercanas (mapa + lista) · Programar recolección (modal)
```

**Patrones y componentes**

| Componente | Descripción |
|---|---|
| Wizard de 3 pasos | Indicador "PASO N/3", navegación lineal con botón atrás/siguiente |
| Card de dirección con "Cambiar" | Muestra la dirección activa; abre selector de direcciones guardadas |
| Libreta de clientes | Selector de destino: clientes frecuentes + todos (A-Z), buscador; un cliente puede tener varias direcciones guardadas |
| Editor de dimensiones + plantillas | Grilla largo/ancho/alto/peso; plantillas reutilizables (buscar, crear, actualizar) |
| Campo "Tipo de producto - SAT" | Clasificación fiscal automática por IA (con estado de carga), editable manualmente |
| Selector de paquetería con tarifas | Lista de opciones con precio y tiempo estimado |
| Resumen editable | Secciones colapsables con botón "Editar" por sección |
| Pantalla de éxito | Resumen de guía + próximos pasos físicos (empacar, sucursal, recolección) |
| Modal de sucursales cercanas | Mapa con distancia y horario de los puntos del carrier |
| Modal "Programar recolección" | Advertencia previa antes de saltar al módulo de recolección |
| Alerta de contenido restringido | Mensaje de advertencia no bloqueante bajo la descripción del contenido |

**Reglas de interacción y validación**

- Si no hay dirección de origen guardada, se fuerza a crearla antes de iniciar el Paso 1.
- Cuando ya existen clientes guardados, el destino se elige de la libreta en vez de capturarse manualmente.
- El asistente de IA propone la clave SAT a partir de la descripción del contenido; el usuario puede sobreescribirla.
- Peso volumétrico se calcula de las dimensiones; el sistema compara peso físico vs. volumétrico (ver "Cotizar" para el criterio de cobro).
- El campo "Valor del contenido" solo aplica cuando el seguro está activo.
- Validaciones de formato en los inputs de contacto/dirección (teléfono, código postal, límite de caracteres en referencias).
- El CTA final de cada paso permanece deshabilitado hasta que la sección es válida/completa.
- La pantalla de éxito no es solo confirmación: orienta explícitamente los pasos físicos siguientes.

### Cotizar

```
[Formulario del cotizador]
    CP origen · CP destino (validación de cobertura en tiempo real)
    Dimensiones: largo · ancho · alto · peso
    ☑ Incluir seguro de envío → Valor del contenido
    Resumen: peso físico · peso volumétrico · peso a cotizar
    Botones: Borrar datos · Cotizar (deshabilitado hasta formulario válido)
         ↓
[Seleccionar paquetería] (resultados)
    Filtros: Paquete · Tipo de servicio · Ventaja
    Tarjetas de opción: carrier + servicio + chip "Recomendado" (opcional) + precio + fecha estimada
    Popup de desglose: precio de guía + seguro + zona extendida → total
    Footer: Ver más opciones · Crear envío (deshabilitado hasta seleccionar una opción)
```

**Patrones y componentes**

| Componente | Descripción |
|---|---|
| Formulario de cotizador | CP origen/destino + dimensiones + seguro condicional |
| Indicador de validación de CP | Progresión vacío → validando → válido → inválido |
| Resumen de pesos | Peso físico, volumétrico y "a cotizar", con tooltips explicativos |
| Tarjeta de opción de paquetería | Radio de selección + carrier + tipo de servicio + precio + fecha |
| Chip "Recomendado" | Marca la opción sugerida (mejor balance precio/tiempo) |
| Popup de desglose de costo | Precio de guía + seguro + zona extendida = total |
| Filtro de paqueterías | Checkboxes con logo para acotar carriers en los resultados |

**Reglas de interacción y validación**

- Cotizar es anónimo y ligero: no requiere cliente ni dirección completa, solo CP + dimensiones — es la puerta de entrada previa a Crear envío.
- El CP se valida contra la cobertura de paqueterías en tiempo real.
- Peso a cotizar = el mayor entre peso físico y peso volumétrico (criterio de tarifación de las paqueterías).
- "Valor del contenido" solo aparece cuando el seguro está activo, y es obligatorio llenarlo para poder cotizar.
- El botón "Cotizar" permanece deshabilitado hasta que el formulario es válido.
- Desde los resultados se puede continuar directo hacia crear el envío con la paquetería elegida.

### Tracking de guías

```
[Listado de guías]
    Buscador + botón de filtro (drawer: Paqueterías · Estado · Fecha · Cliente)
    Tarjetas de guía: carrier + tracking + chip de estado + fecha + cliente (colapsable)
         ↓ tap en tarjeta
[Detalle de guía] (pantalla completa)
    Encabezado: carrier + tracking + tipo de servicio + chip de estado
    Info de guía: No. de pedido · Paquete · Fecha estimada de entrega · Última actualización
    Info de dirección: Origen · Destino
    Historial de actividad: timeline agrupado por día (Hoy/Ayer), eventos expandibles
        último evento expandido → detalles de guía + "Ver/Imprimir guía"
```

**Patrones y componentes**

| Componente | Descripción |
|---|---|
| Tarjeta de guía | Mismo patrón que la tarjeta de envío, orientada a rastreo |
| Drawer de filtros | Paqueterías, estado, fecha, cliente (buscador + checkboxes) |
| Bloques de info | Secciones con banda de título (info de guía / info de dirección) |
| Timeline de historial de actividad | Agrupado por día, eventos con ubicación, expandibles individualmente |

**Reglas de interacción y validación**

- Reutiliza el mismo sistema de chip de estado que el listado general de envíos.
- El historial de actividad es la vista granular del recorrido físico (recolección → hubs → sucursales → entrega), complementaria al timeline resumido del pedido (ver "Listado").
- Cada evento es expandible por separado; el evento raíz enlaza a la guía descargable/imprimible.

### Recolecciones

```
[Listado de recolecciones]
    Buscador + filtro + menú de acciones
    Tarjetas: carrier + tracking + fecha programada (ventana horaria) + paquetes + dirección
    ├── Vacío (sin recolecciones): CTA "Crear recolección"
    └── Vacío (sin envíos): bloqueado — requiere tener envíos creados primero
         ↓
[Crear recolección] — wizard tipo acordeón (4 secciones, no numeradas)
    1. Dirección de recolección — seleccionar guardada (marca de favorita) o agregar nueva
    2. Elige la paquetería — lista con horario de atención por carrier
       (sin cobertura → advertencia + redirige a la sucursal más cercana)
    3. Programar la recolección — fecha (próximos días hábiles + calendario) → horario (ventana de 3h)
    4. Detalles del paquete — número de paquetes + dimensiones/peso promedio del lote
    → CTA "Crear recolección" (deshabilitado hasta completar las 4 secciones)
         ↓
[Éxito]
    Resumen: carrier + guía + paquetes · fecha/hora · lugar de recolección
    CTA "Ir a recolecciones"
    Instrucciones de preparación + política de presencia obligatoria

[Cancelar recolección] (desde el menú de la tarjeta)
    Modal destructivo — cancelación permanente e irreversible
```

**Patrones y componentes**

| Componente | Descripción |
|---|---|
| Tarjeta de recolección | Carrier + tracking + fecha/ventana horaria + número de paquetes + dirección |
| Wizard acordeón | Secciones con estado pendiente (atenuada) → activa → completada (colapsa a resumen) |
| Selector de dirección con favorita | Dropdown con marca de dirección predeterminada + buscador + lista de sucursales/almacenes |
| Selector de paquetería con horario | Dropdown que muestra el horario de atención de cada carrier junto a la opción |
| Selector de fecha + ventana horaria | Fecha con atajos de días hábiles + calendario completo; horario dependiente de la fecha elegida |
| Grilla de dimensiones/peso promedio | Mismos campos que Crear envío, aplicados como promedio del lote |
| Modal destructivo de cancelación | Confirmación irreversible, patrón transversal de la app |

**Reglas de interacción y validación**

- Una recolección depende de tener envíos ya creados — no se puede programar sin envíos previos.
- El wizard usa un patrón de acordeón (no un stepper numerado): cada sección progresa de atenuada → activa → completada, y solo la sección activa muestra sus campos.
- El selector de horario permanece deshabilitado hasta elegir la fecha.
- Las fechas rápidas excluyen fines de semana; hay opción de calendario completo para cualquier fecha.
- Si la ubicación no tiene cobertura de recolección, se bloquea la creación y se sugiere llevar el paquete a la sucursal más cercana.
- Los campos de dimensiones son obligatorios; si faltan, el input pasa a estado de error.
- La cancelación es permanente; el mensaje de éxito advierte que la ausencia en la cita genera un reporte que puede limitar futuras recolecciones.

---

## 25. Configuración de envíos — Reglas de prioridad

**Producto:** T1 Envíos
**Figma:** `Configuracion prioridad`

### Estructura del flujo

```
Envíos (header con ícono de configuración)
│
└── Configuración de envíos (menú)
    ├── Plantillas
    ├── Direcciones de origen
    └── Reglas de prioridad
        ├── Card de regla activa + "Cambiar"
        ├── Lista de paqueterías (combinación carrier + servicio, con chip de estado)
        │
        ├── Modal "Regla de prioridad" — 4 opciones:
        │   Prioridad T1 · Por prioridad · Más económico · Más rápido
        │
        └── Según el modo elegido:
            ├── Prioridad T1 / Por prioridad → card + lista de paqueterías
            │     (Por prioridad: lista reordenable por arrastre)
            └── Más económico / Más rápido → solo card (el sistema decide, sin lista)
```

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Menú de configuración de envíos | Acceso a Plantillas, Direcciones de origen y Reglas de prioridad |
| Card de regla activa | Ícono + nombre + descripción de la regla vigente + botón "Cambiar" |
| Fila paquetería + servicio | Cada combinación carrier/tipo de servicio con su propio chip de estado (activa/inactiva) |
| Modal de selección de regla | Presenta las 4 estrategias con ícono y descripción funcional |
| Lista reordenable (drag-and-drop) | Solo visible en el modo "Por prioridad"; define el orden de intento por paquetería |

### Reglas de interacción y validación

- Cuatro estrategias de selección automática de paquetería: **Prioridad T1** (el sistema decide), **Por prioridad** (el usuario ordena manualmente), **Más económico** (tarifa más baja) y **Más rápido** (menor tiempo de entrega).
- Solo los modos "Prioridad T1" y "Por prioridad" muestran la lista de combinaciones paquetería+servicio; en "Por prioridad" esa lista es reordenable por arrastre y ese orden define la prioridad de intento.
- "Más económico" y "Más rápido" no muestran lista — el criterio se aplica automáticamente sobre todas las opciones disponibles.
- Cada fila de la lista representa una combinación paquetería + tipo de servicio (no solo el carrier); su chip refleja si esa combinación está activa para participar en la selección automática.

---

## 26. Control de calidad — Incidencias

**Producto:** T1 Envíos
**Figma:** `947:60630`

### Estructura del módulo

```
Más › OTROS › Control de calidad
│
├── Tabs: [Gestión de incidencias] · [Sobrepesos]
│
├── LISTADO (KPIs + buscador + filtros + tarjetas INC-XXXXX)
│   └── menú "···" de la tarjeta ─┐
│                                  │
└── DETALLE de incidencia          │
    └── menú "···" del header ─────┤
                                    ▼
                        MENÚ DE ACCIONES (kebab, motivo-dependiente)
                        📍 Cambiar dirección
                        🏪 Recolección en sucursal / Enviar a sucursal
                        ↻  Devolver al remitente
                        (+ Reagendar entrega · Solicitar búsqueda ·
                           Intentar nueva entrega · Agregar detalles de acceso)
                                    │
                    cada ítem abre su propio mini-flujo (1 pantalla a 1 wizard)
                                    │
                                    ▼
                DETALLE — ESTADO FINAL (chip de motivo → chip de acción aplicada)

Entrada independiente — alta de incidencia:
Listado (vacío o con datos) › "Reportar incidencia" › Paso 1/2 › Paso 2/2 (ver Flujo 27)
```

No hay pantalla de éxito dedicada en los flujos de resolución: el cierre es el **retorno al detalle de incidencia con el chip de motivo reemplazado por un chip de acción aplicada** (p. ej. "Enviar a sucursal", morado).

### Catálogo de acciones por motivo

| Motivo de incidencia | Acción disponible | Patrón de UI |
|---|---|---|
| Dirección incompleta o incorrecta | Cambiar dirección | Pantalla completa: formulario → modal de confirmación |
| Destinatario no localizado / Acceso restringido | Enviar a sucursal | Pantalla completa (mapa + radio-cards) + popup de error si no hay sucursales |
| Ruta de escape desde otras acciones no viables | Devolver al origen | Bottom sheet → modal de confirmación |
| Destinatario no localizado | Reagendar entrega | Bottom sheet → date picker → modal de confirmación |
| — | Recolección en sucursal | Pantalla completa (mapa + radio-cards) + popup de error; incluye el menú de acciones y el detalle en estado final |
| Paquete sin movimiento / extravío | Solicitar búsqueda | Pantalla completa, formulario largo (6 campos) → modal de confirmación |
| — | Intentar nueva entrega | Modal único (sin pantalla previa) |
| Acceso restringido | Agregar detalles de acceso | Bottom sheet, sin modal de confirmación |
| Alta de incidencia (cualquier motivo) | Reportar incidencia — Paso 1/2 | Wizard pantalla completa con indicador de progreso |

### Cambiar dirección (detalle)

Formulario de pantalla completa: card "Dirección actual" (read-only, con botón "Replicar" que autocompleta) + formulario "Nueva dirección" de 8 campos (Calle, No. ext/int, CP, Colonia [select], Estado, Ciudad, Referencias). CTA "Cambiar" se habilita solo con todos los campos requeridos completos; valida inline con mensajes "Este campo es obligatorio" / "Selecciona una opción". Cierra con modal de confirmación con dato citado (dirección + botón copiar). Es el punto de derivación de "Cambiar" desde las cards de dirección de otros flujos (Reagendar entrega, Intentar nueva entrega).

### Enviar a sucursal (detalle)

Pantalla completa con header dinámico por paquetería (copy + logo inline), mapa embebido con controles flotantes glassmorphism (Abrir en Mapas, GPS, zoom), copy explicativo y lista de radio-cards de sucursal (nombre, dirección, distancia, horario) con preselección por defecto. CTA "Confirmar" → modal de confirmación con dato citado. Si no hay sucursales para el CP, abre un popup "callejón sin salida" con input de CP + botón Validar y rutas de escape ("Cambiar dirección", "Devolver al origen", "Cancelar").

### Devolver al origen (detalle)

El flujo más corto de los dos pasos: bottom sheet con pregunta de confirmación + card "Dirección de destino" (con botón "Cambiar" que deriva a Cambiar dirección) + CTA "Sí, devolver" → modal de confirmación con dato citado. Es el primer arquetipo de bottom sheet del módulo y la ruta de escape estándar cuando otra acción no es viable.

### Reagendar entrega (detalle)

Bottom sheet con card de dirección (botón "Cambiar" → Cambiar dirección) + select de fecha que abre un date picker compartido (navegación mes/año, grilla 7×6, día seleccionado en círculo rojo). CTA "Continuar" se habilita solo con fecha elegida. Cierra con modal de confirmación (ícono de calendario, cuerpo en texto plano con la fecha, sin card de dato citado).

### Recolección en sucursal + menú de acciones (detalle)

Mismo patrón que "Enviar a sucursal" (mapa, radio-cards, popup de error de CP), pero esta sección es también la que documenta el **menú de acciones** (kebab del detalle, mismo componente que el menú de "···" de otras áreas de la app) y la **variante de detalle "Resumen de envío"**: bloque colapsable con chip de carrier, chip de estado, y pares label/valor (tipo de incidencia, solución estimada, servicio, fechas, dimensiones, peso, costo, seguro). El chip de motivo (naranja) se reemplaza por un chip de acción aplicada (morado) al confirmar — este es el mecanismo real de "pantalla de éxito" de todo el módulo.

### Solicitar búsqueda (detalle)

El formulario más largo del módulo: pantalla completa con 3 textareas (descripción del problema, del empaque, del producto exacto — con placeholders de ejemplo entrecomillado) + Costo + selector de Moneda (dropdown con código y nombre) + Número de piezas. CTA se habilita con todos los campos requeridos completos; incluye footer con degradado de desvanecido para indicar contenido scrolleable. Cierra con modal de confirmación que además advierte el plazo ("puede tardar hasta 20 días hábiles").

### Intentar nueva entrega (detalle)

El flujo más corto: un solo modal, sin pantalla previa. Pregunta de confirmación + card de dirección editable (con botón "Cambiar" → Cambiar dirección) + acciones Cancelar / "Sí, reintentar". Es el único modal cuyo título es el nombre de la acción (afirmativo) en vez de la pregunta.

### Agregar detalles de acceso (detalle)

Bottom sheet con un único campo (textarea "Referencia", con placeholder ejemplificado) para capturar instrucciones de acceso al domicilio. CTA "Guardar" se habilita al escribir. **Es el único flujo de acción sin modal de confirmación** — consistente con la regla general: acciones reversibles guardan directo.

### Reportar incidencia — Paso 1/2 (detalle)

Flujo de alta, independiente de los 8 anteriores (que son de resolución). Primero un selector de envío: pantalla con buscador, filtro de período y lista de tarjetas de envío seleccionables por radio (carrier, guía, chip de estado, destinatario). Al confirmar, entra al wizard "Paso 1/2": indicador con título del paso + "PASO 1/2" + barra de progreso, un resumen del envío colapsable ("Ver más"/"Ver menos") y un select "Tipo de incidencia" que abre un dropdown compartido con 7 opciones (Cambio de dirección, Paquete sin movimiento, Recolecciones fallidas, Retraso en la entrega, Paquete dañado, Paquete perdido, Paquete abierto o alterado). CTA "Continuar" se habilita al elegir un tipo. El Paso 2/2 se documenta en el Flujo 27.

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Modal de confirmación parametrizable | Ícono en círculo + título + cuerpo + [Cancelar] [acción primaria roja]. Variable en ícono, tono (gris neutral / rojo), y tipo de cuerpo: texto plano, card con dato citado + botón copiar, o card editable con botón "Cambiar". Usado en 7 de las 9 acciones que confirman. |
| Card de dirección reutilizable | Título + dirección + botón secundario ("Replicar" o "Cambiar"). Aparece en Cambiar dirección, Devolver al origen, Reagendar entrega e Intentar nueva entrega — mismo componente parametrizable, no piezas distintas. |
| Bottom sheet de acción | Arquetipo anclado al fondo, header con título + botón de cerrar, CTA full-width. Usado en Devolver al origen, Reagendar entrega y Agregar detalles de acceso. |
| Popup "callejón sin salida" con rutas de escape | Cuando la acción elegida no es viable (sin sucursales para el CP): mensaje + reintento (input CP + Validar) + derivaciones a otras acciones + Cancelar. Candidato a componente transversal. |
| Date picker compartido | Popup centrado con navegación mes/año, grilla de días, día seleccionado en círculo. Usado en Reagendar entrega. |
| Dropdown de selección | Dos variantes: opción simple de una línea (tipo de incidencia) y opción de dos líneas código+descripción (moneda). |
| Menú de acciones (kebab) | Mismo componente transversal de menú "···" usado en otras áreas de la app; los ítems mostrados dependen del motivo de la incidencia. |
| Sistema de estados de incidencia | Chips reutilizados en tarjeta y detalle: Requiere acción, En revisión, En proceso, Finalizada. |

### Reglas de interacción y validación

- **Regla general de confirmación:** las acciones reversibles (p. ej. Agregar detalles de acceso) guardan directo sin modal; las acciones irreversibles o de plazo largo (Devolver al origen, Solicitar búsqueda, Cambiar dirección, Enviar/Recolección en sucursal, Reagendar entrega, Intentar nueva entrega) piden confirmación en un modal.
- El CTA principal de cada formulario/sheet permanece deshabilitado hasta que los campos requeridos estén completos.
- El cierre de una acción de resolución no tiene pantalla de éxito dedicada: el usuario vuelve al detalle de la incidencia, donde el chip de motivo se reemplaza por un chip de acción aplicada.
- Cuando una acción no es viable (p. ej. sin sucursales para el CP capturado), el sistema ofrece reintentar, derivar a otra acción de resolución, o cancelar — nunca deja al usuario sin salida.
- El botón "Cambiar" de las cards de dirección, dentro de cualquier flujo, deriva siempre a la acción "Cambiar dirección".
- El flujo de alta ("Reportar incidencia") se accede desde tres puntos: el estado vacío del listado, el menú "···" del listado, y un CTA permanente sobre el listado con datos.
- Los filtros del listado de incidencias reutilizan el drawer "Filtrar" transversal, con la adición de "Ordenar por" respecto a otros módulos.

---

## 27. Reportar incidencia — Paso 2/2

**Producto:** T1 Envíos
**Figma:** `4230:37750`

### Estructura del flujo

```
Paso 1/2 — selección del tipo de incidencia (Flujo 26)
    ↓
[Paso 2/2] — VACÍO
    Header "Reportar incidencia" + back
    Indicador de paso: nombre del tipo elegido + "PASO 2/2" + barra de progreso al 100%
    (Banner informativo azul — solo en tipos que abren investigación de paquetería)
    Formulario específico del tipo de incidencia (ver tabla de variantes)
    CTA "Enviar incidencia" DESHABILITADO
         ↓
    captura de datos ──▶ LLENO · CTA HABILITADO
         ↓
    tap "Enviar incidencia"
         ↓
[Modal de confirmación]
    "Confirmación de creación de incidente" — [Cancelar] [Sí, confirmar]
         ├── éxito ──▶ [Modal de éxito] "Tu incidente se envió con éxito." — [Entendido]
         └── regla de negocio incumplida (solo "Cambio de dirección") ──▶ [Modal de error de negocio] "Dirección duplicada" — [Entendido]
```

El título del wizard ("Reportar incidencia") no cambia por tipo; lo que cambia es el nombre en el tab del indicador de paso y el formulario completo. Los modales de cierre (confirmación y éxito) son **transversales**: mismo ícono, tono, copy y acciones en las 7 variantes.

### Campos por tipo de incidencia

| Tipo de incidencia | Campos específicos del formulario |
|---|---|
| Cambio de dirección | Textarea "Motivo del cambio" · card "Dirección actual" (con acción "Replicar") · bloque colapsable "Nueva dirección" (8 campos: calle, número exterior, número interior [opcional], código postal, colonia [select], estado, ciudad, referencia) |
| Paquete sin movimiento | Banner informativo · 3 textareas (descripción del problema, del empaque, exacta del producto) · fila Costo + Moneda · Número de piezas |
| Recolección fallida | 1 sola textarea: "Descripción del problema" — variante mínima, sin banner ni adjuntos |
| Retraso en la entrega | 3 textareas (empaque, producto, situación/problema) · fila Costo + Moneda · bloque colapsable "Dirección de entrega" (mismos 8 campos que "Cambio de dirección") — variante más extensa, sin banner |
| Paquete dañado | Banner informativo · textarea "Descripción del empaque" · input "Contenido" · input "Número de piezas dañadas" · input "Número de artículos en buen estado" · radio Sí/No · textarea "Descripción del problema" · evidencia fotográfica (dropzone → grid, hasta 4 fotos JPG/PNG, máx. 5 MB c/u) |
| Paquete perdido | Banner informativo · mismos 6 campos que "Paquete sin movimiento" (problema, empaque, producto, Costo + Moneda, número de piezas) · 2 adjuntos de archivo único en PDF ("Adjuntar factura", "Adjuntar guía", máx. 5 MB c/u) |
| Paquete abierto o manipulado | Banner informativo · 4 textareas (empaque, producto, "Contenido declarado del paquete" [pide el contenido esperado según el pedido], problema) · evidencia fotográfica (mismo componente que "Paquete dañado") |

### Patrones y componentes

| Componente | Descripción |
|---|---|
| Indicador de paso | Tab con el nombre del tipo elegido + etiqueta "PASO 2/2" + barra de progreso a ancho completo (100%, vs. 50% en el paso 1/2) |
| Banner informativo (`Messages`) | Aviso azul de que el reporte abre una investigación de hasta 20 días hábiles. Aparece antes de llenar el formulario, en los 4 tipos que abren investigación de paquetería (sin movimiento, dañado, perdido, abierto/manipulado) |
| Textarea de detalle | Bloque label + textarea para descripciones; es el grupo de campo más reutilizado, presente en las 7 variantes |
| Fila compuesta Costo + Moneda | Dos inputs en una sola fila bajo un label único: monto declarado + selector de moneda (MXN). Usado en los tipos con valor económico a reportar |
| Bloque de dirección (8 campos) | Calle, número exterior, número interior (opcional), código postal, colonia (select), estado, ciudad, referencia. Colapsable — expandido por defecto en el formulario vacío, colapsado tras la captura. Se reutiliza como "Nueva dirección" (Cambio de dirección) y "Dirección de entrega" (Retraso en la entrega) |
| Card "Dirección actual" | Card compacta con la dirección vigente del envío y la acción "Replicar". Exclusiva de "Cambio de dirección" |
| Subida de evidencia — modo fotos | Dropzone punteado → grid 2×2 con miniaturas y botón de borrar por foto + un tile para añadir más. Hasta 4 imágenes, formatos JPG/PNG, máximo 5 MB por archivo |
| Subida de evidencia — modo archivo único | Mismo dropzone base, pero acepta un solo archivo PDF por campo; al cargar muestra un thumbnail único con botón de borrar. Usado para adjuntar factura y guía |
| Radio Sí/No | Grupo de dos opciones para preguntas binarias dentro del formulario. Exclusivo de "Paquete dañado" |
| Modal de confirmación | Ícono neutro + "Confirmación de creación de incidente" + referencia al número de rastreo del envío + acciones "Cancelar" / "Sí, confirmar". Idéntico en las 7 variantes |
| Modal de éxito | Ícono verde + "Tu incidente se envió con éxito." + mención al seguimiento y al plazo estimado de respuesta de la paquetería + acción única "Entendido". Idéntico en las 7 variantes |
| Modal de error de negocio | Ícono neutro + "Dirección duplicada" + explicación de que la nueva dirección coincide con la actual + acción única "Entendido". Exclusivo de "Cambio de dirección" |

### Reglas de interacción y validación

- El CTA "Enviar incidencia" permanece deshabilitado hasta que el formulario tiene los datos mínimos capturados.
- Solo "Cambio de dirección" valida una regla de negocio adicional al enviar: la nueva dirección no puede coincidir con la actual — si coincide, se bloquea con el modal de error "Dirección duplicada" en vez de avanzar a confirmación.
- El campo "Número interior" en el bloque de dirección es el único marcado explícitamente como opcional.
- El bloque de dirección (8 campos) es colapsable: aparece expandido en el formulario vacío y colapsado una vez que el usuario ya capturó los datos.
- El banner informativo de investigación se muestra siempre **antes** de llenar el formulario, como advertencia temprana del plazo de resolución.
- La subida de evidencia tiene dos configuraciones de un mismo componente base: **múltiple** (hasta 4 fotos JPG/PNG) para evidenciar daño o manipulación, y **única** (1 PDF por campo) para adjuntar documentos como factura o guía de envío.
- El cierre del flujo es siempre vía modal explícito (confirmación → éxito), a diferencia de los flujos de resolución de incidencias ya reportadas (Flujo 26), donde el cierre es el retorno a la pantalla de detalle sin modal.
