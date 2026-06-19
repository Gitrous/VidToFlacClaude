#!/usr/bin/env python3
"""
build_pages.py — genera páginas de aterrizaje SEO a partir de index.html.
Uso: python3 build_pages.py

Añadir una página nueva = agregar una entrada a PAGES y volver a ejecutar.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# ─────────────────────────────────────────────────────────────────────────────
# Datos de cada página
# ─────────────────────────────────────────────────────────────────────────────
PAGES = [
    {
        "slug":             "convertir-mp4-a-flac",
        "title":            "Convertir MP4 a FLAC – Audio sin pérdida para DaVinci Resolve | VidToFLAC",
        "description":      "Convierte el audio de tus archivos MP4 a FLAC sin pérdida, 100% en tu navegador con FFmpeg. Soluciona el error de códec de audio de DaVinci Resolve en MP4 de cámaras, OBS y smartphones.",
        "keywords":         "convertir MP4 a FLAC, MP4 FLAC DaVinci Resolve, MP4 sin sonido DaVinci Resolve, remux MP4 MKV FLAC, extraer audio MP4 sin pérdida, FFmpeg MP4 navegador",
        "canonical":        "https://vidtoflac.tech/convertir-mp4-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-mp4-a-flac/",
        "og_title":         "Convertir MP4 a FLAC – Audio sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus MP4 a FLAC en segundos, en tu navegador. Soluciona el error de audio de DaVinci Resolve en archivos MP4 — sin subir nada.",
        "tw_title":         "Convertir MP4 a FLAC – Audio sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus MP4 a FLAC en segundos, en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-mp4-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos MP4 a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec de audio en DaVinci Resolve, Premiere y Avid. Funciona 100% en el navegador con FFmpeg (WebAssembly), sin subir archivos.",
        "howto_name":       "Cómo convertir el audio de un MP4 a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">MP4 a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona el error de códec de audio de DaVinci Resolve en archivos MP4 de cámaras, OBS y smartphones. Procesamiento 100% local — no se sube ni un solo byte a ningún servidor.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos MP4?',
        "seo_lede":         'Si has abierto un <strong>archivo MP4</strong> en DaVinci Resolve y aparece <strong>sin sonido</strong> —o con la pista de audio en gris— casi siempre es por el códec de audio. Los MP4 grabados con cámaras, OBS Studio y smartphones llevan audio <strong>AAC o MP3</strong>, y la versión gratuita de DaVinci Resolve —especialmente <strong>en Linux</strong>— no incluye las licencias para decodificarlos.',
        "breadcrumb_label": "Convertir MP4 a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de MP4 a FLAC</h2>
      <h3>El formato MP4 y sus códecs de audio</h3>
      <p>MP4 (MPEG-4 Part 14) es el contenedor de vídeo más extendido: lo usan cámaras DSLR, smartphones (iPhone, Android), OBS Studio y prácticamente cualquier plataforma de vídeo. Su popularidad se debe a que combina vídeo H.264 o H.265 con audio en un archivo compacto. El problema está en el códec de audio: el 95 % de los archivos MP4 llevan <strong>AAC-LC</strong> (Low Complexity), el perfil estándar para dispositivos de consumo. Los MP4 de OBS pueden usar también <strong>MP3</strong> dependiendo de la configuración. En casos menos frecuentes, grabadoras de campo producen MP4 con audio <strong>PCM linear</strong>, que sí es compatible con Resolve sin conversión.</p>
      <h3>Por qué DaVinci Resolve muestra la pista de audio en gris</h3>
      <p>DaVinci Resolve gratuito —especialmente en Linux— no incluye el decodificador de AAC porque su licencia es propietaria y tiene coste por distribución. Al abrir un MP4 con AAC, el inspector de medios puede mostrar la pista de audio en gris, el clip sin forma de onda, o el mensaje <em>"Audio codec not supported (AAC)"</em>. Esta restricción afecta solo al audio: el vídeo H.264 o H.265 se abre correctamente porque sus decodificadores sí están incluidos. La solución es reemplazar el AAC por <strong>FLAC</strong>, que Resolve decodifica de forma nativa en todas las plataformas.</p>
      <h3>Paso a paso: convertir tu MP4 a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .mp4 al área de carga o pulsa <strong>Seleccionar archivos</strong>.</li>
        <li>Elige <strong>MKV</strong> como formato de salida (recomendado por su compatibilidad con Resolve) o MP4 si prefieres mantener la extensión.</li>
        <li>Pulsa <strong>Convertir</strong>. VidToFLAC detecta el códec de audio, recodifica únicamente esa pista a FLAC y copia el vídeo bit a bit sin tocarlo.</li>
        <li>Descarga el resultado e impórtalo al Media Pool de DaVinci Resolve. La pista de audio aparecerá en azul y se reproducirá sin errores.</li>
      </ol>
      <h3>Errores frecuentes y qué hacer</h3>
      <p>Si tu MP4 usa vídeo <strong>H.265 / HEVC</strong> y el proceso tarda más de lo esperado, es porque el navegador no decodifica HEVC para previsualización. VidToFLAC recodifica automáticamente el vídeo a H.264 en ese caso; el audio seguirá siendo FLAC y el archivo será compatible con Resolve. Si el archivo MP4 proviene de una cámara con múltiples pistas de audio (stereo + surround), VidToFLAC convierte todas las pistas al FLAC del contenedor de salida.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-mkv-a-flac",
        "title":            "Convertir MKV a FLAC – Remux sin pérdida para DaVinci Resolve | VidToFLAC",
        "description":      "Cambia el códec de audio de cualquier archivo MKV a FLAC sin pérdida, 100% en tu navegador. Soluciona el error de audio de DaVinci Resolve en MKV de OBS, grabaciones y cámaras.",
        "keywords":         "convertir MKV a FLAC, MKV audio FLAC, MKV DaVinci Resolve sin sonido, remux MKV FLAC, MKV FFmpeg navegador, audio MKV sin pérdida",
        "canonical":        "https://vidtoflac.tech/convertir-mkv-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-mkv-a-flac/",
        "og_title":         "Convertir MKV a FLAC – Remux sin pérdida | VidToFLAC",
        "og_desc":          "Cambia el audio de tus MKV a FLAC en segundos, en tu navegador. Soluciona el error de audio de DaVinci Resolve en archivos MKV — sin subir nada.",
        "tw_title":         "Convertir MKV a FLAC – Remux sin pérdida | VidToFLAC",
        "tw_desc":          "Cambia el audio de tus MKV a FLAC en segundos, en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-mkv-a-flac/",
        "webapp_desc":      "Cambia el códec de audio de archivos MKV a FLAC sin pérdida (remux) para solucionar el error de códec de audio en DaVinci Resolve, Premiere y Avid. Funciona 100% en el navegador con FFmpeg (WebAssembly), sin subir archivos.",
        "howto_name":       "Cómo convertir el audio de un MKV a FLAC para DaVinci Resolve",
        "hero_h1":          'Cambia el audio de tu <span class="accent">MKV a FLAC</span> sin pérdida',
        "hero_sub":         "Recodifica solo el audio de cualquier archivo MKV a FLAC, copiando el vídeo bit a bit. Soluciona el error de códec de audio en DaVinci Resolve — 100% privado, sin subir nada.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos MKV?',
        "seo_lede":         'Si has abierto un <strong>archivo MKV</strong> en DaVinci Resolve y aparece <strong>sin sonido</strong> —o con la pista de audio en gris— el problema es el códec de audio del contenedor. Los MKV de <strong>OBS Studio</strong>, grabaciones de pantalla o cámaras pueden llevar audio en <strong>AAC, Opus, MP3 o Vorbis</strong>, formatos que DaVinci Resolve —sobre todo <strong>en Linux</strong>— no puede decodificar de serie.',
        "breadcrumb_label": "Convertir MKV a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de MKV a FLAC</h2>
      <h3>El contenedor MKV: flexible pero heterogéneo</h3>
      <p>MKV (Matroska Video) es un contenedor de código abierto especialmente popular en la comunidad de grabación y edición: OBS Studio lo usa como formato de grabación por defecto, y muchas herramientas de descarga y transcodificación como FFmpeg o HandBrake lo producen habitualmente. Su característica más importante —y también la más problemática— es que acepta <em>cualquier</em> códec de audio: <strong>AAC, MP3, Vorbis, Opus, DTS, AC3, FLAC, PCM</strong> y muchos más. No hay forma de saber qué códec lleva un MKV sin analizarlo, y esa variedad es exactamente lo que genera problemas de compatibilidad con DaVinci Resolve.</p>
      <h3>Qué códec de audio lleva tu MKV</h3>
      <p>El origen del archivo determina el códec: los MKV de <strong>OBS Studio</strong> suelen tener <strong>AAC o Opus</strong> (según la versión y la configuración). Los descargados con yt-dlp o similar desde YouTube pueden traer <strong>Vorbis u Opus</strong>. Los generados por HandBrake con la configuración por defecto suelen tener <strong>AAC</strong>. Los producidos por conversores online pueden traer <strong>MP3</strong>. Solo los MKV con audio FLAC o PCM linear son directamente compatibles con DaVinci Resolve en todas las plataformas.</p>
      <h3>Por qué la pista de audio de tu MKV aparece en gris en DaVinci Resolve</h3>
      <p>DaVinci Resolve gratuito no incluye decodificadores para AAC, MP3, Vorbis, Opus, DTS ni AC3. En Linux, Resolve depende del sistema operativo para estos códecs y muchas distribuciones no los incluyen por razones de licencia. El resultado es la pista de audio en gris y sin forma de onda. Cambiar el códec a FLAC soluciona el problema porque FLAC es un estándar abierto que Resolve incluye de serie en todas sus versiones.</p>
      <h3>Paso a paso: cambiar el audio de tu MKV a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .mkv a VidToFLAC. La herramienta detecta automáticamente el códec de audio actual.</li>
        <li>Selecciona <strong>MKV</strong> como formato de salida para mantener el mismo contenedor.</li>
        <li>Pulsa <strong>Convertir</strong>. El vídeo se copia sin recodificar; solo el audio cambia a FLAC.</li>
        <li>Importa el nuevo MKV en DaVinci Resolve. La pista de audio aparecerá en azul y podrás editarla sin ningún problema.</li>
      </ol>
      <h3>Caso especial: MKV con audio Opus de OBS</h3>
      <p>OBS Studio 28 y posteriores usan Opus como códec de audio por defecto en grabaciones MKV porque ofrece mejor calidad que MP3 a menor bitrate. Resolve no decodifica Opus de serie en ninguna plataforma, así que si grabas con OBS en esas versiones y ves la pista de audio en gris, la conversión a FLAC con VidToFLAC resuelve el problema de forma inmediata.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-mov-a-flac",
        "title":            "Convertir MOV a FLAC – Audio de iPhone y GoPro para DaVinci Resolve | VidToFLAC",
        "description":      "Convierte el audio de tus archivos MOV de iPhone, GoPro o cámara a FLAC sin pérdida, en tu navegador. Soluciona el error de códec de audio de DaVinci Resolve en clips MOV.",
        "keywords":         "convertir MOV a FLAC, MOV FLAC DaVinci Resolve, MOV iPhone DaVinci Resolve sin sonido, convertir vídeo iPhone a FLAC, GoPro MOV audio FLAC, remux MOV MKV FLAC",
        "canonical":        "https://vidtoflac.tech/convertir-mov-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-mov-a-flac/",
        "og_title":         "Convertir MOV a FLAC – Audio iPhone y GoPro | VidToFLAC",
        "og_desc":          "Convierte el audio de tus clips MOV (iPhone, GoPro, cámara) a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "tw_title":         "Convertir MOV a FLAC – Audio iPhone y GoPro | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus clips MOV a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-mov-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos MOV (iPhone, GoPro, cámara) a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec de audio en DaVinci Resolve, Premiere y Avid. Funciona 100% en el navegador con FFmpeg (WebAssembly), sin subir archivos.",
        "howto_name":       "Cómo convertir el audio de un MOV a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">MOV a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona los clips MOV de iPhone, GoPro o cámara que DaVinci Resolve no puede reproducir. Audio a FLAC sin pérdida, vídeo copiado bit a bit — 100% privado, en tu navegador.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos MOV?',
        "seo_lede":         'Si has abierto un <strong>archivo MOV</strong> en DaVinci Resolve y aparece <strong>sin sonido</strong> —o con la pista de audio en gris— el problema suele ser el códec de audio. Los MOV grabados con <strong>iPhone, GoPro</strong> o la mayoría de cámaras digitales usan <strong>AAC</strong>, y DaVinci Resolve —especialmente <strong>en Linux</strong>— no incluye de serie las licencias para decodificarlo.',
        "breadcrumb_label": "Convertir MOV a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de MOV a FLAC</h2>
      <h3>El formato MOV: nativo de Apple, problemático fuera de macOS</h3>
      <p>MOV es el formato de contenedor de QuickTime, desarrollado por Apple. Es el formato nativo de grabación del <strong>iPhone</strong> (todos los modelos), <strong>GoPro</strong> (antes de cambiar a MP4), cámaras Sony Alpha en modo XAVC S, Canon EOS en algunos modos y muchas otras cámaras digitales orientadas a la producción. En macOS, los archivos MOV se abren sin problemas en casi cualquier aplicación porque el sistema incluye los decodificadores necesarios. En <strong>Linux</strong> —donde reside la mayor parte de los usuarios afectados por el problema de audio en DaVinci Resolve— la historia es diferente.</p>
      <h3>Códecs de audio en archivos MOV</h3>
      <p>Los MOV de iPhone y GoPro usan casi siempre <strong>AAC estéreo</strong> a 44.1 kHz o 48 kHz. Los MOV de cámaras Sony Alpha con grabación de alta calidad pueden usar <strong>PCM linear de 4 canales</strong>. Las cámaras Canon con modo Cinema RAW Light generan MOV con <strong>PCM linear</strong>. Los MOV de grabación en pantalla de macOS (QuickTime Player) suelen tener <strong>AAC</strong>. El denominador común de los problemas en Resolve es el AAC: solo el PCM linear es directamente compatible.</p>
      <h3>El caso especial de los MOV con ProRes</h3>
      <p>Las cámaras de cine como la BlackMagic Pocket Cinema Camera, la Apple ProRes RAW y los flujos de trabajo de postproducción en macOS generan MOV con vídeo <strong>ProRes</strong>. DaVinci Resolve sí decodifica ProRes en macOS y Windows Studio, pero en Linux y en la versión gratuita para Windows el soporte es limitado. Si tu MOV tiene ProRes, VidToFLAC detecta automáticamente el códec y recodifica el vídeo a H.264 para garantizar la previsualización en el navegador y la compatibilidad básica con Resolve.</p>
      <h3>Paso a paso: convertir tu MOV a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .mov a VidToFLAC. La herramienta analiza los códecs de audio y vídeo.</li>
        <li>Selecciona <strong>MKV</strong> como formato de salida. Los MOV de iPhone y GoPro se procesan en segundos.</li>
        <li>Pulsa <strong>Convertir</strong>. Si el vídeo es H.264 o H.265, se copia bit a bit. Si es ProRes, se recodifica a H.264 automáticamente. El audio pasa siempre a FLAC.</li>
        <li>Importa el MKV resultante en DaVinci Resolve y asígnalo a tu timeline.</li>
      </ol>
      <h3>Tip: iPhone graba en HEVC por defecto desde iOS 11</h3>
      <p>Desde iOS 11, el iPhone graba vídeo en <strong>H.265 (HEVC)</strong> con audio AAC dentro de un contenedor MOV. Resolve en Linux no siempre decodifica HEVC de forma nativa. VidToFLAC gestiona ambos casos automáticamente: si el navegador puede decodificar el HEVC, copia el vídeo bit a bit; si no, lo recodifica a H.264 con calidad alta. En ambos casos el audio FLAC del resultado es compatible con Resolve.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-aac-a-flac",
        "title":            "Convertir AAC a FLAC – Audio sin pérdida en el navegador | VidToFLAC",
        "description":      "Convierte archivos AAC a FLAC sin pérdida, 100% en tu navegador con FFmpeg. Sin subir archivos, sin límite de tamaño. Ideal para recuperar audio de vídeos que DaVinci Resolve no reproduce.",
        "keywords":         "convertir AAC a FLAC, AAC a FLAC sin pérdida, AAC FLAC navegador, convertir audio AAC, AAC DaVinci Resolve, FFmpeg AAC FLAC online",
        "canonical":        "https://vidtoflac.tech/convertir-aac-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-aac-a-flac/",
        "og_title":         "Convertir AAC a FLAC – Audio sin pérdida | VidToFLAC",
        "og_desc":          "Convierte tus archivos AAC a FLAC sin pérdida en segundos, directo en el navegador. Sin subir nada, sin registro.",
        "tw_title":         "Convertir AAC a FLAC – Audio sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte tus archivos AAC a FLAC sin pérdida en segundos, directo en el navegador. Sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-aac-a-flac/",
        "webapp_desc":      "Convierte archivos de audio AAC a FLAC sin pérdida, 100% en el navegador con FFmpeg (WebAssembly). También reempaqueta vídeos con audio AAC en MKV+FLAC para solucionar el error de códec en DaVinci Resolve. Sin subir archivos.",
        "howto_name":       "Cómo convertir un archivo AAC a FLAC sin pérdida",
        "hero_h1":          'Convierte tu <span class="accent">AAC a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Transcodifica archivos AAC a FLAC lossless en segundos, directamente en tu navegador. Sin registro, sin límite de tamaño, sin que ningún byte salga de tu equipo.",
        "seo_h2":           '¿Por qué convertir <span class="accent">AAC a FLAC</span> en lugar de quedarte con el AAC?',
        "seo_lede":         '<strong>AAC</strong> es un formato con pérdida: cada vez que lo recodificas vuelves a perder calidad. <strong>FLAC</strong> es sin pérdida: una vez convertido, puedes exportar, editar o archivar sin degradar el audio. Además, DaVinci Resolve —especialmente <strong>en Linux</strong>— no decodifica AAC de serie, por lo que convertir a FLAC soluciona de raíz el <strong>error de códec de audio</strong>.',
        "breadcrumb_label": "Convertir AAC a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de AAC a FLAC</h2>
      <h3>¿Qué es AAC y por qué está en todas partes?</h3>
      <p>AAC (Advanced Audio Coding) es el códec de audio con pérdida que sucedió al MP3 como estándar de la industria. Lo adoptaron Apple (iPhone, iTunes, Apple Music), YouTube (como códec de audio en muchos streams), las grabaciones de voz de WhatsApp, los vídeos de cámaras digitales y la mayoría de aplicaciones de grabación en iOS y Android. AAC ofrece mejor calidad que MP3 al mismo bitrate, pero sigue siendo un formato <strong>con pérdida</strong>: elimina información de frecuencias que el algoritmo considera prescindible. Eso significa que cada vez que recodificas un AAC a otro formato con pérdida, la calidad se degrada un poco más.</p>
      <h3>Por qué no deberías quedarte con el AAC para edición</h3>
      <p>En un flujo de trabajo de edición profesional, el audio pasa por múltiples etapas: importación, edición en el timeline, mezcla, exportación. Si el audio de partida es AAC, cada operación de recodificación acumula artefactos. Además, DaVinci Resolve gratuito —en especial <strong>en Linux</strong>— no incluye el decodificador de AAC, por lo que no podrás ni abrirlo. Convertir a <strong>FLAC</strong> en este paso garantiza que trabajas con audio sin pérdida desde el principio, evitando degradaciones acumulativas y asegurando la compatibilidad con el editor.</p>
      <h3>Diferencias técnicas entre AAC y FLAC</h3>
      <p>AAC usa compresión <em>destructiva</em> basada en modelos perceptuales del oído humano: elimina información que el algoritmo considera inaudible para reducir el tamaño. FLAC usa compresión <em>lossless</em> basada en predicción lineal: codifica la diferencia entre la señal real y la predicha, de modo que la decodificación restaura exactamente la señal original. Un archivo AAC de 3 minutos a 128 kbps pesa unos 2,9 MB; el mismo audio en FLAC a 16 bit / 44.1 kHz pesaría unos 20 MB, pero con calidad idéntica al original sin comprimir.</p>
      <h3>Paso a paso: convertir tu AAC a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .aac (o .m4a con audio AAC) a VidToFLAC.</li>
        <li>La herramienta detecta automáticamente que es un archivo de audio sin pista de vídeo.</li>
        <li>Pulsa <strong>Convertir</strong>. El resultado es un archivo <strong>.flac</strong> con la misma duración y el mismo contenido de audio, en formato lossless.</li>
        <li>Importa el .flac en DaVinci Resolve, Premiere Pro o el editor que uses. La pista de audio debería importarse correctamente sin errores de códec.</li>
      </ol>
      <h3>¿Convierte el AAC a FLAC sin pérdida?</h3>
      <p>Técnicamente, la conversión de AAC a FLAC es sin pérdida en el sentido de que FLAC no añade más degradación. Sin embargo, la calidad ya reducida por el AAC original no se recupera: FLAC solo preserva lo que hay. Si tu AAC fue grabado a 128 kbps, el FLAC resultante tendrá esa misma calidad, simplemente sin pérdidas adicionales. Por eso lo más valioso es convertir a FLAC antes de cualquier edición, no después de múltiples exportaciones.</p>
    </article>
  </section>""",
    },
    # ── Audio-only formats ────────────────────────────────────────────────────
    {
        "slug":             "convertir-mp3-a-flac",
        "title":            "Convertir MP3 a FLAC – Audio lossless en el navegador | VidToFLAC",
        "description":      "Convierte archivos MP3 a FLAC sin pérdida, 100% en tu navegador con FFmpeg. Sin subir archivos, sin registro. Ideal para flujos de trabajo de edición de audio y DaVinci Resolve.",
        "keywords":         "convertir MP3 a FLAC, MP3 a FLAC sin pérdida, MP3 FLAC online, convertir audio MP3 lossless, FFmpeg MP3 FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-mp3-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-mp3-a-flac/",
        "og_title":         "Convertir MP3 a FLAC – Audio lossless | VidToFLAC",
        "og_desc":          "Convierte tus archivos MP3 a FLAC en segundos, directo en el navegador. Sin subir nada, sin registro.",
        "tw_title":         "Convertir MP3 a FLAC – Audio lossless | VidToFLAC",
        "tw_desc":          "Convierte tus archivos MP3 a FLAC en segundos, directo en el navegador. Sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-mp3-a-flac/",
        "webapp_desc":      "Convierte archivos de audio MP3 a FLAC lossless, 100% en el navegador con FFmpeg (WebAssembly). Sin subir archivos, sin límite de tamaño.",
        "howto_name":       "Cómo convertir un archivo MP3 a FLAC sin pérdida",
        "hero_h1":          'Convierte tu <span class="accent">MP3 a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Transcodifica archivos MP3 a FLAC lossless en segundos, directamente en tu navegador. Sin registro, sin límite de tamaño, sin que ningún byte salga de tu equipo.",
        "seo_h2":           '¿Por qué convertir <span class="accent">MP3 a FLAC</span> para tu flujo de trabajo?',
        "seo_lede":         '<strong>MP3</strong> es un formato con pérdida que no es compatible de forma nativa con todos los editores de vídeo profesionales. Convertir a <strong>FLAC</strong> —un formato sin pérdida— garantiza la máxima compatibilidad con DaVinci Resolve, Premiere Pro y Avid, especialmente <strong>en Linux</strong>, donde los decodificadores de MP3 pueden no estar disponibles sin licencias adicionales.',
        "breadcrumb_label": "Convertir MP3 a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de MP3 a FLAC</h2>
      <h3>MP3: el formato más popular y sus limitaciones</h3>
      <p>MP3 (MPEG Audio Layer III) lleva más de 30 años siendo el formato de audio más extendido del mundo. Se popularizó en los años 90 con los primeros reproductores portátiles y sigue siendo el formato por defecto en muchas grabadoras de voz, podcasts, música descargada y archivos de audio de uso general. Sin embargo, MP3 es un formato <strong>con pérdida</strong>: aplica un modelo psicoacústico para eliminar frecuencias "imperceptibles" y reducir el tamaño del archivo. La calidad perdida en ese proceso no se puede recuperar.</p>
      <h3>Problemas de MP3 en flujos de trabajo de edición</h3>
      <p>Además de la degradación inherente al formato, los archivos MP3 presentan dos problemas específicos en edición de vídeo. Primero, <strong>DaVinci Resolve en Linux</strong> no incluye el decodificador de MP3 de serie, lo que provoca que los archivos MP3 no se importen o que la pista de audio aparezca en gris. Segundo, el MP3 tiene una limitación de latencia de codificación (encoder delay) que puede provocar una pequeña desincronización de audio al principio de los clips, un problema bien conocido en flujos de trabajo de edición multicámara. FLAC no tiene este problema.</p>
      <h3>Qué ocurre al convertir MP3 a FLAC</h3>
      <p>La conversión de MP3 a FLAC es una transcodificación de lossy a lossless. El resultado es un archivo FLAC que contiene exactamente el audio que había en el MP3, sin añadir ni quitar información. La calidad no mejora respecto al MP3 original (lo que se perdió en la compresión MP3 no se puede recuperar), pero el archivo resultante es lossless en el sentido de que no hay degradación adicional, y es compatible con todos los editores de vídeo sin problemas de licencia.</p>
      <h3>Paso a paso: convertir tu MP3 a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .mp3 a VidToFLAC. La herramienta detecta que es un archivo de audio sin pista de vídeo.</li>
        <li>Pulsa <strong>Convertir</strong>. Se produce la transcodificación de MP3 a FLAC dentro del navegador con FFmpeg.</li>
        <li>Descarga el archivo .flac resultante.</li>
        <li>Importa el .flac en DaVinci Resolve, Adobe Premiere o Audacity. No habrá problemas de códec ni de latencia de codificación.</li>
      </ol>
      <h3>¿Cuándo tiene sentido convertir MP3 a FLAC?</h3>
      <p>Tiene sentido cuando necesitas importar audio MP3 en un editor que no lo soporta nativamente (especialmente DaVinci Resolve en Linux), cuando quieres evitar la desincronización por encoder delay en proyectos multicámara, o cuando necesitas aplicar efectos de audio y luego exportar sin degradación adicional. No tiene sentido si tu objetivo final es MP3 de nuevo: convertir MP3 → FLAC → MP3 añade una generación extra de pérdida.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-wav-a-flac",
        "title":            "Convertir WAV a FLAC – Compresión lossless en el navegador | VidToFLAC",
        "description":      "Convierte archivos WAV a FLAC sin pérdida, reduciendo el tamaño hasta un 60% sin perder calidad. 100% en tu navegador con FFmpeg. Sin subir archivos.",
        "keywords":         "convertir WAV a FLAC, WAV a FLAC sin pérdida, comprimir WAV a FLAC, WAV FLAC online, FFmpeg WAV FLAC navegador, reducir tamaño WAV",
        "canonical":        "https://vidtoflac.tech/convertir-wav-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-wav-a-flac/",
        "og_title":         "Convertir WAV a FLAC – Compresión lossless | VidToFLAC",
        "og_desc":          "Convierte WAV a FLAC en segundos: misma calidad, hasta un 60% menos de espacio. Directo en el navegador, sin subir nada.",
        "tw_title":         "Convertir WAV a FLAC – Compresión lossless | VidToFLAC",
        "tw_desc":          "Convierte WAV a FLAC en segundos: misma calidad, hasta un 60% menos de espacio. Sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-wav-a-flac/",
        "webapp_desc":      "Convierte archivos WAV a FLAC sin pérdida de calidad, reduciendo el tamaño del archivo hasta un 60%. Funciona 100% en el navegador con FFmpeg (WebAssembly), sin subir archivos.",
        "howto_name":       "Cómo convertir un archivo WAV a FLAC sin pérdida de calidad",
        "hero_h1":          'Convierte tu <span class="accent">WAV a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Misma calidad lossless que el WAV original, hasta un 60% menos de espacio. Conversión en segundos, directamente en tu navegador — sin subir ni un solo byte.",
        "seo_h2":           '¿Por qué convertir <span class="accent">WAV a FLAC</span> en lugar de guardar el WAV?',
        "seo_lede":         '<strong>WAV</strong> y <strong>FLAC</strong> son ambos formatos sin pérdida, pero el WAV no comprime los datos: un archivo de 10 minutos puede pesar más de 100 MB. FLAC aplica compresión lossless y reduce el tamaño entre un 40% y un 60% <strong>sin perder ni un bit de información</strong>. El resultado suena idéntico al WAV original y ocupa mucho menos.',
        "breadcrumb_label": "Convertir WAV a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de WAV a FLAC</h2>
      <h3>WAV vs. FLAC: dos formatos lossless con diferencias importantes</h3>
      <p>WAV (Waveform Audio File Format) fue desarrollado por Microsoft e IBM en 1991 y sigue siendo el formato estándar en estudios de grabación, broadcast y producción musical profesional. Almacena el audio como <strong>PCM sin comprimir</strong>, lo que garantiza la máxima compatibilidad con cualquier software de audio pero genera archivos enormes. FLAC surgió en 2001 como alternativa sin pérdida que añade una capa de compresión reversible sobre el PCM. Ambos formatos preservan el audio al 100 %, pero el tamaño puede diferir enormemente: un WAV de 24 bit / 96 kHz puede pesar 1 GB por cada 30 minutos, mientras que el FLAC equivalente ocupa entre 400 y 600 MB.</p>
      <h3>Cuándo tiene sentido convertir WAV a FLAC</h3>
      <p>La conversión WAV → FLAC es especialmente útil en tres escenarios: cuando trabajas con archivos de audio de larga duración (entrevistas, grabaciones en directo, música) y el espacio en disco es limitado; cuando necesitas archivar audio lossless con metadatos (artista, álbum, pista) que el formato WAV no soporta nativamente; y cuando usas plataformas o repositorios que requieren FLAC en lugar de WAV. La conversión es reversible: puedes recuperar el WAV original bit a bit a partir del FLAC en cualquier momento.</p>
      <h3>Profundidades de bits y tasas de muestreo compatibles</h3>
      <p>FLAC soporta las profundidades de bit más comunes en audio profesional: <strong>16 bit</strong> (CD audio), <strong>24 bit</strong> (grabación de estudio) y <strong>32 bit entero</strong>. Soporta también tasas de muestreo desde 1 Hz hasta 655.350 Hz, cubriendo los estándares de producción: 44.1 kHz, 48 kHz, 88.2 kHz, 96 kHz y 192 kHz. Un caso especial es el audio <strong>PCM de 32 bits en coma flotante</strong> (pcm_f32le), que generan algunos micrófonos USB y DAW: FLAC no puede codificarlo directamente porque requiere muestras enteras. VidToFLAC detecta este caso e inserta automáticamente un paso de conversión a 32 bit entero antes de codificar a FLAC, sin pérdida de calidad audible.</p>
      <h3>Paso a paso: convertir tu WAV a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .wav a VidToFLAC.</li>
        <li>La herramienta detecta la profundidad de bit y la tasa de muestreo del WAV.</li>
        <li>Pulsa <strong>Convertir</strong>. La codificación FLAC es rápida; un archivo WAV de 100 MB tarda habitualmente menos de 10 segundos.</li>
        <li>Descarga el .flac resultante. Puedes verificar que la calidad es idéntica importando ambos archivos en un editor de audio y comparándolos con inversión de fase: el resultado debería ser silencio completo.</li>
      </ol>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-m4a-a-flac",
        "title":            "Convertir M4A a FLAC – Audio de iPhone y iTunes sin pérdida | VidToFLAC",
        "description":      "Convierte archivos M4A (Apple, iPhone, iTunes) a FLAC sin pérdida, 100% en tu navegador. Soluciona la compatibilidad con DaVinci Resolve, Premiere y editores en Linux.",
        "keywords":         "convertir M4A a FLAC, M4A FLAC DaVinci Resolve, M4A iPhone FLAC, convertir audio M4A sin pérdida, FFmpeg M4A FLAC online, iTunes FLAC",
        "canonical":        "https://vidtoflac.tech/convertir-m4a-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-m4a-a-flac/",
        "og_title":         "Convertir M4A a FLAC – Audio iPhone y iTunes | VidToFLAC",
        "og_desc":          "Convierte tus archivos M4A de iPhone o iTunes a FLAC en tu navegador. Compatibilidad total con DaVinci Resolve — sin subir nada.",
        "tw_title":         "Convertir M4A a FLAC – Audio iPhone y iTunes | VidToFLAC",
        "tw_desc":          "Convierte tus archivos M4A a FLAC en tu navegador. Compatibilidad total con DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-m4a-a-flac/",
        "webapp_desc":      "Convierte archivos M4A (iPhone, iTunes, grabaciones de voz Apple) a FLAC sin pérdida, 100% en el navegador con FFmpeg (WebAssembly). Soluciona problemas de compatibilidad con DaVinci Resolve en Linux.",
        "howto_name":       "Cómo convertir un archivo M4A a FLAC sin pérdida",
        "hero_h1":          'Convierte tu <span class="accent">M4A a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Transcodifica archivos M4A de iPhone, iTunes o grabaciones de voz Apple a FLAC lossless. Compatibilidad total con DaVinci Resolve y Premiere — 100% privado, en tu navegador.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no reproduce</span> tus archivos M4A?',
        "seo_lede":         'Los archivos <strong>M4A</strong> de iPhone, grabaciones de voz de Apple o exportaciones de iTunes usan el códec <strong>AAC</strong> envuelto en un contenedor MPEG-4. DaVinci Resolve —sobre todo <strong>en Linux</strong>— no incluye el decodificador de AAC de serie, lo que provoca pistas de audio en gris o un <strong>error de códec de audio</strong> al importar.',
        "breadcrumb_label": "Convertir M4A a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de M4A a FLAC</h2>
      <h3>¿Qué es M4A y en qué se diferencia de AAC?</h3>
      <p>M4A es una extensión de archivo que Apple introdujo para diferenciar los archivos MPEG-4 que contienen <em>solo audio</em> (sin pista de vídeo) de los MP4 que contienen vídeo. Técnicamente, un .m4a y un .mp4 son el mismo contenedor MPEG-4; la diferencia es que en M4A la pista de audio va sola. El códec de audio dentro es casi siempre <strong>AAC</strong>, aunque algunos archivos M4A de alta calidad (como las exportaciones de iTunes Plus o Apple Music en calidad lossless) pueden contener <strong>ALAC</strong> (Apple Lossless Audio Codec).</p>
      <h3>Orígenes habituales de archivos M4A</h3>
      <p>Los archivos M4A provienen principalmente de: <strong>Notas de Voz de iPhone</strong> (grabaciones de voz y entrevistas), <strong>iTunes y Apple Music</strong> (compras de música en el ecosistema Apple), <strong>GarageBand y Logic Pro</strong> (exportaciones de proyectos de audio en Mac), y <strong>grabadoras de voz con micrófono Apple</strong>. Si el M4A contiene ALAC (lossless de Apple), la conversión a FLAC es una transcodificación lossless-a-lossless: la calidad se preserva al 100 %.</p>
      <h3>Por qué DaVinci Resolve no abre archivos M4A con audio AAC</h3>
      <p>El contenedor MPEG-4 (.m4a) no es el problema: Resolve lo reconoce. El problema es el códec de audio AAC dentro. En Linux, Resolve gratuito no incluye el decodificador de AAC. Si intentas importar un archivo M4A en Resolve en Linux, verás que la forma de onda de audio no aparece o que el clip no se importa con sonido. La solución es convertir el M4A a FLAC, que Resolve sí decodifica de serie.</p>
      <h3>Paso a paso: convertir tu M4A a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .m4a a VidToFLAC. La herramienta detecta que es audio-only.</li>
        <li>Pulsa <strong>Convertir</strong>. Si el audio es AAC, se transcodifica a FLAC. Si el audio es ALAC, la conversión de lossless a lossless preserva la calidad exacta.</li>
        <li>Descarga el archivo .flac e impórtalo en tu editor. No habrá errores de códec en DaVinci Resolve, Premiere Pro ni Avid.</li>
      </ol>
      <h3>Tip: grabaciones de entrevistas en iPhone</h3>
      <p>Las Notas de Voz del iPhone crean archivos M4A con audio AAC mono a 44.1 kHz. Si grabas entrevistas con el iPhone para luego montarlas en DaVinci Resolve en Linux, convierte los M4A a FLAC antes de importarlos al proyecto. La calidad de voz se preserva completamente y el flujo de trabajo de edición no tiene interrupciones.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-ogg-a-flac",
        "title":            "Convertir OGG a FLAC – Audio Vorbis sin pérdida en el navegador | VidToFLAC",
        "description":      "Convierte archivos OGG (Vorbis) a FLAC sin pérdida, 100% en tu navegador con FFmpeg. Compatibilidad total con editores de vídeo profesionales. Sin subir archivos.",
        "keywords":         "convertir OGG a FLAC, OGG Vorbis FLAC, OGG FLAC sin pérdida, convertir audio OGG online, FFmpeg OGG FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-ogg-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-ogg-a-flac/",
        "og_title":         "Convertir OGG a FLAC – Audio Vorbis sin pérdida | VidToFLAC",
        "og_desc":          "Convierte tus archivos OGG a FLAC en segundos, en tu navegador. Sin subir nada, sin registro.",
        "tw_title":         "Convertir OGG a FLAC – Audio Vorbis sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte tus archivos OGG a FLAC en segundos, en tu navegador. Sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-ogg-a-flac/",
        "webapp_desc":      "Convierte archivos OGG (Vorbis) a FLAC sin pérdida, 100% en el navegador con FFmpeg (WebAssembly). Sin subir archivos, sin límite de tamaño.",
        "howto_name":       "Cómo convertir un archivo OGG a FLAC sin pérdida",
        "hero_h1":          'Convierte tu <span class="accent">OGG a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Transcodifica archivos OGG Vorbis a FLAC lossless directamente en tu navegador. Máxima compatibilidad con editores de vídeo profesionales — sin subir ni un solo byte.",
        "seo_h2":           '¿Por qué convertir <span class="accent">OGG a FLAC</span> para edición profesional?',
        "seo_lede":         '<strong>OGG Vorbis</strong> es un formato con pérdida de código abierto: ofrece buena calidad a tamaños reducidos, pero no es compatible de forma nativa con la mayoría de editores de vídeo profesionales como DaVinci Resolve, Premiere Pro o Avid. Convertir a <strong>FLAC</strong> resuelve el problema de compatibilidad y garantiza que el audio se importe sin errores.',
        "breadcrumb_label": "Convertir OGG a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de OGG a FLAC</h2>
      <h3>¿Qué es OGG y cuándo lo encuentras?</h3>
      <p>OGG es un formato contenedor de código abierto desarrollado por la Fundación Xiph.Org. El archivo .ogg contiene habitualmente audio con el códec <strong>Vorbis</strong>, aunque también puede contener FLAC u Opus. OGG Vorbis fue diseñado como alternativa libre a MP3 y AAC: ofrece calidad comparable a bitrates más bajos y sin restricciones de patentes. Lo encontrarás en: efectos de sonido de videojuegos (muchos motores como Godot o Unity exportan audio en OGG), música distribuida en plataformas de código abierto, archivos de audio de algunas distribuciones Linux, y exportaciones de software de código abierto como Audacity en ciertas configuraciones.</p>
      <h3>Vorbis vs. FLAC: con pérdida vs. sin pérdida</h3>
      <p>Vorbis —el códec más común dentro de OGG— es un formato con pérdida, comparable en calidad a AAC o MP3 de similar bitrate. FLAC, en cambio, es sin pérdida. La diferencia es crucial para edición de audio profesional: al editar con audio con pérdida y exportar de nuevo, se acumulan artefactos de compresión. Con FLAC, el audio que editas y exportas es matemáticamente idéntico al original en cada generación.</p>
      <h3>Por qué OGG Vorbis no funciona en los principales editores de vídeo</h3>
      <p>DaVinci Resolve, Adobe Premiere Pro y Avid Media Composer están diseñados para flujos de trabajo de producción profesional y no incluyen soporte nativo para Vorbis ni para el contenedor OGG. La razón histórica es que el mercado profesional de vídeo se desarrolló sobre codecs propietarios (AAC, AC3, DTS, PCM) mucho antes de que los formatos de código abierto como Vorbis madurecen. Importar un .ogg en Resolve suele resultar en un error de importación o en que el clip aparece sin pista de audio.</p>
      <h3>Paso a paso: convertir tu OGG a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .ogg a VidToFLAC.</li>
        <li>La herramienta identifica el códec interno (Vorbis u Opus) y lo transcodifica a FLAC.</li>
        <li>Pulsa <strong>Convertir</strong> y descarga el .flac resultante.</li>
        <li>Importa el .flac en DaVinci Resolve o tu editor preferido. La compatibilidad será total.</li>
      </ol>
      <h3>Nota sobre OGG FLAC vs. archivos .flac</h3>
      <p>Existe una variante llamada <em>OGG FLAC</em> que encapsula el códec FLAC dentro del contenedor OGG. Aunque el audio es sin pérdida, algunos editores no reconocen la extensión .ogg con FLAC dentro. VidToFLAC detecta este caso y produce un archivo .flac estándar, que tiene mayor compatibilidad universal.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-wma-a-flac",
        "title":            "Convertir WMA a FLAC – Audio de Windows sin pérdida | VidToFLAC",
        "description":      "Convierte archivos WMA (Windows Media Audio) a FLAC sin pérdida, 100% en tu navegador. Soluciona la compatibilidad con DaVinci Resolve y editores profesionales en Mac y Linux.",
        "keywords":         "convertir WMA a FLAC, WMA FLAC sin pérdida, WMA Windows Media Audio FLAC, convertir audio WMA online, FFmpeg WMA FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-wma-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-wma-a-flac/",
        "og_title":         "Convertir WMA a FLAC – Audio Windows sin pérdida | VidToFLAC",
        "og_desc":          "Convierte tus archivos WMA a FLAC en tu navegador. Compatibilidad total con DaVinci Resolve y editores profesionales — sin subir nada.",
        "tw_title":         "Convertir WMA a FLAC – Audio Windows sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte tus archivos WMA a FLAC en tu navegador. Compatibilidad total con editores profesionales — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-wma-a-flac/",
        "webapp_desc":      "Convierte archivos WMA (Windows Media Audio) a FLAC sin pérdida, 100% en el navegador con FFmpeg (WebAssembly). Soluciona problemas de compatibilidad con DaVinci Resolve, Premiere Pro y Avid.",
        "howto_name":       "Cómo convertir un archivo WMA a FLAC sin pérdida",
        "hero_h1":          'Convierte tu <span class="accent">WMA a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Transcodifica archivos WMA de Windows a FLAC lossless en tu navegador. Compatibilidad total con DaVinci Resolve, Premiere y Avid — 100% privado, sin subir nada.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no abre</span> tus archivos WMA?',
        "seo_lede":         '<strong>WMA (Windows Media Audio)</strong> es un formato propietario de Microsoft que no forma parte del estándar de codecs incluidos en DaVinci Resolve —especialmente <strong>en Linux y macOS</strong>—, lo que provoca que las pistas de audio aparezcan en gris o directamente no se importen. Convertir a <strong>FLAC</strong> resuelve el problema de compatibilidad al instante.',
        "breadcrumb_label": "Convertir WMA a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de WMA a FLAC</h2>
      <h3>¿Qué es WMA y por qué todavía existe?</h3>
      <p>WMA (Windows Media Audio) es el formato de audio propietario de Microsoft, introducido en 1999 como competidor de MP3. Existen varias variantes: <strong>WMA Standard</strong> (con pérdida, equivalente a MP3), <strong>WMA Pro</strong> (con pérdida, mayor calidad y soporte multicanal), y <strong>WMA Lossless</strong> (sin pérdida, equivalente a FLAC). Los archivos WMA son comunes en archivos descargados de Zune (la tienda de música de Microsoft, ya cerrada), grabaciones de Windows Media Player, y algunos archivos de audio de aplicaciones corporativas basadas en tecnología Microsoft.</p>
      <h3>Por qué WMA no funciona en DaVinci Resolve, especialmente en Linux</h3>
      <p>WMA es un formato propietario de Microsoft protegido por patentes. DaVinci Resolve no incluye los decodificadores de WMA en ninguna plataforma excepto Windows, donde puede depender de los códecs del sistema operativo. En <strong>Linux</strong> y en algunos entornos de <strong>macOS</strong>, Resolve no puede decodificar WMA en ninguna de sus variantes. Si intentas importar un .wma en Resolve en Linux, el archivo puede no aparecer en el Media Pool o la pista de audio aparece completamente vacía.</p>
      <h3>WMA Lossless a FLAC: la conversión ideal</h3>
      <p>Si tu archivo WMA es <strong>WMA Lossless</strong>, la conversión a FLAC es lossless-a-lossless: preserva el audio exactamente como estaba. Ambos formatos son sin pérdida; la diferencia es la compatibilidad y el ecosistema. FLAC es un estándar abierto soportado en todos los sistemas operativos y editores de vídeo, mientras que WMA Lossless requiere software con licencia Microsoft. Si tu WMA es estándar (con pérdida), la conversión a FLAC produce un archivo lossless que preserva la calidad del WMA sin pérdidas adicionales.</p>
      <h3>Paso a paso: convertir tu WMA a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .wma a VidToFLAC.</li>
        <li>La herramienta detecta la variante WMA (Standard, Pro o Lossless) y aplica el proceso adecuado.</li>
        <li>Pulsa <strong>Convertir</strong>. El resultado es un archivo .flac compatible con todos los editores.</li>
        <li>Importa el .flac en DaVinci Resolve, Premiere o Audacity sin problemas de códec.</li>
      </ol>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-aiff-a-flac",
        "title":            "Convertir AIFF a FLAC – Audio de Mac y Pro Tools sin pérdida | VidToFLAC",
        "description":      "Convierte archivos AIFF a FLAC sin pérdida, reduciendo el tamaño sin perder calidad. 100% en tu navegador con FFmpeg. Ideal para flujos de trabajo de Mac, Logic Pro y Pro Tools.",
        "keywords":         "convertir AIFF a FLAC, AIFF FLAC sin pérdida, AIFF Mac FLAC, convertir audio AIFF online, FFmpeg AIFF FLAC navegador, Logic Pro AIFF FLAC",
        "canonical":        "https://vidtoflac.tech/convertir-aiff-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-aiff-a-flac/",
        "og_title":         "Convertir AIFF a FLAC – Audio Mac sin pérdida | VidToFLAC",
        "og_desc":          "Convierte AIFF a FLAC: misma calidad lossless, menos espacio. Directo en el navegador, sin subir nada.",
        "tw_title":         "Convertir AIFF a FLAC – Audio Mac sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte AIFF a FLAC: misma calidad lossless, menos espacio. Sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-aiff-a-flac/",
        "webapp_desc":      "Convierte archivos AIFF a FLAC sin pérdida de calidad, 100% en el navegador con FFmpeg (WebAssembly). Ideal para flujos de trabajo de Mac, Logic Pro y Pro Tools. Sin subir archivos.",
        "howto_name":       "Cómo convertir un archivo AIFF a FLAC sin pérdida de calidad",
        "hero_h1":          'Convierte tu <span class="accent">AIFF a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Misma calidad lossless que el AIFF original, con un tamaño hasta un 60% menor. Conversión en segundos, en tu navegador — sin subir ni un solo byte.",
        "seo_h2":           '¿Por qué convertir <span class="accent">AIFF a FLAC</span> en lugar de mantener el AIFF?',
        "seo_lede":         '<strong>AIFF</strong> y <strong>FLAC</strong> son ambos formatos sin pérdida, pero AIFF no comprime los datos de audio: un archivo de 10 minutos puede pesar más de 100 MB. FLAC aplica compresión lossless y reduce el tamaño entre un 40% y un 60% <strong>sin perder ni un bit de información</strong>. El resultado suena idéntico al AIFF original y ocupa mucho menos espacio en disco.',
        "breadcrumb_label": "Convertir AIFF a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de AIFF a FLAC</h2>
      <h3>AIFF: el formato lossless de Apple para producción musical</h3>
      <p>AIFF (Audio Interchange File Format) fue desarrollado por Apple en 1988 basándose en el formato IFF de Electronic Arts. Es el equivalente de Apple al WAV de Microsoft: un formato de audio sin pérdida que almacena PCM sin comprimir. AIFF es el formato nativo de exportación de <strong>Logic Pro</strong> y <strong>GarageBand</strong> en Mac, y es común en proyectos de <strong>Pro Tools</strong> y sesiones de grabación de estudio que usan Mac como plataforma. También lo genera el software de notación musical <strong>Sibelius</strong> y <strong>Finale</strong> al exportar audio.</p>
      <h3>AIFF vs. FLAC: misma calidad, diferente tamaño</h3>
      <p>Ambos formatos son sin pérdida, pero AIFF almacena el audio como PCM sin ninguna compresión, igual que WAV. FLAC aplica compresión lossless basada en predicción lineal y reduce el tamaño entre un 40 % y un 60 % sin eliminar ninguna información. Un proyecto de Logic Pro exportado como AIFF a 24 bit / 96 kHz puede generar archivos de 500 MB por cada 20 minutos; el equivalente en FLAC pesa entre 200 y 300 MB. La conversión es perfectamente reversible: puedes recuperar el AIFF original a partir del FLAC en cualquier momento.</p>
      <h3>AIFF en entornos de edición de vídeo</h3>
      <p>DaVinci Resolve en Linux tiene soporte limitado para AIFF. Aunque el formato usa PCM linear (que Resolve debería decodificar), la extensión .aiff puede no ser reconocida en todas las versiones de Resolve para Linux. Adobe Premiere Pro y Avid sí soportan AIFF en todas las plataformas. Si trabajas en Linux con Resolve y tienes archivos AIFF de un proyecto de Logic Pro, convertirlos a FLAC garantiza la importación sin problemas.</p>
      <h3>Paso a paso: convertir tu AIFF a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .aiff o .aif a VidToFLAC.</li>
        <li>La herramienta detecta la profundidad de bit (16, 24 o 32 bit) y la tasa de muestreo del AIFF.</li>
        <li>Pulsa <strong>Convertir</strong>. La compresión FLAC se aplica sin ninguna pérdida de información.</li>
        <li>Descarga el .flac resultante. Puedes verificar la conversión lossless comparando ambos archivos con inversión de fase: el resultado debe ser silencio.</li>
      </ol>
      <h3>Compatibilidad de AIFF con metadatos</h3>
      <p>AIFF soporta metadatos a través del chunk ID3, pero con limitaciones frente a FLAC, que soporta etiquetas Vorbis Comment nativas con campos arbitrarios (artista, álbum, año, número de pista, letra, portada). Si tu flujo de trabajo de archivo requiere metadatos completos, la conversión a FLAC también mejora la gestión de la biblioteca de audio.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-opus-a-flac",
        "title":            "Convertir OPUS a FLAC – Audio de Discord y YouTube sin pérdida | VidToFLAC",
        "description":      "Convierte archivos OPUS a FLAC sin pérdida, 100% en tu navegador con FFmpeg. Ideal para grabaciones de Discord, YouTube y videollamadas. Sin subir archivos.",
        "keywords":         "convertir OPUS a FLAC, OPUS FLAC sin pérdida, OPUS Discord FLAC, convertir audio OPUS online, FFmpeg OPUS FLAC navegador, grabaciones Discord FLAC",
        "canonical":        "https://vidtoflac.tech/convertir-opus-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-opus-a-flac/",
        "og_title":         "Convertir OPUS a FLAC – Audio Discord y YouTube | VidToFLAC",
        "og_desc":          "Convierte tus archivos OPUS (Discord, YouTube) a FLAC en tu navegador. Sin subir nada, sin registro.",
        "tw_title":         "Convertir OPUS a FLAC – Audio Discord y YouTube | VidToFLAC",
        "tw_desc":          "Convierte tus archivos OPUS a FLAC en tu navegador. Sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-opus-a-flac/",
        "webapp_desc":      "Convierte archivos OPUS a FLAC sin pérdida, 100% en el navegador con FFmpeg (WebAssembly). Ideal para grabaciones de Discord, YouTube y videollamadas. Sin subir archivos.",
        "howto_name":       "Cómo convertir un archivo OPUS a FLAC sin pérdida",
        "hero_h1":          'Convierte tu <span class="accent">OPUS a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Transcodifica grabaciones OPUS de Discord, YouTube o videollamadas a FLAC lossless en tu navegador. Compatibilidad total con editores profesionales — sin subir nada.",
        "seo_h2":           '¿Por qué convertir <span class="accent">OPUS a FLAC</span> para edición profesional?',
        "seo_lede":         '<strong>OPUS</strong> es el códec de audio por defecto en grabaciones de <strong>Discord</strong>, streams de YouTube y muchas videollamadas. Aunque ofrece excelente calidad a bajo bitrate, no es compatible de forma nativa con la mayoría de editores de vídeo profesionales. Convertir a <strong>FLAC</strong> garantiza que el audio se importe sin errores en DaVinci Resolve, Premiere Pro y Avid.',
        "breadcrumb_label": "Convertir OPUS a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de OPUS a FLAC</h2>
      <h3>¿Qué es Opus y por qué lo usan Discord y YouTube?</h3>
      <p>Opus es un códec de audio de código abierto estandarizado por la IETF (RFC 6716) en 2012. Fue diseñado para funcionar bien en un rango muy amplio de bitrates —desde 6 kbps para voz hasta 510 kbps para música— y con latencias muy bajas, lo que lo hace ideal para comunicaciones en tiempo real. <strong>Discord</strong> lo usa como códec de voz y audio en todos sus canales. <strong>YouTube</strong> lo usa para streams de baja latencia y en muchos vídeos del formato WebM. Las grabaciones de Zoom y Teams pueden usar también Opus en sus versiones más recientes. El resultado es que hoy en día muchos usuarios tienen archivos con audio Opus sin saberlo.</p>
      <h3>Por qué Opus no funciona en DaVinci Resolve</h3>
      <p>A diferencia de AAC o MP3, Opus es un códec relativamente reciente y de código abierto. Los editores de vídeo profesionales como DaVinci Resolve, Adobe Premiere Pro y Avid Media Composer todavía no incluyen soporte nativo para Opus. La razón es principalmente de mercado: el ecosistema de producción de vídeo profesional se desarrolló sobre codecs establecidos (AAC, PCM, AC3) y la adopción de Opus en ese ámbito es lenta. Si tienes una grabación de Discord o un vídeo WebM de YouTube con audio Opus e intentas importarlo en Resolve, el clip aparecerá sin pista de audio o con un error de importación.</p>
      <h3>Opus vs. FLAC: con pérdida vs. sin pérdida</h3>
      <p>Opus es un formato con pérdida, optimizado para el transporte eficiente de audio en redes. FLAC es sin pérdida, optimizado para el archivo y la edición. La conversión de Opus a FLAC produce un archivo FLAC que contiene exactamente el audio que había en el Opus, sin degradación adicional. La calidad del audio no mejora más allá de la calidad original del Opus, pero el formato resultante es universalmente compatible con editores de vídeo y no tiene pérdidas adicionales.</p>
      <h3>Paso a paso: convertir tu OPUS a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .opus o el WebM/MKV con audio Opus a VidToFLAC.</li>
        <li>Si el archivo tiene también pista de vídeo, selecciona <strong>MKV</strong> como salida. Si es solo audio, obtendrás un .flac.</li>
        <li>Pulsa <strong>Convertir</strong>. La transcodificación de Opus a FLAC es rápida.</li>
        <li>Importa el resultado en DaVinci Resolve, Premiere o Avid sin errores de códec.</li>
      </ol>
      <h3>Caso frecuente: grabaciones de gameplay con Discord overlay</h3>
      <p>Muchos creadores de contenido graban su gameplay con OBS (que genera MKV con Opus de forma predeterminada en versiones recientes) y simultáneamente graban el audio del chat de Discord. Si el MKV de OBS tiene audio Opus y quieres editarlo en DaVinci Resolve, la conversión a FLAC con VidToFLAC es el paso previo imprescindible.</p>
    </article>
  </section>""",
    },
    # ── Video formats ─────────────────────────────────────────────────────────
    {
        "slug":             "convertir-avi-a-flac",
        "title":            "Convertir AVI a FLAC – Audio sin pérdida para DaVinci Resolve | VidToFLAC",
        "description":      "Convierte el audio de tus archivos AVI a FLAC sin pérdida, 100% en tu navegador. Soluciona el error de códec de audio de DaVinci Resolve en archivos AVI de cámaras antiguas y grabaciones.",
        "keywords":         "convertir AVI a FLAC, AVI audio FLAC, AVI DaVinci Resolve sin sonido, remux AVI MKV FLAC, AVI FFmpeg navegador, audio AVI sin pérdida",
        "canonical":        "https://vidtoflac.tech/convertir-avi-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-avi-a-flac/",
        "og_title":         "Convertir AVI a FLAC – Audio sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus AVI a FLAC en segundos, en tu navegador. Soluciona el error de audio de DaVinci Resolve en archivos AVI — sin subir nada.",
        "tw_title":         "Convertir AVI a FLAC – Audio sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus AVI a FLAC en segundos. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-avi-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos AVI a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec de audio en DaVinci Resolve, Premiere y Avid. Funciona 100% en el navegador con FFmpeg (WebAssembly), sin subir archivos.",
        "howto_name":       "Cómo convertir el audio de un AVI a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">AVI a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona el error de códec de audio de DaVinci Resolve en archivos AVI de cámaras y grabaciones antiguas. Vídeo copiado bit a bit, audio a FLAC — 100% privado, en tu navegador.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos AVI?',
        "seo_lede":         'Los archivos <strong>AVI</strong> de cámaras antiguas, grabadoras y software de captura suelen llevar audio en <strong>MP3 o AC3</strong>. DaVinci Resolve —especialmente <strong>en Linux</strong>— no incluye los decodificadores para estos formatos sin licencias adicionales, provocando pistas de audio en gris o el clásico <strong>error de códec de audio</strong> al importar.',
        "breadcrumb_label": "Convertir AVI a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de AVI a FLAC</h2>
      <h3>AVI: el legado de Microsoft y sus múltiples códecs</h3>
      <p>AVI (Audio Video Interleave) fue el formato de vídeo estándar de Windows desde los años 90. Todavía hoy es el formato de salida de muchas <strong>cámaras digitales compactas antiguas</strong>, <strong>grabadoras de dashcam</strong> y algunas cámaras de seguridad IP. También es el formato de muchas grabaciones y películas en dominio público digitalizadas. El contenedor AVI es muy permisivo en cuanto a códecs: puede contener vídeo DivX, Xvid, H.264, MPEG-4 o incluso MJPEG, y audio en MP3, AC3, PCM linear o incluso AAC. Esta variedad es exactamente lo que genera problemas de compatibilidad.</p>
      <h3>Qué códecs de audio lleva un AVI y por qué fallan</h3>
      <p>Los AVI de cámaras de consumo de los años 2000-2010 suelen llevar audio <strong>MP3</strong>. Los AVI procedentes de DVD ripeados o material de broadcast suelen llevar <strong>AC3 (Dolby Digital)</strong>. Los AVI grabados con software como VirtualDub o Avisynth pueden llevar <strong>PCM linear</strong>, que sí es compatible. DaVinci Resolve en Linux no incluye decodificadores para MP3 ni AC3, lo que provoca que la pista de audio aparezca vacía o en gris al importar. Si el AVI tiene PCM linear, el audio sí se importa correctamente.</p>
      <h3>El problema del vídeo en AVI: DivX y Xvid</h3>
      <p>Muchos AVI de los años 2000 usan vídeo <strong>DivX o Xvid</strong> (variantes de MPEG-4 Part 2), que el navegador moderno no puede decodificar. En ese caso, VidToFLAC detecta el códec de vídeo incompatible y recodifica el vídeo a <strong>H.264</strong> automáticamente, usando calidad alta (CRF 18) para minimizar la degradación. El audio sigue pasando a FLAC. El archivo resultante es un MKV con H.264 + FLAC, totalmente compatible con DaVinci Resolve.</p>
      <h3>Paso a paso: convertir tu AVI a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .avi a VidToFLAC.</li>
        <li>La herramienta analiza el vídeo y el audio. Si el vídeo es DivX/Xvid, lo recodifica a H.264; si es H.264, lo copia bit a bit.</li>
        <li>Pulsa <strong>Convertir</strong>. El audio pasa siempre a FLAC, independientemente del códec original.</li>
        <li>Descarga el MKV resultante e impórtalo en DaVinci Resolve.</li>
      </ol>
      <h3>Consejo: digitalización de material de archivo</h3>
      <p>Si estás digitalizando vídeo antiguo de cintas VHS, Hi8 o MiniDV y el capturador genera archivos AVI con PCM linear, no necesitas conversión para DaVinci Resolve. Pero si el capturador genera AVI con MP3 —algunos capturadores USB económicos lo hacen por defecto—, convierte a FLAC antes de importar al proyecto de Resolve para asegurar la compatibilidad y facilitar la edición.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-webm-a-flac",
        "title":            "Convertir WebM a FLAC – Audio de YouTube sin pérdida | VidToFLAC",
        "description":      "Convierte el audio de tus archivos WebM (YouTube, navegador) a FLAC sin pérdida, 100% en tu navegador con FFmpeg. Soluciona el error de audio de DaVinci Resolve con archivos WebM.",
        "keywords":         "convertir WebM a FLAC, WebM audio FLAC, WebM DaVinci Resolve sin sonido, WebM YouTube FLAC, remux WebM MKV FLAC, FFmpeg WebM FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-webm-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-webm-a-flac/",
        "og_title":         "Convertir WebM a FLAC – Audio YouTube sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus WebM (YouTube, navegador) a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "tw_title":         "Convertir WebM a FLAC – Audio YouTube sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus WebM a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-webm-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos WebM (YouTube, grabaciones de navegador) a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec de audio en DaVinci Resolve. Funciona 100% en el navegador con FFmpeg (WebAssembly), sin subir archivos.",
        "howto_name":       "Cómo convertir el audio de un WebM a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">WebM a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona el error de códec de audio de DaVinci Resolve en archivos WebM de YouTube y grabaciones de navegador. Audio a FLAC lossless, vídeo copiado bit a bit — 100% privado.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos WebM?',
        "seo_lede":         'Los archivos <strong>WebM</strong> descargados de YouTube o generados por grabadores de navegador usan audio <strong>Opus o Vorbis</strong>. DaVinci Resolve —sobre todo <strong>en Linux</strong>— no puede decodificar estos formatos de serie, lo que provoca pistas de audio en gris o un <strong>error de códec de audio</strong> al importar el clip.',
        "breadcrumb_label": "Convertir WebM a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de WebM a FLAC</h2>
      <h3>¿Qué es WebM y de dónde vienen los archivos WebM?</h3>
      <p>WebM es un formato de vídeo de código abierto desarrollado por Google y basado en el contenedor Matroska (MKV). Fue diseñado específicamente para la web: YouTube lo usa para servir vídeo a navegadores que no tienen Flash, y es el formato de exportación de muchas herramientas de grabación de navegador (extensiones de Chrome, Firefox Screen Recorder, etc.). Los archivos .webm descargados con yt-dlp, youtube-dl u otras herramientas suelen tener vídeo <strong>VP9 o AV1</strong> y audio <strong>Opus o Vorbis</strong>.</p>
      <h3>Códecs de audio en WebM y por qué fallan en Resolve</h3>
      <p>YouTube usa <strong>Opus</strong> como códec de audio en la mayoría de sus streams WebM actuales. Los WebM más antiguos de YouTube (anteriores a 2014) pueden tener <strong>Vorbis</strong>. Los WebM de grabadoras de navegador usan también Opus habitualmente. Ninguno de estos códecs (Opus ni Vorbis) está soportado de forma nativa en DaVinci Resolve, Adobe Premiere Pro o Avid Media Composer. Al importar un WebM en Resolve, el audio simplemente no aparece.</p>
      <h3>Vídeo VP9 y AV1 en WebM: compatibilidad con el navegador</h3>
      <p>El vídeo VP9, usado por YouTube para resoluciones hasta 4K, es decodificable por los navegadores modernos (Chrome, Firefox, Edge). VidToFLAC puede copiar el stream VP9 bit a bit si el navegador lo soporta. AV1, el códec más reciente de YouTube para 4K y 8K, tiene soporte variable según el navegador y la CPU disponible. Si el AV1 no se puede decodificar en el navegador, VidToFLAC lo recodifica a H.264 para la previsualización. En todos los casos, el audio pasa siempre a FLAC.</p>
      <h3>Paso a paso: convertir tu WebM a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .webm a VidToFLAC.</li>
        <li>Selecciona <strong>MKV</strong> como formato de salida para mantener la mayor compatibilidad.</li>
        <li>Pulsa <strong>Convertir</strong>. El audio Opus o Vorbis se recodifica a FLAC; el vídeo VP9 o AV1 se copia bit a bit o se recodifica a H.264 según el soporte del navegador.</li>
        <li>Importa el MKV en DaVinci Resolve. La pista de audio FLAC se importará correctamente.</li>
      </ol>
      <h3>Diferencia entre WebM y MKV</h3>
      <p>WebM es un subconjunto de MKV: usa el mismo contenedor pero está restringido a los códecs VP8/VP9/AV1 para vídeo y Vorbis/Opus para audio. Al convertir un WebM a MKV con FLAC, el resultado es técnicamente un MKV estándar con mayor flexibilidad de códec. El archivo resultante es más compatible con software de edición profesional que el WebM original.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-wmv-a-flac",
        "title":            "Convertir WMV a FLAC – Audio sin pérdida para DaVinci Resolve | VidToFLAC",
        "description":      "Convierte el audio de tus archivos WMV (Windows Media Video) a FLAC sin pérdida, 100% en tu navegador. Soluciona el error de audio de DaVinci Resolve y Premiere con archivos WMV.",
        "keywords":         "convertir WMV a FLAC, WMV audio FLAC, WMV DaVinci Resolve sin sonido, remux WMV MKV FLAC, Windows Media Video FLAC, FFmpeg WMV FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-wmv-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-wmv-a-flac/",
        "og_title":         "Convertir WMV a FLAC – Audio Windows Media sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus WMV a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve con archivos Windows Media — sin subir nada.",
        "tw_title":         "Convertir WMV a FLAC – Audio Windows Media sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus WMV a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-wmv-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos WMV (Windows Media Video) a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec de audio en DaVinci Resolve y Premiere. Funciona 100% en el navegador con FFmpeg (WebAssembly).",
        "howto_name":       "Cómo convertir el audio de un WMV a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">WMV a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona el error de códec de audio de DaVinci Resolve en archivos Windows Media Video. Audio a FLAC lossless, vídeo copiado bit a bit — 100% privado, en tu navegador.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos WMV?',
        "seo_lede":         'Los archivos <strong>WMV (Windows Media Video)</strong> usan el códec de audio propietario <strong>WMA</strong> de Microsoft. DaVinci Resolve —especialmente <strong>en Linux y macOS</strong>— no incluye el decodificador de WMA de serie, lo que provoca que las pistas de audio aparezcan en gris o no se importen al abrir el clip.',
        "breadcrumb_label": "Convertir WMV a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de WMV a FLAC</h2>
      <h3>WMV: el formato de vídeo de Microsoft</h3>
      <p>WMV (Windows Media Video) es el formato de vídeo propietario de Microsoft, introducido en 1999 como parte de la plataforma Windows Media. Usa el códec de vídeo <strong>VC-1</strong> (o sus predecesores WMV1, WMV2, WMV3) y el códec de audio <strong>WMA</strong>. WMV fue muy popular en la era de los CD-ROM multimedia, tutoriales corporativos, presentaciones de PowerPoint con vídeo y grabaciones de escritorios Windows. Todavía hoy se puede encontrar en formación empresarial, material de archivo de los años 2000-2010 y algunos dispositivos de grabación industriales que usan tecnología Microsoft.</p>
      <h3>Doble problema: vídeo VC-1 y audio WMA</h3>
      <p>Los archivos WMV presentan dos problemas de compatibilidad: el vídeo <strong>VC-1</strong> y el audio <strong>WMA</strong>. VC-1 es un códec propietario de Microsoft con decodificación limitada en Linux; los navegadores modernos no pueden decodificarlo para previsualización. WMA es también propietario y DaVinci Resolve en Linux y macOS no incluye su decodificador. VidToFLAC gestiona ambos problemas: recodifica el vídeo VC-1 a <strong>H.264</strong> para la previsualización y recodifica el audio WMA a <strong>FLAC</strong>, produciendo un MKV compatible con Resolve y cualquier editor moderno.</p>
      <h3>Recuperar material de archivo en WMV</h3>
      <p>El caso de uso más habitual para la conversión de WMV es la recuperación de material corporativo o educativo antiguo: tutoriales, presentaciones, grabaciones de formación que se hicieron en los años 2000 y que ahora se quieren editar con software moderno. DaVinci Resolve no puede abrir estos archivos directamente; VidToFLAC permite convertirlos a un formato moderno sin necesidad de instalar software adicional ni usar Windows.</p>
      <h3>Paso a paso: convertir tu WMV a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .wmv a VidToFLAC.</li>
        <li>La herramienta detecta el vídeo VC-1 y lo recodifica a H.264 automáticamente, y el audio WMA lo convierte a FLAC.</li>
        <li>Pulsa <strong>Convertir</strong> y espera. La recodificación de VC-1 puede ser más lenta que un simple remux, ya que implica decodificar y recodificar el vídeo.</li>
        <li>Descarga el MKV resultante e impórtalo en DaVinci Resolve.</li>
      </ol>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-flv-a-flac",
        "title":            "Convertir FLV a FLAC – Audio sin pérdida para DaVinci Resolve | VidToFLAC",
        "description":      "Convierte el audio de tus archivos FLV (Flash Video) a FLAC sin pérdida, 100% en tu navegador. Soluciona el error de audio de DaVinci Resolve con vídeos FLV antiguos.",
        "keywords":         "convertir FLV a FLAC, FLV audio FLAC, FLV DaVinci Resolve sin sonido, remux FLV MKV FLAC, Flash Video FLAC, FFmpeg FLV FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-flv-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-flv-a-flac/",
        "og_title":         "Convertir FLV a FLAC – Flash Video sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus FLV a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve con archivos Flash Video — sin subir nada.",
        "tw_title":         "Convertir FLV a FLAC – Flash Video sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus FLV a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-flv-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos FLV (Flash Video) a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec de audio en DaVinci Resolve. Funciona 100% en el navegador con FFmpeg (WebAssembly).",
        "howto_name":       "Cómo convertir el audio de un FLV a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">FLV a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Recupera el audio de vídeos Flash antiguos reempaquetándolo a FLAC lossless. Vídeo copiado bit a bit, audio compatible con cualquier editor profesional — 100% privado, en tu navegador.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos FLV?',
        "seo_lede":         'Los archivos <strong>FLV (Flash Video)</strong> —el formato de vídeo de YouTube hasta 2015 y de muchas plataformas web antiguas— llevan audio en <strong>MP3 o AAC</strong>. DaVinci Resolve —sobre todo <strong>en Linux</strong>— no incluye los decodificadores necesarios de serie, lo que provoca pistas en gris o un <strong>error de códec de audio</strong> al importar estos clips.',
        "breadcrumb_label": "Convertir FLV a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de FLV a FLAC</h2>
      <h3>FLV: el formato Flash que dominó la web</h3>
      <p>FLV (Flash Video) fue el formato de vídeo de Adobe Flash Player y dominó el vídeo web entre 2005 y 2015. YouTube, Dailymotion, Metacafe y prácticamente todas las plataformas de vídeo de esa época servían sus contenidos en FLV. También lo usaban muchos videojuegos Flash y aplicaciones interactivas. Desde que los navegadores abandonaron Flash en 2020, los archivos FLV se han convertido en material de archivo: hay millones de vídeos en este formato que los usuarios quieren editar o conservar en formatos modernos.</p>
      <h3>Códecs en FLV: H.263, H.264, MP3 y AAC</h3>
      <p>Los FLV antiguos (anteriores a 2008) usan vídeo <strong>H.263 (Sorenson Spark o VP6)</strong> y audio <strong>MP3</strong>. Los FLV más modernos de YouTube (2008-2015) usan vídeo <strong>H.264</strong> y audio <strong>AAC</strong>. Los navegadores actuales no pueden reproducir H.263 ni VP6, pero sí H.264. VidToFLAC detecta el códec de vídeo: si es H.264, lo copia bit a bit; si es H.263 o VP6, lo recodifica a H.264. En todos los casos, el audio pasa a FLAC.</p>
      <h3>Por qué DaVinci Resolve no abre el audio de los FLV</h3>
      <p>DaVinci Resolve en Linux no incluye los decodificadores para MP3 ni para AAC. Si intentas importar un FLV en Resolve (suponiendo que el propio contenedor FLV sea reconocido, lo cual no está garantizado), la pista de audio aparecerá vacía. Además, el contenedor FLV en sí tiene soporte limitado en editores modernos. La solución es convertir el FLV a MKV con audio FLAC, que es un formato universalmente compatible.</p>
      <h3>Paso a paso: convertir tu FLV a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .flv a VidToFLAC.</li>
        <li>La herramienta detecta el códec de vídeo (H.263/VP6 o H.264) y el de audio (MP3 o AAC).</li>
        <li>Pulsa <strong>Convertir</strong>. Si el vídeo es H.264, se copia bit a bit; si es H.263/VP6, se recodifica a H.264. El audio siempre pasa a FLAC.</li>
        <li>Importa el MKV resultante en DaVinci Resolve. Tendrás vídeo y audio correctamente sincronizados.</li>
      </ol>
      <h3>Recuperación de vídeos de YouTube descargados en FLV</h3>
      <p>Muchos usuarios descargaron vídeos de YouTube entre 2008 y 2013 en formato FLV usando herramientas como KeepVid o Zamzar. Estos archivos siguen siendo válidos e interesantes como material de archivo, pero necesitan conversión para editarlos con software moderno. VidToFLAC es la forma más rápida de hacerlo directamente en el navegador, sin instalaciones adicionales.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-vob-a-flac",
        "title":            "Convertir VOB a FLAC – Audio de DVD sin pérdida para DaVinci Resolve | VidToFLAC",
        "description":      "Convierte el audio de tus archivos VOB (DVD) a FLAC sin pérdida, 100% en tu navegador. Soluciona el error de códec AC3/DTS de DaVinci Resolve con copias de DVD.",
        "keywords":         "convertir VOB a FLAC, VOB DVD audio FLAC, VOB DaVinci Resolve sin sonido, remux VOB MKV FLAC, DVD VOB FLAC, AC3 FLAC DaVinci Resolve",
        "canonical":        "https://vidtoflac.tech/convertir-vob-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-vob-a-flac/",
        "og_title":         "Convertir VOB a FLAC – Audio DVD sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus archivos VOB de DVD a FLAC en tu navegador. Soluciona el error de AC3/DTS de DaVinci Resolve — sin subir nada.",
        "tw_title":         "Convertir VOB a FLAC – Audio DVD sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus VOB de DVD a FLAC en tu navegador. Soluciona el error de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-vob-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos VOB (DVD) a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec AC3/DTS en DaVinci Resolve. Funciona 100% en el navegador con FFmpeg (WebAssembly).",
        "howto_name":       "Cómo convertir el audio de un VOB de DVD a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">VOB a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona el error de códec AC3/DTS de DaVinci Resolve en archivos VOB de DVD. Audio a FLAC lossless, vídeo copiado bit a bit — 100% privado, en tu navegador.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos VOB?',
        "seo_lede":         'Los archivos <strong>VOB</strong> de copias de DVD llevan audio en <strong>AC3 (Dolby Digital) o DTS</strong>. DaVinci Resolve —especialmente <strong>en Linux</strong>— no incluye los decodificadores para estos formatos sin licencias de pago, lo que provoca que las pistas de audio aparezcan en gris o que el clip no se importe con sonido.',
        "breadcrumb_label": "Convertir VOB a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de VOB a FLAC</h2>
      <h3>VOB: el formato nativo del DVD</h3>
      <p>VOB (Video Object) es el formato de contenedor del DVD-Vídeo. Los archivos .vob se encuentran en la carpeta VIDEO_TS del DVD y contienen los streams de vídeo y audio multiplexados según el estándar MPEG-2 Program Stream. Cada DVD puede tener múltiples archivos VOB (VIDEO_TS_01.VOB, VIDEO_TS_02.VOB…) que corresponden a los capítulos del disco. Los archivos VOB son comunes en copias digitalizadas de DVD personales, material de archivo en formato DVD y proyectos de restauración de vídeo antiguo.</p>
      <h3>Códecs en VOB: MPEG-2 y AC3</h3>
      <p>El vídeo de un archivo VOB es siempre <strong>MPEG-2</strong>, el estándar del DVD. El audio puede ser <strong>AC3 (Dolby Digital)</strong> de 2 a 6 canales —el más habitual en DVDs comerciales—, <strong>DTS</strong> en DVD con pistas de alta calidad, o <strong>PCM linear</strong> en algunos DVDs de karaoke o musicales. MPEG-2 no es decodificable por los navegadores modernos, por lo que VidToFLAC siempre recodifica el vídeo a H.264. AC3 y DTS no están disponibles en DaVinci Resolve gratuito en Linux; el audio pasa a FLAC.</p>
      <h3>El problema del audio multicanal en VOB</h3>
      <p>Los DVDs con audio AC3 5.1 (6 canales: frontal izquierdo, frontal derecho, centro, subwoofer, surround izquierdo, surround derecho) presentan un caso especial. Al convertir a FLAC, VidToFLAC preserva todos los canales: el archivo FLAC resultante será también multicanal (5.1 o el número de canales original). DaVinci Resolve puede importar FLAC multicanal y asignar los canales individuales en el inspector de audio del timeline.</p>
      <h3>Paso a paso: convertir tu VOB a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .vob a VidToFLAC. Si tienes múltiples VOBs de un DVD, conviértelos de uno en uno o únelos antes con una herramienta como MKVToolNix.</li>
        <li>Pulsa <strong>Convertir</strong>. El vídeo MPEG-2 se recodifica a H.264; el audio AC3 o DTS pasa a FLAC.</li>
        <li>Descarga el MKV resultante e impórtalo en DaVinci Resolve.</li>
        <li>Si el audio es 5.1, verifica en el inspector de clips de Resolve que los canales están asignados correctamente.</li>
      </ol>
      <h3>Alternativa: extraer solo el audio</h3>
      <p>Si solo necesitas el audio del DVD (por ejemplo, para sincronizarlo con vídeo grabado en otro dispositivo), puedes usar VidToFLAC para extraer únicamente la pista de audio a un archivo .flac. La herramienta detecta los archivos que tienen vídeo y ofrece la opción de salida en MKV, pero si seleccionas el formato de solo audio, obtendrás el .flac directamente.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-ts-a-flac",
        "title":            "Convertir TS a FLAC – Audio de grabaciones de TV sin pérdida | VidToFLAC",
        "description":      "Convierte el audio de archivos TS (Transport Stream) de grabaciones de TV y Blu-ray a FLAC sin pérdida, 100% en tu navegador. Soluciona el error de audio en DaVinci Resolve.",
        "keywords":         "convertir TS a FLAC, TS Transport Stream FLAC, TS grabación TV FLAC, TS DaVinci Resolve sin sonido, remux TS MKV FLAC, M2TS FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-ts-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-ts-a-flac/",
        "og_title":         "Convertir TS a FLAC – Grabaciones TV sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus archivos TS de grabaciones de TV o Blu-ray a FLAC en tu navegador. Soluciona el error de DaVinci Resolve — sin subir nada.",
        "tw_title":         "Convertir TS a FLAC – Grabaciones TV sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus archivos TS a FLAC en tu navegador. Soluciona el error de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-ts-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos TS y M2TS (Transport Stream, grabaciones de TV, Blu-ray) a FLAC sin pérdida dentro de un MKV (remux). Funciona 100% en el navegador con FFmpeg (WebAssembly).",
        "howto_name":       "Cómo convertir el audio de un archivo TS a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">TS a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona el error de códec de audio de DaVinci Resolve en grabaciones de TV y archivos Blu-ray TS/M2TS. Audio a FLAC lossless, vídeo copiado bit a bit — 100% privado.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos TS?',
        "seo_lede":         'Los archivos <strong>TS y M2TS</strong> —el formato estándar de grabaciones de TDT, sintonizadores de TV y discos Blu-ray— suelen llevar audio en <strong>AC3, AAC o DTS</strong>. DaVinci Resolve —sobre todo <strong>en Linux</strong>— no incluye los decodificadores para estos formatos sin licencias adicionales, provocando pistas de audio en gris al importar.',
        "breadcrumb_label": "Convertir TS a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de TS a FLAC</h2>
      <h3>TS y M2TS: el formato del broadcast digital</h3>
      <p>TS (Transport Stream, MPEG-2 TS) es el formato estándar para la transmisión de vídeo digital terrestre (TDT), por satélite y por cable. Los sintonizadores TDT, los grabadores PVR (Personal Video Recorder) y muchas aplicaciones de grabación de TV como VLC o TVHeadend generan archivos .ts con los contenidos grabados. M2TS es una variante usada por los discos Blu-ray y por las cámaras Sony y Panasonic con grabación AVCHD. Ambos formatos pueden contener múltiples pistas de audio y subtítulos, tal como se transmiten en la señal de televisión.</p>
      <h3>Códecs habituales en archivos TS</h3>
      <p>El vídeo en TS puede ser <strong>H.264</strong> (el más común en TDT moderna), <strong>H.265/HEVC</strong> (en canales de alta definición recientes), o <strong>MPEG-2</strong> (en emisiones más antiguas). El audio puede ser <strong>AC3</strong> (común en señales europeas y estadounidenses), <strong>AAC</strong> (en algunas emisiones de nueva generación), <strong>MP2 (MPEG-1 Audio Layer 2)</strong> (en emisiones antiguas), o <strong>DTS</strong> (en Blu-ray y emisiones de alta calidad). Ninguno de estos códecs de audio excepto PCM está disponible en DaVinci Resolve gratuito en Linux.</p>
      <h3>OBS Studio y el formato TS</h3>
      <p>OBS Studio también puede grabar en formato TS con el nombre de <em>fragmented MP4</em> o como salida de flujo de datos, aunque su formato de grabación principal es MKV. Si usas OBS con codificación de hardware (NVENC, QSV, AMF) y grabas en TS, el audio puede ser AAC o incluso Opus según la configuración. La conversión a FLAC con VidToFLAC soluciona los problemas de compatibilidad con Resolve en cualquier caso.</p>
      <h3>Paso a paso: convertir tu TS a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .ts o .m2ts a VidToFLAC.</li>
        <li>Selecciona <strong>MKV</strong> como formato de salida.</li>
        <li>Pulsa <strong>Convertir</strong>. El vídeo H.264 se copia bit a bit; el MPEG-2 se recodifica a H.264. El audio AC3, AAC, MP2 o DTS pasa a FLAC.</li>
        <li>Descarga el MKV e impórtalo en DaVinci Resolve. Todas las pistas de audio estarán disponibles como FLAC.</li>
      </ol>
      <h3>Pistas múltiples de audio en TS</h3>
      <p>Las grabaciones de TDT pueden incluir varias pistas de audio: el idioma original, el doblaje y la audiodescrípción para personas con discapacidad visual. VidToFLAC convierte todas las pistas de audio del TS a FLAC en el MKV de salida, permitiéndote elegir cuál usar al importar en Resolve.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-m4v-a-flac",
        "title":            "Convertir M4V a FLAC – Audio de iTunes y Apple TV sin pérdida | VidToFLAC",
        "description":      "Convierte el audio de tus archivos M4V (iTunes, Apple TV) a FLAC sin pérdida, 100% en tu navegador. Soluciona el error de audio de DaVinci Resolve con archivos M4V de Apple.",
        "keywords":         "convertir M4V a FLAC, M4V iTunes FLAC, M4V Apple TV FLAC, M4V DaVinci Resolve sin sonido, remux M4V MKV FLAC, FFmpeg M4V FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-m4v-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-m4v-a-flac/",
        "og_title":         "Convertir M4V a FLAC – Audio iTunes sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus archivos M4V de iTunes o Apple TV a FLAC en tu navegador. Soluciona el error de DaVinci Resolve — sin subir nada.",
        "tw_title":         "Convertir M4V a FLAC – Audio iTunes sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus M4V a FLAC en tu navegador. Soluciona el error de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-m4v-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos M4V (iTunes, Apple TV) a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec de audio en DaVinci Resolve. Funciona 100% en el navegador con FFmpeg (WebAssembly).",
        "howto_name":       "Cómo convertir el audio de un M4V a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">M4V a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona el error de códec de audio de DaVinci Resolve en archivos M4V de iTunes y Apple TV. Audio a FLAC lossless, vídeo copiado bit a bit — 100% privado, en tu navegador.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos M4V?',
        "seo_lede":         'Los archivos <strong>M4V</strong> de iTunes y Apple TV usan audio <strong>AAC</strong> envuelto en un contenedor MPEG-4 con extensión Apple. DaVinci Resolve —especialmente <strong>en Linux</strong>— no incluye el decodificador de AAC de serie, lo que provoca pistas de audio en gris o que el clip no se importe con sonido al abrir el archivo.',
        "breadcrumb_label": "Convertir M4V a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de M4V a FLAC</h2>
      <h3>¿Qué es M4V y en qué se diferencia de MP4?</h3>
      <p>M4V es una extensión de archivo creada por Apple para distinguir los archivos de vídeo MPEG-4 del ecosistema Apple de los MP4 genéricos. Técnicamente, M4V es un contenedor MPEG-4 estándar, idéntico a MP4, pero con una marca de Apple y, en algunos casos, protección DRM (Digital Rights Management) mediante el sistema FairPlay de Apple. Los archivos M4V provienen principalmente de compras de películas y series en iTunes (ahora Apple TV), de algunas aplicaciones de vídeo del ecosistema Apple y de exportaciones de iMovie.</p>
      <h3>M4V con DRM: limitaciones importantes</h3>
      <p>Los archivos M4V comprados en iTunes o Apple TV pueden estar protegidos con <strong>DRM FairPlay</strong>. Si el M4V tiene DRM, VidToFLAC <strong>no puede procesarlo</strong>: el DRM impide que cualquier software lea el contenido del archivo. Solo los M4V sin DRM (exportaciones de iMovie, archivos ripeados legalmente de contenido propio, o M4V que hayas creado tú mismo) pueden convertirse. Para verificar si tu M4V tiene DRM, intenta reproducirlo en VLC: si VLC no puede abrirlo o no muestra imagen/audio, probablemente tenga DRM.</p>
      <h3>M4V sin DRM: el mismo proceso que MP4</h3>
      <p>Los M4V sin DRM se procesan exactamente igual que los MP4. Contienen vídeo H.264 o H.265 y audio AAC. DaVinci Resolve en Linux no incluye el decodificador de AAC, por lo que la pista de audio aparecerá en gris al importar. La conversión a FLAC con VidToFLAC produce un MKV con audio FLAC compatible con Resolve.</p>
      <h3>Paso a paso: convertir tu M4V a FLAC</h3>
      <ol>
        <li>Verifica que tu M4V no tiene DRM (prueba a abrirlo en VLC y reproduciéndolo sin problemas).</li>
        <li>Arrastra el archivo .m4v a VidToFLAC.</li>
        <li>Selecciona <strong>MKV</strong> como formato de salida y pulsa <strong>Convertir</strong>.</li>
        <li>Importa el MKV en DaVinci Resolve. La pista de audio FLAC se importará correctamente.</li>
      </ol>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-mpeg-a-flac",
        "title":            "Convertir MPEG a FLAC – Audio sin pérdida para DaVinci Resolve | VidToFLAC",
        "description":      "Convierte el audio de tus archivos MPEG/MPG a FLAC sin pérdida, 100% en tu navegador. Soluciona el error de códec de audio de DaVinci Resolve con archivos MPEG de cámaras y DVDs.",
        "keywords":         "convertir MPEG a FLAC, MPG a FLAC, MPEG audio FLAC, MPEG DaVinci Resolve sin sonido, remux MPEG MKV FLAC, FFmpeg MPEG FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-mpeg-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-mpeg-a-flac/",
        "og_title":         "Convertir MPEG a FLAC – Audio sin pérdida | VidToFLAC",
        "og_desc":          "Convierte el audio de tus archivos MPEG/MPG a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "tw_title":         "Convertir MPEG a FLAC – Audio sin pérdida | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus MPEG a FLAC en tu navegador. Soluciona el error de audio de DaVinci Resolve — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-mpeg-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos MPEG/MPG a FLAC sin pérdida dentro de un MKV (remux) para solucionar el error de códec de audio en DaVinci Resolve. Funciona 100% en el navegador con FFmpeg (WebAssembly).",
        "howto_name":       "Cómo convertir el audio de un MPEG a FLAC para DaVinci Resolve",
        "hero_h1":          'Convierte tu <span class="accent">MPEG a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Soluciona el error de códec de audio de DaVinci Resolve en archivos MPEG/MPG de cámaras, DVDs y grabaciones antiguas. Audio a FLAC lossless, vídeo copiado bit a bit — 100% privado.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos MPEG?',
        "seo_lede":         'Los archivos <strong>MPEG y MPG</strong> —el formato estándar de cámaras de vídeo digitales antiguas, DVD y muchas grabaciones— llevan audio en <strong>MP2, MP3 o AC3</strong>. DaVinci Resolve —sobre todo <strong>en Linux</strong>— no incluye los decodificadores para estos formatos de serie, lo que provoca que las pistas de audio aparezcan en gris o no se importen al abrir el clip.',
        "breadcrumb_label": "Convertir MPEG a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de MPEG a FLAC</h2>
      <h3>MPEG: el estándar de vídeo de los años 90 y 2000</h3>
      <p>MPEG (Moving Picture Experts Group) engloba una familia de estándares de compresión de vídeo: <strong>MPEG-1</strong> (usado en VCD y CD-ROM multimedia de los 90), <strong>MPEG-2</strong> (el estándar del DVD, DVD-R y transmisión terrestre digital), y <strong>MPEG-4</strong> (base del H.264 moderno). Los archivos con extensión .mpeg o .mpg corresponden habitualmente a MPEG-1 o MPEG-2. Son comunes en grabaciones de cámaras de vídeo digital de los años 2000, capturas de TDT y programas de edición de vídeo doméstico como Pinnacle o Nero Video.</p>
      <h3>El códec de audio en archivos MPEG</h3>
      <p>Los archivos MPEG-1 usan casi siempre audio <strong>MPEG-1 Audio Layer 2 (MP2)</strong>, el predecesor del MP3. Los archivos MPEG-2 de DVD y TDT usan <strong>AC3 (Dolby Digital)</strong> o <strong>MP2</strong>. Algunos archivos MPEG generados por cámaras de consumo pueden usar <strong>MP3</strong>. El decodificador de MP2 no está incluido en DaVinci Resolve gratuito en Linux (a pesar de que MP2 es un estándar más antiguo que MP3), ni tampoco AC3. Si tienes un archivo .mpg con audio en gris en Resolve, la conversión a FLAC resuelve el problema.</p>
      <h3>Vídeo MPEG-2: recodificación a H.264</h3>
      <p>MPEG-2 no es decodificable por los navegadores modernos (Chrome, Firefox, Safari). Por eso VidToFLAC siempre recodifica el vídeo de archivos MPEG a <strong>H.264</strong>, lo que permite la previsualización en la propia página web. La recodificación se realiza con calidad alta (CRF 18) para minimizar la degradación visual. El archivo resultante es un MKV con vídeo H.264 y audio FLAC, totalmente compatible con DaVinci Resolve y cualquier editor moderno.</p>
      <h3>Paso a paso: convertir tu MPEG a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .mpeg o .mpg a VidToFLAC.</li>
        <li>La herramienta detecta el códec MPEG-2 y recodifica el vídeo a H.264 automáticamente.</li>
        <li>Pulsa <strong>Convertir</strong>. El proceso puede tardar más que un remux simple, ya que implica decodificar y recodificar el vídeo.</li>
        <li>Descarga el MKV resultante con H.264 + FLAC e impórtalo en DaVinci Resolve.</li>
      </ol>
      <h3>Digitalización de material VHS y Super 8</h3>
      <p>Muchos escáneres y capturadores de vídeo analógico (VHS, Super 8, Betamax) generan archivos MPEG-2 como formato de salida. Si estás digitalizando tu fondo familiar de vídeo analógico y el capturador produce archivos .mpg, VidToFLAC es una herramienta conveniente para convertirlos a un formato moderno (MKV + H.264 + FLAC) que se pueda editar con DaVinci Resolve sin problemas.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convertir-3gp-a-flac",
        "title":            "Convertir 3GP a FLAC – Audio de móviles antiguos sin pérdida | VidToFLAC",
        "description":      "Convierte el audio de tus archivos 3GP de móviles antiguos a FLAC sin pérdida, 100% en tu navegador. Recupera vídeos de Nokia, Samsung y grabaciones antiguas de smartphone.",
        "keywords":         "convertir 3GP a FLAC, 3GP audio FLAC, 3GP móvil FLAC, 3GP DaVinci Resolve sin sonido, remux 3GP MKV FLAC, FFmpeg 3GP FLAC navegador",
        "canonical":        "https://vidtoflac.tech/convertir-3gp-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-3gp-a-flac/",
        "og_title":         "Convertir 3GP a FLAC – Audio móviles antiguos | VidToFLAC",
        "og_desc":          "Convierte el audio de tus archivos 3GP de móviles antiguos a FLAC en tu navegador. Recupera vídeos Nokia, Samsung y grabaciones antiguas — sin subir nada.",
        "tw_title":         "Convertir 3GP a FLAC – Audio móviles antiguos | VidToFLAC",
        "tw_desc":          "Convierte el audio de tus 3GP a FLAC en tu navegador. Recupera vídeos de móviles antiguos — sin subir nada.",
        "webapp_url":       "https://vidtoflac.tech/convertir-3gp-a-flac/",
        "webapp_desc":      "Convierte el audio de archivos 3GP (vídeos de móviles antiguos) a FLAC sin pérdida dentro de un MKV (remux) para compatibilidad con editores de vídeo profesionales. Funciona 100% en el navegador con FFmpeg (WebAssembly).",
        "howto_name":       "Cómo convertir el audio de un archivo 3GP a FLAC",
        "hero_h1":          'Convierte tu <span class="accent">3GP a FLAC</span> sin pérdida de calidad',
        "hero_sub":         "Recupera el audio de vídeos 3GP de Nokia, Samsung y grabaciones antiguas de smartphone a FLAC lossless. Compatible con cualquier editor profesional — 100% privado, en tu navegador.",
        "seo_h2":           '¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus archivos 3GP?',
        "seo_lede":         'Los archivos <strong>3GP</strong> —el formato de vídeo de móviles antiguos (Nokia, Samsung, Motorola) y algunas cámaras compactas— usan audio en <strong>AAC o AMR</strong>. DaVinci Resolve —especialmente <strong>en Linux</strong>— no incluye los decodificadores para estos formatos de serie, lo que provoca que las pistas de audio no se importen o aparezcan en gris al abrir el clip.',
        "breadcrumb_label": "Convertir 3GP a FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Guía de conversión</div>
    <article>
      <h2 id="guia-formato-titulo">Todo sobre la conversión de 3GP a FLAC</h2>
      <h3>3GP: el formato de vídeo de los primeros smartphones</h3>
      <p>3GP (3rd Generation Partnership Project) fue desarrollado para transmitir vídeo en redes de telefonía móvil 3G. Es el formato de grabación nativo de prácticamente todos los teléfonos móviles de la era pre-smartphone: Nokia, Samsung, Motorola, Sony Ericsson y LG usaban 3GP como formato de vídeo estándar entre 2003 y 2010. También está presente en algunas cámaras compactas económicas y videocámaras de bolsillo de esa época. Hoy en día, los archivos 3GP representan un importante fondo de material familiar y documentos históricos que muchos usuarios quieren digitalizar y editar.</p>
      <h3>Códecs en 3GP y sus limitaciones</h3>
      <p>El vídeo en 3GP puede ser <strong>H.263</strong> (el estándar de los primeros teléfonos), <strong>H.264</strong> (en smartphones más recientes de 2008-2010), o <strong>MPEG-4 Part 2</strong>. El audio puede ser <strong>AMR-NB o AMR-WB</strong> (Adaptive Multi-Rate, el códec de voz de la telefonía móvil, muy común en Nokia) o <strong>AAC</strong> (en smartphones más avanzados). AMR es un códec optimizado para voz humana que suena bien en llamadas pero tiene baja calidad para música o audio en general. DaVinci Resolve no incluye decodificadores para AMR ni para AAC en Linux.</p>
      <h3>Calidad de vídeo en 3GP: qué esperar</h3>
      <p>Los archivos 3GP de móviles antiguos tienen resoluciones muy bajas: típicamente <strong>176×144 píxeles (QCIF)</strong> o <strong>320×240 (QVGA)</strong>. La calidad de vídeo es limitada incluso después de la conversión: VidToFLAC recodifica el vídeo a H.264, pero la resolución y la calidad visual original se mantienen tal como estaban. La conversión no mejora la calidad del vídeo; solo mejora la compatibilidad del códec de audio.</p>
      <h3>Paso a paso: convertir tu 3GP a FLAC</h3>
      <ol>
        <li>Arrastra tu archivo .3gp a VidToFLAC.</li>
        <li>La herramienta detecta el códec de vídeo (H.263 o H.264) y el de audio (AMR o AAC).</li>
        <li>Pulsa <strong>Convertir</strong>. El H.263 se recodifica a H.264; el audio AMR o AAC pasa a FLAC.</li>
        <li>Importa el MKV resultante en DaVinci Resolve. El audio ya no aparecerá en gris.</li>
      </ol>
      <h3>Consejo: recuperación de vídeos de Nokia y Samsung antiguos</h3>
      <p>Los vídeos grabados con Nokia N70, N73, N95 y similares están en formato 3GP con audio AMR. Si tienes estos archivos en un ordenador antiguo o los has extraído de una tarjeta de memoria, VidToFLAC te permite convertirlos directamente en el navegador sin instalar ningún software. El resultado es un MKV editable en DaVinci Resolve u otros editores modernos.</p>
    </article>
  </section>""",
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# Cadenas originales a sustituir (copiadas literalmente de index.html)
# ─────────────────────────────────────────────────────────────────────────────
O_TITLE      = '<title>VidToFLAC – Audio de vídeo a FLAC para DaVinci Resolve</title>'
O_META_DESC  = '<meta name="description" content="¿DaVinci Resolve sin sonido? Convierte el audio de tus vídeos a FLAC sin pérdida, gratis y 100% en tu navegador. Sin subir archivos." />'
O_META_KW    = '<meta name="keywords" content="convertir vídeo a FLAC, error de códec de audio, DaVinci Resolve sin sonido, remux de vídeo sin pérdida de calidad, FFmpeg en navegador, MKV audio FLAC, audio AAC DaVinci Resolve Linux" />'
O_CANONICAL  = '<link rel="canonical" href="https://vidtoflac.tech/" />'
O_OG_URL     = '<meta property="og:url" content="https://vidtoflac.tech/" />'
O_OG_TITLE   = '<meta property="og:title" content="VidToFLAC – Audio de vídeo a FLAC para DaVinci Resolve" />'
O_OG_DESC    = '<meta property="og:description" content="Soluciona el audio que DaVinci Resolve no reproduce. Remux a MKV con audio FLAC sin pérdida, 100% en tu navegador y privado. Sin subir archivos." />'
O_TW_TITLE   = '<meta name="twitter:title" content="VidToFLAC – Audio de vídeo a FLAC para DaVinci Resolve" />'
O_TW_DESC    = '<meta name="twitter:description" content="Soluciona el audio que DaVinci Resolve no reproduce. Remux a MKV con audio FLAC sin pérdida, 100% en tu navegador y privado." />'
# url + description combinados para no colisionar con el bloque WebSite/Organization
O_WEBAPP     = ('    "url": "https://vidtoflac.tech/",\n'
                '    "description": "Conversor que cambia el audio de tus vídeos a FLAC dentro de un contenedor MKV (remux sin pérdida) para solucionar el error de códec de audio en DaVinci Resolve, Premiere y Avid. Funciona 100% en el navegador con FFmpeg (WebAssembly), sin subir archivos a ningún servidor.",')
O_HOWTO_NAME = '"name": "Cómo convertir el audio de un vídeo a FLAC para DaVinci Resolve",'
O_HOWTO_URL  = '"url": "https://vidtoflac.tech/#problema-titulo"'
O_HERO_H1    = '    <h1 class="hero-title">Convierte el audio de tus vídeos a <span class="accent">FLAC para DaVinci Resolve</span></h1>'
O_HERO_SUB   = '    <p class="hero-sub">De forma instantánea y 100% privada. Todo el procesamiento ocurre dentro de tu navegador — no se sube ni un solo byte a ningún servidor.</p>'
O_SEO_H2     = '      <h2 id="problema-titulo">¿Por qué <span class="accent">DaVinci Resolve no lee el audio</span> de tus vídeos?</h2>'
O_SEO_LEDE   = ('      <p class="lede">Si has abierto un clip en DaVinci Resolve y aparece <strong>sin sonido</strong>'
                ' —o directamente con la pista de audio en gris— casi siempre es un <strong>error de códec de audio</strong>,'
                ' no un problema de tu micrófono ni de tu proyecto.</p>')
O_BRAND        = '<span class="brand-name">VidTo<span class="brand-accent">FLAC</span></span>'
O_STYLE_END    = '  </style>\n</head>'
O_UNIQUE_GUIDE = '<!--{{UNIQUE_GUIDE}}-->'


# ─────────────────────────────────────────────────────────────────────────────
def build_page(page: dict, template: str) -> str:
    h = template

    h = h.replace(O_TITLE,     f'<title>{page["title"]}</title>')
    h = h.replace(O_META_DESC, f'<meta name="description" content="{page["description"]}" />')
    h = h.replace(O_META_KW,   f'<meta name="keywords" content="{page["keywords"]}" />')
    h = h.replace(O_CANONICAL, f'<link rel="canonical" href="{page["canonical"]}" />')
    h = h.replace(O_OG_URL,    f'<meta property="og:url" content="{page["og_url"]}" />')
    h = h.replace(O_OG_TITLE,  f'<meta property="og:title" content="{page["og_title"]}" />')
    h = h.replace(O_OG_DESC,   f'<meta property="og:description" content="{page["og_desc"]}" />')
    h = h.replace(O_TW_TITLE,  f'<meta name="twitter:title" content="{page["tw_title"]}" />')
    h = h.replace(O_TW_DESC,   f'<meta name="twitter:description" content="{page["tw_desc"]}" />')

    h = h.replace(O_WEBAPP,
        f'    "url": "{page["webapp_url"]}",\n'
        f'    "description": "{page["webapp_desc"]}",')

    h = h.replace(O_HOWTO_NAME, f'"name": "{page["howto_name"]}",')
    h = h.replace(O_HOWTO_URL,  f'"url": "{page["canonical"]}"')

    h = h.replace(O_HERO_H1,  f'    <h1 class="hero-title">{page["hero_h1"]}</h1>')
    h = h.replace(O_HERO_SUB, f'    <p class="hero-sub">{page["hero_sub"]}</p>')
    h = h.replace(O_SEO_H2,   f'      <h2 id="problema-titulo">{page["seo_h2"]}</h2>')
    h = h.replace(O_SEO_LEDE, f'      <p class="lede">{page["seo_lede"]}</p>')
    h = h.replace(O_UNIQUE_GUIDE, page.get("unique_guide", ""))

    # Brand name → enlace de vuelta al inicio
    h = h.replace(O_BRAND,
        f'<a href="/" class="brand-home-link">'
        f'<span class="brand-name">VidTo<span class="brand-accent">FLAC</span></span></a>')

    # CSS para el enlace de marca + cierre de </style>
    h = h.replace(O_STYLE_END,
        '  .brand-home-link { text-decoration: none; color: inherit; }\n'
        + O_STYLE_END)

    # Breadcrumb JSON-LD justo antes de </head>
    breadcrumb = (
        '  <script type="application/ld+json">\n'
        '  {\n'
        '    "@context": "https://schema.org",\n'
        '    "@type": "BreadcrumbList",\n'
        '    "itemListElement": [\n'
        '      {"@type": "ListItem", "position": 1, "name": "VidToFLAC", "item": "https://vidtoflac.tech/"},\n'
        f'      {{"@type": "ListItem", "position": 2, "name": "{page["breadcrumb_label"]}", "item": "{page["canonical"]}"}}\n'
        '    ]\n'
        '  }\n'
        '  </script>\n'
    )
    h = h.replace('</head>', breadcrumb + '</head>')

    return h


def update_sitemap(pages: list) -> None:
    path = os.path.join(BASE, 'sitemap.xml')
    with open(path, 'r', encoding='utf-8') as f:
        sitemap = f.read()

    new_entries = ''
    for page in pages:
        if page['canonical'] not in sitemap:
            new_entries += (
                f'  <url>\n'
                f'    <loc>{page["canonical"]}</loc>\n'
                f'    <lastmod>2026-06-05</lastmod>\n'
                f'    <changefreq>monthly</changefreq>\n'
                f'    <priority>0.8</priority>\n'
                f'  </url>\n'
            )

    if new_entries:
        sitemap = sitemap.replace('</urlset>', new_entries + '</urlset>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(sitemap)
        print('  sitemap.xml actualizado')


def main() -> None:
    with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
        template = f.read()

    for page in PAGES:
        out_dir  = os.path.join(BASE, page['slug'])
        out_path = os.path.join(out_dir, 'index.html')
        os.makedirs(out_dir, exist_ok=True)
        result = build_page(page, template)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(result)
        print(f'  {page["slug"]}/index.html')

    update_sitemap(PAGES)
    print('Listo.')


if __name__ == '__main__':
    main()
