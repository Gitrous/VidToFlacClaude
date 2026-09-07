# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) al trabajar con el código de este repositorio.

## Qué es esto

VidToFLAC es una aplicación web de **una sola página y 100% del lado del cliente** que reempaqueta (remux) vídeo en un MKV con una pista de audio FLAC sin pérdida (o transcodifica archivos solo de audio a FLAC), para solucionar el problema de "sin audio / error de códec de audio" en DaVinci Resolve, Premiere y Avid. Todo el procesamiento ocurre localmente en el navegador mediante **ffmpeg.wasm** — nunca se sube nada. El sitio está en **español** (textos de UI, logs, comentarios) y está muy optimizado para SEO en torno al caso de uso del códec de audio de DaVinci Resolve.

## Sincronización con la versión en inglés

**Cualquier cambio en `index.html` (versión principal en español) debe aplicarse también a `en/index.html` (versión en inglés).** Esto incluye cambios de CSS, layout, lógica JS, slots de anuncios, y cualquier elemento estructural. Los textos de UI van traducidos al inglés; el resto del código es idéntico.

## Toda la app es `index.html`

**No hay dependencias, tests ni package.json.** Sí hay un generador, `build_pages.py`, pero solo para las 20 landings de formato (ver más abajo); la app en sí no se compila. `index.html` (~2200 líneas) contiene todo en línea: el `<head>` de SEO (meta, Open Graph, varios bloques JSON-LD), todo el CSS en un único `<style>`, el cuerpo HTML y la lógica de la aplicación en un solo `<script type="module">`. Los demás archivos versionados son recursos estáticos (iconos, `og-image.png`, `robots.txt`, `sitemap.xml`, `site.webmanifest`, `CNAME`).

Al editar, conserva la estructura de archivo único — no separes en archivos JS/CSS aparte.

## Revisión de políticas de Google AdSense

**Después de completar cualquier cambio** y antes de preguntar al usuario qué hacer, revisa si el cambio podría incumplir alguna política de Google AdSense. Las políticas más relevantes para este sitio son:

- **Contenido valioso para el usuario**: la página debe ofrecer contenido original y útil, no ser un sitio vacío o de relleno.
- **Navegación clara**: el sitio debe ser fácil de navegar; los anuncios no deben interferir con la navegación ni con el contenido principal.
- **Anuncios no engañosos**: los anuncios no pueden colocarse de forma que induzcan a clics accidentales (p. ej., junto a botones de acción, demasiado cerca del contenido interactivo, ni encima de elementos clicables).
- **Sin contenido restringido**: nada de contenido para adultos, violento, engañoso, de juegos de azar no regulados, etc.
- **Sin manipulación del tráfico artificial**: no implementar nada que genere impresiones o clics falsos en anuncios.
- **Política de privacidad y cumplimiento GDPR/CCPA**: si se añade recogida de datos (formularios, cookies, analítica), debe existir política de privacidad visible y consentimiento adecuado.
- **Contenido suficiente**: no publicar páginas casi vacías ni stubs; cada página debe tener contenido sustancial.

Si el cambio **incumple alguna política**, NO lo apliques directamente. En su lugar:

1. Indica exactamente **qué política incumple** y por qué.
2. Explica **qué harías** para corregirlo o adaptarlo.
3. **Pregunta al usuario si quiere que lo hagas** antes de proceder.

Si el cambio no presenta ningún problema con AdSense, continúa con el flujo normal.

## Flujo de trabajo tras cada cambio

**Después de completar cualquier cambio** (y tras la revisión AdSense anterior), pregunta siempre al usuario:

> "¿Quieres arrancar un servidor para verlo (**s**) o subirlo a GitHub (**g**)?"

El usuario responde con una sola letra:

- **`s`** → **Servidor / previsualizar**: arranca `python3 -m http.server 8000` (si no hay ya un servidor corriendo en ese puerto) y muestra una captura headless del resultado.
- **`g`** → **Subir a GitHub**: haz commit de los archivos modificados directamente a `main` y push. El despliegue en GitHub Pages se dispara automáticamente. **Tras el push, programa siempre un `ScheduleWakeup` de ~70 s para monitorizar el despliegue** y avisar al usuario en cuanto el build de GitHub Pages esté en estado `built` con un `updated_at` posterior al momento del push. Usa `gh api repos/Gitrous/VidToFlacClaude/pages/builds/latest` para comprobarlo. Si aún no ha terminado, reprograma otro wakeup de 60 s hasta que esté listo.

Interpreta `s` y `g` (en mayúscula o minúscula) como estos atajos siempre que vengan como respuesta a esta pregunta. No hagas el push ni arranques el servidor sin confirmación explícita del usuario.

## Desarrollo local

Debe servirse por HTTP (la app usa imports de ES modules y `fetch`; `file://` no funciona):

```bash
python3 -m http.server 8000   # luego abre http://localhost:8000/
```

Para verificar visualmente un cambio con Chrome headless (captura de página completa):

```bash
google-chrome --headless --disable-gpu --no-sandbox --hide-scrollbars \
  --window-size=900,3300 --force-device-scale-factor=2 \
  --screenshot=/tmp/shot.png --virtual-time-budget=4500 http://localhost:8000/
```

Nota: las URLs con ancla (`#problema-titulo`) no hacen scroll de forma fiable en modo headless — captura la página completa y recórtala en su lugar.

## Despliegue

GitHub Pages en **modo legacy**, origen = rama `main` raíz (`/`), dominio personalizado `vidtoflac.tech` (definido por `CNAME`, HTTPS forzado). **Hacer push a `main` dispara automáticamente un despliegue** — no hay archivo de workflow. El flujo establecido es commitear directamente a `main` (sin ramas de feature ni PRs). Verifica un despliegue con:

```bash
gh api repos/Gitrous/VidToFlacClaude/pages/builds/latest
```

## Cómo se carga el motor ffmpeg.wasm (el "hack del worker")

ffmpeg.wasm 0.12.x se descarga desde el CDN de unpkg en tiempo de ejecución. Chrome bloquea `new Worker(crossOriginURL, {type:'module'})`, así que el código de arranque (al inicio del `<script>`) lo evita: hace `fetch` de `worker.js` desde el CDN, reescribe sus imports relativos a URLs absolutas, lo envuelve en un Blob URL del mismo origen y **parchea `window.Worker`** para sustituir la URL del worker del CDN por ese blob. Esto evita SharedArrayBuffer / cabeceras COOP-COEP (que GitHub Pages no puede establecer) usando el core de un solo hilo (single-thread). **No toques este bloque de arranque del `<script>`** salvo que trabajes explícitamente en el motor — las URLs del CDN (`@ffmpeg/ffmpeg@0.12.6`, `@ffmpeg/core@0.12.6`, `@ffmpeg/util@0.12.1`) y el parche son interdependientes.

## Pipeline de conversión (el handler de `convertBtn`)

Los archivos se añaden a un `Map<id, entry>` y quedan `pending` — **nada se procesa hasta que el usuario pulsa Convertir**. Entonces cada archivo se procesa secuencialmente en el sistema de archivos virtual de WASM:

1. **Sondea (probe)** los códecs ejecutando `ffmpeg.exec(['-i', input])` y extrayendo con regex los nombres de los códecs de audio/vídeo de la salida del log.
2. **Decide el comando** a partir del probe:
   - Entrada solo de audio → salida `.flac` (`-vn -c:a flac`).
   - Entrada de vídeo → salida `.mkv`, stream de vídeo **copiado** (`-c:v copy`, remux sin pérdida), audio recodificado a FLAC.
   - Códecs de vídeo que el navegador no puede decodificar (ProRes, DNxHD, MJPEG, MPEG-2, VC-1, WMV, …) → recodificar a H.264 (`libx264 -preset ultrafast -crf 18`) para que funcione la previsualización en la página.
   - Audio PCM flotante (`pcm_f32le`, etc.) → insertar `aformat=sample_fmts=s32` antes de FLAC (FLAC necesita muestras enteras).
3. **Fallback ante fallo:** si un remux con `-c:v copy` lanza error, reinicializa el motor y reintenta con libx264.
4. **Recuperación de errores:** ffmpeg.wasm puede caer en seco ("Aborted"); ante cualquier error por archivo el motor se recarga por completo (`loadFFmpeg()`) para que los archivos siguientes sigan convirtiéndose.
5. La salida se lee de vuelta, se envuelve en un Blob + object URL, y los archivos del FS virtual se eliminan.

## Convenciones de renderizado de la UI

- El estado vive en el `Map` `files`; `renderFileList()` y `renderPreviewList()` re-renderizan a partir de él. Los botones usan delegación de eventos mediante `data-action` / `data-id`.
- `renderPreviewList()` es intencionadamente **idempotente** — reutiliza los elementos `<video>`/`<audio>` existentes y solo actualiza etiquetas/enlaces, de modo que re-renderizar (p. ej. tras un renombrado en línea) **no** reinicia la reproducción del medio. Conserva esto al modificarla.
- Los archivos de salida se pueden **renombrar en línea tras la conversión sin reconvertir** — solo cambian `outBaseName` y el enlace de descarga; se mantiene el mismo Blob/object URL.

## Las 20 landings se generan — no las edites a mano

`build_pages.py` genera las páginas `/convertir-*-a-flac/` usando `index.html`
como plantilla más el contenido único de cada formato, que vive en el array
`PAGES` (dentro del propio `build_pages.py`) y en el diccionario `CONTENT` de
`landing_content.py`.

**Consecuencia que cuesta cara: cualquier corrección de texto aplicada
directamente al HTML de una landing se pierde en la siguiente regeneración.**
Ha pasado de verdad — un barrido de estilo se revirtió entero al ejecutar el
generador, porque el texto original seguía en `landing_content.py`. Si un
`grep` encuentra algo que arreglar en `convertir-*/index.html`, busca ese mismo
texto en `landing_content.py` y en `build_pages.py`, arréglalo **ahí**, y
regenera.

Invariantes que el generador ya respeta y que no hay que romper:

- **hreflang:** las 20 landings salen **sin** bloque hreflang. No tienen versión
  inglesa, así que heredar el de la home hacía que declarasen la portada como su
  versión española, contradiciendo su propio canonical. `convertir-formatos/`
  es la excepción: sí tiene contraparte (`/en/convert-formats/`) y sí lo lleva.
- **robots:** solo cuatro landings se ofrecen a Google (conjunto `INDEXABLE`:
  mp4, mkv, mov, wav). El resto va `noindex, follow`.
- **sitemap:** `update_sitemap()` nunca añade una página `noindex` ni duplica
  una `<loc>`. Una `noindex` dentro del sitemap es un error en Search Console.

Antes de regenerar, haz siempre una pasada en seco comparando la salida del
generador con el disco. Después de regenerar, **debe dar 0 líneas de
diferencia**: si no, disco y generador han divergido.

## Un mismo texto vive en muchos sitios a la vez

Nunca cambies una cadena en un solo lugar. Un titular de artículo aparece en
6-8 sitios: `<title>`, `og:title`, `twitter:title`, el `"headline"` del JSON-LD,
el `<h1>`, la `card-title` del índice, los enlaces anterior/siguiente de **otros**
artículos, y el índice de búsqueda JS. Haz la sustitución sobre todo el repo y
**cuenta las ocurrencias**: si el español da 7 y el inglés 2, falta algo.

Dos trampas concretas, ambas sufridas:

- **Los índices de búsqueda** (`articulos/index.html` y `en/articles/index.html`)
  guardan el texto de cada artículo en campos `text:` que son cadenas JS entre
  **comillas simples**. Meter un apóstrofo ahí (`browser's`) rompe el buscador de
  esa página sin ningún aviso. Evita apóstrofos o escápalos, y pasa `node --check`.
- **Los bloques JSON-LD de FAQ** duplican el texto visible. Insertar
  `<a href="...">` en una frase que también está en el JSON-LD invalida el JSON
  por las comillas. En JSON-LD va texto plano, sin marcado.

## Comprobaciones antes de dar algo por terminado

```bash
# JS de las 67 páginas (los índices de búsqueda se rompen en silencio)
for f in $(find . -name '*.html' -not -path './.git/*'); do
  python3 -c "
import re,sys
s=open('$f',encoding='utf-8').read()
b=re.findall(r'<script(?![^>]*\bsrc=)(?![^>]*application/ld)[^>]*>(.*?)</script>',s,re.S)
open('/tmp/_c.mjs','w').write('\n;\n'.join(b))"
  node --check /tmp/_c.mjs || echo "ROTO: $f"
done

# JSON-LD (204 bloques), enlaces internos, sitemap
python3 -c "
import re,json,glob
n=b=0
for f in glob.glob('**/*.html',recursive=True):
    if f.startswith('.git'): continue
    for m in re.findall(r'<script type=\"application/ld\+json\">(.*?)</script>',open(f,encoding='utf-8').read(),re.S):
        n+=1
        try: json.loads(m)
        except Exception as e: b+=1; print('ROTO',f,e)
print(n,'bloques,',b,'rotos')"
```

Valores de referencia: **67** páginas HTML, **48** indexables y **19** `noindex`,
**44** con hreflang, **204** bloques JSON-LD, **48** URLs en el sitemap, **0**
enlaces internos rotos, y el generador en **0** líneas de diferencia.

## Promesas que el producto no puede sostener

El sitio arrastraba afirmaciones que no se cumplen. Al escribir texto nuevo:

- **Nada de cronómetros.** Ni "menos de 30 segundos", ni "en segundos", ni
  "instantáneo". Se dice la relación ("mucho más rápido que una conversión
  completa, porque el vídeo no se recodifica") y de qué depende: tamaño, equipo,
  y si hay que recodificar. Las estimaciones con su condición explícita
  ("depende de tu ordenador") sí valen.
- **El vídeo no siempre se copia.** `browserIncompatibleVideo` en `index.html`
  recodifica a H.264 cuando el navegador no puede decodificar el códec, y esa
  lista **incluye H.265/HEVC** — el caso más frecuente hoy, porque los iPhone
  graban en HEVC desde iOS 11. Toda afirmación de "se copia bit a bit / la
  imagen es idéntica" necesita su condición al lado. Contrasta siempre el texto
  contra esa constante del código, no contra lo que diga otro artículo.
- **Nada de absolutos.** Ni "la única solución", ni "no funciona en ningún
  sistema", ni "todos los errores". El soporte de códecs depende de versión,
  plataforma y configuración.
- **El límite de tamaño.** "Sin límite impuesto por un servidor" siempre con la
  matización de que el techo práctico es la memoria de WebAssembly (~2 GB de
  heap de 32 bits, single-thread).

## Verificar los comandos FFmpeg, no razonarlos

Hay `ffmpeg` en el sistema: los comandos que aparecen en los artículos se
ejecutan contra archivos de prueba en vez de darlos por buenos. Así apareció el
fallo más grave del contenido: tres guías recomendaban
`-vsync cfr -c:v copy` para convertir VFR a CFR, y **no hace nada** — copiar el
flujo no permite reescalar los tiempos de los fotogramas, así que la salida
conserva el frame rate variable del origen. Lo correcto es `-vf fps=N` con
recodificación. Se comprueba con `ffprobe -show_entries stream=avg_frame_rate`.

## Sistema de diseño

Estética oscura de "mesa de mastering": lienzo casi negro y cálido con un único **acento verde de señal** (`--amber` es verde `#19c37d`, a pesar del nombre) más colores de estado. Fuentes: Bricolage Grotesque (display), Hanken Grotesk (cuerpo), JetBrains Mono (etiquetas/logs/meta). Las custom properties de CSS en `:root` controlan todo; reutiliza los tokens existentes (`--ink*`, `--line*`, `--radius*`) y las clases de componentes (`.card`, `.badge`, `.trust-card`, etc.) en lugar de introducir colores nuevos. Respeta `prefers-reduced-motion`.
