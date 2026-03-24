---
name: multi-column
description: 多栏布局技能，用于创建双栏、三栏或多栏文档布局。支持响应式布局、栏间距设置、跨栏内容等。当用户需要：(1) 创建双栏排版 (2) 设置三栏布局 (3) 处理跨栏标题 (4) 调整栏间距 (5) 实现响应式多栏时使用此技能。
---

# Multi Column - 多栏布局

## 核心功能

### 1. 双栏布局

```css
.two-column {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2em;
}

/* 或使用 columns */
.two-column {
  columns: 2;
  column-gap: 2em;
}
```

### 2. 三栏布局

```css
.three-column {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  gap: 1.5em;
}
```

### 3. 跨栏标题

```css
.span-all {
  column-span: all;
  text-align: center;
}
```

### 4. 栏间距设置

| 布局类型 | 推荐间距 |
|----------|----------|
| 双栏 | 2em (约 24pt) |
| 三栏 | 1.5em (约 18pt) |
| 四栏+ | 1em (约 12pt) |

## 使用示例

### Markdown 多栏

```markdown
::: two-column
左栏内容

右栏内容
:::
```

### HTML 模板

```html
<div class="two-column">
  <div class="column">
    <h3>左栏标题</h3>
    <p>左栏内容...</p>
  </div>
  <div class="column">
    <h3>右栏标题</h3>
    <p>右栏内容...</p>
  </div>
</div>
```

### CSS 完整样式

```css
.multi-column {
  columns: 2;
  column-gap: 2em;
  column-rule: 1px solid #ccc;
}

.multi-column h2 {
  column-span: all;
  break-after: avoid;
}

.multi-column p {
  break-inside: avoid;
}
```

## 响应式布局

```css
/* 移动端单栏 */
@media (max-width: 768px) {
  .multi-column {
    columns: 1;
  }
}

/* 平板双栏 */
@media (min-width: 769px) and (max-width: 1024px) {
  .multi-column {
    columns: 2;
  }
}

/* 桌面三栏 */
@media (min-width: 1025px) {
  .multi-column {
    columns: 3;
  }
}
```

## 排版原则

1. **栏数适中** - 不超过 3-4 栏，避免阅读困难
2. **间距合理** - 栏间距大于段落间距
3. **避免断行** - 重要内容不要跨栏断开
4. **视觉平衡** - 各栏内容量尽量均衡