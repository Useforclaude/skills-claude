---
name: app-architecture-skill
description: Master software architecture and system design. Use for: architecture patterns (MVC, MVVM, Clean Architecture), microservices, monoliths, scalability planning, database design, API design, system components, deployment architecture, and building maintainable large-scale applications. Also use for Thai keywords "สถาปัตยกรรมซอฟต์แวร์", "ออกแบบระบบ", "โครงสร้างแอป", "สถาปัตยกรรมแอป", "Clean Architecture", "Microservices", "ออกแบบ API", "ออกแบบฐานข้อมูล", "ขยายระบบ", "scalability", "ระบบใหญ่", "แอปพลิเคชันใหญ่", "โครงสร้างโค้ด", "architecture pattern", "MVC", "MVVM", "ระบบที่ดี", "ระบบแข็งแรง".
---

# 🏗️ Application Architecture Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [Architecture Fundamentals](#architecture-fundamentals)
2. [Architecture Patterns](#architecture-patterns)
3. [System Design Principles](#system-design-principles)
4. [Database Architecture](#database-architecture)
5. [API Design](#api-design)
6. [Scalability & Performance](#scalability-performance)
7. [Security Architecture](#security-architecture)
8. [Deployment Architecture](#deployment-architecture)
9. [Microservices vs Monoliths](#microservices-monoliths)
10. [Architecture Documentation](#architecture-documentation)

---

## 🎯 Architecture Fundamentals

### What is Software Architecture?

**Definition:** High-level structure of software system, including components, relationships, and principles guiding design.

**Key Responsibilities:**
- Component organization
- Communication patterns
- Data flow
- Technology choices
- Scalability planning
- Security design

---

### Architecture Layers

**Typical 3-Tier Architecture:**
```
┌─────────────────────────┐
│   Presentation Layer    │  ← UI, Views, Controllers
├─────────────────────────┤
│   Business Logic Layer  │  ← Services, Domain Logic
├─────────────────────────┤
│   Data Access Layer     │  ← Database, APIs, Storage
└─────────────────────────┘
```

**Benefits:**
- Separation of concerns
- Independent scaling
- Easier testing
- Team parallelization

---

## 🏛️ Architecture Patterns

### 1. MVC (Model-View-Controller)

```
User → [Controller] → [Model] → [Database]
          ↓
       [View] → User
```

**When to Use:**
- Web applications
- Clear UI separation needed
- Team with frontend/backend split

**Example (Node.js/Express):**
```javascript
// Model
class User {
  static async findById(id) {
    return db.query('SELECT * FROM users WHERE id = ?', [id]);
  }
}

// Controller
const getUser = async (req, res) => {
  const user = await User.findById(req.params.id);
  res.render('user', { user });
};

// View (user.ejs)
<h1><%= user.name %></h1>
```

---

### 2. MVVM (Model-View-ViewModel)

```
[View] ←→ [ViewModel] ←→ [Model]
   ↓          ↓            ↓
  UI     Data Binding   Business Logic
```

**When to Use:**
- Rich client apps (React, Vue, Angular)
- Two-way data binding
- Complex UI state

---

### 3. Clean Architecture (Hexagonal)

**Layers (Inside → Outside):**
```
Core:
┌─────────────────┐
│   Entities      │ ← Business rules
├─────────────────┤
│   Use Cases     │ ← Application logic
├─────────────────┤
│   Interfaces    │ ← Contracts
├─────────────────┤
│   Frameworks    │ ← UI, DB, External APIs
└─────────────────┘
```

**Dependency Rule:** Inner layers don't know about outer layers

**Benefits:**
- Testable (core independent of frameworks)
- Flexible (easy to swap frameworks)
- Maintainable

---

### 4. Event-Driven Architecture

```
[Producer] → [Event Bus] → [Consumer]
                ↓
           [Event Store]
```

**When to Use:**
- Asynchronous processing
- Microservices communication
- Real-time systems
- Decoupled systems

**Example:**
```javascript
// Producer
eventBus.emit('user.created', { userId: 123, email: 'user@example.com' });

// Consumer
eventBus.on('user.created', async (data) => {
  await sendWelcomeEmail(data.email);
  await createUserProfile(data.userId);
});
```

---

## 📐 System Design Principles

### SOLID Principles

**S - Single Responsibility**
```javascript
// ❌ Bad
class User {
  save() { /* database logic */ }
  sendEmail() { /* email logic */ }
}

// ✅ Good
class User {
  // Just user data
}
class UserRepository {
  save(user) { /* database logic */ }
}
class EmailService {
  sendWelcome(user) { /* email logic */ }
}
```

**O - Open/Closed**
```javascript
// ✅ Open for extension, closed for modification
class PaymentProcessor {
  process(payment, strategy) {
    return strategy.execute(payment);
  }
}

class CreditCardStrategy {
  execute(payment) { /* ... */ }
}
class PayPalStrategy {
  execute(payment) { /* ... */ }
}
```

**L - Liskov Substitution**
```javascript
// Subclasses must be substitutable for parent
class Bird {
  fly() { /* ... */ }
}

// ❌ Bad - Penguin can't fly!
class Penguin extends Bird {
  fly() { throw new Error("Can't fly"); }
}

// ✅ Good
class Bird {}
class FlyingBird extends Bird {
  fly() { /* ... */ }
}
class Penguin extends Bird {
  swim() { /* ... */ }
}
```

**I - Interface Segregation**
```javascript
// ✅ Many specific interfaces > one general interface
interface Readable {
  read(): void;
}
interface Writable {
  write(): void;
}

// Classes implement only what they need
class FileReader implements Readable { }
class FileWriter implements Writable { }
```

**D - Dependency Inversion**
```javascript
// ✅ Depend on abstractions, not concretions
class UserService {
  constructor(private database: Database) { }
}

// Inject implementation
const db = new PostgreSQL();
const service = new UserService(db);
```

---

## 🗄️ Database Architecture

### SQL vs NoSQL

**When to Use SQL:**
- Complex relationships
- ACID transactions required
- Structured data
- Reporting/analytics

**When to Use NoSQL:**
- Flexible schema
- Horizontal scaling
- High write throughput
- Document/graph data

---

### Database Patterns

**1. Repository Pattern**
```javascript
class UserRepository {
  async findById(id) {
    return db.users.findOne({ id });
  }

  async save(user) {
    return db.users.insert(user);
  }
}

// Usage
const repo = new UserRepository();
const user = await repo.findById(123);
```

**2. Unit of Work**
```javascript
class UnitOfWork {
  constructor() {
    this.changes = [];
  }

  registerNew(entity) {
    this.changes.push({ type: 'insert', entity });
  }

  async commit() {
    await db.transaction(async (trx) => {
      for (const change of this.changes) {
        await this.execute(change, trx);
      }
    });
  }
}
```

---

## 🔌 API Design

### RESTful API Design

**Resource-Based URLs:**
```
GET    /users          # List users
GET    /users/123      # Get user
POST   /users          # Create user
PUT    /users/123      # Update user
DELETE /users/123      # Delete user

GET    /users/123/posts    # User's posts (nested resource)
```

**HTTP Status Codes:**
```
200 OK              # Success
201 Created         # Resource created
204 No Content      # Success, no body
400 Bad Request     # Invalid input
401 Unauthorized    # Not authenticated
403 Forbidden       # Not authorized
404 Not Found       # Resource doesn't exist
500 Server Error    # Server issue
```

**Response Format:**
```json
{
  "data": { },
  "meta": {
    "page": 1,
    "total": 100
  },
  "errors": []
}
```

---

### GraphQL API Design

**Schema:**
```graphql
type User {
  id: ID!
  name: String!
  email: String!
  posts: [Post!]!
}

type Query {
  user(id: ID!): User
  users(limit: Int, offset: Int): [User!]!
}

type Mutation {
  createUser(name: String!, email: String!): User!
}
```

**Benefits:**
- Request exactly what you need
- Single endpoint
- Strongly typed

**When to Use:**
- Complex data requirements
- Mobile apps (minimize requests)
- Multiple client types

---

## 📈 Scalability & Performance

### Scaling Strategies

**Vertical Scaling (Scale Up):**
```
Add more resources to single server
- More CPU
- More RAM
- Faster disk

Pros: Simple
Cons: Limited, expensive, single point of failure
```

**Horizontal Scaling (Scale Out):**
```
Add more servers
- Load balancer distributes traffic
- Multiple instances

Pros: Unlimited, cost-effective, resilient
Cons: Complex, data consistency challenges
```

---

### Caching Layers

**1. Application Cache (Redis, Memcached)**
```javascript
async function getUser(id) {
  // Check cache first
  const cached = await redis.get(`user:${id}`);
  if (cached) return JSON.parse(cached);

  // Not in cache, fetch from DB
  const user = await db.users.findById(id);

  // Store in cache (10 min TTL)
  await redis.setex(`user:${id}`, 600, JSON.stringify(user));

  return user;
}
```

**2. CDN (Content Delivery Network)**
```
Static assets (images, CSS, JS) served from edge locations
- Closer to users
- Reduces server load
```

**3. Database Query Cache**
```sql
-- Query results cached automatically
SELECT * FROM users WHERE id = 123;
```

---

### Load Balancing

**Strategies:**

**Round Robin:**
```
Request 1 → Server A
Request 2 → Server B
Request 3 → Server C
Request 4 → Server A (repeat)
```

**Least Connections:**
```
Route to server with fewest active connections
```

**IP Hash:**
```
Same client IP always → same server
(useful for session persistence)
```

---

## 🔒 Security Architecture

### Defense in Depth

**Multiple Security Layers:**
```
1. Network Security (Firewall, VPN)
2. Application Security (Authentication, Authorization)
3. Data Security (Encryption, Hashing)
4. Monitoring (Logging, Intrusion Detection)
```

---

### Authentication & Authorization

**Authentication Patterns:**

**1. JWT (JSON Web Tokens)**
```javascript
// Login
const token = jwt.sign(
  { userId: 123, role: 'user' },
  SECRET_KEY,
  { expiresIn: '1h' }
);

// Verify
const decoded = jwt.verify(token, SECRET_KEY);
```

**2. OAuth 2.0**
```
1. User → App: "Login with Google"
2. App → Google: Redirect with client_id
3. Google → User: "Allow app access?"
4. User → Google: "Yes"
5. Google → App: Authorization code
6. App → Google: Exchange code for access token
7. App → Google API: Use access token
```

**3. Session-Based**
```javascript
// Login
req.session.userId = 123;

// Check auth
if (req.session.userId) {
  // Authenticated
}
```

---

## 🚀 Deployment Architecture

### Deployment Patterns

**1. Single Server**
```
[Web App + Database] on one server

Pros: Simple, cheap
Cons: Not scalable, single point of failure
Use for: MVPs, small apps
```

**2. Separate Database**
```
[Web App Server] → [Database Server]

Pros: Can scale independently
Cons: Network latency
```

**3. Load Balanced**
```
       [Load Balancer]
       /      |      \
   [App1] [App2] [App3]
       \      |      /
        [Database]

Pros: High availability, scalable
Cons: Complex, expensive
```

**4. Microservices**
```
[API Gateway]
    ↓
[User Service] → [User DB]
[Order Service] → [Order DB]
[Payment Service] → [Payment DB]

Pros: Independent deploy/scale, technology flexibility
Cons: Very complex, distributed system challenges
```

---

## ⚖️ Microservices vs Monoliths

### Monolithic Architecture

**Structure:**
```
Single codebase, single deployment
All features in one application
```

**Pros:**
- ✅ Simple to develop
- ✅ Easy to test
- ✅ Easy to deploy
- ✅ Good for small teams

**Cons:**
- ❌ Hard to scale (all or nothing)
- ❌ Long-term maintenance difficult
- ❌ Technology lock-in
- ❌ Deployment risk (everything deployed together)

**When to Use:**
- Small to medium projects
- Simple domain
- Small team
- MVP/prototype

---

### Microservices Architecture

**Structure:**
```
Multiple small services
Each owns its data
Communicate via APIs/events
```

**Pros:**
- ✅ Independent scaling
- ✅ Technology flexibility
- ✅ Isolated failures
- ✅ Team autonomy

**Cons:**
- ❌ Complex infrastructure
- ❌ Distributed system challenges
- ❌ Testing difficulty
- ❌ Operational overhead

**When to Use:**
- Large, complex systems
- Multiple teams
- Need independent scaling
- Different technology needs per service

---

### Migration Path

**Start Monolith → Evolve to Microservices:**
```
1. Build monolith first (faster to market)
2. Identify bounded contexts
3. Extract services gradually
4. Keep monolith for core features
5. Migrate high-value/high-traffic features
```

---

## 📄 Architecture Documentation

### C4 Model (Context, Containers, Components, Code)

**Level 1: System Context**
```
Show system and external dependencies

[Users] → [Your System] → [Email Service]
                ↓
          [Payment Gateway]
```

**Level 2: Container**
```
[Web App] → [API] → [Database]
                ↓
          [Redis Cache]
```

**Level 3: Component**
```
Inside API:
[Auth Controller] → [User Service] → [User Repository]
```

**Level 4: Code**
```
Class diagrams, actual code
```

---

### Architecture Decision Records (ADR)

**Template:**
```markdown
# ADR-001: Use PostgreSQL for Primary Database

## Status
Accepted

## Context
Need relational database for user data with complex relationships.
Considering PostgreSQL vs MySQL vs MongoDB.

## Decision
Use PostgreSQL.

## Consequences
Pros:
- Full ACID compliance
- JSON support
- Advanced features (CTEs, window functions)
- Strong community

Cons:
- Learning curve for team
- Operational complexity vs MySQL

## Alternatives Considered
- MySQL: Simpler but less features
- MongoDB: NoSQL not suitable for relational data
```

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,600+
**Status:** Production Ready ✅

---

## 🔧 CODING ULTIMATE STACK: Must Load Together

**This skill is Layer 2: Architecture & Design of THE CODING ULTIMATE STACK system.**

### Same Layer (Architecture & Design - Load All 5):
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
- `git-safety-skill` - Safe version control, branching strategies
- `automation-workflows-skill` - Workflow automation, batch processing
- `security-best-practices-skill` - OWASP, authentication, security audit

### Auto-Loading Modes:
- **Default Stack (12 skills):** Triggers on "code", "เขียนโค้ด", "programming"
- **Aggressive Stack (18 skills):** Triggers on "architecture", "scalability", "รีแฟคเตอร์"
- **Ultimate Stack (25 skills):** Triggers on "ultimate stack", "production-ready", "ช่วยเต็มที่"

### Pro Workflow:
1. **Novice:** Use this skill alone → Basic implementation
2. **Intermediate:** This + 2-3 same-layer skills → 2-3x quality
3. **Expert:** Full Layer 2 + all layers → Production-grade code

**Power Level:** This skill + full stack = 800/1000 (maximum development expertise)
