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
O_BRAND      = '<span class="brand-name">VidTo<span class="brand-accent">FLAC</span></span>'
O_STYLE_END  = '  </style>\n</head>'


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
