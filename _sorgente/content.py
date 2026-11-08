"""Contenuti del sito Marsicalluminio. Nessun riferimento al produttore dei profili."""
import drawings as dw

CO = {
    "site": "https://www.marsicalluminio.it/",
    "name": "Marsicalluminio S.r.l.s.",
    "address": "Viale Sesto 19, 00124 Roma (RM)",
    "street": "Viale Sesto 19",
    "cap": "00124",
    "pec": "marsicalluminiosrls@legalmail.it",
    "vat": "18332371006",
    "rea": "RM-1778557",
    "capital": "€ 2.000,00 i.v.",
    "email": "marsicalluminio@gmail.com",
    "tel1": "335 758 4371", "tel1_raw": "+393357584371",
    "tel2": "377 129 0313", "tel2_raw": "+393771290313",
    "wa": "https://wa.me/393357584371",
    "hours": "Lunedì–venerdì, 9:00–18:00",
    "area": "Roma e la Marsica",
    "updated": "Novembre 2026",
    "lastmod": "2026-11-08",
    "form": "https://formspree.io/f/xvzvwoyw",
}
CO["jsonld"] = {
    "@context": "https://schema.org",
    "@type": "HomeAndConstructionBusiness",
    "name": "Marsicalluminio S.r.l.s.",
    "description": "Fornitura e posa di finestre, portefinestre, alzanti scorrevoli e porte d'ingresso in PVC.",
    "url": CO["site"],
    "logo": CO["site"] + "assets/img/logo.svg",
    "image": CO["site"] + "assets/img/og.png",
    "email": CO["email"],
    "telephone": CO["tel1_raw"],
    "vatID": "IT" + CO["vat"],
    "address": {"@type": "PostalAddress", "streetAddress": CO["street"], "postalCode": CO["cap"],
                "addressLocality": "Roma", "addressRegion": "RM", "addressCountry": "IT"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                   "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                   "opens": "09:00", "closes": "18:00"}],
    "areaServed": ["Roma", "Marsica"],
}

REF = "finestra campione 1230 × 1480 mm, triplo vetro Ug 0,5 W/m²K con canalina calda"

# ---------------------------------------------------------------------------
# Dati tecnici delle linee (da catalogo 2026, nomi propri Marsicalluminio)
# ---------------------------------------------------------------------------
WIN = [
    {
        "key": "velino", "name": "Velino 82", "depth": "82 mm", "ch": "6 nel telaio, 6 nell'anta",
        "uw": "0,76", "uf": "1,0", "ug": "0,5", "glass": "da 24 a 48 mm", "bead": "dritti o arrotondati",
        "reinf": "acciaio nel telaio e nell'anta", "gask": "3, con guarnizione centrale",
        "tag": "Il profilo più profondo della gamma: massima rigidità per ante grandi e portefinestre.",
        "intro": "Con 82 mm di profondità e sei camere sia nel telaio sia nell'anta, il Velino 82 è la linea da scegliere quando le dimensioni crescono: portefinestre alte, ante larghe, esposizioni a vento forte. È anche l'unica linea che accetta il rivestimento esterno in alluminio.",
        "variants": [
            ("Versione Classica", "Anta con profilo tradizionale, fermavetri dritti o arrotondati."),
            ("Versione Design in classe A", "Pareti esterne del profilo da 2,8 mm, lo spessore della classe A secondo la norma europea sui profili in PVC: più stabilità nel tempo e angoli più nitidi."),
            ("Rivestimento esterno in alluminio", "Una cover in alluminio verniciato, in qualsiasi colore RAL, protegge il lato esterno di finestre, portefinestre e scorrevoli paralleli. Dentro resta il PVC, fuori la resistenza e il colore dell'alluminio."),
        ],
        "reno": ("Velino 82 R", "Telaio da ristrutturazione con aletta da 35 o 60 mm. Stessa sezione, stessa vetrocamera: Uw 0,76 W/m²K con triplo vetro."),
    },
    {
        "key": "sirente", "name": "Sirente 80", "depth": "80 mm", "ch": "6 nel telaio, 6 nell'anta",
        "uw": "0,72", "uf": "1,0", "ug": "0,5", "glass": "24, 28 o 48 mm", "bead": "dritti o soft",
        "reinf": "acciaio nel telaio e nell'anta", "gask": "3, con guarnizione centrale",
        "tag": "Il valore Uw più basso tra le nostre finestre: 0,72 W/m²K.",
        "intro": "Il Sirente 80 è la linea con il miglior isolamento della gamma. È la scelta naturale per le zone climatiche fredde, per le case che puntano a consumi molto bassi e per chi vuole margine rispetto ai limiti richiesti dalle detrazioni.",
        "variants": [
            ("Disponibile in classe A", "Pareti del profilo da 2,8 mm su richiesta."),
            ("Fermavetri dritti o soft", "Il fermavetro soft, con raggio morbido, si usa anche nelle parti fisse con vetro montato direttamente nel telaio."),
        ],
        "reno": ("Sirente 80 R", "Telaio da ristrutturazione con aletta da 60 mm. Con doppio vetro Ug 1,0: Uw 1,3 W/m²K; con triplo vetro il valore scende e viene calcolato in preventivo."),
    },
    {
        "key": "fucino", "name": "Fucino 76", "depth": "telaio 76 mm, anta 80 mm", "ch": "6 nel telaio",
        "uw": "0,74", "uf": "1,0", "ug": "0,5", "glass": "da 24 a 52 mm", "bead": "dritti, taglio a 90°",
        "reinf": "acciaio; composito termico nel telaio (versione Composito)", "gask": "3, con guarnizione centrale",
        "tag": "Linee squadrate e fermavetri tagliati a 90°: la finestra dal disegno più architettonico.",
        "intro": "Il Fucino 76 ha un'anta più profonda del telaio, spigoli netti e fermavetri con taglio a 90°. Accetta la vetrocamera più spessa della gamma, fino a 52 mm, utile per vetri acustici e di sicurezza stratificati.",
        "variants": [
            ("Fucino 76 Composito", "Nel telaio un rinforzo in materiale composito al posto dell'acciaio: conduce meno calore e porta il telaio a Uf 0,96 e la finestra a Uw 0,73 W/m²K."),
            ("Fucino 76 Centrale", "Due ante senza montante fisso centrale, con la maniglia montata al centro tra anta attiva e anta passiva. Più vetro, più luce e una finestra simmetrica; altezza fino a 2500 mm."),
        ],
        "reno": ("Fucino 76 R", "Telaio da ristrutturazione con aletta da 40 mm, disponibile anche nella versione Centrale. Con doppio vetro Ug 1,0: Uw 1,3 W/m²K."),
    },
    {
        "key": "salviano", "name": "Salviano 72", "depth": "72 mm", "ch": "5 nel telaio, 5 nell'anta",
        "uw": "0,81", "uf": "1,2", "ug": "0,5", "glass": "da 24 a 44 mm", "bead": "dritti o arrotondati",
        "reinf": "acciaio nel telaio e nell'anta", "gask": "3, con guarnizione centrale",
        "tag": "La linea essenziale, con tre guarnizioni come le altre.",
        "intro": "Il Salviano 72 porta il sistema a tre guarnizioni anche nella fascia d'ingresso. È adatto a sostituzioni nelle zone climatiche intermedie, a seconde case e a locali di servizio, dove conta un buon isolamento a un costo contenuto.",
        "variants": [
            ("Con doppio o triplo vetro", "Vetrocamera fino a 44 mm: triplo vetro per l'isolamento, doppio vetro dove serve contenere peso e costo."),
        ],
        "reno": ("Salviano 72 R", "Telaio da ristrutturazione con aletta da 35 o 60 mm. Con doppio vetro Ug 1,1: Uw 1,3 W/m²K."),
    },
]
WIN_BY = {w["key"]: w for w in WIN}


def esc(s):
    return s.replace("&", "&amp;")


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
def home():
    plain = dw.section("velino", "plain", callouts=True, uid="hp")
    therm = dw.section("velino", "thermal", callouts=True, uid="ht").replace('class="section', 'class="therm section')
    lineup = dw.scale_lineup()
    cards = []
    blurbs = {
        "salviano": "La linea essenziale: tre guarnizioni e cinque camere per sostituzioni nelle zone climatiche intermedie.",
        "fucino": "Spigoli netti e fermavetri a 90°. Disponibile con rinforzo composito o senza montante centrale.",
        "sirente": "Il miglior isolamento della gamma, per zone fredde e case a bassi consumi.",
        "velino": "La più profonda e rigida, per portefinestre e ante grandi. Anche con esterno in alluminio.",
    }
    for k, svg in lineup.items():
        w = WIN_BY[k]
        cards.append(f"""<article>
  <div class="fig">{svg}</div>
  <h3>{w['name']}</h3>
  <dl><dt>Profondità</dt><dd>{w['depth'].replace('telaio ', '').replace(', anta ', ' / ')}</dd>
  <dt>Uw</dt><dd>{w['uw']} W/m²K</dd><dt>Vetro</dt><dd>fino a {w['glass'].split(' ')[-2]} mm</dd></dl>
  <p>{blurbs[k]}</p>
  <a class="textlink" href="finestre.html#{k}">Scheda {w['name']}</a>
</article>""")
    return f"""
<section class="hero">
  <div class="wrap">
    <div class="hero-grid">
      <div>
        <h1>Finestre in PVC ad alto isolamento, misurate e posate con metodo</h1>
        <p class="lead">Forniamo e installiamo finestre, portefinestre, alzanti scorrevoli e porte d'ingresso a {CO['area']}. Prima di firmare ti spieghiamo cosa stai comprando, valore per valore. Poi prendiamo le misure e seguiamo la posa fino alla regolazione finale.</p>
        <div class="actions">
          <a class="btn" href="contatti.html">Richiedi un sopralluogo</a>
          <a class="textlink" href="#linee">Confronta le quattro linee</a>
        </div>
      </div>
      <figure class="hero-fig sheet">
        <div class="stack">{plain}{therm}</div>
        <figcaption>
          <span>Velino 82, sezione del traverso inferiore. Campo termico indicativo con 0 °C all'esterno e 20 °C all'interno.</span>
          <span class="scale-bar">0 °C <i></i> 20 °C</span>
        </figcaption>
      </figure>
    </div>
    <dl class="titleblock" style="--cols:4">
      <div><dt>Trasmittanza della finestra</dt><dd>Uw da 0,72 W/m²K<span class="n">misurata sulla finestra campione con triplo vetro</span></dd></div>
      <div><dt>Profondità dei telai</dt><dd>Da 72 a 82 mm<span class="n">con 5 o 6 camere isolanti</span></dd></div>
      <div><dt>Tenuta</dt><dd>Tre guarnizioni<span class="n">su tutte le linee, compresa quella centrale</span></dd></div>
      <div><dt>Sostituzione</dt><dd>Senza opere murarie<span class="n">con telai da ristrutturazione da 35 a 60 mm</span></dd></div>
    </dl>
  </div>
</section>

<section class="band" id="linee" aria-labelledby="linee-t">
  <div class="wrap">
    <div class="band-head">
      <h2 id="linee-t">Quattro linee di finestre, disegnate nella stessa scala</h2>
      <p class="muted">Più il telaio è profondo, più spazio c'è per camere isolanti, rinforzi e vetri spessi. Ogni linea porta il nome di un luogo della Marsica. Su tutte, canalina calda di serie nel vetro.</p>
    </div>
    <div class="lineup sheet">{''.join(cards)}</div>
  </div>
</section>

<section class="band white" aria-labelledby="cat-t">
  <div class="wrap">
    <div class="band-head">
      <h2 id="cat-t">Cosa forniamo e installiamo</h2>
      <p class="muted">Tutti i serramenti sono costruiti su misura sulla base del nostro rilievo.</p>
    </div>
    <div class="catalog">
      <a class="row" href="finestre.html">{dw.elev_window()}<h3>Finestre e portefinestre</h3><p>A una o più ante, con apertura ad anta e ribalta, fisse o con anta senza montante centrale. Quattro profili da 72 a 82 mm.</p><span class="go">Le finestre</span></a>
      <a class="row" href="scorrevoli.html">{dw.elev_sliding()}<h3>Alzanti e scorrevoli</h3><p>Alzanti fino a 6 metri di larghezza con soglia quasi a filo pavimento, scorrevoli leggeri e scorrevoli paralleli con ribalta.</p><span class="go">Gli scorrevoli</span></a>
      <a class="row" href="porte.html">{dw.elev_door()}<h3>Porte d'ingresso</h3><p>Da 76 a 82 mm, serrature da 3 a 5 punti di chiusura, apertura con impronta digitale, codice o smartphone.</p><span class="go">Le porte</span></a>
      <a class="row" href="accessori.html">{dw.elev_shutter()}<h3>Vetri, oscuranti e accessori</h3><p>Vetri di sicurezza e acustici, avvolgibili e cassonetti coibentati, zanzariere, maniglie di sicurezza, aeratori.</p><span class="go">Gli accessori</span></a>
    </div>
  </div>
</section>

<section class="band ink" aria-labelledby="proc-t">
  <div class="wrap">
    <div class="band-head">
      <h2 id="proc-t">Come lavoriamo, dal sopralluogo alla posa</h2>
      <p class="muted">Un solo referente segue il lavoro dall'inizio alla fine.</p>
    </div>
    <ol class="steps">
      <li><h3>Sopralluogo</h3><p>Guardiamo vani, vecchi telai, esposizione e muratura. Ti chiediamo cosa non funziona oggi: freddo, rumore, condensa, poca luce.</p></li>
      <li><h3>Rilievo e scelta</h3><p>Prendiamo le misure e scegliamo con te profilo, vetro, ferramenta e tipo di posa. Verifichiamo i requisiti per la detrazione nella tua zona climatica.</p></li>
      <li><h3>Preventivo dettagliato</h3><p>Ogni voce con il suo valore tecnico: Uw, composizione del vetro, accessori, posa. Nessuna cifra a forfait.</p></li>
      <li><h3>Produzione su misura</h3><p>I serramenti vengono costruiti sulle misure rilevate. Ti comunichiamo la data di posa appena è confermata.</p></li>
      <li><h3>Posa e consegna</h3><p>Smontaggio, posa, sigillatura e regolazione della ferramenta. Ti lasciamo dichiarazione di prestazione e marcatura CE dei serramenti.</p></li>
    </ol>
  </div>
</section>

<section class="band" aria-labelledby="reno-t">
  <div class="wrap split">
    <div>
      <h2 id="reno-t">Cambiare le finestre senza rompere i muri</h2>
      <p class="lead">Quando il vecchio telaio è sano e ben fissato, il nuovo serramento si posa sopra di esso con un telaio da ristrutturazione.</p>
      <ul class="checks">
        <li>Niente demolizioni di intonaci, davanzali e piastrelle.</li>
        <li>Un'aletta da 35, 40 o 60 mm copre il vecchio telaio sul lato interno.</li>
        <li>Lavoro più rapido e più pulito, anche con la casa abitata.</li>
      </ul>
      <p>Al sopralluogo verifichiamo se il telaio esistente lo consente. Se è deteriorato, lo rimuoviamo e posiamo il nuovo serramento sul vano.</p>
      <a class="textlink" href="posa.html">Come facciamo la posa</a>
    </div>
    <figure class="sheet">{dw.renovation()}<figcaption>Schema di posa con telaio da ristrutturazione sul telaio esistente.</figcaption></figure>
  </div>
</section>

<section class="band ink tight" aria-labelledby="det-t">
  <div class="wrap">
    <div class="band-head">
      <h2 id="det-t">Detrazioni 2026: il 50% vale fino al 31 dicembre</h2>
      <p class="muted">Per le spese pagate nel 2026, con Ecobonus o Bonus casa. Dal 2027 la legge in vigore prevede aliquote più basse.</p>
    </div>
    <div class="rates">
      <div><span class="pct">50%</span><p>sull'abitazione principale, se paga il proprietario o il titolare di un diritto reale</p></div>
      <div><span class="pct">36%</span><p>sugli altri immobili, comprese le seconde case</p></div>
      <div><span class="pct">10 anni</span><p>la detrazione si recupera in dieci quote annuali uguali</p></div>
    </div>
    <p style="margin-top:24px"><a class="textlink" href="detrazioni.html" style="color:#fff">Requisiti, zone climatiche e documenti</a></p>
  </div>
</section>

<section class="band" aria-labelledby="faq-t">
  <div class="wrap">
    <div class="band-head"><h2 id="faq-t">Domande frequenti</h2><p class="muted">Se la tua domanda non c'è, chiamaci: rispondiamo noi, non un call center.</p></div>
    <div class="faq">
      <details><summary>Cosa indica il valore Uw?</summary><div><p>Uw è la trasmittanza termica dell'intera finestra: quanti watt di calore passano attraverso un metro quadrato di serramento per ogni grado di differenza tra dentro e fuori. Più è basso, meno calore perdi. Comprende telaio, vetro e bordo del vetro, quindi è il numero giusto per confrontare due finestre.</p></div></details>
      <details><summary>Meglio doppio o triplo vetro?</summary><div><p>Il triplo vetro isola circa il doppio di un buon doppio vetro (Ug 0,5 contro 1,0–1,1 W/m²K) e riduce la sensazione di freddo vicino alla finestra. È la scelta consigliata nelle zone climatiche E ed F e per le stanze esposte a nord. Il doppio vetro resta valido nelle zone più miti o quando serve contenere il peso delle ante.</p></div></details>
      <details><summary>Posso sostituire le finestre senza togliere il vecchio telaio?</summary><div><p>Sì, se il telaio esistente è sano e ben ancorato al muro. Si usa un telaio da ristrutturazione con aletta che copre il vecchio. Lo verifichiamo al sopralluogo: se il legno è marcio o il telaio è instabile, conviene rimuoverlo.</p></div></details>
      <details><summary>Il sopralluogo e il preventivo si pagano?</summary><div><p>No. Il sopralluogo e il preventivo sono gratuiti e senza impegno.</p></div></details>
      <details><summary>Che manutenzione richiede una finestra in PVC?</summary><div><p>Poca. Pulisci i profili con acqua e detergente neutro, senza prodotti abrasivi o solventi. Una volta l'anno lubrifica i punti di chiusura della ferramenta e controlla che le guarnizioni siano pulite ed elastiche. Le fessure di drenaggio nel telaio vanno tenute libere.</p></div></details>
      <details><summary>In quali zone lavorate?</summary><div><p>Operiamo a Roma e nella Marsica. Per altre località contattaci: valutiamo caso per caso.</p></div></details>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# FINESTRE
# ---------------------------------------------------------------------------
def page_head(crumb, h1, lead, toc=None):
    t = ""
    if toc:
        t = '<ul class="toc">' + "".join(f'<li><a href="#{a}">{b}</a></li>' for a, b in toc) + "</ul>"
    return f"""<section class="page-head"><div class="wrap">
<p class="crumbs"><a href="./">Home</a> / {crumb}</p>
<h1>{h1}</h1>
<p class="lead">{lead}</p>{t}
</div></section>"""


def finestre():
    toc = [(w["key"], w["name"]) for w in WIN] + [("confronto", "Confronto"), ("dati", "Come leggere i dati"), ("finiture", "Colori e finiture")]
    blocks = []
    for w in WIN:
        var = "".join(f'<div class="variant"><h3>{a}</h3><p>{b}</p></div>' for a, b in w["variants"])
        rn, rt = w["reno"]
        blocks.append(f"""<section class="product" id="{w['key']}" aria-labelledby="{w['key']}-t"><div class="wrap product-grid">
<figure class="sheet">{dw.section(w['key'], 'plain', uid='f' + w['key'])}<figcaption>{w['name']}: sezione schematica di telaio, anta e vetrocamera. Quote in millimetri.</figcaption></figure>
<div>
  <h2 id="{w['key']}-t">{w['name']}</h2>
  <p class="tag">{w['tag']}</p>
  <p>{w['intro']}</p>
  <dl class="titleblock">
    <div><dt>Uw finestra</dt><dd>{w['uw']} W/m²K</dd></div>
    <div><dt>Uf telaio</dt><dd>{w['uf']} W/m²K</dd></div>
    <div><dt>Ug vetro</dt><dd>{w['ug']} W/m²K</dd></div>
    <div><dt>Profondità</dt><dd>{w['depth']}</dd></div>
    <div><dt>Camere</dt><dd>{w['ch']}</dd></div>
    <div><dt>Guarnizioni</dt><dd>{w['gask']}</dd></div>
    <div><dt>Vetrocamera</dt><dd>{w['glass']}</dd></div>
    <div><dt>Fermavetri</dt><dd>{w['bead']}</dd></div>
    <div><dt>Rinforzi</dt><dd>{w['reinf']}</dd></div>
  </dl>
  {var}
  <div class="variant"><h3>{rn}: versione da ristrutturazione</h3><p>{rt}</p></div>
</div></div></section>""")

    rows = []
    for w in WIN:
        best = ' class="num best"' if w["key"] == "sirente" else ' class="num"'
        rows.append(f"<tr><th scope=row>{w['name']}</th><td>{w['depth']}</td><td>{w['ch']}</td><td>3</td>"
                    f"<td{best}>{w['uw']}</td><td class=num>{w['uf']}</td><td>{w['glass']}</td></tr>")
        if w["key"] == "fucino":
            rows.append("<tr class=sub><th scope=row>Fucino 76 Composito</th><td>telaio 76 mm, anta 80 mm</td><td>6 nel telaio</td><td>3</td><td class=num>0,73</td><td class=num>0,96</td><td>da 24 a 52 mm</td></tr>")
    reno = [
        ("Velino 82 R", "35 o 60 mm", "triplo, Ug 0,5", "0,76"),
        ("Sirente 80 R", "60 mm", "doppio, Ug 1,0", "1,3"),
        ("Fucino 76 R", "40 mm", "doppio, Ug 1,0", "1,3"),
        ("Salviano 72 R", "35 o 60 mm", "doppio, Ug 1,1", "1,3"),
    ]
    rrows = "".join(f"<tr><th scope=row>{a}</th><td>{b}</td><td>{c}</td><td class=num>{d}</td></tr>" for a, b, c, d in reno)

    return page_head(
        "Finestre",
        "Finestre e portefinestre in PVC",
        "Quattro profili da 72 a 82 mm, tutti con tre guarnizioni e rinforzi nel telaio e nell'anta. Per ognuno trovi la sezione, i valori misurati e la versione per sostituire senza opere murarie.",
        toc,
    ) + "".join(blocks) + f"""
<section class="band" id="confronto" aria-labelledby="conf-t"><div class="wrap">
  <div class="band-head"><h2 id="conf-t">Confronto tra le linee</h2><p class="muted">Valori Uw e Uf in W/m²K, riferiti alla {REF}.</p></div>
  <div class="tablewrap"><table class="spec">
    <thead><tr><th scope=col>Linea</th><th scope=col>Profondità</th><th scope=col>Camere</th><th scope=col>Guarnizioni</th><th scope=col class=num>Uw</th><th scope=col class=num>Uf</th><th scope=col>Vetrocamera</th></tr></thead>
    <tbody>{''.join(rows)}</tbody></table></div>
  <h3 style="margin-top:48px">Versioni da ristrutturazione</h3>
  <div class="tablewrap"><table class="spec" style="min-width:560px">
    <thead><tr><th scope=col>Linea</th><th scope=col>Aletta</th><th scope=col>Vetro di riferimento</th><th scope=col class=num>Uw</th></tr></thead>
    <tbody>{rrows}</tbody></table></div>
  <p class="small muted" style="margin-top:12px">Nelle versioni da ristrutturazione il valore indicato dal produttore è riferito al vetro di riferimento della tabella. Con triplo vetro il valore migliora: lo calcoliamo nel preventivo sulle misure reali.</p>
</div></section>

<section class="band white" id="dati" aria-labelledby="dati-t"><div class="wrap">
  <div class="band-head"><h2 id="dati-t">Come leggere i dati tecnici</h2><p class="muted">Sei numeri bastano per confrontare due finestre in modo serio.</p></div>
  <div class="grid-3">
    <div class="item"><h3>Uw, la finestra intera</h3><p>Trasmittanza termica del serramento completo, in W/m²K. È il valore richiesto per le detrazioni e quello da confrontare: più basso è, meno calore si disperde.</p></div>
    <div class="item"><h3>Uf, il telaio</h3><p>Trasmittanza del solo profilo. Dipende da profondità, numero di camere e tipo di rinforzo. Un rinforzo composito al posto dell'acciaio la abbassa.</p></div>
    <div class="item"><h3>Ug, il vetro</h3><p>Trasmittanza della vetrocamera al centro della lastra. Un triplo vetro basso emissivo con gas argon arriva a 0,5 W/m²K.</p></div>
    <div class="item"><h3>Ψ, il bordo del vetro</h3><p>Il ponte termico lungo il perimetro del vetro, dove si trova la canalina distanziatrice. Con la canalina calda è molto più basso che con l'alluminio, e si riduce il rischio di condensa sul bordo.</p></div>
    <div class="item"><h3>Camere e profondità</h3><p>Le camere sono le celle d'aria interne al profilo. Più profondità significa più camere, più spazio per il rinforzo e vetri più spessi.</p></div>
    <div class="item"><h3>Tre guarnizioni</h3><p>Oltre alle guarnizioni esterna e interna, una guarnizione centrale divide la battuta in due zone: migliora tenuta all'aria, isolamento acustico e protegge la ferramenta dall'umidità.</p></div>
  </div>
  <div class="note"><p>Gli angoli dei profili sono giuntati con una tecnica di saldatura di precisione che non lascia il cordone visibile: lo spigolo resta pulito e continuo. Le classi di profilo (A, B) sono definite dalla norma europea sui profili in PVC per serramenti in base allo spessore delle pareti esterne.</p></div>
</div></section>

<section class="band" id="finiture" aria-labelledby="fin-t"><div class="wrap split">
  <div>
    <h2 id="fin-t">Colori e finiture</h2>
    <p>Il profilo è colorato in massa, quindi non va mai verniciato. Sopra si applicano in fabbrica pellicole decorative in tinta unita ed effetto legno, anche diverse tra interno ed esterno. Su ogni linea ci sono alcuni colori standard e circa quaranta colori a richiesta.</p>
    <p>Sui profili colorati gli angoli sono saldati a filo, senza la fresatura che lascia un solco bianco nello spigolo.</p>
    <p>Maniglie, canaline del vetro e coprifili si abbinano al colore scelto. Al sopralluogo portiamo il campionario: i colori a video non sono affidabili.</p>
  </div>
  <div class="titleblock collapse" style="--cols:2">
    <div><span class="k">In massa</span><span class="v">Bianco</span><span class="n">su tutte le linee; il Fucino 76 anche in grafite</span></div>
    <div><span class="k">Effetto legno</span><span class="v">Pellicole goffrate</span><span class="n">rovere dorato, noce, rovere scuro, mogano, douglas, pino</span></div>
    <div><span class="k">Tinte unite</span><span class="v">Pellicole lisce o opache</span><span class="n">antracite, grigi, crema, verde e blu scuro, finiture metallizzate</span></div>
    <div><span class="k">Esterno alluminio</span><span class="v">Tutta la gamma RAL</span><span class="n">rivestimento disponibile sul Velino 82</span></div>
  </div>
</div>
<div class="wrap"><div class="note"><p>Valori tecnici dichiarati dal produttore dei profili, calcolati secondo EN ISO 10077 sulla {REF} dove non diversamente indicato. Le prestazioni del tuo serramento dipendono da misure, vetro e accessori e sono riportate nel preventivo e nella dichiarazione di prestazione (marcatura CE secondo EN 14351-1). I disegni sono schemi illustrativi originali, non disegni costruttivi.</p></div></div>
</section>
"""


# ---------------------------------------------------------------------------
# SCORREVOLI
# ---------------------------------------------------------------------------
def scorrevoli():
    return page_head(
        "Scorrevoli",
        "Alzanti e scorrevoli in PVC",
        "Quattro sistemi per aprire il soggiorno sul terrazzo o sul giardino: dall'alzante da 6 metri con soglia ribassata allo scorrevole parallelo che si apre anche a ribalta.",
        [("alzante", "Alzante scorrevole"), ("tenuta", "Scorrevole a tenuta perimetrale"), ("leggero", "Scorrevole leggero"), ("parallelo", "Scorrevole parallelo"), ("tabella", "Confronto")],
    ) + f"""
<section class="product" id="alzante" aria-labelledby="alz-t"><div class="wrap product-grid">
  <figure class="sheet" style="padding:28px">{dw.scheme('A')}<div style="height:18px"></div>{dw.scheme('4')}<figcaption>Schemi tipici: un campo fisso e un'anta mobile, oppure quattro campi con due ante mobili centrali. Vista dall'interno.</figcaption></figure>
  <div>
    <h2 id="alz-t">Alzante scorrevole</h2>
    <p class="tag">Le aperture più grandi: fino a 6 metri di larghezza in bianco.</p>
    <p>Girando la maniglia l'anta si solleva di pochi millimetri dalle guarnizioni e scorre su carrelli nascosti nella soglia, con uno sforzo minimo anche per ante pesanti. Riportando giù la maniglia l'anta si abbassa e torna a tenuta; si blocca in qualsiasi posizione. Il vetro della parte fissa resta montato nell'anta.</p>
    <p>La soglia in alluminio si può incassare quasi a filo pavimento: con una rampa di raccordo da 5 o 15 mm il passaggio verso il terrazzo è praticamente libero. Nei profili colorati le larghezze massime sono un po' minori, da 5 a 5,25 m secondo la versione.</p>
    <dl class="titleblock">
      <div><dt>Larghezza massima</dt><dd>fino a 6 m</dd></div>
      <div><dt>Uw</dt><dd>da 0,73 W/m²K</dd></div>
      <div><dt>Vetrocamera</dt><dd>da 24 a 52 mm</dd></div>
    </dl>
    <div class="tablewrap"><table class="spec" style="min-width:600px">
      <thead><tr><th scope=col>Versione</th><th scope=col>Telaio / anta</th><th scope=col class=num>Uw</th><th scope=col>Vetrocamera</th><th scope=col>Campione</th></tr></thead>
      <tbody>
        <tr><th scope=row>Alzante 82</th><td>194 / 82 mm</td><td class=num>0,73</td><td>24–48 mm</td><td>4800 × 2500 mm</td></tr>
        <tr><th scope=row>Alzante 80</th><td>190 / 80 mm</td><td class=num>0,74</td><td>48 mm</td><td>4000 × 2300 mm</td></tr>
        <tr><th scope=row>Alzante 76</th><td>175 / 76 mm</td><td class=num>0,75</td><td>24–52 mm</td><td>4800 × 2500 mm</td></tr>
      </tbody></table></div>
    <p class="small muted" style="margin-top:10px">L'alzante non ha la funzione a ribalta. Le versioni 82, 80 e 76 si abbinano rispettivamente alle finestre Velino, Sirente e Fucino.</p>
  </div>
</div></section>

<section class="product" id="tenuta" aria-labelledby="pl-t"><div class="wrap product-grid">
  <figure class="sheet" style="padding:28px">{dw.scheme('A')}<figcaption>Schema con un campo fisso e un'anta scorrevole.</figcaption></figure>
  <div>
    <h2 id="pl-t">Scorrevole a tenuta perimetrale</h2>
    <p class="tag">Il valore Uw più basso tra gli scorrevoli: 0,69 W/m²K.</p>
    <p>Si apre come un alzante, facendo scorrere l'anta principale davanti alla parte fissa con poco sforzo. In chiusura l'anta viene spinta contro il telaio e le guarnizioni lavorano a compressione su tutto il perimetro: ne risultano tenuta all'aria e isolamento molto elevati.</p>
    <p>L'anta si blocca in qualsiasi posizione e ha la microventilazione. Più leggero e meno ingombrante di un alzante, è adatto anche ai piani alti. La soglia è alta 56 mm e si può incassare in parte nel pavimento; il vetro della parte fissa è montato nel telaio.</p>
    <dl class="titleblock">
      <div><dt>Larghezza massima</dt><dd>3,9 m<span class="n">con altezza fino a 2,34 m; alto fino a 2,6 m con larghezza fino a 3,5 m</span></dd></div>
      <div><dt>Uw</dt><dd>0,69 W/m²K</dd></div>
      <div><dt>Telaio / anta</dt><dd>152 / 76 mm</dd></div>
      <div><dt>Vetrocamera</dt><dd>da 24 a 48 mm</dd></div>
      <div><dt>Uf</dt><dd>1,3 W/m²K</dd></div>
      <div><dt>Campione</dt><dd>3460 × 2600 mm</dd></div>
    </dl>
  </div>
</div></section>

<section class="product" id="leggero" aria-labelledby="lg-t"><div class="wrap product-grid">
  <figure class="sheet" style="padding:28px">{dw.scheme('A')}<div style="height:18px"></div>{dw.scheme('D')}<figcaption>Schema con anta fissa e anta mobile, oppure con due ante scorrevoli.</figcaption></figure>
  <div>
    <h2 id="lg-t">Scorrevole leggero</h2>
    <p class="tag">La soluzione semplice per terrazzi, verande e locali di servizio.</p>
    <p>L'anta attiva scorre dietro quella fissa; nella versione a due ante mobili scorrono entrambe. Il telaio da 76 mm fa anche da soglia. Non c'è funzione a ribalta.</p>
    <dl class="titleblock">
      <div><dt>Versione alta</dt><dd>3000 × 2480 mm<span class="n">fino a 6 m² di superficie</span></dd></div>
      <div><dt>Versione bassa</dt><dd>3000 × 1600 mm<span class="n">fino a 5,6 m²; anta attiva max 1000 mm</span></dd></div>
      <div><dt>Uw</dt><dd>1,2 W/m²K<span class="n">con doppio vetro Ug 1,0</span></dd></div>
      <div><dt>Telaio / anta</dt><dd>76 / 50 mm</dd></div>
      <div><dt>Vetrocamera</dt><dd>24 mm</dd></div>
      <div><dt>Uf</dt><dd>1,8 W/m²K</dd></div>
    </dl>
  </div>
</div></section>

<section class="product" id="parallelo" aria-labelledby="par-t"><div class="wrap product-grid">
  <figure class="sheet" style="padding:28px">{dw.scheme('PSK')}<figcaption>Scorrevole parallelo: l'anta si apre prima a ribalta, poi si sposta in parallelo e scorre.</figcaption></figure>
  <div>
    <h2 id="par-t">Scorrevole parallelo con ribalta</h2>
    <p class="tag">L'unico scorrevole che si apre anche a ribalta per arieggiare.</p>
    <p>Da chiuso, anta mobile e parte fissa sono sullo stesso piano, con un aspetto pulito. In apertura l'anta va prima a ribalta, poi si stacca dal telaio e scorre su un binario nella parte bassa, visibile all'esterno e protetto da una copertura.</p>
    <p>Si realizza su tutte le nostre linee di finestre, anche nelle versioni da ristrutturazione Velino 82 R e Salviano 72 R. È lo scorrevole più economico; la soglia non può essere portata a filo pavimento.</p>
    <dl class="titleblock">
      <div><dt>Dimensioni massime</dt><dd>3 × 2,5 m<span class="n">ante fino a 200 kg con la ferramenta a leva</span></dd></div>
      <div><dt>Profili</dt><dd>72, 76, 80, 82 mm</dd></div>
      <div><dt>Vetro fisso</dt><dd>nel telaio o nell'anta</dd></div>
    </dl>
    <div class="variant"><h3>Ferramenta con leva di comando</h3><p>Una maniglia di controllo dedicata aiuta a staccare, far scorrere e richiudere anche ante molto pesanti. In alternativa c'è la versione a comando manuale.</p></div>
    <div class="variant"><h3>Ferramenta con aerazione parallela</h3><p>L'anta si può fermare parallela al telaio, a circa 6 mm di distanza su tutto il perimetro: entra aria, non entrano insetti, e la porta resta chiusa in sicurezza anche quando in casa non c'è nessuno.</p></div>
  </div>
</div></section>

<section class="band white" id="tabella" aria-labelledby="tb-t"><div class="wrap">
  <div class="band-head"><h2 id="tb-t">Quale scorrevole scegliere</h2><p class="muted">Un confronto rapido sui punti che contano nella scelta.</p></div>
  <div class="tablewrap"><table class="spec">
    <thead><tr><th scope=col>Sistema</th><th scope=col>Larghezza max</th><th scope=col class=num>Uw migliore</th><th scope=col>Soglia</th><th scope=col>Ribalta</th><th scope=col>Ideale per</th></tr></thead>
    <tbody>
      <tr><th scope=row>Alzante scorrevole</th><td>6 m</td><td class=num>0,73</td><td>quasi a filo pavimento</td><td>no</td><td>grandi vetrate su terrazzi e giardini</td></tr>
      <tr><th scope=row>Tenuta perimetrale</th><td>3,9 m</td><td class="num best">0,69</td><td>56 mm, in parte incassabile</td><td>no</td><td>massimo isolamento, zone fredde</td></tr>
      <tr><th scope=row>Scorrevole leggero</th><td>3 m</td><td class=num>1,2</td><td>profilo del telaio</td><td>no</td><td>verande, terrazzi coperti, locali di servizio</td></tr>
      <tr><th scope=row>Parallelo con ribalta</th><td>3 m</td><td class=num>secondo la linea</td><td>rialzata</td><td>sì</td><td>portefinestre dove serve anche arieggiare</td></tr>
    </tbody></table></div>
  <div class="note"><p>Valori Uw in W/m²K dichiarati dal produttore dei profili per gli scorrevoli campione indicati, con triplo vetro Ug 0,5 e canalina calda salvo diversa indicazione. Dimensioni massime soggette a verifica statica sul singolo progetto.</p></div>
</div></section>
"""


# ---------------------------------------------------------------------------
# PORTE
# ---------------------------------------------------------------------------
def porte():
    return page_head(
        "Porte d'ingresso",
        "Porte d'ingresso in PVC",
        "Porte su profili da 76 a 82 mm, con soglia in alluminio, serrature multipunto e riempimenti in vetro o pannello. Isolano come una finestra e chiudono come una porta di sicurezza.",
        [("sistemi", "Sistemi"), ("serrature", "Serrature"), ("riempimenti", "Riempimenti e maniglie")],
    ) + f"""
<section class="band" id="sistemi" aria-labelledby="ps-t"><div class="wrap">
  <div class="band-head"><h2 id="ps-t">Tre sistemi, abbinati alle finestre</h2><p class="muted">Ud è la trasmittanza della porta intera, in W/m²K, misurata sulla porta campione 1230 × 2180 mm con triplo vetro.</p></div>
  <div class="tablewrap"><table class="spec">
    <thead><tr><th scope=col>Porta</th><th scope=col>Profondità</th><th scope=col>Camere telaio / anta</th><th scope=col class=num>Ud</th><th scope=col class=num>Uf</th><th scope=col>Vetrocamera</th></tr></thead>
    <tbody>
      <tr><th scope=row>Porta Velino 82</th><td>82 mm</td><td>6 / 5</td><td class="num best">0,83</td><td class=num>1,1</td><td>24–48 mm</td></tr>
      <tr><th scope=row>Porta Fucino 76</th><td>76 mm</td><td>6 / 5</td><td class=num>0,90</td><td class=num>1,4</td><td>24–52 mm</td></tr>
      <tr><th scope=row>Porta Sirente 80</th><td>80 mm</td><td>5 / 5</td><td class=num>0,93</td><td class=num>1,2</td><td>24, 28 o 48 mm</td></tr>
    </tbody></table></div>
  <div class="grid-3" style="margin-top:56px">
    <div class="item">{dw.elev_door().replace('class="elev"', 'class="elev" style="height:110px;width:auto;color:#13294B;margin-bottom:18px"')}<h3>Configurazioni</h3><p>Apertura verso l'interno o verso l'esterno, a un'anta o a due ante, con fianchi laterali e sopraluce fissi.</p></div>
    <div class="item"><h3>Soglia in alluminio</h3><p>Progettata per la tenuta all'acqua e all'aria anche con vento forte, con un ingombro ridotto al passaggio.</p></div>
    <div class="item"><h3>Cerniere standard o a scomparsa</h3><p>Cerniere regolabili in tre direzioni, oppure nascoste nello spessore della porta per una superficie esterna pulita. Sul Velino 82 è disponibile anche il telaio da ristrutturazione con aletta da 35 o 60 mm.</p></div>
  </div>
</div></section>

<section class="band white" id="serrature" aria-labelledby="sr-t"><div class="wrap">
  <div class="band-head"><h2 id="sr-t">Serrature</h2><p class="muted">Tutte con chiusura a ganci, che agganciano il telaio invece di scivolare in una sede: l'anta resta tirata contro le guarnizioni.</p></div>
  <div class="grid-2">
    <div class="item"><h3>Multipunto a chiave</h3><p>Tre punti di chiusura con ganci singoli di serie, oppure cinque punti per una maggiore resistenza. Una o due serrature.</p></div>
    <div class="item"><h3>Automatica autobloccante</h3><p>Chiude da sola tre punti con ganci doppi appena accosti la porta, senza girare la chiave. Il selettore giorno e notte decide se dall'esterno serve la chiave.</p></div>
    <div class="item"><h3>Elettromeccanica</h3><p>Serratura automatica con sblocco elettrico nascosto nell'anta: dall'interno si apre con la maniglia, dall'esterno con lettore d'impronta digitale o tastiera a codice.</p></div>
    <div class="item"><h3>Elettromeccanica connessa</h3><p>La stessa serratura con modulo radio integrato: apri la porta dallo smartphone o dal tablet tramite Bluetooth o rete Wi-Fi, con un'app dedicata.</p></div>
  </div>
</div></section>

<section class="band" id="riempimenti" aria-labelledby="ri-t"><div class="wrap split">
  <div>
    <h2 id="ri-t">Riempimenti e maniglie</h2>
    <p>Il riempimento può essere tutto vetro, vetro parziale o un pannello decorativo, classico o moderno, oltre al pannello liscio in PVC. Per i vetri delle porte usiamo vetri di sicurezza stratificati.</p>
    <p>Le maniglie si scelgono tra maniglia e maniglia, maniglia e pomolo, o maniglione esterno. Sono disponibili in diverse forme e finiture, dal bianco all'antracite fino agli effetti metallici.</p>
    <p>Al sopralluogo ti mostriamo il catalogo completo dei pannelli e dei maniglioni.</p>
  </div>
  <div class="note" style="margin-top:0"><p>Una porta d'ingresso rientra nell'Ecobonus se separa l'ambiente riscaldato dall'esterno o da un vano non riscaldato e rispetta la trasmittanza richiesta per la zona climatica. Se l'obiettivo è soprattutto antintrusione, si valuta il Bonus casa per gli interventi di sicurezza. <a href="detrazioni.html">Dettagli sulle detrazioni</a>.</p></div>
</div></section>
"""


# ---------------------------------------------------------------------------
# VETRI E ACCESSORI
# ---------------------------------------------------------------------------
def accessori():
    return page_head(
        "Vetri e accessori",
        "Vetri, ferramenta e accessori",
        "La metà dell'isolamento e quasi tutta la sicurezza di una finestra dipendono da vetro, ferramenta e maniglia. Qui trovi cosa scegliere e perché.",
        [("vetri", "Vetrocamera"), ("ferramenta", "Ferramenta"), ("maniglie", "Maniglie e sicurezza"), ("aerazione", "Aerazione"), ("oscuranti", "Avvolgibili e cassonetti"), ("finiture", "Finiture e raccordi"), ("alluminio", "Alluminio")],
    ) + f"""
<section class="band" id="vetri" aria-labelledby="v-t"><div class="wrap">
  <div class="band-head"><h2 id="v-t">Vetrocamera</h2><p class="muted">Lastre di vetro separate da una canalina e sigillate, con l'intercapedine riempita di gas nobile, argon o kripton.</p></div>
  <div class="grid-3">
    <div class="item">{dw.glass_build('double')}<h3>Doppio vetro</h3><p>Due lastre con rivestimento basso emissivo e argon: Ug intorno a 1,0–1,1 W/m²K. Adatto alle zone climatiche miti e alle ante dove serve contenere il peso.</p></div>
    <div class="item">{dw.glass_build('triple')}<h3>Triplo vetro</h3><p>Tre lastre e due intercapedini: Ug fino a 0,5 W/m²K. È la composizione di riferimento per i valori Uw delle nostre finestre.</p></div>
    <div class="item">{dw.glass_build('vsg')}<h3>Triplo vetro stratificato</h3><p>Lastre esterna e interna stratificate con pellicola: se il vetro si rompe, i frammenti restano incollati. Più sicurezza e un isolamento acustico migliore.</p></div>
  </div>
  <hr class="rule">
  <div class="grid-2">
    <div class="item"><h3>Canalina calda</h3><p>Il distanziatore tra le lastre è in materiale a bassa conducibilità invece che in alluminio. Riduce il ponte termico sul bordo del vetro, quindi la condensa negli angoli. Disponibile nella versione standard (Ψ 0,040 W/mK) e in quella ad alte prestazioni (Ψ 0,032 W/mK), in nero, grigio, marrone, grigio chiaro o tono legno.</p></div>
    <div class="item"><h3>Rivestimento basso emissivo</h3><p>Uno strato invisibile di ossidi metallici sulla lastra riflette il calore verso l'interno della casa. Il tipo di rivestimento determina sia l'Ug sia la quantità di luce che passa.</p></div>
    <div class="item"><h3>Vetri di sicurezza</h3><p>Il vetro temprato si rompe in piccoli frammenti smussati; il vetro stratificato resta in sede grazie alla pellicola interna, e con più pellicole raggiunge le classi antieffrazione. La norma UNI 7697 indica dove il vetro di sicurezza è obbligatorio: portefinestre, parapetti, ante vetrate vicino al pavimento.</p></div>
    <div class="item"><h3>Vetri acustici</h3><p>Pellicole fonoassorbenti e lastre di spessore diverso, la cosiddetta composizione asimmetrica, riducono il rumore del traffico dove non si può eliminare la sorgente.</p></div>
    <div class="item"><h3>Controllo solare</h3><p>I vetri selettivi riducono il calore del sole in estate lasciando passare molta luce. Esistono anche vetri riflettenti e colorati in pasta, per le facciate più esposte.</p></div>
    <div class="item"><h3>Privacy e decorazione</h3><p>Vetri satinati, sabbiati e stampati riducono la visibilità verso l'interno, per bagni, ingressi e piani terra. Ne abbiamo una quindicina di disegni a catalogo.</p></div>
    <div class="item"><h3>Triplo vetro alleggerito</h3><p>Con la lastra centrale da 3 mm il triplo vetro pesa fino al 25% in meno e poco più di un doppio vetro tradizionale. Utile su ante grandi e su ferramenta già esistente.</p></div>
  </div>
</div></section>

<section class="band white" id="ferramenta" aria-labelledby="fe-t"><div class="wrap">
  <div class="band-head"><h2 id="fe-t">Ferramenta</h2><p class="muted">I meccanismi nascosti nel telaio che muovono e chiudono l'anta. Tutte le versioni hanno microventilazione e blocco della falsa manovra.</p></div>
  <div class="grid-2">
    <div class="item"><h3>Standard anta e ribalta</h3><p>Chiusura con nottolini a fungo ottagonali che agganciano riscontri standard o antieffrazione e permettono di regolare la pressione dell'anta. Di serie la microventilazione, con un'apertura a ribalta di 2–3 mm, e l'elemento che blocca la maniglia ad anta aperta e accompagna l'anta in chiusura.</p></div>
    <div class="item"><h3>Cerniere a scomparsa</h3><p>Le cerniere stanno nella camera asciutta tra anta e telaio e non si vedono a finestra chiusa. La guarnizione corre senza interruzioni su tutto il perimetro e i punti di chiusura sono vicini agli angoli, dove servono di più contro lo scasso.</p></div>
    <div class="item"><h3>Aerazione parallela</h3><p>Oltre ad anta e ribalta, l'anta può restare chiusa e staccata di circa 6 mm dal telaio su tutto il perimetro: l'aria si cambia in modo naturale con la finestra bloccata. Resistenza all'effrazione in classe RC2 anche in questa posizione, sulle finestre a un'anta.</p></div>
    <div class="item"><h3>Prima la ribalta</h3><p>Ordine di apertura invertito: la maniglia apre prima a ribalta, l'apertura completa richiede un'ulteriore rotazione e una maniglia con chiave. Pensata per scuole, ospedali e per le case con bambini piccoli.</p></div>
  </div>
</div></section>

<section class="band" id="maniglie" aria-labelledby="ma-t"><div class="wrap">
  <div class="band-head"><h2 id="ma-t">Maniglie e sicurezza</h2><p class="muted">La maniglia è anche un dispositivo di sicurezza.</p></div>
  <div class="grid-3">
    <div class="item"><h3>Maniglia con blocco</h3><p>Di serie su quasi tutte le linee: un meccanismo interno impedisce di manovrare la ferramenta dall'esterno, mentre dall'interno la maniglia si usa normalmente. Disponibile anche con chiave o con pulsante.</p></div>
    <div class="item"><h3>Maniglie antieffrazione</h3><p>Si bloccano da sole in posizione chiusa e a ribalta e si aprono solo premendo prima il pulsante. Proteggono dai tentativi di apertura con rottura del vetro, foratura del telaio o spostamento della ferramenta.</p></div>
    <div class="item"><h3>Forme e finiture</h3><p>Dalla maniglia classica arrotondata a quella squadrata in alluminio, di serie sul Fucino 76. Finiture bianco, marrone, nero, antracite, titanio, oro, argento ed effetti metallici satinati.</p></div>
    <div class="item"><h3>Blocco di apertura controllata</h3><p>Un fermo invisibile a finestra chiusa che impedisce l'apertura completa dell'anta finché non viene sbloccato in modo consapevole. Protegge bambini e anziani; si monta anche su finestre esistenti.</p></div>
    <div class="item"><h3>Fermo magnetico</h3><p>Blocca anta o portafinestra nella posizione scelta, anche a ribalta: il vento o un animale domestico non la spostano, una persona sì. Invisibile a finestra chiusa.</p></div>
    <div class="item"><h3>Altri accessori</h3><p>Limitatore di apertura, serratura per finestra, scrocco per portafinestra sul balcone, riscontri antieffrazione.</p></div>
  </div>
</div></section>

<section class="band white" id="aerazione" aria-labelledby="ae-t"><div class="wrap split">
  <div>
    <h2 id="ae-t">Aerazione controllata</h2>
    <p>Una finestra nuova chiude molto meglio di quella vecchia. È un vantaggio per il riscaldamento, ma l'umidità prodotta in casa deve comunque uscire. Gli aeratori portano un ricambio d'aria minimo e continuo senza aprire.</p>
    <ul class="checks">
      <li><strong>Igroregolabili</strong>: montati sull'anta, si aprono di più quando l'umidità della stanza sale. Senza alimentazione elettrica; esistono versioni acustiche.</li>
      <li><strong>A regolazione di pressione</strong>: la portata d'aria dipende dalla differenza di pressione tra esterno e interno.</li>
      <li><strong>Autoregolanti nel vetro</strong>: in alluminio, tra vetrocamera e telaio, per vetrocamere da 24 mm. In tutti i colori RAL.</li>
    </ul>
  </div>
  <div class="callout"><p>Se oggi hai condensa o muffa negli angoli delle stanze, parliamone al sopralluogo: spesso la soluzione è un insieme di vetro con canalina calda, posa corretta del giunto e un aeratore dove serve.</p></div>
</div></section>

<section class="band" id="oscuranti" aria-labelledby="os-t"><div class="wrap">
  <div class="band-head"><h2 id="os-t">Avvolgibili e cassonetti</h2><p class="muted">Il cassonetto è spesso il punto più freddo della parete: va scelto insieme alla finestra.</p></div>
  <div class="grid-3">
    <div class="item"><h3>Cassonetto esterno a vista</h3><p>Per edifici esistenti, senza toccare la muratura: montato sopra la finestra o nel vano, a sezione squadrata, ovale o semiovale. Avvolgibile manuale o motorizzato, con zanzariera integrabile.</p></div>
    <div class="item"><h3>Sotto intonaco</h3><p>Per nuove costruzioni e ristrutturazioni con cappotto: il cassonetto sta sotto lo strato isolante e dopo la finitura non si vede. Ispezione dall'esterno, motore o comando manuale, zanzariera integrabile.</p></div>
    <div class="item"><h3>Monoblocco coibentato</h3><p>Il cassonetto arriva montato sulla finestra e si posa con essa: dopo l'intonaco scompare. Misure da 230 × 170 a 255 × 240 mm.</p></div>
    <div class="item"><h3>Cassonetti per ristrutturazione</h3><p>Cassonetti interni da 59 o 129 mm di profondità, con pannelli di ispezione in PVC da 10 o 24 mm, nei colori dei profili.</p></div>
    <div class="item"><h3>Teli e doghe</h3><p>Doghe in PVC o in alluminio coibentato, da 39 a 77 mm di altezza, per superfici fino a 15 m². Per i garage, serrande avvolgibili e portoni sezionali su richiesta.</p></div>
    <div class="item"><h3>Zanzariere</h3><p>A telaio fisso, anche per forme irregolari; a rullo con piccolo cassonetto; scorrevoli e plissettate con binario basso, per alzanti e grandi aperture. Telai in alluminio, rete in fibra di vetro.</p></div>
  </div>
  <div class="note"><p>Anche il cassonetto rientra nelle detrazioni se è coibentato o sostituito insieme agli infissi e rispetta i valori di trasmittanza richiesti per le finestre.</p></div>
</div></section>

<section class="band white" id="finiture" aria-labelledby="fr-t"><div class="wrap">
  <div class="band-head"><h2 id="fr-t">Finiture e raccordi</h2><p class="muted">I dettagli che fanno sembrare la finestra nata con la casa.</p></div>
  <div class="grid-3">
    <div class="item"><h3>Coprifili e angolari</h3><p>Profili in PVC da 30 a 100 mm che chiudono il giunto tra finestra e muro, davanzale o rivestimento, dentro e fuori. Anche in versione camerata, più rigida.</p></div>
    <div class="item"><h3>Profili di compensazione</h3><p>Allargamenti da 10 a 150 mm per adattare il serramento a vani fuori misura o al cassonetto, con o senza rinforzo in acciaio.</p></div>
    <div class="item"><h3>Montanti e accoppiamenti</h3><p>Montanti fissi o mobili e giunti statici per accostare più serramenti, comporre vetrate d'angolo e portefinestre con sopraluce.</p></div>
    <div class="item"><h3>Davanzali esterni</h3><p>In acciaio o alluminio verniciato, nei colori dei serramenti, con sporgenza e pendenza verso l'esterno per allontanare l'acqua dalla facciata.</p></div>
    <div class="item"><h3>Davanzali interni</h3><p>In MDF, agglomerato di marmo e resina, granito o PVC pellicolato abbinato al colore della finestra.</p></div>
    <div class="item"><h3>Scuretti e persiane</h3><p>Scuretti interni e persiane esterne in abbinamento al serramento, su richiesta.</p></div>
  </div>
</div></section>

<section class="band" id="alluminio" aria-labelledby="al-t"><div class="wrap">
  <div class="band-head"><h2 id="al-t">Su richiesta, anche in alluminio</h2><p class="muted">Per le situazioni in cui il PVC non è la scelta giusta: vetrate molto grandi, facciate continue, negozi, giardini.</p></div>
  <div class="grid-4">
    <div class="item"><h3>Finestre e porte a taglio termico</h3><p>Profili da 65 a 90 mm con vetrocamera tripla, anche con anta a scomparsa e cerniere nascoste.</p></div>
    <div class="item"><h3>Grandi scorrevoli</h3><p>Alzanti e scorrevoli con ante fino a diverse centinaia di chili, soglia ribassata e angoli tutto vetro senza montante.</p></div>
    <div class="item"><h3>Pergole bioclimatiche</h3><p>Lamelle orientabili che chiudono a tenuta d'acqua o si aprono per ventilare, con scarico integrato nei pilastri e chiusure laterali opzionali.</p></div>
    <div class="item"><h3>Portoni da garage</h3><p>Serrande avvolgibili coibentate e portoni sezionali, a comando manuale o motorizzato.</p></div>
  </div>
</div></section>
"""


# ---------------------------------------------------------------------------
# POSA
# ---------------------------------------------------------------------------
def posa():
    return page_head(
        "Posa",
        "Sostituzione e posa in opera",
        "Una finestra eccellente posata male isola come una finestra mediocre. Il giunto tra serramento e muro deve essere a tenuta d'acqua fuori, isolato al centro e a tenuta di vapore dentro.",
        [("sostituzione", "Due modi di sostituire"), ("giunto", "Il giunto a tre livelli"), ("processo", "Le fasi del lavoro"), ("documenti", "Cosa ti consegniamo")],
    ) + f"""
<section class="band" id="sostituzione" aria-labelledby="so-t"><div class="wrap split">
  <div>
    <h2 id="so-t">Due modi di sostituire una finestra</h2>
    <h3>Sul telaio esistente</h3>
    <p>Se il vecchio telaio è sano, asciutto e ben ancorato, lo lasciamo in opera e posiamo sopra di esso un telaio da ristrutturazione. L'aletta, da 35, 40 o 60 mm a seconda della linea, copre il vecchio telaio sul lato interno. Non si rompono intonaci né davanzali e i tempi di cantiere si accorciano.</p>
    <h3>Con rimozione completa</h3>
    <p>Se il telaio è deteriorato, fuori squadra o ha zone marce, lo rimuoviamo e posiamo il nuovo serramento direttamente sul vano o su un controtelaio. È la scelta che massimizza la luce e garantisce il giunto migliore. Comporta piccole finiture murarie intorno al vano.</p>
    <p>La scelta la facciamo insieme al sopralluogo, dopo aver controllato il telaio.</p>
  </div>
  <figure class="sheet">{dw.renovation(uid='rv2')}<figcaption>Telaio da ristrutturazione posato sul telaio esistente.</figcaption></figure>
</div></section>

<section class="band white" id="giunto" aria-labelledby="gi-t"><div class="wrap">
  <div class="band-head"><h2 id="gi-t">Il giunto a tre livelli</h2><p class="muted">Lo stesso principio è alla base della norma UNI 11673-1 sulla progettazione della posa dei serramenti. La regola da ricordare: più chiuso dentro che fuori.</p></div>
  <div class="grid-3">
    <div class="item"><h3>Esterno: tenuta all'acqua</h3><p>Sul lato esterno il giunto deve fermare pioggia battente e vento, ma lasciare uscire il vapore. Si usano nastri e sigillanti impermeabili e traspiranti.</p></div>
    <div class="item"><h3>Centro: isolamento</h3><p>Lo spazio tra telaio e muro viene riempito con materiali isolanti termici e acustici, schiume o nastri espandenti, senza lasciare vuoti.</p></div>
    <div class="item"><h3>Interno: barriera al vapore</h3><p>Sul lato interno il giunto deve essere più chiuso al vapore di quello esterno, così l'umidità della casa non condensa dentro l'isolamento.</p></div>
  </div>
  <hr class="rule">
  <div class="grid-3">
    <div class="item"><h3>Fissaggio</h3><p>Viti, tasselli o zanche in acciaio, a non più di 70 cm l'uno dall'altro e a 10–15 cm dagli angoli e dai montanti. La schiuma isola ma non regge il serramento: il fissaggio meccanico va sempre fatto.</p></div>
    <div class="item"><h3>Posizione nel muro</h3><p>Nei muri senza isolamento la finestra si posa verso la metà dello spessore; con il cappotto, nello strato isolante, su un controtelaio isolante. Così la superficie interna del giunto resta calda e non forma condensa.</p></div>
    <div class="item"><h3>Tolleranze e verifica</h3><p>Fuori piombo entro 1,5 mm per metro, differenza tra le diagonali entro 2–3 mm. A fine posa ogni anta deve aprirsi senza attriti, restare ferma da aperta e chiudere premendo in modo uniforme.</p></div>
  </div>
  <div class="note"><p>Davanzale, cassonetto e soglia sono i punti in cui il giunto si interrompe più spesso e vanno risolti uno per uno. La pellicola protettiva dei profili va tolta entro due settimane dalla posa: esposta al sole, poi si stacca a fatica.</p></div>
</div></section>

<section class="band ink" id="processo" aria-labelledby="pr-t"><div class="wrap">
  <div class="band-head"><h2 id="pr-t">Le fasi del lavoro</h2><p class="muted">Cosa succede dal primo contatto alla consegna.</p></div>
  <ol class="steps">
    <li><h3>Sopralluogo</h3><p>Stato dei vecchi telai, muratura, esposizione, cassonetti. Raccogliamo le tue esigenze su freddo, rumore e luce.</p></li>
    <li><h3>Rilievo</h3><p>Misure di ogni vano e scelta del metodo di sostituzione, finestra per finestra.</p></li>
    <li><h3>Preventivo</h3><p>Serramento, vetro, accessori, posa e smontaggio indicati voce per voce, con i valori tecnici.</p></li>
    <li><h3>Posa</h3><p>Protezione degli ambienti, smontaggio, posa con giunto a tre livelli, montaggio di coprifili e accessori.</p></li>
    <li><h3>Regolazione e verifica</h3><p>Regoliamo la ferramenta, controlliamo chiusure e scorrimenti e ti mostriamo come usare e pulire i serramenti.</p></li>
  </ol>
</div></section>

<section class="band" id="documenti" aria-labelledby="do-t"><div class="wrap split">
  <div>
    <h2 id="do-t">Cosa ti consegniamo</h2>
    <ul class="checks">
      <li>Dichiarazione di prestazione e marcatura CE di ogni serramento, secondo la norma EN 14351-1.</li>
      <li>Valori di trasmittanza Uw dei serramenti installati, necessari per la pratica di detrazione.</li>
      <li>Istruzioni d'uso e di manutenzione di ferramenta e guarnizioni.</li>
      <li>Fattura con la descrizione dell'intervento coerente con l'agevolazione scelta.</li>
    </ul>
  </div>
  <div class="callout"><p>La comunicazione all'ENEA va inviata entro 90 giorni dalla fine dei lavori. Ti diciamo quali dati servono e te li forniamo già pronti per il tuo tecnico o per il CAF.</p></div>
</div></section>
"""


# ---------------------------------------------------------------------------
# DETRAZIONI
# ---------------------------------------------------------------------------
def detrazioni():
    return page_head(
        "Detrazioni",
        "Detrazioni fiscali 2026 per finestre e porte",
        "La sostituzione degli infissi si detrae con l'Ecobonus o con il Bonus casa. Nel 2026 entrambi valgono il 50% sull'abitazione principale e il 36% sugli altri immobili. Aggiornato a novembre 2026.",
        [("aliquote", "Aliquote"), ("quale", "Ecobonus o Bonus casa"), ("zone", "Zone climatiche"), ("documenti", "Documenti e scadenze")],
    ) + f"""
<section class="band" id="aliquote" aria-labelledby="al-t"><div class="wrap">
  <div class="band-head"><h2 id="al-t">Le aliquote per le spese pagate nel 2026</h2><p class="muted">La detrazione si recupera in dieci quote annuali dall'IRPEF. Non sono più disponibili lo sconto in fattura né la cessione del credito.</p></div>
  <div class="rates">
    <div><span class="pct">50%</span><p>abitazione principale, se la spesa è sostenuta dal proprietario o dal titolare di un diritto reale (usufrutto, uso, abitazione)</p></div>
    <div><span class="pct">36%</span><p>tutti gli altri casi: seconde case, immobili non abitativi, inquilini e comodatari</p></div>
    <div><span class="pct">2027</span><p>la legge oggi in vigore prevede il 36% sull'abitazione principale e il 30% sugli altri immobili, salvo modifiche della prossima legge di bilancio</p></div>
  </div>
  <div class="callout"><p>Conta la data del bonifico, non quella dei lavori o della fattura. Per avere il 50% il pagamento deve partire entro il 31 dicembre 2026.</p></div>
</div></section>

<section class="band white" id="quale" aria-labelledby="qu-t"><div class="wrap">
  <div class="band-head"><h2 id="qu-t">Ecobonus o Bonus casa</h2><p class="muted">Stessa aliquota, regole diverse. Si sceglie prima dell'ordine.</p></div>
  <div class="tablewrap"><table class="spec">
    <thead><tr><th scope=col></th><th scope=col>Ecobonus</th><th scope=col>Bonus casa (ristrutturazioni)</th></tr></thead>
    <tbody>
      <tr><th scope=row>Cosa agevola</th><td>Sostituzione di finestre che delimitano ambienti riscaldati, per risparmio energetico</td><td>Interventi di recupero edilizio, compresa la sostituzione degli infissi</td></tr>
      <tr><th scope=row>Limite</th><td>60.000 € di detrazione per unità immobiliare</td><td>96.000 € di spesa per unità immobiliare, comprensivo degli altri lavori</td></tr>
      <tr><th scope=row>Requisito tecnico</th><td>Uw non superiore al limite della zona climatica</td><td>Miglioramento rispetto all'esistente; se cambiano forma, materiale o colore può servire un titolo edilizio</td></tr>
      <tr><th scope=row>ENEA</th><td>Comunicazione entro 90 giorni dalla fine lavori, obbligatoria</td><td>Comunicazione entro 90 giorni prevista anche per gli infissi</td></tr>
      <tr><th scope=row>Beneficiari</th><td>Persone fisiche, anche titolari di reddito d'impresa, e società</td><td>Persone fisiche soggette a IRPEF</td></tr>
    </tbody></table></div>
  <p class="small muted" style="margin-top:12px">Non sono agevolabili le nuove aperture o l'ampliamento dei vani: la detrazione riguarda la sostituzione di serramenti esistenti. Per porte blindate, grate, serrature e vetri antisfondamento si può usare il Bonus casa per gli interventi di sicurezza.</p>
</div></section>

<section class="band" id="zone" aria-labelledby="zo-t"><div class="wrap split">
  <div>
    <h2 id="zo-t">Il limite di trasmittanza dipende dal comune</h2>
    <p>Per l'Ecobonus il valore Uw del nuovo serramento non deve superare il limite della zona climatica del comune in cui si trova l'immobile (allegato E del DM 6 agosto 2020).</p>
    <p>Roma è in zona D. Avezzano e gran parte della Marsica sono in zona E; diversi comuni di montagna sono in zona F, dove il limite è 1,0 W/m²K e serve il triplo vetro.</p>
    <p>Tutte le nostre linee con triplo vetro restano sotto il limite della zona F. Le versioni da ristrutturazione con doppio vetro arrivano a 1,3 W/m²K: vanno bene fino alla zona E, mentre in zona F richiedono il triplo vetro.</p>
  </div>
  <div class="tablewrap"><table class="spec" style="min-width:0">
    <thead><tr><th scope=col>Zona climatica</th><th scope=col class=num>Uw massimo</th><th scope=col>Esempi</th></tr></thead>
    <tbody>
      <tr><th scope=row>A e B</th><td class=num>2,60</td><td>Lampedusa, Palermo</td></tr>
      <tr><th scope=row>C</th><td class=num>1,75</td><td>Napoli, Bari</td></tr>
      <tr><th scope=row>D</th><td class=num>1,67</td><td>Roma, Firenze</td></tr>
      <tr><th scope=row>E</th><td class=num>1,30</td><td>Avezzano, L'Aquila, Milano</td></tr>
      <tr><th scope=row>F</th><td class=num>1,00</td><td>comuni di alta montagna</td></tr>
    </tbody></table></div>
</div></section>

<section class="band white" id="documenti" aria-labelledby="dc-t"><div class="wrap">
  <div class="band-head"><h2 id="dc-t">Documenti e scadenze</h2><p class="muted">Cosa serve per non perdere la detrazione.</p></div>
  <ol class="steps four">
    <li><h3>Prima dell'ordine</h3><p>Scegli l'agevolazione e verifica la zona climatica. Il preventivo deve indicare serramenti, posa, accessori e trasmittanza.</p></li>
    <li><h3>Pagamento</h3><p>Bonifico parlante per detrazioni fiscali, con causale, codice fiscale di chi detrae e partita IVA dell'impresa.</p></li>
    <li><h3>Fine lavori</h3><p>Entro 90 giorni, comunicazione all'ENEA sul portale dell'anno di fine lavori.</p></li>
    <li><h3>Conservazione</h3><p>Fatture, ricevute dei bonifici, schede tecniche e marcatura CE dei serramenti, ricevuta ENEA, eventuale asseverazione del tecnico.</p></li>
  </ol>
  <div class="note"><p>Queste informazioni hanno scopo divulgativo, sono aggiornate a novembre 2026 sulla base della Legge di Bilancio 2026 e delle indicazioni ENEA, e non costituiscono consulenza fiscale. Prima di avviare i lavori verifica la tua situazione con un commercialista o un CAF. Fonti ufficiali: <a href="https://www.agenziaentrate.gov.it/portale/web/guest/agevolazioni" rel="noopener">Agenzia delle Entrate</a> e <a href="https://www.efficienzaenergetica.enea.it/detrazioni-fiscali.html" rel="noopener">ENEA, detrazioni fiscali</a>.</p></div>
</div></section>
"""


# ---------------------------------------------------------------------------
# CONTATTI
# ---------------------------------------------------------------------------
def contatti():
    chips = "".join(
        f'<label><input type="checkbox" name="interesse" value="{v}"> {v}</label>'
        for v in ["Finestre", "Portefinestre", "Alzante o scorrevole", "Porta d'ingresso", "Avvolgibili e cassonetti", "Altro"]
    )
    return page_head(
        "Contatti",
        "Richiedi un sopralluogo",
        "Raccontaci cosa vuoi sostituire. Ti richiamiamo entro un giorno lavorativo per fissare il sopralluogo: è gratuito e senza impegno.",
    ) + f"""
<section class="band"><div class="wrap contact-grid">
  <div>
    <h2>Parla direttamente con noi</h2>
    <div class="people">
      <div><span class="name">Telefono</span><br><a class="tel" href="tel:{CO['tel1_raw']}">{CO['tel1']}</a><br><a class="tel" href="tel:{CO['tel2_raw']}">{CO['tel2']}</a></div>
      <div><span class="name">Email</span><br><a class="mail" href="mailto:{CO['email']}">{CO['email']}</a></div>
      <div><span class="name">WhatsApp</span><br><a href="{CO['wa']}" rel="noopener">Scrivici al {CO['tel1']}</a></div>
    </div>
    <dl class="titleblock collapse" style="--cols:1">
      <div><dt>Orari</dt><dd>{CO['hours']}</dd></div>
      <div><dt>Zona di lavoro</dt><dd>{CO['area']}</dd></div>
      <div><dt>Sede legale</dt><dd>{CO['address']}</dd></div>
    </dl>
    <h3 style="margin-top:36px">Per un preventivo più preciso</h3>
    <ul class="checks">
      <li>Indica quante finestre e porte vuoi cambiare e le misure approssimative.</li>
      <li>Allega o mandaci su WhatsApp una foto dei vecchi infissi, dentro e fuori.</li>
      <li>Dicci il comune: serve per la zona climatica e le detrazioni.</li>
    </ul>
  </div>
  <form class="quote" action="{CO['form']}" method="POST">
    <h2 style="font-size:1.5rem">Modulo di richiesta</h2>
    <input type="hidden" name="_subject" value="Richiesta sopralluogo dal sito">
    <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
    <div class="two">
      <div class="field"><label for="nome">Nome e cognome</label><input id="nome" name="nome" type="text" autocomplete="name" required></div>
      <div class="field"><label for="tel">Telefono</label><input id="tel" name="telefono" type="tel" autocomplete="tel" required></div>
    </div>
    <div class="two">
      <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
      <div class="field"><label for="comune">Comune dell'immobile</label><input id="comune" name="comune" type="text" autocomplete="address-level2"></div>
    </div>
    <fieldset class="field"><legend>Cosa ti interessa <span class="hint">(anche più di una voce)</span></legend><div class="chips">{chips}</div></fieldset>
    <div class="field"><label for="n">Quanti serramenti, circa <span class="hint">(facoltativo)</span></label>
      <select id="n" name="quantita"><option value="">Seleziona</option><option>1–3</option><option>4–8</option><option>9–15</option><option>Più di 15</option><option>Non so ancora</option></select></div>
    <div class="field"><label for="msg">Messaggio</label><textarea id="msg" name="messaggio" placeholder="Per esempio: 6 finestre in legno degli anni '80, zona rumorosa, vorrei sapere se posso usare il 50%."></textarea></div>
    <div class="field consent"><input id="ok" name="consenso_privacy" type="checkbox" value="sì" required><label for="ok" style="font-weight:400;margin:0">Ho letto l'<a href="privacy.html">informativa sulla privacy</a> e acconsento al trattamento dei dati per ricevere una risposta alla mia richiesta.</label></div>
    <button class="btn" type="submit">Invia la richiesta</button>
    <p class="form-msg" role="status" aria-live="polite"></p>
  </form>
</div></section>
"""


def grazie():
    return f"""<section class="page-head"><div class="wrap">
<h1>Richiesta inviata</h1>
<p class="lead">Grazie. Ti richiamiamo entro un giorno lavorativo per fissare il sopralluogo. Se è urgente, chiamaci al <a href="tel:{CO['tel1_raw']}">{CO['tel1']}</a> o al <a href="tel:{CO['tel2_raw']}">{CO['tel2']}</a>, oppure scrivi a <a href="mailto:{CO['email']}">{CO['email']}</a>.</p>
<p style="margin-top:28px"><a class="btn ghost" href="./">Torna alla home</a></p>
</div></section>"""


def notfound():
    return """<section class="page-head"><div class="wrap">
<h1>Pagina non trovata</h1>
<p class="lead">L'indirizzo che hai aperto non esiste o è stato spostato. Da qui puoi tornare alle sezioni principali.</p>
<ul class="toc"><li><a href="/">Home</a></li><li><a href="/finestre.html">Finestre</a></li><li><a href="/scorrevoli.html">Scorrevoli</a></li><li><a href="/porte.html">Porte d'ingresso</a></li><li><a href="/contatti.html">Contatti</a></li></ul>
</div></section>"""


# ---------------------------------------------------------------------------
# PAGINE LEGALI
# ---------------------------------------------------------------------------
def privacy():
    return page_head("Privacy", "Informativa sulla privacy", "Come trattiamo i dati personali che ci invii tramite il sito, ai sensi degli articoli 13 e 14 del Regolamento (UE) 2016/679 (GDPR).") + f"""
<section class="band"><div class="wrap prose">
<h2>Titolare del trattamento</h2>
<p>{CO['name']}, {CO['address']}, P. IVA {CO['vat']}. Email <a href="mailto:{CO['email']}">{CO['email']}</a>, PEC {CO['pec']}.</p>
<h2>Quali dati trattiamo</h2>
<ul>
<li><strong>Dati che ci invii</strong> con il modulo di contatto, per email, telefono o WhatsApp: nome, telefono, email, comune dell'immobile, contenuto del messaggio ed eventuali foto.</li>
<li><strong>Dati tecnici di navigazione</strong> registrati automaticamente dal servizio di hosting (indirizzo IP, data e ora, pagina richiesta), necessari al funzionamento e alla sicurezza del sito.</li>
</ul>
<p>Il sito non usa cookie di profilazione, strumenti di statistica o pubblicità, né carica caratteri, mappe o video da server di terze parti.</p>
<h2>Finalità e basi giuridiche</h2>
<ul>
<li>Rispondere alla tua richiesta, fissare il sopralluogo e predisporre il preventivo: misure precontrattuali richieste da te (art. 6.1.b GDPR).</li>
<li>Gestire l'eventuale contratto e gli obblighi fiscali e contabili: esecuzione del contratto e obbligo di legge (art. 6.1.b e 6.1.c).</li>
<li>Garantire la sicurezza del sito: legittimo interesse (art. 6.1.f).</li>
</ul>
<h2>Destinatari</h2>
<p>I messaggi del modulo di contatto passano attraverso Formspree, Inc. (Stati Uniti), che agisce come responsabile del trattamento; il trasferimento è tutelato dalle clausole contrattuali standard della Commissione europea e, ove applicabile, dal Data Privacy Framework UE-USA. I dati possono essere comunicati al consulente fiscale, al servizio di hosting e, se acquisti, ai fornitori che producono i serramenti, limitatamente a quanto necessario per l'ordine. Non vendiamo né cediamo dati a terzi per finalità commerciali.</p>
<h2>Conservazione</h2>
<p>Le richieste che non portano a un contratto sono cancellate entro 24 mesi. I dati legati a un contratto sono conservati per 10 anni, come richiesto dalla normativa fiscale. I dati di navigazione sono conservati dal servizio di hosting per il tempo strettamente necessario.</p>
<h2>I tuoi diritti</h2>
<p>Puoi chiedere accesso, rettifica, cancellazione, limitazione, portabilità e opporti al trattamento scrivendo a <a href="mailto:{CO['email']}">{CO['email']}</a>. Hai diritto di proporre reclamo al Garante per la protezione dei dati personali (<a href="https://www.garanteprivacy.it" rel="noopener">garanteprivacy.it</a>).</p>
<p>Il conferimento dei dati del modulo è facoltativo, ma senza nome e almeno un recapito non possiamo risponderti.</p>
<p class="muted small">Ultimo aggiornamento: {CO['updated'].lower()}.</p>
</div></section>"""


def cookie():
    return page_head("Cookie", "Cookie", "Questo sito non installa cookie di profilazione né cookie di terze parti.") + f"""
<section class="band"><div class="wrap prose">
<p>Il sito usa soltanto le risorse tecniche necessarie a mostrare le pagine. Non usiamo strumenti di statistica, pixel pubblicitari, pulsanti social, mappe o video incorporati, e i caratteri tipografici sono ospitati sul nostro server. Per questo non ti chiediamo alcun consenso e non mostriamo il banner dei cookie, come previsto dalle Linee guida del Garante del 10 giugno 2021.</p>
<p>I link verso siti esterni, come WhatsApp, Agenzia delle Entrate o ENEA, ti portano su pagine con proprie informative sui cookie.</p>
<p>Se in futuro introdurremo strumenti che richiedono il consenso, aggiorneremo questa pagina e te lo chiederemo prima di attivarli.</p>
<p>Per domande: <a href="mailto:{CO['email']}">{CO['email']}</a>.</p>
</div></section>"""


def note_legali():
    return page_head("Note legali", "Note legali", "Dati societari e condizioni d'uso delle informazioni pubblicate sul sito.") + f"""
<section class="band"><div class="wrap prose">
<h2>Dati societari</h2>
<p>{CO['name']}<br>Sede legale: {CO['address']}<br>Registro delle Imprese di Roma, C.F. e P. IVA {CO['vat']}, REA {CO['rea']}<br>Capitale sociale {CO['capital']}<br>PEC: {CO['pec']} · Codice destinatario SDI: 5RUO82D</p>
<h2>Informazioni tecniche</h2>
<p>I valori di trasmittanza (Uw, Uf, Ug, Ud) sono dichiarati dal produttore dei profili e calcolati secondo EN ISO 10077-1 e 10077-2 su serramenti campione delle dimensioni indicate. I valori del singolo serramento dipendono da misure, vetro e accessori e sono riportati nel preventivo e nella dichiarazione di prestazione rilasciata con la marcatura CE secondo EN 14351-1.</p>
<p>I disegni e gli schemi pubblicati sono elaborazioni originali a scopo illustrativo e non costituiscono disegni costruttivi. I colori visualizzati a schermo possono differire dai campioni reali e tra lotti di produzione possono esserci lievi differenze di tonalità.</p>
<h2>Vetri di sicurezza</h2>
<p>La scelta del vetro deve rispettare la norma UNI 7697 sui vetri di sicurezza nelle applicazioni edilizie. In fase di preventivo indichiamo le composizioni idonee a ogni posizione.</p>
<h2>Prezzi e offerte</h2>
<p>Il sito non pubblica prezzi. Ogni offerta è formulata per iscritto dopo il sopralluogo e ha validità indicata nel preventivo.</p>
<h2>Detrazioni fiscali</h2>
<p>Le informazioni sulle detrazioni hanno scopo divulgativo e non costituiscono consulenza fiscale. La spettanza della detrazione dipende dalla situazione del contribuente e va verificata con un professionista.</p>
<h2>Proprietà intellettuale</h2>
<p>Testi, disegni e grafica del sito sono di {CO['name']}. Il riuso è consentito citando la fonte, salvo che per fini commerciali. I marchi citati appartengono ai rispettivi titolari.</p>
</div></section>"""


def redirect(target):
    def f():
        return f'<section class="page-head"><div class="wrap"><h1>Pagina spostata</h1><p class="lead">Il contenuto è ora in <a href="{target}">{target}</a>.</p></div></section><script>location.replace("{target}")</script>'
    return f


PAGES = [
    {"file": "index.html", "title": "Marsicalluminio · Finestre in PVC ad alto isolamento a Roma e nella Marsica",
     "desc": "Fornitura e posa di finestre, portefinestre, alzanti scorrevoli e porte d'ingresso in PVC. Uw fino a 0,72 W/m²K, sostituzione senza opere murarie, detrazioni 2026.",
     "body": home},
    {"file": "finestre.html", "title": "Finestre in PVC: Velino 82, Sirente 80, Fucino 76, Salviano 72 · Marsicalluminio",
     "desc": "Quattro linee di finestre in PVC da 72 a 82 mm con tre guarnizioni: sezioni, valori Uw, versioni da ristrutturazione, colori e finiture.",
     "body": finestre},
    {"file": "scorrevoli.html", "title": "Alzanti e scorrevoli in PVC · Marsicalluminio",
     "desc": "Alzanti scorrevoli fino a 6 m con soglia ribassata, scorrevoli a tenuta perimetrale con Uw 0,69, scorrevoli leggeri e paralleli con ribalta.",
     "body": scorrevoli},
    {"file": "porte.html", "title": "Porte d'ingresso in PVC · Marsicalluminio",
     "desc": "Porte d'ingresso in PVC da 76 a 82 mm con Ud fino a 0,83 W/m²K, serrature multipunto, automatiche ed elettromeccaniche con apertura da smartphone.",
     "body": porte},
    {"file": "accessori.html", "title": "Vetri, ferramenta e accessori per finestre · Marsicalluminio",
     "desc": "Doppio e triplo vetro, canalina calda, vetri di sicurezza e acustici, ferramenta con aerazione parallela, maniglie antieffrazione, avvolgibili e cassonetti.",
     "body": accessori},
    {"file": "posa.html", "title": "Sostituzione e posa dei serramenti · Marsicalluminio",
     "desc": "Sostituzione delle finestre con o senza rimozione del vecchio telaio, giunto di posa a tre livelli, fasi del lavoro e documenti consegnati.",
     "body": posa},
    {"file": "detrazioni.html", "title": "Detrazioni 2026 per infissi: Ecobonus e Bonus casa · Marsicalluminio",
     "desc": "Bonus infissi 2026: 50% sull'abitazione principale e 36% sugli altri immobili. Limiti Uw per zona climatica, ENEA, bonifico e documenti.",
     "body": detrazioni},
    {"file": "contatti.html", "title": "Contatti e sopralluogo gratuito · Marsicalluminio",
     "desc": "Richiedi un sopralluogo gratuito per finestre, porte e scorrevoli in PVC. Telefono 335 758 4371 o 377 129 0313, email marsicalluminio@gmail.com.",
     "body": contatti, "no_cta": True},
    {"file": "privacy.html", "title": "Informativa sulla privacy · Marsicalluminio", "desc": "Informativa sul trattamento dei dati personali.", "body": privacy, "no_cta": True},
    {"file": "cookie.html", "title": "Cookie · Marsicalluminio", "desc": "Informativa sui cookie.", "body": cookie, "no_cta": True},
    {"file": "note-legali.html", "title": "Note legali · Marsicalluminio", "desc": "Dati societari e note legali.", "body": note_legali, "no_cta": True},
    {"file": "grazie.html", "title": "Richiesta inviata · Marsicalluminio", "desc": "Richiesta inviata.", "body": grazie, "noindex": True, "no_cta": True},
    {"file": "404.html", "title": "Pagina non trovata · Marsicalluminio", "desc": "Pagina non trovata.", "body": notfound, "noindex": True},
    {"file": "tech.html", "title": "Schede tecniche · Marsicalluminio", "desc": "Le schede tecniche sono ora nella pagina Finestre.", "body": redirect("finestre.html"), "noindex": True, "no_cta": True},
    {"file": "marsicalluminio.html", "title": "Marsicalluminio", "desc": "Pagina spostata.", "body": redirect("./"), "noindex": True, "no_cta": True},
]
