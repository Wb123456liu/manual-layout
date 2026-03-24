#!/usr/bin/env python3
"""
Review Agent - 产品手册评审专家
"""

import json
import os
from datetime import datetime
from pathlib import Path


class ReviewAgent:
    """产品手册评审 Agent"""
    
    def __init__(self, config_path=None):
        """
        初始化评审 Agent
        
        Args:
            config_path: 配置文件路径，默认使用 config/review_rules.json
        """
        if config_path is None:
            config_path = Path(__file__).parent.parent.parent / "config" / "review_rules.json"
        
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        self.review_rules = self.config['review_rules']
        self.safety_levels = self.config['safety_levels']
        self.timeout_minutes = self.config.get('review_timeout_minutes', 30)
    
    def get_config(self, region, product_type, manual_type):
        """
        获取对应组合的配置
        
        Args:
            region: 销售区域 (CN/EU/US/SEA)
            product_type: 产品类型 (AC_Charger/DC_Charger/Home_Storage/PCS)
            manual_type: 手册类型 (UM/IM/MM/DS)
        
        Returns:
            配置字典
        """
        # 简写映射
        manual_type_map = {
            "User_Manual": "UM",
            "Installation_Manual": "IM",
            "Maintenance_Manual": "MM",
            "Spec_Sheet": "DS",
            "UM": "UM",
            "IM": "IM",
            "MM": "MM",
            "DS": "DS"
        }
        
        manual_type_short = manual_type_map.get(manual_type, manual_type)
        config_id = f"{region}_{product_type}_{manual_type_short}"
        return self.review_rules.get(config_id)
    
    def review(self, manual_content, region, product_type, manual_type):
        """
        评审手册
        
        Args:
            manual_content: 手册内容（文本或文件路径）
            region: 销售区域
            product_type: 产品类型
            manual_type: 手册类型
        
        Returns:
            评审报告字典
        """
        config = self.get_config(region, product_type, manual_type)
        
        if not config:
            raise ValueError(f"未找到配置：{region}_{product_type}_{manual_type}")
        
        # 构建评审 Prompt
        prompt = self._build_prompt(manual_content, config)
        
        # 调用 AI 模型进行评审（这里用伪代码，实际调用需要接入 AI 模型）
        # review_result = call_ai_model(prompt)
        
        # 模拟评审结果
        review_result = self._simulate_review(config)
        
        return review_result
    
    def _build_prompt(self, manual_content, config):
        """构建评审 Prompt"""
        prompt_template = Path(__file__).parent / "prompts" / "review_expert.md"
        
        with open(prompt_template, 'r', encoding='utf-8') as f:
            template = f.read()
        
        # 替换变量
        prompt = template.replace("{{region}}", config['region'])
        prompt = prompt.replace("{{product_type}}", config['product_type'])
        prompt = prompt.replace("{{manual_type}}", config['manual_type'])
        prompt = prompt.replace("{{manual_content}}", str(manual_content))
        
        return prompt
    
    def _simulate_review(self, config):
        """
        模拟评审结果（用于测试）
        
        实际使用时替换为 AI 模型调用
        """
        return {
            "basic_info": {
                "manual_name": "IEC11kW Bi-directional DC Wallbox Use Manual",
                "version": "v1.0",
                "review_time": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "region": config['region'],
                "product_type": config['product_type'],
                "manual_type": config['manual_type']
            },
            "review_result": {
                "conclusion": "⚠️ 需修改",
                "problems": {
                    "P0": [
                        {
                            "page": 15,
                            "description": "接线图 L1 相线颜色错误",
                            "type": "安全",
                            "risk": "可能导致用户接线错误，不符合 IEC 60446 标准",
                            "suggestion": "将 L1 相线颜色改为棕色 #8B4513"
                        },
                        {
                            "page": 3,
                            "description": "封面缺少 CE 认证标志",
                            "type": "安全",
                            "risk": "不符合欧盟法规要求，产品无法上市",
                            "suggestion": "在封面添加 CE 标志，尺寸不小于 5mm"
                        }
                    ],
                    "P1": [
                        {
                            "page": 22,
                            "description": "术语不一致，'充电桩'和'充电机'混用",
                            "type": "技术",
                            "risk": "影响专业性和用户理解",
                            "suggestion": "统一使用'充电桩'"
                        }
                    ],
                    "P2": [
                        {
                            "page": 5,
                            "description": "目录页码右对齐不一致",
                            "type": "格式",
                            "risk": "影响美观",
                            "suggestion": "统一右对齐"
                        }
                    ]
                },
                "statistics": {
                    "total": 4,
                    "P0": 2,
                    "P1": 1,
                    "P2": 1
                },
                "suggestions": {
                    "review_rounds": 2,
                    "estimated_time_hours": 1,
                    "re_review_required": True
                }
            }
        }
    
    def generate_report(self, review_result, format='markdown'):
        """
        生成评审报告
        
        Args:
            review_result: 评审结果字典
            format: 输出格式 (markdown/html/json)
        
        Returns:
            格式化的评审报告
        """
        if format == 'markdown':
            return self._generate_markdown_report(review_result)
        elif format == 'json':
            return json.dumps(review_result, ensure_ascii=False, indent=2)
        else:
            raise ValueError(f"不支持的格式：{format}")
    
    def _generate_markdown_report(self, review_result):
        """生成 Markdown 格式评审报告"""
        basic = review_result['basic_info']
        result = review_result['review_result']
        
        report = f"""# 评审报告

## 基本信息
- 手册名称：{basic['manual_name']}
- 版本：{basic['version']}
- 评审时间：{basic['review_time']}
- 销售区域：{basic['region']}
- 产品类型：{basic['product_type']}
- 手册类型：{basic['manual_type']}

## 评审结果
**结论：** {result['conclusion']}

## 问题清单

### P0 关键问题（必须修改）
"""
        
        for i, problem in enumerate(result['problems']['P0'], 1):
            report += f"""
{i}. 【页码 {problem['page']}】{problem['description']}
   - 类型：{problem['type']}
   - 风险：{problem['risk']}
   - 修改建议：{problem['suggestion']}
"""
        
        report += "\n### P1 重要问题（建议修改）\n"
        for i, problem in enumerate(result['problems']['P1'], 1):
            report += f"""
{i}. 【页码 {problem['page']}】{problem['description']}
   - 类型：{problem['type']}
   - 修改建议：{problem['suggestion']}
"""
        
        report += "\n### P2 一般问题（可选修改）\n"
        for i, problem in enumerate(result['problems']['P2'], 1):
            report += f"""
{i}. 【页码 {problem['page']}】{problem['description']}
   - 类型：{problem['type']}
   - 修改建议：{problem['suggestion']}
"""
        
        stats = result['statistics']
        suggestions = result['suggestions']
        
        report += f"""
## 统计
- 问题总数：{stats['total']} 个
- P0 关键：{stats['P0']} 个
- P1 重要：{stats['P1']} 个
- P2 一般：{stats['P2']} 个

## 修改建议
- 建议修改轮次：{suggestions['review_rounds']} 轮
- 预计修改时间：{suggestions['estimated_time_hours']} 小时
- 复审建议：{'需要' if suggestions['re_review_required'] else '不需要'}

---
**评审 Agent：** Review Agent
**生成时间：** {datetime.now().strftime("%Y-%m-%d %H:%M")}
"""
        
        return report


# 测试
if __name__ == "__main__":
    # 创建评审 Agent
    reviewer = ReviewAgent()
    
    # 模拟评审
    result = reviewer.review(
        manual_content="手册内容...",
        region="EU",
        product_type="DC",
        manual_type="UM"
    )
    
    # 生成报告
    report = reviewer.generate_report(result, format='markdown')
    print(report)
    
    # 保存到文件
    output_path = Path(__file__).parent.parent.parent / "review_report.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ 评审报告已保存到：{output_path}")
