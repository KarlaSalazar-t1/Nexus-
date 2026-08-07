# CLAUDE-CONTROLLER.md

> Entry point unificado para instancias de Claude trabajando en proyectos T1 / NEXUS V2.0.  
> Lee este archivo **primero**, antes de escribir cualquier código o tomar cualquier decisión de diseño.

---

## 1. Contexto del sistema

Este proyecto pertenece al ecosistema **T1**, una plataforma integral de e-commerce para el mercado mexicano. Todo código generado debe cumplir con el sistema de diseño **NEXUS V2.0**.

**Productos del ecosistema:**

| Producto | Descripción |
|---|---|
| T1 Tienda | Creación y gestión de tiendas en línea |
| T1 Envíos | Gestión logística y envíos nacionales e internacionales |
| T1 Pagos | Procesamiento de pagos, facturación y finanzas |
| T1 Score | Analytics y métricas de rendimiento |
| T1 Marketing | Campañas, canales de venta y herramientas de marketing |
| T1 POS | Punto de venta físico |
| T1 Cuenta | Cuenta única de acceso al ecosistema |

**Fuente de verdad:** Figma (`SD - Migration V2`). Cuando cualquier archivo del repo contradiga valores de Figma, Figma gana.

---

## 2. Detección de contexto — qué archivos cargar

Antes de comenzar cualquier tarea, identifica el tipo de proyecto por las keywords del request. Carga siempre `references/foundation.md`. Carga el archivo de contexto específico según lo que detectes.

### Keywords de detección

| Contexto | Keywords | Archivo a cargar |
|---|---|---|
| **Landing** | "landing", "página pública", "sitio web", "home", "landing page", "página de inicio", "marketing site" | `references/landing.md` |
| **Dashboard** | "admin", "dashboard", "panel", "backoffice", "back office", "plataforma interna", "sistema" | `references/dashboard.md` |
| **Componente sin contexto claro** | nombre de componente sin plataforma definida | Pregunta antes de continuar |
| **Ambos contextos** | request que menciona landing Y dashboard | Carga ambos references |

### Enrutamiento de tareas de copy

| Si la tarea es… | Cargar |
|---|---|
| Escribir copy de landing, sublanding o superficie de marketing | `content/MARKETING-COPY.md` + `workflows/COPY-WORKFLOW.md` (modo escritura) |
| Auditar o corregir copy de una página existente | `workflows/COPY-WORKFLOW.md` (modo revisión) |
| Microcopy de dashboard o App | `content/UX-WRITING.md` |

`CLAUDE-CONTROLLER.md` sigue siendo el único router del repo. No se crea un controller de copy.

### Regla de carga condicional

```
SIEMPRE:
  → references/foundation.md       (tokens compartidos)
  → references/anti-patterns.md    (guardrails NEXUS)

SI landing detectado:
  → references/landing.md

SI dashboard detectado:
  → references/dashboard.md

SI se piden componentes específicos:
  → references/components.md

SI se pide copy de landing o marketing:
  → references/marketing-copy.md
```

### Si el contexto no está claro

Pregunta explícitamente: *"¿Esto es para una landing page pública o para el dashboard/admin?"* No asumas. La tipografía, colores primarios, border radius y sistema de sombras difieren entre contextos y un error aquí contamina todo el output.

---

## 3. Siempre hacer primero

### 3.1 Imágenes de referencia

- Si se proporciona imagen de referencia: replicar layout, spacing, tipografía y color con exactitud. Usar contenido placeholder (`https://placehold.co/WIDTHxHEIGHT`, copy genérico). **No mejorar ni agregar al diseño.**
- Si no hay referencia: diseñar desde cero con los tokens y reglas de NEXUS V2.0. Aplicar los guardrails anti-genéricos de la sección 6.

### 3.2 Brand assets

Revisar la carpeta `brand_assets/` del proyecto antes de diseñar. Si existen logos, guías de color o imágenes de marca, usarlos. No usar placeholders donde hay assets reales disponibles.

### 3.3 Servidor local

Siempre servir en localhost. Nunca tomar screenshots de una URL `file:///`.

```bash
node serve.mjs   # sirve el proyecto en http://localhost:3000
```

Si el servidor ya está corriendo, no iniciar una segunda instancia.

---

## 4. Workflow de screenshot y QA visual

Ver `workflows/SCREENSHOT-QA.md` para el proceso completo. Resumen ejecutivo:

1. Tomar screenshot desde localhost con `node screenshot.mjs http://localhost:3000`
2. Leer el PNG con el Read tool y analizar visualmente
3. Comparar contra referencia con especificidad: *"el heading es 32px pero la referencia muestra 24px"*, *"el gap entre cards es 16px, debe ser 24px"*
4. Corregir y re-screenshot
5. Mínimo **2 rondas de comparación**. Detener solo cuando no hay diferencias visibles o el usuario lo indica

**Qué revisar en cada screenshot:**

| Categoría | Qué verificar |
|---|---|
| Tipografía | Tamaño, peso, line-height, familia correcta por contexto |
| Colores | Hex exacto — rojo landing (`#E26153`) ≠ rojo dashboard (`#DB3B2B`) |
| Espaciado | Padding, gap, margin según escala de spacing |
| Border radius | 10px estándar dashboard / 18-24px landing |
| Sombras | Sistema correcto por contexto (ver foundation) |
| Alineación | Grids, contenedores, offsets |
| Estados | Hover, focus, disabled visibles y correctos |

---

## 5. Diferencias críticas entre contextos

Esta tabla previene los errores más comunes. Cuando el output mezcla valores de contextos distintos, el resultado rompe la identidad visual del sistema.

| Token | Landing | Dashboard |
|---|---|---|
| **Tipografía títulos** | Sora | Manrope |
| **Tipografía cuerpo** | Inter | Manrope |
| **Rojo primario** | Red 600 `#E26153` | Red 500 `#DB3B2B` |
| **Rojo en texto** | Permitido como acento | ❌ Se lee como error — no usar |
| **Contenedor máx.** | `max-w-[1018px]` | `max-w-[1600px]` |
| **Border radius cards** | 24px | 10px (20px solo cards grandes) |
| **Border radius botones** | 18px | 10px |
| **Sombras** | Sistema multicapa con color tint | Solo 2: button shadow + card-selected (Red 200) |
| **Fondos** | Degradados, mesh gradients, secciones oscuras | Blanco por defecto, Gray 50/100 ocasional |
| **Dropdowns/menús** | — | Flat, sin sombra |
| **Sidebar** | No aplica | 284px, flat |
| **Desktop breakpoint** | 1280px | 1280px |

> **Manrope NUNCA en landing. Sora/Inter NUNCA en dashboard.** Esta es la regla de tipografía más importante del sistema.

---

## 6. Guardrails anti-genéricos — NEXUS

Aplican a todos los outputs. El diseño genérico degrada la identidad de T1.

### Colores

- Nunca usar la paleta default de Tailwind (indigo-500, blue-600, sky-400, etc.)
- Siempre derivar de los tokens de NEXUS definidos en `references/foundation.md`
- El rojo T1 es el único color primario. No inventar colores de marca

### Tipografía

- Nunca usar la misma familia para títulos y cuerpo
- Dashboard: Manrope en todos los niveles, variando peso para jerarquía
- Landing: Sora para títulos, Inter para cuerpo — sin excepciones
- Escala Manrope dashboard: 20 / 16 / 14 / 12px (no usar 22px ni 18px)
- Tracking ajustado en headings grandes (`-0.03em`)

### Sombras

- Nunca usar `shadow-md` flat de Tailwind
- Dashboard: solo las dos sombras del sistema (button shadow, card-selected Red 200)
- Landing: sombras multicapa con color tint y baja opacidad

### Degradados y texturas

- Landing: siempre mesh gradient en secciones oscuras — nunca `bg-gray-900` plano
- Agregar grain/textura vía SVG noise filter para profundidad
- Glow blobs, dot pattern, noise overlay son elementos decorativos obligatorios en landing

### Animaciones

- Solo animar `transform` y `opacity`
- Nunca `transition-all`
- Easing de tipo spring para interacciones

### Interactividad

- Todo elemento clickable requiere estados: hover, focus-visible y active
- Sin excepciones

### Imágenes

- Aplicar overlay gradiente (`bg-gradient-to-t from-black/60`)
- Capa de tratamiento de color con `mix-blend-multiply`

### Layouts landing

- Variedad obligatoria: no usar el mismo tipo de layout en secciones consecutivas
- Grids asimétricos (no todos `grid-cols-3`)
- Mínimo 2 secciones con fondo oscuro para ritmo visual
- **Sublanding (página de producto):** hero arranca oscuro (`#0F1419`, texto blanco); fondos agrupados en bloques (oscuro → claro → oscuro), no alternancia sección a sección. Resto del ADN igual al landing principal. Ver `platforms/LANDING.md` §16
- Títulos left-aligned por defecto (excepciones deben justificarse)

---

## 7. Reglas de implementación

1. Siempre usar los tokens de color definidos en `references/foundation.md` — nunca colores arbitrarios
2. Respetar la escala tipográfica — no inventar tamaños intermedios
3. Todo componente interactivo requiere los 10 estados obligatorios: Default, Hover, Active, Focus, Disabled, Loading, Error, Success, Selected, Empty
4. Usar border radius del sistema según contexto (ver sección 5)
5. Responsive obligatorio — mobile-first desde 360px
6. Íconos SVG en grid de 24px con stroke de 1.5px — heredan `currentColor`
7. Nomenclatura de componentes: prefijo `T1` + PascalCase (ej: `T1Button`, `T1PricingCard`)
8. Todo contenido textual, URLs y datos de configuración van en `constants.ts` — los componentes nunca hardcodean contenido
9. Overlay de modales: `rgba(0,0,0,0.6)`
10. Focus state con outline `#2180FF` de 2px en todos los elementos interactivos — usar siempre `:focus-visible`, nunca `:focus` genérico (`:focus-visible` solo se activa con navegación por teclado, evitando el outline en interacciones de mouse/tap)
11. Touch targets mínimo 44×44px

---

## 8. Tech stack

Ver `workflows/TECH-STACK.md` para el detalle completo. Stack obligatorio:

| Tecnología | Versión | Notas |
|---|---|---|
| Next.js | 14+ (App Router) | No Pages Router |
| TypeScript | — | Estricto |
| Tailwind CSS | v4 | Config en `globals.css` con `@theme inline` |

**Tailwind v4 — nota crítica:** La configuración va en `globals.css` con `@theme inline {}`, **no** en `tailwind.config.js`. Los tokens son CSS custom properties (`--color-brand-red-500: #DB3B2B;`).

**Estructura de componente — plantilla base:**

```tsx
"use client"; // solo si tiene interactividad

import SectionWrapper from "./ui/SectionWrapper";
import { DATOS } from "@/lib/constants";

export default function T1NombreSeccion() {
  return (
    <SectionWrapper id="seccion-id" className="py-20 tablet:py-28">
      {/* Elementos decorativos (absolute) */}
      {/* Contenido con z-10 relative */}
      <div className="relative z-10">
        {/* contenido */}
      </div>
    </SectionWrapper>
  );
}
```

---

## 9. Reglas absolutas — nunca romper

| Regla | Descripción |
|---|---|
| No mejorar referencias | Si hay imagen de referencia, replicar exacto — no agregar ni mejorar |
| No parar después de un screenshot | Mínimo 2 rondas de QA visual |
| No `transition-all` | Solo `transform` y `opacity` |
| No Tailwind blue/indigo como primario | El primario siempre es el rojo T1 |
| No Manrope en landing | Sin excepciones |
| No Sora/Inter en dashboard | Sin excepciones |
| No rojo en texto de dashboard | Se interpreta como estado de error |
| No hardcodear contenido en componentes | Todo va en `constants.ts` |
| No asumir contexto | Si no está claro si es landing o dashboard, preguntar |
| No ignorar brand assets | Siempre revisar `brand_assets/` antes de diseñar |

---

## 10. Mapa de references

Los archivos de `references/` son versiones condensadas de la documentación completa del repo, optimizadas para el context window de Claude. Cargarlos según la detección de contexto de la sección 2.

| Archivo | Contenido | Cuándo cargarlo |
|---|---|---|
| `references/foundation.md` | Tokens compartidos: colores, tipografía, spacing, elevación | Siempre |
| `references/anti-patterns.md` | Guardrails NEXUS: qué nunca hacer y qué hacer en su lugar | Siempre |
| `references/landing.md` | Tokens + patrones específicos de landing pages | Contexto landing |
| `references/dashboard.md` | Tokens + patrones específicos del admin/backoffice | Contexto dashboard |
| `references/components.md` | Catálogo compacto de componentes con variantes y estados | Cuando se piden componentes |
| `references/marketing-copy.md` | Reglas accionables de copy de landing y marketing | Contexto landing / copy de marketing |

Para documentación completa dirigida a humanos, ver los archivos en `foundation/`, `components/`, `platforms/` y `patterns/`.
