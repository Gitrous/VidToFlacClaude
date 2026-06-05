# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) al trabajar con el código de este repositorio.

## Qué es esto

VidToFLAC es una aplicación web de **una sola página y 100% del lado del cliente** que reempaqueta (remux) vídeo en un MKV con una pista de audio FLAC sin pérdida (o transcodifica archivos solo de audio a FLAC), para solucionar el problema de "sin audio / error de códec de audio" en DaVinci Resolve, Premiere y Avid. Todo el procesamiento ocurre localmente en el navegador mediante **ffmpeg.wasm** — nunca se sube nada. El sitio está en **español** (textos de UI, logs, comentarios) y está muy optimizado para SEO en torno al caso de uso del códec de audio de DaVinci Resolve.

## Toda la app es `index.html`

**No hay sistema de build, dependencias, tests ni package.json.** `index.html` (~2200 líneas) contiene todo en línea: el `<head>` de SEO (meta, Open Graph, varios bloques JSON-LD), todo el CSS en un único `<style>`, el cuerpo HTML y la lógica de la aplicación en un solo `<script type="module">`. Los demás archivos versionados son recursos estáticos (iconos, `og-image.png`, `robots.txt`, `sitemap.xml`, `site.webmanifest`, `CNAME`).

Al editar, conserva la estructura de archivo único — no separes en archivos JS/CSS aparte.

## Flujo de trabajo tras cada cambio

**Después de completar cualquier cambio**, pregunta siempre al usuario:

> "¿Quieres arrancar un servidor para verlo (**s**) o subirlo a GitHub (**g**)?"

El usuario responde con una sola letra:

- **`s`** → **Servidor / previsualizar**: arranca `python3 -m http.server 8000` (si no hay ya un servidor corriendo en ese puerto) y muestra una captura headless del resultado.
- **`g`** → **Subir a GitHub**: haz commit de los archivos modificados directamente a `main` y push. El despliegue en GitHub Pages se dispara automáticamente.

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

## Sistema de diseño

Estética oscura de "mesa de mastering": lienzo casi negro y cálido con un único **acento verde de señal** (`--amber` es verde `#19c37d`, a pesar del nombre) más colores de estado. Fuentes: Bricolage Grotesque (display), Hanken Grotesk (cuerpo), JetBrains Mono (etiquetas/logs/meta). Las custom properties de CSS en `:root` controlan todo; reutiliza los tokens existentes (`--ink*`, `--line*`, `--radius*`) y las clases de componentes (`.card`, `.badge`, `.trust-card`, etc.) en lugar de introducir colores nuevos. Respeta `prefers-reduced-motion`.
