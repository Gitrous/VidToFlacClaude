# -*- coding: utf-8 -*-
"""
merged_content.py — las cuatro páginas que agrupan las landings de formato.

Las 32 landings minoritarias (AVI, WebM, MP3, Opus…) eran demasiado parecidas
entre sí para indexarse por separado, así que build_pages.py las junta en dos
páginas por idioma: una de vídeo y otra de audio. Cada formato conserva su guía
propia (`unique_guide` + `seo_body` de su entrada original) como una sección con
ancla, y las URL antiguas pasan a redirigir a esa ancla.

Aquí solo vive lo que es de la página agrupada: metadatos, cabecera, el texto
que sustituye a "La solución" y la presentación del índice de formatos.
"""

VIDEO_FORMATS = ['avi', 'webm', 'wmv', 'flv', 'mpeg', 'ts', 'vob', '3gp', 'm4v']
AUDIO_FORMATS = ['mp3', 'aac', 'm4a', 'aiff', 'ogg', 'opus', 'wma']

LABEL = {
    'avi': 'AVI', 'webm': 'WebM', 'wmv': 'WMV', 'flv': 'FLV', 'mpeg': 'MPEG',
    'ts': 'TS', 'vob': 'VOB', '3gp': '3GP', 'm4v': 'M4V',
    'mp3': 'MP3', 'aac': 'AAC', 'm4a': 'M4A', 'aiff': 'AIFF', 'ogg': 'OGG',
    'opus': 'Opus', 'wma': 'WMA',
}

MERGED_ES = [
    {
        "slug":             "convertir-video-a-flac",
        "hero_figure":      """      <figure class="fig">
        <svg class="fig-svg" viewBox="0 0 660 262" width="660" height="262" role="img" aria-labelledby="t2127 d2909" xmlns="http://www.w3.org/2000/svg"><title id="t2127">Remux: el vídeo se copia y solo se recodifica el audio</title><desc id="d2909">Diagrama: la pista de vídeo pasa sin recodificar al MKV de salida, mientras la pista de audio AAC, MP3, AC-3 u Opus se decodifica y se vuelve a codificar en FLAC.</desc><text x="20" y="26" font-family="JetBrains Mono, ui-monospace, monospace" font-size="11" fill="#66666e">ARCHIVO DE ENTRADA</text><text x="640" y="26" text-anchor="end" font-family="JetBrains Mono, ui-monospace, monospace" font-size="11" fill="#66666e">ARCHIVO DE SALIDA (MKV)</text><rect x="20" y="40" width="170" height="70" rx="8" fill="#131316" stroke="rgba(255,255,255,.14)"/><text x="105.0" y="64" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Pista de vídeo</text><text x="105.0" y="84" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">H.264 · VP9 · MPEG-4</text><line x1="190" y1="75" x2="267" y2="75" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/><polygon points="275,75 267,71 267,79" fill="rgba(255,255,255,.28)"/><text x="232.5" y="66" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10" fill="#66666e">se copia</text><rect x="275" y="40" width="150" height="70" rx="8" fill="rgba(25,195,125,.08)" stroke="#19c37d"/><text x="350.0" y="64" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Sin tocar</text><text x="350.0" y="84" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">0 recodificaciones</text><line x1="425" y1="75" x2="482" y2="75" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/><polygon points="490,75 482,71 482,79" fill="rgba(255,255,255,.28)"/><rect x="490" y="40" width="150" height="70" rx="8" fill="rgba(25,195,125,.08)" stroke="#19c37d"/><text x="565.0" y="64" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Vídeo idéntico</text><text x="565.0" y="84" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">misma calidad</text><rect x="20" y="135" width="170" height="70" rx="8" fill="rgba(255,96,88,.07)" stroke="#ff6058"/><text x="105.0" y="159" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Pista de audio</text><text x="105.0" y="179" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">AAC · MP3 · AC-3 · Opus</text><line x1="190" y1="170" x2="267" y2="170" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/><polygon points="275,170 267,166 267,174" fill="rgba(255,255,255,.28)"/><text x="232.5" y="161" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10" fill="#66666e">decodifica</text><rect x="275" y="135" width="150" height="70" rx="8" fill="#131316" stroke="rgba(255,255,255,.14)"/><text x="350.0" y="159" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Recodificar</text><text x="350.0" y="179" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">a FLAC sin pérdida</text><line x1="425" y1="170" x2="482" y2="170" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/><polygon points="490,170 482,166 482,174" fill="rgba(255,255,255,.28)"/><rect x="490" y="135" width="150" height="70" rx="8" fill="rgba(25,195,125,.08)" stroke="#19c37d"/><text x="565.0" y="159" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Audio FLAC</text><text x="565.0" y="179" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">el editor sí lo lee</text><text x="20" y="228" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="12" fill="#a7a7ad">Excepción: si el navegador no puede decodificar el vídeo</text><text x="20" y="245" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="12" fill="#a7a7ad">(H.265/HEVC, MPEG-2, WMV, VP6), también se recodifica a H.264.</text></svg>
        <figcaption>Qué se copia y qué se recodifica en cada uno de estos nueve formatos de vídeo.</figcaption>
      </figure>""",
        "faqs":             [
            ("¿Por qué un AVI, un WebM o un VOB entran en DaVinci Resolve sin sonido?",
             "Por el códec de audio, que cambia con cada formato: los AVI antiguos suelen llevar <strong>MP3 o AC-3</strong>; los WebM, <strong>Opus o Vorbis</strong>; los VOB y los MPEG, <strong>AC-3 o MPEG Audio</strong>; los WMV, <strong>WMA</strong>; los TS de televisión, <strong>AC-3 o AAC</strong>; y los 3GP de móviles antiguos, <strong>AMR</strong>. DaVinci Resolve no decodifica ninguno de forma fiable, sobre todo en Linux, así que ves la imagen pero la pista queda vacía."),
            ("¿Se recodifica el vídeo al convertir?",
             "Depende del códec, no de la extensión. H.264, VP8, VP9, MPEG-4 (DivX, Xvid) y H.263 se copian sin recodificar. MPEG-2, WMV, VP6 y H.265/HEVC se recodifican a H.264 con calidad alta (<code>-crf 18</code>), lo que tarda más y no deja un vídeo idéntico bit a bit, aunque la diferencia no se aprecia a simple vista."),
            ("La vista previa de la página no muestra la imagen de mi AVI o 3GP, ¿ha fallado?",
             "No necesariamente. Si el vídeo es DivX, Xvid o H.263, VidToFLAC lo copia tal cual al MKV, pero el navegador no sabe decodificar esos códecs para enseñarlo. El archivo descargado está completo; compruébalo abriéndolo en tu editor o en un reproductor como VLC."),
            ("¿Por qué la salida es MKV y no el formato original?",
             "Porque casi ninguno de estos contenedores admite audio FLAC. AVI, WMV, FLV, VOB y 3GP no lo contemplan, y en MP4 su soporte no es fiable. <strong>MKV</strong> sí lo admite de forma estándar, acepta prácticamente cualquier códec de vídeo y DaVinci Resolve lo importa sin problemas."),
            ("¿Puedo convertir el audio DTS de un TS o un M2TS?",
             "Sí. La pista DTS se decodifica y se codifica en FLAC, que es sin pérdida, de modo que el editor recibe exactamente el sonido que había decodificado. Si el archivo tiene varias pistas de audio, VidToFLAC convierte solo una, la que FFmpeg elige por defecto; para conservarlas todas, usa FFmpeg de escritorio: <code>ffmpeg -i entrada -map 0:v -map 0:a -c:v copy -c:a flac salida.mkv</code>."),
            ("¿Sirve para VOB de un DVD protegido contra copia?",
             "No. Si el VOB está cifrado con CSS no se puede procesar. Funciona con VOB sin cifrar, como los de DVD grabados en casa o los que ya has copiado de discos de los que tienes los derechos."),
            ("¿Hay un límite de tamaño?",
             "No imponemos ninguno, porque el archivo no sale de tu ordenador. El límite práctico lo pone la memoria de WebAssembly del navegador, unos 2 GB en total: vídeos de varias horas o archivos de más de 1-2 GB pueden no caber."),
        ],
        "formats":          VIDEO_FORMATS,
        "title":            "Convertir AVI, WebM, WMV, FLV y otros vídeos a FLAC | VidToFLAC",
        "description":      "Nueve formatos de vídeo —AVI, WebM, WMV, FLV, MPEG, TS, VOB, 3GP y M4V—: qué códec de audio llevan y cómo pasarlo a FLAC en tu propio navegador.",
        "keywords":         "convertir AVI a FLAC, convertir WebM a FLAC, WMV a FLAC, FLV a FLAC, VOB a FLAC, TS a FLAC, 3GP a FLAC, M4V a FLAC, MPEG a FLAC, DaVinci Resolve sin audio",
        "canonical":        "https://vidtoflac.tech/convertir-video-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-video-a-flac/",
        "og_title":         "Convertir AVI, WebM, WMV y otros vídeos a FLAC | VidToFLAC",
        "og_desc":          "Nueve formatos de vídeo y el códec de audio que hace fallar a cada uno en DaVinci Resolve. Pásalo a FLAC en tu navegador, sin subir nada.",
        "tw_title":         "Convertir AVI, WebM, WMV y otros vídeos a FLAC | VidToFLAC",
        "tw_desc":          "Nueve formatos de vídeo y el códec de audio que hace fallar a cada uno en DaVinci Resolve. Pásalo a FLAC en tu navegador.",
        "webapp_url":       "https://vidtoflac.tech/convertir-video-a-flac/",
        "webapp_desc":      "Convierte a FLAC el audio de vídeos AVI, WebM, WMV, FLV, MPEG, TS, VOB, 3GP y M4V dentro de un MKV, para que DaVinci Resolve, Premiere y Avid lo reproduzcan. Funciona en el navegador con FFmpeg (WebAssembly), sin subir archivos.",
        "howto_name":       "Cómo convertir a FLAC el audio de un AVI, WebM u otro vídeo para DaVinci Resolve",
        "hero_h1":          'Convierte el audio de <span class="accent">AVI, WebM, WMV y otros vídeos</span> a FLAC',
        "hero_sub":         "Nueve formatos de vídeo con el mismo síntoma: la imagen entra en DaVinci Resolve y el sonido no. Arrastra el archivo y VidToFLAC pasa su audio a FLAC en tu navegador, sin subir nada.",
        "seo_h2":           'Nueve formatos, <span class="accent">nueve motivos</span> para quedarte sin audio',
        "seo_lede":         'Un <strong>AVI</strong> de cámara antigua suele traer MP3 o AC-3; un <strong>WebM</strong> descargado, Opus o Vorbis; un <strong>VOB</strong> de DVD, AC-3 o MPEG; un <strong>WMV</strong>, WMA. Ninguno de esos códecs es de fiar en DaVinci Resolve, y en Linux fallan casi siempre. Más abajo tienes la guía de cada formato: qué lleva dentro, por qué falla y qué hace la herramienta con él.',
        "seo_body": (
            '      <h3>Qué hace VidToFLAC con cualquiera de estos vídeos</h3>\n'
            '      <p>El proceso es el mismo para los nueve: la herramienta lee el archivo, identifica sus códecs y genera un <strong>MKV</strong> con la pista de audio en <strong>FLAC</strong>, un formato sin pérdida que DaVinci Resolve, Premiere Pro y Avid decodifican de forma nativa.</p>\n\n'
            '      <p>Lo que cambia entre formatos es el vídeo. H.264, VP8, VP9, MPEG-4 (DivX, Xvid) y H.263 se copian sin recodificar, así que la imagen no pierde nada. MPEG-2 —el de los VOB, muchos MPEG y algunos TS—, WMV, VP6 y H.265/HEVC se recodifican a H.264 de alta calidad (<code>-crf 18</code>): tarda más, y el resultado es muy parecido al original pero no idéntico bit a bit.</p>\n\n'
            '      <p>Cuando el vídeo se copia pero el navegador no sabe decodificarlo, como pasa con DivX o H.263, la vista previa de la página puede quedarse sin imagen. El archivo descargado está completo igualmente.</p>'
        ),
        "breadcrumb_label": "Convertir vídeo a FLAC",
        "faq_h2":           "Preguntas frecuentes sobre convertir vídeo a FLAC",
        "index_title":      "Elige tu formato de vídeo",
        "index_intro":      'Cada formato tiene su guía más abajo. MP4, MKV y MOV, los más habituales, tienen página propia: <a href="/convertir-mp4-a-flac/">MP4</a>, <a href="/convertir-mkv-a-flac/">MKV</a> y <a href="/convertir-mov-a-flac/">MOV</a>. Si tu archivo es solo de audio, ve a <a href="/convertir-audio-a-flac/">convertir MP3, AAC, Opus y otros audios a FLAC</a>.',
    },
    {
        "slug":             "convertir-audio-a-flac",
        "hero_figure":      """      <figure class="fig">
        <img src="/media/capturas/vidtoflac-archivo-cargado.webp" width="1100" height="784" loading="lazy" decoding="async" alt="VidToFLAC en el navegador con un archivo cargado y las opciones de salida" />
        <figcaption>La conversión ocurre en el navegador: el archivo aparece cargado y nunca se sube a un servidor.</figcaption>
      </figure>""",
        "faqs":             [
            ("¿Convertir un MP3, un AAC o un Opus a FLAC mejora la calidad?",
             "No. Esos formatos descartan información al comprimir y ya no se puede recuperar. FLAC guarda exactamente lo que queda, así que el resultado suena igual que el original, ni mejor ni peor."),
            ("Entonces, ¿para qué sirve pasarlo a FLAC?",
             "Para dos cosas. La primera, compatibilidad: DaVinci Resolve, Premiere y Avid leen FLAC de forma nativa, y muchos de ellos no leen Opus, Vorbis o WMA, ni AAC y MP3 en Linux. La segunda, que al editar y exportar no sumes una segunda compresión con pérdida sobre la que ya tenía el archivo."),
            ("¿Cuánto más ocupa el FLAC?",
             "Bastante más que un formato con pérdida: un FLAC suele ocupar varias veces lo que un MP3 o un AAC de buena calidad, y todavía más frente a un Opus de voz. Frente a un AIFF o un WAV sin comprimir, en cambio, ocupa menos, normalmente entre la mitad y dos tercios, según el contenido."),
            ("¿Pierdo algo al pasar un AIFF a FLAC?",
             "No. Los dos son formatos sin pérdida, así que el audio es el mismo muestra a muestra, con su frecuencia de muestreo y su número de canales. Si el AIFF es de coma flotante, se convierte a enteros de 32 bits, porque FLAC no admite muestras en coma flotante."),
            ("¿Por qué no se importan mis grabaciones de Discord o mis notas de voz?",
             "Porque suelen estar en <strong>Opus</strong>, a veces dentro de un archivo .ogg. Opus es excelente para voz por internet, pero los editores de vídeo no lo decodifican de serie. Al pasarlo a FLAC se importa sin problemas."),
            ("Mi WMA funciona en Windows pero no en Mac ni en Linux, ¿por qué?",
             "WMA es un formato de Microsoft con poco soporte fuera de Windows, y DaVinci Resolve no lo decodifica en macOS ni en Linux. FLAC se lee en los tres sistemas."),
            ("¿Se suben mis archivos a algún servidor?",
             "No. La conversión se hace con FFmpeg compilado a WebAssembly dentro de tu navegador; el audio no sale de tu ordenador en ningún momento."),
        ],
        "formats":          AUDIO_FORMATS,
        "title":            "Convertir MP3, AAC, M4A, OGG, Opus, WMA y AIFF a FLAC | VidToFLAC",
        "description":      "Siete formatos de audio —MP3, AAC, M4A, AIFF, OGG, Opus y WMA—: por qué tu editor no los lee y qué ganas, y qué no, al pasarlos a FLAC.",
        "keywords":         "convertir MP3 a FLAC, convertir AAC a FLAC, M4A a FLAC, OGG a FLAC, Opus a FLAC, WMA a FLAC, AIFF a FLAC, audio a FLAC DaVinci Resolve",
        "canonical":        "https://vidtoflac.tech/convertir-audio-a-flac/",
        "og_url":           "https://vidtoflac.tech/convertir-audio-a-flac/",
        "og_title":         "Convertir MP3, AAC, Opus y otros audios a FLAC | VidToFLAC",
        "og_desc":          "Siete formatos de audio que los editores de vídeo leen mal o no leen. Pásalos a FLAC en tu navegador, sin subir nada.",
        "tw_title":         "Convertir MP3, AAC, Opus y otros audios a FLAC | VidToFLAC",
        "tw_desc":          "Siete formatos de audio que los editores de vídeo leen mal o no leen. Pásalos a FLAC en tu navegador.",
        "webapp_url":       "https://vidtoflac.tech/convertir-audio-a-flac/",
        "webapp_desc":      "Convierte archivos de audio MP3, AAC, M4A, AIFF, OGG, Opus y WMA a FLAC para que DaVinci Resolve, Premiere y Avid los importen. Funciona en el navegador con FFmpeg (WebAssembly), sin subir archivos.",
        "howto_name":       "Cómo convertir un MP3, AAC u otro archivo de audio a FLAC",
        "hero_h1":          'Convierte <span class="accent">MP3, AAC, Opus y otros audios</span> a FLAC',
        "hero_sub":         "Siete formatos de audio que DaVinci Resolve y otros editores leen mal o no leen. VidToFLAC los pasa a FLAC en tu navegador, sin subir nada.",
        "seo_h2":           '¿Por qué tu editor <span class="accent">no lee este archivo de audio</span>?',
        "seo_lede":         'Los archivos de audio sueltos fallan por lo mismo que los vídeos: el <strong>códec</strong>. MP3, AAC y M4A dependen de licencias que DaVinci Resolve no incluye en Linux; Opus, Vorbis (el de los OGG) y WMA no tienen soporte fiable en ninguna plataforma; y AIFF, aunque es sin pérdida, da problemas en algunas combinaciones. Más abajo tienes la guía de cada uno.',
        "seo_body": (
            '      <h3>Qué hace VidToFLAC con un archivo de audio</h3>\n'
            '      <p>Cuando el archivo no tiene vídeo, la salida es directamente un <strong>.flac</strong>, sin contenedor MKV. La herramienta decodifica el audio original y lo codifica en FLAC, un formato sin pérdida que DaVinci Resolve, Premiere Pro, Audacity y la mayoría de reproductores leen sin plugins.</p>\n\n'
            '      <p>Conviene tener clara una cosa: <strong>FLAC no recupera lo que el MP3, el AAC o el Opus descartaron al comprimir</strong>. El archivo resultante suena igual que el original y ocupa más. Lo que ganas es compatibilidad, y que las ediciones y exportaciones posteriores no sumen una segunda pérdida. Con AIFF, que ya es sin pérdida, el FLAC guarda exactamente el mismo audio en menos espacio.</p>'
        ),
        "breadcrumb_label": "Convertir audio a FLAC",
        "faq_h2":           "Preguntas frecuentes sobre convertir audio a FLAC",
        "index_title":      "Elige tu formato de audio",
        "index_intro":      'Cada formato tiene su guía más abajo. WAV tiene página propia: <a href="/convertir-wav-a-flac/">convertir WAV a FLAC</a>. Si lo que tienes es un vídeo, ve a <a href="/convertir-video-a-flac/">convertir AVI, WebM, WMV y otros vídeos a FLAC</a>.',
    },
]

MERGED_EN = [
    {
        "slug":             "convert-video-to-flac",
        "hero_figure":      """      <figure class="fig">
        <svg class="fig-svg" viewBox="0 0 660 262" width="660" height="262" role="img" aria-labelledby="t7617 d9084" xmlns="http://www.w3.org/2000/svg"><title id="t7617">Remux: the video is copied and only the audio is re-encoded</title><desc id="d9084">Diagram: the video track passes into the output MKV without re-encoding, while the AAC, MP3, AC-3 or Opus audio track is decoded and re-encoded as FLAC.</desc><text x="20" y="26" font-family="JetBrains Mono, ui-monospace, monospace" font-size="11" fill="#66666e">INPUT FILE</text><text x="640" y="26" text-anchor="end" font-family="JetBrains Mono, ui-monospace, monospace" font-size="11" fill="#66666e">OUTPUT FILE (MKV)</text><rect x="20" y="40" width="170" height="70" rx="8" fill="#131316" stroke="rgba(255,255,255,.14)"/><text x="105.0" y="64" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Video track</text><text x="105.0" y="84" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">H.264 · VP9 · MPEG-4</text><line x1="190" y1="75" x2="267" y2="75" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/><polygon points="275,75 267,71 267,79" fill="rgba(255,255,255,.28)"/><text x="232.5" y="66" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10" fill="#66666e">copied</text><rect x="275" y="40" width="150" height="70" rx="8" fill="rgba(25,195,125,.08)" stroke="#19c37d"/><text x="350.0" y="64" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Untouched</text><text x="350.0" y="84" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">0 re-encodes</text><line x1="425" y1="75" x2="482" y2="75" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/><polygon points="490,75 482,71 482,79" fill="rgba(255,255,255,.28)"/><rect x="490" y="40" width="150" height="70" rx="8" fill="rgba(25,195,125,.08)" stroke="#19c37d"/><text x="565.0" y="64" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Identical video</text><text x="565.0" y="84" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">same quality</text><rect x="20" y="135" width="170" height="70" rx="8" fill="rgba(255,96,88,.07)" stroke="#ff6058"/><text x="105.0" y="159" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Audio track</text><text x="105.0" y="179" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">AAC · MP3 · AC-3 · Opus</text><line x1="190" y1="170" x2="267" y2="170" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/><polygon points="275,170 267,166 267,174" fill="rgba(255,255,255,.28)"/><text x="232.5" y="161" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10" fill="#66666e">decoded</text><rect x="275" y="135" width="150" height="70" rx="8" fill="#131316" stroke="rgba(255,255,255,.14)"/><text x="350.0" y="159" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">Re-encoded</text><text x="350.0" y="179" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">to lossless FLAC</text><line x1="425" y1="170" x2="482" y2="170" stroke="rgba(255,255,255,.28)" stroke-width="1.5"/><polygon points="490,170 482,166 482,174" fill="rgba(255,255,255,.28)"/><rect x="490" y="135" width="150" height="70" rx="8" fill="rgba(25,195,125,.08)" stroke="#19c37d"/><text x="565.0" y="159" text-anchor="middle" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="14" font-weight="600" fill="#f3f3ef">FLAC audio</text><text x="565.0" y="179" text-anchor="middle" font-family="JetBrains Mono, ui-monospace, monospace" font-size="10.5" fill="#a7a7ad">the editor reads it</text><text x="20" y="228" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="12" fill="#a7a7ad">Exception: when the browser cannot decode the video</text><text x="20" y="245" font-family="Hanken Grotesk, system-ui, sans-serif" font-size="12" fill="#a7a7ad">(H.265/HEVC, MPEG-2, WMV, VP6), it is re-encoded to H.264 too.</text></svg>
        <figcaption>What gets copied and what gets re-encoded in each of these nine video formats.</figcaption>
      </figure>""",
        "faqs":             [
            ("Why does an AVI, WebM or VOB import into DaVinci Resolve with no sound?",
             "Because of the audio codec, which differs from format to format: old AVI files usually carry <strong>MP3 or AC-3</strong>; WebM, <strong>Opus or Vorbis</strong>; VOB and MPEG, <strong>AC-3 or MPEG Audio</strong>; WMV, <strong>WMA</strong>; broadcast TS, <strong>AC-3 or AAC</strong>; and old phone 3GP files, <strong>AMR</strong>. DaVinci Resolve decodes none of them reliably, least of all on Linux, so you see the picture while the audio track stays empty."),
            ("Is the video re-encoded during conversion?",
             "It depends on the codec, not the file extension. H.264, VP8, VP9, MPEG-4 (DivX, Xvid) and H.263 are copied without re-encoding. MPEG-2, WMV, VP6 and H.265/HEVC are re-encoded to high-quality H.264 (<code>-crf 18</code>), which takes longer and does not leave the video bit-for-bit identical, although the difference is not visible to the eye."),
            ("The page preview shows no picture for my AVI or 3GP. Did it fail?",
             "Not necessarily. If the video is DivX, Xvid or H.263, VidToFLAC copies it into the MKV as it is, but the browser cannot decode those codecs to display them. The downloaded file is complete; check it by opening it in your editor or in a player such as VLC."),
            ("Why is the output an MKV rather than the original format?",
             "Because hardly any of these containers accept FLAC audio. AVI, WMV, FLV, VOB and 3GP do not allow for it, and in MP4 support is unreliable. <strong>MKV</strong> supports it as standard, takes almost any video codec, and DaVinci Resolve imports it without trouble."),
            ("Can I convert the DTS audio in a TS or M2TS file?",
             "Yes. The DTS track is decoded and encoded as FLAC, which is lossless, so the editor receives exactly the sound that was decoded. If the file has several audio tracks, VidToFLAC converts only one, the track FFmpeg picks by default; to keep them all, use desktop FFmpeg: <code>ffmpeg -i input -map 0:v -map 0:a -c:v copy -c:a flac output.mkv</code>."),
            ("Does it work with VOB files from a copy-protected DVD?",
             "No. A VOB encrypted with CSS cannot be processed. It works with unencrypted VOB files, such as home-recorded DVDs or files you have already copied from discs you hold the rights to."),
            ("Is there a size limit?",
             "We impose none, because the file never leaves your computer. The practical limit is the browser WebAssembly memory, about 2 GB in total: videos several hours long or files over 1 to 2 GB may not fit."),
        ],
        "formats":          VIDEO_FORMATS,
        "title":            "Convert AVI, WebM, WMV, FLV and Other Video to FLAC | VidToFLAC",
        "description":      "Nine video formats (AVI, WebM, WMV, FLV, MPEG, TS, VOB, 3GP, M4V): which audio codec each carries and how to turn it into FLAC in your browser.",
        "keywords":         "convert AVI to FLAC, convert WebM to FLAC, WMV to FLAC, FLV to FLAC, VOB to FLAC, TS to FLAC, 3GP to FLAC, M4V to FLAC, MPEG to FLAC, DaVinci Resolve no audio",
        "canonical":        "https://vidtoflac.tech/en/convert-video-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-video-to-flac/",
        "og_title":         "Convert AVI, WebM, WMV and Other Video to FLAC | VidToFLAC",
        "og_desc":          "Nine video formats and the audio codec that makes each one fail in DaVinci Resolve. Turn it into FLAC in your browser, nothing uploaded.",
        "tw_title":         "Convert AVI, WebM, WMV and Other Video to FLAC | VidToFLAC",
        "tw_desc":          "Nine video formats and the audio codec that makes each one fail in DaVinci Resolve. Turn it into FLAC in your browser.",
        "webapp_url":       "https://vidtoflac.tech/en/convert-video-to-flac/",
        "webapp_desc":      "Converts the audio of AVI, WebM, WMV, FLV, MPEG, TS, VOB, 3GP and M4V videos to FLAC inside an MKV, so DaVinci Resolve, Premiere and Avid can play it. Runs in the browser with FFmpeg (WebAssembly), with no uploads.",
        "howto_name":       "How to convert the audio of an AVI, WebM or other video to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert the audio of <span class="accent">AVI, WebM, WMV and other video</span> to FLAC',
        "hero_sub":         "Nine video formats with the same symptom: the picture makes it into DaVinci Resolve and the sound does not. Drop the file in and VidToFLAC turns its audio into FLAC in your browser, nothing uploaded.",
        "seo_h2":           'Nine formats, <span class="accent">nine ways</span> to end up with no audio',
        "seo_lede":         'An old camcorder <strong>AVI</strong> usually carries MP3 or AC-3; a downloaded <strong>WebM</strong>, Opus or Vorbis; a DVD <strong>VOB</strong>, AC-3 or MPEG audio; a <strong>WMV</strong>, WMA. None of those codecs is dependable in DaVinci Resolve, and on Linux they nearly always fail. Below is a guide to each format: what is inside, why it fails and what the tool does with it.',
        "seo_body": (
            '      <h3>What VidToFLAC does with any of these videos</h3>\n'
            '      <p>The process is the same for all nine: the tool reads the file, identifies its codecs and writes an <strong>MKV</strong> with the audio track in <strong>FLAC</strong>, a lossless format that DaVinci Resolve, Premiere Pro and Avid decode natively.</p>\n\n'
            '      <p>What changes from one format to the next is the video. H.264, VP8, VP9, MPEG-4 (DivX, Xvid) and H.263 are copied without re-encoding, so the picture loses nothing. MPEG-2 (found in VOB files, many MPEG files and some TS files), WMV, VP6 and H.265/HEVC are re-encoded to high-quality H.264 (<code>-crf 18</code>): it takes longer, and the result is very close to the original but not bit-for-bit identical.</p>\n\n'
            '      <p>When the video is copied but the browser cannot decode it, as with DivX or H.263, the page preview may show no picture. The downloaded file is complete all the same.</p>'
        ),
        "breadcrumb_label": "Convert video to FLAC",
        "faq_h2":           "Common questions about converting video to FLAC",
        "index_title":      "Pick your video format",
        "index_intro":      'Each format has its own guide below. MP4, MKV and MOV, the most common ones, have pages of their own: <a href="/en/convert-mp4-to-flac/">MP4</a>, <a href="/en/convert-mkv-to-flac/">MKV</a> and <a href="/en/convert-mov-to-flac/">MOV</a>. If your file is audio only, go to <a href="/en/convert-audio-to-flac/">convert MP3, AAC, Opus and other audio to FLAC</a>.',
    },
    {
        "slug":             "convert-audio-to-flac",
        "hero_figure":      """      <figure class="fig">
        <img src="/media/capturas/vidtoflac-archivo-cargado.webp" width="1100" height="784" loading="lazy" decoding="async" alt="VidToFLAC in a browser with a file loaded and the output options" />
        <figcaption>The conversion happens in the browser: the file shows up loaded and is never uploaded to a server.</figcaption>
      </figure>""",
        "faqs":             [
            ("Does converting an MP3, AAC or Opus file to FLAC improve the quality?",
             "No. Those formats throw information away when they compress, and it cannot be brought back. FLAC stores exactly what is left, so the result sounds the same as the original, no better and no worse."),
            ("So what is the point of converting to FLAC?",
             "Two things. First, compatibility: DaVinci Resolve, Premiere and Avid read FLAC natively, and many of them do not read Opus, Vorbis or WMA, nor AAC and MP3 on Linux. Second, it keeps edits and exports from stacking a second lossy compression on top of the one the file already had."),
            ("How much bigger is the FLAC file?",
             "Considerably bigger than a lossy format: a FLAC file is usually several times the size of a good-quality MP3 or AAC, and larger still next to a speech Opus file. Next to an uncompressed AIFF or WAV, though, it is smaller, typically between half and two thirds of the size, depending on the material."),
            ("Do I lose anything converting AIFF to FLAC?",
             "No. Both are lossless formats, so the audio is identical sample for sample, with the same sample rate and channel count. If the AIFF uses floating-point samples, they are converted to 32-bit integers, because FLAC does not support floating point."),
            ("Why will my Discord recordings or voice notes not import?",
             "Because they are usually <strong>Opus</strong>, sometimes inside an .ogg file. Opus is excellent for voice over the internet, but video editors do not decode it out of the box. Converted to FLAC, it imports without trouble."),
            ("My WMA plays on Windows but not on Mac or Linux. Why?",
             "WMA is a Microsoft format with little support outside Windows, and DaVinci Resolve does not decode it on macOS or Linux. FLAC is read on all three."),
            ("Are my files uploaded to a server?",
             "No. The conversion runs with FFmpeg compiled to WebAssembly inside your browser; the audio never leaves your computer."),
        ],
        "formats":          AUDIO_FORMATS,
        "title":            "Convert MP3, AAC, M4A, OGG, Opus, WMA and AIFF to FLAC | VidToFLAC",
        "description":      "Seven audio formats (MP3, AAC, M4A, AIFF, OGG, Opus, WMA): why your editor will not read them, and what you do and do not gain from FLAC.",
        "keywords":         "convert MP3 to FLAC, convert AAC to FLAC, M4A to FLAC, OGG to FLAC, Opus to FLAC, WMA to FLAC, AIFF to FLAC, audio to FLAC DaVinci Resolve",
        "canonical":        "https://vidtoflac.tech/en/convert-audio-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-audio-to-flac/",
        "og_title":         "Convert MP3, AAC, Opus and Other Audio to FLAC | VidToFLAC",
        "og_desc":          "Seven audio formats that video editors read badly or not at all. Turn them into FLAC in your browser, nothing uploaded.",
        "tw_title":         "Convert MP3, AAC, Opus and Other Audio to FLAC | VidToFLAC",
        "tw_desc":          "Seven audio formats that video editors read badly or not at all. Turn them into FLAC in your browser.",
        "webapp_url":       "https://vidtoflac.tech/en/convert-audio-to-flac/",
        "webapp_desc":      "Converts MP3, AAC, M4A, AIFF, OGG, Opus and WMA audio files to FLAC so DaVinci Resolve, Premiere and Avid can import them. Runs in the browser with FFmpeg (WebAssembly), with no uploads.",
        "howto_name":       "How to convert an MP3, AAC or other audio file to FLAC",
        "hero_h1":          'Convert <span class="accent">MP3, AAC, Opus and other audio</span> to FLAC',
        "hero_sub":         "Seven audio formats that DaVinci Resolve and other editors read badly or not at all. VidToFLAC turns them into FLAC in your browser, nothing uploaded.",
        "seo_h2":           'Why will your editor <span class="accent">not read this audio file</span>?',
        "seo_lede":         'Standalone audio files fail for the same reason videos do: the <strong>codec</strong>. MP3, AAC and M4A depend on licences DaVinci Resolve does not ship on Linux; Opus, Vorbis (the codec inside OGG files) and WMA have no dependable support on any platform; and AIFF, lossless as it is, causes trouble in some combinations. Below is a guide to each one.',
        "seo_body": (
            '      <h3>What VidToFLAC does with an audio file</h3>\n'
            '      <p>When the file has no video, the output is a plain <strong>.flac</strong>, with no MKV container. The tool decodes the original audio and encodes it as FLAC, a lossless format that DaVinci Resolve, Premiere Pro, Audacity and most players read without plugins.</p>\n\n'
            '      <p>One thing is worth being clear about: <strong>FLAC does not bring back what MP3, AAC or Opus threw away when they compressed the audio</strong>. The resulting file sounds the same as the original and takes more space. What you gain is compatibility, and the fact that later edits and exports do not add a second loss. With AIFF, which is already lossless, the FLAC keeps exactly the same audio in less space.</p>'
        ),
        "breadcrumb_label": "Convert audio to FLAC",
        "faq_h2":           "Common questions about converting audio to FLAC",
        "index_title":      "Pick your audio format",
        "index_intro":      'Each format has its own guide below. WAV has a page of its own: <a href="/en/convert-wav-to-flac/">convert WAV to FLAC</a>. If what you have is a video, go to <a href="/en/convert-video-to-flac/">convert AVI, WebM, WMV and other video to FLAC</a>.',
    },
]
