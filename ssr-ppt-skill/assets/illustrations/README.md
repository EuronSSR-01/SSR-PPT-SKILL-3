# 插画素材库

这里放的是**物体和场景插画**：货车、仓库、工厂、门店、面料、银行卡、人物……用来让观众一眼看到“讲的是什么东西、在什么场景”。它和图标不同：图标是小号的识别符号，放在标题、表头、节点旁；插画是页面上的画面，可以做主视觉，也可以拼成一条链。

本 Skill 自带的插画都是自绘的，不含第三方素材，可在演示中直接使用和修改。

## 现有风格只是样本

| 风格 | 文件夹 | 样子 | 数量 |
|---|---|---|---|
| 扁平圆润 | `flat/` | 纯色块、圆角、深浅三档、浅色地面阴影 | 41 |
| 线描 | `line/` | 深色线条勾轮廓，浅色底色错开，一处强调色 | 8 |

先看每个文件夹的 `sheet.png`（全部插画的总览图）和 `INDEX.md`（名称、含义、风格说明）。

这些不是全部可能，也不要求每份演示都用它们：

- 合适就直接用，换成这份演示的颜色；
- 差一点就改：改 SVG 源码里的形状、比例、细节；
- 缺某个物体就按下面的方法补画，补进对应风格；
- 这份演示需要别的画风（等距立体、手绘、剪纸、厚涂……）就新建一个风格文件夹，或只为这个项目画；
- 页面用照片、图表或排版更好时，不用插画。

一份演示里通常只用一种插画风格；两种风格混在一起很容易显得像拼凑的素材，除非是有意的对比。

## 怎么用

```bash
python scripts/illustrations.py styles                       # 有哪些风格
python scripts/illustrations.py list --style flat            # 名称与含义
python scripts/illustrations.py export truck --primary 0B3D91 --accent E8590C --out build/truck.svg --png-width 960
python scripts/illustrations.py scene factory truck warehouse truck store --primary 0B3D91 --out build/chain.svg
python scripts/illustrations.py sheet --style flat --primary 0B6E4F --accent E4572E --out build/sheet.png
```

- **PPTX**（`scripts/pptx_kit.py`）：

  ```python
  deck.illustration(slide, "truck", x, y, w, h, primary="0B3D91", accent="E8590C")          # 单个物体
  deck.illustration(slide, ["factory", "truck", "store"], x, y, w, h, primary="0B3D91")   # 一排场景
  deck.illustration(slide, "warehouse", x, y, w, h, style="line")                         # 换风格
  deck.illustration(slide, "build/my-product.svg", x, y, w, h, primary="0B3D91")          # 自己画的 SVG
  ```

  插入的是按版位 2 倍分辨率生成的 PNG：能移动、缩放、裁切，不能在 PPT 里逐个部件改。要改画面就改 SVG 再生成。
- **HTML**：用 `export` 得到换好颜色的 SVG，直接内联。
- **场景**：`scene` 把多个物体放在同一条地平线上，车辆、人物、小物件按各自的 `data-scale` 自动缩小；`"truck:0.8"` 可以单独指定大小。

### 颜色

每张插画只用下面这些“占位色”，`recolor()` 按演示的配色整体替换：给出主色和强调色，深浅两档自动算出。

| 角色 | 占位色 | 用在哪里 | 怎么改 |
|---|---|---|---|
| `primary` | `#2F6FDE` | 主体大面积 | `primary=` |
| `primary_dark` | `#1D4FAE` | 背光面、边沿、深色部件 | 由主色算出 |
| `primary_light` | `#D6E4FA` | 玻璃、屏幕、受光面、浅色底 | 由主色算出 |
| `accent` | `#F28C28` | 一两个关键部件 | `accent=` |
| `accent_dark` | `#C86512` | 强调部件的背光面 | 由强调色算出 |
| `accent_light` | `#FDE3C8` | 纸箱、浅色强调 | 由强调色算出 |
| `ink` | `#22303F` | 轮胎、深色细节、线描风格的线条 | `ink=` |
| `surface` | `#E8ECF1` | 墙面、浅灰底 | `surface=` |
| `line` | `#C8D0DB` | 地面、阴影、金属、细节 | `line=` |
| `leaf` `leaf_dark` `leaf_light` | `#4E9F5D` `#35754A` `#CFE8C9` | 植物，默认保持自然绿色 | `leaf=` |
| `soil` `soil_dark` | `#C49A6C` `#9C7148` | 泥土、木头、纸袋，默认自然棕色 | `soil=` |

白色 `#FFFFFF`、三种肤色 `#EFC3A0` `#D9A47E` `#A8714E` 和棕色头发 `#5B3A29` 不替换。

换色后看一眼：主色很浅（如浅黄）时，浅色那档会接近白色，物体边缘可能看不清；这时换一个更深的主色，或把 `surface`、`line` 调深。

## 补画一个物体

以给 `flat` 补一台“冷藏车”为例（库里的 `reefer-truck.svg` 就是这样从 `truck.svg` 改出来的）：

1. **先想清楚要认出什么**：冷藏车 = 货车 + 车厢上的制冷机组 + 冷色车厢。写下两三个必须画出来的特征，其余能省就省。
2. **找参考**：上网搜几张实物照片看轮廓和比例，再打开同风格里最接近的一张（这里是 `truck.svg`）。从相近的图改，比从零画更快，也更统一。
3. **按画布和地面画**：画布 `viewBox="0 0 320 240"`，物体站在 y≈212 的地面上，底部加一道浅色椭圆阴影；侧面或正面略带角度；四周留 10–20 的空。
4. **按风格的规矩上色**（见各风格的 `INDEX.md`）：
   - `flat`：只用色块不描边；主体用 `primary`，背光面用 `primary_dark`，玻璃和高光用 `primary_light`，强调色只给一两个部件，轮胎和深色细节用 `ink`；圆角 2–6。
   - `line`：外轮廓 3、内部细节 2 的 `ink` 线条，圆头圆角；浅色底色块向右下错开约 7；一处强调色。
5. **写清大小**：不是建筑的，在 `<svg>` 上写 `data-scale`（建筑 = 1，货车 0.62，人物 0.62，手持物 0.35–0.5）。
6. **检查**：
   ```bash
   python scripts/illustrations.py check assets/illustrations/flat/reefer-truck.svg
   python scripts/illustrations.py sheet --style flat --out build/sheet.png
   ```
   `check` 会指出文字、渐变、滤镜、id、占位色以外的颜色等问题。然后看总览图：和同风格的图放在一起，线条粗细、细节多少、明暗方向是否一致；缩到 120px 宽还认不认得出；用另一套配色（如 `--primary 0B6E4F --accent E4572E`）再看一遍。
7. **登记**：在该风格的 `INDEX.md` 加一行名称、含义、场景大小，并重新生成 `sheet.png`。

起步模板：

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 240" data-scale="0.62">
  <ellipse cx="160" cy="214" rx="140" ry="7" fill="#C8D0DB" opacity="0.7"/>
  <!-- 主体：#2F6FDE；背光面 #1D4FAE；玻璃 #D6E4FA；关键部件 #F28C28；深色细节 #22303F -->
</svg>
```

画得好看的几个要点：

- **先剪影后细节**：只看外轮廓就该认得出是什么，细节只补必要的两三处。
- **明暗方向一致**：光从左上来，背光面在右侧和底部。
- **细节密度一致**：同一套里，不要一张画得很满、一张只有几个方块。小于 2 个单位的细节在幻灯片上看不见，不画。
- **重复的部件可以用代码生成**：窗户、齿、硬币这类重复元素，用一小段 Python 算坐标再写成 SVG，比手写整齐。
- **避开陈词滥调**：握手、灯泡、火箭、齿轮、地球不画成主角。
- **人物**：不画五官，肤色和发色有变化，姿态自然，不做夸张表情。

## 新建一种风格

1. 新建文件夹，例如 `assets/illustrations/isometric/`。
2. 写 `INDEX.md`：这种风格的样子（线条、色块、明暗、圆角、视角）、画面效果、适合搭配什么，以及每张图的名称、含义、场景大小。
3. 先画最常用的几个物体（货车、仓库、工厂、门店、人物、电脑），**名称与 `flat` 相同**，换风格时只改 `style=`。
4. 仍然只用上面的占位色，这样整套能跟着演示换色；确实需要固定颜色时写进 `INDEX.md`。
5. 用 `check` 和 `sheet` 检查，把 `sheet.png` 放进文件夹。

## 只为一个项目画

演示的主角常常是这份材料特有的东西，例如客户的某款产品、一条特定的产线。可以只为这个项目画：SVG 放在构建目录，仍用占位色以便换色（或直接用产品的真实颜色），再用 `deck.illustration(slide, "build/xxx.svg", ...)` 或 `deck.svg_picture()` 插入，HTML 直接内联。画法同上，同样要渲染出来看。

画得好、以后还会用的，再按“补画一个物体”的步骤收进素材库。

## 不适合用插画的时候

- 要证明真实存在的人物、产品、门店、现场：用真实照片，不用插画冒充。
- 数量、比例、趋势：用图表；流程和关系：用流程图或原生形状。不把数字画进插画。
- 插画里不放文字：标签和说明用原生文字放在图旁。
