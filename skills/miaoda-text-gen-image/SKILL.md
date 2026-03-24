---
name: miaoda-text-gen-image
description: 妙答文字生成图片技能，使用 AI 根据文字描述生成图片。支持文生图、图生图、风格迁移、图片编辑等。当用户需要：(1) 根据描述生成图片 (2) 修改现有图片 (3) 风格转换 (4) AI 绘画时使用此技能。
---

# Miaoda Text Gen Image - 妙答文字生成图片

## 核心功能

### 1. 文生图

```python
def text_to_image(prompt, 
                  negative_prompt=None,
                  width=512,
                  height=512,
                  steps=20,
                  cfg_scale=7.0,
                  seed=None):
    """
    根据文字描述生成图片
    
    Args:
        prompt: 正向提示词
        negative_prompt: 负向提示词
        width: 图片宽度
        height: 图片高度
        steps: 生成步数
        cfg_scale: CFG 引导强度
        seed: 随机种子
    
    Returns:
        生成的图片
    """
    pass
```

### 2. 图生图

```python
def image_to_image(input_image,
                   prompt,
                   strength=0.75,
                   **kwargs):
    """
    基于输入图片生成新图片
    
    Args:
        input_image: 输入图片
        prompt: 提示词
        strength: 变化强度 (0-1)
    
    Returns:
        生成的新图片
    """
    pass
```

### 3. 局部重绘

```python
def inpaint(image,
            mask,
            prompt,
            **kwargs):
    """
    局部重绘
    
    Args:
        image: 原图
        mask: 蒙版（白色区域会被重绘）
        prompt: 重绘提示词
    
    Returns:
        重绘后的图片
    """
    pass
```

### 4. 图片扩展

```python
def outpaint(image,
             direction,
             expand_size,
             prompt=None,
             **kwargs):
    """
    扩展图片边界
    
    Args:
        image: 原图
        direction: 扩展方向 ('left', 'right', 'top', 'bottom')
        expand_size: 扩展尺寸
        prompt: 提示词
    
    Returns:
        扩展后的图片
    """
    pass
```

### 5. 风格迁移

```python
def style_transfer(content_image,
                   style_prompt,
                   strength=0.5,
                   **kwargs):
    """
    风格迁移
    
    Args:
        content_image: 内容图片
        style_prompt: 风格描述
        strength: 风格强度
    
    Returns:
        风格迁移后的图片
    """
    pass
```

## 提示词技巧

### 通用模板

```
[主体] + [动作/状态] + [环境] + [风格] + [质量标签]

示例：
一只可爱的猫咪，坐在窗台上，阳光明媚的午后，油画风格，高清细节
```

### 质量标签

```
正向：masterpiece, best quality, high resolution, detailed
负向：low quality, blurry, watermark, bad anatomy
```

### 风格关键词

| 风格 | 关键词 |
|------|--------|
| 写实 | photorealistic, realistic, 8k |
| 动漫 | anime style, manga |
| 油画 | oil painting, canvas texture |
| 水彩 | watercolor, soft colors |
| 赛素 | sketch, pencil drawing |

## 使用示例

```python
# 文生图
img = text_to_image(
    prompt="一只橘猫在阳光下打盹，温馨的室内场景",
    width=1024,
    height=768
)

# 图生图
new_img = image_to_image(
    input_image="photo.jpg",
    prompt="转换为水彩画风格",
    strength=0.6
)

# 局部重绘
result = inpaint(
    image="portrait.jpg",
    mask="mask.png",
    prompt="戴上一副墨镜"
)
```