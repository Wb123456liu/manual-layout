---
name: typeset-pro
description: 专业排版技能，用于手册、文档的专业排版处理。支持字体设置、段落间距、对齐方式、缩进控制等排版功能。当用户需要：(1) 设置文档字体和字号 (2) 调整段落间距和行距 (3) 设置对齐方式 (4) 处理缩进和悬挂缩进 (5) 进行专业排版时使用此技能。
---

# Typeset Pro - 专业排版

## 核心功能

### 1. 字体设置

```css
/* 标题字体 */
font-family: "思源黑体", "Source Han Sans", sans-serif;

/* 正文字体 */
font-family: "思源宋体", "Source Han Serif", serif;

/* 代码字体 */
font-family: "JetBrains Mono", "Fira Code", monospace;
```

### 2. 字号规范

| 元素 | 字号 | 行高 |
|------|------|------|
| 一级标题 | 24pt | 1.4 |
| 二级标题 | 18pt | 1.4 |
| 三级标题 | 14pt | 1.5 |
| 正文 | 12pt | 1.75 |
| 脚注 | 10pt | 1.5 |

### 3. 段落间距

- 段前间距：0.5 行
- 段后间距：0.5 行
- 首行缩进：2 字符
- 行间距：1.75 倍

### 4. 对齐方式

- 标题：居中对齐
- 正文：两端对齐
- 图片说明：居中对齐
- 表格内容：左对齐

## 使用方法

### Markdown 排版

```markdown
# 一级标题（居中，24pt）

## 二级标题（左对齐，18pt）

正文内容，首行缩进两字符，两端对齐。
```

### CSS 样式模板

```css
/* 专业文档排版样式 */
.document {
  font-family: "思源宋体", serif;
  font-size: 12pt;
  line-height: 1.75;
  text-align: justify;
  text-indent: 2em;
}

.document h1 {
  font-family: "思源黑体", sans-serif;
  font-size: 24pt;
  text-align: center;
  text-indent: 0;
  margin-top: 24pt;
  margin-bottom: 12pt;
}

.document h2 {
  font-family: "思源黑体", sans-serif;
  font-size: 18pt;
  text-align: left;
  text-indent: 0;
  margin-top: 18pt;
  margin-bottom: 9pt;
}
```

## 排版原则

1. **一致性** - 全文档使用统一的字体、字号、间距
2. **层次感** - 标题与正文有明显区分
3. **可读性** - 行长不超过 45-75 字符
4. **美观性** - 合理的留白和对齐