# LANDING-COMPONENTS.md — Catálogo de componentes de landing

> Componentes y variantes de las landing pages públicas del ecosistema T1.
> Agrupados por **familia estructural** (no por el contenido que muestran hoy).
> Cada componente lista **usos sugeridos abiertos** — cómo se ha usado, sin limitarlo a eso.
>
> **Fuente de verdad:** repo `KarlaSalazar-t1/T1landing` (`src/components/*`). No hay Figma.
> **Tokens** → `platforms/LANDING.md` + `LANDING-TOKENS-DELTA.md`.
> **Secuencia en página** → `patterns/LANDING-SECTIONS.md`.
> **Owner:** Karla Salazar — Head of UX/UI
>
> **Estado v3:** estructura, mapeo a archivo, usos, **tokens reales** y **responsive** = extraídos del repo.
> **Objetivo:** que este catálogo + `LANDING.md` (tokens) + `LANDING-SECTIONS.md` (secuencia) permitan
> generar un landing con el estilo T1 desde un solo prompt. Por eso cada componente lleva tokens + layout + responsive.

---

## Leyenda

- **Archivo:** componente(s) real(es) en `src/components/`.
- **Usos sugeridos:** patrones observados, no restrictivos.
- **§N sin prefijo** = sección de `platforms/LANDING.md` (ej. "§11" = `LANDING.md §11 — Componentes de landing`).
- **Procedencia:** 🧬 heredado del doc anterior · ✨ nuevo (salió del repo).
- 🔴 = valor de token por confirmar (ya no quedan).

---

## Responsive — reglas del sistema

**Mobile-first:** las clases base son mobile; el prefijo **`tablet:`** (≥768px) aplica desktop; `lg:` (≥1280px) refina. Breakpoints `mobile 360 / tablet 768 / desktop 1280 / wide 1920` (ver `LANDING.md §2`).

**Patrones transversales:**

| Aspecto | Mobile (base) | Desktop (`tablet:`) |
|---|---|---|
| Grids de sección | `grid-cols-1` (stack vertical) | `tablet:grid-cols-2/3` o `grid-cols-[fracciones]` |
| Split título + contenido | stack (título arriba) | 2 columnas (título izq / contenido der) |
| Escala tipográfica | H `28–32px`, body `14–16px` | H `44–60px` (`lg:`), body `16–18px` |
| Padding de sección | `px-5 py-[100px]` | `tablet:px-10 tablet:py-[128px]` |
| Espaciados (padding/margin/gap) | **múltiplos de 4px** | múltiplos de 4px |
| Contenedor | `max-w-[var(--max-w)]` (1220) + `px-5` | `px-6/10` |
| Mostrar/ocultar | `tablet:hidden` (solo mobile) · `hidden tablet:block` (solo desktop) | — |

**Por componente (comportamiento no obvio):**
- **Hero:** `min-h-[86svh]` mobile → `tablet:h-[88vh]`; heading `28 → 48 → 60px`.
- **Mega-menú:** desktop = dropdown (`hidden tablet:block`); mobile = panel full-screen deslizable (`tablet:hidden`, `fixed inset-0 top-[60px]`) + hamburguesa. Barra `60px`.
- **Tabs auto-rotación (7.1b):** desktop tabs izq + contenido der; mobile stack.
- **Carruseles:** scroll horizontal por gesto en mobile; flechas / dots en desktop.
- **Grids de card:** `grid-cols-1` → `tablet:grid-cols-2/3`.
- **Footer:** 1 columna (stack) en mobile → multi-columna en desktop.
- **Blobs / glass / overlay:** iguales; los blobs pueden reducir tamaño en mobile.

---

## 1. Hero

### 1.1 Hero centrado
- **Archivo:** base de `patterns/LANDING-SECTIONS.md` (§Hero)
- **Descripción:** título + subtítulo + CTAs sobre fondo con blobs decorativos.
- **Usos sugeridos:** aperturas simples de cualquier página.

### 1.2 Hero oscuro (landing principal)
- **Archivo:** `T1Hero.tsx`
- **Descripción:** hero **oscuro** con degradado + glows radiales; texto blanco, CTAs y (opcional) campo de input IA.
- **Usos sugeridos:** apertura del landing principal.
- **Tokens:** sección `min-h-[92svh]` / `tablet:min-h-screen`. Fondo `linear-gradient(180deg, #0e0d0d 0%, #020101 100%)` + glows radiales rojo `rgba(112,10,10,..)` y azul `rgba(3,20,70,..)`. Heading `font-sora` blanco. CTA `h-[50px] rounded-[23px] bg-[#DB3B2B]` hover `#C0332A`. Campo input `rounded-[14px] bg-[#1D1D1D] text-white`.
- **Nota:** el video full-bleed es **opcional**, no obligatorio; el estándar es el degradado oscuro. Texto **siempre blanco** (el hero siempre es oscuro).

### 1.3 Hero dividido con panel (sublanding)
- **Archivo:** heros de `T1Productos`, `T1POS`, `T1Multipaqueteria`, `T1ControlCalidad`, `T1ReportesLogisticos`, `T1LinksDePago`, `T1PagosEnLinea`, `T1Marketplaces`
- **Descripción:** sobre **fondo oscuro**, copy + CTA (texto **blanco**) a un lado y **panel visual** (cards blancas) al otro. El panel es intercambiable.
- **Usos sugeridos:** mostrar el producto "en acción", features, comparativas — es el hero por defecto del sublanding.
- **Tokens:** fondo = **degradado oscuro similar al hero principal** (base `180deg #0e0d0d→#020101` + glows rojo/azul + fade a negro). *Variante actual en algunas páginas: `linear-gradient(135deg, #261515→#1A0A0A→#261515)` — a unificar.* Texto blanco. Padding `px-5 pt-28 pb-16` → `tablet:px-10 tablet:pt-36 tablet:pb-24`.
- **Variantes de panel:** product cards · phone/POS · dashboard + stat cards · stat cards + chart · fila de logos/carriers.

### 1.4 Hero con campo interactivo
- **Archivo:** `T1AISectionV2.tsx` + `showcase/TiendaPromptPanel.tsx`
- **Descripción:** el elemento central es un **control en vivo** (textarea + contador + chips).
- **Usos sugeridos:** demos, generación IA, calculadoras, cualquier "pruébalo desde el inicio".
- **Tokens:** campo `rounded-[18px] border rgba(0,0,0,0.08) bg-white`. Contador `text-[9px] text-black/35`, `maxLength 500`. Chips `rounded-full bg-black/[0.04] px-2.5 py-1 text-[9px] font-medium`. Botón enviar circular `rounded-full`.

### 1.6 Hero con cards glass sobre imagen
- **Archivo:** `T1Reclamaciones.tsx`, `T1Reportes.tsx`, `T1ReportesLogisticos.tsx`  ✨ nuevo
- **Descripción:** texto a la izquierda + **cards glass (blanco translúcido) escalonadas sobre una imagen/gráfico** de fondo (ej. `contracargo-hero.png`).
- **Usos sugeridos:** heros de producto data-heavy (reportería, disputas) donde las cards muestran métricas/estados sobre un visual.
- **Tokens:** cards glass radio `12` + sombra sutil; imagen `drop-shadow(0 24px 50px rgba(0,0,0,0.5))`, posicionada con overflow (`right/top` negativos, `width ~104%`).
- **Responsive:** en móvil las cajas/cards se ocultan o reordenan (ej. Control calidad, Reportes).

---

## 2. Cards

### 2.1 Card con ícono
- **Archivo:** `T1POS.tsx` — sección "Tu sucursal, lista para vender" (sublanding `punto-de-venta`). Mismo patrón en otros grids de feature.
- **Descripción:** **ícono de línea negro directamente sobre la card** (sin contenedor de color) + título + texto.
- **Usos sugeridos:** beneficios, capacidades, cualquier set de 3–6 ideas equivalentes.
- **Tokens:** card `rounded-[16px] border border-black/[0.07] bg-white p-6` shadow `0 4px 20px rgba(0,0,0,0.04)`; ícono `24×24` línea `stroke #111827 1.6`, en contenedor `h-[40px] w-[40px]` **sin fondo**; título `font-sora 16px`, desc `font-inter 13px light`.
- ⚠️ El modelo `LANDING.md §11` ("ícono rojo en contenedor `#FEF4F4`") quedó **obsoleto**: hoy el ícono es negro y sin contenedor de color.

### 2.1b Card glass con glow + imagen (Vende/Cobra/Envía)
- **Archivo:** `T1FeatureIntro.tsx`  ✨ vigente
- **Descripción:** card glass con glow de color que contiene **label + descripción + imagen** (`card-vende-v2.png`, `card-pagos-v2.png`, `card-envia-v2.png`). Es la sección Vende/Cobra/Envía actual.
- **Usos sugeridos:** features destacados con imagen sobre fondo oscuro, agrupaciones de producto.
- **Tokens:** `rounded-[12px]` (compacta) / `rounded-[15px]` (grande); `boxShadow 0 14px 34px rgba(0,0,0,0.5), 0 0 58px -22px {glow}40`; glow rojo `#E0402F` / azul `#2F6BFF`; label `text-[16–20px] uppercase tracking-[0.04em] white`.

### 2.2 Card con imagen
- **Archivo:** grids image-led (ej. "Todo incluido desde el día uno" en `tienda-con-ia`; "Todo para administrar" en `T1Productos`; `TodoIncluidoDark`)
- **Descripción:** card **estática** que lidera con imagen renderizada + título + 1 línea. Es un **tipo de card**, **no un carrusel** — se usa en **grids** de 3–6. *(El carrusel de features es 3.1 / 3.3; estas cards pueden ir dentro de uno.)*
- **Usos sugeridos:** features, diferenciadores, "todo incluido" — cualquier set visual.
- **Tokens:** card blanca `rounded-[16–20px] border border-black/[0.06–0.07] bg-white`; imagen interna `rounded-[14px]`; sombra `0 4px 20px rgba(0,0,0,0.04–0.05)`.

### 2.3 Card de texto
- **Archivo:** `T1Problema.tsx`
- **Descripción:** solo título + párrafo, sin imagen ni ícono.
- **Usos sugeridos:** problemas/dolores, comparaciones, principios — cualquier set narrativo.

### 2.4 Card de elección
- **Archivo:** mega-menú `T1Navbar` — "¿Cómo quieres empezar?" (Emprendedor → `/registro`, PyME → `/precios`, Enterprise → `/contacto-ventas`)
- **Descripción:** card clicable que **sí navega** a distinto destino (título + descripción + chevron).
- **Usos sugeridos:** ramificar por intención/audiencia hacia distintos destinos, elegir producto.
- ⚠️ No confundir con las **tabs de audiencia (7.1b)**, que cambian foco pero **no navegan**.

### 2.5 Card de plan (tiers)
- **Archivo:** `T1Pricing.tsx`
- **Descripción:** columna con precio, features y CTA; soporta "Recomendado".
- **Usos sugeridos:** pricing, planes, paquetes, niveles.
- ⚠️ Reconciliar con §14 (anti-patrón "pricing table simétrica"): hoy existe y se usa.
- **Tokens:** card `rounded-[20px] border border-black/[0.06] bg-white`, hover `border-black/[0.12]` + `shadow-[0_4px_30px_rgba(0,0,0,0.06)]`. Precio `font-sora 24→28px light`. Badge tier `rounded-full bg-black/[0.05] text-[11px] uppercase tracking-[0.06em]`. Badge "Recomendado" `rounded-[6px] px-2 py-0.5 text-[11px] font-semibold`.

### 2.6 Card con cita
- **Archivo:** `T1EnterpriseCarousel.tsx` / `T1Enterprise.tsx`
- **Descripción:** imagen-still con **botón de play centrado** + métrica destacada + quote + atribución.
- **Usos sugeridos:** casos de éxito, reseñas, logros, prueba social.
- **Tokens:** sección `bg-[#0F0E0D]`; card `rounded-[22px]`, ancho carrusel `82% / tablet 62%`, alto `tablet:460px`; imagen `h-[200px]`; logo chip `rounded-[11px] bg-white shadow 0 3px 10px rgba(0,0,0,0.22)`; botón play `play-circle.svg` `56×56` centrado sobre la imagen, `drop-shadow(0 4px 16px rgba(0,0,0,0.45))`; métrica `font-sora 26px semibold white`; quote `text-[13px] italic white/70`.

### 2.7 Card glass (sobre oscuro)
- **Archivo:** `GlassProductCard.tsx`
- **Descripción:** card translúcida sobre fondo oscuro.
- **Usos sugeridos:** ecosistema, secciones dark, destacados.
- **Tokens:** `.glass-card` radius `24px` · `backdrop-blur(32px) saturate(1.4)` · inset shadows + `0 8px 32px rgba(0,0,0,0.12)`
- ✅ Usa **Manrope** — es una card que imita el producto real (excepción acotada de paneles simulados, ver §4 y `LANDING.md §1`).

---

## 3. Secuencias de cards

### 3.1 Stack cards (paginado)
- **Archivo:** `T1Solutions.tsx` (contador "1/5", slides con `label`/`description`/`panel`)
- **Descripción:** cards paginadas con avance/contador; cada una = copy + visual grande.
- **Usos sugeridos:** presentar **distintos productos o plataformas**, features destacados, pasos de un flujo — no se limita a features.

### 3.2 Sticky-scroll glass cards
- **Archivo:** `T1ScrollShowcase.tsx` (Vende/Cobra/Envía/Todo en uno)
- **Descripción:** cards glass que se auto-inclinan (`cardTilt` + `blobMove`) ancladas por scroll.
- **Usos sugeridos:** narrativa secuencial de capacidades, storytelling de producto.
- **Tokens:** `cardTilt 6s` · `blobMove 8s` · ✅ Manrope (excepción de panel simulado).

### 3.3 Carrusel horizontal
- **Archivo:** `T1Productos.tsx` ("Crea productos como prefieras"), `StoreShowcase.tsx`, `StoreCarousel` (en `T1Features`), `T1EnterpriseCarousel`
- **Descripción:** cards en riel deslizable. **Navegación:** flechas prev/next (ej. "Crea productos como prefieras") o dots.
- **Usos sugeridos:** presentar formas/opciones, casos, catálogos, showcase de tiendas, cualquier colección larga.
- **Tokens (card blanca estándar):** `w-[270px] rounded-[20px] border border-black/[0.07] bg-white p-6` shadow `0 4px 20px rgba(0,0,0,0.05)`; título `font-sora 19px`; imagen interna `rounded-[14px] h-[240px] object-cover`.
- **Layout (instancia "Crea productos como prefieras"):** sección de **2 columnas — título/intro + CTA a la IZQUIERDA, carrusel a la DERECHA**. Desktop `grid tablet:grid-cols-[minmax(0,0.8fr)_minmax(0,1.35fr)] tablet:items-center`; título `max-width ~420px`.
- **Responsive:** mobile `grid-cols-1` (stack: título arriba, carrusel abajo) con scroll horizontal por gesto (`overflow-x-auto`, scrollbar oculto); desktop añade flechas prev/next. Padding `px-5 py-[100px]` → `tablet:px-10 tablet:py-[128px]`.

### 3.4 Marquee
- **Archivo:** logos (en `T1Hero`/`T1FeatureIntro`/`T1Solutions`), carriers (`T1Multipaqueteria`)
- **Descripción:** riel en loop con fades laterales.
- **Usos sugeridos:** logos, carriers, sellos, cualquier set de marcas.
- **Tokens:** `--animate-marquee: 50s` (no 30s) · grayscale/opacity §11

---

## 4. Paneles simulados (réplicas de UI) — reemplaza al browser mockup

> **Excepción tipográfica:** estos paneles pueden usar **Manrope** para replicar la UI real del producto (dashboard/app). Es la **única** excepción a la regla Sora+Inter del landing. Prohibida fuera de paneles simulados. Ver `LANDING.md §1`.

### 4.1 Panel de producto
- **Archivo:** `showcase/PedidosPanel.tsx`, `showcase/CotizadorPanel.tsx`, `showcase/PagoMockups.tsx`, + paneles inline en `T1Productos`, `T1ControlCalidad`, `T1ReportesLogisticos`, `T1LinksDePago`
- **Descripción:** reconstrucción de una interfaz real (no screenshot). Sub-tipos: dashboard/stat · tabla de datos · formulario · chart/data-viz · chat.
- **Usos sugeridos:** mostrar el producto sin capturas; embeber en hero, features o steps.
- **Tokens:** radios `8–12px`; acento `#DB3B2B`; thumbs `rounded-[8px]`; tabs underline `h-[2px] bg-[#DB3B2B]`; chips/pills `rounded-full`. Tipografía **Manrope** (excepción, ver arriba).

### 4.2 Phone mockup
- **Archivo:** `showcase/PosMockups.tsx` (`PosCheckoutMobileScreen`), `T1POS.tsx`
- **Descripción:** marco de teléfono con UI.
- **Usos sugeridos:** features de usuario final (checkout, POS, tracking).
- **Tokens (POS real):** search `rounded-[12px] h-[44px] border black/[0.10]`; botón `rounded-[12px] bg-[#DB3B2B]`; thumbs `rounded-[8px]`; iconos `rounded-[9px]`.
- **Nota:** el teléfono usa **status bar** (hora/señal/batería), **no** barra de navegador (Pagos en línea migró de browser-bar a status bar).

### 4.3 Browser mockup
- **Archivo:** `LANDING.md §11` · 🧬 heredado — **aún usado dentro de `T1Solutions`** (no retirado del todo)
- **Descripción:** marco de navegador con captura (barra de tráfico + URL).
- **Usos sugeridos:** capturas dentro de paneles; ya no es el patrón dominante (lo reemplazan las réplicas de UI §4.1).

---

## 5. Proceso

### 5.1 Steps numerados
- **Archivo:** bloques "N pasos" en `T1Productos`, `T1PagosEnLinea`, `tienda-con-ia`
- **Descripción:** `01–0N` con número + título + texto, vertical u horizontal.
- **Usos sugeridos:** onboarding, "cómo funciona", cualquier proceso.

### 5.2 Steps con toggle
- **Archivo:** `T1ControlCalidad.tsx` (paquetería/usuario), `T1LinksDePago.tsx` (monto/productos)
- **Descripción:** el contenido de los steps cambia según pestaña/segmento.
- **Usos sugeridos:** procesos con dos rutas o modos, comparar variantes de un flujo.

---

## 6. Stats

### 6.1 Banda de stats
- **Archivo:** `T1Metrics.tsx` (`AnimatedMetric`, count-up)
- **Descripción:** fila de números grandes con animación de conteo (IntersectionObserver).
- **Usos sugeridos:** tracción, resultados, cualquier dato duro.
- **Tokens:** sección **oscura**; número `font-sora 40→72px light white tracking-tight`; label `font-inter 16px white`; blobs `blur 50–70px` rojo `rgba(219,59,43,0.1)` + indigo/purple.

### 6.2 Stats inline
- **Archivo:** dentro de statements en `T1LinksDePago`, `T1PagosEnLinea`
- **Descripción:** 2–4 cifras grandes dentro de un bloque de texto.
- **Usos sugeridos:** reforzar un mensaje con números.

---

## 7. Tabs / segmentadores

### 7.1 Tabs de contenido (manuales)
- **Archivo:** `T1Features.tsx` (capacidades), tabs de contexto en `T1PagosEnLinea`
- **Descripción:** pestañas que intercambian panel/imagen/UI **al hacer clic**.
- **Usos sugeridos:** explorar capacidades, segmentar por producto/caso de uso, cualquier contenido conmutable.

### 7.1b Tabs con auto-rotación (timer)
- **Archivo:** `T1AudienceRotator.tsx` — sección "Para cada etapa de tu negocio" (landing principal)
- **Descripción:** pestañas a la **izquierda** que **avanzan solas con timer** (`DURATION 5000ms`); al cambiar el foco cambia la **imagen/contenido de la derecha**. Clic en una pestaña cambia el foco y **reinicia el timer** — **no navega**.
- **Usos sugeridos:** presentar audiencias, segmentos, etapas o features de forma automática con contenido visual sincronizado.
- **Layout:** desktop `grid tablet:grid-cols-[minmax(0,0.95fr)_minmax(0,1fr)] tablet:items-center` (tabs izq / contenido der); mobile `grid-cols-1` (stack).
- **Tokens:** sección oscura (texto blanco); heading `font-sora 28→44px light` centrado; imágenes `emprendedor/pyme/enterprise-v4.png`.
- ⚠️ `T1Audience.tsx` (3 cards con link) está **comentado / no usado** — lo reemplazó este rotator.

### 7.1c Accordion rotativo
- **Archivo:** `T1PagosEnLinea.tsx` — "Cobra desde donde vendas"  ✨ nuevo
- **Descripción:** acordeón cuyas filas **se expanden solas con timer** (`CHANNELS_DURATION 11000ms`) con **barra de progreso** que se llena (`#DB3B2B`); al cambiar, cambia la simulación/contenido asociado. Mismo principio que 7.1b, en formato acordeón.
- **Usos sugeridos:** presentar canales / modos / pasos con contenido visual sincronizado y control de tiempo por fila.

### 7.2 Filtros (chips)
- **Archivo:** dentro de réplicas UI (Todos/Activos/Próximos)
- **Descripción:** segmentos tipo tab dentro de una interfaz simulada.
- **Usos sugeridos:** filtrado de listas y catálogos.

---

## 8. Navegación

### 8.1 Mega-menú (dropdowns)
- **Archivo:** `T1Navbar.tsx`
- **Descripción:** **dos** dropdowns — **Productos** (columnas de producto + panel promo de casos + novedades + cards de elección "¿Cómo quieres empezar?") y **Recursos** (Aprende / Soporte / Comunidad / Contacto / Página de estatus), este más simple (items `12px`, con borde de header).
- **Usos sugeridos:** catálogo de productos, recursos/soporte, cualquier navegación rica.
- **Tokens:** panel **oscuro sólido** `bg-[#1b1714]` (no glass), `border-t border-white/[0.08]`, `shadow-[0_24px_50px_rgba(0,0,0,0.55)]`, ancla `top-[60px]`. Columna promo `w-[270px] bg-[#242019]`, imagen `h-[100px] rounded-[10px]`. Animación `slideDown 200ms`.

### 8.2 Header glass
- **Archivo:** `T1Navbar.tsx` · cruza con `ORGANISMS.md §8`
- **Descripción:** barra fija translúcida con blur.
- **Nota:** nav actual = **Productos** (dropdown) · **Recursos** (dropdown) · **Precios** · **Enterprise** · Iniciar sesión · **Comienza gratis**. ('Clientes' se eliminó.)

### 8.3 Footer oscuro
- **Archivo:** `T1Footer.tsx`
- **Descripción:** footer negro con **4 columnas** (Productos / Recursos / Comunidad / T1) + redes + sello **"Hecho en México"** con texto **"Una empresa 100% mexicana"**.
- **Tokens:** título de columna `font-inter 15px semibold white`, links `14px white/50`; redes `30×30 rounded-full bg-white/10`; sello `hecho-en-mexico.jpg` `52×52 rounded-[8px]`.
- **Responsive:** desktop = logo + 4 columnas; mobile = columnas en `grid-cols-2` (2×2).

---

## 9. Bloques compuestos

### 9.1 Bloque problema→solución
- **Archivo:** `T1Problema.tsx` + statement de resolución
- **Descripción:** statement de dolor + resolución (se arma con card de texto o stats).
- **Usos sugeridos:** narrativa antes/después, framing de valor.

### 9.2 Bloque de descarga
- **Archivo:** dentro de `T1POS.tsx`
- **Descripción:** QR + badges App Store/Play + imagen de dispositivos.
- **Usos sugeridos:** apps, cualquier descarga.

### 9.3 Bloque de ecosistema
- **Archivo:** `TodoIncluidoDark.tsx` / ecosistema en `T1Solutions`
- **Descripción:** productos relacionados con iconos + CTA.
- **Usos sugeridos:** cross-sell, "es parte de", relacionados.

### 9.4 CTA final
- **Archivo:** `T1FinalCTA.tsx`
- **Descripción:** cierre con statement + botón, sobre sección oscura con glow rojo.
- **Usos sugeridos:** cierre de cualquier página.
- **Tokens:** contenedor `max-w-[860px]`; glow rojo `800×500 blur(40px)`; reveal `blur(8→0px)` + scale; heading `font-sora 32→48→60px light white`; subtítulo `text-[15–18px] white/40`; botón = **igual que hero** `h-[50px] rounded-[23px] bg-[#DB3B2B] px-7` hover `#C0332A` (decisión owner).
- ⚠️ Corrige §11 "CTA Final = bg-gray-900 rounded-[32px]": la realidad es sección oscura + glow. 
- 🛠️ **Cambio de código pendiente:** el botón está en `rounded-full h-[48px]` → cambiar a `rounded-[23px] h-[50px]` para igualar al hero.

---

## 10. Media (imágenes dinámicas)

- **Video:** `T1Hero` (`hero.mp4`).
- **Imágenes renderizadas full-bleed:** bg-score, PNG/WebP de marketing.
- **Screenshots emparejados desktop+mobile:** `StoreShowcase` (LochWild, Lover Boy, Pirma).

---

## Procedencia y validez (heredado vs nuevo)

Cruce de cada familia contra el doc anterior (`LANDING.md §9–§11`, `§16`) y el repo real.

| Componente | Proc. | Validez en repo |
|---|---|---|
| Hero centrado (1.1) | 🧬 | Vigente (base) |
| Hero video (1.2) | ✨ | Vigente (`T1Hero`) |
| Hero split con panel (1.3) | ✨ | Vigente (sublandings) |
| Hero input IA (1.4) | ✨ | Vigente (`T1AISectionV2`) |
| Hero de declaración (1.5) | 🧬 | Vigente (owner) |
| Card con ícono (2.1) | 🧬 | Vigente (beneficios) |
| Card glass+glow+imagen (2.1b) | ✨ | Vigente (`T1FeatureIntro`) |
| Card imagen / texto / elección / plan / cita (2.2–2.6) | ✨ | Vigentes |
| Card glass dark (2.7) | 🧬 | Vigente (`GlassProductCard`) |
| Stack cards / sticky glass / carrusel (3.1–3.3) | ✨ | Vigentes |
| Marquee (3.4) | 🧬 | Vigente |
| Paneles simulados (4.1) | ✨ | Vigentes (reemplazan browser mockup) |
| Phone mockup (4.2) | 🧬 | Vigente (`PosMockups`) |
| Browser mockup (4.3) | 🧬 | **Parcial** — solo en `T1Solutions` |
| Steps numerados / toggle (5.1–5.2) | ✨ | Vigentes |
| Stats banda / inline (6.1–6.2) | ✨ | Vigentes |
| Tabs / filtros (7.1–7.2) | ✨ | Vigentes |
| Mega-menú (8.1) | ✨ | Vigente (`T1Navbar`) |
| Problema→solución / app download / ecosistema (9.1–9.3) | ✨ | Vigentes |
| CTA final (9.4) | 🧬 | Vigente (cambió forma) |
| **Floating badges** | 🧬 | **❌ NO vigente** (0 usos en el repo) |

> **Acción:** deprecar formalmente **Floating badges** de `LANDING.md §11` (ya no se usan). Browser mockup y gradient border → marcar como "uso residual", no como patrón recomendado.

---

## Landing principal vs Sublanding — ritmo de fondos

| | Landing principal (`/`) | Sublanding (`/productos/…`) |
|---|---|---|
| Base | **Oscura** — hero degradado + secciones oscuras (Métricas, Enterprise `#0F0E0D`, ScrollShowcase, Footer) con respiros claros | **Hero oscuro** (degradado) + **cuerpo claro** (blanco / `#FFFAFA` con paneles) |
| Respiros | Secciones **blancas / grises** intercaladas | Cierre **oscuro** (CTA final + Footer) |
| Hero | Oscuro — degradado `180deg #0e0d0d→#020101` + glows (video opcional) | Oscuro — **mismo estilo de degradado** que el principal, dividido con panel blanco |

> Reemplaza el modelo de §16 ("sublanding arranca oscuro + ritmo por bloques"), que no coincide con el repo. **Confirmar** este framing antes de reescribir §16 formalmente.

---

## Deltas encontrados en la pasada fina (para decisión)

1. **Radios de card:** el modelo documentado (24px) casi no se usa; dominan `10/12/14/16px`. El `24px` queda para glass cards grandes. → actualizar §4/§11.
2. ✅ **Botones (resuelto):** §3 ajustado al valor real `#DB3B2B` (Red 500) + hover `#C0332A`. Radio por tamaño: nav `18px`, hero `23px`, CTA final `23px` (= hero).
3. ✅ **CTA final (resuelto):** botón = hero (`23px`); pendiente el cambio de código (`rounded-full` → `rounded-[23px]`).
4. **Mega-menú:** panel oscuro sólido `#1b1714`, no glass.

## Pendientes menores

1. Confirmar archivo exacto de: grids image-led (card imagen), ecosistema, steps numerados.
2. Deprecación formal de browser mockup (4.3) y hero de declaración (1.5).
3. Rutas no muestreadas (`enrutamiento`, `recolecciones`, `reglas`, `rastreo`, `marketplaces`, `pasarela`, `reportes` de tienda, `precios`, `colombia`).
