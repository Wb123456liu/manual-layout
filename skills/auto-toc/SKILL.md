---
name: auto-toc
description: 自动目录生成技能，自动从文档内容生成目录/大纲。支持多级目录、目录样式设置、目录更新、锚点链接等。当用户需要：(1) 生成文档目录 (2) 创建章节大纲 (3) 添加目录跳转链接 (4) 更新目录内容时使用此技能。
---

# Auto TOC - 自动目录

## 核心功能

### 1. 从 Markdown 生成目录

```python
import re

def generate_toc(markdown_text):
    """从 Markdown 标题生成目录"""
    toc = []
    lines = markdown_text.split('\n')
    
    for line in lines:
        # 匹配 Markdown 标题
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            title = match.group(2)
            anchor = title.lower().replace(' ', '-')
            toc.append({
                'level': level,
                'title': title,
                'anchor': anchor
            })
    
    return toc
```

### 2. 目录输出格式

#### Markdown 格式

```markdown
## 目录

1. [第一章 概述](#第一章-概述)
   - [1.1 背景](#11-背景)
   - [1.2 目标](#12-目标)
2. [第二章 方案](#第二章-方案)
   - [2.1 设计思路](#21-设计思路)
   - [2.2 实施步骤](#22-实施步骤)
```

#### HTML 格式

```html
<nav class="toc">
  <ul>
    <li><a href="#chapter1">第一章 概述</a>
      <ul>
        <li><a href="#section1-1">1.1 背景</a></li>
        <li><a href="#section1-2">1.2 目标</a></li>
      </ul>
    </li>
  </ul>
</nav>
```

### 3. 目录样式

```css
.toc {
  background: #f9f9f9;
  border: 1px solid #e5e5e5;
  padding: 1.5em;
  border-radius: 6px;
  margin-bottom: 2em;
}

.toc ul {
  list-style: none;
  padding-left: 0;
}

.toc li {
  margin: 0.5em 0;
}

.toc a {
  color: #2563eb;
  text-decoration: none;
}

.toc a:hover {
  text-decoration: underline;
}

/* 多级缩进 */
.toc ul ul {
  padding-left: 1.5em;
}
```

### 4. 目录配置

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| max_depth | 最大目录层级 | 3 |
| numbered | 是否编号 | true |
| anchor | 是否生成锚点 | true |
| style | 目录样式 | 'default' |

## 使用示例

### Python 脚本

```python
def create_toc(markdown_file, output_file):
    """为 Markdown 文件生成目录"""
    with open(markdown_file, 'r') as f:
        content = f.read()
    
    toc = generate_toc(content)
    toc_md = format_toc_markdown(toc)
    
    # 在第一个标题后插入目录
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('#'):
            lines.insert(i + 1, '\n' + toc_md + '\n')
            break
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(lines))
```

## 目录生成原则

1. **层级清晰** - 不超过 3-4 级
2. **编号规范** - 使用 1.1.1 格式
3. **链接有效** - 锚点与标题对应
4. **位置合理** - 放在文档开头