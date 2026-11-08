#!/usr/bin/env python3
"""Genera il sito statico di Marsicalluminio (Revisione 4).

Uso:  python3 build.py <cartella_di_uscita>
Tutti i dati aziendali e tecnici sono in questo file e in content.py.
"""
import json
import shutil
import sys
from pathlib import Path

import drawings as dw
from content import PAGES, CO

HERE = Path(__file__).parent
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else HERE / "dist")

# Strumento interno per le offerte (accesso con credenziali personali)
AREA_RISERVATA = "https://marsicalluminio.eu.pythonanywhere.com"

NAV = [
    ("finestre.html", "Finestre"),
    ("scorrevoli.html", "Scorrevoli"),
    ("porte.html", "Porte d'ingresso"),
    ("accessori.html", "Vetri e accessori"),
    ("posa.html", "Posa"),
    ("detrazioni.html", "Detrazioni"),
]


def head(page):
    title = page["title"]
    desc = page["desc"]
    url = CO["site"] + ("" if page["file"] == "index.html" else page["file"])
    noindex = '<meta name="robots" content="noindex">' if page.get("noindex") else ""
    ld = ""
    if page["file"] == "index.html":
        ld = '<script type="application/ld+json">' + json.dumps(CO["jsonld"], ensure_ascii=False) + "</script>"
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{noindex}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="Marsicalluminio">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{CO['site']}assets/img/og.png">
<meta name="theme-color" content="#13294b">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="assets/img/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preload" href="assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/site.css">
{ld}
</head>
<body>
<a class="skip" href="#main">Vai al contenuto</a>
"""


def header(page):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if page["file"] == href else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return f"""<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="./" aria-label="Marsicalluminio, pagina iniziale"><img src="assets/img/logo.svg" alt="Marsicalluminio — Energia &amp; Design" width="262" height="100"></a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav"><span aria-hidden="true"></span>Menu</button>
    <nav class="nav" id="nav" aria-label="Principale">
      {''.join(links)}
      <a class="btn" href="contatti.html">Richiedi un sopralluogo</a>
    </nav>
    <div class="head-cta">
      <a class="head-tel" href="tel:{CO['tel1_raw']}">{CO['tel1']}</a>
      <a class="btn sm" href="contatti.html">Richiedi un sopralluogo</a>
    </div>
  </div>
</header>
<main id="main">
"""


def cta_band(page):
    if page.get("no_cta"):
        return ""
    return f"""<section class="cta-band" aria-labelledby="cta-t">
  <div class="wrap cta-in">
    <div>
      <h2 id="cta-t">Partiamo dalle misure vere</h2>
      <p>Al sopralluogo rileviamo i vani, guardiamo i vecchi telai e ti diciamo quale linea ha senso per casa tua e per la tua zona climatica. Preventivo dettagliato, senza impegno.</p>
    </div>
    <div class="cta-actions">
      <a class="btn" href="contatti.html">Richiedi un sopralluogo</a>
      <div class="tels">
        <a href="tel:{CO['tel1_raw']}">{CO['tel1']}</a>
        <a href="tel:{CO['tel2_raw']}">{CO['tel2']}</a>
        <a href="mailto:{CO['email']}">{CO['email']}</a>
      </div>
    </div>
  </div>
</section>
"""


def footer(page):
    return f"""</main>
{cta_band(page)}
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-block">
      <div class="logo">
        <img src="assets/img/logo.svg" alt="Marsicalluminio" width="136" height="52" loading="lazy">
        <p>{CO['name']}</p>
        <p class="muted small">Fornitura e posa di finestre, porte e scorrevoli in PVC</p>
      </div>
      <div>
        <span class="k">Contatti</span>
        <p><a href="tel:{CO['tel1_raw']}">{CO['tel1']}</a></p>
        <p><a href="tel:{CO['tel2_raw']}">{CO['tel2']}</a></p>
        <p><a href="mailto:{CO['email']}">{CO['email']}</a></p>
        <p class="muted">{CO['hours']}</p>
      </div>
      <div>
        <span class="k">Sede legale</span>
        <p>{CO['address']}</p>
        <span class="k">PEC</span>
        <p>{CO['pec']}</p>
      </div>
      <div>
        <span class="k">Dati societari</span>
        <p>P. IVA e C.F. {CO['vat']}</p>
        <p>REA {CO['rea']}</p>
        <p>Capitale sociale {CO['capital']}</p>
      </div>
      <div class="wide">
        <span class="k">Prodotti</span>
        <ul>
          <li><a href="finestre.html">Finestre e portefinestre</a></li>
          <li><a href="scorrevoli.html">Alzanti e scorrevoli</a></li>
          <li><a href="porte.html">Porte d'ingresso</a></li>
          <li><a href="accessori.html">Vetri, ferramenta, oscuranti</a></li>
          <li><a href="posa.html">Sostituzione e posa</a></li>
          <li><a href="detrazioni.html">Detrazioni fiscali 2026</a></li>
        </ul>
      </div>
      <div>
        <span class="k">Informazioni legali</span>
        <p><a href="privacy.html">Privacy</a> · <a href="cookie.html">Cookie</a> · <a href="note-legali.html">Note legali</a></p>
        <span class="k">Area riservata</span>
        <p><a href="{AREA_RISERVATA}" rel="nofollow">Accesso soci</a></p>
      </div>
      <div>
        <span class="k">Aggiornamento</span>
        <p>{CO['updated']}</p>
      </div>
    </div>
    <div class="foot-legal">
      <span>© 2026 {CO['name']} Disegni e schemi tecnici originali, a scopo illustrativo.</span>
      <span>I valori tecnici sono riferiti a serramenti campione: quelli del tuo ordine sono indicati nel preventivo.</span>
    </div>
  </div>
</footer>
<div class="quickbar" aria-label="Contatto rapido">
  <a class="btn ghost" href="tel:{CO['tel1_raw']}">Chiama</a>
  <a class="btn" href="contatti.html">Sopralluogo</a>
</div>
<script src="assets/js/site.js" defer></script>
</body>
</html>
"""


def build():
    if OUT.exists():
        for p in OUT.iterdir():
            if p.name in (".git", "_sorgente", "README.md", ".gitignore"):
                continue
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copytree(HERE / "static", OUT, dirs_exist_ok=True)
    for page in PAGES:
        html = head(page) + header(page) + page["body"]() + footer(page)
        (OUT / page["file"]).write_text(html, encoding="utf-8")
    # sitemap
    urls = "".join(
        f"<url><loc>{CO['site']}{'' if p['file'] == 'index.html' else p['file']}</loc><lastmod>{CO['lastmod']}</lastmod></url>"
        for p in PAGES if not p.get("noindex")
    )
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n'
    )
    print("ok", len(PAGES), "pagine in", OUT)


if __name__ == "__main__":
    build()
