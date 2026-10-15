"""Layout examples L11-L14: time, process, systems and hierarchies. Fictional content."""
import content as C
from gallery import example
from look import (ACCENT, ACCENT_LIGHT, FAINT, INK, LINE, M, MUTED, PRIMARY, PRIMARY_LIGHT, SANS, SANS_BLACK, W,
                  WARM, ill, source, title)

F = (SANS,)
QUARTERS = ["2026 Q3", "2026 Q4", "2027 Q1", "2027 Q2", "2027 Q3", "2027 Q4", "2028 Q1"]


# ---------------------------------------------------------------- L11 time
@example("layouts", "L11-a", "时间线 A：横轴，上下交替", "节点按真实时间间隔排（2027 Q3 空了一格）；已完成实线实心，计划虚线空心。", F)
def timeline_axis(deck, s):
    title(deck, s, "一年完成 126 家门店升级，下一步是会员和新仓")
    x0, x1, y = 120, 1160, 420
    step = (x1 - x0) / (len(QUARTERS) - 1)
    now = x0 + 3.5 * step
    deck.line(s, x0, y, now, y, color=PRIMARY, width=4)
    deck.line(s, now, y, x1, y, color=FAINT, width=3, dash=True)
    deck.line(s, now, y - 150, now, y + 14, color=ACCENT, width=1.5, dash=True)
    deck.text(s, now - 40, y - 186, 80, 26, "现在", size=16, font=SANS, bold=True, color=ACCENT, align="center")
    for i, (q, label, done) in enumerate(C.TIMELINE):
        x = x0 + QUARTERS.index(q) * step
        deck.ellipse(s, x, y, 11, fill=PRIMARY if done else "FFFFFF", line=PRIMARY if done else FAINT, line_width=3)
        up = i % 2 == 0
        ty = y - 118 if up else y + 34
        align = "left" if i < len(C.TIMELINE) - 1 else "right"
        bx = x - 8 if align == "left" else x - 212
        deck.line(s, x, y - 12 if up else y + 12, x, ty + (82 if up else 0), color=LINE, width=1)
        deck.text(s, bx, ty, 220, 26, q, size=17, font=SANS, bold=True, color=PRIMARY if done else MUTED, align=align)
        deck.text(s, bx, ty + 30, 220, 56, label, size=21, font=SANS, bold=done, color=INK if done else MUTED,
                  align=align, line_spacing=1.25)
    source(deck, s, "按季度排列，间隔与真实时间一致（虚构示例）")


@example("layouts", "L11-b", "时间线 B：纵向，按阶段分段", "阶段用浅色色带分组，里程碑挂在一条竖线上；适合节点多、每个要写一句的情况。", F)
def timeline_vertical(deck, s):
    deck.text(s, M, 80, 380, 200, "三个阶段，\n两段已经走完", size=44, font=SANS, bold=True, color=INK, line_spacing=1.25)
    deck.text(s, M, 230, 360, 60, "2026 年 7 月至 2028 年 3 月", size=20, font=SANS, color=MUTED)
    phases = [("试点", 0, 2, PRIMARY_LIGHT), ("推广", 2, 4, PRIMARY_LIGHT), ("深化", 4, 6, ACCENT_LIGHT)]
    top, row = 60, 100
    for name, a, b, colour in phases:
        deck.rect(s, 560, top + a * row, 640, (b - a) * row - 8, fill=colour, radius=8)
        deck.text(s, 1100, top + a * row + 14, 84, 30, name, size=18, font=SANS, bold=True,
                  color=ACCENT if colour == ACCENT_LIGHT else PRIMARY, align="right")
    deck.rect(s, 620, top + 40, 3, len(C.TIMELINE) * row - 80, fill=FAINT)
    for i, (q, label, done) in enumerate(C.TIMELINE):
        y = top + i * row + row / 2 - 4
        deck.ellipse(s, 621.5, y, 9, fill=PRIMARY if done else "FFFFFF", line=PRIMARY if done else FAINT, line_width=3)
        deck.text(s, 650, y - 28, 160, 24, q, size=16, font=SANS, bold=True, color=PRIMARY if done else MUTED)
        deck.text(s, 650, y - 2, 420, 34, label, size=22, font=SANS, bold=done, color=INK if done else MUTED)


@example("layouts", "L11-c", "时间线 C：路线图（甘特条）", "几条工作并行时，用横条看起止和重叠；一条竖线标出“现在”。", F)
def roadmap(deck, s):
    title(deck, s, "四条工作线并行，会员体系是下一个重点", sub="按季度，2026 年 7 月至 2028 年 3 月（虚构示例）")
    x0, cw, y0, rh = 300, 128, 200, 96
    for i, q in enumerate(QUARTERS):
        deck.text(s, x0 + i * cw, y0 - 36, cw, 24, q, size=15, font=SANS, color=MUTED, align="center")
        deck.rect(s, x0 + i * cw, y0 - 6, 1, rh * 4 + 8, fill=LINE)
    streams = [("城市仓", 0, 2, True, "3 座建成"), ("门店改造", 1, 4, True, "126 家"),
               ("会员体系", 3, 6, False, "12 月上线"), ("损耗看板", 2, 6, False, "12 月全部接入")]
    for j, (name, a, b, done, note) in enumerate(streams):
        y = y0 + j * rh
        deck.text(s, M, y + 26, 200, 34, name, size=22, font=SANS, bold=True, color=INK)
        deck.rect(s, x0 + a * cw + 6, y + 20, (b - a) * cw - 12, 44, fill=PRIMARY if done else ACCENT if j == 2 else FAINT,
                  radius=22)
        deck.text(s, x0 + a * cw + 24, y + 29, (b - a) * cw - 40, 28, note, size=17, font=SANS, bold=True, color="FFFFFF")
    now = x0 + 4 * cw + cw * 0.25
    deck.line(s, now, y0 - 10, now, y0 + rh * 4 + 6, color=ACCENT, width=2)
    deck.text(s, now - 40, y0 + rh * 4 + 12, 80, 24, "现在", size=15, font=SANS, bold=True, color=ACCENT, align="center")


# ---------------------------------------------------------------- L12 process
@example("layouts", "L12-a", "流程 A：横向编号步骤配图标", "每步是编号、动词短语和一个图标；瓶颈步骤用强调色；箭头只表示先后。", F)
def process_icons(deck, s):
    title(deck, s, "四步把菜送到家，瓶颈在城市仓分拣")
    steps = [("leaf", "产地直采", "清晨采摘，当天装车"), ("warehouse", "城市仓分拣", "原来 5 小时，现在 2 小时"),
             ("store", "门店上架", "上午 10 点前完成"), ("house", "30 分钟到家", "骑手只跑最后 3 公里")]
    for i, (icon, name, note) in enumerate(steps):
        x = M + i * 290
        hot = i == 1
        colour = ACCENT if hot else PRIMARY
        deck.text(s, x, 210, 120, 70, f"0{i + 1}", size=56, font=SANS_BLACK, color=colour)
        deck.icon(s, icon, x, 310, size=48, color=colour)
        deck.text(s, x, 380, 240, 40, name, size=28, font=SANS, bold=True, color=INK)
        deck.text(s, x, 428, 230, 70, note, size=19, font=SANS, color=ACCENT if hot else MUTED, line_spacing=1.5)
        if i < len(steps) - 1:
            deck.icon(s, "arrow-right", x + 220, 236, size=32, color=FAINT)
    deck.rect(s, M + 290 - 16, 190, 270, 330, line=ACCENT, line_width=1.5, radius=12, dash=True)


@example("layouts", "L12-b", "流程 B：插画链条", "每一站一个物体插画，站在同一条地平线上；下面只留两字标题和一个时间。", F)
def process_chain(deck, s):
    title(deck, s, "从地里到家里：五站，不超过 18 小时")
    ground = 500
    slot = W / len(C.STEPS)
    height = {"farm": 186, "truck": 120, "warehouse": 186, "store": 186, "person": 150}
    for i, (name, label, note) in enumerate(C.STEPS):
        x = M + i * slot
        h = height[name]
        w = h * 4 / 3
        ill(deck, s, name, x + (slot - w) / 2, ground - h * 0.92, w, h)
        deck.text(s, x, ground + 40, slot, 36, label, size=24, font=SANS, bold=True, color=INK, align="center")
        deck.text(s, x, ground + 80, slot, 30, note, size=18, font=SANS, color=MUTED, align="center")
    deck.rect(s, M, ground + 4, W, 5, fill=LINE, radius=2)


@example("layouts", "L12-c", "流程 C：步骤长度按真实时长", "步骤的条长就是用时，一眼看出哪一步最费时间；数字写在条旁。", F)
def process_durations(deck, s):
    title(deck, s, "30 分钟里，等骑手就占了 6 分钟", sub="一张订单从下单到签收的平均用时，分钟（虚构示例）")
    steps = [("门店拣货", 8), ("打包", 4), ("等待骑手", 6), ("配送", 12)]
    total = sum(v for _, v in steps)
    x0, full = 300, 820
    for i, (name, minutes) in enumerate(steps):
        y = 210 + i * 96
        deck.text(s, M, y + 10, 200, 40, name, size=24, font=SANS, bold=True, color=INK)
        before = sum(v for _, v in steps[:i])
        hot = name == "等待骑手"
        deck.rect(s, x0 + full * before / total, y, full * minutes / total, 56, fill=ACCENT if hot else PRIMARY, radius=6)
        deck.text(s, x0 + full * (before + minutes) / total + 12, y + 12, 200, 36, f"{minutes} 分钟", size=22, font=SANS,
                  bold=True, color=ACCENT if hot else INK)
    deck.text(s, x0, 610, 820, 30, "“等待骑手”是下一步要压缩的环节：门店和骑手共享出餐提醒", size=19, font=SANS, color=ACCENT)


# ---------------------------------------------------------------- L13 system
@example("layouts", "L13-a", "系统架构 A：分层", "按真实层级分三层，同层对齐；要讨论的模块强调，其余灰；层间只用一条汇流箭头。", F)
def system_layers(deck, s):
    title(deck, s, "库存中台是这次升级的核心", sub="系统分层（虚构示例）")
    layers = [("前台", [("smartphone", "小程序"), ("store", "门店收银"), ("truck", "骑手 App")]),
              ("中台", [("receipt", "订单"), ("boxes", "库存"), ("users", "会员")]),
              ("后台", [("warehouse", "城市仓 WMS"), ("leaf", "供应商平台"), ("calculator", "财务")])]
    for i, (layer, modules) in enumerate(layers):
        y = 170 + i * 160
        deck.rect(s, M, y, W, 120, fill="F4F6F9", radius=10)
        deck.text(s, M + 24, y + 44, 100, 34, layer, size=22, font=SANS, bold=True, color=MUTED)
        for j, (icon, name) in enumerate(modules):
            x = 260 + j * 320
            hot = name == "库存"
            deck.rect(s, x, y + 20, 280, 80, fill="FFFFFF", line=ACCENT if hot else LINE, line_width=2.5 if hot else 1,
                      radius=8)
            deck.icon(s, icon, x + 24, y + 42, size=36, color=ACCENT if hot else PRIMARY)
            deck.text(s, x + 80, y + 42, 190, 40, name, size=24, font=SANS, bold=True, color=INK)
        if i < 2:
            deck.line(s, 740, y + 120, 740, y + 160, color=FAINT, width=2.5, arrow=True)


@example("layouts", "L13-b", "系统架构 B：中心辐射", "主角放中间，参与方围一圈；每条连线都写清流的是什么。", F)
def system_hub(deck, s):
    title(deck, s, "城市仓连起供应商、门店、骑手和总部")
    cx, cy = 640, 410
    nodes = [("farm", "供应商", 260, 260, "每日订货"), ("store", "社区门店", 1020, 260, "2 小时补货"),
             ("truck", "骑手", 260, 560, "就近取货"), ("dashboard", "总部看板", 1020, 560, "实时库存")]
    for name, label, x, y, flow in nodes:
        deck.line(s, cx, cy, x, y, color=LINE, width=3)
        mx, my = (cx + x) / 2, (cy + y) / 2
        deck.rect(s, mx - 70, my - 18, 140, 36, fill="FFFFFF")
        deck.text(s, mx - 70, my - 14, 140, 30, flow, size=17, font=SANS, bold=True, color=ACCENT, align="center")
    deck.ellipse(s, cx, cy, 120, fill=PRIMARY_LIGHT)
    ill(deck, s, "warehouse", cx - 100, cy - 90, 200, 150)
    deck.text(s, cx - 100, cy + 52, 200, 34, "城市仓", size=24, font=SANS, bold=True, color=INK, align="center")
    for name, label, x, y, _ in nodes:
        deck.ellipse(s, x, y, 70, fill="FFFFFF", line=LINE, line_width=1.5)
        ill(deck, s, name, x - 56, y - 50, 112, 84)
        deck.text(s, x - 100, y + 76, 200, 30, label, size=20, font=SANS, bold=True, color=INK, align="center")


# ---------------------------------------------------------------- L14 hierarchy
@example("layouts", "L14-a", "层级结构 A：议题树，只展开一支", "从左到右拆解；各分支的数加起来等于根；只展开要讨论的一支，其余灰。", F)
def issue_tree(deck, s):
    title(deck, s, "损耗下降的 3.7 个百分点，四成来自采购端")
    deck.rect(s, M, 300, 250, 120, fill=INK, radius=10)
    deck.text(s, M + 20, 318, 210, 90, "损耗率下降\n3.7 个百分点", size=24, font=SANS, bold=True, color="FFFFFF",
              line_spacing=1.35)
    branches = [("采购端", "−1.6", True), ("仓储端", "−1.2", False), ("门店端", "−0.9", False)]
    for i, (name, value, open_) in enumerate(branches):
        y = 170 + i * 150
        deck.polygon(s, [(M + 250, 360), (M + 290, 360), (M + 290, y + 50), (420, y + 50)], line=FAINT, line_width=2,
                     closed=False)
        deck.rect(s, 420, y, 260, 100, fill=ACCENT_LIGHT if open_ else "F4F6F9", radius=10)
        deck.text(s, 444, y + 16, 140, 34, name, size=24, font=SANS, bold=True, color=INK if open_ else MUTED)
        deck.text(s, 444, y + 54, 220, 34, f"{value} 个百分点", size=20, font=SANS, bold=open_,
                  color=ACCENT if open_ else FAINT)
    leaves = [("产地直采，少一次中转", "−0.9"), ("按日订货，不囤货", "−0.7")]
    for j, (name, value) in enumerate(leaves):
        y = 150 + j * 90
        deck.polygon(s, [(680, 220), (720, 220), (720, y + 32), (760, y + 32)], line=ACCENT, line_width=2, closed=False)
        deck.text(s, 770, y + 14, 330, 36, name, size=22, font=SANS, color=INK)
        deck.text(s, 1100, y + 14, 100, 36, value, size=22, font=SANS, bold=True, color=ACCENT, align="right")
        deck.rect(s, 770, y + 62, 430, 1, fill=LINE)
    source(deck, s, "按各项措施启用前后的损耗变化拆分（虚构示例）")


@example("layouts", "L14-b", "层级结构 B：组织架构，只展开一组", "从上到下；同级对齐；只展开本页要讲的一组，其余只写人数。", F)
def org_chart(deck, s):
    title(deck, s, "供应链组 9 人，负责三座新仓")
    cx = 640

    def box(x, y, w, name, role, hot=False, dim=False):
        deck.rect(s, x, y, w, 84, fill=PRIMARY if hot else "FFFFFF", line=None if hot else LINE, radius=10)
        deck.icon(s, "user", x + 18, y + 24, size=34, color="FFFFFF" if hot else (FAINT if dim else PRIMARY))
        deck.text(s, x + 64, y + 14, w - 74, 30, name, size=21, font=SANS, bold=True,
                  color="FFFFFF" if hot else (MUTED if dim else INK))
        deck.text(s, x + 64, y + 46, w - 74, 26, role, size=16, font=SANS, color="DCE6F5" if hot else MUTED)

    box(cx - 140, 180, 280, "项目负责人", "升级项目总负责")
    groups = [("林岚", "运营组 · 6 人", False), ("周牧", "供应链组 · 9 人", True), ("许安", "数据组 · 4 人", False)]
    deck.line(s, cx, 264, cx, 310, color=FAINT, width=2)
    deck.line(s, 240, 310, 1040, 310, color=FAINT, width=2)
    for i, (name, role, hot) in enumerate(groups):
        x = 100 + i * 400
        deck.line(s, x + 140, 310, x + 140, 340, color=FAINT, width=2)
        box(x, 340, 280, name, role, hot=hot, dim=not hot)
    subs = [("城市仓", "3 人"), ("冷链", "2 人"), ("采购", "4 人")]
    deck.line(s, 640, 424, 640, 470, color=PRIMARY, width=2)
    deck.line(s, 420, 470, 860, 470, color=PRIMARY, width=2)
    for j, (name, n) in enumerate(subs):
        x = 330 + j * 220
        deck.line(s, x + 90, 470, x + 90, 500, color=PRIMARY, width=2)
        deck.rect(s, x, 500, 180, 76, fill=PRIMARY_LIGHT, radius=10)
        deck.text(s, x + 20, 512, 140, 30, name, size=22, font=SANS, bold=True, color=INK)
        deck.text(s, x + 20, 544, 140, 24, n, size=17, font=SANS, color=MUTED)
