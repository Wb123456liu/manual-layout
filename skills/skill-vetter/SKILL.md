---
name: skill-vetter
description: 技能审查技能，用于评估和验证技能质量。支持代码检查、安全审计、性能评估、最佳实践检查等。当用户需要：(1) 审查技能质量 (2) 检查安全性 (3) 评估性能 (4) 验证最佳实践时使用此技能。
---

# Skill Vetter - 技能审查

## 核心功能

### 1. 代码检查

```python
import ast
import os

def check_skill_structure(skill_path):
    """检查技能结构"""
    issues = []
    
    # 检查必要文件
    skill_md = os.path.join(skill_path, 'SKILL.md')
    if not os.path.exists(skill_md):
        issues.append({
            'level': 'error',
            'message': '缺少 SKILL.md 文件'
        })
    else:
        # 检查 SKILL.md 内容
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查 frontmatter
        if not content.startswith('---'):
            issues.append({
                'level': 'error',
                'message': 'SKILL.md 缺少 YAML frontmatter'
            })
        
        # 检查必要字段
        if 'name:' not in content:
            issues.append({
                'level': 'error',
                'message': 'SKILL.md 缺少 name 字段'
            })
        
        if 'description:' not in content:
            issues.append({
                'level': 'error',
                'message': 'SKILL.md 缺少 description 字段'
            })
    
    return issues
```

### 2. 安全审计

```python
SECURITY_PATTERNS = [
    ('eval(', '使用 eval() 可能存在代码注入风险'),
    ('exec(', '使用 exec() 可能存在代码注入风险'),
    ('subprocess.call(', '使用 subprocess 可能存在命令注入风险'),
    ('os.system(', '使用 os.system 可能存在命令注入风险'),
    ('pickle.loads(', '使用 pickle 可能存在反序列化风险'),
    ('__import__(', '动态导入可能存在风险'),
]

def security_audit(skill_path):
    """安全审计"""
    issues = []
    
    for root, dirs, files in os.walk(skill_path):
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for pattern, message in SECURITY_PATTERNS:
                    if pattern in content:
                        issues.append({
                            'level': 'warning',
                            'file': filepath,
                            'message': message
                        })
    
    return issues
```

### 3. 性能评估

```python
def evaluate_performance(skill_path):
    """评估技能性能"""
    metrics = {}
    
    # 文件大小
    total_size = 0
    file_count = 0
    for root, dirs, files in os.walk(skill_path):
        for file in files:
            filepath = os.path.join(root, file)
            total_size += os.path.getsize(filepath)
            file_count += 1
    
    metrics['total_size'] = total_size
    metrics['file_count'] = file_count
    metrics['avg_size'] = total_size / file_count if file_count else 0
    
    # SKILL.md 大小（影响加载时间）
    skill_md = os.path.join(skill_path, 'SKILL.md')
    if os.path.exists(skill_md):
        metrics['skill_md_size'] = os.path.getsize(skill_md)
        metrics['skill_md_lines'] = sum(1 for _ in open(skill_md))
    
    return metrics
```

### 4. 最佳实践检查

```python
BEST_PRACTICES = [
    {
        'check': lambda c: '## ' in c,
        'message': '建议使用二级标题组织内容'
    },
    {
        'check': lambda c: '```' in c,
        'message': '建议包含代码示例'
    },
    {
        'check': lambda c: len(c) < 10000,
        'message': 'SKILL.md 建议控制在 10000 字符以内'
    },
]

def check_best_practices(skill_path):
    """检查最佳实践"""
    results = []
    
    skill_md = os.path.join(skill_path, 'SKILL.md')
    if os.path.exists(skill_md):
        with open(skill_md, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for practice in BEST_PRACTICES:
            if practice['check'](content):
                results.append({
                    'status': 'pass',
                    'message': practice['message']
                })
            else:
                results.append({
                    'status': 'fail',
                    'message': practice['message']
                })
    
    return results
```

### 5. 综合评估

```python
def vet_skill(skill_path):
    """综合评估技能"""
    report = {
        'path': skill_path,
        'structure': check_skill_structure(skill_path),
        'security': security_audit(skill_path),
        'performance': evaluate_performance(skill_path),
        'best_practices': check_best_practices(skill_path)
    }
    
    # 计算总分
    score = 100
    score -= len([i for i in report['structure'] if i['level'] == 'error']) * 20
    score -= len([i for i in report['security'] if i['level'] == 'warning']) * 10
    score -= len([i for i in report['best_practices'] if i['status'] == 'fail']) * 5
    
    report['score'] = max(0, score)
    
    return report
```

## 使用示例

```python
# 审查技能
report = vet_skill('./skills/my-skill')

print(f"总分: {report['score']}/100")
print(f"结构问题: {len(report['structure'])}")
print(f"安全问题: {len(report['security'])}")
```

## 审查标准

| 类别 | 权重 |
|------|------|
| 结构完整性 | 20分/项 |
| 安全问题 | 10分/项 |
| 最佳实践 | 5分/项 |