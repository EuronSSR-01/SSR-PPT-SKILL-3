"""Style recipe examples R14-R21, added in SKILL 3 to show that the recipe list keeps growing: flat illustration
story, line-drawing manual, bento grid, formal report, notebook, riso print, colour fields and cool airy.
Fictional content."""
import content as C
from gallery import bg, crop, example, generated, photo, treated

SANS, SANS_BLACK, SANS_MED = "Noto Sans SC", "Noto Sans SC Black", "Noto Sans SC Medium"
SERIF, SERIF_BLACK = "Noto Serif SC", "Noto Serif SC Black"
MISANS, MISANS_SEMI, MISANS_HEAVY = "MiSans", "MiSans Semibold", "MiSans Heavy"
HOS, MONO, KAI, QINGKE = "HarmonyOS Sans SC", "JetBrains Mono", "LXGW WenKai", "ZCOOL QingKe HuangYou"


# ====================================================================== R14 flat illustration story
R14 = dict(sky="EAF2FC", ground="DCE7D3", ink="22303F", gray="5D6B7A", primary="2F6FDE", accent="F28C28", accent_text="CE7722", card="FFFFFF")


def r14_ill(deck, s, name, x, y, w, h, **kw):
    return deck.illustration(s, name, x, y, w, h, primary=R14["primary"], accent=R14["accent"], **kw)


@example("recipes", "R14-a", "R14 扁平插画叙事 · 封面", "插画场景就是主视觉：天空和地面两块底色，物体站在同一条地平线上，标题压在天空里。", (MISANS_HEAVY,))
def r14_cover(deck, s):
    k = R14
    bg(s, k["sky"])
    deck.rect(s, 0, 600, 1280, 120, fill=k["ground"])
    deck.ellipse(s, 1130, 110, 46, fill="FFD38A")
    r14_ill(deck, s, ["farm", "truck", "warehouse", "truck", "store"], 20, 300, 1240, 310)
    deck.text(s, 80, 70, 900, 110, C.COVER_TITLE, size=80, font=MISANS_HEAVY, color=k["ink"])
    deck.text(s, 84, 180, 800, 36, C.COVER_SUB, size=24, font=MISANS, color=k["gray"])


@example("recipes", "R14-b", "R14 扁平插画叙事 · 数据页", "图表旁边站一个“主角”插画，让数字有了对象；配色和插画同一套。", (MISANS_HEAVY,))
def r14_data(deck, s):
    k = R14
    bg(s, "F7FAFE")
    deck.text(s, 80, 60, 1000, 70, "扔掉的菜，半年少了近四成", size=44, font=MISANS_HEAVY, color=k["ink"])
    deck.text(s, 84, 128, 800, 30, "生鲜损耗率，%，2027 年 1–6 月（虚构示例）", size=18, font=MISANS, color=k["gray"])
    deck.rect(s, 80, 180, 760, 470, fill=k["card"], radius=28)
    deck.bar_chart(s, 110, 210, 700, 420, C.MONTHS, C.LOSS, highlight={5}, horizontal=False, color=k["accent"],
                   base="BFD3F5", number_format='0.0"%"', font=MISANS, size=18, label_color=k["ink"], axis_color=k["gray"],
                   gap_width=45)
    r14_ill(deck, s, "produce", 880, 230, 330, 248)
    deck.text(s, 880, 500, 330, 90, "按日订货以后，\n菜不再在店里过夜", size=24, font=MISANS_SEMI, color=k["ink"], line_spacing=1.4)


@example("recipes", "R14-c", "R14 扁平插画叙事 · 图片页", "三张插画卡片讲三个环节，每张一个物体、一个时间、一句话；箭头只表示先后。", (MISANS_HEAVY,))
def r14_picture(deck, s):
    k = R14
    bg(s, "F7FAFE")
    deck.text(s, 80, 60, 1000, 70, "从地里到家里", size=44, font=MISANS_HEAVY, color=k["ink"])
    cards = [("farm", "06:00", "清晨采摘"), ("warehouse", "10:00", "城市仓分拣"), ("store", "次日 09:30", "门店上架")]
    for i, (name, time, text) in enumerate(cards):
        x = 80 + i * 390
        deck.rect(s, x, 170, 340, 450, fill=k["card"], radius=28)
        deck.rect(s, x, 170, 340, 240, fill=k["sky"], radius=28)
        deck.rect(s, x, 380, 340, 30, fill=k["sky"])
        r14_ill(deck, s, name, x + 30, 190, 280, 210)
        deck.text(s, x + 30, 440, 280, 60, time, size=40, font=MISANS_HEAVY, color=k["accent_text"] if i == 1 else k["primary"])
        deck.text(s, x + 30, 506, 280, 36, text, size=24, font=MISANS_SEMI, color=k["ink"])
        if i < 2:
            deck.icon(s, "arrow-right", x + 350, 380, size=32, color="9AB3DC")


@example("recipes", "R14-d", "R14 扁平插画叙事 · 特色页", "像连环画一样按时间讲一个人的一天：三格画面、时间戳、一句旁白。", (MISANS_HEAVY,))
def r14_signature(deck, s):
    k = R14
    bg(s, "FFFFFF")
    deck.text(s, 80, 50, 1000, 60, "一棵青菜的一天", size=40, font=MISANS_HEAVY, color=k["ink"])
    panels = [("farm", "06:00", "在地里被摘下", "EAF2FC"), ("store", "次日 09:30", "摆上社区店的货架", "FFF1E2"),
              ("shopping-cart", "18:30", "被放进购物车带回家", "E8F4EA")]
    for i, (name, time, text, tint) in enumerate(panels):
        x = 80 + i * 380
        deck.rect(s, x, 140, 360, 400, fill=tint, line=k["ink"], line_width=2.5, radius=12)
        r14_ill(deck, s, name, x + 30, 190, 300, 225)
        deck.rect(s, x + 20, 156, 150, 40, fill=k["ink"], radius=20)
        deck.text(s, x + 20, 162, 150, 30, time, size=20, font=MISANS_SEMI, color="FFFFFF", align="center")
        deck.text(s, x, 560, 360, 40, text, size=24, font=MISANS_SEMI, color=k["ink"], align="center")


# ====================================================================== R15 line-drawing manual
R15 = dict(ink="22303F", gray="6A7684", accent="F28C28", accent_text="AC631C", tint="D6E4FA", paper="FFFFFF")


def num_badge(deck, s, x, y, n, r=16, fill=None):
    k = R15
    deck.ellipse(s, x, y, r, fill=fill or "FFFFFF", line=k["ink"], line_width=2)
    deck.text(s, x - r, y - r * 0.68, 2 * r, r * 1.4, str(n), size=r * 1.1, font=MONO, color="FFFFFF" if fill else k["ink"],
              align="center", ea=HOS)


def r15_frame(deck, s):
    k = R15
    deck.rect(s, 40, 40, 1200, 640, line=k["ink"], line_width=1.5)
    for x, y in ((40, 40), (1240, 40), (40, 680), (1240, 680)):
        deck.line(s, x - 14, y, x + 14, y, color=k["ink"], width=1)
        deck.line(s, x, y - 14, x, y + 14, color=k["ink"], width=1)


@example("recipes", "R15-a", "R15 线描说明书 · 封面", "线描插画配等宽小字和裁切标记，像一本产品说明书；只有一处强调色。", (HOS, MONO))
def r15_cover(deck, s):
    k = R15
    r15_frame(deck, s)
    deck.text(s, 90, 100, 600, 24, "说明书 · 第 1 版 · 2027.07", size=16, font=MONO, color=k["gray"], ea=HOS)
    deck.text(s, 90, 200, 560, 200, "把产地\n搬进社区", size=72, font=HOS, bold=True, color=k["ink"], line_spacing=1.15)
    deck.text(s, 90, 420, 520, 60, "社区店升级的四个步骤", size=24, font=HOS, color=k["ink"])
    deck.rect(s, 92, 470, 40, 4, fill=k["accent"])
    deck.illustration(s, "store", 640, 150, 560, 420, style="line")


@example("recipes", "R15-b", "R15 线描说明书 · 数据页", "图表也用细线；关键点用带圈编号标出，说明写在图下的图例里。", (HOS, MONO))
def r15_data(deck, s):
    k = R15
    r15_frame(deck, s)
    deck.text(s, 90, 80, 1000, 50, "损耗率：6 个月从 9.6% 降到 5.9%", size=34, font=HOS, bold=True, color=k["ink"])
    deck.line_chart(s, 80, 150, 840, 400, C.MONTHS, {"损耗率": C.LOSS}, colors=[k["ink"]], labels="all",
                    number_format='0.0"%"', font=MONO, size=16, axis_color=k["ink"], axis_line=k["ink"], width=2,
                    markers=True, min_value=4)
    num_badge(deck, s, 432, 344, 1, fill=k["accent"])
    num_badge(deck, s, 852, 462, 2)
    deck.rect(s, 90, 570, 1100, 1, fill=k["ink"])
    deck.text(s, 90, 590, 40, 30, "①", size=22, font=HOS, color=k["accent_text"])
    deck.text(s, 130, 592, 450, 30, "3 月：门店改为按日订货", size=19, font=HOS, color=k["ink"])
    deck.text(s, 600, 590, 40, 30, "②", size=22, font=HOS, color=k["ink"])
    deck.text(s, 640, 592, 500, 30, "6 月：5.9%，比 1 月低 3.7 个百分点", size=19, font=HOS, color=k["ink"])
    deck.rect(s, 940, 160, 260, 380, line=k["ink"], line_width=1, dash=True)
    deck.text(s, 960, 180, 220, 24, "单位：%", size=16, font=MONO, color=k["gray"], ea=HOS)
    deck.text(s, 960, 214, 224, 300, "口径：报损金额 ÷\n进货金额；打折售出\n不计入报损。\n\n数据为虚构示例。", size=17, font=HOS,
              color=k["gray"], line_spacing=1.55)


@example("recipes", "R15-c", "R15 线描说明书 · 图片页", "一张线描图，三处带圈编号指到部位；右侧图例逐条说明，像零件表。", (HOS, MONO))
def r15_picture(deck, s):
    k = R15
    r15_frame(deck, s)
    deck.text(s, 90, 80, 1000, 50, "城市仓的三个部位", size=34, font=HOS, bold=True, color=k["ink"])
    x, y, w, h = 90, 150, 640, 480
    deck.illustration(s, "warehouse", x, y, w, h, style="line")
    kx = w / 320
    spots = [((160, 96), 1), ((160, 175), 2), ((65, 176), 3)]
    for (px, py), n in spots:
        num_badge(deck, s, x + px * kx, y + py * kx, n, fill=k["accent"] if n == 2 else None)
    items = [("通风口", "冷链区每小时换气"), ("卷帘门", "每天 3 趟车进出补货"), ("理货区", "按门店订单拆箱")]
    for i, (name, note) in enumerate(items):
        yy = 210 + i * 120
        num_badge(deck, s, 800, yy + 18, i + 1, fill=k["accent"] if i == 1 else None)
        deck.text(s, 836, yy, 360, 36, name, size=24, font=HOS, bold=True, color=k["ink"])
        deck.text(s, 836, yy + 40, 360, 30, note, size=18, font=HOS, color=k["gray"])
        deck.rect(s, 800, yy + 90, 390, 1, fill="C8D0DB")


@example("recipes", "R15-d", "R15 线描说明书 · 特色页", "分步图：每一步一个编号格子、一张线描、一句动作；像组装说明一样一步一步读。", (HOS, MONO))
def r15_signature(deck, s):
    k = R15
    r15_frame(deck, s)
    deck.text(s, 90, 70, 900, 50, "一单菜怎么到家：四步", size=34, font=HOS, bold=True, color=k["ink"])
    steps = [("truck", "冷链车送到城市仓"), ("warehouse", "按门店订单分拣"), ("store", "门店上午上架"), ("person", "骑手 30 分钟送到")]
    for i, (name, text) in enumerate(steps):
        x = 90 + i * 280
        deck.rect(s, x, 150, 260, 440, line=k["ink"], line_width=1.5)
        num_badge(deck, s, x + 34, 184, i + 1, r=20, fill=k["accent"] if i == 3 else None)
        deck.illustration(s, name, x + 10, 230, 240, 180, style="line")
        deck.rect(s, x + 20, 440, 220, 1, fill="C8D0DB")
        deck.text(s, x + 20, 460, 220, 90, text, size=21, font=HOS, color=k["ink"], line_spacing=1.4)


# ====================================================================== R16 bento
R16 = dict(bg="F2F2F4", tile="FFFFFF", ink="1C1C1E", gray="6D6D71", accent="CC482B", soft="FFE9E3")


def tile(deck, s, x, y, w, h, fill=None):
    deck.rect(s, x, y, w, h, fill=fill or R16["tile"], radius=28)


@example("recipes", "R16-a", "R16 便当格 · 封面", "大小不同的圆角格子各放一件事：标题、照片、一个数字、一张插画；格子间距统一。", (MISANS_HEAVY,))
def r16_cover(deck, s):
    k = R16
    bg(s, k["bg"])
    tile(deck, s, 48, 48, 704, 400)
    deck.text(s, 88, 90, 640, 240, "把产地\n搬进社区", size=88, font=MISANS_HEAVY, color=k["ink"], line_spacing=1.08)
    deck.text(s, 92, 360, 600, 34, C.COVER_SUB, size=22, font=MISANS, color=k["gray"])
    deck.picture(s, treated("squash", "round_corners", ext="png", radius=56, size=(960, 800)), 768, 48, 464, 400)
    tile(deck, s, 48, 464, 344, 208, fill=k["accent"])
    deck.text(s, 80, 494, 300, 100, [[("30", {"size": 80, "font": MISANS_HEAVY}), (" 分钟", {"size": 26, "font": MISANS_SEMI})]],
              color="FFFFFF", font=MISANS)
    deck.text(s, 82, 612, 300, 30, "下单到送达", size=20, font=MISANS, color="FFFFFF")
    tile(deck, s, 408, 464, 344, 208)
    deck.illustration(s, "store", 440, 474, 280, 190, primary="3A6FD8", accent=k["accent"])
    tile(deck, s, 768, 464, 464, 208, fill=k["ink"])
    deck.text(s, 808, 500, 400, 50, "2027 · 07", size=40, font=MISANS_SEMI, color="FFFFFF")
    deck.text(s, 808, 566, 400, 60, "126 家门店完成升级", size=22, font=MISANS, color="C7C7CC")


@example("recipes", "R16-b", "R16 便当格 · 数据页", "大格放图表，小格放结论数字和一句说明；每格只说一件事。", (MISANS_HEAVY,))
def r16_data(deck, s):
    k = R16
    bg(s, k["bg"])
    tile(deck, s, 48, 48, 784, 624)
    deck.text(s, 88, 80, 700, 50, "损耗率，2027 年 1–6 月", size=26, font=MISANS_SEMI, color=k["ink"])
    deck.line_chart(s, 70, 140, 740, 500, C.MONTHS, {"知野": C.LOSS, "同业": C.LOSS_PEERS}, colors=[k["accent"], "C7C7CC"],
                    number_format='0.0"%"', font=MISANS, size=16, axis_color=k["gray"], axis_line="E5E5EA", width=4,
                    min_value=4)
    tile(deck, s, 848, 48, 384, 300, fill=k["soft"])
    deck.text(s, 884, 80, 320, 30, "6 月损耗率", size=20, font=MISANS, color=k["accent"])
    deck.text(s, 884, 120, 320, 130, [[("5.9", {"size": 104, "font": MISANS_HEAVY}), ("%", {"size": 40, "font": MISANS_SEMI})]],
              color=k["accent"], font=MISANS)
    deck.text(s, 884, 270, 320, 40, "比 1 月 −3.7 个百分点", size=20, font=MISANS_SEMI, color=k["ink"])
    tile(deck, s, 848, 364, 384, 308)
    deck.icon(s, "calendar", 884, 400, size=40, color=k["ink"])
    deck.text(s, 884, 466, 320, 120, "3 月起按日订货，\n临期商品晚 8 点折扣", size=24, font=MISANS_SEMI, color=k["ink"],
              line_spacing=1.4)


@example("recipes", "R16-c", "R16 便当格 · 图片页", "照片格子圆角裁切、大小不一；一个深色文字格把三张照片串起来。", (MISANS_HEAVY,))
def r16_picture(deck, s):
    k = R16
    bg(s, k["bg"])
    deck.picture(s, treated("farm", "round_corners", ext="png", radius=56, size=(1100, 800)), 48, 48, 560, 408)
    deck.picture(s, treated("market-people", "round_corners", ext="png", radius=56, size=(1000, 800)), 624, 48, 296, 408)
    deck.picture(s, treated("potatoes", "round_corners", ext="png", radius=56, size=(600, 800)), 936, 48, 296, 408)
    tile(deck, s, 48, 472, 872, 200, fill=k["ink"])
    deck.text(s, 88, 506, 800, 60, "从地里到家里，不超过 18 小时", size=36, font=MISANS_HEAVY, color="FFFFFF")
    deck.text(s, 88, 576, 800, 60, "照片：~MVI~ (warped)、Wonderlane（CC BY 2.0），rawpixel（CC0）", size=15, font=MISANS,
              color="AEAEB2")
    tile(deck, s, 936, 472, 296, 200)
    deck.text(s, 968, 500, 240, 80, [[("5", {"size": 64, "font": MISANS_HEAVY}), (" 座", {"size": 24, "font": MISANS_SEMI})]],
              color=k["ink"], font=MISANS)
    deck.text(s, 970, 600, 240, 30, "城市仓", size=20, font=MISANS, color=k["gray"])


@example("recipes", "R16-d", "R16 便当格 · 特色页", "功能总览：六个格子、两种大小，图标统一；适合发布会的“一页看全”。", (MISANS_HEAVY,))
def r16_signature(deck, s):
    k = R16
    bg(s, k["bg"])
    feats = [(48, 48, 576, 300, "clock", "30 分钟", "下单到送达", True), (640, 48, 288, 300, "leaf", "5.9%", "损耗率", False),
             (944, 48, 288, 300, "store", "126", "家门店", False), (48, 364, 288, 308, "warehouse", "5 座", "城市仓", False),
             (352, 364, 288, 308, "repeat", "57%", "会员复购", False), (656, 364, 576, 308, "truck", "每日 3 趟", "补货到门店", False)]
    for x, y, w, h, icon, big, small, hot in feats:
        tile(deck, s, x, y, w, h, fill=k["accent"] if hot else None)
        deck.icon(s, icon, x + 32, y + 32, size=40, color="FFFFFF" if hot else k["accent"])
        deck.text(s, x + 32, y + h - 130, w - 64, 80, big, size=56, font=MISANS_HEAVY, color="FFFFFF" if hot else k["ink"])
        deck.text(s, x + 32, y + h - 52, w - 64, 30, small, size=19, font=MISANS, color="FFFFFF" if hot else k["gray"])


# ====================================================================== R17 formal report
R17 = dict(red="9E1B1B", gold="B8925A", ink="1A1A1A", gray="666666", light="FAF7F2")


def r17_header(deck, s, text, page):
    k = R17
    deck.rect(s, 80, 58, 8, 40, fill=k["red"])
    deck.text(s, 104, 54, 1000, 50, text, size=30, font=SERIF_BLACK, color=k["ink"])
    deck.rect(s, 80, 116, 1120, 1.5, fill=k["gold"])
    deck.text(s, 0, 680, 1280, 20, f"— {page} —", size=13, font=SERIF, color=k["gray"], align="center")


@example("recipes", "R17-a", "R17 政企庄重 · 封面", "上方深红色带配一道金线，宋体标题居中对称；单位与日期在下方居中。不使用政治符号。", (SERIF_BLACK,))
def r17_cover(deck, s):
    k = R17
    deck.rect(s, 0, 0, 1280, 150, fill=k["red"])
    deck.rect(s, 0, 156, 1280, 3, fill=k["gold"])
    deck.text(s, 0, 270, 1280, 80, "把产地搬进社区", size=60, font=SERIF_BLACK, color=k["ink"], align="center")
    deck.text(s, 0, 370, 1280, 40, "—— 知野生鲜 2027 年社区店升级工作汇报", size=26, font=SERIF, color=k["ink"], align="center")
    deck.text(s, 0, 540, 1280, 70, "知野生鲜运营中心\n2027 年 7 月", size=22, font=SERIF, color=k["gray"], align="center",
              line_spacing=1.6)
    deck.rect(s, 0, 680, 1280, 40, fill=k["red"])
    deck.rect(s, 0, 674, 1280, 2, fill=k["gold"])


@example("recipes", "R17-b", "R17 政企庄重 · 数据页", "统一页眉（红色竖条、宋体标题、金线）；图表用红色突出、其余灰；右侧编号写主要成效。", (SERIF_BLACK, SANS))
def r17_data(deck, s):
    k = R17
    r17_header(deck, s, "一、损耗率连续 6 个月下降", 3)
    deck.text(s, 80, 136, 700, 26, "生鲜损耗率，%，2027 年 1–6 月（虚构示例）", size=16, font=SANS, color=k["gray"])
    deck.bar_chart(s, 70, 170, 720, 480, C.MONTHS, C.LOSS, highlight={5}, horizontal=False, color=k["red"], base="C9C3B8",
                   number_format='0.0"%"', font=SANS, size=17, label_color=k["ink"], axis_color=k["ink"], gap_width=60)
    deck.rect(s, 840, 170, 360, 460, fill=k["light"], line=k["gold"], line_width=1)
    deck.text(s, 870, 190, 300, 34, "主要成效", size=22, font=SERIF_BLACK, color=k["red"])
    items = ["损耗率由 9.6% 降至 5.9%", "低于同城同业 3.2 个百分点", "3 月起降幅明显加快"]
    for i, text in enumerate(items):
        y = 250 + i * 110
        deck.ellipse(s, 886, y + 16, 16, fill=k["red"])
        deck.text(s, 870, y + 2, 32, 30, str(i + 1), size=18, font=SERIF_BLACK, color="FFFFFF", align="center")
        deck.text(s, 916, y, 270, 70, text, size=20, font=SANS, color=k["ink"], line_spacing=1.4)


@example("recipes", "R17-c", "R17 政企庄重 · 图片页", "照片配金色细框、居中对称；三组数字等宽排开，数字用红色宋体。", (SERIF_BLACK, SANS))
def r17_picture(deck, s):
    k = R17
    r17_header(deck, s, "二、从产地到社区的供应链", 4)
    deck.picture(s, photo("farm"), 104, 164, 520, 360)
    deck.rect(s, 96, 156, 536, 376, line=k["gold"], line_width=1.5)
    deck.text(s, 96, 544, 536, 22, "示意图片：~MVI~ (warped)，CC BY 2.0", size=13, font=SANS, color=k["gray"], align="center")
    for i, (num, unit, label) in enumerate(C.FACTS):
        y = 170 + i * 130
        deck.text(s, 700, y, 500, 70, [[(num, {"size": 56, "font": SERIF_BLACK, "color": k["red"]}),
                                        (" " + unit, {"size": 24, "font": SERIF, "color": k["ink"]})]])
        deck.text(s, 700, y + 72, 500, 30, label, size=19, font=SANS, color=k["gray"])
        deck.rect(s, 700, y + 116, 500, 1, fill=k["gold"])


@example("recipes", "R17-d", "R17 政企庄重 · 特色页", "汇报提纲：编号圆、金色引导点线、页码右对齐；正式、对称、好查找。", (SERIF_BLACK,))
def r17_signature(deck, s):
    k = R17
    deck.rect(s, 0, 0, 1280, 16, fill=k["red"])
    deck.text(s, 0, 80, 1280, 70, "汇报提纲", size=48, font=SERIF_BLACK, color=k["ink"], align="center")
    deck.rect(s, 560, 160, 160, 2, fill=k["gold"])
    items = [("升级工作总体情况", 3), ("损耗率下降的主要做法", 5), ("各城市进展与差距", 8), ("下半年工作安排", 11)]
    for i, (text, page) in enumerate(items):
        y = 220 + i * 100
        deck.ellipse(s, 300, y + 24, 24, fill=k["red"])
        deck.text(s, 276, y + 6, 48, 40, str(i + 1), size=24, font=SERIF_BLACK, color="FFFFFF", align="center")
        deck.text(s, 350, y + 4, 520, 44, text, size=28, font=SERIF, color=k["ink"])
        deck.line(s, 760, y + 34, 940, y + 34, color=k["gold"], width=1.5, dash=True)
        deck.text(s, 950, y + 4, 60, 44, str(page), size=28, font=SERIF, color=k["red"], align="right")


# ====================================================================== R18 notebook
R18 = dict(paper="FBF8F1", ink="2B2B2B", gray="77726A", yellow="FFE45C", red="E2553F", blue="3D7BD9")


def r18_bg(deck, s):
    deck.picture(s, generated("dots", size=(1280, 720), bg="FBF8F1", dot="D6CFC2", gap=28), 0, 0, 1280, 720)


def polaroid(deck, s, key, x, y, w, h, rotation, caption=None, source=None):
    k = R18
    deck.rect(s, x + 6, y + 8, w, h, fill="000000", alpha=0.12).rotation = rotation
    deck.rect(s, x, y, w, h, fill="FFFFFF").rotation = rotation
    pic = deck.picture(s, source or photo(key), x + 16, y + 16, w - 32, h - 76)
    pic.rotation = rotation
    if caption:
        deck.text(s, x + 16, y + h - 54, w - 32, 36, caption, size=20, font=KAI, color=k["ink"], align="center").rotation = rotation
    deck.rect(s, x + w / 2 - 60, y - 16, 120, 34, fill="F5D9A8", alpha=0.75).rotation = rotation - 4


def highlight(deck, s, x, y, w, h):
    deck.rect(s, x, y, w, h, fill=R18["yellow"], alpha=0.75, radius=6)


@example("recipes", "R18-a", "R18 手账笔记 · 封面", "点阵纸做底，关键词下面一道荧光笔；拍立得照片用胶带“贴”在页上，楷体写批注。", (SANS_BLACK, KAI))
def r18_cover(deck, s):
    k = R18
    r18_bg(deck, s)
    highlight(deck, s, 76, 330, 330, 70)
    deck.text(s, 80, 180, 700, 260, "把产地\n搬进社区", size=96, font=SANS_BLACK, color=k["ink"], line_spacing=1.1)
    deck.text(s, 84, 470, 520, 40, "2027 年 7 月 · 半年小结", size=28, font=KAI, color=k["red"])
    deck.polygon(s, [(84, 516), (200, 512), (330, 518), (420, 512)], line=k["red"], line_width=3, closed=False)
    polaroid(deck, s, "tomato-picking", 760, 130, 400, 400, 4, caption="早上摘的菜")


@example("recipes", "R18-b", "R18 手账笔记 · 数据页", "图表照常是原生的，批注是手写感：圈出最后一根，箭头指过去，写一句人话。", (SANS, KAI))
def r18_data(deck, s):
    k = R18
    r18_bg(deck, s)
    highlight(deck, s, 76, 96, 250, 50)
    deck.text(s, 80, 80, 1000, 70, "损耗率 · 1–6 月", size=40, font=SANS, bold=True, color=k["ink"])
    deck.bar_chart(s, 70, 170, 820, 470, C.MONTHS, C.LOSS, highlight={5}, horizontal=False, color=k["blue"], base="C9C2B4",
                   number_format='0.0"%"', font=SANS, size=17, label_color=k["ink"], axis_color=k["ink"], gap_width=55)
    deck.ellipse(s, 816, 520, 62, ry=150, line=k["red"], line_width=3).rotation = 6
    deck.text(s, 930, 240, 300, 120, "降到 5.9% 了！\n比 1 月少扔近四成", size=28, font=KAI, color=k["red"], line_spacing=1.4)
    deck.polygon(s, [(960, 360), (930, 410), (890, 440)], line=k["red"], line_width=3, closed=False)
    deck.polygon(s, [(880, 446), (902, 428), (896, 452)], fill=k["red"])
    deck.text(s, 930, 560, 300, 60, "（数据为虚构示例）", size=16, font=KAI, color=k["gray"])


@example("recipes", "R18-c", "R18 手账笔记 · 图片页", "两张拍立得斜着贴，各写一句楷体图注；右边是带勾的清单。", (SANS, KAI))
def r18_picture(deck, s):
    k = R18
    r18_bg(deck, s)
    polaroid(deck, s, "farm", 70, 120, 360, 380, -4, caption="产地 · 清晨")
    polaroid(deck, s, "potatoes", 400, 200, 330, 380, 5, caption="第二天进店")
    deck.text(s, 800, 120, 420, 60, "从地里到家里", size=36, font=SANS, bold=True, color=k["ink"])
    for i, (num, unit, label) in enumerate(C.FACTS):
        y = 220 + i * 100
        deck.icon(s, "circle-check", 800, y + 6, size=34, color=k["red"])
        deck.text(s, 850, y, 380, 50, f"{num} {unit} {label}", size=26, font=KAI, color=k["ink"])
    deck.text(s, 70, 650, 700, 20, "照片：~MVI~ (warped)，CC BY 2.0；rawpixel，CC0", size=12, font=SANS, color=k["gray"])


@example("recipes", "R18-d", "R18 手账笔记 · 特色页", "下半年待办：方框打勾、便利贴、页边小涂鸦；适合内部工作坊和复盘。", (KAI,))
def r18_signature(deck, s):
    k = R18
    r18_bg(deck, s)
    highlight(deck, s, 76, 92, 300, 52)
    deck.text(s, 80, 76, 700, 70, "下半年 To-do", size=44, font=KAI, color=k["ink"])
    todo = [("合肥城市仓选址（周牧，11 月底）", False), ("会员体系上线（林岚，12 月）", False),
            ("损耗看板接入全部门店（许安，12 月中）", False), ("126 家门店完成升级", True)]
    for i, (text, done) in enumerate(todo):
        y = 200 + i * 96
        deck.rect(s, 90, y, 34, 34, line=k["ink"], line_width=2.5, radius=4)
        if done:
            deck.polygon(s, [(96, y + 16), (106, y + 28), (128, y - 4)], line=k["red"], line_width=4, closed=False)
        deck.text(s, 150, y - 4, 640, 44, text, size=28, font=KAI, color=k["gray"] if done else k["ink"])
    deck.rect(s, 880, 190, 300, 260, fill="FFE98A").rotation = 3
    deck.text(s, 905, 220, 250, 200, "别忘了：\n合肥、无锡还没有城市仓，送达慢 5 分钟", size=24, font=KAI, color=k["ink"],
              line_spacing=1.5).rotation = 3
    deck.icon(s, "map-pin", 1110, 520, size=60, color=k["blue"], stroke=1.6)


# ====================================================================== R19 riso print
R19 = dict(paper="F4EFE6", pink="FF48B0", blue="0078BF", ink="1F2A44")


def r19_paper(deck, s):
    bg(s, R19["paper"])


def r19_grain(deck, s):
    deck.picture(s, generated("grain", size=(1280, 720), amount=0.07, seed=11), 0, 0, 1280, 720)


def misprint(deck, s, x, y, w, h, text, size, dx=7, dy=5, **kw):
    deck.text(s, x + dx, y + dy, w, h, text, size=size, font=QINGKE, color=R19["pink"], **kw)
    deck.text(s, x, y, w, h, text, size=size, font=QINGKE, color=R19["blue"], **kw)


@example("recipes", "R19-a", "R19 复古印刷 · 封面", "只用两种油墨（荧光粉、蓝）：标题错版叠印、半调网点、叠色圆，再加一层纸张颗粒。", (QINGKE,))
def r19_cover(deck, s):
    k = R19
    r19_paper(deck, s)
    deck.picture(s, generated("halftone", size=(1280, 720), colour="FF48B0", gap=16, max_r=6), 0, 0, 1280, 720)
    deck.ellipse(s, 1000, 300, 220, fill=k["blue"], alpha=0.85)
    deck.ellipse(s, 860, 470, 180, fill=k["pink"], alpha=0.8)
    misprint(deck, s, 80, 140, 900, 330, "把产地\n搬进社区", 128, line_spacing=1.05)
    deck.text(s, 84, 500, 600, 40, C.COVER_SUB, size=24, font=SANS_MED, color=k["ink"])
    r19_grain(deck, s)


@example("recipes", "R19-b", "R19 复古印刷 · 数据页", "柱子用一种油墨，重点用另一种；标题错版；颗粒让平涂色块有纸感。", (QINGKE, SANS_MED))
def r19_data(deck, s):
    k = R19
    r19_paper(deck, s)
    misprint(deck, s, 80, 60, 1100, 90, "损耗率连降 6 个月", 64, dx=5, dy=4)
    deck.bar_chart(s, 70, 180, 820, 460, C.MONTHS, C.LOSS, highlight={5}, horizontal=False, color=k["blue"], base=k["pink"],
                   number_format='0.0"%"', font=SANS_MED, size=18, label_color=k["ink"], axis_color=k["ink"], gap_width=40)
    deck.ellipse(s, 1060, 380, 130, fill=k["blue"], alpha=0.9)
    deck.text(s, 930, 334, 260, 100, "−3.7", size=64, font="Archivo Black", ea=SANS_MED, color=k["paper"], align="center")
    deck.text(s, 930, 410, 260, 40, "个百分点", size=22, font=SANS_MED, color=k["paper"], align="center")
    r19_grain(deck, s)


@example("recipes", "R19-c", "R19 复古印刷 · 图片页", "照片转成蓝色双色调，像两色印刷；粉色色块叠在一角，文字压在纸面上。", (QINGKE, SANS_MED))
def r19_picture(deck, s):
    k = R19
    r19_paper(deck, s)
    deck.picture(s, treated("squash", "duotone", dark="0078BF", light="F4EFE6"), 480, 60, 720, 520)
    deck.rect(s, 420, 440, 260, 200, fill=k["pink"], alpha=0.85)
    misprint(deck, s, 80, 140, 420, 260, "颜色最鲜\n就上架", 76, dx=5, dy=4, line_spacing=1.1)
    deck.text(s, 84, 420, 320, 90, "30 分钟送达\n126 家门店 · 5 座城市仓", size=22, font=SANS_MED, color=k["ink"], line_spacing=1.6)
    deck.text(s, 480, 600, 720, 20, "照片：USDA，公有领域，已做双色调", size=13, font=SANS, color=k["ink"], align="right")
    r19_grain(deck, s)


@example("recipes", "R19-d", "R19 复古印刷 · 特色页", "海报式：两个叠色大圆、一个巨大的错版数字、半调网点从一侧渐变。", (QINGKE,))
def r19_signature(deck, s):
    k = R19
    r19_paper(deck, s)
    deck.picture(s, generated("halftone", size=(1280, 720), colour="0078BF", gap=14, max_r=5), 0, 0, 1280, 720)
    deck.ellipse(s, 470, 380, 260, fill=k["pink"], alpha=0.85)
    deck.ellipse(s, 740, 340, 230, fill=k["blue"], alpha=0.8)
    misprint(deck, s, 300, 150, 700, 420, "30", 380, dx=10, dy=8, align="center", wrap=False)
    misprint(deck, s, 80, 70, 600, 80, "下单到送达", 56, dx=4, dy=3)
    deck.text(s, 80, 590, 400, 70, "分钟", size=60, font=QINGKE, color=k["ink"])
    r19_grain(deck, s)


# ====================================================================== R20 colour fields
# Added after DSH runs kept choosing warm paper + ink + one red: a recipe that starts from saturated flat
# colour fields instead of a paper tone.
R20 = dict(field="0E5E4E", mint="D8EEE6", coral="C9442D", ink="0F1F1A", gray="3F5550", on_field="CFE8DF",
           white="FFFFFF", bar="9CC9BB")


@example("recipes", "R20-a", "R20 色块分区 · 封面", "整页切成两块：一大块饱和的平涂色压着白色大标题，另一块白底只放一个超大数字。", (HOS,))
def r20_cover(deck, s):
    k = R20
    bg(s, k["white"])
    deck.rect(s, 0, 0, 760, 720, fill=k["field"])
    deck.text(s, 80, 80, 600, 26, "知野生鲜 · 2027", size=18, font=HOS, color=k["on_field"], spacing=0.08)
    deck.text(s, 80, 190, 640, 260, "把产地\n搬进社区", size=96, font=HOS, bold=True, color=k["white"], line_spacing=1.08)
    deck.text(s, 82, 470, 600, 36, C.COVER_SUB, size=24, font=HOS, color=k["on_field"])
    deck.text(s, 820, 170, 420, 240, "126", size=200, font=HOS, bold=True, color=k["field"], wrap=False)
    deck.text(s, 828, 410, 400, 36, "家社区店完成升级", size=26, font=HOS, color=k["ink"])
    deck.rect(s, 830, 470, 80, 10, fill=k["coral"])
    deck.text(s, 828, 640, 400, 24, "2027 年 7 月 · 虚构示例", size=16, font=HOS, color=k["gray"])


@example("recipes", "R20-b", "R20 色块分区 · 数据页", "色块做页眉压住标题；图表用同一种绿的深浅，只有结论数字用整块主色。", (HOS,))
def r20_data(deck, s):
    k = R20
    bg(s, k["white"])
    deck.rect(s, 0, 0, 1280, 150, fill=k["field"])
    deck.text(s, 80, 40, 1100, 56, "损耗率连续 6 个月下降", size=40, font=HOS, bold=True, color=k["white"])
    deck.text(s, 82, 100, 900, 28, "生鲜损耗率，%，2027 年 1–6 月（虚构示例）", size=18, font=HOS, color=k["on_field"])
    deck.bar_chart(s, 70, 190, 780, 450, C.MONTHS, C.LOSS, highlight={5}, horizontal=False, color=k["field"],
                   base=k["bar"], number_format='0.0"%"', font=HOS, size=18, label_color=k["ink"], axis_color=k["gray"],
                   gap_width=45)
    deck.rect(s, 900, 190, 300, 300, fill=k["field"])
    deck.text(s, 930, 220, 260, 30, "6 月", size=22, font=HOS, color=k["on_field"])
    deck.text(s, 926, 270, 260, 130, [[("5.9", {"size": 104, "bold": True}), ("%", {"size": 40, "bold": True})]],
              font=HOS, color=k["white"], wrap=False)
    deck.text(s, 930, 410, 250, 60, "比 1 月低 3.7 个百分点", size=20, font=HOS, color=k["on_field"])
    deck.rect(s, 900, 520, 80, 10, fill=k["coral"])
    deck.text(s, 900, 548, 300, 80, "3 月起按日订货，\n临期商品晚 8 点折扣", size=20, font=HOS, color=k["ink"], line_spacing=1.4)


@example("recipes", "R20-c", "R20 色块分区 · 图片页", "照片占半页出血，另一半是整块主色，白字写一句话和三个数字。", (HOS,))
def r20_picture(deck, s):
    k = R20
    deck.picture(s, photo("farm"), 560, 0, 720, 720)
    deck.rect(s, 0, 0, 560, 720, fill=k["field"])
    deck.text(s, 64, 110, 460, 160, "清晨采摘，\n当天进城", size=56, font=HOS, bold=True, color=k["white"], line_spacing=1.15)
    for i, (num, unit, label) in enumerate(C.FACTS):
        y = 330 + i * 96
        deck.rect(s, 64, y, 432, 1, fill=k["on_field"])
        deck.text(s, 64, y + 14, 220, 70, [[(num, {"size": 52, "bold": True}), (" " + unit, {"size": 22})]],
                  font=HOS, color=k["white"], wrap=False)
        deck.text(s, 280, y + 34, 220, 30, label, size=20, font=HOS, color=k["on_field"])
    deck.text(s, 64, 670, 460, 22, "照片：~MVI~ (warped)，CC BY 2.0（示意）", size=13, font=HOS, color=k["on_field"])


@example("recipes", "R20-d", "R20 色块分区 · 特色页", "四宫格成绩单：四块不同的平涂色各放一个数字，颜色本身就是分组。", (HOS,))
def r20_signature(deck, s):
    k = R20
    cells = [(0, 0, k["field"], k["white"], k["on_field"]), (640, 0, k["mint"], k["field"], k["gray"]),
             (0, 360, k["coral"], k["white"], k["white"]), (640, 360, k["white"], k["field"], k["gray"])]
    for (x, y, fill, big, small), (num, unit, label, icon) in zip(cells, C.KPIS):
        deck.rect(s, x, y, 640, 360, fill=fill)
        deck.icon(s, icon, x + 64, y + 56, size=44, color=big, stroke=2.0)
        deck.text(s, x + 60, y + 120, 560, 150, [[(num, {"size": 128, "bold": True}), (" " + unit, {"size": 40, "bold": True})]],
                  font=HOS, color=big, wrap=False)
        deck.text(s, x + 64, y + 280, 540, 34, label, size=24, font=HOS, color=small)
    deck.text(s, 1000, 64, 220, 26, "上半年成绩单", size=18, font=HOS, color=k["gray"], align="right")


# ====================================================================== R21 cool and airy
R21 = dict(bg="F5F8FB", card="FFFFFF", ink="1E2A4A", gray="4A5875", line="DCE3EE", mint="DDF3EC", sky="DDEBFB",
           lilac="E9E5FA", accent="3B5BDB", green="12B886")


@example("recipes", "R21-a", "R21 清透柔和 · 封面", "冷白底上几团浅薄荷、浅天蓝、浅紫的圆形色块托着一张插画；深靛蓝字，轻、干净、友好。", (MISANS_HEAVY,))
def r21_cover(deck, s):
    k = R21
    bg(s, k["bg"])
    deck.ellipse(s, 990, 300, 230, fill=k["sky"])
    deck.ellipse(s, 1150, 520, 140, fill=k["mint"])
    deck.ellipse(s, 840, 540, 100, fill=k["lilac"])
    deck.illustration(s, "store", 810, 250, 380, 285, primary=k["accent"], accent=k["green"])
    deck.text(s, 80, 190, 680, 240, "把产地\n搬进社区", size=84, font=MISANS_HEAVY, color=k["ink"], line_spacing=1.1)
    deck.text(s, 84, 430, 620, 36, C.COVER_SUB, size=24, font=MISANS, color=k["gray"])
    deck.rect(s, 84, 500, 220, 40, fill=k["card"], line=k["line"], radius=20)
    deck.text(s, 84, 510, 220, 24, "2027 · 虚构示例", size=16, font=MISANS, color=k["gray"], align="center")


@example("recipes", "R21-b", "R21 清透柔和 · 数据页", "白色圆角卡片放图表，右侧三张浅色小卡各放一个前后对比；只用一种靛蓝做强调。", (MISANS_HEAVY,))
def r21_data(deck, s):
    k = R21
    bg(s, k["bg"])
    deck.text(s, 80, 50, 1100, 60, "损耗率半年降到 5.9%", size=40, font=MISANS_HEAVY, color=k["ink"])
    deck.text(s, 82, 112, 900, 28, "生鲜损耗率，%，2027 年 1–6 月（虚构示例）", size=18, font=MISANS, color=k["gray"])
    deck.rect(s, 80, 168, 760, 480, fill=k["card"], radius=24)
    deck.line_chart(s, 100, 188, 720, 440, C.MONTHS, {"知野": C.LOSS, "同城同业": C.LOSS_PEERS}, colors=[k["accent"], "AEB9CC"],
                    number_format='0.0"%"', font=MISANS, size=16, label_color=k["gray"], axis_color=k["gray"],
                    axis_line=k["line"], grid="EEF2F7", label_bg=k["card"], width=3.5, min_value=4)
    icons = ["clock", "leaf", "repeat"]
    for i, ((name, before, after), fill, icon) in enumerate(zip(C.BEFORE_AFTER, (k["mint"], k["sky"], k["lilac"]), icons)):
        y = 168 + i * 168
        deck.rect(s, 880, y, 320, 144, fill=fill, radius=24)
        deck.ellipse(s, 930, y + 50, 26, fill=k["card"])
        deck.icon(s, icon, 916, y + 36, size=28, color=k["accent"], stroke=2.0)
        deck.text(s, 976, y + 22, 210, 54, after, size=36, font=MISANS_HEAVY, color=k["ink"], wrap=False)
        deck.text(s, 976, y + 84, 210, 44, f"{name}\n原来 {before}", size=16, font=MISANS, color=k["gray"], line_spacing=1.3)


@example("recipes", "R21-c", "R21 清透柔和 · 图片页", "照片做大圆角放在浅色卡片里，旁边三张浅色小卡写数字；没有阴影，靠浅色块分组。", (MISANS_HEAVY,))
def r21_picture(deck, s):
    k = R21
    bg(s, k["bg"])
    deck.rect(s, 64, 64, 652, 560, fill=k["sky"], radius=36)
    deck.picture(s, treated("market-people", "round_corners", ext="png", radius=48, size=(1200, 900)), 96, 96, 588, 441)
    deck.text(s, 96, 560, 588, 24, "社区菜市场（示意图片）。照片：Wonderlane，CC BY 2.0", size=14, font=MISANS, color=k["gray"])
    deck.text(s, 770, 96, 450, 60, "社区店里的早市", size=40, font=MISANS_HEAVY, color=k["ink"])
    deck.text(s, 772, 160, 440, 70, "“" + C.QUOTE + "”", size=22, font=MISANS, color=k["gray"], line_spacing=1.4)
    for i, ((num, unit, label), fill) in enumerate(zip(C.FACTS, (k["mint"], k["lilac"], k["card"]))):
        y = 262 + i * 122
        deck.rect(s, 770, y, 430, 104, fill=fill, line=k["line"] if fill == k["card"] else None, radius=24)
        deck.text(s, 800, y + 18, 200, 70, [[(num, {"size": 48, "font": MISANS_HEAVY}), (" " + unit, {"size": 22})]],
                  font=MISANS, color=k["ink"], wrap=False)
        deck.text(s, 990, y + 40, 200, 30, label, size=20, font=MISANS, color=k["gray"])


@example("recipes", "R21-d", "R21 清透柔和 · 特色页", "像手机 App 的引导页：五张浅色卡片一字排开，每张一个编号、一个图标、一句话。", (MISANS_HEAVY,))
def r21_signature(deck, s):
    k = R21
    bg(s, k["bg"])
    deck.text(s, 80, 60, 1100, 60, "从地里到家里，五站", size=40, font=MISANS_HEAVY, color=k["ink"])
    icons = {"farm": "leaf", "truck": "truck", "warehouse": "warehouse", "store": "store", "person": "house"}
    fills = (k["mint"], k["sky"], k["lilac"], k["mint"], k["sky"])
    for i, ((ill, name, text), fill) in enumerate(zip(C.STEPS, fills)):
        x = 80 + i * 228
        deck.rect(s, x, 170, 208, 400, fill=fill, radius=28)
        deck.rect(s, x + 24, 194, 56, 32, fill=k["card"], radius=16)
        deck.text(s, x + 24, 200, 56, 22, f"{i + 1:02d}", size=16, font=MISANS_HEAVY, color=k["accent"], align="center")
        deck.ellipse(s, x + 104, 320, 48, fill=k["card"])
        deck.icon(s, icons[ill], x + 82, 298, size=44, color=k["accent"], stroke=2.0)
        deck.text(s, x + 20, 410, 168, 36, name, size=24, font=MISANS_HEAVY, color=k["ink"], align="center")
        deck.text(s, x + 20, 456, 168, 60, text, size=18, font=MISANS, color=k["gray"], align="center", line_spacing=1.35)
    deck.text(s, 80, 610, 1120, 28, "全程不超过 18 小时（虚构示例）", size=18, font=MISANS, color=k["gray"])