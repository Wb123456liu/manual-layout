---
name: miaoda-doc-parse
description: 妙答文档解析技能，用于解析各种格式的文档。支持 PDF、Word、Excel、PPT、Markdown 等格式的解析和内容提取。当用户需要：(1) 解析文档内容 (2) 提取文档数据 (3) 转换文档格式 (4) 分析文档结构时使用此技能。
---

# Miaoda Doc Parse - 妙答文档解析

## 核心功能

### 1. PDF 解析

```python
import fitz  # PyMuPDF

def parse_pdf(pdf_path):
    """解析 PDF 文档"""
    doc = fitz.open(pdf_path)
    
    content = {
        'metadata': doc.metadata,
        'pages': [],
        'toc': doc.get_toc()
    }
    
    for page_num, page in enumerate(doc):
        text = page.get_text()
        images = page.get_images()
        
        content['pages'].append({
            'number': page_num + 1,
            'text': text,
            'images': len(images)
        })
    
    return content

def extract_pdf_text(pdf_path):
    """提取 PDF 全文"""
    doc = fitz.open(pdf_path)
    return '\n'.join(page.get_text() for page in doc)
```

### 2. Word 解析

```python
from docx import Document

def parse_docx(docx_path):
    """解析 Word 文档"""
    doc = Document(docx_path)
    
    content = {
        'paragraphs': [],
        'tables': [],
        'images': []
    }
    
    # 提取段落
    for para in doc.paragraphs:
        if para.text.strip():
            content['paragraphs'].append({
                'text': para.text,
                'style': para.style.name
            })
    
    # 提取表格
    for table in doc.tables:
        table_data = []
        for row in table.rows:
            row_data = [cell.text for cell in row.cells]
            table_data.append(row_data)
        content['tables'].append(table_data)
    
    return content
```

### 3. Excel 解析

```python
import pandas as pd

def parse_excel(excel_path, sheet_name=None):
    """解析 Excel 文档"""
    if sheet_name:
        df = pd.read_excel(excel_path, sheet_name=sheet_name)
    else:
        # 读取所有工作表
        xl = pd.ExcelFile(excel_path)
        return {sheet: pd.read_excel(excel_path, sheet_name=sheet)
                for sheet in xl.sheet_names}
    
    return df

def excel_to_dict(excel_path):
    """Excel 转字典列表"""
    df = pd.read_excel(excel_path)
    return df.to_dict('records')
```

### 4. PPT 解析

```python
from pptx import Presentation

def parse_pptx(pptx_path):
    """解析 PPT 文档"""
    prs = Presentation(pptx_path)
    
    content = {
        'slides': []
    }
    
    for slide_num, slide in enumerate(prs.slides):
        slide_content = {
            'number': slide_num + 1,
            'shapes': []
        }
        
        for shape in slide.shapes:
            if hasattr(shape, 'text') and shape.text:
                slide_content['shapes'].append({
                    'type': 'text',
                    'content': shape.text
                })
            elif shape.shape_type == 13:  # 图片
                slide_content['shapes'].append({
                    'type': 'image'
                })
        
        content['slides'].append(slide_content)
    
    return content
```

### 5. Markdown 解析

```python
import re

def parse_markdown(md_path):
    """解析 Markdown 文档"""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    result = {
        'headings': [],
        'code_blocks': [],
        'links': [],
        'images': []
    }
    
    # 提取标题
    headings = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
    for level, text in headings:
        result['headings'].append({
            'level': len(level),
            'text': text
        })
    
    # 提取代码块
    code_blocks = re.findall(r'```(\w*)\n(.+?)```', content, re.DOTALL)
    for lang, code in code_blocks:
        result['code_blocks'].append({
            'language': lang,
            'code': code
        })
    
    # 提取链接
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    result['links'] = [{'text': t, 'url': u} for t, u in links]
    
    # 提取图片
    images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
    result['images'] = [{'alt': a, 'url': u} for a, u in images]
    
    return result
```

## 统一接口

```python
def parse_document(file_path):
    """统一文档解析接口"""
    ext = file_path.lower().split('.')[-1]
    
    parsers = {
        'pdf': parse_pdf,
        'docx': parse_docx,
        'xlsx': parse_excel,
        'pptx': parse_pptx,
        'md': parse_markdown
    }
    
    parser = parsers.get(ext)
    if parser:
        return parser(file_path)
    
    raise ValueError(f"不支持的文件格式: {ext}")
```

## 使用示例

```python
# 解析 PDF
pdf_content = parse_pdf("document.pdf")
print(f"页数: {len(pdf_content['pages'])}")

# 解析 Word
doc_content = parse_docx("report.docx")
print(f"段落数: {len(doc_content['paragraphs'])}")

# 统一接口
content = parse_document("data.xlsx")
```

## 支持的格式

| 格式 | 库 | 功能 |
|------|-----|------|
| PDF | PyMuPDF | 文本、图片、目录 |
| Word | python-docx | 段落、表格、图片 |
| Excel | pandas | 数据、工作表 |
| PPT | python-pptx | 幻灯片、形状 |
| Markdown | re | 标题、代码、链接 |