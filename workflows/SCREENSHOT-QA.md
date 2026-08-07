# SCREENSHOT-QA.md

> Proceso de QA visual para proyectos T1 / NEXUS V2.0.  
> Aplica a landing pages y dashboard. Mínimo 2 rondas de comparación por sesión.

---

## 1. Setup requerido

### Servidor local

Siempre servir desde localhost. **Nunca** tomar screenshots de una URL `file:///` — los estilos pueden no cargar correctamente fuera de un servidor HTTP.

```bash
# Iniciar el servidor de desarrollo
node serve.mjs
# Sirve el proyecto en http://localhost:3000
```

`serve.mjs` vive en la raíz del proyecto. Si el servidor ya está corriendo, no iniciar una segunda instancia.

### Puppeteer

Puppeteer está instalado en el proyecto. El script `screenshot.mjs` también vive en la raíz y se usa tal cual — no modificar.

```bash
# Screenshot básico
node screenshot.mjs http://localhost:3000

# Screenshot con label descriptivo
node screenshot.mjs http://localhost:3000 nombre-label
# → guarda como screenshot-N-nombre-label.png
```

Los screenshots se guardan automáticamente en `./temporary screenshots/screenshot-N.png` con auto-incremento. Nunca sobreescriben archivos existentes.

---

## 2. Proceso de QA — paso a paso

### Ronda 1

1. Asegurarse de que el servidor local está corriendo
2. Ejecutar `node screenshot.mjs http://localhost:3000`
3. Leer el PNG desde `temporary screenshots/` con el Read tool
4. Comparar visualmente contra la referencia (si existe) o contra las reglas de NEXUS
5. Documentar todas las discrepancias con especificidad (ver sección 3)
6. Aplicar correcciones

### Ronda 2

7. Re-ejecutar el screenshot
8. Verificar que todas las discrepancias de la ronda 1 fueron corregidas
9. Buscar regresiones introducidas por las correcciones
10. Si persisten diferencias, repetir desde el paso 6

### Criterio de parada

Detener el ciclo cuando:
- No hay diferencias visibles entre el output y la referencia, **o**
- El usuario indica explícitamente que el resultado es aceptable

**Nunca parar después de una sola ronda.** El primer screenshot casi siempre revela al menos un ajuste necesario.

---

## 3. Cómo reportar discrepancias

Ser específico y medible. Las descripciones vagas no permiten correcciones precisas.

| ❌ Vago | ✅ Específico |
|---|---|
| "el título es muy grande" | "el heading es 48px pero la referencia muestra ~36px" |
| "hay demasiado espacio" | "el padding top de la sección es 80px, debe ser 48px" |
| "el color no es correcto" | "el botón usa `#E26153` pero en dashboard debe ser `#DB3B2B`" |
| "las cards no se ven bien" | "el gap entre cards es 16px, debe ser 24px según la escala de spacing" |
| "la sombra está mal" | "hay `shadow-md` de Tailwind, debe reemplazarse por la sombra del sistema" |

---

## 4. Checklist de revisión por categoría

Revisar en este orden en cada ronda de screenshot.

### Tipografía

- [ ] Familia correcta según contexto: Sora/Inter en landing, Manrope en dashboard
- [ ] Manrope NUNCA aparece en landing
- [ ] Sora/Inter NUNCA aparecen en dashboard
- [ ] Tamaños respetan la escala tipográfica (no hay tamaños inventados)
- [ ] Pesos correctos: Bold para títulos, Medium para labels, Regular para cuerpo
- [ ] Line-height aplicado: `1.366em` Manrope / `1.2em` Sora / `1.5em` Inter
- [ ] Tracking ajustado en headings grandes (`-0.03em`)
- [ ] Eyebrow badges: `text-[11px] font-semibold uppercase tracking-[0.15em]` (landing)

### Colores

- [ ] Rojo primario correcto según contexto: `#E26153` landing / `#DB3B2B` dashboard
- [ ] No hay colores arbitrarios ni de la paleta default de Tailwind
- [ ] Texto sobre fondos oscuros usa `text-white` o `text-gray-400`, nunca `text-gray-900`
- [ ] Números/métricas sobre fondos de color usan `text-white`, nunca rojo
- [ ] Rojo en texto solo aparece en landing (en dashboard indica error)
- [ ] Estados semánticos correctos: success `#4FC153`, warning `#FF6700`, error `#CC0000`, info `#2180FF`

### Espaciado

- [ ] Padding y gap siguen la escala de spacing del sistema
- [ ] No hay valores de spacing arbitrarios (ej: `p-[17px]`)
- [ ] Espaciado consistente entre secciones equivalentes

### Layout y contenedores

- [ ] Contenedor máximo correcto: `max-w-[1018px]` landing / `max-w-[1600px]` dashboard
- [ ] Breakpoint desktop en 1280px
- [ ] Mobile-first: diseño funcional desde 360px
- [ ] Landing: variedad de layouts por sección (no todos grid-cols-3)
- [ ] Landing principal: mínimo 2 secciones con fondo oscuro para ritmo visual
- [ ] Sublanding: hero arranca oscuro (`#0F1419`); fondos agrupados en bloques (oscuro → claro → oscuro), no alternancia sección a sección

### Border radius

- [ ] Landing: 24px cards, 18px botones
- [ ] Dashboard: 10px estándar (cards, inputs, modales, badges), 20px solo cards grandes
- [ ] Sidebar dashboard: 18px
- [ ] No hay mezcla de valores de contextos distintos

### Sombras

- [ ] Dashboard: solo 2 sombras permitidas (button shadow, card-selected con Red 200)
- [ ] Dashboard: dropdowns y sidebar sin sombra
- [ ] Landing: sombras multicapa con color tint y baja opacidad
- [ ] No hay `shadow-md` plano de Tailwind en ningún contexto

### Fondos y profundidad

- [ ] Landing secciones oscuras: mesh gradient — nunca `bg-gray-900` plano
- [ ] Noise overlay `.bg-noise` presente en secciones con mesh gradient
- [ ] Sistema de capas visible: base → elevated → floating

### Estados interactivos

- [ ] Hover state visible en todos los elementos clickables
- [ ] Focus state: outline `#2180FF` 2px con `:focus-visible`
- [ ] Active/pressed state presente
- [ ] Disabled state con opacidad reducida y `cursor: not-allowed`

### Imágenes

- [ ] Overlay gradiente aplicado: `bg-gradient-to-t from-black/60`
- [ ] Capa de tratamiento de color con `mix-blend-multiply`
- [ ] Imágenes usando `<Image>` de Next.js, no `<img>` directo

### Animaciones

- [ ] Solo se animan `transform` y `opacity`
- [ ] No hay `transition-all` en ninguna parte
- [ ] `data-animate` presente en todos los bloques de contenido (landing)

### Accesibilidad básica

- [ ] Touch targets mínimo 44×44px
- [ ] Contraste de texto adecuado (WCAG AA mínimo)
- [ ] Texto sobre fondo nunca depende solo del color para comunicar estado

---

## 5. Naming de screenshots

Usar labels descriptivos para facilitar la comparación entre rondas.

```bash
# Primera ronda
node screenshot.mjs http://localhost:3000 r1

# Segunda ronda con correcciones
node screenshot.mjs http://localhost:3000 r2

# Screenshot de sección específica (con scroll o ruta)
node screenshot.mjs http://localhost:3000/pricing r1-pricing

# Comparación de estado hover (captura manual necesaria)
node screenshot.mjs http://localhost:3000 r1-hover-state
```

---

## 6. Casos especiales

### Sin imagen de referencia

Cuando no hay referencia visual, el criterio de QA es el cumplimiento de las reglas de NEXUS. Usar el checklist completo de la sección 4. El output debe verse como un producto T1 — no como un template genérico.

### Con imagen de referencia

El objetivo es **replicar exacto**, no mejorar. Si la referencia muestra algo que parece un error (spacing inconsistente, jerarquía extraña), igualmente replicarlo. Las mejoras se proponen por separado al usuario — nunca se aplican unilateralmente.

### Páginas con scroll largo

Para landings de una sola página, tomar screenshots adicionales de secciones específicas cuando sea necesario:

```bash
node screenshot.mjs http://localhost:3000#pricing r1-pricing
node screenshot.mjs http://localhost:3000#features r1-features
```

### Responsive

Cuando el request lo requiera, verificar también en viewports móviles. Puppeteer permite configurar el viewport en `screenshot.mjs` si es necesario. Prioridad de verificación: desktop 1280px → tablet 768px → mobile 360px.
