#!/usr/bin/env python3
"""Photo treatments and generated backgrounds for slides (Pillow). PPTX cannot apply CSS filters, so treat
pictures before inserting them; HTML can use the same files or CSS.

  image_fx.py gray in.jpg out.jpg [--contrast 1.3]           black and white, optional contrast
  image_fx.py duotone in.jpg out.jpg --dark 1B2A4A --light F2E9D8
  image_fx.py grade in.jpg out.jpg --saturation 0.7 --warmth 0.08 [--brightness 1.0]
  image_fx.py darken in.jpg out.jpg --amount 0.45            darker copy to put text on
  image_fx.py round in.jpg out.png --radius 40 [--size 1200x800]   rounded corners (transparent PNG)
  image_fx.py circle in.jpg out.png [--size 800]             round crop for portraits
  image_fx.py grain out.png --size 1280x720 --amount 0.06    transparent noise to lay over a slide
  image_fx.py glow out.png --size 1280x720 --colors FF7A45,FFC145 --bg 07080C
  image_fx.py dots out.png --size 1280x720 --bg FBF8F1 --dot C9C2B4 --gap 24
  image_fx.py halftone out.png --size 1280x720 --colors 0078BF --gap 14       dots that grow across the slide

Keep the treatment the same across a deck (one grade for every photo). Check the result by eye: duotone and
heavy grades can hide the subject; text needs enough contrast on the treated picture.
"""
import argparse
import random
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps


def _rgb(hex_colour):
    h = hex_colour.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _open(src, size=None):
    img = Image.open(src).convert("RGB")
    if size:
        img = ImageOps.fit(img, size, Image.LANCZOS)
    return img


def gray(src, out, contrast=1.0):
    img = ImageOps.grayscale(_open(src))
    if contrast != 1:
        img = ImageEnhance.Contrast(img).enhance(contrast)
    img.convert("RGB").save(out, quality=90)
    return Path(out)


def duotone(src, out, dark="1B2A4A", light="F2E9D8"):
    img = ImageOps.grayscale(_open(src))
    ImageOps.colorize(img, _rgb(dark), _rgb(light)).save(out, quality=90)
    return Path(out)


def grade(src, out, saturation=1.0, warmth=0.0, brightness=1.0, contrast=1.0):
    """Shared colour grade: saturation < 1 calms busy photos; warmth > 0 warms, < 0 cools."""
    img = _open(src)
    img = ImageEnhance.Color(img).enhance(saturation)
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    if warmth:
        r, g, b = img.split()
        r = r.point(lambda v: min(255, v * (1 + warmth)))
        b = b.point(lambda v: v * (1 - warmth))
        img = Image.merge("RGB", (r, g, b))
    img.save(out, quality=90)
    return Path(out)


def darken(src, out, amount=0.45, colour="000000"):
    img = _open(src)
    Image.blend(img, Image.new("RGB", img.size, _rgb(colour)), amount).save(out, quality=90)
    return Path(out)


def round_corners(src, out, radius=40, size=None):
    img = _open(src, size).convert("RGBA")
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img.width - 1, img.height - 1), radius=radius, fill=255)
    img.putalpha(mask)
    img.save(out)
    return Path(out)


def circle(src, out, size=800):
    img = _open(src, (size, size)).convert("RGBA")
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    img.putalpha(mask)
    img.save(out)
    return Path(out)


def grain(out, size=(1280, 720), amount=0.06, seed=7):
    """Transparent PNG of fine noise; lay it over the whole slide to break up flat colour and banding."""
    rnd = random.Random(seed)
    w, h = size
    noise = Image.new("L", (w // 2, h // 2))
    noise.putdata([rnd.randint(0, 255) for _ in range((w // 2) * (h // 2))])
    noise = noise.resize(size, Image.NEAREST)
    alpha = noise.point(lambda v: int(abs(v - 128) * 2 * amount))
    tone = noise.point(lambda v: 255 if v > 128 else 0)
    img = Image.merge("RGBA", (tone, tone, tone, alpha))
    img.save(out)
    return Path(out)


def glow(out, size=(1280, 720), colors=("FF7A45", "FFC145"), bg="07080C", spots=None, blur=None, strength=0.55):
    """Dark background with soft coloured light (for launch and tech looks); text stays native on top."""
    w, h = size
    img = Image.new("RGB", size, _rgb(bg))
    layer = Image.new("RGB", size, (0, 0, 0))
    draw = ImageDraw.Draw(layer)
    spots = spots or [(0.72, 0.38, 0.36), (0.86, 0.72, 0.28)]
    for i, (fx, fy, fr) in enumerate(spots):
        c = _rgb(colors[i % len(colors)])
        r = fr * w
        draw.ellipse((fx * w - r, fy * h - r, fx * w + r, fy * h + r), fill=c)
    layer = layer.filter(ImageFilter.GaussianBlur(blur or w * 0.09))
    img = ImageChops.add(img, ImageEnhance.Brightness(layer).enhance(strength))
    img.save(out)
    return Path(out)


def dots(out, size=(1280, 720), bg="FBF8F1", dot="C9C2B4", gap=24, radius=1.6):
    """Dot-grid paper (notebook looks)."""
    scale = 2
    w, h = size[0] * scale, size[1] * scale
    img = Image.new("RGB", (w, h), _rgb(bg))
    draw = ImageDraw.Draw(img)
    r = radius * scale
    for y in range(gap * scale // 2, h, gap * scale):
        for x in range(gap * scale // 2, w, gap * scale):
            draw.ellipse((x - r, y - r, x + r, y + r), fill=_rgb(dot))
    img.resize(size, Image.LANCZOS).save(out)
    return Path(out)


def halftone(out, size=(1280, 720), colour="0078BF", gap=14, max_r=5.5, angle_fade="x"):
    """Transparent halftone dots that grow across the slide (print and riso looks)."""
    w, h = size
    img = Image.new("RGBA", (w * 2, h * 2), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    c = _rgb(colour) + (255,)
    for y in range(0, h * 2, gap * 2):
        for x in range(0, w * 2, gap * 2):
            t = x / (w * 2) if angle_fade == "x" else y / (h * 2)
            r = max_r * 2 * t
            if r > 0.6:
                draw.ellipse((x - r, y - r, x + r, y + r), fill=c)
    img.resize(size, Image.LANCZOS).save(out)
    return Path(out)


def _size(text):
    if not text:
        return None
    w, _, h = text.lower().partition("x")
    return (int(w), int(h or w))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=["gray", "duotone", "grade", "darken", "round", "circle", "grain", "glow", "dots", "halftone"])
    ap.add_argument("paths", nargs="+", help="input and output (generated backgrounds take only the output)")
    ap.add_argument("--contrast", type=float, default=1.0)
    ap.add_argument("--dark", default="1B2A4A")
    ap.add_argument("--light", default="F2E9D8")
    ap.add_argument("--saturation", type=float, default=1.0)
    ap.add_argument("--warmth", type=float, default=0.0)
    ap.add_argument("--brightness", type=float, default=1.0)
    ap.add_argument("--amount", type=float)
    ap.add_argument("--radius", type=int, default=40)
    ap.add_argument("--size")
    ap.add_argument("--colors", default="FF7A45,FFC145")
    ap.add_argument("--bg")
    ap.add_argument("--dot", default="C9C2B4")
    ap.add_argument("--gap", type=int, help="dot spacing (dots 24, halftone 14)")
    a = ap.parse_args()
    p = a.paths
    if a.command == "gray":
        print(gray(p[0], p[1], a.contrast))
    elif a.command == "duotone":
        print(duotone(p[0], p[1], a.dark, a.light))
    elif a.command == "grade":
        print(grade(p[0], p[1], a.saturation, a.warmth, a.brightness, a.contrast))
    elif a.command == "darken":
        print(darken(p[0], p[1], a.amount if a.amount is not None else 0.45))
    elif a.command == "round":
        print(round_corners(p[0], p[1], a.radius, _size(a.size)))
    elif a.command == "circle":
        print(circle(p[0], p[1], (_size(a.size) or (800, 800))[0]))
    elif a.command == "grain":
        print(grain(p[0], _size(a.size) or (1280, 720), a.amount if a.amount is not None else 0.06))
    elif a.command == "glow":
        print(glow(p[0], _size(a.size) or (1280, 720), a.colors.split(","), a.bg or "07080C"))
    elif a.command == "dots":
        print(dots(p[0], _size(a.size) or (1280, 720), a.bg or "FBF8F1", a.dot, a.gap or 24))
    elif a.command == "halftone":
        print(halftone(p[0], _size(a.size) or (1280, 720), a.colors.split(",")[0], a.gap or 14))


if __name__ == "__main__":
    main()
