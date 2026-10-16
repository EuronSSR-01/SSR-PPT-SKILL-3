"""改写：the same page before and after, inside a company template. The "a" page is the usual text version
(labels and short sentences in a grid, icons only in the headings); the "b" page keeps every item and
carries most of them with pictures: illustrations, dot charts, clock and timer icons, flow arrows,
proportion bars, charts. The template (title top-left, logo top-right, hairline, two-colour footer band) is
fictional and only stands in for a real company template: its colours and fonts are kept, pictures are
added inside its content area. All content is fictional (知野生鲜, see content.py)."""
from gallery import example
from look import SANS
from content import CITY_TABLE, OPTIONS, LOSS, ORDERS

# the fictional company template
G = "1E6B52"        # template primary
G2 = "2E8B6A"
MINT = "DDEEE5"
AMBER = "F29F38"
AMBER_D = "B86F12"
RED = "C2410C"
INK = "1F2A37"
MUTED = "5E6B78"
FAINT = "98A2AD"
LINE = "DCE2E8"
PANEL = "F2F5F3"
L, R = 80, 1200
ILL = dict(primary=G2, accent=AMBER)
FONTS = ("Noto Sans SC",)


def frame(deck, s, title, page):
    """The company template: title, logo, hairline, footer band and page number."""
    deck.text(s, L, 32, 960, 46, title, size=28, font=SANS, bold=True, color=INK)
    deck.ellipse(s, 1104, 54, 15, fill=G)
    deck.icon(s, "leaf", 1095, 45, size=18, color="FFFFFF", stroke=2.4)
    deck.text(s, 1088, 40, 112, 28, "知野生鲜", size=19, font=SANS, bold=True, color=G, align="right")
    deck.line(s, 40, 92, 1240, 92, color=LINE, width=1)
    deck.rect(s, 0, 708, 320, 12, fill=AMBER)
    deck.rect(s, 320, 708, 960, 12, fill=G)
    deck.text(s, L, 682, 500, 18, "知野生鲜 · 内部汇报 · 虚构示例", size=12, font=SANS, color=FAINT)
    deck.text(s, 1000, 682, 200, 18, f"{page:02d}", size=12, font=SANS, color=FAINT, align="right")


def t(deck, s, x, y, w, h, content, size=15, color=INK, bold=False, align="left", **kw):
    return deck.text(s, x, y, w, h, content, size=size, font=SANS, color=color, bold=bold, align=align, **kw)


def num(deck, s, x, y, w, value, unit, size=34, color=G, unit_size=None):
    """A big number with its unit on one line."""
    t(deck, s, x, y, w, size * 1.3, [[(value, {"size": size, "bold": True, "color": color}),
                                      (unit, {"size": unit_size or max(14, int(size * 0.45)), "bold": True,
                                              "color": color})]], wrap=False)


def width_of(text, size):
    return sum(size if ord(c) > 255 else size * 0.56 for c in text)


def chip(deck, s, x, y, text, size=14, color=G):
    w = width_of(text, size) + 20
    deck.rect(s, x, y, w, size + 14, fill="FFFFFF", line=color, line_width=1, radius=(size + 14) / 2)
    t(deck, s, x, y + 6, w, size + 4, text, size=size, color=color, align="center", wrap=False)
    return w


def chevron(deck, s, x1, x2, y, color="C9D3DC", h=14):
    """A flat arrow from x1 to x2 at height y: the direction goods move."""
    deck.polygon(s, [(x1, y - h / 2), (x2 - h, y - h / 2), (x2 - h, y - h), (x2, y), (x2 - h, y + h),
                     (x2 - h, y + h / 2), (x1, y + h / 2)], fill=color)


def dots(deck, s, x, y, total, marked, per_row, r=7, gap=19, on=G2, off=MINT):
    """Dot chart: one dot per item, the first `marked` in the strong colour."""
    for i in range(total):
        deck.ellipse(s, x + r + (i % per_row) * gap, y + r + (i // per_row) * gap, r, fill=on if i < marked else off)


def heading(deck, s, x, w, text, color=G2, y=106):
    t(deck, s, x, y, w, 26, text, size=18, bold=True)
    deck.rect(s, x, y + 32, w, 3, fill=color)


def pairs(deck, s, x, y, w, items, step=74):
    """The 'before' habit: a label and a short sentence, repeated down a column."""
    for label, value in items:
        t(deck, s, x, y, w, 20, label, size=14, bold=True, color=G2)
        t(deck, s, x, y + 24, w, 44, value, size=15, color=MUTED, line_spacing=1.3)
        y += step


# ------------------------------------------------------------------ C01 一条链
CHAIN_TITLE = "一条链：从产地到社区，货一天走完"
CHAIN = [
    ("产地", "leaf", [("合作农场", "48 家，其中合作社 30 家"), ("规模", "大到产地批发市场，小到单个农户"),
                      ("采摘", "清晨 5 点采摘")]),
    ("冷链干线", "truck", [("车辆", "自有冷藏车 26 辆"), ("时效", "采摘后 4 小时内入仓"), ("温度", "全程 0–4℃")]),
    ("城市仓", "warehouse", [("数量", "城市仓 5 座"), ("分拣", "入仓后 2 小时完成"), ("覆盖", "杭州、苏州、南京、宁波")]),
    ("门店与到家", "store", [("门店", "社区门店 126 家"), ("上架", "上午 10 点前上架"), ("到家", "下单后 30 分钟送达")]),
]
COLS = [80, 365, 650, 935]
CW = 265


@example("convert", "C01-a", "产业链 A：改写前，16 条信息全是字",
         "标签加短句排成四栏格子，图标只在栏头：每格都要读一句话，看不出哪个是物件、哪个是数量、哪个是流向。"
         "信息 16 条：图 0 · 文 16。", fonts=FONTS)
def chain_before(deck, s):
    frame(deck, s, CHAIN_TITLE, 4)
    for x, (name, icon, items) in zip(COLS, CHAIN):
        deck.rect(s, x, 110, CW, 46, fill=PANEL)
        deck.icon(s, icon, x + 14, 121, size=24, color=G2, stroke=2.0)
        t(deck, s, x + 48, 120, CW - 60, 26, name, size=18, bold=True)
        pairs(deck, s, x, 178, CW, items, step=92)
    deck.line(s, L, 466, R, 466, color=LINE, width=1)
    rows = [("结算", "公司向农场预付三成货款，到货后结清。"),
            ("顾客付款", "小程序付款占 68%，门店收银占 32%。"),
            ("损耗", "全程生鲜损耗率 5.9%（1 月为 9.6%）。")]
    pairs(deck, s, L, 484, 1120, rows, step=60)


@example("convert", "C01-b", "产业链 B：改写后，同样 16 条，14 条由图承载",
         "每站一幅插画放在自己的栏头；农场数画成点阵，时间用时钟和计时图标，货的方向用箭头，钱的方向用带标签的"
         "箭头，付款构成用比例条。文字只剩短标签。信息 16 条：图 14 · 文 2。", fonts=FONTS)
def chain_after(deck, s):
    frame(deck, s, CHAIN_TITLE, 4)
    names = ["farm", "reefer-truck", "warehouse", "store"]
    for i, (x, (name, _, _)) in enumerate(zip(COLS, CHAIN)):
        heading(deck, s, x, CW, name)
        deck.illustration(s, names[i], x, 150, 176, 104, **ILL)
        if i < 3:
            chevron(deck, s, x + 192, x + CW + 6, 204)
    # 产地: farms as dots, size range
    dots(deck, s, COLS[0], 268, 48, 30, 12)
    t(deck, s, COLS[0], 348, CW, 22, [[("48 家合作农场", {"bold": True}), ("，绿色为合作社 30 家", {"color": MUTED})]],
      size=14)
    deck.icon(s, "clock", COLS[0], 384, size=24, color=G2, stroke=2.0)
    t(deck, s, COLS[0] + 34, 383, 220, 26, [[("5:00", {"size": 20, "bold": True, "color": G}),
                                             ("  清晨采摘", {"size": 14, "color": MUTED})]], wrap=False)
    # 冷链
    num(deck, s, COLS[1], 266, CW, "26", " 辆冷藏车")
    deck.icon(s, "timer", COLS[1], 326, size=24, color=G2, stroke=2.0)
    t(deck, s, COLS[1] + 34, 325, 220, 26, [[("4 小时", {"size": 20, "bold": True, "color": G}),
                                             ("内入仓", {"size": 14, "color": MUTED})]], wrap=False)
    chip(deck, s, COLS[1], 380, "全程 0–4℃", color=G2)
    # 城市仓
    num(deck, s, COLS[2], 266, CW, "5", " 座城市仓")
    deck.icon(s, "timer", COLS[2], 326, size=24, color=G2, stroke=2.0)
    t(deck, s, COLS[2] + 34, 325, 220, 26, [[("2 小时", {"size": 20, "bold": True, "color": G}),
                                             ("分拣完", {"size": 14, "color": MUTED})]], wrap=False)
    deck.icon(s, "map-pin", COLS[2], 384, size=20, color=MUTED, stroke=2.0)
    t(deck, s, COLS[2] + 26, 384, 240, 20, "杭州、苏州、南京、宁波", size=14, color=MUTED)
    # 门店与到家
    num(deck, s, COLS[3], 266, CW, "126", " 家门店")
    deck.icon(s, "clock", COLS[3], 326, size=24, color=G2, stroke=2.0)
    t(deck, s, COLS[3] + 34, 325, 220, 26, [[("10:00", {"size": 20, "bold": True, "color": G}),
                                             (" 前上架", {"size": 14, "color": MUTED})]], wrap=False)
    deck.icon(s, "house", COLS[3], 384, size=24, color=AMBER_D, stroke=2.0)
    t(deck, s, COLS[3] + 34, 383, 220, 26, [[("30 分钟", {"size": 20, "bold": True, "color": AMBER_D}),
                                             ("到家", {"size": 14, "color": MUTED})]], wrap=False)
    # money: who pays whom
    deck.rect(s, L, 440, R - L, 124, fill=PANEL)
    deck.icon(s, "banknote", L + 16, 452, size=22, color=MUTED, stroke=2.0)
    t(deck, s, L + 46, 453, 300, 20, "钱怎么走", size=14, bold=True, color=MUTED)
    x = L + 20
    for c in ("预付三成", "到货结清"):
        x += chip(deck, s, x, 486, c) + 8
    deck.line(s, COLS[2] + 120, 538, L + 20, 538, color=G, width=2.2, arrow=True)
    t(deck, s, L + 20, 544, 300, 16, "公司 → 农场", size=12, color=FAINT)
    t(deck, s, COLS[3], 456, CW, 20, "顾客 → 门店：怎么付款", size=14, color=MUTED)
    deck.rect(s, COLS[3], 486, CW * 0.68, 30, fill=G2)
    deck.rect(s, COLS[3] + CW * 0.68 + 2, 486, CW * 0.32 - 2, 30, fill=AMBER)
    t(deck, s, COLS[3] + 10, 492, 160, 20, "小程序 68%", size=14, bold=True, color="FFFFFF", wrap=False)
    t(deck, s, COLS[3] + CW * 0.68 + 6, 492, 80, 20, "收银 32%", size=13, bold=True, color="FFFFFF", wrap=False)
    # size range of the farms, loss rate
    t(deck, s, L, 586, 80, 22, "农场规模", size=14, bold=True, color=MUTED)
    deck.icon(s, "building-2", L + 84, 578, size=40, color=G2, stroke=1.8)
    t(deck, s, L + 134, 588, 140, 22, "产地批发市场", size=14, color=MUTED)
    deck.line(s, L + 238, 600, L + 330, 600, color=FAINT, width=1.2, dash=True)
    deck.polygon(s, [(L + 330, 595), (L + 340, 600), (L + 330, 605)], fill=FAINT)
    t(deck, s, L + 350, 588, 100, 22, "单个农户", size=14, color=MUTED)
    deck.icon(s, "user", L + 418, 590, size=22, color=G2, stroke=2.0)
    deck.icon(s, "leaf", COLS[2], 592, size=30, color=G2, stroke=2.0)
    num(deck, s, COLS[2] + 40, 584, 120, "5.9", "%", size=30)
    t(deck, s, COLS[2] + 140, 598, 300, 22, "全程生鲜损耗率（1 月为 9.6%）", size=14, color=MUTED)


# ------------------------------------------------------------------ C02 三件事
ASK_TITLE = "需要总部支持的三件事"
X3 = [80, 475, 870]
W3 = 330


@example("convert", "C02-a", "三项诉求 A：改写前，三段要点",
         "每项一个标题加两三句话：数字埋在句子里，城市、系统、账期都要读完才看得出。信息 14 条：图 0 · 文 14。",
         fonts=FONTS)
def asks_before(deck, s):
    frame(deck, s, ASK_TITLE, 9)
    sections = [
        ("01", "在合肥、无锡建城市仓", [
            "六座城市里合肥、无锡还没有城市仓，下单到送达分别要 35 分钟、34 分钟，杭州只要 26 分钟。",
            "两城生鲜损耗率 7.2%、6.9%，高于杭州的 5.1%。",
            "每座自建城市仓约 2,400 万元，6 个月上线。"]),
        ("02", "统一门店收银系统", [
            "门店现在用 3 套收银系统，同一位会员在不同门店是不同账号，会员数据不通。",
            "建议统一为一套，12 月随会员体系上线。"]),
        ("03", "缩短农场账期", [
            "合作农场多为合作社，资金紧张；现在的账期是 45 天。",
            "建议缩短到 15 天，需要周转资金约 3,000 万元，换来采购价下降约 3%。"]),
    ]
    y = 112
    for n, head, bullets in sections:
        t(deck, s, L, y - 2, 60, 36, n, size=28, bold=True, color=G2)
        t(deck, s, L + 64, y + 2, 900, 30, head, size=20, bold=True)
        for i, b in enumerate(bullets):
            t(deck, s, L + 64, y + 44 + i * 36, 1056, 26, "· " + b, size=16, color=MUTED)
        y += 60 + len(bullets) * 36 + 40
        if n != "03":
            deck.line(s, L, y - 22, R, y - 22, color=LINE, width=1)


@example("convert", "C02-b", "三项诉求 B：改写后，每项一张小图",
         "城市仓画成六个城市格子（有的打勾、没有的打叉）加送达时间条形图；收银系统画成三台收银机连着同一位会员，"
         "再合成一台；账期画成两根长短不同的条，资金和采购价用图标加数字。信息 14 条：图 12 · 文 2。", fonts=FONTS)
def asks_after(deck, s):
    frame(deck, s, ASK_TITLE, 9)
    heads = [("01", "在合肥、无锡建城市仓"), ("02", "统一门店收银系统"), ("03", "缩短农场账期")]
    for x0, (n, head) in zip(X3, heads):
        t(deck, s, x0, 104, 50, 36, n, size=26, bold=True, color=G2)
        t(deck, s, x0 + 46, 108, W3 - 46, 30, head, size=20, bold=True)
        deck.line(s, x0, 152, x0 + W3, 152, color=LINE, width=1)

    # 01 city warehouses: which cities have one, delivery time, cost
    x0 = X3[0]
    t(deck, s, x0, 164, W3, 20, "哪些城市有城市仓", size=13, color=MUTED)
    has = {r[0]: int(r[2]) for r in CITY_TABLE[1:]}
    for i, city in enumerate(["杭州", "苏州", "南京", "宁波", "合肥", "无锡"]):
        tx, ty = x0 + (i % 3) * 113, 188 + (i // 3) * 48
        ok = has[city] > 0
        deck.rect(s, tx, ty, 104, 40, fill=MINT if ok else "FFFFFF", line=None if ok else AMBER, radius=6,
                  dash=not ok)
        deck.icon(s, "warehouse" if ok else "circle-x", tx + 10, ty + 9, size=22, color=G if ok else AMBER_D,
                  stroke=2.0)
        t(deck, s, tx + 40, ty + 10, 60, 22, city, size=15, bold=True, color=G if ok else AMBER_D)
    t(deck, s, x0, 296, W3, 20, "下单到送达（分钟）", size=13, color=MUTED)
    rows = sorted(((r[0], int(r[3])) for r in CITY_TABLE[1:]), key=lambda p: -p[1])
    deck.bar_chart(s, x0, 316, W3, 170, [c for c, _ in rows], [m for _, m in rows], highlight=[0, 1],
                   color=AMBER, base="C5CED6", font=SANS, size=14, label_color=MUTED, gap_width=45)
    t(deck, s, x0, 494, W3, 22, "两城损耗率也最高：7.2%、6.9%（杭州 5.1%）", size=14, color=MUTED)
    deck.icon(s, "coins", x0, 540, size=26, color=G2, stroke=2.0)
    num(deck, s, x0 + 34, 532, 170, "2,400", " 万元/座", size=24)
    deck.icon(s, "calendar", x0 + 196, 540, size=26, color=G2, stroke=2.0)
    num(deck, s, x0 + 230, 532, 110, "6", " 个月上线", size=24)

    # 02 one till system: three tills, one member with three accounts, merged into one
    x0 = X3[1]
    cx = x0 + W3 / 2
    tills = [(x0 + 30, G2, "系统 A"), (x0 + 145, AMBER_D, "系统 B"), (x0 + 260, MUTED, "系统 C")]
    for tx, colour, label in tills:
        deck.icon(s, "monitor", tx, 170, size=40, color=colour, stroke=1.8)
        t(deck, s, tx - 10, 214, 60, 20, label, size=13, color=colour, align="center")
        deck.line(s, tx + 20, 238, cx, 280, color=FAINT, width=1.2, dash=True)
    deck.icon(s, "user", cx - 20, 282, size=40, color=INK, stroke=1.8)
    t(deck, s, x0, 328, W3, 22, "同一位会员，3 个账号，数据不通", size=14, color=MUTED, align="center")
    deck.line(s, cx, 362, cx, 404, color=G, width=2.2, arrow=True)
    deck.rect(s, x0 + 20, 414, W3 - 40, 76, fill=MINT, radius=8)
    deck.icon(s, "monitor", x0 + 40, 430, size=44, color=G, stroke=1.8)
    deck.icon(s, "circle-check", x0 + 72, 462, size=22, color=G, stroke=2.4)
    t(deck, s, x0 + 104, 438, 200, 28, "统一为一套", size=20, bold=True, color=G)
    t(deck, s, x0 + 104, 466, 200, 20, "会员一个账号走遍门店", size=13, color=MUTED)
    deck.icon(s, "calendar", x0 + 20, 540, size=26, color=G2, stroke=2.0)
    num(deck, s, x0 + 54, 532, 80, "12", " 月", size=24)
    t(deck, s, x0 + 128, 544, 200, 20, "随会员体系上线", size=14, color=MUTED)

    # 03 farm payment terms: 45 days now, 15 days asked; money needed and what it buys
    x0 = X3[2]
    t(deck, s, x0, 164, W3, 20, "付给农场的账期（天）", size=13, color=MUTED)
    full = W3 - 60
    t(deck, s, x0, 196, 50, 22, "现在", size=14, color=MUTED)
    deck.rect(s, x0 + 50, 192, full, 30, fill="C5CED6")
    t(deck, s, x0 + 50 + full - 70, 197, 64, 22, "45 天", size=15, bold=True, color="FFFFFF", align="right")
    t(deck, s, x0, 244, 50, 22, "建议", size=14, color=G, bold=True)
    deck.rect(s, x0 + 50, 240, full / 3, 30, fill=G2)
    t(deck, s, x0 + 56 + full / 3, 245, 80, 22, "15 天", size=15, bold=True, color=G)
    deck.icon(s, "users", x0, 300, size=24, color=MUTED, stroke=2.0)
    t(deck, s, x0 + 34, 302, W3 - 34, 22, "合作农场多为合作社，资金紧", size=14, color=MUTED)
    deck.icon(s, "coins", x0, 366, size=30, color=G2, stroke=2.0)
    num(deck, s, x0 + 42, 356, 260, "3,000", " 万元", size=32)
    t(deck, s, x0 + 42, 402, 260, 20, "需要的周转资金", size=14, color=MUTED)
    deck.icon(s, "trending-down", x0, 454, size=30, color=G2, stroke=2.0)
    num(deck, s, x0 + 42, 444, 260, "约 −3", "%", size=32)
    t(deck, s, x0 + 42, 490, 260, 20, "换来的采购价下降", size=14, color=MUTED)


# ------------------------------------------------------------------ C03 公司概况
PROFILE_TITLE = "知野生鲜：六座城市、126 家社区店"


@example("convert", "C03-a", "公司概况 A：改写前，一段话加五条要点",
         "公司概况写成一段介绍和一列要点：13 条信息都要读，规模、设施、经营数字混在一起。信息 13 条：图 0 · 文 13。",
         fonts=FONTS)
def profile_before(deck, s):
    frame(deck, s, PROFILE_TITLE, 2)
    t(deck, s, L, 120, 500, 220, "知野生鲜成立于 2019 年，是一家社区生鲜连锁，在杭州、苏州、合肥、南京、宁波、无锡 6 座城市"
      "开设 126 家社区门店，会员 52 万人。", size=19, color=INK, line_spacing=1.6)
    points = ["自有城市仓 5 座、冷藏车 26 辆，下单到送达 30 分钟。",
              "在售商品约 1,800 种，生鲜占销售额 64%。",
              "员工约 2,300 人。",
              "月订单从 1 月的 18 万单增长到 6 月的 36 万单。",
              f"生鲜损耗率 {LOSS[-1]}%，同城同业均值 9.1%。"]
    for i, p in enumerate(points):
        t(deck, s, 660, 124 + i * 58, 540, 50, "· " + p, size=17, color=MUTED, line_spacing=1.4)


@example("convert", "C03-b", "公司概况 B：改写后，规模、设施、经营各成一组",
         "门店用插画加大数字，六座城市排成标签；城市仓、冷藏车、员工各配一幅小插画，送达、商品、会员、成立年份配图标；"
         "订单增长画成折线，生鲜占比画成比例条，损耗和同业并排成两根短条。信息 13 条：图 11 · 文 2。", fonts=FONTS)
def profile_after(deck, s):
    frame(deck, s, PROFILE_TITLE, 2)
    # scale
    deck.illustration(s, "store", L, 112, 240, 150, **ILL)
    num(deck, s, L, 272, 360, "126", " 家社区门店", size=44)
    x, y = L, 338
    for i, city in enumerate(r[0] for r in CITY_TABLE[1:]):
        if i == 3:
            x, y = L, 376
        x += chip(deck, s, x, y, city, color=G2) + 8
    deck.icon(s, "users", L, 440, size=28, color=G2, stroke=2.0)
    num(deck, s, L + 38, 430, 200, "52", " 万会员", size=30)
    deck.icon(s, "calendar", L, 500, size=28, color=G2, stroke=2.0)
    num(deck, s, L + 38, 490, 200, "2019", " 年成立", size=30)
    # facilities and people
    cells = [("ill", "warehouse", "5", " 座城市仓"), ("ill", "reefer-truck", "26", " 辆冷藏车"),
             ("ill", "team", "约 2,300", " 名员工"), ("icon", "clock", "30", " 分钟送达"),
             ("icon", "package", "约 1,800", " 种商品")]
    for i, (kind, name, value, unit) in enumerate(cells):
        cx0, cy0 = 470 + (i % 2) * 190, 112 + (i // 2) * 158
        if kind == "ill":
            deck.illustration(s, name, cx0, cy0, 120, 72, **ILL)
        else:
            deck.icon(s, name, cx0 + 4, cy0 + 20, size=40, color=G2, stroke=1.8)
        num(deck, s, cx0, cy0 + 80, 180, value, unit, size=26)
    # business
    bx = 880
    t(deck, s, bx, 112, 320, 20, "月订单（万单）", size=13, color=MUTED)
    deck.line_chart(s, bx, 134, 320, 150, ["1月", "2月", "3月", "4月", "5月", "6月"], {"订单": ORDERS},
                    colors=[G2], labels="all", font=SANS, size=13, label_color=G, axis_color=MUTED)
    t(deck, s, bx, 314, 320, 20, "生鲜占销售额", size=13, color=MUTED)
    deck.rect(s, bx, 338, 320 * 0.64, 30, fill=G2)
    deck.rect(s, bx + 320 * 0.64 + 2, 338, 320 * 0.36 - 2, 30, fill="D5DCE2")
    t(deck, s, bx + 10, 343, 120, 22, "64%", size=16, bold=True, color="FFFFFF")
    t(deck, s, bx, 400, 320, 20, "生鲜损耗率（%）", size=13, color=MUTED)
    for i, (label, value, colour) in enumerate((("知野", LOSS[-1], G2), ("同城同业", 9.1, "C5CED6"))):
        yy = 426 + i * 40
        t(deck, s, bx, yy + 4, 70, 22, label, size=14, color=MUTED)
        deck.rect(s, bx + 74, yy, 200 * value / 9.1, 28, fill=colour)
        t(deck, s, bx + 80 + 200 * value / 9.1, yy + 3, 60, 22, f"{value}", size=15, bold=True,
          color=G if i == 0 else MUTED)


# ------------------------------------------------------------------ C04 门店分布
MAP_TITLE = "门店分布：杭州最多，合肥、无锡还没有城市仓"
# rough relative positions (not a map, no borders): west to east, north to south
PLACES = {"合肥": (190, 360), "南京": (360, 250), "无锡": (560, 230), "苏州": (700, 330), "杭州": (590, 500),
          "宁波": (820, 560)}


@example("convert", "C04-a", "门店分布 A：改写前，六行城市清单",
         "每座城市一行字：门店数、城市仓数、送达时间要逐行读、自己比较。信息 19 条：图 0 · 文 19。", fonts=FONTS)
def map_before(deck, s):
    frame(deck, s, MAP_TITLE, 5)
    for i, (city, stores, wh, minutes, *_rest) in enumerate(CITY_TABLE[1:]):
        x, y = L + (i % 2) * 570, 128 + (i // 2) * 92
        t(deck, s, x, y, 520, 26, city, size=19, bold=True, color=G2)
        t(deck, s, x, y + 34, 540, 24, f"门店 {stores} 家，城市仓 {wh} 座，下单到送达 {minutes} 分钟。",
          size=16, color=MUTED)
    deck.line(s, L, 418, R, 418, color=LINE, width=1)
    t(deck, s, L, 436, 1120, 26, "合肥、无锡还没有城市仓，送达时间是六座城市里最长的。", size=17, color=INK)


@example("convert", "C04-b", "门店分布 B：改写后，城市圆点按大致方位摆放",
         "圆的大小是门店数，实心是有城市仓（旁边几个仓库图标就是几座），虚线圈是还没有；送达分钟标在城市名旁。"
         "位置只是大致方位，不画省界，不是地图。信息 19 条：图 18 · 文 1。", fonts=FONTS)
def map_after(deck, s):
    frame(deck, s, MAP_TITLE, 5)
    for city, stores, wh, minutes, *_rest in CITY_TABLE[1:]:
        cx, cy = PLACES[city]
        r = 11 * int(stores) ** 0.5
        has = int(wh) > 0
        deck.ellipse(s, cx, cy, r, fill=G2 if has else "FFFFFF", line=None if has else AMBER, line_width=2,
                     dash=not has)
        t(deck, s, cx - r, cy - 17, 2 * r, 34, stores, size=26, bold=True, color="FFFFFF" if has else AMBER_D,
          align="center", valign="middle", wrap=False)
        lx = cx + r + 12
        t(deck, s, lx, cy - 30, 140, 26, city, size=19, bold=True, color=INK)
        t(deck, s, lx, cy + 2, 140, 22, [[(minutes, {"bold": True, "color": AMBER_D if not has else G, "size": 17}),
                                          (" 分钟送达", {"color": MUTED, "size": 13})]], wrap=False)
        if has:
            for k in range(int(wh)):
                deck.icon(s, "warehouse", lx + k * 24, cy + 30, size=20, color=G, stroke=2.0)
        else:
            t(deck, s, lx, cy + 30, 120, 20, "无城市仓", size=13, bold=True, color=AMBER_D)
    # legend
    lx = 980
    deck.rect(s, lx - 20, 112, 240, 300, fill=PANEL, radius=8)
    t(deck, s, lx, 128, 200, 20, "怎么看", size=14, bold=True, color=MUTED)
    deck.ellipse(s, lx + 16, 178, 16, fill=G2)
    t(deck, s, lx + 44, 168, 160, 20, "有城市仓", size=14, color=INK)
    deck.icon(s, "warehouse", lx + 6, 212, size=20, color=G, stroke=2.0)
    t(deck, s, lx + 44, 212, 160, 20, "一个图标一座仓", size=14, color=INK)
    deck.ellipse(s, lx + 16, 266, 16, fill="FFFFFF", line=AMBER, line_width=2, dash=True)
    t(deck, s, lx + 44, 256, 160, 20, "还没有城市仓", size=14, color=INK)
    t(deck, s, lx, 302, 200, 60, "圆越大，门店越多；\n圆里的数字是门店数", size=14, color=INK, line_spacing=1.3)
    t(deck, s, lx, 364, 190, 40, "位置为大致方位，不是地图", size=12, color=FAINT)


# ------------------------------------------------------------------ C05 方案选择
OPTION_TITLE = "城市仓怎么建：自建投入最高，但两年收回"


@example("convert", "C05-a", "方案选择 A：改写前，三段方案说明",
         "三种建法各写一句，推荐理由写在最后：投入、时间、损耗要在三句话之间来回比。信息 12 条：图 0 · 文 12。",
         fonts=FONTS)
def options_before(deck, s):
    frame(deck, s, OPTION_TITLE, 7)
    lines = [("自建城市仓", "投入约 2,400 万元，6 个月上线，损耗最低。"),
             ("租用第三方仓", "投入约 600 万元，2 个月上线，损耗中等。"),
             ("门店前置仓", "投入约 900 万元，3 个月上线，损耗受门店面积限制。")]
    for i, (name, text) in enumerate(lines):
        y = 124 + i * 96
        t(deck, s, L, y, 400, 28, name, size=20, bold=True, color=G2)
        t(deck, s, L, y + 38, 1120, 26, text, size=17, color=MUTED)
    deck.rect(s, L, 430, 1120, 96, fill=PANEL, radius=8)
    t(deck, s, L + 24, 448, 1080, 28, "推荐：自建城市仓", size=19, bold=True, color=G)
    t(deck, s, L + 24, 484, 1080, 26, "按每年少损耗约 1,200 万元估算，两年收回投入。", size=17, color=MUTED)


@example("convert", "C05-b", "方案选择 B：改写后，三列同尺比较，回收期画成两段",
         "每种建法一幅插画；投入画成同一比例的条，上线时间画成月份圆点，损耗画成三格刻度；推荐的一列加底色和勾。"
         "回收期画成两段“每年 1,200 万”拼满 2,400 万。信息 12 条：图 11 · 文 1。", fonts=FONTS)
def options_after(deck, s):
    frame(deck, s, OPTION_TITLE, 7)
    pictures = ["warehouse", "pallet-rack", "store"]
    money = [2400, 600, 900]
    months = [6, 2, 3]
    loss = [1, 2, None]                      # 1 = lowest of three steps, 2 = middle; None = no level
    deck.rect(s, X3[0] - 16, 102, W3 + 32, 346, fill=MINT, radius=10)
    for i, (x0, (name, cells, best)) in enumerate(zip(X3, OPTIONS)):
        deck.illustration(s, pictures[i], x0 + 70, 112, 190, 104, **ILL)
        t(deck, s, x0, 222, W3, 30, name, size=21, bold=True, color=G if best else INK, align="center")
        if best:
            deck.icon(s, "circle-check", x0 + 248, 226, size=24, color=G, stroke=2.4)
            chip(deck, s, x0 + 6, 116, "推荐", size=14, color=AMBER_D)
        t(deck, s, x0, 270, 60, 20, "投入", size=13, color=MUTED)
        deck.rect(s, x0 + 50, 268, 200 * money[i] / 2400, 24, fill=G2 if best else "B9C4CE")
        t(deck, s, x0 + 58 + 200 * money[i] / 2400, 268, 120, 24, cells[0], size=15, bold=True, color=INK, wrap=False)
        t(deck, s, x0, 322, 60, 20, "上线", size=13, color=MUTED)
        for m in range(6):
            deck.ellipse(s, x0 + 62 + m * 26, 332, 9, fill=(G2 if best else "8A97A4") if m < months[i] else "E3E8EC")
        t(deck, s, x0 + 220, 321, 100, 22, cells[1], size=15, bold=True, color=INK, wrap=False)
        t(deck, s, x0, 374, 60, 20, "损耗", size=13, color=MUTED)
        if loss[i]:
            for k in range(3):
                fill = (G2 if loss[i] == 1 else AMBER) if k < loss[i] else "E3E8EC"
                deck.rect(s, x0 + 50 + k * 54, 372, 50, 22, fill=fill)
            t(deck, s, x0 + 220, 371, 100, 24, cells[2], size=15, bold=True, color=INK, wrap=False)
        else:
            deck.icon(s, "ruler", x0 + 50, 370, size=24, color=AMBER_D, stroke=2.0)
            t(deck, s, x0 + 82, 372, 240, 24, cells[2], size=15, bold=True, color=AMBER_D)
    t(deck, s, X3[0], 420, W3, 20, "损耗刻度：一格最低，三格最高", size=12, color=FAINT)
    # payback: two years of savings fill the investment
    y0 = 500
    deck.icon(s, "coins", L, y0 + 4, size=28, color=G, stroke=2.0)
    t(deck, s, L + 38, y0 + 4, 260, 26, "自建两年收回", size=19, bold=True, color=G)
    bx, bw = 330, 600
    deck.rect(s, bx, y0, bw / 2 - 2, 36, fill=G2)
    deck.rect(s, bx + bw / 2 + 2, y0, bw / 2 - 2, 36, fill=G)
    t(deck, s, bx, y0 + 8, bw / 2, 22, "第 1 年少损耗 1,200 万", size=14, bold=True, color="FFFFFF", align="center")
    t(deck, s, bx + bw / 2, y0 + 8, bw / 2, 22, "第 2 年少损耗 1,200 万", size=14, bold=True, color="FFFFFF",
      align="center")
    deck.line(s, bx, y0 + 52, bx + bw, y0 + 52, color=INK, width=1.2)
    deck.line(s, bx, y0 + 46, bx, y0 + 58, color=INK, width=1.2)
    deck.line(s, bx + bw, y0 + 46, bx + bw, y0 + 58, color=INK, width=1.2)
    t(deck, s, bx, y0 + 62, bw, 22, "= 投入 2,400 万元", size=15, bold=True, color=INK, align="center")
