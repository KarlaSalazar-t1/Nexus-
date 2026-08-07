# Copy Workflow — Superficies de marketing

**Última actualización:** Agosto 2026 · **Owner:** Karla Salazar — Head of UX/UI

> Este documento es el **proceso**. Las reglas están en [`../content/MARKETING-COPY.md`](../content/MARKETING-COPY.md).
> Uno dice qué está bien; el otro dice cómo se llega ahí.

---

## Los dos modos

| Modo | Cuándo | Salida |
|---|---|---|
| **Escritura** | La página no existe | Copy propuesto, bloque por bloque |
| **Revisión** | La página existe y hay que corregirla | Tabla de reemplazos aprobados |

Los dos terminan igual: **una lista exacta que alguien aplica.** Claude nunca edita copy de marketing
directamente en el repo.

---

## La regla que sostiene todo

> **Claude propone. Karla aprueba. La ejecución lleva la lista exacta.**

Un prompt que diga "corrige el tono de estas páginas" le da a Claude licencia para reescribir la marca
a su criterio, y el resultado son 19 páginas de texto que hay que revisar línea por línea. Separar
propuesta de ejecución convierte una revisión editorial imposible en una aprobación de cinco minutos.

**Lo que Claude nunca decide solo:**

| Tema | Quién decide |
|---|---|
| Cifras nuevas o distintas a las de `MARKETING-COPY.md` §2 | Owners de producto |
| Claims comparativos y superlativos nuevos | Legal |
| Terminología que no esté en `GLOSSARY.md` | Dueño del dominio |
| Formulación de la promesa de marca | UX |
| Destinos de CTA y rutas | Producto / growth |

Ante cualquiera de estos: se marca `[PENDIENTE]` y se sigue. No se inventa.

---

## Modo escritura

Para una página que no existe.

### Prompt

```
Vas a escribir el copy de la landing de [PRODUCTO / FUNCIÓN] para T1.

ANTES DE ESCRIBIR
1. Lee content/MARKETING-COPY.md completo.
2. Lee la página de referencia canónica: https://t1-landing-neon.vercel.app/
   Es la voz de T1. La estás imitando, no reinterpretando.
3. Lee content/VOICE-TONE.md §2 y §4.

QUÉ ESCRIBIR
Estructura de MARKETING-COPY §8, en este orden:
  hero · enunciado del problema · solución · funcionalidades ·
  prueba · preguntas frecuentes · cierre
Usa las plantillas de §14 para cada bloque. No inventes estructura.

RESTRICCIONES
- Cifras: solo las de la tabla canónica de §2. Si necesitas una que no
  está ahí, márcala [PENDIENTE] y sigue. No la inventes.
- Superlativos: ninguno sin dato al lado.
- Terminología: la de GLOSSARY.md. Reclamación, no disputa ni chargeback.
  Paquetería, no carrier. Clic, no click.
- CTAs: imperativo tú. Si va a /registro, termina en "gratis".
- Tabs y filtros: sustantivo.
- No nombres a la persona. El copy se dirige al negocio y a la tienda.

ANTES DE ENTREGAR
Corre el checklist de §16 sobre tu propio texto. Repórtame qué puntos
fallaron y cómo los corregiste. Si ninguno falló, dilo explícitamente.

FORMATO DE ENTREGA
Tabla bloque por bloque:
  | Bloque | Elemento | Texto propuesto |
No entregues la página redactada de corrido y no escribas código.
```

El punto que hace la diferencia es el penúltimo: **pedir el reporte de autorevisión mueve la revisión
de quien aprueba a quien escribe.**

---

## Modo revisión

Para páginas que ya existen. Cuatro fases, con alto entre cada una.

### Fase 1 · Inventario

Claude lee y reporta. **No cambia nada.**

```
Vas a auditar el copy de [PÁGINAS].
Esta fase es de lectura. No edites ningún archivo.

Lee content/MARKETING-COPY.md completo antes de empezar.

Reporta toda ocurrencia que viole alguna regla, con esta tabla:

  | Página | Archivo:línea | Regla | Texto literal | Tipo de elemento |

En "Tipo de elemento" clasifica: H1/H2/H3 · subtítulo · párrafo · CTA ·
label de tab · texto dentro de mockup · pregunta de FAQ · respuesta de
FAQ · metadata · aria-label

Reglas a verificar:
  §1  títulos sin punto · longitud
  §2  cifras contra la tabla canónica
  §3  superlativos sin dato
  §5  CTAs en imperativo · una etiqueta un destino · sufijo "gratis"
  §7  copy y datos de ejemplo dentro de mockups
  §9  FAQ que introduce información nueva
  §10 bloque de cierre · honestidad del destino
  §11 metadata propia por página
  §12 promesa de marca sin ancla · muletillas
  §14 bloques que no siguen la plantilla
  §15 verbos fuera del léxico

Además, reporta aparte:
  - Copy hardcodeado que debería estar en constants.ts
  - Etiquetas duplicadas con destinos distintos
  - Enlaces rotos
  - Datos de prueba visibles en producción
```

Un inventario sin propuestas evita que la conversación se vuelva sobre gustos antes de saber el
tamaño real del problema.

### Fase 2 · Propuestas

Claude propone reescrituras. **Sigue sin cambiar nada.**

```
Con el inventario de la fase 1, propón la corrección de cada hallazgo.

  | Página | Actual | Propuesta | Regla que aplica | Confianza |

"Confianza": alta si la regla determina la corrección (punto final,
infinitivo, terminología); baja si es criterio editorial (reescribir un
título, romper una muletilla).

Ordena de mayor a menor confianza. Las de confianza baja las reviso una
por una; las de confianza alta las apruebo en bloque.

Si una corrección necesita una cifra, un claim o un término que no está
en MARKETING-COPY.md ni en GLOSSARY.md, márcala [PENDIENTE] y no la
propongas.
```

Separar por confianza es lo que hace revisable un lote de 200 líneas: lo mecánico se aprueba de un
jalón y la atención se va a las 20 que sí requieren criterio.

### Fase 3 · Aprobación

Fuera de Claude. Karla marca aprobado / rechazado / modificado sobre la tabla de la fase 2.

Las que se modifican regresan con el texto final, no con una nota.

### Fase 4 · Ejecución

```
Aplica exactamente esta lista de reemplazos. No agregues, no interpretes,
no mejores nada que no esté en la tabla.

[tabla aprobada]

Al terminar:
1. Diff resumido por archivo.
2. Grep de verificación de cada término retirado.
3. Reporta cualquier reemplazo que no pudiste aplicar y por qué.
```

Si en la fase 4 Claude encuentra algo que debería corregirse y no está en la lista, lo **reporta**;
no lo corrige. Ese hallazgo entra al siguiente ciclo.

---

## Cuándo se corre cada modo

| Situación | Modo |
|---|---|
| Landing o sublanding nueva | Escritura |
| Cambio de terminología o de cifras | Revisión, fases 1–4 |
| Página que lleva más de un trimestre sin tocarse | Revisión, fase 1 |
| Antes de publicar cualquier página nueva | Checklist de `MARKETING-COPY.md` §16 |
| Cierre de trimestre | Revisión de cifras contra `MARKETING-COPY.md` §2 |

---

## Referencias

- [`../content/MARKETING-COPY.md`](../content/MARKETING-COPY.md) — reglas de copy de marketing
- [`../content/VOICE-TONE.md`](../content/VOICE-TONE.md) — voz de marca
- [`../content/UX-WRITING.md`](../content/UX-WRITING.md) — microcopy de producto
- [`../GLOSSARY.md`](../GLOSSARY.md) — terminología canónica
- [`./SCREENSHOT-QA.md`](./SCREENSHOT-QA.md) — flujo equivalente para revisión visual
- [`./CLAUDE-CONTROLLER.md`](./CLAUDE-CONTROLLER.md) — enrutamiento
