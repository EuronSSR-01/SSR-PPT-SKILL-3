"""改写：the same page before and after, inside a company template. The "a" page is the usual text version
(labels and sentences, icons only in the headings); the "b" page (and "c" for C04) is drawn from the same
material, keeps every item with its qualifiers (约、预计、估算, time starts, conditions) and carries most of
them with pictures: illustrations, time bars, dot and icon arrays, flow bands, proportion bars, charts.

Three fictional organisations, each with its own template frame, stand in for real company templates:
青川医院 (header band), 启明中学 (side bar), 恒川电机 (top rule, footer logo). Their colours and fonts are
kept; pictures go inside the content area. Every name and number is invented; each page's material is
the FACTS list next to it, and the A, B (and C) pages are drawn from that same list and its numbers.

Type sizes are canvas px on 1280 x 720 (pt = px x 0.75): labels beside pictures at least 16px (12pt),
sentences 18px or more; only footers go below that."""
from pathlib import Path

from gallery import example
from look import SANS

HERE = Path(__file__).resolve().parent
COMPRESSOR = HERE / "art" / "air-compressor.svg"   # drawn for this example, see assets/illustrations/README.md
FONTS = ("Noto Sans SC",)


def width_of(text, size):
    return sum(size if ord(c) > 255 else size * 0.56 for c in text)


def t(deck, s, x, y, w, h, content, size=18, color="1E2433", bold=False, align="left", **kw):
    return deck.text(s, x, y, w, h, content, size=size, font=SANS, color=color, bold=bold, align=align, **kw)


def num(deck, s, x, y, w, value, unit, size=34, color="1E2433", unit_size=None, align="left", pre=None):
    """A big number with its unit on one line; pre is a qualifier set small before it ("约", "≤")."""
    small = unit_size or max(16, int(size * 0.5))
    runs = [(pre + " ", {"size": small, "bold": True, "color": color})] if pre else []
    runs += [(value, {"size": size, "bold": True, "color": color}), (unit, {"size": small, "bold": True, "color": color})]
    t(deck, s, x, y, w, size * 1.3, [runs], wrap=False, align=align)


def chip(deck, s, x, y, text, color, size=16, fill="FFFFFF"):
    w = width_of(text, size) + 22
    deck.rect(s, x, y, w, size + 14, fill=fill, line=color, line_width=1.2, radius=(size + 14) / 2)
    t(deck, s, x, y + 6, w, size + 4, text, size=size, color=color, bold=True, align="center", wrap=False)
    return w


def machine(deck, s, x, y, body, screen, slot, w=28, h=46):
    """A small self-service kiosk: body, screen, slot."""
    deck.rect(s, x, y, w, h, fill=body, radius=3)
    deck.rect(s, x + 5, y + 6, w - 10, 12, fill=screen, radius=2)
    deck.rect(s, x + 7, y + h - 15, w - 14, 4, fill=slot, radius=2)


def before_pairs(deck, s, x, y, w, items, label_color, step=92):
    """The 'before' habit: a label and a sentence, repeated down a column."""
    for label, value in items:
        t(deck, s, x, y, w, 22, label, size=16, bold=True, color=label_color)
        t(deck, s, x, y + 26, w, 52, value, size=18, color="4F5866", line_spacing=1.3)
        y += step


def bullets(deck, s, x, y, w, lines, color="4F5866", size=18, step=40, h=30):
    for line in lines:
        t(deck, s, x, y, w, h, "· " + line, size=size, color=color, line_spacing=1.3)
        y += step
    return y


# ================================================================== 青川医院：页眉色带
A = dict(main="0F5C6E", mid="2A8C9E", soft="7FB9C4", tint="E3F1F3", hot="E2725B", hot_d="B24A33",
         ink="1E2B33", muted="56636B", faint="8C979E", panel="F1F6F7", grey="C3CDD1")
A_L, A_R = 64, 1216


def frame_hospital(deck, s, title, page, section):
    """青川医院 template: full-width colour band holding the title, a cross mark and the section."""
    deck.rect(s, 0, 0, 1280, 88, fill=A["main"])
    deck.rect(s, A_L + 9, 30, 10, 30, fill="FFFFFF", radius=2)
    deck.rect(s, A_L, 39, 28, 10, fill="FFFFFF", radius=2)
    t(deck, s, A_L + 46, 22, 860, 44, title, size=30, bold=True, color="FFFFFF")
    t(deck, s, 960, 34, A_R - 960, 24, f"{section} · {page:02d}", size=16, color="CFE7EC", align="right")
    t(deck, s, A_L, 684, 600, 20, "青川医院 · 门诊部 · 虚构示例", size=13, color=A["faint"])


# ------------------------------------------------------------------ C01 门诊时间
VISIT = dict(month="9 月", online=72, wait=38, wait_before=52, target=25, target_by="12 月前", consult=9,
             pay=4, pickup=6, kiosks=6, total=57, tests="约四成", blood="预计 2 小时内")
V = VISIT
VISIT_FACTS = [
    f"{V['month']}门诊运营数据。",
    f"线上预约占 {V['online']}%，现场挂号占 {100 - V['online']}%。",
    f"签到后平均候诊 {V['wait']} 分钟；8 月平均为 {V['wait_before']} 分钟。",
    f"目标：{V['target_by']}把候诊降到 {V['target']} 分钟以内。",
    f"医生问诊平均约 {V['consult']} 分钟。",
    f"{V['tests']}患者需要做检查，抽血结果{V['blood']}出。",
    f"诊间扫码缴费，平均 {V['pay']} 分钟。",
    f"自助取药机 {V['kiosks']} 台，取药平均 {V['pickup']} 分钟。",
    f"不需要做检查的患者，从签到到取药平均 {V['total']} 分钟。",
]
VISIT_TITLE = "看一次门诊：近三分之二的时间在候诊"


@example("convert", "C01-a", "门诊时间 A：改写前，四栏标签加句子",
         "四栏“标签＋句子”：每格都要读，看不出时间花在哪一段、候诊比问诊长多少。"
         "材料与 B 页相同（convert_examples.py 的 VISIT_FACTS），12 条信息全是字。", fonts=FONTS)
def visit_before(deck, s):
    frame_hospital(deck, s, VISIT_TITLE, 3, "门诊运营")
    t(deck, s, A_L, 108, 900, 26, f"{V['month']}门诊运营数据", size=18, color=A["muted"])
    cols = [
        ("挂号", "smartphone", [("方式", f"线上预约占 {V['online']}%，现场挂号占 {100 - V['online']}%")]),
        ("候诊", "hourglass", [("时长", f"签到后平均候诊 {V['wait']} 分钟"), ("变化", f"8 月平均为 {V['wait_before']} 分钟"),
                               ("目标", f"{V['target_by']}降到 {V['target']} 分钟以内")]),
        ("问诊与检查", "clipboard-list", [("问诊", f"医生问诊平均约 {V['consult']} 分钟"),
                                          ("检查", f"{V['tests']}患者需要做检查"), ("抽血", f"结果{V['blood']}出")]),
        ("缴费与取药", "package", [("缴费", f"诊间扫码缴费，平均 {V['pay']} 分钟"),
                                   ("取药", f"自助取药机 {V['kiosks']} 台，平均 {V['pickup']} 分钟")]),
    ]
    for i, (name, icon, items) in enumerate(cols):
        x = A_L + i * 292
        deck.rect(s, x, 148, 276, 50, fill=A["panel"])
        deck.icon(s, icon, x + 14, 160, size=26, color=A["mid"], stroke=2.0)
        t(deck, s, x + 50, 159, 220, 28, name, size=20, bold=True, color=A["ink"])
        before_pairs(deck, s, x, 218, 276, items, A["mid"], step=100)
    deck.line(s, A_L, 540, A_R, 540, color="DCE3E6", width=1)
    before_pairs(deck, s, A_L, 560, 1152, [("全程", f"不需要做检查的患者，从签到到取药平均 {V['total']} 分钟。")], A["mid"])


@example("convert", "C01-b", "门诊时间 B：改写后，一根时间条加四张小图",
         "从签到到取药画成一根按分钟比例的时间条，候诊一段最长、用强调色；候诊的变化和目标画成三根条，"
         "挂号方式画成比例条，要做检查的患者画成十个人里涂四个，取药机画成六台。“不需要做检查”“约”“预计”都留在图旁。"
         "12 条信息：10 条在图里，字只剩标题和一行口径。", fonts=FONTS)
def visit_after(deck, s):
    frame_hospital(deck, s, VISIT_TITLE, 3, "门诊运营")
    t(deck, s, A_L, 112, 820, 26, [[(f"{V['month']}平均", {"bold": True, "color": A["main"]}),
                                     ("  ·  不需要做检查的患者，从签到到取药", {"color": A["muted"]})]], size=18)
    num(deck, s, 980, 100, A_R - 980, str(V["total"]), " 分钟", size=40, color=A["main"], align="right")
    deck.illustration(s, "hospital", A_L, 160, 150, 112, primary=A["mid"], accent=A["hot"])
    x0, x1, y0, h = 236, A_R, 190, 56
    scale = (x1 - x0) / V["total"]
    parts = [("候诊", V["wait"], A["hot"], "hourglass", f"{V['wait']} 分钟"),
             ("问诊", V["consult"], A["main"], "clipboard-list", f"约 {V['consult']} 分钟"),
             ("扫码缴费", V["pay"], A["mid"], "qr-code", f"{V['pay']} 分钟"),
             ("取药", V["pickup"], A["soft"], "package", f"{V['pickup']} 分钟")]
    x = x0
    for i, (name, minutes, colour, icon, label) in enumerate(parts):
        w = minutes * scale - (3 if i < len(parts) - 1 else 0)
        deck.rect(s, x, y0, w, h, fill=colour)
        if i == 0:
            deck.icon(s, icon, x + 18, y0 + 12, size=32, color="FFFFFF", stroke=2.2)
            t(deck, s, x + 62, y0 + 13, 300, 32, [[("候诊 ", {"size": 22}), (label, {"size": 24, "bold": True})]],
              color="FFFFFF", wrap=False)
        else:
            cx = x + w / 2
            deck.icon(s, icon, cx - 15, y0 - 40, size=30, color=A["main"], stroke=2.0)
            t(deck, s, cx - 60, y0 + h + 10, 120, 22, name, size=16, color=A["muted"], align="center")
            t(deck, s, cx - 60, y0 + h + 34, 120, 26, label, size=20, bold=True, color=A["ink"], align="center",
              wrap=False)
        x += minutes * scale

    panels = ["候诊在缩短（分钟）", "挂号方式", "要做检查的患者", "自助取药机"]
    for i, head in enumerate(panels):
        px = A_L + i * 292
        deck.rect(s, px, 344, 276, 300, fill=A["panel"], radius=10)
        t(deck, s, px + 20, 362, 240, 26, head, size=18, bold=True, color=A["ink"])
    # 1 waiting time: August, September, target
    px = A_L
    rows = [("8 月", V["wait_before"], A["grey"], A["muted"], str(V["wait_before"])),
            ("9 月", V["wait"], A["hot"], A["hot_d"], str(V["wait"])),
            ("目标", V["target"], None, A["main"], f"≤{V['target']}")]
    for k, (label, minutes, fill, ink, value) in enumerate(rows):
        y = 414 + k * 54
        t(deck, s, px + 20, y + 4, 50, 22, label, size=16, color=A["muted"])
        w = 150 * minutes / V["wait_before"]
        deck.rect(s, px + 70, y, w, 30, fill=fill, line=None if fill else A["main"], line_width=1.6, dash=not fill)
        t(deck, s, px + 78 + w, y + 2, 60, 26, value, size=20, bold=True, color=ink, wrap=False)
    t(deck, s, px + 20, 584, 240, 22, f"目标在{V['target_by']}达到", size=16, color=A["main"])
    # 2 how people book
    px = A_L + 292
    deck.icon(s, "smartphone", px + 20, 412, size=40, color=A["main"], stroke=1.8)
    deck.icon(s, "user", px + 216, 412, size=40, color=A["faint"], stroke=1.8)
    bw = 236
    deck.rect(s, px + 20, 470, bw * V["online"] / 100 - 2, 40, fill=A["main"])
    deck.rect(s, px + 20 + bw * V["online"] / 100, 470, bw * (100 - V["online"]) / 100, 40, fill=A["grey"])
    num(deck, s, px + 20, 522, 150, f"{V['online']}", "%", size=28, color=A["main"])
    t(deck, s, px + 20, 562, 150, 22, "线上预约", size=16, color=A["muted"])
    num(deck, s, px + 156, 522, 100, f"{100 - V['online']}", "%", size=28, color=A["muted"], align="right")
    t(deck, s, px + 156, 562, 100, 22, "现场挂号", size=16, color=A["muted"], align="right")
    # 3 four in ten need a test
    px = A_L + 2 * 292
    for k in range(10):
        deck.icon(s, "user", px + 20 + (k % 5) * 48, 404 + (k // 5) * 48, size=36,
                  color=A["hot"] if k < 4 else A["grey"], stroke=2.2)
    t(deck, s, px + 20, 510, 240, 32, [[(V["tests"], {"size": 24, "bold": True, "color": A["hot_d"]}),
                                        (" 要做检查", {"size": 16, "color": A["muted"]})]], wrap=False)
    deck.icon(s, "clock", px + 20, 566, size=26, color=A["main"], stroke=2.0)
    t(deck, s, px + 54, 568, 210, 24, f"抽血结果{V['blood']}出", size=16, color=A["ink"])
    # 4 self-service kiosks
    px = A_L + 3 * 292
    for k in range(V["kiosks"]):
        machine(deck, s, px + 20 + k * 38, 410, A["main"], A["tint"], "0B4654")
    num(deck, s, px + 20, 476, 200, str(V["kiosks"]), " 台", size=40, color=A["main"])


# ================================================================== 启明中学：左侧竖条
B = dict(main="283C7A", mid="4A62A8", soft="AEBBE0", tint="E8ECF7", gold="E9A23B", gold_d="A86A10",
         ink="1E2433", muted="5A6273", faint="8E95A3", panel="F4F5F9", grey="D3D8E2")
B_L, B_R = 88, 1192


def frame_school(deck, s, title, page, kicker):
    """启明中学 template: a full-height bar on the left with the mark and page number, a kicker above the
    title. The content area keeps equal margins from the page edges."""
    deck.rect(s, 0, 0, 36, 720, fill=B["main"])
    deck.icon(s, "book-open", 6, 26, size=24, color="FFFFFF", stroke=2.0)
    t(deck, s, 0, 684, 36, 20, f"{page:02d}", size=13, color="FFFFFF", align="center")
    t(deck, s, B_L, 28, 700, 22, kicker, size=15, bold=True, color=B["gold_d"], spacing=0.04)
    t(deck, s, B_L, 52, 1104, 44, title, size=30, bold=True, color=B["main"])
    t(deck, s, B_L, 684, 600, 20, "启明中学 · 虚构示例", size=13, color=B["faint"])


# ------------------------------------------------------------------ C03 图书馆改造
LIB = dict(seats=(120, 260), hours=((8, 17), (7.5, 21.5)), kiosks=4, rooms=6, room_size="6–8",
           visits=(310, 640), cost=380, grant="七成", own="三成", peak=300)
L_ = LIB
LIB_FACTS = [
    f"座位从 {L_['seats'][0]} 个增加到 {L_['seats'][1]} 个。",
    "开放时间（周一至周五）从 8:00–17:00 延长到 7:30–21:30。",
    f"新增自助借还机 {L_['kiosks']} 台，原来没有。",
    f"新增小组讨论室 {L_['rooms']} 间，每间可坐 {L_['room_size']} 人。",
    f"9 月日均进馆约 {L_['visits'][1]} 人次，去年 9 月约 {L_['visits'][0]} 人次。",
    f"改造费用约 {L_['cost']} 万元，区教育局专项承担约{L_['grant']}，学校自筹约{L_['own']}。",
    f"期中考试周预计高峰需要约 {L_['peak']} 个座位，仍差约 {L_['peak'] - L_['seats'][1]} 个。",
    "建议下学期试点周六开放。",
]
LIB_TITLE = "图书馆改造后：座位翻倍，晚上开到 21:30"


@example("convert", "C03-a", "图书馆改造 A：改写前，两栏要点",
         "改造前后的变化写成一列句子，费用和下一步写在右边：座位、时间、人次都要读完才比得出。"
         "材料与 B 页相同（LIB_FACTS），10 条信息全是字。", fonts=FONTS)
def library_before(deck, s):
    frame_school(deck, s, LIB_TITLE, 4, "图书馆改造 · 9 月汇报")
    t(deck, s, B_L, 124, 600, 28, "改造带来的变化", size=20, bold=True, color=B["main"])
    bullets(deck, s, B_L, 168, 600, LIB_FACTS[:5], step=56, h=50)
    deck.rect(s, 736, 124, B_R - 736, 400, fill=B["panel"], radius=10)
    t(deck, s, 760, 144, 400, 28, "费用", size=20, bold=True, color=B["main"])
    bullets(deck, s, 760, 184, B_R - 784, LIB_FACTS[5:6], h=80)
    t(deck, s, 760, 300, 400, 28, "下一步", size=20, bold=True, color=B["main"])
    bullets(deck, s, 760, 340, B_R - 784, LIB_FACTS[6:], step=80, h=76)


@example("convert", "C03-b", "图书馆改造 B：改写后，六个小图各管一件事",
         "座位画成方格（一格 20 个，考试周还差的两格用虚线），开放时间画在一条时间轴上、晚上延长的一段换色，"
         "人次画成两根柱，新增的借还机和讨论室直接画出台数和间数，费用画成比例条，建议画成一周七格、周六虚线。"
         "10 条信息：9 条在图里。", fonts=FONTS)
def library_after(deck, s):
    frame_school(deck, s, LIB_TITLE, 4, "图书馆改造 · 9 月汇报")
    cols, rows, w, h = [B_L, 464, 840], [116, 392], 352, 256
    heads = ["座位", "开放时间（周一至周五）", "日均进馆（人次）", "新增设施", f"改造费用", "下学期"]
    for i, head in enumerate(heads):
        x, y = cols[i % 3], rows[i // 3]
        deck.rect(s, x, y, w, h, fill=B["panel"], radius=10)
        t(deck, s, x + 20, y + 16, w - 40, 26, head, size=18, bold=True, color=B["ink"])

    # seats: one square = 20 seats
    x, y = cols[0], rows[0]
    before, after = L_["seats"]
    lines = [(f"改造前 ", str(before), before // 20, B["soft"], B["muted"]),
             ("改造后 ", str(after), after // 20, B["main"], B["main"])]
    for k, (label, value, n, fill, ink) in enumerate(lines):
        yy = y + 52 + k * 58
        t(deck, s, x + 20, yy, 300, 24, [[(label, {"color": B["muted"]}), (value, {"bold": True, "color": ink,
                                                                               "size": 20})]], size=16)
        for q in range(n):
            deck.rect(s, x + 20 + q * 21, yy + 28, 16, 16, fill=fill, radius=2)
    yy = y + 168
    gap = (L_["peak"] - after) // 20
    t(deck, s, x + 20, yy, 320, 24, [[("考试周预计需要约 ", {"color": B["muted"]}),
                                      (str(L_["peak"]), {"bold": True, "color": B["gold_d"], "size": 20}),
                                      ("，差约 ", {"color": B["muted"]}),
                                      (str(L_["peak"] - after), {"bold": True, "color": B["gold_d"], "size": 20})]],
      size=16)
    for q in range(after // 20 + gap):
        filled = q < after // 20
        deck.rect(s, x + 20 + q * 21, yy + 28, 16, 16, fill=B["grey"] if filled else None,
                  line=None if filled else B["gold_d"], line_width=1.4, dash=not filled, radius=2)
    t(deck, s, x + 20, y + h - 34, 300, 20, "一格 = 20 个座位", size=16, color=B["faint"])

    # opening hours on a 7:00-22:00 axis
    x, y = cols[1], rows[0]
    ax0, ax1 = x + 20, x + w - 20
    hx = lambda hour: ax0 + (hour - 7) * (ax1 - ax0) / 15
    (b0, b1), (a0, a1) = L_["hours"]
    t(deck, s, x + 20, y + 54, 200, 22, "改造前", size=16, color=B["muted"])
    deck.rect(s, hx(b0), y + 80, hx(b1) - hx(b0), 30, fill=B["soft"])
    t(deck, s, hx(b0), y + 85, hx(b1) - hx(b0), 22, "8:00–17:00", size=16, bold=True, color=B["ink"],
      align="center")
    t(deck, s, x + 20, y + 120, 200, 22, "改造后", size=16, bold=True, color=B["main"])
    deck.rect(s, hx(a0), y + 146, hx(17) - hx(a0), 30, fill=B["main"])
    deck.rect(s, hx(17), y + 146, hx(a1) - hx(17), 30, fill=B["gold"])
    t(deck, s, hx(a0) + 6, y + 151, 80, 22, "7:30", size=16, bold=True, color="FFFFFF")
    t(deck, s, hx(a1) - 66, y + 151, 60, 22, "21:30", size=16, bold=True, color=B["ink"], align="right")
    deck.line(s, ax0, y + 194, ax1, y + 194, color=B["faint"], width=1)
    for hour in (8, 12, 16, 20):
        deck.line(s, hx(hour), y + 190, hx(hour), y + 198, color=B["faint"], width=1)
        t(deck, s, hx(hour) - 30, y + 204, 60, 20, f"{hour} 时", size=16, color=B["faint"], align="center")

    # visits per day: last September vs this September
    x, y = cols[2], rows[0]
    base, top = y + 206, 118
    for k, (label, value, fill, ink, size) in enumerate((("去年 9 月", L_["visits"][0], B["soft"], B["muted"], 20),
                                                         ("今年 9 月", L_["visits"][1], B["main"], B["main"], 24))):
        bx = x + 56 + k * 140
        bh = top * value / L_["visits"][1]
        deck.rect(s, bx, base - bh, 96, bh, fill=fill)
        t(deck, s, bx - 22, base - bh - 34, 140, 30, f"约 {value}", size=size, bold=True, color=ink, align="center")
        t(deck, s, bx - 22, base + 10, 140, 22, label, size=16, color=B["muted"], align="center")

    # new facilities: kiosks and group rooms, drawn one by one
    x, y = cols[0], rows[1]
    chip(deck, s, x + w - 120, y + 14, "原来没有", B["gold_d"])
    for k in range(L_["kiosks"]):
        machine(deck, s, x + 20 + k * 40, y + 60, B["main"], B["tint"], "1B2A57")
    num(deck, s, x + 196, y + 56, 60, str(L_["kiosks"]), " 台", size=30, color=B["main"])
    t(deck, s, x + 196, y + 96, 140, 22, "自助借还机", size=16, color=B["muted"])
    for k in range(L_["rooms"]):
        deck.rect(s, x + 20 + k * 52, y + 136, 44, 44, fill=B["tint"], line=B["mid"], line_width=1.2, radius=6)
        deck.icon(s, "users", x + 30 + k * 52, y + 146, size=24, color=B["main"], stroke=2.0)
    t(deck, s, x + 20, y + 194, 320, 26, [[("讨论室 ", {"color": B["muted"]}),
                                           (f"{L_['rooms']} 间", {"bold": True, "color": B["main"], "size": 20}),
                                           (f" · 每间 {L_['room_size']} 人", {"color": B["muted"]})]], size=16)

    # cost and who pays
    x, y = cols[1], rows[1]
    num(deck, s, x + 20, y + 52, 300, str(L_["cost"]), " 万元", size=40, color=B["main"], pre="约")
    bw = w - 40
    deck.rect(s, x + 20, y + 124, bw * 0.7 - 2, 40, fill=B["main"])
    deck.rect(s, x + 20 + bw * 0.7, y + 124, bw * 0.3, 40, fill=B["soft"])
    t(deck, s, x + 20, y + 133, bw * 0.7 - 2, 22, f"约{L_['grant']}", size=16, bold=True, color="FFFFFF",
      align="center")
    t(deck, s, x + 20 + bw * 0.7, y + 133, bw * 0.3, 22, f"约{L_['own']}", size=16, bold=True, color=B["ink"],
      align="center")
    deck.icon(s, "landmark", x + 20, y + 178, size=24, color=B["main"], stroke=2.0)
    t(deck, s, x + 50, y + 180, 150, 22, "区教育局专项", size=16, color=B["ink"])
    deck.icon(s, "school", x + w - 44, y + 178, size=24, color=B["mid"], stroke=2.0)
    t(deck, s, x + w - 140, y + 180, 90, 22, "学校自筹", size=16, color=B["muted"], align="right")

    # proposal: open on Saturdays next term
    x, y = cols[2], rows[1]
    deck.illustration(s, "school", x + 196, y + 34, 136, 100, primary=B["mid"], accent=B["gold"])
    chip(deck, s, x + 20, y + 58, "建议", B["gold_d"])
    t(deck, s, x + 20, y + 100, 180, 28, "试点周六开放", size=20, bold=True, color=B["ink"])
    for k, day in enumerate("一二三四五六日"):
        dx = x + 20 + k * 45
        if k < 5:
            deck.rect(s, dx, y + 156, 40, 40, fill=B["main"], radius=4)
            colour = "FFFFFF"
        elif k == 5:
            deck.rect(s, dx, y + 156, 40, 40, fill="FFFFFF", line=B["gold_d"], line_width=1.6, dash=True, radius=4)
            colour = B["gold_d"]
        else:
            deck.rect(s, dx, y + 156, 40, 40, fill="FFFFFF", line=B["grey"], line_width=1.2, radius=4)
            colour = B["faint"]
        t(deck, s, dx, y + 165, 40, 22, day, size=16, bold=True, color=colour, align="center")
    t(deck, s, x + 20, y + 206, 320, 22, "实色为开放日，虚线为试点", size=16, color=B["faint"])


# ------------------------------------------------------------------ C04 开放日人数：位置和排序
SITES = [("实验楼", 1240), ("宿舍样板间", 1050), ("图书馆", 980), ("体育馆", 860), ("食堂", 610), ("艺术楼", 420),
         ("校史馆", 260)]
OPEN_DAY = dict(date="10 月 12 日 9:00–16:00", count="人次为志愿者每小时点数相加，约数", busy=1000, queue="20 分钟",
                gate="南门")
O = OPEN_DAY
OPEN_FACTS = [f"{name}：约 {n:,} 人次。" for name, n in SITES] + [
    f"开放时间 {O['date']}；{O['count']}。",
    f"超过 1,000 人次的两处，下午排队超过 {O['queue']}。",
    f"入口在{O['gate']}。",
]
OPEN_TITLE = "开放日：实验楼和宿舍样板间人最多"
# rough positions on the campus (not to scale, no paths: the material gives none)
PLACES = {"宿舍样板间": (610, 196), "实验楼": (262, 250), "体育馆": (664, 396), "图书馆": (430, 372),
          "艺术楼": (210, 452), "食堂": (590, 520), "校史馆": (300, 548)}


@example("convert", "C04-a", "开放日人数 A：改写前，七行数字",
         "七个展点一行一个数字，排队和入口写在最后：要逐行读、自己比大小，也看不出人挤在哪里。"
         "材料与 B、C 页相同（SITES、OPEN_FACTS），11 条信息全是字。", fonts=FONTS)
def open_day_before(deck, s):
    frame_school(deck, s, OPEN_TITLE, 6, "校园开放日 · 复盘")
    t(deck, s, B_L, 116, 1104, 26, f"{O['date']} · {O['count']}", size=18, color=B["muted"])
    for i, (name, n) in enumerate(SITES):
        x, y = B_L + (i % 2) * 560, 168 + (i // 2) * 76
        t(deck, s, x, y, 520, 28, name, size=20, bold=True, color=B["main"])
        t(deck, s, x, y + 32, 520, 26, f"到访约 {n:,} 人次。", size=18, color=B["muted"])
    deck.line(s, B_L, 488, B_R, 488, color=B["grey"], width=1)
    bullets(deck, s, B_L, 508, 1104, OPEN_FACTS[-2:], step=44)


@example("convert", "C04-b", "开放日人数 B：改写后，按大致位置摆",
         "展点按校园里的大致方位摆，圆越大人次越多，排长队的两处换色并配沙漏，入口画在南门。"
         "看得出人挤在哪里、离入口多远，适合安排路线和志愿者；比较多少要在圆之间来回找。"
         "11 条信息：8 条在图里，时间和口径留在图例。", fonts=FONTS)
def open_day_place(deck, s):
    frame_school(deck, s, OPEN_TITLE, 6, "校园开放日 · 复盘")
    deck.rect(s, B_L, 116, 760, 536, fill=B["panel"], radius=14)
    for name, n in SITES:
        cx, cy = PLACES[name]
        r = 1.3 * n ** 0.5
        busy = n > O["busy"]
        deck.ellipse(s, cx, cy, r, fill=B["gold"] if busy else B["mid"])
        lx = cx + r + 12
        if busy:
            deck.icon(s, "hourglass", lx, cy - 30, size=24, color=B["gold_d"], stroke=2.2)
        t(deck, s, lx + (30 if busy else 0), cy - 30, 160, 26, name, size=18, bold=True, color=B["ink"], wrap=False)
        t(deck, s, lx, cy + 2, 140, 22, f"约 {n:,}", size=16, color=B["muted"], wrap=False)
    gx, gy = 468, 600  # the south gate: two posts and a lintel on the campus edge
    deck.rect(s, gx - 40, gy, 12, 52, fill=B["main"], radius=2)
    deck.rect(s, gx + 28, gy, 12, 52, fill=B["main"], radius=2)
    deck.rect(s, gx - 48, gy - 8, 96, 12, fill=B["main"], radius=3)
    t(deck, s, gx + 56, gy + 14, 160, 24, f"{O['gate']} · 入口", size=18, bold=True, color=B["main"])
    lx = 880
    t(deck, s, lx, 124, 312, 26, "怎么看", size=18, bold=True, color=B["ink"])
    deck.ellipse(s, lx + 16, 186, 16, fill=B["mid"])
    deck.ellipse(s, lx + 54, 186, 9, fill=B["mid"])
    t(deck, s, lx + 76, 175, 230, 22, "圆越大，人次越多", size=16, color=B["ink"])
    deck.ellipse(s, lx + 16, 236, 16, fill=B["gold"])
    deck.icon(s, "hourglass", lx + 44, 224, size=24, color=B["gold_d"], stroke=2.2)
    t(deck, s, lx + 76, 214, 236, 46, f"超过 1,000 人次，\n下午排队超过 {O['queue']}", size=16, color=B["ink"],
      line_spacing=1.25)
    deck.line(s, lx, 288, B_R, 288, color=B["grey"], width=1)
    t(deck, s, lx, 302, 312, 120, [O["date"], O["count"], "位置为大致方位，不按比例"], size=16, color=B["muted"],
      line_spacing=1.35, space_after=6)


@example("convert", "C04-c", "开放日人数 C：同一份数据，按人次排序",
         "同样的七个数按多少排成条形图，超过 1,000 的两根换色、旁边写排队：一眼比出谁多谁少，适合排名和取舍；"
         "看不出位置，入口只能写在旁边。B、C 都没丢信息，按这一页要回答的问题选：问“在哪里”用位置，问“谁多”用排序。",
         fonts=FONTS)
def open_day_sorted(deck, s):
    frame_school(deck, s, OPEN_TITLE, 6, "校园开放日 · 复盘")
    t(deck, s, B_L, 116, 760, 26, "到访人次，从多到少（约数）", size=18, color=B["muted"])
    names = [n for n, _ in SITES]
    deck.bar_chart(s, B_L, 150, 760, 500, names, [v for _, v in SITES], highlight=[0, 1], color=B["gold"],
                   base=B["soft"], font=SANS, size=18, label_color=B["ink"], axis_color=B["ink"], gap_width=55,
                   number_format="#,##0")
    lx = 880
    deck.rect(s, lx, 150, B_R - lx, 102, fill=B["panel"], radius=10)
    deck.rect(s, lx + 20, 174, 28, 18, fill=B["gold"])
    deck.icon(s, "hourglass", lx + 22, 208, size=24, color=B["gold_d"], stroke=2.2)
    t(deck, s, lx + 64, 170, 240, 60, f"超过 1,000 人次的两处\n下午排队超过 {O['queue']}", size=18, bold=True,
      color=B["ink"], line_spacing=1.3)
    deck.icon(s, "flag", lx, 300, size=24, color=B["main"], stroke=2.0)
    t(deck, s, lx + 34, 301, 280, 24, f"入口在{O['gate']}", size=16, color=B["ink"])
    t(deck, s, lx, 350, 312, 100, [O["date"], O["count"]], size=16, color=B["muted"], line_spacing=1.35,
      space_after=6)


# ================================================================== 恒川电机：顶部细条，页脚标志
C = dict(main="2F5D7C", mid="5E88A6", soft="A9C1D3", tint="E6EDF2", hot="E8742A", hot_d="B4521A",
         ink="23262B", muted="5C636D", faint="8F959D", panel="F3F4F6", warm="FFF1E6", grey="CDD3D9")
C_L, C_R = 64, 1216


def frame_factory(deck, s, title, page):
    """恒川电机 template: an orange rule along the top edge, a short rule under the title, the logo and
    page number together at the bottom left."""
    deck.rect(s, 0, 0, 1280, 8, fill=C["hot"])
    t(deck, s, C_L, 34, 1120, 46, title, size=30, bold=True, color=C["ink"])
    deck.rect(s, C_L, 90, 56, 4, fill=C["hot"])
    t(deck, s, C_L, 680, 700, 22, [[("恒川电机", {"bold": True, "color": C["ink"], "size": 16}),
                                    (f"   |   设备部 · 虚构示例   |   {page:02d}", {"color": C["faint"]})]], size=13)


# ------------------------------------------------------------------ C02 边角料去向
SCRAP = dict(total=120, melt=70, sell=38, landfill=12, period="1–9 月平均", buyers=2, pickups="每周 2 次",
             landfill_fee=180, cement_fee=260, extra="约 1.2 万元")
S_ = SCRAP
SCRAP_FACTS = [
    f"冲压和绕线每月产生边角料约 {S_['total']} 吨（{S_['period']}）。",
    f"约 {S_['melt']} 吨回炉，在本厂铸造车间自用。",
    f"约 {S_['sell']} 吨卖给 {S_['buyers']} 家回收商，按吨结算、月结；回收商上门拉运，{S_['pickups']}。",
    f"约 {S_['landfill']} 吨送填埋场，主要是漆包线头和油污铁屑；填埋处置费每吨约 {S_['landfill_fee']} 元。",
    "建议：填埋部分改为与水泥厂协同处置，预计明年起填埋降到 0。",
    f"协同处置每吨约 {S_['cement_fee']} 元，比填埋高约 {S_['cement_fee'] - S_['landfill_fee']} 元；预计每年多付{S_['extra']}。",
]
SCRAP_TITLE = f"边角料去向：每月约 {S_['total']} 吨，一成仍在填埋"


@example("convert", "C02-a", "边角料去向 A：改写前，分段要点",
         "三个去向各写一两句，建议放在右边：吨数、结算方式、处置费都埋在句子里，看不出量的大小和流向。"
         "材料与 B 页相同（SCRAP_FACTS），13 条信息全是字。", fonts=FONTS)
def scrap_before(deck, s):
    frame_factory(deck, s, SCRAP_TITLE, 6)
    t(deck, s, C_L, 116, 1150, 28, SCRAP_FACTS[0], size=18, color=C["ink"])
    y = 168
    for head, lines in (("回炉自用", [SCRAP_FACTS[1]]),
                        ("卖给回收商", [f"约 {S_['sell']} 吨卖给 {S_['buyers']} 家回收商，按吨结算、月结。",
                                    f"回收商上门拉运，{S_['pickups']}。"]),
                        ("填埋", [f"约 {S_['landfill']} 吨送填埋场，主要是漆包线头和油污铁屑。",
                                f"填埋处置费每吨约 {S_['landfill_fee']} 元。"])):
        t(deck, s, C_L, y, 600, 28, head, size=20, bold=True, color=C["main"])
        y = bullets(deck, s, C_L, y + 38, 640, lines) + 18
    deck.rect(s, 752, 168, C_R - 752, 300, fill=C["panel"], radius=10)
    t(deck, s, 776, 188, 400, 28, "建议", size=20, bold=True, color=C["hot_d"])
    bullets(deck, s, 776, 230, C_R - 800, ["填埋部分改为与水泥厂协同处置，预计明年起填埋降到 0。"], h=70)
    bullets(deck, s, 776, 310, C_R - 800, [f"协同处置每吨约 {S_['cement_fee']} 元，比填埋高约 "
                                          f"{S_['cement_fee'] - S_['landfill_fee']} 元。",
                                          f"预计每年多付{S_['extra']}。"], step=44)


@example("convert", "C02-b", "边角料去向 B：改写后，按吨数画宽窄的流向",
         "工厂插画出发，三条流向按吨数画宽窄（2 像素 = 1 吨），结算和拉运方式写在回收商那条上；"
         "回收商配货车插画，填埋一条换成强调色。建议画成填埋 12 → 0 和两根处置费条，多付的钱写成数字。"
         "13 条信息：10 条在图里。", fonts=FONTS)
def scrap_after(deck, s):
    frame_factory(deck, s, SCRAP_TITLE, 6)
    deck.illustration(s, "factory", C_L, 128, 200, 150, primary=C["main"], accent=C["hot"])
    num(deck, s, C_L, 288, 220, str(S_["total"]), " 吨/月", size=36, color=C["ink"], pre="约")
    t(deck, s, C_L, 340, 210, 50, ["冲压和绕线", S_["period"]], size=16, color=C["muted"], line_spacing=1.2)
    k = 2  # px per tonne
    src_x, bend0, bend1, end_x = 280, 400, 580, 760
    flows = [(S_["melt"], 112, C["main"]), (S_["sell"], 300, C["mid"]), (S_["landfill"], 470, C["hot"])]
    sy = 150
    for tonnes, dy, colour in flows:
        th = tonnes * k
        deck.polygon(s, [(src_x, sy), (bend0, sy), (bend1, dy), (end_x, dy), (end_x + 22, dy + th / 2),
                         (end_x, dy + th), (bend1, dy + th), (bend0, sy + th), (src_x, sy + th)], fill=colour)
        sy += th
    # how the sold part moves: on its band
    t(deck, s, bend1 + 10, 308, 170, 22, "按吨结算 · 月结", size=16, bold=True, color="FFFFFF", wrap=False)
    t(deck, s, bend1 + 10, 336, 170, 22, f"上门拉运 {S_['pickups']}", size=16, color="FFFFFF", wrap=False)
    dx = 800
    deck.icon(s, "recycle", dx, 140, size=44, color=C["main"], stroke=2.0)
    num(deck, s, dx + 58, 128, 300, str(S_["melt"]), " 吨", size=32, color=C["main"], pre="约")
    t(deck, s, dx + 58, 176, 340, 22, "回炉，铸造车间自用", size=16, color=C["muted"])
    deck.illustration(s, "truck", dx - 6, 300, 112, 76, primary=C["mid"], accent=C["hot"])
    num(deck, s, dx + 118, 300, 280, str(S_["sell"]), " 吨", size=28, color=C["mid"], pre="约")
    t(deck, s, dx + 118, 342, 280, 22, f"卖给 {S_['buyers']} 家回收商", size=16, color=C["muted"])
    deck.icon(s, "triangle-alert", dx, 458, size=32, color=C["hot"], stroke=2.0)
    num(deck, s, dx + 46, 448, 300, str(S_["landfill"]), " 吨送填埋", size=28, color=C["hot_d"], pre="约")
    t(deck, s, dx + 46, 490, 370, 22, f"漆包线头、油污铁屑 · 约 {S_['landfill_fee']} 元/吨", size=16,
      color=C["muted"])

    # proposal
    y0 = 540
    deck.rect(s, C_L, y0, C_R - C_L, 112, fill=C["warm"], radius=10)
    chip(deck, s, C_L + 20, y0 + 18, "建议", C["hot_d"])
    t(deck, s, C_L + 92, y0 + 20, 400, 28, "填埋改为水泥厂协同处置", size=20, bold=True, color=C["ink"])
    t(deck, s, C_L + 20, y0 + 66, 120, 30, [[(f"约 {S_['landfill']} 吨", {"color": C["faint"], "size": 20})]],
      wrap=False)
    deck.line(s, C_L + 112, y0 + 80, C_L + 170, y0 + 80, color=C["hot_d"], width=2, arrow=True)
    num(deck, s, C_L + 180, y0 + 60, 100, "0", " 吨", size=28, color=C["hot_d"])
    t(deck, s, C_L + 260, y0 + 70, 140, 22, "预计明年起", size=16, color=C["muted"])
    bx = 560
    t(deck, s, bx, y0 + 16, 260, 22, "每吨处置费（元）", size=16, color=C["muted"])
    for i, (label, fee, colour) in enumerate((("填埋", S_["landfill_fee"], C["grey"]),
                                              ("协同处置", S_["cement_fee"], C["hot"]))):
        yy = y0 + 46 + i * 30
        t(deck, s, bx, yy + 2, 70, 22, label, size=16, color=C["ink"])
        bw = 0.75 * fee
        deck.rect(s, bx + 76, yy + 2, bw, 22, fill=colour)
        t(deck, s, bx + 84 + bw, yy + 1, 70, 24, f"约 {fee}", size=16, bold=True, color=C["ink"], wrap=False)
    num(deck, s, 1000, y0 + 22, 200, "1.2", " 万元", size=30, color=C["hot_d"], align="right", pre="约")
    t(deck, s, 1000, y0 + 70, 200, 22, "预计每年多付", size=16, color=C["muted"], align="right")


# ------------------------------------------------------------------ C05 空压机方案
AIR = dict(age=14, power="约 10.4 万度", options=[
    dict(name="大修旧机", cost=45, cost_text="约 45 万元", down=10, saving=None, extra="预计再用约 3 年"),
    dict(name="换新变频机", cost=120, cost_text="约 120 万元", down=3, saving=30, extra=None),
    dict(name="租赁变频机", cost=None, cost_text="每月约 3.8 万元 · 5 年期", down=2, saving=30, extra=None)],
    pick=1, price=0.8, per_year=30, years=4)
AIR_FACTS = [
    f"现有空压机已用 {AIR['age']} 年，每月耗电{AIR['power']}。",
    "大修旧机：约 45 万元，停机约 10 天；电耗不变，预计还能用约 3 年。",
    "换新变频机：约 120 万元，停机约 3 天；电耗预计降约 30%。",
    "租赁变频机：每月租金约 3.8 万元，5 年期；停机约 2 天；电耗预计降约 30%。",
    f"推荐换新变频机：按电耗降约 30%、电价 {AIR['price']} 元/度估算，每年少付电费约 {AIR['per_year']} 万元，"
    f"预计约 {AIR['years']} 年收回。",
]
AIR_TITLE = f"空压机：建议换新变频机，预计约 {AIR['years']} 年收回"


@example("convert", "C05-a", "设备方案 A：改写前，三段方案说明",
         "三种做法各写一句，推荐和测算写在最后：投入、停机、电耗要在三句话之间来回比。"
         "材料与 B 页相同（AIR_FACTS），17 条信息全是字。", fonts=FONTS)
def air_before(deck, s):
    frame_factory(deck, s, AIR_TITLE, 9)
    t(deck, s, C_L, 116, 1150, 28, AIR_FACTS[0], size=18, color=C["ink"])
    for i, fact in enumerate(AIR_FACTS[1:4]):
        name, text = fact.split("：", 1)
        y = 170 + i * 92
        t(deck, s, C_L, y, 400, 28, name, size=20, bold=True, color=C["main"])
        t(deck, s, C_L, y + 36, 1150, 28, text, size=18, color=C["muted"])
    deck.rect(s, C_L, 460, C_R - C_L, 120, fill=C["panel"], radius=10)
    pick, reason = AIR_FACTS[4].split("：", 1)
    t(deck, s, C_L + 24, 480, 1100, 28, pick, size=20, bold=True, color=C["main"])
    t(deck, s, C_L + 24, 520, 1100, 50, reason, size=18, color=C["muted"], line_spacing=1.3)


@example("convert", "C05-b", "设备方案 B：改写后，三列同尺比较，回收画成四段",
         "每种做法配同一张空压机插画（为这个例子画的，见 art/air-compressor.svg）；一次性投入画成同一比例的条，"
         "租赁按月付、不和一次性投入比长短，写成数字；停机按天画方块，电耗画成剩下的长度；推荐的一列加底色。"
         "回收画成四段“每年约 30 万”拼成 120 万，“预计”“估算”和电价都留在旁边。17 条信息：14 条在图里。",
         fonts=FONTS)
def air_after(deck, s):
    frame_factory(deck, s, AIR_TITLE, 9)
    deck.icon(s, "hourglass", C_L, 112, size=24, color=C["muted"], stroke=2.0)
    t(deck, s, C_L + 32, 113, 260, 24, [[("现有空压机已用 ", {}), (f"{AIR['age']} 年", {"bold": True, "color": C["ink"]})]],
      size=16, color=C["muted"])
    deck.icon(s, "zap", C_L + 250, 112, size=24, color=C["muted"], stroke=2.0)
    t(deck, s, C_L + 282, 113, 300, 24, [[("每月耗电", {}), (AIR["power"], {"bold": True, "color": C["ink"]})]],
      size=16, color=C["muted"])
    xs, w = [C_L, 460, 856], 360
    deck.rect(s, xs[AIR["pick"]] - 4, 148, w + 8, 372, fill=C["tint"], radius=12)
    for i, (x, o) in enumerate(zip(xs, AIR["options"])):
        best = i == AIR["pick"]
        deck.illustration(s, str(COMPRESSOR), x + 100, 156, 160, 110, primary=C["main"] if best else C["soft"],
                          accent=C["hot"])
        if i == 0:
            deck.icon(s, "wrench", x + 262, 166, size=34, color=C["muted"], stroke=2.0)
        if i == 2:
            deck.icon(s, "file-signature", x + 262, 166, size=34, color=C["muted"], stroke=2.0)
        if best:
            chip(deck, s, x + 16, 162, "推荐", C["hot_d"])
        t(deck, s, x, 274, w, 30, o["name"], size=22, bold=True, color=C["main"] if best else C["ink"], align="center")
        # one-off cost, on one scale; the lease is monthly, so it is a number, not a bar
        t(deck, s, x + 16, 324, 54, 22, "投入", size=16, color=C["muted"])
        if o["cost"]:
            bw = 170 * o["cost"] / 120
            deck.rect(s, x + 70, 322, bw, 26, fill=C["main"] if best else C["soft"])
            t(deck, s, x + 78 + bw, 322, 120, 26, o["cost_text"].replace("元", ""), size=18, bold=True,
              color=C["ink"], wrap=False)
        else:
            t(deck, s, x + 70, 322, 290, 26, o["cost_text"].replace("元", ""), size=18, bold=True, color=C["ink"],
              wrap=False)
            t(deck, s, x + 70, 350, 290, 22, "按月付，不和一次性投入比长短", size=16, color=C["faint"])
        t(deck, s, x + 16, 386, 54, 22, "停机", size=16, color=C["muted"])
        for d in range(o["down"]):
            deck.rect(s, x + 70 + d * 19, 389, 15, 18, fill=C["hot"], radius=2)
        t(deck, s, x + 78 + o["down"] * 19, 384, 120, 26, f"约 {o['down']} 天", size=18, bold=True, color=C["ink"],
          wrap=False)
        t(deck, s, x + 16, 440, 54, 22, "电耗", size=16, color=C["muted"])
        if o["saving"]:
            keep = 170 * (100 - o["saving"]) / 100
            deck.rect(s, x + 70, 438, 170, 26, fill=None, line=C["grey"], line_width=1.2, dash=True)
            deck.rect(s, x + 70, 438, keep, 26, fill=C["main"] if best else C["soft"])
            t(deck, s, x + 248, 438, 110, 26, f"约 −{o['saving']}%", size=18, bold=True, color=C["ink"], wrap=False)
            t(deck, s, x + 70, 468, 200, 22, "预计", size=16, color=C["faint"])
        else:
            deck.rect(s, x + 70, 438, 170, 26, fill=C["grey"])
            t(deck, s, x + 248, 438, 110, 26, "不变", size=18, bold=True, color=C["ink"])
        if o["extra"]:
            deck.icon(s, "hourglass", x + 70, 480, size=22, color=C["muted"], stroke=2.0)
            t(deck, s, x + 100, 480, 240, 24, o["extra"], size=16, color=C["ink"])

    # payback of the recommended option: four years of savings fill the investment
    y0 = 546
    deck.icon(s, "coins", C_L, y0 + 2, size=28, color=C["main"], stroke=2.0)
    t(deck, s, C_L + 38, y0 + 2, 300, 28, "换新的回收（预计）", size=20, bold=True, color=C["main"])
    t(deck, s, C_L + 38, y0 + 38, 330, 48, f"按电耗降约 30%、电价 {AIR['price']} 元/度估算", size=16,
      color=C["muted"])
    bx, bw = 440, C_R - 440
    seg = bw / AIR["years"]
    for k in range(AIR["years"]):
        deck.rect(s, bx + k * seg, y0, seg - 4, 38, fill=C["main"] if k % 2 == 0 else C["mid"])
        t(deck, s, bx + k * seg, y0 + 9, seg - 4, 22, f"第 {k + 1} 年 约 {AIR['per_year']} 万", size=16, bold=True,
          color="FFFFFF", align="center")
    deck.line(s, bx, y0 + 54, C_R - 4, y0 + 54, color=C["ink"], width=1.2)
    deck.line(s, bx, y0 + 48, bx, y0 + 60, color=C["ink"], width=1.2)
    deck.line(s, C_R - 4, y0 + 48, C_R - 4, y0 + 60, color=C["ink"], width=1.2)
    t(deck, s, bx, y0 + 66, bw, 24, "= 投入约 120 万元", size=18, bold=True, color=C["ink"], align="center")
