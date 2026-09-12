#!/usr/bin/env python3
"""
landing_content_en.py — contenido en inglés de las landings SEO.

Equivale a build_pages.PAGES + landing_content.CONTENT, pero para /en/.
build_pages.py lo importa desde main(); si el archivo no existe, solo genera
las españolas.

Añadir un formato = una entrada en PAGES_EN y otra en CONTENT_EN con el mismo
slug, y volver a ejecutar build_pages.py.
"""

PAGES_EN = [
    {
        "slug":             "convert-mp4-to-flac",
        "title":            "Convert MP4 to FLAC – Lossless Audio for DaVinci Resolve | VidToFLAC",
        "description":      "Convert the audio in your MP4 files to lossless FLAC, 100% in your browser with FFmpeg. Fixes the DaVinci Resolve audio codec error on MP4s from cameras, OBS and phones.",
        "keywords":         "convert MP4 to FLAC, MP4 FLAC DaVinci Resolve, MP4 no sound DaVinci Resolve, remux MP4 MKV FLAC, extract MP4 audio lossless, FFmpeg MP4 browser",
        "canonical":        "https://vidtoflac.tech/en/convert-mp4-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-mp4-to-flac/",
        "og_title":         "Convert MP4 to FLAC – Lossless Audio | VidToFLAC",
        "og_desc":          "Convert your MP4 audio to FLAC in your browser. Fixes the DaVinci Resolve audio error on MP4 files — nothing uploaded.",
        "tw_title":         "Convert MP4 to FLAC – Lossless Audio | VidToFLAC",
        "tw_desc":          "Convert your MP4 audio to FLAC in your browser. Fixes the DaVinci Resolve audio error — nothing uploaded.",
        "webapp_url":       "https://vidtoflac.tech/en/convert-mp4-to-flac/",
        "webapp_desc":      "Converter that turns the audio of MP4 files into lossless FLAC inside an MKV (remux) to fix the audio codec error in DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert MP4 audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">MP4 to FLAC</span> without losing quality',
        "hero_sub":         "Fixes the DaVinci Resolve audio codec error on MP4 files from cameras, OBS and smartphones. Processing is 100% local — not a single byte is uploaded to any server.",
        "seo_h2":           'Why does <span class="accent">DaVinci Resolve have no audio</span> from your MP4 files?',
        "seo_lede":         'If you have opened an <strong>MP4 file</strong> in DaVinci Resolve and it plays <strong>silently</strong> — or the audio track sits greyed out — it is almost always the audio codec. MP4s recorded by cameras, OBS Studio and smartphones carry <strong>AAC or MP3</strong> audio, and the free DaVinci Resolve — especially <strong>on Linux</strong> — ships no licence to decode them.',
        "breadcrumb_label": "Convert MP4 to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting MP4 to FLAC</h2>
      <h3>The MP4 container and its audio codecs</h3>
      <p>MP4 (MPEG-4 Part 14) is the most widespread video container there is: DSLRs, smartphones, OBS Studio and practically every video platform use it. Its popularity comes from packing H.264 or H.265 video together with audio into one compact file. The trouble is the audio codec: the overwhelming majority of MP4 files carry <strong>AAC-LC</strong> (Low Complexity), the standard profile for consumer devices. OBS can also produce <strong>MP3</strong> depending on how it is configured. Less commonly, field recorders write MP4 with <strong>linear PCM</strong>, which Resolve does read without conversion.</p>
      <h3>Why DaVinci Resolve greys out the audio track</h3>
      <p>The free DaVinci Resolve — most visibly on Linux — ships no AAC decoder, because the licence is proprietary and costs money per distribution. Open an MP4 with AAC and the media inspector may show the audio greyed out, the clip with no waveform, or the message <em>"Audio codec not supported (AAC)"</em>. The restriction affects audio only: H.264 and H.265 video open fine, because those decoders are included. The fix is to replace the AAC with <strong>FLAC</strong>, which Resolve decodes natively on every platform.</p>
      <h3>Step by step: converting your MP4 to FLAC</h3>
      <ol>
        <li>Drop your .mp4 onto the upload area, or click <strong>Select files</strong>.</li>
        <li>Pick <strong>MKV</strong> as the output (recommended for Resolve compatibility), or MP4 if you would rather keep the extension.</li>
        <li>Press <strong>Convert</strong>. VidToFLAC detects the audio codec, re-encodes only that track to FLAC, and copies the video across untouched.</li>
        <li>Download the result and import it into Resolve's Media Pool. The audio track will appear in blue and play without errors.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If your MP4 carries <strong>H.265 / HEVC</strong> video and the job takes longer than you expected, it is because the browser cannot decode HEVC for preview. VidToFLAC re-encodes the video to H.264 in that case; the audio is still FLAC and the file still works in Resolve. If the MP4 came from a camera with several audio tracks (stereo plus surround), every track is converted into the output container.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-mkv-to-flac",
        "title":            "Convert MKV to FLAC – Lossless Remux for DaVinci Resolve | VidToFLAC",
        "description":      "Convert the audio inside your MKV files to lossless FLAC without re-encoding the video. Fixes silent OBS and screen recordings in DaVinci Resolve, entirely in your browser.",
        "keywords":         "convert MKV to FLAC, MKV FLAC DaVinci Resolve, OBS MKV no sound, MKV audio remux, MKV AAC DaVinci Resolve Linux",
        "canonical":        "https://vidtoflac.tech/en/convert-mkv-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-mkv-to-flac/",
        "og_title":         "Convert MKV to FLAC – Lossless Remux | VidToFLAC",
        "og_desc":          "Swap the audio in your MKV files for lossless FLAC without touching the video. Fixes silent OBS recordings in DaVinci Resolve.",
        "tw_title":         "Convert MKV to FLAC – Lossless Remux | VidToFLAC",
        "tw_desc":          "Swap the audio in your MKV files for lossless FLAC without touching the video. Fixes silent OBS recordings.",
        "webapp_url":       "https://vidtoflac.tech/en/convert-mkv-to-flac/",
        "webapp_desc":      "Converter that replaces the audio track of MKV files with lossless FLAC, keeping the same container and copying the video untouched. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert MKV audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">MKV to FLAC</span> without re-encoding the video',
        "hero_sub":         "Fixes silent OBS Studio recordings, screen captures and camera MKVs in DaVinci Resolve. Everything runs in your browser — nothing is uploaded anywhere.",
        "seo_h2":           'Why does <span class="accent">DaVinci Resolve have no audio</span> from your MKV files?',
        "seo_lede":         'An <strong>MKV</strong> is a container that accepts almost any codec, and that is exactly where the trouble starts. MKVs from <strong>OBS Studio</strong>, screen recorders and cameras usually store audio as <strong>AAC</strong>, sometimes Opus — and the free DaVinci Resolve decodes neither reliably, least of all on Linux.',
        "breadcrumb_label": "Convert MKV to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting MKV to FLAC</h2>
      <h3>Why MKV is both the best and the worst container</h3>
      <p>Matroska (MKV) is an open container that imposes almost no limits on what goes inside it: any video codec, any audio codec, any number of tracks, subtitles and chapters. That flexibility is why OBS Studio recommends it for recording — an MKV survives a crash, whereas a half-written MP4 is often unusable. The flip side is that "MKV" tells you nothing about whether your editor can read the contents. Two MKVs can behave completely differently.</p>
      <h3>The OBS Studio case</h3>
      <p>OBS records MKV with <strong>AAC audio at 160 kbps</strong> by default. That single default is behind a large share of the "no audio in DaVinci Resolve" reports from people editing on Linux. The video, normally H.264, imports perfectly; the audio track shows up greyed out or silent. Converting that audio to FLAC inside the same MKV is enough — the container never has to change.</p>
      <h3>Step by step: converting your MKV to FLAC</h3>
      <ol>
        <li>Drop the .mkv file onto the upload area. You can queue several recordings at once.</li>
        <li>Leave <strong>MKV</strong> as the output. The container stays the same; only the audio track changes.</li>
        <li>Press <strong>Convert</strong>. The video stream is copied across and only the audio is re-encoded to FLAC.</li>
        <li>Import the result into DaVinci Resolve. The waveform appears and the sound plays.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If your MKV carries <strong>H.265 / HEVC</strong> video, the browser cannot decode it for preview and VidToFLAC re-encodes it to H.264 at high quality. If the file holds several audio tracks — a game feed plus a microphone, say — all of them are converted. And if the MKV came from a download rather than a recording, check first whether the audio is <strong>Opus</strong>: Resolve struggles with that one even on Windows, and the same conversion fixes it.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-mov-to-flac",
        "title":            "Convert MOV to FLAC – iPhone and GoPro Audio for DaVinci Resolve | VidToFLAC",
        "description":      "Convert the audio in MOV files from iPhone, GoPro and mirrorless cameras to lossless FLAC. Fixes the DaVinci Resolve audio codec error, entirely in your browser.",
        "keywords":         "convert MOV to FLAC, MOV FLAC DaVinci Resolve, iPhone MOV no sound, GoPro MOV audio, MOV ProRes FLAC, QuickTime audio DaVinci Resolve",
        "canonical":        "https://vidtoflac.tech/en/convert-mov-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-mov-to-flac/",
        "og_title":         "Convert MOV to FLAC – iPhone and GoPro Audio | VidToFLAC",
        "og_desc":          "Convert MOV audio from iPhone, GoPro and cameras to lossless FLAC. Fixes the DaVinci Resolve audio error — nothing uploaded.",
        "tw_title":         "Convert MOV to FLAC – iPhone and GoPro Audio | VidToFLAC",
        "tw_desc":          "Convert MOV audio from iPhone, GoPro and cameras to lossless FLAC. Fixes the DaVinci Resolve audio error.",
        "webapp_url":       "https://vidtoflac.tech/en/convert-mov-to-flac/",
        "webapp_desc":      "Converter that turns the audio of QuickTime MOV files into lossless FLAC inside an MKV, to fix the audio codec error in DaVinci Resolve. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert MOV audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">MOV to FLAC</span> without losing quality',
        "hero_sub":         "For MOV files from iPhone, GoPro, Sony, Canon and Fujifilm. Fixes the DaVinci Resolve audio codec error without uploading a single byte.",
        "seo_h2":           'Why does <span class="accent">DaVinci Resolve have no audio</span> from your MOV files?',
        "seo_lede":         '<strong>MOV</strong> is the QuickTime container, and it is what iPhone, GoPro and most mirrorless cameras write. Nearly all of them store audio as <strong>AAC</strong> — the codec the free DaVinci Resolve cannot decode without a licence, particularly on Linux. The video is fine; only the sound is missing.',
        "breadcrumb_label": "Convert MOV to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting MOV to FLAC</h2>
      <h3>What is actually inside a camera MOV</h3>
      <p>MOV is Apple's QuickTime container and the native format of the iPhone, GoPro and most Sony, Canon and Fujifilm bodies. Inside you will usually find <strong>H.264 or H.265 video with AAC audio</strong>. Professional workflows are the exception: field and cinema cameras write <strong>ProRes video with linear PCM audio</strong>, which behaves very differently. Knowing which of the two you have explains most of what happens next.</p>
      <h3>The iPhone and HEVC</h3>
      <p>Since iOS 11 the iPhone has recorded in <strong>HEVC (H.265)</strong> by default, in "High Efficiency" mode. That halves the file size, but the browser cannot decode HEVC for preview, so VidToFLAC re-encodes the video to H.264 at high quality (<code>-crf 18</code>) — visually very close to the original, though not bit-for-bit identical. If you would rather keep the video untouched, switch the iPhone to <em>Settings → Camera → Formats → Most Compatible</em>, which records H.264.</p>
      <h3>Step by step: converting your MOV to FLAC</h3>
      <ol>
        <li>Drop the .mov file onto the upload area.</li>
        <li>Choose <strong>MKV</strong> as the output for the widest Resolve compatibility.</li>
        <li>Press <strong>Convert</strong>. Only the audio track is re-encoded, to FLAC.</li>
        <li>Import the result into DaVinci Resolve, where the audio now plays.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If your MOV is <strong>ProRes</strong>, the browser cannot decode it either and the video is re-encoded to H.264 — fine for editing proxies, but not what you want for a ProRes master. Use desktop FFmpeg for those. If the audio is <strong>PCM at 24 bit</strong>, it already works in Resolve and you may not need to convert anything; check the codec before assuming the audio is at fault.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-avi-to-flac",
        "title":            "Convert AVI to FLAC – Rescue Audio From Old Video | VidToFLAC",
        "description":      "Convert the audio in AVI files to lossless FLAC in your browser. Fixes MP3 and AC3 audio from old camcorders, capture cards and legacy software in DaVinci Resolve.",
        "keywords":         "convert AVI to FLAC, AVI FLAC DaVinci Resolve, AVI no sound editor, old AVI audio MP3 AC3, convert AVI browser",
        "canonical":        "https://vidtoflac.tech/en/convert-avi-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-avi-to-flac/",
        "og_title":         "Convert AVI to FLAC – Rescue Audio From Old Video | VidToFLAC",
        "og_desc":          "Convert AVI audio to lossless FLAC in your browser. Fixes MP3 and AC3 tracks that editors refuse to read.",
        "tw_title":         "Convert AVI to FLAC – Rescue Audio From Old Video | VidToFLAC",
        "tw_desc":          "Convert AVI audio to lossless FLAC in your browser. Fixes MP3 and AC3 tracks editors refuse to read.",
        "webapp_url":       "https://vidtoflac.tech/en/convert-avi-to-flac/",
        "webapp_desc":      "Converter that turns the audio of AVI files into lossless FLAC inside an MKV, so old recordings import correctly into DaVinci Resolve and other editors. Runs 100% in the browser with FFmpeg (WebAssembly).",
        "howto_name":       "How to convert AVI audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">AVI to FLAC</span> and get the sound back',
        "hero_sub":         "For AVI files from old camcorders, capture cards and legacy recording software. Everything runs in your browser — nothing is uploaded.",
        "seo_h2":           'Why does <span class="accent">your AVI import without sound</span> into DaVinci Resolve?',
        "seo_lede":         '<strong>AVI</strong> files from old camcorders, capture cards and recording software usually carry audio as <strong>MP3 or AC3</strong>, formats DaVinci Resolve does not decode out of the box — and on Linux not at all. The picture appears; the audio track does not.',
        "breadcrumb_label": "Convert AVI to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting AVI to FLAC</h2>
      <h3>Why AVI causes more trouble than newer containers</h3>
      <p>AVI dates from 1992 and was never designed for what people ask of it today. It has no standard way to signal variable frame rate, its timestamps are rudimentary, and it accepts codecs that modern software has long stopped shipping decoders for. An AVI from a 2005 camcorder might hold DivX or Xvid video with MP3 audio; one from a capture card might hold uncompressed video with PCM. The container name tells you very little.</p>
      <h3>What VidToFLAC does with an AVI</h3>
      <p>The audio always becomes FLAC. The video depends on the codec: if the browser can decode it, it is copied across bit for bit with no loss. If it is a legacy codec the browser has never supported — DivX, Xvid, Cinepak, Indeo — it is re-encoded to H.264, which also makes the result far easier to edit than the original.</p>
      <h3>Step by step: converting your AVI to FLAC</h3>
      <ol>
        <li>Drop the .avi onto the upload area.</li>
        <li>Choose <strong>MKV</strong> as the output — modern editors handle it far better than AVI.</li>
        <li>Press <strong>Convert</strong> and wait. Legacy codecs need re-encoding, so this takes longer than a plain remux.</li>
        <li>Import the result and check the audio now plays.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Old AVIs are frequently <strong>interlaced</strong>. Converting the audio does not deinterlace the picture — you will want to handle that in your editor's clip attributes. If the AVI is very large and uncompressed, remember the browser's practical ceiling is around 1 GB; split long captures before converting.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-webm-to-flac",
        "title":            "Convert WebM to FLAC – Opus and Vorbis Audio for Editors | VidToFLAC",
        "description":      "Convert the Opus or Vorbis audio in WebM files to lossless FLAC in your browser. Fixes downloaded video and screen recordings that import silently into DaVinci Resolve.",
        "keywords":         "convert WebM to FLAC, WebM Opus DaVinci Resolve, WebM no sound editor, Vorbis FLAC conversion, YouTube WebM audio",
        "canonical":        "https://vidtoflac.tech/en/convert-webm-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-webm-to-flac/",
        "og_title":         "Convert WebM to FLAC – Opus and Vorbis Audio | VidToFLAC",
        "og_desc":          "Convert WebM audio from Opus or Vorbis to lossless FLAC in your browser. Makes downloaded video editable.",
        "tw_title":         "Convert WebM to FLAC – Opus and Vorbis Audio | VidToFLAC",
        "tw_desc":          "Convert WebM audio from Opus or Vorbis to lossless FLAC in your browser. Makes downloaded video editable.",
        "webapp_url":       "https://vidtoflac.tech/en/convert-webm-to-flac/",
        "webapp_desc":      "Converter that turns the Opus or Vorbis audio of WebM files into lossless FLAC inside an MKV, so the result imports into DaVinci Resolve with sound. Runs 100% in the browser with FFmpeg (WebAssembly).",
        "howto_name":       "How to convert WebM audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">WebM to FLAC</span> and make it editable',
        "hero_sub":         "For downloaded video, screen recordings and browser captures with Opus or Vorbis audio. Everything happens locally in your browser.",
        "seo_h2":           'Why does <span class="accent">your WebM import without sound</span> into DaVinci Resolve?',
        "seo_lede":         '<strong>WebM</strong> pairs VP8 or VP9 video with <strong>Opus or Vorbis</strong> audio. Both audio codecs are open and excellent, and both are outside what video editors decode as standard — which is why a downloaded WebM lands in DaVinci Resolve with the picture intact and no sound at all.',
        "breadcrumb_label": "Convert WebM to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting WebM to FLAC</h2>
      <h3>Why WebM and video editors do not get along</h3>
      <p>WebM was designed by Google for the web, not for editing: royalty-free codecs, small files, fast streaming. Those goals are the opposite of what an NLE optimises for. Editors are built around codecs the broadcast industry standardised on decades ago — H.264, ProRes, DNxHD, PCM, AAC — and Opus and Vorbis never entered that world. The format is not broken; it is simply aimed elsewhere.</p>
      <h3>Opus is better than what replaces it, and that is fine</h3>
      <p>Worth being clear about this: Opus is a superb codec, better than AAC at the same bitrate. Converting it to FLAC does not improve the audio — nothing can recover what lossy compression already discarded. What FLAC buys you is that everything downstream can read it, and that no further quality is lost from this point on. It is a compatibility move, not a quality one.</p>
      <h3>Step by step: converting your WebM to FLAC</h3>
      <ol>
        <li>Drop the .webm onto the upload area.</li>
        <li>Choose <strong>MKV</strong> as the output.</li>
        <li>Press <strong>Convert</strong>. VP8 and VP9 video is copied across when the browser can decode it.</li>
        <li>Import the MKV into your editor, where the audio now plays.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Screen recordings made in a browser are very often <strong>variable frame rate</strong>, which makes audio drift as the clip progresses. Converting the audio does not fix that — you need a constant frame rate, which means re-encoding the video with <code>-vf fps=N</code>. If the drift grows over time rather than staying constant, VFR is your problem, not the codec.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-wav-to-flac",
        "title":            "Convert WAV to FLAC – Lossless Compression in Your Browser | VidToFLAC",
        "description":      "Convert WAV to FLAC with no quality loss and roughly half the file size. Runs entirely in your browser with FFmpeg — nothing is uploaded to any server.",
        "keywords":         "convert WAV to FLAC, WAV FLAC lossless, compress WAV without quality loss, WAV FLAC DaVinci Resolve, WAV converter browser",
        "canonical":        "https://vidtoflac.tech/en/convert-wav-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-wav-to-flac/",
        "og_title":         "Convert WAV to FLAC – Lossless Compression | VidToFLAC",
        "og_desc":          "Convert WAV to FLAC with identical quality and around half the size. Entirely in your browser, nothing uploaded.",
        "tw_title":         "Convert WAV to FLAC – Lossless Compression | VidToFLAC",
        "tw_desc":          "Convert WAV to FLAC with identical quality and around half the size. Entirely in your browser.",
        "webapp_url":       "https://vidtoflac.tech/en/convert-wav-to-flac/",
        "webapp_desc":      "Converter that compresses WAV audio into FLAC losslessly, keeping every sample while roughly halving the file size. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert WAV to FLAC without losing quality",
        "hero_h1":          'Convert your <span class="accent">WAV to FLAC</span> and halve the size',
        "hero_sub":         "Identical quality, roughly half the space. FLAC keeps every single sample of your WAV — the conversion is reversible, and nothing leaves your browser.",
        "seo_h2":           'Why convert <span class="accent">WAV to FLAC</span> at all?',
        "seo_lede":         'Both <strong>WAV and FLAC are lossless</strong>, so this is not about quality — it is about size. WAV stores audio uncompressed, which means a two-hour recording can run to several gigabytes. FLAC stores exactly the same samples in <strong>40 to 60% less space</strong>, and DaVinci Resolve, Premiere and Avid all read it natively.',
        "breadcrumb_label": "Convert WAV to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting WAV to FLAC</h2>
      <h3>Lossless does not mean identical file, it means identical audio</h3>
      <p>This trips people up, so it is worth stating plainly: FLAC compresses the way ZIP does. It finds patterns in the data and stores them more efficiently, and decoding returns <strong>exactly the original samples, bit for bit</strong>. Convert WAV to FLAC and back, and you get a file whose audio content is indistinguishable from where you started — not approximately, but precisely. What you lose is only the wasted space.</p>
      <h3>How much smaller, in practice</h3>
      <p>Typically <strong>40 to 60%</strong>, though it depends entirely on the material. Dense, loud music compresses least; speech, podcasts and anything with silence in it compress most. A field recording with long quiet passages can drop by 70%. Uncompressed 24-bit multitrack sessions sit at the other end. The only way to know your number is to convert and compare.</p>
      <h3>When to stay with WAV</h3>
      <ol>
        <li><strong>When a delivery spec demands it.</strong> Some broadcasters and mastering houses require PCM explicitly. Follow the spec.</li>
        <li><strong>When your hardware cannot read FLAC.</strong> Older field recorders and some embedded players are PCM-only.</li>
        <li><strong>Mid-session, for scratch files.</strong> Encoding costs a little CPU; for temporary files nobody will keep, it is not worth the round trip.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If your WAV came from a USB microphone it may be <strong>32-bit floating point</strong> (<code>pcm_f32le</code>). FLAC only stores integer samples, so VidToFLAC converts it to 32-bit integer first. That step is handled automatically and is not audible, but it is why the file is not a pure repackage in that case.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-aac-to-flac",
        "title":            "Convert AAC to FLAC – Lossless Audio for Editors | VidToFLAC",
        "description":      'Convert AAC audio to lossless FLAC, 100% in your browser with FFmpeg. AAC is the standard lossy codec in MP4 and MOV files, and the one DaVinci Resolve most often refuses to decode without a licence. No file uploads and no sign-up.',
        "keywords":         "convert AAC to FLAC, AAC FLAC DaVinci Resolve, aac to flac converter, AAC audio editor compatibility",
        "canonical":        "https://vidtoflac.tech/en/convert-aac-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-aac-to-flac/",
        "og_title":         "Convert AAC to FLAC – Lossless Audio for Editors | VidToFLAC",
        "og_desc":          'Convert AAC audio to lossless FLAC in your browser. AAC is the standard lossy codec in MP4 and MOV files, and the one DaVinci Resolve most often refuses to decode without a licence.',
        "tw_title":         "Convert AAC to FLAC – Lossless Audio for Editors | VidToFLAC",
        "tw_desc":          'Convert AAC audio to lossless FLAC in your browser. AAC is the standard lossy codec in MP4 and MOV files, and the one DaVinci Resolve most often refuses to decode without a licence.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-aac-to-flac/",
        "webapp_desc":      "Converter that transcodes AAC audio to lossless FLAC so it imports correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert AAC to FLAC for video editing",
        "hero_h1":          'Convert your <span class="accent">AAC to FLAC</span> losslessly',
        "hero_sub":         'AAC is the standard lossy codec in MP4 and MOV files, and the one DaVinci Resolve most often refuses to decode without a licence. Everything runs inside your browser with FFmpeg — not a single byte is uploaded to any server.',
        "seo_h2":           'Why convert <span class="accent">AAC to FLAC</span>?',
        "seo_lede":         'AAC (Advanced Audio Coding) succeeded MP3 and is what almost every camera, phone and streaming platform records. It is efficient and it sounds good, but it is patent-encumbered, and that is precisely why the free DaVinci Resolve ships no decoder for it on Linux.',
        "breadcrumb_label": "Convert AAC to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting AAC to FLAC</h2>
      <h3>What AAC actually is</h3>
      <p>AAC (Advanced Audio Coding) succeeded MP3 and is what almost every camera, phone and streaming platform records. It is efficient and it sounds good, but it is patent-encumbered, and that is precisely why the free DaVinci Resolve ships no decoder for it on Linux.</p>
      <h3>What this conversion does, and what it does not</h3>
      <p>Converting AAC to FLAC does not recover quality that lossy compression already discarded — nothing can. What it does is stop any further loss and produce a file every editor can read. Treat it as a compatibility conversion, not a restoration.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .aac file onto the upload area, or click <strong>Select files</strong>. You can queue several at once.</li>
        <li>Choose <strong>FLAC</strong> as the output format.</li>
        <li>Press <strong>Convert</strong>. The file is processed on your own machine and never uploaded.</li>
        <li>Download the FLAC and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If the source is 32-bit floating point audio, FLAC needs integer samples, so it is converted to 32-bit integer first — handled automatically and inaudible. If a file fails outright, open <strong>Technical details · FFmpeg</strong> and read the log: it usually names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-mp3-to-flac",
        "title":            "Convert MP3 to FLAC – Lossless Container for Editing | VidToFLAC",
        "description":      'Convert MP3 audio to lossless FLAC, 100% in your browser with FFmpeg. MP3 is everywhere, and it is also one of the formats video editors handle least gracefully in a professional timeline. No file uploads and no sign-up.',
        "keywords":         "convert MP3 to FLAC, MP3 FLAC DaVinci Resolve, mp3 to flac converter, MP3 audio editor compatibility",
        "canonical":        "https://vidtoflac.tech/en/convert-mp3-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-mp3-to-flac/",
        "og_title":         "Convert MP3 to FLAC – Lossless Container for Editing | VidToFLAC",
        "og_desc":          'Convert MP3 audio to lossless FLAC in your browser. MP3 is everywhere, and it is also one of the formats video editors handle least gracefully in a professional timeline.',
        "tw_title":         "Convert MP3 to FLAC – Lossless Container for Editing | VidToFLAC",
        "tw_desc":          'Convert MP3 audio to lossless FLAC in your browser. MP3 is everywhere, and it is also one of the formats video editors handle least gracefully in a professional timeline.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-mp3-to-flac/",
        "webapp_desc":      "Converter that transcodes MP3 audio to lossless FLAC so it imports correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert MP3 to FLAC for video editing",
        "hero_h1":          'Convert your <span class="accent">MP3 to FLAC</span> losslessly',
        "hero_sub":         'MP3 is everywhere, and it is also one of the formats video editors handle least gracefully in a professional timeline. Everything runs inside your browser with FFmpeg — not a single byte is uploaded to any server.',
        "seo_h2":           'Why convert <span class="accent">MP3 to FLAC</span>?',
        "seo_lede":         'MP3 is the format that made digital audio mainstream, and thirty years on it remains the most widely supported lossy codec there is. In video editing the story differs: many NLEs decode it inconsistently, and DaVinci Resolve on Linux does not decode it at all.',
        "breadcrumb_label": "Convert MP3 to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting MP3 to FLAC</h2>
      <h3>What MP3 actually is</h3>
      <p>MP3 is the format that made digital audio mainstream, and thirty years on it remains the most widely supported lossy codec there is. In video editing the story differs: many NLEs decode it inconsistently, and DaVinci Resolve on Linux does not decode it at all.</p>
      <h3>What this conversion does, and what it does not</h3>
      <p>Be clear about what this conversion does and does not do. FLAC preserves exactly what is in your MP3, including the artefacts the MP3 encoder introduced. The file gets larger and no better sounding. What you gain is a format your editor reads natively and that will not degrade again on re-export.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .mp3 file onto the upload area, or click <strong>Select files</strong>. You can queue several at once.</li>
        <li>Choose <strong>FLAC</strong> as the output format.</li>
        <li>Press <strong>Convert</strong>. The file is processed on your own machine and never uploaded.</li>
        <li>Download the FLAC and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If the source is 32-bit floating point audio, FLAC needs integer samples, so it is converted to 32-bit integer first — handled automatically and inaudible. If a file fails outright, open <strong>Technical details · FFmpeg</strong> and read the log: it usually names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-m4a-to-flac",
        "title":            "Convert M4A to FLAC – Apple Audio for Video Editing | VidToFLAC",
        "description":      'Convert M4A audio to lossless FLAC, 100% in your browser with FFmpeg. M4A is the Apple audio container, typical of Voice Memos, iTunes and anything recorded on an iPhone. No file uploads and no sign-up.',
        "keywords":         "convert M4A to FLAC, M4A FLAC DaVinci Resolve, m4a to flac converter, M4A audio editor compatibility",
        "canonical":        "https://vidtoflac.tech/en/convert-m4a-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-m4a-to-flac/",
        "og_title":         "Convert M4A to FLAC – Apple Audio for Video Editing | VidToFLAC",
        "og_desc":          'Convert M4A audio to lossless FLAC in your browser. M4A is the Apple audio container, typical of Voice Memos, iTunes and anything recorded on an iPhone.',
        "tw_title":         "Convert M4A to FLAC – Apple Audio for Video Editing | VidToFLAC",
        "tw_desc":          'Convert M4A audio to lossless FLAC in your browser. M4A is the Apple audio container, typical of Voice Memos, iTunes and anything recorded on an iPhone.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-m4a-to-flac/",
        "webapp_desc":      "Converter that transcodes M4A audio to lossless FLAC so it imports correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert M4A to FLAC for video editing",
        "hero_h1":          'Convert your <span class="accent">M4A to FLAC</span> losslessly',
        "hero_sub":         'M4A is the Apple audio container, typical of Voice Memos, iTunes and anything recorded on an iPhone. Everything runs inside your browser with FFmpeg — not a single byte is uploaded to any server.',
        "seo_h2":           'Why convert <span class="accent">M4A to FLAC</span>?',
        "seo_lede":         'An M4A is an MP4 container carrying audio only. Inside you will normally find AAC, though Apple Lossless (ALAC) also appears. Voice Memos, GarageBand exports and iTunes purchases all land in this format, and all of them tend to import silently into editors on Linux.',
        "breadcrumb_label": "Convert M4A to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting M4A to FLAC</h2>
      <h3>What M4A actually is</h3>
      <p>An M4A is an MP4 container carrying audio only. Inside you will normally find AAC, though Apple Lossless (ALAC) also appears. Voice Memos, GarageBand exports and iTunes purchases all land in this format, and all of them tend to import silently into editors on Linux.</p>
      <h3>What this conversion does, and what it does not</h3>
      <p>If your M4A holds ALAC rather than AAC, the conversion to FLAC is genuinely lossless end to end: both formats store the same samples, so nothing at all is discarded. If it holds AAC, the FLAC preserves that AAC exactly as it is, artefacts included.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .m4a file onto the upload area, or click <strong>Select files</strong>. You can queue several at once.</li>
        <li>Choose <strong>FLAC</strong> as the output format.</li>
        <li>Press <strong>Convert</strong>. The file is processed on your own machine and never uploaded.</li>
        <li>Download the FLAC and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If the source is 32-bit floating point audio, FLAC needs integer samples, so it is converted to 32-bit integer first — handled automatically and inaudible. If a file fails outright, open <strong>Technical details · FFmpeg</strong> and read the log: it usually names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-ogg-to-flac",
        "title":            "Convert OGG to FLAC – Vorbis Audio for Editors | VidToFLAC",
        "description":      'Convert OGG audio to lossless FLAC, 100% in your browser with FFmpeg. OGG Vorbis is the open codec behind a great deal of game audio, podcast archives and open-source software. No file uploads and no sign-up.',
        "keywords":         "convert OGG to FLAC, OGG FLAC DaVinci Resolve, ogg to flac converter, OGG audio editor compatibility",
        "canonical":        "https://vidtoflac.tech/en/convert-ogg-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-ogg-to-flac/",
        "og_title":         "Convert OGG to FLAC – Vorbis Audio for Editors | VidToFLAC",
        "og_desc":          'Convert OGG audio to lossless FLAC in your browser. OGG Vorbis is the open codec behind a great deal of game audio, podcast archives and open-source software.',
        "tw_title":         "Convert OGG to FLAC – Vorbis Audio for Editors | VidToFLAC",
        "tw_desc":          'Convert OGG audio to lossless FLAC in your browser. OGG Vorbis is the open codec behind a great deal of game audio, podcast archives and open-source software.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-ogg-to-flac/",
        "webapp_desc":      "Converter that transcodes OGG audio to lossless FLAC so it imports correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert OGG to FLAC for video editing",
        "hero_h1":          'Convert your <span class="accent">OGG to FLAC</span> losslessly',
        "hero_sub":         'OGG Vorbis is the open codec behind a great deal of game audio, podcast archives and open-source software. Everything runs inside your browser with FFmpeg — not a single byte is uploaded to any server.',
        "seo_h2":           'Why convert <span class="accent">OGG to FLAC</span>?',
        "seo_lede":         'Ogg is a container and Vorbis the codec usually inside it. Both are open and royalty-free, which is why they became standard in game engines, Wikipedia and Linux software. That same independence is why commercial video editors, built around industry codecs, rarely decode them.',
        "breadcrumb_label": "Convert OGG to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting OGG to FLAC</h2>
      <h3>What OGG actually is</h3>
      <p>Ogg is a container and Vorbis the codec usually inside it. Both are open and royalty-free, which is why they became standard in game engines, Wikipedia and Linux software. That same independence is why commercial video editors, built around industry codecs, rarely decode them.</p>
      <h3>What this conversion does, and what it does not</h3>
      <p>Vorbis is a capable codec and this conversion will not make it sound better. FLAC simply gives you something every editor reads, and guarantees no further generation loss.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .ogg file onto the upload area, or click <strong>Select files</strong>. You can queue several at once.</li>
        <li>Choose <strong>FLAC</strong> as the output format.</li>
        <li>Press <strong>Convert</strong>. The file is processed on your own machine and never uploaded.</li>
        <li>Download the FLAC and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If the source is 32-bit floating point audio, FLAC needs integer samples, so it is converted to 32-bit integer first — handled automatically and inaudible. If a file fails outright, open <strong>Technical details · FFmpeg</strong> and read the log: it usually names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-wma-to-flac",
        "title":            "Convert WMA to FLAC – Windows Media Audio for Editors | VidToFLAC",
        "description":      'Convert WMA audio to lossless FLAC, 100% in your browser with FFmpeg. WMA is the proprietary Microsoft audio format, still common in old recordings and Windows-era archives. No file uploads and no sign-up.',
        "keywords":         "convert WMA to FLAC, WMA FLAC DaVinci Resolve, wma to flac converter, WMA audio editor compatibility",
        "canonical":        "https://vidtoflac.tech/en/convert-wma-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-wma-to-flac/",
        "og_title":         "Convert WMA to FLAC – Windows Media Audio for Editors | VidToFLAC",
        "og_desc":          'Convert WMA audio to lossless FLAC in your browser. WMA is the proprietary Microsoft audio format, still common in old recordings and Windows-era archives.',
        "tw_title":         "Convert WMA to FLAC – Windows Media Audio for Editors | VidToFLAC",
        "tw_desc":          'Convert WMA audio to lossless FLAC in your browser. WMA is the proprietary Microsoft audio format, still common in old recordings and Windows-era archives.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-wma-to-flac/",
        "webapp_desc":      "Converter that transcodes WMA audio to lossless FLAC so it imports correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert WMA to FLAC for video editing",
        "hero_h1":          'Convert your <span class="accent">WMA to FLAC</span> losslessly',
        "hero_sub":         'WMA is the proprietary Microsoft audio format, still common in old recordings and Windows-era archives. Everything runs inside your browser with FFmpeg — not a single byte is uploaded to any server.',
        "seo_h2":           'Why convert <span class="accent">WMA to FLAC</span>?',
        "seo_lede":         'Windows Media Audio was the Microsoft answer to MP3 and shipped with every copy of Windows for years. Outside that ecosystem support has always been thin, and it has thinned further: on macOS and Linux almost nothing decodes it, DaVinci Resolve included.',
        "breadcrumb_label": "Convert WMA to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting WMA to FLAC</h2>
      <h3>What WMA actually is</h3>
      <p>Windows Media Audio was the Microsoft answer to MP3 and shipped with every copy of Windows for years. Outside that ecosystem support has always been thin, and it has thinned further: on macOS and Linux almost nothing decodes it, DaVinci Resolve included.</p>
      <h3>What this conversion does, and what it does not</h3>
      <p>WMA files usually come from old archives, so treat this as a rescue operation. Converting to FLAC preserves whatever is in the original and gives you a format that will still be readable in twenty years, which WMA increasingly will not.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .wma file onto the upload area, or click <strong>Select files</strong>. You can queue several at once.</li>
        <li>Choose <strong>FLAC</strong> as the output format.</li>
        <li>Press <strong>Convert</strong>. The file is processed on your own machine and never uploaded.</li>
        <li>Download the FLAC and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If the source is 32-bit floating point audio, FLAC needs integer samples, so it is converted to 32-bit integer first — handled automatically and inaudible. If a file fails outright, open <strong>Technical details · FFmpeg</strong> and read the log: it usually names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-aiff-to-flac",
        "title":            "Convert AIFF to FLAC – Halve the Size, Keep the Quality | VidToFLAC",
        "description":      'Convert AIFF audio to lossless FLAC, 100% in your browser with FFmpeg. AIFF is the Apple uncompressed format: lossless like WAV, and just as large. No file uploads and no sign-up.',
        "keywords":         "convert AIFF to FLAC, AIFF FLAC DaVinci Resolve, aiff to flac converter, AIFF audio editor compatibility",
        "canonical":        "https://vidtoflac.tech/en/convert-aiff-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-aiff-to-flac/",
        "og_title":         "Convert AIFF to FLAC – Halve the Size, Keep the Quality | VidToFLAC",
        "og_desc":          'Convert AIFF audio to lossless FLAC in your browser. AIFF is the Apple uncompressed format: lossless like WAV, and just as large.',
        "tw_title":         "Convert AIFF to FLAC – Halve the Size, Keep the Quality | VidToFLAC",
        "tw_desc":          'Convert AIFF audio to lossless FLAC in your browser. AIFF is the Apple uncompressed format: lossless like WAV, and just as large.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-aiff-to-flac/",
        "webapp_desc":      "Converter that transcodes AIFF audio to lossless FLAC so it imports correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert AIFF to FLAC for video editing",
        "hero_h1":          'Convert your <span class="accent">AIFF to FLAC</span> losslessly',
        "hero_sub":         'AIFF is the Apple uncompressed format: lossless like WAV, and just as large. Everything runs inside your browser with FFmpeg — not a single byte is uploaded to any server.',
        "seo_h2":           'Why convert <span class="accent">AIFF to FLAC</span>?',
        "seo_lede":         'AIFF (Audio Interchange File Format) is the Apple equivalent of WAV: uncompressed PCM audio, no quality loss, and files that grow enormous. It is the standard delivery format in a lot of Mac-based music production, and it is supported everywhere — it is simply wasteful.',
        "breadcrumb_label": "Convert AIFF to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting AIFF to FLAC</h2>
      <h3>What AIFF actually is</h3>
      <p>AIFF (Audio Interchange File Format) is the Apple equivalent of WAV: uncompressed PCM audio, no quality loss, and files that grow enormous. It is the standard delivery format in a lot of Mac-based music production, and it is supported everywhere — it is simply wasteful.</p>
      <h3>What this conversion does, and what it does not</h3>
      <p>Because AIFF is already lossless, converting to FLAC discards nothing whatsoever. You keep every sample and typically reclaim 40 to 60% of the disk space. This is the one conversion on this site with no trade-off to explain.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .aiff file onto the upload area, or click <strong>Select files</strong>. You can queue several at once.</li>
        <li>Choose <strong>FLAC</strong> as the output format.</li>
        <li>Press <strong>Convert</strong>. The file is processed on your own machine and never uploaded.</li>
        <li>Download the FLAC and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If the source is 32-bit floating point audio, FLAC needs integer samples, so it is converted to 32-bit integer first — handled automatically and inaudible. If a file fails outright, open <strong>Technical details · FFmpeg</strong> and read the log: it usually names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-opus-to-flac",
        "title":            "Convert Opus to FLAC – Discord and Streaming Audio for Editors | VidToFLAC",
        "description":      'Convert Opus audio to lossless FLAC, 100% in your browser with FFmpeg. Opus is the default in Discord, streaming and video calls, and almost no video editor reads it. No file uploads and no sign-up.',
        "keywords":         "convert Opus to FLAC, Opus FLAC DaVinci Resolve, opus to flac converter, Opus audio editor compatibility",
        "canonical":        "https://vidtoflac.tech/en/convert-opus-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-opus-to-flac/",
        "og_title":         "Convert Opus to FLAC – Discord and Streaming Audio for Editors | VidToFLAC",
        "og_desc":          'Convert Opus audio to lossless FLAC in your browser. Opus is the default in Discord, streaming and video calls, and almost no video editor reads it.',
        "tw_title":         "Convert Opus to FLAC – Discord and Streaming Audio for Editors | VidToFLAC",
        "tw_desc":          'Convert Opus audio to lossless FLAC in your browser. Opus is the default in Discord, streaming and video calls, and almost no video editor reads it.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-opus-to-flac/",
        "webapp_desc":      "Converter that transcodes Opus audio to lossless FLAC so it imports correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert Opus to FLAC for video editing",
        "hero_h1":          'Convert your <span class="accent">Opus to FLAC</span> losslessly',
        "hero_sub":         'Opus is the default in Discord, streaming and video calls, and almost no video editor reads it. Everything runs inside your browser with FFmpeg — not a single byte is uploaded to any server.',
        "seo_h2":           'Why convert <span class="accent">Opus to FLAC</span>?',
        "seo_lede":         'Opus is the best lossy codec available at low bitrates, which is why Discord, WhatsApp, Zoom and WebRTC all adopted it. It is also recent and open, and the professional editing world settled on its codecs long before Opus existed. The result is that recordings of calls and Discord sessions import silently.',
        "breadcrumb_label": "Convert Opus to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting Opus to FLAC</h2>
      <h3>What Opus actually is</h3>
      <p>Opus is the best lossy codec available at low bitrates, which is why Discord, WhatsApp, Zoom and WebRTC all adopted it. It is also recent and open, and the professional editing world settled on its codecs long before Opus existed. The result is that recordings of calls and Discord sessions import silently.</p>
      <h3>What this conversion does, and what it does not</h3>
      <p>Nothing about converting Opus to FLAC improves the audio — Opus already performed the lossy compression, and that is permanent. The point is purely that your editor can read the result.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .opus file onto the upload area, or click <strong>Select files</strong>. You can queue several at once.</li>
        <li>Choose <strong>FLAC</strong> as the output format.</li>
        <li>Press <strong>Convert</strong>. The file is processed on your own machine and never uploaded.</li>
        <li>Download the FLAC and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>If the source is 32-bit floating point audio, FLAC needs integer samples, so it is converted to 32-bit integer first — handled automatically and inaudible. If a file fails outright, open <strong>Technical details · FFmpeg</strong> and read the log: it usually names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-wmv-to-flac",
        "title":            "Convert WMV to FLAC – Windows Media Video for Editors | VidToFLAC",
        "description":      'Convert WMV audio to lossless FLAC, 100% in your browser with FFmpeg. WMV is the Microsoft video format, and outside Windows almost nothing opens it cleanly. No file uploads and no sign-up.',
        "keywords":         "convert WMV to FLAC, WMV FLAC DaVinci Resolve, wmv no sound editor, WMV audio conversion browser",
        "canonical":        "https://vidtoflac.tech/en/convert-wmv-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-wmv-to-flac/",
        "og_title":         "Convert WMV to FLAC – Windows Media Video for Editors | VidToFLAC",
        "og_desc":          'Convert WMV audio to lossless FLAC in your browser. WMV is the Microsoft video format, and outside Windows almost nothing opens it cleanly.',
        "tw_title":         "Convert WMV to FLAC – Windows Media Video for Editors | VidToFLAC",
        "tw_desc":          'Convert WMV audio to lossless FLAC in your browser. WMV is the Microsoft video format, and outside Windows almost nothing opens it cleanly.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-wmv-to-flac/",
        "webapp_desc":      "Converter that turns the audio of WMV files into lossless FLAC inside an MKV, so they import correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert WMV audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">WMV to FLAC</span> and get the sound back',
        "hero_sub":         'WMV is the Microsoft video format, and outside Windows almost nothing opens it cleanly. Everything runs inside your browser — not a single byte is uploaded to any server.',
        "seo_h2":           'Why does <span class="accent">your WMV import without sound</span>?',
        "seo_lede":         'WMV wraps VC-1 or WMV3 video with WMA audio, and both are proprietary Microsoft codecs. On Windows with the right components installed it plays; on macOS and Linux it usually does not, and DaVinci Resolve rejects it on every platform more often than not.',
        "breadcrumb_label": "Convert WMV to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting WMV to FLAC</h2>
      <h3>What WMV actually is</h3>
      <p>WMV wraps VC-1 or WMV3 video with WMA audio, and both are proprietary Microsoft codecs. On Windows with the right components installed it plays; on macOS and Linux it usually does not, and DaVinci Resolve rejects it on every platform more often than not.</p>
      <h3>What VidToFLAC does with it</h3>
      <p>Neither the video nor the audio can be decoded in the browser, so both are re-encoded: video to H.264, audio to FLAC. That means this is a full conversion rather than a remux, so it takes longer and the video is not bit-for-bit identical. At <code>-crf 18</code> the difference is not visible in practice, and it is the most practical way to make the clip editable outside the Windows Media ecosystem.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .wmv file onto the upload area, or click <strong>Select files</strong>.</li>
        <li>Choose <strong>MKV</strong> as the output — modern editors handle it best.</li>
        <li>Press <strong>Convert</strong>. Everything is processed on your own machine, with no uploads.</li>
        <li>Download the result and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Older formats are frequently <strong>interlaced</strong>; converting the audio does not deinterlace the picture, so handle that in your editor's clip attributes. Large files can exhaust the browser's memory — the practical ceiling is around 1 GB — so split long recordings before converting. If a file fails, open <strong>Technical details · FFmpeg</strong>: the log names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-flv-to-flac",
        "title":            "Convert FLV to FLAC – Rescue Audio From Flash Video | VidToFLAC",
        "description":      'Convert FLV audio to lossless FLAC, 100% in your browser with FFmpeg. FLV is the old Flash video format, common in archived web recordings and screencasts. No file uploads and no sign-up.',
        "keywords":         "convert FLV to FLAC, FLV FLAC DaVinci Resolve, flv no sound editor, FLV audio conversion browser",
        "canonical":        "https://vidtoflac.tech/en/convert-flv-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-flv-to-flac/",
        "og_title":         "Convert FLV to FLAC – Rescue Audio From Flash Video | VidToFLAC",
        "og_desc":          'Convert FLV audio to lossless FLAC in your browser. FLV is the old Flash video format, common in archived web recordings and screencasts.',
        "tw_title":         "Convert FLV to FLAC – Rescue Audio From Flash Video | VidToFLAC",
        "tw_desc":          'Convert FLV audio to lossless FLAC in your browser. FLV is the old Flash video format, common in archived web recordings and screencasts.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-flv-to-flac/",
        "webapp_desc":      "Converter that turns the audio of FLV files into lossless FLAC inside an MKV, so they import correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert FLV audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">FLV to FLAC</span> and get the sound back',
        "hero_sub":         'FLV is the old Flash video format, common in archived web recordings and screencasts. Everything runs inside your browser — not a single byte is uploaded to any server.',
        "seo_h2":           'Why does <span class="accent">your FLV import without sound</span>?',
        "seo_lede":         'FLV was the format of web video for over a decade, until Flash was retired in 2020. What survives is archives: old screencasts, downloaded lectures, recordings from long-dead platforms. Inside you might find H.264 with AAC, which modern software reads, or legacy Sorenson and VP6 video with MP3 or Nellymoser audio, which it does not.',
        "breadcrumb_label": "Convert FLV to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting FLV to FLAC</h2>
      <h3>What FLV actually is</h3>
      <p>FLV was the format of web video for over a decade, until Flash was retired in 2020. What survives is archives: old screencasts, downloaded lectures, recordings from long-dead platforms. Inside you might find H.264 with AAC, which modern software reads, or legacy Sorenson and VP6 video with MP3 or Nellymoser audio, which it does not.</p>
      <h3>What VidToFLAC does with it</h3>
      <p>If the video is H.264 it is copied across untouched. If it is a legacy Flash codec the browser cannot decode, it is re-encoded to H.264 — which is what you want anyway, since nothing modern edits VP6 comfortably. The audio always becomes FLAC.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .flv file onto the upload area, or click <strong>Select files</strong>.</li>
        <li>Choose <strong>MKV</strong> as the output — modern editors handle it best.</li>
        <li>Press <strong>Convert</strong>. Everything is processed on your own machine, with no uploads.</li>
        <li>Download the result and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Older formats are frequently <strong>interlaced</strong>; converting the audio does not deinterlace the picture, so handle that in your editor's clip attributes. Large files can exhaust the browser's memory — the practical ceiling is around 1 GB — so split long recordings before converting. If a file fails, open <strong>Technical details · FFmpeg</strong>: the log names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-vob-to-flac",
        "title":            "Convert VOB to FLAC – DVD Audio for Video Editing | VidToFLAC",
        "description":      'Convert VOB audio to lossless FLAC, 100% in your browser with FFmpeg. VOB is the DVD video format, with MPEG-2 video and AC3 audio that editors rarely decode. No file uploads and no sign-up.',
        "keywords":         "convert VOB to FLAC, VOB FLAC DaVinci Resolve, vob no sound editor, VOB audio conversion browser",
        "canonical":        "https://vidtoflac.tech/en/convert-vob-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-vob-to-flac/",
        "og_title":         "Convert VOB to FLAC – DVD Audio for Video Editing | VidToFLAC",
        "og_desc":          'Convert VOB audio to lossless FLAC in your browser. VOB is the DVD video format, with MPEG-2 video and AC3 audio that editors rarely decode.',
        "tw_title":         "Convert VOB to FLAC – DVD Audio for Video Editing | VidToFLAC",
        "tw_desc":          'Convert VOB audio to lossless FLAC in your browser. VOB is the DVD video format, with MPEG-2 video and AC3 audio that editors rarely decode.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-vob-to-flac/",
        "webapp_desc":      "Converter that turns the audio of VOB files into lossless FLAC inside an MKV, so they import correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert VOB audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">VOB to FLAC</span> and get the sound back',
        "hero_sub":         'VOB is the DVD video format, with MPEG-2 video and AC3 audio that editors rarely decode. Everything runs inside your browser — not a single byte is uploaded to any server.',
        "seo_h2":           'Why does <span class="accent">your VOB import without sound</span>?',
        "seo_lede":         'A VOB is what sits inside the VIDEO_TS folder of a DVD: MPEG-2 video paired with AC3 (Dolby Digital) or PCM audio. Both are licensed codecs, and AC3 in particular is one DaVinci Resolve does not decode on Linux and handles unevenly elsewhere.',
        "breadcrumb_label": "Convert VOB to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting VOB to FLAC</h2>
      <h3>What VOB actually is</h3>
      <p>A VOB is what sits inside the VIDEO_TS folder of a DVD: MPEG-2 video paired with AC3 (Dolby Digital) or PCM audio. Both are licensed codecs, and AC3 in particular is one DaVinci Resolve does not decode on Linux and handles unevenly elsewhere.</p>
      <h3>What VidToFLAC does with it</h3>
      <p>MPEG-2 cannot be decoded in the browser, so the video is re-encoded to H.264 and the AC3 becomes FLAC. Note that VOB files from commercial DVDs are usually encrypted with CSS; those cannot be processed by any tool without circumventing the protection, and this one will not open them.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .vob file onto the upload area, or click <strong>Select files</strong>.</li>
        <li>Choose <strong>MKV</strong> as the output — modern editors handle it best.</li>
        <li>Press <strong>Convert</strong>. Everything is processed on your own machine, with no uploads.</li>
        <li>Download the result and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Older formats are frequently <strong>interlaced</strong>; converting the audio does not deinterlace the picture, so handle that in your editor's clip attributes. Large files can exhaust the browser's memory — the practical ceiling is around 1 GB — so split long recordings before converting. If a file fails, open <strong>Technical details · FFmpeg</strong>: the log names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-ts-to-flac",
        "title":            "Convert TS to FLAC – Broadcast and Recording Streams | VidToFLAC",
        "description":      'Convert TS audio to lossless FLAC, 100% in your browser with FFmpeg. TS is the MPEG transport stream used by digital TV, capture cards and stream recorders. No file uploads and no sign-up.',
        "keywords":         "convert TS to FLAC, TS FLAC DaVinci Resolve, ts no sound editor, TS audio conversion browser",
        "canonical":        "https://vidtoflac.tech/en/convert-ts-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-ts-to-flac/",
        "og_title":         "Convert TS to FLAC – Broadcast and Recording Streams | VidToFLAC",
        "og_desc":          'Convert TS audio to lossless FLAC in your browser. TS is the MPEG transport stream used by digital TV, capture cards and stream recorders.',
        "tw_title":         "Convert TS to FLAC – Broadcast and Recording Streams | VidToFLAC",
        "tw_desc":          'Convert TS audio to lossless FLAC in your browser. TS is the MPEG transport stream used by digital TV, capture cards and stream recorders.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-ts-to-flac/",
        "webapp_desc":      "Converter that turns the audio of TS files into lossless FLAC inside an MKV, so they import correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert TS audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">TS to FLAC</span> and get the sound back',
        "hero_sub":         'TS is the MPEG transport stream used by digital TV, capture cards and stream recorders. Everything runs inside your browser — not a single byte is uploaded to any server.',
        "seo_h2":           'Why does <span class="accent">your TS import without sound</span>?',
        "seo_lede":         'MPEG-TS was designed for broadcast: a stream of small packets that survives transmission errors and can be tuned into halfway through. That makes it ideal for digital television and capture hardware, and awkward for editing, because it has no clean index and often carries several programmes at once.',
        "breadcrumb_label": "Convert TS to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting TS to FLAC</h2>
      <h3>What TS actually is</h3>
      <p>MPEG-TS was designed for broadcast: a stream of small packets that survives transmission errors and can be tuned into halfway through. That makes it ideal for digital television and capture hardware, and awkward for editing, because it has no clean index and often carries several programmes at once.</p>
      <h3>What VidToFLAC does with it</h3>
      <p>TS files usually hold H.264 or MPEG-2 video. If it is H.264 the video is copied across untouched; MPEG-2 is re-encoded to H.264 because the browser cannot decode it. Either way the audio, typically AC3 or AAC, becomes FLAC and the result imports cleanly.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .ts file onto the upload area, or click <strong>Select files</strong>.</li>
        <li>Choose <strong>MKV</strong> as the output — modern editors handle it best.</li>
        <li>Press <strong>Convert</strong>. Everything is processed on your own machine, with no uploads.</li>
        <li>Download the result and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Older formats are frequently <strong>interlaced</strong>; converting the audio does not deinterlace the picture, so handle that in your editor's clip attributes. Large files can exhaust the browser's memory — the practical ceiling is around 1 GB — so split long recordings before converting. If a file fails, open <strong>Technical details · FFmpeg</strong>: the log names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-m4v-to-flac",
        "title":            "Convert M4V to FLAC – Apple Video for Editing | VidToFLAC",
        "description":      'Convert M4V audio to lossless FLAC, 100% in your browser with FFmpeg. M4V is the Apple video container, used by iTunes, Apple TV and iPhone exports. No file uploads and no sign-up.',
        "keywords":         "convert M4V to FLAC, M4V FLAC DaVinci Resolve, m4v no sound editor, M4V audio conversion browser",
        "canonical":        "https://vidtoflac.tech/en/convert-m4v-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-m4v-to-flac/",
        "og_title":         "Convert M4V to FLAC – Apple Video for Editing | VidToFLAC",
        "og_desc":          'Convert M4V audio to lossless FLAC in your browser. M4V is the Apple video container, used by iTunes, Apple TV and iPhone exports.',
        "tw_title":         "Convert M4V to FLAC – Apple Video for Editing | VidToFLAC",
        "tw_desc":          'Convert M4V audio to lossless FLAC in your browser. M4V is the Apple video container, used by iTunes, Apple TV and iPhone exports.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-m4v-to-flac/",
        "webapp_desc":      "Converter that turns the audio of M4V files into lossless FLAC inside an MKV, so they import correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert M4V audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">M4V to FLAC</span> and get the sound back',
        "hero_sub":         'M4V is the Apple video container, used by iTunes, Apple TV and iPhone exports. Everything runs inside your browser — not a single byte is uploaded to any server.',
        "seo_h2":           'Why does <span class="accent">your M4V import without sound</span>?',
        "seo_lede":         'M4V is essentially MP4 with an Apple label, and the contents are much the same: H.264 or HEVC video with AAC audio. The difference that matters is that M4V files bought from iTunes carry FairPlay DRM, which changes what is possible entirely.',
        "breadcrumb_label": "Convert M4V to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting M4V to FLAC</h2>
      <h3>What M4V actually is</h3>
      <p>M4V is essentially MP4 with an Apple label, and the contents are much the same: H.264 or HEVC video with AAC audio. The difference that matters is that M4V files bought from iTunes carry FairPlay DRM, which changes what is possible entirely.</p>
      <h3>What VidToFLAC does with it</h3>
      <p>For your own exports the conversion is straightforward: the audio becomes FLAC, and the video is copied if it is H.264 or re-encoded if it is HEVC. For DRM-protected purchases nothing can be done — the file is encrypted and no tool opens it legally, this one included.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .m4v file onto the upload area, or click <strong>Select files</strong>.</li>
        <li>Choose <strong>MKV</strong> as the output — modern editors handle it best.</li>
        <li>Press <strong>Convert</strong>. Everything is processed on your own machine, with no uploads.</li>
        <li>Download the result and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Older formats are frequently <strong>interlaced</strong>; converting the audio does not deinterlace the picture, so handle that in your editor's clip attributes. Large files can exhaust the browser's memory — the practical ceiling is around 1 GB — so split long recordings before converting. If a file fails, open <strong>Technical details · FFmpeg</strong>: the log names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-mpeg-to-flac",
        "title":            "Convert MPEG to FLAC – Legacy Video for Modern Editors | VidToFLAC",
        "description":      'Convert MPEG audio to lossless FLAC, 100% in your browser with FFmpeg. MPEG-1 and MPEG-2 files come from VCDs, old capture hardware and broadcast archives. No file uploads and no sign-up.',
        "keywords":         "convert MPEG to FLAC, MPEG FLAC DaVinci Resolve, mpeg no sound editor, MPEG audio conversion browser",
        "canonical":        "https://vidtoflac.tech/en/convert-mpeg-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-mpeg-to-flac/",
        "og_title":         "Convert MPEG to FLAC – Legacy Video for Modern Editors | VidToFLAC",
        "og_desc":          'Convert MPEG audio to lossless FLAC in your browser. MPEG-1 and MPEG-2 files come from VCDs, old capture hardware and broadcast archives.',
        "tw_title":         "Convert MPEG to FLAC – Legacy Video for Modern Editors | VidToFLAC",
        "tw_desc":          'Convert MPEG audio to lossless FLAC in your browser. MPEG-1 and MPEG-2 files come from VCDs, old capture hardware and broadcast archives.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-mpeg-to-flac/",
        "webapp_desc":      "Converter that turns the audio of MPEG files into lossless FLAC inside an MKV, so they import correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert MPEG audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">MPEG to FLAC</span> and get the sound back',
        "hero_sub":         'MPEG-1 and MPEG-2 files come from VCDs, old capture hardware and broadcast archives. Everything runs inside your browser — not a single byte is uploaded to any server.',
        "seo_h2":           'Why does <span class="accent">your MPEG import without sound</span>?',
        "seo_lede":         'MPEG is the family of standards that digital video began with. MPEG-1 gave us the Video CD and the MP3; MPEG-2 gave us the DVD and digital television. Files in these formats are usually old, often interlaced, and carry MP2 or AC3 audio that modern editors decode poorly if at all.',
        "breadcrumb_label": "Convert MPEG to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting MPEG to FLAC</h2>
      <h3>What MPEG actually is</h3>
      <p>MPEG is the family of standards that digital video began with. MPEG-1 gave us the Video CD and the MP3; MPEG-2 gave us the DVD and digital television. Files in these formats are usually old, often interlaced, and carry MP2 or AC3 audio that modern editors decode poorly if at all.</p>
      <h3>What VidToFLAC does with it</h3>
      <p>Neither MPEG-1 nor MPEG-2 video can be decoded in the browser, so the picture is re-encoded to H.264 and the audio becomes FLAC. The result is far easier to edit than the original, though it is a full conversion rather than a remux.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .mpeg file onto the upload area, or click <strong>Select files</strong>.</li>
        <li>Choose <strong>MKV</strong> as the output — modern editors handle it best.</li>
        <li>Press <strong>Convert</strong>. Everything is processed on your own machine, with no uploads.</li>
        <li>Download the result and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Older formats are frequently <strong>interlaced</strong>; converting the audio does not deinterlace the picture, so handle that in your editor's clip attributes. Large files can exhaust the browser's memory — the practical ceiling is around 1 GB — so split long recordings before converting. If a file fails, open <strong>Technical details · FFmpeg</strong>: the log names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    {
        "slug":             "convert-3gp-to-flac",
        "title":            "Convert 3GP to FLAC – Mobile Recordings for Editors | VidToFLAC",
        "description":      'Convert 3GP audio to lossless FLAC, 100% in your browser with FFmpeg. 3GP is the old mobile phone video format, with AMR audio that almost nothing decodes. No file uploads and no sign-up.',
        "keywords":         "convert 3GP to FLAC, 3GP FLAC DaVinci Resolve, 3gp no sound editor, 3GP audio conversion browser",
        "canonical":        "https://vidtoflac.tech/en/convert-3gp-to-flac/",
        "og_url":           "https://vidtoflac.tech/en/convert-3gp-to-flac/",
        "og_title":         "Convert 3GP to FLAC – Mobile Recordings for Editors | VidToFLAC",
        "og_desc":          'Convert 3GP audio to lossless FLAC in your browser. 3GP is the old mobile phone video format, with AMR audio that almost nothing decodes.',
        "tw_title":         "Convert 3GP to FLAC – Mobile Recordings for Editors | VidToFLAC",
        "tw_desc":          'Convert 3GP audio to lossless FLAC in your browser. 3GP is the old mobile phone video format, with AMR audio that almost nothing decodes.',
        "webapp_url":       "https://vidtoflac.tech/en/convert-3gp-to-flac/",
        "webapp_desc":      "Converter that turns the audio of 3GP files into lossless FLAC inside an MKV, so they import correctly into DaVinci Resolve, Premiere and Avid. Runs 100% in the browser with FFmpeg (WebAssembly), with no file uploads.",
        "howto_name":       "How to convert 3GP audio to FLAC for DaVinci Resolve",
        "hero_h1":          'Convert your <span class="accent">3GP to FLAC</span> and get the sound back',
        "hero_sub":         '3GP is the old mobile phone video format, with AMR audio that almost nothing decodes. Everything runs inside your browser — not a single byte is uploaded to any server.',
        "seo_h2":           'Why does <span class="accent">your 3GP import without sound</span>?',
        "seo_lede":         '3GP was designed for early mobile networks, when bandwidth was measured in kilobits. It pairs H.263 or MPEG-4 video with AMR audio, a codec built for speech at very low bitrates. Files in this format are usually old phone recordings or voice notes, and their audio is rarely readable by editing software.',
        "breadcrumb_label": "Convert 3GP to FLAC",
        "unique_guide":     """\
  <section class="card seo-card" aria-labelledby="guia-formato-titulo">
    <div class="card-title">Conversion guide</div>
    <article>
      <h2 id="guia-formato-titulo">Everything about converting 3GP to FLAC</h2>
      <h3>What 3GP actually is</h3>
      <p>3GP was designed for early mobile networks, when bandwidth was measured in kilobits. It pairs H.263 or MPEG-4 video with AMR audio, a codec built for speech at very low bitrates. Files in this format are usually old phone recordings or voice notes, and their audio is rarely readable by editing software.</p>
      <h3>What VidToFLAC does with it</h3>
      <p>AMR is decoded and re-encoded to FLAC. Be realistic about the result: AMR discards a great deal to hit its bitrate, and FLAC preserves exactly what remains — it cannot restore what was never stored. The video, usually H.263, is re-encoded to H.264 because the browser cannot decode it.</p>
      <h3>Step by step</h3>
      <ol>
        <li>Drop your .3gp file onto the upload area, or click <strong>Select files</strong>.</li>
        <li>Choose <strong>MKV</strong> as the output — modern editors handle it best.</li>
        <li>Press <strong>Convert</strong>. Everything is processed on your own machine, with no uploads.</li>
        <li>Download the result and import it into your editor.</li>
      </ol>
      <h3>Common problems and what to do</h3>
      <p>Older formats are frequently <strong>interlaced</strong>; converting the audio does not deinterlace the picture, so handle that in your editor's clip attributes. Large files can exhaust the browser's memory — the practical ceiling is around 1 GB — so split long recordings before converting. If a file fails, open <strong>Technical details · FFmpeg</strong>: the log names the codec that could not be decoded.</p>
    </article>
  </section>""",
    },
    # <<PAGES_END>>
]

CONTENT_EN = {
    "convert-mp4-to-flac": {
        "faq_h2": "Frequently asked questions about converting MP4 to FLAC",
        "seo_body": """\
      <h3>The fix for your MP4: remux to MKV with FLAC audio</h3>
      <p>The trick is to separate the two halves of the problem. The <strong>video</strong> in your MP4 — normally H.264 or H.265 — is almost always perfectly compatible; what DaVinci Resolve cannot stomach is the <strong>AAC or MP3 audio</strong>. VidToFLAC repackages the MP4 into an <strong>MKV</strong> container, copying the video across <strong>bit for bit</strong> and re-encoding only the audio track to lossless <strong>FLAC</strong>.</p>

      <p>Because the video is never recompressed, no quality is lost and the job is far quicker than a full conversion. The resulting MKV imports with sound into DaVinci Resolve, Premiere Pro and Avid, with no codecs or plugins to install.</p>

      <p>If your MP4 carries video the browser cannot decode — HEVC/H.265 on some machines, for instance — VidToFLAC re-encodes it to H.264 at high quality so that preview works on the page. The audio still ends up as FLAC either way.</p>""",
        "faqs": [
            ("Do I lose video quality converting an MP4 to FLAC?",
             "If the video is H.264 it is copied <strong>bit for bit</strong> without recompression: that is a remux, not a re-encode. If it is <strong>H.265/HEVC</strong> the browser cannot decode it, so the video is re-encoded to H.264 at high quality (<code>-crf 18</code>) — very close to the original, though not bit-for-bit identical. The audio becomes FLAC, which is lossless, in both cases."),
            ("Why does DaVinci Resolve open my MP4 but play no sound?",
             "Because the MP4 stores its audio as <strong>AAC or MP3</strong>, and the free DaVinci Resolve — especially on Linux — ships no licence to decode them. The video decoders are included, which is why you see the picture but hear nothing."),
            ("Does this work for MP4s recorded with OBS Studio or a phone?",
             "Yes. MP4s from OBS, smartphones, cameras and capture cards all use AAC audio, which is exactly the source of the problem. VidToFLAC repackages them without touching the video."),
            ("Does it work with H.265 (HEVC) MP4 files?",
             "Yes. The audio is converted to FLAC regardless. If your browser cannot decode the HEVC video for on-page preview, VidToFLAC re-encodes it to H.264 — which is also what DaVinci Resolve Free prefers, since it struggles with HEVC in its own right."),
            ("How long does a large MP4 take?",
             "When it is a remux the video is never re-rendered, so the time depends mostly on reading and writing the file rather than on its duration. The exact figure depends on the file size, your machine, and whether the video needs re-encoding."),
        ],
    },
    "convert-mkv-to-flac": {
        "faq_h2": "Frequently asked questions about converting MKV to FLAC",
        "seo_body": """\
      <h3>The fix for your MKV: swap the audio, keep the container</h3>
      <p>Because <strong>MKV is already the output container</strong>, nothing about the packaging has to change. VidToFLAC copies the video stream across untouched and re-encodes only the audio track to lossless <strong>FLAC</strong>. The file you get back is the same MKV in every respect that matters, with an audio track DaVinci Resolve can actually read.</p>

      <p>This is the cleanest case on the whole site: when the video codec can be copied, nothing is decoded, nothing is recompressed, and the picture that comes out is identical to the one that went in.</p>

      <p>If the MKV carries <strong>H.265/HEVC</strong> video, the browser cannot decode it for preview and VidToFLAC re-encodes it to H.264 at high quality. Everything else is copied as-is.</p>""",
        "faqs": [
            ("Do I lose quality converting an MKV to FLAC?",
             "If the video codec can be copied — H.264, VP9 and similar — it is copied <strong>bit for bit</strong> and the picture is exactly the original. If the MKV holds <strong>H.265/HEVC</strong> it is re-encoded to H.264 at high quality. Only the audio track changes in either case, and FLAC is lossless."),
            ("Why does my OBS recording have no audio in DaVinci Resolve?",
             "OBS records <strong>AAC</strong> audio by default, sometimes Opus, and DaVinci Resolve — most notably on Linux — ships no decoder for either. Converting that track to FLAC inside the same MKV restores the sound."),
            ("Is there a size limit for an MKV?",
             "We impose none: processing happens on your own computer with FFmpeg (WebAssembly) and nothing is uploaded. The practical ceiling is the WebAssembly engine's memory — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file."),
            ("What if my MKV has several audio tracks?",
             "All of them are converted to FLAC and kept in the output. That matters for OBS recordings that capture game audio and a microphone on separate tracks — you keep the ability to mix them in your editor."),
            ("Can I keep MKV instead of converting to MP4?",
             "Yes, and you should. DaVinci Resolve handles MKV without trouble, and MP4 does not officially support FLAC audio. Staying with MKV is the path of least resistance."),
        ],
    },
    "convert-mov-to-flac": {
        "faq_h2": "Frequently asked questions about converting MOV to FLAC",
        "seo_body": """\
      <h3>The fix for your MOV: remux to MKV with FLAC audio</h3>
      <p>MOV files from iPhone, GoPro and most cameras store their audio as <strong>AAC</strong>, the codec DaVinci Resolve cannot decode without a licence. VidToFLAC repackages the MOV into an <strong>MKV</strong> and re-encodes only that audio track to lossless <strong>FLAC</strong>, leaving the picture alone wherever it can.</p>

      <p>If the video is H.264, it is copied across <strong>bit for bit</strong> and the image is exactly the original. iPhones have recorded in <strong>HEVC</strong> since iOS 11, and that codec cannot be decoded in the browser, so it is re-encoded to H.264 at high quality — visually very close, though not bit-for-bit identical.</p>

      <p>The resulting MKV imports with sound into DaVinci Resolve, Premiere Pro and Avid on Windows, macOS and Linux alike.</p>""",
        "faqs": [
            ("Will I lose quality converting an iPhone MOV?",
             "If the video is H.264 it is copied <strong>bit for bit</strong> and the recording is identical. iPhones record in <strong>HEVC</strong> by default since iOS 11, and that codec cannot be decoded in the browser, so it is re-encoded to H.264 at high quality (<code>-crf 18</code>) — very close to the original, but not bit-for-bit identical. The audio becomes lossless FLAC in both cases."),
            ("My GoPro MOV imports into Resolve without audio. Why?",
             "GoPro records audio as <strong>AAC</strong>, which DaVinci Resolve does not decode out of the box, least of all on Linux. Moving that audio into FLAC inside an MKV restores the sound."),
            ("What if my MOV is ProRes?",
             "ProRes cannot be decoded in the browser, so VidToFLAC re-encodes the video to H.264 to make preview work, and leaves the audio as FLAC. For ProRes masters you want kept intact, use desktop FFmpeg instead."),
            ("Does it work with MOV files from Sony, Canon and Fujifilm?",
             "Yes. These cameras write H.264 or H.265 video with AAC or PCM audio. AAC is the one that causes the silence, and it is exactly what this conversion replaces."),
            ("Is my MOV uploaded anywhere?",
             "No. Everything runs inside your browser through FFmpeg compiled to WebAssembly. The file never leaves your device, which is also why there is no server-imposed size limit."),
        ],
    },
    "convert-wav-to-flac": {
        "faq_h2": "Frequently asked questions about converting WAV to FLAC",
        "seo_body": """\
      <h3>The point of WAV to FLAC: same audio, half the size</h3>
      <p>This conversion is not about fixing anything — WAV already works in every editor. It is about <strong>size</strong>. WAV stores audio completely uncompressed, so a stereo file at 48 kHz and 24 bit consumes about 250 MB per hour, and multitrack sessions multiply that quickly.</p>

      <p><strong>FLAC compresses losslessly</strong>, the way ZIP does: it finds redundancy and stores it more efficiently, and decoding returns exactly the original samples. Typically that means <strong>40 to 60% less space</strong> for audio that is bit-for-bit identical to what you started with.</p>

      <p>DaVinci Resolve, Premiere Pro, Avid and Final Cut all read FLAC natively, so there is no compatibility cost to pay for the saving.</p>""",
        "faqs": [
            ("Do I lose any quality converting WAV to FLAC?",
             "None at all. FLAC is <strong>lossless</strong>: it stores exactly the same samples as the WAV, just packed more efficiently. Convert back and you get the original data bit for bit. The only thing that changes is the file size."),
            ("How much smaller will my file be?",
             "Usually <strong>40 to 60%</strong>, though it depends on the material. Speech, podcasts and recordings with silence compress most; dense loud music compresses least. The only way to know your figure is to convert and compare."),
            ("When should I stay with WAV instead?",
             "When a delivery specification demands PCM explicitly, when your hardware cannot read FLAC — some older field recorders are PCM-only — or for temporary scratch files nobody will keep, where the encoding time is not worth it."),
            ("What about 32-bit float WAV files from USB microphones?",
             "FLAC only stores integer samples, so a <code>pcm_f32le</code> source is converted to 32-bit integer first. This happens automatically and is inaudible, but it does mean the conversion is not a pure repackage in that particular case."),
            ("Can DaVinci Resolve read FLAC on Linux?",
             "Yes. FLAC is one of the formats DaVinci Resolve decodes natively on Windows, macOS and Linux, in both the free edition and Studio, which is exactly why it is the recommended target here."),
        ],
    },
    "convert-aac-to-flac": {
        "faq_h2": "Frequently asked questions about converting AAC to FLAC",
        "seo_body": """\
      <h3>The fix for your AAC files: transcode the audio to FLAC</h3>
      <p>AAC turns up in MP4 and MOV files from cameras, phones and OBS. AAC is patent-encumbered, and the free DaVinci Resolve ships no licence to decode it — most visibly on Linux, where it fails outright.</p>

      <p>VidToFLAC decodes the AAC audio and re-encodes it to <strong>FLAC</strong>, an open lossless format that DaVinci Resolve, Premiere Pro, Avid and Final Cut all read natively on Windows, macOS and Linux. The whole job runs inside your browser through FFmpeg compiled to WebAssembly, so the file never leaves your machine.</p>

      <p>Nothing is recovered that AAC already discarded; FLAC preserves what remains, exactly, and every editor can read it.</p>""",
        "faqs": [
            ("Does converting AAC to FLAC improve the audio quality?",
             'No, and it is worth being clear about that. AAC is a lossy format: data was discarded when the file was created, and nothing can bring it back. FLAC preserves exactly what remains, so no further quality is lost from this point on — but it does not restore anything.'),
            ("Why will my editor not read AAC files?",
             'AAC is patent-encumbered, and the free DaVinci Resolve ships no licence to decode it — most visibly on Linux, where it fails outright. FLAC is the practical way around it, because it is one of the few lossless formats every major editor decodes natively.'),
            ("Will the FLAC file be bigger than the AAC?",
             'Usually yes, and sometimes by a lot. AAC is lossy and already threw data away to get small; FLAC is lossless and stores everything that is left. You are trading disk space for compatibility and for no further generation loss.'),
            ("Is my file uploaded to a server?",
             "No. Everything runs inside your browser through FFmpeg compiled to WebAssembly. Your audio never leaves your device, which is also why there is no server-imposed size limit — the practical ceiling is the memory your browser makes available."),
            ("Can I convert several files at once?",
             "Yes. Queue as many as you like and they are processed one after another on your own machine. Nothing is sent anywhere, and you can download them individually or all together."),
        ],
    },
    "convert-mp3-to-flac": {
        "faq_h2": "Frequently asked questions about converting MP3 to FLAC",
        "seo_body": """\
      <h3>The fix for your MP3 files: transcode the audio to FLAC</h3>
      <p>MP3 turns up in screen recordings, old capture software and legacy archives. MP3 decoding in video editors is inconsistent, and DaVinci Resolve on Linux does not decode it at all.</p>

      <p>VidToFLAC decodes the MP3 audio and re-encodes it to <strong>FLAC</strong>, an open lossless format that DaVinci Resolve, Premiere Pro, Avid and Final Cut all read natively on Windows, macOS and Linux. The whole job runs inside your browser through FFmpeg compiled to WebAssembly, so the file never leaves your machine.</p>

      <p>FLAC preserves the MP3 content exactly, artefacts included. The file grows and sounds no different; what you gain is native editor support.</p>""",
        "faqs": [
            ("Does converting MP3 to FLAC improve the audio quality?",
             'No, and it is worth being clear about that. MP3 is a lossy format: data was discarded when the file was created, and nothing can bring it back. FLAC preserves exactly what remains, so no further quality is lost from this point on — but it does not restore anything.'),
            ("Why will my editor not read MP3 files?",
             'MP3 decoding in video editors is inconsistent, and DaVinci Resolve on Linux does not decode it at all. FLAC is the practical way around it, because it is one of the few lossless formats every major editor decodes natively.'),
            ("Will the FLAC file be bigger than the MP3?",
             'Usually yes, and sometimes by a lot. MP3 is lossy and already threw data away to get small; FLAC is lossless and stores everything that is left. You are trading disk space for compatibility and for no further generation loss.'),
            ("Is my file uploaded to a server?",
             "No. Everything runs inside your browser through FFmpeg compiled to WebAssembly. Your audio never leaves your device, which is also why there is no server-imposed size limit — the practical ceiling is the memory your browser makes available."),
            ("Can I convert several files at once?",
             "Yes. Queue as many as you like and they are processed one after another on your own machine. Nothing is sent anywhere, and you can download them individually or all together."),
        ],
    },
    "convert-m4a-to-flac": {
        "faq_h2": "Frequently asked questions about converting M4A to FLAC",
        "seo_body": """\
      <h3>The fix for your M4A files: transcode the audio to FLAC</h3>
      <p>M4A turns up in Voice Memos, GarageBand exports and iTunes audio. M4A usually wraps AAC, which DaVinci Resolve cannot decode without a licence. Purchased iTunes files may also carry FairPlay DRM, which nothing can open.</p>

      <p>VidToFLAC decodes the M4A audio and re-encodes it to <strong>FLAC</strong>, an open lossless format that DaVinci Resolve, Premiere Pro, Avid and Final Cut all read natively on Windows, macOS and Linux. The whole job runs inside your browser through FFmpeg compiled to WebAssembly, so the file never leaves your machine.</p>

      <p>If the M4A holds Apple Lossless (ALAC), the conversion is lossless end to end. If it holds AAC, FLAC preserves that AAC exactly as it is.</p>""",
        "faqs": [
            ("Does converting M4A to FLAC improve the audio quality?",
             'No, and it is worth being clear about that. M4A is a lossy format: data was discarded when the file was created, and nothing can bring it back. FLAC preserves exactly what remains, so no further quality is lost from this point on — but it does not restore anything.'),
            ("Why will my editor not read M4A files?",
             'M4A usually wraps AAC, which DaVinci Resolve cannot decode without a licence. Purchased iTunes files may also carry FairPlay DRM, which nothing can open. FLAC is the practical way around it, because it is one of the few lossless formats every major editor decodes natively.'),
            ("Will the FLAC file be bigger than the M4A?",
             'Usually yes, and sometimes by a lot. M4A is lossy and already threw data away to get small; FLAC is lossless and stores everything that is left. You are trading disk space for compatibility and for no further generation loss.'),
            ("Is my file uploaded to a server?",
             "No. Everything runs inside your browser through FFmpeg compiled to WebAssembly. Your audio never leaves your device, which is also why there is no server-imposed size limit — the practical ceiling is the memory your browser makes available."),
            ("Can I convert several files at once?",
             "Yes. Queue as many as you like and they are processed one after another on your own machine. Nothing is sent anywhere, and you can download them individually or all together."),
        ],
    },
    "convert-ogg-to-flac": {
        "faq_h2": "Frequently asked questions about converting OGG to FLAC",
        "seo_body": """\
      <h3>The fix for your OGG files: transcode the audio to FLAC</h3>
      <p>OGG turns up in game audio, podcast archives and open-source software. Vorbis is open and royalty-free, which is exactly why commercial editors built around industry codecs rarely decode it.</p>

      <p>VidToFLAC decodes the OGG audio and re-encodes it to <strong>FLAC</strong>, an open lossless format that DaVinci Resolve, Premiere Pro, Avid and Final Cut all read natively on Windows, macOS and Linux. The whole job runs inside your browser through FFmpeg compiled to WebAssembly, so the file never leaves your machine.</p>

      <p>Vorbis is a capable codec and FLAC will not improve it. What changes is that your editor can finally read the file.</p>""",
        "faqs": [
            ("Does converting OGG to FLAC improve the audio quality?",
             'No, and it is worth being clear about that. OGG is a lossy format: data was discarded when the file was created, and nothing can bring it back. FLAC preserves exactly what remains, so no further quality is lost from this point on — but it does not restore anything.'),
            ("Why will my editor not read OGG files?",
             'Vorbis is open and royalty-free, which is exactly why commercial editors built around industry codecs rarely decode it. FLAC is the practical way around it, because it is one of the few lossless formats every major editor decodes natively.'),
            ("Will the FLAC file be bigger than the OGG?",
             'Usually yes, and sometimes by a lot. OGG is lossy and already threw data away to get small; FLAC is lossless and stores everything that is left. You are trading disk space for compatibility and for no further generation loss.'),
            ("Is my file uploaded to a server?",
             "No. Everything runs inside your browser through FFmpeg compiled to WebAssembly. Your audio never leaves your device, which is also why there is no server-imposed size limit — the practical ceiling is the memory your browser makes available."),
            ("Can I convert several files at once?",
             "Yes. Queue as many as you like and they are processed one after another on your own machine. Nothing is sent anywhere, and you can download them individually or all together."),
        ],
    },
    "convert-wma-to-flac": {
        "faq_h2": "Frequently asked questions about converting WMA to FLAC",
        "seo_body": """\
      <h3>The fix for your WMA files: transcode the audio to FLAC</h3>
      <p>WMA turns up in old Windows recordings and Windows-era archives. WMA is proprietary to Microsoft, and support outside Windows has always been thin and keeps thinning.</p>

      <p>VidToFLAC decodes the WMA audio and re-encodes it to <strong>FLAC</strong>, an open lossless format that DaVinci Resolve, Premiere Pro, Avid and Final Cut all read natively on Windows, macOS and Linux. The whole job runs inside your browser through FFmpeg compiled to WebAssembly, so the file never leaves your machine.</p>

      <p>Treat this as a rescue operation: FLAC preserves whatever the WMA still holds, in a format that will still be readable decades from now.</p>""",
        "faqs": [
            ("Does converting WMA to FLAC improve the audio quality?",
             'No, and it is worth being clear about that. WMA is a lossy format: data was discarded when the file was created, and nothing can bring it back. FLAC preserves exactly what remains, so no further quality is lost from this point on — but it does not restore anything.'),
            ("Why will my editor not read WMA files?",
             'WMA is proprietary to Microsoft, and support outside Windows has always been thin and keeps thinning. FLAC is the practical way around it, because it is one of the few lossless formats every major editor decodes natively.'),
            ("Will the FLAC file be bigger than the WMA?",
             'Usually yes, and sometimes by a lot. WMA is lossy and already threw data away to get small; FLAC is lossless and stores everything that is left. You are trading disk space for compatibility and for no further generation loss.'),
            ("Is my file uploaded to a server?",
             "No. Everything runs inside your browser through FFmpeg compiled to WebAssembly. Your audio never leaves your device, which is also why there is no server-imposed size limit — the practical ceiling is the memory your browser makes available."),
            ("Can I convert several files at once?",
             "Yes. Queue as many as you like and they are processed one after another on your own machine. Nothing is sent anywhere, and you can download them individually or all together."),
        ],
    },
    "convert-aiff-to-flac": {
        "faq_h2": "Frequently asked questions about converting AIFF to FLAC",
        "seo_body": """\
      <h3>The fix for your AIFF files: transcode the audio to FLAC</h3>
      <p>AIFF turns up in Mac-based music production and mastering deliveries. AIFF itself is widely supported — the problem is size, not compatibility. Uncompressed PCM eats disk space at about 250 MB per stereo hour.</p>

      <p>VidToFLAC decodes the AIFF audio and re-encodes it to <strong>FLAC</strong>, an open lossless format that DaVinci Resolve, Premiere Pro, Avid and Final Cut all read natively on Windows, macOS and Linux. The whole job runs inside your browser through FFmpeg compiled to WebAssembly, so the file never leaves your machine.</p>

      <p>Because AIFF is already lossless, nothing at all is discarded. You keep every sample and typically reclaim 40 to 60% of the space.</p>""",
        "faqs": [
            ("Does converting AIFF to FLAC improve the audio quality?",
             'It cannot improve it, and it does not need to. AIFF is already lossless, so the FLAC contains exactly the same samples — nothing is discarded in either direction. The gain is purely in file size.'),
            ("Why will my editor not read AIFF files?",
             'AIFF itself is widely supported — the problem is size, not compatibility. Uncompressed PCM eats disk space at about 250 MB per stereo hour. FLAC is the practical way around it, because it is one of the few lossless formats every major editor decodes natively.'),
            ("Will the FLAC file be bigger than the AIFF?",
             'No, considerably smaller — typically 40 to 60% smaller, because AIFF stores audio uncompressed while FLAC compresses it losslessly.'),
            ("Is my file uploaded to a server?",
             "No. Everything runs inside your browser through FFmpeg compiled to WebAssembly. Your audio never leaves your device, which is also why there is no server-imposed size limit — the practical ceiling is the memory your browser makes available."),
            ("Can I convert several files at once?",
             "Yes. Queue as many as you like and they are processed one after another on your own machine. Nothing is sent anywhere, and you can download them individually or all together."),
        ],
    },
    "convert-opus-to-flac": {
        "faq_h2": "Frequently asked questions about converting Opus to FLAC",
        "seo_body": """\
      <h3>The fix for your Opus files: transcode the audio to FLAC</h3>
      <p>Opus turns up in Discord, WhatsApp, Zoom and WebRTC recordings. Opus postdates the codecs the editing industry standardised on, so almost no NLE decodes it, on any platform.</p>

      <p>VidToFLAC decodes the Opus audio and re-encodes it to <strong>FLAC</strong>, an open lossless format that DaVinci Resolve, Premiere Pro, Avid and Final Cut all read natively on Windows, macOS and Linux. The whole job runs inside your browser through FFmpeg compiled to WebAssembly, so the file never leaves your machine.</p>

      <p>Opus already performed the lossy compression and that is permanent. Converting to FLAC is purely about making the file readable.</p>""",
        "faqs": [
            ("Does converting Opus to FLAC improve the audio quality?",
             'No, and it is worth being clear about that. Opus is a lossy format: data was discarded when the file was created, and nothing can bring it back. FLAC preserves exactly what remains, so no further quality is lost from this point on — but it does not restore anything.'),
            ("Why will my editor not read Opus files?",
             'Opus postdates the codecs the editing industry standardised on, so almost no NLE decodes it, on any platform. FLAC is the practical way around it, because it is one of the few lossless formats every major editor decodes natively.'),
            ("Will the FLAC file be bigger than the Opus?",
             'Usually yes, and sometimes by a lot. Opus is lossy and already threw data away to get small; FLAC is lossless and stores everything that is left. You are trading disk space for compatibility and for no further generation loss.'),
            ("Is my file uploaded to a server?",
             "No. Everything runs inside your browser through FFmpeg compiled to WebAssembly. Your audio never leaves your device, which is also why there is no server-imposed size limit — the practical ceiling is the memory your browser makes available."),
            ("Can I convert several files at once?",
             "Yes. Queue as many as you like and they are processed one after another on your own machine. Nothing is sent anywhere, and you can download them individually or all together."),
        ],
    },
    "convert-avi-to-flac": {
        "faq_h2": "Frequently asked questions about converting AVI to FLAC",
        "seo_body": """\
      <h3>The fix for your AVI files: FLAC audio in an MKV</h3>
      <p>AVI files from old camcorders, capture cards and legacy recording software carry their audio as <strong>MP3 or AC3</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is copied bit for bit when the browser can decode it, or re-encoded to H.264 when it is a legacy codec such as DivX, Xvid or Cinepak.</p>

      <p>Old AVIs are frequently interlaced. Converting the audio does not deinterlace the picture — set that in your editor's clip attributes.</p>""",
        "faqs": [
            ("Do I lose video quality converting an AVI?",
             'It depends on the codec. When the video can be copied it is copied <strong>bit for bit</strong> and the picture is exactly the original. When it cannot be decoded in the browser it is re-encoded to H.264 at high quality (<code>-crf 18</code>) — very close to the original, but not bit-for-bit identical. The audio becomes FLAC, which is lossless, either way.'),
            ("Why does my AVI import without sound?",
             'Because the audio is <strong>MP3 or AC3</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    "convert-webm-to-flac": {
        "faq_h2": "Frequently asked questions about converting WebM to FLAC",
        "seo_body": """\
      <h3>The fix for your WebM files: FLAC audio in an MKV</h3>
      <p>WebM files from downloaded video, browser captures and screen recordings carry their audio as <strong>Opus or Vorbis</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is copied bit for bit when the VP8 or VP9 video can be decoded by the browser.</p>

      <p>Browser-made screen recordings are often variable frame rate, which makes audio drift as the clip runs. That needs a constant frame rate, not an audio conversion.</p>""",
        "faqs": [
            ("Do I lose video quality converting an WebM?",
             'No, provided the video codec can be copied into the output container: it is copied <strong>bit for bit</strong>, with no decoding and no recompression, so the picture is exactly the original. Only the audio track changes, and FLAC is lossless.'),
            ("Why does my WebM import without sound?",
             'Because the audio is <strong>Opus or Vorbis</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    "convert-wmv-to-flac": {
        "faq_h2": "Frequently asked questions about converting WMV to FLAC",
        "seo_body": """\
      <h3>The fix for your WMV files: FLAC audio in an MKV</h3>
      <p>WMV files from Windows-era recordings and old corporate video carry their audio as <strong>WMA</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is re-encoded to H.264, because neither VC-1 nor WMV3 can be decoded in the browser.</p>

      <p>This is a full conversion rather than a remux, so it takes noticeably longer than other formats and the video is not bit-for-bit identical. At -crf 18 the difference is not visible in practice.</p>""",
        "faqs": [
            ("Do I lose video quality converting an WMV?",
             'The video is re-encoded to H.264, because its original codec cannot be decoded in the browser. That means it is not bit-for-bit identical to the source, though at <code>-crf 18</code> the difference is not visible in practice. The audio becomes FLAC, which is lossless.'),
            ("Why does my WMV import without sound?",
             'Because the audio is <strong>WMA</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    "convert-flv-to-flac": {
        "faq_h2": "Frequently asked questions about converting FLV to FLAC",
        "seo_body": """\
      <h3>The fix for your FLV files: FLAC audio in an MKV</h3>
      <p>FLV files from archived screencasts, old lectures and downloads from retired platforms carry their audio as <strong>MP3 or Nellymoser</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is copied when it is H.264, or re-encoded to H.264 when it is a legacy Flash codec such as Sorenson or VP6.</p>

      <p>Flash video was retired in 2020, so anything you still have is an archive. Converting it now is also the simplest way to make sure it stays playable.</p>""",
        "faqs": [
            ("Do I lose video quality converting an FLV?",
             'It depends on the codec. When the video can be copied it is copied <strong>bit for bit</strong> and the picture is exactly the original. When it cannot be decoded in the browser it is re-encoded to H.264 at high quality (<code>-crf 18</code>) — very close to the original, but not bit-for-bit identical. The audio becomes FLAC, which is lossless, either way.'),
            ("Why does my FLV import without sound?",
             'Because the audio is <strong>MP3 or Nellymoser</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    "convert-vob-to-flac": {
        "faq_h2": "Frequently asked questions about converting VOB to FLAC",
        "seo_body": """\
      <h3>The fix for your VOB files: FLAC audio in an MKV</h3>
      <p>VOB files from DVDs and the VIDEO_TS folders ripped from them carry their audio as <strong>AC3 or PCM</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is re-encoded to H.264, because MPEG-2 cannot be decoded in the browser.</p>

      <p>VOB files from commercial DVDs are usually encrypted with CSS. Those cannot be processed by any tool without circumventing the protection, and this one will not open them.</p>""",
        "faqs": [
            ("Do I lose video quality converting an VOB?",
             'The video is re-encoded to H.264, because its original codec cannot be decoded in the browser. That means it is not bit-for-bit identical to the source, though at <code>-crf 18</code> the difference is not visible in practice. The audio becomes FLAC, which is lossless.'),
            ("Why does my VOB import without sound?",
             'Because the audio is <strong>AC3 or PCM</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    "convert-ts-to-flac": {
        "faq_h2": "Frequently asked questions about converting TS to FLAC",
        "seo_body": """\
      <h3>The fix for your TS files: FLAC audio in an MKV</h3>
      <p>TS files from digital television, capture cards and stream recorders carry their audio as <strong>AC3 or AAC</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is copied when it is H.264, or re-encoded to H.264 when it is MPEG-2.</p>

      <p>Transport streams often carry several programmes and have no clean index, so some players show odd durations. Converting to MKV gives you a properly indexed file.</p>""",
        "faqs": [
            ("Do I lose video quality converting an TS?",
             'It depends on the codec. When the video can be copied it is copied <strong>bit for bit</strong> and the picture is exactly the original. When it cannot be decoded in the browser it is re-encoded to H.264 at high quality (<code>-crf 18</code>) — very close to the original, but not bit-for-bit identical. The audio becomes FLAC, which is lossless, either way.'),
            ("Why does my TS import without sound?",
             'Because the audio is <strong>AC3 or AAC</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    "convert-m4v-to-flac": {
        "faq_h2": "Frequently asked questions about converting M4V to FLAC",
        "seo_body": """\
      <h3>The fix for your M4V files: FLAC audio in an MKV</h3>
      <p>M4V files from iTunes, Apple TV and iPhone exports carry their audio as <strong>AAC</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is copied when it is H.264, or re-encoded to H.264 when it is HEVC.</p>

      <p>M4V files bought from iTunes carry FairPlay DRM. Those are encrypted and no tool opens them legally, this one included. Your own exports convert normally.</p>""",
        "faqs": [
            ("Do I lose video quality converting an M4V?",
             'It depends on the codec. When the video can be copied it is copied <strong>bit for bit</strong> and the picture is exactly the original. When it cannot be decoded in the browser it is re-encoded to H.264 at high quality (<code>-crf 18</code>) — very close to the original, but not bit-for-bit identical. The audio becomes FLAC, which is lossless, either way.'),
            ("Why does my M4V import without sound?",
             'Because the audio is <strong>AAC</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    "convert-mpeg-to-flac": {
        "faq_h2": "Frequently asked questions about converting MPEG to FLAC",
        "seo_body": """\
      <h3>The fix for your MPEG files: FLAC audio in an MKV</h3>
      <p>MPEG files from VCDs, old capture hardware and broadcast archives carry their audio as <strong>MP2 or AC3</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is re-encoded to H.264, because neither MPEG-1 nor MPEG-2 video can be decoded in the browser.</p>

      <p>MPEG files are usually old and often interlaced. The conversion makes them far easier to edit, but it is a full re-encode rather than a remux.</p>""",
        "faqs": [
            ("Do I lose video quality converting an MPEG?",
             'The video is re-encoded to H.264, because its original codec cannot be decoded in the browser. That means it is not bit-for-bit identical to the source, though at <code>-crf 18</code> the difference is not visible in practice. The audio becomes FLAC, which is lossless.'),
            ("Why does my MPEG import without sound?",
             'Because the audio is <strong>MP2 or AC3</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    "convert-3gp-to-flac": {
        "faq_h2": "Frequently asked questions about converting 3GP to FLAC",
        "seo_body": """\
      <h3>The fix for your 3GP files: FLAC audio in an MKV</h3>
      <p>3GP files from early mobile phone recordings and voice notes carry their audio as <strong>AMR</strong>, and that is what DaVinci Resolve refuses to decode — on Linux always, and on Windows and macOS depending on version and configuration. The picture imports; the sound does not.</p>

      <p>VidToFLAC repackages the file into an <strong>MKV</strong> and re-encodes the audio track to lossless <strong>FLAC</strong>, which every major editor reads natively. The video is re-encoded to H.264, because H.263 cannot be decoded in the browser.</p>

      <p>Be realistic about AMR: it discards a great deal to reach very low bitrates, and FLAC preserves exactly what remains. It cannot restore what was never stored.</p>""",
        "faqs": [
            ("Do I lose video quality converting an 3GP?",
             'The video is re-encoded to H.264, because its original codec cannot be decoded in the browser. That means it is not bit-for-bit identical to the source, though at <code>-crf 18</code> the difference is not visible in practice. The audio becomes FLAC, which is lossless.'),
            ("Why does my 3GP import without sound?",
             'Because the audio is <strong>AMR</strong>, and DaVinci Resolve ships no licence to decode it on Linux — and handles it unevenly elsewhere. The video decoders are included, which is why you see the picture but hear nothing.'),
            ("What output format should I choose?",
             "<strong>MKV</strong>. It accepts FLAC audio without complaint and DaVinci Resolve handles it without trouble, whereas MP4 does not officially support FLAC. If you need MP4 specifically, convert the audio to AAC afterwards with desktop FFmpeg."),
            ("Is there a size limit?",
             "We impose none, and nothing is uploaded. The practical ceiling is the memory your browser makes available to WebAssembly — roughly 2 GB for input and output combined, which works comfortably up to around 1 GB of source file. Split longer recordings before converting."),
            ("Is my file uploaded to a server?",
             "No. Everything is processed on your own machine through FFmpeg compiled to WebAssembly. The file never leaves your browser."),
        ],
    },
    # <<CONTENT_END>>
}
