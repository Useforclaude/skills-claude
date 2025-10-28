---
name: database-design-skill
description: Master database design and optimization for SQL and NoSQL systems. Use for normalization (1NF-5NF), database schema design, indexing strategies, query optimization, SQL design patterns, NoSQL patterns (MongoDB, Redis, Cassandra), ACID vs BASE, CAP theorem, database migrations, data modeling, performance tuning, and production-ready database architecture. Also use for Thai keywords (ฐานข้อมูล, database, SQL, NoSQL, schema, query, index, optimization, ออกแบบฐานข้อมูล).
---

# Database Design Skill

> **Master database design and optimization for production-ready systems**

## Table of Contents

1. [Database Fundamentals](#database-fundamentals)
2. [Relational Database Design (SQL)](#relational-database-design-sql)
3. [Normalization](#normalization)
4. [Indexes and Performance](#indexes-and-performance)
5. [Query Optimization](#query-optimization)
6. [NoSQL Database Patterns](#nosql-database-patterns)
7. [ACID vs BASE](#acid-vs-base)
8. [Database Migrations](#database-migrations)
9. [Data Modeling Best Practices](#data-modeling-best-practices)
10. [Production Database Strategies](#production-database-strategies)

---

## Database Fundamentals

### When to Use SQL vs NoSQL

| Factor | SQL (Relational) | NoSQL (Non-Relational) |
|--------|------------------|------------------------|
| **Data Structure** | Structured, tabular | Flexible, varied |
| **Schema** | Fixed schema | Dynamic schema |
| **Scaling** | Vertical (scale up) | Horizontal (scale out) |
| **Transactions** | ACID guaranteed | Eventually consistent |
| **Best For** | Complex queries, relationships | High throughput, flexibility |
| **Examples** | PostgreSQL, MySQL | MongoDB, Redis, Cassandra |

**Use SQL When:**
- ✅ Data has clear relationships (users → orders → products)
- ✅ Need ACID transactions (banking, e-commerce)
- ✅ Complex queries with JOINs
- ✅ Data integrity is critical

**Use NoSQL When:**
- ✅ Massive scale (millions of writes/sec)
- ✅ Flexible schema (evolving data model)
- ✅ Simple queries (key-value lookups)
- ✅ High availability over consistency

---

## Relational Database Design (SQL)

### Entity-Relationship Diagram (ERD)

**Example: E-Commerce System**

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Users     │         │   Orders     │         │  Products   │
├─────────────┤         ├──────────────┤         ├─────────────┤
│ id (PK)     │────┐    │ id (PK)      │    ┌───│ id (PK)     │
│ email       │    │    │ user_id (FK) │────┘   │ name        │
│ username    │    └───→│ created_at   │        │ price       │
│ created_at  │         │ status       │        │ stock       │
└─────────────┘         └──────────────┘        └─────────────┘
                               │                        │
                               │                        │
                               ↓                        │
                        ┌──────────────┐               │
                        │ Order_Items  │               │
                        ├──────────────┤               │
                        │ id (PK)      │               │
                        │ order_id (FK)│───────────────┘
                        │ product_id(FK)
                        │ quantity     │
                        │ price        │
                        └──────────────┘
```

**SQL Schema:**
```sql
-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    total_amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_status CHECK (status IN ('pending', 'processing', 'completed', 'cancelled'))
);

-- Order_Items table (junction table)
CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER NOT NULL REFERENCES products(id) ON DELETE RESTRICT,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    price DECIMAL(10, 2) NOT NULL,  -- Price at time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(order_id, product_id)  -- Prevent duplicate items in same order
);
```

---

## Normalization

### Normal Forms (1NF to 5NF)

#### **1NF (First Normal Form)**

**Rule:** Eliminate repeating groups, atomic values only

**❌ Not 1NF:**
```sql
CREATE TABLE orders (
    id INTEGER,
    customer_name VARCHAR(100),
    products VARCHAR(500)  -- ❌ "Apple, Orange, Banana" (not atomic!)
);
```

**✅ 1NF:**
```sql
CREATE TABLE orders (
    id INTEGER,
    customer_name VARCHAR(100)
);

CREATE TABLE order_items (
    order_id INTEGER,
    product VARCHAR(100)  -- ✅ Atomic values
);
```

---

#### **2NF (Second Normal Form)**

**Rule:** Must be in 1NF + eliminate partial dependencies (all non-key attributes depend on the whole primary key)

**❌ Not 2NF:**
```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    product_name VARCHAR(100),  -- ❌ Depends only on product_id, not (order_id, product_id)
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```

**✅ 2NF:**
```sql
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100)  -- ✅ Moved to separate table
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER REFERENCES products(product_id),
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```

---

#### **3NF (Third Normal Form)**

**Rule:** Must be in 2NF + eliminate transitive dependencies (non-key attributes depend only on primary key)

**❌ Not 3NF:**
```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    department_id INTEGER,
    department_name VARCHAR(100),  -- ❌ Depends on department_id, not id
    department_location VARCHAR(100)  -- ❌ Transitive dependency
);
```

**✅ 3NF:**
```sql
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    department_id INTEGER REFERENCES departments(id)  -- ✅ No transitive dependency
);
```

---

#### **Denormalization (When to Break Rules)**

**Use Cases:**
- ✅ Read-heavy workloads (100:1 read:write ratio)
- ✅ Performance critical queries
- ✅ Data warehouse / analytics

**Example: Denormalized for Performance**
```sql
-- Normalized (requires JOIN)
SELECT u.username, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;

-- Denormalized (no JOIN needed)
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR(100),
    order_count INTEGER DEFAULT 0  -- ✅ Cached count for performance
);

-- Update via trigger
CREATE TRIGGER update_order_count
AFTER INSERT ON orders
FOR EACH ROW
UPDATE users SET order_count = order_count + 1 WHERE id = NEW.user_id;
```

---

## Indexes and Performance

### Index Types

#### **1. B-Tree Index (Default)**

**Best For:**
- ✅ Equality queries: `WHERE id = 123`
- ✅ Range queries: `WHERE age BETWEEN 18 AND 65`
- ✅ Sorting: `ORDER BY created_at DESC`

**Example:**
```sql
-- Create index
CREATE INDEX idx_users_email ON users(email);

-- Query uses index
SELECT * FROM users WHERE email = 'test@example.com';  -- ✅ Fast
```

---

#### **2. Unique Index**

**Enforce Uniqueness:**
```sql
CREATE UNIQUE INDEX idx_users_email_unique ON users(email);

-- Prevents duplicates
INSERT INTO users (email) VALUES ('test@example.com');  -- OK
INSERT INTO users (email) VALUES ('test@example.com');  -- ❌ ERROR: duplicate key
```

---

#### **3. Composite Index (Multi-Column)**

**Order Matters!**
```sql
-- Create composite index
CREATE INDEX idx_orders_user_status ON orders(user_id, status);

-- ✅ Uses index (leftmost prefix)
SELECT * FROM orders WHERE user_id = 123;
SELECT * FROM orders WHERE user_id = 123 AND status = 'pending';

-- ❌ Does NOT use index (missing leftmost column)
SELECT * FROM orders WHERE status = 'pending';
```

**Rule:** Place most selective column first (the one that filters out most rows)

---

#### **4. Partial Index**

**Index Only Specific Rows:**
```sql
-- Index only active users
CREATE INDEX idx_active_users ON users(email) WHERE is_active = TRUE;

-- Query uses partial index
SELECT * FROM users WHERE email = 'test@example.com' AND is_active = TRUE;  -- ✅ Fast
```

---

#### **5. Full-Text Index (PostgreSQL)**

**For Text Search:**
```sql
-- Add tsvector column
ALTER TABLE products ADD COLUMN search_vector tsvector;

-- Create GIN index
CREATE INDEX idx_products_search ON products USING GIN(search_vector);

-- Update search vector
UPDATE products
SET search_vector = to_tsvector('english', name || ' ' || description);

-- Full-text search
SELECT * FROM products
WHERE search_vector @@ to_tsquery('english', 'laptop & gaming');
```

---

### Index Best Practices

**✅ DO:**
```sql
-- Index foreign keys
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Index columns used in WHERE
CREATE INDEX idx_orders_status ON orders(status);

-- Index columns used in JOIN
CREATE INDEX idx_order_items_product_id ON order_items(product_id);

-- Index columns used in ORDER BY
CREATE INDEX idx_products_price ON products(price DESC);
```

**❌ DON'T:**
```sql
-- Don't index low-cardinality columns (few unique values)
CREATE INDEX idx_users_gender ON users(gender);  -- ❌ Only 3 values: M/F/Other

-- Don't index small tables (< 1000 rows)
CREATE INDEX idx_settings_key ON settings(key);  -- ❌ Table has 10 rows

-- Don't create too many indexes (slows down writes)
-- ❌ 20+ indexes on a single table
```

---

## Query Optimization

### EXPLAIN ANALYZE

**PostgreSQL:**
```sql
EXPLAIN ANALYZE
SELECT u.username, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id;
```

**Output:**
```
Hash Right Join  (cost=15.23..35.67 rows=500 width=12) (actual time=0.234..0.567 rows=500 loops=1)
  Hash Cond: (o.user_id = u.id)
  ->  Seq Scan on orders o  (cost=0.00..18.50 rows=1000 width=4) (actual time=0.012..0.089 rows=1000 loops=1)
  ->  Hash  (cost=10.00..10.00 rows=500 width=8) (actual time=0.156..0.156 rows=500 loops=1)
        ->  Seq Scan on users u  (cost=0.00..10.00 rows=500 width=8) (actual time=0.008..0.045 rows=500 loops=1)
Planning Time: 0.234 ms
Execution Time: 0.789 ms
```

**Key Metrics:**
- **cost:** Estimated cost (lower is better)
- **rows:** Estimated rows returned
- **actual time:** Real execution time
- **Seq Scan:** Table scan (slow for large tables)
- **Index Scan:** Using index (fast)

---

### Common Query Anti-Patterns

#### **❌ N+1 Query Problem**

**Bad:**
```python
# Fetch users
users = db.query("SELECT * FROM users")

# N+1: One query per user!
for user in users:
    orders = db.query("SELECT * FROM orders WHERE user_id = ?", user.id)
```

**Good:**
```python
# Single query with JOIN
results = db.query("""
    SELECT u.*, o.id as order_id, o.total_amount
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
""")
```

---

#### **❌ SELECT * (Select All Columns)**

**Bad:**
```sql
SELECT * FROM products;  -- ❌ Returns all columns (wasteful)
```

**Good:**
```sql
SELECT id, name, price FROM products;  -- ✅ Only needed columns
```

---

#### **❌ LIKE with Leading Wildcard**

**Bad:**
```sql
SELECT * FROM users WHERE email LIKE '%@gmail.com';  -- ❌ Cannot use index
```

**Good:**
```sql
SELECT * FROM users WHERE email LIKE 'john%';  -- ✅ Can use index
```

---

#### **❌ OR in WHERE Clause**

**Bad:**
```sql
SELECT * FROM products WHERE category = 'Electronics' OR category = 'Books';
-- ❌ Cannot efficiently use index
```

**Good:**
```sql
SELECT * FROM products WHERE category IN ('Electronics', 'Books');
-- ✅ Can use index
```

---

### Query Optimization Techniques

#### **1. Use LIMIT for Pagination**

```sql
-- Efficient pagination
SELECT * FROM products
ORDER BY created_at DESC
LIMIT 20 OFFSET 0;  -- Page 1

-- Keyset pagination (better for large offsets)
SELECT * FROM products
WHERE created_at < '2024-01-01 00:00:00'
ORDER BY created_at DESC
LIMIT 20;
```

---

#### **2. Use EXISTS Instead of COUNT**

**Bad:**
```sql
-- Scans entire table
SELECT * FROM users
WHERE (SELECT COUNT(*) FROM orders WHERE user_id = users.id) > 0;
```

**Good:**
```sql
-- Stops at first match
SELECT * FROM users
WHERE EXISTS (SELECT 1 FROM orders WHERE user_id = users.id);
```

---

#### **3. Use UNION ALL Instead of UNION**

```sql
-- UNION removes duplicates (expensive)
SELECT name FROM products WHERE category = 'Electronics'
UNION
SELECT name FROM products WHERE category = 'Books';

-- UNION ALL keeps duplicates (faster)
SELECT name FROM products WHERE category = 'Electronics'
UNION ALL
SELECT name FROM products WHERE category = 'Books';
```

---

## NoSQL Database Patterns

### MongoDB (Document Database)

**When to Use:**
- ✅ Flexible schema (evolving data model)
- ✅ Embedded documents (avoid JOINs)
- ✅ Hierarchical data

**Schema Design:**
```javascript
// Embedded documents (denormalized)
{
  "_id": ObjectId("..."),
  "username": "john_doe",
  "email": "john@example.com",
  "addresses": [  // ✅ Embedded array
    {
      "type": "home",
      "street": "123 Main St",
      "city": "Bangkok"
    },
    {
      "type": "work",
      "street": "456 Office Rd",
      "city": "Bangkok"
    }
  ],
  "orders": [  // ✅ Denormalized for read performance
    {
      "order_id": "ORD-001",
      "total": 1500.00,
      "created_at": ISODate("2024-01-01")
    }
  ]
}
```

**Indexing:**
```javascript
// Create index
db.users.createIndex({ "email": 1 }, { unique: true });

// Compound index
db.orders.createIndex({ "user_id": 1, "status": 1 });

// Text index for search
db.products.createIndex({ "name": "text", "description": "text" });

// Query with text search
db.products.find({ $text: { $search: "laptop gaming" } });
```

---

### Redis (Key-Value Store)

**When to Use:**
- ✅ Caching
- ✅ Session storage
- ✅ Real-time counters
- ✅ Pub/Sub messaging

**Common Patterns:**

**1. Caching:**
```python
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

# Cache user data
user_id = 123
cache_key = f"user:{user_id}"

# Check cache first
user_data = r.get(cache_key)
if user_data:
    return json.loads(user_data)

# Cache miss: fetch from database
user = db.query("SELECT * FROM users WHERE id = ?", user_id)
r.setex(cache_key, 3600, json.dumps(user))  # Cache for 1 hour
return user
```

**2. Rate Limiting:**
```python
def check_rate_limit(user_id, limit=100, window=3600):
    """Allow 100 requests per hour"""
    key = f"rate_limit:{user_id}"
    current = r.incr(key)

    if current == 1:
        r.expire(key, window)  # Set expiration on first request

    return current <= limit
```

**3. Leaderboard:**
```python
# Add score
r.zadd("leaderboard", {"player1": 1500, "player2": 2000})

# Get top 10
top_10 = r.zrevrange("leaderboard", 0, 9, withscores=True)

# Get rank
rank = r.zrevrank("leaderboard", "player1")
```

---

### Cassandra (Wide-Column Store)

**When to Use:**
- ✅ Massive write throughput (millions/sec)
- ✅ Time-series data
- ✅ Distributed across data centers

**Schema Design:**
```cql
-- Time-series data (IoT sensor readings)
CREATE TABLE sensor_readings (
    sensor_id UUID,
    reading_time TIMESTAMP,
    temperature DECIMAL,
    humidity DECIMAL,
    PRIMARY KEY (sensor_id, reading_time)
) WITH CLUSTERING ORDER BY (reading_time DESC);

-- Query recent readings
SELECT * FROM sensor_readings
WHERE sensor_id = uuid-value
  AND reading_time > '2024-01-01 00:00:00'
ORDER BY reading_time DESC
LIMIT 100;
```

---

## ACID vs BASE

### ACID (SQL Databases)

**Atomicity:** All or nothing (transaction commits or rolls back completely)
**Consistency:** Data always valid (constraints enforced)
**Isolation:** Transactions don't interfere
**Durability:** Committed data persists (survives crashes)

**Example:**
```sql
BEGIN TRANSACTION;

-- Deduct from sender
UPDATE accounts SET balance = balance - 100 WHERE id = 1;

-- Add to receiver
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

-- ✅ Both succeed or both fail (atomicity)
COMMIT;
```

---

### BASE (NoSQL Databases)

**Basically Available:** System always responds (may be stale data)
**Soft state:** State may change over time (even without input)
**Eventually consistent:** Data becomes consistent eventually (not immediately)

**Example (MongoDB):**
```javascript
// Write to primary
db.users.updateOne({ _id: 123 }, { $set: { status: "active" } });

// Read from replica (may be stale for a few milliseconds)
db.users.findOne({ _id: 123 });  // Might still show old status

// Eventually consistent: Replica catches up within seconds
```

---

## Database Migrations

### PostgreSQL - Alembic (Python)

**Installation:**
```bash
pip install alembic
alembic init migrations
```

**Create Migration:**
```bash
alembic revision -m "create_users_table"
```

**Migration File:**
```python
# migrations/versions/001_create_users_table.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    """Apply migration"""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('username', sa.String(100), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now())
    )
    op.create_index('idx_users_email', 'users', ['email'])

def downgrade():
    """Rollback migration"""
    op.drop_index('idx_users_email')
    op.drop_table('users')
```

**Run Migrations:**
```bash
# Apply all migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# Show current version
alembic current
```

---

### Node.js - Knex Migrations

**Create Migration:**
```bash
npx knex migrate:make create_users_table
```

**Migration File:**
```javascript
// migrations/20240101000000_create_users_table.js
exports.up = function(knex) {
  return knex.schema.createTable('users', (table) => {
    table.increments('id').primary();
    table.string('email', 255).unique().notNullable();
    table.string('username', 100).notNullable();
    table.timestamp('created_at').defaultTo(knex.fn.now());
    table.index('email');
  });
};

exports.down = function(knex) {
  return knex.schema.dropTable('users');
};
```

**Run Migrations:**
```bash
# Apply migrations
npx knex migrate:latest

# Rollback
npx knex migrate:rollback
```

---

## Data Modeling Best Practices

### 1. Choose Primary Keys Wisely

**Auto-Increment (SERIAL):**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY  -- ✅ Simple, fast, sequential
);
```

**UUID:**
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid()  -- ✅ Globally unique, distributed systems
);
```

**When to Use:**
- **SERIAL:** Single database, sequential IDs acceptable
- **UUID:** Distributed systems, merge data from multiple sources

---

### 2. Use Appropriate Data Types

**❌ Bad:**
```sql
CREATE TABLE products (
    price VARCHAR(50),  -- ❌ Should be DECIMAL
    stock VARCHAR(50),  -- ❌ Should be INTEGER
    is_active VARCHAR(10)  -- ❌ Should be BOOLEAN
);
```

**✅ Good:**
```sql
CREATE TABLE products (
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- ✅ Precise money
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),  -- ✅ Integer
    is_active BOOLEAN DEFAULT TRUE  -- ✅ Boolean
);
```

---

### 3. Add Timestamps

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- ✅ Track creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- ✅ Track updates
);

-- Trigger to update updated_at
CREATE TRIGGER update_users_updated_at
BEFORE UPDATE ON users
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();
```

---

## Production Database Strategies

### 1. Connection Pooling

**PostgreSQL - psycopg2 (Python):**
```python
from psycopg2 import pool

# Create connection pool
db_pool = pool.SimpleConnectionPool(
    minconn=5,
    maxconn=20,
    host="localhost",
    database="mydb",
    user="user",
    password="password"
)

# Get connection from pool
conn = db_pool.getconn()
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

# Return connection to pool
db_pool.putconn(conn)
```

---

### 2. Read Replicas

**Setup:**
```
┌─────────────┐
│   Primary   │  ← Writes
└──────┬──────┘
       │ Replication
       ├────────────┬─────────────┐
       ↓            ↓             ↓
  ┌─────────┐  ┌─────────┐  ┌─────────┐
  │Replica 1│  │Replica 2│  │Replica 3│  ← Reads
  └─────────┘  └─────────┘  └─────────┘
```

**Usage (Python):**
```python
# Write to primary
primary_db.execute("INSERT INTO users (email) VALUES ('test@example.com')")

# Read from replica
replica_db.execute("SELECT * FROM users WHERE email = 'test@example.com'")
```

---

### 3. Backup Strategies

**PostgreSQL - pg_dump:**
```bash
# Full backup
pg_dump -U postgres -d mydb -F c -f backup_$(date +%Y%m%d).dump

# Restore
pg_restore -U postgres -d mydb backup_20240101.dump

# Automated daily backup (cron)
0 2 * * * pg_dump -U postgres -d mydb -F c -f /backups/backup_$(date +\%Y\%m\%d).dump
```

---

### 4. Monitoring

**Key Metrics:**
- ✅ Query performance (slow query log)
- ✅ Connection count
- ✅ Cache hit ratio
- ✅ Replication lag
- ✅ Disk space

**PostgreSQL - Enable Slow Query Log:**
```sql
-- Log queries slower than 1 second
ALTER DATABASE mydb SET log_min_duration_statement = 1000;

-- View slow queries
SELECT query, mean_exec_time, calls
FROM pg_stat_statements
ORDER BY mean_exec_time DESC
LIMIT 10;
```

---

## Quick Reference - Database Commands

### PostgreSQL
```bash
# Connect to database
psql -U postgres -d mydb

# List databases
\l

# List tables
\dt

# Describe table
\d users

# Execute SQL file
psql -U postgres -d mydb -f schema.sql

# Backup
pg_dump -U postgres -d mydb > backup.sql

# Restore
psql -U postgres -d mydb < backup.sql
```

### MongoDB
```bash
# Connect to database
mongosh

# Show databases
show dbs

# Use database
use mydb

# Show collections
show collections

# Query
db.users.find({ email: "test@example.com" })

# Backup
mongodump --db mydb --out /backup/

# Restore
mongorestore --db mydb /backup/mydb/
```

### Redis
```bash
# Connect
redis-cli

# Set key
SET user:123 "John Doe"

# Get key
GET user:123

# List all keys
KEYS *

# Delete key
DEL user:123

# Flush all data
FLUSHALL
```

---

## Summary: Database Design Checklist

**Schema Design:**
- [ ] Normalize to 3NF (or justify denormalization)
- [ ] Use appropriate data types
- [ ] Add constraints (NOT NULL, CHECK, UNIQUE)
- [ ] Add timestamps (created_at, updated_at)
- [ ] Choose appropriate primary key (SERIAL vs UUID)

**Performance:**
- [ ] Index foreign keys
- [ ] Index columns used in WHERE/JOIN/ORDER BY
- [ ] Avoid indexing low-cardinality columns
- [ ] Use EXPLAIN ANALYZE to verify query plans
- [ ] Implement connection pooling

**Production:**
- [ ] Set up read replicas for scalability
- [ ] Implement automated backups
- [ ] Monitor slow queries
- [ ] Use migrations for schema changes
- [ ] Test disaster recovery procedures

---

**Power Level:** Database design mastery + full CODING ULTIMATE STACK = 800/1000 development expertise

---

## 🔧 CODING ULTIMATE STACK: Must Load Together

**This skill is Layer 2: Architecture & Design of THE CODING ULTIMATE STACK system.**

### Same Layer (Architecture & Design - Load All 6):
- `app-architecture-skill` - System design, microservices, scalability
- `architecture-patterns-skill` - MVC, MVVM, Clean Architecture, design patterns
- `design-systems-skill` - Component architecture, design tokens
- `api-wrapper-saas-skill` - API design, Gateway patterns
- `modern-frontend-skill` - Frontend architecture, state management

### Next Layer (Implementation - Load 3-5):
- `python-best-practices-skill` - Pythonic code, PEP 8, type hints
- `javascript-modern-skill` - ES6+, async/await, modern JS
- `code-quality-standards-skill` - Clean code, SOLID, refactoring, code smells
- `automation-workflows-skill` - Workflow automation, batch processing
- `document-conversion-skill` - MD → PDF, HTML → PDF, Pandoc

### Deployment Layer (Load 2-3):
- `docker-containerization-skill` - Docker, Kubernetes, container orchestration
- `git-safety-skill` - Safe version control, branching strategies
- `automation-workflows-skill` - Workflow automation, batch processing

### Auto-Loading Modes:
- **Default Stack (12 skills):** Triggers on "code", "เขียนโค้ด", "programming"
- **Aggressive Stack (20 skills):** Triggers on "architecture", "scalability", "รีแฟคเตอร์"
- **Ultimate Stack (28 skills):** Triggers on "ultimate stack", "production-ready", "ช่วยเต็มที่"

### Pro Workflow:
1. **Novice:** Use this skill alone → Basic implementation
2. **Intermediate:** This + 2-3 same-layer skills → 2-3x quality
3. **Expert:** Full Layer 2 + all layers → Production-grade code

**Power Level:** This skill + full stack = 800/1000 (maximum development expertise)
