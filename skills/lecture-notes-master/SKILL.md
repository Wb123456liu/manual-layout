---
name: lecture-notes-master
description: 讲座笔记大师技能，用于管理和整理讲座、课程笔记。支持笔记记录、结构整理、知识点提取、复习计划生成等。当用户需要：(1) 记录讲座笔记 (2) 整理课程内容 (3) 提取知识点 (4) 生成复习计划时使用此技能。
---

# Lecture Notes Master - 讲座笔记大师

## 核心功能

### 1. 笔记结构

```markdown
# [课程/讲座名称]

**日期：** YYYY-MM-DD  
**讲师：** XXX  
**时长：** XX 分钟

---

## 概要

[一句话总结讲座核心内容]

---

## 主要内容

### 1. [主题一]

#### 核心观点
- 观点 1
- 观点 2

#### 详细笔记
[详细内容]

#### 案例/例子
[具体案例]

---

### 2. [主题二]

...

---

## 关键概念

| 概念 | 定义 | 备注 |
|------|------|------|
| XXX | ... | ... |

---

## 重要公式/代码

```
[公式或代码]
```

---

## 疑问待解

- [ ] 问题 1
- [ ] 问题 2

---

## 行动项

- [ ] 复习相关章节
- [ ] 完成作业
- [ ] 查阅扩展资料

---

## 参考资料

1. [资料名称](链接)
2. ...
```

### 2. 知识点提取

```python
import re

def extract_key_points(notes):
    """从笔记中提取知识点"""
    points = []
    
    # 提取标题下的要点
    pattern = r'###\s+(.+?)\n\n(.+?)(?=\n###|\n---|\Z)'
    matches = re.findall(pattern, notes, re.DOTALL)
    
    for title, content in matches:
        points.append({
            'topic': title.strip(),
            'content': content.strip()
        })
    
    return points

def extract_questions(notes):
    """提取疑问"""
    pattern = r'-\s*\[\s*\]\s*(.+)'
    return re.findall(pattern, notes)
```

### 3. 复习计划生成

```python
from datetime import datetime, timedelta

def generate_review_plan(notes_date, difficulty='medium'):
    """生成复习计划（艾宾浩斯遗忘曲线）"""
    intervals = {
        'easy': [1, 3, 7, 14, 30],
        'medium': [1, 2, 4, 7, 15, 30],
        'hard': [1, 1, 2, 4, 7, 15, 30]
    }
    
    plan = []
    base_date = datetime.strptime(notes_date, '%Y-%m-%d')
    
    for days in intervals.get(difficulty, intervals['medium']):
        review_date = base_date + timedelta(days=days)
        plan.append({
            'date': review_date.strftime('%Y-%m-%d'),
            'day': days
        })
    
    return plan
```

### 4. 笔记合并

```python
def merge_notes(notes_list, output_path):
    """合并多个笔记"""
    merged = {
        'title': '综合笔记',
        'topics': {},
        'questions': [],
        'references': []
    }
    
    for notes in notes_list:
        # 提取主题
        points = extract_key_points(notes)
        for point in points:
            topic = point['topic']
            if topic not in merged['topics']:
                merged['topics'][topic] = []
            merged['topics'][topic].append(point['content'])
        
        # 提取疑问
        merged['questions'].extend(extract_questions(notes))
    
    return merged
```

### 5. 导出格式

```python
def export_to_markdown(notes, output_path):
    """导出为 Markdown"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(notes)

def export_to_anki(notes, output_path):
    """导出为 Anki 卡片"""
    cards = []
    points = extract_key_points(notes)
    
    for point in points:
        cards.append({
            'front': point['topic'],
            'back': point['content']
        })
    
    # 写入 CSV 格式
    import csv
    with open(output_path, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for card in cards:
            writer.writerow([card['front'], card['back']])
```

## 使用示例

```python
# 生成复习计划
plan = generate_review_plan("2024-01-15", difficulty='hard')
for item in plan:
    print(f"第 {item['day']} 天复习：{item['date']}")

# 提取知识点
points = extract_key_points(lecture_notes)
for p in points:
    print(f"主题: {p['topic']}")
```

## 笔记原则

1. **结构清晰** - 使用统一的模板
2. **重点突出** - 标记核心概念
3. **及时复习** - 按遗忘曲线复习
4. **主动思考** - 记录疑问和见解