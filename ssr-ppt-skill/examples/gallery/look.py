"""Neutral look shared by the layout examples, so the layouts differ only in composition.
Fonts: Noto Sans SC / Noto Serif SC (思源黑体 / 思源宋体; their Black weights are named instances of
the variable fonts) and LXGW WenKai (霞鹜文楷) for one quote. Colours are roles, not a brand."""

SANS = "Noto Sans SC"
SANS_BLACK = "Noto Sans SC Black"
SANS_MEDIUM = "Noto Sans SC Medium"
SERIF = "Noto Serif SC"
SERIF_BLACK = "Noto Serif SC Black"
KAI = "LXGW WenKai"

INK = "1F2A37"
MUTED = "4F5866"
FAINT = "646C78"
LINE = "D9DEE5"
BG = "FFFFFF"
WARM = "F3F5F8"   # a light neutral panel; the name is historical
PRIMARY = "1F4E9E"
PRIMARY_LIGHT = "E3EBF7"
ACCENT = "C2440A"
ACCENT_LIGHT = "FDF0E8"

M = 80          # outer margin (px on a 1280 x 720 canvas)
W = 1120        # content width


def title(deck, s, text, sub=None, y=56, size=40, color=INK, x=M, w=W):
    deck.text(s, x, y, w, size * 2.6 if "\n" in text else size * 1.5, text, size=size, font=SANS, bold=True,
              color=color, line_spacing=1.15)
    if sub:
        deck.text(s, x, y + (size * 2.75 if "\n" in text else size * 1.55), w, 30, sub, size=18, font=SANS, color=MUTED)


def eyebrow(deck, s, text, x=M, y=40, color=MUTED):
    deck.text(s, x, y, 600, 24, text, size=15, font=SANS, color=color, spacing=0.06)


def source(deck, s, text, x=M, y=664, w=W, color=FAINT):
    deck.text(s, x, y, w, 22, text, size=13, font=SANS, color=color)


def ill(deck, s, name, x, y, w, h, **kw):
    kw.setdefault("primary", PRIMARY)
    kw.setdefault("accent", ACCENT)
    return deck.illustration(s, name, x, y, w, h, **kw)
