# reference-app.md

> Tokens y patrones exclusivos de la **app móvil nativa** de T1 (iOS/Android).
> Versión condensada para context window de Claude.
> Fuente completa: `plataform/APP.md` (tokens), `patterns/APP-FLOWS.md` (flujos).
> ❌ Nada de este archivo aplica en dashboard/admin ni en landing pages.

---

## Regla cardinal

| Token | App | Dashboard | Landing |
|---|---|---|---|
| Tipografía | Inter (todo, salvo Nova bajo evaluación) | Manrope | Sora + Inter |
| Superficie | Mobile-first fijo, sin breakpoints desktop | Responsive `360px`–`1600px`+ | Responsive `360px`–`1220px` |
| Rojo primario | `#DB3B2B` | `#DB3B2B` | `#E26153` |
| Pressed/active | `#CC0000` | `#CC0000` (hover) | N/A |
| Border radius botón primario | `16px` | `8px` | `18px` |
| Border radius cards | `12px`–`20px` (sin escala cerrada) | `10px`/`20px` | `24px` |
| Altura botón primario | `48px` | `35px` | `45px` |
| Navegación | Tab bar + FAB + bottom sheets | Sidebar fijo | Header sticky |

> ❌ Manrope en la App fuera de Nova es siempre anomalía — auditar el componente compartido en origen, no la pantalla.

---

## Tipografía (Inter — exclusiva)

**Familia única: Inter.** Manrope prohibida fuera de Nova (chat IA, bajo evaluación).

| Token | Tamaño | Pesos | Uso |
|---|---|---|---|
| T1 | `24px` | SemiBold 600 | Título de paso/pantalla |
| B1 | `16px` | Regular 400 · Medium 500 · SemiBold 600 | Cuerpo destacado, tarjetas de opción |
| B2 | `14px` | Regular 400 · Medium 500 · SemiBold 600 | Cuerpo estándar, labels, botones, inputs |
| B3 | `12px` | Regular 400 · Medium 500 · SemiBold 600 | Captions, helper text, metadata, chips |

### Colores de texto

| Rol | Hex | Uso |
|---|---|---|
| Primary | `#4C4C4C` | Texto secundario, subtítulos |
| Texto principal | `#000000` | Valores, títulos de card |
| Disabled | `#9CA3AF` | Texto deshabilitado |
| Inverse | `#FFFFFF` | Texto sobre botón primario |
| Placeholder | `#A3A3A3` / `#C3C3C3` | Placeholders de input |
| Accento IA (Nova) | `#7C3AED` | Acentos y CTA de funciones de IA |

---

## Estructura de pantalla

```
┌─────────────────────────┐
│ Status bar (50px)       │
├─────────────────────────┤
│ Header (título + back)  │
│                          │
│ Contenido                │
│ margen lateral 16px      │
│ (ancho útil 328px)       │
│                          │
├─────────────────────────┤
│ Tab bar + FAB (86px)     │
│ Home indicator           │
└─────────────────────────┘
```

| Token | Valor |
|---|---|
| Mockup base | `360×780` |
| Margen lateral | `16px` |
| Área táctil mínima | `44px` |
| Tarjeta de opción (alto) | `64px` |
| Botón (alto) | `48px` |
| Contenedor de ícono | `40×40` |
| Tab bar | `86px`, píldora `260×56` |

---

## Botones

| Propiedad | Primario | Secundario |
|---|---|---|
| Background | `#DB3B2B` | `#FFFFFF` / `#F8F8F8` |
| Texto | `#FFFFFF` B2 S | `#4C4C4C` B2 S |
| Border | ninguno | `1px #F3F3F3` |
| Radius | `16px` | `16px` |
| Alto | `48px` | variable (~`51px` social) |
| Pressed | `#CC0000` | `#F2F2F2` |
| Disabled | bg `#F3F3F3`, texto `#9CA3AF` | border `#E5E5E5`, texto `#A3A3A3` |

Variante IA/Nova: sin fondo/borde, texto `#7C3AED` + ícono `ai-magic`.

---

## Border radius y sombras

> ⚠️ Sin escala cerrada — usar como diagnóstico, no receta fija.

| Radio | Uso típico |
|---|---|
| `20px` | Inputs, textareas |
| `16px` | Tarjetas de opción, botón primario |
| `12px` | Cards, popups, contenedores generales (el más frecuente) |
| `10px`–`13px` | Cards secundarias, contenedores de ícono |
| `8px` | Botones internos de popups/modales |
| `6px` | Chips de estado/motivo |
| `4px` | Badges |

Overlay de modal/sheet: `rgba(0,0,0,0.4)`. Sombra de card flotante: `0 3.66px 21.88px rgba(0,0,0,0.1)` (no reusar la sombra de Dashboard).

---

## Colores semánticos

| Rol | Hex | Estado |
|---|---|---|
| Primario / CTA | `#DB3B2B` | ✅ estable |
| Fondo de selección | `#FFF0EF` | ✅ estable |
| Éxito | `#4FC153` o `#51AF70` | 🔴 dos verdes compitiendo, sin token único |
| Error (input) | `#CC0000` / `#DB3B2B` / `#DB362B` | 🔴 tres rojos compitiendo, sin token único |
| IA/Nova fuerte | `#7C3AED` | 🔴 numeración de escala invertida |
| Advertencia fuerte | `#FF6700` | 🔴 numeración de escala invertida |
| Disabled texto | `#9CA3AF` | ✅ estable |
| Border default | `#F3F3F3` | ✅ estable |

---

## Componentes clave

**Tarjeta de opción seleccionable:** default `bg white` / border `#F3F3F3` / r16 / h64 — seleccionada `bg #FFF0EF` / border `#DB3B2B` + check 20px.

**Chip de sugerencia:** r11, variante IA `bg #F5EFFF` texto `#7C3AED` SemiBold 12; variante normal `bg #F8F8F8` texto negro Regular 12.

**Modal de confirmación:** ícono en círculo + título + cuerpo + [Cancelar] [acción primaria]. Ícono corresponde a la acción, nunca heredado de otro flujo. CTA afirmativo nombra la acción ("Sí, devolver", no "Sí, confirmar" salvo que no haya verbo propio).

**Bottom sheet:** header (título + cerrar) + contenido + CTA full-width fijo; sube con el teclado nativo en captura de texto.

**Confirmación de tareas de setup (Home):** siempre retorna al Home completo + animación de confeti — nunca un banner de éxito adicional. El estado de la tarjeta completada (desaparece / se mueve al final / permanece) varía por flujo, sin regla canónica aún.

**Toast:** píldora flotante sobre la tab bar, usada en flujos de creación que no tienen pantalla de éxito dedicada (ej. Agregar producto).

**Wizard con stepper:** indicador "PASO N/M" + barra de progreso; navegación lineal con atrás/siguiente; CTA deshabilitado hasta que la sección actual es válida.

**Wizard acordeón** (alternativa al stepper, ej. Crear recolección): secciones que progresan atenuada → activa → completada (colapsa a resumen); solo la sección activa muestra sus campos.

**Regla de confirmación (R4):** acciones reversibles guardan directo, sin modal. Acciones irreversibles o de plazo largo requieren confirmación.

---

## Patrones de flujo

### 1. Formulario de setup (Home → tarea → Home)

```
[Home] (tarjeta de setup)
   ↓
[Formulario / modal de la tarea]
   │ Guardar / Descartar
   ↓
[Home + confeti]
```

Usado en: agregar dirección, tarifas de envío, activar pagos, nombre de tienda, dominio, redes sociales, políticas. Ver `patterns/APP-FLOWS.md` §6–12.

### 2. Listado → detalle → menú de acciones

```
[Listado] (buscador + filtros + tarjetas)
   ↓ tap tarjeta
[Detalle] (header + bloques + menú "···")
   ↓ tap acción
[Mini-flujo de la acción] (modal / sheet / pantalla completa)
   ↓
[Detalle actualizado]
```

Usado en: Pedidos, Productos, Envíos, Incidencias. Ver `patterns/APP-FLOWS.md` §13–14, §17, §24, §26.

### 3. Wizard multi-paso con confirmación

```
[Paso 1/N] → [Paso 2/N] → ... → [Resumen]
   ↓ CTA final
[Modal de confirmación] → [Éxito / Toast]
```

Usado en: Crear pedido, Agregar producto, Crear envío, Reportar incidencia. Ver `patterns/APP-FLOWS.md` §15, §18, §24, §27.

### 4. Paywall / gating por plan

```
[Acción que requiere plan] → [Modal de planes] (Gratis · Básico · Avanzado)
   → usuario elige plan de pago → función desbloqueada
```

Componente reutilizado en dominio personalizado, redes sociales (burbuja WhatsApp) y otras features premium. Ver `patterns/APP-FLOWS.md` §10.

---

## Reglas generales

| Regla | Valor |
|---|---|
| Familia tipográfica | Inter exclusivo (R3) — Manrope fuera de Nova es siempre anomalía |
| Confirmación | Reversible = directo; irreversible/plazo largo = modal (R4) |
| CTA afirmativo | Nombra la acción, no "Sí, confirmar" salvo sin verbo propio (R5) |
| Escala de color | Número mayor = más oscuro (R6) — Orange/Purple/Blue hoy invertidos |
| Ancho de texto | Nunca ancho fijo en nodos con texto variable (R2) |
| Valores decimales | Nunca token — son escalado horneado, redondear al origen (R1) |
| Ícono de confirmación | Corresponde a la acción, nunca heredado (R8) |
| Mensaje de validación | Uno solo por condición, sin importar el tipo de control (R7) |
