---
name: ecto-migrator
description: Ecto 迁移工具技能，用于数据库迁移管理。支持迁移生成、版本控制、回滚、状态检查等。当用户需要：(1) 管理数据库迁移 (2) 生成迁移脚本 (3) 执行迁移 (4) 回滚操作时使用此技能。
---

# Ecto Migrator - 数据库迁移工具

## 核心功能

### 1. 迁移文件结构

```python
# migrations/001_create_users.py
from datetime import datetime

def up():
    """升级迁移"""
    return """
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        password_hash VARCHAR(255) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    
    CREATE INDEX idx_users_email ON users(email);
    """

def down():
    """回滚迁移"""
    return """
    DROP INDEX IF EXISTS idx_users_email;
    DROP TABLE IF EXISTS users;
    """
```

### 2. 迁移管理器

```python
import os
import psycopg2
from datetime import datetime

class MigrationManager:
    def __init__(self, db_url):
        self.conn = psycopg2.connect(db_url)
        self._ensure_migrations_table()
    
    def _ensure_migrations_table(self):
        """确保迁移记录表存在"""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS migrations (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL UNIQUE,
                executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()
    
    def get_pending_migrations(self, migrations_dir):
        """获取待执行的迁移"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM migrations")
        executed = {row[0] for row in cursor.fetchall()}
        
        pending = []
        for filename in sorted(os.listdir(migrations_dir)):
            if filename.endswith('.py') and filename not in executed:
                pending.append(filename)
        
        return pending
    
    def migrate(self, migrations_dir):
        """执行所有待执行的迁移"""
        pending = self.get_pending_migrations(migrations_dir)
        
        for migration_file in pending:
            self._run_migration(migrations_dir, migration_file)
            print(f"✓ Executed: {migration_file}")
    
    def _run_migration(self, migrations_dir, filename):
        """执行单个迁移"""
        # 加载迁移模块
        import importlib.util
        path = os.path.join(migrations_dir, filename)
        spec = importlib.util.spec_from_file_location("migration", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # 执行 up 函数
        cursor = self.conn.cursor()
        cursor.execute(module.up())
        
        # 记录迁移
        cursor.execute(
            "INSERT INTO migrations (name) VALUES (%s)",
            (filename,)
        )
        self.conn.commit()
    
    def rollback(self, migrations_dir, steps=1):
        """回滚迁移"""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT name FROM migrations ORDER BY id DESC LIMIT %s",
            (steps,)
        )
        
        for (filename,) in cursor.fetchall():
            # 加载并执行 down 函数
            path = os.path.join(migrations_dir, filename)
            # ... 执行 down()
            
            # 删除记录
            cursor.execute(
                "DELETE FROM migrations WHERE name = %s",
                (filename,)
            )
            print(f"✓ Rolled back: {filename}")
        
        self.conn.commit()
```

### 3. 生成迁移

```python
def generate_migration(name, migrations_dir):
    """生成新的迁移文件"""
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"{timestamp}_{name}.py"
    filepath = os.path.join(migrations_dir, filename)
    
    template = '''def up():
    """TODO: 升级迁移"""
    return """
    -- 在这里写 SQL
    """

def down():
    """TODO: 回滚迁移"""
    return """
    -- 在这里写回滚 SQL
    """
'''
    
    with open(filepath, 'w') as f:
        f.write(template)
    
    print(f"Created: {filepath}")
```

## 使用示例

```python
# 初始化管理器
manager = MigrationManager("postgresql://localhost/mydb")

# 执行迁移
manager.migrate("./migrations")

# 回滚一步
manager.rollback("./migrations", steps=1)

# 生成新迁移
generate_migration("add_posts_table", "./migrations")
```

## 迁移最佳实践

1. 每个迁移只做一件事
2. 总是提供 down 函数
3. 使用事务确保原子性
4. 迁移文件命名包含时间戳