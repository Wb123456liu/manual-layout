# IDML 结构分析报告

## 文档基本信息

- **文档名：** IEC11kW Bi-directional DC Wallbox Use Manual
- **InDesign 版本：** 20.4 (52)
- **色彩配置：**
  - CMYK: Japan Color 2001 Coated
  - RGB: sRGB IEC61966-2.1
- **语言：** 英文 (UK) + 简体中文

---

## IDML 文件结构

```
document.idml/
├── mimetype                          # 文件类型标识
├── META-INF/
│   ├── container.xml                 # 容器配置
│   └── metadata.xml                  # 元数据
├── designmap.xml                     # 主文档定义 ⭐
├── MasterSpreads/                    # 母版页
│   ├── MasterSpread_u117e0.xml
│   └── ...
├── Spreads/                          # 实际页面 ⭐
│   ├── Spread_u27c.xml
│   └── ... (约 429 个文件)
├── Stories/                          # 文本内容 ⭐
│   └── Story_u10b87.xml
├── Resources/                        # 资源定义
│   ├── Fonts.xml                     # 字体配置
│   ├── Styles.xml                    # 样式定义 ⭐
│   ├── Graphic.xml                   # 图形资源
│   └── Preferences.xml               # 首选项
└── XML/
    └── Tags.xml                      # XML 标签
```

---

## 关键样式分析

### 字符样式 (Character Styles)

| 样式名 | 字体 | 字号 | 行距 | 用途 |
|-------|------|------|------|------|
| 正文 | Mulish | 10pt | 18pt | 正文内容 |
| 正文 regular | HarmonyOS Sans SC | 12pt | 12pt | 正文变体 |
| 小标题 | HarmonyOS Sans SC | 8pt | 12pt | 小标题 |
| 大标题 | Mulish | 15pt | 18pt | 大标题 (橙色 #DC4F03) |
| 字符样式 1 | Mulish | 7pt | 10pt | 注释 |

### 段落样式 (Paragraph Styles)

| 样式名 | 字体 | 字号 | 缩进 | 间距 | 用途 |
|-------|------|------|------|------|------|
| 正文 | Mulish | 10pt | - | After: 0 | 标准正文 |
| 正文 首行缩进 | - | 10pt | 9pt | - | 中文段落 |
| 目录 | 阿里巴巴普惠体 | 9pt | - | - | 目录内容 |
| 目录格式：一级目录 | - | 8pt | - | - | 目录一级 |
| 项目符号 正文 | - | 10pt | 9pt | - | 列表项 |
| Normal | 宋体 | 10.5pt | - | - | 默认样式 |

### 字体使用

| 字体 | 用途 | 类型 |
|-----|------|------|
| Mulish | 英文正文 | 西文 |
| HarmonyOS Sans SC | 中文正文/标题 | 中文 |
| 阿里巴巴普惠体 | 目录 | 中文 |
| Adobe 宋体 Std | 中文正文 | 中文 |
| 宋体 | 默认中文 | 中文 |

---

## 页面设置

### 边距 (Margin)
- **上：** 56.69pt (20mm)
- **下：** 42.52pt (15mm)
- **左：** 28.35pt (10mm)
- **右：** 28.35pt (10mm)

### 页面尺寸
- **A4:** 595.28 x 841.89 pt

### 分栏
- **栏数：** 1
- **栏间距：** 14.17pt (5mm)

---

## 颜色配置

### 专色
- **大标题色：** R=220 G=79 B=3 (橙色)
- **超链接色：** 蓝色

### 色彩管理
- **CMYK Profile:** Japan Color 2001 Coated
- **RGB Profile:** sRGB IEC61966-2.1

---

## IDML 生成关键点

### 1. 必需文件
- `mimetype` - 必须是第一个文件，内容为 `application/vnd.adobe.indesign-idml`
- `META-INF/container.xml` - 指定根文件
- `designmap.xml` - 文档根元素

### 2. 样式映射
```
HTML/CSS → IDML 样式
--------------------------
font-family → AppliedFont
font-size → PointSize
line-height → Leading
color → FillColor
text-align → Justification
margin → SpaceBefore/SpaceAfter
```

### 3. 页面结构
```
Spread (页面)
  └─ Page (页面对象)
      ├─ TextFrame (文本框)
      │   └─ Story (文本内容)
      │       └─ ParagraphStyle (段落样式)
      └─ Rectangle (图形框)
          └─ Image (图片)
```

### 4. 文本流
- 使用 `Story` 元素管理文本流
- 通过 `NextTextFrame` / `PreviousTextFrame` 链接跨页文本

---

## 开发建议

### 阶段 1：基础生成器
1. 创建基本 IDML 结构 (ZIP + XML)
2. 实现简单文本页面
3. 支持基本段落样式

### 阶段 2：样式系统
1. 实现 CSS → IDML 样式转换
2. 支持中文字体
3. 支持段落间距/缩进

### 阶段 3：高级功能
1. 母版页支持
2. 图片插入
3. 目录生成
4. 页眉页脚

---

## 参考资源

- Adobe IDML 规范：https://github.com/adobe/IDML
- Python IDML 库：https://pypi.org/project/idml/ (已废弃)
- 替代方案：手动构建 XML + zipfile 打包
