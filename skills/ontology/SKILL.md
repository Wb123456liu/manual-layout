---
name: ontology
description: 本体论技能，用于知识本体建模和管理。支持概念定义、关系建模、层次结构、推理查询等。当用户需要：(1) 构建知识本体 (2) 定义概念关系 (3) 层次分类 (4) 知识推理时使用此技能。
---

# Ontology - 本体论

## 核心功能

### 1. 概念定义

```python
class Concept:
    def __init__(self, name, attributes=None, parent=None):
        self.name = name
        self.attributes = attributes or {}
        self.parent = parent
        self.children = []
        self.relations = []
    
    def add_attribute(self, key, value, required=False):
        """添加属性"""
        self.attributes[key] = {
            'value': value,
            'required': required
        }
    
    def add_child(self, child):
        """添加子概念"""
        self.children.append(child)
        child.parent = self
    
    def is_instance_of(self, other):
        """判断是否是某概念的实例"""
        current = self
        while current:
            if current.name == other.name:
                return True
            current = current.parent
        return False
```

### 2. 关系建模

```python
class Relation:
    def __init__(self, name, source, target, properties=None):
        self.name = name
        self.source = source
        self.target = target
        self.properties = properties or {}

class Ontology:
    def __init__(self):
        self.concepts = {}
        self.relations = []
    
    def add_concept(self, concept):
        """添加概念"""
        self.concepts[concept.name] = concept
    
    def add_relation(self, relation_name, source_name, target_name, **props):
        """添加关系"""
        source = self.concepts.get(source_name)
        target = self.concepts.get(target_name)
        
        if source and target:
            relation = Relation(relation_name, source, target, props)
            self.relations.append(relation)
            source.relations.append(relation)
    
    def get_relations(self, concept_name, relation_name=None):
        """获取概念的关系"""
        concept = self.concepts.get(concept_name)
        if not concept:
            return []
        
        if relation_name:
            return [r for r in concept.relations if r.name == relation_name]
        return concept.relations
```

### 3. 层次结构

```python
def build_hierarchy(ontology):
    """构建层次结构树"""
    def build_node(concept):
        return {
            'name': concept.name,
            'attributes': concept.attributes,
            'children': [build_node(c) for c in concept.children]
        }
    
    roots = [c for c in ontology.concepts.values() if c.parent is None]
    return [build_node(r) for r in roots]

def get_ancestors(concept):
    """获取所有祖先概念"""
    ancestors = []
    current = concept.parent
    while current:
        ancestors.append(current)
        current = current.parent
    return ancestors

def get_descendants(concept):
    """获取所有后代概念"""
    descendants = []
    for child in concept.children:
        descendants.append(child)
        descendants.extend(get_descendants(child))
    return descendants
```

### 4. 推理查询

```python
def infer_properties(ontology, concept_name):
    """推理概念属性（继承父概念属性）"""
    concept = ontology.concepts.get(concept_name)
    if not concept:
        return {}
    
    properties = {}
    
    # 从祖先继承属性
    for ancestor in reversed(get_ancestors(concept)):
        for key, attr in ancestor.attributes.items():
            if key not in properties:
                properties[key] = attr
    
    # 自身属性覆盖
    for key, attr in concept.attributes.items():
        properties[key] = attr
    
    return properties

def find_by_attribute(ontology, attr_name, attr_value):
    """按属性查找概念"""
    results = []
    for concept in ontology.concepts.values():
        props = infer_properties(ontology, concept.name)
        if props.get(attr_name, {}).get('value') == attr_value:
            results.append(concept)
    return results
```

## 使用示例

```python
# 创建本体
onto = Ontology()

# 定义概念
animal = Concept('Animal', {'living': True})
mammal = Concept('Mammal', {'warm_blooded': True})
dog = Concept('Dog', {'barks': True})

# 建立层次
animal.add_child(mammal)
mammal.add_child(dog)

# 添加到本体
onto.add_concept(animal)
onto.add_concept(mammal)
onto.add_concept(dog)

# 添加关系
onto.add_relation('eats', 'Dog', 'Animal')

# 推理属性
props = infer_properties(onto, 'Dog')
print(props)  # 包含 living, warm_blooded, barks
```

## 本体建模原则

1. **明确概念边界** - 每个概念有清晰定义
2. **合理层次深度** - 不超过 5-7 层
3. **属性继承** - 子概念继承父概念属性
4. **关系明确** - 关系有明确的语义