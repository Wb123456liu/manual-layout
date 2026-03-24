---
name: chart-generator
description: 图表生成器技能，用于生成各种类型的数据可视化图表。支持柱状图、折线图、饼图、散点图、热力图等。当用户需要：(1) 生成数据图表 (2) 可视化数据 (3) 创建统计图 (4) 制作报告图表时使用此技能。
---

# Chart Generator - 图表生成器

## 核心功能

### 1. 柱状图

```python
import matplotlib.pyplot as plt

def bar_chart(data, labels, title=None, output_path=None):
    """生成柱状图"""
    plt.figure(figsize=(10, 6))
    plt.bar(labels, data)
    if title:
        plt.title(title)
    plt.xlabel('类别')
    plt.ylabel('数值')
    
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    else:
        plt.show()
    plt.close()
```

### 2. 折线图

```python
def line_chart(data_list, labels, legends=None, title=None, output_path=None):
    """生成折线图"""
    plt.figure(figsize=(10, 6))
    
    for i, data in enumerate(data_list):
        legend = legends[i] if legends else None
        plt.plot(labels, data, label=legend, marker='o')
    
    if legends:
        plt.legend()
    if title:
        plt.title(title)
    
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
```

### 3. 饼图

```python
def pie_chart(data, labels, title=None, output_path=None):
    """生成饼图"""
    plt.figure(figsize=(8, 8))
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
    if title:
        plt.title(title)
    
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
```

### 4. 散点图

```python
def scatter_plot(x_data, y_data, title=None, output_path=None):
    """生成散点图"""
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, alpha=0.6)
    if title:
        plt.title(title)
    plt.xlabel('X')
    plt.ylabel('Y')
    
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
```

### 5. 热力图

```python
import seaborn as sns

def heatmap(data, x_labels, y_labels, title=None, output_path=None):
    """生成热力图"""
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, xticklabels=x_labels, yticklabels=y_labels, 
                annot=True, fmt='d', cmap='YlOrRd')
    if title:
        plt.title(title)
    
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
```

### 6. 雷达图

```python
import numpy as np

def radar_chart(data, labels, title=None, output_path=None):
    """生成雷达图"""
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
    data = data + data[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.plot(angles, data, 'o-', linewidth=2)
    ax.fill(angles, data, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    
    if title:
        plt.title(title)
    
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    plt.close()
```

## 使用示例

```python
# 柱状图
bar_chart([10, 20, 15, 25], ['A', 'B', 'C', 'D'], 
          title='销售数据', output_path='bar.png')

# 折线图
line_chart([[1, 2, 3, 4], [2, 3, 2, 5]], 
           ['Q1', 'Q2', 'Q3', 'Q4'],
           legends=['产品A', '产品B'],
           output_path='line.png')

# 饼图
pie_chart([30, 25, 20, 25], ['A', 'B', 'C', 'D'],
          title='市场份额', output_path='pie.png')
```

## 支持的图表类型

| 类型 | 用途 |
|------|------|
| 柱状图 | 类别比较 |
| 折线图 | 趋势展示 |
| 饼图 | 占比分布 |
| 散点图 | 相关性分析 |
| 热力图 | 密度/相关性 |
| 雷达图 | 多维对比 |