"""Style recipe examples R01-R07. Every recipe draws the same three pages (a cover, b data, c picture) from
content.py, plus one page (d) that shows what is special about it. Fictional content."""
import content as C
from gallery import bg, crop, example, generated, photo, treated

SANS, SANS_BLACK, SANS_MED = "Noto Sans SC", "Noto Sans SC Black", "Noto Sans SC Medium"
SERIF, SERIF_BLACK, SERIF_SEMI = "Noto Serif SC", "Noto Serif SC Black", "Noto Serif SC SemiBold"
INTER, INTER_BLACK = "Inter", "Inter Black"
DATA_TITLE = "损耗率连续 6 个月下降，6 月降到 5.9%"


def facts_plain(deck, s, x, y, gap, num_font, num_size, num_color, unit_color, label_font, label_color, first=None,
                ea=SANS, label_size=18):
    for i, (num, unit, label) in enumerate(C.FACTS):
        yy = y + i * gap
        deck.text(s, x, yy, 420, num_size * 1.2, [[(num, {"size": num_size, "font": num_font, "ea": ea,
                                                         "color": first if (first and i == 0) else num_color}),
                                                   (" " + unit, {"size": num_size * 0.36, "font": label_font,
                                                                 "color": unit_color, "bold": True})]], wrap=False)
        deck.text(s, x, yy + num_size * 1.12, 420, 30, label, size=label_size, font=label_font, color=label_color)


# ====================================================================== R01 Swiss editorial grid
R1 = dict(bg="F4F4F0", ink="111111", gray="5C5C5C", rule="CFCFC8", red="E4002B")


def swiss_head(deck, s, mid, num):
    k = R1
    deck.rect(s, 72, 40, 1136, 2, fill=k["ink"])
    deck.text(s, 72, 52, 300, 20, f"{num}  知野生鲜", size=13, font=SANS, color=k["ink"])
    deck.text(s, 72 + 4 * 96.7, 52, 300, 20, mid, size=13, font=SANS, color=k["ink"])
    deck.text(s, 908, 52, 300, 20, "2027 · 07", size=13, font=INTER, color=k["ink"], align="right")


@example("recipes", "R01-a", "R1 瑞士编辑网格 · 封面", "超大黑体贴网格左对齐；唯一的红色给年份，并让它从页边裁出。", (SANS_BLACK, INTER))
def r1_cover(deck, s):
    k = R1
    bg(s, k["bg"])
    swiss_head(deck, s, "社区店升级计划", "01")
    deck.text(s, 64, 120, 900, 340, "把产地\n搬进社区", size=150, font=SANS_BLACK, color=k["ink"], line_spacing=1.0)
    deck.text(s, 72, 470, 520, 70, "知野生鲜 2027 社区店升级计划\n半年回顾与下一步", size=20, font=SANS, color=k["gray"],
              line_spacing=1.5)
    deck.text(s, 650, 470, 720, 300, "2027", size=250, font=INTER_BLACK, color=k["red"], wrap=False)


@example("recipes", "R01-b", "R1 瑞士编辑网格 · 数据页", "细线、灰阶和一个红色；图表挂在网格上，结论数字在右侧单独成列。", (SANS, INTER))
def r1_data(deck, s):
    k = R1
    bg(s, k["bg"])
    swiss_head(deck, s, "经营数据", "02")
    deck.text(s, 72, 96, 760, 130, "损耗率连续 6 个月下降，\n6 月降到 5.9%", size=44, font=SANS, bold=True, color=k["ink"],
              line_spacing=1.2)
    deck.text(s, 72, 232, 600, 24, "生鲜损耗率，%，2027 年 1–6 月（虚构示例）", size=17, font=SANS, color=k["gray"])
    deck.bar_chart(s, 66, 280, 760, 370, C.MONTHS, C.LOSS, highlight={5}, horizontal=False, color=k["red"],
                   base="A8A8A2", number_format="0.0", font=INTER, size=16, label_color=k["ink"], axis_color=k["ink"],
                   gap_width=40)
    deck.rect(s, 880, 280, 328, 2, fill=k["ink"])
    deck.text(s, 880, 296, 328, 130, "−3.7", size=110, font=INTER_BLACK, color=k["red"], ea=SANS)
    deck.text(s, 884, 430, 320, 60, "个百分点\n1 月 9.6% → 6 月 5.9%", size=17, font=SANS, color=k["ink"], line_spacing=1.5)
    deck.rect(s, 880, 520, 328, 1, fill=k["rule"])
    deck.text(s, 884, 534, 320, 60, "3 月起按日订货，\n临期商品晚 8 点折扣", size=16, font=SANS, color=k["gray"], line_spacing=1.5)


@example("recipes", "R01-c", "R1 瑞士编辑网格 · 图片页", "黑白高对比照片占 8 栏、硬边；数字在左侧纵列，用细线分隔。", (SANS, INTER_BLACK))
def r1_picture(deck, s):
    k = R1
    bg(s, k["bg"])
    swiss_head(deck, s, "从地里到家里", "03")
    deck.picture(s, treated("farm", "gray", contrast=1.35), 560, 96, 648, 560)
    deck.text(s, 72, 96, 440, 50, "从地里到家里", size=32, font=SANS, bold=True, color=k["ink"])
    for i, (num, unit, label) in enumerate(C.FACTS):
        y = 200 + i * 150
        deck.rect(s, 72, y, 440, 2 if i == 0 else 1, fill=k["ink"] if i == 0 else k["rule"])
        deck.text(s, 72, y + 12, 440, 90, [[(num, {"size": 76, "font": INTER_BLACK, "ea": SANS,
                                                    "color": k["red"] if i == 0 else k["ink"]}),
                                            (" " + unit, {"size": 24, "font": SANS, "bold": True, "color": k["ink"]})]])
        deck.text(s, 72, y + 104, 440, 26, label, size=16, font=SANS, color=k["gray"])
    deck.text(s, 560, 664, 648, 20, "照片：~MVI~ (warped)，CC BY 2.0，已转黑白", size=12, font=SANS, color=k["gray"],
              align="right")


@example("recipes", "R01-d", "R1 瑞士编辑网格 · 特色页", "网格本身成为画面：超大数字出血，注释极小、挂在栏线上。", (SANS, INTER_BLACK))
def r1_signature(deck, s):
    k = R1
    bg(s, k["bg"])
    for i in range(13):
        x = 72 + i * (1136 + 24) / 12 - (24 if i == 12 else 0)
        deck.rect(s, x, 0, 1, 720, fill="E2E2DC")
    swiss_head(deck, s, "一个数字", "04")
    deck.text(s, -40, 110, 1100, 420, "5.9%", size=380, font=INTER_BLACK, color=k["red"], wrap=False, ea=SANS)
    deck.text(s, 72, 600, 250, 60, "生鲜损耗率\n2027 年 6 月", size=16, font=SANS, color=k["ink"], line_spacing=1.5)
    deck.text(s, 72 + 3 * 96.7, 600, 250, 60, "1 月\n9.6%", size=16, font=INTER, color=k["gray"], line_spacing=1.5, ea=SANS)
    deck.text(s, 72 + 6 * 96.7, 600, 250, 60, "同城同业\n9.1%", size=16, font=INTER, color=k["gray"], line_spacing=1.5,
              ea=SANS)
    deck.text(s, 72 + 9 * 96.7, 600, 300, 60, "差距\n3.2 个百分点", size=16, font=SANS, color=k["ink"], line_spacing=1.5)


# ====================================================================== R02 dark launch
R2 = dict(bg="050506", panel="16161A", text="F5F5F7", gray="86868B", acc="FF6A2B")
HOS, HOS_BLACK = "HarmonyOS Sans SC", "HarmonyOS Sans SC Black"


@example("recipes", "R02-a", "R2 暗场发布会 · 封面", "黑底只给主角打光：产品（这里是 App）配一团橙色柔光，标题极简。", (HOS_BLACK,))
def r2_cover(deck, s):
    k = R2
    deck.picture(s, generated("glow", size=(1280, 720), colors=("FF6A2B",), bg="050506", spots=[(0.72, 0.52, 0.26)],
                              strength=0.5), 0, 0, 1280, 720)
    deck.illustration(s, "phone", 600, 130, 600, 450, primary="FF6A2B", accent="FFC145", ink="2B2B30", surface="2A2A30",
                      line="3A3A40", tokens={"primary_light": "3A2418", "accent_light": "4A3A1C"})
    deck.text(s, 80, 230, 560, 220, "把产地\n搬进社区", size=88, font=HOS_BLACK, color=k["text"], line_spacing=1.05)
    deck.text(s, 84, 470, 520, 40, "知野 App · 30 分钟送达", size=24, font=HOS, color=k["gray"])


@example("recipes", "R02-b", "R2 暗场发布会 · 数据页", "一页一个数：巨大的白色数字配小号灰色单位，下面一条极细的趋势线。", (HOS, INTER))
def r2_data(deck, s):
    k = R2
    bg(s, k["bg"])
    deck.text(s, 0, 110, 1280, 30, "生鲜损耗率 · 2027 年 6 月", size=20, font=HOS, color=k["gray"], align="center")
    deck.text(s, 0, 150, 1280, 260, [[("5.9", {"size": 230, "font": INTER_BLACK, "color": k["text"]}),
                                      ("%", {"size": 80, "font": INTER, "color": k["gray"]})]], align="center", ea=HOS)
    deck.text(s, 0, 420, 1280, 40, "半年降了 3.7 个百分点", size=30, font=HOS, bold=True, color=k["acc"], align="center")
    deck.line_chart(s, 340, 480, 600, 170, C.MONTHS, {"损耗率": C.LOSS}, colors=[k["acc"]], labels=None, font=HOS,
                    size=16, axis_color=k["gray"], axis_line="2A2A30", width=3, min_value=4)


@example("recipes", "R02-c", "R2 暗场发布会 · 图片页", "暗调照片做背景，一句话配一张图；其余事实压成一行小字。", (HOS_BLACK,))
def r2_picture(deck, s):
    k = R2
    bg(s, k["bg"])
    deck.picture(s, treated("potatoes", "darken", amount=0.25), 520, 0, 760, 720)
    deck.gradient_rect(s, 516, 0, 420, 720, [(0, "050506", 1), (1, "050506", 0)])
    deck.text(s, 80, 240, 560, 220, "土豆出地，\n第二天进店。", size=68, font=HOS_BLACK, color=k["text"], line_spacing=1.15)
    deck.text(s, 84, 480, 600, 30, "30 分钟送达  ·  126 家门店  ·  5 座城市仓", size=20, font=HOS, color=k["gray"])
    deck.text(s, 900, 690, 360, 20, "照片：rawpixel，CC0", size=12, font=HOS, color="5A5A60", align="right")


@example("recipes", "R02-d", "R2 暗场发布会 · 特色页", "关键句逐步揭示：已讲过的句子压暗，正在讲的一句最亮；静态稿保留全部文字。", (HOS_BLACK,))
def r2_signature(deck, s):
    k = R2
    bg(s, k["bg"])
    lines = [("清晨，在地里采摘。", "3A3A40"), ("中午，在城市仓分拣。", "3A3A40")]
    for i, (text, colour) in enumerate(lines):
        deck.text(s, 120, 150 + i * 140, 1040, 110, text, size=72, font=HOS_BLACK, color=colour)
    deck.text(s, 120, 430, 1040, 110, [[("下单 ", {}), ("30 分钟", {"color": k["acc"]}), ("，送到家。", {})]], size=72,
              font=HOS_BLACK, color=k["text"])
    for i in range(3):
        deck.ellipse(s, 600 + i * 30, 640, 6, fill=k["text"] if i == 2 else "3A3A40")


# ====================================================================== R03 data journalism
R3 = dict(bg="FBF9F4", ink="1A1A1A", gray="666158", grid="E2DED5", red="D7263D", blue="0F4C81")


def r3_mark(deck, s, y=72):
    deck.rect(s, 80, y, 48, 6, fill=R3["red"])


@example("recipes", "R03-a", "R3 数据新闻 · 封面", "像报纸专题的刊头：短色块、宋体标题、导语；底部用真实数据画一条线做主视觉。", (SERIF, SANS))
def r3_cover(deck, s):
    k = R3
    bg(s, k["bg"])
    r3_mark(deck, s, 96)
    deck.text(s, 80, 112, 600, 26, "知野生鲜 · 经营专题", size=16, font=SANS, color=k["gray"])
    deck.text(s, 80, 150, 1000, 110, "把产地搬进社区", size=80, font=SERIF, bold=True, color=k["ink"])
    deck.text(s, 80, 270, 900, 80, "半年里，一家社区生鲜连锁把损耗率从 9.6% 降到 5.9%。\n我们把这 3.7 个百分点拆开来看。", size=22,
              font=SANS, color=k["ink"], line_spacing=1.6)
    deck.text(s, 80, 372, 600, 22, "2027 年 7 月 · 虚构示例", size=16, font=SANS, color=k["gray"])
    deck.text(s, 80, 428, 600, 26, "月订单，1 月 18 万单 → 6 月 36 万单", size=17, font=SANS, color=k["gray"])
    deck.line_chart(s, 70, 456, 1140, 210, C.MONTHS, {"月订单": C.ORDERS}, colors=[k["red"]], labels="last",
                    number_format='0" 万单"', font=SANS, size=17, axis_color=k["gray"], axis_line=k["grid"], width=4,
                    min_value=0)


@example("recipes", "R03-b", "R3 数据新闻 · 数据页", "标题就是结论；灰色衬托唯一的红线；注释直接写在图上；底部写来源。", (SERIF, SANS))
def r3_data(deck, s):
    k = R3
    bg(s, k["bg"])
    r3_mark(deck, s)
    deck.text(s, 80, 88, 1000, 60, "损耗率连续下降，已比同城同业低 3.2 个百分点", size=36, font=SERIF, bold=True, color=k["ink"])
    deck.text(s, 80, 146, 800, 26, "生鲜损耗率，%，2027 年 1–6 月", size=17, font=SANS, color=k["gray"])
    deck.line_chart(s, 70, 190, 960, 440, C.MONTHS, {"知野生鲜": C.LOSS, "同城同业": C.LOSS_PEERS},
                    colors=[k["red"], "A39E93"], number_format='0.0"%"', font=SANS, size=16, grid=k["grid"],
                    label_bg=k["bg"], width=3.5)
    deck.text(s, 1050, 236, 200, 30, "同城同业", size=17, font=SANS, color=k["gray"])
    deck.text(s, 1050, 386, 200, 30, "知野生鲜", size=17, font=SANS, bold=True, color=k["red"])
    deck.line(s, 502, 322, 502, 430, color=k["ink"], width=1)
    deck.ellipse(s, 502, 322, 4, fill=k["ink"])
    deck.text(s, 510, 424, 260, 50, "3 月：按日订货\n全面执行", size=16, font=SANS, color=k["ink"], line_spacing=1.4)
    deck.text(s, 80, 664, 900, 22, "来源：知野生鲜经营数据；同城同业为三家公开披露数据的均值（均为虚构示例）", size=13, font=SANS,
              color=k["gray"])


@example("recipes", "R03-c", "R3 数据新闻 · 图片页", "照片像新闻配图：占 7 栏，图注写清是示意；关键数字在侧栏。", (SERIF, SANS))
def r3_picture(deck, s):
    k = R3
    bg(s, k["bg"])
    r3_mark(deck, s)
    deck.text(s, 80, 88, 1000, 60, "从地里到家里，不超过 18 小时", size=36, font=SERIF, bold=True, color=k["ink"])
    deck.picture(s, photo("market-people"), 80, 170, 700, 440)
    deck.text(s, 80, 620, 700, 40, "社区菜市场（示意图片）。照片：Wonderlane，CC BY 2.0", size=13, font=SANS, color=k["gray"])
    deck.rect(s, 830, 170, 370, 2, fill=k["ink"])
    for i, (num, unit, label) in enumerate(C.FACTS):
        y = 190 + i * 140
        deck.text(s, 830, y, 370, 70, [[(num, {"size": 60, "font": SERIF, "bold": True, "color": k["red"] if i == 0 else k["ink"]}),
                                        (" " + unit, {"size": 22, "font": SANS, "color": k["ink"]})]])
        deck.text(s, 830, y + 76, 370, 26, label, size=17, font=SANS, color=k["gray"])
        deck.rect(s, 830, y + 120, 370, 1, fill=k["grid"])


@example("recipes", "R03-d", "R3 数据新闻 · 特色页", "小倍数图：六座城市用同一刻度并排，慢的两座用红色，一眼可比。", (SERIF, SANS))
def r3_signature(deck, s):
    k = R3
    bg(s, k["bg"])
    r3_mark(deck, s)
    deck.text(s, 80, 88, 1000, 60, "六座城市都在下降，合肥、无锡最慢", size=36, font=SERIF, bold=True, color=k["ink"])
    deck.text(s, 80, 146, 900, 26, "各城市生鲜损耗率，%，2027 年 1–6 月；纵轴均为 4%–10%", size=17, font=SANS, color=k["gray"])
    for i, city in enumerate(C.CITIES):
        x, y = 80 + (i % 3) * 380, 196 + (i // 3) * 236
        slow = city in ("合肥", "无锡")
        deck.text(s, x, y, 300, 30, city, size=20, font=SANS, bold=True, color=k["red"] if slow else k["ink"])
        deck.line_chart(s, x - 10, y + 30, 360, 190, C.MONTHS, {city: C.CITY_LOSS[city]},
                        colors=[k["red"] if slow else k["blue"]], number_format='0.0"%"', font=SANS, size=16,
                        grid=k["grid"], label_bg=k["bg"], width=2.5, min_value=4, max_value=10)


# ====================================================================== R04 Japanese magazine
R4 = dict(bg="F3F0E8", text="2A2925", gray="7A766C", line="D8D3C7", acc="9C3B2E")
CORM = "Cormorant Garamond"


@example("recipes", "R04-a", "R4 日式杂志留白 · 封面", "照片不出血、四周留大白；竖排标题贴在照片旁；西文小注做点缀。", (SERIF_SEMI, CORM))
def r4_cover(deck, s):
    k = R4
    bg(s, k["bg"])
    deck.picture(s, treated("radishes", "grade", saturation=0.72, warmth=0.05, brightness=1.04), 540, 96, 620, 528)
    deck.text(s, 432, 96, 64, 420, "把产地搬进社区", size=40, font=SERIF_SEMI, color=k["text"], vertical=True)
    deck.text(s, 96, 96, 300, 22, "知 野 生 鲜", size=16, font=SERIF, color=k["text"], spacing=0.3)
    deck.text(s, 96, 540, 330, 34, "Field to Neighbourhood", size=24, font=CORM, color=k["text"], ea=SERIF)
    deck.text(s, 96, 580, 330, 26, "No. 07  —  Summer 2027", size=16, font=CORM, color=k["gray"], ea=SERIF)
    deck.rect(s, 96, 624, 24, 2, fill=k["acc"])


@example("recipes", "R04-b", "R4 日式杂志留白 · 数据页", "图表也要安静：一条细线、没有网格、只标首尾；留白占一半以上。", (SERIF, CORM))
def r4_data(deck, s):
    k = R4
    bg(s, k["bg"])
    deck.text(s, 120, 120, 800, 50, "半年，损耗率从 9.6% 降到 5.9%", size=32, font=SERIF_SEMI, color=k["text"])
    deck.text(s, 120, 176, 600, 26, "生鲜损耗率，2027 年 1–6 月", size=16, font=SERIF, color=k["gray"])
    deck.line_chart(s, 110, 250, 760, 330, C.MONTHS, {"损耗率": C.LOSS}, colors=[k["text"]], labels="all",
                    number_format='0.0"%"', font=SERIF, size=16, axis_color=k["gray"], axis_line=k["line"], width=1.75,
                    markers=True, min_value=4)
    deck.text(s, 1040, 250, 40, 300, "按日订货　临期折扣", size=17, font=SERIF, color=k["gray"], vertical=True)
    deck.text(s, 1090, 250, 40, 300, "三月起实施", size=17, font=SERIF, color=k["acc"], vertical=True)
    deck.text(s, 120, 640, 400, 24, "— 07 —", size=16, font=CORM, color=k["gray"], ea=SERIF)


@example("recipes", "R04-c", "R4 日式杂志留白 · 图片页", "一大幅照片配一小段文字；字不多，靠位置和留白取胜。", (SERIF_SEMI,))
def r4_picture(deck, s):
    k = R4
    bg(s, k["bg"])
    deck.picture(s, treated("potatoes", "grade", saturation=0.7, warmth=0.06, brightness=1.08), 96, 96, 700, 528)
    deck.text(s, 860, 380, 340, 50, "土豆出地，第二天进店。", size=28, font=SERIF_SEMI, color=k["text"])
    deck.text(s, 860, 440, 340, 100, "清晨采摘，四小时内入城市仓，\n第二天上午摆上社区店的货架。", size=18, font=SERIF,
              color=k["gray"], line_spacing=1.7)
    deck.text(s, 860, 560, 340, 24, "30 分钟送达 · 126 家门店", size=16, font=SERIF, color=k["acc"])
    deck.text(s, 96, 640, 400, 20, "Photo: rawpixel, CC0", size=13, font=CORM, color=k["gray"], ea=SERIF)


@example("recipes", "R04-d", "R4 日式杂志留白 · 特色页", "竖排大标题、竖排小注、不对称的一小张照片；页码用小号西文。", (SERIF_SEMI, CORM))
def r4_signature(deck, s):
    k = R4
    bg(s, k["bg"])
    deck.text(s, 1060, 90, 90, 560, "早上摘的菜", size=60, font=SERIF_SEMI, color=k["text"], vertical=True)
    deck.text(s, 990, 96, 44, 520, "中午就在社区店里了", size=24, font=SERIF, color=k["gray"], vertical=True)
    deck.text(s, 944, 96, 40, 300, "杭州某社区店店长（虚构）", size=16, font=SERIF, color=k["acc"], vertical=True)
    deck.picture(s, treated("radishes", "grade", saturation=0.72, warmth=0.05, brightness=1.04), 96, 360, 360, 264)
    deck.text(s, 96, 96, 400, 30, "Interview", size=22, font=CORM, color=k["text"], ea=SERIF)
    deck.rect(s, 96, 136, 24, 2, fill=k["acc"])
    deck.text(s, 480, 600, 300, 24, "— 12 —", size=16, font=CORM, color=k["gray"], ea=SERIF)


# ====================================================================== R05 Eastern contemporary
R5 = dict(bg="EFE9DE", ink="1E1D1B", red="A8322D", teal="2F4B53", gold="A88B5A", gray="6B655B")
BRUSH, KAI = "Ma Shan Zheng", "LXGW WenKai"


def seal(deck, s, x, y, size=64, text="知野"):
    deck.rect(s, x, y, size, size, fill=R5["red"], radius=4)
    deck.text(s, x + size * 0.16, y + size * 0.1, size * 0.7, size * 0.84, text, size=size * 0.36, font=SERIF_BLACK,
              color="FFFFFF", vertical=True, align="center")


@example("recipes", "R05-a", "R5 东方当代 · 封面", "一个书法大字做主视觉；竖排标题、朱色印章、极细金线框，留白像山水。", (BRUSH, SERIF_BLACK))
def r5_cover(deck, s):
    k = R5
    bg(s, k["bg"])
    deck.rect(s, 40, 40, 1200, 640, line=k["gold"], line_width=1)
    deck.text(s, 300, 40, 600, 600, "鲜", size=440, font=BRUSH, color=k["ink"], align="center")
    deck.text(s, 1110, 110, 70, 420, "把产地搬进社区", size=36, font=SERIF_BLACK, color=k["ink"], vertical=True)
    deck.text(s, 1060, 110, 40, 300, "知野生鲜 二〇二七", size=16, font=SERIF, color=k["gray"], vertical=True)
    seal(deck, s, 1106, 560)
    deck.text(s, 100, 590, 500, 30, "社区店升级计划", size=18, font=SERIF, color=k["teal"], spacing=0.2)


@example("recipes", "R05-b", "R5 东方当代 · 数据页", "黛青线条配朱砂重点；极细金线分区；数字用宋体，克制不花哨。", (SERIF,))
def r5_data(deck, s):
    k = R5
    bg(s, k["bg"])
    deck.text(s, 100, 90, 900, 60, "损耗率六月连降，至百分之五点九", size=38, font=SERIF_BLACK, color=k["ink"])
    deck.text(s, 100, 150, 700, 26, "生鲜损耗率，%，2027 年 1–6 月（虚构示例）", size=16, font=SERIF, color=k["gray"])
    deck.rect(s, 100, 196, 1080, 1, fill=k["gold"])
    deck.line_chart(s, 90, 220, 780, 420, C.MONTHS, {"知野": C.LOSS, "同业": C.LOSS_PEERS}, colors=[k["red"], "B3AA9A"],
                    number_format='0.0"%"', font=SERIF, size=16, axis_color=k["ink"], axis_line=k["gold"], width=3,
                    min_value=4)
    deck.rect(s, 900, 220, 1, 400, fill=k["gold"])
    deck.text(s, 930, 240, 260, 120, "三月起\n按日订货\n晚八点折扣", size=24, font=KAI, color=k["teal"], line_spacing=1.6)
    seal(deck, s, 930, 520, size=52)


@example("recipes", "R05-c", "R5 东方当代 · 图片页", "窄长的照片像立轴，低饱和暖调；文字在窄栏里，配一方小印。", (SERIF_BLACK, KAI))
def r5_picture(deck, s):
    k = R5
    bg(s, k["bg"])
    deck.picture(s, treated("radishes", "grade", saturation=0.55, warmth=0.08, brightness=1.0), 120, 60, 320, 600)
    deck.rect(s, 120, 60, 320, 600, line=k["gold"], line_width=1)
    deck.text(s, 560, 150, 520, 70, "从地里到家里", size=48, font=SERIF_BLACK, color=k["ink"])
    deck.text(s, 560, 240, 420, 110, "清晨采摘，午前入仓，\n次日上午便在社区店里。", size=24, font=KAI, color=k["ink"], line_spacing=1.7)
    for i, (num, unit, label) in enumerate(C.FACTS):
        x = 560 + i * 190
        deck.rect(s, x, 420, 1, 120, fill=k["gold"])
        deck.text(s, x + 18, 420, 170, 60, num + " " + unit, size=34, font=SERIF_BLACK, color=k["red"] if i == 0 else k["teal"])
        deck.text(s, x + 18, 480, 170, 50, label, size=16, font=SERIF, color=k["gray"])
    seal(deck, s, 1120, 590, size=48)


@example("recipes", "R05-d", "R5 东方当代 · 特色页", "竖排成列、极细界格，像一卷展开的文书；标题竖排在右，印章收尾。", (KAI, SERIF_BLACK))
def r5_signature(deck, s):
    k = R5
    bg(s, k["bg"])
    cols = ["清晨采摘，不隔夜", "四小时内入城市仓", "按门店订单分拣", "上午十点前上架", "晚八点临期折扣"]
    deck.text(s, 1080, 90, 90, 540, "社区店的一天", size=48, font=SERIF_BLACK, color=k["ink"], vertical=True)
    deck.rect(s, 1040, 90, 1, 540, fill=k["gold"])
    for i, text in enumerate(cols):
        x = 960 - i * 150
        deck.text(s, x, 110, 50, 500, text, size=28, font=KAI, color=k["ink"], vertical=True)
        deck.rect(s, x - 50, 90, 1, 540, fill=k["gold"])
    seal(deck, s, 120, 560)


# ====================================================================== R06 engineering blueprint
R6 = dict(bg="0C1117", panel="141B24", line="263241", text="E6EDF3", gray="8B98A8", blue="4CC2FF", green="7EE0A1")
MONO = "JetBrains Mono"


def r6_bg(deck, s):
    deck.picture(s, generated("dots", size=(1280, 720), bg="0C1117", dot="1E2A36", gap=24), 0, 0, 1280, 720)


def r6_box(deck, s, x, y, w, h, label, tag=None, hot=False):
    k = R6
    deck.rect(s, x, y, w, h, fill=k["panel"], line=k["blue"] if hot else k["line"], line_width=1.5 if hot else 1)
    if tag:
        deck.text(s, x + 12, y + 9, w - 24, 22, tag, size=16, font=MONO, color=k["blue"] if hot else k["gray"], ea=HOS)
    deck.text(s, x + 12, y + (35 if tag else 14), w - 24, 30, label, size=18, font=HOS, bold=True, color=k["text"])


@example("recipes", "R06-a", "R6 工程蓝图 · 封面", "点阵底、等宽小标签、细线框；右侧一张简化架构图就是主视觉。", (HOS, MONO))
def r6_cover(deck, s):
    k = R6
    r6_bg(deck, s)
    deck.text(s, 80, 180, 560, 30, "[ v2027.07 ]  社区店升级 / 系统方案", size=16, font=MONO, color=k["blue"], ea=HOS)
    deck.text(s, 80, 220, 600, 200, "把产地\n搬进社区", size=76, font=HOS, bold=True, color=k["text"], line_spacing=1.1)
    deck.text(s, 80, 430, 520, 30, "订单、库存、城市仓三套系统打通", size=20, font=HOS, color=k["gray"])
    r6_box(deck, s, 760, 170, 200, 76, "订单", "01 / order")
    r6_box(deck, s, 760, 320, 200, 76, "库存", "02 / stock", hot=True)
    r6_box(deck, s, 760, 470, 200, 76, "城市仓 WMS", "03 / wms")
    for y in (246, 396):
        deck.line(s, 860, y, 860, y + 74, color=k["blue"], width=1.5, arrow=True)
    deck.line(s, 960, 358, 1060, 358, color=k["line"], width=1.5, arrow=True)
    r6_box(deck, s, 1060, 320, 150, 76, "门店", "04 / pos")


@example("recipes", "R06-b", "R6 工程蓝图 · 数据页", "图表放进带细边的面板，标注用等宽字；只有一个亮色。", (HOS, MONO))
def r6_data(deck, s):
    k = R6
    r6_bg(deck, s)
    deck.text(s, 80, 70, 1000, 50, DATA_TITLE, size=34, font=HOS, bold=True, color=k["text"])
    deck.rect(s, 80, 150, 1120, 500, fill=k["panel"], line=k["line"])
    deck.text(s, 104, 166, 600, 22, "loss_rate  ·  %  ·  2027-01 … 2027-06  （虚构示例）", size=16, font=MONO, color=k["gray"],
              ea=HOS)
    deck.line_chart(s, 96, 200, 800, 430, C.MONTHS, {"知野": C.LOSS, "同业": C.LOSS_PEERS}, colors=[k["blue"], "4A5868"],
                    number_format='0.0"%"', font=MONO, size=16, axis_color=k["gray"], axis_line=k["line"], grid="1E2833",
                    label_bg=k["panel"], width=3, min_value=4)
    deck.rect(s, 920, 200, 1, 420, fill=k["line"])
    deck.text(s, 950, 210, 230, 24, "delta", size=16, font=MONO, color=k["gray"], ea=HOS)
    deck.text(s, 950, 236, 230, 70, "−3.7pt", size=48, font=MONO, color=k["green"], ea=HOS)
    deck.text(s, 950, 330, 230, 24, "since", size=16, font=MONO, color=k["gray"], ea=HOS)
    deck.text(s, 950, 356, 230, 60, "2027-03\n按日订货上线", size=18, font=MONO, color=k["text"], ea=HOS, line_spacing=1.5)


@example("recipes", "R06-c", "R6 工程蓝图 · 图片页", "线描插画换成深色版：线条变浅、底色变深；配三行等宽规格。", (HOS, MONO))
def r6_picture(deck, s):
    k = R6
    r6_bg(deck, s)
    deck.text(s, 80, 70, 900, 50, "城市仓：离门店 5 公里", size=34, font=HOS, bold=True, color=k["text"])
    deck.illustration(s, "warehouse", 80, 150, 620, 465, style="line", ink=k["text"], primary=k["blue"], accent="F2B13C",
                      surface="18222E", line="2A3746", tokens={"primary_light": "17324A", "accent_light": "3A2E1A"})
    specs = [("sort_time", "2 h", "分拣完一天的订单"), ("sku", "1,200", "按门店订单拆箱"), ("trips", "3 / day", "补货到门店")]
    for i, (key, val, label) in enumerate(specs):
        y = 200 + i * 130
        deck.rect(s, 760, y, 440, 1, fill=k["line"])
        deck.text(s, 760, y + 14, 200, 22, key, size=16, font=MONO, color=k["gray"], ea=HOS)
        deck.text(s, 760, y + 40, 440, 50, val, size=36, font=MONO, color=k["blue"], ea=HOS)
        deck.text(s, 960, y + 50, 240, 30, label, size=17, font=HOS, color=k["text"], align="right")


@example("recipes", "R06-d", "R6 工程蓝图 · 特色页", "局部放大：架构图里圈出一个模块，用虚线引到右侧的放大面板说明细节。", (HOS, MONO))
def r6_signature(deck, s):
    k = R6
    r6_bg(deck, s)
    deck.text(s, 80, 60, 900, 44, "库存服务：每 5 分钟同步一次", size=30, font=HOS, bold=True, color=k["text"])
    layers = [("前台", ["小程序", "门店收银", "骑手 App"]), ("中台", ["订单", "会员", "库存"]), ("后台", ["WMS", "供应商", "财务"])]
    for i, (name, mods) in enumerate(layers):
        y = 150 + i * 160
        deck.text(s, 80, y + 30, 80, 24, name, size=16, font=MONO, color=k["gray"], ea=HOS)
        for j, m in enumerate(mods):
            r6_box(deck, s, 160 + j * 170, y, 150, 90, m, f"{i}{j}", hot=(m == "库存"))
    deck.rect(s, 492, 302, 166, 106, line=k["blue"], line_width=1.5, dash=True)
    deck.line(s, 658, 302, 720, 150, color=k["blue"], width=1.2, dash=True)
    deck.line(s, 658, 408, 720, 650, color=k["blue"], width=1.2, dash=True)
    deck.rect(s, 720, 150, 480, 500, fill=k["panel"], line=k["blue"], line_width=1.5)
    deck.text(s, 744, 170, 440, 22, "zoom / stock-service", size=16, font=MONO, color=k["blue"], ea=HOS)
    rows = [("sync", "every 5 min"), ("scope", "按门店 × 按批次"), ("alert", "临期 < 24 h"), ("owner", "数据组 · 许安")]
    for i, (key, val) in enumerate(rows):
        y = 220 + i * 100
        deck.rect(s, 744, y, 432, 1, fill=k["line"])
        deck.text(s, 744, y + 16, 140, 26, key, size=16, font=MONO, color=k["gray"], ea=HOS)
        deck.text(s, 880, y + 12, 300, 34, val, size=22, font=MONO, color=k["text"], ea=HOS)


# ====================================================================== R07 brutalist poster
R7 = dict(yellow="F2E94E", black="0B0B0B", white="FFFFFF", blue="2B59FF")
SMILEY, ARCHIVO, BEBAS = "Smiley Sans Oblique", "Archivo Black", "Bebas Neue"


def sticker(deck, s, x, y, w, h, text, fill, color, rotation=-6, size=28, font=SMILEY):
    deck.rect(s, x + 8, y + 8, w, h, fill=R7["black"]).rotation = rotation
    deck.rect(s, x, y, w, h, fill=fill, line=R7["black"], line_width=3).rotation = rotation
    deck.text(s, x, y + (h - size * 1.3) / 2, w, size * 1.4, text, size=size, font=font, color=color, align="center",
              ea=SMILEY).rotation = rotation


@example("recipes", "R07-a", "R7 粗野海报 · 封面", "得意黑超大、行距收紧、贴边；撞色贴纸和黑色跑马条；每页只破一处网格。", (SMILEY, ARCHIVO))
def r7_cover(deck, s):
    k = R7
    bg(s, k["yellow"])
    deck.text(s, 40, 20, 1200, 560, "把产地\n搬进社区", size=196, font=SMILEY, color=k["black"], line_spacing=0.95)
    sticker(deck, s, 960, 120, 230, 110, "2027", k["blue"], k["white"], rotation=8, size=64, font=ARCHIVO)
    deck.rect(s, 0, 600, 1280, 120, fill=k["black"])
    deck.text(s, 40, 626, 1240, 70, "知野生鲜 · 社区店升级计划 · 30 分钟送达 · 126 家门店", size=40, font=SMILEY,
              color=k["yellow"], wrap=False)


@example("recipes", "R07-b", "R7 粗野海报 · 数据页", "粗黑框、黑色柱子、一根撞色；结论用贴纸压在图上。", (SMILEY, ARCHIVO))
def r7_data(deck, s):
    k = R7
    bg(s, k["white"])
    deck.rect(s, 24, 24, 1232, 672, line=k["black"], line_width=4)
    deck.text(s, 64, 50, 1100, 100, "损耗率连降 6 个月", size=72, font=SMILEY, color=k["black"])
    deck.bar_chart(s, 64, 170, 900, 480, C.MONTHS, C.LOSS, highlight={5}, horizontal=False, color=k["blue"],
                   base=k["black"], number_format="0.0", font=ARCHIVO, size=20, label_color=k["black"], axis_color=k["black"],
                   gap_width=30)
    sticker(deck, s, 960, 240, 240, 120, "−3.7 个点!", k["yellow"], k["black"], rotation=-7, size=40)
    deck.text(s, 990, 420, 230, 90, "6 月：5.9%\n同业：9.1%", size=26, font=SMILEY, color=k["black"], line_spacing=1.2)


@example("recipes", "R07-c", "R7 粗野海报 · 图片页", "高对比照片装进粗黑框，加无模糊的硬投影；撞色色块和贴纸压住画面。", (SMILEY,))
def r7_picture(deck, s):
    k = R7
    bg(s, k["blue"])
    deck.rect(s, 640, 0, 640, 720, fill=k["yellow"])
    deck.rect(s, 584, 104, 600, 450, fill=k["black"])
    deck.picture(s, crop("tomatoes", (0.0, 0.25, 0.75, 1.0)), 570, 90, 600, 450)
    deck.rect(s, 570, 90, 600, 450, line=k["black"], line_width=4)
    deck.text(s, 60, 120, 520, 300, "颜色最鲜\n就上架", size=110, font=SMILEY, color=k["white"], line_spacing=0.95)
    sticker(deck, s, 80, 470, 210, 80, "30 分钟", k["yellow"], k["black"], rotation=-5, size=34)
    sticker(deck, s, 310, 500, 210, 80, "126 家店", k["white"], k["black"], rotation=4, size=34)
    deck.text(s, 600, 600, 640, 30, "照片：Jun Seita，CC BY 2.0（已裁切）", size=14, font=SANS, color=k["black"])


@example("recipes", "R07-d", "R7 粗野海报 · 特色页", "色块把整页一分为二，巨大的数字横跨分界；贴纸斜放，只破这一处。", (ARCHIVO, SMILEY))
def r7_signature(deck, s):
    k = R7
    bg(s, k["yellow"])
    deck.rect(s, 0, 360, 1280, 360, fill=k["blue"])
    deck.text(s, 40, 40, 1000, 680, "30", size=560, font=ARCHIVO, color=k["black"], wrap=False)
    sticker(deck, s, 820, 150, 300, 120, "分钟", k["white"], k["black"], rotation=-8, size=64)
    deck.text(s, 820, 470, 420, 140, "下单到\n送到家", size=60, font=SMILEY, color=k["white"], line_spacing=1.0)
