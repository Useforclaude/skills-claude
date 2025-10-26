# 🤔 จำเป็นต้องสร้าง Coding Skills หรือไม่?

## คำถาม: Claude Code เขียนโค้ดเก่งอยู่แล้ว ต้องสร้าง Skills เพิ่มมั้ย?

**คำตอบสั้น:** **ส่วนใหญ่ไม่จำเป็น** แต่มีบางกรณีที่**คุ้มมาก**

---

## 🎯 ทำไม Coding Skills ส่วนใหญ่ไม่จำเป็น

### 1. Claude Code ถูกออกแบบมาเพื่อ Coding โดยเฉพาะ

```
Marketing/Copywriting Skills:
❌ Claude base ไม่เชี่ยวชาญ → ต้องมี skills
✅ เพิ่ม skills แล้วดีขึ้น 10 เท่า (1-2% → 8-15% conversion)

Coding Skills:
✅ Claude Code เชี่ยวชาญอยู่แล้ว → ไม่จำเป็นต้องมี skills
⚠️ เพิ่ม skills อาจดีขึ้นแค่ 10-20% (ไม่คุ้ม)
```

**เหตุผล:**
- Claude Code มี coding knowledge ใน base model สูงมาก (70-80% ของความรู้)
- Marketing/copywriting มีแค่ 1-2% → ต้องเสริม skills
- Coding มี 70-80% → เสริมแล้วได้แค่ +10-20%

---

### 2. Claude Code มี Tools พิเศษสำหรับ Coding อยู่แล้ว

**Built-in Tools:**
- ✅ Read/Write/Edit files
- ✅ Bash commands
- ✅ Git integration
- ✅ Grep/Search codebase
- ✅ MCP servers (database, API, etc.)

**Skills ไม่ได้เพิ่ม tools เหล่านี้** - มันเพิ่มแค่ knowledge เท่านั้น

---

## ⚠️ กรณีที่ควรสร้าง Coding Skills

### ✅ Case 1: Company-Specific Code Standards

**ตัวอย่าง:**
```yaml
---
name: acme-corp-coding-standards
description: ACME Corp internal coding standards, architecture patterns, and best practices. Use when writing code for ACME Corp projects. Includes: naming conventions, file structure, security policies, code review checklist, deployment procedures.
---

# ACME Corp Coding Standards

## File Naming Convention
- Components: PascalCase (UserProfile.tsx)
- Utilities: camelCase (formatDate.ts)
- Constants: SCREAMING_SNAKE_CASE (API_BASE_URL.ts)

## Folder Structure
```
src/
  ├── features/          # Feature-based modules
  │   ├── auth/
  │   │   ├── components/
  │   │   ├── hooks/
  │   │   ├── services/
  │   │   └── types/
  ├── shared/            # Shared utilities
  ├── config/            # Configuration
  └── tests/             # Test files
```

## Security Rules (MANDATORY)
1. Never hardcode API keys
2. Always use environment variables
3. Sanitize user input
4. Use prepared statements for SQL
...
```

**ทำไมคุ้ม:**
- ✅ Claude ไม่รู้ internal standards ของบริษัทคุณ
- ✅ เซฟเวลา (ไม่ต้องบอกทุกครั้ง)
- ✅ Consistency (ทีมเขียนโค้ดแบบเดียวกัน)
- ✅ ลดข้อผิดพลาด (security, compliance)

---

### ✅ Case 2: Legacy Codebase Patterns

**ตัวอย่าง:**
```yaml
---
name: legacy-php-system-skill
description: Working with our legacy PHP 5.6 e-commerce system. Use when modifying or debugging the old PHP codebase. Includes: database schema, custom ORM, quirks and gotchas, migration patterns.
---

# Legacy PHP E-Commerce System

## Database Schema (Custom)
```php
// Users table uses custom encryption
$encrypted_email = legacy_encrypt($email, SALT_KEY);

// Orders table has weird status codes
// 1 = pending, 2 = processing, 5 = shipped (no 3,4!)
// 99 = cancelled (bug in old system)
```

## Quirks & Gotchas
1. **Don't use `isset()`** - Use `legacy_isset()` instead
   Why: Old system overrides isset() behavior

2. **Session handling is broken** - Use custom session wrapper
   ```php
   // ❌ Don't
   $_SESSION['user'] = $user;

   // ✅ Do
   LegacySession::set('user', $user);
   ```

3. **Price must be stored as cents** (not dollars!)
   Bug: Decimal calculations have rounding errors
```

**ทำไมคุ้ม:**
- ✅ Legacy code มี quirks ที่ Claude ไม่รู้
- ✅ ป้องกัน bugs จากการไม่รู้ gotchas
- ✅ เร็วกว่า (ไม่ต้องหา documentation เอง)

---

### ✅ Case 3: Specialized Domain Knowledge

**ตัวอย่าง:**
```yaml
---
name: fintech-compliance-skill
description: Financial software compliance and regulations (PCI-DSS, SOC2, GDPR). Use when building payment systems or handling financial data. Includes: encryption requirements, audit logging, data retention policies.
---

# FinTech Compliance Skill

## PCI-DSS Requirements

### Level 1: NEVER store these
- ❌ Full card number (except last 4 digits)
- ❌ CVV/CVC code
- ❌ PIN

### Level 2: Store encrypted only
- 🔐 Cardholder name
- 🔐 Expiration date
- 🔐 Billing address

### Code Example
```typescript
// ❌ WRONG - PCI violation!
const saveCard = (cardNumber: string) => {
  db.save({ card: cardNumber });
};

// ✅ CORRECT
const saveCard = (cardNumber: string) => {
  const token = tokenizeCard(cardNumber); // Use payment gateway
  db.save({ token }); // Store token only
};
```

## Audit Logging (SOC2 Required)
Every financial transaction MUST log:
1. User ID
2. Timestamp (UTC)
3. Action performed
4. Before/after state
5. IP address
6. Session ID
```

**ทำไมคุ้ม:**
- ✅ Compliance ผิด = โดนปรับหลักล้าน
- ✅ Claude รู้แค่ general → ต้องมี specific rules
- ✅ ป้องกันความผิดพลาดร้ายแรง

---

### ✅ Case 4: Complex Architecture Patterns

**ตัวอย่าง:**
```yaml
---
name: microservices-architecture-skill
description: Our microservices architecture patterns and inter-service communication. Use when building or modifying services. Includes: service boundaries, event schemas, API contracts, deployment patterns.
---

# Microservices Architecture

## Service Communication Matrix

```
┌─────────────┬──────────────┬─────────────┬──────────────┐
│   Service   │   Protocol   │   Pattern   │    Events    │
├─────────────┼──────────────┼─────────────┼──────────────┤
│ Auth        │ gRPC         │ Sync        │ user.*       │
│ Payment     │ REST         │ Async       │ payment.*    │
│ Inventory   │ GraphQL      │ Event-driven│ stock.*      │
│ Notification│ Pub/Sub      │ Fire-forget │ notify.*     │
└─────────────┴──────────────┴─────────────┴──────────────┘
```

## Event Schema Standard

```typescript
// ✅ CORRECT - Follow this exact structure
interface DomainEvent<T> {
  id: string;              // UUID v4
  type: string;            // domain.action (e.g., user.created)
  timestamp: string;       // ISO 8601 UTC
  version: string;         // Semantic versioning
  data: T;                 // Event payload
  metadata: {
    correlationId: string; // For tracing
    causationId: string;   // What caused this
    userId?: string;       // Who triggered
  };
}

// Example
const userCreatedEvent: DomainEvent<UserData> = {
  id: "550e8400-e29b-41d4-a716-446655440000",
  type: "user.created",
  timestamp: "2025-01-24T10:30:00Z",
  version: "1.0.0",
  data: { userId: "123", email: "..." },
  metadata: {
    correlationId: "abc-123",
    causationId: "signup-flow",
    userId: "123"
  }
};
```

## Service Boundaries (DDD)

**Auth Service:**
- ✅ User authentication
- ✅ Token generation
- ❌ User profile data (belongs to User Service)
- ❌ Permissions (belongs to Authorization Service)
```

**ทำไมคุ้ม:**
- ✅ Architecture ซับซ้อน Claude อาจทำผิด
- ✅ Consistency ระหว่าง services
- ✅ ป้องกัน coupling ที่ผิด

---

### ✅ Case 5: Testing Strategies & Patterns

**ตัวอย่าง:**
```yaml
---
name: testing-best-practices-skill
description: Testing strategies, patterns, and our test pyramid. Use when writing tests. Includes: unit test templates, integration test patterns, E2E scenarios, test data factories.
---

# Testing Best Practices

## Test Pyramid (Our Standards)

```
      ╱╲
     ╱E2E╲         10% - Critical user flows only
    ╱────╲
   ╱ INT  ╲        20% - Service integration
  ╱────────╲
 ╱   UNIT   ╲      70% - Business logic, pure functions
╱────────────╲
```

## Unit Test Template

```typescript
// ✅ CORRECT - Follow AAA pattern
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with hashed password', () => {
      // Arrange
      const mockHasher = jest.fn().mockReturnValue('hashed');
      const service = new UserService(mockHasher);
      const input = { email: 'test@test.com', password: 'plain' };

      // Act
      const result = service.createUser(input);

      // Assert
      expect(mockHasher).toHaveBeenCalledWith('plain');
      expect(result.password).toBe('hashed');
    });

    it('should throw error if email already exists', () => {
      // ... (AAA pattern)
    });
  });
});
```

## Test Data Factories

```typescript
// ✅ Use factories - never hardcode test data
import { userFactory, orderFactory } from '@/test/factories';

it('should process order', () => {
  const user = userFactory.build({ role: 'premium' });
  const order = orderFactory.build({
    userId: user.id,
    items: 3
  });

  // Test with realistic data
});
```

## Integration Test Pattern

```typescript
// ✅ CORRECT - Clean database before each test
describe('PaymentAPI', () => {
  beforeEach(async () => {
    await db.clean();
    await seedTestData();
  });

  afterEach(async () => {
    await db.clean();
  });

  it('should process payment', async () => {
    const response = await request(app)
      .post('/api/payments')
      .send({ amount: 1000, currency: 'USD' });

    expect(response.status).toBe(200);

    // Verify database state
    const payment = await db.payments.findOne({ id: response.body.id });
    expect(payment.status).toBe('completed');
  });
});
```

**ทำไมคุ้ม:**
- ✅ Enforce testing standards
- ✅ เร็วกว่า (มี templates)
- ✅ Quality consistency

---

## ❌ กรณีที่ไม่ควรสร้าง Coding Skills

### 1. General Best Practices

**ไม่ควรสร้าง:**
```yaml
---
name: react-best-practices-skill
description: React best practices, hooks, performance optimization
---
```

**ทำไมไม่คุ้ม:**
- ❌ Claude รู้อยู่แล้ว (เก่งมาก)
- ❌ Documentation มีอยู่แล้วเยอะ
- ❌ Skills ไม่ได้ดีกว่า base knowledge

---

### 2. Framework Documentation

**ไม่ควรสร้าง:**
```yaml
---
name: nextjs-documentation-skill
description: Next.js API routes, SSR, SSG, ISR patterns
---
```

**ทำไมไม่คุ้ม:**
- ❌ Claude รู้ Next.js ดีอยู่แล้ว
- ❌ Official docs ดีกว่า
- ❌ Framework เปลี่ยนบ่อย → skills เก่าเร็ว

**ทำแทน:**
- ✅ ให้ Claude อ่าน official docs ตอนต้องใช้
- ✅ ใช้ MCP servers เชื่อม API docs

---

### 3. Language Syntax

**ไม่ควรสร้าง:**
```yaml
---
name: typescript-syntax-skill
description: TypeScript types, interfaces, generics
---
```

**ทำไมไม่คุ้ม:**
- ❌ Claude expert TypeScript อยู่แล้ว
- ❌ Syntax ไม่ซับซ้อน
- ❌ เสียเวลาสร้างโดยใช่เหตุ

---

## 📊 สรุป: สร้างหรือไม่สร้าง?

### ✅ สร้าง (คุ้ม) ถ้า:

| กรณี | ตัวอย่าง | ROI |
|------|---------|-----|
| **Company Standards** | Code style, folder structure, security | ⭐⭐⭐⭐⭐ |
| **Legacy Systems** | Quirks, gotchas, custom frameworks | ⭐⭐⭐⭐⭐ |
| **Compliance** | PCI-DSS, HIPAA, GDPR, SOC2 | ⭐⭐⭐⭐⭐ |
| **Complex Architecture** | Microservices, event-driven | ⭐⭐⭐⭐ |
| **Domain-Specific** | Financial calculations, medical | ⭐⭐⭐⭐ |
| **Internal Tools/APIs** | Custom libraries, internal services | ⭐⭐⭐⭐ |
| **Testing Standards** | Test pyramid, factories, patterns | ⭐⭐⭐ |

---

### ❌ ไม่สร้าง (ไม่คุ้ม) ถ้า:

| กรณี | ตัวอย่าง | ทำแทน |
|------|---------|--------|
| **General Best Practices** | React, Node.js, Python | ใช้ base Claude Code |
| **Framework Docs** | Next.js, FastAPI, Django | ให้ Claude อ่าน docs |
| **Language Syntax** | TypeScript, Rust, Go | ใช้ base knowledge |
| **Common Patterns** | MVC, Repository, Factory | Claude รู้อยู่แล้ว |
| **Public APIs** | Stripe, AWS, Twilio | ใช้ MCP servers |

---

## 🎯 Decision Tree

```
มี code ที่ต้องเขียนบ่อยหรือเปล่า?
│
├─ ใช่ → Claude รู้วิธีเขียนอยู่แล้วหรือเปล่า?
│       │
│       ├─ ใช่ → ❌ ไม่ต้องสร้าง skill
│       │
│       └─ ไม่ → มันเป็น company-specific/legacy/compliance?
│               │
│               ├─ ใช่ → ✅ ควรสร้าง skill (คุ้มมาก!)
│               │
│               └─ ไม่ → เขียน documentation ธรรมดาก็พอ
│
└─ ไม่ → ❌ ไม่ต้องสร้าง skill (ไม่คุ้ม)
```

---

## 💡 คำแนะนำ

### 1. เริ่มจากปัญหาจริง

**❌ อย่าทำ:**
"เราสร้าง 100 coding skills ไว้ก่อน!"

**✅ ทำ:**
"เราเจอ Claude ทำผิด company standards 10 ครั้งแล้ว → สร้าง skill"

---

### 2. วัด ROI ก่อนสร้าง

**คำถามที่ต้องถาม:**
1. ปัญหานี้เจอบ่อยแค่ไหน? (ต่อสัปดาห์)
2. ใช้เวลาแก้นานเท่าไหร่? (ต่อครั้ง)
3. Skill จะช่วยลดเวลาได้เท่าไหร่?
4. ใช้เวลาสร้าง skill นานเท่าไหร่?

**ตัวอย่าง:**
```
ปัญหา: Claude ไม่รู้ company code standards
- เจอ: 20 ครั้ง/สัปดาห์
- เสียเวลาแก้: 10 นาที/ครั้ง
- Total: 200 นาที/สัปดาห์ (3.3 ชม.)

Skill จะช่วย: ลด 80% → เซฟ 2.6 ชม./สัปดาห์
เวลาสร้าง skill: 2 ชม.

ROI: คืนทุนใน 1 สัปดาห์! ✅ คุ้มมาก
```

---

### 3. Keep It Simple

**❌ อย่าทำ:**
สร้าง mega-skill 10,000 บรรทัดครอบคลุมทุกอย่าง

**✅ ทำ:**
สร้างหลาย skills เล็กๆ ตาม domain:
- `company-security-policies-skill`
- `company-code-style-skill`
- `company-deployment-process-skill`

**ทำไมดีกว่า:**
- โหลดเร็วกว่า (โหลดแค่ที่ต้องใช้)
- Update ง่ายกว่า
- Claude เลือก skill ที่เกี่ยวข้องได้แม่นกว่า

---

## 📚 ตัวอย่าง Skills ที่คุ้มจริง

### Example 1: Startup Internal Standards

```yaml
---
name: startup-monorepo-standards
description: Our monorepo structure, shared utilities, and cross-package dependencies. Use when working with our pnpm workspace.
---

# Monorepo Standards

## Package Naming
- Apps: `@company/app-*` (e.g., @company/app-web)
- Packages: `@company/pkg-*` (e.g., @company/pkg-ui)
- Tools: `@company/tool-*` (e.g., @company/tool-build)

## Import Rules
```typescript
// ✅ CORRECT
import { Button } from '@company/pkg-ui';
import { api } from '@company/pkg-api-client';

// ❌ WRONG - Never relative imports across packages
import { Button } from '../../../packages/ui/src/Button';
```

## Shared Config
All packages must extend base configs:
- `tsconfig.base.json`
- `eslint.config.base.js`
- `jest.config.base.js`
```

**ROI:** ทีม 5 คน x 10 นาที/วัน = 50 นาที/วัน = 4+ ชม./สัปดาห์

---

### Example 2: Database Migration Standards

```yaml
---
name: database-migration-standards
description: Database migration patterns and rollback strategies. Use when creating database migrations.
---

# Database Migration Standards

## Migration Naming
```
YYYYMMDDHHMMSS_descriptive_name.sql

Example:
20250124143000_add_user_preferences_table.sql
```

## Safety Checklist
1. ✅ Every migration has UP and DOWN
2. ✅ Test rollback locally
3. ✅ Use transactions
4. ✅ Add indexes CONCURRENTLY (PostgreSQL)
5. ✅ Never drop columns (deprecate instead)

## Template
```sql
-- UP
BEGIN;

CREATE TABLE user_preferences (
  id SERIAL PRIMARY KEY,
  user_id INT NOT NULL REFERENCES users(id),
  theme VARCHAR(20) DEFAULT 'light',
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX CONCURRENTLY idx_user_preferences_user_id
ON user_preferences(user_id);

COMMIT;

-- DOWN
BEGIN;

DROP INDEX IF EXISTS idx_user_preferences_user_id;
DROP TABLE IF EXISTS user_preferences;

COMMIT;
```

**ROI:** ป้องกัน downtime → Worth millions!

---

## 🎉 สรุป

### Marketing/Copywriting Skills
- ✅ **คุ้มมาก** - Base knowledge แค่ 1-2%
- ✅ Conversion เพิ่ม 5-10 เท่า
- ✅ ROI สูงมาก

### Coding Skills (General)
- ❌ **ส่วนใหญ่ไม่คุ้ม** - Base knowledge อยู่ที่ 70-80%
- ⚠️ Improvement แค่ 10-20%
- ⚠️ ROI ต่ำ

### Coding Skills (Specific Cases)
- ✅ **คุ้มมาก** ถ้าเป็น:
  - Company-specific standards
  - Legacy system quirks
  - Compliance requirements
  - Complex architecture patterns
  - Domain-specific rules

---

## 🚀 แนวทางปฏิบัติ

**สำหรับ Skills ที่มีอยู่ (Marketing/Copywriting):**
- ✅ Keep using! คุ้มมาก

**สำหรับ Coding Skills:**
- ⏸️ อย่าเพิ่งสร้าง
- 👀 สังเกตปัญหาที่เจอบ่อย
- 📊 วัด ROI ก่อนสร้าง
- ✅ สร้างเฉพาะที่คุ้มจริงๆ (company-specific, compliance, legacy)

**Rule of Thumb:**
> "ถ้า Claude ทำได้ดีอยู่แล้ว → ไม่ต้องสร้าง skill"
>
> "ถ้า Claude ไม่รู้ company-specific knowledge → สร้าง skill คุ้ม!"

---

**Next Steps:**
1. ใช้ Marketing/Copywriting skills ที่มีอยู่ต่อ (39 skills)
2. สังเกตดูว่ามีปัญหา coding อะไรที่เจอบ่อย
3. ถ้าเจอปัญหาซ้ำๆ → ค่อยพิจารณาสร้าง coding skill
4. ไม่ต้องรีบ - สร้างเมื่อจำเป็นจริงๆ

---

**อัพเดท:** 2025-10-24
**สถานะ:** ✅ มี 39 Marketing/Copywriting Skills (คุ้มมาก!)
**Coding Skills:** ⏸️ รอดูปัญหาก่อน (ไม่ต้องรีบ)
