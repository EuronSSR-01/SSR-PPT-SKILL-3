# 字体与中文排版

字体是演示气质的第一来源。全套只用系统默认字体、单一字重，是“看起来普通”最常见的原因。本文件列出可选字体（每款都有同一句标题、同一段正文、同一组数字的字样图）、搭配、字号阶梯、中文排版细则，以及 HTML 和 PPTX 里怎么让字体真正生效。

字样图在 `assets/gallery/type/`，集中看 [`assets/design-examples.html`](../assets/design-examples.html) 的“字体”部分；代码在 `examples/gallery/type_specimens.py`。

## 可选字体

获取顺序：用户提供的字体文件 → 本机已安装（Windows `C:\Windows\Fonts`、`%LOCALAPPDATA%\Microsoft\Windows\Fonts`；macOS `/Library/Fonts`、`~/Library/Fonts`；Linux `/usr/share/fonts`、`~/.local/share/fonts`）→ 环境允许联网时从官方来源下载（见 `examples/gallery/README.md` 的字体表）。使用前以官方页面的最新许可为准，在 `sources.md` 或构建记录写明字体来源。

“覆盖”是实测的字体文件字符数：GB2312 收录 6,763 个常用汉字；人名、地名和生僻字常在这之外。

### 中文

| 字体 | 字样 | 许可 | 覆盖 | 效果与用法 | 注意 |
|---|---|---|---|---|---|
| 思源黑体 Noto Sans SC | [T01](../assets/gallery/type/T01.png) | SIL OFL | 常用字全有，约 2.7 万汉字 | 中性清楚，字重从 Light 到 Black；正文首选，Black 做大标题和大数字 | 默认感强，靠字号、字重和留白拉开层级 |
| 思源宋体 Noto Serif SC | [T02](../assets/gallery/type/T02.png) | SIL OFL | 约 2.8 万汉字 | 编辑感、文化感、权威；结论标题、引文、细读的正文 | 投影时细笔画变淡，正文不小于 20px |
| 鸿蒙黑体 HarmonyOS Sans SC | [T03](../assets/gallery/type/T03.png) | 华为许可：可免费商用，**不得修改字体文件** | 约 2.7 万汉字 | 几何、现代、略宽，数字清楚；产品、科技、发布会 | 子集化嵌入网页算修改，有争议：HTML 优先用 OFL 字体 |
| MiSans | [T04](../assets/gallery/type/T04.png) | 小米许可：可免费商用，条款以官网为准 | 约 2.7 万汉字 | 圆润、清爽、亲和，10 档字重；消费、服务、人文 | 嵌入网页前先读官网许可 |
| 得意黑 Smiley Sans | [T05](../assets/gallery/type/T05.png) | SIL OFL | 常用字全有，约 8,100 汉字 | 窄、斜、硬朗，有态度；只做大标题和海报感的短句 | 一个字重、本身是斜体；人名和生僻字先查 |
| 霞鹜文楷 LXGW WenKai | [T06](../assets/gallery/type/T06.png) | SIL OFL | 约 2.8 万汉字 | 楷书感、温和、像手写；引文、批注、故事性的短句，也能排长文 | 和黑体同排时字号大一档才平衡 |
| 站酷小薇 ZCOOL XiaoWei | [T07](../assets/gallery/type/T07.png) | SIL OFL | **只有** 6,763 个常用字，缺“·〇℃” | 细、清雅、文艺；品牌故事的标题和短句 | 人名、生僻字、部分符号会缺 |
| 站酷庆科黄油体 | [T08](../assets/gallery/type/T08.png) | SIL OFL | 约 9,200 汉字，缺“·〇℃” | 粗圆、俏皮，像手绘招牌；活动和年轻品牌的大标题 | **数字“7”像“1”**：不要用它排数字 |
| 马善政楷书 Ma Shan Zheng | [T09](../assets/gallery/type/T09.png) | SIL OFL | 只有 6,763 个常用字 | 毛笔书法；单个大字做图形、文化主题的题字 | 只用于极少的字，不排正文 |
| 阿里巴巴普惠体、OPPO Sans | 未出字样图 | 各自官方许可，可免费商用 | — | 圆润亲和，和 MiSans 同一类 | 下载后用本文末的方法补字样图 |
| 方正、汉仪等商业字体 | — | 需要用户确认已有授权 | — | — | 没有授权不用 |

**系统字体**（[T10](../assets/gallery/type/T10.png)）：Windows 有微软雅黑、等线、宋体、楷体、黑体；macOS 有苹方、宋体-简。它们随系统授权，只作本机回退，不嵌入网页、不随文件分发。优点是交给别人后在 WPS／PowerPoint 里不会走样；缺点是大家都在用，要靠字号、字重、留白和构图拉开差异。**系统宋体、楷体、黑体里的数字和小数点间距很怪（“5. 9%”），数字要另配字体。**

### 西文与数字

| 字体 | 字样 | 效果与用法 | 注意 |
|---|---|---|---|
| Inter | [T11](../assets/gallery/type/T11.png) | 中性，数字清楚，字重全；数字和西文首选 | 表格数字用等宽数字（CSS `tabular-nums`） |
| Space Grotesk | [T12](../assets/gallery/type/T12.png) | 几何感、有个性；科技、设计的标题和数字 | 正文用 Inter 更稳 |
| Bebas Neue / Oswald | [T13](../assets/gallery/type/T13.png) | 窄体，海报感，省横向空间；大数字、短标签、编号 | Bebas 只有大写和一个字重 |
| Archivo Black | [T14](../assets/gallery/type/T14.png) | 极粗、宽，冲击力强；海报式大数字 | 只有一个字重 |
| Playfair Display | [T15](../assets/gallery/type/T15.png) | 高反差衬线，优雅；品牌、奢华、杂志的大标题和大数字 | 默认旧式数字（高低不齐），表格里不用 |
| DM Serif Display | [T16](../assets/gallery/type/T16.png) | 粗衬线，杂志感；标题、引文、大数字 | 只有一个字重 |
| Cormorant Garamond | [T17](../assets/gallery/type/T17.png) | 古典、纤细；西文小注、成对的中英文标题 | 至少 18px，旧式数字 |
| Source Serif 4 | [T18](../assets/gallery/type/T18.png) | 耐读，数字整齐；学术、报告的西文正文和图注 | — |
| JetBrains Mono / IBM Plex Mono | [T19](../assets/gallery/type/T19.png) | 等宽，技术感；代码、编号、规格 | — |
| Bahnschrift | [T20](../assets/gallery/type/T20.png) | Windows 自带的 DIN 风格字体，有窄体；不能装字体时的稳妥数字字体 | 只在 Windows 上有，随系统授权 |

同一组数字在不同字体里的样子：[N01 数字字体对比](../assets/gallery/type/N01.png)。

## 搭配

- **起步建议**：一个中文家族加一个西文数字字体，必要时再加一个点缀字体（楷体引文、书法大字、等宽标注）。这是起点，不是上限；配方需要时可以多用，只要每款都有明确的角色。公司模板任务在模板允许的字体里，靠字号、字重和层级做出差别。
- 层级主要靠字号和字重建立，同一家族内字重至少差 300（如 900 对 400）。
- 宋体标题配黑体正文，立刻有编辑感；黑体标题配宋体正文适合长阅读。
- 数字和西文单独指定字体：CSS 里把西文字体写在中文字体前面（`font-family: "Inter", "Noto Sans SC", sans-serif`）；PPTX 里 `latin` 用西文字体、`ea` 用中文字体（`pptx_kit` 的 `font=` 和 `ea=`）。排好后看两种字体的基线和字高是否协调。
- 粗体要用真实的字重文件或可变字体的命名实例，不要依赖软件的合成粗体；中文不用斜体表示强调。

同一页内容换七组搭配：

| 搭配 | 标题 | 正文 | 数字 | 示例 |
|---|---|---|---|---|
| 编辑对比 | 思源宋体 Bold | 思源黑体 | Inter | [P01](../assets/gallery/type/P01.png) |
| 现代无衬线 | 思源黑体 Black | 思源黑体 Regular | Inter Black | [P02](../assets/gallery/type/P02.png) |
| 产品科技 | 鸿蒙黑体 Bold | 鸿蒙黑体 | JetBrains Mono | [P03](../assets/gallery/type/P03.png) |
| 年轻有力 | 得意黑 | 思源黑体 Medium | Archivo Black | [P04](../assets/gallery/type/P04.png) |
| 人文温度 | MiSans Heavy | MiSans（引文霞鹜文楷） | MiSans Heavy | [P05](../assets/gallery/type/P05.png) |
| 东方雅致 | 思源宋体 SemiBold | 霞鹜文楷 | Cormorant Garamond | [P06](../assets/gallery/type/P06.png) |
| 稳妥系统 | 微软雅黑 Bold | 等线 | Bahnschrift 窄体 | [P07](../assets/gallery/type/P07.png) |

## 字号阶梯

以 1280×720 画布为准；PPTX 宽 13.333 英寸 = 960pt，所以 **pt = px × 0.75**。公司模板常用其他尺寸，按 [pptx.md](pptx.md) 的“单位与排版”换算，并核对最终文件的实际字号。

| 层级 | HTML（px） | PPTX（pt） | 说明 |
|---|---|---|---|
| 展示字（封面、大数字、金句） | 120–300 | 90–225 | 高冲击页使用；行高 0.95–1.1 |
| 页标题 | 36–64 | 27–48 | 结论句不超过两行 |
| 小标题、引导语 | 24–32 | 18–24 | |
| 正文 | 20–26 | 15–20 | 现场演讲不小于 20px；独立阅读最小 18px |
| 标注、来源、页码 | 13–16 | 10–12 | 绝对下限 12px（9pt） |

尺度反差制造冲击力：每页最大文字与正文的字号比至少 2:1，高冲击页至少 5:1。字号拉开后层级仍然不清楚，通常是内容太多，应拆分或删减，而不是继续缩小字号。

## 中文排版细则

- **行高**：正文 1.5–1.7；标题 1.15–1.3；展示字 0.95–1.1。
- **字距**：正文 0 至 0.02em；中文大标题 0 至 -0.02em，不要加大字距装“高级感”；小号全大写西文标签可加 0.08–0.3em（`pptx_kit` 的 `spacing=`）。
- **中西混排**：汉字与西文或数字之间留一个空格（“增长 23%”）；全角标点前后不加空格。
- **断行**：标题在语义边界手动断行，避免末行只剩一两个字；不拆开数字与单位、人名、专有名词；行首不出现句读标点，行尾不留开引号或开括号。HTML 标题可加 `text-wrap: balance`，正文可用 `line-break: strict`，最终仍以实际渲染为准。
- **竖排**：短标题和小注可以竖排（`deck.text(..., vertical=True)`，HTML 用 `writing-mode: vertical-rl`），从右往左读；竖排里不放长串数字和英文。
- **行长**：幻灯片正文每行约 18–32 个汉字，更长时分栏或缩短。
- **对齐**：中文正文默认左对齐；两端对齐只用于较宽的纯中文段落。
- **数字**：表格与对比数字用等宽数字。大数字配小单位：单位约为数字的 0.3–0.5 倍，与数字基线对齐，`wrap=False` 防止单位换行。
- **强调**：用字重、颜色或尺度，不用下划线和中文斜体；一段内的强调不超过一处。

## 缺字检查

字体缺某个字时，PowerPoint 和 WPS 会挑另一款字体（常是宋体或等线）只显示这个字，一行展示字里就混进一个普通字；网页会回落到系统字体。做完先检查：

```bash
python scripts/font_coverage.py fonts/SmileySans-Oblique.ttf --pptx build/deck.pptx
python scripts/font_coverage.py fonts/ZCOOLXiaoWei-Regular.ttf --text "周牧 · 杭州 〇 ℃"
```

有缺字时：给这段文字换一款覆盖更全的字体；改写措辞；或者把缺字所在的文字段单独设成回退字体（`pptx_kit` 的文字段可以单独写 `font`）。HTML 用 `embed_fonts.py` 时它也会列出缺字。

## HTML：子集化并内联字体

单文件离线 HTML 想用设计字体，就要把字体按实际用到的字子集化，再以 base64 内联。中文字体原文件 8–25MB，子集后一般只有几十到几百 KB。

```bash
python scripts/embed_fonts.py build/index.html \
  --font "Noto Sans SC=fonts/NotoSansSC-VF.ttf" \
  --font "Noto Serif SC=fonts/NotoSerifSC-VF.ttf@700" \
  --font "Inter=fonts/Inter-Variable.ttf" \
  -o build/index.html
```

- 参数格式为 `族名=文件路径[#TTC 序号][@字重或字重范围][:italic]`。可变字体不写字重时保留全部范围；写单个字重（如 `@700`）时先固定为该字重的静态字体，体积更小。
- 脚本收集 HTML 中出现的全部字符（包括播放器的提示文字）和基础 ASCII，生成 `<style id="ssr-embedded-fonts">` 插入 `</head>` 前；每次改完文字都要重新运行。
- 页面 CSS 照常写 `font-family`，并保留系统回退：`"Noto Sans SC", "PingFang SC", "Microsoft YaHei", sans-serif`。
- 嵌入前确认许可允许网页嵌入与分发（OFL 可以；鸿蒙黑体不允许修改字体文件；系统字体和未授权的商业字体不嵌入）。

## PPTX：字体设置与可用性

PPTX 一般不带字体。观看或编辑的电脑没有装该字体时会替换成默认字体，排版随之走样。策划时选定一种策略，并在交付说明里写明：

1. **稳妥**：正文用目标电脑大概率已有的字体（Windows 微软雅黑或等线，macOS 苹方），标题与数字用设计字体，并随交付附上字体文件和安装说明；或者标题也用系统字体（[P07](../assets/gallery/type/P07.png) 那样靠字号和字重拉开）。
2. **设计优先**：全套用设计字体，交付字体文件（确认许可允许分发），说明先安装。
3. **用户环境已知**：用户确认演示电脑已装的字体。

技术要点：

- 中文必须设置东亚字体。OOXML 的文字属性里 `<a:latin>` 管西文，`<a:ea>` 管中日韩文字；python-pptx 的 `font.name` 只写 `a:latin`，`pptx_kit` 会同时写 `a:ea`。PptxGenJS 的 `fontFace` 会同时写 latin、ea、cs，但 `pptx.theme` 只写主题的 latin，图表的轴和数据标签也只写 latin。
- **可变字体的字重**：在 Windows 上，可变字体的命名实例是单独的字体名，如 `Noto Sans SC Black`、`Noto Serif SC SemiBold`、`MiSans Heavy`；写 `font="Noto Sans SC", bold=True` 得到 Bold。LibreOffice 实测认这些名字；WPS／PowerPoint 以实际导出为准（`preview.py pptx --export wps`）。个别可变字体（实测 Bodoni Moda）在 LibreOffice 里会错用最粗字重，用静态字体文件更稳。
- 新建文件用 `deck.save(path, theme_fonts=(标题字体, 正文字体))` 或 `scripts/set_theme_fonts.py` 把主题的标题／正文字体（latin、ea 与简体中文字体）设为设计字体，图表中文和用户新增的文本框都会沿用。公司模板默认保留主题、占位符和运行级字体，只有任务要求时才改。
- 用 `scripts/preview.py pptx` 输出的字体清单核对实际用了哪些字体。渲染验收所用的电脑必须装有目标字体，否则看到的是替换后的效果；渲染图和预期不符时，先查字体是否被替换。
- 图表的轴、数据标签字体要单独设置，不会自动继承页面字体（`pptx_kit` 的图表函数用 `font=`）。

## 新增一款字体

1. 从官方来源下载，读许可：能否商用、能否嵌入网页、能否随文件分发、能否修改（子集化）。
2. 量覆盖：`python scripts/font_coverage.py 新字体.ttf --text "常用的人名、地名和符号"`。
3. 做字样图：在 `examples/gallery/type_specimens.py` 的 `CJK` 或 `LATIN` 列表加一行（编号、名字、字体名、许可、字重、覆盖、三句说明），运行 `python examples/gallery/build.py --section type --only T21 --fonts <字体目录>`，看图。
4. 在本文件的表里加一行：字样图链接、许可、覆盖、效果与用法、注意。
