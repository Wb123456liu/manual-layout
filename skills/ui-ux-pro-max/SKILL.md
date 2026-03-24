---
name: ui-ux-pro-max
description: UI/UX 专业版技能，用于用户界面和体验设计。支持设计系统、组件库、原型设计、可用性测试等。当用户需要：(1) 设计用户界面 (2) 创建设计系统 (3) 构建原型 (4) 评估可用性时使用此技能。
---

# UI/UX Pro Max - UI/UX 专业版

## 核心功能

### 1. 设计系统

```yaml
# design-system.yaml
colors:
  primary:
    50: '#f0f9ff'
    100: '#e0f2fe'
    500: '#0ea5e9'
    900: '#0c4a6e'
  neutral:
    50: '#fafafa'
    500: '#737373'
    900: '#171717'
  success: '#10b981'
  warning: '#f59e0b'
  error: '#ef4444'

typography:
  fontFamily:
    heading: 'Inter, sans-serif'
    body: 'Inter, sans-serif'
    mono: 'JetBrains Mono, monospace'
  fontSize:
    xs: '0.75rem'
    sm: '0.875rem'
    base: '1rem'
    lg: '1.125rem'
    xl: '1.25rem'
    2xl: '1.5rem'
    3xl: '1.875rem'
  fontWeight:
    normal: 400
    medium: 500
    semibold: 600
    bold: 700

spacing:
  0: '0'
  1: '0.25rem'
  2: '0.5rem'
  4: '1rem'
  8: '2rem'
  16: '4rem'

borderRadius:
  none: '0'
  sm: '0.125rem'
  md: '0.375rem'
  lg: '0.5rem'
  full: '9999px'
```

### 2. 组件规范

```css
/* 按钮组件 */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: var(--spacing-2) var(--spacing-4);
  font-size: var(--font-size-base);
  font-weight: var(--font-weight-medium);
  border-radius: var(--radius-md);
  transition: all 0.2s ease;
}

.btn-primary {
  background: var(--color-primary-500);
  color: white;
}

.btn-primary:hover {
  background: var(--color-primary-600);
}

.btn-secondary {
  background: var(--color-neutral-100);
  color: var(--color-neutral-900);
}

/* 输入框组件 */
.input {
  width: 100%;
  padding: var(--spacing-2) var(--spacing-3);
  font-size: var(--font-size-base);
  border: 1px solid var(--color-neutral-300);
  border-radius: var(--radius-md);
}

.input:focus {
  outline: none;
  border-color: var(--color-primary-500);
  box-shadow: 0 0 0 3px var(--color-primary-100);
}
```

### 3. 布局系统

```css
/* 栅格系统 */
.grid {
  display: grid;
  gap: var(--spacing-4);
}

.grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
.grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
.grid-cols-4 { grid-template-columns: repeat(4, 1fr); }

/* Flex 布局 */
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-between { justify-content: space-between; }
.gap-4 { gap: var(--spacing-4); }

/* 响应式 */
@media (max-width: 768px) {
  .grid-cols-2, .grid-cols-3, .grid-cols-4 {
    grid-template-columns: 1fr;
  }
}
```

### 4. 可用性检查清单

```markdown
## 可用性检查清单

### 视觉设计
- [ ] 对比度符合 WCAG 2.1 AA 标准（4.5:1）
- [ ] 色彩不只作为唯一信息传达方式
- [ ] 字体大小足够（正文至少 16px）
- [ ] 行高适当（1.5-1.8）

### 交互
- [ ] 所有交互元素可键盘访问
- [ ] 焦点状态清晰可见
- [ ] 表单有清晰的标签和错误提示
- [ ] 加载状态有反馈

### 内容
- [ ] 标题层次清晰（h1-h6）
- [ ] 图片有替代文本
- [ ] 链接文本有意义（避免"点击这里"）
- [ ] 语言属性正确设置

### 响应式
- [ ] 在移动端可用
- [ ] 触摸目标足够大（至少 44x44px）
- [ ] 内容不溢出
```

### 5. 原型模板

```html
<!-- 移动端页面模板 -->
<!DOCTYPE html>
<html lang="zh">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prototype</title>
  <link rel="stylesheet" href="design-system.css">
</head>
<body>
  <!-- 顶部导航 -->
  <header class="sticky top-0 bg-white border-b">
    <nav class="flex items-center justify-between p-4">
      <div class="logo">Logo</div>
      <button class="btn-icon">☰</button>
    </nav>
  </header>
  
  <!-- 主内容 -->
  <main class="p-4">
    <!-- 内容区域 -->
  </main>
  
  <!-- 底部导航 -->
  <nav class="fixed bottom-0 left-0 right-0 bg-white border-t">
    <div class="flex justify-around p-2">
      <a href="#" class="flex flex-col items-center">
        <span>🏠</span>
        <span class="text-xs">首页</span>
      </a>
      <a href="#" class="flex flex-col items-center">
        <span>🔍</span>
        <span class="text-xs">搜索</span>
      </a>
      <a href="#" class="flex flex-col items-center">
        <span>👤</span>
        <span class="text-xs">我的</span>
      </a>
    </div>
  </nav>
</body>
</html>
```

## 设计原则

1. **一致性** - 统一的视觉语言
2. **可访问性** - 所有人可用
3. **响应式** - 适配各种设备
4. **性能** - 快速加载响应
5. **简洁** - 减少认知负担

## 常用工具

| 工具 | 用途 |
|------|------|
| Figma | 设计/原型 |
| Tailwind CSS | 样式框架 |
| Storybook | 组件文档 |
| axe DevTools | 可访问性测试 |