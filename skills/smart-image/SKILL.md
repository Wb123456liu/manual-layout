---
name: smart-image
description: 智能图片处理技能，用于文档中图片的智能处理。支持图片尺寸调整、位置设置、说明文字、图文环绕、图片压缩等。当用户需要：(1) 调整图片大小 (2) 设置图片位置 (3) 添加图片说明 (4) 处理图文混排 (5) 优化图片质量时使用此技能。
---

# Smart Image - 智能图片处理

## 核心功能

### 1. 图片尺寸

```css
/* 小图 */
.image-small {
  width: 30%;
  max-width: 300px;
}

/* 中图 */
.image-medium {
  width: 60%;
  max-width: 600px;
}

/* 大图 */
.image-large {
  width: 90%;
  max-width: 900px;
}

/* 全宽 */
.image-full {
  width: 100%;
}
```

### 2. 图片位置

```css
/* 居中 */
.image-center {
  display: block;
  margin: 1em auto;
}

/* 左浮动 */
.image-left {
  float: left;
  margin-right: 1em;
  margin-bottom: 0.5em;
}

/* 右浮动 */
.image-right {
  float: right;
  margin-left: 1em;
  margin-bottom: 0.5em;
}
```

### 3. 图片说明

```html
<figure class="image-container">
  <img src="image.png" alt="图片描述">
  <figcaption>图 1-1：图片说明文字</figcaption>
</figure>
```

```css
.image-container {
  text-align: center;
  margin: 1.5em 0;
}

.image-container img {
  max-width: 100%;
  height: auto;
}

.image-container figcaption {
  font-size: 10pt;
  color: #666;
  margin-top: 0.5em;
  font-style: italic;
}
```

### 4. 图文环绕

```css
/* 左图右文 */
.wrap-left {
  float: left;
  width: 40%;
  margin: 0 1em 1em 0;
  shape-outside: margin-box;
}

/* 右图左文 */
.wrap-right {
  float: right;
  width: 40%;
  margin: 0 0 1em 1em;
  shape-outside: margin-box;
}
```

### 5. 图片编号

```python
class ImageNumbering:
    def __init__(self):
        self.chapter = 1
        self.counter = 0
    
    def get_number(self):
        self.counter += 1
        return f"图 {self.chapter}-{self.counter}"
    
    def new_chapter(self):
        self.chapter += 1
        self.counter = 0
```

## 使用示例

### Markdown 图片

```markdown
![图片说明](image.png){width=60% .center}

*图 1-1：图片说明文字*
```

### HTML 模板

```html
<figure class="image-container center">
  <img src="diagram.png" 
       alt="系统架构图"
       width="600"
       loading="lazy">
  <figcaption>图 2-1：系统架构示意图</figcaption>
</figure>
```

## 图片处理原则

1. **尺寸适中** - 不超过页面宽度 90%
2. **说明清晰** - 每张图都有说明
3. **编号规范** - 按章节编号（如 图 1-2）
4. **位置合理** - 图片靠近相关文字
5. **质量优化** - 适当压缩，保持清晰