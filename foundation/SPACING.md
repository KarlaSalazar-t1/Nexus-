# Espaciado — NEXUS V2.0

> Unidad base de **4px**. La escala completa va de 0 a 128px. Los tokens semánticos (padding, gap, margin) usan alias de tamaño (2xs–4xl) que referencian la escala base.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (variables) · **Owner:** Karla Salazar — Head of UX/UI

---

## Escala base

La colección `T1spacing` define los valores primitivos que alimentan todos los tokens semánticos.

| Token | Valor |
|---|---|
| `spacing_0` | 0px |
| `spacing_1` | 4px |
| `spacing_2` | 8px |
| `spacing_3` | 12px |
| `spacing_4` | 16px |
| `spacing_5` | 20px |
| `spacing_6` | 24px |
| `spacing_8` | 32px |
| `spacing_10` | 40px |
| `spacing_12` | 48px |
| `spacing_16` | 64px |
| `spacing_20` | 80px |
| `spacing_24` | 96px |
| `spacing_32` | 128px |

> **Nota:** La escala usa múltiplos de 4px. Los nombres de token reflejan un multiplicador (spacing_8 = 8×4 = 32px).

---

## Tokens semánticos

La colección `Nexus` define aliases de tamaño que se aplican en tres contextos: **padding**, **gap** y **margin**. Los tres contextos comparten la misma escala de valores.

### Padding

| Nombre | Token base | Valor | Uso |
|---|---|---|---|
| `padding/None` | spacing_0 | 0px | Sin padding |
| `padding/2xs` | spacing_1 | 4px | Padding mínimo, badges, tags |
| `padding/xs` | spacing_2 | 8px | Padding de inputs internos, chips |
| `padding/sm` | spacing_3 | 12px | Padding de botones, cells de tabla |
| `padding/md` | spacing_4 | 16px | Padding estándar de cards, modales |
| `padding/lg` | spacing_5 | 20px | Padding de secciones internas |
| `padding/xl` | spacing_6 | 24px | Padding de panels, sidebar items |
| `padding/2xl` | spacing_8 | 32px | Padding de cards grandes (p-8) |
| `padding/3xl` | spacing_10 | 40px | Padding de secciones de página |
| `padding/4xl` | spacing_12 | 48px | Padding de hero sections, áreas amplias |

### Gap

| Nombre | Token base | Valor | Uso |
|---|---|---|---|
| `gap/None` | spacing_0 | 0px | Sin gap |
| `gap/2xs` | spacing_1 | 4px | Gap entre ícono y texto inline |
| `gap/xs` | spacing_2 | 8px | Gap entre elementos compactos |
| `gap/sm` | spacing_3 | 12px | Gap entre items de lista, form fields |
| `gap/md` | spacing_4 | 16px | Gap estándar entre cards, grid items |
| `gap/lg` | spacing_5 | 20px | Gap entre bloques de contenido |
| `gap/xl` | spacing_6 | 24px | Gap entre secciones internas |
| `gap/2xl` | spacing_8 | 32px | Gap entre grupos de contenido |
| `gap/3xl` | spacing_10 | 40px | Gap entre secciones de página |
| `gap/4xl` | spacing_12 | 48px | Gap entre secciones mayores |

### Margin

| Nombre | Token base | Valor | Uso |
|---|---|---|---|
| `margin/None` | spacing_0 | 0px | Sin margin |
| `margin/2xs` | spacing_1 | 4px | Margin mínimo, micro-ajustes |
| `margin/xs` | spacing_2 | 8px | Margin entre elementos inline |
| `margin/sm` | spacing_3 | 12px | Margin entre párrafos, items |
| `margin/md` | spacing_4 | 16px | Margin estándar entre componentes |
| `margin/lg` | spacing_5 | 20px | Margin entre bloques |
| `margin/xl` | spacing_6 | 24px | Margin entre secciones |
| `margin/2xl` | spacing_8 | 32px | Margin entre grupos |
| `margin/3xl` | spacing_10 | 40px | Margin entre secciones de página |
| `margin/4xl` | spacing_12 | 48px | Margin entre secciones mayores |

---

## Tabla de referencia rápida

| Alias | Valor | Tailwind | Uso típico |
|---|---|---|---|
| **None** | 0px | `p-0` / `gap-0` / `m-0` | Reset |
| **2xs** | 4px | `p-1` / `gap-1` / `m-1` | Micro-espacios, ícono + texto |
| **xs** | 8px | `p-2` / `gap-2` / `m-2` | Espaciado compacto |
| **sm** | 12px | `p-3` / `gap-3` / `m-3` | Botones, cells, items de lista |
| **md** | 16px | `p-4` / `gap-4` / `m-4` | Estándar de componentes |
| **lg** | 20px | `p-5` / `gap-5` / `m-5` | Secciones internas |
| **xl** | 24px | `p-6` / `gap-6` / `m-6` | Panels, áreas amplias |
| **2xl** | 32px | `p-8` / `gap-8` / `m-8` | Cards grandes, bloques |
| **3xl** | 40px | `p-10` / `gap-10` / `m-10` | Secciones de página |
| **4xl** | 48px | `p-12` / `gap-12` / `m-12` | Hero, áreas mayores |

Valores extendidos (sin alias semántico):

| Token | Valor | Tailwind | Uso típico |
|---|---|---|---|
| `spacing_16` | 64px | `p-16` / `m-16` | Padding de secciones landing (py-16) |
| `spacing_20` | 80px | `p-20` / `m-20` | Section padding landing (py-20) |
| `spacing_24` | 96px | `p-24` / `m-24` | Section padding amplio (py-24) |
| `spacing_32` | 128px | `p-32` / `m-32` | Section padding máximo (py-32) |

---

## Spacing por contexto de plataforma

### Dashboard

| Propiedad | Desktop (1920px) | Tablet (768px) | Mobile (360px) |
|---|---|---|---|
| Page padding | 160px | 24px | 16px |
| Content gap | 28px | 24px | 16px |
| Card padding | 16–32px | 16px | 16px |

### Landing

| Propiedad | Desktop | Tablet | Mobile |
|---|---|---|---|
| Section padding vertical | 80–128px (py-20 a py-32) | 64–96px | 48–64px |
| Container padding horizontal | 24px | 24px | 20px |
| Content gap | 24–32px | 20–24px | 16px |
| Card padding | 32px (p-8) | 24px (p-6) | 20px (p-5) |

---

## Configuración Tailwind CSS

```js
spacing: {
  // Escala base T1spacing
  0: '0px',
  1: '4px',      // spacing_1
  2: '8px',      // spacing_2
  3: '12px',     // spacing_3
  4: '16px',     // spacing_4
  5: '20px',     // spacing_5
  6: '24px',     // spacing_6
  8: '32px',     // spacing_8
  10: '40px',    // spacing_10
  12: '48px',    // spacing_12
  16: '64px',    // spacing_16
  20: '80px',    // spacing_20
  24: '96px',    // spacing_24
  32: '128px',   // spacing_32
  // Tokens de layout
  'content-gap': '28px',
  'page-padding': '160px',
  'sidebar-width': '284px',
},
```

> **Nota:** La escala de Tailwind default ya coincide con estos valores (p-1 = 4px, p-2 = 8px, etc.). Los tokens custom son para layout-specific values.

---

## Anti-patrones

- ❌ Usar valores de spacing fuera de la escala (ej: 10px, 15px, 18px, 22px, 30px).
- ❌ Usar margin/padding arbitrarios con `[]` cuando existe un token equivalente.
- ❌ Mezclar unidades (rem y px) en un mismo componente.
- ❌ Hardcodear spacing en CSS cuando hay un token de Tailwind disponible.
- ❌ Usar spacing_32 (128px) para gaps — los valores extendidos son para section padding, no para gaps entre elementos.

---

## Referencias

- [LAYOUT.md](./LAYOUT.md) — Grid, breakpoints, contenedores, sidebar (decisiones estructurales)
- [PRINCIPLES.md](./PRINCIPLES.md) — Principio de Consistencia (uso de tokens)
- [THEMES.md](./THEMES.md) — Variaciones de spacing por plataforma si aplican
