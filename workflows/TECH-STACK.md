# TECH-STACK.md

> Stack técnico obligatorio y convenciones de código para proyectos T1 / NEXUS V2.0.  
> Todo código generado debe cumplir con estas especificaciones sin excepción.

---

## 1. Stack obligatorio

| Tecnología | Versión | Notas |
|---|---|---|
| **Next.js** | 14+ | App Router obligatorio — no usar Pages Router |
| **TypeScript** | Latest | Modo estricto |
| **Tailwind CSS** | v4 | Configuración en `globals.css` — no en `tailwind.config.js` |

No agregar dependencias fuera de este stack sin aprobación explícita. Si una funcionalidad puede resolverse con las herramientas del stack, no instalar una librería adicional.

---

## 2. Tailwind CSS v4 — configuración

### Diferencia crítica con v3

En Tailwind v4 **no existe `tailwind.config.js`**. Toda la configuración — tokens, breakpoints, keyframes, colores — vive en `globals.css` dentro de un bloque `@theme inline {}`.

### Estructura de `globals.css`

```css
@import "tailwindcss";

@theme inline {
  /* Colores de marca */
  --color-brand-red-500: #DB3B2B;
  --color-brand-red-600: #E26153;
  --color-brand-red-900: #CC0000;
  /* ... resto de la escala */

  /* Breakpoints */
  --breakpoint-mobile: 360px;
  --breakpoint-tablet: 768px;
  --breakpoint-desktop: 1280px;
  --breakpoint-wide: 1920px;

  /* Keyframes */
  --animate-fade-in: fade-in 0.3s ease-out;
  --animate-slide-up: slide-up 0.4s cubic-bezier(0.16, 1, 0.3, 1);
}
```

### Reglas de uso

- Los tokens se definen como CSS custom properties con el prefijo `--color-`, `--breakpoint-`, `--animate-`
- Para colores en clases de Tailwind, usar notación directa: `text-[#E26153]` — **no** variables CSS en las clases
- `!important` con el prefijo `!` (ej: `!text-white`) puede no funcionar como se espera en v4 — preferir especificidad CSS natural
- Los keyframes se definen dentro de `@theme inline` — no en bloques `@keyframes` separados en este contexto

---

## 3. Estructura de componentes

### Convención de naming

Todo componente del sistema usa el prefijo `T1` + PascalCase descriptivo.

```
T1Button
T1PricingCard
T1HeroSection
T1SidebarMenu
T1DataTable
```

No usar nombres genéricos sin el prefijo (`Button`, `Card`, `Hero`). El prefijo identifica que el componente pertenece al sistema NEXUS y cumple con sus reglas.

### Plantilla base — componente de sección

```tsx
"use client"; // solo si el componente tiene interactividad (useState, useEffect, handlers)

import SectionWrapper from "./ui/SectionWrapper";
import { NOMBRE_DATOS } from "@/lib/constants";

// Subcomponentes internos — no exportar
function T1SubComponente() {
  return (/* ... */);
}

// Componente principal — siempre export default
export default function T1NombreSeccion() {
  return (
    <SectionWrapper id="id-de-seccion" className="py-20 tablet:py-28">
      {/* Elementos decorativos — siempre position absolute */}
      <div aria-hidden="true" className="absolute inset-0 pointer-events-none">
        {/* glow blobs, dot pattern, noise overlay */}
      </div>

      {/* Contenido principal — siempre relative z-10 */}
      <div className="relative z-10">
        {/* Eyebrow + título — siempre con data-animate */}
        <div data-animate>
          <p className="mb-3 font-inter text-[11px] font-semibold uppercase tracking-[0.15em] text-gray-400">
            Eyebrow label
          </p>
          <h2 className="font-sora text-[32px] font-light text-gray-900 tablet:text-[44px]">
            Título con <span className="text-[#E26153]">acento</span>
          </h2>
        </div>

        {/* Contenido — data-animate separado del header */}
        <div data-animate>
          {/* contenido */}
        </div>
      </div>
    </SectionWrapper>
  );
}
```

### Cuándo usar `"use client"`

Solo agregar la directiva si el componente usa:
- Hooks de React (`useState`, `useEffect`, `useRef`, `useCallback`, etc.)
- Event handlers del DOM (`onClick`, `onChange`, `onSubmit`)
- APIs del browser (`window`, `document`, `localStorage`)
- Librerías que requieren el browser

Si el componente solo renderiza JSX estático, **no** agregar `"use client"`.

---

## 4. Separación de datos y lógica

### Regla fundamental

Los componentes **nunca** hardcodean contenido. Todo texto, URLs, imágenes, configuraciones y datos estáticos viven en `src/lib/constants.ts`.

### Estructura de `constants.ts`

```ts
// Navegación
export const NAV_LINKS = [...];

// URLs externas
export const SIGNUP_URL = "https://...";
export const WHATSAPP_URL = "https://wa.me/...";

// Secciones de contenido
export const HERO_DATA = {...};
export const FEATURES = [...];
export const PRICING = [...];
export const TESTIMONIALS = [...];
export const FAQ = [...];

// Assets
export const CLIENT_LOGOS = [...];

// Footer
export const FOOTER_LINKS = [...];
export const SOCIAL_LINKS = [...];
```

### Cómo consumir en componentes

```tsx
import { FEATURES } from "@/lib/constants";

export default function T1Features() {
  return (
    <div>
      {FEATURES.map((feature) => (
        <T1FeatureCard key={feature.id} {...feature} />
      ))}
    </div>
  );
}
```

---

## 5. Alias de rutas

Usar el alias `@/` para imports absolutos desde la raíz de `src/`.

```tsx
// ✅ Correcto
import { DATOS } from "@/lib/constants";
import T1Button from "@/components/ui/T1Button";

// ❌ Incorrecto
import { DATOS } from "../../lib/constants";
```

---

## 6. Tipografía — carga de fuentes

Las tres familias del sistema se cargan desde Google Fonts. La carga se configura una sola vez en `layout.tsx` (o equivalente en App Router) y se aplica vía clases de Tailwind.

| Familia | Variable CSS | Clase Tailwind |
|---|---|---|
| Manrope | `--font-manrope` | `font-manrope` |
| Sora | `--font-sora` | `font-sora` |
| Inter | `--font-inter` | `font-inter` |

> **TODO:** Documentar la implementación exacta de `next/font` cuando esté disponible.

---

## 7. Imágenes

- Siempre usar el componente `<Image>` de Next.js — **nunca** `<img>` directo
- Logos e íconos de UI como SVG inline cuando sea posible (menor peso, heredan `currentColor`)
- Imágenes de contenido con `priority` solo en elementos above the fold (hero)
- Placeholders durante desarrollo: `https://placehold.co/WIDTHxHEIGHT`

```tsx
import Image from "next/image";

<Image
  src="/assets/imagen.webp"
  alt="Descripción significativa"
  width={800}
  height={600}
  priority // solo above the fold
/>
```

---

## 8. Deployment — Vercel

| Configuración | Valor |
|---|---|
| Plan | Hobby |
| Production branch | Configurar en Settings → Environments → Production → Branch Tracking |
| Commit author email | Debe coincidir con el email de la cuenta Vercel para activar deployments automáticos |
| Deployment Protection | Deshabilitar en Settings → Deployment Protection para que preview URLs sean accesibles sin autenticación |

---

## 9. Checklist pre-deployment

Antes de hacer deploy de cualquier proyecto T1:

**TypeScript y build:**
- [ ] `npm run build` sin errores ni warnings de TypeScript
- [ ] No hay imports de componentes huérfanos o sin usar
- [ ] No hay `any` sin justificación

**Performance:**
- [ ] Imágenes con `<Image>` de Next.js — no `<img>` directo
- [ ] Logos como SVG cuando sea posible
- [ ] Sin dependencias instaladas sin usar

**Código:**
- [ ] Todo contenido textual en `constants.ts` — ningún string hardcodeado en componentes
- [ ] Ningún componente con `"use client"` innecesario
- [ ] Naming `T1` + PascalCase en todos los componentes del sistema

**Tailwind v4:**
- [ ] Configuración en `globals.css` — no en `tailwind.config.js`
- [ ] No hay `transition-all` en ninguna parte
- [ ] No hay colores de la paleta default de Tailwind (indigo, blue, sky, etc.)

---

## 10. Pendientes — completar cuando esté disponible

> Estas secciones se completan cuando el equipo de desarrollo proporcione la información faltante.

- **Estructura de carpetas del proyecto** — organización de `/app`, `/components`, `/lib`, `/public`
- **Breakpoints exactos** — valores completos definidos en `globals.css`
- **Carga de fuentes** — implementación exacta con `next/font` en `layout.tsx`
- **Convenciones de imports** — barrel exports, orden de imports, agrupación
