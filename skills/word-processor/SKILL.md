---
name: word-processor
description: Word 文档处理器，用于创建、编辑、转换 Word 文档。支持 DOCX 格式读写、样式设置、表格操作、模板应用等。当用户需要：(1) 创建 Word 文档 (2) 编辑 DOCX 文件 (3) 设置文档样式 (4) 插入表格图片时使用此技能。
---

# Word Processor - Word 文档处理器

## 核心功能

### 1. 创建文档

```python
from docx import Document

def create_document():
    """创建新文档"""
    return Document()

def add_paragraph(doc, text, style=None):
    """添加段落"""
    return doc.add_paragraph(text, style=style)

def add_heading(doc, text, level=1):
    """添加标题"""
    return doc.add_heading(text, level=level)
```

### 2. 样式设置

```python
def set_paragraph_format(paragraph, 
                         font_name='宋体',
                         font_size=12,
                         bold=False,
                         alignment='left'):
    """设置段落格式"""
    run = paragraph.runs[0] if paragraph.runs else paragraph.add_run()
    run.font.name = font_name
    run.font.size = Pt(font_size)
    run.font.bold = bold
    
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    align_map = {
        'left': WD_ALIGN_PARAGRAPH.LEFT,
        'center': WD_ALIGN_PARAGRAPH.CENTER,
        'right': WD_ALIGN_PARAGRAPH.RIGHT
    }
    paragraph.alignment = align_map.get(alignment)
```

### 3. 表格操作

```python
def add_table(doc, rows, cols, data=None):
    """添加表格"""
    table = doc.add_table(rows=rows, cols=cols)
    if data:
        for i, row_data in enumerate(data):
            for j, cell_data in enumerate(row_data):
                table.rows[i].cells[j].text = str(cell_data)
    return table

def set_table_style(table, style='Table Grid'):
    """设置表格样式"""
    table.style = style
```

### 4. 图片插入

```python
def add_image(doc, image_path, width=None, height=None):
    """插入图片"""
    if width:
        doc.add_picture(image_path, width=Inches(width))
    elif height:
        doc.add_picture(image_path, height=Inches(height))
    else:
        doc.add_picture(image_path)
```

## 使用示例

```python
# 创建报告文档
doc = create_document()
add_heading(doc, "工作报告", level=1)
add_paragraph(doc, "这是报告内容...")
add_table(doc, 3, 3, [
    ["项目", "进度", "负责人"],
    ["项目A", "80%", "张三"],
    ["项目B", "60%", "李四"]
])
doc.save("report.docx")
```

## 中文排版规范

| 元素 | 字体 | 字号 |
|------|------|------|
| 标题 | 黑体 | 16pt |
| 正文 | 宋体 | 12pt |
| 脚注 | 宋体 | 10pt |