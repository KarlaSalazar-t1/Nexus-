# Principios de Diseño — NEXUS V2.0

> Nuestros principios de diseño son las creencias fundamentales que guían todas nuestras decisiones. Sirven como criterios para evaluar nuestro trabajo y asegurar que estamos creando experiencias que realmente aportan valor a nuestros usuarios.

**Última actualización:** Marzo 2026 · **Owner:** Karla Salazar — Head of UX/UI

---

## Resumen rápido

| # | Principio | En una línea |
|---|---|---|
| 1 | **Claridad** | Hacemos que lo complejo sea comprensible |
| 2 | **Consistencia** | Creamos una experiencia unificada a través de todo el ecosistema |
| 3 | **Confiabilidad** | Generamos confianza a través de cada interacción |
| 4 | **Eficiencia** | Optimizamos cada interacción para el máximo valor |
| 5 | **Adaptabilidad** | Diseñamos para diversos contextos y necesidades |
| 6 | **Tecnología Humanizada** | Hacemos que la tecnología avanzada sea accesible para todos |

---

## 1. Claridad por encima de todo

> Hacemos que lo complejo sea comprensible.

El ecosistema T1 aborda operaciones de negocio complejas, desde logística hasta pagos y marketing. Nuestra responsabilidad es transformar esta complejidad en interfaces claras e intuitivas. Priorizamos la claridad en la presentación de información, en los flujos de trabajo y en el lenguaje que utilizamos.

**Valor de marca asociado:** *Simplicidad* — Creemos en el poder de la simplicidad para transformar lo complejo en accesible.

### En la práctica

Eliminamos la información innecesaria, utilizamos lenguaje directo y organizamos el contenido de manera jerárquica.

**Esto significa:**
- Una jerarquía tipográfica clara y predecible: cada nivel tiene un tamaño, peso y color definido (ver [TYPOGRAPHY.md](./TYPOGRAPHY.md)).
- Contenido organizado con títulos left-aligned como regla general (el ojo escanea de izquierda a derecha).
- Uso de colores semánticos consistentes: verde = éxito, rojo = error, naranja = advertencia, azul = información (ver [COLORS.md](./COLORS.md)).
- Labels, descripciones y CTAs en lenguaje directo, sin jerga técnica innecesaria.

### Pregúntate

¿Podría un usuario nuevo entender rápidamente qué está sucediendo y qué acciones puede realizar?

### Anti-patrones que violan este principio

- ❌ Mezclar 3+ tamaños de texto en una misma línea — máximo 2 niveles: el base + uno de de-emphasis.
- ❌ Usar pesos tipográficos prohibidos (Bold 700 en Sora para headings de landing, Bold 700 en Inter).
- ❌ Crear tamaños tipográficos intermedios fuera de la escala definida.
- ❌ Centrar todos los títulos — left-aligned es la regla, centrado es la excepción justificada.
- ❌ Usar colores arbitrarios fuera del sistema cromático para comunicar estados.

---

## 2. Consistencia que conecta

> Creamos una experiencia unificada a través de todo el ecosistema.

El poder del ecosistema T1 reside en la integración de sus diferentes plataformas. La consistencia visual e interactiva entre ellas permite a los usuarios transferir conocimientos y habilidades de una plataforma a otra, reduciendo la curva de aprendizaje y aumentando la confianza.

**Valor de marca asociado:** *Integración sin fracturas* — Valoramos las experiencias fluidas donde cada componente se conecta perfectamente con los demás.

### En la práctica

Utilizamos los mismos patrones para acciones similares, mantenemos un lenguaje visual coherente y aplicamos terminología consistente en todas las plataformas.

**Esto significa:**
- Los mismos tokens de color, spacing y elevación en T1tienda, T1envíos, T1pagos, T1score y T1marketing.
- Componentes con los mismos 10 estados obligatorios en toda la plataforma: Default, Hover, Active, Focus, Disabled, Loading, Error, Success, Selected, Empty.
- Nomenclatura de tokens estandarizada: `{categoría}/{rol}/{variante}` (ej: `color/brand/red/500`).
- Diferencias entre landing y dashboard documentadas explícitamente en [THEMES.md](./THEMES.md), no improvisadas.

### Pregúntate

¿Un usuario que conoce una de nuestras plataformas podría intuir cómo usar esta nueva función?

### Anti-patrones que violan este principio

- ❌ Usar colores del palette default de Tailwind (indigo-500, blue-600) en lugar de los tokens NEXUS.
- ❌ Inventar border-radius fuera del sistema (el sistema define 4px, 8px, 10px, 13px, 14px, 18px, 20px, 24px).
- ❌ Usar Manrope en landing pages o Sora en el dashboard — cada contexto tiene su familia asignada.
- ❌ Usar Red 500 (`#DB3B2B`) como primario en landing (es Red 600 `#E26153`) o Red 600 en dashboard (es Red 500).
- ❌ Crear componentes con estados incompletos — todo interactivo debe tener los 10 estados.
- ❌ Mezclar terminología entre productos (ej: "pedido" en uno y "orden" en otro para el mismo concepto).

---

## 3. Confiabilidad demostrable

> Generamos confianza a través de cada interacción.

La confianza es fundamental en servicios que gestionan aspectos críticos de un negocio como ventas, pagos y logística. Cada elemento de nuestra interfaz debe reforzar la sensación de seguridad, profesionalismo y fiabilidad.

**Valor de marca asociado:** *Confiabilidad absoluta* — Nos comprometemos con los más altos estándares de seguridad, disponibilidad y precisión, construyendo confianza a través de cada interacción.

### En la práctica

Proporcionamos feedback claro sobre las acciones, mostramos transparencia en procesos críticos y diseñamos sistemas de prevención y recuperación de errores.

**Esto significa:**
- Todo botón de acción destructiva (eliminar, cancelar pedido) requiere confirmación con doble paso en modal.
- Los estados de loading son explícitos — el usuario siempre sabe que algo está sucediendo.
- Los mensajes de error son específicos y accionables, no genéricos ("Hubo un error").
- Las transacciones financieras muestran resumen antes de confirmar.
- Los empty states guían al usuario hacia la siguiente acción en lugar de mostrar pantallas vacías.

### Pregúntate

¿Este diseño genera confianza? ¿El usuario se siente seguro realizando esta acción?

### Anti-patrones que violan este principio

- ❌ Botones destructivos sin confirmación modal (overlay `rgba(0,0,0,0.6)` + modal con doble acción).
- ❌ Spinners sin contexto — siempre indicar qué se está procesando.
- ❌ Mensajes de error genéricos sin indicar qué salió mal ni cómo solucionarlo.
- ❌ Flujos de pago sin resumen previo a la confirmación.
- ❌ Empty states que solo dicen "No hay datos" sin CTA de siguiente paso.
- ❌ Eliminar el estado de éxito después de una acción — el usuario necesita confirmación visual de que funcionó.

---

## 4. Eficiencia que transforma

> Optimizamos cada interacción para el máximo valor.

Nuestros usuarios son emprendedores y empresarios cuyo tiempo es su recurso más valioso. Cada interacción con nuestras plataformas debe ser eficiente y aportar valor real a sus operaciones. Diseñamos para minimizar los pasos necesarios y maximizar los resultados.

**Valor de marca asociado:** *Eficiencia consciente* — Respetamos el tiempo y los recursos de nuestros usuarios. Optimizamos cada proceso y función para maximizar resultados minimizando esfuerzos.

### En la práctica

Reducimos los pasos en flujos comunes, recordamos preferencias de usuario y automatizamos tareas repetitivas.

**Esto significa:**
- Formularios que solo piden lo necesario, con defaults inteligentes y autocompletado donde sea posible.
- Tablas con sorting, filtros y búsqueda integrada — el 80% del dashboard admin son tablas de datos.
- Acciones bulk disponibles donde el usuario gestiona múltiples elementos (productos, envíos, facturas).
- Flujos de onboarding progresivos que no bloquean al usuario con formularios de 20 campos.
- Shortcuts y acciones rápidas para usuarios frecuentes.

### Pregúntate

¿Esta solución ahorra tiempo y esfuerzo al usuario? ¿Hemos eliminado toda fricción innecesaria?

### Anti-patrones que violan este principio

- ❌ Formularios que piden información que el sistema ya tiene.
- ❌ Flujos de más de 3 pasos para acciones frecuentes (crear producto, procesar envío).
- ❌ Tablas sin paginación, sorting o filtros — forzar scroll infinito en datos tabulares.
- ❌ Modales dentro de modales (excepto confirmaciones destructivas).
- ❌ Forzar al usuario a llenar todo un formulario antes de poder guardar un borrador.
- ❌ Navegación que requiere más de 3 clicks para llegar a cualquier función principal.

---

## 5. Adaptabilidad inteligente

> Diseñamos para diversos contextos y necesidades.

Las soluciones T1 sirven a una amplia gama de negocios, desde emprendedores individuales hasta grandes corporativos. Nuestro diseño debe adaptarse inteligentemente a diferentes escalas, industrias y niveles de experiencia técnica, sin sacrificar calidad o usabilidad.

**Valor de marca asociado:** *Adaptabilidad inclusiva* — Reconocemos la diversidad de negocios y sus necesidades únicas. Nos comprometemos a crear soluciones que escalen y se adapten a diferentes contextos.

### En la práctica

Creamos interfaces que se escalan según el nivel de complejidad necesario, ofrecemos múltiples vías para completar tareas y consideramos diversos contextos de uso.

**Esto significa:**
- Responsive obligatorio desde 360px (mobile) hasta 1920px (desktop), con breakpoint intermedio en 768px (tablet).
- Sidebar de dashboard que colapsa: 284px expandido → icono colapsado → drawer en mobile.
- Tablas que se transforman en cards en mobile.
- Contenedores que se adaptan: 1600px en dashboard, 1018px en landing, fluid en mobile.
- Touch targets mínimos de 44px en interfaces mobile.

### Pregúntate

¿Esta solución funciona tanto para un pequeño emprendedor como para un equipo corporativo? ¿Se ve bien en el celular de un vendedor ambulante y en el monitor de un centro de operaciones?

### Anti-patrones que violan este principio

- ❌ Diseñar solo para desktop y "ver cómo queda" en mobile después.
- ❌ Usar contenedores fijos que no respetan los breakpoints del sistema (360px, 768px, 1920px).
- ❌ Botones o áreas tocables menores a 44px en interfaces mobile.
- ❌ Tablas que se cortan horizontalmente en mobile sin transformación a cards o scroll controlado.
- ❌ Sidebar siempre visible en mobile — debe colapsar a drawer.
- ❌ Ignorar el contexto de uso: un dashboard de envíos se usa frecuentemente desde un almacén con celular, no solo desde escritorio.

---

## 6. Tecnología humanizada

> Hacemos que la tecnología avanzada sea accesible para todos.

El ecosistema T1 aprovecha tecnologías avanzadas como IA y análisis de datos, pero la complejidad técnica nunca debe ser una barrera. Nuestra misión es humanizar estas tecnologías, haciéndolas accesibles y útiles para todos los usuarios, independientemente de su experiencia técnica.

**Valor de marca asociado:** *Innovación responsable* — Abrazamos la innovación con propósito, no por moda. Implementamos nuevas tecnologías cuando genuinamente mejoran la experiencia y generan valor real.

### En la práctica

Traducimos conceptos técnicos complejos a lenguaje cotidiano, proporcionamos asistencia contextual y creamos interfaces que guían al usuario.

**Esto significa:**
- Tonos cálidos en la paleta (los rojos y naranjas de T1, no azules corporativos fríos).
- Lenguaje cercano y en español mexicano natural — no traducciones literales ni tecnicismos innecesarios.
- Tooltips y ayuda contextual en funciones avanzadas (analytics, configuración de reglas, integraciones).
- Onboarding progresivo que enseña mientras el usuario usa la plataforma.
- Mensajes de éxito que celebran logros del usuario ("¡Tu primera venta!" no "Transacción procesada exitosamente").

### Pregúntate

¿Hemos ocultado la complejidad técnica manteniendo todo el poder de la funcionalidad? ¿Un usuario sin experiencia técnica podría completar este flujo sin ayuda externa?

### Anti-patrones que violan este principio

- ❌ Exponer IDs técnicos, códigos de error crudos o mensajes del servidor al usuario.
- ❌ Usar jerga técnica sin explicación ("webhook", "API key", "SKU") cuando el usuario no es técnico.
- ❌ Interfaces frías y corporativas que no reflejan la calidez de la marca T1.
- ❌ Funciones avanzadas sin onboarding ni tooltips explicativos.
- ❌ Mensajes del sistema que suenan a máquina: "Operación completada" en vez de "¡Listo! Tu envío está en camino".
- ❌ Implementar IA o automatización sin explicar qué hace y por qué se sugiere una acción.

---

## Las 12 reglas mandatorias

Estas reglas se derivan directamente de los principios y aplican a toda implementación en el ecosistema T1:

| # | Regla | Principio |
|---|---|---|
| 1 | Siempre usar los tokens de color definidos — nunca colores arbitrarios | Consistencia |
| 2 | Manrope para dashboard, Sora+Inter para landing — sin excepciones | Consistencia |
| 3 | Respetar la escala tipográfica — no inventar tamaños intermedios | Claridad |
| 4 | Todo componente interactivo debe tener los 10 estados | Confiabilidad |
| 5 | Usar border-radius del sistema — nunca valores inventados | Consistencia |
| 6 | Responsive obligatorio — mobile-first desde 360px | Adaptabilidad |
| 7 | Íconos SVG 24px con stroke 1.5px, heredan `currentColor` | Consistencia |
| 8 | Nomenclatura de tokens: `{categoría}/{rol}/{variante}` | Consistencia |
| 9 | Overlay de modales: `rgba(0,0,0,0.6)` | Confiabilidad |
| 10 | Datos en `constants.ts` — nunca hardcodear contenido en componentes | Eficiencia |
| 11 | Stack obligatorio: Next.js 14+ (App Router), TypeScript, Tailwind CSS v4 | Consistencia |
| 12 | Spacing en múltiplos de 8px — unidad base del sistema | Claridad |

---

## Cómo usar este documento

**Para diseño:** Usa los principios como criterio de revisión. Antes de entregar un diseño, recorre los 6 "pregúntate" como checklist.

**Para desarrollo:** Los anti-patrones son tu lista de verificación negativa — si tu implementación cae en alguno, hay que corregir antes de merge.

**Para producto:** Los principios guían la priorización. Si una feature no puede cumplir al menos con Claridad, Confiabilidad y Eficiencia, necesita rediseño.

**Para contenido:** El principio de Tecnología Humanizada es tu norte — todo texto en la plataforma debe pasar por ese filtro. Ver [content/VOICE-TONE.md](../content/VOICE-TONE.md) para guías específicas de escritura.

---

## Referencias

- [COLORS.md](./COLORS.md) — Sistema cromático completo
- [TYPOGRAPHY.md](./TYPOGRAPHY.md) — Familias, pesos y escala tipográfica
- [SPACING.md](./SPACING.md) — Escala de spacing base 8px
- [THEMES.md](./THEMES.md) — Variaciones por plataforma (landing vs dashboard)
- [../components/STATES.md](../components/STATES.md) — Los 10 estados obligatorios
- [../content/VOICE-TONE.md](../content/VOICE-TONE.md) — Voz y tono de marca
