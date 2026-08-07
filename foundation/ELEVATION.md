# Elevación — NEXUS V2.0

> Sombras, border-radius y z-index definen la profundidad visual del sistema. Dashboard y landing usan valores diferentes para el mismo tipo de componente.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma · **Owner:** Karla Salazar — Head of UX/UI

---

## Sombras — Dashboard

| Token | Valor CSS | Uso |
|---|---|---|
| `shadow/button` | `0 0 4px 0 rgba(0,0,0,0.14)` | Botones con elevación |
| `shadow/card-selected` | `0 0 4.5px 0.9px #F1B0A9` | Card seleccionada (ej: onboarding, selección activa) |

> **Nota:** Dropdowns, sidebar y menús **no llevan sombra** en dashboard.

```js
// Tailwind config
boxShadow: {
  button: '0 0 4px 0 rgba(0, 0, 0, 0.14)',
  'card-selected': '0 0 4.5px 0.9px #F1B0A9',
},
```

---

## Sombras — Landing

Las sombras de landing son más suaves y difusas que las del dashboard, con mayor spread para un look más elevado.

| Token | Valor CSS | Uso |
|---|---|---|
| `shadow/landing-card` | `0 0 25px 2px rgba(0,0,0,0.06)` | Cards de beneficios, features, pricing |
| `shadow/landing-card-hover` | `0 20px 50px rgba(0,0,0,0.08)` | Cards en hover (con `-translate-y-1.5`) |
| `shadow/landing-badge` | `0 12px 40px rgba(0,0,0,0.1)` | Floating badges en hero |
| `shadow/landing-mockup` | `0 25px 80px -15px rgba(0,0,0,0.18), 0 0 0 1px rgba(0,0,0,0.04)` | Browser mockup, screenshots de plataforma |
| `shadow/landing-header` | `0 0 25px 2px rgba(0,0,0,0.06)` | Header on scroll |
| `shadow/landing-screenshot` | `0 0 40px 8px rgba(0,0,0,0.08)` | Screenshots de plataforma en hero |

```js
// Tailwind config (extender boxShadow)
boxShadow: {
  // ... dashboard shadows arriba
  'landing-card': '0 0 25px 2px rgba(0,0,0,0.06)',
  'landing-card-hover': '0 20px 50px rgba(0,0,0,0.08)',
  'landing-badge': '0 12px 40px rgba(0,0,0,0.1)',
  'landing-mockup': '0 25px 80px -15px rgba(0,0,0,0.18), 0 0 0 1px rgba(0,0,0,0.04)',
  'landing-header': '0 0 25px 2px rgba(0,0,0,0.06)',
  'landing-screenshot': '0 0 40px 8px rgba(0,0,0,0.08)',
},
```

---

## Border radius — Dashboard

El dashboard usa un sistema simplificado: **10px como valor estándar** para la mayoría de componentes, y **20px para cards grandes**.

| Valor | Componentes |
|---|---|
| `20px` | Cards grandes, contenedores principales |
| `10px` | Botones, inputs, selects, badges, cards estándar, modales, bottom sheet (mobile) |

```js
// Tailwind config
borderRadius: {
  'card-lg': '20px',
  DEFAULT: '10px',  // botones, inputs, cards, modales, badges
},
```

---

## Border radius — Landing

Los border-radius de landing son más generosos que los del dashboard, dando un aspecto más suave y moderno.

| Componente | Valor | Nota |
|---|---|---|
| **Cards** | `24px` | Todas las cards de landing |
| **CTA Final card** | `32px` | Card de CTA con fondo oscuro |
| **Botones** | `18px` | Primario y secundario |
| **Icon containers** | `14px` | Contenedores de íconos 52×52 |
| **Tabs / Pills** | `rounded-full` | Pills de filtro, tabs de navegación |
| **Browser mockup** | `24px` | Contenedor del mockup |
| **Gradient containers** | `24px` desktop / `0px` mobile | Contenedores con degradado pierden radius en mobile |

---

## Comparativa rápida Dashboard vs Landing

| Componente | Dashboard | Landing |
|---|---|---|
| **Cards** | `10px` (estándar) / `20px` (grandes) | `24px` |
| **Botones** | `10px` | `18px` |
| **Sombra de card** | Sin sombra (flat) | `0 0 25px 2px rgba(0,0,0,0.06)` |
| **Sombra selección** | `0 0 4.5px 0.9px #F1B0A9` | Hover glow `rgba(226,97,83,0.08)` |
| **Inputs** | `10px` | `18px` (mismos que botones) |

> Las diferencias son intencionales: el dashboard prioriza densidad de información, las landing priorizan impacto visual. Ver [THEMES.md](./THEMES.md).

---

## Z-index

Escala de capas para controlar el apilamiento de elementos. Los valores dejan espacio entre sí para permitir intercalaciones si se necesitan.

| Token | Valor | Uso |
|---|---|---|
| `z/base` | `0` | Contenido normal |
| `z/elevated` | `10` | Cards con hover elevado, elementos destacados |
| `z/sticky` | `20` | Headers sticky, tabs fijos |
| `z/sidebar` | `30` | Sidebar del dashboard |
| `z/dropdown` | `40` | Dropdowns, popovers, select menus |
| `z/header` | `50` | Header fijo (landing y dashboard) |
| `z/modal` | `60` | Modales, dialogs |
| `z/toast` | `70` | Notificaciones toast |
| `z/tooltip` | `80` | Tooltips |
| `z/overlay` | `90` | Overlay detrás de modales (`rgba(0,0,0,0.6)`) |
| `z/max` | `100` | Emergencias, loaders full-screen |

> **Nota:** El overlay (`z/overlay: 90`) va detrás del modal (`z/modal: 60`) en la lógica visual, pero se implementa como un sibling del modal. En la práctica ambos suelen ir dentro de un mismo portal con el overlay como primer hijo.

---

## Overlay de modales

| Propiedad | Valor |
|---|---|
| Background | `rgba(0,0,0,0.6)` |
| Z-index | 90 (detrás del contenido del modal) |
| Comportamiento | Click para cerrar (opcional según contexto) |

---

## Anti-patrones

- ❌ Usar `shadow-md` o `shadow-lg` de Tailwind default en lugar de los tokens del sistema.
- ❌ Agregar sombras a dropdowns o sidebar en dashboard — son flat.
- ❌ Usar border-radius de landing (24px) en componentes de dashboard.
- ❌ Usar border-radius de dashboard (10px) en cards de landing.
- ❌ Inventar valores de border-radius fuera de los definidos (ej: 6px, 8px, 13px, 15px en dashboard).
- ❌ Z-index arbitrarios (999, 9999) — usar la escala definida.
- ❌ Sombras con opacidad alta (>0.2) — el sistema usa sombras sutiles.

---

## Referencias

- [COLORS.md](./COLORS.md) — Colores de overlay y opacidades
- [LAYOUT.md](./LAYOUT.md) — Estructura de página y sidebar
- [THEMES.md](./THEMES.md) — Diferencias de elevación entre plataformas
- [SPACING.md](./SPACING.md) — Padding de cards y componentes
- [../components/ATOMS.md](../components/ATOMS.md) — Border-radius de botones e inputs
