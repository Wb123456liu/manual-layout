---
name: find-skills
description: 查找技能技能，用于搜索和发现可用的技能。支持关键词搜索、分类浏览、功能匹配、推荐等。当用户需要：(1) 查找特定功能技能 (2) 浏览技能分类 (3) 发现新技能 (4) 获取技能推荐时使用此技能。
---

# Find Skills - 查找技能

## 核心功能

### 1. 关键词搜索

```python
def search_skills(query, skills_dir):
    """按关键词搜索技能"""
    import os
    import re
    
    results = []
    query_lower = query.lower()
    
    for skill_name in os.listdir(skills_dir):
        skill_path = os.path.join(skills_dir, skill_name, 'SKILL.md')
        if os.path.exists(skill_path):
            with open(skill_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 搜索名称和描述
            if query_lower in skill_name.lower() or query_lower in content.lower():
                # 提取描述
                desc_match = re.search(r'description:\s*(.+?)(?:\n|$)', content)
                description = desc_match.group(1) if desc_match else ''
                
                results.append({
                    'name': skill_name,
                    'description': description[:200],
                    'relevance': content.lower().count(query_lower)
                })
    
    return sorted(results, key=lambda x: x['relevance'], reverse=True)
```

### 2. 分类浏览

```python
SKILL_CATEGORIES = {
    'browser': ['agent-browser', 'browser-use', 'desktop-control'],
    'document': ['word-processor', 'pdf-editor', 'pdf-generator', 'html-to-pdf'],
    'typesetting': ['typeset-pro', 'multi-column', 'style-kit', 'auto-toc'],
    'image': ['image', 'imagemagick', 'smart-image', 'image-extract'],
    'data': ['chart-generator'],
    'development': ['typescript-pro', 'ecto-migrator'],
    'ai': ['miaoda-image-understanding', 'miaoda-text-gen-image'],
    'search': ['miaoda-web-search', 'miaoda-web-fetch'],
    'notes': ['lecture-notes-master'],
    'voice': ['miaoda-speech-to-text'],
    'design': ['ui-ux-pro-max']
}

def list_by_category(category=None):
    """按分类列出技能"""
    if category:
        return SKILL_CATEGORIES.get(category, [])
    return SKILL_CATEGORIES
```

### 3. 功能匹配

```python
def find_by_function(required_function, skills_metadata):
    """根据功能需求匹配技能"""
    matches = []
    
    function_keywords = {
        'edit': ['editor', 'edit', 'modify'],
        'convert': ['convert', 'transform', 'generator'],
        'analyze': ['analyze', 'understanding', 'detect'],
        'generate': ['generate', 'create', 'builder'],
        'search': ['search', 'find', 'query'],
        'format': ['format', 'style', 'typeset']
    }
    
    keywords = function_keywords.get(required_function, [required_function])
    
    for skill, meta in skills_metadata.items():
        desc_lower = meta.get('description', '').lower()
        for kw in keywords:
            if kw in desc_lower:
                matches.append(skill)
                break
    
    return matches
```

### 4. 技能推荐

```python
def recommend_skills(user_history, all_skills):
    """基于使用历史推荐技能"""
    from collections import Counter
    
    # 分析常用类别
    categories = [get_category(skill) for skill in user_history]
    top_categories = Counter(categories).most_common(3)
    
    recommendations = []
    for category, _ in top_categories:
        # 推荐该类别下未使用的技能
        category_skills = SKILL_CATEGORIES.get(category, [])
        for skill in category_skills:
            if skill not in user_history:
                recommendations.append(skill)
    
    return recommendations[:5]
```

## 使用示例

```python
# 搜索技能
results = search_skills("pdf", "./skills")
for r in results:
    print(f"{r['name']}: {r['description']}")

# 按分类浏览
doc_skills = list_by_category('document')
print(f"文档处理技能: {doc_skills}")

# 功能匹配
edit_skills = find_by_function('edit', skills_metadata)
print(f"编辑类技能: {edit_skills}")
```

## CLI 命令

```bash
# 搜索技能
clawhub search "关键词"

# 列出所有技能
clawhub list

# 查看技能详情
clawhub info skill-name
```