---
name: manual-typesetting
description: 手册排版技能，专门用于产品手册、用户手册的专业排版。支持章节结构、图文混排、页眉页脚、目录生成、样式模板等。当用户需要：(1) 排版产品手册 (2) 制作用户指南 (3) 创建技术文档 (4) 生成说明书时使用此技能。
---

# Manual Typesetting - 手册排版

## 核心功能

### 1. 文档结构

```markdown
# 产品名称 用户手册

**版本：** V1.0  
**日期：** 2024-01-01

---

## 目录

1. 产品概述
2. 快速入门
3. 功能说明
4. 常见问题
5. 附录

---

## 1. 产品概述

### 1.1 产品简介

### 1.2 适用范围

### 1.3 技术参数

## 2. 快速入门

### 2.1 开箱检查

### 2.2 安装步骤

### 2.3 首次使用
```

### 2. 图文排版规范

```css
/* 手册排版样式 */
.manual {
    font-family: "思源宋体", serif;
    font-size: 12pt;
    line-height: 1.8;
}

.manual h1 {
    font-family: "思源黑体", sans-serif;
    font-size: 22pt;
    text-align: center;
    margin-top: 24pt;
}

.manual h2 {
    font-size: 16pt;
    margin-top: 18pt;
}

.manual h3 {
    font-size: 14pt;
    margin-top: 12pt;
}

/* 图片样式 */
.manual figure {
    text-align: center;
    margin: 1em 0;
}

.manual figcaption {
    font-size: 10pt;
    color: #666;
    margin-top: 0.5em;
}

/* 表格样式 */
.manual table {
    width: 100%;
    border-collapse: collapse;
}

.manual th, .manual td {
    border: 1px solid #333;
    padding: 8pt;
}

/* 注意事项 */
.manual .notice {
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 1em;
    margin: 1em 0;
}

.manual .warning {
    background: #f8d7da;
    border-left: 4px solid #dc3545;
    padding: 1em;
    margin: 1em 0;
}
```

### 3. 页眉页脚模板

```html
<!-- 页眉 -->
<header>
    <span class="left">产品名称 用户手册</span>
    <span class="right">V1.0</span>
</header>

<!-- 页脚 -->
<footer>
    <span class="center">第 <span class="page"></span> 页</span>
</footer>
```

### 4. 常用元素模板

#### 步骤说明

```markdown
**操作步骤：**

1. 第一步操作
2. 第二步操作
3. 第三步操作

![步骤示意图](step.png)
*图 1：操作步骤示意*
```

#### 参数表格

```markdown
**技术参数：**

| 参数 | 规格 | 说明 |
|------|------|------|
| 尺寸 | 200×150×50mm | 长×宽×高 |
| 重量 | 500g | 含电池 |
| 功率 | 10W | 额定功率 |
```

#### 注意事项

```markdown
> ⚠️ **注意：** 请确保电源已断开后再进行操作。

> 🔥 **警告：** 禁止在高温环境下使用。
```

## 排版原则

1. **层次清晰** - 标题层级不超过 4 级
2. **图文并茂** - 每个步骤配图说明
3. **重点突出** - 注意事项用特殊样式
4. **易于查阅** - 完整目录和索引