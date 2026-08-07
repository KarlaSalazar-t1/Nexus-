# Empty States — NEXUS V2.0

> Los empty states son el primer punto de contacto con un módulo vacío. En el ecosistema T1, son oportunidades de orientar y motivar — no solo de informar que no hay datos.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (`SD---Migration-V2`) · **Owner:** Karla Salazar — Head of UX/UI

---

## Principios

- **Orientar antes que informar.** El empty state no solo dice "no hay nada" — explica por qué y qué hacer.
- **Tono motivador, no neutral.** El usuario acaba de llegar a un módulo vacío; es el momento de invitarlo a actuar.
- **El contexto determina la urgencia.** Un empty state en un módulo de configuración inicial es diferente al de una búsqueda sin resultados.
- **Sin ilustración no es un estado incompleto.** La versión sin ilustración es válida y es el estado actual de producción.

---

## Anatomía

El empty state tiene tres elementos y un elemento opcional:

```
[ Ilustración contextual ]     ← Opcional (planeado, en construcción)
[ Título ]                     ← Obligatorio
[ Descripción ]                ← Obligatorio
[ CTA ]                        ← Obligatorio en la mayoría de casos
[ Link secundario ]            ← Opcional
```

### Reglas por elemento

| Elemento | Regla |
|---|---|
| **Ilustración** | Isométrica, línea negra con acento rojo (`#DB3B2B`). Tamaño máximo `120px`. Solo cuando existe la ilustración para ese módulo. |
| **Título** | Describe la ausencia con contexto. `font-manrope font-bold text-[20px] text-gray-900`. Sin punto final. |
| **Descripción** | Accionable: dice qué hacer o qué ocurrirá. `font-manrope font-normal text-[14px] text-gray-500`. Con punto final. |
| **CTA** | Botón primario (`#DB3B2B`) en la mayoría de casos. Secundario si la acción no es la principal del módulo. Ancho fijo ~`300px`. |
| **Link secundario** | Texto plano `text-[14px] text-gray-500` con `hover:underline`. Para ayuda contextual ("¿Cómo hacer X?"). |

---

## Layout

### Sin ilustración (estado actual de producción)

Todo el contenido centrado horizontal y verticalmente dentro del área disponible. Ocupa el 100% del contenedor padre, sin card ni borde propio.

```tsx
<div className="flex flex-col items-center justify-center gap-4 py-24 text-center">
  <div className="flex flex-col items-center gap-2">
    <h3 className="font-manrope font-bold text-[20px] text-gray-900">
      {titulo}
    </h3>
    <p className="font-manrope font-normal text-[14px] text-gray-500 max-w-[420px]">
      {descripcion}
    </p>
  </div>
  <T1Button variant="primary" className="w-[300px]">
    {labelCTA}
  </T1Button>
</div>
```

> **Nota sobre el contenedor:** El empty state no tiene card ni borde propio. Si aparece dentro de una subsección que ya tiene card (ej: tabla, panel lateral), hereda ese contenedor. No agregar bordes ni backgrounds adicionales.

### Con ilustración (planeado)

Layout horizontal: ilustración a la izquierda, texto y CTA a la derecha. Alineación vertical centrada entre los dos bloques.

```tsx
<div className="flex items-center justify-center gap-10 py-16">
  <div className="shrink-0">
    <img src="/assets/illustrations/{modulo}.svg" alt="" aria-hidden="true" className="w-[120px]" />
  </div>
  <div className="flex flex-col gap-3 max-w-[460px]">
    <h3 className="font-manrope font-bold text-[20px] text-gray-900">
      {titulo}
    </h3>
    <p className="font-manrope font-normal text-[14px] text-gray-500">
      {descripcion}
    </p>
    <T1Button variant="primary" className="w-[280px]">
      {labelCTA}
    </T1Button>
  </div>
</div>
```

> **Ilustraciones:** Viven en `/public/assets/illustrations/` dentro de cada proyecto T1. Son SVG isométricos, línea negra con acento rojo `#DB3B2B`. Se agregan progresivamente conforme se diseñan por módulo.

---

## Variantes por tipo de contexto

### 1. Primera vez en el módulo (onboarding)

El usuario nunca ha creado nada. Máxima motivación — explicar el valor, no solo la ausencia.

**Patrón de título:** `Aún no tienes [entidad]` o `Aún no cuentas con [entidad]`
**Patrón de descripción:** Explica qué permite el módulo + invita a la acción.
**CTA:** Primario. Acción de creación directa.

### 2. Submódulo dependiente

El módulo requiere que algo esté configurado primero (ej: dirección de origen antes de crear envíos).

**Patrón de título:** `Aún no cuentas con [prerequisito]`
**Patrón de descripción:** Explica el prerequisito y por qué es necesario.
**CTA:** Primario. Lleva a configurar el prerequisito.

### 3. Búsqueda sin resultados

El usuario aplicó una búsqueda o filtros y no hay coincidencias.

**Patrón de título:** `No encontramos resultados para "[término]"` o `Nada coincide con tus filtros`
**Patrón de descripción:** Sugiere acciones concretas para resolver.
**CTA:** Secundario o ausente. Puede ser "Limpiar filtros" o "Buscar con otro término".

### 4. Submódulo secundario sin acción directa

El contenido se genera automáticamente (ej: historial, reportes sin datos).

**Patrón de título:** `Aún no hay [entidad] disponibles`
**Patrón de descripción:** Explica qué evento generará el contenido.
**CTA:** Secundario o ausente.

---

## Catálogo por producto

### T1 Tienda

| Módulo | Título | Descripción | CTA | Tipo botón |
|---|---|---|---|---|
| Productos (listado) | Aún no tienes productos | Empieza a cargar tus productos, puedes hacerlo de manera masiva o individual. | Agregar producto | Primario |
| Productos (inventario) | Aún no tienes productos | Carga tus productos para poder administrar el inventario. | Ir a listado de productos | Primario |
| Transferencias | Transfiere inventario entre sucursales | Registra y da seguimiento a los movimientos de productos entre tus sucursales para mantener tu inventario siempre actualizado. | Crear transferencia | Primario |
| Pedidos | Aún no tienes pedidos | Cuando recibas tu primer pedido, aparecerá aquí. | — | — |
| Clientes | Aún no tienes clientes registrados | Importa tu base de clientes o espera a que llegue tu primer pedido. | Importar clientes | Primario |
| Canales de venta | Aún no tienes canales conectados | Conecta tu tienda con marketplaces y redes sociales para vender en más lugares. | Conectar canal | Primario |

### T1 Envíos

| Módulo | Título | Descripción | CTA | Tipo botón |
|---|---|---|---|---|
| Dirección de origen | Aún no cuentas con una dirección de origen | Antes de realizar tu primer envío, necesitamos saber desde dónde se enviarán tus paquetes. | Agregar dirección | Primario |
| Envíos pendientes | Sin envíos pendientes | Cuando crees un envío, aparecerá aquí hasta que sea recolectado. | Crear envío | Primario |
| Historial de envíos | Aún no tienes envíos realizados | Cuando completes tu primer envío, podrás ver el historial aquí. | — | — |

### T1 Pagos

| Módulo | Título | Descripción | CTA | Tipo botón |
|---|---|---|---|---|
| Transacciones | Sin movimientos registrados | Cuando realices o recibas tu primer pago, aparecerá aquí. | Configurar pagos | Secundario |
| Métodos de pago | Aún no tienes métodos de pago configurados | Agrega los métodos de pago que aceptarás en tu tienda. | Agregar método | Primario |
| Reclamaciones | Sin reclamaciones activas | Aquí aparecerán las reclamaciones que requieran tu atención. | — | — |

### T1 Score

| Módulo | Título | Descripción | CTA | Tipo botón |
|---|---|---|---|---|
| Score crediticio | Aún no tienes un score disponible | Conecta tu cuenta bancaria o historial de ventas para calcular tu score. | Conectar cuenta | Primario |
| Historial | Sin historial disponible | Tu historial crediticio aparecerá aquí conforme generes actividad. | — | — |

### T1 Marketing

| Módulo | Título | Descripción | CTA | Tipo botón |
|---|---|---|---|---|
| Campañas | Aún no tienes campañas | Crea tu primera campaña para empezar a conectar con tus clientes. | Crear campaña | Primario |
| Analytics | Sin datos suficientes | Conecta una fuente de datos o espera a que tu campaña genere métricas. | Conectar fuente | Secundario |
| Audiencias | Aún no tienes audiencias creadas | Define segmentos de clientes para personalizar tus campañas. | Crear audiencia | Primario |

---

## Búsqueda y filtros sin resultados

Este tipo de empty state aplica en cualquier tabla o listado del sistema cuando una búsqueda o filtro activo no devuelve resultados.

```
No encontramos resultados para "[término]"
Intenta con otros términos o revisa los filtros aplicados.
[ Limpiar filtros ]   ← Secundario
```

```
Nada coincide con tus filtros
Ajusta o elimina los filtros para ver más resultados.
[ Limpiar filtros ]   ← Secundario
```

> **Regla:** El término de búsqueda siempre va entre comillas en el título. El CTA es siempre secundario — la acción destructiva principal (buscar de nuevo) la hace el usuario directamente en el input.

---

## Tokens de estilo

| Elemento | Token / Valor |
|---|---|
| Título color | `text-gray-900` (`#1A1A1A`) |
| Título tipografía | `font-manrope font-bold text-[20px]` |
| Descripción color | `text-gray-500` (`#737373`) |
| Descripción tipografía | `font-manrope font-normal text-[14px]` |
| Descripción ancho máximo | `max-w-[420px]` |
| Gap título–descripción | `gap-2` (8px) |
| Gap texto–CTA | `gap-4` (16px) |
| CTA primario color | `#DB3B2B` (Red 500) |
| CTA ancho | `w-[300px]` (sin ilustración) / `w-[280px]` (con ilustración) |
| CTA border-radius | `10px` (hereda de `T1Button`) |
| Link secundario | `text-[14px] text-gray-500 hover:underline` |
| Padding vertical del contenedor | `py-24` (sin ilustración) / `py-16` (con ilustración) |
| Ilustración tamaño | `w-[120px]` |
| Gap ilustración–texto | `gap-10` (40px) |

---

## Anti-patrones

| ❌ Evitar | ✅ En cambio |
|---|---|
| "No hay productos" | "Aún no tienes productos" |
| "Sin datos" | Título específico al módulo |
| "Error al cargar" | Eso es un estado de error, no un empty state — ver `NOTIFICATIONS.md` |
| Botón primario en búsqueda sin resultados | Botón secundario "Limpiar filtros" |
| Agregar card/borde al empty state | El contenedor es heredado del contexto |
| Ilustración genérica para todos los módulos | Ilustración específica por módulo o sin ilustración |
| Descripción sin punto de acción ("No tienes pedidos aún.") | Descripción accionable ("Cuando recibas tu primer pedido, aparecerá aquí.") |
| CTA en módulos de historial automático | Sin CTA si el contenido se genera solo |

---

## Referencias cruzadas

- **Copy de empty states** → `content/UX-WRITING.md` §6
- **Estados de error vs empty** → `components/STATES.md`
- **Botón primario y secundario** → `components/ATOMS.md` §Buttons
- **Tipografía Manrope** → `foundation/TYPOGRAPHY.md`
- **Tokens de color** → `foundation/COLORS.md`
- **Ilustraciones** → `assets/BRAND-ASSETS.md` (cuando estén disponibles)
