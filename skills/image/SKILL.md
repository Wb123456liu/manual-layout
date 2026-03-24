---
name: image
description: 图片处理技能，用于图片的基本处理和转换。支持格式转换、尺寸调整、裁剪、旋转、压缩等。当用户需要：(1) 转换图片格式 (2) 调整图片大小 (3) 裁剪图片 (4) 压缩图片时使用此技能。
---

# Image - 图片处理

## 核心功能

### 1. 格式转换

```python
from PIL import Image

def convert_format(input_path, output_path, format='PNG'):
    """转换图片格式"""
    img = Image.open(input_path)
    if format in ['JPEG', 'JPG']:
        img = img.convert('RGB')
    img.save(output_path, format=format)

def batch_convert(input_dir, output_dir, format='PNG'):
    """批量格式转换"""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            input_path = os.path.join(input_dir, filename)
            name = os.path.splitext(filename)[0]
            output_path = os.path.join(output_dir, f"{name}.{format.lower()}")
            convert_format(input_path, output_path, format)
```

### 2. 尺寸调整

```python
def resize(input_path, output_path, width=None, height=None, keep_ratio=True):
    """调整图片尺寸"""
    img = Image.open(input_path)
    
    if keep_ratio:
        original_width, original_height = img.size
        if width and not height:
            ratio = width / original_width
            height = int(original_height * ratio)
        elif height and not width:
            ratio = height / original_height
            width = int(original_width * ratio)
    
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    img.save(output_path)

def resize_to_max(input_path, output_path, max_size):
    """限制最大尺寸"""
    img = Image.open(input_path)
    img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
    img.save(output_path)
```

### 3. 裁剪

```python
def crop(input_path, output_path, box):
    """裁剪图片 (left, upper, right, lower)"""
    img = Image.open(input_path)
    img = img.crop(box)
    img.save(output_path)

def crop_center(input_path, output_path, width, height):
    """居中裁剪"""
    img = Image.open(input_path)
    original_width, original_height = img.size
    
    left = (original_width - width) / 2
    upper = (original_height - height) / 2
    right = (original_width + width) / 2
    lower = (original_height + height) / 2
    
    img = img.crop((left, upper, right, lower))
    img.save(output_path)
```

### 4. 旋转

```python
def rotate(input_path, output_path, degrees, expand=True):
    """旋转图片"""
    img = Image.open(input_path)
    img = img.rotate(degrees, expand=expand)
    img.save(output_path)

def flip_horizontal(input_path, output_path):
    """水平翻转"""
    img = Image.open(input_path)
    img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    img.save(output_path)

def flip_vertical(input_path, output_path):
    """垂直翻转"""
    img = Image.open(input_path)
    img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    img.save(output_path)
```

### 5. 压缩

```python
def compress(input_path, output_path, quality=85):
    """压缩图片"""
    img = Image.open(input_path)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    img.save(output_path, 'JPEG', quality=quality, optimize=True)

def compress_to_size(input_path, output_path, max_size_kb):
    """压缩到指定大小"""
    quality = 95
    while quality > 10:
        compress(input_path, output_path, quality)
        if os.path.getsize(output_path) <= max_size_kb * 1024:
            break
        quality -= 5
```

## 使用示例

```python
# 格式转换
convert_format("photo.png", "photo.jpg", "JPEG")

# 调整大小
resize("large.png", "small.png", width=800)

# 居中裁剪
crop_center("photo.jpg", "avatar.jpg", 200, 200)

# 压缩
compress("original.jpg", "compressed.jpg", quality=70)
```

## 支持的格式

| 格式 | 说明 |
|------|------|
| JPEG | 有损压缩，适合照片 |
| PNG | 无损压缩，支持透明 |
| GIF | 支持动画 |
| BMP | 无压缩 |
| WebP | 高效压缩 |