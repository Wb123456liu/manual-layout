---
name: bilingual-sync
description: 双语同步技能，用于中英文双语文档的同步管理。支持双语对照、段落对齐、翻译标记、版本同步等。当用户需要：(1) 创建双语文档 (2) 同步中英文内容 (3) 管理翻译版本 (4) 生成对照文档时使用此技能。
---

# Bilingual Sync - 双语同步

## 核心功能

### 1. 双语文档结构

```markdown
# 产品手册 / Product Manual

## 概述 / Overview

**中文：**
这是产品概述的中文内容。

**English:**
This is the product overview in English.

---

## 功能说明 / Features

### 功能一 / Feature One

**中文：**
功能一的详细说明。

**English:**
Detailed description of feature one.
```

### 2. 段落对齐

```html
<div class="bilingual">
  <div class="zh">
    <p>中文段落内容。</p>
  </div>
  <div class="en">
    <p>English paragraph content.</p>
  </div>
</div>
```

```css
.bilingual {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2em;
}

.bilingual .zh {
  border-right: 1px solid #e5e5e5;
  padding-right: 1em;
}

.bilingual .en {
  padding-left: 1em;
}
```

### 3. 翻译状态标记

```markdown
<!-- 翻译状态：已完成 ✓ -->
**中文：** 已完成翻译的段落。

**English:** Translated paragraph.

---

<!-- 翻译状态：待翻译 ⏳ -->
**中文：** 还未翻译的段落。

**English:** [待翻译 / To be translated]
```

### 4. 同步管理

```python
class BilingualSync:
    def __init__(self):
        self.paragraphs = []
    
    def add(self, zh_content, en_content=None, status='pending'):
        """添加双语段落"""
        self.paragraphs.append({
            'zh': zh_content,
            'en': en_content,
            'status': status  # 'done', 'pending', 'review'
        })
    
    def get_pending(self):
        """获取待翻译段落"""
        return [p for p in self.paragraphs if p['status'] == 'pending']
    
    def sync(self, index, en_content):
        """同步翻译"""
        self.paragraphs[index]['en'] = en_content
        self.paragraphs[index]['status'] = 'done'
    
    def export(self, format='parallel'):
        """导出双语文档"""
        if format == 'parallel':
            return self._export_parallel()
        elif format == 'separate':
            return self._export_separate()
```

### 5. 对照视图

```css
/* 并排对照 */
.view-parallel .bilingual {
  display: grid;
  grid-template-columns: 1fr 1fr;
}

/* 上下对照 */
.view-stacked .bilingual {
  display: block;
}

.view-stacked .zh,
.view-stacked .en {
  margin-bottom: 1em;
}

/* 标签样式 */
.lang-label {
  font-size: 0.8em;
  font-weight: 600;
  color: #666;
  text-transform: uppercase;
}
```

## 使用示例

### 创建双语文档

```python
doc = BilingualSync()

doc.add(
    zh="产品名称是一款智能排版工具。",
    en="Product Name is an intelligent typesetting tool.",
    status='done'
)

doc.add(
    zh="它支持多种文档格式。",
    status='pending'
)

# 查看待翻译
pending = doc.get_pending()
print(f"待翻译：{len(pending)} 段")
```

### Markdown 模板

```markdown
---
title: 产品手册
title_en: Product Manual
lang: zh-CN
---

# {{title}} / {{title_en}}

{% for para in paragraphs %}
## {{para.section}}

**中文：**
{{para.zh}}

**English：**
{{para.en or '[待翻译]'}}

---
{% endfor %}
```

## 双语同步原则

1. **段落对齐** - 中英文段落一一对应
2. **状态跟踪** - 标记翻译状态
3. **版本同步** - 中文更新时同步英文
4. **格式统一** - 双方使用相同格式