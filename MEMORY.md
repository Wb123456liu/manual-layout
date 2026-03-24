# MEMORY.md - 长期记忆

## 关于老铁

- **称呼：** 老铁（不是"大哥"！）
- **风格偏好：** 喜欢幽默风格

---

## 当前项目：AI 产品手册排版系统

### 系统架构

```
用户提交 → 排版 Agent → 评审 Agent → 输出模块 → 交付
```

### 核心组件

| 组件 | 状态 | 说明 |
|-----|------|------|
| **排版 Agent** | ✅ 已完成 | manual-typesetting + style-kit |
| **评审 Agent** | ✅ 已完成 | 技术 + 安全 + 本地化检查 |
| **PDF 输出** | ✅ 已完成 | WeasyPrint (300DPI, CMYK) |
| **IDML 输出** | ✅ 已完成 | idml-generator |
| **配置系统** | ✅ 已完成 | 16 种组合规则 |

---

## 评审 Agent 设计

### 角色定位
资深产品手册评审专家，20 年技术文档审核经验

### 检查范围
- **技术检查（40%）**：参数准确性、电路图、操作步骤、术语一致性
- **安全检查（40%）**：安全标识、警告语、认证标志
- **本地化检查（20%）**：翻译、单位、日期格式

### 问题分级
| 级别 | 说明 | 处理 |
|-----|------|------|
| P0 | 安全事故/违反法规/严重误导 | 必须修改，复审 |
| P1 | 影响理解/不专业/不符合标准 | 建议修改 |
| P2 | 格式小问题/可优化细节 | 可选修改 |

### 评审报告
- 基本信息（手册名称、版本、区域、类型）
- 评审结论（通过/需修改/驳回）
- 问题清单（P0/P1/P2）
- 统计数据
- 修改建议

---

## 配置系统

### 16 种组合规则

| 区域 | 产品类型 | 手册类型 | 配置 ID |
|-----|---------|---------|--------|
| CN | AC/DC/HS/PCS | UM/IM/MM/DS | CN_AC_UM 等 |
| EU | AC/DC/HS/PCS | UM/IM/MM/DS | EU_AC_UM 等 |
| US | AC/DC/HS/PCS | UM/IM/MM/DS | US_AC_UM 等 |
| SEA | AC/DC/HS/PCS | UM/IM/MM/DS | SEA_AC_UM 等 |

### 配置内容
- 适用标准（GB/CE/UL/IEC）
- 认证要求（CCC/CE/UL）
- 语言配置
- 输出格式
- 评审重点

---

## 技术栈

| 功能 | 工具 | 状态 |
|-----|------|------|
| 文档解析 | miaoda-doc-parse | ✅ |
| 排版 | manual-typesetting + style-kit | ✅ |
| PDF 生成 | WeasyPrint v68.1 | ✅ |
| IDML 生成 | idml-generator (自研) | ✅ |
| 评审 | review-agent (自研) | ✅ |
| 配置管理 | JSON 配置文件 | ✅ |

---

## 文件位置

- **评审 Agent：** `/root/.openclaw/workspace/skills/review-agent/`
- **配置文件：** `/root/.openclaw/workspace/config/review_rules.json`
- **IDML 生成器：** `/root/.openclaw/workspace/skills/idml-generator/`
- **测试报告：** `/root/.openclaw/workspace/review_report.md`

---

## 下一步

1. ⏳ 标准化输入表单/提示词
2. ⏳ 端到端集成测试
3. ⏳ 真实案例验证

---

**状态：** 核心功能开发完成，待集成测试  
**目标：** 月底前完成工作流搭建
