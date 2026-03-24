---
name: miaoda-web-search
description: 妙答网页搜索技能，用于智能网页搜索。支持多引擎搜索、结果过滤、内容摘要、相关推荐等。当用户需要：(1) 搜索网页信息 (2) 查找资料 (3) 获取搜索结果摘要 (4) 发现相关内容时使用此技能。
---

# Miaoda Web Search - 妙答网页搜索

## 核心功能

### 1. 多引擎搜索

```python
import requests

def search_google(query, num_results=10):
    """Google 搜索"""
    # 使用 Google Custom Search API
    pass

def search_bing(query, num_results=10):
    """Bing 搜索"""
    # 使用 Bing Search API
    pass

def search_baidu(query, num_results=10):
    """百度搜索"""
    # 使用百度搜索 API
    pass

def multi_search(query, engines=['google', 'bing'], num_results=10):
    """多引擎搜索"""
    results = []
    for engine in engines:
        if engine == 'google':
            results.extend(search_google(query, num_results))
        elif engine == 'bing':
            results.extend(search_bing(query, num_results))
        elif engine == 'baidu':
            results.extend(search_baidu(query, num_results))
    
    # 去重并排序
    return deduplicate_and_rank(results)
```

### 2. 结果过滤

```python
def filter_by_date(results, start_date, end_date):
    """按日期过滤"""
    return [
        r for r in results
        if start_date <= r.get('date', '') <= end_date
    ]

def filter_by_domain(results, allowed_domains):
    """按域名过滤"""
    from urllib.parse import urlparse
    return [
        r for r in results
        if urlparse(r['url']).netloc in allowed_domains
    ]

def filter_by_keywords(results, include_keywords, exclude_keywords):
    """按关键词过滤"""
    filtered = []
    for r in results:
        text = (r.get('title', '') + ' ' + r.get('snippet', '')).lower()
        
        # 必须包含的关键词
        if include_keywords:
            if not any(kw.lower() in text for kw in include_keywords):
                continue
        
        # 排除的关键词
        if exclude_keywords:
            if any(kw.lower() in text for kw in exclude_keywords):
                continue
        
        filtered.append(r)
    
    return filtered
```

### 3. 内容摘要

```python
def summarize_results(results, max_length=500):
    """生成搜索结果摘要"""
    summaries = []
    
    for r in results[:5]:  # 只处理前 5 个结果
        summary = {
            'title': r.get('title', ''),
            'url': r.get('url', ''),
            'snippet': r.get('snippet', '')[:200],
            'key_points': extract_key_points(r.get('content', ''))
        }
        summaries.append(summary)
    
    return summaries

def extract_key_points(content):
    """提取关键点"""
    # 使用 NLP 提取关键信息
    pass
```

### 4. 相关推荐

```python
def get_related_queries(query, results):
    """获取相关搜索建议"""
    # 从搜索结果中提取相关主题
    related = []
    
    for r in results:
        title = r.get('title', '')
        # 提取标题中的关键词
        keywords = extract_keywords(title)
        related.extend(keywords)
    
    # 去重并排序
    from collections import Counter
    return [q for q, _ in Counter(related).most_common(5)]
```

### 5. 智能搜索

```python
def smart_search(query, context=None):
    """智能搜索（结合上下文）"""
    # 1. 理解查询意图
    intent = analyze_query_intent(query)
    
    # 2. 扩展查询词
    expanded_query = expand_query(query, intent)
    
    # 3. 执行搜索
    results = multi_search(expanded_query)
    
    # 4. 根据意图过滤
    filtered = filter_by_intent(results, intent)
    
    # 5. 生成摘要
    summary = summarize_results(filtered)
    
    return {
        'query': query,
        'expanded_query': expanded_query,
        'intent': intent,
        'results': filtered,
        'summary': summary
    }
```

## 使用示例

```python
# 基础搜索
results = multi_search("Python 教程", engines=['google', 'bing'])

# 过滤结果
filtered = filter_by_date(results, '2024-01-01', '2024-12-31')
filtered = filter_by_keywords(filtered, ['入门'], ['付费'])

# 生成摘要
summary = summarize_results(filtered)
for s in summary:
    print(f"标题: {s['title']}")
    print(f"摘要: {s['snippet']}")
```

## 搜索技巧

1. 使用精确匹配 `"关键词"`
2. 排除关键词 `-排除词`
3. 指定站点 `site:example.com`
4. 指定文件类型 `filetype:pdf`