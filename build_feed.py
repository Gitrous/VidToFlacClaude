#!/usr/bin/env python3
"""Genera feed.xml y en/feed.xml a partir de los artículos publicados.

Lee cada articulos/*/index.html y en/articles/*/index.html, saca el titular del
JSON-LD (que es el texto canónico: el <title> lleva a veces el sufijo del sitio),
la meta description y las fechas, y escribe un RSS 2.0.

No inventa fechas: si un artículo no declara datePublished, se avisa y se
excluye, porque un elemento sin pubDate desordena el feed en cualquier lector.
"""
import html
import re
import sys
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
BASE = "https://vidtoflac.tech"

IDIOMAS = {
    "es": {
        "dir": RAIZ / "articulos",
        "salida": RAIZ / "feed.xml",
        "ruta": "/feed.xml",
        "lang": "es-ES",
        "titulo": "VidToFLAC — Guías de audio para DaVinci Resolve",
        "desc": ("Artículos medidos sobre audio en DaVinci Resolve, códecs y "
                 "conversión a FLAC. Cada afirmación se prueba con archivos "
                 "reales antes de publicarla."),
        "enlace": f"{BASE}/articulos/",
    },
    "en": {
        "dir": RAIZ / "en" / "articles",
        "salida": RAIZ / "en" / "feed.xml",
        "ruta": "/en/feed.xml",
        "lang": "en",
        "titulo": "VidToFLAC — Audio guides for DaVinci Resolve",
        "desc": ("Measured articles on audio in DaVinci Resolve, codecs and "
                 "FLAC conversion. Every claim is tested against real files "
                 "before it is published."),
        "enlace": f"{BASE}/en/articles/",
    },
}

AUTOR = "Guillem Sánchez"


def _campo(texto, patron):
    m = re.search(patron, texto)
    return m.group(1) if m else None


def leer_articulo(carpeta):
    f = carpeta / "index.html"
    if not f.is_file():
        return None
    s = f.read_text(encoding="utf-8")
    titular = _campo(s, r'"headline":\s*"([^"]+)"')
    if not titular:
        titular = _campo(s, r"<title>(.*?)</title>")
    desc = _campo(s, r'<meta name="description" content="([^"]*)"')
    pub = _campo(s, r'"datePublished":\s*"(\d{4}-\d{2}-\d{2})"')
    mod = _campo(s, r'"dateModified":\s*"(\d{4}-\d{2}-\d{2})"') or pub
    if not (titular and pub):
        print(f"  aviso: {carpeta} sin titular o sin datePublished, se omite")
        return None
    return {
        "titulo": html.unescape(titular),
        "desc": html.unescape(desc or ""),
        "pub": pub,
        "mod": mod,
        "slug": carpeta.name,
    }


def fecha_rss(iso):
    d = datetime.strptime(iso, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return format_datetime(d)


def construir(idioma, cfg):
    carpetas = sorted(p for p in cfg["dir"].iterdir() if p.is_dir())
    arts = [a for a in (leer_articulo(p) for p in carpetas) if a]
    # Más recientes primero; a igualdad de fecha, orden alfabético estable.
    arts.sort(key=lambda a: (a["pub"], a["slug"]), reverse=True)

    prefijo = "/articulos" if idioma == "es" else "/en/articles"
    ultima = max(a["mod"] for a in arts)

    items = []
    for a in arts:
        url = f"{BASE}{prefijo}/{a['slug']}/"
        items.append(
            "    <item>\n"
            f"      <title>{html.escape(a['titulo'])}</title>\n"
            f"      <link>{url}</link>\n"
            f"      <guid isPermaLink=\"true\">{url}</guid>\n"
            f"      <description>{html.escape(a['desc'])}</description>\n"
            f"      <dc:creator>{html.escape(AUTOR)}</dc:creator>\n"
            f"      <pubDate>{fecha_rss(a['pub'])}</pubDate>\n"
            "    </item>"
        )

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
        "  <channel>\n"
        f"    <title>{html.escape(cfg['titulo'])}</title>\n"
        f"    <link>{cfg['enlace']}</link>\n"
        f"    <description>{html.escape(cfg['desc'])}</description>\n"
        f"    <language>{cfg['lang']}</language>\n"
        f"    <lastBuildDate>{fecha_rss(ultima)}</lastBuildDate>\n"
        f"    <atom:link href=\"{BASE}{cfg['ruta']}\" rel=\"self\" "
        'type="application/rss+xml" />\n'
        + "\n".join(items) + "\n"
        "  </channel>\n"
        "</rss>\n"
    )
    return xml, len(arts)


def main():
    seco = "--dry-run" in sys.argv
    for idioma, cfg in IDIOMAS.items():
        xml, n = construir(idioma, cfg)
        destino = cfg["salida"]
        actual = destino.read_text(encoding="utf-8") if destino.is_file() else None
        if actual == xml:
            print(f"{destino.relative_to(RAIZ)}: sin cambios ({n} artículos)")
            continue
        if seco:
            print(f"{destino.relative_to(RAIZ)}: CAMBIA ({n} artículos)")
            continue
        destino.write_text(xml, encoding="utf-8")
        print(f"{destino.relative_to(RAIZ)}: escrito ({n} artículos)")
    print("Listo.")


if __name__ == "__main__":
    main()
