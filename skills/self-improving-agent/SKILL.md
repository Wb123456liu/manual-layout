---
name: self-improving-agent
description: 自我改进代理技能，用于 Agent 的自我优化和迭代改进。支持性能分析、错误学习、策略调整、能力扩展等。当用户需要：(1) 优化 Agent 性能 (2) 学习错误案例 (3) 改进策略 (4) 扩展能力时使用此技能。
---

# Self Improving Agent - 自我改进代理

## 核心功能

### 1. 性能分析

```python
import time
from collections import defaultdict

class PerformanceTracker:
    def __init__(self):
        self.metrics = defaultdict(list)
    
    def track(self, operation, duration, success=True):
        """记录性能指标"""
        self.metrics[operation].append({
            'duration': duration,
            'success': success,
            'timestamp': time.time()
        })
    
    def analyze(self, operation):
        """分析操作性能"""
        data = self.metrics[operation]
        if not data:
            return None
        
        durations = [d['duration'] for d in data]
        success_rate = sum(d['success'] for d in data) / len(data)
        
        return {
            'count': len(data),
            'avg_duration': sum(durations) / len(durations),
            'max_duration': max(durations),
            'min_duration': min(durations),
            'success_rate': success_rate
        }
    
    def get_slow_operations(self, threshold=1.0):
        """获取慢操作"""
        slow = []
        for op, data in self.metrics.items():
            avg = sum(d['duration'] for d in data) / len(data)
            if avg > threshold:
                slow.append((op, avg))
        return sorted(slow, key=lambda x: x[1], reverse=True)
```

### 2. 错误学习

```python
import json

class ErrorLearner:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.errors = self._load()
    
    def _load(self):
        try:
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        except:
            return []
    
    def _save(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.errors, f, indent=2)
    
    def record_error(self, error_type, context, solution=None):
        """记录错误"""
        self.errors.append({
            'type': error_type,
            'context': context,
            'solution': solution,
            'timestamp': time.time()
        })
        self._save()
    
    def find_similar(self, error_type, context):
        """查找相似错误"""
        similar = []
        for err in self.errors:
            if err['type'] == error_type:
                # 简单相似度计算
                similarity = self._calculate_similarity(context, err['context'])
                if similarity > 0.5:
                    similar.append((err, similarity))
        
        return sorted(similar, key=lambda x: x[1], reverse=True)
    
    def suggest_solution(self, error_type, context):
        """建议解决方案"""
        similar = self.find_similar(error_type, context)
        if similar:
            return similar[0][0].get('solution')
        return None
```

### 3. 策略调整

```python
class StrategyOptimizer:
    def __init__(self):
        self.strategies = {}
        self.performance = defaultdict(list)
    
    def register_strategy(self, name, func, conditions):
        """注册策略"""
        self.strategies[name] = {
            'func': func,
            'conditions': conditions,
            'weight': 1.0
        }
    
    def select_strategy(self, context):
        """选择最佳策略"""
        candidates = []
        for name, strategy in self.strategies.items():
            if self._matches_conditions(context, strategy['conditions']):
                candidates.append((name, strategy['weight']))
        
        if not candidates:
            return None
        
        # 选择权重最高的
        return max(candidates, key=lambda x: x[1])[0]
    
    def update_weight(self, strategy_name, success, reward):
        """更新策略权重"""
        if strategy_name in self.strategies:
            current = self.strategies[strategy_name]['weight']
            # 简单的强化学习更新
            delta = 0.1 * (reward if success else -reward)
            self.strategies[strategy_name]['weight'] = max(0.1, current + delta)
```

### 4. 能力扩展

```python
class CapabilityManager:
    def __init__(self):
        self.capabilities = {}
    
    def register(self, name, func, description):
        """注册新能力"""
        self.capabilities[name] = {
            'func': func,
            'description': description,
            'usage_count': 0
        }
    
    def execute(self, name, *args, **kwargs):
        """执行能力"""
        if name not in self.capabilities:
            raise ValueError(f"Unknown capability: {name}")
        
        result = self.capabilities[name]['func'](*args, **kwargs)
        self.capabilities[name]['usage_count'] += 1
        return result
    
    def get_capabilities(self):
        """获取所有能力"""
        return [
            {'name': name, **info}
            for name, info in self.capabilities.items()
        ]
```

## 使用示例

```python
# 创建自我改进代理
tracker = PerformanceTracker()
learner = ErrorLearner("./errors.json")
optimizer = StrategyOptimizer()

# 记录性能
start = time.time()
# ... 执行操作 ...
tracker.track("process_document", time.time() - start)

# 学习错误
try:
    # ... 执行操作 ...
except Exception as e:
    solution = learner.suggest_solution(type(e).__name__, str(e))
    if solution:
        print(f"建议解决方案: {solution}")
```

## 改进原则

1. 持续监控性能指标
2. 从错误中学习并记录
3. 根据反馈调整策略
4. 逐步扩展能力边界