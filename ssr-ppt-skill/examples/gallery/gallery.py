"""Core of the design-example gallery: register examples, build decks with pptx_kit, render, export PNGs.

Each example is a function that draws one slide:

    @example("layouts", "L05-a", "大数字页 A：数字压左，解读在右", fonts=("Noto Sans SC",))
    def big_number_left(deck, s):
        ...

build.py imports the example modules, then calls build(). The PNGs go to assets/gallery/<section>/<id>.png
(and a manifest.json that assets/design-examples.html reads); full-size renders for checking go to the
build folder. All content is fictional.
"""
import ctypes
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from contextlib import contextmanager
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent.parent
sys.path.insert(0, str(SKILL / "scripts"))
from pptx_kit import Deck, rgb  # noqa: E402

REGISTRY = []
SECTIONS = ("layouts", "convert", "recipes", "type", "imagery")


def example(section, id, title, note="", fonts=()):
    """Register a one-slide example. title: shown under the image; note: what to notice."""
    def wrap(fn):
        REGISTRY.append({"section": section, "id": id, "title": title, "note": note, "fn": fn,
                         "fonts": list(fonts), "source": f"examples/gallery/{Path(fn.__code__.co_filename).name}"})
        return fn
    return wrap


def bg(slide, colour):
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = rgb(colour)


# ------------------------------------------------------------------ photos (downloaded on first use)
PHOTOS = json.loads((HERE / "photos.json").read_text(encoding="utf-8"))
CACHE = Path(os.environ.get("SSR_GALLERY_CACHE", Path(tempfile.gettempdir()) / "ssr-gallery-cache"))


def photo(key, max_width=1920):
    """Local copy of a photo listed in photos.json (licence and author are recorded there)."""
    out = CACHE / "photos" / f"{key}.jpg"
    if not out.exists():
        out.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(PHOTOS[key]["url"], headers={"User-Agent": "ssr-ppt-skill gallery build"})
        with urllib.request.urlopen(req, timeout=120) as resp:
            out.write_bytes(resp.read())
        from PIL import Image
        img = Image.open(out).convert("RGB")
        if img.width > max_width:
            img = img.resize((max_width, round(img.height * max_width / img.width)), Image.LANCZOS)
        img.save(out, quality=90)
    return out


def crop(key, box, name=None):
    """Crop a photo to (left, top, right, bottom) fractions, e.g. to cut away a price sign."""
    from PIL import Image
    src = photo(key)
    out = CACHE / "photos" / f"{name or key}-crop-{'-'.join(f'{v:.2f}' for v in box)}.jpg"
    if not out.exists():
        img = Image.open(src)
        w, h = img.size
        img.crop((round(box[0] * w), round(box[1] * h), round(box[2] * w), round(box[3] * h))).save(out, quality=90)
    return out


def scratch(name):
    """Path for an intermediate file (illustration PNG, background texture)."""
    out = CACHE / "work" / name
    out.parent.mkdir(parents=True, exist_ok=True)
    return out


def _fx():
    import importlib.util
    spec = importlib.util.spec_from_file_location("image_fx", SKILL / "scripts" / "image_fx.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


FX = _fx()


def _tag(kw):
    return "-".join(f"{k}{v}" for k, v in sorted(kw.items())).replace(",", "_").replace(" ", "")[:80]


def treated(key, fn, ext="jpg", source=None, **kw):
    """A photo from photos.json run through scripts/image_fx.py, e.g. treated("farm", "gray", contrast=1.3)."""
    out = scratch(f"{key}-{fn}-{_tag(kw)}.{ext}")
    if not out.exists():
        getattr(FX, fn)(source or photo(key), out, **kw)
    return out


def generated(fn, **kw):
    """A generated background from scripts/image_fx.py, e.g. generated("glow", colors=("FF7A45", "FFC145"))."""
    out = scratch(f"{fn}-{_tag(kw)}.png")
    if not out.exists():
        getattr(FX, fn)(out, **kw)
    return out


# ------------------------------------------------------------------ fonts for rendering
@contextmanager
def session_fonts(folder):
    """Make the font files in folder available to LibreOffice while rendering. Windows: added to this logon
    session with AddFontResource and removed afterwards (nothing is installed). Elsewhere install them."""
    added = []
    files = [p for p in Path(folder).rglob("*") if p.suffix.lower() in (".ttf", ".otf") and "__MACOSX" not in str(p)] \
        if folder else []
    if files and os.name == "nt":
        gdi = ctypes.windll.gdi32
        added = [str(f) for f in files if gdi.AddFontResourceW(str(f))]
        print(f"fonts: {len(added)} files added for this session")
    elif files:
        print("fonts: install the files in --fonts (or copy them to ~/.local/share/fonts) before rendering")
    try:
        yield
    finally:
        for f in added:
            ctypes.windll.gdi32.RemoveFontResourceW(f)


def soffice():
    for name in ("soffice.com", "soffice"):
        found = shutil.which(name)
        if found:
            return found
    for cand in (r"C:\Program Files\LibreOffice\program\soffice.com", "/usr/bin/soffice",
                 "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
        if Path(cand).exists():
            return cand
    sys.exit("LibreOffice (soffice) is needed to render the gallery")


def to_pdf(pptx, out_dir):
    with tempfile.TemporaryDirectory() as tmp:
        profile = Path(tmp, "profile").resolve().as_uri()
        subprocess.run([soffice(), f"-env:UserInstallation={profile}", "--headless", "--norestore",
                        "--convert-to", "pdf", "--outdir", str(out_dir), str(pptx)],
                       check=True, capture_output=True, timeout=900)
    return Path(out_dir) / (Path(pptx).stem + ".pdf")


def small_image(src, stem, width):
    """Downscaled copy for the skill folder, whichever is smaller: a 128-colour PNG (flat pages, crisp text)
    or a JPEG (pages with photos). stem is the path without extension; returns the file written."""
    import io
    from PIL import Image
    img = Image.open(src).convert("RGB")
    img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    png, jpg = io.BytesIO(), io.BytesIO()
    img.quantize(colors=128, method=Image.Quantize.FASTOCTREE).save(png, format="PNG", optimize=True)
    img.save(jpg, format="JPEG", quality=85, optimize=True, progressive=True)
    ext, data = ("png", png) if png.tell() <= jpg.tell() * 1.1 else ("jpg", jpg)
    stem = Path(stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    for old in (stem.with_suffix(".png"), stem.with_suffix(".jpg")):
        if old.exists():
            old.unlink()
    out = stem.with_suffix("." + ext)
    out.write_bytes(data.getvalue())
    return out


def relink(manifest, docs):
    """Point links like assets/gallery/layouts/L05-a.png in the given Markdown files at the file the build
    kept (.png or .jpg); report links to examples that do not exist."""
    import re
    files = {(m["section"], m["id"]): m["file"] for m in manifest}
    missing = []
    for doc in docs:
        text = Path(doc).read_text(encoding="utf-8")

        def fix(match):
            key = (match.group(2), match.group(3))
            if key not in files:
                missing.append(f"{Path(doc).name}: {match.group(0)}")
                return match.group(0)
            return f"{match.group(1)}{files[key]}"
        new = re.sub(r"(assets/gallery/)(\w+)/([\w-]+)\.(?:png|jpg)", fix, text)
        if new != text:
            Path(doc).write_text(new, encoding="utf-8")
    return missing


SECTION_INFO = {
    "layouts": ("版式原型", "每个原型的几种排法。为了看清构图，每页只放了三五条信息；真实页面放多少由材料决定。说明见 references/layouts.md；代码见 examples/gallery/layouts_*.py。"),
    "convert": ("改写", "同一页的改写前（A）和改写后（B）：信息和它的限定一条不少，从文字改成图（插画、图标、时间条、点阵、流向、比例条、图表），文字只剩短标签。套在三个虚构机构的模板里（医院、学校、工厂），模板的配色和字体不变；每组 A、B 依据同一份编好的材料。C04 另有一页 C，把同样的数按多少排序，和按位置摆的 B 对照。说明见 references/imagery.md 的“把一页文字改成图”；代码见 examples/gallery/convert_examples.py。"),
    "recipes": ("风格配方", "每套配方用同一份内容做 a 封面、b 数据页、c 图片页，再加一页 d 特色页。说明见 references/style-recipes.md。"),
    "type": ("字体", "每款字体同一句标题、同一段正文、同一组数字；P 开头是搭配，N01 是数字对比。说明见 references/typography.md。"),
    "imagery": ("配图", "找图、照片处理、文字压图、裁切、插画换色、补画物体、图标。说明见 references/imagery.md。"),
}

HTML_PAGE = """<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>设计示例</title>
<style>
:root { --bg:#F3F4F6; --card:#FFFFFF; --ink:#1F2A37; --muted:#4F5866; --line:#DDE1E6; --accent:#2F5BD3; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#15171B; --card:#1E2127; --ink:#E9ECF0; --muted:#9AA3AE; --line:#2C3038; --accent:#FF8A4C; } }
:root[data-theme="dark"] { --bg:#15171B; --card:#1E2127; --ink:#E9ECF0; --muted:#9AA3AE; --line:#2C3038; --accent:#FF8A4C; }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font:15px/1.6 "Noto Sans SC","PingFang SC","Microsoft YaHei",sans-serif; }
header { padding:28px 16px 8px; max-width:1280px; margin:0 auto; }
h1 { font-size:28px; margin:0 0 6px; }
.lead { color:var(--muted); margin:0 0 14px; }
nav { position:sticky; top:0; z-index:5; background:var(--bg); border-bottom:1px solid var(--line); }
nav .in { max-width:1280px; margin:0 auto; padding:10px 16px; display:flex; gap:14px; flex-wrap:wrap; align-items:center; }
nav a { color:var(--ink); text-decoration:none; font-weight:600; }
nav a:hover { color:var(--accent); }
nav input { margin-left:auto; min-width:180px; flex:1 1 180px; max-width:320px; padding:6px 10px; border:1px solid var(--line); border-radius:8px; background:var(--card); color:var(--ink); }
main { max-width:1280px; margin:0 auto; padding:0 16px 60px; }
section h2 { font-size:22px; margin:34px 0 4px; }
section > p { color:var(--muted); margin:0 0 14px; }
.group { margin:0 0 22px; }
.group h3 { font-size:15px; margin:0 0 8px; }
.row { display:grid; grid-template-columns:repeat(auto-fill, minmax(260px, 1fr)); gap:12px; }
figure { margin:0; background:var(--card); border:1px solid var(--line); border-radius:10px; overflow:hidden; cursor:zoom-in; }
figure img { display:block; width:100%; aspect-ratio:16/9; object-fit:cover; background:var(--line); }
figcaption { padding:8px 10px 10px; font-size:13px; }
figcaption b { display:block; font-size:13px; }
figcaption span { color:var(--muted); }
.hidden { display:none !important; }
dialog { border:none; padding:0; max-width:min(1100px, 96vw); background:var(--card); color:var(--ink); border-radius:12px; }
dialog img { display:block; width:100%; height:auto; }
dialog .meta { padding:12px 16px 16px; }
dialog .meta code { color:var(--muted); font-size:12px; }
dialog::backdrop { background:rgba(0,0,0,.6); }
footer { color:var(--muted); font-size:13px; max-width:1280px; margin:0 auto; padding:0 16px 40px; }
</style>
</head>
<body>
<header>
<h1>设计示例</h1>
<p class="lead">SSR-PPT-SKILL 自带的成品示例：都是用 scripts/pptx_kit.py 做成的原生 PPTX，经 LibreOffice 渲染。内容都是虚构的：版式、配方、字体、配图用“知野生鲜社区店升级”，改写一节用三个虚构机构；照片来源见 examples/gallery/photos.json。这些是参考，不是模板：可以照做、改编、组合，也可以完全自定。</p>
</header>
<nav><div class="in">__NAV__<input id="q" type="search" placeholder="搜索编号或名称，如 L05、数据新闻" aria-label="搜索"></div></nav>
<main id="main"></main>
<footer>重新生成：python examples/gallery/build.py --fonts &lt;字体目录&gt;（见 examples/gallery/README.md）。</footer>
<dialog id="dlg"><img id="dimg" alt=""><div class="meta"><b id="dtitle"></b><div id="dnote"></div><code id="dsrc"></code></div></dialog>
<script>
const DATA = __DATA__;
const INFO = __INFO__;
const main = document.getElementById('main');
const groupKey = m => m.section === 'type' ? m.id[0] : m.id.split('-')[0];
const groupName = {T: '单款字体', P: '字体搭配', N: '数字字体'};
for (const [sec, [name, intro]] of Object.entries(INFO)) {
  const items = DATA.filter(m => m.section === sec);
  if (!items.length) continue;
  const s = document.createElement('section'); s.id = sec;
  s.innerHTML = `<h2>${name}</h2><p>${intro}</p>`;
  const groups = {};
  for (const m of items) (groups[groupKey(m)] ||= []).push(m);
  for (const [k, list] of Object.entries(groups)) {
    const g = document.createElement('div'); g.className = 'group';
    const label = sec === 'type' ? (groupName[k] || k) : (sec === 'recipes' ? list[0].title.split(' · ')[0] : `${k} ${list[0].title.split('：')[0].replace(/ [A-Z]$/, '')}`);
    g.innerHTML = `<h3>${label}</h3>`;
    const row = document.createElement('div'); row.className = 'row';
    for (const m of list) {
      const f = document.createElement('figure');
      f.dataset.search = `${m.id} ${m.title} ${m.note}`.toLowerCase();
      f.innerHTML = `<img loading="lazy" src="gallery/${m.file}" alt="${m.title}"><figcaption><b>${m.id}　${m.title}</b><span>${m.note}</span></figcaption>`;
      f.onclick = () => { dimg.src = `gallery/${m.file}`; dtitle.textContent = `${m.id}　${m.title}`; dnote.textContent = m.note; dsrc.textContent = `${m.source} · 字体：${m.fonts.join('、')}`; dlg.showModal(); };
      row.appendChild(f);
    }
    g.appendChild(row); s.appendChild(g);
  }
  main.appendChild(s);
}
dlg.onclick = () => dlg.close();
document.getElementById('q').oninput = e => {
  const q = e.target.value.trim().toLowerCase();
  document.querySelectorAll('figure').forEach(f => f.classList.toggle('hidden', q && !f.dataset.search.includes(q)));
  document.querySelectorAll('.group').forEach(g => g.classList.toggle('hidden', !g.querySelector('figure:not(.hidden)')));
};
</script>
</body>
</html>
"""


def write_html(manifest, path):
    """assets/design-examples.html: every example grouped by section, offline (images by relative path)."""
    nav = "".join(f'<a href="#{k}">{v[0]}</a>' for k, v in SECTION_INFO.items())
    page = (HTML_PAGE.replace("__NAV__", nav)
            .replace("__DATA__", json.dumps(manifest, ensure_ascii=False))
            .replace("__INFO__", json.dumps(SECTION_INFO, ensure_ascii=False)))
    Path(path).write_text(page, encoding="utf-8")
    return Path(path)


def build(sections, out_dir, assets_dir, fonts_dir=None, width=960, only=None):
    import pymupdf
    out_dir, assets_dir = Path(out_dir), Path(assets_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = assets_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else []
    for section in sections:
        items = [e for e in REGISTRY if e["section"] == section and (not only or e["id"] in only)]
        if not items:
            continue
        if not only:  # a full rebuild of the section also drops examples that no longer exist
            manifest = [m for m in manifest if m["section"] != section]
            for old in (assets_dir / section).glob("*.*") if (assets_dir / section).exists() else ():
                if old.stem not in {e["id"] for e in items}:
                    old.unlink()
        deck = Deck()
        for e in items:
            s = deck.slide(bg="FFFFFF")
            e["fn"](deck, s)
            deck.notes(s, f"{e['id']} {e['title']}\n{e['note']}\n示例内容均为虚构。")
        pptx = out_dir / f"{section}.pptx"
        deck.save(pptx)
        with session_fonts(fonts_dir):
            pdf = to_pdf(pptx, out_dir)
        doc = pymupdf.open(pdf)
        review = out_dir / "review" / section
        review.mkdir(parents=True, exist_ok=True)
        for e, page in zip(items, doc):
            full = review / f"{e['id']}.png"
            page.get_pixmap(matrix=pymupdf.Matrix(1280 / page.rect.width, 1280 / page.rect.width)).save(full)
            kept = small_image(full, assets_dir / section / e["id"], width)
            manifest = [m for m in manifest if not (m["section"] == section and m["id"] == e["id"])]
            manifest.append({"section": section, "id": e["id"], "title": e["title"], "note": e["note"],
                             "file": f"{section}/{kept.name}", "source": e["source"], "fonts": e["fonts"]})
            print(f"{section}/{e['id']}  {e['title']}")
        doc.close()
    order = {s: i for i, s in enumerate(SECTIONS)}
    manifest.sort(key=lambda m: (order.get(m["section"], 9), m["id"]))
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    return manifest
