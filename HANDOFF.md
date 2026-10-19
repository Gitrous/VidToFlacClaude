# HANDOFF — migración de Google AdSense a Monetag

Estado a **19 de octubre de 2026**.

---

## Por qué se hizo

AdSense rechazó el sitio **dos veces** por "contenido de poco valor". Se
abandona esa vía y se monetiza con **Monetag**, que no somete el contenido a
revisión editorial.

## Qué se decidió y qué se descartó

**Formatos activos:**
- **Native Banner** → rellena los huecos `.ad-slot`.
- **Vignette** → solo en `/articulos/` y `/en/articles/`, por `VIGNETTE_PATHS`.
- **Push** → `sw.js` instalado en la raíz (ver más abajo).

**Descartados a propósito — no es un olvido:**
- **Popunder y onclick.** Se enganchan a un escuchador de clics *a nivel de
  documento*: no se pueden excluir de un botón concreto, y el clic más
  frecuente del sitio es "Convertir". Se dispararían en la primera conversión
  de cada visitante.

---

## Qué está hecho

- **AdSense eliminado por completo**: 0 referencias (eran **634 en 51
  páginas**: 50 scripts de cabecera, 120 bloques `<ins>`, 120 llamadas
  `push()`).
- **`ads.js` nuevo** — único punto de configuración, con `CONFIG`
  (ahora **vacío**), el cargador y el aviso de consentimiento ES/EN. **Es la
  única excepción a la regla de archivo único**, documentada en `CLAUDE.md`.
- **Cada página**: una línea `<script src="/ads.js" defer>` y **cero IDs**. Los
  huecos son `<div class="ad-slot" hidden>`.
- **`build_pages.py`**: `FAQ_AD` → `faq_ad(lang)`, porque el rótulo
  ("Publicidad" / "Advertisement") es visible y va traducido.
- **`ads.txt`**: fuera la línea de Google; quedan comentarios y el hueco.
- **Las 4 páginas legales** nombran Monetag, describen el consentimiento previo
  y declaran el service worker de notificaciones.

### Verificaciones pasadas

| Comprobación | Resultado |
|---|---|
| Referencias a AdSense | 0 |
| JS de las 99 páginas | 0 roto |
| `ads.js` / `sw.js` | sintaxis OK |
| JSON-LD | 198 bloques, 0 rotos |
| Enlaces internos | 0 rotos |
| Generador vs disco | 0 diferencias |
| Rótulos ES / EN | 60 / 60, sin fugas |
| Conversión real en navegador | OK — 2,0 s, igual que `origin/main` sin tocar |

---

## QUÉ FALTA

### 1. Los Zone ID de Monetag — bloqueante

Sin esto **no se carga publicidad ni aparece el aviso de cookies**. El sitio
funciona, pero no ingresa nada. En `ads.js`:

```js
var CONFIG = {
  host: '',            // ← host del tag
  zones: {
    native:   '',      // ← Zone ID del Native Banner
    vignette: ''       // ← Zone ID del Vignette
  }
};
```

**Dato ya conocido:** del `sw.js` se extrae el dominio **`3nbf4.com`** (y
`zoneId 11862981`, que es el de *push* y no sirve para los otros formatos).
Faltan los Zone ID de Native Banner y Vignette: panel → Sites → el sitio → el
formato → Get code.

### 2. Las líneas de `ads.txt`

Pegarlas del panel (Sites → el sitio → ads.txt), con la forma
`monetag.com, <ID>, DIRECT, <TAG_ID>`. Ahora el archivo solo tiene comentarios,
que es válido y no autoriza a nadie.

### 3. Decisión pendiente: el modal de 3 conversiones

El usuario pidió conservar el modal de "3 conversiones gratuitas" con anuncio.
**No se ha hecho**, y conviene entender por qué:

El 26-09-2026, el commit aislado `45520eb` quitó ese modal y los anuncios de la
lista de resultados **porque incumplían políticas de AdSense** (recompensa por
ver un anuncio, anuncio encima de un botón, anuncios entre botones de
descarga). La petición del usuario se hizo sobre una copia del repo anterior a
ese commit, sin saberlo.

Al migrar a Monetag, **la razón de AdSense desaparece**: Monetag no prohíbe la
recompensa por ver un anuncio. Pero las otras dos razones son de producto, no
de política, y siguen en pie.

**Si el usuario quiere recuperarlo:** `git revert 45520eb` y después recolocar
los huecos para que no queden pegados a ningún control. `CLAUDE.md` ya advertía
de que no se restaurase *tal cual*.

### 4. `sw.js` (push) — instalado, con una salvedad

**Qué se probó** (sin puppeteer: Chrome por el protocolo DevTools, conversión
real de un MP4 H.264 + AAC generado con ffmpeg):

| Escenario | Service worker | Conversión |
|---|---|---|
| Control | sin SW | OK — `prueba.mkv`, 2,0 s |
| `sw.js` de Monetag | **no llegó a registrarse** | no concluyente |
| SW de ámbito raíz con `fetch` que intercepta todo | activo y controlando | OK — 2,0 s |

**El límite:** el `sw.js` real no se pudo probar porque `3nbf4.com` resuelve a
`::` en la máquina del usuario — bloqueado por su resolver DNS local
(`nameserver 127.0.0.1`). Se probó el *mecanismo* con un worker equivalente, y
**el motor aguanta**.

Lo que esto **no** demuestra: que el script que Monetag sirva en
`https://3nbf4.com/act/files/service-worker.min.js?r=sw` sea inocuo. Se
descarga en tiempo de ejecución y puede cambiar cuando ellos quieran.

**Si aparecen fallos intermitentes del motor en producción, este es el primer
sospechoso**: se borra `sw.js` de la raíz y se despliega.

Nota: como el dominio está bloqueado en su máquina, el usuario **tampoco verá
los anuncios al probar en local**. No será un fallo del sitio.

---

## Nota sobre cómo se hizo (incidencia de git)

La migración se construyó primero sobre una base **32 commits anticuada**. Al
intentar el push, GitHub lo rechazó. Se descartó ese trabajo y **se rehízo
entero sobre `origin/main`**, porque forzarlo habría machacado 32 commits
(banco de pruebas, feed RSS, correcciones de MP3 en Linux, rediseño de
portadas) y habría resucitado el modal y los anuncios de resultados que se
habían quitado a propósito.

El intento antiguo queda en la rama local **`monetag-sobre-base-antigua`** y en
un parche en el scratchpad de la sesión. Se puede borrar sin pérdida: todo lo
aprovechable está ya en `main`.

---

## Avisos para quien siga

- **No edites el HTML de las landings a mano**: se regeneran con
  `build_pages.py`. El texto vive en `landing_content*.py`, `merged_content.py`
  y `PAGES`/`PAGES_EN`.
- **Hay cuatro copias del conversor**, no dos: `index.html`, `en/index.html`,
  `convertir-formatos/` y `en/convert-formats/`.
- **Tras tocar `ads.js`**, comprueba que el camino sin aceptar el aviso no
  inserta ningún `<script>` de la red.
- **`node --check` solo mira la sintaxis.** Después de borrar código, pruébalo
  en el navegador: el guion `drive.mjs` del scratchpad conduce Chrome por el
  protocolo DevTools y hace una conversión real.
- **La primera conversión en un perfil de Chrome nuevo tarda mucho más**: el
  core de ffmpeg.wasm se descarga de unpkg con la caché fría. En esta migración
  eso produjo un timeout que se leyó como regresión, y no lo era. Antes de
  concluir que algo se ha roto, repite con el perfil caliente y compara contra
  un checkout limpio de `origin/main` servido en otro puerto.
