---
name: browser-use
description: 浏览器使用技能，提供高级浏览器自动化能力。支持智能元素定位、多标签页管理、Cookie 管理、文件下载等。当用户需要：(1) 智能操作网页 (2) 管理多标签页 (3) 处理登录状态 (4) 下载文件时使用此技能。
---

# Browser Use - 浏览器使用

## 核心功能

### 1. 智能元素定位

```python
def find_by_text(page, text):
    """通过文本定位元素"""
    return page.get_by_text(text)

def find_by_role(page, role, name=None):
    """通过角色定位元素"""
    return page.get_by_role(role, name=name)

def find_by_label(page, label):
    """通过标签定位表单元素"""
    return page.get_by_label(label)
```

### 2. 多标签页管理

```python
def open_new_tab(context, url):
    """打开新标签页"""
    page = context.new_page()
    page.goto(url)
    return page

def switch_tab(context, index):
    """切换标签页"""
    pages = context.pages
    return pages[index]

def close_tab(page):
    """关闭标签页"""
    page.close()
```

### 3. Cookie 管理

```python
def save_cookies(context, path):
    """保存 Cookie"""
    cookies = context.cookies()
    with open(path, 'w') as f:
        json.dump(cookies, f)

def load_cookies(context, path):
    """加载 Cookie"""
    with open(path, 'r') as f:
        cookies = json.load(f)
    context.add_cookies(cookies)
```

### 4. 文件下载

```python
def download_file(page, trigger_selector, save_path):
    """下载文件"""
    with page.expect_download() as download_info:
        page.click(trigger_selector)
    download = download_info.value
    download.save_as(save_path)
```

## 使用示例

```python
# 智能搜索示例
page.get_by_placeholder("搜索").fill("关键词")
page.get_by_role("button", name="搜索").click()
results = page.get_by_role("listitem").all()
```

## 最佳实践

1. 优先使用语义化定位器
2. 使用上下文管理器处理下载
3. 保存登录状态避免重复登录
4. 处理页面加载状态