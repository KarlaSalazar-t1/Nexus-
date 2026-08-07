# Marketing Copy — NEXUS V2.0

> `UX-WRITING.md` cubre el microcopy de producto: errores, labels, empty states, confirmaciones. Nada de eso existe en una landing. Este documento cubre lo contrario: el copy de conversión — headlines, cifras, claims, testimoniales y jerarquía de CTA.

**Estado:** 🟢 v1.3 — sin decisiones bloqueantes
**Última actualización:** Agosto 2026 · **Owner:** Karla Salazar — Head of UX/UI

---

## Alcance

| Aplica a | No aplica a |
|---|---|
| Landing principal y sublandings | Dashboard y App |
| Páginas de producto (`/productos/*`) | Copy dentro de mockups de producto (ver §7) |
| Precios, casos de éxito, partners | Emails transaccionales |
| Blog (headlines y metadatos) | Centro de ayuda |

La **voz** es la misma en todas las superficies — ver `VOICE-TONE.md` §2. Lo que cambia aquí es el **tono** y el **modo verbal**.

---

## Resumen rápido

| Tipo de texto | Regla principal |
|---|---|
| **H1** | Máx. 8 palabras. Sin punto. Beneficio, no producto. |
| **H2 de sección** | Máx. 6 palabras. Sin punto. |
| **Subtítulo de apoyo** | 1 oración, máx. 15 palabras, con punto. No repite el H2. |
| **CTA primario** | Imperativo tú. Sufijo "gratis" si va a registro. |
| **CTA secundario** | Patrón fijo: Conoce + [producto/función]. |
| **Cifras** | Numeral siempre. Una sola fuente de verdad. |
| **Claims comparativos** | Todo superlativo necesita dato o desaparece. |
| **Testimoniales** | Métrica + descriptor + cita + atribución. |
| **FAQ** | La respuesta abre con la respuesta. Nunca introduce un dato nuevo. |
| **Bloque de cierre** | Uno por página. El apoyo declara a dónde lleva el botón. |
| **Metadata** | Una description por página. Terminología canónica. |
| **Voz** | La promesa de marca nunca viaja sola. Sin muletillas. |
| **Antes de escribir** | Leer la home. Es la referencia canónica. |

---

## 1. Headlines y subheads

### Reglas

| Elemento | Longitud | Punto final | Contenido |
|---|---|---|---|
| **H1** | Máx. 8 palabras | No | El beneficio para el usuario, no el nombre del producto |
| **H2 de sección** | Máx. 6 palabras | No | Qué resuelve esa sección |
| **H3 de bloque** | Máx. 10 palabras | No | Puede nombrar el producto: "Envía a todo México con T1 Envíos" |
| **Subtítulo de apoyo** | 1 oración, máx. 15 palabras | Sí | Información nueva — nunca parafrasea el título |

### Regla de no-redundancia

El subtítulo no puede repetir palabras significativas del título ni del CTA. Si al quitar el subtítulo no se pierde información, el subtítulo sobra.

| ❌ Incorrecto | Problema |
|---|---|
| **¿Listo para hacer crecer tu negocio?** / Comienza gratis y haz crecer tu negocio con T1. / `[Comenzar ahora]` | "hacer crecer tu negocio" 2×; el subtítulo solo repite el botón |

| ✅ Correcto |
|---|
| **¿Listo para hacer crecer tu negocio?** / Vende, cobra y envía desde un solo lugar. Sin tarjeta de crédito. / `[Comienza gratis]` |

### Interrogativos

Los H2 en pregunta llevan signos de apertura y cierre y **no** llevan punto adicional. Se reservan para secciones de cierre y selectores de audiencia — máximo 2 por página.

---

## 2. Cifras y social proof

### Fuente de verdad

**Owners:** Alonso Charbel · Felipe Caicedo · José Luis Dorantes
**Fecha de corte:** 30 de junio de 2026

Estos son los únicos valores publicables:

| Métrica | Valor canónico | Qué mide |
|---|---|---|
| Negocios | `+50,000` | Comercios en el ecosistema, todos los productos |
| Tiendas en línea | `+6 mil` | Tiendas creadas, total — no solo las de IA |
| Envíos | `+30M` | Envíos entregados |
| Transacciones | `+200M` | Transacciones procesadas, total |
| Paqueterías | `+10` | Paqueterías integradas |
| Tasa de aprobación | `+85%` | Aprobación en T1 Pagos |

Cualquier cifra que no esté en esta tabla se marca `[PENDIENTE]` y se consulta con los owners antes
de publicarse. Las cifras se revisan cada cierre de trimestre.

**Negocios (+50,000) y tiendas (+6 mil) no se contradicen:** miden cosas distintas. Un comercio puede
usar T1 Envíos o T1 Pagos sin tener tienda en línea. No se presentan juntos sin descriptor que los
distinga.

- Toda cifra de social proof vive en `constants.ts` en un único objeto. **Nunca se escribe el mismo número en dos componentes.**
- El MD registra la cifra vigente, su fecha y su origen. Si el número no tiene origen declarado, no se publica.

### Formato

| Rango | Formato | Ejemplo |
|---|---|---|
| < 1,000,000 | Coma de millar | `+50,000` |
| ≥ 1,000,000 | Abreviatura M | `+30M` |
| Montos | Símbolo + abreviatura | `+$1,000M` |
| Porcentajes | Sin espacio | `98%`, `−40%` |
| Tiempo en claims | Numeral | `1 minuto`, no "un minuto" |
| Cantidades en claims | Numeral con `+` | `+10 paqueterías` |

### Reglas

- **Redondeo hacia abajo**, siempre con `+` al frente. Nunca cifras exactas que envejezcan mal.
- **Coherencia de unidad dentro de una misma tira**: si un elemento usa `M`, todos usan `M`. Prohibido mezclar `+40,000 envíos` con `+30M transacciones` en la misma línea.
- Las cifras del hero, del contador de "Nuestros números" y de cualquier mockup **son el mismo dato**. Si difieren, hay un bug de contenido.
- Los contadores animados (count-up) son exclusivos de landing — prohibidos en dashboard (`DASHBOARD.md`).

### Tiras de stats

Bloque de 3 cifras con descriptor, usado bajo el hero de varias sublandings.

**Las tres cifras deben ser del mismo tipo de claim.** No se mezcla una métrica de volumen con
una de tiempo con un conteo de funcionalidades — no son comparables y la tira pierde sentido.

| ❌ Actual (`/tienda-con-ia`) | Problema |
|---|---|
| `+6 mil tiendas creadas` · `<1 min` · `+5 métodos` | Volumen + tiempo + inventario de features. Tres unidades incomparables |

| ✅ Correcto |
|---|
| Tres métricas de volumen, o tres de rendimiento, o tres de alcance |

- Formato: cifra grande + descriptor de máx. 4 palabras.
- El descriptor no repite la unidad que ya está en la cifra: `+30M` / `envíos entregados`, no `+30M` / `millones de envíos`.
- Abreviaturas expandidas: `menos de 1 min`, no `<1 min`.

#### La tira no se rellena

> **Si no existen 3 cifras del mismo tipo y del mismo nivel, no se fuerza la tira.** Se usan 1 o 2,
> o se quita el bloque.

Dos condiciones, no una:

| Condición | Qué significa |
|---|---|
| **Mismo tipo** | Las tres son de volumen, o las tres de rendimiento, o las tres de alcance. No se mezcla volumen con tiempo con inventario de features |
| **Mismo nivel** | Las tres son del producto, o las tres del ecosistema. No se mezclan |

**Prohibido rellenar con cifras globales del ecosistema** —`+50,000 negocios`, `+200M transacciones`—
en la página de un solo producto. La cifra del ecosistema en una página de producto no prueba nada
sobre ese producto: infla el bloque y le resta credibilidad a las cifras que sí son suyas.

Una tira de dos cifras propias es más fuerte que una de tres donde la tercera está de relleno.

---

## 3. Claims y lenguaje comparativo

Los claims comparativos vigentes del sitio **ya fueron revisados y aprobados por Legal (ago 2026)**.
No requieren cambio. Lo que sigue aplica a copy nuevo.

En México la publicidad comparativa necesita sustento (LFPC art. 32), así que todo superlativo nuevo
pasa por la misma revisión antes de publicarse.

### Regla

> **Todo superlativo nuevo necesita un dato verificable adjunto, o se elimina.**

Y aun con sustento: si tienes la cifra, publica la cifra. `+85% de aprobación` convence más que
`la mejor tasa de aprobación`, porque el superlativo lo puede escribir cualquiera.

| Superlativo | Alternativa con dato |
|---|---|
| `con la mejor tasa de aprobación` | `con +85% de aprobación` |
| `al mejor precio` | `a tarifas negociadas por volumen` |
| `las mejores tarifas del mercado` | `sin mensualidad ni mínimo de envíos` |

### Mensajes de conversión y aprobación

Cuando el mensaje sea sobre **conversión** o **tasa de aprobación**, va anclado al dato duro, no al
adjetivo.

| ❌ Adjetivo vago | ✅ Anclado al dato |
|---|---|
| `Optimizado para conversión` | `+18% de conversión` |
| `La mejor tasa de aprobación` | `+85% de aprobación` |
| `Checkout que convierte más` | `Pasarela con +18% de conversión` |

**El mensaje se conserva; lo que cambia es que va respaldado.** No se trata de dejar de prometer
conversión: se trata de probarla. Si la cifra no está en la tabla canónica de §2, se marca
`[PENDIENTE]` y se consulta con los owners antes de publicar.

### Claims permitidos sin dato

- Descriptivos de funcionalidad: "Vende en línea y en marketplaces desde un solo lugar"
- Relativos a sí mismo: "Sin mensualidad ni mínimo de envíos"
- De ausencia de fricción: "Sin tarjeta de crédito", "Sin experiencia técnica"

### Claims que requieren revisión legal

Cualquier mención de: tasas de aprobación, tiempos de entrega garantizados, ahorro porcentual, cobertura geográfica total, o comparación explícita con un competidor nombrado.

---

## 4. Testimoniales y casos de éxito

### Estructura

```
[Métrica destacada]        ← cifra grande, sin oración
[Descriptor]               ← qué significa la métrica, máx. 8 palabras
"[Cita]"                   ← comillas tipográficas, 1–2 oraciones
[Nombre] · [CARGO] | [EMPRESA]
```

### Reglas

- **Métrica primero.** El lector escanea el número antes que la cita.
- La cita **no repite** la métrica del descriptor con las mismas palabras.
- Comillas tipográficas (`" "`), nunca rectas.
- La cita se transcribe literal. Si necesita edición, se marca con corchetes.
- **Cargo en mayúsculas** — excepción documentada a `VOICE-TONE.md` §4.2: funciona como etiqueta visual, no como texto corrido.
- Nombre en sentence case, empresa en mayúsculas.

### Variante institucional

Cuando no hay persona atribuible, la cita es de T1 sobre el cliente y **no lleva comillas**:

```
[Métrica]
[Descriptor]
[Párrafo descriptivo del caso, en tercera persona, máx. 30 palabras]
```

**Casos actuales en esta variante:** Casa de Toño y Telcel. Su texto lo escribe T1 en tercera persona
sobre el cliente, así que **no lleva comillas** — ponerlas presentaría como cita algo que el cliente
no dijo. Los otros cinco casos sí son citas atribuidas y conservan comillas y persona.

---

## 5. Jerarquía de CTA

### Tipos

| Nivel | Función | Modo verbal | Patrón |
|---|---|---|---|
| **Primario global** | Conversión a registro | Imperativo tú | Verbo + objeto + **gratis** |
| **Primario de sección** | Conversión contextual | Imperativo tú | Verbo + beneficio de la sección |
| **Secundario** | Navegación a producto | Imperativo tú | **Conoce** + [producto/función] |
| **Terciario** | Contacto comercial | Imperativo tú | Habla con un experto |

### Reglas duras

1. **Una etiqueta = un destino.** Ninguna etiqueta puede apuntar a dos rutas distintas en la misma landing.
2. **Todo CTA que termina en "gratis" lleva a `/registro`.** Ninguna otra etiqueta lleva ahí.
3. **Máximo 1 CTA primario por viewport.** Nunca dos primarios compitiendo en el mismo bloque.
4. El texto del CTA se lee solo: debe tener sentido sin el título de la sección.
5. Sin punto final. Sentence case.

### Modo verbal — diferencia con producto

| Superficie | Modo | Ejemplo |
|---|---|---|
| **Landing** | Imperativo tú | Crea tu tienda gratis |
| **Dashboard / App** | Infinitivo | Crear tienda |

Fundamento: `VOICE-TONE.md` §1.5 — *"Preferimos 'Crea tu primera tienda' sobre 'Comenzar proceso de alta'."* El imperativo pone al usuario en control; en producto, el infinitivo describe la operación de forma neutra.

### Etiquetas de navegación interna (tabs, pestañas, filtros)

Un tab **no es un CTA**. El CTA promete una acción; el tab nombra un destino dentro de la misma
página. Por eso no comparten modo gramatical.

| Elemento | Modo | Ejemplo |
|---|---|---|
| CTA | Imperativo tú | `Crea tu tienda gratis` |
| Tab / pestaña / filtro | **Sustantivo** | `Tienda en línea`, `Checkout`, `Rastreo` |

La regla aplica a los dos niveles de tabs. Un mismo set de tabs no puede mezclar sustantivos con
imperativos: `Catálogo` · `Checkout` · `Conecta canales` es incorrecto — el tercero rompe la serie.

**Una etiqueta por tab.** Si el código guarda un nombre y la interfaz muestra otro, la interfaz manda
y el código se alinea. No se mantienen dos juegos de nombres para el mismo elemento.

### Tabla canónica de CTAs de landing

| Etiqueta | Destino | Nivel | Estado |
|---|---|---|---|
| Comienza gratis | `/registro` | Primario global | ✅ en producción |
| Crea tu tienda gratis | `/registro` | Primario de sección | ✅ |
| Crea tu cuenta gratis | `/registro` | Primario de sección | ✅ |
| Empieza a cobrar gratis | `/registro` | Primario de sección | ✅ |
| Empieza a enviar gratis | `/registro` | Primario de sección | ✅ |
| Empieza gratis sin tarjeta | `/registro` | Primario de mega-menú | ✅ |
| Iniciar sesión | `/login` | Nav | ✅ |
| Ver planes | `/precios` | Secundario | ⚠️ propuesto — hoy el card PyME dice `Empezar ahora` y va a `/registro` |
| Habla con un experto | `/contacto-ventas` | Terciario | ✅ |
| Conoce T1 Tienda / T1 Pagos / T1 Envíos / T1 POS | `/productos/*` | Secundario | ✅ |
| Conoce los reportes | `/productos/t1tienda/reportes` | Secundario | ✅ |
| Crea tu tienda con IA | `/productos/t1tienda/tienda-con-ia` | Primario de sección | ✅ |
| Conoce los links de pago | `/productos/t1pagos/links-de-pago` | Secundario | ⚠️ propuesto — hoy dice `Empezar a cobrar` (infinitivo) |
| Conoce la multipaquetería | `/productos/t1envios/multipaqueteria` | Secundario | ⚠️ propuesto — hoy dice `Cotizar envío` (infinitivo) |

Al agregar un CTA nuevo, se agrega aquí. Si la etiqueta ya existe con otro destino, no se agrega — se reformula.

### Excepción a la longitud de CTA

`VOICE-TONE.md` §4.4 fija `Botón / CTA: 1–3 palabras`. Esa regla está calibrada para producto, donde el
botón acompaña a un contexto ya establecido. En landing el CTA se lee solo y necesita cargar la
promesa completa. **Longitud de CTA en landing: 2–5 palabras.**

---

## 6. Copy de segmentación de audiencia

Los selectores de audiencia son la **única** superficie de T1 donde se escribe en primera persona del usuario.

| Superficie | Persona gramatical | Ejemplo |
|---|---|---|
| Selector de audiencia | **Primera persona del usuario** | "Soy emprendedor", "Tengo una PyME" |
| Todo lo demás | Segunda persona (tú) | "Tu tienda", "Crea tu cuenta" |

Excepción deliberada a `VOICE-TONE.md` §4.1. Se justifica porque el usuario se está autoclasificando, no recibiendo una instrucción.

### Reglas

- Los tres segmentos usan la misma estructura gramatical: verbo + sustantivo. No mezclar "Soy emprendedor" con "Para empresas".
- **Un segmento tiene un solo destino en toda la landing.** Si el mega-menú manda a PyME a `/precios` y la tarjeta de segmento a `/registro`, hay un error.
- El copy de apoyo del segmento sí vuelve a segunda persona: "Planes y precios a tu medida".

### Segmentos canónicos

| Segmento | Copy | Destino |
|---|---|---|
| Emprendedor | Soy emprendedor | `/registro` |
| PyME | Tengo una PyME | `/login` |
| Empresa | Soy empresa | `/contacto-ventas` |

El destino de cada segmento es único en todo el sitio. Hoy el mega-menú manda PyME a `/precios` y el
card a `/registro`: los dos se alinean a `/login`.

---

## 7. Copy dentro de mockups de producto

Las landings de T1 muestran mockups de dashboard, App y checkout con texto legible.

> **Regla dura: el texto dentro de un mockup es UI, no marketing. Sigue `UX-WRITING.md`, no este documento.**

Esto significa que dentro de un mockup aplican:

- Labels: sustantivo preciso, sin punto (`UX-WRITING.md` §4)
- Placeholders: ejemplo concreto o instrucción breve (§5)
- CTAs en **infinitivo**, no imperativo (§1)
- Terminología canónica del `GLOSSARY.md`
- Ortografía y acentuación completas

### Errores típicos a vigilar

| ❌ En mockup | ✅ Correcto | Regla |
|---|---|---|
| "Búsqueda" como placeholder | "Buscar producto" | Placeholder = instrucción, no categoría |
| "Tenis blancos clasicos" | "clásicos" | Acentuación |
| "$249.001 disponible" | "$249.00 · 1 disponible" | Separación de datos |
| Social proof con cifras distintas al hero | Mismo dato | §2 |

El mockup es una promesa visual del producto real. Si el texto del mockup no pasaría un review de UI writing, no debe publicarse.

### Datos de ejemplo

**Los datos de ejemplo de un mockup son copy y se revisan como copy.** Nombres, productos, montos,
folios y estados son texto visible en producción, no relleno técnico.

| Regla | Detalle |
|---|---|
| Nombres de persona | Nombre y apellido ficticios, verosímiles, en formato correcto: `Laura Medina`, no `test lopez quiroz` |
| Idioma | Español. Sin excepciones: `Paquete entregado`, no `Package delivered successfully` |
| Estados | Terminología canónica del producto. Sin notas de desarrollo: `Devolución rechazada · fuera de plazo`, no `rechazada — no vale` |
| Folios e IDs | Formato consistente y prefijo comprensible. Si el prefijo abrevia un término del dominio, usa el canónico |
| Abreviaturas | Expandidas. `Tasa de reclamaciones`, no `Tasa de CB` |
| Montos | Formato de moneda completo, con separador entre precio y otro dato |
| Placeholders | Instrucción o ejemplo real. Nunca la palabra `Placeholder` |

Todo dato de ejemplo entra al mismo review que el copy de la página. Un mockup con datos de prueba
publicado comunica que el producto no está terminado.

---

## 8. Estructura narrativa de sublanding

Las sublandings de T1 siguen un arco repetido. Documentarlo evita que cada página lo reinvente y
permite detectar cuándo falta un bloque.

| # | Bloque | Función | Tipo de copy |
|---|---|---|---|
| 1 | Hero | Qué es y para quién | H1 + subtítulo + CTA |
| 2 | Enunciado del problema | El dolor, en palabras del lector | H2 |
| 3 | Solución | Cómo lo resuelve T1 | H2 + cards |
| 4 | Funcionalidades | Qué incluye | H3 + descripciones |
| 5 | Prueba | Cifras o casos | Tira de stats / testimonial |
| 6 | Preguntas frecuentes | Objeciones | Pregunta + respuesta |
| 7 | Cierre | Conversión | Pregunta + apoyo + CTA |

### El enunciado del problema

Es el bloque con voz más marcada de la página, y el que más se recicla. Reglas:

- **Se escribe desde el lector, no desde T1.** `Negociar con cada paquetería no debería ser tu trabajo` funciona; `Con T1, olvídate de todo esto` no dice cuál es el problema.
- **No se recicla entre páginas.** La frase `Con T1, olvídate de todo esto` aparece hoy en tres sublandings distintas. Si el problema es distinto, la frase es distinta.
- **No nombra a T1 en la misma línea que el dolor.** El problema existe sin T1; esa es la premisa.
- Sin punto final, máx. 10 palabras.

---

## 9. Preguntas frecuentes

Todas las sublandings tienen FAQ. Es el bloque con más texto de la página y el que más contradice
al cuerpo.

### Estructura

```
¿[Pregunta en primera persona del lector]?
[Respuesta directa]. [Explicación breve].
```

### Reglas

| Elemento | Regla |
|---|---|
| **Pregunta** | Primera persona del lector: `¿Necesito saber de diseño?`, `¿Puedo vender en marketplaces desde T1?`. Es la misma excepción gramatical que los selectores de audiencia (§6) |
| **Longitud de pregunta** | Máx. 10 palabras |
| **Apertura de la respuesta** | La respuesta va primero: `Sí.` / `No.` / el dato concreto. Nunca abre con contexto |
| **Longitud de respuesta** | 1–2 oraciones, máx. 30 palabras |
| **Cantidad** | 4–6 preguntas por página |
| **Persona** | La respuesta vuelve a segunda persona (tú) |

### Regla dura: la FAQ no introduce información nueva

**Ningún dato, cifra, promesa o término puede aparecer por primera vez en la FAQ.** Si está en la
FAQ, tiene que estar antes en el cuerpo, con el mismo valor.

Es la regla que hoy más se rompe, y es la fuente de las contradicciones detectadas en la auditoría:

| Página | Cuerpo dice | FAQ dice |
|---|---|---|
| `/t1tienda` | `en segundos` (H1) | `En segundos tienes una tienda base… personalizarla toma unos minutos` |
| `/tienda-con-ia` | `en menos de 1 minuto` (hero) | `menos de 2 minutos` |
| `/t1pagos/reclamaciones` | `reclamación` (todo el cuerpo) | `¿Qué es un chargeback?` |

La FAQ resuelve objeciones; no es un lugar para matizar una promesa que el hero ya hizo. Si la
promesa necesita matiz, el matiz va en el hero.

---

## 10. Bloque de cierre

Componente compartido al final de cada página: pregunta + copy de apoyo + botón.

### Estructura

```
¿[Listo para + beneficio]?
[Qué obtiene y qué no cuesta].
[CTA]
```

### Reglas

- **Uno por página.** Nunca dos bloques de cierre.
- **La pregunta usa el patrón `¿Listo para + [beneficio]?`** — es el dominante hoy y funciona. El beneficio se escribe desde el lector, no desde el producto.
- **El copy de apoyo aporta información nueva.** No parafrasea la pregunta ni repite las palabras del botón.
- **El CTA de cierre no repite literalmente el CTA del hero.** Hoy cuatro páginas usan la misma etiqueta arriba y abajo (`Crea tus reglas`, `Revisa tus reportes`, `Programa tu recolección`, `Gestiona tus reclamaciones`). Si el lector llegó hasta el final, el segundo botón debe sonar distinto al primero.
- **Sin marcos de miedo.** `No pierdas otra disputa.` apela a la pérdida, no al beneficio. El cierre invita, no amenaza.

### Regla de honestidad del destino

Todos los CTAs de cierre de sublanding llevan a `/registro`. Cuando la etiqueta promete una acción
específica —`Programa tu recolección`, `Revisa tus reportes`— el lector espera esa pantalla y recibe
un formulario de alta.

> **El copy de apoyo debe declarar el paso real.** Si el botón dice `Programa tu recolección`, el
> apoyo dice: `Crea tu cuenta gratis y programa tu primera recolección hoy.`

La etiqueta puede ser contextual; lo que no puede es ocultar que hay un registro de por medio.

### Sufijo "gratis": alcance

El sufijo se reserva a los **CTAs de conversión genérica**: nav, hero de home, cierre de home y
tarjetas de segmento. Ahí, `gratis` apunta solo a `/registro` y ninguna otra etiqueta lo hace.

Los CTAs de cierre de sublanding quedan fuera de esa regla: son contextuales y la señal de
gratuidad la carga el copy de apoyo. Lo que **no** se relaja en ningún nivel: una etiqueta, un
destino.

---

## 11. Metadata

El `<title>` y la `description` son copy: son lo primero que ve alguien que llega desde buscador.

| Campo | Regla | Ejemplo |
|---|---|---|
| `title` | `[Función] · [Producto]` | `Reclamaciones · T1 Pagos` |
| `description` | 1–2 oraciones, máx. 155 caracteres | — |

### Reglas

- **Cada página tiene su propia `description`.** Hoy las 19 sublandings comparten `Todo en uno. Tienda, pagos y envios para tu negocio.` — con la falta de acento incluida.
- **La `description` usa la terminología canónica.** Es la superficie donde más se cuela lo prohibido: la única página con description propia (`/reclamaciones`) mete `disputas` ×2, `chargebacks` y `contracargos` en una sola oración, mientras su `<title>` sí dice `Reclamaciones`.
- **No contradice al cuerpo.** Si el H1 promete `en menos de 1 minuto`, la description no dice `en segundos`.
- **No repite el `<title>`.**
- Acentuación completa. Es texto que se indexa.

> Cambiar metadata tiene consecuencias de SEO. Toda corrección de terminología en `description` se
> revisa con quien lleve posicionamiento antes de publicarse.

---

## 12. La promesa de marca y las muletillas

La voz de T1 está definida en [`VOICE-TONE.md`](./VOICE-TONE.md) §2. Esta sección cubre dos cosas
propias de landing: cómo se usa la promesa de marca, y qué construcciones la debilitan.

### La promesa de marca

**T1 unifica lo que hoy está separado.** Es el diferenciador y se declara con frecuencia. Tiene
cuatro formulaciones, y no son intercambiables:

| Formulación | Nivel | Cuándo |
|---|---|---|
| `un solo ecosistema` | Marca | Cuando se habla de T1 completo, no de un producto |
| `una sola plataforma` | Producto | Cuando se habla de uno de los productos frente a sus alternativas |
| `un solo lugar` | Función | Cuando se unifica una tarea concreta: cotizar, cobrar, rastrear |
| `todo en uno` | Paquete | Cuando lo que se unifica son piezas de hardware o de servicio |

Elegir el nivel correcto evita que dos páginas contiguas usen la misma literal, sin renunciar a la
promesa.

### Regla: la promesa nunca viaja sola

> Cada vez que aparece, la promesa debe nombrar **qué se unifica** y, cuando aporta, **contra qué
> estado**. Sola, es una afirmación sin contenido: sirve para cualquier producto y por eso no
> distingue a ninguno.

| ❌ La promesa sola | ✅ La promesa anclada |
|---|---|
| `Resuelve incidencias de envío desde un solo lugar` | `Resuelve incidencias de todas tus paqueterías desde un solo lugar` |
| `Todos tus envíos, un solo lugar` | `Cotiza, crea guías y rastrea desde un solo lugar` |
| `Reclamaciones en un solo lugar` | `Las reclamaciones de todos tus procesadores, en un solo lugar` |
| `Un solo lugar para todos tus envíos` | ya está anclada — se queda |
| `Vende en +10 marketplaces desde un solo lugar` | ya está anclada — se queda |

**La prueba:** si la frase sirve igual para envíos, pagos y tienda sin cambiar una palabra, le falta
el ancla.

### Muletillas

Estas sí son relleno: no son la promesa, la imitan sin decir nada.

| Construcción | Veces hoy | Uso máximo | Por qué |
|---|---|---|---|
| `olvídate de…` | 4 | 1 | Dice de qué te libras, no qué ganas. Y `Con T1, olvídate de todo esto` está idéntica en dos páginas |
| `sin complicaciones` / `cero complicaciones` / `sin fricción` | 4 | 1 | Tres formas de no nombrar la complicación |
| `los números hablan` / `números que hablan por sí solos` | 4 | 0 | Cliché. La cifra habla sola; el título sobra |


### `Fácil y seguro` no es muletilla

Es una promesa real: en pagos, la seguridad es diferenciador. Se conserva. Lo que sí hay que
corregir son dos cosas concretas:

**1. Una página y su hija no pueden abrir casi igual.**

| Página | H1 actual |
|---|---|
| `/t1pagos` | `Cobra en línea, fácil y seguro` |
| `/t1pagos/pagos-en-linea` | `Cobra en línea fácil, rápido y seguro` |

Casi la misma frase, una dentro de la otra. La hija tiene que decir algo que la madre no dijo.

**2. Donde hay dato, el dato gana.**

`Cobra en línea con +85% de aprobación` es más fuerte que `Cobra en línea, fácil y seguro`, porque el
adjetivo lo puede decir cualquiera y la cifra no. La regla no es "no uses adjetivos": es **si tienes
el número, úsalo**.

Se sustituyen por lo concreto que estaban tapando:

| ❌ | ✅ |
|---|---|
| `Una plataforma, cero complicaciones` | Nombrar qué deja de hacer el comerciante |
| `Con T1, olvídate de todo esto` | Nombrar el problema específico de esa página |
| `Los números hablan` | Quitar el título y dejar la tira de cifras |

### Marcadores de la voz

Lo que sí se repite en todas las páginas, porque es lo que hace que suene la misma persona:

| Marcador | Regla |
|---|---|
| **Longitud de oración** | Corta. Una idea por oración. Si hay dos comas, revisa |
| **Verbo al frente** | `Crea tu tienda`, no `La creación de tu tienda` |
| **Segunda persona** | `tu tienda`, `tus envíos`, `tus reclamaciones` |
| **Concreto sobre abstracto** | `+10 paqueterías` sobre `múltiples opciones logísticas` |
| **Un adjetivo por oración** | Y solo si aporta |
| **Sin marcos de miedo** | El copy invita. `No pierdas otra venta` se reescribe en positivo |
| **El comerciante es el sujeto** | `Crea tu tienda`, no `T1 crea tu tienda` |

---

## 13. Página de referencia canónica

> **La home (`/`) es la referencia de voz de T1.** Antes de escribir cualquier página nueva, se lee
> completa. Ninguna regla de este documento sustituye ese paso: la voz se imita, no se deduce.

### Qué imitar

| Rasgo | Ejemplo literal de la home |
|---|---|
| **H1 con verbo y objeto del lector** | `Un solo lugar para crear tu tienda` |
| **Título de sección de 3–5 palabras** | `Crece sin complicaciones` · `Lo que tu negocio necesita` · `Para cada etapa de tu negocio` |
| **Subtítulo que agrega, no repite** | `Vende, cobra y envía en un solo ecosistema conectado.` |
| **Card: verbo solo como título** | `Vende` · `Cobra` · `Envía` |
| **Descripción con dato concreto** | `Crea guías con +10 paqueterías a tarifas negociadas por volumen y rastréalas todas en un solo panel.` |
| **Bloque de producto: acción + producto** | `Envía a todo México con T1 Envíos` · `Cobra en tu tienda física con T1 POS` |
| **Promesa anclada** | `Vende, cobra y envía desde un solo lugar. Sin tarjeta de crédito.` |
| **Restricción como beneficio** | `Sin mensualidad ni mínimo de envíos.` · `sin experiencia técnica` |
| **Enumeración de tres** | `vender, cobrar y enviar` — el ritmo de tres es el patrón de T1 |

### Lo que NO se imita de la home

La referencia no es perfecta. Estas cuatro cosas están pendientes y no deben replicarse:

| No imitar | Por qué |
|---|---|
| `Cobra de forma fácil y segura con T1 Pagos` | Rompe el patrón de sus cuatro hermanas, que nombran qué o dónde. Corrección: `Cobra en línea con T1 Pagos` |
| `Empezar a cobrar` · `Cotizar envío` (CTAs de §5) | Infinitivos. La landing va en imperativo — ver §5 |
| `Empezar ahora` (card PyME) | Etiqueta genérica e infinitiva. Destino ya resuelto: `/login` |
| `Asignación automática de carriers` (mega-menú) | `carrier` es anglicismo. Va `paquetería` |

Cuando estos cuatro se corrijan, se retira esta tabla.

---

## 14. Plantillas por bloque

Estructura literal con huecos. Escribir es llenarlos, no inventar el molde.

### Hero

```
H1    [verbo imperativo] + [objeto del lector] + [ancla concreta]
      máx. 8 palabras · sin punto

Sub   [qué obtiene]. [qué no le cuesta o qué no necesita].
      1 oración · máx. 15 palabras · con punto

CTA   [verbo imperativo] + [objeto] + gratis
      2–5 palabras · sin punto
```

| ✅ | ❌ |
|---|---|
| `Rastrea todas tus guías desde T1` | `Un solo lugar para todos tus envíos` — la promesa sin ancla |
| `Cotiza, crea guías y rastrea sin cambiar de pestaña.` | `Cotiza, crea y rastrea.` — no dice qué gana |
| `Empieza a enviar gratis` | `Comenzar ahora` — genérico e infinitivo |

### Enunciado del problema

```
H2    [el dolor, en palabras del lector]
      máx. 10 palabras · sin punto · sin nombrar a T1
```

| ✅ | ❌ |
|---|---|
| `Negociar con cada paquetería no debería ser tu trabajo` | `Con T1, olvídate de todo esto` — no nombra el problema |
| `Elegir cada paquetería a mano cuesta tiempo y dinero` | `Una plataforma, cero complicaciones` — no hay problema, hay eslogan |

El problema existe sin T1. Esa es la premisa del bloque: si T1 aparece en la línea, el bloque ya no
enuncia un problema, anuncia una solución.

### Bloque de funcionalidad

```
H3    [verbo imperativo] + [beneficio] + con [Producto]
      máx. 10 palabras · sin punto

Desc  [qué hace]. [qué más incluye o qué no cuesta].
      1–2 oraciones · máx. 30 palabras · con punto

CTA   Conoce + [producto o función]      ← navegación
      [verbo] + [objeto] + gratis         ← conversión
```

| ✅ | ❌ |
|---|---|
| `Envía a todo México con T1 Envíos` | `Todos tus envíos, un solo lugar` |
| `Cotiza +10 paqueterías y crea guías en segundos. Sin mensualidad ni mínimo de envíos.` | `Cotiza y compara tarifas desde un solo panel.` — la promesa cargando sola |

### Tira de stats

```
[cifra] + [descriptor de máx. 4 palabras]   ×3
Las tres del mismo tipo de claim. Abreviaturas expandidas.
```

| ✅ | ❌ |
|---|---|
| `+50,000 negocios` · `+30M envíos` · `+200M transacciones` | `+6 mil tiendas` · `<1 min` · `+5 métodos` — volumen, tiempo e inventario mezclados |

### Testimonial

```
[métrica]
[descriptor, máx. 8 palabras]
"[cita literal, 1–2 oraciones]"
[Nombre] · [CARGO] | [EMPRESA]
```

Sin persona atribuida: sin comillas y en tercera persona. Ver §4.

### Preguntas frecuentes

```
¿[pregunta en primera persona del lector]?
[Sí. / No. / dato]. [Explicación breve].
4–6 preguntas · respuesta máx. 30 palabras
```

Nada aparece aquí por primera vez. Ver §9.

### Cierre

```
H2    ¿Listo para [beneficio en palabras del lector]?
Sub   [qué obtiene]. [qué no le cuesta].
CTA   [verbo imperativo] + [objeto]
```

| ✅ | ❌ |
|---|---|
| `¿Listo para hacer crecer tu negocio?` / `Vende, cobra y envía desde un solo lugar. Sin tarjeta de crédito.` / `Comienza gratis` | `¿Listo para hacer crecer tu negocio?` / `Comienza gratis y haz crecer tu negocio con T1.` / `Comenzar ahora` — el sub repite el título y el botón |

El beneficio del cierre es distinto en cada página. Si dos páginas cierran igual, una de las dos no
tiene identidad.

---

## 15. Léxico

### Verbos de T1

Los que aparecen en la home y en el producto. Son la columna vertebral del tono:

```
crea · cobra · envía · vende · conecta · gestiona · rastrea · acepta
revisa · consulta · describe · elige · completa · activa · programa
responde · sube · mantén · automatiza · resuelve · detecta · bloquea
evalúa · comparte · entrega · centraliza · sincroniza · monitorea
```

### Verbos que T1 no usa

Vocabulario de folleto. Prometen sin decir qué:

```
potencia · impulsa · revoluciona · transforma · empodera · maximiza
optimiza · desbloquea · escala · digitaliza · disrumpe
```

#### `Optimizar` / `optimizado`

**No se usan.** Es la única entrada de la lista con excepción explícita:

> Solo se admite si lleva **el dato al lado**, en la misma frase. Sin cifra, se elimina.

| ❌ | ✅ |
|---|---|
| `Optimizado para mayor conversión` | `+18% de conversión` |
| `Pasarela optimizada` | `Pasarela con +85% de aprobación` |
| `Optimiza tus envíos` | `Reduce el costo de cada envío` |

El problema es que `optimizado` describe una intención, no un resultado: lo puede escribir cualquier
competidor sobre cualquier producto. La cifra no.

### Sustantivos del lector

T1 se dirige al **negocio** y a la **tienda**, no a "el comerciante" ni a "el usuario":

```
tu negocio · tu tienda · tus productos · tus pedidos · tus ventas
tus envíos · tus guías · tus cobros · tus clientes · tu catálogo
tu inventario · tus canales · tus reclamaciones
```

> **T1 no nombra a la persona.** `Seller` está descartado por ser anglicismo y `comerciante` ya no se
> usa. El copy se dirige al negocio y a la tienda, en segunda persona. Ver `VOICE-TONE.md` §4.5.

### Construcciones de la casa

Patrones que sí se repiten porque son la firma:

| Patrón | Ejemplo |
|---|---|
| **Enumeración de tres** | `vender, cobrar y enviar` · `Cotiza, crea guías y rastrea` |
| **Restricción como beneficio** | `Sin mensualidad ni mínimo de envíos` · `Sin tarjeta de crédito` · `sin experiencia técnica` |
| **Cifra pegada al beneficio** | `+10 paqueterías a tarifas negociadas por volumen` |
| **Producto al final del título** | `Envía a todo México con T1 Envíos` |

---

## 16. Checklist antes de entregar

Quien escribe corre esta lista sobre su propio texto. Si algo falla, se corrige antes de entregar,
no después.

**Voz**
1. ¿Cada frase que usa la promesa de marca dice también **qué** se unifica?
2. ¿Alguna frase sirve igual para otro producto sin cambiar una palabra? Si sí, le falta ancla.
3. ¿Hay muletillas de §12? `olvídate de`, `sin complicaciones`, `los números hablan`. `Fácil y seguro` no es muletilla, pero si existe la cifra, la cifra gana
4. ¿Algún adjetivo apilado? Máximo uno por oración.
5. ¿El sujeto es el comerciante y no T1?

**Estructura**
6. ¿Los H1, H2 y H3 van sin punto? ¿Los subtítulos con punto?
7. ¿Los CTAs van en imperativo tú? ¿Los tabs en sustantivo?
8. ¿Alguna etiqueta de CTA existe ya en el sitio con otro destino?

**Contenido**
9. ¿Toda cifra viene de la tabla canónica de §2?
10. ¿Hay algún superlativo sin dato al lado?
11. ¿La FAQ introduce algún dato que no esté antes en el cuerpo?
12. ¿El copy de apoyo del cierre declara que hay un registro de por medio?

**Prueba final**
13. Leer la página nueva inmediatamente después de la home. ¿Suenan a la misma persona?

---

## 17. Cómo se opera

Este documento es normativo: dice qué está bien y qué no. El **proceso** —cómo se escribe una página
nueva y cómo se audita y reescribe una existente— vive en
[`../workflows/COPY-WORKFLOW.md`](../workflows/COPY-WORKFLOW.md), con los prompts listos para usar.

La regla que sostiene ese flujo:

> **Claude propone. Karla aprueba. La ejecución lleva la lista exacta.**

Claude nunca edita copy de marketing directamente en el repo.

---

## Decisiones pendientes

| # | Tema | Bloquea |
|---|---|---|
| 1 | Reglas de `/precios` y `/contacto-ventas` — pendientes de captura | Alcance |

### Resueltas

| Tema | Resolución | Fecha |
|---|---|---|
| Cifras publicables | Tabla canónica en §2. Owners: Alonso Charbel, Felipe Caicedo, José Luis Dorantes. Corte 30 jun 2026 | Ago 2026 |
| Claims comparativos | Revisados y aprobados por Legal. Sin cambios | Ago 2026 |
| Atribución de Casa de Toño y Telcel | Variante institucional, sin comillas | Ago 2026 |
| Terminología de Pagos | `Reclamación` es el término único | Ago 2026 |
| Nombres de producto | `T1 Tienda`, `T1 Envíos`, `T1 Pagos`, `T1 Score`, `T1 POS` | Ago 2026 |
| Destino del segmento PyME | `/login`, en mega-menú y en card | Ago 2026 |
| Cómo se nombra a la persona | No se nombra. `Seller` y `comerciante` quedan descartados | Ago 2026 |
| Promesa de marca | Se conserva y se usa con frecuencia, siempre anclada | Ago 2026 |
| Alcance de `/por-que-t1` | Fuera — el producto aún no está definido | Ago 2026 |
| Enlaces a T1 Score | Se conservan hasta la fase siguiente | Ago 2026 |

---

## Referencias

- [VOICE-TONE.md](./VOICE-TONE.md) — Voz de marca, personalidad, terminología canónica
- [UX-WRITING.md](./UX-WRITING.md) — Microcopy de producto (dashboard y App)
- [../GLOSSARY.md](../GLOSSARY.md) — Nombres de producto y terminología del ecosistema
- [../workflows/COPY-WORKFLOW.md](../workflows/COPY-WORKFLOW.md) — Proceso de escritura y revisión
- [../platforms/LANDING.md](../platforms/LANDING.md) — Reglas visuales de landing
- [../patterns/LANDING-SECTIONS.md](../patterns/LANDING-SECTIONS.md) — Catálogo de secciones
