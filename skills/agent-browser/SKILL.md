---
name: agent-browser
description: 浏览器代理技能，用于自动化浏览器操作。支持网页导航、元素交互、表单填写、截图等。当用户需要：(1) 自动打开网页 (2) 点击按钮或链接 (3) 填写表单 (4) 截取网页截图 (5) 抓取网页内容时使用此技能。
---

# Agent Browser - 浏览器代理

## 核心功能

### 1. 网页导航

```python
from playwright.sync_api import sync_playwright

def navigate(url):
    """打开网页"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        return page
```

### 2. 元素交互

```python
def click_element(page, selector):
    """点击元素"""
    page.click(selector)

def fill_input(page, selector, value):
    """填写输入框"""
    page.fill(selector, value)

def select_option(page, selector, value):
    """选择下拉选项"""
    page.select_option(selector, value)
```

### 3. 截图

```python
def screenshot(page, path="screenshot.png"):
    """截取页面截图"""
    page.screenshot(path=path)
```

### 4. 内容抓取

```python
def get_text(page, selector):
    """获取元素文本"""
    return page.locator(selector).text_content()

def get_all_links(page):
    """获取所有链接"""
    return page.eval_on_selector_all('a', 'els => els.map(e => e.href)')
```

## 使用示例

```python
# 自动登录示例
page = navigate("https://example.com/login")
fill_input(page, "#username", "user@example.com")
fill_input(page, "#password", "password123")
click_element(page, "#login-button")
screenshot(page, "after_login.png")
```

## 最佳实践

1. 使用显式等待而非固定延迟
2. 处理弹窗和对话框
3. 捕获异常和错误
4. 关闭浏览器释放资源