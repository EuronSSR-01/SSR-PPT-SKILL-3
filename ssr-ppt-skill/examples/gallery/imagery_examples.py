"""Imagery examples (section "imagery"): choosing a photo, treating it, putting text on it, cropping,
recolouring illustrations, drawing a project object, and using icons. Photos: see photos.json."""
from gallery import bg, crop, example, generated, photo, scratch, treated
from look import ACCENT, FAINT, INK, LINE, M, MUTED, PRIMARY, PRIMARY_LIGHT, SANS, SANS_BLACK, W, WARM, ill, title

F = (SANS,)
GOOD, BAD = "1E8E5A", "C8372D"


def verdict(deck, s, x, y, ok, text, w=360):
    deck.icon(s, "circle-check" if ok else "circle-x", x, y, size=28, color=GOOD if ok else BAD)
    deck.text(s, x + 38, y - 2, w - 38, 60, text, size=17, font=SANS, color=INK, line_spacing=1.4)


@example("imagery", "I01-a", "找图：先看候选，再选一张", "按主体、清晰度、水印和许可挑；标题对不上画面、像素太小的都不要。", F)
def choose_photo(deck, s):
    title(deck, s, "找图：先看候选，再选一张", sub="find_images.py search 生成候选总览；打开原图核对后再用", size=34)
    small = scratch("squash-tiny.jpg")
    if not small.exists():
        from PIL import Image
        img = Image.open(photo("squash"))
        img.resize((180, round(180 * img.height / img.width))).resize((900, round(900 * img.height / img.width)),
                                                                       Image.NEAREST).save(small)
    cards = [(photo("radishes"), True, "主体清楚、颜色好；公有领域，可直接用"),
             (photo("fabric-gold"), False, "画面是布料：题目叫 book cover fabric，和“蔬菜”无关"),
             (small, False, "原图只有 180px 宽：放大到半页就糊")]
    for i, (path, ok, text) in enumerate(cards):
        x = M + i * 380
        deck.picture(s, path, x, 190, 350, 240)
        deck.rect(s, x, 190, 350, 240, line=GOOD if ok else LINE, line_width=4 if ok else 1)
        verdict(deck, s, x, 450, ok, text, w=350)
    deck.rect(s, M, 560, W, 1, fill=LINE)
    deck.text(s, M, 576, W, 60, "写进 sources.md：图片 radishes.jpg｜第 5 页｜“20120414-DM-LSC-2796”, USDAgov, Public Domain｜"
              "来源页 flickr.com/photos/41284017@N08/8427643419", size=16, font=SANS, color=MUTED, line_spacing=1.45)


@example("imagery", "I02-a", "同一张照片的四种处理", "原图、黑白、降饱和偏暖、双色调：全套选一种并保持一致。", F)
def treatments(deck, s):
    title(deck, s, "同一张照片的四种处理", sub="scripts/image_fx.py：gray / grade / duotone；一套演示只选一种", size=34)
    versions = [(photo("farm"), "原图"), (treated("farm", "gray", contrast=1.35), "黑白高对比 · gray --contrast 1.35"),
                (treated("farm", "grade", saturation=0.65, warmth=0.07, brightness=1.04), "降饱和偏暖 · grade"),
                (treated("farm", "duotone", dark="1B2A4A", light="F2E9D8"), "双色调 · duotone")]
    for i, (path, cap) in enumerate(versions):
        x, y = M + (i % 2) * 570, 170 + (i // 2) * 250
        deck.picture(s, path, x, y, 550, 200)
        deck.text(s, x, y + 206, 550, 26, cap, size=16, font=SANS, color=INK)
    deck.text(s, M, 680, W, 20, "照片：~MVI~ (warped)，CC BY 2.0", size=12, font=SANS, color=FAINT)


@example("imagery", "I03-a", "文字压在照片上：只盖住文字那一侧", "整张压暗让照片发灰；只在文字一侧加渐变，照片其余部分保持原样。", F)
def text_on_photo(deck, s):
    title(deck, s, "文字压在照片上：只盖住文字那一侧", size=34)
    for i, good in enumerate((False, True)):
        x = M + i * 570
        deck.picture(s, photo("tomato-picking"), x, 140, 550, 340)
        if good:
            deck.gradient_rect(s, x + 260, 140, 290, 340, [(0, "0E1B12", 0), (0.5, "0E1B12", 0.8), (1, "0E1B12", 0.9)])
            deck.text(s, x + 300, 250, 236, 120, "每一颗\n都在成熟那天摘下", size=26, font=SANS, bold=True, color="FFFFFF",
                      line_spacing=1.3)
        else:
            deck.rect(s, x, 140, 550, 340, fill="000000", alpha=0.5)
            deck.text(s, x + 300, 250, 236, 120, "每一颗\n都在成熟那天摘下", size=26, font=SANS, bold=True, color="FFFFFF",
                      line_spacing=1.3)
        verdict(deck, s, x, 500, good, "只在文字一侧加渐变：照片的颜色保住了" if good else "整张盖 50% 黑：字能读，但照片发灰、发脏",
                w=550)
    deck.text(s, M, 680, W, 20, "照片：Alachua County，公有领域", size=12, font=SANS, color=FAINT)


@example("imagery", "I04-a", "裁切：给主体留位置，特写更有力", "同一张照片三种裁法：全景交代环境，特写更有冲击力；不要切掉主体。", F)
def cropping(deck, s):
    title(deck, s, "裁切：给主体留位置，特写更有力", size=34)
    crops = [(photo("potatoes"), True, "全景：交代环境，适合封面或分屏"),
             (crop("potatoes", (0.05, 0.25, 0.65, 0.75)), True, "特写：只留手和土豆，适合大图配一句话"),
             (crop("potatoes", (0.45, 0.0, 1.0, 0.5)), False, "切掉了主体：只剩衣服和背景")]
    for i, (path, ok, text) in enumerate(crops):
        x = M + i * 380
        deck.picture(s, path, x, 150, 350, 300)
        verdict(deck, s, x, 470, ok, text, w=350)
    deck.text(s, M, 680, W, 20, "照片：rawpixel，CC0", size=12, font=SANS, color=FAINT)


@example("imagery", "I05-a", "插画跟着演示换色", "同一组插画给出主色和强调色就整体换色；深色底再把浅色档调暗。", F)
def recolour(deck, s):
    title(deck, s, "插画跟着演示换色", sub="deck.illustration(..., primary=, accent=)；深色底用 tokens= 调暗浅色档", size=34)
    rows = [("默认蓝橙", {}, "FFFFFF"), ("绿与红", {"primary": "0B6E4F", "accent": "E4572E"}, "F4F1EA"),
            ("深色底", {"primary": "4CC2FF", "accent": "F2B13C", "ink": "0B1426", "surface": "1B2633", "line": "2A3746",
                       "tokens": {"primary_light": "17324A", "accent_light": "3A2E1A"}}, "0C1117")]
    for i, (label, kw, paper) in enumerate(rows):
        y = 170 + i * 165
        deck.rect(s, M, y, W, 150, fill=paper, radius=12, line=LINE if paper == "FFFFFF" else None)
        deck.text(s, M + 24, y + 58, 160, 30, label, size=20, font=SANS, bold=True, color="E6EDF3" if paper == "0C1117" else INK)
        for j, name in enumerate(("factory", "reefer-truck", "store", "shopping-cart")):
            deck.illustration(s, name, M + 200 + j * 230, y + 8, 200, 136, **kw)


@example("imagery", "I06-a", "为项目补画一个物体：冷藏车", "从库里最接近的货车改：换车厢颜色、加制冷机组和雪花标；然后放进页面看效果。", F)
def draw_object(deck, s):
    title(deck, s, "为项目补画一个物体：冷藏车", sub="从 truck.svg 改出 reefer-truck.svg：同一画布、同一地平线、同一套可替换的颜色", size=34)
    ill(deck, s, "truck", M, 190, 330, 248)
    deck.icon(s, "arrow-right", M + 350, 290, size=44, color=FAINT)
    ill(deck, s, "reefer-truck", M + 420, 190, 330, 248)
    steps = ["1  要认出什么：车厢 + 制冷机组 + 冷色", "2  从最像的图改：truck.svg", "3  车厢改浅色、加机组和雪花标",
             "4  check 检查，和同风格的图放在一起看", "5  登记进 INDEX.md"]
    for i, text in enumerate(steps):
        deck.text(s, 900, 190 + i * 56, 320, 50, text, size=17, font=SANS, color=INK)
    deck.rect(s, M, 470, W, 180, fill=WARM, radius=12)
    deck.text(s, M + 30, 500, 500, 40, "全程冷链，4 小时内入仓", size=30, font=SANS, bold=True, color=INK)
    deck.text(s, M + 30, 550, 520, 60, "车厢温度 0–4°C，城市仓到门店每日 3 趟", size=20, font=SANS, color=MUTED)
    ill(deck, s, ["reefer-truck", "warehouse", "reefer-truck", "store"], 640, 480, 540, 160)


@example("imagery", "I07-a", "图标：一套风格、一种线宽、贴切", "左边混用实心、彩色圆底和不相干的图标；右边统一线性图标，只给重点上色。", F)
def icon_use(deck, s):
    title(deck, s, "图标：一套风格、一种线宽、贴切", size=34)
    items = [("clock", "30 分钟送达"), ("leaf", "损耗率 5.9%"), ("store", "126 家门店"), ("warehouse", "5 座城市仓")]
    deck.text(s, M, 150, 520, 30, "不要这样", size=20, font=SANS, bold=True, color=BAD)
    wrong = [("clock", "E8590C", True), ("lightbulb", "2E7D6B", False), ("star", "8E44AD", True), ("rocket", "1F4E9E", False)]
    for i, ((icon, colour, filled), (_, text)) in enumerate(zip(wrong, items)):
        y = 200 + i * 100
        deck.ellipse(s, M + 30, y + 24, 30, fill=colour)
        deck.icon(s, icon, M + 12, y + 6, size=36, color="FFFFFF", fill="FFFFFF" if filled else None)
        deck.text(s, M + 80, y + 8, 400, 34, text, size=24, font=SANS, color=INK)
    deck.text(s, 680, 150, 520, 30, "改成这样", size=20, font=SANS, bold=True, color=GOOD)
    for i, (icon, text) in enumerate(items):
        y = 200 + i * 100
        deck.icon(s, icon, 680, y + 6, size=36, color=ACCENT if i == 1 else PRIMARY)
        deck.text(s, 736, y + 8, 400, 34, text, size=24, font=SANS, color=INK)
    deck.text(s, M, 620, W, 60, "左：实心与线性混用、每个一种颜色、灯泡和火箭与内容无关。右：同一套线性图标、同样大小，强调色只给要讲的那一条。",
              size=18, font=SANS, color=MUTED, line_spacing=1.5)
