"""Type specimens (section "type"): one page per font with the same headline, paragraph and numbers, then
pairings and a numbers comparison. Coverage figures were measured from the font files (fontTools cmap)."""
from gallery import bg, example

SANS = "Noto Sans SC"
INK, GRAY, LINE, ACCENT, PAPER = "1F2A37", "4F5866", "D9DEE5", "C2440A", "F6F7F9"
HEAD_CN = "把产地搬进社区"
BODY_CN = "清晨采摘的蔬菜，四小时内进入城市仓，按门店订单分拣，第二天上午摆上社区店的货架。"
HEAD_EN = "Fresh to the Neighbourhood"
BODY_EN = "Picked at dawn, sorted by noon, on the shelf by nine the next morning."
NUMS = "0123456789   5.9%   2,480 万元"

CJK = [
    ("T01", "思源黑体", "Noto Sans SC", "中文黑体 · SIL OFL 1.1 · Google Fonts / Adobe",
     [("Light", "Noto Sans SC Light", False), ("Regular", "Noto Sans SC", False), ("Medium", "Noto Sans SC Medium", False),
      ("Bold", "Noto Sans SC", True), ("Black", "Noto Sans SC Black", False)],
     "GB2312 常用汉字 6,763/6,763 · 约 2.7 万汉字",
     ["中性、清楚，字重从细到特粗都有", "正文首选；Black 做大标题和大数字", "默认感强：靠字号、字重和留白拉开层级"]),
    ("T02", "思源宋体", "Noto Serif SC", "中文宋体 · SIL OFL 1.1 · Google Fonts / Adobe",
     [("Light", "Noto Serif SC Light", False), ("Regular", "Noto Serif SC", False), ("SemiBold", "Noto Serif SC SemiBold", False),
      ("Bold", "Noto Serif SC", True), ("Black", "Noto Serif SC Black", False)],
     "GB2312 常用汉字 6,763/6,763 · 约 2.8 万汉字",
     ["编辑感、文化感、有权威", "结论标题、引文、需要细读的正文", "投影时细笔画会变淡，正文不小于 20px"]),
    ("T03", "鸿蒙黑体", "HarmonyOS Sans SC", "中文黑体 · 华为字体许可（可免费商用，不得修改字体文件）",
     [("Light", "HarmonyOS Sans SC Light", False), ("Regular", "HarmonyOS Sans SC", False),
      ("Medium", "HarmonyOS Sans SC Medium", False), ("Bold", "HarmonyOS Sans SC", True), ("Black", "HarmonyOS Sans SC Black", False)],
     "GB2312 常用汉字 6,763/6,763 · 约 2.7 万汉字",
     ["几何、现代、略宽，数字清楚", "产品、科技、发布会；标题正文都可", "许可不允许修改字体文件：网页子集化嵌入有争议"]),
    ("T04", "MiSans", "MiSans", "中文黑体 · 小米字体许可（可免费商用，条款以官网为准）",
     [("Light", "MiSans Light", False), ("Regular", "MiSans", False), ("Medium", "MiSans Medium", False),
      ("Semibold", "MiSans Semibold", False), ("Heavy", "MiSans Heavy", False)],
     "GB2312 常用汉字 6,763/6,763 · 约 2.7 万汉字",
     ["圆润、清爽、亲和，10 档字重", "消费、服务、人文主题；正文舒展", "嵌入网页前先读官网许可"]),
    ("T05", "得意黑", "Smiley Sans Oblique", "中文展示 · SIL OFL 1.1 · GitHub atelier-anchor",
     [("Oblique", "Smiley Sans Oblique", False)],
     "GB2312 常用汉字 6,763/6,763 · 约 8,100 汉字",
     ["窄、斜、硬朗，有态度", "只做大标题和海报感的短句", "一个字重、本身是斜体；生僻字和人名先查"]),
    ("T06", "霞鹜文楷", "LXGW WenKai", "中文楷体 · SIL OFL 1.1 · GitHub lxgw",
     [("Regular", "LXGW WenKai", False), ("Medium", "LXGW WenKai Medium", False)],
     "GB2312 常用汉字 6,763/6,763 · 约 2.8 万汉字",
     ["楷书感、温和，像手写", "引文、批注、故事性的短句，也能排长文", "与黑体同排时，字号大一档才平衡"]),
    ("T07", "站酷小薇", "ZCOOL XiaoWei", "中文展示 · SIL OFL 1.1 · Google Fonts",
     [("Regular", "ZCOOL XiaoWei", False)],
     "仅 GB2312 常用汉字 6,763 个 · 缺“·〇℃”",
     ["细、清雅、有文艺气", "品牌故事、文艺主题的标题和短句", "字库小：人名、生僻字和部分符号会缺"]),
    ("T08", "站酷庆科黄油体", "ZCOOL QingKe HuangYou", "中文展示 · SIL OFL 1.1 · Google Fonts",
     [("Regular", "ZCOOL QingKe HuangYou", False)],
     "GB2312 常用汉字 6,763/6,763 · 约 9,200 汉字 · 缺“·〇℃”",
     ["粗圆、俏皮，像手绘招牌", "活动、年轻品牌的大标题", "数字“7”像“1”：不要用它排数字"]),
    ("T09", "马善政楷书", "Ma Shan Zheng", "中文书法 · SIL OFL 1.1 · Google Fonts",
     [("Regular", "Ma Shan Zheng", False)],
     "仅 GB2312 常用汉字 6,763 个 · 缺“·〇℃”",
     ["毛笔书法，力度强", "单个大字做图形，或文化主题的题字", "只用于极少的字，不排正文"]),
]

LATIN = [
    ("T11", "Inter", "Inter", "西文无衬线 · SIL OFL 1.1",
     [("Regular", "Inter", False), ("Bold", "Inter", True), ("Black", "Inter Black", False)],
     ["中性，数字清楚，字重全", "数字和西文首选；配任何中文黑体", "表格数字用等宽数字（CSS tabular-nums）"]),
    ("T12", "Space Grotesk", "Space Grotesk", "西文无衬线 · SIL OFL 1.1",
     [("Regular", "Space Grotesk", False), ("Bold", "Space Grotesk", True)],
     ["几何感、字形有个性", "科技、设计类的标题和数字", "个性强，正文用 Inter 更稳"]),
    ("T13", "Bebas Neue / Oswald", "Bebas Neue", "西文窄体展示 · SIL OFL 1.1",
     [("Bebas Neue", "Bebas Neue", False), ("Oswald Bold", "Oswald", True)],
     ["窄体大写，海报感，省横向空间", "大数字、短标签、章节编号", "Bebas 只有大写、一个字重；不排长句"]),
    ("T14", "Archivo Black", "Archivo Black", "西文展示 · SIL OFL 1.1",
     [("Regular", "Archivo Black", False)],
     ["极粗、宽，冲击力强", "海报式大数字和短词", "只有一个字重"]),
    ("T15", "Playfair Display", "Playfair Display", "西文衬线展示 · SIL OFL 1.1",
     [("Regular", "Playfair Display", False), ("Bold", "Playfair Display", True)],
     ["高反差衬线，优雅", "品牌、奢华、杂志的大标题和大数字", "默认旧式数字（高低不齐），表格里不用"]),
    ("T16", "DM Serif Display", "DM Serif Display", "西文衬线展示 · SIL OFL 1.1",
     [("Regular", "DM Serif Display", False)],
     ["粗衬线标题，杂志感", "标题、引文、大数字", "只有一个字重"]),
    ("T17", "Cormorant Garamond", "Cormorant Garamond", "西文衬线 · SIL OFL 1.1",
     [("Regular", "Cormorant Garamond", False), ("Bold", "Cormorant Garamond", True)],
     ["古典、纤细、安静", "西文小注、成对的中英文标题", "笔画细，至少 18px"]),
    ("T18", "Source Serif 4", "Source Serif 4", "西文衬线正文 · SIL OFL 1.1",
     [("Regular", "Source Serif 4", False), ("Bold", "Source Serif 4", True)],
     ["耐读，数字整齐", "学术、报告的西文正文和图注", "标题用 Bold，正文用 Regular"]),
    ("T19", "JetBrains Mono / IBM Plex Mono", "JetBrains Mono", "等宽 · SIL OFL 1.1",
     [("JetBrains Mono", "JetBrains Mono", False), ("IBM Plex Mono", "IBM Plex Mono", False)],
     ["等宽，技术感", "代码、编号、规格、版本号", "中文要另配字体（ea 设为中文黑体）"]),
    ("T20", "Bahnschrift", "Bahnschrift", "西文无衬线 · Windows 自带（随系统授权）",
     [("Regular", "Bahnschrift", False), ("SemiBold Condensed", "Bahnschrift SemiBold Condensed", False)],
     ["DIN 风格，有窄体，大数字好看", "不能装字体时的稳妥数字字体（Windows）", "随系统授权：不嵌入网页、不随文件分发"]),
]


def header(deck, s, code, name_cn, name_en, tag, coverage=None):
    deck.text(s, 64, 40, 900, 30, [[(name_cn, {"bold": True, "color": INK}), ("   " + name_en, {"color": GRAY})]], size=20, font=SANS)
    deck.text(s, 64, 72, 1150, 24, tag + (f"   ·   {coverage}" if coverage else ""), size=14, font=SANS, color=GRAY)
    deck.rect(s, 64, 106, 1152, 1, fill=LINE)


def notes(deck, s, items, x=880, y=150):
    labels = ["效果", "用法", "注意"]
    for i, text in enumerate(items):
        yy = y + i * 92
        deck.text(s, x, yy, 340, 22, labels[i], size=14, font=SANS, bold=True, color=ACCENT if i == 2 else GRAY)
        deck.text(s, x, yy + 24, 336, 60, text, size=17, font=SANS, color=INK, line_spacing=1.45)


def _register_cjk(entry):
    code, cn, family, tag, weights, coverage, note = entry

    @example("type", code, f"{cn}（{family.replace(' Oblique', '')}）", note[0], (family,))
    def page(deck, s):
        bg(s, PAPER)
        header(deck, s, code, cn, family, tag, coverage)
        main = weights[-1] if len(weights) > 1 else weights[0]
        deck.text(s, 60, 130, 800, 150, HEAD_CN, size=104, font=main[1], bold=main[2], color=INK)
        reg = next((w for w in weights if w[0] in ("Regular", "Oblique")), weights[0])
        deck.text(s, 64, 300, 780, 100, BODY_CN, size=22, font=reg[1], bold=reg[2], color=INK, line_spacing=1.6)
        deck.text(s, 64, 410, 800, 80, NUMS, size=48, font=main[1], bold=main[2], color=ACCENT, wrap=False)
        deck.rect(s, 64, 512, 780, 1, fill=LINE)
        for i, (label, fam, bold) in enumerate(weights):
            x = 64 + i * 158
            deck.text(s, x, 530, 150, 70, "鲜 Aa", size=44, font=fam, bold=bold, color=INK)
            deck.text(s, x, 602, 150, 22, label, size=13, font=SANS, color=GRAY)
        notes(deck, s, note)
    return page


def _register_latin(entry):
    code, name, family, tag, weights, note = entry

    @example("type", code, name, note[0], (family,))
    def page(deck, s):
        bg(s, PAPER)
        header(deck, s, code, name, "", tag)
        main = weights[-1] if len(weights) > 1 else weights[0]
        deck.text(s, 60, 130, 800, 220, HEAD_EN, size=80, font=main[1], bold=main[2], ea=SANS, color=INK, line_spacing=1.05)
        deck.text(s, 64, 336, 780, 80, BODY_EN, size=22, font=weights[0][1], bold=weights[0][2], ea=SANS, color=INK,
                  line_spacing=1.5)
        deck.text(s, 64, 432, 800, 80, "0123456789  5.9%  $2,480", size=46, font=main[1], bold=main[2], ea=SANS,
                  color=ACCENT, wrap=False)
        deck.rect(s, 64, 512, 780, 1, fill=LINE)
        for i, (label, fam, bold) in enumerate(weights):
            x = 64 + i * 260
            deck.text(s, x, 530, 250, 70, "Ag 5.9%", size=44, font=fam, bold=bold, ea=SANS, color=INK, wrap=False)
            deck.text(s, x, 602, 250, 22, label, size=13, font=SANS, color=GRAY)
        notes(deck, s, note)
    return page


for _e in CJK:
    _register_cjk(_e)
for _e in LATIN:
    _register_latin(_e)


@example("type", "T10", "系统字体：微软雅黑、等线、宋体、楷体、黑体", "稳妥的回退：几乎每台 Windows 都有，PPTX 交给别人不会被替换。",
         ("Microsoft YaHei",))
def system_fonts(deck, s):
    bg(s, PAPER)
    header(deck, s, "T10", "系统字体", "Windows", "随操作系统授权 · 只作本机回退：不嵌入网页、不随文件分发")
    rows = [("微软雅黑", "Microsoft YaHei", True), ("等线", "DengXian", False), ("宋体", "SimSun", False),
            ("楷体", "KaiTi", False), ("黑体", "SimHei", False)]
    for i, (cn, fam, bold) in enumerate(rows):
        y = 130 + i * 100
        deck.text(s, 64, y + 18, 140, 30, cn, size=18, font=SANS, color=GRAY)
        deck.text(s, 200, y, 660, 80, HEAD_CN + "  5.9%", size=52, font=fam, bold=bold, color=INK, wrap=False)
        deck.rect(s, 64, y + 88, 780, 1, fill=LINE)
    notes(deck, s, ["人人都有，PPTX 在 WPS / PowerPoint 里不走样", "公司模板、需要别人继续编辑、不能装字体的场合",
                    "大家都在用：靠字号、字重、留白和构图拉开差异"])


PAIRS = [
    ("P01", "编辑对比：思源宋体 + 思源黑体 + Inter", "Noto Serif SC", True, "Noto Sans SC", "Inter", True, "FBF9F4", "1A1A1A", "D7263D"),
    ("P02", "现代无衬线：思源黑体 Black + Regular + Inter", "Noto Sans SC Black", False, "Noto Sans SC", "Inter Black", False,
     "FFFFFF", "111111", "1F3FFF"),
    ("P03", "产品科技：鸿蒙黑体 + JetBrains Mono", "HarmonyOS Sans SC", True, "HarmonyOS Sans SC", "JetBrains Mono", False,
     "0C1117", "E6EDF3", "4CC2FF"),
    ("P04", "年轻有力：得意黑 + 思源黑体 Medium + Archivo Black", "Smiley Sans Oblique", False, "Noto Sans SC Medium",
     "Archivo Black", False, "F2E94E", "0B0B0B", "2853ED"),
    ("P05", "人文温度：MiSans + 霞鹜文楷", "MiSans Heavy", False, "MiSans", "MiSans Heavy", False, "FBF6EF", "2D2A26", "B25435"),
    ("P06", "东方雅致：思源宋体 SemiBold + 霞鹜文楷 + Cormorant", "Noto Serif SC SemiBold", False, "LXGW WenKai",
     "Cormorant Garamond", False, "EFE9DE", "1E1D1B", "A8322D"),
    ("P07", "稳妥系统：微软雅黑 + 等线 + Bahnschrift", "Microsoft YaHei", True, "DengXian", "Bahnschrift SemiBold Condensed",
     False, "FFFFFF", "1F2A37", "C2440A"),
]


def _register_pair(entry):
    code, title, head, head_bold, body, num, num_bold, paper, ink, accent = entry

    @example("type", code, title, "同一页内容换一组字体搭配：标题、正文、数字各用一款。", (head, body, num))
    def page(deck, s):
        bg(s, paper)
        deck.text(s, 64, 40, 1100, 24, title, size=15, font=SANS, color=accent)
        deck.text(s, 64, 120, 720, 160, "损耗率半年\n降了 3.7 个百分点", size=56, font=head, bold=head_bold, color=ink,
                  line_spacing=1.2)
        deck.text(s, 64, 320, 640, 100, "3 月起门店按日订货，临期商品晚 8 点折扣；\n合肥、无锡还没有城市仓，是下半年的重点。", size=22,
                  font=body, color=ink, line_spacing=1.7)
        deck.text(s, 760, 150, 480, 220, "5.9%", size=170, font=num, bold=num_bold, ea=body, color=accent, wrap=False)
        deck.text(s, 770, 380, 460, 30, "6 月生鲜损耗率", size=20, font=body, color=ink)
        deck.rect(s, 64, 520, 1152, 1, fill=accent)
        deck.text(s, 64, 540, 1100, 60, [[("标题 ", {"color": accent}), (head + ("  Bold" if head_bold else ""), {}),
                                          ("    正文 ", {"color": accent}), (body, {}), ("    数字 ", {"color": accent}),
                                          (num, {})]], size=16, font=SANS, color=ink)
    return page


for _e in PAIRS:
    _register_pair(_e)


@example("type", "N01", "数字字体对比", "同一组数字在不同字体里：宽窄、高低、是否等宽都会影响表格和大数字。", ("Inter",))
def numbers(deck, s):
    bg(s, PAPER)
    header(deck, s, "N01", "数字字体对比", "", "同一组数字：2,480 万元 · 5.9% · 0123456789")
    fonts = [("思源黑体", "Noto Sans SC", True), ("Inter", "Inter", True), ("鸿蒙黑体", "HarmonyOS Sans SC", True),
             ("MiSans", "MiSans Semibold", False), ("Bahnschrift 窄体", "Bahnschrift SemiBold Condensed", False),
             ("Playfair（旧式数字）", "Playfair Display", True), ("Source Serif 4", "Source Serif 4", True),
             ("JetBrains Mono（等宽）", "JetBrains Mono", False), ("Bebas Neue", "Bebas Neue", False)]
    for i, (label, fam, bold) in enumerate(fonts):
        y = 124 + i * 62
        deck.text(s, 64, y + 14, 260, 26, label, size=16, font=SANS, color=GRAY)
        deck.text(s, 330, y, 900, 56, "2,480 万元   5.9%   0123456789", size=40, font=fam, bold=bold, ea=SANS, color=INK,
                  wrap=False)
        deck.rect(s, 64, y + 58, 1152, 1, fill=LINE)
