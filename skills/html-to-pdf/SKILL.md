---
name: html-to-pdf
description: HTML 转 PDF 技能，专门用于将 HTML 内容转换为 PDF 文件。支持 CSS 样式、页眉页脚、分页控制、中文支持等。当用户需要：(1) HTML 转 PDF (2) 网页打印为 PDF (3) 报告生成 PDF 时使用此技能。
---

# HTML to PDF - HTML 转 PDF

## 核心功能

### 1. 基础转换

```python
from weasyprint import HTML, CSS

def convert(html_path, output_path):
    """基础 HTML 转 PDF"""
    HTML(filename=html_path).write_pdf(output_path)

def convert_from_string(html_content, output_path):
    """从字符串转换"""
    HTML(string=html_content).write_pdf(output_path)

def convert_from_url(url, output_path):
    """从 URL 转换"""
    HTML(url=url).write_pdf(output_path)
```

### 2. 样式支持

```python
def convert_with_css(html_path, css_path, output_path):
    """带 CSS 样式转换"""
    html = HTML(filename=html_path)
    css = CSS(filename=css_path)
    html.write_pdf(output_path, stylesheets=[css])

def convert_with_styles(html_content, output_path):
    """内联样式转换"""
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            @page {{
                size: A4;
                margin: 2cm;
            }}
            body {{
                font-family: 'SimSun', serif;
                font-size: 12pt;
                line-height: 1.8;
            }}
            h1, h2, h3 {{
                font-family: 'SimHei', sans-serif;
            }}
        </style>
    </head>
    <body>{html_content}</body>
    </html>
    """
    HTML(string=styled_html).write_pdf(output_path)
```

### 3. 页眉页脚

```python
def convert_with_header_footer(html_path, output_path):
    """带页眉页脚转换"""
    html_with_hf = f"""
    <html>
    <head>
        <style>
            @page {{
                @top-center {{
                    content: "文档标题";
                }}
                @bottom-center {{
                    content: "第 " counter(page) " 页";
                }}
            }}
        </style>
    </head>
    <body>
        ...内容...
    </body>
    </html>
    """
    HTML(string=html_with_hf).write_pdf(output_path)
```

### 4. 分页控制

```css
/* CSS 分页控制 */
.page-break {
    page-break-after: always;
}

.avoid-break {
    page-break-inside: avoid;
}

/* 表格不分页 */
table {
    page-break-inside: avoid;
}

/* 图片不分页 */
img {
    page-break-inside: avoid;
}
```

## 中文支持

```python
def convert_chinese(html_content, output_path):
    """中文 HTML 转 PDF"""
    styled_html = f"""
    <html>
    <head>
        <style>
            @font-face {{
                font-family: 'SimSun';
                src: url('simsun.ttc');
            }}
            body {{
                font-family: 'SimSun', serif;
            }}
        </style>
    </head>
    <body>{html_content}</body>
    </html>
    """
    HTML(string=styled_html).write_pdf(output_path)
```

## 使用示例

```python
# 简单转换
convert("report.html", "report.pdf")

# 带样式转换
convert_with_css("page.html", "style.css", "output.pdf")

# 从 URL 转换
convert_from_url("https://example.com", "saved.pdf")
```