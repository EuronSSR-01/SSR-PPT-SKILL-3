"""Style recipe examples R08-R13 (same three common pages plus one signature page each). Fictional content."""
import content as C
from gallery import bg, crop, example, generated, photo, treated

SANS, SANS_BLACK = "Noto Sans SC", "Noto Sans SC Black"
SERIF, SERIF_LIGHT, SERIF_BLACK = "Noto Serif SC", "Noto Serif SC Light", "Noto Serif SC Black"
INTER, INTER_BLACK = "Inter", "Inter Black"
PLAYFAIR, CORM = "Playfair Display", "Cormorant Garamond"
MISANS, MISANS_SEMI, MISANS_HEAVY = "MiSans", "MiSans Semibold", "MiSans Heavy"
KAI, MONO, PLEX = "LXGW WenKai", "JetBrains Mono", "IBM Plex Mono"


# ====================================================================== R08 quiet luxury
R8 = dict(ivory="F6F2EA", char="1B1A18", gray="8A8378", champ="B59B74")


@example("recipes", "R08-a", "R8 静奢品牌 · 封面", "压暗的材质照片铺底，居中细字重标题；香槟色只用在细线和小字。", (SERIF_LIGHT, CORM))
def r8_cover(deck, s):
    k = R8
    deck.picture(s, treated("fabric-gold", "darken", amount=0.62), 0, 0, 1280, 720)
    deck.text(s, 0, 220, 1280, 24, "Z H I Y E   F R E S H   ·   2 0 2 7", size=16, font=CORM, color="CDBB98", align="center",
              ea=SERIF)
    deck.text(s, 0, 270, 1280, 90, "把产地搬进社区", size=60, font=SERIF_LIGHT, color=k["ivory"], align="center", spacing=0.08)
    deck.rect(s, 610, 384, 60, 1, fill=k["champ"])
    deck.text(s, 0, 404, 1280, 40, "From the field to the neighbourhood", size=26, font=CORM, color="D8CFC0", align="center",
              ea=SERIF)
    deck.text(s, 0, 668, 1280, 20, "Photo: Delany Dean, CC BY 2.0", size=13, font=CORM, color="8A8378", align="center", ea=SERIF)


@example("recipes", "R08-b", "R8 静奢品牌 · 数据页", "居中对称、元素极少：一个大数字、一条细线、一行小字；大面积留白就是高级感。", (PLAYFAIR, SERIF_LIGHT))
def r8_data(deck, s):
    k = R8
    bg(s, k["ivory"])
    deck.text(s, 0, 108, 1280, 24, "L O S S   R A T E   ·   J U N E   2 0 2 7", size=16, font=CORM, color=k["champ"],
              align="center", ea=SERIF)
    deck.text(s, 0, 150, 1280, 220, "5.9%", size=170, font=PLAYFAIR, color=k["char"], align="center", ea=SERIF)
    deck.text(s, 0, 380, 1280, 30, "生鲜损耗率，半年下降 3.7 个百分点", size=20, font=SERIF_LIGHT, color=k["char"], align="center")
    deck.line_chart(s, 390, 440, 500, 190, C.MONTHS, {"损耗率": C.LOSS}, colors=[k["champ"]], labels="last",
                    number_format='0.0"%"', font=SERIF, size=16, axis_color=k["gray"], axis_line="E3DCCF", width=1.5,
                    min_value=4)


@example("recipes", "R08-c", "R8 静奢品牌 · 图片页", "质感照片放在细框里，配成对的中英文标题；数字小而疏。", (SERIF_LIGHT, CORM))
def r8_picture(deck, s):
    k = R8
    bg(s, k["ivory"])
    deck.picture(s, treated("potatoes", "grade", saturation=0.8, warmth=0.05, brightness=1.05), 120, 90, 420, 540)
    deck.rect(s, 104, 74, 452, 572, line=k["champ"], line_width=0.75)
    deck.text(s, 660, 200, 520, 60, "土豆，第二天进店", size=40, font=SERIF_LIGHT, color=k["char"])
    deck.text(s, 660, 266, 520, 36, "Harvested at dawn, on the shelf by morning", size=22, font=CORM, color=k["gray"], ea=SERIF)
    deck.rect(s, 660, 330, 40, 1, fill=k["champ"])
    for i, (num, unit, label) in enumerate(C.FACTS):
        x = 660 + i * 170
        deck.text(s, x, 370, 160, 50, num, size=40, font=PLAYFAIR, color=k["char"], ea=SERIF)
        deck.text(s, x, 424, 160, 40, f"{unit} · {label}", size=16, font=SERIF_LIGHT, color=k["gray"])
    deck.text(s, 104, 660, 452, 20, "Photo: rawpixel, CC0", size=13, font=CORM, color=k["gray"], ea=SERIF)


@example("recipes", "R08-d", "R8 静奢品牌 · 特色页", "深色底居中构图：一枚圆形特写、上下成对的中英文，一切都很小、很稀。", (SERIF_LIGHT, CORM))
def r8_signature(deck, s):
    k = R8
    bg(s, k["char"])
    deck.picture(s, treated("squash", "circle", ext="png", size=700), 530, 150, 220, 220)
    deck.ellipse(s, 640, 260, 124, line=k["champ"], line_width=0.75)
    deck.text(s, 0, 420, 1280, 60, "颜色最鲜的时候上架", size=36, font=SERIF_LIGHT, color=k["ivory"], align="center", spacing=0.06)
    deck.text(s, 0, 478, 1280, 34, "Picked at their brightest", size=22, font=CORM, color=k["champ"], align="center", ea=SERIF)
    deck.text(s, 0, 640, 1280, 20, "Photo: USDA, public domain", size=13, font=CORM, color=k["gray"], align="center", ea=SERIF)


# ====================================================================== R09 warm and human
R9 = dict(bg="FBF6EF", text="2D2A26", gray="6E665C", terra="C65D3B", olive="6D7B3B", mist="7A9CB8", block="F1E6D6")


@example("recipes", "R09-a", "R9 温暖人文 · 封面", "大圆角色块托住一张有人、有动作的照片；手写感的楷体点一句。", (MISANS_HEAVY, KAI))
def r9_cover(deck, s):
    k = R9
    bg(s, k["bg"])
    deck.rect(s, 600, 60, 620, 600, fill=k["block"], radius=32)
    deck.picture(s, treated("tomato-picking", "round_corners", ext="png", radius=56, size=(1040, 820)), 640, 100, 540, 426)
    deck.text(s, 664, 556, 500, 60, "“早上摘的菜，中午就在社区店里了。”", size=22, font=KAI, color=k["terra"])
    deck.text(s, 80, 190, 520, 220, "把产地\n搬进社区", size=80, font=MISANS_HEAVY, color=k["text"], line_spacing=1.1)
    deck.text(s, 84, 430, 480, 30, C.COVER_SUB, size=22, font=MISANS, color=k["gray"])
    deck.text(s, 664, 610, 520, 20, "照片：Alachua County，公有领域", size=12, font=MISANS, color=k["gray"])


@example("recipes", "R09-b", "R9 温暖人文 · 数据页", "圆角白板托住图表；暖色只给要说的那根；一句楷体批注把数字翻译成人话。", (MISANS, KAI))
def r9_data(deck, s):
    k = R9
    bg(s, k["bg"])
    deck.text(s, 80, 70, 1100, 60, DATA_TITLE_R9, size=38, font=MISANS_SEMI, color=k["text"])
    deck.rect(s, 80, 160, 1120, 490, fill="FFFFFF", radius=28)
    deck.bar_chart(s, 120, 200, 760, 420, C.MONTHS, C.LOSS, highlight={5}, horizontal=False, color=k["terra"],
                   base="DCD2C4", number_format='0.0"%"', font=MISANS, size=17, label_color=k["text"], axis_color=k["gray"],
                   gap_width=55)
    deck.text(s, 920, 280, 250, 120, "比 1 月\n少扔了近四成", size=34, font=KAI, color=k["terra"], line_spacing=1.3)
    deck.polygon(s, [(930, 400), (900, 430), (850, 440)], line=k["terra"], line_width=2.5, closed=False)
    deck.text(s, 920, 470, 260, 60, "生鲜损耗率，2027 年 1–6 月\n（虚构示例）", size=16, font=MISANS, color=k["gray"],
              line_spacing=1.5)


DATA_TITLE_R9 = "半年下来，扔掉的菜少了很多"


@example("recipes", "R09-c", "R9 温暖人文 · 图片页", "照片圆角、有人的手和动作；三个事实用三种柔和的颜色区分。", (MISANS_SEMI,))
def r9_picture(deck, s):
    k = R9
    bg(s, k["bg"])
    deck.picture(s, treated("potatoes", "round_corners", ext="png", radius=56, size=(1000, 1100)), 80, 80, 500, 560)
    deck.text(s, 660, 130, 540, 120, "土豆出地，\n第二天进店", size=48, font=MISANS_HEAVY, color=k["text"], line_spacing=1.2)
    colours = [k["terra"], k["olive"], k["mist"]]
    for i, (num, unit, label) in enumerate(C.FACTS):
        y = 330 + i * 100
        deck.rect(s, 660, y, 520, 84, fill=k["block"], radius=20)
        deck.ellipse(s, 700, y + 42, 12, fill=colours[i])
        deck.text(s, 730, y + 16, 260, 56, [[(num, {"size": 40, "font": MISANS_HEAVY, "color": colours[i]}),
                                             (" " + unit, {"size": 20, "font": MISANS, "color": k["text"]})]])
        deck.text(s, 900, y + 28, 260, 30, label, size=20, font=MISANS, color=k["text"])
    deck.text(s, 80, 656, 500, 20, "照片：rawpixel，CC0", size=12, font=MISANS, color=k["gray"])


@example("recipes", "R09-d", "R9 温暖人文 · 特色页", "引言页：大引号配楷体原话，旁边一张手部特写；全套圆角保持一致。", (KAI, MISANS))
def r9_signature(deck, s):
    k = R9
    bg(s, k["block"])
    deck.text(s, 90, 70, 200, 200, "“", size=220, font=SERIF_BLACK, color=k["terra"])
    deck.text(s, 120, 240, 640, 200, "早上摘的菜，\n中午就在社区店里了。", size=52, font=KAI, color=k["text"], line_spacing=1.4)
    deck.text(s, 124, 470, 600, 30, "—— " + C.QUOTE_BY, size=20, font=MISANS, color=k["gray"])
    deck.picture(s, treated("tomato-picking", "round_corners", ext="png", radius=48, source=crop("tomato-picking", (0.0, 0.0, 0.55, 0.75)),
                            size=(700, 760)), 820, 100, 360, 390)
    deck.text(s, 820, 500, 360, 20, "照片：Alachua County，公有领域", size=12, font=MISANS, color=k["gray"])


# ====================================================================== R10 consulting
R10 = dict(white="FFFFFF", navy="0B1F33", gray="5B6878", line="D9DEE5", primary="0B3D91", teal="00A19A")


def r10_frame(deck, s, current, page):
    k = R10
    steps = ["背景", "结果", "原因", "下一步"]
    for i, name in enumerate(steps):
        x = 80 + i * 130
        deck.rect(s, x, 36, 122, 4, fill=k["primary"] if i == current else k["line"])
        deck.text(s, x, 46, 122, 20, name, size=12, font=SANS, bold=i == current, color=k["primary"] if i == current else k["gray"])
    deck.rect(s, 80, 676, 1120, 1, fill=k["line"])
    deck.text(s, 80, 684, 900, 20, "来源：知野生鲜经营数据（虚构示例）", size=12, font=SANS, color=k["gray"])
    deck.text(s, 1100, 684, 100, 20, str(page), size=12, font=INTER, color=k["gray"], align="right")


@example("recipes", "R10-a", "R10 咨询商务 · 封面", "克制的封面：左侧标题写清讨论什么，右侧深色块列出本次要回答的三个问题。", (SANS,))
def r10_cover(deck, s):
    k = R10
    deck.rect(s, 860, 0, 420, 720, fill=k["navy"])
    deck.text(s, 80, 80, 500, 24, "知野生鲜 · 管理层讨论材料", size=16, font=SANS, color=k["gray"])
    deck.text(s, 80, 210, 720, 160, "把产地搬进社区：\n社区店升级半年回顾", size=48, font=SANS, bold=True, color=k["navy"], line_spacing=1.3)
    deck.rect(s, 80, 400, 64, 4, fill=k["teal"])
    deck.text(s, 80, 424, 600, 30, "2027 年 7 月", size=18, font=SANS, color=k["gray"])
    deck.text(s, 910, 200, 320, 30, "本次讨论回答", size=16, font=SANS, color="9FB0C6")
    for i, q in enumerate(["升级达到目标了吗？", "损耗为什么下降？", "下半年先做什么？"]):
        y = 250 + i * 90
        deck.text(s, 910, y, 60, 50, f"{i + 1}", size=36, font=INTER, bold=True, color=k["teal"], ea=SANS)
        deck.text(s, 960, y + 8, 290, 40, q, size=21, font=SANS, bold=True, color="FFFFFF")


@example("recipes", "R10-b", "R10 咨询商务 · 数据页", "动作标题贯穿；左图右结论；顶部章节条标出位置；页脚写来源和页码。", (SANS, INTER))
def r10_data(deck, s):
    k = R10
    r10_frame(deck, s, 1, 3)
    deck.text(s, 80, 86, 1120, 100, "损耗率半年下降 3.7 个百分点，已比同城同业低 3.2 个百分点", size=30, font=SANS, bold=True,
              color=k["navy"], line_spacing=1.3)
    deck.text(s, 80, 140, 700, 26, "生鲜损耗率，%，2027 年 1–6 月", size=17, font=SANS, color=k["gray"])
    deck.line_chart(s, 70, 180, 720, 470, C.MONTHS, {"知野": C.LOSS, "同城同业": C.LOSS_PEERS}, colors=[k["primary"], "A9B3C1"],
                    number_format='0.0"%"', font=SANS, size=16, grid="EEF1F4", label_bg="FFFFFF", width=3)
    deck.rect(s, 840, 190, 360, 2, fill=k["navy"])
    deck.text(s, 840, 204, 360, 30, "关键发现", size=18, font=SANS, bold=True, color=k["navy"])
    finds = [("采购端贡献最多", "产地直采、按日订货合计 −1.6 个百分点"), ("3 月是拐点", "按日订货全面执行后，降幅明显加快"),
             ("合肥、无锡最慢", "两城尚无城市仓，下半年补上")]
    for i, (head, body) in enumerate(finds):
        y = 250 + i * 130
        deck.text(s, 840, y, 40, 40, f"{i + 1}", size=26, font=INTER, bold=True, color=k["teal"], ea=SANS)
        deck.text(s, 880, y + 2, 320, 34, head, size=20, font=SANS, bold=True, color=k["navy"])
        deck.text(s, 880, y + 38, 320, 60, body, size=16, font=SANS, color=k["gray"], line_spacing=1.5)


@example("recipes", "R10-c", "R10 咨询商务 · 图片页", "价值链箭头配图标和指标：每一环一个动作、一个数字，比照片更能说明“哪里变了”。", (SANS, INTER))
def r10_picture(deck, s):
    k = R10
    r10_frame(deck, s, 1, 4)
    deck.text(s, 80, 86, 1120, 60, "从地里到家里，每一环都缩短了时间", size=30, font=SANS, bold=True, color=k["navy"])
    stages = [("leaf", "产地直采", "4 小时", "内入城市仓"), ("warehouse", "城市仓", "2 小时", "分拣完一天订单"),
              ("store", "社区门店", "10 点前", "完成上架"), ("house", "到家", "30 分钟", "下单到送达")]
    w = 270
    for i, (icon, name, big, small) in enumerate(stages):
        x = 80 + i * (w + 13)
        tip = 0 if i == len(stages) - 1 else 24
        pts = [(x, 200), (x + w - tip, 200), (x + w, 250), (x + w - tip, 300), (x, 300)] if tip else \
            [(x, 200), (x + w, 200), (x + w, 300), (x, 300)]
        if i:
            pts.append((x + 24, 250))
        deck.polygon(s, pts, fill=k["primary"] if i == 1 else "E8EDF5")
        deck.icon(s, icon, x + 40, 232, size=36, color="FFFFFF" if i == 1 else k["primary"])
        deck.text(s, x + 90, 234, 160, 34, name, size=20, font=SANS, bold=True, color="FFFFFF" if i == 1 else k["navy"])
        deck.text(s, x + 10, 340, w - 20, 70, big, size=48, font=INTER, bold=True, color=k["teal"] if i == 1 else k["navy"], ea=SANS)
        deck.text(s, x + 10, 410, w - 20, 30, small, size=17, font=SANS, color=k["gray"])
    deck.rect(s, 80, 480, 1120, 1, fill=k["line"])
    deck.text(s, 80, 500, 1120, 60, "城市仓是改动最大的一环：分拣从 5 小时缩短到 2 小时，门店因此可以按日订货。", size=20, font=SANS,
              color=k["navy"])


@example("recipes", "R10-d", "R10 咨询商务 · 特色页", "瀑布图拆解变化：起点、三项贡献、终点，加减关系一目了然；用原生形状画，可编辑。", (SANS, INTER))
def r10_signature(deck, s):
    k = R10
    r10_frame(deck, s, 2, 5)
    deck.text(s, 80, 86, 1120, 60, "损耗率下降 3.7 个百分点，采购端贡献最多", size=30, font=SANS, bold=True, color=k["navy"])
    deck.text(s, 80, 140, 700, 24, "生鲜损耗率，个百分点，1 月 → 6 月", size=17, font=SANS, color=k["gray"])
    bars = [("1 月", 9.6, None), ("采购端", -1.6, None), ("仓储端", -1.2, None), ("门店端", -0.9, None), ("6 月", 5.9, None)]
    base_y, scale, w, gap, x0 = 600, 40, 150, 70, 120
    level = 0
    for i, (name, v, _) in enumerate(bars):
        x = x0 + i * (w + gap)
        if i in (0, 4):
            top, h, colour = base_y - v * scale, v * scale, k["navy"] if i == 0 else k["primary"]
            level = v
        else:
            top, h, colour = base_y - level * scale, -v * scale, k["teal"]
            level += v
        deck.rect(s, x, top, w, h, fill=colour)
        label = f"{v:+.1f}".replace("-", "−") if i not in (0, 4) else f"{v:.1f}%"
        deck.text(s, x, top - 40, w, 34, label, size=22, font=INTER, bold=True, color=k["navy"], align="center", ea=SANS)
        deck.text(s, x, base_y + 12, w, 30, name, size=17, font=SANS, color=k["navy"], align="center")
        if i < 4:
            y = base_y - level * scale
            deck.line(s, x + w, y, x + w + gap, y, color="A9B3C1", width=1, dash=True)
    deck.rect(s, 100, base_y, 1080, 1.5, fill=k["navy"])


# ====================================================================== R11 glow tech
R11 = dict(bg="07080C", panel="11131A", border="262A33", text="F2F3F5", gray="8E95A3", amber="FFC145", orange="FF7A45")


def r11_bg(deck, s, spots=None):
    deck.picture(s, generated("glow", size=(1280, 720), colors=("FF7A45", "FFC145"), bg="07080C",
                              spots=spots or [(0.78, 0.30, 0.30), (0.95, 0.75, 0.22)], strength=0.45), 0, 0, 1280, 720)
    deck.picture(s, generated("grain", size=(1280, 720), amount=0.05), 0, 0, 1280, 720)


@example("recipes", "R11-a", "R11 光感科技 · 封面", "大面积柔光只在背景里，加一层颗粒防色带；产品卡片用 1px 细边浮在光上。", (MISANS_SEMI, MONO))
def r11_cover(deck, s):
    k = R11
    r11_bg(deck, s)
    deck.text(s, 80, 120, 400, 24, "ZHIYE / 2027.07", size=16, font=MONO, color=k["gray"], ea=MISANS)
    deck.text(s, 80, 220, 620, 220, "把产地\n搬进社区", size=84, font=MISANS_SEMI, color=k["text"], line_spacing=1.1, spacing=-0.01)
    deck.text(s, 84, 450, 560, 30, "知野 App：下单 30 分钟送到家", size=22, font=MISANS, color=k["gray"])
    deck.rect(s, 800, 200, 360, 300, fill=k["panel"], line=k["border"], radius=20, alpha=0.85)
    deck.text(s, 830, 226, 300, 22, "今日订单", size=16, font=MISANS, color=k["gray"])
    deck.text(s, 830, 254, 300, 70, "12,480", size=52, font=MONO, color=k["text"], ea=MISANS)
    for i, v in enumerate([42, 58, 50, 66, 74, 90, 82]):
        deck.rect(s, 830 + i * 44, 460 - v * 1.2, 28, v * 1.2, fill=k["amber"] if i == 5 else "343844", radius=6)


@example("recipes", "R11-b", "R11 光感科技 · 数据页", "图表放进半透明面板；线条用光源色，数值用等宽字；不做渐变文字。", (MISANS_SEMI, MONO))
def r11_data(deck, s):
    k = R11
    r11_bg(deck, s, spots=[(0.15, 0.85, 0.28), (0.9, 0.15, 0.2)])
    deck.text(s, 80, 70, 1100, 60, "损耗率连续 6 个月下降", size=40, font=MISANS_SEMI, color=k["text"])
    deck.rect(s, 80, 160, 1120, 490, fill=k["panel"], line=k["border"], radius=20, alpha=0.88)
    deck.text(s, 120, 190, 400, 24, "loss_rate  %", size=16, font=MONO, color=k["gray"], ea=MISANS)
    deck.line_chart(s, 110, 220, 760, 400, C.MONTHS, {"知野": C.LOSS, "同业": C.LOSS_PEERS}, colors=[k["amber"], "4A4F5C"],
                    number_format='0.0"%"', font=MONO, size=16, axis_color=k["gray"], axis_line=k["border"], width=3.5,
                    min_value=4)
    deck.text(s, 920, 260, 260, 26, "6 月", size=16, font=MISANS, color=k["gray"])
    deck.text(s, 920, 290, 260, 90, "5.9%", size=72, font=MONO, color=k["amber"], ea=MISANS)
    deck.text(s, 920, 400, 260, 60, "比 1 月 −3.7pt\n比同业 −3.2pt", size=18, font=MONO, color=k["text"], ea=MISANS, line_spacing=1.5)


@example("recipes", "R11-c", "R11 光感科技 · 图片页", "产品界面做主视觉：插画换成深色界面配色，背后一团光；三个功能点用等宽编号。", (MISANS_SEMI, MONO))
def r11_picture(deck, s):
    k = R11
    r11_bg(deck, s, spots=[(0.35, 0.5, 0.3)])
    deck.illustration(s, "laptop", 70, 120, 640, 480, primary=k["orange"], accent=k["amber"], ink="2A2D36", surface="1A1D24",
                      line="2F333D", tokens={"primary_light": "3A2A20", "accent_light": "3D3220"})
    deck.text(s, 760, 130, 440, 60, "一块看板管住 126 家店", size=36, font=MISANS_SEMI, color=k["text"])
    feats = [("01", "库存每 5 分钟同步"), ("02", "临期商品自动标价"), ("03", "骑手就近派单")]
    for i, (n, text) in enumerate(feats):
        y = 250 + i * 100
        deck.rect(s, 760, y, 440, 1, fill=k["border"])
        deck.text(s, 760, y + 22, 60, 30, n, size=18, font=MONO, color=k["amber"], ea=MISANS)
        deck.text(s, 820, y + 20, 380, 34, text, size=22, font=MISANS, color=k["text"])


@example("recipes", "R11-d", "R11 光感科技 · 特色页", "功能格子：细边面板、统一圆角，只有一处有光；图标用光源色。", (MISANS_SEMI,))
def r11_signature(deck, s):
    k = R11
    deck.picture(s, generated("glow", size=(1280, 720), colors=("FF7A45",), bg="07080C", spots=[(0.5, 0.62, 0.22)],
                              strength=0.5), 0, 0, 1280, 720)
    deck.text(s, 0, 70, 1280, 60, "三件事，一个 App", size=40, font=MISANS_SEMI, color=k["text"], align="center")
    cards = [("clock", "30 分钟", "下单到送达"), ("leaf", "5.9%", "生鲜损耗率"), ("store", "126 家", "门店一键补货")]
    for i, (icon, big, small) in enumerate(cards):
        x = 110 + i * 360
        deck.rect(s, x, 200, 340, 380, fill=k["panel"], line=k["border"], radius=24, alpha=0.82)
        deck.icon(s, icon, x + 36, 240, size=44, color=k["amber"])
        deck.text(s, x + 36, 420, 280, 70, big, size=52, font=MISANS_SEMI, color=k["text"])
        deck.text(s, x + 36, 500, 280, 30, small, size=19, font=MISANS, color=k["gray"])


# ====================================================================== R12 academic
R12 = dict(text="1F2328", gray="57606A", line="D0D7DE", red="B31B1B")
VIRIDIS = ["440154", "414487", "2A788E", "22A884", "5DB14A", "A89A00"]
SSERIF = "Source Serif 4"


@example("recipes", "R12-a", "R12 学术研究 · 封面", "标题写研究问题与证据来源；作者、单位、日期规范排列；不加装饰图。", (SERIF, SANS))
def r12_cover(deck, s):
    k = R12
    deck.text(s, 100, 170, 1080, 150, "社区生鲜门店升级对损耗率的影响：\n来自 6 座城市 126 家门店的证据", size=42, font=SERIF, bold=True,
              color=k["text"], line_spacing=1.35)
    deck.rect(s, 100, 350, 1080, 1, fill=k["line"])
    deck.text(s, 100, 372, 1080, 34, [[("林岚", {}), ("¹", {"size": 14}), ("　周牧", {}), ("¹", {"size": 14}), ("　许安", {}),
                                       ("²", {"size": 14})]], size=22, font=SANS, color=k["text"])
    deck.text(s, 100, 414, 1080, 50, "¹ 知野生鲜运营中心　² 知野生鲜数据部（均为虚构示例）", size=16, font=SANS, color=k["gray"])
    deck.text(s, 100, 600, 600, 26, "内部研讨会 · 2027 年 7 月", size=16, font=SANS, color=k["gray"])


@example("recipes", "R12-b", "R12 学术研究 · 数据页", "图号与图注完整；六条线用 viridis 序列色并在线尾标名；结论写在标题里。", (SERIF, SANS))
def r12_data(deck, s):
    k = R12
    deck.text(s, 80, 60, 1100, 50, "六座城市的生鲜损耗率均下降", size=32, font=SANS, bold=True, color=k["text"])
    deck.line_chart(s, 70, 120, 1000, 480, C.MONTHS, {c: C.CITY_LOSS[c] for c in C.CITIES}, colors=VIRIDIS, labels=None,
                    number_format='0.0', font=SANS, size=16, grid="EEF1F4", width=2.5, min_value=4, max_value=10.5)
    order = sorted(C.CITIES, key=lambda c: -C.CITY_LOSS[c][-1])
    for i, c in enumerate(order):
        deck.text(s, 1090, 250 + i * 34, 140, 28, f"{c}  {C.CITY_LOSS[c][-1]:.1f}", size=16, font=SANS, bold=True,
                  color=VIRIDIS[C.CITIES.index(c)])
    deck.text(s, 80, 620, 1120, 60, "图 1｜各城市生鲜损耗率（%），2027 年 1–6 月。右侧城市名按 6 月数值从高到低排列，与线尾上下位置一致。n = 126 家门店"
              "（虚构示例）。", size=17, font=SERIF, color=k["gray"], line_spacing=1.45)


@example("recipes", "R12-c", "R12 学术研究 · 图片页", "一张图版两个面板 A、B：照片作证据、图表作度量；图注逐项说明。", (SERIF, SANS))
def r12_picture(deck, s):
    k = R12
    deck.text(s, 80, 60, 1100, 50, "损耗下降主要来自采购端", size=32, font=SANS, bold=True, color=k["text"])
    deck.text(s, 80, 130, 40, 30, "A", size=22, font=SANS, bold=True, color=k["text"])
    deck.picture(s, photo("radishes"), 110, 136, 480, 380)
    deck.text(s, 650, 130, 40, 30, "B", size=22, font=SANS, bold=True, color=k["text"])
    deck.bar_chart(s, 680, 150, 520, 360, ["采购端", "仓储端", "门店端"], [43, 32, 24], highlight={0}, color=VIRIDIS[1],
                   base="B7C0CA", number_format='0"%"', font=SANS, size=16, label_color=k["text"], axis_color=k["text"])
    deck.text(s, 80, 560, 1120, 90, "图 2｜A. 叶菜到店时的状态（示意图片；USDA，公有领域）。B. 各环节对损耗下降的贡献占比，"
              "以 1 月至 6 月的下降幅度（3.7 个百分点）为 100%；因四舍五入合计不为 100%（虚构示例）。", size=17, font=SERIF,
              color=k["gray"], line_spacing=1.5)


@example("recipes", "R12-d", "R12 学术研究 · 特色页", "一页一个研究问题：问题、方法、结果三栏，引用编号写在文中，来源列在页脚。", (SERIF, SANS))
def r12_signature(deck, s):
    k = R12
    deck.text(s, 80, 60, 1100, 50, "研究问题：按日订货能否降低叶菜损耗？", size=32, font=SANS, bold=True, color=k["text"])
    cols = [("方法", "比较 38 家先实施按日订货的门店与 38 家同城、同面积的对照门店，观察 3–6 月的叶菜损耗率 [1]。"),
            ("结果", "实施门店叶菜损耗率平均下降 2.4 个百分点，对照门店下降 0.6 个百分点；差异 1.8 个百分点。"),
            ("局限", "门店并非随机分配；同期临期折扣也在推行，两项措施的作用难以完全分开 [2]。")]
    for i, (head, body) in enumerate(cols):
        x = 80 + i * 380
        deck.rect(s, x, 150, 350, 2, fill=k["text"] if i == 1 else k["line"])
        deck.text(s, x, 170, 350, 34, head, size=20, font=SANS, bold=True, color=k["red"] if i == 1 else k["text"])
        deck.text(s, x, 216, 340, 300, body, size=19, font=SERIF, color=k["text"], line_spacing=1.75)
    deck.rect(s, 80, 600, 1120, 1, fill=k["line"])
    deck.text(s, 80, 612, 1120, 60, "[1] 知野生鲜数据部，《门店订货方式与损耗》，2027。[2] 知野生鲜运营中心，《临期折扣执行记录》，2027。"
              "（均为虚构示例）", size=14, font=SERIF, color=k["gray"], line_spacing=1.5)


# ====================================================================== R13 documentary
R13 = dict(bg="0E0E0E", text="F2F2F2", gray="A3A3A3", accent="E0533D")


@example("recipes", "R13-a", "R13 纪实影像 · 封面", "真实照片全出血；标题像片头字幕，克制地落在暗部；章节和地点用等宽小字。", (SERIF, PLEX))
def r13_cover(deck, s):
    k = R13
    deck.picture(s, treated("market-people", "darken", amount=0.2), 0, 0, 1280, 720)
    deck.gradient_rect(s, 0, 380, 1280, 342, [(0, "0E0E0E", 0), (1, "0E0E0E", 0.9)], angle=90)
    deck.text(s, 80, 500, 600, 24, "一 · 早市", size=16, font=PLEX, color=k["gray"], ea=SANS)
    deck.text(s, 80, 530, 900, 80, "把产地搬进社区", size=60, font=SERIF, bold=True, color=k["text"])
    deck.text(s, 80, 618, 900, 30, "知野生鲜 2027 社区店升级计划", size=20, font=SANS, color=k["gray"])
    deck.text(s, 880, 684, 380, 20, "照片：Wonderlane，CC BY 2.0（示意）", size=12, font=SANS, color="8A8A8A", align="right")


@example("recipes", "R13-b", "R13 纪实影像 · 数据页", "黑场字幕卡：一个数字、一句把数字翻成生活的话，没有图表也成立。", (SERIF, PLEX))
def r13_data(deck, s):
    k = R13
    bg(s, k["bg"])
    deck.text(s, 0, 170, 1280, 24, "生鲜损耗率 · 2027 年 6 月", size=16, font=PLEX, color=k["gray"], align="center", ea=SANS)
    deck.text(s, 0, 210, 1280, 180, "5.9%", size=150, font=SERIF, bold=True, color=k["text"], align="center")
    deck.text(s, 0, 420, 1280, 40, "每 100 元的菜，只有不到 6 元被扔掉。", size=30, font=SERIF, color=k["text"], align="center")
    deck.text(s, 0, 480, 1280, 30, "1 月时，这个数是 9.6 元。", size=20, font=SANS, color=k["gray"], align="center")


@example("recipes", "R13-c", "R13 纪实影像 · 图片页", "照片铺满，一句字幕在下方居中；不在照片上贴卡片和图标。", (SERIF, PLEX))
def r13_picture(deck, s):
    k = R13
    deck.picture(s, photo("potatoes"), 0, 0, 1280, 720)
    deck.gradient_rect(s, 0, 480, 1280, 242, [(0, "000000", 0), (1, "000000", 0.75)], angle=90)
    deck.text(s, 60, 50, 400, 24, "二 · 产地 · 特写", size=15, font=PLEX, color="DADADA", ea=SANS)
    deck.text(s, 0, 600, 1280, 44, "土豆从地里到店里，不超过 18 小时。", size=30, font=SERIF, color=k["text"], align="center")
    deck.text(s, 0, 660, 1280, 20, "照片：rawpixel，CC0", size=12, font=SANS, color="BBBBBB", align="center")


@example("recipes", "R13-d", "R13 纪实影像 · 特色页", "景别组：全景、中景、特写三张并排，像纪录片的一组镜头；等宽小字标注景别。", (SERIF, PLEX))
def r13_signature(deck, s):
    k = R13
    bg(s, k["bg"])
    shots = [("farm", "全景 / 产地"), ("market-people", "中景 / 门店"), ("potatoes", "特写 / 商品")]
    for i, (key, cap) in enumerate(shots):
        x = 60 + i * 395
        deck.picture(s, photo(key), x, 120, 375, 420)
        deck.text(s, x, 556, 375, 26, cap, size=17, font=PLEX, color=k["gray"], ea=SANS)
    deck.text(s, 60, 50, 800, 40, "清晨、上午、餐桌", size=28, font=SERIF, bold=True, color=k["text"])
    deck.text(s, 60, 620, 1160, 50, "照片：~MVI~ (warped)，CC BY 2.0；Wonderlane，CC BY 2.0；rawpixel，CC0（均为示意）", size=13,
              font=SANS, color="8A8A8A")
