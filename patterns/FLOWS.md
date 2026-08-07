# Flows — NEXUS V2.0

> Los flujos documentan cómo se ensamblan pantallas y componentes para completar tareas de usuario de principio a fin. Son la referencia de implementación para secuencias de más de una pantalla.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (`SD---Migration-V2`, `Nuevo-onboarding`, `T1envios---Crear-envio`) · **Owner:** Karla Salazar — Head of UX/UI

---

## Índice

1. [Registro y login](#1-registro-y-login)
2. [Onboarding — Encuesta inicial](#2-onboarding--encuesta-inicial)
3. [Crear envío](#3-crear-envío)
4. [Checkout — Tienda en línea](#4-checkout--tienda-en-línea)
5. [Checkout — Link de pago](#5-checkout--link-de-pago)
6. [CRUD genérico](#6-crud-genérico)
7. [Búsqueda y filtrado](#7-búsqueda-y-filtrado)

---

## 1. Registro y login

**Producto:** Ecosistema T1 (login unificado para todos los productos)
**Contexto:** Pantalla de autenticación compartida — mismo flujo independientemente del producto al que accede el usuario.

### Flujo de login

```
[Pantalla de login]
├── Email + contraseña → [Dashboard]
├── "Continuar con Google" (OAuth) → [Dashboard]
├── "Continuar con correo" → [Dashboard]
└── "¿Nuevo? Crear cuenta" → [Flujo de registro]
```

### Flujo de registro

```
[1] Datos básicos
    Nombre · Email · Contraseña
    Indicador de fuerza de contraseña (4 niveles)
    ↓
[2] Verificación OTP
    5 dígitos vía SMS
    Opción "Reenviar vía SMS" con contador regresivo
    ↓
[3] Encuesta inicial  ← Solo si el registro NO viene de "crear página"
    Ver §2
    ↓
[Dashboard del producto]
```

### Indicador de fuerza de contraseña

4 segmentos de barra que se activan progresivamente según la fortaleza:

| Nivel | Condición | Mensaje |
|---|---|---|
| Débil | < 8 caracteres | "Contraseña débil: Tu contraseña debe tener al menos 8 caracteres" |
| Moderada | ≥ 8 caracteres | "Contraseña moderada: Te sugerimos alargarla y combinar letras, números y símbolos." |
| Segura | ≥ 8 chars + combinación | "Contraseña segura: Tu contraseña cumple con las recomendaciones de seguridad." |
| Fuerte | ≥ 15 chars + combinación | "Contraseña fuerte" |

### Excepción: registro desde creación de página

Cuando el usuario llega al registro desde un flujo de creación de página T1 (integración externa), **la encuesta se omite** y accede directamente al dashboard del producto correspondiente.

### Navegación entre pasos

- Indicador de progreso: dots (elipse activa = pill alargada `#DB3B2B`, inactivas = círculos grises)
- Botón "Atrás" (`icon-nav/chevron-left` + texto) alineado izquierda
- Botón "Continuar" / "Siguiente" (primario) alineado derecha
- Sin barra de progreso numérica — solo dots

---

## 2. Onboarding — Encuesta inicial

**Producto:** Ecosistema T1 (post-registro)
**Figma:** `Nuevo-onboarding` · node `51:3666`
**Propósito:** Personalizar la experiencia inicial según el tipo de negocio, canales y madurez del usuario.

### Estructura del flujo (desktop + mobile)

```
[P1] ¿Qué quieres hacer?  (selección múltiple con íconos)
     □ Crear mi tienda en línea
     □ Cotizar y realizar mis envíos
     □ Vender en marketplaces (Mercado Libre, Amazon, etc.)
     □ Cobrar con tarjeta o transferencia
     ↓
[P2] ¿Dónde vendes?  (selección múltiple con íconos)
     □ Tienda en línea propia
     □ Tienda física
     □ Redes sociales (Instagram, Facebook, etc.)
     □ Marketplaces (Mercado Libre, Amazon, etc.)
     □ Aún no lo decido / No estoy vendiendo actualmente
     ↓
[P3] ¿Cuánto llevas operando?  (selección única con radio)
     ○ Estoy empezando (Empresa nueva)
     ○ Ya está operando (Empresa existente)
     ↓
[P4] ¿Cuál es el nombre de tu tienda?
     Input de texto + asistente IA ("¿Aún no lo decides? → Usar IA")
     Panel IA: "Cuéntanos sobre tu tienda" + input multiline + botón IA
     ↓
[P5] ¿Cuál es tu rango de ventas mensual?  (selección única)
     ○ Menos de $250 mil
     ○ $250 mil - $1 millón
     ○ Más de $1 millón
     ↓
[Pantalla de carga]
Logo T1 centrado + spinner
     ↓
[Dashboard del producto]
```

### Reglas de navegación

- El usuario puede regresar con "Atrás" en cualquier paso
- El botón "Continuar" se activa solo cuando hay al menos una selección (P1, P2, P3, P5) o hay texto (P4)
- Las respuestas determinan qué módulos/onboarding específico se muestra en el dashboard
- El asistente IA en P4 es opcional — el usuario puede omitirlo e ingresar el nombre manualmente

### Diferencias mobile

- Layout de selecciones: lista vertical (no grid) con opciones a ancho completo `328px`
- Íconos `24×24px` alineados a la izquierda de cada opción (en desktop son `40×40px` centrados sobre el label)

---

## 3. Crear envío

**Producto:** T1 Envíos
**Figma:** `T1envios---Crear-envio` · node `5:29808`

### Estructura del flujo

```
[Step 1] Direcciones
    Dirección de origen  (selector dropdown — dirección guardada)
    Dirección de destino (formulario completo)
         ↓
[Step 2] Paquete
    Peso · Dimensiones · Tipo de contenido · Valor declarado
         ↓
[Step 3] Cotización
    Comparador de paqueterías (DHL, FedEx, Estafeta, UPS...)
    Precio · Tiempo estimado · Servicio
         ↓
[Step 4] Confirmación y pago
    Resumen del envío · CTA "Crear guía"
         ↓
[Guía generada]
    Descargar PDF · Historial de envíos
```

### Step 1 — Direcciones (detalle)

La pantalla está dividida en dos secciones dentro de la misma vista:

**Dirección de origen**
- Dropdown con las direcciones guardadas del usuario (badge "Principal" en la predeterminada)
- Muestra nombre completo y dirección debajo del selector
- Link "Cambiar" para seleccionar otra dirección guardada
- Cambio de origen: abre submenu con buscador + lista de direcciones guardadas (desktop) o bottom sheet (mobile)

**Dirección de destino**
- Buscador de dirección por texto (autocompletado)
- Divider "o" para separar buscador del formulario manual
- Formulario manual completo:
  - Datos de contacto: Nombre · Apellido · Email · Teléfono · Empresa (opcional)
  - Dirección: Calle · Número exterior · Número interior · CP · Colonia (dropdown) · Estado · Ciudad
  - Referencias (textarea — notas de entrega)
  - Checkbox "Guardar dirección de destino"
- CTA "Siguiente" alineado a la derecha

**Desktop:** Ambas secciones en layout vertical dentro de un contenedor centrado `800px`.
**Mobile:** Layout de pantalla completa, scroll vertical. El cambio de origen abre un bottom sheet con buscador y lista.

### Casos del flujo

| Caso | Comportamiento |
|---|---|
| Sin dirección de origen configurada | Empty state con CTA "Agregar dirección" — ver `patterns/EMPTY-STATES.md` |
| Dirección de origen guardada | Muestra selector con badge + datos de la dirección activa |
| Cambiar dirección de origen | Abre panel/bottom sheet con lista de direcciones guardadas + buscador |
| Destino vacío | Formulario en estado vacío, botón "Siguiente" deshabilitado |
| Destino con datos | Todos los campos requeridos llenos activan "Siguiente" |

---

## 4. Checkout — Tienda en línea

**Producto:** T1 Tienda (tienda en línea del comerciante)
**Contexto:** El comprador final llega desde el carrito de compras de la tienda.

### Estructura del flujo

```
[Carrito]
    Resumen de productos · Subtotal · Cantidad
    CTA "Ir a pagar"
         ↓
[Checkout]  ← Pantalla única con dos secciones
    Sección izquierda: Datos de envío
        Nombre · Email · Teléfono
        Dirección completa (Calle, No. ext/int, CP, Colonia, Estado, Ciudad)
    Sección derecha: Método de pago
        Tarjeta de crédito/débito
        SPEI / Transferencia
        Otros métodos habilitados por el comerciante
    Resumen de orden (sticky)
         ↓
[Confirmación]
    Número de orden · Resumen · Tiempo estimado de entrega
    Email de confirmación enviado automáticamente
```

### Reglas

- El checkout es una **pantalla única** que contiene tanto el formulario de envío como el método de pago — no son pasos separados.
- El CTA "Pagar" se activa solo cuando todos los campos requeridos están llenos y hay un método de pago seleccionado.
- Validación inline de campos al perder foco (`onBlur`).
- El resumen de orden es sticky en desktop (columna derecha) y se colapsa como sección expandible en mobile.

---

## 5. Checkout — Link de pago

**Producto:** T1 Pagos (link de pago o gateway de integración)
**Contexto:** El comprador llega directamente a través de un link, sin pasar por carrito.

### Estructura del flujo

```
[Checkout]  ← Sin paso previo de carrito
    Descripción del producto/servicio · Monto
    Datos del comprador: Nombre · Email · Teléfono
    Método de pago:
        Tarjeta de crédito/débito
        SPEI / Transferencia
        Otros métodos configurados en T1 Pagos
         ↓
[Confirmación]
    Pago exitoso · Referencia de transacción
    Email de confirmación al comprador
```

### Diferencias vs tienda en línea

| Aspecto | Tienda en línea | Link de pago |
|---|---|---|
| Entrada | Desde carrito | Directo al checkout |
| Datos de envío | Sí (domicilio completo) | No (solo datos de contacto) |
| Resumen | Líneas de producto | Concepto + monto único |
| Confirmación | Número de orden | Referencia de transacción |

### Manejo de errores de pago

Los errores de pago se manejan caso por caso según el tipo de error. No hay un flujo único de recuperación — el mensaje y las opciones disponibles varían según el código de error devuelto por el procesador. Ver `content/UX-WRITING.md` §2 para patrones de mensajes de error de sistema.

---

## 6. CRUD genérico

Patrón reutilizable en todos los módulos del sistema (productos, clientes, descuentos, sucursales, etc.).

### Flujo base

```
[Listado]
    Tabla con filtros + búsqueda
    CTA "Agregar [entidad]" (primario, esquina superior derecha)
         ↓
[Crear]
    Formulario en página o modal según la complejidad
    CTA "Guardar" (primario) · "Cancelar" (secundario)
         ↓
[Listado]  ← Toast "Creaste [entidad] con éxito"
```

### Editar

```
[Listado]
    Click en fila o ícono "···" → "Editar"
         ↓
[Editar]
    Mismo formulario que Crear, con datos precargados
    CTA "Guardar cambios" (primario) · "Descartar cambios" (secundario)
         ↓
[Listado]  ← Toast "Cambios guardados"
```

### Eliminar

```
[Listado]
    Click en "···" → "Eliminar"
         ↓
[Modal de confirmación destructiva]
    "¿Eliminar [entidad]?"
    "Esta acción no se puede deshacer."
    CTA "Eliminar" (danger) · "Cancelar" (secundario)
         ↓
[Listado]  ← Toast "Se eliminó [entidad]"
         o
[Listado sin cambios]  ← Si el usuario cancela
```

### Reglas del patrón

- La confirmación destructiva **siempre** va en modal — nunca inline ni directa.
- El botón destructivo en el modal usa variante `danger` (`#CC0000`), no rojo primario.
- Las acciones de edición/eliminar se acceden desde el menú de tres puntos `···` en la fila de la tabla.
- Si la creación es simple (pocos campos), usar modal. Si es compleja (muchos campos, secciones), usar página propia.
- Validación inline en todos los formularios — al perder foco en cada campo.
- El CTA "Guardar" se deshabilita si hay errores de validación pendientes.

---

## 7. Búsqueda y filtrado

Patrón reutilizable en todos los listados del sistema.

### Flujo

```
[Listado con contenido]
    Barra de búsqueda + filtros en pills/dropdowns
         ↓ El usuario escribe o aplica filtros
[Resultados filtrados]
    Tabla actualizada · Pills activos con "X" para remover
    Contador "N resultados"
         ↓ Si no hay resultados
[Empty state — búsqueda sin resultados]
    "No encontramos resultados para '[término]'"
    "Intenta con otros términos o revisa los filtros aplicados."
    CTA "Limpiar filtros" (secundario)
```

### Tipos de filtro en el sistema

| Tipo | Implementación | Ejemplo de uso |
|---|---|---|
| Período de tiempo | Dropdown: Hoy / Esta semana / Este mes / Rango personalizado | Historial de movimientos, pedidos |
| Estatus | Pills seleccionables o dropdown multi-select | Pedidos, envíos, productos |
| Categoría | Dropdown single o multi-select | Productos, transacciones |
| Canal de venta | Dropdown multi-select | Pedidos, productos |
| Búsqueda libre | Input con ícono lupa, búsqueda por texto | Todos los listados |

### Reglas

- Los filtros activos se muestran como pills con `×` para remover individualmente.
- "Limpiar filtros" limpia todos los filtros activos a la vez.
- La búsqueda es en tiempo real (debounce `300ms`) — no requiere presionar Enter.
- El estado de filtros activos persiste durante la sesión, pero no entre sesiones.
- Cuando hay filtros activos y no hay resultados, mostrar siempre el CTA "Limpiar filtros" — nunca dejar al usuario sin salida.

---

## Referencias cruzadas

- **Empty states por módulo** → `patterns/EMPTY-STATES.md`
- **Toast de confirmación de acciones** → `patterns/NOTIFICATIONS.md` §1
- **Modal de confirmación destructiva** → `components/MOLECULES.md` §Modal
- **Copy de errores, confirmaciones y CTAs** → `content/UX-WRITING.md`
- **Steps / Stepper (indicador de pasos)** → `components/ATOMS.md` §8.3
- **Inputs y formularios** → `components/ATOMS.md` §3
- **Tablas con filtros** → `components/TABLES.md`
