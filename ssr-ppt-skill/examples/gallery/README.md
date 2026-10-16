# 示例图库

`assets/gallery/` 里的成品图和 `assets/design-examples.html` 都由这里的代码生成。每个示例是一个函数，用 `scripts/pptx_kit.py` 画一页原生 PPTX；构建时用 LibreOffice 渲染，再缩成 960px 宽的图（纯色页存 PNG，带照片的页存 JPEG）。代码本身就是可以照着改的模板。

| 文件 | 内容 |
|---|---|
| `content.py` | 版式和配方示例共用的虚构内容（知野生鲜社区店升级）：所有名字和数字都是编的 |
| `look.py` | 版式示例共用的中性外观（字体、颜色角色、边距） |
| `layouts_1.py`–`layouts_3.py` | 版式原型 L01–L24 |
| `convert_examples.py` | 改写 C01–C05：同一页改写前（A，文字）和改写后（B，信息不减、大部分画成图；C04 另有按排序画的 C），套在三个虚构机构的模板里；每组的材料是文件里的 `*_FACTS` 列表 |
| `art/` | 只为某个示例画的插画（例如 C05 的空压机），画法同 `assets/illustrations/README.md` 的“只为一个项目画” |
| `recipes_1.py`–`recipes_3.py` | 风格配方 R1–R19，每套 a 封面、b 数据页、c 图片页、d 特色页 |
| `type_specimens.py` | 字体字样、字体搭配、数字对比 |
| `imagery_examples.py` | 找图、照片处理、文字压图、裁切、插画换色、补画物体、图标 |
| `photos.json` | 示例用到的照片：链接、作者、许可（构建时下载） |
| `gallery.py` / `build.py` | 注册、渲染、导出、改文档链接、生成 `design-examples.html` |

## 重新生成

```bash
python examples/gallery/build.py --fonts path/to/fonts --out build/gallery              # 全部
python examples/gallery/build.py --fonts path/to/fonts --section recipes --only R03-a   # 只重做一张
```

- 需要 python-pptx、PyMuPDF、Pillow 和 LibreOffice；第一次运行会下载 `photos.json` 里的照片（缓存在系统临时目录，可用环境变量 `SSR_GALLERY_CACHE` 指定）。
- `--fonts` 指向放字体文件的文件夹。Windows 上构建时临时加载这些字体（`AddFontResource`，渲染完就移除，不安装到系统）；其他系统先把它们装好。缺字体时 LibreOffice 会替换成别的字体，生成的图就不对了。
- 全尺寸渲染图在 `<out>/review/`，生成后逐张看；也可以对 `<out>/<section>.pptx` 跑 `scripts/preview.py pptx` 做版面检查。
- 构建结束会更新 `assets/gallery/manifest.json`，把 `references/*.md` 里的图片链接改成实际扩展名，并重写 `assets/design-examples.html`。

## 用到的字体

| 字体 | 来源 | 许可 |
|---|---|---|
| 思源黑体、思源宋体（Noto Sans SC、Noto Serif SC，可变字体） | Google Fonts，或 Adobe 的 source-han-sans / source-han-serif | SIL OFL 1.1 |
| 鸿蒙黑体 HarmonyOS Sans SC | developer.huawei.com 的 HarmonyOS Sans 下载包 | 华为字体许可：可免费商用，不得修改字体文件 |
| MiSans | hyperos.mi.com/font | 小米字体许可：可免费商用，条款以官网为准 |
| 得意黑 Smiley Sans | github.com/atelier-anchor/smiley-sans | SIL OFL 1.1 |
| 霞鹜文楷 LXGW WenKai（Regular、Medium） | github.com/lxgw/LxgwWenKai | SIL OFL 1.1 |
| 站酷小薇、站酷庆科黄油体、马善政楷书 | Google Fonts（ZCOOL XiaoWei、ZCOOL QingKe HuangYou、Ma Shan Zheng） | SIL OFL 1.1 |
| Inter、Space Grotesk、Bebas Neue、Oswald、Archivo Black、Playfair Display、DM Serif Display、Cormorant Garamond、Source Serif 4、JetBrains Mono、IBM Plex Mono | Google Fonts | SIL OFL 1.1 |
| 微软雅黑、等线、宋体、楷体、黑体、Bahnschrift | Windows 自带 | 随系统授权，不打包 |

字体文件不放进仓库（中文字体每个 8–25MB）。

## 照片

示例只用开放许可的照片（CC0、公有领域、CC BY），都由 `scripts/find_images.py` 搜到、看过后选用，作者和许可记在 `photos.json`；CC BY 的照片在页面上署了名。照片只作示意，和虚构内容没有真实关系。

## 加一个示例

1. 在合适的文件里写一个函数，签名是 `(deck, s)`，用 `@example(section, id, title, note, fonts)` 注册；内容取自 `content.py`，或在示例旁写一份编好的材料。
2. `python examples/gallery/build.py --section <section> --only <id> --fonts <字体目录>`，打开 `review/` 里的图看。
3. 在对应的文档（`references/layouts.md`、`style-recipes.md`、`typography.md`、`imagery.md`；改写示例也写在 `imagery.md`）里加链接和说明。

示例的内容只用编的。不要把真实任务、测试用的模板或材料改个名字做成示例：模型下次拿到同一份材料，会照抄示例而不是自己想，名称和数字也可能泄露。模板外框、页面类型和题材都换成和实际任务不相干的。

再加一组改写对照时：

- 先在示例旁写一份材料（`*_FACTS` 列表），A、B 页都从这份材料和它的数字画出来，说明里写明两页用同一份材料。
- A 页照常见的文字写法写（标签加短句、段落、要点）；B 页保留 A 页的每一条信息和它的限定（约、预计、估算、时间起点、条件），大部分画成图。说明里可以写信息有几条、几条在图里，以 A 页的条目为准。
- 字号照 `references/typography.md` 的下限：正文不小于 18px，图旁标签不小于 16px（12pt），只有页脚和来源可以更小。
- 换一种外框（页眉、侧栏、页脚的组合）和一个新的虚构机构，让示例之间也不雷同。
