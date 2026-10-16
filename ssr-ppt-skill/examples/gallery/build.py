#!/usr/bin/env python3
"""Rebuild the design-example gallery (assets/gallery/*.png and manifest.json).

  python examples/gallery/build.py --out build/gallery --fonts path/to/fonts            # everything
  python examples/gallery/build.py --out build/gallery --fonts fonts --section layouts --only L05-a L05-b

Needs python-pptx, PyMuPDF, Pillow and LibreOffice. Photos listed in photos.json are downloaded on first
use. --fonts is a folder with the font files the examples use (see README.md); on Windows they are added
for this session only while LibreOffice renders, elsewhere install them first. Full-size renders for
checking go to <out>/review/<section>/.
"""
import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import gallery  # noqa: E402

MODULES = ["layouts_1", "layouts_2", "layouts_3", "convert_examples", "recipes_1", "recipes_2", "recipes_3",
           "type_specimens", "imagery_examples"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="build/gallery")
    ap.add_argument("--fonts", help="folder of font files used by the examples")
    ap.add_argument("--section", nargs="*", default=list(gallery.SECTIONS))
    ap.add_argument("--only", nargs="*", help="example ids to rebuild")
    ap.add_argument("--assets", default=str(gallery.SKILL / "assets" / "gallery"))
    ap.add_argument("--width", type=int, default=960, help="width of the PNGs kept in the skill (default 960)")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for name in MODULES:
        if (HERE / f"{name}.py").exists():
            __import__(name)
    manifest = gallery.build(args.section, args.out, args.assets, args.fonts, args.width, args.only)
    print(f"{len(manifest)} examples in {Path(args.assets) / 'manifest.json'}")
    docs = sorted((gallery.SKILL / "references").glob("*.md")) + [gallery.SKILL / "assets" / "illustrations" / "README.md"]
    for line in gallery.relink(manifest, docs):
        print(f"missing example: {line}")
    print(gallery.write_html(manifest, gallery.SKILL / "assets" / "design-examples.html"))


if __name__ == "__main__":
    main()
