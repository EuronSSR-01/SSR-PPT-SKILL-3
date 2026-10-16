"""Layout examples L15-L24: pictures, people, reading pages, tables, endings, and two added archetypes
(L23 object callouts, L24 bento grid). Fictional content; photos are openly licensed (photos.json)."""
import content as C
from gallery import bg, crop, example, photo
from look import (ACCENT, ACCENT_LIGHT, FAINT, INK, LINE, M, MUTED, PRIMARY, PRIMARY_LIGHT, SANS, SANS_BLACK, SERIF,
                  W, WARM, ill, source, title)

F = (SANS,)


# ---------------------------------------------------------------- L15 full-bleed picture
@example("layouts", "L15-a", "全出血图 A：照片配文字", "主体留在左侧，文字落在右侧的叶子上；渐变只盖住文字这一侧。", F)
def bleed_photo(deck, s):
    deck.picture(s, photo("tomato-picking"), 0, 0, 1280, 720)
    deck.gradient_rect(s, 560, 0, 722, 720, [(0, "0E1B12", 0), (0.45, "0E1B12", 0.78), (1, "0E1B12", 0.9)])
    deck.text(s, 760, 250, 440, 140, "每一颗\n都在成熟那天摘下", size=48, font=SANS, bold=True, color="FFFFFF", line_spacing=1.25)
    deck.rect(s, 762, 400, 48, 3, fill=ACCENT)
    deck.text(s, 760, 420, 420, 70, "合作产地距城市仓不超过 200 公里", size=22, font=SANS, color="E3EBE5")


@example("layouts", "L15-b", "全出血图 B：夜景插画配一句话", "插画也可以铺满整页：把配色换成夜色，场景横跨底部，文字在上方。", F)
def bleed_illustration(deck, s):
    bg(s, "13213A")
    for x, y, r in ((180, 120, 2), (420, 70, 1.5), (760, 140, 2), (980, 60, 1.5), (1120, 170, 2), (300, 210, 1.5)):
        deck.ellipse(s, x, y, r, fill="FFFFFF", alpha=0.7)
    deck.ellipse(s, 1090, 110, 34, fill="F6E7B0")
    deck.ellipse(s, 1104, 100, 30, fill="13213A")
    deck.text(s, M, 120, 760, 80, "晚上 8 点以后", size=28, font=SANS, color="B9CBEA")
    deck.text(s, M, 170, 900, 100, "临期蔬菜打七折，第二天不过夜", size=52, font=SANS, bold=True, color="FFFFFF")
    ill(deck, s, ["city", "store", "shopping-cart", "person"], -20, 330, 1320, 390, primary="4A6FB3", accent="F2B13C",
        ink="0B1426", surface="2A3C5E", line="2F4166")


# ---------------------------------------------------------------- L16 picture + text
@example("layouts", "L16-a", "图文分屏 A：照片出血 7:5", "照片占 7 栏并出血到页边；文字挂在网格上，与照片的视觉中心对齐。", F)
def split_photo(deck, s):
    deck.picture(s, photo("potatoes"), 560, 0, 720, 720)
    deck.text(s, M, 190, 440, 150, "土豆出地，\n第二天进店", size=48, font=SANS, bold=True, color=INK, line_spacing=1.25)
    facts = [("clock", "4 小时内进城市仓"), ("warehouse", "按门店订单分拣"), ("store", "次日上午上架")]
    for i, (icon, text) in enumerate(facts):
        y = 380 + i * 64
        deck.icon(s, icon, M, y, size=30, color=PRIMARY)
        deck.text(s, M + 48, y + 1, 400, 34, text, size=22, font=SANS, color=INK)


@example("layouts", "L16-b", "图文分屏 B：插画半屏配三条事实", "插画讲“是什么”，右侧只放三条短事实，每条一个图标。", F)
def split_illustration(deck, s):
    deck.rect(s, 0, 0, 600, 720, fill=PRIMARY_LIGHT)
    ill(deck, s, "warehouse", 60, 190, 480, 360)
    deck.text(s, 680, 150, 520, 80, "城市仓：离门店 5 公里", size=40, font=SANS, bold=True, color=INK)
    facts = [("clock", "2 小时", "分拣完一天的订单"), ("boxes", "1,200 种", "按门店订单拆箱"), ("truck", "每日 3 趟", "补货到门店")]
    for i, (icon, big, small) in enumerate(facts):
        y = 270 + i * 110
        deck.icon(s, icon, 680, y + 6, size=36, color=ACCENT)
        deck.text(s, 736, y - 6, 200, 50, big, size=34, font=SANS_BLACK, color=INK)
        deck.text(s, 736, y + 46, 420, 30, small, size=19, font=SANS, color=MUTED)


# ---------------------------------------------------------------- L17 photo group
@example("layouts", "L17-a", "照片组 A：一主二辅", "主图占一半以上；两张小图补细节；间距统一 12px；图注一行。", F)
def photo_main(deck, s):
    title(deck, s, "颜色最鲜的时候上架", y=48, size=36)
    deck.picture(s, photo("squash"), M, 130, 740, 500)
    deck.picture(s, photo("radishes"), M + 752, 130, 368, 244)
    deck.picture(s, crop("tomatoes", (0.0, 0.25, 0.75, 1.0)), M + 752, 386, 368, 244)
    deck.text(s, M, 642, 900, 22, "照片：USDA（公有领域）；Jun Seita，CC BY 2.0（番茄，已裁切）", size=13, font=SANS, color=FAINT)


@example("layouts", "L17-b", "照片组 B：全景、中景、特写", "三种景别排成一行讲一个过程；等高条带，图注写“在哪、是什么”。", F)
def photo_strip(deck, s):
    title(deck, s, "产地、门店、餐桌", y=48, size=36)
    shots = [("farm", "产地 · 全景"), ("market-people", "门店 · 中景"), ("potatoes", "商品 · 特写")]
    for i, (key, cap) in enumerate(shots):
        x = M + i * 380
        deck.picture(s, photo(key), x, 130, 360, 460)
        deck.text(s, x, 604, 360, 30, cap, size=19, font=SANS, bold=True, color=INK)
    deck.text(s, M, 650, W, 22, "照片：~MVI~ (warped)，CC BY 2.0；Wonderlane，CC BY 2.0；rawpixel，CC0", size=13, font=SANS,
              color=FAINT)


# ---------------------------------------------------------------- L18 people
def avatar(deck, s, cx, cy, r, char, colour):
    deck.ellipse(s, cx, cy, r, fill=colour)
    deck.text(s, cx - r, cy - r * 0.62, 2 * r, r * 1.2, char, size=r * 0.95, font=SANS, bold=True, color="FFFFFF",
              align="center")


@example("layouts", "L18-a", "人物 A：三人并列", "没有统一的人像照片时，用同样大小的字头像；每人一句与本次任务相关的话。", F)
def people_row(deck, s):
    title(deck, s, "三位负责人，分别管门店、仓和数据")
    colours = [PRIMARY, ACCENT, "2E7D6B"]
    for i, (name, role, note) in enumerate(C.TEAM):
        x = M + i * 380
        avatar(deck, s, x + 80, 290, 80, name[0], colours[i])
        deck.text(s, x, 400, 340, 40, name, size=30, font=SANS, bold=True, color=INK)
        deck.text(s, x, 446, 340, 30, role, size=19, font=SANS, color=MUTED)
        deck.rect(s, x, 494, 300, 1, fill=LINE)
        deck.text(s, x, 512, 320, 60, note, size=22, font=SANS, color=INK)


@example("layouts", "L18-b", "人物 B：关键人物放大", "本页的主角放大并配一句职责，其余成员缩成一列名单。", F)
def people_lead(deck, s):
    bg(s, WARM)
    avatar(deck, s, 240, 360, 150, "周", ACCENT)
    deck.text(s, 450, 230, 500, 60, "周牧", size=48, font=SANS, bold=True, color=INK)
    deck.text(s, 450, 296, 500, 30, "供应链负责人 · 城市仓项目", size=20, font=SANS, color=MUTED)
    deck.text(s, 450, 360, 460, 120, "11 月底前定下合肥城市仓的位置，\n2028 年一季度投用。", size=26, font=SANS,
              color=INK, line_spacing=1.5)
    deck.rect(s, 980, 230, 1, 260, fill=LINE)
    for i, (name, role, _) in enumerate([t for t in C.TEAM if t[0] != "周牧"]):
        y = 250 + i * 110
        avatar(deck, s, 1040, y + 30, 30, name[0], [PRIMARY, "2E7D6B"][i])
        deck.text(s, 1084, y + 6, 160, 30, name, size=21, font=SANS, bold=True, color=INK)
        deck.text(s, 1084, y + 38, 160, 26, role, size=16, font=SANS, color=MUTED)


# ---------------------------------------------------------------- L19 numbered points
@example("layouts", "L19-a", "编号要点 A：三条横排", "超大编号做视觉锚点，顶部细线分组；每条一个短标题、一句解释。", F)
def points_row(deck, s):
    title(deck, s, "小店卖得更多，靠三件事")
    pts = [("离得近", "城市仓在 5 公里内，\n一天补货三次"), ("订得准", "按前一天销量订货，\n不再凭经验囤货"),
           ("卖得快", "晚 8 点临期折扣，\n当天清掉")]
    for i, (head, body) in enumerate(pts):
        x = M + i * 380
        deck.rect(s, x, 240, 340, 2, fill=INK)
        deck.text(s, x, 262, 200, 110, f"0{i + 1}", size=96, font=SANS_BLACK, color=ACCENT)
        deck.text(s, x, 400, 340, 44, head, size=34, font=SANS, bold=True, color=INK)
        deck.text(s, x, 462, 330, 90, body, size=21, font=SANS, color=MUTED, line_spacing=1.6)


@example("layouts", "L19-b", "编号要点 B：四条纵排配图标", "条目多时纵排；图标、短标题、一句话三列对齐，读起来像清单。", F)
def points_list(deck, s):
    deck.text(s, M, 120, 380, 200, "门店改造的\n四条原则", size=48, font=SANS, bold=True, color=INK, line_spacing=1.25)
    deck.text(s, M, 270, 360, 60, "适用于全部 126 家门店", size=20, font=SANS, color=MUTED)
    rules = [("ruler", "面积减到 180 平方米", "租金省下来给冷柜"), ("leaf", "叶菜放在进门第一排", "卖得最快，也坏得最快"),
             ("clock", "晚 8 点统一折扣", "价签由系统自动更新"), ("users", "每店 3 人轮班", "拣货和收银同一组人")]
    for i, (icon, head, body) in enumerate(rules):
        y = 110 + i * 130
        deck.rect(s, 560, y + 110, 640, 1, fill=LINE)
        deck.icon(s, icon, 560, y + 26, size=40, color=PRIMARY)
        deck.text(s, 630, y + 12, 560, 40, head, size=26, font=SANS, bold=True, color=INK)
        deck.text(s, 630, y + 58, 560, 30, body, size=19, font=SANS, color=MUTED)


# ---------------------------------------------------------------- L20 reading page
BODY_1 = ("损耗率按“报损金额 ÷ 进货金额”计算，每天闭店后由门店系统自动汇总。报损包括过期、破损和品相下降后"
          "无法销售的商品；打折售出的部分不计入报损，而是记为折扣损失，单独统计。")
BODY_2 = ("同城同业均值取自三家公开披露经营数据的社区生鲜连锁，按月取平均。因为各家口径略有不同，这个均值只用来"
          "看趋势，不用来比较具体数字。城市仓启用前后的对比，只统计同一批门店，避免新店拉低数字。")


@example("layouts", "L20-a", "编辑式长文 A：两栏正文加边注", "供会后阅读的说明页：左侧窄栏放小标题和摘要，正文两栏，每行约 20 字。", F)
def reading_two_cols(deck, s):
    bg(s, WARM)
    deck.text(s, M, 80, 260, 40, "附录 · 口径", size=16, font=SANS, color=ACCENT, spacing=0.08)
    deck.text(s, M, 116, 260, 160, "损耗率\n怎么算", size=40, font=SANS, bold=True, color=INK, line_spacing=1.2)
    deck.text(s, M, 260, 250, 120, "一句话：报损金额除以进货金额，打折售出的不算报损。", size=18, font=SANS, color=MUTED,
              line_spacing=1.6)
    deck.text(s, 400, 120, 380, 500, BODY_1, size=21, font=SERIF, color=INK, line_spacing=1.75)
    deck.text(s, 820, 120, 380, 500, BODY_2, size=21, font=SERIF, color=INK, line_spacing=1.75)


@example("layouts", "L20-b", "编辑式长文 B：一栏正文加旁注数字", "正文一栏、行长适中；把文中最重要的数字提出来放在旁边，读者扫一眼就知道重点。", F)
def reading_pull(deck, s):
    deck.text(s, M, 80, 700, 60, "同城同业均值怎么来", size=36, font=SANS, bold=True, color=INK)
    deck.text(s, M, 170, 640, 420, BODY_2 + "\n" + BODY_1, size=20, font=SERIF, color=INK, line_spacing=1.8, space_after=12)
    deck.rect(s, 800, 170, 3, 300, fill=ACCENT)
    deck.text(s, 830, 160, 380, 120, "3 家", size=96, font=SANS_BLACK, color=ACCENT)
    deck.text(s, 830, 290, 360, 90, "公开披露经营数据的\n社区生鲜连锁", size=22, font=SANS, color=INK, line_spacing=1.5)
    deck.text(s, 830, 400, 360, 60, "只看趋势，不比具体数字", size=18, font=SANS, color=MUTED)


# ---------------------------------------------------------------- L21 tables
@example("layouts", "L21-a", "表格页 A：原生表格，突出要讲的行", "表头配图标；数字右对齐；只把要讨论的两行变色，其余保持安静。", F)
def table_cities(deck, s):
    title(deck, s, "合肥、无锡还没有城市仓，送达和损耗都落后", sub="2027 年 6 月（虚构示例）")
    rows = C.CITY_TABLE
    emphasis = {(r, c): ACCENT for r in (3, 6) for c in range(6)}
    deck.table(s, M, 210, W, rows, col_widths=[200, 160, 160, 220, 190, 190], row_height=62, size=21, font=SANS,
               header_color=MUTED, align=["left", "right", "right", "right", "right", "right"], emphasis=emphasis)
    for icon, right in (("store", 440), ("warehouse", 600), ("clock", 820), ("leaf", 1010), ("repeat", 1200)):
        deck.icon(s, icon, right - 32, 172, size=26, color=PRIMARY)


@example("layouts", "L21-b", "表格页 B：用图标代替“有/无”", "只需看“有没有”时，用对勾和叉代替文字；结论写在表格下方一行。", F)
def table_checks(deck, s):
    title(deck, s, "三种配送方式，只有城市仓能做到四项全有")
    cols = ["自建城市仓", "第三方仓", "门店前置仓"]
    rows = [("当天补货", [1, 1, 1]), ("2 小时内分拣", [1, 0, 1]), ("全程冷链", [1, 1, 0]), ("按门店拆箱", [1, 0, 0])]
    for j, name in enumerate(cols):
        deck.text(s, 520 + j * 230, 180, 210, 34, name, size=22, font=SANS, bold=True,
                  color=ACCENT if j == 0 else INK, align="center")
    deck.rect(s, 520, 176, 210, 4, fill=ACCENT)
    for i, (label, marks) in enumerate(rows):
        y = 240 + i * 90
        deck.rect(s, M, y + 78, W, 1, fill=LINE)
        deck.text(s, M, y + 22, 400, 40, label, size=24, font=SANS, color=INK)
        for j, ok in enumerate(marks):
            deck.icon(s, "circle-check" if ok else "circle-x", 520 + j * 230 + 87, y + 18, size=36,
                      color=(ACCENT if j == 0 else PRIMARY) if ok else LINE)


# ---------------------------------------------------------------- L22 ending
@example("layouts", "L22-a", "结束页 A：下一步行动", "写清做什么、谁负责、何时完成；封面的路线母题回到页面上，首尾呼应。", F)
def ending_actions(deck, s):
    bg(s, WARM)
    deck.text(s, M, 80, 700, 70, "接下来三件事", size=52, font=SANS, bold=True, color=INK)
    for i, (what, who, when) in enumerate(C.ACTIONS):
        y = 220 + i * 136
        deck.text(s, M, y, 90, 80, f"{i + 1}", size=64, font=SANS_BLACK, color=ACCENT)
        deck.text(s, M + 90, y + 6, 560, 40, what, size=28, font=SANS, bold=True, color=INK)
        deck.text(s, M + 90, y + 50, 560, 30, f"{who} · {when}", size=20, font=SANS, color=MUTED)
    route = [(850, 620), (880, 560), (950, 545), (990, 480), (950, 420), (1010, 370), (1090, 380), (1140, 310)]
    deck.polygon(s, route, line=ACCENT, line_width=5, closed=False, dash=True)
    for x, y in (route[0], route[3], route[6]):
        deck.ellipse(s, x, y, 9, fill="FFFFFF", line=ACCENT, line_width=4)
    deck.icon(s, "map-pin", 1108, 236, size=64, color=ACCENT, stroke=2.2)


@example("layouts", "L22-b", "结束页 B：回顾三个数字", "培训或分享的收尾：只回顾最该记住的三个数，配一张主题插画。", F)
def ending_recap(deck, s):
    deck.text(s, M, 90, 700, 60, "记住三个数字", size=44, font=SANS, bold=True, color=INK)
    recap = [("30 分钟", "下单到送达"), ("5.9%", "生鲜损耗率"), ("126 家", "升级门店")]
    for i, (num, label) in enumerate(recap):
        y = 200 + i * 130
        deck.text(s, M, y, 420, 90, num, size=72, font=SANS_BLACK, color=PRIMARY if i else ACCENT)
        deck.text(s, M + 4, y + 90, 400, 30, label, size=20, font=SANS, color=MUTED)
    ill(deck, s, "store", 640, 200, 560, 420)
    source(deck, s, "知野生鲜 · 社区店升级计划 · 虚构示例", x=640, w=560)


# ---------------------------------------------------------------- L23 object with callouts (added archetype)
def callouts(deck, s, items, colour=INK):
    for (px_, py_), (tx, ty), head, body, side in items:
        end = tx + (0 if side == "left" else 0)
        deck.line(s, px_, py_, end, ty + 16, color=FAINT, width=1.5)
        deck.ellipse(s, px_, py_, 6, fill=ACCENT)
        bx = tx - 260 if side == "left" else tx + 10
        deck.text(s, bx, ty, 250, 34, head, size=22, font=SANS, bold=True, color=colour, align="right" if side == "left" else "left")
        deck.text(s, bx, ty + 36, 250, 50, body, size=17, font=SANS, color=MUTED, align="right" if side == "left" else "left",
                  line_spacing=1.4)


@example("layouts", "L23-a", "物件标注 A：门店的三处改动", "新增的原型：一张大插画，引线指到具体部位，旁边写改了什么。适合讲产品、设备、门店。", F)
def callout_store(deck, s):
    title(deck, s, "新门店改了三处")
    x, y, w, h = 380, 150, 560, 420
    ill(deck, s, "store", x, y, w, h)
    k = w / 320
    items = [((x + 160 * k, y + 88 * k), (320, 200), "招牌更亮", "夜里 200 米外能看见", "left"),
             ((x + 120 * k, y + 182 * k), (320, 470), "冷柜挪到门口", "叶菜和水果进门就能拿", "left"),
             ((x + 229 * k, y + 176 * k), (990, 420), "自提柜", "线上订单 24 小时可取", "right")]
    callouts(deck, s, items)


@example("layouts", "L23-b", "物件标注 B：产品卖点", "产品插画放大到一半页面，三条卖点挂在部位上，不另做卖点卡片。", F)
def callout_shoe(deck, s):
    bg(s, WARM)
    deck.text(s, M, 70, 600, 60, "示例：一双通勤跑鞋的三个卖点", size=36, font=SANS, bold=True, color=INK)
    x, y, w, h = 300, 150, 680, 510
    ill(deck, s, "sneaker", x, y, w, h)
    k = w / 320
    items = [((x + 160 * k, y + 120 * k), (420, 190), "一体编织鞋面", "透气，不磨脚背", "left"),
             ((x + 130 * k, y + 150 * k), (250, 560), "反光条", "夜跑时 150 米可见", "left"),
             ((x + 250 * k, y + 178 * k), (1040, 560), "回弹中底", "比上一代轻 18%", "right")]
    callouts(deck, s, items)


# ---------------------------------------------------------------- L24 bento grid (added archetype)
@example("layouts", "L24-a", "便当格：一页看全貌", "新增的原型：大小不同的圆角格子各放一样东西（照片、数字、图表、插画）；适合概览、总结和发布会。", F)
def bento(deck, s):
    bg(s, "F2F3F5")
    g, x0, y0 = 16, 64, 60
    cw, rh = (1280 - 2 * x0 - 3 * g) / 4, (720 - 2 * y0 - 2 * g) / 3

    def cell(c, r, cs=1, rs=1, fill="FFFFFF"):
        x, y = x0 + c * (cw + g), y0 + r * (rh + g)
        w, h = cs * cw + (cs - 1) * g, rs * rh + (rs - 1) * g
        deck.rect(s, x, y, w, h, fill=fill, radius=20)
        return x, y, w, h

    x, y, w, h = cell(0, 0, 2, 2)
    deck.picture(s, photo("squash"), x, y, w, h)
    deck.gradient_rect(s, x, y + h - 140, w, 140, [(0, "000000", 0), (1, "000000", 0.6)], angle=90)
    deck.text(s, x + 28, y + h - 76, w - 56, 50, "上半年：把产地搬进社区", size=30, font=SANS, bold=True, color="FFFFFF")
    x, y, w, h = cell(2, 0, 1, 1, fill=ACCENT)
    deck.text(s, x + 24, y + 22, w - 48, 90, [[("30", {"size": 72, "font": SANS_BLACK}), ("分钟", {"size": 26, "bold": True})]],
              color="FFFFFF", font=SANS)
    deck.text(s, x + 24, y + h - 44, w - 48, 28, "下单到送达", size=18, font=SANS, color="FFE7D9")
    x, y, w, h = cell(3, 0, 1, 1)
    deck.icon(s, "leaf", x + 24, y + 24, size=34, color="2E7D6B")
    deck.text(s, x + 24, y + 72, w - 48, 60, [[("5.9", {"size": 52, "font": SANS_BLACK}), ("%", {"size": 24, "bold": True})]],
              color=INK, font=SANS)
    deck.text(s, x + 24, y + h - 44, w - 48, 28, "生鲜损耗率", size=18, font=SANS, color=MUTED)
    x, y, w, h = cell(2, 1, 2, 1)
    deck.text(s, x + 24, y + 18, 300, 28, "月订单，万单", size=16, font=SANS, color=MUTED)
    deck.bar_chart(s, x + 16, y + 44, w - 32, h - 56, C.MONTHS, C.ORDERS, highlight={5}, horizontal=False, color=ACCENT,
                   base="C9CFD8", font=SANS, size=16, label_color=INK, gap_width=50)
    x, y, w, h = cell(0, 2, 1, 1, fill=PRIMARY_LIGHT)
    ill(deck, s, "truck", x + 20, y + 14, w - 40, h - 60)
    deck.text(s, x + 24, y + h - 42, w - 48, 28, "每日 3 趟补货", size=18, font=SANS, bold=True, color=INK)
    x, y, w, h = cell(1, 2, 1, 1)
    deck.text(s, x + 24, y + 20, w - 48, 70, [[("126", {"size": 52, "font": SANS_BLACK}), ("家", {"size": 22, "bold": True})]],
              color=PRIMARY, font=SANS)
    deck.text(s, x + 24, y + h - 44, w - 48, 28, "门店完成升级", size=18, font=SANS, color=MUTED)
    x, y, w, h = cell(2, 2, 2, 1, fill=INK)
    deck.text(s, x + 28, y + 30, w - 56, 90, "“早上摘的菜，中午就在社区店里了。”", size=26, font=SANS, bold=True,
              color="FFFFFF", line_spacing=1.4)
    deck.text(s, x + 28, y + h - 44, w - 56, 28, C.QUOTE_BY, size=16, font=SANS, color="AEB6C2")  # light grey on the dark tile
