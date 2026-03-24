---
name: document-ocr
description: 文档 OCR 技能，用于识别图片和扫描文档中的文字。支持多语言识别、表格识别、手写识别、批量处理等。当用户需要：(1) 识别图片文字 (2) 处理扫描文档 (3) 提取表格数据 (4) 批量 OCR 时使用此技能。
---

# Document OCR - 文档 OCR

## 核心功能

### 1. 图片文字识别

```python
import pytesseract
from PIL import Image

def recognize_text(image_path, lang='chi_sim+eng'):
    """识别图片中的文字"""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang=lang)
    return text

def recognize_with_confidence(image_path, lang='chi_sim+eng'):
    """带置信度的识别"""
    image = Image.open(image_path)
    data = pytesseract.image_to_data(image, lang=lang, output_type=pytesseract.Output.DICT)
    return data
```

### 2. 表格识别

```python
def recognize_table(image_path):
    """识别表格结构"""
    image = Image.open(image_path)
    # 使用 pytesseract 的表格识别
    table_data = pytesseract.image_to_data(
        image,
        lang='chi_sim+eng',
        output_type=pytesseract.Output.DATAFRAME
    )
    return table_data
```

### 3. PDF OCR

```python
import pdf2image

def ocr_pdf(pdf_path, lang='chi_sim+eng'):
    """OCR 处理 PDF"""
    images = pdf2image.convert_from_path(pdf_path)
    results = []
    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image, lang=lang)
        results.append({
            'page': i + 1,
            'text': text
        })
    return results
```

### 4. 批量处理

```python
import os
from concurrent.futures import ThreadPoolExecutor

def batch_ocr(image_dir, output_dir, lang='chi_sim+eng'):
    """批量 OCR 处理"""
    os.makedirs(output_dir, exist_ok=True)
    
    def process_file(filename):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_dir, filename)
            text = recognize_text(image_path, lang)
            output_path = os.path.join(output_dir, f"{filename}.txt")
            with open(output_path, 'w') as f:
                f.write(text)
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(process_file, os.listdir(image_dir))
```

### 5. 预处理

```python
import cv2
import numpy as np

def preprocess_image(image_path):
    """图像预处理"""
    img = cv2.imread(image_path)
    
    # 灰度化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 二值化
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # 降噪
    denoised = cv2.medianBlur(binary, 3)
    
    return denoised
```

## 使用示例

```python
# 识别单张图片
text = recognize_text("scanned.png")
print(text)

# 处理扫描 PDF
results = ocr_pdf("scanned_document.pdf")
for r in results:
    print(f"第 {r['page']} 页:\n{r['text']}")

# 批量处理
batch_ocr("./images", "./output")
```

## 支持的语言

| 语言代码 | 说明 |
|----------|------|
| chi_sim | 简体中文 |
| chi_tra | 繁体中文 |
| eng | 英文 |
| jpn | 日文 |
| kor | 韩文 |