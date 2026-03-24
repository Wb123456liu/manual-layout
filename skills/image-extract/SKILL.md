---
name: image-extract
description: 图片提取技能，用于从文档、网页、PDF 中提取图片。支持批量提取、格式转换、尺寸筛选、去重等。当用户需要：(1) 从文档提取图片 (2) 从 PDF 提取图片 (3) 批量下载图片 (4) 图片去重时使用此技能。
---

# Image Extract - 图片提取

## 核心功能

### 1. 从 PDF 提取图片

```python
import fitz  # PyMuPDF
from PIL import Image
import io

def extract_images_from_pdf(pdf_path, output_dir):
    """从 PDF 提取所有图片"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    images = []
    
    for page_num, page in enumerate(doc):
        image_list = page.get_images()
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            
            # 保存图片
            image_path = f"{output_dir}/page{page_num+1}_img{img_index+1}.{base_image['ext']}"
            with open(image_path, 'wb') as f:
                f.write(image_bytes)
            images.append(image_path)
    
    return images
```

### 2. 从 Word 提取图片

```python
from docx import Document
import zipfile
import os

def extract_images_from_docx(docx_path, output_dir):
    """从 Word 文档提取图片"""
    os.makedirs(output_dir, exist_ok=True)
    
    # Word 文档实际上是 ZIP 文件
    with zipfile.ZipFile(docx_path, 'r') as z:
        for name in z.namelist():
            if name.startswith('word/media/'):
                # 提取媒体文件
                data = z.read(name)
                filename = os.path.basename(name)
                with open(f"{output_dir}/{filename}", 'wb') as f:
                    f.write(data)
```

### 3. 从网页提取图片

```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def extract_images_from_webpage(url, output_dir, min_size=10000):
    """从网页提取图片"""
    os.makedirs(output_dir, exist_ok=True)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    images = []
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            img_url = urljoin(url, src)
            
            # 下载图片
            try:
                img_response = requests.get(img_url)
                if len(img_response.content) > min_size:
                    filename = os.path.basename(urlparse(img_url).path)
                    filepath = f"{output_dir}/{filename}"
                    with open(filepath, 'wb') as f:
                        f.write(img_response.content)
                    images.append(filepath)
            except:
                continue
    
    return images
```

### 4. 图片去重

```python
import hashlib

def get_image_hash(image_path):
    """计算图片哈希"""
    with open(image_path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def remove_duplicates(image_dir):
    """去除重复图片"""
    hashes = {}
    duplicates = []
    
    for filename in os.listdir(image_dir):
        filepath = os.path.join(image_dir, filename)
        if os.path.isfile(filepath):
            h = get_image_hash(filepath)
            if h in hashes:
                duplicates.append(filepath)
                os.remove(filepath)
            else:
                hashes[h] = filepath
    
    return duplicates
```

## 使用示例

```python
# 从 PDF 提取图片
images = extract_images_from_pdf("report.pdf", "./images")

# 从 Word 提取图片
extract_images_from_docx("document.docx", "./images")

# 从网页提取图片
extract_images_from_webpage("https://example.com", "./images")

# 去重
duplicates = remove_duplicates("./images")
```

## 支持的来源

| 来源 | 方法 |
|------|------|
| PDF | PyMuPDF |
| Word | ZIP 解压 |
| 网页 | BeautifulSoup |
| PPT | ZIP 解压 |