---
name: style-kit
description: 样式工具包，提供预设样式模板和样式管理功能。包含标题样式、段落样式、列表样式、表格样式、代码样式等预设。当用户需要：(1) 应用预设样式 (2) 创建自定义样式 (3) 管理样式库 (4) 批量修改样式时使用此技能。
---

# Style Kit - 样式工具包

## 预设样式库

### 1. 标题样式

```css
/* 标题样式预设 */
.heading-1 {
  font-size: 24pt;
  font-weight: 700;
  color: #1a1a1a;
  margin-top: 24pt;
  margin-bottom: 12pt;
}

.heading-2 {
  font-size: 18pt;
  font-weight: 600;
  color: #333;
  margin-top: 18pt;
  margin-bottom: 9pt;
}

.heading-3 {
  font-size: 14pt;
  font-weight: 600;
  color: #444;
  margin-top: 14pt;
  margin-bottom: 7pt;
}
```

### 2. 段落样式

```css
/* 正文段落 */
.paragraph {
  font-size: 12pt;
  line-height: 1.75;
  text-align: justify;
  text-indent: 2em;
  margin-bottom: 0.5em;
}

/* 引用段落 */
.quote {
  font-style: italic;
  padding-left: 1.5em;
  border-left: 3px solid #666;
  color: #555;
}
```

### 3. 列表样式

```css
/* 有序列表 */
.ordered-list {
  list-style-type: decimal;
  padding-left: 2em;
  line-height: 1.75;
}

/* 无序列表 */
.unordered-list {
  list-style-type: disc;
  padding-left: 2em;
  line-height: 1.75;
}
```

### 4. 表格样式

```css
.table {
  width: 100%;
  border-collapse: collapse;
  font-size: 11pt;
}

.table th {
  background: #f5f5f5;
  font-weight: 600;
  padding: 8pt;
  border: 1px solid #ddd;
}

.table td {
  padding: 8pt;
  border: 1px solid #ddd;
}
```

### 5. 代码样式

```css
.code-inline {
  font-family: "JetBrains Mono", monospace;
  font-size: 0.9em;
  background: #f4f4f4;
  padding: 0.2em 0.4em;
  border-radius: 3px;
}

.code-block {
  font-family: "JetBrains Mono", monospace;
  font-size: 10pt;
  line-height: 1.5;
  background: #282c34;
  color: #abb2bf;
  padding: 1em;
  border-radius: 6px;
  overflow-x: auto;
}
```

## 样式模板

### 技术文档模板

```css
.tech-doc {
  --heading-font: "思源黑体", sans-serif;
  --body-font: "思源宋体", serif;
  --code-font: "JetBrains Mono", monospace;
  --primary-color: #2563eb;
  --text-color: #1a1a1a;
}
```

### 产品手册模板

```css
.product-manual {
  --heading-font: "苹方", sans-serif;
  --body-font: "苹方", serif;
  --primary-color: #10b981;
  --text-color: #374151;
}
```

## 使用方法

1. 选择合适的样式模板
2. 根据需要调整变量值
3. 应用到文档中

## 样式管理原则

1. **一致性** - 同类元素使用相同样式
2. **可复用** - 使用 CSS 变量便于修改
3. **层次清晰** - 标题层级分明
4. **可读性** - 保证阅读舒适