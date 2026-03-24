# IDML Generator - IDML 生成器

## 功能

将 HTML/CSS 转换为 Adobe InDesign IDML 格式。

## 使用方式

```python
from idml_generator import IDMLGenerator

# 创建生成器
generator = IDMLGenerator(
    document_name="Product Manual",
    page_size="A4",
    language="zh-CN"
)

# 添加样式
generator.add_paragraph_style("正文", {
    "font": "HarmonyOS Sans SC",
    "size": 10,
    "leading": 18,
    "space_after": 0
})

# 添加内容
generator.add_page([
    {"type": "heading", "text": "产品概述", "style": "大标题"},
    {"type": "paragraph", "text": "这是正文内容...", "style": "正文"}
])

# 生成 IDML
generator.save("output.idml")
```

## IDML 结构

```
document.idml/
├── mimetype
├── META-INF/container.xml
├── designmap.xml
├── Stories/Story_u1.xml
├── Spreads/Spread_u1.xml
└── Resources/Styles.xml
```

## 样式映射表

| CSS 属性 | IDML 属性 | 示例 |
|---------|----------|------|
| font-family | AppliedFont | "HarmonyOS Sans SC" |
| font-size | PointSize | 10 (pt) |
| line-height | Leading | 18 (pt) |
| color | FillColor | "Color/Black" |
| text-align | Justification | "LeftJustified" |
| margin-top | SpaceBefore | 0 (pt) |
| margin-bottom | SpaceAfter | 8.5 (pt) |
| text-indent | FirstLineIndent | 9 (pt) |

## 支持的特性

### 已实现
- ✅ 基本文档结构
- ✅ 段落样式
- ✅ 字符样式
- ✅ 文本内容
- ✅ 页面设置 (A4/A3/Letter)
- ✅ 中文字体支持

### 待实现
- ⏳ 图片插入
- ⏳ 表格支持
- ⏳ 母版页
- ⏳ 目录生成
- ⏳ 页眉页脚
- ⏳ 安全标识样式

## 输出配置

### 打印级 PDF 配置
```python
pdf_options = {
    "dpi": 300,
    "color_space": "CMYK",
    "embed_fonts": True,
    "pdf_variant": "PDF/X-3"
}
```

### 区域配置
| 区域 | 字体 | 色彩配置 |
|-----|------|---------|
| CN | HarmonyOS Sans SC + 宋体 | Japan Color 2001 Coated |
| EU | Mulish + Arial | Coated FOGRA39 |
| US | Mulish + Arial | Coated GRACoL 2006 |
