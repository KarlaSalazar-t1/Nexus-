# UX Writing — NEXUS V2.0

> El microcopy es la capa de texto que hace que una interfaz sea comprensible, confiable y humana. Este documento define las reglas y patrones de escritura para cada tipo de texto en el ecosistema T1, con ejemplos reales de la plataforma.

**Última actualización:** Agosto 2026 · **Owner:** Karla Salazar — Head of UX/UI

> **Alcance:** este documento cubre el microcopy de producto — dashboard y App. Para landing,
> sublandings y superficies de marketing, ver [`MARKETING-COPY.md`](./MARKETING-COPY.md).

---

## Resumen rápido

| Tipo de texto | Regla principal |
|---|---|
| **CTAs** | Verbo de acción + objeto. Sin punto final. |
| **Errores inline** | Descriptivo, sin culpar. Con solución cuando existe. |
| **Errores de sistema** | Explica qué pasó + qué hacer. |
| **Confirmaciones** | Conciso, positivo, en pasado o presente. |
| **Labels** | Sustantivo preciso. Sin punto final. |
| **Placeholders** | Ejemplo concreto o instrucción breve. Sin punto final. |
| **Empty states** | Contexto + acción. Motivador, no neutro. |
| **Loading states** | Específico sobre qué está ocurriendo. |
| **Destructivos** | Directo + consecuencia + alternativa si existe. |

---

## 1. CTAs (Llamadas a la acción)

Los CTAs son el texto más leído y más accionado en la interfaz. Deben ser inequívocos sobre qué ocurre al presionarlos.

### Reglas

- Siempre **verbo + objeto**. El usuario debe saber qué acción ejecuta y sobre qué.
- **Sin punto final.**
- **Solo primera letra en mayúscula** (sentence case).
- Verbos en **infinitivo** para acciones principales; **imperativo** es aceptable en contextos conversacionales.
- El texto del botón debe poder leerse independientemente del contexto visual — no depender del título de la página para tener sentido.
- **Una etiqueta, un destino.** Ninguna etiqueta de botón o enlace puede apuntar a dos rutas distintas dentro del mismo producto. Si el destino cambia, la etiqueta cambia.

> **Longitud.** El rango de 1–3 palabras (`VOICE-TONE.md` §4.4) aplica a producto. En landing el CTA
> se lee sin contexto previo y necesita cargar la promesa completa: ahí el rango es de 2 a 5
> palabras. Ver [`MARKETING-COPY.md`](./MARKETING-COPY.md) §5.

### Patrones de CTA por tipo

| Tipo | Patrón | Ejemplo |
|---|---|---|
| **Primario / Creación** | Crear + [entidad] | Crear tienda, Crear pedido |
| **Adición** | Agregar + [entidad] | Agregar producto |
| **Acción destructiva directa** | Solo verbo (en contexto claro) | Eliminar |
| **Acción destructiva global** | Eliminar + [especificador] | Eliminar productos prueba |
| **Guardar estado** | Guardar + [objeto] | Guardar cambios |
| **Cancelar cambios** | Descartar + [objeto] | Descartar cambios |
| **Expansión de opciones** | Más opciones | Más opciones |

### Tabla de CTAs del sistema

| CTA | Contexto de uso | Tipo de botón |
|---|---|---|
| Crear tienda | Alta de nueva tienda en T1 Tienda | Primario |
| Crear pedido | Creación manual de pedido | Primario |
| Agregar producto | Adición de producto al listado | Primario |
| Más opciones | Menú secundario de acciones | Secundario / Ghost |
| Eliminar | Acción destructiva directa sobre un item específico | Destructivo (danger) |
| Eliminar productos prueba | Limpieza global de productos de prueba | Destructivo (danger) |
| Guardar cambios | Confirmación de edición en formularios | Primario |
| Descartar cambios | Cancelación de edición con cambios pendientes | Secundario / Ghost |

### ✅ / ❌ Ejemplos

| ✅ Correcto | ❌ Incorrecto | Problema |
|---|---|---|
| Crear tienda | Crear una nueva tienda | Verboso innecesariamente |
| Agregar producto | + Producto | Ambiguo sin contexto |
| Guardar cambios | Guardar | Poco específico — ¿qué se guarda? |
| Descartar cambios | Cancelar | "Cancelar" puede confundirse con cancelar el proceso completo |
| Eliminar | Borrar / Remover | Inconsistente con la terminología canónica |

---

## 2. Mensajes de error

Los errores son momentos de alta fricción. El objetivo es que el usuario entienda qué salió mal y qué puede hacer para resolverlo — sin sentirse culpable ni confundido.

### Reglas generales

- **Nunca culpar al usuario.** El error sucedió, no "el usuario hizo algo mal".
- **Siempre descriptivo.** "Formato inválido" > "Error".
- **Agregar solución** cuando existe y es accionable.
- **Punto final** en mensajes que son oraciones completas.
- **Sin signos de exclamación** en errores — generan alarma innecesaria.

---

### 2.1 Errores inline (debajo del input)

Aparecen inmediatamente debajo del campo afectado. Máximo 1–2 oraciones.

| Mensaje | Contexto de uso |
|---|---|
| Formato inválido | El valor ingresado no cumple con el formato esperado (email, teléfono, URL, etc.) |
| Código erróneo | El código ingresado no coincide con el esperado |
| El código ya venció. Genera uno nuevo. | Código de verificación o descuento expirado |
| Ingresa un nombre de plantilla | Campo requerido vacío — nombre de plantilla |
| Alcanzaste el límite máximo de caracteres | El campo superó el límite permitido |
| Debe contener 10 dígitos | Formato numérico específico no cumplido (ej. teléfono MX) |

**Notas de uso:**
- El error se muestra **bajo el input**, en rojo semántico (Error `#CC0000`), tamaño `text-xs` o `text-sm`.
- Acompañado del borde del input en rojo.
- Desaparece cuando el usuario corrige el valor.

### 2.2 Errores de sistema

Aparecen como toast, banner o modal según la criticidad. Explican qué falló y qué puede hacer el usuario.

| Mensaje | Contexto | Presentación |
|---|---|---|
| Acceso restringido. Tu perfil no tiene acceso a este módulo. | Usuario sin permisos intenta acceder a una sección | Banner o modal bloqueante |
| Tu producto no pudo crearse. Inténtalo más tarde. | Error del servidor al crear un producto | Toast error |
| Tu pago no pudo ser procesado. Comunícate con tu banco. | Fallo en pasarela de pago | Modal o banner crítico |

**Notas de uso:**
- Usar **voz activa**: "Tu producto no pudo crearse" — no "El producto no fue creado".
- Cuando el error tiene solución del lado del sistema (reintentar), incluir CTA de reintento.
- Cuando el error requiere acción externa (banco, soporte), indicarlo claramente.

### 2.3 Errores de conexión

| Mensaje | Contexto |
|---|---|
| No tienes conexión. Verifica el estado e intenta nuevamente. | Sin internet o servidor inaccesible |

**Notas de uso:**
- Mostrar como **banner persistente** en la parte superior de la pantalla, no como toast (que desaparece).
- Incluir botón "Reintentar" cuando aplique.
- Desaparece automáticamente cuando se restablece la conexión.

---

## 3. Mensajes de confirmación y éxito

Las confirmaciones cierran el loop de una acción. Deben ser concisas, positivas y específicas sobre qué se completó.

### Reglas

- **Pasado reciente** para acciones completadas: "Creaste un producto con éxito."
- **Presente** para estados resultantes: "Tu tienda está lista para vender."
- **Sin exceso de entusiasmo.** Un solo mensaje positivo, sin signos de exclamación múltiples.
- **Punto final** en oraciones completas.
- Presentación: **toast** para confirmaciones simples; **modal** o **banner** para procesos críticos o de alta importancia.

### Tabla de mensajes de éxito

| Mensaje | Acción que confirma | Presentación |
|---|---|---|
| Tu tienda está lista para vender. | Configuración inicial de tienda completada | Banner celebratorio / modal de hito |
| Creaste un producto con éxito. | Alta de un nuevo producto | Toast success |
| Proceso finalizado. Exportación completa. | Exportación de datos terminada | Toast success o banner |

### ✅ / ❌ Ejemplos

| ✅ Correcto | ❌ Incorrecto | Problema |
|---|---|---|
| Creaste un producto con éxito. | ¡El proceso de creación de tu producto ha sido completado exitosamente! | Verboso y excesivo |
| Tu tienda está lista para vender. | Operación completada. | Frío, genérico, sin contexto |
| Proceso finalizado. Exportación completa. | OK | No comunica qué ocurrió |

---

## 4. Labels de formulario

Los labels son la identidad de cada campo. Deben ser precisos, consistentes y nunca ambiguos.

### Reglas

- **Sustantivo o frase nominal.** Sin verbos.
- **Sin punto final.**
- **Solo primera letra en mayúscula** (sentence case).
- **Consistentes** con la terminología canónica del sistema (ver [GLOSSARY.md](../GLOSSARY.md)).
- **No abreviar** a menos que sea terminología estándar del sector.

### Labels del sistema

| Label | Contexto de uso |
|---|---|
| Nombre del producto | Campo de nombre en formulario de producto |
| Código de barras (EAN, ISBN, UPC, GTIN) | Campo de identificador de producto con paréntesis explicativo |
| Etiquetas | Campo de tags o categorías |
| Correo electrónico | Campo de email en autenticación y perfil |
| Contraseña | Campo de contraseña en autenticación |

**Nota:** El label "Código de barras" incluye entre paréntesis los formatos estándar aceptados — esto es un patrón de helper text integrado al label, no una descripción adicional.

---

## 5. Placeholder text

Los placeholders son sugerencias visuales dentro del campo vacío. Desaparecen al escribir.

### Reglas

- **Nunca reemplazar el label.** El placeholder es un complemento, no el identificador del campo.
- **Ejemplo concreto o instrucción muy breve.**
- **Sin punto final.**
- **Tono:** neutro-instructivo, nunca imperativo fuerte.
- **No usar "Escribe aquí..." o "Ingresa..."** — prefiere el ejemplo directo.

### Placeholders del sistema

| Placeholder | Campo asociado | Por qué funciona |
|---|---|---|
| `Almacén Central` | Nombre de sucursal / ubicación | Ejemplo concreto y reconocible |
| `maria.gonzalez@ejemplo.com` | Correo electrónico | Formato claro con dominio de ejemplo |
| `Selecciona una opción` | Dropdowns y selects | Instrucción neutra sin implicar que hay una opción predeterminada |
| `Buscar por cliente o dirección` | Barra de búsqueda en pedidos / envíos | Especifica los criterios de búsqueda disponibles |

### ✅ / ❌ Ejemplos

| ✅ Correcto | ❌ Incorrecto | Problema |
|---|---|---|
| `Almacén Central` | `Ingresa el nombre de tu sucursal` | Verboso; el label ya dice qué va ahí |
| `Selecciona una opción` | `- Selecciona -` | Guiones decorativos son innecesarios |
| `Buscar por cliente o dirección` | `Buscar...` | Demasiado vago — no especifica los criterios |

---

## 6. Empty states (Estados vacíos)

Los empty states son oportunidades de orientar y motivar, no solo de informar que no hay datos.

### Estructura recomendada

```
[Ilustración o ícono contextual]
[Título: Qué falta y por qué importa]
[Descripción: Qué puede hacer el usuario para resolverlo]
[CTA opcional: Acción directa]
```

### Reglas

- **El título** describe la ausencia con contexto, no solo el estado vacío. "Aún no tienes productos" > "Sin productos".
- **La descripción** es accionable: dice qué hacer, no solo que no hay nada.
- **Tono:** orientador y motivador. Nunca neutral en exceso ni alarmista.
- **CTA** cuando existe una acción clara que el usuario puede tomar desde ahí.

### Empty states del sistema

**Dirección de origen (T1 Envíos)**

> **Título:** Aún no cuentas con una dirección de origen.
> **Descripción:** Antes de realizar tu primer envío, necesitamos saber desde dónde se enviarán tus paquetes.
> **CTA sugerido:** Agregar dirección de origen

**Productos (T1 Tienda)**

> **Título:** Aún no tienes productos.
> **Descripción:** Empieza a cargar tus productos — puedes hacerlo de manera masiva o individual.
> **CTA sugerido:** Agregar producto

### Patrón general para nuevos empty states

| Contexto | Patrón de título | Patrón de descripción |
|---|---|---|
| Primera vez en módulo | "Aún no tienes [entidad]." | "Cuando [evento], aparecerá aquí." o "Empieza [acción]." |
| Búsqueda sin resultados | "No encontramos resultados para '[término]'." | "Intenta con otros términos o revisa los filtros aplicados." |
| Filtros activos sin resultados | "Nada coincide con tus filtros." | "Ajusta los filtros o elimínalos para ver todos los resultados." |
| Error de carga | "No pudimos cargar [entidad]." | "Intenta recargar la página. Si el problema persiste, contáctanos." |

---

## 7. Loading states (Estados de carga)

Los mensajes de carga comunican que el sistema está trabajando. Reducen la percepción de espera cuando son específicos.

### Reglas

- **Específico sobre qué está ocurriendo.** "Descargando CSV" > "Cargando..."
- **Gerundio** (acción en progreso): "Analizando", "Descargando", "Cargando".
- **Sin punto final** en mensajes cortos de loading.
- Para procesos con IA, mencionar que está en curso para establecer expectativas de tiempo.
- **Puntos suspensivos** (`...`) son aceptables en loading text para indicar progreso.

### Loading states del sistema

| Mensaje | Contexto | Duración estimada |
|---|---|---|
| Descargando CSV... | Exportación de datos a archivo CSV | Segundos a minutos |
| Analizando con IA... | Proceso de análisis automático con inteligencia artificial | Variable — puede ser lento |
| Cargando archivo... | Upload de archivo en proceso | Segundos |

### Patrón para procesos largos

Para procesos que pueden tardar más de 10 segundos, agregar contexto de tiempo o progreso:

```
Analizando con IA...
Esto puede tardar unos minutos.
```

---

## 8. Confirmaciones destructivas

Las acciones irreversibles (eliminar, inactivar, revocar) requieren un modal de confirmación. El objetivo es que el usuario tome la decisión con información completa — sin alarmismo, sin ambigüedad.

### Estructura del modal destructivo

```
[Título: Pregunta directa]
[Descripción: Consecuencia + alternativa si existe]
[CTA secundario: Cancelar]
[CTA primario destructivo: [Verbo acción] (danger/red)]
```

### Reglas

- **El título es una pregunta directa.** No un aviso: "¿Estás seguro que deseas eliminar...?" confirma que el usuario es el agente de la acción.
- **La descripción explica la consecuencia real.** "Esta acción es irreversible" es más claro que "No se puede deshacer".
- **Cuando existe una alternativa** (ej. pausar en vez de eliminar), mencionarla en la descripción — esto reduce eliminaciones accidentales.
- **El CTA destructivo** usa el mismo verbo que la acción: "Eliminar", "Inactivar", "Revocar".
- **Sin signos de exclamación.** La gravedad se comunica con claridad, no con urgencia tipográfica.

### Confirmaciones destructivas del sistema

**Eliminar productos seleccionados**

> **Título:** ¿Estás seguro que deseas eliminar los productos seleccionados?
> **Descripción:** Ten en cuenta que esta acción es irreversible. Si no quieres que aparezcan en tus canales de venta temporalmente, puedes pausarlos desde el submenú.
> **CTA cancelar:** Cancelar
> **CTA confirmar:** Eliminar productos

**Eliminar rol**

> **Título:** ¿Seguro que deseas eliminar este rol?
> **Descripción:** Esta acción no se puede deshacer. Al eliminar el rol, se perderán todos los permisos asignados a él.
> **CTA cancelar:** Cancelar
> **CTA confirmar:** Eliminar rol

**Inactivar sucursal**

> **Título:** ¿Estás seguro que deseas inactivar esta sucursal?
> **Descripción:** Puedes volver a activarla cuando lo desees.
> **CTA cancelar:** Cancelar
> **CTA confirmar:** Inactivar sucursal

**Nota:** La confirmación de inactivar sucursal tiene tono más ligero porque la acción es **reversible** — se refleja en la descripción tranquilizadora y en que no hay advertencia de irreversibilidad.

### Escala de severidad en destructivos

| Tipo de acción | Reversible | Tono de descripción | Ejemplo de consecuencia |
|---|---|---|---|
| **Eliminar** (permanente) | ❌ No | Claro sobre consecuencias | "Esta acción es irreversible." |
| **Inactivar** | ✅ Sí | Tranquilizador | "Puedes volver a activarla cuando lo desees." |
| **Revocar acceso** | ✅ Condicional | Informativo | "El usuario perderá el acceso hasta que se le reasigne un rol." |
| **Cancelar proceso** | ✅ Parcial | Contextual | "Se perderán los cambios no guardados." |

---

## 9. Helper text

El helper text aparece debajo del label o campo para dar contexto adicional antes de que el usuario interactúe.

### Reglas

- Se usa cuando el campo puede generar duda sobre su formato, restricciones o propósito.
- **Máximo 1 oración.**
- **Punto final** si es oración completa.
- Desaparece o cambia a mensaje de error cuando hay validación fallida.

### Ejemplos de helper text

| Campo | Helper text |
|---|---|
| Código de barras | Acepta formatos EAN, ISBN, UPC y GTIN. |
| Contraseña (creación) | Mínimo 8 caracteres, incluye una mayúscula y un número. |
| Etiquetas | Presiona Enter para agregar cada etiqueta. |
| Precio | El precio se mostrará en MXN a tus compradores. |

---

## Referencias

- [VOICE-TONE.md](./VOICE-TONE.md) — Personalidad de marca, principios de voz y tono
- [MARKETING-COPY.md](./MARKETING-COPY.md) — Copy de landing y superficies de marketing
- [foundation/PRINCIPLES.md](../foundation/PRINCIPLES.md) — Principio de Tecnología Humanizada
- [GLOSSARY.md](../GLOSSARY.md) — Terminología canónica del ecosistema T1
- [patterns/NOTIFICATIONS.md](../patterns/NOTIFICATIONS.md) — Cuándo usar toast vs banner vs modal
- [patterns/EMPTY-STATES.md](../patterns/EMPTY-STATES.md) — Layouts y composición de estados vacíos
- [components/STATES.md](../components/STATES.md) — Estados de componentes (disabled, error, loading)
