# Sito Marsicalluminio — Revisione 4 (novembre 2026)

Sito statico, nessun framework: le pagine HTML nella radice sono pronte da pubblicare.

## Struttura
- `*.html` — pagine del sito (generate, non modificare a mano)
- `assets/` — foglio di stile, script, font Archivo ospitato in locale, logo
- `_sorgente/` — generatore del sito
  - `content.py` — tutti i testi, i dati aziendali e i dati tecnici delle linee
  - `drawings.py` — disegni tecnici SVG originali (sezioni, prospetti, schemi)
  - `build.py` — assembla le pagine
  - `static/` — file copiati così come sono

## Rigenerare il sito dopo una modifica ai testi
```
cd _sorgente
python3 build.py ..
```
Il comando riscrive le pagine nella radice del repository (non tocca `.git` né `_sorgente`).

## Regola
Nessun nome, logo, codice profilo o immagine del produttore dei profili deve comparire nel sito.
Le linee si chiamano Velino 82, Sirente 80, Fucino 76, Salviano 72 (versioni da ristrutturazione con suffisso R).
