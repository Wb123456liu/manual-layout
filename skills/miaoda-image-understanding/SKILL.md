---
name: miaoda-image-understanding
description: 妙答图像理解技能，使用 AI 进行图像内容理解和分析。支持图像描述、物体识别、文字提取、场景分析等。当用户需要：(1) 分析图片内容 (2) 识别图中物体 (3) 提取图中文字 (4) 理解图像场景时使用此技能。
---

# Miaoda Image Understanding - 妙答图像理解

## 核心功能

### 1. 图像描述

```python
def describe_image(image_path, detail_level='normal'):
    """
    生成图像描述
    
    Args:
        image_path: 图片路径
        detail_level: 详细程度 ('brief', 'normal', 'detailed')
    
    Returns:
        图像的文字描述
    """
    # 调用视觉模型 API
    pass
```

### 2. 物体识别

```python
def detect_objects(image_path, categories=None):
    """
    识别图像中的物体
    
    Args:
        image_path: 图片路径
        categories: 指定识别类别（可选）
    
    Returns:
        物体列表，包含名称、位置、置信度
    """
    pass

def count_objects(image_path, object_type):
    """
    统计特定物体数量
    
    Args:
        image_path: 图片路径
        object_type: 物体类型
    
    Returns:
        物体数量
    """
    pass
```

### 3. 文字提取

```python
def extract_text(image_path, regions=None):
    """
    从图像中提取文字
    
    Args:
        image_path: 图片路径
        regions: 指定区域（可选）
    
    Returns:
        提取的文字内容
    """
    pass

def read_document(image_path):
    """
    读取文档图片
    
    Args:
        image_path: 文档图片路径
    
    Returns:
        结构化的文档内容
    """
    pass
```

### 4. 场景分析

```python
def analyze_scene(image_path):
    """
    分析图像场景
    
    Returns:
        场景类型、主要元素、氛围等
    """
    pass

def compare_images(image1_path, image2_path):
    """
    比较两张图片的相似度
    
    Returns:
        相似度分数和差异描述
    """
    pass
```

### 5. 问答

```python
def answer_question(image_path, question):
    """
    针对图像回答问题
    
    Args:
        image_path: 图片路径
        question: 问题
    
    Returns:
        答案
    """
    pass
```

## 使用示例

```python
# 描述图片
description = describe_image("photo.jpg")
print(description)
# 输出: "这是一张户外风景照片，蓝天白云下有一片绿色的草地..."

# 识别物体
objects = detect_objects("street.jpg")
for obj in objects:
    print(f"{obj['name']}: {obj['confidence']:.2%}")

# 提取文字
text = extract_text("document.png")
print(text)

# 问答
answer = answer_question("product.jpg", "这个产品是什么颜色的？")
print(answer)
```

## 支持的分析类型

| 类型 | 说明 |
|------|------|
| 描述 | 生成图像的整体描述 |
| 物体识别 | 识别并定位物体 |
| 文字提取 | OCR 提取文字 |
| 场景分析 | 分析场景类型和元素 |
| 问答 | 针对图像回答问题 |