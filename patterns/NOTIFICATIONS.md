# Notifications — NEXUS V2.0

> El sistema de notificaciones de T1 comunica el resultado de acciones, estados del sistema y alertas que requieren atención. Cada tipo tiene un propósito específico — elegir el tipo incorrecto genera ruido o hace que información crítica pase desapercibida.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (`SD---Migration-V2`) · **Owner:** Karla Salazar — Head of UX/UI

---

## Mapa de decisión

```
¿Requiere acción inmediata del usuario?
├── Sí, bloquea el flujo → Modal
└── No bloquea
    ├── ¿Es un aviso persistente de sistema/plan/estado?
    │   └── Sí → Banner
    └── ¿Es feedback de una acción reciente?
        ├── Acción simple completada / en proceso → Toast
        └── Error en contexto de formulario → Alerta inline
```

---

## Tipos del sistema

| Tipo | Cuándo usarlo | Posición | Persistencia | Dismiss |
|---|---|---|---|---|
| **Toast** | Feedback de acciones: éxito, proceso en curso | Esquina inferior derecha | Auto o hasta completar proceso | X manual |
| **Banner** | Avisos de sistema, plan, configuración pendiente | Debajo del header, full-width del contenido | Hasta dismiss manual o hasta resolver | X o sin dismiss según severidad |
| **Alerta inline** | Error de límite de plan dentro de una sección | Debajo del search/header de sección, full-width de la tabla/card | Hasta resolver la condición | Sin dismiss |
| **Modal** | Confirmaciones destructivas, errores críticos que bloquean | Centro de pantalla con overlay | Hasta acción del usuario | Solo vía acción explícita |

> **Nota:** Los modales de confirmación están documentados en `components/MOLECULES.md`. Este archivo cubre toast, banner y alerta inline.

---

## 1. Toast

Los toasts son notificaciones transitorias que aparecen en la **esquina inferior derecha** de la pantalla. No interrumpen el flujo del usuario.

### Variantes

El sistema tiene dos estilos visuales de toast según el tipo de evento:

#### Toast de proceso (fondo dark)

Para eventos que tienen duración: procesos en curso y su resultado final (éxito o error).

```
┌─────────────────────────────────────┐
│ [Título del estado]              [X]│
│ ○ [Descripción del proceso]  HH:MM  │
└─────────────────────────────────────┘
```

- **Fondo:** `#4C4C4C` (Oxford)
- **Título:** `font-manrope font-semibold text-[14px] text-white`
- **Descripción:** `font-manrope font-normal text-[12px] text-gray-400`
- **Timestamp:** `font-manrope text-[11px] text-gray-500`, alineado a la derecha
- **Ícono de estado:** spinner rojo (`#DB3B2B`) para "procesando", check verde (`#4FC153`) para "éxito"
- **Dismiss:** X esquina superior derecha, siempre visible
- **Ancho:** fijo `~320px`
- **Border-radius:** `10px`

**Estados del toast de proceso:**

| Estado | Título | Ícono |
|---|---|---|
| En proceso | `Procesando` | Spinner `#DB3B2B` girando |
| Completado con éxito | `Proceso finalizado` | Check circle `#4FC153` |
| Completado con error | `Ocurrió un error` | X circle `#CC0000` |

#### Toast de acción simple (fondo de color)

Para confirmaciones inmediatas de acciones de usuario: crear, guardar, eliminar.

```
┌─────────────────────────────────────┐
│ ✓  [Título bold]                    │
│    [Descripción o siguiente paso]   │
└─────────────────────────────────────┘
```

- **Fondo success:** `#4FC153` (Green 500)
- **Fondo error:** `#CC0000` (Red 900)
- **Fondo warning:** `#FF6700` (Orange 500)
- **Texto:** `text-white` para todos los casos
- **Título:** `font-manrope font-bold text-[14px] text-white`
- **Descripción:** `font-manrope font-normal text-[13px] text-white/90`
- **Ícono:** check `✓` para success, `✕` para error — siempre blanco
- **Dismiss:** No tiene X explícito — auto-dismiss a los **5 segundos**
- **Ancho:** fijo `~380px`
- **Border-radius:** `10px`

### Comportamiento

| Regla | Valor |
|---|---|
| Posición | `fixed bottom-6 right-6` |
| Auto-dismiss (acción simple) | 5 segundos |
| Toast de proceso | Persiste hasta que el proceso termina, luego transiciona al estado final |
| Stacking | Máximo 3 toasts visibles simultáneamente, FIFO (el más antiguo se descarta primero) |
| Animación entrada | Slide desde la derecha + fade in |
| Animación salida | Fade out |
| Z-index | Por encima de todo el contenido, por debajo de modales |

### Sin acción secundaria

Los toasts del sistema **no tienen CTA ni acción secundaria** — solo dismiss manual (toast de proceso) o auto-dismiss (toast de acción simple). Si el evento requiere que el usuario tome una acción, usar banner o modal.

### Ejemplos reales del sistema

| Acción | Tipo toast | Título | Descripción |
|---|---|---|---|
| Exportar CSV | Proceso → dark | `Procesando` → `Proceso finalizado` | `Descargando CSV` → `Archivo.CSV` |
| Crear producto | Acción simple → verde | `Creaste un producto con éxito` | `Continúa completando la información de los canales de venta` |
| Error de exportación | Proceso → dark | `Ocurrió un error` | `No fue posible descargar el archivo` |

### Accesibilidad

```tsx
// Toast success / info
<div role="status" aria-live="polite" aria-atomic="true">
  {/* contenido del toast */}
</div>

// Toast error crítico
<div role="alert" aria-live="assertive" aria-atomic="true">
  {/* contenido del toast */}
</div>
```

> Ver reglas completas en `accessibility/A11Y.md` §ARIA → Toasts y notificaciones.

---

## 2. Banner

Los banners comunican información de sistema que el usuario debe atender, pero que no bloquea el flujo inmediato. Aparecen **debajo del header de la página**, ocupando el ancho completo del área de contenido.

### Componente base: T1Message

Los banners usan el componente `T1Message` definido en `components/MOLECULES.md` §10. Es un mensaje inline — no flotante — con borde completo, ícono a la izquierda y texto.

```
┌────────────────────────────────────────────────────────────┐  ← border completo
│ [○]  [Mensaje, puede incluir link inline]              [X] │  ← dismiss opcional
└────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────  [Botón CTA] ──┐  ← con acción
│ [○]  [Mensaje del banner]                                  │  ← sin dismiss
└────────────────────────────────────────────────────────────┘
```

- **Ícono:** átomo indicador de estado `30×30px` — `InformationCircleIcon`, `ExclamationTriangleIcon` o `XCircleIcon`
- **Mensaje:** `font-manrope font-normal text-[14px] text-oxford`. Puede incluir `<a>` con `font-semibold underline` para links inline
- **Borde:** completo `1px solid {color-variante}` — **no solo izquierdo**
- **Border-radius:** `10px`
- **Padding:** `12px 16px`
- **Ancho:** `688px` desktop · `w-full` mobile
- **Dismiss:** X esquina derecha — **opcional**, según si la condición es postergable
- **Botón CTA:** exterior al componente, alineado a la derecha — solo cuando hay acción directa disponible

### Variantes por severidad

| Variante | Cuándo | Token BG | Token border/ícono | Dismiss |
|---|---|---|---|---|
| **Danger** | Acción bloqueante: tarjeta expirada, límite alcanzado con impacto directo | `red-50` | `red-700` | No — tiene botón CTA obligatorio |
| **Caution** | Configuración pendiente recomendada, aviso no urgente | `orange-100` | `orange-500` | Sí — el usuario puede posponer |
| **Info** | Nuevas funcionalidades, avisos neutrales de sistema | `blue-100` | `blue-500` | Sí |

### Comportamiento

| Regla | Valor |
|---|---|
| Posición | Debajo del `<h1>` de página, antes del contenido principal |
| Persistencia | Permanece hasta que el usuario hace dismiss o resuelve la condición |
| Sin dismiss | Cuando la acción es obligatoria (ej: tarjeta expirada con botón "Actualizar tarjeta") |
| Stacking | Máximo 1 banner visible por página. Si hay múltiples condiciones, priorizar: error > warning > info |
| Mobile | Full-width, el botón CTA baja a una segunda línea |

### Ejemplos reales del sistema

| Contexto | Severidad | Mensaje | CTA / Dismiss |
|---|---|---|---|
| Tarjeta de pago expirada | Error | `Tu tarjeta con terminación ···· 1234 ha expirado, actualiza tu método de pago para continuar recargando.` | Botón "Actualizar tarjeta" — sin dismiss |
| Información fiscal faltante | Warning | `Ingresa tu información fiscal [aquí] para recibir facturas automáticamente.` | Dismiss X — sin botón |

---

## 3. Alerta inline

La alerta inline es una notificación que aparece **dentro de una sección de contenido**, generalmente debajo del área de búsqueda o filtros de una tabla. No es un banner de página — está contextualizada dentro de la subsección donde ocurre la condición.

### Anatomía

```
┌───────────────────────────────────────────────────────────────┐
│         [Mensaje descriptivo de la condición o límite]        │
└───────────────────────────────────────────────────────────────┘
```

- **Alineación:** texto centrado
- **Fondo:** heredado de la severidad (igual que banner)
- **Sin ícono lateral** — el color comunica la severidad
- **Sin dismiss** — la condición debe resolverse para desaparecer
- **Sin botón** — si requiere acción, usar banner
- **Border-radius:** `6px`
- **Padding:** `px-4 py-2`

### Cuándo usar alerta inline vs banner

| Condición | Tipo |
|---|---|
| Afecta a toda la página o sesión | Banner |
| Afecta específicamente a una tabla, sección o módulo | Alerta inline |
| Requiere acción con botón | Banner |
| Solo informa sin CTA | Alerta inline |

### Ejemplo real del sistema

| Contexto | Mensaje |
|---|---|
| Límite de imágenes alcanzado en Archivos multimedia | `Has alcanzado el límite de imágenes almacenadas. Elimina algunas o actualiza tu plan para seguir subiendo contenido.` |

---

## Prioridad del sistema

Cuando múltiples notificaciones coexisten, se aplica esta jerarquía:

```
Error > Warning > Info > Success
```

- **Banners:** solo 1 visible por página — se muestra el de mayor prioridad
- **Toasts:** hasta 3 simultáneos — se apilan desde abajo hacia arriba
- **Alerta inline:** puede coexistir con un banner (son niveles diferentes)
- **Toast + Banner:** pueden coexistir — son capas visuales independientes

---

## Tokens de estilo

### Toast de proceso (dark)

| Elemento | Valor |
|---|---|
| Fondo | `#4C4C4C` (Oxford) |
| Título | `font-manrope font-semibold text-[14px] text-white` |
| Descripción | `font-manrope font-normal text-[12px] text-gray-400` |
| Timestamp | `font-manrope text-[11px] text-gray-500` |
| Ícono procesando | Spinner `#DB3B2B` |
| Ícono completado | Check circle `#4FC153` |
| Ícono error | X circle `#CC0000` |
| Ancho | `320px` |
| Border-radius | `10px` |

### Toast de acción simple

| Elemento | Valor |
|---|---|
| Fondo success | `#4FC153` |
| Fondo error | `#CC0000` |
| Fondo warning | `#FF6700` |
| Título | `font-manrope font-bold text-[14px] text-white` |
| Descripción | `font-manrope font-normal text-[13px] text-white/90` |
| Auto-dismiss | `5000ms` |
| Ancho | `380px` |
| Border-radius | `10px` |

### Banner (T1Message)

| Elemento | Valor |
|---|---|
| Mensaje | `font-manrope font-normal text-[14px] text-oxford` |
| Link inline | `font-semibold underline` |
| Padding | `12px 16px` |
| Border-radius | `10px` |
| Border | `1px solid {token-variante}` — completo, no solo izquierdo |
| Ancho | `688px` desktop · `w-full` mobile |
| Ícono | `30×30px` — átomo indicador de estado |

---

## Anti-patrones

| ❌ Evitar | ✅ En cambio |
|---|---|
| Toast para errores que requieren acción del usuario | Banner con CTA |
| Banner para confirmar acciones simples | Toast de acción simple |
| Más de 1 banner simultáneo en la misma página | Priorizar por severidad — mostrar solo el más crítico |
| Toast con auto-dismiss en procesos asincrónicos | Toast de proceso persistente hasta completar |
| Alerta inline con botón CTA | Banner si requiere acción directa |
| Modal para notificaciones informativas | Toast o banner según persistencia necesaria |
| `aria-live="assertive"` en toasts informativos | `aria-live="polite"` — assertive solo para errores críticos |

---

## Referencias cruzadas

- **Modales de confirmación destructiva** → `components/MOLECULES.md` §Modal
- **Copy de mensajes de error y éxito** → `content/UX-WRITING.md` §2, §3
- **ARIA para notificaciones** → `accessibility/A11Y.md` §ARIA → Toasts y notificaciones
- **Colores semánticos** → `foundation/COLORS.md` §Colores Semánticos
- **Estados de componente** → `components/STATES.md`
