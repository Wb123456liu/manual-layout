---
name: desktop-control
description: 桌面控制技能，用于自动化桌面操作。支持窗口管理、鼠标键盘控制、应用程序操作等。当用户需要：(1) 控制桌面应用 (2) 自动化鼠标键盘操作 (3) 管理窗口 (4) 截取屏幕时使用此技能。
---

# Desktop Control - 桌面控制

## 核心功能

### 1. 鼠标操作

```python
import pyautogui

def move_to(x, y):
    """移动鼠标到指定位置"""
    pyautogui.moveTo(x, y)

def click(x=None, y=None, button='left'):
    """点击鼠标"""
    pyautogui.click(x, y, button=button)

def double_click(x=None, y=None):
    """双击"""
    pyautogui.doubleClick(x, y)

def drag_to(start_x, start_y, end_x, end_y):
    """拖拽"""
    pyautogui.moveTo(start_x, start_y)
    pyautogui.drag(end_x - start_x, end_y - start_y)
```

### 2. 键盘操作

```python
def type_text(text, interval=0.1):
    """输入文字"""
    pyautogui.typewrite(text, interval=interval)

def press_key(key):
    """按键"""
    pyautogui.press(key)

def hotkey(*keys):
    """组合键"""
    pyautogui.hotkey(*keys)
```

### 3. 屏幕操作

```python
def screenshot(region=None):
    """截屏"""
    return pyautogui.screenshot(region=region)

def locate_on_screen(image_path):
    """在屏幕上定位图片"""
    return pyautogui.locateOnScreen(image_path)

def get_screen_size():
    """获取屏幕尺寸"""
    return pyautogui.size()
```

### 4. 窗口管理

```python
import pygetwindow as gw

def get_active_window():
    """获取活动窗口"""
    return gw.getActiveWindow()

def get_windows_by_title(title):
    """通过标题获取窗口"""
    return gw.getWindowsWithTitle(title)

def move_window(window, x, y):
    """移动窗口"""
    window.moveTo(x, y)
```

## 使用示例

```python
# 打开应用并操作
hotkey('win', 'r')  # 打开运行对话框
type_text('notepad')
press_key('enter')
type_text('Hello World!')
hotkey('ctrl', 's')  # 保存
```

## 最佳实践

1. 添加适当的等待时间
2. 使用图片识别定位元素
3. 处理异常情况
4. 设置安全措施防止失控