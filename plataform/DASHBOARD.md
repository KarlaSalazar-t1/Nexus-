# DASHBOARD.md — Contexto de plataforma: Admin / Backoffice

> Este archivo documenta los tokens, reglas y componentes exclusivos del **admin y backoffice** del ecosistema T1.  
> **No aplica** en landing pages públicas.  
> Para el contexto opuesto, ver [`platforms/LANDING.md`](./LANDING.md).

---

## Diferencias clave vs Landing

| Propiedad | Dashboard | Landing |
|---|---|---|
| Tipografía headings | Manrope SemiBold / Bold | Sora Light 300 / Regular 400 |
| Tipografía cuerpo | Manrope Regular | Inter Regular / Medium |
| Contenedor principal | `1600px` | `1018px` |
| Border radius cards | `10px`–`20px` | `24px` |
| Border radius botones | `8px` | `18px` |
| Altura botones | variable | `45px` |
| Color botón primario | `#DB3B2B` (Red 500) | `#E26153` (Red 600) |
| Sombra cards | `0 0 5px 1px rgba(0,0,0,0.1)` | `0 0 25px 2px rgba(0,0,0,0.06)` |
| Sidebar | `284px`, `border-radius: 18px` | No aplica |
| Fondo header | Blanco sólido | Glass semitransparente |

---

## 1. Tipografía

El dashboard usa **Manrope** como única familia tipográfica. Sora e Inter están **prohibidas** en este contexto.

### Escala completa

| Nombre | Tamaño | Peso | Uso |
|---|---|---|---|
| Display 2XL | `72px` | Bold 700 | Solo para landing — no usar en dashboard |
| Display XL | `60px` | Bold 700 | Páginas de marketing internas excepcionales |
| Display Large | `48px` | Bold 700 | Títulos de página principal |
| Medium Large | `36px` | SemiBold 600 | Subtítulos prominentes, métricas grandes |
| Semi Medium | `28px` | SemiBold 600 | Encabezados de sección |
| Title Base | `24px` | SemiBold 600 | Títulos de card, headers de panel |
| Standard | `22px` | Medium 500 | Table headers, etiquetas destacadas |
| Small | `18px` | Medium 500 | Subtítulos, nav items |
| XS | `16px` | Regular 400 | Cuerpo de texto, descripciones |
| 2XS | `14px` | Regular 400 | Body principal, inputs, labels |
| Micro | `12px` | Regular 400 | Captions, badges, helper text |

**Line-height:** `1.366em` para toda la escala Manrope.

### Pesos válidos

| Peso | Uso |
|---|---|
| Regular 400 | Cuerpo de texto, valores en inputs, descripciones |
| Medium 500 | Labels, nav items, table headers |
| SemiBold 600 | Títulos de card, encabezados de sección, CTA |
| Bold 700 | Títulos de página, métricas destacadas, headings principales |

### Color de texto

| Rol | Hex | Uso |
|---|---|---|
| Primary (Oxford) | `#4C4C4C` | Texto principal, body copy |
| Dark | `#1F2937` | Headings, labels enfáticos |
| Secondary | `#737373` | Texto secundario, placeholders |
| Disabled | `#A3A3A3` | Texto deshabilitado |
| Inverse | `#FFFFFF` | Texto sobre fondos oscuros o primarios |
| Link | `#2180FF` | Links interactivos |

### Anti-patrones tipográficos

- ❌ Sora en cualquier elemento de dashboard
- ❌ Inter en cualquier elemento de dashboard
- ❌ Texto en rojo (`#DB3B2B` o `#E26153`) para acentos decorativos — en dashboard el rojo comunica error o estado crítico
- ❌ Pesos fuera de los 4 válidos (400/500/600/700)

---

## 2. Layout y contenedor

### Contenedor principal

| Breakpoint | Content Width | Page Padding | Sidebar |
|---|---|---|---|
| Mobile `360px` | `100% - 32px` | `16px` | Oculto / Drawer |
| Tablet `768px` | `100% - 32px` | `24px` | Colapsado |
| Desktop `1280px`+ | `1600px` | `160px` | `284px` expandido |

> El canvas de Figma es `1440px` pero el target real de usuarios es `1280px`–`1366px`. El contenedor de `1600px` se centra con `mx-auto` y tiene padding lateral que absorbe las pantallas intermedias.

### Grid interno

| Propiedad | Valor |
|---|---|
| Content gap | `28px` |
| Sidebar width | `284px` expandido |
| Sidebar collapsed | Solo íconos, sin labels |
| Sidebar mobile | Drawer full-height, overlay |

### Estructura base de página

```tsx
<div className="flex min-h-screen bg-[#F8F8F8]">
  {/* Sidebar */}
  <aside className="w-[284px] shrink-0 rounded-[18px] bg-white shadow-[2px_0px_8px_rgba(0,0,0,0.08)]">
    {/* navegación */}
  </aside>

  {/* Main content */}
  <main className="flex-1 overflow-auto">
    <div className="mx-auto max-w-[1600px] px-[160px] py-8">
      {/* contenido */}
    </div>
  </main>
</div>
```

---

## 3. Botones

| Propiedad | Primario | Secundario |
|---|---|---|
| Background | `#DB3B2B` | `transparent` / `white` |
| Texto | `#FFFFFF` | `#4C4C4C` (Oxford) |
| Border | ninguno | `1px solid #D9D9D9` |
| Border Radius | `8px` | `8px` |
| Fuente | Manrope SemiBold 600 | Manrope SemiBold 600 |
| Hover bg | `#CC0000` (Red 900) | `#F8F8F8` (Gray 50) |
| Active bg | `#CC0000` opacidad 0.9 | `#F2F2F2` (Gray 100) |
| Disabled | `#A3A3A3`, texto blanco | Border `#E5E5E5`, texto `#A3A3A3` |

### Variantes adicionales

| Variante | Descripción | Uso |
|---|---|---|
| Link | Sin borde/fondo, texto azul o rojo | Acciones terciarias, navegación inline |
| Split | Botón dividido con dropdown arrow | Acciones con múltiples opciones |
| Icon | Solo ícono, sin texto | Toolbars, acciones compactas |
| IA | Estilo diferenciado (violeta) | Acciones de inteligencia artificial |
| Social | Login con proveedor (Google, etc.) | Autenticación con terceros |

---

## 4. Border Radius

| Componente | Radius |
|---|---|
| Sidebar / Panels | `18px` |
| Cards grandes | `20px` |
| Cards medianas | `13px` |
| Cards / Modales | `10px` |
| Inputs / Buttons | `8px` |
| Badges / Tags | `4px` |

---

## 5. Sombras del sistema

El dashboard tiene **solo 3 sombras**. No hay más variantes.

| Nombre | Valor CSS | Uso |
|---|---|---|
| Shadow Card | `0px 0px 5px 1px rgba(0,0,0,0.1)` | Cards, modales, paneles |
| Shadow Dropdown | `0px 4px 8px rgba(0,0,0,0.12)` | Dropdowns, popovers, tooltips |
| Shadow Sidebar | `2px 0px 8px rgba(0,0,0,0.08)` | Menú lateral |

> ❌ Dropdowns y sidebar **no** tienen shadow card. Cada elemento usa solo su sombra correspondiente.  
> ❌ No usar las sombras de landing (`0 0 25px 2px rgba(0,0,0,0.06)`) en dashboard.

---

## 6. Colores semánticos (uso en dashboard)

En dashboard el color comunica estado funcional. El rojo **siempre** indica error o acción destructiva — nunca decoración.

| Rol | Color | Hex | Uso |
|---|---|---|---|
| Primario / CTA | Red 500 | `#DB3B2B` | Botones primarios, tab activa, sidebar selected |
| Error / Destructivo | Red 900 | `#CC0000` | Errores, eliminaciones, estados críticos |
| Error BG | Red 50 | `#FEF4F4` | Background de alertas de error, input error |
| Success | Green 500 | `#4FC153` | Confirmaciones, pagos exitosos, stock |
| Success BG | Green 100 | `#F0FDF4` | Background alertas de éxito |
| Warning | Orange 500 | `#FF6700` | Acciones que requieren atención |
| Warning BG | Orange 100 | `#FFF0E5` | Background alertas de advertencia |
| Caution | Yellow 500 | `#EDBD55` | Estados pendientes, precaución |
| Info / Links | Blue 500 | `#2180FF` | Links, selección activa, badges info |
| Info BG | Blue 100 | `#F0F8FF` | Background informativo, table headers (`#F4F8FF`) |
| Disabled Text | Gray 400 | `#A3A3A3` | Texto deshabilitado |
| Disabled BG | Gray 100 | `#F2F2F2` | Background deshabilitado |
| Overlay modal | — | `rgba(0,0,0,0.6)` | Overlay de modales |

### Fondos de página y superficies

| Superficie | Hex | Uso |
|---|---|---|
| Page background | `#F8F8F8` | Fondo general de la app |
| Card / Panel | `#FFFFFF` | Cards, modales, sidebar |
| Table header | `#F4F8FF` | Encabezado de tabla |
| Input default | `#FFFFFF` | Campo vacío o en uso |
| Input disabled | `#F2F2F2` | Campo deshabilitado |
| Border default | `#D9D9D9` | Bordes de inputs, dividers |
| Border hover | `#A3A3A3` | Hover en inputs |

---

## 7. Sidebar

El sidebar es el elemento de navegación principal del dashboard.

| Propiedad | Valor |
|---|---|
| Ancho expandido | `284px` |
| Border Radius | `18px` |
| Background | `#FFFFFF` |
| Shadow | `2px 0px 8px rgba(0,0,0,0.08)` |
| Fuente nav items | Manrope Medium 500, 14px |

### Estados de ítem de menú

| Estado | Background | Texto | Indicador |
|---|---|---|---|
| Default | Transparente | `#4C4C4C` | — |
| Hover | `#F8F8F8` | `#4C4C4C` | — |
| Selected (main) | Highlight sutil | `#DB3B2B` | Borde izq Red 500 |
| Selected (sub) | Highlight sutil | `#4C4C4C` Bold | — |

### Comportamiento responsive

| Breakpoint | Comportamiento |
|---|---|
| Desktop `1280px`+ | Visible, expandido `284px` |
| Tablet `768px` | Colapsado — solo íconos, sin labels |
| Mobile `360px` | Oculto. Se abre como drawer full-height con overlay |

---

## 8. Inputs y formularios

**Tipografía:** Manrope en todos los estados.

| Elemento | Tamaño | Peso |
|---|---|---|
| Label | `14px` | Medium 500 |
| Value / Input text | `14px` | Regular 400 |
| Placeholder | `14px` | Regular 400, `#A3A3A3` |
| Helper text | `12px` | Regular 400 |

### Estados de input

| Estado | Border | Background | Label |
|---|---|---|---|
| Default | `#D9D9D9` | `#FFFFFF` | `#4C4C4C` |
| Focus | `#2180FF` | `#FFFFFF` | `#2180FF` |
| Error | `#CC0000` | `#FEF4F4` | `#CC0000` |
| Disabled | `#E5E5E5` | `#F2F2F2` | `#A3A3A3` |
| Success | `#4FC153` | `#FFFFFF` | `#4FC153` |
| Read Only | `#E5E5E5` | `#F8F8F8` | `#737373` |

Border radius: `8px` en todos los estados.

---

## 9. Tablas

Las tablas son el patrón de visualización de datos más común en dashboard.

| Propiedad | Valor |
|---|---|
| Table header bg | `#F4F8FF` |
| Header texto | Manrope SemiBold 600, `14px`, `#4C4C4C` |
| Row texto | Manrope Regular 400, `14px`, `#4C4C4C` |
| Row hover | `#F8F8F8` |
| Row selected | `#F0F8FF` con border-left `#2180FF` |
| Border separador | `1px solid #E5E5E5` |
| Border radius tabla | `10px` en contenedor |

Ver documentación completa en [`components/TABLES.md`](../components/TABLES.md).

---

## 10. Alertas y mensajes del sistema

| Variante | Background | Border | Texto |
|---|---|---|---|
| Success | `#F0FDF4` | `#4FC153` | `#4C4C4C` |
| Error | `#FEF4F4` | `#CC0000` | `#4C4C4C` |
| Warning | `#FFF0E5` | `#FF6700` | `#4C4C4C` |
| Info | `#F0F8FF` | `#2180FF` | `#4C4C4C` |

---

## 11. Modales

| Propiedad | Valor |
|---|---|
| Border Radius | `10px` |
| Shadow | `0px 0px 5px 1px rgba(0,0,0,0.1)` |
| Overlay | `rgba(0,0,0,0.6)` |
| Fondo | `#FFFFFF` |
| Ancho típico | `480px`–`640px` |

Los modales siempre usan doble confirmación para acciones destructivas (eliminar, cancelar, revocar acceso).

---

## 12. Badges y estados

| Tipo | Color | Uso |
|---|---|---|
| Success | Green 500 `#4FC153` / BG Green 100 | Activo, completado, pagado |
| Warning | Orange 500 `#FF6700` / BG Orange 100 | Pendiente, en revisión |
| Caution | Yellow 500 `#EDBD55` / BG Yellow 100 | Precaución, en espera |
| Error | Red 900 `#CC0000` / BG Red 50 | Error, cancelado, rechazado |
| Info | Blue 500 `#2180FF` / BG Blue 100 | Informativo, en proceso |
| Neutral | Gray 500 `#737373` / BG Gray 50 | Inactivo, archivado |
| Premium | Gold 500 `#EDBD55` con corona | Plan avanzado, feature premium |

Border radius: `4px` en todos los badges.

---

## 13. Tabs

| Propiedad | Valor |
|---|---|
| Tab activa | Indicador inferior en Red 500 (`#DB3B2B`) |
| Fuente | Manrope Medium 500, `14px` |
| Color activo | `#DB3B2B` |
| Color inactivo | `#737373` |
| Hover | `#4C4C4C` |

---

## 14. Estructura de componente estándar

```tsx
"use client"; // solo si tiene interactividad

import { DATOS } from "@/lib/constants";

export default function T1NombreComponente() {
  return (
    <div className="rounded-[10px] bg-white p-6 shadow-[0px_0px_5px_1px_rgba(0,0,0,0.1)]">
      <h2 className="font-manrope text-[24px] font-semibold text-[#1F2937]">
        Título
      </h2>
      {/* contenido */}
    </div>
  );
}
```

**Naming:** `T1` + PascalCase — ej. `T1OrdersTable`, `T1DashboardStats`, `T1SidebarNav`.  
**Contenido:** Todo texto va en `src/lib/constants.ts`. Nunca hardcodear contenido en el componente.

---

## 15. Anti-patrones de dashboard

| Anti-patrón | Corrección |
|---|---|
| Usar `#E26153` (Red 600) como color primario | En dashboard el primario es `#DB3B2B` (Red 500) |
| Rojo decorativo en texto o acentos | En dashboard el rojo comunica error — usar solo en estados de error o CTA primario |
| Contenedor `max-w-[1018px]` | Dashboard usa `max-w-[1600px]` |
| Border radius `24px` en cards | Cards de dashboard: `10px`–`20px` |
| Border radius `18px` en botones | Botones de dashboard: `8px` |
| Sora o Inter en cualquier elemento | Dashboard es exclusivamente Manrope |
| Sombras de landing (`0 0 25px...`) | Usar solo las 3 sombras del sistema dashboard |
| Sidebar con shadow card | Sidebar usa su shadow propia: `2px 0px 8px rgba(0,0,0,0.08)` |
| Table header en blanco | Table header siempre en `#F4F8FF` |
| Glassmorphism, glow blobs, mesh gradient | Elementos decorativos de landing — no aplican en dashboard |

---

## 16. Checklist de QA — Pre-deployment

**Tipografía**
- [ ] Toda la interfaz usa Manrope (nunca Sora ni Inter)
- [ ] Pesos solo: Regular 400, Medium 500, SemiBold 600, Bold 700
- [ ] Labels de input: Medium 500, 14px
- [ ] Body / values: Regular 400, 14px
- [ ] Helper text: Regular 400, 12px

**Colores**
- [ ] Botón primario: `#DB3B2B` (nunca `#E26153`)
- [ ] Rojo solo en: botón primario, sidebar selected, estados de error/destructivo
- [ ] Table header bg: `#F4F8FF`
- [ ] Page background: `#F8F8F8`
- [ ] Cards y panels: `#FFFFFF`

**Layout**
- [ ] Contenedor: `max-w-[1600px]` (nunca `1018px`)
- [ ] Sidebar: `284px` expandido, colapsado en tablet, drawer en mobile
- [ ] Page padding desktop: `160px` lateral

**Componentes**
- [ ] Border radius cards: `10px`–`20px` según tamaño
- [ ] Border radius inputs y botones: `8px`
- [ ] Border radius sidebar: `18px`
- [ ] Shadow cards: `0px 0px 5px 1px rgba(0,0,0,0.1)`
- [ ] Overlay modales: `rgba(0,0,0,0.6)`
- [ ] Acciones destructivas con modal de doble confirmación

**Estados**
- [ ] Todos los inputs tienen los 6 estados documentados
- [ ] Focus state: outline `#2180FF` 2px en todos los interactivos
- [ ] Empty states con ilustración + texto + CTA
- [ ] Loading: skeleton para contenido largo, spinner para acciones puntuales

**Accesibilidad**
- [ ] Focus visible en todos los elementos interactivos
- [ ] Touch targets mínimo `44px` en mobile
- [ ] Contraste suficiente en todos los textos (ver `accessibility/A11Y.md`)

---

## Referencias

- [`foundation/COLORS.md`](../foundation/COLORS.md) — Paleta completa y tokens semánticos
- [`foundation/TYPOGRAPHY.md`](../foundation/TYPOGRAPHY.md) — Escala tipográfica del sistema
- [`foundation/SPACING.md`](../foundation/SPACING.md) — Escala de spacing
- [`foundation/ELEVATION.md`](../foundation/ELEVATION.md) — Sombras y border-radius completos
- [`foundation/LAYOUT.md`](../foundation/LAYOUT.md) — Grid, breakpoints, responsive
- [`components/ATOMS.md`](../components/ATOMS.md) — Botones, inputs, badges, switches
- [`components/TABLES.md`](../components/TABLES.md) — Tablas de datos: header, filas, paginación, sorting
- [`components/STATES.md`](../components/STATES.md) — 10 estados obligatorios
- [`accessibility/A11Y.md`](../accessibility/A11Y.md) — WCAG AA, contraste, ARIA
- [`platforms/LANDING.md`](./LANDING.md) — Contexto opuesto: landing pages públicas
- [`workflows/CLAUDE-CONTROLLER.md`](../workflows/CLAUDE-CONTROLLER.md) — Entry point para Claude
