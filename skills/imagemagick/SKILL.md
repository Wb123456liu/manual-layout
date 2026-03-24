---
name: imagemagick
description: ImageMagick 图像处理技能，提供强大的命令行图像处理能力。支持批量处理、高级转换、特效处理、元数据操作等。当用户需要：(1) 高级图像处理 (2) 批量转换 (3) 添加特效 (4) 处理元数据时使用此技能。
---

# ImageMagick - 图像处理

## 核心功能

### 1. 基础转换

```bash
# 格式转换
convert input.png output.jpg

# 调整大小
convert input.jpg -resize 800x600 output.jpg

# 保持比例调整
convert input.jpg -resize 800x output.jpg

# 缩放到指定百分比
convert input.jpg -resize 50% output.jpg
```

### 2. 批量处理

```bash
# 批量调整大小
mogrify -resize 800x600 *.jpg

# 批量格式转换
mogrify -format png *.jpg

# 批量压缩
mogrify -quality 85 *.jpg
```

### 3. 裁剪和旋转

```bash
# 裁剪
convert input.jpg -crop 800x600+100+50 output.jpg

# 居中裁剪
convert input.jpg -gravity center -crop 200x200+0+0 output.jpg

# 旋转
convert input.jpg -rotate 90 output.jpg

# 自动旋转（根据 EXIF）
convert input.jpg -auto-orient output.jpg
```

### 4. 特效处理

```bash
# 模糊
convert input.jpg -blur 0x4 output.jpg

# 锐化
convert input.jpg -sharpen 0x2 output.jpg

# 灰度
convert input.jpg -colorspace Gray output.jpg

# 反色
convert input.jpg -negate output.jpg

# 边缘检测
convert input.jpg -edge 1 output.jpg

# 浮雕
convert input.jpg -emboss 2 output.jpg
```

### 5. 水印

```bash
# 文字水印
convert input.jpg -pointsize 36 -fill white \
  -gravity southeast -annotate +10+10 "Copyright" \
  output.jpg

# 图片水印
composite -dissolve 50% -gravity southeast \
  watermark.png input.jpg output.jpg
```

### 6. 元数据

```bash
# 查看 EXIF 信息
identify -verbose input.jpg

# 删除 EXIF
convert input.jpg -strip output.jpg

# 设置注释
convert input.jpg -comment "My photo" output.jpg
```

## Python 封装

```python
import subprocess

def imagemagick_convert(input_path, output_path, options):
    """ImageMagick 转换"""
    cmd = ['convert', input_path] + options + [output_path]
    subprocess.run(cmd, check=True)

def resize(input_path, output_path, width, height=None):
    """调整大小"""
    size = f"{width}x{height}" if height else f"{width}"
    imagemagick_convert(input_path, output_path, ['-resize', size])

def add_watermark(input_path, watermark_path, output_path, opacity=50):
    """添加水印"""
    cmd = [
        'composite', '-dissolve', f'{opacity}%',
        '-gravity', 'southeast',
        watermark_path, input_path, output_path
    ]
    subprocess.run(cmd, check=True)
```

## 使用示例

```bash
# 创建缩略图
convert photo.jpg -thumbnail 200x200 -gravity center -extent 200x200 thumb.jpg

# 拼接图片
convert img1.jpg img2.jpg +append combined.jpg

# 制作 GIF 动画
convert -delay 100 frame*.jpg animation.gif

# PDF 转图片
convert document.pdf page.png
```