"""Disegni tecnici originali (SVG) per il sito Marsicalluminio.

Tutti i disegni sono schemi generati qui: nessuna immagine del fornitore.
Unità interne in millimetri; asse y verso l'alto, convertito in SVG.
"""
from dataclasses import dataclass, field

INK = "#13294B"
STEEL = "#5B6673"
LINE = "#9FB0C0"
FILL = "#E8EEF3"
GLASS = "#D7E7F2"
GASKET = "#2B2F36"


def f(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s == "-0" else s


@dataclass
class Line:
    key: str
    name: str
    depth: int            # profondità telaio
    sash: int             # profondità anta
    chambers_f: int
    chambers_s: int
    glass: int            # spessore vetrocamera disegnato
    panes: int = 3
    bead: str = "straight"   # straight | round | square | soft
    composite: bool = False


LINES = {
    "velino": Line("velino", "Velino 82", 82, 82, 6, 6, 48, bead="round"),
    "sirente": Line("sirente", "Sirente 80", 80, 80, 6, 6, 48, bead="soft"),
    "fucino": Line("fucino", "Fucino 76", 76, 80, 6, 5, 48, bead="square", composite=True),
    "salviano": Line("salviano", "Salviano 72", 72, 72, 5, 5, 44, bead="round"),
}


class Canvas:
    """Accumula elementi SVG in coordinate mm con y verso l'alto."""

    def __init__(self, x0, y0, x1, y1):
        self.x0, self.y0, self.x1, self.y1 = x0, y0, x1, y1
        self.parts = []

    def Y(self, y):
        return self.y1 - y + self.y0

    def pts(self, pts):
        return " ".join(f"{f(x)},{f(self.Y(y))}" for x, y in pts)

    def poly(self, pts, cls="", extra=""):
        self.parts.append(f'<polygon class="{cls}" points="{self.pts(pts)}" {extra}/>')

    def rect(self, x, y, w, h, cls="", extra=""):
        self.parts.append(
            f'<rect class="{cls}" x="{f(x)}" y="{f(self.Y(y + h))}" width="{f(w)}" height="{f(h)}" {extra}/>'
        )

    def path(self, d, cls="", extra=""):
        self.parts.append(f'<path class="{cls}" d="{d}" {extra}/>')

    def line(self, xa, ya, xb, yb, cls="", extra=""):
        self.parts.append(
            f'<line class="{cls}" x1="{f(xa)}" y1="{f(self.Y(ya))}" x2="{f(xb)}" y2="{f(self.Y(yb))}" {extra}/>'
        )

    def text(self, x, y, s, cls="", anchor="start", extra=""):
        self.parts.append(
            f'<text class="{cls}" x="{f(x)}" y="{f(self.Y(y))}" text-anchor="{anchor}" {extra}>{s}</text>'
        )

    def raw(self, s):
        self.parts.append(s)

    def viewbox(self):
        return f"{f(self.x0)} {f(self.y0)} {f(self.x1 - self.x0)} {f(self.y1 - self.y0)}"


def chamber_cols(x0, x1, y0, y1, n, wall, main_frac=0.34):
    """Divide un'area in n camere a colonne; la camera principale è più larga."""
    w = x1 - x0 - wall * (n - 1)
    if n >= 5:
        side = (1 - main_frac) / (n - 1)
        fr = [side] * n
        mi = n // 2 if n % 2 else n // 2 - 1
        fr[mi] = main_frac
    else:
        fr = [1 / n] * n
        mi = n // 2
    cols = []
    x = x0
    for i, fr_i in enumerate(fr):
        cw = w * fr_i
        cols.append((x, y0, cw, y1 - y0))
        x += cw + wall
    return cols, mi


def steel_u(c, x, y, w, h, t=1.6, cls="steel", extra=""):
    inset = 1.4
    x0, y0, x1, y1 = x + inset, y + inset, x + w - inset, y + h - inset
    pts = [(x0, y1), (x0, y0), (x1, y0), (x1, y1), (x1 - t, y1), (x1 - t, y0 + t), (x0 + t, y0 + t), (x0 + t, y1)]
    c.poly(pts, cls, extra)


def section(line_key, mode="plain", callouts=False, dims=True, uid="s", show_names=False, glass_top=None, x_extent=None):
    """Sezione verticale del traverso inferiore (telaio + anta + vetrocamera).

    mode: "plain" disegno tecnico; "thermal" campo termico indicativo.
    """
    L = LINES[line_key]
    D = L.depth
    Hf = 64.0                     # altezza telaio
    lip_h = 16.0                  # aletta esterna del telaio
    gap = 3.0                     # spazio guarnizione centrale
    s0 = 9.0                      # faccia esterna anta
    s1 = D + 7.0                  # faccia interna anta (sormonto)
    body_top = Hf + gap + 38.0    # piano d'appoggio della vetrocamera
    up = 20.0                     # altezza fermavetro / aletta anta
    gx0 = s0 + 7 + 3              # inizio vetro
    G = L.glass
    gx1 = gx0 + G
    top = glass_top if glass_top else body_top + up + 56

    pad_l = 30 if callouts else 16
    pad_r = 84 if callouts else 16
    c = Canvas(-pad_l, -22 if dims else -6, x_extent if x_extent else s1 + pad_r, top + 8)
    wall = 2.4 if L.chambers_f >= 6 else 2.6

    # --- geometria esterna ---
    frame = [(0, 0), (D, 0), (D, Hf), (6, Hf), (6, Hf + lip_h), (1.5, Hf + lip_h), (0, Hf + lip_h - 2.5)]
    # piccola gola inferiore per accessori di raccordo
    frame = [(0, 0), (D * 0.22, 0), (D * 0.22, 3), (D * 0.22 + 8, 3), (D * 0.22 + 8, 0)] + frame[1:]
    lip_x0 = D + 3.0
    sash = [
        (s0, Hf + gap), (lip_x0, Hf + gap), (lip_x0, Hf - 12), (s1, Hf - 12), (s1, body_top + up),
        (gx1 + 3, body_top + up), (gx1 + 3, body_top), (gx0 - 3, body_top), (gx0 - 3, body_top + up),
        (s0, body_top + up - 2), (s0, Hf + gap),
    ]
    # fermavetro
    bx0, bx1 = gx1 + 3.4, s1
    by0, by1 = body_top + 0.4, body_top + up
    if L.bead == "round":
        r = min(9, bx1 - bx0 - 2)
        bead_d = (
            f"M{f(bx0)},{f(c.Y(by0))} L{f(bx1)},{f(c.Y(by0))} L{f(bx1)},{f(c.Y(by1 - r))} "
            f"A{f(r)},{f(r)} 0 0 0 {f(bx1 - r)},{f(c.Y(by1))} L{f(bx0)},{f(c.Y(by1))} Z"
        )
    elif L.bead == "soft":
        ch = 5
        bead_d = (
            f"M{f(bx0)},{f(c.Y(by0))} L{f(bx1)},{f(c.Y(by0))} L{f(bx1)},{f(c.Y(by1 - ch))} "
            f"Q{f(bx1)},{f(c.Y(by1))} {f(bx1 - ch)},{f(c.Y(by1))} L{f(bx0)},{f(c.Y(by1))} Z"
        )
    else:  # straight / square
        ch = 1.2 if L.bead == "square" else 2.5
        bead_d = (
            f"M{f(bx0)},{f(c.Y(by0))} L{f(bx1)},{f(c.Y(by0))} L{f(bx1)},{f(c.Y(by1 - ch))} "
            f"L{f(bx1 - ch)},{f(c.Y(by1))} L{f(bx0)},{f(c.Y(by1))} Z"
        )

    # --- vetrocamera ---
    pane = 4.0
    cav = (G - pane * L.panes) / (L.panes - 1)
    panes = [gx0 + i * (pane + cav) for i in range(L.panes)]
    g_bottom = body_top + 3.0

    defs = []
    hatch = f"h{uid}"
    defs.append(
        f'<pattern id="{hatch}" width="2.2" height="2.2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        f'<line x1="0" y1="0" x2="0" y2="2.2" stroke="{INK}" stroke-width=".5"/></pattern>'
    )
    dots = f"d{uid}"
    defs.append(
        f'<pattern id="{dots}" width="1.8" height="1.8" patternUnits="userSpaceOnUse">'
        f'<circle cx=".9" cy=".9" r=".42" fill="{INK}"/></pattern>'
    )
    therm = f"t{uid}"
    if mode == "thermal":
        defs.append(
            f'<linearGradient id="{therm}" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{f(s1)}" y2="0">'
            '<stop offset="0" stop-color="#2F5F9E"/><stop offset=".18" stop-color="#4F8DC2"/>'
            '<stop offset=".45" stop-color="#8FC3B0"/><stop offset=".66" stop-color="#E7CF6A"/>'
            '<stop offset=".84" stop-color="#E9A04A"/><stop offset="1" stop-color="#DB7A3A"/></linearGradient>'
        )
        defs.append(
            f'<linearGradient id="{therm}a" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{f(s1)}" y2="0">'
            '<stop offset="0" stop-color="#5E8FC4"/><stop offset=".2" stop-color="#86B3D8"/>'
            '<stop offset=".5" stop-color="#C2DFCF"/><stop offset=".7" stop-color="#F2E2A0"/>'
            '<stop offset="1" stop-color="#F2BE86"/></linearGradient>'
        )
    solid = f"url(#{therm})" if mode == "thermal" else FILL
    air = f"url(#{therm}a)" if mode == "thermal" else "#fff"

    c.raw(f"<defs>{''.join(defs)}</defs>")

    g = []
    # contorni pieni
    c.raw(f'<g class="solid" fill="{solid}" stroke="{INK}" stroke-width=".7" stroke-linejoin="round">')
    c.poly(frame, "draw")
    c.poly(sash, "draw")
    c.path(bead_d, "draw")
    c.raw("</g>")

    # camere telaio
    c.raw(f'<g class="ch" fill="{air}" stroke="{INK}" stroke-width=".45">')
    # camera principale con rinforzo
    fy0, fy1 = 2.4, Hf - 2.4
    cols, mi = chamber_cols(2.4, D - 2.4, fy0, fy1, L.chambers_f, wall)
    main_f = None
    for i, (x, y, w, h) in enumerate(cols):
        if i == mi:
            main_f = (x, y, w, h)
            c.rect(x, y, w, h, "draw")
        elif i == 0:
            # camera esterna divisa in due (drenaggio)
            c.rect(x, y, w, h * 0.45 - wall / 2, "draw")
            c.rect(x, y + h * 0.45 + wall / 2, w, h * 0.55 - wall / 2, "draw")
        else:
            c.rect(x, y, w, h, "draw")
    # camere anta
    sy0, sy1 = Hf + gap + 2.4, body_top - 2.4
    scols, smi = chamber_cols(s0 + 2.4, lip_x0 - 2.4, sy0, sy1, L.chambers_s, wall, 0.36)
    main_s = None
    for i, (x, y, w, h) in enumerate(scols):
        c.rect(x, y, w, h, "draw")
        if i == smi:
            main_s = (x, y, w, h)
    # camera nel sormonto e nel fermavetro
    c.rect(lip_x0 + 1.8, Hf - 10.2, s1 - lip_x0 - 3.6, 10.2 + gap - 1.8 + 34, "draw")
    c.rect(bx0 + 2.2, by0 + 2.2, max(2, (bx1 - bx0) - 6), up - 6.5, "draw")
    c.raw("</g>")

    # rinforzi
    c.raw(f'<g class="reinf" fill="url(#{hatch})" stroke="{INK}" stroke-width=".45">')
    if L.composite:
        x, y, w, h = main_f
        c.rect(x + 1.2, y + 1.2, w - 2.4, h - 2.4, "draw", f'fill="url(#{dots})"')
    else:
        steel_u(c, *main_f, cls="draw")
    steel_u(c, *main_s, cls="draw")
    c.raw("</g>")

    # vetrocamera
    c.raw(f'<g class="glass" stroke="{INK}" stroke-width=".5">')
    for i in range(L.panes - 1):
        cx0 = panes[i] + pane
        c.rect(cx0, g_bottom, cav, top - g_bottom, "draw", f'fill="{air if mode == "thermal" else "#F4F9FC"}"')
    for px in panes:
        c.rect(px, g_bottom, pane, top - g_bottom, "draw", f'fill="{solid if mode == "thermal" else GLASS}"')
    # canaline calde + sigillante
    for i in range(L.panes - 1):
        cx0 = panes[i] + pane
        c.rect(cx0, g_bottom, cav, 2.2, "draw", f'fill="{STEEL}"')
        c.rect(cx0 + 0.6, g_bottom + 2.2, cav - 1.2, 7.5, "draw spacer", f'fill="{GASKET}"')
    # rivestimento basso emissivo (linee tratteggiate sulle facce interne)
    for i in (0, L.panes - 1):
        xx = panes[i] + (pane if i == 0 else 0)
        c.line(xx + (0.5 if i == 0 else -0.5), g_bottom + 12, xx + (0.5 if i == 0 else -0.5), top - 2,
               "lowe", f'stroke="{"#fff" if mode == "thermal" else "#3C82B5"}" stroke-width=".55" stroke-dasharray="2 1.4"')
    c.raw("</g>")
    # tasselli di appoggio
    c.rect(gx0 - 0.5, body_top, G + 1, 3, "draw", f'fill="{STEEL}" stroke="{INK}" stroke-width=".35"')

    # guarnizioni (EPDM)
    c.raw(f'<g class="gasket" fill="{GASKET}" stroke="none">')
    xc = D * 0.47
    c.path(  # guarnizione centrale a pinna
        f"M{f(xc)},{f(c.Y(Hf))} l0,-2 q1.6,-1.8 3.4,-1 l0,3 z", "draw")
    c.rect(xc + 0.3, Hf, 2.6, gap, "draw")
    c.rect(6, Hf + 8, 3, 6, "draw")               # esterna (battuta sull'aletta)
    c.rect(D, Hf - 9, 3, 6, "draw")                # interna (sormonto)
    c.rect(gx0 - 3, body_top + up - 7, 3, 6.5, "draw")   # vetro esterna
    c.rect(gx1, body_top + up - 7, 3.4, 6.5, "draw")     # vetro interna
    c.raw("</g>")

    # linea di interruzione sul vetro
    zz = []
    x = gx0 - 6
    step = (G + 12) / 6
    for i in range(7):
        zz.append((x + i * step, top - (1.6 if i % 2 else 0)))
    c.path("M" + " L".join(f"{f(px)},{f(c.Y(py))}" for px, py in zz), "brk",
           f'fill="none" stroke="{STEEL}" stroke-width=".4"')

    # quote
    if dims:
        dy = -12
        c.line(0, 0, 0, dy - 3, "ext", f'stroke="{STEEL}" stroke-width=".3"')
        c.line(D, 0, D, dy - 3, "ext", f'stroke="{STEEL}" stroke-width=".3"')
        c.line(-3, dy, D + 3, dy, "dim", f'stroke="{INK}" stroke-width=".4"')
        for xx in (0, D):
            c.line(xx - 1.6, dy - 1.6, xx + 1.6, dy + 1.6, "tick", f'stroke="{INK}" stroke-width=".7"')
        lab = f"{D}" if L.depth == L.sash else f"{D} / {L.sash}"
        c.text(D / 2, dy + 2.2, lab, "dimt", "middle")
        if callouts:
            c.text(-6, dy - 1.4, "esterno", "side", "end")
            c.text(D + 6, dy - 1.4, "interno", "side", "start")

    if callouts:
        notes = [
            ((panes[1] + 2, top - 26), "Triplo vetro basso emissivo"),
            ((panes[0] + pane + cav / 2, g_bottom + 6), "Canalina calda tra le lastre"),
            ((xc + 1.5, Hf + 1.5), "Guarnizione centrale"),
            ((main_s[0] + main_s[2] / 2, main_s[1] + main_s[3] / 2), "Rinforzo in acciaio"),
            ((cols[-2][0] + cols[-2][2] / 2, 20), f"{L.chambers_f} camere isolanti"),
        ]
        ys = [top - 14, g_bottom + 8, None, None, 20]
        ys[2] = main_s[1] + main_s[3] / 2 + 6
        ys[3] = Hf + 3
        # ordina le note dall'alto verso il basso: vetro, canalina, rinforzo, guarnizione, camere
        notes = [notes[0], notes[1], notes[3], notes[2], notes[4]]
        lx = s1 + 8
        c.raw(f'<g class="callouts" stroke="{INK}" stroke-width=".35" fill="none">')
        for ((px, py), label), ly in zip(notes, ys):
            c.parts.append(
                f'<path class="ldr" d="M{f(px)},{f(c.Y(py))} L{f(lx - 4)},{f(c.Y(ly))} L{f(lx)},{f(c.Y(ly))}"/>'
                f'<circle cx="{f(px)}" cy="{f(c.Y(py))}" r=".9" fill="{INK}" stroke="none"/>'
            )
        c.raw("</g>")
        for ((px, py), label), ly in zip(notes, ys):
            c.text(lx + 1.5, ly - 1.4, label, "cl")

    css = (
        f".dimt{{font:600 4.6px/1 Archivo,sans-serif;fill:{INK}}}"
        f".side{{font:500 4.4px/1 Archivo,sans-serif;fill:{STEEL}}}"
        f".cl{{font:500 4.7px/1 Archivo,sans-serif;fill:{INK}}}"
    )
    return (
        f'<svg class="section section-{line_key} mode-{mode}" viewBox="{c.viewbox()}" '
        f'xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sezione schematica {L.name}">'
        f"<style>{css}</style>{''.join(c.parts)}</svg>"
    )


def scale_lineup():
    """Le quattro sezioni affiancate nella stessa scala, allineate sulla base."""
    order = ["salviano", "fucino", "sirente", "velino"]
    out = []
    for k in order:
        out.append(section(k, uid=f"lu{k}", glass_top=150, x_extent=82 + 7 + 6))
    return dict(zip(order, out))


def renovation(uid="rv"):
    """Telaio da ristrutturazione posato sul vecchio telaio in legno."""
    c = Canvas(-40, -24, 178, 122)
    D = 82
    # vecchio telaio in legno (a sinistra/sotto), muratura
    defs = (
        f'<defs><pattern id="w{uid}" width="6" height="3" patternUnits="userSpaceOnUse">'
        f'<path d="M0,1.5 q1.5,-1.2 3,0 t3,0" fill="none" stroke="#9A7B55" stroke-width=".35"/></pattern>'
        f'<pattern id="m{uid}" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        f'<line x1="0" y1="0" x2="0" y2="4" stroke="{STEEL}" stroke-width=".35"/></pattern>'
        f'<pattern id="h{uid}" width="2.2" height="2.2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
        f'<line x1="0" y1="0" x2="0" y2="2.2" stroke="{INK}" stroke-width=".5"/></pattern></defs>'
    )
    c.raw(defs)
    # muratura
    c.rect(-36, -20, 176, 18, "", f'fill="url(#m{uid})" stroke="{STEEL}" stroke-width=".4"')
    # vecchio telaio legno
    c.rect(-10, -2, 70, 46, "", f'fill="#F3EBDD" stroke="#7D6342" stroke-width=".6"')
    c.rect(-10, -2, 70, 46, "", f'fill="url(#w{uid})" stroke="none"')
    c.rect(5, 14, 40, 7.5, "", 'fill="#fff" stroke="none" opacity=".9"')
    c.text(25, 16, "telaio esistente", "lbl2", "middle")
    # nuovo telaio da ristrutturazione con aletta interna
    x0 = 20
    fr = [(x0, 44), (x0 + D, 44), (x0 + D, 44 + 60), (x0 + 6, 104), (x0 + 6, 118), (x0, 118)]
    c.poly(fr, "", f'fill="{FILL}" stroke="{INK}" stroke-width=".7"')
    # aletta che copre il vecchio telaio verso l'interno
    al = [(x0 + D - 3, 44), (x0 + D - 3, 4), (x0 + D + 2, 4), (x0 + D + 2, 44)]
    c.poly(al, "", f'fill="{FILL}" stroke="{INK}" stroke-width=".7"')
    cols, mi = chamber_cols(x0 + 2.4, x0 + D - 2.4, 46.4, 101.6, 6, 2.4)
    for i, (x, y, w, h) in enumerate(cols):
        c.rect(x, y, w, h, "", f'fill="#fff" stroke="{INK}" stroke-width=".45"')
        if i == mi:
            steel_u(c, x, y, w, h, extra=f'fill="url(#h{uid})" stroke="{INK}" stroke-width=".45"')
    # schiuma / sigillatura
    c.rect(x0, 41, D - 3, 3, "", 'fill="#F2D27A" stroke="none"')
    c.text(x0 + D + 6, 20, "aletta di copertura", "lbl", "start")
    c.text(x0 + D + 6, 14, "35 · 40 · 60 mm", "lbl2", "start")
    c.text(x0 + D + 6, 80, "nuovo telaio", "lbl", "start")
    c.text(x0 + D + 6, 74, "profilo da ristrutturazione", "lbl2", "start")
    c.text(-36, 111, "esterno", "lbl2")
    c.text(146, 111, "interno", "lbl2", "end")
    css = (
        f".lbl{{font:600 4.4px Archivo,sans-serif;fill:{INK}}}.lbl2{{font:400 4px Archivo,sans-serif;fill:{STEEL}}}"
    )
    return (
        f'<svg class="renovation" viewBox="{c.viewbox()}" xmlns="http://www.w3.org/2000/svg" role="img" '
        f'aria-label="Schema di sostituzione con telaio da ristrutturazione posato sul telaio esistente">'
        f"<style>{css}</style>{''.join(c.parts)}</svg>"
    )


# ---------------------------------------------------------------------------
# Prospetti con simboli di apertura (convenzione dei disegni di serramento)
# ---------------------------------------------------------------------------

def _svg(vb, body, label, cls="elev"):
    return (f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="{label}" fill="none" stroke="currentColor" stroke-linejoin="round">'
            f'<style>*{{vector-effect:non-scaling-stroke}}</style>{body}</svg>')


def elev_window():
    b = (
        '<rect x="2" y="2" width="76" height="96" stroke-width="2.4"/>'
        '<rect x="7" y="7" width="31" height="86" stroke-width="1.4"/>'
        '<rect x="42" y="7" width="31" height="86" stroke-width="1.4"/>'
        # anta-ribalta: battente (triangolo dal lato cerniere) + ribalta (dal basso)
        '<path d="M73 7 L42 50 L73 93" stroke-width=".9" stroke-dasharray="3 2.4"/>'
        '<path d="M42 7 L57.5 93 L73 7" stroke-width=".9" stroke-dasharray="1 2"/>'
        '<path d="M7 7 L38 50 L7 93" stroke-width=".9" stroke-dasharray="3 2.4"/>'
        '<line x1="41" y1="46" x2="41" y2="56" stroke-width="2"/>'
    )
    return _svg("0 0 80 100", b, "Prospetto finestra a due ante con apertura ad anta e ribalta")


def elev_sliding():
    b = (
        '<rect x="2" y="2" width="136" height="96" stroke-width="2.4"/>'
        '<rect x="7" y="7" width="64" height="86" stroke-width="1.4"/>'
        '<rect x="69" y="7" width="64" height="86" stroke-width="1.4"/>'
        '<path d="M88 54 H120 M112 48 L120 54 L112 60" stroke-width="1.4"/>'
        '<line x1="76" y1="45" x2="76" y2="63" stroke-width="2"/>'
    )
    return _svg("0 0 140 100", b, "Prospetto alzante scorrevole: un campo fisso e un'anta scorrevole")


def elev_door():
    b = (
        '<rect x="2" y="2" width="56" height="116" stroke-width="2.4"/>'
        '<rect x="7" y="7" width="46" height="111" stroke-width="1.4"/>'
        '<rect x="15" y="16" width="30" height="40" stroke-width=".9"/>'
        '<path d="M53 7 L7 62 L53 118" stroke-width=".9" stroke-dasharray="3 2.4"/>'
        '<line x1="47" y1="60" x2="47" y2="76" stroke-width="2"/>'
        '<line x1="0" y1="118.5" x2="60" y2="118.5" stroke-width="1.2"/>'
    )
    return _svg("0 0 60 120", b, "Prospetto porta d'ingresso a un'anta")


def elev_shutter():
    slats = "".join(f'<line x1="9" y1="{y}" x2="71" y2="{y}" stroke-width=".9"/>' for y in range(26, 92, 7))
    b = (
        '<rect x="2" y="2" width="76" height="96" stroke-width="2.4"/>'
        '<rect x="2" y="2" width="76" height="16" stroke-width="1.4"/>'
        f'<rect x="7" y="18" width="66" height="75" stroke-width="1.2"/>{slats}'
        '<path d="M40 8 V14 M37 11 L40 8 L43 11" stroke-width="1"/>'
    )
    return _svg("0 0 80 100", b, "Prospetto avvolgibile con cassonetto")


def scheme(kind):
    """Schemi di apertura scorrevoli (vista da interno)."""
    if kind == "A":
        b = ('<rect x="1.5" y="1.5" width="117" height="57" stroke-width="2"/>'
             '<line x1="60" y1="1.5" x2="60" y2="58.5" stroke-width="1.2"/>'
             '<text x="30" y="34" font-size="8" fill="currentColor" stroke="none" text-anchor="middle" font-family="Archivo,sans-serif">fisso</text>'
             '<path d="M70 30 H106 M100 25 L106 30 L100 35" stroke-width="1.3"/>')
        return _svg("0 0 120 60", b, "Schema con un campo fisso e un'anta scorrevole", "scheme")
    if kind == "D":
        b = ('<rect x="1.5" y="1.5" width="117" height="57" stroke-width="2"/>'
             '<line x1="60" y1="1.5" x2="60" y2="58.5" stroke-width="1.2"/>'
             '<path d="M50 30 H14 M20 25 L14 30 L20 35" stroke-width="1.3"/>'
             '<path d="M70 30 H106 M100 25 L106 30 L100 35" stroke-width="1.3"/>')
        return _svg("0 0 120 60", b, "Schema con due ante scorrevoli", "scheme")
    if kind == "4":
        b = ('<rect x="1.5" y="1.5" width="157" height="57" stroke-width="2"/>'
             + "".join(f'<line x1="{x}" y1="1.5" x2="{x}" y2="58.5" stroke-width="1.2"/>' for x in (40, 80, 120))
             + '<text x="20" y="34" font-size="8" fill="currentColor" stroke="none" text-anchor="middle" font-family="Archivo,sans-serif">fisso</text>'
             '<text x="140" y="34" font-size="8" fill="currentColor" stroke="none" text-anchor="middle" font-family="Archivo,sans-serif">fisso</text>'
             '<path d="M74 30 H48 M54 25 L48 30 L54 35" stroke-width="1.3"/>'
             '<path d="M86 30 H112 M106 25 L112 30 L106 35" stroke-width="1.3"/>')
        return _svg("0 0 160 60", b, "Schema a quattro campi con due ante scorrevoli centrali", "scheme")
    if kind == "PSK":
        b = ('<rect x="1.5" y="1.5" width="117" height="57" stroke-width="2"/>'
             '<line x1="60" y1="1.5" x2="60" y2="58.5" stroke-width="1.2"/>'
             '<path d="M61.5 4 L89.5 56 L117.5 4" stroke-width=".8" stroke-dasharray="1 1.8"/>'
             '<path d="M70 30 H106 M100 25 L106 30 L100 35" stroke-width="1.3"/>'
             '<text x="30" y="34" font-size="8" fill="currentColor" stroke="none" text-anchor="middle" font-family="Archivo,sans-serif">fisso</text>')
        return _svg("0 0 120 60", b, "Schema scorrevole parallelo con ribalta", "scheme")
    raise ValueError(kind)


def sliding_section(kind, uid="ss"):
    """Sezione orizzontale semplificata di un alzante (due binari)."""
    c = Canvas(-8, -18, 210, 70)
    frame_depth = {"hst82": 194, "hst76": 175, "hst80": 190, "plus": 152}[kind]
    sash = {"hst82": 82, "hst76": 76, "hst80": 80, "plus": 76}[kind]
    W = frame_depth
    c.raw(f'<defs><pattern id="h{uid}" width="2.2" height="2.2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
          f'<line x1="0" y1="0" x2="0" y2="2.2" stroke="{INK}" stroke-width=".5"/></pattern></defs>')
    # soglia
    c.rect(0, 0, W, 10, "", f'fill="{FILL}" stroke="{INK}" stroke-width=".6"')
    for i, x in enumerate(range(4, int(W) - 8, 22)):
        c.rect(x, 2.4, 18, 5.2, "", 'fill="#fff" stroke="#13294B" stroke-width=".35"')
    # binari
    c.rect(W * 0.25, 10, 3, 5, "", f'fill="{STEEL}"')
    c.rect(W * 0.72, 10, 3, 5, "", f'fill="{STEEL}"')
    # ante (esterna fissa, interna scorrevole)
    for x0, lab in ((4, "fisso"), (W - sash - 4, "anta mobile")):
        c.rect(x0, 15, sash, 36, "", f'fill="{FILL}" stroke="{INK}" stroke-width=".6"')
        c.rect(x0 + 12, 51, sash - 24, 14, "", f'fill="{GLASS}" stroke="{INK}" stroke-width=".5"')
        c.text(x0 + sash / 2, 31, lab, "lbl2", "middle")
    # quota
    c.line(0, -8, W, -8, "", f'stroke="{INK}" stroke-width=".4"')
    for xx in (0, W):
        c.line(xx - 1.6, -9.6, xx + 1.6, -6.4, "", f'stroke="{INK}" stroke-width=".7"')
    c.text(W / 2, -14, f"telaio {W} mm · anta {sash} mm", "lbl", "middle")
    css = f".lbl{{font:600 5px Archivo,sans-serif;fill:{INK}}}.lbl2{{font:400 4.6px Archivo,sans-serif;fill:{STEEL}}}"
    return (f'<svg class="slsec" viewBox="{c.viewbox()}" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="Schema della soglia e delle ante">'
            f"<style>{css}</style>{''.join(c.parts)}</svg>")


def glass_build(kind):
    """Composizione della vetrocamera: lastre, intercapedini, canaline."""
    if kind == "double":
        layers = [("v", 4), ("g", 16), ("v", 4)]
    elif kind == "triple":
        layers = [("v", 4), ("g", 18), ("v", 4), ("g", 18), ("v", 4)]
    elif kind == "vsg":
        layers = [("v", 3), ("p", 0.76), ("v", 3), ("g", 16), ("v", 4), ("g", 16), ("v", 3), ("p", 0.76), ("v", 3)]
    s = 2.2
    total = sum(t for _, t in layers)
    x = 6.0
    body = []
    for kind_, t in layers:
        w = t * s
        if kind_ == "v":
            body.append(f'<rect x="{f(x)}" y="6" width="{f(w)}" height="70" fill="{GLASS}" stroke="{INK}" stroke-width=".7"/>')
        elif kind_ == "p":
            body.append(f'<rect x="{f(x)}" y="6" width="{f(max(w, 1.6))}" height="70" fill="{INK}" stroke="none"/>')
        else:
            body.append(f'<rect x="{f(x)}" y="6" width="{f(w)}" height="70" fill="#F7FBFD" stroke="none"/>'
                        f'<rect x="{f(x + 1)}" y="62" width="{f(w - 2)}" height="9" fill="{GASKET}"/>'
                        f'<rect x="{f(x)}" y="71" width="{f(w)}" height="5" fill="{STEEL}"/>')
        x += max(w, 1.6) if kind_ == "p" else w
    W = x + 6
    body.append(f'<line x1="6" y1="84" x2="{f(x)}" y2="84" stroke="{INK}" stroke-width=".6"/>')
    body.append(f'<text x="{f((6 + x) / 2)}" y="94" text-anchor="middle" font-family="Archivo,sans-serif" '
                f'font-size="8" font-weight="600" fill="{INK}">{f(round(total))} mm</text>')
    return (f'<svg class="gbuild" viewBox="0 0 {f(W)} 98" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="Composizione vetrocamera {kind}">{"".join(body)}</svg>')
