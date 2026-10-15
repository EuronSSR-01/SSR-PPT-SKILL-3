#!/usr/bin/env python3
"""SVG illustrations of objects and scenes (assets/illustrations/<style>/), recoloured to a deck's palette.

  illustrations.py styles                                styles and how many drawings each has
  illustrations.py list [--style flat]                   names and meanings (from the style's INDEX.md)
  illustrations.py export truck --primary 0B3D91 --accent E8590C --out build/truck.svg [--png-width 800]
  illustrations.py scene factory truck warehouse truck store --primary 0B3D91 --out build/chain.svg
  illustrations.py sheet --style flat --out build/sheet.png [--primary ... --accent ...]
  illustrations.py check assets/illustrations/flat/forklift.svg build/my-drawing.svg

Each style is a folder of SVG files plus INDEX.md. The bundled styles are samples, not the full range:
add drawings to a style, add a style folder, or draw project-specific SVGs and pass their file paths
(see assets/illustrations/README.md). Every drawing uses the same placeholder colours (TOKENS);
recolor() swaps them for a palette derived from a primary and an accent colour, so one drawing fits any
deck. White and the people colours in FIXED stay as drawn. Drawings carry no text, ids, gradients or
filters, so browsers, PyMuPDF (pptx_kit Deck.illustration / svg_picture) and LibreOffice render them the
same. Python standard library only; `sheet` and --png-width need PyMuPDF (and Pillow for `sheet`).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "assets" / "illustrations"
DEFAULT_STYLE = "flat"

# token -> placeholder colour used in the SVG files (also the default palette)
TOKENS = {
    "primary": "2F6FDE",
    "primary_dark": "1D4FAE",
    "primary_light": "D6E4FA",
    "accent": "F28C28",
    "accent_dark": "C86512",
    "accent_light": "FDE3C8",
    "ink": "22303F",
    "surface": "E8ECF1",
    "line": "C8D0DB",
    # plants and earth keep natural colours unless leaf= / soil= is given
    "leaf": "4E9F5D",
    "leaf_dark": "35754A",
    "leaf_light": "CFE8C9",
    "soil": "C49A6C",
    "soil_dark": "9C7148",
}
# colours that are never swapped: white, three skin tones, brown hair
FIXED = {"FFFFFF", "EFC3A0", "D9A47E", "A8714E", "5B3A29"}


def _rgb(hex_colour):
    h = hex_colour.lstrip("#")
    if not re.fullmatch(r"[0-9A-Fa-f]{6}", h):
        raise ValueError(f"not a hex colour: {hex_colour}")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _mix(a, b, t):
    """Blend colour a toward b by t (0 = a, 1 = b)."""
    ra, rb = _rgb(a), _rgb(b)
    return "".join(f"{round(x + (y - x) * t):02X}" for x, y in zip(ra, rb))


def palette(primary=None, accent=None, ink=None, surface=None, line=None, leaf=None, soil=None, extra=None):
    """Full palette from a primary and an accent colour (hex, with or without #). Darker and lighter
    tones are derived; ink, surface and line can be set separately (e.g. a warm grey deck), and so can
    the natural colours of plants (leaf) and earth or wood (soil). extra={"primary_light": "1A3346"}
    overrides any single token, e.g. darker "light" tones for a dark slide."""
    p = dict(TOKENS)
    if primary:
        p["primary"] = primary.lstrip("#").upper()
        p["primary_dark"] = _mix(p["primary"], "000000", 0.28)
        p["primary_light"] = _mix(p["primary"], "FFFFFF", 0.82)
    if accent:
        p["accent"] = accent.lstrip("#").upper()
        p["accent_dark"] = _mix(p["accent"], "000000", 0.22)
        p["accent_light"] = _mix(p["accent"], "FFFFFF", 0.78)
    if leaf:
        p["leaf"] = leaf.lstrip("#").upper()
        p["leaf_dark"] = _mix(p["leaf"], "000000", 0.28)
        p["leaf_light"] = _mix(p["leaf"], "FFFFFF", 0.75)
    if soil:
        p["soil"] = soil.lstrip("#").upper()
        p["soil_dark"] = _mix(p["soil"], "000000", 0.22)
    for key, value in (("ink", ink), ("surface", surface), ("line", line)):
        if value:
            p[key] = value.lstrip("#").upper()
    for key, value in (extra or {}).items():
        if key not in TOKENS:
            raise KeyError(f"unknown colour token {key!r}; tokens: {', '.join(TOKENS)}")
        p[key] = value.lstrip("#").upper()
    return p


def recolor(svg_text, colours=None, **kwargs):
    """Swap the placeholder colours for a palette: colours is a palette() dict, or pass primary=,
    accent=, ink=, surface=, line= directly."""
    pal = colours or palette(**kwargs)
    mapping = {TOKENS[k].upper(): pal[k] for k in TOKENS}
    return re.sub(r"#([0-9A-Fa-f]{6})\b", lambda m: "#" + mapping.get(m.group(1).upper(), m.group(1)), svg_text)


def styles():
    """Style folders that hold at least one drawing."""
    return sorted(p.name for p in ROOT.iterdir() if p.is_dir() and any(p.glob("*.svg")))


def names(style=None):
    folder = ROOT / (style or DEFAULT_STYLE)
    return sorted(p.stem for p in folder.glob("*.svg") if not p.stem.startswith("_"))


def path(name, style=None):
    """File of a drawing: a name in a style folder, or a path to any SVG file."""
    if str(name).lower().endswith(".svg"):
        p = Path(name)
        if not p.exists():
            raise FileNotFoundError(f"no SVG file {p}")
        return p
    style = style or DEFAULT_STYLE
    p = ROOT / style / f"{name}.svg"
    if not p.exists():
        raise FileNotFoundError(f"no illustration '{name}' in style '{style}'; see {ROOT / style / 'INDEX.md'} "
                                f"or run: illustrations.py list --style {style}")
    return p


def load(name, colours=None, style=None, **kwargs):
    """SVG text of one illustration, recoloured (no colour arguments: the default palette)."""
    return recolor(path(name, style).read_text(encoding="utf-8"), colours, **kwargs)


def _parts(svg_text):
    root = re.search(r"<svg\b[^>]*>", svg_text, flags=re.S)
    tag = root.group(0) if root else ""
    view = re.search(r'viewBox="([-\d.\s,]+)"', tag)
    x, y, w, h = (float(v) for v in re.split(r"[\s,]+", view.group(1).strip())) if view else (0, 0, 320, 240)
    scale = re.search(r'data-scale="([\d.]+)"', tag)
    inner = svg_text[root.end():] if root else svg_text
    inner = re.sub(r"</svg>\s*$", "", inner.strip(), flags=re.S)
    return (x, y, w, h), (float(scale.group(1)) if scale else 1.0), inner


def scene(items, width=1280, height=320, ground=True, gap=0, colours=None, style=None, **kwargs):
    """Lay drawings side by side on one ground line, e.g. scene(["factory", "truck", "warehouse"]).
    items: names or SVG paths ("truck", or "truck:0.8" to set the size), or (name, scale) pairs. Without
    a size, each drawing's data-scale (buildings = 1, a truck 0.62, a person 0.62) keeps the proportions.
    Returns SVG text."""
    def parse(item):
        if not isinstance(item, str):
            return item[0], float(item[1])
        name, _, size = item.rpartition(":") if re.search(r":[\d.]+$", item) else (item, "", "")
        return name, float(size) if size else None
    items = [parse(i) for i in items]
    base_h = height * 0.86
    parts, cursor = [], 0.0
    for name, scale in items:
        (vx, vy, vw, vh), own, inner = _parts(load(name, colours, style, **kwargs))
        s = base_h / vh * (own if scale is None else scale)
        y = height - vh * s - height * 0.04
        parts.append(f'<g transform="translate({cursor - vx * s:.1f} {y - vy * s:.1f}) scale({s:.4f})">{inner}</g>')
        cursor += vw * s + gap
    total = cursor - gap
    pal = colours or palette(**kwargs)
    road = (f'<rect x="0" y="{height * 0.955:.1f}" width="{total:.1f}" height="{height * 0.03:.1f}" rx="4" '
            f'fill="#{pal["line"]}"/>') if ground else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total:.1f} {height}">{road}'
            + "".join(parts) + "</svg>")


def check(svg_file):
    """Problems that stop a drawing from recolouring or rendering the same everywhere ([] = fine)."""
    text = Path(svg_file).read_text(encoding="utf-8")
    problems = []
    root = re.search(r"<svg\b[^>]*>", text)
    if not root:
        return ["no <svg> element"]
    if 'xmlns="http://www.w3.org/2000/svg"' not in root.group(0):
        problems.append('root <svg> needs xmlns="http://www.w3.org/2000/svg"')
    if "viewBox=" not in root.group(0):
        problems.append("root <svg> needs a viewBox (objects use 0 0 320 240)")
    for tag, why in (("text", "text: put words on the slide as native text"),
                     ("image", "embedded image: draw with shapes"),
                     ("filter", "filter: PyMuPDF and LibreOffice ignore it"),
                     ("linearGradient", "gradient: use flat tones (light/dark tokens)"),
                     ("radialGradient", "gradient: use flat tones (light/dark tokens)"),
                     ("mask", "mask: renderers differ"), ("clipPath", "clipPath: renderers differ"),
                     ("style", "<style>: put fill/stroke on each element"), ("use", "<use>: copy the shape")):
        if re.search(rf"<{tag}\b", text):
            problems.append(f"<{tag}> found ({why})")
    if re.search(r"\s(id|class)=", text):
        problems.append("id/class attributes found (drawings are pasted into scenes; ids would clash)")
    if re.search(r"url\(|rgba?\(|hsla?\(", text):
        problems.append("url()/rgb()/hsl() colour found: use #RRGGBB placeholders")
    named = re.findall(r'(?:fill|stroke)="(?!none|#)([^"]+)"', text)
    if named:
        problems.append(f"named colours {sorted(set(named))}: use #RRGGBB placeholders")
    short = re.findall(r"#[0-9A-Fa-f]{3}\b", text)
    if short:
        problems.append(f"3-digit colours {sorted(set(short))}: write all six digits")
    allowed = {v.upper() for v in TOKENS.values()} | FIXED
    stray = sorted({c.upper() for c in re.findall(r"#([0-9A-Fa-f]{6})\b", text)} - allowed)
    if stray:
        problems.append(f"colours outside the placeholders {stray}: they would not follow the deck palette")
    return problems


def render_png(svg_text, out, width_px):
    """Rasterise SVG text to a PNG of the given width (PyMuPDF)."""
    try:
        import pymupdf as fitz
    except ImportError:
        import fitz
    doc = fitz.open(stream=svg_text.encode("utf-8"), filetype="svg")
    page = doc[0]
    zoom = width_px / page.rect.width
    page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=True).save(str(out))
    doc.close()
    return Path(out)


def sheet(out, colours=None, columns=4, cell=360, style=None, files=None, **kwargs):
    """Contact sheet of a style's drawings (or of the given SVG files) with their names."""
    from io import BytesIO
    from PIL import Image, ImageDraw
    try:
        import pymupdf as fitz
    except ImportError:
        import fitz
    items = [(Path(f).stem, Path(f)) for f in files] if files else [(n, path(n, style)) for n in names(style)]
    rows = (len(items) + columns - 1) // columns
    pad, label = 16, 28
    img = Image.new("RGB", (columns * cell, max(1, rows) * (int(cell * 0.75) + label)), "white")
    draw = ImageDraw.Draw(img)
    for i, (name, file) in enumerate(items):
        svg = recolor(file.read_text(encoding="utf-8"), colours, **kwargs)
        doc = fitz.open(stream=svg.encode("utf-8"), filetype="svg")
        page = doc[0]
        zoom = (cell - 2 * pad) / page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=True)
        tile = Image.open(BytesIO(pix.tobytes("png"))).convert("RGBA")
        doc.close()
        cx, cy = (i % columns) * cell, (i // columns) * (int(cell * 0.75) + label)
        img.paste(tile, (cx + pad, cy + pad), tile)
        draw.text((cx + pad, cy + int(cell * 0.75) + 4), name, fill="#444444")
    img.save(out)
    return Path(out)


def _index(style):
    meanings = {}
    index = ROOT / style / "INDEX.md"
    if index.exists():
        for line in index.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\|\s*`([\w-]+)`\s*\|\s*([^|]+)\|", line)
            if m:
                meanings[m.group(1)] = m.group(2).strip()
    return meanings


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["styles", "list", "export", "scene", "sheet", "check"])
    ap.add_argument("names", nargs="*", help="drawing names or SVG file paths")
    ap.add_argument("--style", default=DEFAULT_STYLE, help=f"style folder (default {DEFAULT_STYLE})")
    ap.add_argument("--primary")
    ap.add_argument("--accent")
    ap.add_argument("--ink")
    ap.add_argument("--surface")
    ap.add_argument("--line")
    ap.add_argument("--leaf", help="plant colour (default a natural green)")
    ap.add_argument("--soil", help="earth and wood colour (default a natural brown)")
    ap.add_argument("--out")
    ap.add_argument("--png-width", type=int, help="also write a PNG of this width next to --out")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    colours = palette(args.primary, args.accent, args.ink, args.surface, args.line, args.leaf, args.soil)
    if args.command == "styles":
        for s in styles():
            print(f"{s:<12} {len(names(s))} drawings   {ROOT / s}")
        return
    if args.command == "list":
        meanings = _index(args.style)
        for n in names(args.style):
            print(f"{n:<18} {meanings.get(n, '')}")
        return
    if args.command == "check":
        files = [Path(n) if n.lower().endswith(".svg") else path(n, args.style) for n in args.names] \
            or [path(n, args.style) for n in names(args.style)]
        failed = 0
        for f in files:
            problems = check(f)
            failed += bool(problems)
            print(f"{'ok  ' if not problems else 'FAIL'} {f}")
            for p in problems:
                print(f"     - {p}")
        sys.exit(1 if failed else 0)
    if args.command == "sheet":
        files = [n for n in args.names if n.lower().endswith(".svg")] or None
        print(sheet(args.out or "illustrations.png", colours, style=args.style, files=files))
        return
    if not args.names:
        ap.error("name the illustration(s)")
    if args.command == "export":
        svg = load(args.names[0], colours, args.style)
    else:
        svg = scene(args.names, colours=colours, style=args.style)
    if args.out:
        Path(args.out).write_text(svg, encoding="utf-8")
        print(args.out)
        if args.png_width:
            print(render_png(svg, Path(args.out).with_suffix(".png"), args.png_width))
    else:
        print(svg)


if __name__ == "__main__":
    main()
