# Cruce Nexus ↔ t1components ↔ Phoenix (l3-nexus-react)

> Inventario para la migración del design system a Phoenix (`libs/shared/nexus`). Compara tres estados: lo que Figma/Nexus documenta como canon, lo que `t1components` implementa realmente en código, y lo que ya existe como skeleton en `l3-nexus-react`.

**Contexto oficial (Phoenix `docs/legacy-inventory/README.md`):**
> "T1 components (design system)" → **Nexus** (`libs/shared/nexus`) · Phase A: **⬜ Pending** · Owner: **Karla Salazar** · *"t1components is the legacy DS; migration = absorb into Nexus, no standalone lib"*

No hay ingeniero de plataforma asignado explícitamente a esta línea en `developers.md`. El candidato natural del lado de ingeniería es **Mario Alberto Cárdenas Ramírez** (Technical Lead — Frontend, Cross-cutting/client tier), quien aparece como responsable de facto en casi todas las líneas de frontend transversal del inventario.

---

## 1. El canon importado a Phoenix está desactualizado

`libs/shared/nexus/documentation/canon/` es una copia de este mismo repo, importada como **v2.2.0** (2026-05-06), traducida al inglés. Este repo está hoy en **v2.5.0** (2026-09-03). Falta:

| Versión no importada | Contenido |
|---|---|
| 2.3.0 | Rename `STOREFRONT.md` → `PERFIL-DE-CLIENTE.md` |
| 2.4.0 | `LANDING-COMPONENTS.md`, `METRICS.md`, actualización de `LANDING.md` |
| 2.5.0 | Toda la familia de archivos de App (`APP.md`, `APP-FLOWS.md`, `reference-app.md`) + limpieza de `T1APP.md` |

Confirmado: `canon/platform/` en Phoenix solo tiene `DASHBOARD.md` y `LANDING.md` — no existe `APP.md`.

---

## 2. Íconos — la brecha más grande (ver análisis detallado previo)

| | Nexus/Figma | `t1components` |
|---|---|---|
| Definidos | 222 | 728 archivos físicos, **248 exportados** (480 huérfanos) |
| Coincidencia de nombre | — | **18 de 222 (8%)** |

170 archivos `RectangleIcon{N}.svg` + 159 `ArrowIcon{N}.svg` = 45% del total sin nombre real. Logos: 93 en Figma vs. 42 exportados en código (todos los físicos sí se exportan, pero es menos de la mitad de lo que Figma documenta).

---

## 3. Átomos / Moléculas / Organismos — el hallazgo clave

Comparación de nombres entre los **52 componentes de `t1components`** (el código real, "legacy DS") y los **32 componentes del skeleton `l3-nexus-react`** en Phoenix:

### Coinciden (5 de 32 — 16%)

| `l3-nexus-react` | `t1components` | Confianza |
|---|---|---|
| `Button` | `Button` | Exacta |
| `Checkbox` | `CheckBox` | Exacta (case) |
| `Switch` | `Switch` | Exacta |
| `Select` | `select` / `SelectAtom` | Exacta |
| `PageHeader` | `PageHeader` | Exacta |

### Semánticamente parecidos, nombre distinto (revisar antes de dar por sentado que son el mismo)

| `l3-nexus-react` | Posible equivalente en `t1components` |
|---|---|
| `DataTable` | `Table` / `AdaptiveTable` |
| `Dialog` | `SimpleModal` |
| `Pagination` | `CustomPagination` |
| `RowActionsMenu` | `ActionMenu` |

### Sin ningún equivalente en `t1components` (23 de 32 — 72%)

`Alert`, `AnnouncementBar`, `Avatar`, `Badge`, `Banner`, `Collage`, `EmptyState`, `FallbackImage`, `Hero`, `IconButton`, `ImageWithText`, `Input`, `RichText`, `SectionStack`, `SurfaceCard`, `T1FinalCTA`, `T1LifestyleCards`, `Tabs`, `Tag`, `Textarea`, `Toast`, `ToastProvider`.

**Patrón claro:** `Hero`, `Collage`, `ImageWithText`, `RichText`, `SectionStack`, `AnnouncementBar`, `T1FinalCTA`, `T1LifestyleCards`, `SurfaceCard` son componentes **de landing** — coinciden en forma con `patterns/LANDING-COMPONENTS.md`, no con nada de `t1components` (que no tiene ni una sola pieza de landing). El skeleton de `l3-nexus-react` parece haberse poblado a partir del **canon/documentación de Nexus** (landing + átomos genéricos), **no a partir del código real de `t1components`**.

### Lo que le falta a `l3-nexus-react` — componentes de `t1components` con cero presencia en el skeleton

`ActionMenu`* , `AdaptiveTable`*, `AmountInput`, `Autocomplete`, `BalanceBanner`, `Card`, `Chip`, `CloseButton`, `CollapsibleCardT1`, `ColorPicker`, `ConfirmationDialog`, `CustomAmountInput`, `CustomInput`, `DatePicker`, `DynamicSelector`, `ItemLink`, `LayoutMenu`, `LineProgress`, `Loader`, `Messages`, `Navbar`, `PercentageInput`, `PhoneInputT1`, `ProductCheckList`, `ProductImage`, `ProductList`, `ProductPrice`, `ProductStockIndicator`, `Profile`, `Radio`, `Searchinput`, `SettingsCard`, `Sidebar`, `StoreSelector`, `StoreSelectorOnSidebar`, `T1Selector`, `T1ShippingBanner`, `TableItem`, `TextFieldAndButton`, `Tooltip`

*(con posible equivalente parcial, ver tabla de arriba)

**Es decir: ninguno de los componentes específicos del dominio T1 — `ProductList`, `StoreSelector`, `BalanceBanner`, `T1ShippingBanner`, `DatePicker`, `Sidebar`, `Navbar`, etc. — existe todavía en el skeleton de Phoenix.** La "absorción de t1components en Nexus" que describe el README de Phoenix **no ha empezado a nivel de componente**, solo existe la carpeta y unos ~30 componentes genéricos/landing de relleno.

---

## 4. Conclusión — qué es realmente "el inventario"

1. **El skeleton `l3-nexus-react` no es un punto de partida útil para migrar `t1components`.** Trae landing + primitivos genéricos, no los componentes de negocio reales (Dashboard/App). Migrar no es "completar el skeleton" — es traer los ~40+ componentes reales de `t1components` desde cero, y decidir caso por caso si los ~5 que coinciden por nombre (`Button`, `Checkbox`, `Switch`, `Select`, `PageHeader`) se reutilizan o se reemplazan.
2. **El naming es la primera decisión, no la última.** Antes de portar código, hay que resolver el mismo problema que `HOMOLOGACION.md` ya diagnosticó en Figma: qué nombre final tiene cada componente. Migrar `t1components/Table` a Phoenix con el nombre `DataTable` (ya ocupado por otra cosa en el skeleton) o con su nombre propio es una decisión de una sola vez — hacerla mal la primera vez duplica el trabajo.
3. **`icons.ts` de Nexus (222, ya normalizado) es más confiable que ambos lados de código** — ni los 728 archivos de `t1components` ni el `Icon.tsx` de `l3-nexus-react` tienen ese nivel de curación. Migrar los íconos desde `icons.ts` (no desde `t1components`) evita arrastrar los 480 huérfanos y el ruido de `RectangleIcon`/`ArrowIcon`.

## 5. Siguiente paso sugerido

Compartir este cruce con **Karla Salazar** (owner formal) y **Mario Cárdenas** (probable owner técnico) antes de escribir una sola línea de componente en `l3-nexus-react` — la fila sigue en ⬜ Pending en el inventario de Phoenix, así que no hay trabajo en curso que se pise.
