# Temas — NEXUS V2.0

> Dos ejes de variación: **plataforma** (landing vs dashboard) y **modo** (light vs dark). Los tokens semánticos adaptan su valor según el contexto, los absolutos permanecen fijos.

**Última actualización:** Marzo 2026 · **Fuente de verdad:** Figma (variables, modos Light/Dark) · **Owner:** Karla Salazar — Head of UX/UI

---

## Estructura del sistema de temas

El sistema de color de NEXUS opera en dos capas:

**Capa 1 — Tokens absolutos:** Valores que NUNCA cambian entre light/dark ni entre plataformas. Son los colores de marca y elementos que deben verse idénticos siempre.

**Capa 2 — Tokens semánticos:** Valores que se adaptan al modo (light/dark). Los backgrounds se invierten, los textos se ajustan para mantener contraste, los colores de acción se preservan.

---

## Tokens absolutos

Estos valores son inmunes al dark mode. Se usan en elementos que deben mantener su apariencia exacta en cualquier contexto.

| Token | Hex | Uso |
|---|---|---|
| `absolute-white` | `#FFFFFF` | Texto sobre botón primario, texto sobre fondos de color |
| `absolute-oxford` | `#4C4C4C` | Oxford se mantiene fijo para ciertos contextos |
| `absolute-red` | `#DB3B2B` | Botón primario dashboard — rojo con texto blanco en ambos modos |

**Ejemplo — Botón primario en dark mode:**
El botón primario sigue siendo `bg-[#DB3B2B] text-white` en dark mode. No se invierte. El rojo de marca es un absoluto porque es parte de la identidad visual de T1.

> **Detalle de implementación por componente:** Ver [../components/ATOMS.md](../components/ATOMS.md) para cómo cada componente usa estos tokens.

---

## Dark mode — Solo dashboard

El dark mode aplica actualmente solo al dashboard. Landing pages no tienen dark mode.

### Color / Base

| Token | Light | Dark | Nota |
|---|---|---|---|
| **White** | `#FFFFFF` | `#0F1419` | Fondo principal → oscuro profundo |
| **Black-oxford** | `#4C4C4C` | `#F9FAFB` | Texto principal → casi blanco |
| **Black** | `#000000` | `#FFFFFF` | Inversión completa |
| **Off white** | `#FEFEFE` | `#1A1F2E` | Fondo alternativo → azul oscuro |

### Color / Brand (Red)

| Token | Light | Dark | Nota |
|---|---|---|---|
| **Red** (base) | `#DB3B2B` | `absolute-white` | En dark el fondo rojo se reemplaza por blanco en ciertos contextos |
| **Red-800** | `#E26153` | `#E26153` | Sin cambio |
| **Red-600** | `#E9897E` | `#E9897E` | Sin cambio |
| **Red-400** | `#F1B0A9` | `#374151` | Rosa claro → gris azulado oscuro |
| **Red-200** | `#F9D2D2` | `#F9D2D2` | Sin cambio |
| **Red-50** | `#FEF4F4` | `overlay/Black` | BG de alerta → overlay oscuro |
| **Dark-red** | `#CC0000` | `#CC0000` | Sin cambio — error/destructivo |

### Color / Neutral (Gray)

| Token | Light | Dark | Nota |
|---|---|---|---|
| **Gray** (base) | `#C3C3C3` | `#F9F9F9` | Base → casi blanco |
| **Gray-800** | `#CFCFCF` | `#EBEBEB` | Se aclara |
| **Gray-600** | `#DBDBDB` | `#DBDBDB` | Sin cambio — punto medio |
| **Gray-400** | `#E7E7E7` | `#374151` | Claro → azul oscuro |
| **Gray-200** | `#F3F3F3` | `#F8F8F8` | Casi sin cambio |
| **Gray-100** | `#F8F8F8` | `#242937` | BG de página → oscuro azulado |

### Color / Contextual

Los colores contextuales (semánticos) **no cambian** entre light y dark. El rojo sigue significando error, el verde sigue significando éxito.

| Token | Light | Dark | Nota |
|---|---|---|---|
| **Yellow** | `#F5A623` | `#F5A623` | Sin cambio |
| **Orange** | `#FF6900` | `#FF6900` | Sin cambio |
| **Green** | `#51AF70` | `#51AF70` | Sin cambio |
| **Red** | `#DB362B` | `#DB362B` | Sin cambio |
| **Light_yellow** | `#FFF4BF` | `#FFF4BF` | Sin cambio |

### Color / Overlay

Los overlays **no cambian** entre light y dark.

| Token | Light | Dark |
|---|---|---|
| Orange | `#FF6700` 10% | `#FF6700` 10% |
| Blue | `#2180FF` 10% | `#2180FF` 10% |
| Turquoise | `#52F5B0` 10% | `#52F5B0` 10% |
| Yellow | `#EDBD55` 10% | `#EDBD55` 10% |

---

## Dark mode — Colores extendidos (propuesta)

Los siguientes valores siguen el patrón establecido en Figma: shades claros (100) se reemplazan por el tono oscuro `#242937`, shades medios (300, 500) se mantienen, shades oscuros (700, 900) se aclaran para legibilidad.

> **Estado:** Propuesta pendiente de validación en Figma. Usar con precaución hasta que se confirmen.

### Blue

| Token | Light | Dark (propuesta) |
|---|---|---|
| Blue 100 | `#F0F8FF` | `#242937` |
| Blue 300 | `#7DB3FF` | `#7DB3FF` |
| Blue 500 | `#2180FF` | `#2180FF` |
| Blue 700 | `#005EDC` | `#7DB3FF` |
| Blue 900 | `#0F3D7A` | `#93C5FD` |

### Green

| Token | Light | Dark (propuesta) |
|---|---|---|
| Green 100 | `#F0FDF4` | `#242937` |
| Green 300 | `#6FCF97` | `#6FCF97` |
| Green 500 | `#4FC153` | `#4FC153` |
| Green 700 | `#16A34A` | `#6FCF97` |
| Green 900 | `#14532D` | `#86EFAC` |

### Orange

| Token | Light | Dark (propuesta) |
|---|---|---|
| Orange 100 | `#FFF0E5` | `#242937` |
| Orange 300 | `#FFB380` | `#FFB380` |
| Orange 500 | `#FF6700` | `#FF6700` |
| Orange 700 | `#CC5200` | `#FFB380` |
| Orange 900 | `#8A3600` | `#FDBA74` |

### Yellow

| Token | Light | Dark (propuesta) |
|---|---|---|
| Yellow 100 | `#FFF4BF` | `#242937` |
| Yellow 300 | `#FEF08A` | `#FEF08A` |
| Yellow 500 | `#EDBD55` | `#EDBD55` |
| Yellow 700 | `#A96A00` | `#FEF08A` |
| Yellow 900 | `#713F12` | `#FDE68A` |

### Brown

| Token | Light | Dark (propuesta) |
|---|---|---|
| Brown 100 | `#FAF8F3` | `#242937` |
| Brown 300 | `#F0E6B8` | `#F0E6B8` |
| Brown 500 | `#976905` | `#976905` |
| Brown 700 | `#6B4A04` | `#F0E6B8` |
| Brown 900 | `#4A3202` | `#E6D5A8` |

### Purple

| Token | Light | Dark (propuesta) |
|---|---|---|
| Purple 100 | `#FAF7FF` | `#242937` |
| Purple 300 | `#D0B3FF` | `#D0B3FF` |
| Purple 500 | `#A064FF` | `#A064FF` |
| Purple 700 | `#6537AE` | `#D0B3FF` |
| Purple 900 | `#3C1361` | `#C4B5FD` |

### Turquoise

| Token | Light | Dark (propuesta) |
|---|---|---|
| Turquoise 100 | `#F0FDFA` | `#242937` |
| Turquoise 300 | `#ADFFDC` | `#ADFFDC` |
| Turquoise 500 | `#52F5B0` | `#52F5B0` |
| Turquoise 700 | `#0F766E` | `#ADFFDC` |
| Turquoise 900 | `#134E4A` | `#5EEAD4` |

---

## Variaciones Landing vs Dashboard

Independiente de light/dark, estos tokens cambian entre plataformas. Documentados aquí como referencia centralizada.

| Propiedad | Dashboard | Landing |
|---|---|---|
| **Color primario botón** | Red 500 `#DB3B2B` | Red 400 `#E26153` |
| **Tipografía headings** | Manrope | Sora |
| **Tipografía body** | Manrope | Inter |
| **Border-radius cards** | `10px` / `20px` (grandes) | `24px` |
| **Border-radius botones** | `10px` | `18px` |
| **Sombra de card** | Sin sombra (flat) | `0 0 25px 2px rgba(0,0,0,0.06)` |
| **Contenedor máximo** | `1600px` | `1018px` |
| **Fondo de página** | `#FFFFFF` (siempre blanco) | `#FFFFFF` con secciones alternadas |
| **Acento rojo en texto** | No — puede confundirse con error | Sí — patrón de títulos con span rojo |
| **Floating badges** | No | Sí — con animaciones float |
| **Glow blobs** | No | Sí — decorativos con pulse-soft |

> **Detalle completo:** Ver [../platforms/LANDING.md](../platforms/LANDING.md) y [../platforms/DASHBOARD.md](../platforms/DASHBOARD.md).

---

## Implementación técnica

### Tailwind v4 con @theme inline

```css
/* globals.css */
@theme inline {
  /* Tokens que cambian con dark mode */
  --color-surface: #FFFFFF;
  --color-surface-alt: #FEFEFE;
  --color-on-surface: #4C4C4C;
  --color-on-surface-inverse: #FFFFFF;

  /* Absolutos — no cambian */
  --color-absolute-white: #FFFFFF;
  --color-absolute-oxford: #4C4C4C;
  --color-absolute-red: #DB3B2B;
}

/* Dark mode override */
@media (prefers-color-scheme: dark) {
  :root {
    --color-surface: #0F1419;
    --color-surface-alt: #1A1F2E;
    --color-on-surface: #F9FAFB;
    --color-on-surface-inverse: #0F1419;
    /* absolutos NO se sobreescriben */
  }
}
```

### Patrón de uso en componentes

```html
<!-- Botón primario — usa absolutos, inmune a dark mode -->
<button class="bg-absolute-red text-absolute-white rounded-[10px]">
  Guardar
</button>

<!-- Card — usa tokens semánticos, se adapta -->
<div class="bg-surface text-on-surface rounded-[10px]">
  contenido
</div>
```

---

## Anti-patrones

- ❌ Hardcodear `bg-white` o `bg-[#FFFFFF]` — usar `bg-surface` para que se adapte a dark mode.
- ❌ Hardcodear `text-[#4C4C4C]` para texto — usar `text-on-surface` para adaptabilidad.
- ❌ Invertir el botón primario en dark mode — es un absoluto, siempre rojo con texto blanco.
- ❌ Asumir que los colores contextuales (success, warning, error) cambian en dark — no cambian.
- ❌ Usar shades claros (100) como background en dark sin mappear al equivalente oscuro.
- ❌ Implementar dark mode en landing pages — solo aplica a dashboard por ahora.

---

## Referencias

- [COLORS.md](./COLORS.md) — Paleta completa light mode (fuente de verdad para valores base)
- [TYPOGRAPHY.md](./TYPOGRAPHY.md) — Variaciones tipográficas por plataforma
- [ELEVATION.md](./ELEVATION.md) — Sombras y border-radius por plataforma
- [LAYOUT.md](./LAYOUT.md) — Contenedores y estructura por plataforma
- [../components/ATOMS.md](../components/ATOMS.md) — Cómo cada componente usa tokens absolutos vs semánticos
- [../platforms/LANDING.md](../platforms/LANDING.md) — Tokens específicos de landing
- [../platforms/DASHBOARD.md](../platforms/DASHBOARD.md) — Tokens específicos de dashboard
