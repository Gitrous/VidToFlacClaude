# -*- coding: utf-8 -*-
"""
landing_content.py — contenido único por formato para las landings SEO.

Lo consume build_pages.py para reemplazar, en cada página convertir-*-a-flac,
la sección "La solución", la FAQ visible y el JSON-LD FAQPage, evitando así el
contenido duplicado entre páginas (requisito de calidad de Google AdSense).

Cada entrada:
  faq_h2   → encabezado de la sección de preguntas (único por formato)
  seo_body → bloque que sustituye a "La solución" (empieza por <h3>)
  faqs     → lista de (pregunta, respuesta) específicas del formato
"""

CONTENT = {

    # ── MP4 ──────────────────────────────────────────────────────────────────
    "convertir-mp4-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir MP4 a FLAC",
        "seo_body": (
            '      <h3>La solución para tus MP4: remux a MKV con audio FLAC</h3>\n'
            '      <p>El truco está en separar el problema: el <strong>vídeo</strong> de tu MP4 (normalmente H.264 o H.265) casi siempre es perfectamente compatible; lo que DaVinci Resolve no digiere es el <strong>audio AAC o MP3</strong>. VidToFLAC reempaqueta el MP4 en un contenedor <strong>MKV</strong> copiando el vídeo <strong>bit a bit</strong> y recodificando únicamente la pista de audio a <strong>FLAC</strong> sin pérdida.</p>\n\n'
            '      <p>Como el vídeo no se vuelve a comprimir, no hay pérdida de calidad ni esperas largas: un MP4 de varios gigabytes se procesa en segundos. El MKV resultante se importa con sonido en DaVinci Resolve, Premiere Pro y Avid, sin instalar códecs ni plugins.</p>\n\n'
            '      <p>Si tu MP4 incluye un vídeo que el navegador no puede decodificar (por ejemplo HEVC/H.265 en algunos equipos), VidToFLAC lo recodifica a H.264 para que la previsualización funcione; en cualquier otro caso, el vídeo se conserva intacto.</p>'
        ),
        "faqs": [
            ("¿Pierdo calidad de vídeo al convertir un MP4 a FLAC?",
             "No. El flujo de vídeo del MP4 se copia <strong>bit a bit</strong> sin recomprimirlo: es un remux, no un re-encode. Solo la pista de audio pasa a FLAC, que es un formato sin pérdida, así que la imagen final es idéntica al original."),
            ("¿Por qué DaVinci Resolve abre mi MP4 pero sin sonido?",
             "Porque el MP4 lleva el audio en <strong>AAC o MP3</strong>, y la versión gratuita de DaVinci Resolve —sobre todo en Linux— no incluye las licencias para decodificar esos códecs. Al pasar el audio a FLAC dentro de un MKV, Resolve lo reproduce de forma nativa."),
            ("¿Sirve para los MP4 grabados con OBS Studio o con el móvil?",
             "Sí. Los MP4 de OBS, smartphones, cámaras y capturadoras usan precisamente audio AAC, que es el origen del problema. VidToFLAC los reempaqueta sin tocar el vídeo y recupera el audio compatible."),
            ("¿Funciona con MP4 en H.265 (HEVC)?",
             "Sí. El audio se convierte a FLAC igualmente. Si tu navegador no puede decodificar el vídeo HEVC para la previsualización en la página, VidToFLAC lo recodifica a H.264; el archivo descargado sigue siendo válido para editar."),
            ("¿Cuánto tarda en convertirse un MP4 grande?",
             "Muy poco. Al ser un remux (no se re-renderiza el vídeo) el tiempo depende sobre todo de leer y escribir el archivo, no de su duración. Un MP4 de varios GB suele estar listo en segundos, y todo ocurre en tu equipo sin subidas."),
        ],
    },

    # ── MKV ──────────────────────────────────────────────────────────────────
    "convertir-mkv-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir MKV a FLAC",
        "seo_body": (
            '      <h3>La solución para tus MKV: cambiar solo el audio a FLAC</h3>\n'
            '      <p>El contenedor <strong>MKV</strong> (Matroska) acepta casi cualquier códec, y ahí está la trampa: muchos MKV de <strong>OBS Studio</strong>, grabaciones de pantalla o cámaras guardan el audio en <strong>Opus, AAC, MP3 o Vorbis</strong>, formatos que DaVinci Resolve no decodifica de serie. VidToFLAC mantiene el MKV, copia el vídeo <strong>bit a bit</strong> y recodifica únicamente el audio a <strong>FLAC</strong>.</p>\n\n'
            '      <p>Como el MKV ya es el contenedor de salida, no hay cambio de formato del vídeo ni recompresión: el proceso es prácticamente instantáneo y la calidad de imagen permanece intacta. El resultado se importa con sonido en cualquier editor profesional.</p>\n\n'
            '      <p>FLAC es la opción ideal aquí porque MKV lo admite de forma estándar y DaVinci Resolve lo reproduce de forma nativa, sin licencias de pago ni decodificadores externos.</p>'
        ),
        "faqs": [
            ("¿Tengo que recodificar el vídeo de mi MKV?",
             "No. El vídeo se copia <strong>bit a bit</strong> dentro del mismo contenedor MKV; solo se transforma la pista de audio a FLAC. La calidad de imagen es exactamente la del archivo original."),
            ("Mi grabación MKV de OBS no tiene sonido en DaVinci Resolve, ¿por qué?",
             "OBS suele grabar el audio en <strong>AAC</strong> (o a veces Opus), y DaVinci Resolve —especialmente en Linux— no incluye su decodificador. Convertir ese audio a FLAC dentro del MKV soluciona el problema al instante."),
            ("¿Por qué la salida sigue siendo MKV y no MP4?",
             "Porque el contenedor MKV admite audio <strong>FLAC</strong> de forma estándar, mientras que MP4 no lo hace de manera fiable. MKV es además el formato que mejor manejan DaVinci Resolve, Premiere y Avid para este flujo de trabajo."),
            ("¿Funciona con MKV de grabaciones de pantalla o gameplay?",
             "Sí. Tanto si el MKV viene de OBS, de un capturador o de una descarga, VidToFLAC reempaqueta el vídeo sin tocarlo y deja el audio en FLAC listo para editar."),
            ("¿Hay límite de tamaño para un MKV?",
             "No imponemos ninguno: el procesamiento ocurre en tu propio ordenador con FFmpeg (WebAssembly) y no se sube nada a ningún servidor. El único límite práctico es la memoria disponible en tu equipo."),
        ],
    },

    # ── MOV ──────────────────────────────────────────────────────────────────
    "convertir-mov-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir MOV a FLAC",
        "seo_body": (
            '      <h3>La solución para tus MOV de iPhone, GoPro o cámara</h3>\n'
            '      <p>Los <strong>MOV</strong> de iPhone, GoPro y la mayoría de cámaras guardan el audio en <strong>AAC</strong>, el códec que DaVinci Resolve no decodifica sin licencia. VidToFLAC reempaqueta el MOV en un <strong>MKV</strong>, copia el vídeo <strong>bit a bit</strong> y convierte solo el audio a <strong>FLAC</strong> sin pérdida.</p>\n\n'
            '      <p>Para grabaciones normales de iPhone o GoPro (vídeo H.264/HEVC) el proceso es un remux instantáneo. La calidad de imagen no se toca y el sonido vuelve a estar disponible en tu editor.</p>\n\n'
            '      <p>Caso especial: si el MOV contiene <strong>ProRes</strong> —habitual en flujos profesionales—, el navegador no puede decodificarlo para previsualizar, así que VidToFLAC recodifica el vídeo a H.264 manteniendo el audio en FLAC.</p>'
        ),
        "faqs": [
            ("¿Perderé calidad al convertir un MOV de iPhone?",
             "No, si el vídeo es H.264 o HEVC: se copia <strong>bit a bit</strong> y solo el audio pasa a FLAC sin pérdida. La grabación de tu iPhone queda idéntica."),
            ("Mi MOV de GoPro entra en Resolve sin audio, ¿por qué?",
             "Las GoPro graban el audio en <strong>AAC</strong>, que DaVinci Resolve no decodifica de serie —sobre todo en Linux—. Pasar ese audio a FLAC dentro de un MKV restaura el sonido."),
            ("¿Qué pasa si mi MOV es ProRes?",
             "ProRes no se puede decodificar en el navegador, así que VidToFLAC recodifica el vídeo a H.264 para que la previsualización funcione y deja el audio en FLAC. Para masters ProRes intactos conviene usar FFmpeg de escritorio."),
            ("¿Vale para vídeos grabados con cámaras Canon, Sony o Nikon en MOV?",
             "Sí. La mayoría usan audio AAC dentro del MOV, exactamente el caso que VidToFLAC resuelve reempaquetando a MKV con audio FLAC."),
            ("¿Se sube mi MOV a algún servidor?",
             "Nunca. Todo se procesa localmente en tu navegador con FFmpeg compilado a WebAssembly; el archivo no sale de tu dispositivo en ningún momento."),
        ],
    },

    # ── AVI ──────────────────────────────────────────────────────────────────
    "convertir-avi-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir AVI a FLAC",
        "seo_body": (
            '      <h3>La solución para tus AVI: audio compatible sin tocar el vídeo</h3>\n'
            '      <p>Los <strong>AVI</strong> de cámaras antiguas, grabadoras y software de captura suelen llevar el audio en <strong>MP3 o AC3</strong>, formatos que DaVinci Resolve no decodifica sin licencias adicionales. VidToFLAC reempaqueta el AVI en un <strong>MKV</strong> y convierte únicamente esa pista de audio a <strong>FLAC</strong>.</p>\n\n'
            '      <p>Siempre que el navegador pueda decodificar el vídeo, este se copia <strong>bit a bit</strong> sin pérdida. El resultado es un MKV que se importa con sonido en cualquier editor profesional moderno.</p>\n\n'
            '      <p>Si el AVI usa un códec de vídeo antiguo que el navegador no soporta, VidToFLAC lo recodifica automáticamente a H.264 para garantizar que el clip se vea correctamente.</p>'
        ),
        "faqs": [
            ("¿Por qué mi AVI no tiene audio en DaVinci Resolve?",
             "Los AVI suelen guardar el audio en <strong>MP3 o AC3</strong>, códecs que Resolve no decodifica sin licencias —especialmente en Linux—. Convertirlo a FLAC dentro de un MKV soluciona la falta de sonido."),
            ("¿Se conserva la calidad del vídeo del AVI?",
             "Si el navegador puede decodificar el vídeo, se copia <strong>bit a bit</strong> sin recomprimir. Solo el audio cambia a FLAC, que es sin pérdida."),
            ("Tengo AVI muy antiguos de una cámara, ¿funcionarán?",
             "Sí. Si el códec de vídeo es demasiado antiguo para el navegador, VidToFLAC lo recodifica a H.264 automáticamente y deja el audio en FLAC, de modo que el clip se importe con imagen y sonido."),
            ("¿Puedo convertir varios AVI a la vez?",
             "Sí. Puedes añadir varios archivos y se procesan de uno en uno dentro de tu navegador, sin subir nada a ningún servidor."),
            ("¿Es gratis convertir AVI a FLAC?",
             "Sí, totalmente gratis y sin registro. El procesamiento ocurre en tu propio equipo con FFmpeg (WebAssembly)."),
        ],
    },

    # ── WEBM ─────────────────────────────────────────────────────────────────
    "convertir-webm-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir WebM a FLAC",
        "seo_body": (
            '      <h3>La solución para tus WebM: de Opus/Vorbis a FLAC</h3>\n'
            '      <p>Los <strong>WebM</strong> descargados de YouTube o generados por grabadores de navegador llevan el audio en <strong>Opus o Vorbis</strong>, dos códecs que DaVinci Resolve no decodifica de serie. VidToFLAC reempaqueta el WebM en un <strong>MKV</strong> y convierte solo el audio a <strong>FLAC</strong> sin pérdida.</p>\n\n'
            '      <p>El vídeo (normalmente VP8 o VP9) se copia <strong>bit a bit</strong> siempre que el navegador pueda manejarlo, sin recompresión ni pérdida de calidad. El MKV resultante se importa con sonido en cualquier editor profesional.</p>\n\n'
            '      <p>Si el vídeo no se puede decodificar en el navegador, VidToFLAC lo recodifica a H.264 para asegurar una previsualización correcta.</p>'
        ),
        "faqs": [
            ("¿Por qué mi WebM de YouTube no tiene audio en el editor?",
             "Los WebM usan audio <strong>Opus o Vorbis</strong>, que DaVinci Resolve no decodifica sin más. Pasar ese audio a FLAC dentro de un MKV lo hace compatible al instante."),
            ("¿Pierdo calidad al convertir WebM a FLAC?",
             "No en el audio: FLAC es sin pérdida. El vídeo VP8/VP9 se copia <strong>bit a bit</strong> cuando el navegador puede decodificarlo, conservando la calidad original."),
            ("¿Sirve para grabaciones hechas con extensiones del navegador?",
             "Sí. Muchos grabadores de pantalla web exportan WebM con audio Opus; VidToFLAC los reempaqueta a MKV con audio FLAC listo para editar."),
            ("¿Puedo extraer solo el audio del WebM?",
             "Si el archivo es solo de audio, la salida será un FLAC. Si tiene vídeo, obtienes un MKV con el vídeo intacto y el audio en FLAC sincronizado."),
            ("¿Se suben mis WebM a la nube?",
             "No. Todo el proceso ocurre localmente en tu navegador mediante WebAssembly; tus archivos no salen del equipo."),
        ],
    },

    # ── WMV ──────────────────────────────────────────────────────────────────
    "convertir-wmv-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir WMV a FLAC",
        "seo_body": (
            '      <h3>La solución para tus WMV: salir del ecosistema Windows Media</h3>\n'
            '      <p>Los <strong>WMV (Windows Media Video)</strong> usan el códec de audio propietario <strong>WMA</strong> de Microsoft, que DaVinci Resolve no decodifica —sobre todo en Linux y macOS—. VidToFLAC convierte ese audio a <strong>FLAC</strong>, un formato abierto y sin pérdida, dentro de un contenedor <strong>MKV</strong>.</p>\n\n'
            '      <p>Como el vídeo de los WMV (VC-1 / WMV3) tampoco es decodificable en el navegador, VidToFLAC lo recodifica a <strong>H.264</strong> para que el clip se importe y se previsualice correctamente, mientras el audio queda en FLAC.</p>\n\n'
            '      <p>El resultado es un archivo estándar y multiplataforma que cualquier editor profesional moderno reproduce sin depender de los códecs propietarios de Windows.</p>'
        ),
        "faqs": [
            ("¿Por qué DaVinci Resolve no abre el audio de mi WMV?",
             "Porque el WMV lleva audio <strong>WMA</strong>, un códec propietario de Microsoft que Resolve no incluye en Linux ni macOS. Convertirlo a FLAC elimina esa dependencia."),
            ("¿El vídeo del WMV se recodifica?",
             "Sí. El vídeo VC-1/WMV3 no se puede decodificar en el navegador, así que se recodifica a <strong>H.264</strong>. Es la única forma de que el clip sea editable fuera del ecosistema Windows Media."),
            ("¿Sirve para vídeos antiguos grabados en Windows?",
             "Sí. Los WMV de grabadoras o software antiguo de Windows son justo el caso que VidToFLAC resuelve, dejando un MKV con vídeo H.264 y audio FLAC."),
            ("¿Funciona en Mac y Linux?",
             "Sí. Al ejecutarse en el navegador, VidToFLAC funciona igual en Windows, macOS y Linux, y el archivo de salida es compatible con todos ellos."),
            ("¿Tiene coste convertir WMV a FLAC?",
             "Ninguno. Es gratuito, sin registro y sin subir archivos: todo el trabajo lo hace FFmpeg dentro de tu navegador."),
        ],
    },

    # ── FLV ──────────────────────────────────────────────────────────────────
    "convertir-flv-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir FLV a FLAC",
        "seo_body": (
            '      <h3>La solución para tus FLV: rescatar audio y vídeo del formato Flash</h3>\n'
            '      <p>Los <strong>FLV (Flash Video)</strong> —el formato de YouTube hasta 2015 y de muchas webs antiguas— llevan audio en <strong>MP3 o AAC</strong> y vídeo en códecs como H.263 o VP6. DaVinci Resolve no decodifica esas pistas de serie. VidToFLAC convierte el audio a <strong>FLAC</strong> dentro de un <strong>MKV</strong>.</p>\n\n'
            '      <p>Si el vídeo está en un códec moderno que el navegador entiende, se copia <strong>bit a bit</strong>; si es un códec Flash heredado (VP6, H.263) que no se puede decodificar, VidToFLAC lo recodifica a <strong>H.264</strong>.</p>\n\n'
            '      <p>Así, un archivo Flash obsoleto se transforma en un MKV moderno que cualquier editor importa con imagen y sonido.</p>'
        ),
        "faqs": [
            ("¿Por qué mi FLV no se importa bien en el editor?",
             "Los FLV usan códecs Flash heredados (H.263, VP6) y audio MP3/AAC que los editores modernos no manejan bien. VidToFLAC los convierte a un MKV con vídeo H.264 (si hace falta) y audio FLAC."),
            ("¿Se recodifica siempre el vídeo de un FLV?",
             "Solo si su códec no se puede decodificar en el navegador. Cuando es posible, el vídeo se copia <strong>bit a bit</strong>; si no, se recodifica a H.264 para garantizar compatibilidad."),
            ("Tengo FLV descargados de webs antiguas, ¿servirán?",
             "Sí. Es justo el escenario para el que es útil: VidToFLAC los moderniza a MKV con audio FLAC listo para editar o archivar."),
            ("¿Puedo quedarme solo con el audio del FLV?",
             "Si el FLV solo tiene audio, obtendrás un FLAC. Si tiene vídeo, el resultado es un MKV con el audio en FLAC sincronizado con la imagen."),
            ("¿Es seguro subir mis FLV aquí?",
             "No hay ninguna subida: el procesamiento es 100% local en tu navegador. Tus archivos nunca salen de tu equipo."),
        ],
    },

    # ── VOB ──────────────────────────────────────────────────────────────────
    "convertir-vob-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir VOB a FLAC",
        "seo_body": (
            '      <h3>La solución para tus VOB de DVD: AC3/DTS fuera, FLAC dentro</h3>\n'
            '      <p>Los <strong>VOB</strong> de copias de DVD guardan el audio en <strong>AC3 (Dolby Digital) o DTS</strong> y el vídeo en <strong>MPEG-2</strong>. Ninguno de los dos es decodificable sin licencias en DaVinci Resolve. VidToFLAC convierte el audio a <strong>FLAC</strong> y recodifica el vídeo MPEG-2 a <strong>H.264</strong> dentro de un <strong>MKV</strong>.</p>\n\n'
            '      <p>De este modo, el material de un DVD que no se importaba con sonido queda listo para editar en cualquier programa profesional moderno, sin pasar por códecs de pago.</p>\n\n'
            '      <p>Recuerda conservar siempre una copia del VOB original antes de convertir, como con cualquier flujo de digitalización.</p>'
        ),
        "faqs": [
            ("¿Por qué los VOB de DVD entran sin audio en Resolve?",
             "Porque su audio está en <strong>AC3 o DTS</strong>, formatos con licencia que DaVinci Resolve no decodifica de serie —menos aún en Linux—. Convertirlo a FLAC elimina ese obstáculo."),
            ("¿El vídeo MPEG-2 del DVD se recodifica?",
             "Sí. El vídeo MPEG-2 no se decodifica en el navegador, así que se recodifica a <strong>H.264</strong>. El audio se pasa a FLAC y todo queda en un MKV editable."),
            ("¿Puedo unir varios VOB de un mismo DVD?",
             "VidToFLAC procesa cada archivo por separado. Para un DVD partido en varios VOB, conviértelos y únelos después en tu editor de vídeo."),
            ("¿Convierte VOB protegidos contra copia?",
             "No. Si el VOB tiene protección anticopia (CSS) no podrá procesarse; solo funciona con archivos VOB sin cifrar de los que tengas los derechos."),
            ("¿Se sube el VOB a algún servidor?",
             "No. Todo el proceso ocurre en tu navegador con FFmpeg (WebAssembly); el archivo no abandona tu equipo."),
        ],
    },

    # ── TS / M2TS ──────────────────────────────────────────────────────────────
    "convertir-ts-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir TS y M2TS a FLAC",
        "seo_body": (
            '      <h3>La solución para tus TS y M2TS: grabaciones de TV y Blu-ray editables</h3>\n'
            '      <p>Los <strong>TS y M2TS</strong> —el formato de grabaciones de TDT, sintonizadores de TV y discos Blu-ray— llevan audio en <strong>AC3, AAC o DTS</strong>. DaVinci Resolve no decodifica esos formatos sin licencias. VidToFLAC convierte el audio a <strong>FLAC</strong> dentro de un <strong>MKV</strong>.</p>\n\n'
            '      <p>El vídeo suele ser H.264 o MPEG-2: si el navegador puede decodificarlo, se copia <strong>bit a bit</strong>; si es MPEG-2 no soportado, se recodifica a H.264. En ambos casos recuperas el sonido en tu editor.</p>\n\n'
            '      <p>Es la forma directa de aprovechar grabaciones de televisión o capturas Blu-ray que de otro modo entrarían mudas en la línea de tiempo.</p>'
        ),
        "faqs": [
            ("¿Por qué mi grabación TS de la TDT no tiene sonido en Resolve?",
             "Las grabaciones de TDT usan audio <strong>AC3 o AAC</strong>, que DaVinci Resolve no decodifica sin licencias. Convertir ese audio a FLAC dentro de un MKV soluciona el problema."),
            ("¿Funciona con archivos M2TS de Blu-ray o de videocámaras AVCHD?",
             "Sí. Los M2TS de Blu-ray y de cámaras AVCHD llevan audio AC3/DTS; VidToFLAC los reempaqueta a MKV y pasa el audio a FLAC compatible."),
            ("¿Se conserva la calidad del vídeo?",
             "Si el vídeo es H.264, se copia <strong>bit a bit</strong> sin pérdida. Si es MPEG-2 no decodificable en el navegador, se recodifica a H.264 para garantizar compatibilidad."),
            ("¿Puedo convertir audio DTS a FLAC?",
             "Sí. El audio DTS de la pista se decodifica y se vuelve a codificar a FLAC sin pérdida, de modo que sea reproducible en editores que no admiten DTS."),
            ("¿Hay límite de tamaño para grabaciones largas?",
             "No imponemos límite de servidor porque nada se sube. El tope práctico lo marca la memoria de tu equipo al procesar archivos muy grandes."),
        ],
    },

    # ── M4V ──────────────────────────────────────────────────────────────────
    "convertir-m4v-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir M4V a FLAC",
        "seo_body": (
            '      <h3>La solución para tus M4V de iTunes y Apple TV</h3>\n'
            '      <p>Los <strong>M4V</strong> son contenedores MPEG-4 de Apple con audio <strong>AAC</strong>. DaVinci Resolve no decodifica AAC de serie —sobre todo en Linux—, así que el clip entra sin sonido. VidToFLAC reempaqueta el M4V en un <strong>MKV</strong>, copia el vídeo <strong>bit a bit</strong> y convierte el audio a <strong>FLAC</strong>.</p>\n\n'
            '      <p>Para grabaciones propias (vídeo H.264/HEVC) es un remux instantáneo sin pérdida de calidad. El sonido vuelve a estar disponible en cualquier editor profesional.</p>\n\n'
            '      <p>Importante: los M4V comprados en la iTunes Store suelen tener <strong>protección DRM (FairPlay)</strong> y no pueden convertirse; VidToFLAC solo procesa archivos sin protección de los que tengas los derechos.</p>'
        ),
        "faqs": [
            ("¿Por qué mi M4V no tiene audio en DaVinci Resolve?",
             "Porque el M4V lleva audio <strong>AAC</strong>, que Resolve no decodifica sin licencia —menos aún en Linux—. Pasarlo a FLAC dentro de un MKV restaura el sonido."),
            ("¿Puedo convertir películas compradas en iTunes?",
             "No, si tienen <strong>DRM FairPlay</strong>. Los M4V comprados en la tienda están protegidos y no pueden procesarse. Solo funcionan los M4V sin protección, como tus propias exportaciones."),
            ("¿Pierdo calidad de imagen al convertir un M4V?",
             "No, si el vídeo es H.264 o HEVC: se copia <strong>bit a bit</strong>. Solo el audio cambia a FLAC, que es sin pérdida."),
            ("¿Sirve para vídeos exportados desde la app Apple TV o iMovie?",
             "Sí, siempre que no tengan DRM. Esos M4V usan audio AAC y se reempaquetan sin problema a MKV con audio FLAC."),
            ("¿Se sube mi M4V a algún servidor?",
             "No. El procesamiento es 100% local en tu navegador; el archivo no sale de tu dispositivo."),
        ],
    },

    # ── MPEG / MPG ─────────────────────────────────────────────────────────────
    "convertir-mpeg-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir MPEG y MPG a FLAC",
        "seo_body": (
            '      <h3>La solución para tus MPEG/MPG: modernizar audio y vídeo</h3>\n'
            '      <p>Los <strong>MPEG y MPG</strong> de cámaras digitales antiguas, DVD y grabaciones suelen llevar audio en <strong>MP2, MP3 o AC3</strong> y vídeo <strong>MPEG-1/MPEG-2</strong>. DaVinci Resolve no maneja bien esas combinaciones. VidToFLAC convierte el audio a <strong>FLAC</strong> dentro de un <strong>MKV</strong>.</p>\n\n'
            '      <p>Como el vídeo MPEG-1/2 no se decodifica en el navegador, se recodifica a <strong>H.264</strong>, mientras el audio queda en FLAC. El clip pasa de ser un archivo heredado a un MKV moderno y editable.</p>\n\n'
            '      <p>Es la vía rápida para aprovechar metraje antiguo digitalizado sin pelear con códecs descatalogados.</p>'
        ),
        "faqs": [
            ("¿Por qué mi MPEG no entra con sonido en el editor?",
             "Porque usa audio <strong>MP2, MP3 o AC3</strong>, formatos que DaVinci Resolve no decodifica de serie. Convertir el audio a FLAC dentro de un MKV resuelve la falta de sonido."),
            ("¿El vídeo MPEG-2 se recodifica?",
             "Sí. El vídeo MPEG-1/2 no se puede decodificar en el navegador, así que se recodifica a <strong>H.264</strong>. El audio se pasa a FLAC y todo queda en un MKV."),
            ("Tengo MPG de una cámara o de un DVD antiguo, ¿funciona?",
             "Sí. Es justo el caso de uso: VidToFLAC moderniza esos archivos a MKV con vídeo H.264 y audio FLAC compatibles con editores actuales."),
            ("¿Qué diferencia hay entre .mpeg y .mpg?",
             "Ninguna relevante: son la misma familia de formato con distinta extensión. VidToFLAC los trata igual."),
            ("¿Es gratuito y privado?",
             "Sí. Es gratis, sin registro y sin subidas: todo se procesa en tu navegador con FFmpeg (WebAssembly)."),
        ],
    },

    # ── 3GP ──────────────────────────────────────────────────────────────────
    "convertir-3gp-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir 3GP a FLAC",
        "seo_body": (
            '      <h3>La solución para tus 3GP de móviles antiguos</h3>\n'
            '      <p>Los <strong>3GP</strong> de teléfonos antiguos (Nokia, Samsung, Motorola) y cámaras compactas usan audio en <strong>AAC o AMR</strong> y vídeo H.263/MPEG-4. DaVinci Resolve no decodifica esas pistas de serie. VidToFLAC convierte el audio a <strong>FLAC</strong> dentro de un <strong>MKV</strong>.</p>\n\n'
            '      <p>El audio AMR (típico de grabaciones de voz móviles) se decodifica y se vuelve a codificar a FLAC sin pérdida. Si el vídeo no se puede decodificar en el navegador, se recodifica a <strong>H.264</strong> para garantizar la previsualización.</p>\n\n'
            '      <p>Así recuperas grabaciones antiguas de móvil en un formato moderno y editable.</p>'
        ),
        "faqs": [
            ("¿Por qué mi 3GP no tiene audio compatible?",
             "Los 3GP usan audio <strong>AAC o AMR</strong>, que DaVinci Resolve no decodifica de serie. Convertirlo a FLAC dentro de un MKV lo hace reproducible en tu editor."),
            ("¿Qué es el audio AMR y se puede convertir?",
             "AMR es un códec de voz de baja tasa usado en móviles antiguos. VidToFLAC lo decodifica y lo pasa a FLAC; la calidad no mejora respecto al original, pero gana compatibilidad."),
            ("¿Se recodifica el vídeo del 3GP?",
             "Solo si su códec no es decodificable en el navegador, en cuyo caso se recodifica a H.264. Si es compatible, se copia <strong>bit a bit</strong>."),
            ("¿Sirve para grabaciones de teléfonos viejos?",
             "Sí. Es justo para ese metraje heredado: lo moderniza a MKV con audio FLAC para que puedas editarlo o archivarlo."),
            ("¿Tengo que instalar algo?",
             "No. Funciona directamente en el navegador, sin instalaciones ni registro, y sin subir archivos."),
        ],
    },

    # ── AAC ──────────────────────────────────────────────────────────────────
    "convertir-aac-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir AAC a FLAC",
        "seo_body": (
            '      <h3>La solución: pasar tu AAC a FLAC para compatibilidad sin pérdidas futuras</h3>\n'
            '      <p><strong>AAC</strong> es un formato <strong>con pérdida</strong>: cada recodificación degrada un poco más el audio. Convertir a <strong>FLAC</strong> no recupera la calidad ya perdida, pero <strong>congela</strong> el audio en un formato sin pérdida, de modo que cualquier edición o exportación posterior no añade más degradación.</p>\n\n'
            '      <p>Además, DaVinci Resolve —especialmente en Linux— no decodifica AAC de serie, por lo que pasar tu audio a FLAC soluciona de raíz el <strong>error de códec de audio</strong> al importar.</p>\n\n'
            '      <p>Como se trata de un archivo solo de audio, la salida es un <strong>.flac</strong> directo, generado en tu navegador sin subir nada a ningún servidor.</p>'
        ),
        "faqs": [
            ("¿Convertir AAC (con pérdida) a FLAC mejora la calidad?",
             "No. FLAC no puede recuperar la información que el AAC ya descartó. Lo que consigues es <strong>evitar pérdidas adicionales</strong> en futuras ediciones y ganar compatibilidad lossless."),
            ("¿Por qué pasar el AAC a FLAC en lugar de dejarlo como está?",
             "Porque muchos editores —DaVinci Resolve en Linux, entre otros— no decodifican AAC sin licencia. FLAC se reproduce de forma nativa y es ideal para edición y archivado."),
            ("¿El archivo FLAC será más grande que el AAC?",
             "Sí. AAC comprime con pérdida y ocupa poco; FLAC es sin pérdida y pesa más. A cambio, obtienes un audio que no se degrada al reeditarlo."),
            ("¿Sirve para música, podcasts o pistas de voz?",
             "Sí. Cualquier archivo AAC (.aac o dentro de M4A) puede pasarse a FLAC para edición profesional o archivado de máxima compatibilidad."),
            ("¿Se sube mi audio a internet?",
             "No. La conversión ocurre íntegramente en tu navegador con FFmpeg (WebAssembly); el archivo no sale de tu equipo."),
        ],
    },

    # ── MP3 ──────────────────────────────────────────────────────────────────
    "convertir-mp3-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir MP3 a FLAC",
        "seo_body": (
            '      <h3>La solución: convertir MP3 a FLAC para edición y archivado</h3>\n'
            '      <p><strong>MP3</strong> es el formato con pérdida más extendido, pero no siempre se integra bien en editores de vídeo profesionales. Convertir a <strong>FLAC</strong> —sin pérdida— garantiza compatibilidad nativa con DaVinci Resolve, Premiere Pro y Avid, sobre todo en <strong>Linux</strong>, donde los decodificadores de MP3 pueden faltar.</p>\n\n'
            '      <p>Pasar de MP3 a FLAC no recupera la calidad perdida en la compresión original, pero <strong>evita que se degrade más</strong> y deja el audio en un formato estable para reeditar tantas veces como quieras.</p>\n\n'
            '      <p>Al ser un archivo solo de audio, obtienes un <strong>.flac</strong> directamente, generado de forma local en tu navegador.</p>'
        ),
        "faqs": [
            ("¿Mejora la calidad al convertir MP3 a FLAC?",
             "No. FLAC no recupera lo que el MP3 eliminó al comprimir. Lo útil es que <strong>no se pierde más calidad</strong> en sucesivas ediciones y que ganas compatibilidad sin pérdida."),
            ("¿Por qué un editor de vídeo no reproduce mi MP3?",
             "En algunos sistemas, sobre todo Linux, DaVinci Resolve no incluye el decodificador de MP3 con licencia. Convertir a FLAC, que es abierto, soluciona el problema."),
            ("¿Cuánto ocupará el FLAC respecto al MP3?",
             "Bastante más: el MP3 es muy comprimido con pérdida y el FLAC es sin pérdida. El tamaño extra es el precio de un audio estable y de máxima compatibilidad."),
            ("¿Puedo convertir varios MP3 de golpe?",
             "Sí. Añade todos los que quieras y se convierten uno a uno en tu navegador, sin subir nada."),
            ("¿Es gratis y privado?",
             "Sí. Es gratuito, sin registro, y el audio no sale de tu equipo en ningún momento."),
        ],
    },

    # ── WAV ──────────────────────────────────────────────────────────────────
    "convertir-wav-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir WAV a FLAC",
        "seo_body": (
            '      <h3>La solución: comprimir tu WAV a FLAC sin perder ni un bit</h3>\n'
            '      <p><strong>WAV</strong> y <strong>FLAC</strong> son ambos formatos <strong>sin pérdida</strong>, pero el WAV no comprime: un archivo de 10 minutos puede superar los 100 MB. FLAC aplica compresión lossless y reduce el tamaño entre un <strong>40% y un 60%</strong> conservando exactamente la misma información.</p>\n\n'
            '      <p>El resultado suena <strong>idéntico</strong> al WAV original —misma frecuencia de muestreo y profundidad de bits— pero ocupa mucho menos en disco y se transfiere más rápido, sin sacrificar calidad.</p>\n\n'
            '      <p>La conversión genera un <strong>.flac</strong> directamente en tu navegador, sin enviar el audio a ningún servidor.</p>'
        ),
        "faqs": [
            ("¿Pierdo calidad al convertir un WAV a FLAC?",
             "No. FLAC es sin pérdida: guarda exactamente los mismos datos de audio que el WAV. La conversión es <strong>bit a bit reversible</strong>, sin ninguna degradación."),
            ("¿Cuánto se reduce el tamaño?",
             "Normalmente entre un <strong>40% y un 60%</strong>, según el contenido del audio. Música y voz se comprimen bien; el silencio y los tonos puros, aún más."),
            ("¿Se mantienen la frecuencia de muestreo y los bits?",
             "Sí. FLAC conserva la misma frecuencia (44.1 kHz, 48 kHz, etc.) y la misma profundidad de bits (16, 24…) que el WAV de origen."),
            ("¿Por qué usar FLAC en lugar de WAV al editar?",
             "Porque ocupa mucho menos manteniendo idéntica calidad, y editores como DaVinci Resolve lo soportan de forma nativa. Es ideal para archivar proyectos sin llenar el disco."),
            ("¿Se sube mi WAV a algún sitio?",
             "No. Todo el proceso es local en tu navegador mediante WebAssembly; el archivo no abandona tu equipo."),
        ],
    },

    # ── M4A ──────────────────────────────────────────────────────────────────
    "convertir-m4a-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir M4A a FLAC",
        "seo_body": (
            '      <h3>La solución: liberar el audio AAC de tus M4A a FLAC</h3>\n'
            '      <p>Los <strong>M4A</strong> de iPhone, las grabaciones de voz de Apple y las exportaciones de iTunes contienen audio <strong>AAC</strong> dentro de un contenedor MPEG-4. DaVinci Resolve no decodifica AAC de serie —menos en Linux—, lo que provoca pistas en gris o un <strong>error de códec de audio</strong>.</p>\n\n'
            '      <p>VidToFLAC extrae ese audio y lo convierte a <strong>FLAC</strong>, un formato abierto y sin pérdida. No recupera la calidad perdida por el AAC, pero evita degradaciones futuras y da compatibilidad inmediata.</p>\n\n'
            '      <p>La salida es un <strong>.flac</strong> generado en tu navegador, sin subir el archivo a ningún servidor.</p>'
        ),
        "faqs": [
            ("¿Por qué mi M4A no se importa con sonido?",
             "Porque su audio es <strong>AAC</strong>, que DaVinci Resolve no decodifica sin licencia. Convertirlo a FLAC soluciona la pista muda o el error de códec."),
            ("¿Mejora la calidad al pasar M4A a FLAC?",
             "No. El M4A es con pérdida (AAC) y FLAC no recupera lo descartado; lo que ganas es <strong>compatibilidad sin pérdidas adicionales</strong> al reeditar."),
            ("¿Sirve para las grabaciones de voz del iPhone?",
             "Sí. Las notas de voz de Apple se guardan como M4A/AAC y se convierten sin problema a FLAC para edición o archivado."),
            ("¿El FLAC pesará más que el M4A?",
             "Sí, porque FLAC es sin pérdida y el M4A está muy comprimido. A cambio obtienes un audio estable y de máxima compatibilidad."),
            ("¿Es necesario registrarse?",
             "No. Es gratis, sin cuenta y sin subidas: todo ocurre en tu navegador."),
        ],
    },

    # ── OGG ──────────────────────────────────────────────────────────────────
    "convertir-ogg-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir OGG a FLAC",
        "seo_body": (
            '      <h3>La solución: de OGG Vorbis a FLAC para compatibilidad total</h3>\n'
            '      <p><strong>OGG Vorbis</strong> es un formato con pérdida de código abierto que ofrece buena calidad a tamaños reducidos, pero no es compatible de forma nativa con la mayoría de editores de vídeo profesionales. Convertir a <strong>FLAC</strong> resuelve el problema de compatibilidad de inmediato.</p>\n\n'
            '      <p>El paso de OGG a FLAC no recupera la información perdida en la compresión Vorbis, pero <strong>evita más pérdidas</strong> en sucesivas ediciones y deja el audio listo para DaVinci Resolve, Premiere o Avid.</p>\n\n'
            '      <p>Al ser solo audio, obtienes un <strong>.flac</strong> directamente, generado en local en tu navegador.</p>'
        ),
        "faqs": [
            ("¿Por qué mi OGG no funciona en el editor de vídeo?",
             "Porque OGG Vorbis no está entre los códecs que los editores profesionales decodifican de serie. FLAC, en cambio, se reproduce de forma nativa."),
            ("¿Convertir OGG a FLAC sube la calidad?",
             "No. Vorbis es con pérdida y FLAC no recupera lo descartado; el beneficio es la <strong>compatibilidad</strong> y no perder más calidad al reeditar."),
            ("¿Sirve para audio de juegos o de aplicaciones?",
             "Sí. Muchos juegos y apps usan OGG; convertirlo a FLAC permite editarlo o archivarlo en un formato sin pérdida estándar."),
            ("¿El FLAC ocupará más que el OGG?",
             "Sí, porque FLAC es sin pérdida. El tamaño extra es el coste de un audio compatible y estable."),
            ("¿Se procesa en la nube?",
             "No. Todo es local en tu navegador con FFmpeg (WebAssembly); el archivo no sale de tu dispositivo."),
        ],
    },

    # ── WMA ──────────────────────────────────────────────────────────────────
    "convertir-wma-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir WMA a FLAC",
        "seo_body": (
            '      <h3>La solución: salir del WMA propietario hacia FLAC abierto</h3>\n'
            '      <p><strong>WMA (Windows Media Audio)</strong> es un formato propietario de Microsoft que no forma parte de los códecs incluidos en DaVinci Resolve —especialmente en <strong>Linux y macOS</strong>—, donde las pistas aparecen en gris o no se importan. Convertir a <strong>FLAC</strong>, abierto y sin pérdida, resuelve la compatibilidad al instante.</p>\n\n'
            '      <p>La conversión decodifica el WMA y vuelve a codificar el audio a FLAC. Si el WMA era con pérdida, FLAC no recupera lo descartado, pero asegura que no haya más degradación y que el audio sea editable en cualquier plataforma.</p>\n\n'
            '      <p>La salida es un <strong>.flac</strong> creado en tu navegador, sin subir nada a ningún servidor.</p>'
        ),
        "faqs": [
            ("¿Por qué mi WMA no se reproduce en Mac o Linux?",
             "WMA es un formato propietario de Microsoft con escaso soporte fuera de Windows. DaVinci Resolve no lo decodifica en Linux ni macOS; FLAC, en cambio, es universal."),
            ("¿Convertir WMA a FLAC mejora el sonido?",
             "No, si el WMA era con pérdida: FLAC no recupera la información eliminada. Lo que ganas es <strong>compatibilidad multiplataforma</strong> sin más degradación."),
            ("¿Sirve para música antigua rippeada en Windows?",
             "Sí. Las bibliotecas WMA de Windows Media Player se convierten a FLAC para escucharlas y editarlas en cualquier sistema."),
            ("¿Necesito Windows para convertir WMA?",
             "No. Al ejecutarse en el navegador, VidToFLAC convierte WMA igual en Windows, macOS o Linux."),
            ("¿Se suben mis archivos WMA?",
             "No. La conversión es 100% local; tus archivos no salen del equipo."),
        ],
    },

    # ── AIFF ─────────────────────────────────────────────────────────────────
    "convertir-aiff-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir AIFF a FLAC",
        "seo_body": (
            '      <h3>La solución: comprimir AIFF a FLAC sin perder calidad</h3>\n'
            '      <p><strong>AIFF</strong> —el equivalente de Apple al WAV— y <strong>FLAC</strong> son ambos <strong>sin pérdida</strong>, pero AIFF no comprime los datos: ocupa mucho espacio. FLAC aplica compresión lossless y reduce el tamaño entre un <strong>40% y un 60%</strong> sin descartar ni un bit de información.</p>\n\n'
            '      <p>El audio resultante es <strong>idéntico</strong> al AIFF original —misma frecuencia y profundidad de bits— pero mucho más ligero, perfecto para archivar o editar sin saturar el disco.</p>\n\n'
            '      <p>Obtienes un <strong>.flac</strong> generado en tu navegador, sin enviar el audio a ningún servidor.</p>'
        ),
        "faqs": [
            ("¿Pierdo calidad al convertir AIFF a FLAC?",
             "No. Ambos son sin pérdida; FLAC guarda exactamente los mismos datos que el AIFF, solo que comprimidos. El sonido es idéntico."),
            ("¿Cuánto espacio ahorro?",
             "Habitualmente entre un <strong>40% y un 60%</strong> respecto al AIFF sin comprimir, según el material de audio."),
            ("¿Se conservan los parámetros del audio?",
             "Sí. FLAC mantiene la misma frecuencia de muestreo y profundidad de bits que el AIFF de origen."),
            ("¿Por qué pasar de AIFF a FLAC?",
             "Para ahorrar espacio sin perder calidad y ganar compatibilidad: FLAC es soportado de forma nativa por más programas que el AIFF en sistemas no-Apple."),
            ("¿Es privado?",
             "Totalmente. El proceso ocurre en tu navegador con WebAssembly; el archivo no sale de tu equipo."),
        ],
    },

    # ── OPUS ─────────────────────────────────────────────────────────────────
    "convertir-opus-a-flac": {
        "faq_h2": "Preguntas frecuentes sobre convertir Opus a FLAC",
        "seo_body": (
            '      <h3>La solución: de Opus a FLAC para editar grabaciones de Discord y voz</h3>\n'
            '      <p><strong>Opus</strong> es el códec por defecto en grabaciones de <strong>Discord</strong>, streams y videollamadas. Ofrece gran calidad a bajo bitrate, pero no es compatible de forma nativa con la mayoría de editores de vídeo. Convertir a <strong>FLAC</strong> garantiza que el audio se importe sin errores.</p>\n\n'
            '      <p>El paso de Opus a FLAC no recupera lo perdido en la compresión, pero <strong>evita más pérdidas</strong> y deja el audio listo para DaVinci Resolve, Premiere o Avid.</p>\n\n'
            '      <p>Como es solo audio, la salida es un <strong>.flac</strong> directo, creado en local en tu navegador.</p>'
        ),
        "faqs": [
            ("¿Por qué mi grabación Opus de Discord no se importa?",
             "Porque Opus no está entre los códecs que los editores de vídeo decodifican de serie. Convertirlo a FLAC lo hace compatible al instante."),
            ("¿Convertir Opus a FLAC mejora la calidad?",
             "No. Opus es con pérdida y FLAC no recupera lo descartado; el beneficio es la <strong>compatibilidad</strong> y no degradar más el audio al editarlo."),
            ("¿Sirve para audio de videollamadas o streams?",
             "Sí. Muchas plataformas graban en Opus; pasarlo a FLAC permite editarlo en programas que no lo soportan de forma nativa."),
            ("¿El archivo FLAC será más grande?",
             "Sí, porque FLAC es sin pérdida y Opus está muy comprimido. Es el coste de un audio compatible y estable."),
            ("¿Se sube mi audio a algún servidor?",
             "No. La conversión es 100% local en tu navegador; nada sale de tu equipo."),
        ],
    },

}
