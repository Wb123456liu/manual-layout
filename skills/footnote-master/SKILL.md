---
name: footnote-master
description: 脚注管理技能，用于文档中脚注和尾注的管理。支持脚注添加、编号、引用、样式设置、脚注区排版等。当用户需要：(1) 添加脚注 (2) 管理参考文献 (3) 设置脚注样式 (4) 转换脚注/尾注时使用此技能。
---

# Footnote Master - 脚注管理

## 核心功能

### 1. 脚注添加

#### Markdown 格式

```markdown
正文内容[^1]，需要添加脚注的地方。

[^1]: 这是脚注内容。
```

#### HTML 格式

```html
<p>正文内容<sup><a href="#fn1" id="ref1">[1]</a></sup></p>

<div class="footnotes">
  <p id="fn1">[1] 脚注内容。<a href="#ref1">↩</a></p>
</div>
```

### 2. 脚注编号

```python
class FootnoteManager:
    def __init__(self):
        self.notes = []
        self.counter = 0
    
    def add(self, content, source=None):
        """添加脚注"""
        self.counter += 1
        note = {
            'number': self.counter,
            'content': content,
            'source': source
        }
        self.notes.append(note)
        return self.counter
    
    def render(self):
        """渲染脚注区"""
        output = "\n---\n\n## 脚注\n\n"
        for note in self.notes:
            output += f"[{note['number']}] {note['content']}\n\n"
        return output
```

### 3. 脚注样式

```css
/* 脚注引用标记 */
.footnote-ref {
  font-size: 0.75em;
  vertical-align: super;
  color: #2563eb;
  text-decoration: none;
}

.footnote-ref:hover {
  text-decoration: underline;
}

/* 脚注区 */
.footnotes {
  margin-top: 2em;
  padding-top: 1em;
  border-top: 1px solid #e5e5e5;
  font-size: 10pt;
}

/* 脚注条目 */
.footnotes p {
  margin: 0.5em 0;
  text-indent: -2em;
  padding-left: 2em;
}

/* 返回链接 */
.footnote-backref {
  font-size: 0.9em;
  color: #666;
}
```

### 4. 参考文献格式

```markdown
## 参考文献

[1] 作者. 书名[M]. 出版地: 出版社, 年份.

[2] 作者. 论文题目[J]. 期刊名, 年份, 卷(期): 页码.

[3] 作者. 文章标题[EB/OL]. 网址, 访问日期.
```

### 5. 脚注/尾注转换

```python
def convert_to_endnotes(document):
    """将脚注转换为尾注"""
    # 收集所有脚注
    footnotes = extract_footnotes(document)
    
    # 移除原脚注位置
    document = remove_inline_footnotes(document)
    
    # 在文档末尾添加尾注区
    document += "\n\n---\n\n## 尾注\n\n"
    for i, note in enumerate(footnotes, 1):
        document += f"[{i}] {note}\n\n"
    
    return document
```

## 使用示例

### 完整脚注流程

```markdown
# 文档标题

正文内容，这里需要一个脚注[^1]。

另一个地方需要脚注[^2]。

---

## 脚注

[^1]: 第一个脚注的详细内容。
[^2]: 第二个脚注的详细内容，可以很长。
```

## 脚注管理原则

1. **编号连续** - 从 1 开始连续编号
2. **内容简洁** - 脚注内容尽量简短
3. **位置合理** - 脚注区放在文档末尾
4. **双向链接** - 正文与脚注可互相跳转