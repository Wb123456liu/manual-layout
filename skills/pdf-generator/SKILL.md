---
name: pdf-generator
description: PDF 生成器技能，用于从各种格式生成 PDF 文件。支持 HTML 转 PDF、Markdown 转 PDF、图片转 PDF、空白 PDF 创建等。当用户需要：(1) 从 HTML 生成 PDF (2) 从 Markdown 生成 PDF (3) 图片转 PDF (4) 创建 PDF 报告时使用此技能。
---

# PDF Generator - PDF 生成器

## 核心功能

### 1. HTML 转 PDF

```python
from weasyprint import HTML, CSS

def html_to_pdf(html_path, output_path, css_path=None):
    """HTML 转 PDF"""
    html = HTML(filename=html_path)
    if css_path:
        css = CSS(filename=css_path)
        html.write_pdf(output_path, stylesheets=[css])
    else:
        html.write_pdf(output_path)

def html_string_to_pdf(html_content, output_path):
    """HTML 字符串转 PDF"""
    HTML(string=html_content).write_pdf(output_path)
```

### 2. Markdown 转 PDF

```python
import markdown

def markdown_to_pdf(md_path, output_path):
    """Markdown 转 PDF"""
    with open(md_path, 'r') as f:
        md_content = f.read()
    
    # 转换为 HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code']
    )
    
    # 添加样式
    styled_html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'SimSun', serif; font-size: 12pt; }}
            h1 {{ font-family: 'SimHei', sans-serif; }}
            table {{ border-collapse: collapse; }}
        </style>
    </head>
    <body>{html_content}</body>
    </html>
    """
    
    HTML(string=styled_html).write_pdf(output_path)
```

### 3. 图片转 PDF

```python
from PIL import Image

def images_to_pdf(image_paths, output_path):
    """多张图片转 PDF"""
    images = [Image.open(path) for path in image_paths]
    # 转换为 RGB 模式
    images = [img.convert('RGB') for img in images]
    # 保存为 PDF
    images[0].save(
        output_path,
        save_all=True,
        append_images=images[1:]
    )
```

### 4. 从零创建 PDF

```python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_pdf(output_path, content):
    """创建 PDF 文档"""
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    
    # 注册中文字体
    pdfmetrics.registerFont(TTFont('SimSun', 'simsun.ttc'))
    
    c.setFont('SimSun', 12)
    y = height - 50
    
    for line in content.split('\n'):
        c.drawString(50, y, line)
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50
    
    c.save()
```

## 使用示例

```python
# HTML 报告转 PDF
html_to_pdf("report.html", "report.pdf")

# Markdown 文档转 PDF
markdown_to_pdf("README.md", "README.pdf")

# 多张扫描图片转 PDF
images_to_pdf(["scan1.jpg", "scan2.jpg"], "scanned.pdf")
```

## 支持的输入格式

| 格式 | 方法 |
|------|------|
| HTML | WeasyPrint |
| Markdown | markdown + WeasyPrint |
| 图片 | Pillow |
| 纯文本 | ReportLab |