# NEXUS V2.0 — Sistema de Diseño del Ecosistema T1

**Versión:** 2.0 · **Última actualización:** Enero 2026 · [Ver changelog](./CHANGELOG.md)

---

## ¿Qué es esto?

Este repositorio contiene la documentación completa del sistema de diseño **NEXUS V2.0**, el estándar visual y de interacción que unifica todos los productos del ecosistema **T1** — una plataforma integral de e-commerce para el mercado mexicano.

Cada decisión de diseño, cada token de color, cada componente y cada patrón de interacción que usamos en T1 está documentado aquí. Si estás construyendo, diseñando o tomando decisiones sobre cualquier producto T1, este es tu punto de partida.

### Productos del ecosistema

| Producto | Descripción |
|---|---|
| **T1 Tienda** | Creación y gestión de tiendas en línea |
| **T1 Envíos** | Gestión logística y envíos nacionales e internacionales |
| **T1 Pagos** | Procesamiento de pagos, facturación y finanzas |
| **T1 Score** | Analytics y métricas de rendimiento |
| **T1 Marketing** | Campañas, canales de venta y herramientas de marketing |

---

## Principios de Diseño

Estos 6 principios guían todas las decisiones del sistema. Cada uno tiene definición extendida, ejemplos y anti-patrones en [foundation/PRINCIPLES.md](./foundation/PRINCIPLES.md).

| # | Principio | En una línea |
|---|---|---|
| 1 | **Claridad** | Interfaces legibles con jerarquía visual bien definida |
| 2 | **Consistencia** | Patrones repetibles en todo el ecosistema |
| 3 | **Eficiencia** | Minimizar acciones del usuario con flujos inteligentes |
| 4 | **Adaptabilidad** | Responsive desde 360px móvil hasta 1920px desktop |
| 5 | **Confiabilidad** | Feedback claro de estados y manejo robusto de errores |
| 6 | **Tecnología Humanizada** | Lenguaje cercano, tonos cálidos, experiencia guiada |

---

## Estructura del Repositorio

```
t1-design-system/
│
├── README.md                          ← Estás aquí
├── CHANGELOG.md                       ← Registro de cambios con versionado semántico
├── GLOSSARY.md                        ← Términos del ecosistema T1 y e-commerce MX
│
├── foundation/                        ← Tokens y bases del sistema
│   ├── PRINCIPLES.md                  ← Principios de diseño con ejemplos
│   ├── COLORS.md                      ← Sistema cromático completo
│   ├── TYPOGRAPHY.md                  ← Familias, pesos, escala tipográfica
│   ├── SPACING.md                     ← Unidad base 8px, escala de spacing, gaps, paddings
│   ├── LAYOUT.md                      ← Grid, breakpoints, contenedores, sidebar, responsive
│   ├── ELEVATION.md                   ← Shadows, border-radius, z-index
│   ├── ANIMATION.md                   ← Keyframes, transiciones, micro-interacciones
│   └── THEMES.md                      ← Tokens semánticos, variaciones por plataforma, dark mode
│
├── components/                        ← Catálogo de componentes
│   ├── ATOMS.md                       ← Buttons, inputs, badges, avatars, loaders
│   ├── MOLECULES.md                   ← Modals, tabs, timeline, upload, pickers, cards
│   ├── ORGANISMS.md                   ← Sidebar, header, footer, forms compuestos
│   ├── TABLES.md                      ← Tablas de datos: header, filas, paginación, sorting, filtros
│   └── STATES.md                      ← 10 estados obligatorios + patrones de interacción
│
├── patterns/                          ← Cómo se ensamblan componentes en experiencias
│   ├── FLOWS.md                       ← Flujos UX: onboarding, checkout, CRUD, búsqueda
│   ├── EMPTY-STATES.md                ← Empty states por contexto: pedidos, productos, envíos
│   ├── NOTIFICATIONS.md               ← Sistema de notificaciones: toasts, banners, alertas, modales
│   ├── LANDING-SECTIONS.md            ← Catálogo de secciones para landings
│   ├── DASHBOARD-LAYOUTS.md           ← Layouts admin: sidebar, wizard, master-detail
│   └── RESPONSIVE.md                  ← Cómo colapsa cada patrón por breakpoint
│
├── content/                           ← Voz, tono y escritura
│   ├── VOICE-TONE.md                  ← Personalidad de marca, do's/don'ts
│   └── UX-WRITING.md                  ← Microcopy: errores, confirmaciones, CTAs, labels
│
├── assets/                            ← Iconografía y recursos de marca
│   ├── ICONOGRAPHY.md                 ← Catálogo de íconos, reglas de uso
│   └── BRAND-ASSETS.md               ← Logos T1, marcas terceros, restricciones
│
├── accessibility/
│   └── A11Y.md                        ← Contraste, focus, ARIA, touch targets
│
├── platforms/                         ← Estilos específicos por contexto
│   ├── LANDING.md                     ← Sora+Inter, radius 24px, contenedor 1018px
│   ├── DASHBOARD.md                   ← Manrope, sidebar 284px, contenedor 1600px
│   └── APP.md                         ← Inter, mobile-first fijo, sin breakpoints desktop
│
└── workflows/                         ← Instrucciones operativas para AI y devs
    ├── CLAUDE-CONTROLLER.md           ← Entry point unificado: routing + references
    ├── references/                    ← Versiones condensadas para context window de Claude
    │   ├── foundation.md              ← Tokens compartidos (condensado)
    │   ├── components.md              ← Catálogo de componentes (condensado)
    │   ├── landing.md                 ← Tokens + patrones landing (condensado)
    │   ├── dashboard.md               ← Tokens + patrones dashboard (condensado)
    │   ├── app.md                     ← Tokens + patrones app móvil (condensado)
    │   └── anti-patterns.md           ← Guardrails NEXUS
    ├── SCREENSHOT-QA.md              ← Proceso de QA visual
    └── TECH-STACK.md                  ← Stack técnico y convenciones
```

Además, `patterns/APP-FLOWS.md` documenta los ~27 flujos de la app móvil (nivel de implementación, como `patterns/FLOWS.md`), y `plataform/T1APP.md` es su detalle profundo pantalla-por-pantalla con trazabilidad a Figma.

**Total: 40 archivos** (3 root + 8 foundation + 5 components + 7 patterns + 2 content + 2 assets + 1 accessibility + 3 platforms + 3 workflows + 6 references + 1 detalle profundo App)

---

## ¿Qué necesitas?

Dependiendo de tu rol o tarea, estos son los archivos que te conviene leer primero:

| Si eres / necesitas... | Empieza por | Complementa con |
|---|---|---|
| **Desarrollo frontend** | `workflows/TECH-STACK.md` → `platforms/LANDING.md` o `DASHBOARD.md` | `foundation/` completo, `components/` |
| **Diseño UI** | `foundation/PRINCIPLES.md` → `foundation/COLORS.md` + `TYPOGRAPHY.md` | `components/`, `patterns/` |
| **Producto / PM** | Este `README.md` → `foundation/PRINCIPLES.md` | `patterns/FLOWS.md`, `content/VOICE-TONE.md` |
| **Contenido / Marketing** | `content/VOICE-TONE.md` → `content/UX-WRITING.md` | `GLOSSARY.md`, `assets/BRAND-ASSETS.md` |
| **QA / Testing** | `components/STATES.md` → `workflows/SCREENSHOT-QA.md` | `accessibility/A11Y.md` |
| **Nuevo en el equipo** | Este `README.md` → `foundation/PRINCIPLES.md` → `foundation/COLORS.md` | Explora según tu rol |
| **Construir una landing** | `platforms/LANDING.md` → `patterns/LANDING-SECTIONS.md` | `foundation/`, `components/ATOMS.md` |
| **Construir un dashboard** | `platforms/DASHBOARD.md` → `patterns/DASHBOARD-LAYOUTS.md` | `foundation/`, `components/TABLES.md` |
| **Construir la app móvil** | `platforms/APP.md` → `patterns/APP-FLOWS.md` | `foundation/`, `plataform/T1APP.md` (detalle profundo) |

---

## Tech Stack

Todo proyecto del ecosistema T1 usa el siguiente stack obligatorio:

| Tecnología | Versión | Notas |
|---|---|---|
| **Next.js** | 14+ | App Router obligatorio |
| **TypeScript** | Strict mode | En todo el codebase |
| **Tailwind CSS** | v4 | Config en `globals.css` con `@theme inline`, sin `tailwind.config.js` |

Detalle completo en [workflows/TECH-STACK.md](./workflows/TECH-STACK.md).

### Tres contextos, un sistema

NEXUS maneja tres contextos visuales distintos que comparten los mismos fundamentos pero difieren en ejecución. Las variaciones entre plataformas están documentadas formalmente en [foundation/THEMES.md](./foundation/THEMES.md).

| | Landing (público) | Dashboard (admin) | App (móvil nativa) |
|---|---|---|---|
| **Tipografía** | Sora + Inter | Manrope | Inter |
| **Contenedor** | 1018px | 1600px | Mobile-first fijo (360px, sin breakpoints) |
| **Border radius** | 24px (cards), 18px (buttons) | 10-20px (cards), 8px (buttons) | 12-20px (cards), 16px (buttons) |
| **Color primario** | Red 600 (`#E26153`) | Red 500 (`#DB3B2B`) | Red 500 (`#DB3B2B`) |

Más detalle en `platforms/LANDING.md`, `platforms/DASHBOARD.md` y `platforms/APP.md`.

---

## Contribuir y Mantener

### Ownership

| | |
|---|---|
| **Owner** | Karla Salazar — Head of UX/UI |
| **Canal** | Slack — consultas, propuestas de cambios, reportes de inconsistencias |

### Reglas del repositorio

1. **Un archivo = un tema.** No mezclar tokens con flujos ni componentes con workflows.
2. **Cada archivo es autocontenido.** Puede referenciar otros con links relativos, pero debe poder leerse solo.
3. **Código siempre con ejemplo.** Cada token, componente o patrón incluye snippet HTML/JSX/CSS.
4. **Dashboard vs Landing siempre diferenciado.** Cuando un valor cambia entre contextos, documentar ambos.
5. **References sincronizadas.** Al actualizar un MD del repo, actualizar la referencia condensada correspondiente en `workflows/references/`.
6. **Cross-references claras.** Cuando un tema se toca en múltiples archivos, incluir links explícitos entre ellos indicando qué cubre cada uno.

### Proceso de cambios

1. **Proponer** — Comunica el cambio en Slack con contexto: qué quieres modificar y por qué.
2. **Validar** — Karla (Head of UX/UI) revisa que el cambio sea consistente con los principios de NEXUS.
3. **Documentar** — Actualiza el MD correspondiente siguiendo las reglas de arriba.
4. **Sincronizar** — Si el cambio afecta tokens o componentes, actualiza también `workflows/references/`.
5. **Registrar** — Agrega una entrada en `CHANGELOG.md`.

### ¿Encontraste una inconsistencia?

Si algo en el código no coincide con lo que dice este repo, o si dos archivos se contradicen entre sí, repórtalo en Slack. El design system es la fuente de verdad — el código se adapta al sistema, no al revés.

---

## Licencia

Repositorio interno de T1. Uso exclusivo para equipos del ecosistema T1.
