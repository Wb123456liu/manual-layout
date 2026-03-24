---
name: manual-translation
description: 手册翻译技能，专门用于技术手册、产品说明书的翻译。支持术语管理、格式保留、双语对照、翻译记忆等。当用户需要：(1) 翻译产品手册 (2) 处理技术文档翻译 (3) 管理翻译术语 (4) 生成双语版本时使用此技能。
---

# Manual Translation - 手册翻译

## 核心功能

### 1. 翻译工作流

```python
class ManualTranslator:
    def __init__(self, terminology=None):
        self.terminology = terminology or {}
        self.translation_memory = {}
    
    def translate(self, text, source_lang, target_lang):
        """翻译文本"""
        # 1. 检查翻译记忆
        if text in self.translation_memory:
            return self.translation_memory[text]
        
        # 2. 预处理：标记术语
        marked_text = self._mark_terms(text)
        
        # 3. 调用翻译 API
        translated = self._call_api(marked_text, source_lang, target_lang)
        
        # 4. 后处理：恢复术语
        final = self._restore_terms(translated)
        
        # 5. 存入翻译记忆
        self.translation_memory[text] = final
        
        return final
```

### 2. 术语管理

```python
import json

class TerminologyManager:
    def __init__(self, term_file=None):
        self.terms = {}
        if term_file:
            self.load(term_file)
    
    def load(self, filepath):
        """加载术语库"""
        with open(filepath, 'r', encoding='utf-8') as f:
            self.terms = json.load(f)
    
    def save(self, filepath):
        """保存术语库"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.terms, f, ensure_ascii=False, indent=2)
    
    def add_term(self, source, target, category=None):
        """添加术语"""
        self.terms[source] = {
            'target': target,
            'category': category
        }
    
    def lookup(self, word):
        """查询术语"""
        return self.terms.get(word)
```

### 3. 格式保留

```python
import re

def translate_with_format(text, translator):
    """保留格式的翻译"""
    # 提取格式标记
    patterns = [
        (r'\*\*(.+?)\*\*', 'bold'),      # **粗体**
        (r'\*(.+?)\*', 'italic'),         # *斜体*
        (r'`(.+?)`', 'code'),             # `代码`
        (r'\[(.+?)\]\((.+?)\)', 'link'),  # [链接](url)
    ]
    
    # 保护格式标记
    protected = text
    placeholders = {}
    
    for pattern, ptype in patterns:
        matches = re.finditer(pattern, text)
        for i, match in enumerate(matches):
            placeholder = f"__{ptype}_{i}__"
            placeholders[placeholder] = match.group(0)
            protected = protected.replace(match.group(0), placeholder)
    
    # 翻译
    translated = translator.translate(protected)
    
    # 恢复格式标记
    for placeholder, original in placeholders.items():
        translated = translated.replace(placeholder, original)
    
    return translated
```

### 4. 双语对照输出

```python
def generate_bilingual(source_text, translated_text, output_format='parallel'):
    """生成双语对照"""
    if output_format == 'parallel':
        return f"""
<table>
<tr><td><b>原文：</b></td><td>{source_text}</td></tr>
<tr><td><b>译文：</b></td><td>{translated_text}</td></tr>
</table>
"""
    elif output_format == 'interleaved':
        return f"""
**原文：** {source_text}

**译文：** {translated_text}

---
"""
```

## 术语库示例

```json
{
  "产品": {
    "target": "Product",
    "category": "general"
  },
  "用户手册": {
    "target": "User Manual",
    "category": "document"
  },
  "安全警告": {
    "target": "Safety Warning",
    "category": "safety"
  }
}
```

## 翻译原则

1. **术语一致** - 同一术语翻译统一
2. **格式保留** - 不破坏原文格式
3. **风格统一** - 保持技术文档风格
4. **本地化** - 适应目标语言习惯