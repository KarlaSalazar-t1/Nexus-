# reference-marketing-copy.md

> Reglas accionables de copy de **landing, sublandings y superficies de marketing** T1 / NEXUS V2.0.
> Versión condensada para context window de Claude.
> Fuente completa: `content/MARKETING-COPY.md`. Proceso: `workflows/COPY-WORKFLOW.md`.
> ❌ Nada de este archivo aplica a dashboard ni App — ahí manda `content/UX-WRITING.md`.

---

## Regla cardinal

| Elemento | Landing | Dashboard / App |
|---|---|---|
| Modo verbal de CTA | Imperativo tú (`Crea tu tienda gratis`) | Infinitivo (`Crear tienda`) |
| Longitud de CTA | 2–5 palabras | 1–3 palabras |
| Tabs, pestañas, filtros | Sustantivo | Sustantivo |
| Texto dentro de mockup | Sigue `UX-WRITING.md`, no este archivo | — |

---

## Longitud y puntuación

| Elemento | Longitud | Punto final |
|---|---|---|
| H1 | Máx. 8 palabras | No |
| H2 de sección | Máx. 6 palabras | No |
| H3 de bloque | Máx. 10 palabras | No |
| Subtítulo de apoyo | 1 oración, máx. 15 palabras | Sí |
| Enunciado del problema | Máx. 10 palabras | No |
| Pregunta de FAQ | Máx. 10 palabras | Signos `¿ ?`, sin punto extra |
| Respuesta de FAQ | 1–2 oraciones, máx. 30 palabras | Sí |
| `description` | 1–2 oraciones, máx. 155 caracteres | Sí |

**No-redundancia:** el subtítulo no repite palabras significativas del título ni del CTA. Si al quitarlo no se pierde información, sobra.

---

## Cifras — tabla canónica

Corte 30 jun 2026. Owners: Alonso Charbel, Felipe Caicedo, José Luis Dorantes.

| Métrica | Valor | Qué mide |
|---|---|---|
| Negocios | `+50,000` | Comercios en el ecosistema |
| Tiendas en línea | `+6 mil` | Tiendas creadas, total |
| Envíos | `+30M` | Envíos entregados |
| Transacciones | `+200M` | Transacciones procesadas |
| Paqueterías | `+10` | Paqueterías integradas |
| Tasa de aprobación | `+90%` | Aprobación en T1 Pagos |

- Cualquier cifra fuera de esta tabla → `[PENDIENTE]`. **Nunca se inventa.**
- Formato: `<1M` coma de millar · `≥1M` abreviatura `M` · porcentajes sin espacio · siempre `+` y redondeo hacia abajo.
- Coherencia de unidad dentro de una misma tira. Nunca mezclar `+40,000` con `+30M`.
- Tira de stats: las 3 cifras del mismo tipo **y** del mismo nivel (producto o ecosistema). Si no existen 3 comparables, se usan 1–2 o se quita el bloque.
- Prohibido rellenar una tira de producto con cifras del ecosistema (`+50,000 negocios`, `+200M transacciones`).
- Las cifras del hero, del contador y de los mockups son el mismo dato.
- Toda cifra vive en `constants.ts`, en un solo objeto.
- Tira de stats: las 3 cifras deben ser del mismo tipo de claim (volumen, o rendimiento, o alcance).

---

## Claims

- Mensajes de conversión o aprobación: anclados al dato duro, no al adjetivo. `+18% de conversión`, no `optimizado para conversión`.

> Todo superlativo nuevo necesita dato verificable adjunto, o se elimina.

Y aun con sustento: **si tienes la cifra, publica la cifra.** `+90% de aprobación` > `la mejor tasa de aprobación`.

- **Sin dato:** descriptivos de funcionalidad, relativos a sí mismo (`Sin mensualidad`), ausencia de fricción (`Sin tarjeta de crédito`).
- **Requieren Legal:** tasas de aprobación, tiempos de entrega garantizados, ahorro porcentual, cobertura total, comparación con competidor nombrado.

---

## CTAs

| Nivel | Patrón |
|---|---|
| Primario global | Verbo + objeto + **gratis** → `/registro` |
| Primario de sección | Verbo + beneficio de la sección |
| Secundario | **Conoce** + [producto/función] |
| Terciario | `Habla con un experto` |

**Reglas duras:**
1. Una etiqueta = un destino. Si el destino cambia, la etiqueta cambia.
2. Todo CTA que termina en `gratis` lleva a `/registro`, y ninguna otra etiqueta lleva ahí.
3. Máximo 1 CTA primario por viewport.
4. El CTA se lee solo, sin el título de la sección.
5. Sin punto final. Sentence case.
6. El CTA de cierre no repite literalmente el del hero.
7. Un set de tabs no mezcla sustantivos con imperativos.

Etiqueta nueva → se agrega a la tabla canónica de `MARKETING-COPY.md` §5. Si ya existe con otro destino, se reformula.

---

## Estructura de sublanding

`hero · enunciado del problema · solución · funcionalidades · prueba · FAQ · cierre`

**Enunciado del problema:** se escribe desde el lector, no nombra a T1 en la misma línea que el dolor, y no se recicla entre páginas.

**FAQ — regla dura:** ningún dato, cifra, promesa o término aparece por primera vez en la FAQ. Si está en la FAQ, está antes en el cuerpo con el mismo valor. 4–6 preguntas. La respuesta abre con `Sí.` / `No.` / el dato.

**Cierre:** uno por página, patrón `¿Listo para + [beneficio]?`. El copy de apoyo aporta información nueva y **declara el paso real** — si el botón dice `Programa tu recolección` y va a `/registro`, el apoyo lo dice. Sin marcos de miedo.

---

## Promesa de marca

**T1 unifica lo que hoy está separado.** Cuatro formulaciones, no intercambiables:

| Formulación | Nivel |
|---|---|
| `un solo ecosistema` | Marca — T1 completo |
| `una sola plataforma` | Producto |
| `un solo lugar` | Función concreta |
| `todo en uno` | Paquete de hardware o servicio |

> **La promesa nunca viaja sola.** Siempre nombra qué se unifica.
> Prueba: si la frase sirve igual para envíos, pagos y tienda sin cambiar una palabra, le falta el ancla.

`Reclamaciones en un solo lugar` ❌ → `Las reclamaciones de todos tus procesadores, en un solo lugar` ✅

**`Fácil y seguro` NO es muletilla** — en pagos la seguridad es diferenciador real. Se conserva. Pero donde hay dato, el dato gana.

---

## Muletillas

| Construcción | Máximo |
|---|---|
| `olvídate de…` | 1 por sitio |
| `sin complicaciones` / `cero complicaciones` / `sin fricción` | 1 por sitio |
| `los números hablan` / `números que hablan por sí solos` | 0 |

---

## Léxico

**Verbos de T1:** crea · cobra · envía · vende · conecta · gestiona · rastrea · acepta · revisa · consulta · elige · activa · programa · responde · automatiza · resuelve · detecta · bloquea · evalúa · entrega · centraliza · sincroniza · monitorea

**Verbos prohibidos:** potencia · impulsa · revoluciona · transforma · empodera · maximiza · optimiza · desbloquea · escala · digitaliza · disrumpe

**`optimizar` / `optimizado`:** solo si lleva el dato al lado en la misma frase. Sin cifra, se elimina.

**Extranjerismos:** traducir por defecto. `dashboard`→panel · `responsive`→"se ve bien en celular y computadora" (nunca "adaptable") · `checkout`→pasarela de pago/caja · `tracking`→rastreo · `hosting`→alojamiento · `insights`→información/hallazgos. Conservar contextualizados: SEO · SPEI · Fulfillment · PyME.

**Internos, no en copy de cliente:** `seller` · `contracargo` (se dice reclamación).

**Sustantivos del lector:** tu negocio · tu tienda · tus productos · tus pedidos · tus ventas · tus envíos · tus guías · tus cobros · tus clientes · tu catálogo · tus canales · tus reclamaciones

> **T1 no nombra a la persona.** Evitar `seller`, `merchant`, `comerciante`, `vendedor`, `usuario`.
> Terminología canónica: `Reclamación` (nunca `contracargo`, `chargeback`, `disputa`, `CB`) · `paquetería` (nunca `carrier`) · `clic` (nunca `click`).

**Construcciones de la casa:** enumeración de tres (`vender, cobrar y enviar`) · restricción como beneficio (`Sin mensualidad ni mínimo de envíos`) · cifra pegada al beneficio · producto al final del título (`Envía a todo México con T1 Envíos`).

---

## Marcadores de voz

- Oración corta, una idea por oración. Si hay dos comas, revisa.
- Verbo al frente: `Crea tu tienda`, no `La creación de tu tienda`.
- Segunda persona: `tu tienda`, `tus envíos`.
- Concreto sobre abstracto: `+10 paqueterías` sobre `múltiples opciones logísticas`.
- Un adjetivo por oración, y solo si aporta.
- El comerciante es el sujeto: `Crea tu tienda`, no `T1 crea tu tienda`.
- Sin marcos de miedo. `No pierdas otra venta` se reescribe en positivo.

---

## Mockups y datos de ejemplo

> El texto dentro de un mockup es UI, no marketing. Sigue `UX-WRITING.md`.

Los datos de ejemplo son copy y se revisan como copy: nombres verosímiles (`Laura Medina`, no `test lopez quiroz`), español sin excepción, estados con terminología canónica, abreviaturas expandidas (`Tasa de reclamaciones`, no `Tasa de CB`), montos con formato de moneda completo, nunca la palabra `Placeholder`.

---

## Metadata

- `title`: `[Función] · [Producto]` → `Reclamaciones · T1 Pagos`
- Cada página tiene su propia `description`. No repite el `title` ni contradice al cuerpo.
- Terminología canónica y acentuación completa — es texto que se indexa.
- Toda corrección de terminología en `description` se revisa con quien lleve posicionamiento.

---

## Antes de entregar

1. ¿Cada uso de la promesa dice **qué** se unifica?
2. ¿Alguna frase sirve igual para otro producto sin cambiar una palabra?
3. ¿Hay muletillas de §12?
4. ¿Algún adjetivo apilado?
5. ¿El sujeto es el comerciante y no T1?
6. ¿H1/H2/H3 sin punto, subtítulos con punto?
7. ¿CTAs en imperativo tú, tabs en sustantivo?
8. ¿Alguna etiqueta de CTA ya existe con otro destino?
9. ¿Toda cifra viene de la tabla canónica?
10. ¿Algún superlativo sin dato al lado?
11. ¿La FAQ introduce algo que no esté antes en el cuerpo?
12. ¿El copy de apoyo del cierre declara que hay un registro de por medio?
13. Leer la página nueva justo después de la home: ¿suenan a la misma persona?

---

## Regla de operación

> **Claude propone. Karla aprueba. La ejecución lleva la lista exacta.**

Claude nunca edita copy de marketing directamente en el repo. Ver `workflows/COPY-WORKFLOW.md`.

**La home (`/`) es la referencia de voz.** Se lee completa antes de escribir cualquier página nueva. Ninguna regla de este archivo sustituye ese paso.
