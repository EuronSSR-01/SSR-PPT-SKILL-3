"""Tests for what SKILL 3 added: illustration library, image treatments, image search, pptx_kit additions,
font coverage, layout-check rules for intentional effects, and the example gallery and its links."""
import contextlib
import importlib.util
import io
import json
import re
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "ssr-ppt-skill"
SCRIPTS = SKILL / "scripts"
sys.path.insert(0, str(SCRIPTS))


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ill = load("illustrations")
fx = load("image_fx")
find_images = load("find_images")
font_coverage = load("font_coverage")
preview = load("preview")
from pptx_kit import Deck  # noqa: E402


def opened(path):
    """A loaded copy of an image, with the file closed again."""
    with Image.open(path) as im:
        im.load()
        return im.copy()


def soffice_or_none():
    for cand in (shutil.which("soffice.com"), shutil.which("soffice"), r"C:\Program Files\LibreOffice\program\soffice.com",
                 "/usr/bin/soffice", "/Applications/LibreOffice.app/Contents/MacOS/soffice"):
        if cand and Path(cand).exists():
            return cand
    return None


class IllustrationTests(unittest.TestCase):
    def test_every_drawing_passes_check_and_matches_its_index(self):
        self.assertIn("flat", ill.styles())
        for style in ill.styles():
            index = (ill.ROOT / style / "INDEX.md").read_text(encoding="utf-8")
            rows = dict(re.findall(r"\|\s*`([\w-]+)`\s*\|[^|]+\|\s*([\d.]+)\s*\|", index))
            self.assertEqual(set(rows), set(ill.names(style)), style)
            self.assertTrue((ill.ROOT / style / "sheet.png").exists(), style)
            for name in ill.names(style):
                path = ill.path(name, style)
                self.assertEqual(ill.check(path), [], f"{style}/{name}")
                _, scale, _ = ill._parts(path.read_text(encoding="utf-8"))
                self.assertAlmostEqual(scale, float(rows[name]), msg=f"{style}/{name}")

    def test_palette_recolor_and_overrides(self):
        pal = ill.palette("#0B6E4F", "E4572E", extra={"primary_light": "17324A"})
        self.assertEqual(pal["primary"], "0B6E4F")
        self.assertEqual(pal["primary_light"], "17324A")
        self.assertNotEqual(pal["accent_dark"], ill.TOKENS["accent_dark"])
        self.assertEqual(pal["leaf"], ill.TOKENS["leaf"])            # plants stay natural unless asked
        with self.assertRaises(KeyError):
            ill.palette(extra={"glow": "FFFFFF"})
        svg = '<svg><rect fill="#2F6FDE"/><rect fill="#FFFFFF"/><rect stroke="#22303f"/></svg>'
        out = ill.recolor(svg, primary="0B6E4F", ink="111111")
        self.assertIn("#0B6E4F", out)
        self.assertIn("#FFFFFF", out)                                # fixed colours stay
        self.assertIn("#111111", out)

    def test_scene_keeps_vehicles_smaller_than_buildings(self):
        svg = ill.scene(["warehouse", "truck", "truck:1"])
        scales = [float(s) for s in re.findall(r"scale\(([\d.]+)\)", svg)]
        self.assertEqual(len(scales), 3)
        self.assertAlmostEqual(scales[1] / scales[0], 0.62, places=2)
        self.assertAlmostEqual(scales[2], scales[0], places=4)       # an explicit size wins

    def test_check_names_each_problem(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.svg"
            bad.write_text('<svg viewBox="0 0 320 240"><defs><linearGradient/></defs><text>价</text>'
                           '<rect id="a" fill="red"/><rect fill="#123456"/><rect fill="#abc"/></svg>', encoding="utf-8")
            problems = " ".join(ill.check(bad))
        for word in ("xmlns", "<text>", "gradient", "id/class", "named colours", "3-digit", "123456"):
            self.assertIn(word, problems)

    def test_cli_lists_styles_and_exports(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()) as out:
            with mock.patch.object(sys, "argv", ["illustrations.py", "export", "reefer-truck", "--primary", "0B3D91",
                                                 "--out", str(Path(tmp) / "t.svg")]):
                ill.main()
            text = (Path(tmp) / "t.svg").read_text(encoding="utf-8")
        self.assertIn("#0B3D91", text)
        self.assertNotIn("#2F6FDE", text)

    @unittest.skipUnless(importlib.util.find_spec("pymupdf") or importlib.util.find_spec("fitz"), "PyMuPDF is needed")
    def test_deck_inserts_single_scene_styled_and_custom_drawings(self):
        with tempfile.TemporaryDirectory() as tmp:
            custom = Path(tmp) / "mine.svg"
            custom.write_text((ill.ROOT / "flat" / "truck.svg").read_text(encoding="utf-8"), encoding="utf-8")
            deck = Deck()
            s = deck.slide()
            pics = [deck.illustration(s, "store", 0, 0, 320, 240, primary="0B3D91", out=Path(tmp) / "a.png"),
                    deck.illustration(s, ["factory", "truck", "store"], 0, 300, 900, 200, out=Path(tmp) / "b.png"),
                    deck.illustration(s, "warehouse", 400, 0, 320, 240, style="line", out=Path(tmp) / "c.png"),
                    deck.illustration(s, str(custom), 800, 0, 320, 240, tokens={"primary_light": "17324A"},
                                      out=Path(tmp) / "d.png")]
            self.assertTrue(all(p.shape_type == 13 for p in pics))   # pictures
            self.assertGreater(opened(Path(tmp) / "b.png").width, 1000)


class ImageFxTests(unittest.TestCase):
    def test_treatments_and_generated_backgrounds(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            src = tmp / "src.jpg"
            Image.new("RGB", (300, 200), (200, 80, 40)).save(src)
            self.assertEqual(opened(fx.gray(src, tmp / "g.jpg", 1.3)).mode, "RGB")
            r, g, b = opened(fx.duotone(src, tmp / "d.jpg", "000000", "FFFFFF")).convert("RGB").getpixel((10, 10))
            self.assertTrue(abs(r - g) < 6 and abs(g - b) < 6)       # a neutral duotone stays grey
            warm = opened(fx.grade(src, tmp / "w.jpg", saturation=0.5, warmth=0.1)).getpixel((10, 10))
            self.assertLess(warm[1], 120)
            rounded = opened(fx.round_corners(src, tmp / "r.png", radius=30))
            self.assertEqual(rounded.mode, "RGBA")
            self.assertEqual(rounded.getpixel((0, 0))[3], 0)          # corner is transparent
            self.assertEqual(opened(fx.circle(src, tmp / "c.png", 100)).size, (100, 100))
            self.assertEqual(opened(fx.grain(tmp / "n.png", (160, 90), 0.1)).mode, "RGBA")
            self.assertEqual(opened(fx.glow(tmp / "l.png", (160, 90))).size, (160, 90))
            self.assertEqual(opened(fx.dots(tmp / "p.png", (160, 90))).size, (160, 90))
            self.assertEqual(opened(fx.halftone(tmp / "h.png", (160, 90))).mode, "RGBA")


class FindImagesTests(unittest.TestCase):
    OPENVERSE = {"results": [{"id": "abc", "title": "Tomatoes <b>at</b> market", "creator": "Jun", "license": "by",
                              "license_version": "2.0", "license_url": "https://creativecommons.org/licenses/by/2.0/",
                              "foreign_landing_url": "https://example.org/p/1", "url": "https://example.org/1.jpg",
                              "thumbnail": "https://example.org/t1.jpg", "width": 1600, "height": 1000, "source": "flickr"},
                             {"id": "small", "title": "Tiny", "creator": "X", "license": "cc0", "license_version": "1.0",
                              "license_url": "", "foreign_landing_url": "", "url": "https://example.org/2.jpg",
                              "thumbnail": "", "width": 400, "height": 300, "source": "flickr"}]}
    COMMONS = {"query": {"pages": {"7": {"pageid": 7, "index": 1, "title": "File:Farm.jpg", "imageinfo": [{
        "url": "https://upload.example/farm.jpg", "descriptionurl": "https://commons.example/Farm", "thumburl": "",
        "width": 3000, "height": 2000, "extmetadata": {"LicenseShortName": {"value": "Public domain"},
                                                      "Artist": {"value": "<a>USDA</a>"}}}]},
        "8": {"pageid": 8, "index": 2, "title": "File:NC.jpg", "imageinfo": [{
            "url": "https://upload.example/nc.jpg", "descriptionurl": "", "thumburl": "", "width": 3000, "height": 2000,
            "extmetadata": {"LicenseShortName": {"value": "CC BY-NC 2.0"}}}]}}}}

    def test_licence_names_orientation_and_attribution(self):
        self.assertEqual(find_images.commons_license("CC BY-SA 4.0"), "by-sa")
        self.assertEqual(find_images.commons_license("Public domain"), "pdm")
        self.assertEqual(find_images.commons_license("CC0"), "cc0")
        self.assertEqual(find_images.commons_license("CC BY-NC 2.0"), "by-nc")
        self.assertTrue(find_images.orientation_ok(1600, 900, "landscape"))
        self.assertFalse(find_images.orientation_ok(900, 1600, "landscape"))
        cand = {"title": "T", "creator": "A", "license": "by", "license_version": "2.0", "page": "https://p"}
        self.assertIn("CC BY 2.0", find_images.attribution(cand))
        self.assertIn("无需署名", find_images.attribution(dict(cand, license="cc0")))

    def test_search_filters_and_get_records_the_source(self):
        def fake_json(url):
            return self.OPENVERSE if "openverse" in url else self.COMMONS
        with tempfile.TemporaryDirectory() as tmp, mock.patch.object(find_images, "fetch_json", fake_json), \
                mock.patch.object(find_images, "fetch", lambda url, timeout=40: b"JPEGDATA"), \
                contextlib.redirect_stdout(io.StringIO()) as out:
            store = Path(tmp) / "c.json"
            args = type("A", (), dict(query="farm", source="openverse,commons", license="cc0,pdm,by,by-sa",
                                      orientation="landscape", min_width=1000, n=12, json=str(store), sheet=None))
            find_images.cmd_search(args)
            cands = json.loads(store.read_text(encoding="utf-8"))["candidates"]
            self.assertEqual([c["id"] for c in cands], ["ov:abc", "wc:7"])   # too small and NC are left out
            self.assertEqual(cands[0]["title"], "Tomatoes at market")
            self.assertEqual(cands[1]["creator"], "USDA")
            sources = Path(tmp) / "sources.md"
            get = type("G", (), dict(which="1", json=str(store), out=str(Path(tmp) / "img" / "t.jpg"), max_width=2400,
                                     record=str(sources), page="5"))
            find_images.cmd_get(get)
            self.assertEqual((Path(tmp) / "img" / "t.jpg").read_bytes(), b"JPEGDATA")
            line = sources.read_text(encoding="utf-8")
        self.assertIn("第 5 页", line)
        self.assertIn("CC BY 2.0", line)
        self.assertIn("credit needed", out.getvalue())


class KitAdditionTests(unittest.TestCase):
    def test_line_chart_labels_shapes_text_options(self):
        deck = Deck()
        s = deck.slide()
        deck.line_chart(s, 80, 100, 800, 400, ["1月", "2月", "3月"], {"本店": [9.6, 8.8, 7.9], "同业": [9.4, 9.3, 9.5]},
                        number_format='0.0"%"', grid="E9ECF0", label_bg="FFFFFF", min_value=4)
        deck.polygon(s, [(0, 0), (100, 50), (200, 0)], line="E8590C", line_width=4, closed=False, dash=True)
        deck.polygon(s, [(0, 100), (50, 150), (100, 100)], fill="E8590C")
        deck.gradient_rect(s, 0, 0, 640, 720, [(0, "000000", 0.8), (1, "000000", 0)])
        deck.rect(s, 10, 10, 100, 100, fill="0B3D91", alpha=0.25, radius=12)
        deck.text(s, 10, 200, 60, 300, "竖排标题", size=40, vertical=True)
        deck.text(s, 100, 200, 600, 40, "SPACED", size=14, spacing=0.2)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "k.pptx"
            deck.save(path)
            with zipfile.ZipFile(path) as z:
                slide = z.read("ppt/slides/slide1.xml").decode("utf-8")
                chart = z.read([n for n in z.namelist() if n.startswith("ppt/charts/chart")][0]).decode("utf-8")
        self.assertEqual(chart.count("<c:dLbl>"), 2)                 # last value of each line
        self.assertIn('formatCode="0.0&quot;%&quot;"', chart)
        self.assertRegex(chart, r"<c:dLbl>.*?<c:spPr><a:solidFill><a:srgbClr val=\"FFFFFF\"/>")
        self.assertRegex(chart, r'<c:min val="4(\.0)?"/>')
        self.assertIn("<a:custGeom>", slide)
        self.assertIn("<a:gradFill", slide)
        self.assertIn('<a:alpha val="25000"/>', slide)
        self.assertIn('vert="eaVert"', slide)
        self.assertRegex(slide, r'spc="\d+"')

    def test_pptx_md_example_runs(self):
        text = (SKILL / "references" / "pptx.md").read_text(encoding="utf-8")
        code = re.search(r"```python\n(.*?)```", text, re.S).group(1)
        code = code.replace('"<技能目录>/scripts"', repr(str(SCRIPTS)))
        with tempfile.TemporaryDirectory() as tmp:
            code = code.replace('"deck.pptx"', repr(str(Path(tmp) / "deck.pptx")))
            exec(compile(code, "pptx.md", "exec"), {})
            self.assertTrue((Path(tmp) / "deck.pptx").exists())


class FontCoverageTests(unittest.TestCase):
    def test_reports_missing_characters(self):
        from fontTools.fontBuilder import FontBuilder
        from fontTools.pens.ttGlyphPen import TTGlyphPen
        with tempfile.TemporaryDirectory() as tmp:
            fb = FontBuilder(1000, isTTF=True)
            glyphs = [".notdef", "A", "uni4E2D"]
            fb.setupGlyphOrder(glyphs)
            fb.setupCharacterMap({ord("A"): "A", ord("中"): "uni4E2D"})
            pen = TTGlyphPen(None)
            pen.moveTo((0, 0)); pen.lineTo((0, 500)); pen.lineTo((500, 0)); pen.closePath()
            fb.setupGlyf({g: pen.glyph() for g in glyphs})
            fb.setupHorizontalMetrics({g: (600, 0) for g in glyphs})
            fb.setupHorizontalHeader(ascent=800, descent=-200)
            fb.setupNameTable({"familyName": "Tiny Test", "styleName": "Regular"})
            fb.setupOS2()
            fb.setupPost()
            font = Path(tmp) / "tiny.ttf"
            fb.save(str(font))
            with mock.patch.object(sys, "argv", ["font_coverage.py", str(font), "--text", "中文A"]), \
                    contextlib.redirect_stdout(io.StringIO()) as out, self.assertRaises(SystemExit) as code:
                font_coverage.main()
        self.assertEqual(code.exception.code, 1)
        self.assertIn("本文缺 1 个字符：文", out.getvalue())
        self.assertIn("GB2312 常用汉字 1/6763", out.getvalue())


@unittest.skipUnless(soffice_or_none() and preview.pymupdf_or_none(), "LibreOffice and PyMuPDF are needed to render")
class IntentionalEffectTests(unittest.TestCase):
    def test_bleed_misprint_and_vertical_text_are_warnings(self):
        deck = Deck()
        s = deck.slide()
        deck.text(s, 900, 400, 600, 400, "30", size=300, wrap=False)                  # display bleed
        deck.text(s, 80, 60, 600, 100, "错版标题", size=60, color="FF48B0")              # misprint copy
        deck.text(s, 74, 56, 600, 100, "错版标题", size=60, color="0078BF")
        deck.text(s, 60, 200, 60, 400, "社区店的一天", size=40, vertical=True)            # vertical: no orphans
        s2 = deck.slide()
        deck.text(s2, 1200, 300, 400, 40, "普通文字跑出页面", size=24, wrap=False)        # still an error
        deck.text(s2, 80, 80, 600, 60, "第一段文字", size=40)
        deck.text(s2, 90, 90, 600, 60, "另一段文字", size=40)                           # different text: error
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "fx.pptx"
            deck.save(src)
            layout = []
            preview.pptx_to_pngs(src, Path(tmp) / "out", soffice_or_none(), 800, layout)
        first = {(f["kind"], f["severity"]) for f in layout[0]["findings"]}
        self.assertIn(("text_outside_slide", "warning"), first)
        self.assertIn(("text_overlap", "warning"), first)
        self.assertNotIn(("orphan_line", "warning"), first)
        self.assertFalse(any(sev == "error" for _, sev in first))
        second = {(f["kind"], f["severity"]) for f in layout[1]["findings"]}
        self.assertIn(("text_outside_slide", "error"), second)
        self.assertIn(("text_overlap", "error"), second)


class GalleryTests(unittest.TestCase):
    def test_manifest_files_html_and_doc_links(self):
        assets = SKILL / "assets"
        manifest = json.loads((assets / "gallery" / "manifest.json").read_text(encoding="utf-8"))
        self.assertGreater(len(manifest), 150)
        for m in manifest:
            self.assertTrue((assets / "gallery" / m["file"]).exists(), m["file"])
            self.assertTrue((SKILL / m["source"]).exists(), m["source"])
        html = (assets / "design-examples.html").read_text(encoding="utf-8")
        for m in manifest:
            self.assertIn(f'"{m["id"]}"', html)
        docs = sorted((SKILL / "references").glob("*.md")) + [SKILL / "SKILL.md", assets / "illustrations" / "README.md",
                                                              SKILL / "examples" / "gallery" / "README.md"]
        for doc in docs:
            text = doc.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
                if target.startswith(("http", "mailto")):
                    continue
                self.assertTrue((doc.parent / target).exists(), f"{doc.name}: {target}")

    def test_every_layout_and_recipe_page_is_documented(self):
        manifest = json.loads((SKILL / "assets" / "gallery" / "manifest.json").read_text(encoding="utf-8"))
        docs = {"layouts": "layouts.md", "recipes": "style-recipes.md", "type": "typography.md", "imagery": "imagery.md"}
        for m in manifest:
            text = (SKILL / "references" / docs[m["section"]]).read_text(encoding="utf-8")
            self.assertIn(f"assets/gallery/{m['file']}", text, m["id"])


if __name__ == "__main__":
    unittest.main()
