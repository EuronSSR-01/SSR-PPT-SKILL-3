#!/usr/bin/env python3
"""Search openly licensed photos, look at the candidates, download one and record its source.

  find_images.py search "warehouse forklift" --sheet build/img/candidates.png
  find_images.py search "rice field" --license cc0,pdm --orientation landscape --min-width 1600
  find_images.py get 3 --out build/img/warehouse.jpg --record sources.md --page 4

search  asks Openverse (openly licensed images from Flickr, Wikimedia and others) and Wikimedia Commons,
        keeps results whose licence allows commercial use and editing (by default CC0, public domain,
        CC BY, CC BY-SA), saves them to a candidates JSON and, with --sheet, draws a numbered contact sheet
        of thumbnails. Look at the sheet before choosing: titles and tags often do not match the picture.
get     downloads the chosen candidate (number from the sheet, or its id), prints the attribution and,
        with --record, appends a line to sources.md (title, author, licence, source page, file, page).
        Open the downloaded file and check subject, sharpness, watermarks and text before using it.

Licences: CC0 / public domain need no credit; CC BY needs credit (author, licence, link) on the slide or
in the notes; CC BY-SA also asks that edited versions keep the same licence. NC (non-commercial) and ND
(no derivatives) are left out by default because company decks are commercial and get cropped.
Python standard library only; --sheet needs Pillow. Needs network access.
"""
import argparse
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

UA = "ssr-ppt-skill/3 (presentation image search; https://github.com/EuronSSR-01/SSR-PPT-SKILL-3)"
OPENVERSE = "https://api.openverse.org/v1/images/"
COMMONS = "https://commons.wikimedia.org/w/api.php"
DEFAULT_LICENSES = "cc0,pdm,by,by-sa"
LICENSE_NAMES = {"cc0": "CC0", "pdm": "Public Domain", "by": "CC BY", "by-sa": "CC BY-SA", "by-nc": "CC BY-NC",
                 "by-nd": "CC BY-ND", "by-nc-sa": "CC BY-NC-SA", "by-nc-nd": "CC BY-NC-ND"}


def fetch(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def fetch_json(url):
    return json.loads(fetch(url).decode("utf-8"))


def plain(text):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", text or ""))).strip()


def commons_license(short):
    """Map a Commons LicenseShortName to the Openverse-style code."""
    s = (short or "").lower().replace("-", " ")
    if "cc0" in s:
        return "cc0"
    if "public domain" in s or s.startswith("pd") or "no restrictions" in s:
        return "pdm"
    m = re.search(r"cc (by(?: nc)?(?: nd)?(?: sa)?)", s)
    return m.group(1).replace(" ", "-") if m else "other"


def orientation_ok(w, h, orientation):
    if not w or not h or orientation == "any":
        return True
    r = w / h
    return {"landscape": r >= 1.2, "portrait": r <= 0.85, "square": 0.85 < r < 1.2}[orientation]


def search_openverse(query, licenses, n):
    params = {"q": query, "license": licenses, "page_size": min(20, max(n, 1)), "mature": "false"}
    data = fetch_json(OPENVERSE + "?" + urllib.parse.urlencode(params))
    out = []
    for r in data.get("results", []):
        out.append({"id": f"ov:{r['id']}", "title": plain(r.get("title")) or "(untitled)",
                    "creator": plain(r.get("creator")) or "unknown", "license": r.get("license", ""),
                    "license_version": r.get("license_version") or "", "license_url": r.get("license_url") or "",
                    "page": r.get("foreign_landing_url") or "", "url": r.get("url") or "",
                    "thumb": r.get("thumbnail") or r.get("url") or "", "width": r.get("width") or 0,
                    "height": r.get("height") or 0, "provider": f"Openverse/{r.get('source', '')}"})
    return out


def search_commons(query, licenses, n):
    params = {"action": "query", "format": "json", "generator": "search", "gsrnamespace": 6,
              "gsrsearch": f"{query} filetype:bitmap", "gsrlimit": min(40, max(n * 2, 10)),
              "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": 400}
    data = fetch_json(COMMONS + "?" + urllib.parse.urlencode(params))
    pages = sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    wanted = set(licenses.split(","))
    out = []
    for p in pages:
        info = (p.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata", {})
        short = meta.get("LicenseShortName", {}).get("value", "")
        code = commons_license(short)
        if code not in wanted:
            continue
        version = (re.search(r"(\d\.\d)", short) or [None, ""])[1]
        out.append({"id": f"wc:{p['pageid']}", "title": p.get("title", "").replace("File:", ""),
                    "creator": plain(meta.get("Artist", {}).get("value")) or "unknown", "license": code,
                    "license_version": version, "license_url": meta.get("LicenseUrl", {}).get("value", ""),
                    "page": info.get("descriptionurl", ""), "url": info.get("url", ""),
                    "thumb": info.get("thumburl", ""), "width": info.get("width", 0), "height": info.get("height", 0),
                    "provider": "Wikimedia Commons"})
    return out


def attribution(c):
    name = LICENSE_NAMES.get(c["license"], c["license"].upper())
    lic = f"{name} {c['license_version']}".strip()
    if c["license"] in ("cc0", "pdm"):
        return f"“{c['title']}”, {c['creator']}, {lic}（无需署名）"
    return f"“{c['title']}” by {c['creator']}, {lic}, {c['page']}"


def contact_sheet(cands, out, cols=4, cell=320):
    from io import BytesIO
    from PIL import Image, ImageDraw
    rows = (len(cands) + cols - 1) // cols
    label = 40
    sheet = Image.new("RGB", (cols * cell, max(1, rows) * (cell * 3 // 4 + label)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, c in enumerate(cands):
        x, y = (i % cols) * cell, (i // cols) * (cell * 3 // 4 + label)
        try:
            img = Image.open(BytesIO(fetch(c["thumb"], timeout=30))).convert("RGB")
            img.thumbnail((cell - 8, cell * 3 // 4 - 8))
            sheet.paste(img, (x + (cell - img.width) // 2, y + 4))
        except Exception as exc:  # a missing thumbnail should not stop the sheet
            draw.text((x + 8, y + 8), f"no preview: {exc.__class__.__name__}", fill="#999999")
        lic = LICENSE_NAMES.get(c["license"], c["license"])
        draw.text((x + 6, y + cell * 3 // 4 + 4), f"{i + 1}. {lic}  {c['width']}x{c['height']}", fill="#222222")
        draw.text((x + 6, y + cell * 3 // 4 + 20), c["title"][:44], fill="#666666")
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out)
    return Path(out)


def cmd_search(args):
    cands, notes = [], []
    sources = [s.strip() for s in args.source.split(",")]
    for src, fn in (("openverse", search_openverse), ("commons", search_commons)):
        if src not in sources:
            continue
        try:
            cands += fn(args.query, args.license, args.n)
        except Exception as exc:
            notes.append(f"{src}: {exc}")
    cands = [c for c in cands if c["url"] and (c["width"] or 0) >= args.min_width
             and orientation_ok(c["width"], c["height"], args.orientation)][:args.n]
    store = Path(args.json)
    store.parent.mkdir(parents=True, exist_ok=True)
    store.write_text(json.dumps({"query": args.query, "candidates": cands}, ensure_ascii=False, indent=1), encoding="utf-8")
    for i, c in enumerate(cands, 1):
        print(f"{i:>2}. [{LICENSE_NAMES.get(c['license'], c['license'])} {c['license_version']}] {c['width']}x{c['height']} "
              f"{c['title'][:60]} — {c['creator'][:30]}  ({c['provider']})")
    for n in notes:
        print(f"note: {n}", file=sys.stderr)
    if not cands:
        print("no candidates: try other words (English often finds more), a wider --license or a lower --min-width")
    print(f"saved {len(cands)} candidates to {store}")
    if args.sheet and cands:
        print(f"contact sheet: {contact_sheet(cands, args.sheet)}  (look at it before choosing)")


def cmd_get(args):
    data = json.loads(Path(args.json).read_text(encoding="utf-8"))
    cands = data["candidates"]
    pick = next((c for c in cands if c["id"] == args.which), None)
    if pick is None and args.which.isdigit() and 1 <= int(args.which) <= len(cands):
        pick = cands[int(args.which) - 1]
    if pick is None:
        sys.exit(f"no candidate {args.which!r} in {args.json}")
    url = pick["url"]
    if args.max_width and pick["provider"] == "Wikimedia Commons" and pick["width"] > args.max_width:
        info = fetch_json(COMMONS + "?" + urllib.parse.urlencode({"action": "query", "format": "json",
                          "pageids": pick["id"][3:], "prop": "imageinfo", "iiprop": "url", "iiurlwidth": args.max_width}))
        url = next(iter(info["query"]["pages"].values()))["imageinfo"][0].get("thumburl") or url
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(fetch(url, timeout=120))
    credit = attribution(pick)
    print(f"saved {out}\nattribution: {credit}")
    if args.record:
        line = (f"- 图片 {out.name}｜第 {args.page or '?'} 页｜{credit}｜来源页 {pick['page']}｜"
                f"许可 {pick['license_url'] or LICENSE_NAMES.get(pick['license'], pick['license'])}\n")
        with open(args.record, "a", encoding="utf-8") as f:
            f.write(line)
        print(f"recorded in {args.record}")
    if pick["license"] not in ("cc0", "pdm"):
        print("credit needed: put the attribution on the slide (small) or in its notes")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="command", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--source", default="openverse,commons", help="openverse, commons or both (default)")
    s.add_argument("--license", default=DEFAULT_LICENSES, help=f"comma list (default {DEFAULT_LICENSES})")
    s.add_argument("--orientation", default="any", choices=["any", "landscape", "portrait", "square"])
    s.add_argument("--min-width", type=int, default=1000)
    s.add_argument("-n", type=int, default=12)
    s.add_argument("--json", default="image-candidates.json")
    s.add_argument("--sheet", help="PNG contact sheet of the candidates")
    g = sub.add_parser("get")
    g.add_argument("which", help="number from the search output, or a candidate id")
    g.add_argument("--json", default="image-candidates.json")
    g.add_argument("--out", required=True)
    g.add_argument("--max-width", type=int, default=2400, help="download a resized copy from Commons (default 2400)")
    g.add_argument("--record", help="sources.md to append the attribution to")
    g.add_argument("--page", help="slide number for the record")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    {"search": cmd_search, "get": cmd_get}[args.command](args)


if __name__ == "__main__":
    main()
