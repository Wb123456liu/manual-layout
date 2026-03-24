---
name: typescript-pro
description: TypeScript 专业版技能，提供高级 TypeScript 开发支持。支持类型推断、代码生成、重构、类型定义生成等。当用户需要：(1) TypeScript 开发 (2) 类型定义 (3) 代码重构 (4) 类型检查时使用此技能。
---

# TypeScript Pro - TypeScript 专业版

## 核心功能

### 1. 类型推断

```typescript
// 自动类型推断
const inferType = (value: unknown) => {
  if (typeof value === 'string') return 'string';
  if (typeof value === 'number') return 'number';
  if (typeof value === 'boolean') return 'boolean';
  if (Array.isArray(value)) return 'array';
  if (value instanceof Date) return 'date';
  if (typeof value === 'object' && value !== null) return 'object';
  return 'unknown';
};
```

### 2. 类型定义生成

```typescript
// 从 JSON 生成类型定义
type JsonToType<T> = T extends string ? string :
  T extends number ? number :
  T extends boolean ? boolean :
  T extends Array<infer U> ? JsonToType<U>[] :
  T extends object ? { [K in keyof T]: JsonToType<T[K]> } :
  never;

// 示例：从 API 响应生成类型
interface ApiResponse {
  code: number;
  message: string;
  data: {
    id: string;
    name: string;
    items: Array<{
      title: string;
      value: number;
    }>;
  };
}
```

### 3. 工具类型

```typescript
// 深度只读
type DeepReadonly<T> = {
  readonly [P in keyof T]: T[P] extends object 
    ? DeepReadonly<T[P]> 
    : T[P];
};

// 深度可选
type DeepPartial<T> = {
  [P in keyof T]?: T[P] extends object 
    ? DeepPartial<T[P]> 
    : T[P];
};

// 提取函数参数类型
type Parameters<T> = T extends (...args: infer P) => any ? P : never;

// 提取函数返回类型
type ReturnType<T> = T extends (...args: any) => infer R ? R : never;
```

### 4. 代码生成

```typescript
// 生成接口定义
function generateInterface(name: string, fields: Record<string, string>): string {
  const fieldDefs = Object.entries(fields)
    .map(([key, type]) => `  ${key}: ${type};`)
    .join('\n');
  return `interface ${name} {\n${fieldDefs}\n}`;
}

// 示例
const UserInterface = generateInterface('User', {
  id: 'string',
  name: 'string',
  email: 'string',
  age: 'number',
  createdAt: 'Date'
});
```

### 5. 类型守卫

```typescript
// 类型守卫函数
function isString(value: unknown): value is string {
  return typeof value === 'string';
}

function isNumber(value: unknown): value is number {
  return typeof value === 'number';
}

function isArray<T>(value: unknown, itemGuard: (v: unknown) => v is T): value is T[] {
  return Array.isArray(value) && value.every(itemGuard);
}

// 使用示例
function process(value: unknown) {
  if (isString(value)) {
    console.log(value.toUpperCase());
  } else if (isNumber(value)) {
    console.log(value.toFixed(2));
  }
}
```

## 常用模式

### 泛型约束

```typescript
// 约束必须有 id 属性
interface WithId {
  id: string;
}

function getById<T extends WithId>(items: T[], id: string): T | undefined {
  return items.find(item => item.id === id);
}
```

### 条件类型

```typescript
// 根据条件选择类型
type ApiResponse<T> = T extends { error: string } 
  ? { success: false; error: string }
  : { success: true; data: T };
```

## 最佳实践

1. 使用 `strict` 模式
2. 优先使用 `interface` 定义对象类型
3. 使用 `type` 定义联合类型和工具类型
4. 善用类型守卫进行运行时检查