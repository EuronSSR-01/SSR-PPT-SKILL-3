"""Layout examples L01-L10: opening, transitions, single points and data. Fictional content."""
import content as C
from gallery import bg, crop, example, photo
from look import (ACCENT, ACCENT_LIGHT, FAINT, INK, KAI, LINE, M, MUTED, PRIMARY, PRIMARY_LIGHT, SANS, SANS_BLACK,
                  SERIF, SERIF_BLACK, W, WARM, eyebrow, ill, source, title)

F = (SANS,)


# ---------------------------------------------------------------- L01 cover
@example("layouts", "L01-a", "封面 A：大字型", "标题本身就是主视觉；右侧一条路线母题，暗示“从产地到社区”。", F)
def cover_type(deck, s):
    bg(s, WARM)
    eyebrow(deck, s, "知野生鲜 · 2027", y=64)
    deck.text(s, M, 170, 820, 340, "把产地\n搬进社区", size=136, font=SANS_BLACK, color=INK, line_spacing=1.0)
    deck.text(s, M + 4, 520, 700, 40, C.COVER_SUB, size=26, font=SANS, color=MUTED)
    route = [(850, 620), (880, 560), (950, 545), (990, 480), (950, 420), (1010, 370), (1090, 380), (1140, 310)]
    deck.polygon(s, route, line=ACCENT, line_width=5, closed=False, dash=True)
    for x, y in (route[0], route[3], route[6]):
        deck.ellipse(s, x, y, 9, fill="FFFFFF", line=ACCENT, line_width=4)
    deck.icon(s, "map-pin", 1108, 236, size=64, color=ACCENT, stroke=2.2)
    source(deck, s, "2027 年 7 月 · 虚构示例", y=650)


@example("layouts", "L01-b", "封面 B：主视觉型", "照片全出血，只在文字一侧加渐变遮罩；CC BY 照片在角落署名。", F)
def cover_photo(deck, s):
    deck.picture(s, photo("farm"), 0, 0, 1280, 720)
    deck.gradient_rect(s, -2, 0, 900, 720, [(0, "10202A", 0.92), (0.55, "10202A", 0.55), (1, "10202A", 0)])
    eyebrow(deck, s, "知野生鲜 · 2027", y=64, color="C9D3DC")
    deck.text(s, M, 220, 760, 230, "把产地\n搬进社区", size=104, font=SANS_BLACK, color="FFFFFF", line_spacing=1.0)
    deck.text(s, M + 2, 470, 640, 40, C.COVER_SUB, size=24, font=SANS, color="E6ECF1")
    deck.text(s, 900, 684, 360, 20, "照片：~MVI~ (warped)，CC BY 2.0", size=13, font=SANS, color="E6ECF1", align="right")


@example("layouts", "L01-c", "封面 C：插画场景型", "没有好照片时，用插画拼出主题场景；标题仍然是最大的元素。", F)
def cover_scene(deck, s):
    deck.text(s, M, 80, 900, 110, C.COVER_TITLE, size=84, font=SANS_BLACK, color=INK)
    deck.text(s, M + 2, 196, 800, 36, C.COVER_SUB, size=26, font=SANS, color=MUTED)
    ill(deck, s, ["farm", "truck", "warehouse", "store"], M, 290, W, 370)
    source(deck, s, "2027 年 7 月 · 虚构示例", y=676)


# ---------------------------------------------------------------- L02 section
@example("layouts", "L02-a", "章节页 A：超大编号出血", "编号裁出页面，用尺度制造停顿；章节名配一句“这一章回答什么”。", F)
def section_number(deck, s):
    bg(s, PRIMARY)
    deck.text(s, 10, 290, 660, 600, "02", size=440, font=SANS_BLACK, color="2E62B8", line_spacing=1.0)
    deck.text(s, 640, 236, 560, 24, "第二部分", size=18, font=SANS, color="AFC4E6", spacing=0.1)
    deck.text(s, 640, 272, 600, 90, "城市仓怎么建", size=64, font=SANS, bold=True, color="FFFFFF")
    deck.text(s, 640, 380, 520, 80, "这一章回答：建几座、建在哪、多久收回投入", size=24, font=SANS,
              color="DCE6F5", line_spacing=1.4)


@example("layouts", "L02-b", "章节页 B：进度式", "列出全部章节、高亮当前一章，长演示里观众知道自己在哪。", F)
def section_progress(deck, s):
    chapters = ["为什么要升级", "城市仓怎么建", "门店怎么改", "需要的支持"]
    for i, name in enumerate(chapters):
        y = 150 + i * 104
        current = i == 1
        if current:
            deck.rect(s, M, y - 6, 6, 74, fill=ACCENT)
        deck.text(s, M + 30, y, 90, 60, f"0{i + 1}", size=40, font=SANS_BLACK, color=ACCENT if current else LINE)
        deck.text(s, M + 120, y + 8, 360, 50, name, size=30 if current else 24, font=SANS, bold=current,
                  color=INK if current else FAINT)
    deck.rect(s, 600, 96, 1, 528, fill=LINE)
    deck.text(s, 660, 150, 560, 80, "城市仓怎么建", size=56, font=SANS, bold=True, color=INK)
    deck.text(s, 660, 236, 520, 70, "建几座、建在哪、多久收回投入", size=24, font=SANS, color=MUTED)
    ill(deck, s, "warehouse", 700, 330, 440, 330)


@example("layouts", "L02-c", "章节页 C：色块分屏", "一侧强调色块放编号，和内容页明显不同，但不需要照片。", F)
def section_split(deck, s):
    deck.rect(s, 0, 0, 480, 720, fill=ACCENT)
    deck.text(s, 70, 200, 400, 320, "03", size=260, font=SANS_BLACK, color="FFFFFF", line_spacing=1.0)
    deck.text(s, 560, 200, 640, 80, "门店怎么改", size=60, font=SANS, bold=True, color=INK)
    deck.text(s, 560, 292, 600, 40, "面积更小、商品更少，为什么卖得更多", size=24, font=SANS, color=MUTED)
    ill(deck, s, "store", 820, 400, 380, 285)


# ---------------------------------------------------------------- L03 quote
@example("layouts", "L03-a", "引言页 A：大引号配楷体", "引文用楷体放大，引号单独成图形；出处与引文左对齐并拉开距离。", (KAI,))
def quote_kai(deck, s):
    bg(s, WARM)
    deck.text(s, 96, 70, 200, 260, "“", size=300, font=SERIF_BLACK, color=ACCENT)
    deck.text(s, 170, 250, 980, 220, "早上摘的菜，\n中午就在社区店里了。", size=60, font=KAI, color=INK, line_spacing=1.3)
    deck.rect(s, 172, 520, 48, 3, fill=ACCENT)
    deck.text(s, 172, 540, 700, 30, C.QUOTE_BY, size=20, font=SANS, color=MUTED)


@example("layouts", "L03-b", "引言页 B：人物插画分屏", "说话的人和原话放在一起；没有授权照片时用插画代表“谁说的”。", F)
def quote_split(deck, s):
    deck.rect(s, 0, 0, 560, 720, fill=PRIMARY_LIGHT)
    ill(deck, s, "shop-assistant", 40, 170, 480, 360)
    deck.text(s, 640, 200, 560, 60, "“", size=96, font=SERIF_BLACK, color=PRIMARY)
    deck.text(s, 640, 290, 560, 200, "早上摘的菜，\n中午就在社区店里了。", size=44, font=SERIF, bold=True, color=INK,
              line_spacing=1.35)
    deck.rect(s, 642, 462, 40, 3, fill=PRIMARY)
    deck.text(s, 640, 480, 560, 30, C.QUOTE_BY, size=20, font=SANS, color=MUTED)


# ---------------------------------------------------------------- L04 breathing
@example("layouts", "L04-a", "呼吸页 A：一个问题", "深色底只放一个问题，引出下一部分；大面积留白就是停顿。", F)
def breath_question(deck, s):
    bg(s, INK)
    deck.rect(s, M, 236, 56, 4, fill=ACCENT)
    deck.text(s, M, 270, 1000, 200, "如果门店不再囤货，\n损耗能降到多少？", size=64, font=SANS, bold=True, color="FFFFFF",
              line_spacing=1.25)


@example("layouts", "L04-b", "呼吸页 B：一张小图一句话", "图很小、留白很大；适合章节之间的过渡。", F)
def breath_picture(deck, s):
    ill(deck, s, "produce", 470, 150, 340, 255)
    deck.text(s, 240, 450, 800, 50, "下一部分：1,200 种商品怎么选", size=34, font=SANS, bold=True, color=INK, align="center")
    deck.text(s, 240, 506, 800, 30, "先看损耗最高的叶菜", size=20, font=SANS, color=MUTED, align="center")


# ---------------------------------------------------------------- L05 big number
@example("layouts", "L05-a", "大数字页 A：数字压左，解读在右", "数字占左侧，单位缩小并与数字同一基线；口径放在底部小字。", F)
def number_left(deck, s):
    deck.text(s, 64, 150, 640, 360, [[("30", {"size": 270, "font": SANS_BLACK, "color": ACCENT}),
                                      ("分钟", {"size": 72, "font": SANS, "bold": True, "color": INK})]],
              line_spacing=1.0, wrap=False)
    deck.text(s, 690, 220, 510, 120, "下单到送达，中位数\n从 52 分钟降到 30 分钟", size=36, font=SANS, bold=True,
              color=INK, line_spacing=1.3)
    deck.text(s, 690, 350, 480, 90, "城市仓把分拣挪到离门店 5 公里以内，\n骑手只跑最后 3 公里。", size=20, font=SANS,
              color=MUTED, line_spacing=1.5)
    source(deck, s, "口径：2027 年 6 月全部订单，下单到签收的中位数（虚构示例）")


@example("layouts", "L05-b", "大数字页 B：数字加迷你图", "数字是结论，底部一条迷你折线是证据；强调色只给数字和最后一个点。", F)
def number_spark(deck, s):
    deck.text(s, M, 70, 640, 280, [[("5.9", {"size": 220, "font": SANS_BLACK, "color": ACCENT}),
                                    ("%", {"size": 90, "font": SANS, "bold": True, "color": ACCENT})]], line_spacing=1.0)
    deck.text(s, 720, 120, 480, 120, "生鲜损耗率\n半年降了 3.7 个百分点", size=34, font=SANS, bold=True, color=INK,
              line_spacing=1.3)
    deck.text(s, 720, 240, 470, 60, "按日订货、临期折扣两项措施 3 月起全面执行", size=20, font=SANS, color=MUTED,
              line_spacing=1.5)
    deck.line_chart(s, M, 380, W, 250, C.MONTHS, {"损耗率": C.LOSS}, colors=[ACCENT], labels="all",
                    number_format='0.0"%"', font=SANS, size=16, width=3.5, markers=True, min_value=4)
    source(deck, s, "生鲜损耗率，%，2027 年 1–6 月；纵轴从 4% 起（虚构示例）")


@example("layouts", "L05-c", "大数字页 C：数字配插画", "数字讲“多少”，插画讲“是什么”；两者面积相当，互相支撑。", F)
def number_picture(deck, s):
    deck.text(s, M, 150, 560, 300, [[("126", {"size": 230, "font": SANS_BLACK, "color": PRIMARY}),
                                     ("家", {"size": 72, "font": SANS, "bold": True, "color": INK})]], line_spacing=1.0)
    deck.text(s, M + 6, 420, 520, 50, "门店完成升级", size=36, font=SANS, bold=True, color=INK)
    deck.text(s, M + 6, 476, 520, 40, "覆盖杭州、苏州等 6 座城市", size=22, font=SANS, color=MUTED)
    deck.rect(s, 660, 110, 540, 500, fill=PRIMARY_LIGHT, radius=24)
    ill(deck, s, "city", 690, 200, 480, 360)


# ---------------------------------------------------------------- L06 one chart, one point
@example("layouts", "L06-a", "主图加结论 A：看趋势", "标题写结论，副标题写指标与期间；两条线直接在线尾标注，不用图例。", F)
def chart_trend(deck, s):
    title(deck, s, "损耗率连续 6 个月下降，6 月降到 5.9%", sub="生鲜损耗率，%，2027 年 1–6 月（虚构示例）")
    deck.line_chart(s, M, 170, 820, 460, C.MONTHS, {"知野": C.LOSS, "同城同业": C.LOSS_PEERS},
                    number_format='0.0"%"', font=SANS, size=16, grid="E9ECF0", width=4,
                    label_bg="FFFFFF")
    deck.text(s, 940, 230, 260, 30, "同城同业均值", size=18, font=SANS, color=MUTED)
    deck.text(s, 940, 352, 260, 30, "知野生鲜", size=20, font=SANS, bold=True, color=ACCENT)
    deck.rect(s, 940, 440, 260, 1, fill=LINE)
    deck.text(s, 940, 456, 260, 110, "3 月起：门店按日订货，\n临期商品晚 8 点折扣", size=18, font=SANS, color=INK,
              line_spacing=1.5)


@example("layouts", "L06-b", "主图加结论 B：比较排序", "比较用横向条形并排序；只给要讲的两根上色，其余灰。", F)
def chart_compare(deck, s):
    title(deck, s, "杭州、苏州增长最快，合肥、无锡还有空间", sub="上半年订单增长，%（虚构示例）")
    deck.bar_chart(s, M, 170, 760, 460, C.CITIES, C.CITY_GROWTH, highlight={0, 1}, color=ACCENT, base="C9CFD8",
                   font=SANS, size=18, label_color=INK)
    deck.text(s, 900, 230, 300, 80, "两座城都在\n春节前开了城市仓", size=24, font=SANS, bold=True, color=INK,
              line_spacing=1.35)
    deck.text(s, 900, 330, 290, 100, "合肥、无锡还靠外仓配送，\n是下半年的重点", size=18, font=SANS, color=MUTED,
              line_spacing=1.5)


@example("layouts", "L06-c", "主图加结论 C：指出关键细节", "整张图保持安静，只把要讲的那一根标出来，并用一句注释说清原因。", F)
def chart_detail(deck, s):
    title(deck, s, "6 月订单 36 万单，会员日贡献了单月最高峰", sub="月订单，万单，2027 年 1–6 月（虚构示例）")
    deck.bar_chart(s, M, 180, 760, 450, C.MONTHS, C.ORDERS, highlight={5}, horizontal=False, color=ACCENT,
                   base="C9CFD8", font=SANS, size=18, label_color=INK, gap_width=70)
    deck.line(s, 900, 262, 818, 262, color=INK, width=1.5)
    deck.ellipse(s, 818, 262, 4, fill=INK)
    deck.text(s, 912, 236, 300, 60, "会员日 6 月 18 日", size=22, font=SANS, bold=True, color=INK)
    deck.text(s, 912, 276, 290, 80, "单日 2.1 万单，\n约为平日的 2 倍", size=18, font=SANS, color=MUTED, line_spacing=1.5)


# ---------------------------------------------------------------- L07 KPI group
@example("layouts", "L07-a", "指标组 A：横排加细线", "四个指标等宽排开，用细竖线分隔而不是卡片；单位小一号。", F)
def kpi_row(deck, s):
    title(deck, s, "上半年四个指标全部达标", sub="2027 年 6 月（虚构示例）")
    deltas = ["比去年 −22 分钟", "比 1 月 −3.7 个百分点", "比去年 +16 个百分点", "计划 126 家，已全部完成"]
    for i, (num, unit, label, _icon) in enumerate(C.KPIS):
        x = M + i * 280
        if i:
            deck.rect(s, x - 20, 300, 1, 250, fill=LINE)
        deck.text(s, x, 300, 260, 120, [[(num, {"size": 96, "font": SANS_BLACK, "color": INK}),
                                          (unit, {"size": 32, "font": SANS, "bold": True, "color": INK})]])
        deck.text(s, x, 430, 250, 30, label, size=20, font=SANS, color=MUTED)
        deck.text(s, x, 470, 250, 30, deltas[i], size=17, font=SANS, color=ACCENT)


@example("layouts", "L07-b", "指标组 B：指标配图标", "图标让每个数字一眼可辨，统一线宽和颜色；图标与标签对齐。", F)
def kpi_icons(deck, s):
    bg(s, WARM)
    deck.text(s, M, 120, 400, 200, "上半年\n四个指标\n全部达标", size=52, font=SANS, bold=True, color=INK, line_spacing=1.2)
    deck.text(s, M, 380, 360, 60, "2027 年 6 月，与升级前相比（虚构示例）", size=18, font=SANS, color=MUTED)
    for i, (num, unit, label, icon) in enumerate(C.KPIS):
        x, y = 560 + (i % 2) * 330, 120 + (i // 2) * 240
        deck.icon(s, icon, x, y, size=44, color=PRIMARY)
        deck.text(s, x, y + 64, 300, 100, [[(num, {"size": 80, "font": SANS_BLACK, "color": INK}),
                                             (unit, {"size": 28, "font": SANS, "bold": True, "color": INK})]])
        deck.text(s, x, y + 170, 300, 30, label, size=19, font=SANS, color=MUTED)


@example("layouts", "L07-c", "指标组 C：一大三小", "最重要的指标放大一档并用强调色，其余三个靠边排成一列。", F)
def kpi_hero(deck, s):
    title(deck, s, "送达快了，顾客也回来得更勤")
    deck.text(s, M, 170, 620, 300, [[("30", {"size": 240, "font": SANS_BLACK, "color": ACCENT}),
                                     ("分钟", {"size": 72, "font": SANS, "bold": True, "color": INK})]], line_spacing=1.0)
    deck.text(s, M + 6, 460, 560, 40, "下单到送达（中位数），去年是 52 分钟", size=22, font=SANS, color=MUTED)
    for i, (num, unit, label, icon) in enumerate(C.KPIS[1:]):
        y = 170 + i * 140
        deck.rect(s, 780, y, 420, 1, fill=LINE)
        deck.icon(s, icon, 780, y + 30, size=32, color=PRIMARY)
        deck.text(s, 830, y + 16, 200, 70, [[(num, {"size": 52, "font": SANS_BLACK, "color": INK}),
                                             (unit, {"size": 22, "font": SANS, "bold": True, "color": INK})]])
        deck.text(s, 1010, y + 36, 190, 30, label, size=18, font=SANS, color=MUTED, align="right")


# ---------------------------------------------------------------- L08 before / after
@example("layouts", "L08-a", "前后对比 A：左右对半", "“之前”灰、“之后”用强调色；三行同一基线，差异直接标出来。", F)
def before_after_cols(deck, s):
    title(deck, s, "升级前后：三个数字的变化")
    deck.text(s, 360, 170, 300, 30, "升级前", size=20, font=SANS, color=FAINT)
    deck.text(s, 760, 170, 300, 30, "升级后", size=20, font=SANS, bold=True, color=ACCENT)
    deltas = ["−22 分钟", "−3.7 个百分点", "+16 个百分点"]
    for i, (name, before, after) in enumerate(C.BEFORE_AFTER):
        y = 230 + i * 130
        deck.rect(s, M, y + 104, W, 1, fill=LINE)
        deck.text(s, M, y + 30, 260, 50, name, size=26, font=SANS, bold=True, color=INK)
        deck.text(s, 360, y + 10, 330, 90, before, size=60, font=SANS, color=FAINT)
        deck.icon(s, "arrow-right", 680, y + 34, size=40, color=FAINT)
        deck.text(s, 760, y + 10, 330, 90, after, size=60, font=SANS_BLACK, color=INK)
        deck.text(s, 1040, y + 36, 160, 40, deltas[i], size=20, font=SANS, bold=True, color=ACCENT, align="right")


@example("layouts", "L08-b", "前后对比 B：同一张插画的前后", "同一物体画两遍：之前去色，之后上色；面积相同，比较才公平。", F)
def before_after_picture(deck, s):
    title(deck, s, "门店变小了，卖得反而更多")
    ill(deck, s, "store", M, 170, 480, 360, primary="A9B1BB", accent="C9CED5", ink="8A939D", surface="EEF0F2",
        line="D5D9DE")
    ill(deck, s, "store", 720, 170, 480, 360)
    deck.icon(s, "arrow-right", 610, 320, size=56, color=ACCENT)
    deck.text(s, M, 550, 480, 40, "改造前", size=22, font=SANS, color=FAINT)
    deck.text(s, M, 590, 480, 40, "300 平方米 · 2,000 种商品", size=24, font=SANS, color=MUTED)
    deck.text(s, 720, 550, 480, 40, "改造后", size=22, font=SANS, bold=True, color=ACCENT)
    deck.text(s, 720, 590, 480, 40, "180 平方米 · 1,200 种 · 坪效 +38%", size=24, font=SANS, bold=True, color=INK)


# ---------------------------------------------------------------- L09 options
@example("layouts", "L09-a", "方案并列 A：三列，推荐列加底色", "每列结构相同、各行对齐；推荐列用浅底和顶边标出，理由写在下面。", F)
def options_cols(deck, s):
    title(deck, s, "推荐自建城市仓：投入最高，但损耗最低、两年收回")
    rows = ["投入", "上线时间", "损耗"]
    for i, (name, facts, rec) in enumerate(C.OPTIONS):
        x = 300 + i * 310
        if rec:
            deck.rect(s, x - 20, 150, 290, 470, fill=PRIMARY_LIGHT)
            deck.rect(s, x - 20, 150, 290, 6, fill=ACCENT)
            deck.text(s, x, 170, 120, 26, "推荐", size=16, font=SANS, bold=True, color=ACCENT)
        deck.text(s, x, 200, 260, 50, name, size=28, font=SANS, bold=True, color=INK)
        for j, fact in enumerate(facts):
            deck.text(s, x, 300 + j * 90, 260, 40, fact, size=24, font=SANS, bold=rec, color=INK if rec else MUTED)
    for j, label in enumerate(rows):
        deck.text(s, M, 302 + j * 90, 180, 40, label, size=20, font=SANS, color=MUTED)
        deck.rect(s, M, 360 + j * 90, W, 1, fill=LINE)
    deck.text(s, 280, 580, 280, 30, "按每年节省损耗 1,200 万元估算", size=16, font=SANS, color=MUTED)


@example("layouts", "L09-b", "方案并列 B：表格加推荐标记", "方案多、维度多时用原生表格；表头配图标，推荐行加粗变色。", F)
def options_table(deck, s):
    title(deck, s, "三种建仓方式，按投入、速度和损耗比较")
    rows = [["方案", "投入", "上线时间", "损耗", "结论"],
            ["自建城市仓", "2,400 万元", "6 个月", "最低", "推荐"],
            ["租用第三方仓", "600 万元", "2 个月", "中等", "过渡用"],
            ["门店前置仓", "900 万元", "3 个月", "受面积限制", "不推荐"]]
    widths = [300, 220, 200, 220, 180]
    deck.table(s, M, 250, W, rows, col_widths=widths, row_height=96, size=24, font=SANS, header_color=MUTED,
               emphasis={(1, 0): ACCENT, (1, 1): ACCENT, (1, 2): ACCENT, (1, 3): ACCENT, (1, 4): ACCENT})
    for icon, x in (("banknote", 380), ("clock", 600), ("leaf", 800), ("badge-check", 1020)):
        deck.icon(s, icon, x + 6, 200, size=30, color=PRIMARY)


# ---------------------------------------------------------------- L10 2x2
def _matrix(deck, s, x0, y0, size, bubbles=False):
    deck.rect(s, x0, y0, size / 2, size / 2, fill=ACCENT_LIGHT)
    deck.rect(s, x0, y0, size, size, line=LINE, line_width=1.5)
    deck.line(s, x0 + size / 2, y0, x0 + size / 2, y0 + size, color=LINE, width=1.5)
    deck.line(s, x0, y0 + size / 2, x0 + size, y0 + size / 2, color=LINE, width=1.5)
    deck.text(s, x0 + 14, y0 + 12, 200, 26, "优先扩品", size=16, font=SANS, bold=True, color=ACCENT)
    deck.line(s, x0, y0 + size + 22, x0 + size, y0 + size + 22, color=MUTED, width=1.5, arrow=True)
    deck.text(s, x0, y0 + size + 30, size, 26, "损耗率  低 → 高", size=16, font=SANS, color=MUTED, align="right")
    deck.line(s, x0 - 22, y0 + size, x0 - 22, y0, color=MUTED, width=1.5, arrow=True)
    deck.text(s, x0 - 80, y0 - 34, 160, 26, "毛利率 高", size=16, font=SANS, color=MUTED)
    deck.text(s, x0 - 64, y0 + size - 26, 36, 26, "低", size=16, font=SANS, color=MUTED, align="right")
    sales = {"叶菜": 34, "水果": 26, "熟食": 14, "肉禽": 22, "乳品": 12, "冻品": 9}
    for name, loss, margin in C.CATEGORIES:
        cx, cy = x0 + loss * size, y0 + (1 - margin) * size
        r = 6 + sales[name] * 0.9 if bubbles else 9
        good = loss < 0.5 and margin > 0.5
        deck.ellipse(s, cx, cy, r, fill=ACCENT if good else PRIMARY, alpha=0.75 if bubbles else None)
        side = -1 if loss > 0.7 else 1
        deck.text(s, cx + side * (r + 8) - (90 if side < 0 else 0), cy - 15, 90, 30, name, size=19, font=SANS, bold=True,
                  color=INK, align="right" if side < 0 else "left")


@example("layouts", "L10-a", "2×2 矩阵 A：点在真实位置", "两个轴都有方向；对象按数据落点，标签紧贴圆点；结论写在右侧。", F)
def matrix_points(deck, s):
    title(deck, s, "冻品和肉禽：损耗低、毛利不差，适合扩品")
    _matrix(deck, s, 150, 160, 430)
    deck.text(s, 700, 220, 500, 90, "先扩冻品、肉禽", size=32, font=SANS, bold=True, color=INK)
    deck.text(s, 700, 280, 480, 160, "两类商品损耗率都在 3% 以下，\n毛利与水果接近；\n叶菜继续按日订货，不扩品。", size=20,
              font=SANS, color=MUTED, line_spacing=1.6)
    source(deck, s, "位置按 2027 年上半年各品类损耗率与毛利率（虚构示例）", x=700, y=640, w=500)


@example("layouts", "L10-b", "2×2 矩阵 B：气泡大小表示销售额", "第三个变量用气泡面积表示，半透明避免互相遮挡；图注写清气泡含义。", F)
def matrix_bubbles(deck, s):
    title(deck, s, "叶菜卖得最多，也坏得最快")
    _matrix(deck, s, 150, 160, 430, bubbles=True)
    deck.text(s, 700, 220, 500, 90, "叶菜是损耗的大头", size=32, font=SANS, bold=True, color=INK)
    deck.text(s, 700, 280, 480, 120, "销售额占三成以上，损耗率最高；\n降损耗先从叶菜下手。", size=20, font=SANS, color=MUTED,
              line_spacing=1.6)
    deck.ellipse(s, 712, 470, 14, fill=PRIMARY, alpha=0.75)
    deck.text(s, 740, 456, 440, 30, "气泡面积 = 上半年销售额", size=17, font=SANS, color=MUTED)
