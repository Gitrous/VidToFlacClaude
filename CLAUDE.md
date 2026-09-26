# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) al trabajar con el código de este repositorio.

## Qué es esto

VidToFLAC es una aplicación web de **una sola página y 100% del lado del cliente** que reempaqueta (remux) vídeo en un MKV con una pista de audio FLAC sin pérdida (o transcodifica archivos solo de audio a FLAC), para solucionar el problema de "sin audio / error de códec de audio" en DaVinci Resolve, Premiere y Avid. Todo el procesamiento ocurre localmente en el navegador mediante **ffmpeg.wasm** — nunca se sube nada. El sitio está en **español** (textos de UI, logs, comentarios) y está muy optimizado para SEO en torno al caso de uso del códec de audio de DaVinci Resolve.

## Sincronización con la versión en inglés

**Cualquier cambio en `index.html` (versión principal en español) debe aplicarse también a `en/index.html` (versión en inglés).** Esto incluye cambios de CSS, layout, lógica JS, slots de anuncios, y cualquier elemento estructural. Los textos de UI van traducidos al inglés; el resto del código es idéntico.

## Toda la app es `index.html`

**No hay dependencias, tests ni package.json.** Sí hay un generador, `build_pages.py`, pero solo para las landings de formato: 12 páginas completas y 32 redirecciones (ver más abajo); la app en sí no se compila. `index.html` (~2200 líneas) contiene todo en línea: el `<head>` de SEO (meta, Open Graph, varios bloques JSON-LD), todo el CSS en un único `<style>`, el cuerpo HTML y la lógica de la aplicación en un solo `<script type="module">`. Los demás archivos versionados son recursos estáticos (iconos, `og-image.png`, `robots.txt`, `sitemap.xml`, `site.webmanifest`, `CNAME`).

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

GitHub Pages en **modo legacy**, origen = rama `main` raíz (`/`), dominio personalizado `vidtoflac.tech` (definido por `CNAME`).

**El HTTPS no lo pone GitHub, lo pone Cloudflare**, que hace de proxy delante del dominio (las respuestas llevan `Server: cloudflare`). Por eso `gh api repos/Gitrous/VidToFlacClaude/pages` da `https_enforced: false` y ningún certificado: GitHub no puede emitirlo con el proxy delante. Comprobado el 26-09-2026: `http://vidtoflac.tech/` respondía **200 sin redirigir** a HTTPS. La canónica evita el duplicado, pero la redirección se activa en Cloudflare (SSL/TLS → *Always Use HTTPS*), no en el repositorio. `www` sí redirige (301) al dominio sin `www`. **Hacer push a `main` dispara automáticamente un despliegue** — no hay archivo de workflow. El flujo establecido es commitear directamente a `main` (sin ramas de feature ni PRs). Verifica un despliegue con:

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

## Las landings se generan — no las edites a mano

`build_pages.py` genera, por idioma (español desde `index.html`, inglés desde
`en/index.html`):

- **4 landings propias**: MP4, MKV, MOV y WAV (`/convertir-mp4-a-flac/`,
  `/en/convert-mp4-to-flac/`…).
- **2 landings agrupadas**: `/convertir-video-a-flac/` (AVI, WebM, WMV, FLV,
  MPEG, TS, VOB, 3GP, M4V) y `/convertir-audio-a-flac/` (MP3, AAC, M4A, AIFF,
  OGG, Opus, WMA), con sus equivalentes en `/en/`. Cada formato es una sección
  con ancla (`#avi`, `#opus`…).
- **16 redirecciones** en las URL antiguas de esos formatos, que llevan a su
  sección (`noindex`, canonical y `meta refresh`, igual que `en/articulos/`).

El texto de cada formato sigue en `PAGES` (dentro de `build_pages.py`) y
`CONTENT` (`landing_content.py`), o en `PAGES_EN`/`CONTENT_EN`
(`landing_content_en.py`): **las guías de los formatos agrupados se editan ahí**,
aunque ya no tengan página propia. Lo que es de la página agrupada —cabecera,
índice, "La solución" y FAQ— está en `merged_content.py`.

**Por qué se juntaron en vez de borrarse.** Las 32 landings minoritarias eran
`noindex` y se parecían hasta un 82 % entre sí (las inglesas, escritas sobre
plantilla). Juntas, cada página agrupada comparte un 13-27 % de n-gramas con la
portada. Al juntarlas aparecieron dos cosas que no se ven con páginas sueltas:

- **La repetición se traslada dentro de la página.** Las guías inglesas repetían
  pasos y cierre con el nombre del formato cambiado: un 40-44 % de las secciones
  eran iguales entre sí. `dedupe_sections()` conserva la primera aparición de
  cada bloque y quita las demás (queda en 1-8 %). Por eso las FAQ tampoco se
  heredan: si `merged_content.py` trae `faqs`, mandan esas.
- **Enlaces viejos.** `rewrite_old_links()` apunta a la sección nueva todo
  enlace o `data-url` de una landing absorbida en las páginas generadas; en las
  que no genera el script (portadas, artículos) hay que cambiarlos a mano.

Los textos de la plantilla que hay que sustituir están en `A_ES` y `A_EN`, un
diccionario de anclajes por idioma. Los largos no se copian a mano: se extraen
de la propia plantilla en `_fill_anchors()`, porque cuando estaban escritos
literalmente se desincronizaron sin avisar y el `replace` pasó a ser un no-op
silencioso — así fue como las landings acabaron heredando las keywords de la
home durante meses.

**Consecuencia que cuesta cara: cualquier corrección de texto aplicada
directamente al HTML de una landing se pierde en la siguiente regeneración.**
Ha pasado de verdad — un barrido de estilo se revirtió entero al ejecutar el
generador, porque el texto original seguía en `landing_content.py`. Si un
`grep` encuentra algo que arreglar en `convertir-*/index.html`, busca ese mismo
texto en `landing_content.py` y en `build_pages.py`, arréglalo **ahí**, y
regenera.

Invariantes que el generador ya respeta y que no hay que romper:

- **hreflang:** cada landing declara su par ES/EN autorreferenciado, que se
  calcula en `hreflang_for()` a partir del diccionario `PAIRS`. Mientras no
  existió la versión inglesa el bloque se eliminaba, porque heredar el de la
  home hacía que cada landing declarase la portada como su versión española,
  contradiciendo su canonical. Si añades un formato sin su par, no lo metas en
  `PAIRS`: sin par, sin hreflang.
- **selector de idioma:** `build_page()` reescribe el enlace `.nav-lang` para
  que apunte a la página equivalente y no a la portada del otro idioma.
- **robots:** las 12 páginas completas están en `INDEXABLE`; las
  redirecciones van `noindex, follow`.
- **la guía técnica compartida se elimina** (`RE_SHARED_GUIDE`). Copiada tal
  cual, esas ~916 palabras hacían que cada landing fuese un 64 % idéntica a la
  portada y a sus hermanas, y Google rechazó AdSense por "contenido de poco
  valor". Cada landing ya trae su propia guía en `unique_guide`. Al añadir
  contenido a la home, comprueba que no se replica a las 12.
- **sitemap:** `update_sitemap()` nunca añade una página `noindex` ni duplica
  una `<loc>`. Una `noindex` dentro del sitemap es un error en Search Console.

Antes de regenerar, haz siempre una pasada en seco comparando la salida del
generador con el disco. Después de regenerar, **debe dar 0 líneas de
diferencia**: si no, disco y generador han divergido.

## El feed RSS se genera, como las landings

`build_feed.py` escribe `feed.xml` y `en/feed.xml` leyendo los 16 artículos de
cada idioma. Saca el titular del `"headline"` del JSON-LD y no del `<title>`,
porque el `<title>` lleva a veces el sufijo del sitio; la entradilla sale de la
`meta description`, y las fechas de `datePublished` / `dateModified`. Un
artículo sin `datePublished` se omite con un aviso en vez de inventarle una
fecha, porque un `<item>` sin `pubDate` desordena el feed en cualquier lector.

Al publicar un artículo hay que **ejecutar `build_feed.py`**: es el noveno sitio
que tocar, además de los ocho de la sección de arriba. Tiene `--dry-run`, igual
que `build_pages.py`.

El `<link rel="alternate" type="application/rss+xml">` está en **52 páginas**:
portada, índice de artículos, los 32 artículos, las 12 landings, el banco de
pruebas y las páginas de autor, cada idioma apuntando a su propio feed. En las
landings no se pone a mano: viene de `index.html` y `en/index.html` a través del
generador. Comprueba que ninguna página española enlace `en/feed.xml`.

## Medir duplicación: n-gramas, nunca vocabulario

Para saber si dos páginas son duplicados, compara **conjuntos de n-gramas de 8
palabras**, no vocabulario compartido. La diferencia no es académica: sobre las
mismas landings, el solapamiento de vocabulario daba 36-45 % (tranquilizador) y
el de n-gramas 64-67 % (motivo real del rechazo de AdSense). El vocabulario
coincide por fuerza entre páginas del mismo tema; lo que delata el copiado son
las secuencias literales.

Referencia actual (25-09-2026, después de adelgazar las landings): **18,7-20,7 %**
entre las cuatro landings propias y su portada, y **28-29 %** en el peor par de
landings entre sí. Lo que queda es cabecera, pie, los controles del conversor y
el texto de consentimiento: *boilerplate* funcional que no se puede quitar sin
romper la página. Las páginas agrupadas van en el 4,6-9,7 %, y los artículos y
el banco de pruebas en el 1 %.

Antes de ese cambio eran **37-39 %** contra la portada y **39,5 %** entre
landings. Si vuelves a ver cifras así, alguien ha repuesto un bloque de la
portada en la plantilla: mira la sección siguiente.

## Las landings llevan el conversor, no la portada entera

AdSense rechazó por "contenido de poco valor" una **tercera** vez el 22 de
septiembre de 2026, después de dos semanas añadiendo contenido original medido.
Eso descartaba los artículos, así que se midió el sitio entero con n-gramas de 8
palabras y salió dónde estaba: los artículos y el banco compartían un **1 %** con
la portada, pero las cuatro landings propias un **37-39 %**, y entre ellas hasta
un **39,5 %**. Desglosada una landing, **683 de sus 1.991 palabras eran la
interfaz de la portada copiada**.

`strip_home_chrome()` en `build_pages.py` quita de las doce landings, con el
mismo patrón que `RE_DEMO` y `RE_SHARED_GUIDE`:

- los **pilares de confianza** (`RE_TRUST`),
- los **pasos "Cómo funciona"** (`RE_STEPS`),
- la tarjeta **"Antes y después"** (`RE_COMPARE`),
- el **selector de formato** del paso 01 (`RE_FORMAT_PICKER`), que ofrece las
  veinte guías: en la portada es navegación, dentro de la guía de MP4 es la
  lista otra vez. El JS ya lo daba por opcional (`formatDropdown?.` y
  `if (ddSummary && ddPanel)`), así que no rompe nada,
- el **párrafo compartido** de la sección del problema (`RE_PROBLEM_SHARED`), el
  de "muchas cámaras graban en AAC". Alrededor todo es propio —el h2, la
  entradilla y, desde el `<h3>`, el `seo_body` de cada formato—, así que
  quitándolo la sección entera pasa a ser única,
- el **JSON-LD de `HowTo`** (`RE_HOWTO_JSONLD`), porque sus tres pasos dejan de
  estar visibles y los datos estructurados describen lo que la página muestra.
  De ahí que los bloques JSON-LD bajaran de 210 a 198.

**Las secciones de cierre se tratan distinto según el idioma**, y la condición
está en el código: si la sección lleva `<nav>` se conserva sin su entradilla, y
si no, sobra entera. La española mete los enlaces a los artículos dentro de la
misma sección de formatos; la inglesa los tiene en `guides-titulo` y su
`formatos-titulo` es solo texto repetido, así que desaparece.

**El hueco de anuncio se recoloca** (`RE_AD_TOOL`). Iba "entre la herramienta y
el contenido SEO", apoyado en la tarjeta "Antes y después"; sin ella quedaba
pegado al panel de registro del conversor, que es el patrón de clic accidental
que AdSense trata como infracción. En las landings baja hasta justo antes de las
preguntas frecuentes, con texto por arriba y un encabezado por abajo. La portada
no se toca.

Lo que **sí** se queda en la landing: el conversor completo —zona de arrastre,
botón de convertir, progreso, previsualización, registro—, los dos `.ad-modal`,
la cabecera, el pie y los enlaces internos. Una landing sigue siendo una página
donde se puede convertir; lo que ya no es es otra copia de la home.

Al añadir un bloque nuevo a `index.html`, pregúntate si tiene sentido repetido
doce veces. Si no, añádele su regex aquí.

## Enlaces que Google puede seguir: `<a href>`, no botones

El 26-09-2026, con Search Console mostrando solo 6 páginas indexadas, se midieron
los enlaces internos que recibe cada página indexable (solo `<a href>` del
cuerpo, sin `<head>` ni JS). Las páginas que más importan eran las peor
enlazadas: las cuatro landings propias recibían 5 y las dos guías medidas 4-5,
frente a una mediana de 11.

El motivo: **la portada solo llevaba a las landings a través del selector de
formato, que usa `<button data-url>`**, y Google no sigue botones. La página más
fuerte del sitio no les pasaba ni un enlace. Se añadieron seis `<a href>` a la
sección de cierre "Guías y artículos" de las dos portadas (las cuatro landings y
las dos guías medidas). Como esa `<nav>` sobrevive en las landings, también se
enlazan entre ellas. Resultado: de 4-5 a 10-12 enlaces entrantes, sin subir la
duplicación.

Al añadir una página que importa, compruébalo: que tenga enlaces `<a href>`
desde la portada o desde páginas que la reciben. Un `data-url`, un `onclick` o
un botón no cuentan.

## Anuncios dentro de la herramienta: quitados, y lo que costó verlos

El 26-09-2026 se quitaron el aviso de "3 conversiones gratuitas" con anuncio y
los anuncios que se insertaban en la lista de resultados, porque incumplen las
políticas de AdSense (recompensa por ver un anuncio, anuncio encima de un botón,
anuncios entre botones de descarga). Está todo en el commit aislado `45520eb`:
el usuario quiere recuperarlo más adelante, pero **no tal cual** — antes de un
`git revert` hay que proponerle una forma que cumpla.

Tres cosas que salieron al hacerlo:

- **Los anuncios que mete el JavaScript no se ven en el HTML.** La comprobación
  de "ningún anuncio junto a los controles" buscaba `<ins class="adsbygoogle">`
  fijos, y dio 0 mientras la lista de resultados recibía un anuncio cada cinco
  archivos. Busca también `className = 'adsbygoogle'` y `adsbygoogle.push` fuera
  de los huecos conocidos.
- **`node --check` solo mira la sintaxis.** Al quitar el bloque de la cuota,
  `fmtName` se quedó sin declarar en las páginas de formatos: el JS pasaba la
  comprobación y el botón de convertir moría al ejecutarse. Después de borrar
  código, pruébalo en el navegador.
- **Hay cuatro copias del conversor, no dos.** Además de `index.html` y
  `en/index.html`, `convertir-formatos/` y `en/convert-formats/` llevan su propia
  copia (una herramienta de conversión entre formatos), hecha a mano y fuera del
  generador. Y **las dos portadas ya no tienen el JS idéntico**: la selección de
  pistas se escribió distinta en cada idioma (la española aplica la cuota y
  luego sondea; la inglesa sondea primero, con `probedBatch` y `actualList`). Un
  cambio en la lógica hay que comprobarlo en las cuatro.

## La versión inglesa se escribe, no se traduce a medias

Al generar las landings inglesas aparecieron 14 cadenas en español dentro del
`<script type="module">` de `en/index.html` —las etiquetas del motor ("En
espera", "Cargando"), los avisos de tamaño, los mensajes del registro— visibles
para cualquier usuario anglófono y heredadas por las 20 páginas nuevas.
`en/convert-formats/index.html` tenía otras 5, y como no lo genera el script
hubo que traducirlo aparte.

Al tocar textos de la interfaz, barre el JS de `/en/` buscando `[ñáéíóú]` en
literales de cadena. Es una comprobación de dos líneas que detecta justo lo que
la revisión visual pasa por alto, porque son mensajes que solo aparecen durante
una conversión.

## La demo en vídeo de la portada

`media/demo-es.mp4` y `media/demo-en.mp4` (~950 KB, 29 s, 1280×800, H.264 +
AAC con `faststart`) muestran el problema y la solución con una grabación real.
Viven solo en `index.html` y `en/index.html`; `build_pages.py` los retira de
las landings con `RE_DEMO`, porque repetir el bloque y su `VideoObject` en
cada una sería otra fuente de duplicado.

Tres decisiones que no son obvias y que no conviene deshacer:

- **Los rótulos van en una franja superior, no inferior.** La barra de
  controles del reproductor ocupa la parte baja del vídeo y, en pausa o al
  pasar el ratón, tapaba exactamente el mensaje. Solo se ve en el navegador,
  no en los fotogramas extraídos con ffmpeg: compruébalo con una captura.
- **La sección va después del hueco de anuncio**, con título y entradilla de por
  medio. Colocada antes, los controles del reproductor quedaban pegados al
  anuncio: riesgo de clic accidental, que AdSense trata como infracción.
- **`preload="none"` con póster**: la página solo descarga la imagen (~85 KB)
  hasta que alguien pulsa reproducir. Sin autoplay, así que el audio suena al
  pulsar, que es lo que la demo necesita: el contraste silencio → sonido.

**Lo que demuestra la grabación contradice parte del sitio.** El archivo
original era H.264 + **AAC-LC**, y **DaVinci Resolve Studio 21 sobre Linux no
lo reprodujo**. Tres artículos por idioma decían lo contrario (Studio "incluye
AAC en Linux", tablas con "Parcial", FAQ "solo algunos perfiles de AAC" cuando
falló el perfil más común); ya están corregidos citando la prueba y enlazando
a `/#demo-titulo`. La evidencia de primera mano gana a lo que diga cualquier
artículo. No escribas "Studio lo soluciona en Linux" sin una prueba nueva que
lo demuestre.

Al corregir una afirmación, lee el artículo entero en una captura, no solo la
frase buscada: en `davinci-resolve-gratuito-vs-studio`, dos párrafos más abajo
de la advertencia seguían "copia el vídeo bit a bit (cero pérdida de calidad)"
y "el problema desaparece completamente", que ningún `grep` sobre Studio/AAC
iba a encontrar.

Un barrido por frases largas no detecta promesas escritas como viñetas cortas:
la tarjeta "Antes y después" de la portada conservaba "Proceso en segundos,
solo se toca el audio" y "Sin errores de códec… en Windows, macOS y Linux"
después de varios barridos. Revisa también los `<li>` de las tarjetas.

## Autoría: el sitio lo firma una persona

AdSense rechazó dos veces por "contenido de poco valor" con el sitio en
anónimo: `author` era la propia Organization y el nombre real solo aparecía en
un párrafo suelto de `/sobre-vidtoflac/`. Ahora la autoría vive en cuatro
sitios a la vez, y hay que mantenerlos sincronizados:

1. `/autor/guillem-sanchez/` y `/en/author/guillem-sanchez/` — página propia con
   `ProfilePage` + `Person` (`sameAs` a github.com/Gitrous), el equipo de pruebas
   (DaVinci Resolve Studio 21 sobre Ubuntu) y la lista de afirmaciones corregidas
   tras probarlas. Al publicar un artículo nuevo, **añádelo a esa lista**.
2. La firma de `.hero-meta` en los 28 artículos (`rel="author"`).
3. La caja `.author-box` al final del `<article>`, antes de `.prev-next-nav`.
4. El `author` de tipo `Person` en el JSON-LD `Article`, con `url` a la página de
   autor del idioma correspondiente. `publisher` sigue siendo la Organization.

Las páginas institucionales llevan ahora `AboutPage`, `ContactPage` con
`ContactPoint`, `WebPage` en las legales, y `BreadcrumbList` en todas.

## Imágenes propias: de dónde salen y dónde no van

Las capturas de `media/capturas/` se extraen con ffmpeg de las grabaciones
originales del usuario (`~/Descargas/Clip1.mp4` y `Clip2.mp4`, 1920×1080), no
del montaje publicado: el montaje lleva rótulos quemados en una franja superior
y ata la imagen a un idioma. Se recorta la zona útil y se codifica en WebP
(`-c:v libwebp -quality 80-82`, 1100-1200 px de ancho, 8-25 KB cada una).

Reglas que ya están aplicadas y conviene no romper:

- **Ninguna figura pegada a un anuncio.** Al insertarlas antes de un `<h2>`
  quedaron justo debajo del hueco de anuncio, que es el patrón de clic
  accidental que AdSense penaliza. Van después del primer párrafo de la sección.
  Hay un script de comprobación en el historial de esta tarea; repítelo al añadir
  figuras.
- **El pie es contenido, no decoración**: dice qué se ve, con qué versión y en
  qué sistema. El `alt` describe la imagen y no repite el pie.
- `width`, `height`, `loading="lazy"` y `decoding="async"` siempre, para no
  mover el layout.
- Los diagramas son **SVG en línea** con los tokens de color del sitio, sin
  archivos ni peticiones. El mismo SVG se reutiliza en varios artículos: su
  texto cuenta como contenido compartido, así que no lo repitas en más de
  cinco páginas por idioma.

Al añadir un gráfico, la paleta se valida con el script de la skill de
visualización antes de dibujarlo. El verde del sitio (`#19c37d`) **no pasa** la
banda de luminosidad como color de serie: el gráfico de tamaños usa `#12a068`
con `#9b7bc8`, que sí pasa las seis comprobaciones sobre fondo oscuro.

## El banco de pruebas es la fuente de verdad

`/banco-de-pruebas/` y `/en/test-bench/` publican diecisiete combinaciones de
contenedor y códec generadas con FFmpeg y pasadas por la misma cadena que
ejecuta la app. **Si una guía contradice esa tabla, gana la tabla.** Al añadir
una afirmación sobre qué se copia, qué se recodifica o cuánto ocupa algo,
mídela allí primero y enlaza la página.

Lo que salió de la primera tanda, todo verificado el 19 de septiembre de 2026:

- Se copian H.264, AV1, VP8, VP9 y MPEG-4 (Xvid). Se recodifican a H.264 siete:
  WMV2, MPEG-2 y HEVC porque el navegador no los decodifica, y H.263, Theora,
  FLV1 y MS MPEG-4 v3 porque **Resolve los importa sin imagen** (ver más abajo).
  Ninguno de los diecisiete archivos falló al convertir.
- Desde audio con pérdida, el FLAC **engorda** el archivo; desde PCM lo reduce;
  un FLAC de entrada sale idéntico byte a byte.
- Recodificar HEVC a H.264 multiplicó el tamaño por cinco.
- La compresión de FLAC va del 53 % del WAV (ruido blanco, peor caso) al 6 %
  (grabación de pantalla real). **Nunca des un porcentaje único.**

Dato que conviene recordar: **las grabaciones originales del usuario
(`~/Descargas/Clip1.mp4` y `Clip2.mp4`) son AV1 con audio FLAC**, no H.264 con
AAC. El montaje publicado sí es H.264 + AAC porque se recodificó al montarlo.

## Copyright: cómo se habla de vídeo ajeno

AdSense tiene una política aparte sobre facilitar el acceso a contenido
protegido, y este sitio explica cómo convertir vídeo. Por eso no se nombran
descargadores (yt-dlp, KeepVid, Zamzar y similares) ni se plantea la descarga
de vídeo de terceros como caso de uso. Se habla de *vídeo publicado en la web
del que tengas los derechos*, de grabaciones propias y de material de archivo
propio. Los hechos técnicos —que YouTube sirve Opus en WebM, por ejemplo— sí
se pueden contar: lo que no se hace es dar el método para bajarlo.

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
# JS de las 87 páginas (los índices de búsqueda se rompen en silencio)
for f in $(find . -name '*.html' -not -path './.git/*'); do
  python3 -c "
import re,sys
s=open('$f',encoding='utf-8').read()
b=re.findall(r'<script(?![^>]*\bsrc=)(?![^>]*application/ld)[^>]*>(.*?)</script>',s,re.S)
open('/tmp/_c.mjs','w').write('\n;\n'.join(b))"
  node --check /tmp/_c.mjs || echo "ROTO: $f"
done

# JSON-LD (306 bloques), enlaces internos, sitemap
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

Valores de referencia: **99** páginas HTML, **64** indexables y **35** `noindex`,
**66** con hreflang, **198** bloques JSON-LD, **64** URLs en el sitemap, **0**
enlaces internos rotos (anclas `#formato` incluidas), **0** descripciones de más
de 160 caracteres, y el generador en **0** líneas de diferencia.

## Publicar un artículo nuevo: los ocho sitios que hay que tocar

Un artículo no es un directorio con un `index.html`. Al añadir uno hay que
actualizar, en los dos idiomas: (1) el archivo nuevo, generado a partir de otro
artículo como plantilla —se sustituyen `<head>`, hero, índice lateral, cuerpo,
anterior/siguiente y relacionados, y se conserva todo lo demás—; (2) la tarjeta
del índice (`articulos/index.html`), que lleva su propia miniatura SVG de
400×110; (3) el `CORPUS` del buscador de ese índice, con el texto **sin
apóstrofos**; (4) el `prev-next-nav` de los dos artículos vecinos, que en los
extremos de la cadena tienen un `<div></div>` vacío que hay que sustituir; (5)
la lista «Guías que he escrito» de la página de autor; (6) el `sitemap.xml`; y
(7) los valores de referencia de aquí arriba. Falta uno y el artículo queda
huérfano sin que ninguna comprobación se queje.

Dos cosas que solo se ven ejecutando:

- **`.error-box` no tiene CSS compartido: cada artículo lleva la regla en su
  `<style>`.** Durante meses 34 cajas en 12 artículos se quedaron sin borde,
  porque sus estilos en línea fijan el color pero no `border-style`. Arreglado
  el 25-09-2026 copiando solo la regla de la caja. **No copies también
  `.error-box code{display:block;white-space:pre}`** de los artículos nuevos: en
  los viejos la caja lleva prosa con `<code>` en línea, y esa regla convierte
  cada código en un bloque. Al crear un artículo a partir de otro, comprueba que
  la regla viaja con la plantilla.
- **Las etiquetas de un gráfico se solapan con las barras.** El texto de la
  izquierda no se recorta solo: si pasa de la `x` donde empiezan las barras, se
  superpone. Solo se ve en una captura, no en el SVG.

Y el error que se coló dos veces en el mismo sitio: formatear miles con
`.replace(',', '.')` sobre la cadena entera del SVG convierte también
`font-family="JetBrains Mono, ui-monospace, monospace"` en
`"JetBrains Mono. ui-monospace. monospace"`, que el navegador descarta. El
gráfico del banco de pruebas lo arrastró desde su primera versión, y se había
copiado al artículo de HEVC; arreglados los dos el 25-09-2026 (16 atributos).
Los `rgba()` y las coordenadas de esos SVG no salieron dañados. Comprobación:
`grep -rE 'font-family="[^"]*\. ' --include=*.html .` tiene que dar vacío.

## El audio tiene que empezar en cero, y el vídeo casi siempre se copia

Dos cosas distintas, aprendidas el 20-22 de septiembre de 2026 sobre Studio
21.0.4 en Ubuntu, y una de ellas por el camino largo.

**1. DaVinci Resolve exige que la pista de audio arranque exactamente en 0.**
Con 3 ms de desfase basta para que importe el clip con la caja de audio puesta
y sin sonido hasta el final. Al vídeo el desfase le da igual: hay archivos con
la imagen empezando en 0,005 y 0,021 s que suenan perfectamente. La correlación
sobre los diecisiete archivos del banco no tiene excepciones — audio en 0,000,
suena; audio en 0,007 / 0,003 / 0,086, falla.

El desfase lo trae el origen: Opus guarda un *pre-skip* en su cabecera (el WebM
llega con el audio en −0,007 s) y ASF trae su preroll. Como FFmpeg no escribe
tiempos negativos, al remuxar desplaza todo hacia delante. La cadena lleva por
eso `aresample=async=1:first_pts=0` en el filtro de audio. Comprobado que **no
toca los archivos que ya empezaban en cero**: diferencia muestra a muestra
exactamente 0,00e+00 en trece de los diecisiete.

`-avoid_negative_ts make_zero` **no** sirve: empeora siete archivos que hoy
funcionan, moviéndoles el audio a 0,067. Se probó.

La excepción conocida: cuando la entrada ya es FLAC el audio se copia
(`-c:a copy`) y no pasa por el filtro. Si ese FLAC viniera desplazado, seguiría
fallando. No se ha dado el caso en el banco.

**2. `editorIncompatibleVideo` es para lo que Resolve no dibuja.** Cuatro
códecs que el navegador lee y Resolve importa **sin imagen**: `h263`, `theora`,
`flv1` (Sorenson) y `msmpeg4v3` (DivX 3). Esos sí se recodifican a H.264.
**VP8, VP9 y AV1 se copian** — son el vídeo web y el de los capturadores de
pantalla, y recodificarlos cuesta unos 0,75 s por segundo de vídeo (un WebM de
120 s en 1080p: 0,5 s copiando contra 90,5 s recodificando) sin ganar nada.

### La lección de método, que es la que más cara salió

Durante dos días el sitio afirmó que el códec de vídeo era la causa del audio
mudo, y se llegó a publicar un cambio que recodificaba VP8 y VP9. Era falso.
El error fue un **experimento de control que cambiaba dos variables a la vez**:
al recodificar el vídeo a H.264 para "aislar el códec", FFmpeg ponía además las
marcas de tiempo a cero. Sonó, y se atribuyó al códec.

Antes de dar por buena una causa, comprueba con `ffprobe` que el archivo de
control **solo** difiere en la variable que dices estar probando:

```bash
ffprobe -v error -show_entries stream=codec_type,codec_name,start_time -of csv=p=0 archivo
```

Y al cambiar estas listas hay que barrer el texto del sitio: la tabla del banco
de pruebas, las FAQ de `merged_content.py`, las guías de WebM, MKV y 3GP en
`build_pages.py` y `landing_content*.py`, y esta misma sección.

## Dos pistas de audio: el archivo está bien, lo que engaña es Resolve

Medido el 22 de septiembre de 2026 sobre Studio 21.0.4 en Ubuntu. Un MKV con
**dos pistas FLAC** dentro, verificadas con `ffprobe`, se importa a veces con
**una sola pista** en la línea de tiempo. Se generaron **trece variantes**
cambiando una propiedad cada vez —marca de pista predeterminada, nombres de
pista, 16 vs 24 bits, 44,1 vs 48 kHz, resolución, duración, etiquetas
`HANDLER_NAME`/`VENDOR_ID` heredadas de un origen MP4, MKV vs MP4— y **ninguna
explica la diferencia**: unas abrían dos y otras una.

La salida no es convertir otra vez, es **Clip Attributes**: clic derecho en el
Media Pool → `Clip Attributes…` → pestaña `Audio`. `Format` deja elegir el
número de pistas y `Source Channel` lista `Embedded Channel 1` y `2`, es decir,
los canales que el archivo trae de verdad. Hay que hacerlo **antes** de
arrastrar el clip.

Esto está publicado en la guía de OBS de los dos idiomas (sección
`#clip-attributes`) y en el banco de pruebas. Corrige de paso una afirmación que
había escrito yo: que el Inspector mostraba un selector con las pistas al
importar. No lo hace.

**La lección de método, distinta de la del experimento de control.** Cuando cada
variable queda descartada por separado pero la combinación sí cambia el
resultado, la causa no está donde estás mirando. Aquí estaba en el estado del
programa —Resolve cachea los atributos de audio de un clip la primera vez que lo
lee—, no en el archivo. Señal para parar de generar archivos y decirlo así en el
sitio, con la incertidumbre incluida, en vez de publicar una causa inventada.

## Promesas que el producto no puede sostener

El sitio arrastraba afirmaciones que no se cumplen. Al escribir texto nuevo:

- **"En segundos" sí; "instantáneo" y cifras concretas, no.** Decisión del
  usuario el 26-09-2026: prefiere "en segundos" a "instantáneamente", y los ~45
  "en segundos" del sitio se quedan (portada incluida: "Gratis, en segundos y
  100% privado"). **No los "corrijas".** Lo que sigue prohibido: "instantáneo",
  "instantly", "near-instant" y cronómetros exactos ("menos de 30 segundos").
  "Descarga al instante" sí vale, porque habla de bajar un archivo que ya está
  en el navegador, no de convertir. Dato para cuando haga falta matizar: el
  remux de un WebM de 120 s en 1080p tardó 0,5 s, pero recodificar HEVC cuesta
  ~0,75 s por segundo de vídeo, así que un vídeo de iPhone de 5 minutos tarda
  casi 4. Donde el texto hable de HEVC o de recodificar, lleva la condición al
  lado.
- **El vídeo no siempre se copia.** `browserIncompatibleVideo` en `index.html`
  recodifica a H.264 cuando el navegador no puede decodificar el códec, y esa
  lista **incluye H.265/HEVC** — el caso más frecuente hoy, porque los iPhone
  graban en HEVC desde iOS 11. Toda afirmación de "se copia bit a bit / la
  imagen es idéntica" necesita su condición al lado. Contrasta siempre el texto
  contra esa constante del código, no contra lo que diga otro artículo.
- **Xvid se copia; DivX 3 no es lo mismo que Xvid.** Xvid es MPEG-4 part 2 y se
  copia al MKV (la vista previa del navegador puede quedarse sin imagen, pero
  Resolve lo abre bien). DivX 3 es `msmpeg4v3`, y ese sí se recodifica porque
  Resolve lo importa sin imagen. Ver "El audio tiene que empezar en cero".
- **Las pistas de audio: se conservan desde el 24-09-2026, pero hay un paso.**
  Hasta esa fecha el comando no llevaba `-map` y FFmpeg elegía una; el sitio lo
  decía así. Los commits `d3ad75e`/`ebe326b` (otra sesión) añadieron la
  selección: al pulsar Convertir la app sondea el archivo y, si hay varias
  pistas, se para y enseña una casilla por pista (todas marcadas) hasta que se
  pulsa «Iniciar conversión». Probado el 25-09-2026 en la propia app, en el
  navegador, con un MKV de dos pistas AAC: dos marcadas → dos FLAC; una
  desmarcada → la marcada; salida MP4 → dos FLAC; archivo de una pista → sin
  casillas. **Todas las pistas con `start_time` 0,000**, que es lo que exige
  Resolve. Al escribir: no digas "conserva todas" sin decir que se eligen, y
  no quites la advertencia de Clip Attributes: que el archivo lleve dos pistas
  no impide que Resolve enseñe una (ver "Dos pistas de audio" más arriba).

  **Cómo se probó, por si hay que repetirlo:** la app solo sondea al pulsar
  Convertir, no al añadir el archivo. Para sacar la salida del navegador sin
  descargarla, un receptor HTTP con CORS en `127.0.0.1:8765` y un `fetch` del
  blob desde la página. Tras tres conversiones salta el aviso de anuncio: en
  `localhost` se reinicia borrando `vidtoflac_quota_v2` de `localStorage`.
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
