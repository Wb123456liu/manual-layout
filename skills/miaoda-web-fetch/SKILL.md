---
name: miaoda-web-fetch
description: 妙答网页抓取技能，用于抓取和解析网页内容。支持内容提取、结构化解析、反爬处理、批量抓取等。当用户需要：(1) 抓取网页内容 (2) 提取页面数据 (3) 解析 HTML (4) 批量采集时使用此技能。
---

# Miaoda Web Fetch - 妙答网页抓取

## 核心功能

### 1. 基础抓取

```python
import requests
from bs4 import BeautifulSoup

def fetch(url, headers=None, timeout=10):
    """抓取网页"""
    default_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    headers = headers or default_headers
    
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    
    return response.text

def fetch_json(url, headers=None):
    """抓取 JSON API"""
    response = requests.get(url, headers=headers)
    return response.json()
```

### 2. 内容提取

```python
def extract_text(html, selector=None):
    """提取文本内容"""
    soup = BeautifulSoup(html, 'html.parser')
    
    if selector:
        elements = soup.select(selector)
        return [e.get_text(strip=True) for e in elements]
    
    # 提取主要内容
    # 移除脚本和样式
    for tag in soup(['script', 'style', 'nav', 'footer']):
        tag.decompose()
    
    return soup.get_text(strip=True)

def extract_links(html, base_url=None):
    """提取所有链接"""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    
    for a in soup.find_all('a', href=True):
        href = a['href']
        if base_url:
            from urllib.parse import urljoin
            href = urljoin(base_url, href)
        links.append({
            'url': href,
            'text': a.get_text(strip=True)
        })
    
    return links

def extract_images(html, base_url=None):
    """提取所有图片"""
    soup = BeautifulSoup(html, 'html.parser')
    images = []
    
    for img in soup.find_all('img', src=True):
        src = img['src']
        if base_url:
            from urllib.parse import urljoin
            src = urljoin(base_url, src)
        images.append({
            'url': src,
            'alt': img.get('alt', '')
        })
    
    return images
```

### 3. 结构化解析

```python
def parse_article(html):
    """解析文章结构"""
    soup = BeautifulSoup(html, 'html.parser')
    
    # 提取标题
    title = soup.find('h1')
    title_text = title.get_text(strip=True) if title else ''
    
    # 提取正文
    # 尝试常见的文章容器
    article = (soup.find('article') or 
               soup.find('div', class_='content') or
               soup.find('div', class_='article'))
    
    content = ''
    if article:
        content = article.get_text(strip=True)
    
    # 提取元信息
    meta = {}
    for tag in soup.find_all('meta'):
        name = tag.get('name') or tag.get('property')
        if name:
            meta[name] = tag.get('content', '')
    
    return {
        'title': title_text,
        'content': content,
        'meta': meta
    }
```

### 4. 反爬处理

```python
import time
import random

class SmartFetcher:
    def __init__(self, delay_range=(1, 3)):
        self.delay_range = delay_range
        self.session = requests.Session()
    
    def fetch(self, url, retries=3):
        """智能抓取（带重试和延迟）"""
        for attempt in range(retries):
            try:
                # 随机延迟
                time.sleep(random.uniform(*self.delay_range))
                
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
                return response.text
                
            except requests.exceptions.RequestException as e:
                if attempt == retries - 1:
                    raise
                time.sleep(2 ** attempt)  # 指数退避
```

### 5. 批量抓取

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def batch_fetch(urls, max_workers=5, callback=None):
    """批量抓取"""
    results = {}
    
    def fetch_one(url):
        try:
            content = fetch(url)
            return url, content, None
        except Exception as e:
            return url, None, str(e)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_one, url): url for url in urls}
        
        for future in as_completed(futures):
            url, content, error = future.result()
            results[url] = {
                'content': content,
                'error': error
            }
            if callback:
                callback(url, content, error)
    
    return results
```

## 使用示例

```python
# 抓取网页
html = fetch("https://example.com")

# 提取文本
text = extract_text(html)

# 解析文章
article = parse_article(html)
print(f"标题: {article['title']}")

# 批量抓取
results = batch_fetch(["url1", "url2", "url3"])
```

## 注意事项

1. 遵守 robots.txt
2. 添加适当延迟
3. 设置 User-Agent
4. 处理异常和重试