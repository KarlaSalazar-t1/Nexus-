# Changelog — NEXUS V2.0

Todos los cambios relevantes al sistema de diseño se documentan aquí. Formato basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/).

---

## [2.5.0] — 2026-09-03

### Familia de archivos de la App móvil nativa (paridad con Dashboard/Landing) + limpieza de T1APP.md

Origen: `plataform/T1APP.md` (documentación de flujos y pantallas de la app móvil, 9001 líneas) se había agregado como un único documento de auditoría screen-por-screen, mezclando decisiones de producto/copy con hallazgos de diseño, y sin la familia de archivos de plataforma (tokens, patrones de implementación, referencia condensada) que sí tienen Dashboard y Landing. "App" tampoco existía en `CLAUDE-CONTROLLER.md` ni en la estructura documentada de `README.md`. Esta versión: (1) limpia T1APP.md de decisiones de producto/negocio/copy y de ruido residual de auditoría (secciones QA redundantes, resúmenes narrativos, higiene de Figma, IDs de Figma excesivos), deduplicando además una sección documentada dos veces; (2) crea la familia de archivos de plataforma para App — `plataform/APP.md` (tokens), `patterns/APP-FLOWS.md` (flujos a nivel de implementación, como `patterns/FLOWS.md`), `workflows/reference-app.md` (versión condensada) —; y (3) da de alta "App" en el entry point (`CLAUDE-CONTROLLER.md`) y en la estructura documentada (`README.md`). `T1APP.md` queda como el archivo de detalle profundo y trazabilidad a Figma, no como punto de entrada.

**Owner:** Karla Salazar — Head of UX/UI

**Archivos afectados:**
- `plataform/T1APP.md` — limpieza de contenido + reframe de header (9001 → 7502 líneas)
- `plataform/APP.md` — archivo nuevo (movido y renombrado desde `patterns/DESIGN-SYSTEM-APP.md`)
- `patterns/APP-FLOWS.md` — archivo nuevo
- `workflows/reference-app.md` — archivo nuevo
- `workflows/CLAUDE-CONTROLLER.md` — §2, §10
- `README.md` — estructura del repo, tabla "¿Qué necesitas?", sección "Tres contextos, un sistema"

#### Añadido

- **`plataform/APP.md` — fundamentos de la plataforma App.** Tipografía (Inter, escala T1/B1/B2/B3), layout mobile-first, botones, radios, sombras, colores semánticos, inputs, cards, chips, modales, y las 8 reglas de sistema R1–R8 consolidadas desde T1APP.md §CC.23. Marca explícitamente con 🔴 los valores todavía en disputa (token de error con 3 hex, verde de éxito con 2 hex, escalas Orange/Purple/Blue invertidas, radios sin escala cerrada) en vez de decidirlos unilateralmente.
- **`patterns/APP-FLOWS.md` — mapas de flujo de la App, nivel de implementación.** 27 flujos documentados al mismo nivel de abstracción que `patterns/FLOWS.md`: estructura, patrones/componentes y reglas de interacción, sin hallazgos de auditoría ni IDs de Figma inline.
- **`workflows/reference-app.md` — versión condensada de APP.md + APP-FLOWS.md** para el context window de Claude, siguiendo la estructura de `reference-dashboard.md`.
- **`workflows/CLAUDE-CONTROLLER.md` — "App" como contexto detectable.** Nueva fila en la tabla de keywords de detección, rama `SI app detectado` en la regla de carga condicional, y fila en el mapa de references.
- **`README.md` — App en la estructura documentada.** `platforms/APP.md`, `patterns/APP-FLOWS.md` y `workflows/references/app.md` en el árbol del repo; fila "Construir la app móvil" en la tabla "¿Qué necesitas?"; tercera columna en la tabla de contextos (antes solo Landing/Dashboard).

#### Cambiado

- **`plataform/T1APP.md` — limpieza en dos pasadas.** (1) Se removieron decisiones de producto/negocio/naming/taxonomía que estaban mezcladas con hallazgos de diseño (incluida la tabla completa de 13 decisiones D1-D13, ya fuera de esta guía). (2) Se removió ruido residual de auditoría: ~34 secciones "QA — Comparación vs Figma", ~40 bloques "Resumen:" narrativos, notas de higiene de capas Figma, notas de datos dummy, y ~600 IDs de Figma inline (se conservó un ID localizador por sección/componente para no perder trazabilidad). Reducción total: 9001 → 7502 líneas.
- **`plataform/T1APP.md` — header reframeado.** Ya no se presenta como punto de entrada; dirige explícitamente a `APP.md` + `patterns/APP-FLOWS.md` para diseñar a fidelidad 90-100%, y se declara como referencia profunda de auditoría/trazabilidad.

#### Corregido

- **Enlace roto a `DESIGN-SYSTEM-APP.md`.** T1APP.md referenciaba 9 veces `../patterns/DESIGN-SYSTEM-APP.md`, un archivo que no existía en esa ruta. Se resolvió moviendo y renombrando el archivo a `plataform/APP.md` (junto a `DASHBOARD.md`/`LANDING.md`, la ubicación real de los Nivel 1 de plataforma) y actualizando todas las referencias.
- **Sección §PE (Canales de venta) duplicada.** El Flujo 18 · Paso 4 estaba documentado dos veces completas en T1APP.md; se conservó la versión más completa y verificada, se eliminó la redundante.
- **Fila del índice duplicada** para "Agregar producto — Paso 4: Canales de venta" y "Productos · Sub-tab Inventario".

---

## [2.4.0] — 2026-08-10

### Capa visual y de componentes de landing + documentación de métricas de dashboard

Origen: re-sincronización con el repo `T1landing` tras varios ajustes de la landing y sublandings (nuevo hero, mega-menús, componentes y estilos). **La fuente de verdad de landing es ahora el código del repo — ya no hay Figma.** Se agregan dos documentos de componentes (`LANDING-COMPONENTS.md`, `METRICS.md`), se actualiza `plataform/LANDING.md` al estado real (verificado archivo por archivo sobre las 16 rutas de producto) y se reescribe `patterns/LANDING-SECTIONS.md` con alcance recortado para eliminar duplicación.

**Owner:** Karla Salazar — Head of UX/UI

**Archivos afectados:**
- `components/LANDING-COMPONENTS.md` — archivo nuevo
- `components/METRICS.md` — archivo nuevo
- `plataform/LANDING.md` — §1, §2, §3, §6, §7, §8, §11, §16
- `patterns/LANDING-SECTIONS.md` — reescrito (alcance recortado a ensamblaje de página)

#### Añadido

- **`components/LANDING-COMPONENTS.md` — catálogo de componentes de landing.** Agrupado por familia estructural (hero, cards, secuencias de cards, paneles de UI simulada, proceso, stats, tabs/segmentadores, navegación, bloques compuestos, media), cada componente mapeado a su archivo real en `src/components/`, con usos sugeridos abiertos, tokens reales y responsive. Incluye sección **Responsive** del sistema, tabla de **Procedencia y validez** (heredado vs nuevo) y tabla **Landing vs Sublanding**. Objetivo: junto con `LANDING.md` y `patterns/LANDING-SECTIONS.md`, permitir generar un landing con estilo T1 desde un solo prompt.
- **`components/METRICS.md` — paneles de métricas del dashboard.** 12 secciones: grid de paneles (tokens, spans permitidos 3/4/6/12, reglas), panel contenedor, card data (anatomía, variantes, estados, chip de comparativa), gráficas de barras verticales y horizontales, lista de estatus, tabla de cohortes, dona de distribución, estado vacío, tokens de data visualization (bloque `color/dataviz/`), reglas de implementación y discrepancias detectadas.
- **`plataform/LANDING.md` §2 — breakpoints de landing** (`mobile 360 / tablet 768 / desktop 1280 / wide 1920`) y **regla de espaciado base 4px** (padding/margin/gap en múltiplos de 4).

#### Cambiado

- **`plataform/LANDING.md` §2 — modelo de contenedor.** De un contenedor único `1018px` a **cota externa `1220px` (`--max-w`) + anchos de contenido granulares** (texto 680–760, panel 820–960, angosto 300–320). Se retiran `721` y `850`.
- **`plataform/LANDING.md` §3 — botón primario a valor real.** Background `#DB3B2B` (Red 500) + hover `#C0332A` (antes documentaba `#E26153`). Nueva tabla de tamaño/radio por contexto: nav `45px/18px`, hero `50px/23px`, CTA final `50px/23px`. `#E26153` (Red 400) queda exclusivo de acentos en headings.
- **`plataform/LANDING.md` §6 — regla de texto en hero.** El hero **siempre es oscuro** (negro o degradado) → **texto siempre blanco**. Degradado **unificado**: landing y sublanding usan un degradado similar al del hero principal (`linear-gradient(180deg, #0e0d0d→#020101)` + glows radiales rojo/azul). Se retira la regla previa "nunca texto blanco en hero" y la rama de hero claro.
- **`plataform/LANDING.md` §7 — nav.** `Productos` y `Recursos` como dropdowns + `Precios` + `Enterprise`; se elimina `Clientes`; CTA primario `Comienza gratis`.
- **`plataform/LANDING.md` §8 — footer.** Pasa a **4 columnas** (Productos / Recursos / Comunidad / T1) + sello **Hecho en México** con "Una empresa 100% mexicana".
- **`plataform/LANDING.md` §11 — marquee de logos** `30s` → `50s` (token `--animate-marquee`).
- **`plataform/LANDING.md` §16 — Variante Sublanding reescrita.** Se retira el modelo "hero arranca oscuro + ritmo por bloques oscuro→claro→oscuro" (verificado como falso en el repo). El sublanding real: **hero oscuro dividido** + esqueleto canónico de 12 partes + base de cuerpo clara con cierre oscuro.
- **`patterns/LANDING-SECTIONS.md` — reescrito con alcance recortado.** Pasa de catálogo de secciones (con anatomía y tokens por sección) a **capa de ensamblaje de página** únicamente: secuencia típica (landing principal + sublanding), ritmo de fondos, estructura base de sección, anti-patrones de layout y checklist QA de composición. Se retira la anatomía/tokens por sección — ahora en `components/LANDING-COMPONENTS.md` — eliminando la duplicación. Se actualiza al estado real del repo: hero oscuro (antes degradado rosa `#FDF0EF→#F2B5AE`), secuencia real de `page.tsx`, esqueleto de sublanding de 12 partes, contenedor `1220`, footer 4 columnas. Se corrigen anti-patrones y checklist stale (Manrope, `#E26153` vs `#DB3B2B`, texto blanco en hero, floating badges, browser mockup obligatorio, pricing simétrica). Metadata: fuente = repo (ya no Figma), Owner = Head of UX/UI.

#### Corregido

- **`plataform/LANDING.md` — label de color.** `#E26153` estaba etiquetado como "Red 600"; es **Red 400** (5 ocurrencias). `foundation/COLORS.md` siempre fue correcto; el código coincide 1:1 con COLORS.md.

#### Eliminado

- **`plataform/LANDING.md` §11 — sección Floating Badges** (verificado: 0 usos en el repo) y sus filas asociadas en las tablas de sombras y glassmorphism, más la fila de eyebrow badge glass. Se documenta que el hero actual usa degradado, no badges flotantes.

---

## [2.3.0] — 2026-08-07

### Capa de contenido: copy de marketing, terminología y nomenclatura de producto

Origen: auditoría de copy de la home y las 19 landings y sublandings de `T1landing`, agosto 2026.
A diferencia de 2.1.0 y 2.2.0, que trabajaron la capa visual de landing, esta versión toca solo la
capa de contenido: `content/`, `GLOSSARY.md` y `workflows/`. No modifica componentes ni tokens.

**Owner:** Karla Salazar — Head of UX/UI

**Archivos afectados:**
- `content/VOICE-TONE.md` — §2, §4.2, §4.3, §4.4, §4.5, §4.6 nueva, §7.1 nueva, referencias
- `content/UX-WRITING.md` — nota de alcance, §1, referencias
- `GLOSSARY.md` — productos, terminología de negocio, pagos, convenciones de nombres
- `workflows/CLAUDE-CONTROLLER.md` — enrutamiento de tareas de copy y mapa de references
- `content/MARKETING-COPY.md` — archivo nuevo
- `workflows/COPY-WORKFLOW.md` — archivo nuevo
- `workflows/references/marketing-copy.md` — archivo nuevo
- 20 archivos de `components/`, `patterns/`, `platforms/`, `foundation/` y `references/` — migración de nomenclatura

#### Añadido

- **`content/MARKETING-COPY.md` v1.2 — reglas de copy para landing y superficies de marketing.** 17 secciones normativas: headlines, cifras y social proof, claims, testimoniales, jerarquía de CTA, segmentación, copy dentro de mockups, estructura narrativa de sublanding, FAQ, bloque de cierre, metadata, promesa de marca y muletillas, página de referencia canónica, plantillas por bloque, léxico y checklist de entrega. `UX-WRITING.md` cubre el microcopy de producto; nada de eso existe en una landing.
- **`workflows/COPY-WORKFLOW.md` — modos de escritura y revisión de copy de marketing.** Modo escritura para páginas que no existen; modo revisión en cuatro fases (inventario, propuestas, aprobación, ejecución) con alto entre cada una. La separación entre reglas y proceso sigue el precedente de `SCREENSHOT-QA.md`. Regla que sostiene el flujo: Claude propone, Karla aprueba, la ejecución lleva la lista exacta.
- **`workflows/references/marketing-copy.md` — espejo condensado** de `MARKETING-COPY.md` para el context window de Claude. Solo reglas accionables, sin ejemplos extensos ni justificaciones, siguiendo el formato de los `reference-*.md` existentes.
- **`content/VOICE-TONE.md` §4.6 — Modo verbal por plataforma.** Imperativo tú en landing y sublandings, infinitivo en dashboard y App, sustantivo en tabs, pestañas y filtros. El fundamento ya existía en §1.5 (*"Crea tu primera tienda"* sobre *"Comenzar proceso de alta"*); esta sección lo formaliza como regla por superficie. Un tab no promete una acción: nombra un destino.
- **`content/VOICE-TONE.md` §7.1 — Voz por superficie.** §7 organizaba la voz por producto, pero el eje que realmente cambia el tono es landing / dashboard / App. §7.1 documenta ese eje sin quitar la tabla por producto: el producto marca el énfasis, la superficie marca el tono.
- **`content/UX-WRITING.md` §1 — Regla "una etiqueta, un destino".** Ninguna etiqueta de botón o enlace puede apuntar a dos rutas distintas dentro del mismo producto. Si el destino cambia, la etiqueta cambia.
- **`GLOSSARY.md` — 8 entradas nuevas:** `T1 POS`, `T1 Cuenta`, `Reclamación`, `Devolución`, `Punto de venta`, `Estatus del servicio`, `Negocio`, `Tienda`.
- **`workflows/CLAUDE-CONTROLLER.md` — tabla de enrutamiento de tareas de copy** en §2, más `references/marketing-copy.md` registrado en el mapa de §10. `CLAUDE-CONTROLLER.md` sigue siendo el único router del repo; no se crea un controller de copy.

#### Cambiado

- **Nomenclatura de producto migrada a forma con espacio:** `T1tienda` → `T1 Tienda`, `T1envíos` → `T1 Envíos`, `T1pagos` → `T1 Pagos`, `T1score` → `T1 Score`, `T1marketing` → `T1 Marketing`, `T1cuenta` → `T1 Cuenta`. Migración completa: 185 ocurrencias de prosa en 24 archivos `.md` — 24 en los cuatro archivos de contenido y 161 en los 20 restantes. Los identificadores de código quedan intactos: nombres de archivo `.svg`, claves de asset, rutas `public/assets/logos/t1/`, slugs `/productos/t1tienda/*`, dominio `app.t1pagos.com` y nombres de archivo de Figma (`T1envios---Crear-envio`). Los wireframes ASCII, comentarios JSX, arreglos de strings renderizados y atributos `alt` sí se migraron: son texto que lee una persona.
- **`patterns/EMPTY-STATES.md` — empty state de T1 Pagos alineado a la terminología nueva.** `Disputas / Sin disputas activas / …las disputas o contracargos que requieran tu atención` pasa a `Reclamaciones / Sin reclamaciones activas / …las reclamaciones que requieran tu atención`. Es la única superficie de producto que quedaba usando los términos retirados en §4.5.
- **`VOICE-TONE.md` §2 — el rasgo "Consistente"** ejemplificaba con `seller` / `comerciante` y contradecía la decisión de §4.5. Ahora remite a la regla de negocio y tienda.
- **`VOICE-TONE.md` §4.2 — capitalización de producto.** La fila pasa de "Nombres de plataformas T1 / Siempre capitalizados / T1tienda, T1envíos, T1pagos" a "Nombres de producto T1 / Espacio y ambas iniciales en mayúscula / T1 Tienda, T1 Envíos, T1 Pagos, T1 Score, T1 POS".
- **`VOICE-TONE.md` §4.3 — alcance explícito de la regla de punto final.** "Los títulos de sección no llevan punto final" se leía como regla exclusiva de producto. Aplica también a H1, H2 y H3 de landing y sublandings. Subtítulos, párrafos de apoyo y respuestas de FAQ sí llevan punto.
- **`VOICE-TONE.md` §4.4 — longitud de CTA acotada por superficie.** El rango de 1–3 palabras aplica a producto. En landing el CTA se lee sin contexto previo y necesita cargar la promesa completa: 2 a 5 palabras.
- **`VOICE-TONE.md` §4.5 — `Reclamación` como término único.** Confirmado con el dueño del dominio de T1 Pagos: `reclamación`, `disputa` y `contracargo` son el mismo concepto, la plataforma dice "Reclamaciones" y no hay obligación regulatoria de nomenclatura. `Contracargo` se admite exclusivamente en metadata de páginas públicas como término secundario de búsqueda. `Chargeback`, `disputa` y `CB` quedan fuera de toda superficie.
- **`GLOSSARY.md` — `Contracargo / Reclamación` reescrita como `Reclamación`,** con `Devolución` registrada por separado. La reclamación es bancaria; la devolución es la entrega física del producto por parte del comprador. Se documentan aparte para evitar que se unifiquen en una limpieza futura.
- **`GLOSSARY.md` — convenciones de nombres** adopta la forma con espacio.
- **`content/UX-WRITING.md` — nota de alcance en el encabezado:** el documento cubre microcopy de producto (dashboard y App).

#### Eliminado

- **`VOICE-TONE.md` §4.5 — fila `Seller / Comerciante`.** `Seller` se descarta por anglicismo y `comerciante` deja de usarse. T1 no nombra a la persona: el copy se dirige al **negocio** y a la **tienda**, en segunda persona (`tu negocio`, `tu tienda`, `tus pedidos`). Se evitan `seller`, `merchant`, `comerciante`, `vendedor` y `usuario`.
- **`GLOSSARY.md` — entrada `Comerciante / Seller`,** sustituida por `Negocio` y `Tienda`.

#### Corregido

- **`content/MARKETING-COPY.md` §5 — referencia cruzada de longitud de CTA.** Apuntaba a `UX-WRITING.md` §4.4; la regla `Botón / CTA: 1–3 palabras` vive en `VOICE-TONE.md` §4.4.
- **`content/MARKETING-COPY.md` §15 — nota sobre `Seller / Comerciante`.** Decía que la fila seguía viva en `VOICE-TONE.md` §4.5 y había que retirarla. Ya se retiró en esta misma versión.
- **`content/MARKETING-COPY.md` §16 — punto 3 del checklist.** Listaba `fácil y seguro` como muletilla, contradiciendo a §12, que la documenta como promesa real porque en pagos la seguridad es diferenciador.

- **`platforms/PERFIL-DE-CLIENTE.md` — `T1tiendas` en plural retirado.** La nomenclatura nueva no tiene forma plural válida. Las 2 ocurrencias del empty state de Perfil de Cliente pasan a `T1 Tienda`.
- **Campo `Owner` normalizado a `Karla Salazar — Head of UX/UI`** en 22 archivos. `Lead UX/UI` no es un título vigente.
- **`platforms/STOREFRONT.md` renombrado a `platforms/PERFIL-DE-CLIENTE.md`,** y `storefront` sustituido por `perfil de cliente` en las 41 ocurrencias del archivo. El anglicismo queda retirado; `GLOSSARY.md` registra `Perfil de cliente` como forma canónica y `storefront` como término a evitar. La definición se acotó: el archivo documenta la cuenta del comprador —seguimiento de pedidos, métodos de pago, direcciones y facturación—, no el catálogo, carrito ni checkout, que el término anterior abarcaba y el documento nunca cubrió.
- **`platforms/PERFIL-DE-CLIENTE.md` §1 — tabla de contextos de plataforma.** La fila de Dashboard decía `Comerciante / seller`; ahora dice `Negocio`, conforme a §4.5 de `VOICE-TONE.md`.
- **`disputa` y `contracargo` retirados de las superficies restantes.** `patterns/EMPTY-STATES.md` (empty state de T1 Pagos), `components/ICON-COMPONENT.md` (`aria-label` de ejemplo) y `T1_Admin_App_Context.md` (prosa de contexto). Los términos solo sobreviven en las columnas de "evitar" de `VOICE-TONE.md` §4.5, `GLOSSARY.md` y `MARKETING-COPY.md`, donde documentan qué no se usa.

#### Pendiente

- **`content/MARKETING-COPY.md` — decisión abierta #1:** reglas de `/precios` y `/contacto-ventas`, pendientes de captura.

---

## [2.3.0] — 2026-08-07

### Regla de extranjerismos, términos internos y refinamiento de copy de marketing

Auditoría de la sublanding `/productos/t1tienda/tienda-con-ia` que destapó cinco huecos en la documentación: no existía una regla de extranjerismos —el sistema conservaba "checkout" y "fulfillment" pero no decía nada de "dashboard", "responsive" o "tracking", que se colaban al copy—, el verbo "optimizar" estaba documentado como excepción discutible en lugar de regla, las tiras de stats no tenían regla para cuando no existen tres cifras comparables, los mensajes de conversión no estaban obligados a anclarse al dato duro, y el flujo de revisión no advertía que una ruta se compone de varios componentes.

Se incorpora además la distinción **interno vs. copy de cliente**: `seller` y `contracargo` son correctos dentro del equipo y no hacia el cliente.

**Owner:** Karla Salazar — Head of UX/UI

**Archivos afectados:**
- `content/VOICE-TONE.md` — nueva tabla de extranjerismos y bloque de términos internos en §4.5
- `GLOSSARY.md` — nuevas secciones "Extranjerismos" y "Términos internos" + notas de convención
- `content/MARKETING-COPY.md` — §2 tiras de stats, §3 mensajes de conversión, §15 `optimizar`
- `workflows/COPY-WORKFLOW.md` — alcance por ruta y código muerto en Fase 1
- `workflows/reference-marketing-copy.md` — espejo condensado sincronizado

#### Añadido

- **Regla de extranjerismos** en `VOICE-TONE.md` §4.5, con dos tablas: "Traducir siempre" y "Conservar". El criterio rector es **cuál término entiende más gente**, no cuál es más literal o más técnico. Traducir: `dashboard` → panel · `checkout` → pasarela de pago / caja · `tracking` → rastreo · `hosting` → alojamiento · `insights` → información / hallazgos. Conservar contextualizados en su primera aparición: SEO, SPEI, Fulfillment, PyME. **Regla por defecto:** ante un anglicismo nuevo, traducir, salvo que se agregue explícitamente a la tabla de conservar.
- **`responsive` no se traduce como "adaptable"**, porque no se entiende. Se dice el beneficio directo: "se ve bien en celular y computadora" o "para celular".
- **Bloque "Términos internos"** en `VOICE-TONE.md` §4.5 y sección equivalente en `GLOSSARY.md`. `Seller` y `contracargo` son válidos dentro del equipo y no en copy de cliente. Marcado `[PENDIENTE]`: con qué término nombrar a la persona en copy de cliente, si llegara a hacer falta.
- **Sección "Extranjerismos"** en `GLOSSARY.md`, en formato de referencia rápida, con las definiciones de SEO, SPEI, Fulfillment y PyME.
- **Regla de alcance por ruta** en `COPY-WORKFLOW.md`, Fase 1: una ruta se compone de varios componentes —`tienda-con-ia` renderiza `T1Features` + `TodoIncluidoDark` + `StoreShowcase`— y se auditan todos, no solo el principal.
- **Tratamiento de código muerto** en `COPY-WORKFLOW.md`, Fase 1: los bloques `{false && …}` y los componentes no montados se marcan y se reportan aparte como tarea de limpieza, pero no se auditan.
- **Regla de mensajes de conversión y aprobación** en `MARKETING-COPY.md` §3: cuando el mensaje sea sobre conversión o tasa de aprobación, se ancla al dato duro en lugar del adjetivo. El mensaje se conserva; lo que cambia es que va respaldado por la cifra.

#### Cambiado

- **`optimizar` / `optimizado` pasa de excepción discutible a regla firme** en `MARKETING-COPY.md` §15. Queda en la lista de verbos que T1 no usa, con una única excepción explícita: solo se admite si lleva el dato al lado, en la misma frase. Sin cifra, se elimina.
- **Tiras de stats: dos condiciones en lugar de una** en `MARKETING-COPY.md` §2. Las tres cifras deben ser del mismo tipo *y* del mismo nivel (producto o ecosistema). Si no existen tres cifras comparables, no se fuerza la tira: se usan 1 o 2, o se quita el bloque. Queda prohibido rellenar con cifras globales del ecosistema en la página de un solo producto.
- **`Reclamación` en `VOICE-TONE.md` §4.5** precisa su alcance: es el término único en **copy de cliente**; `contracargo` sigue siendo válido internamente.
- **Tasa de aprobación canónica: `+85%` → `+90%`** en `MARKETING-COPY.md` §2 y en el espejo condensado. Actualizado por los owners de producto. Todos los ejemplos que citaban la cifra quedaron alineados.

---

## [2.2.0] — 2026-05-06

### Refactor a filosofía catálogo

Cambio de paradigma en la documentación de landing pages tras revisión del estado real de `t1landing.vercel.app`. La versión 2.1.0 documentaba una "secuencia obligatoria" de secciones donde toda landing T1 debía tener hero video loop multi-escena + Section Stack con cards flotantes + Bento grid asimétrico + storytelling explícito + sticky scroll, en ese orden. Esta filosofía producía landings monolíticas que se sentían como copias unas de otras.

**v2.2.0 reformula:** las landings T1 son un **catálogo de componentes y patrones**, no una receta fija. **La cohesión viene de los tokens y estilo** (Sora+Inter, rojo `#E26153`, border-radius 24/18, header glass, footer negro, sin eyebrows, texto blanco opacidad 100 sobre oscuros), **no de tener los mismos elementos en el mismo orden**. Dos landings T1 pueden verse muy diferentes en composición y aún así sentirse familia.

**Owner:** Karla Salazar — Head of UX/UI

**Archivos afectados:**
- `platforms/LANDING.md` — refactor de filosofía + nuevas variantes de hero
- `patterns/LANDING-SECTIONS.md` — nuevo bloque inicial "Filosofía catálogo" + reglas de cohesión + tabla de componentes con variantes + ejemplos de composición + variantes de Hero, Section Stack, Bento IA, Pricing
- `references/reference-landing.md` — versión condensada actualizada
- `references/reference-anti-patterns.md` — anti-patrón crítico nuevo (#1: receta fija prohibida)

#### Añadido

- **Filosofía "Catálogo + Cohesión"** documentada en bloque inicial de `LANDING.md` y `LANDING-SECTIONS.md`. Define qué es obligatorio (tokens, mínimos de calidad) y qué es flexible (composición, número de secciones, énfasis narrativo).
- **4 variantes de Hero documentadas** en lugar de una sola obligatoria:
  - **A.1 — Hero con video único** (default en producción `t1landing.vercel.app`): un solo `/img/hero.mp4` + preheader fijo. La opción más liviana y suficiente para la mayoría de landings.
  - **A.2 — Hero con video loop multi-escena**: 4 videos que cician cada 5s con preheader sincronizado. Para lanzamientos y campañas especiales.
  - **A.3 — Hero con preheader animado** (sin video): visual estático + preheader que rota entre términos. Más sostenible que A.2.
  - **A.4 — Hero estático con visual rico**: sin animación. El interés visual lo carga el mockup, ilustración o foto humana. Para sublandings deep dive o enterprise.
- **2 variantes de Section Stack producto documentadas:**
  - **Variante A — Carrusel paginado** (en producción): título + descripción + CTA en columna izquierda, mockup desktop + mobile superpuesto en columna derecha, paginación 1/N entre productos. Más sostenible para producción.
  - **Variante B — Phone mockup + cards flotantes**: phone central + 2-4 cards flotantes con `animate-float` desfasadas. Más rico visualmente, más caro de mantener.
- **2 variantes de Bento IA documentadas:**
  - **Variante A — Carrusel paginado** (en producción `t1landing.vercel.app`): 1 card hero por slide con feature interactivo + paginación `1 / 5`. Documentadas las 5 cards verificadas en producción (input "Cuéntame qué vendes", color picker tienda, foto + texto IA, logos paqueterías en órbita, donut chart riesgo).
  - **Variante B — Grid asimétrico tipo bento**: 5-6 celdas con `col-span-5/7`, `col-span-7/5`, `col-span-12` y componentes simultáneamente visibles. Para sublandings donde la IA es el producto principal (ej: `/productos/t1tienda/tienda-con-ia`).
- **Variante C de Pricing — Layout 2+2 cards** (verificada en producción): 2 cards principales en fila superior (T1tienda Integrador GRATIS + Tienda en línea $399/mes) + 2 cards secundarias en fila inferior (T1pagos + T1envíos). Sirve para landing principal que comunica múltiples productos sin tabla simétrica.
- **Sticky Scroll Stack — secuencia documentada explícitamente:** Vende → Cobra → Envía → **Todo en uno (cierre)**. La última card es estructuralmente distinta — muestra los 4 íconos de productos + statement "Activa todo el ecosistema en minutos" + CTA "Crear cuenta gratis". No es solo otra capability al mismo nivel sino el cierre narrativo.
- **Formato de atribución de testimoniales documentado:** `Nombre · CARGO | EMPRESA` (middle dot entre nombre y cargo, pipe entre cargo y empresa). Verificado en producción: `"Mario Muñoz · CHIEF DIGITAL OFFICER | SEARS"`.
- **Tabla de catálogo de secciones por categoría** en `LANDING-SECTIONS.md`: 12 categorías (Hero / Social proof / Beneficios / Producto / IA-tech / Métricas / Lifestyle / Storytelling / Pricing / FAQ / Cierre / CTA Final) con todas las variantes disponibles por categoría.
- **3 ejemplos de composición real** documentados: landing principal `t1landing.vercel.app`, sublanding "Tienda con IA", y sublanding mínima de feature (hipotética). Demuestra que landings T1 pueden tener composición muy distinta y aún sentirse familia.
- **Reglas de cohesión explícitas** separadas de reglas de composición. Distingue claramente entre lo que toda landing debe tener (tokens) y lo que cada landing decide (componentes).

#### Cambiado

- **Stats counter — animación `useCountUp` ahora es opcional**, no obligatoria. La sección en producción muestra valores fijos (`+25 mil / +$25 B / +40 M`). Documentado que la animación es **mejora opcional** según preferencia del producto: sin animación es más sostenible y suficiente cuando los números son aspiracionales redondos; con animación es recomendable cuando los números son ultra-precisos (ej: 12,743 negocios) y la animación enfatiza la magnitud.
- **Stats counter header** documentado como `H3 "Nuestros números:"` (verificado en producción), permitiendo también H2 más fuerte si la sección lleva más peso narrativo.
- **Stats counter label** documentado en formato descriptivo no-uppercase: `Negocios`, `procesados en pagos`, `de envíos gestionados` (antes documentado como Inter SemiBold uppercase tracking).
- **Mínimo de fondos oscuros bajado de 2 a 1.** El requisito anterior de "mínimo 2 secciones con fondo oscuro" era prescriptivo en exceso para sublandings pequeñas.
- **Storytelling explícito ya no es obligatorio en toda landing.** Mantenido como recomendación fuerte para sublandings principales (`/productos/t1tienda/tienda-con-ia` usa Antes/Hoy completo); sublandings deep dive de un solo feature pueden prescindir.
- **Sección Lifestyle obligatoria con excepción explícita:** aplica a landing principal y sublandings principales; sublandings deep dive de un solo feature pueden prescindir.
- **"Secuencia recomendada" reformulada como "Composición orientativa"** en `LANDING.md` §16. Incluye esqueleto mínimo (Header → Hero → ... → CTA → Footer), reglas de selección, y 2 ejemplos de composición real distinta.
- **Atribución de testimoniales en código de ejemplo de LANDING.md** actualizada: `Mario Muñoz · CHIEF DIGITAL OFFICER | SEARS` (era `· SEARS`).

#### Eliminado

- **"Toda landing T1 debe tener exactamente las mismas secciones en el mismo orden"** — eliminado como filosofía. Es ahora un anti-patrón explícito en `reference-anti-patterns.md`.
- **Section Stack producto ×3 obligatorio** (uno por producto) — eliminado como obligatorio. La landing principal puede usar 1 Section Stack carrusel paginado para los 3 productos, o 3 Section Stack flotantes individuales, según preferencia.
- **Hero con video loop multi-escena como variante única** — ahora es 1 de 4 variantes disponibles.
- **Bento IA grid asimétrico como única opción** — ahora es 1 de 2 variantes disponibles (la otra es carrusel paginado).
- **"Mínimo 2 secciones con fondo oscuro"** — bajado a mínimo 1.
- **Eyebrow / chip / pill sobre títulos de sección** — sigue PROHIBIDO (regla v2.1.0 mantenida).

#### Corregido

- **Atribución de testimoniales:** producción usa `Nombre · CARGO | EMPRESA`, no `· EMPRESA`. Documentación actualizada en `LANDING-SECTIONS.md §11 Casos de éxito` y `LANDING.md §3 Texto sobre fondos oscuros`.
- **Stats counter:** label en formato descriptivo no-uppercase (verificado en producción). Antes documentado como uppercase con tracking.

#### Reglas v2.1.0 que se mantienen

- ❌ Eyebrow / chip / pill / tag sobre H1 o H2 de sección **PROHIBIDO**. Solo tags pequeños DENTRO de cards.
- ✅ Texto sobre fondos oscuros: `text-white` opacidad 100 obligatoria. Sin `text-white/X` ni `text-gray-300/400` para texto leíble.
- ✅ Mega menu de productos en header (4 cols + panel lateral 3 bloques).
- ✅ Footer `#000000` con texto blanco opacidad 100.
- ✅ Hero gradient `linear-gradient(180deg, #FDF0EF 0%, #FFFFFF 60%, #FFFFFF 100%)`.
- ✅ No repetir mismo layout en 3+ secciones consecutivas.
- ✅ No repetir mismo fondo en secciones consecutivas.

---

## [2.1.0] — 2026-05-05

### Rediseño de landing — t1landing.vercel.app

Versión refactorizada de toda la documentación de landing pages a partir del rediseño en producción de `t1landing.vercel.app` y la sublanding `t1landing.vercel.app/productos/t1tienda/tienda-con-ia`. El objetivo es que con los `.md` se puedan crear landings modernas, tech, interactivas, no planas — incorporando línea lifestyle (foto humana real, no solo paneles UI) y storytelling explícito.

**Owner:** Karla Salazar — Head of UX/UI

**Archivos afectados:**
- `platforms/LANDING.md` — reescrito completo
- `patterns/LANDING-SECTIONS.md` — reescrito completo (template base + 13 secciones + footer + anti-patrones + checklist QA)
- `foundation/ANIMATION.md` — keyframes nuevos + 4 patrones avanzados
- `references/reference-landing.md` — versión condensada actualizada
- `references/reference-anti-patterns.md` — anti-patrones críticos v2.1.0

#### Añadido

- **Hero con video loop crossfade (4 escenas):** documentado componente con 4 videos `/img/hero-1.mp4` a `hero-4.mp4` que cician cada 5s con `transition-opacity duration-700`. Preheader sincronizado con índice activo. Comprimir <2MB cada uno.
- **Header con Mega Menu de Productos:** 4 columnas (T1tienda / T1envíos / T1pagos / T1score) con features cada uno + panel lateral derecho con 3 bloques (Casos de éxito, Novedades recientes, ¿Cómo quieres empezar?). Documentado anatomía completa con HTML/JSX.
- **Section Stack — Producto (Tienda / Envíos / Pagos):** patrón nuevo con phone mockup central + 2-4 cards flotantes alrededor representando eventos del producto (orden #112, FedEx, VISA aprobado). Cada card flotante con `animate-float`, `animate-float-slow` o `animate-float-reverse` desfasadas + rotaciones leves `±3deg`.
- **Bento Grid IA asimétrico:** 6 cards con `col-span-5/7`, `col-span-7/5`, `col-span-12`. Cada celda con componente visual distinto (color picker, logos paqueterías en órbita, input chat, foto + texto IA, donut chart 78). Reglas de asimetría obligatoria.
- **Stats Counter:** 3 stats centradas con `useCountUp` + IntersectionObserver. Variante con fondo oscuro mesh + texto blanco opacidad 100. Sin eyebrow.
- **Lifestyle Cards — "¿Para quién es T1?":** patrón nuevo con 3 cards full-bleed `aspect-[4/5]` con foto humana real (Emprendedor / PyME / Enterprise) + gradient overlay inferior + texto blanco opacidad 100. Carrusel horizontal con snap en mobile. Casting con apariencia local (México), iluminación natural.
- **Tabs Verticales con auto-play:** layout 2 columnas (lista 40% / preview 60%). Auto-rotación 5s con barra de progreso `animate-progress` visible bajo tab activo. Pause on hover. **Click manual rompe auto-play permanentemente** (UX pattern: si el usuario interactuó, no le quites control).
- **Storytelling — Antes / Hoy:** patrón narrativo con 3 cards de problema (Antes) en gris apagado + bloque de solución (Hoy) con input grande interactivo + chips de ejemplo. Variante completa para sublanding, reducida para landing principal.
- **Pasos numerados 1→4:** números gigantes Sora Light 300 `clamp(56px, 8vw, 88px)` color rojo como visual hero. Sin línea conectora horizontal — la tipografía es el ritmo. Stagger de 150ms entre pasos.
- **Pricing transparente — variantes asimétricas:**
  - Variante A (T1tienda): statement gigante "GRATIS" Sora Light 300 `clamp(72px, 12vw, 144px)` + bullets
  - Variante B (T1pagos premium): cards asimétricas con plan destacado 10% más alto
  - Variante C (T1pagos métodos): marquee de logos de pago
- **Casos de éxito — sección oscura mesh:** marquee de logos blancos arriba + video card principal `aspect-[16/9]` con quote, nombre, cargo todos `text-white` opacidad 100 + thumbnails clicables con fade.
- **Sticky Scroll Stack final:** 4 cards apiladas con `position: sticky; top: 80+i*16px; z-index: i+10;`. Cada card con acento/glow distinto. Desactivado en mobile con `lg:sticky`.
- **CTA Final con avatares humanos:** 5 avatares circulares `h-12 w-12 rounded-full ring-2 ring-white -ml-3` superpuestos. Personas reales con diversidad visible. Variante Dark con texto blanco opacidad 100 + glow Red 600.
- **Logos marquee bajo el hero:** verificado en producción con 9 logos clientes (Sears, Círculo de Crédito, Mercado Libre, Telcel, Pirma, Makora, Sanborns, PASE, Claro). Velocidad 30s para 6-8 logos, 40s para 9+.
- **Keyframes nuevos en `ANIMATION.md`:**
  - `progress` — barra de progreso para tabs verticales (5s linear forwards)
  - `count-tick` — pulso sutil al cambiar de dígito en stats counter
  - `shimmer` — placeholder de carga para inputs de IA
- **Beneficios con ilustración rica:** variante recomendada — 3 cards con imagen `aspect-[4/3]` arriba de la card (VENDE / COBRA / ENVÍA), no ícono plano. Ícono plano queda como variante alternativa solo cuando no hay budget de ilustración.

#### Cambiado

- **Template base de sección elimina el eyebrow.** Antes:
  ```html
  <p class="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">Eyebrow</p>
  <h2>...</h2>
  ```
  Ahora: directo al H2 con descripción opcional debajo. Sin pill, badge ni tag sobre el título de sección.
- **Secuencia típica de secciones expandida de 10 a 16 secciones** con las nuevas: Section Stack ×3 (uno por producto), Bento IA, Stats Counter, Lifestyle Cards, Tabs Verticales, Casos de éxito, Sticky Scroll Stack, CTA con avatares.
- **Hero gradient ajustado:** `linear-gradient(180deg, #FDF0EF 0%, #FFFFFF 60%, #FFFFFF 100%)` — inicia en `#FDF0EF` (más cercano a blanco) para no chocar visualmente con el header glass.
- **Contenedor por sección diferenciado:**
  - `max-w-[1018px]` — secciones generales (era el único)
  - `max-w-[1280px]` — Hero, Casos de éxito, Sticky Scroll Stack
  - `max-w-[721px]` — Hero text, CTA final, FAQ
  - `max-w-[850px]` — Browser mockups
- **Reglas obligatorias por landing:**
  - Mínimo 1 sección con foto humana real (Lifestyle Cards o CTA con avatares)
  - Mínimo 1 sección con storytelling explícito (Antes/Hoy)
  - Mínimo 1 sección interactiva animada (Bento, Tabs verticales, Sticky Scroll, Hero video loop)
  - Mínimo 2 secciones con fondo oscuro
- **Footer texto:** todos los links pasan de `#9CA3AF` a `text-white` opacidad 100. El gris sobre `#000000` falla contraste WCAG AA.
- **Marquee multi-velocidad:** `30s` para 6-8 logos, `40s` para 9+ logos, `35s` para casos de éxito sobre fondo oscuro.

#### Eliminado

- **Eyebrow / chip / pill / tag sobre H1 o H2 de sección — PROHIBIDO.** Solo se permite tag pequeño DENTRO de cards (bento, lifestyle, beneficios), nunca sobre el título de sección.
- **Badge glass como eyebrow** (`bg-white/75 backdrop-blur-lg border border-white/50 rounded-full`): eliminado del catálogo de glassmorphism. El badge glass queda solo para floating badges contextuales (no encima de títulos).
- **Línea conectora horizontal** entre pasos numerados: eliminada. Los números gigantes son el ritmo visual.
- **Tabla simétrica de pricing 3 planes idénticos:** patrón eliminado. Usar statement gigante o asimetría.

#### Corregido

- **Texto blanco sobre fondos oscuros:** `text-white/80`, `text-white/90`, `text-white/[0.7]`, `text-gray-300`, `text-gray-400` para descripciones sobre fondo oscuro **prohibidos**. Sobre `#0f1219`, `#000000`, mesh dark, footer y secciones oscuras: `text-white` opacidad 100 obligatoria. La opacidad menor a 100 falla contraste WCAG AA y se ve descolorida cuando el fondo tiene textura mesh.
- **Quote, nombre, cargo en sección de Casos de éxito:** todos `text-white` opacidad 100 (antes a veces se documentaban en `text-gray-400`).
- **Header contenedor:** ampliado a `max-w-[1280px]` para acomodar el mega menu de productos.

#### Anti-patrones nuevos críticos (v2.1.0)

1. Eyebrow / chip / pill / tag sobre títulos de sección
2. `text-white/X` con opacidad menor a 100 sobre fondos oscuros
3. Landing solo con paneles UI sin sección lifestyle
4. Landing sin storytelling explícito
5. Pricing como tabla simétrica
6. Section Stack sin cards flotantes desfasadas
7. Tabs verticales sin barra de progreso
8. Tabs verticales que reanudan auto-play tras click manual
9. Sticky Scroll Stack activo en mobile
10. Sticky Scroll Stack con cards idénticas
11. Hero sin video loop ni interactividad
12. Pasos con línea conectora horizontal
13. CTA Final sin avatares humanos
14. Casos de éxito sobre fondo claro

---

## [2.0.0] — 2026-01-01

### Lanzamiento inicial del repositorio

**Añadido:**
- Estructura modular del repositorio con 37 archivos organizados por dominio
- `README.md` como entry point con índice, principios y guía por rol
- `GLOSSARY.md` en root como referencia transversal de terminología
- Arquitectura definida: `foundation/`, `components/`, `patterns/`, `content/`, `assets/`, `accessibility/`, `platforms/`, `workflows/`

**Decisiones de arquitectura:**
- `SPACING.md` y `LAYOUT.md` separados (tokens puros vs decisiones estructurales)
- `TABLES.md` como archivo propio en `components/` (core del admin, 80% del dashboard son tablas)
- `THEMES.md` en `foundation/` como placeholder para tokens semánticos y dark mode
- `EMPTY-STATES.md` y `NOTIFICATIONS.md` como patrones propios en `patterns/`
- `skill/` consolidado dentro de `workflows/` como `CLAUDE-CONTROLLER.md` + `references/`
- `GLOSSARY.md` movido a root (transversal a todas las áreas, no solo content)
- `ANIMATION.md` diferido a P1 (nice-to-have, animaciones documentadas inline donde se usan)

**Contexto:**
NEXUS V2.0 existía como documentación consolidada en archivos monolíticos (`CLAUDE.md`, `LANDING.md`). Esta versión del repositorio reorganiza todo el contenido en archivos modulares, autocontenidos y orientados por tema, para mejorar la mantenibilidad y permitir que cada área del equipo encuentre lo que necesita sin leer todo.

---

<!-- 
Formato para nuevas entradas:

## [2.X.Y] — YYYY-MM-DD

### Categoría del cambio
Usar las siguientes categorías según aplique:
- **Añadido** — Funcionalidad o documentación nueva
- **Cambiado** — Cambios en documentación o tokens existentes
- **Corregido** — Correcciones de errores o inconsistencias
- **Eliminado** — Documentación o tokens deprecados/removidos
- **Deprecado** — Algo que se mantendrá temporalmente pero será removido
-->
