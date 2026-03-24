---
name: pdf-editor
description: PDF 编辑器技能，用于编辑和修改 PDF 文件。支持页面操作、文本编辑、合并拆分、水印添加等。当用户需要：(1) 编辑 PDF 内容 (2) 合并多个 PDF (3) 拆分 PDF (4) 添加水印时使用此技能。
---

# PDF Editor - PDF 编辑器

## 核心功能

### 1. 页面操作

```python
from PyPDF2 import PdfReader, PdfWriter

def extract_pages(pdf_path, pages, output_path):
    """提取指定页面"""
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page_num in pages:
        writer.add_page(reader.pages[page_num])
    with open(output_path, 'wb') as f:
        writer.write(f)

def rotate_pages(pdf_path, rotation, output_path):
    """旋转页面"""
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(rotation)
        writer.add_page(page)
    with open(output_path, 'wb') as f:
        writer.write(f)
```

### 2. 合并拆分

```python
def merge_pdfs(pdf_list, output_path):
    """合并多个 PDF"""
    writer = PdfWriter()
    for pdf_path in pdf_list:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, 'wb') as f:
        writer.write(f)

def split_pdf(pdf_path, output_dir):
    """拆分 PDF 为单页"""
    reader = PdfReader(pdf_path)
    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        with open(f"{output_dir}/page_{i+1}.pdf", 'wb') as f:
            writer.write(f)
```

### 3. 水印添加

```python
def add_watermark(pdf_path, watermark_text, output_path):
    """添加文字水印"""
    # 使用 reportlab 创建水印
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    
    # 创建水印 PDF
    watermark_pdf = "watermark.pdf"
    c = canvas.Canvas(watermark_pdf, pagesize=letter)
    c.setFont("Helvetica", 50)
    c.setFillColorRGB(0.5, 0.5, 0.5, alpha=0.3)
    c.rotate(45)
    c.drawString(200, 200, watermark_text)
    c.save()
    
    # 合并水印到原 PDF
    # ... 合并逻辑
```

### 4. 元信息操作

```python
def get_metadata(pdf_path):
    """获取 PDF 元信息"""
    reader = PdfReader(pdf_path)
    return reader.metadata

def set_metadata(pdf_path, metadata, output_path):
    """设置 PDF 元信息"""
    reader = PdfReader(pdf_path)
    writer = PdfWriter()
    writer.add_pages(reader.pages)
    writer.add_metadata(metadata)
    with open(output_path, 'wb') as f:
        writer.write(f)
```

## 使用示例

```python
# 合并多个报告
merge_pdfs(["report1.pdf", "report2.pdf"], "combined.pdf")

# 提取第 1-3 页
extract_pages("document.pdf", [0, 1, 2], "extracted.pdf")
```

## 常用操作

| 操作 | 说明 |
|------|------|
| 合并 | 多个 PDF 合并为一个 |
| 拆分 | 一个 PDF 拆分为多页 |
| 旋转 | 旋转页面 90/180/270 度 |
| 提取 | 提取指定页面 |
| 水印 | 添加文字或图片水印 |