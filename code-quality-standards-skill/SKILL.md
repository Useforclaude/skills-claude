---
name: code-quality-standards-skill
description: Master code quality standards and best practices. Use for: clean code principles, SOLID, code review guidelines, refactoring techniques, naming conventions, code smells detection, technical debt management, and writing maintainable, readable, professional-grade code. Also use for Thai keywords "คุณภาพโค้ด", "เขียนโค้ดให้ดี", "Clean Code", "SOLID", "รีวิวโค้ด", "code review", "refactoring", "ปรับปรุงโค้ด", "โค้ดสะอาด", "อ่านโค้ดง่าย", "โค้ดที่ดี", "ตั้งชื่อตัวแปร", "naming convention", "code smell", "หนี้ทางเทคนิค", "technical debt", "เขียนโค้ดมืออาชีพ", "โค้ดมาตรฐาน".
---

# ✨ Code Quality Standards Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [Clean Code Principles](#clean-code-principles)
2. [Naming Conventions](#naming-conventions)
3. [Function Design](#function-design)
4. [Code Organization](#code-organization)
5. [Comments & Documentation](#comments-documentation)
6. [Error Handling](#error-handling)
7. [Code Smells](#code-smells)
8. [Refactoring Techniques](#refactoring-techniques)
9. [Code Review Guidelines](#code-review-guidelines)
10. [Technical Debt Management](#technical-debt)

---

## 🎯 Clean Code Principles

### The Boy Scout Rule
**"Leave code cleaner than you found it"**

**Apply when:**
- Fixing bugs → clean surrounding code
- Adding features → refactor related code
- Reviewing code → suggest improvements

---

### DRY (Don't Repeat Yourself)
```javascript
// ❌ Bad - Repetition
function getUserEmail(userId) {
  const user = db.query('SELECT * FROM users WHERE id = ?', [userId]);
  return user.email;
}

function getUserName(userId) {
  const user = db.query('SELECT * FROM users WHERE id = ?', [userId]);
  return user.name;
}

// ✅ Good - Reusable
function getUser(userId) {
  return db.query('SELECT * FROM users WHERE id = ?', [userId]);
}

function getUserEmail(userId) {
  return getUser(userId).email;
}

function getUserName(userId) {
  return getUser(userId).name;
}
```

---

### KISS (Keep It Simple, Stupid)
```javascript
// ❌ Bad - Overcomplicated
function isEven(num) {
  return num % 2 === 0 ? true : num % 2 !== 0 ? false : null;
}

// ✅ Good - Simple
function isEven(num) {
  return num % 2 === 0;
}
```

---

### YAGNI (You Aren't Gonna Need It)
```javascript
// ❌ Bad - Building for future that may never come
class User {
  id: string;
  name: string;
  email: string;
  // These fields "might be needed later"
  middleName?: string;
  phoneNumber2?: string;
  faxNumber?: string;
  maidenName?: string;
}

// ✅ Good - Only what's needed now
class User {
  id: string;
  name: string;
  email: string;
}
// Add fields when actually needed
```

---

## 📛 Naming Conventions

### Variables

**Rules:**
- Descriptive, not abbreviated
- Pronounceable
- Searchable
- No mental mapping

```javascript
// ❌ Bad
let d; // What is d?
let usr; // Abbreviated
let yyyymmdstr; // Unpronounceable

// ✅ Good
let daysSinceCreation;
let user;
let currentDate;
```

---

### Functions

**Rules:**
- Verb + noun
- Describe what it does
- Consistent naming pattern

```javascript
// ❌ Bad
function data() {} // What data?
function handle() {} // Handle what?
function doStuff() {} // Too vague

// ✅ Good
function getUserData() {}
function handleSubmit() {}
function validateEmail() {}
function calculateTotal() {}
```

---

### Classes

**Rules:**
- Noun/noun phrase
- PascalCase
- Specific, not generic

```javascript
// ❌ Bad
class Manager {} // Too generic
class Data {} // What kind of data?
class MyClass {} // Meaningless

// ✅ Good
class UserManager {}
class OrderProcessor {}
class EmailValidator {}
```

---

### Constants

```javascript
// ✅ SCREAMING_SNAKE_CASE for true constants
const MAX_RETRIES = 3;
const API_BASE_URL = 'https://api.example.com';

// ✅ camelCase for config objects
const config = {
  maxRetries: 3,
  timeout: 5000
};
```

---

## ⚙️ Function Design

### Single Responsibility
**Each function should do ONE thing**

```javascript
// ❌ Bad - Multiple responsibilities
function processUserData(userData) {
  // Validate
  if (!userData.email) throw new Error('Invalid email');

  // Transform
  const user = {
    id: generateId(),
    email: userData.email.toLowerCase(),
    name: userData.name.trim()
  };

  // Save
  db.users.insert(user);

  // Send email
  emailService.send(user.email, 'Welcome!');

  // Log
  logger.info('User created', user.id);

  return user;
}

// ✅ Good - Single responsibility per function
function validateUserData(userData) {
  if (!userData.email) throw new Error('Invalid email');
  if (!userData.name) throw new Error('Invalid name');
}

function transformUserData(userData) {
  return {
    id: generateId(),
    email: userData.email.toLowerCase(),
    name: userData.name.trim()
  };
}

function createUser(userData) {
  validateUserData(userData);
  const user = transformUserData(userData);
  db.users.insert(user);
  emailService.sendWelcome(user.email);
  logger.info('User created', user.id);
  return user;
}
```

---

### Small Functions
**Ideal: 5-10 lines, Max: 20 lines**

```javascript
// ❌ Bad - Too long
function processOrder(order) {
  // 100 lines of code...
}

// ✅ Good - Broken down
function processOrder(order) {
  validateOrder(order);
  const total = calculateTotal(order);
  const payment = processPayment(order, total);
  updateInventory(order);
  sendConfirmation(order);
  return { order, payment };
}
```

---

### Function Arguments
**Ideal: 0-2 arguments, Max: 3**

```javascript
// ❌ Bad - Too many arguments
function createUser(name, email, age, address, phone, country) {
  // ...
}

// ✅ Good - Use object
function createUser(userData) {
  const { name, email, age, address, phone, country } = userData;
  // ...
}

// ✅ Even better - Destructure in parameters
function createUser({ name, email, age, address, phone, country }) {
  // ...
}
```

---

### No Side Effects
**Functions should not modify external state**

```javascript
// ❌ Bad - Modifies global state
let total = 0;
function addToTotal(amount) {
  total += amount; // Side effect!
}

// ✅ Good - Pure function
function add(a, b) {
  return a + b;
}

let total = 0;
total = add(total, amount);
```

---

## 📁 Code Organization

### File Structure

```
src/
├── components/        # Reusable UI components
├── services/         # Business logic
├── utils/            # Helper functions
├── config/           # Configuration
├── types/            # TypeScript types
├── constants/        # Constants
└── tests/            # Tests
```

---

### Module Organization

```javascript
// ✅ Good file structure
// user.service.js

// 1. Imports
import db from './database';
import logger from './logger';

// 2. Constants
const MAX_RETRIES = 3;

// 3. Helper functions (private)
function validateEmail(email) {
  // ...
}

// 4. Main functions (public)
export async function createUser(userData) {
  validateEmail(userData.email);
  // ...
}

export async function getUser(id) {
  // ...
}

// 5. Exports (if not inline)
```

---

## 💬 Comments & Documentation

### When to Comment

**✅ DO comment:**
```javascript
// Business rule: Users can't be deleted if they have active orders
if (user.hasActiveOrders()) {
  throw new Error('Cannot delete user with active orders');
}

// Workaround for bug in library v2.3.1
// TODO: Remove when upgrading to v2.4.0
const data = processDataWithWorkaround(input);

// Complex algorithm explanation
// Using Boyer-Moore string search for O(n) performance
function search(text, pattern) {
  // ...
}
```

**❌ DON'T comment:**
```javascript
// ❌ Obvious comments
let user = getUser(); // Get user
let total = 0; // Initialize total to zero

// ❌ Commented out code (use git instead)
// function oldFunction() {
//   // old implementation
// }

// ❌ Noise comments
// =================
// User Functions
// =================

// ❌ Redundant comments
// This function adds two numbers
function add(a, b) {
  return a + b;
}
```

---

### Documentation Comments

```javascript
/**
 * Creates a new user account
 *
 * @param {Object} userData - User information
 * @param {string} userData.email - User's email address
 * @param {string} userData.name - User's full name
 * @returns {Promise<User>} Created user object
 * @throws {ValidationError} If email is invalid
 *
 * @example
 * const user = await createUser({
 *   email: 'john@example.com',
 *   name: 'John Doe'
 * });
 */
async function createUser(userData) {
  // Implementation
}
```

---

## 🚨 Error Handling

### Use Exceptions, Not Error Codes

```javascript
// ❌ Bad - Error codes
function divide(a, b) {
  if (b === 0) return -1; // Error code
  return a / b;
}

const result = divide(10, 0);
if (result === -1) {
  // Handle error
}

// ✅ Good - Exceptions
function divide(a, b) {
  if (b === 0) {
    throw new Error('Division by zero');
  }
  return a / b;
}

try {
  const result = divide(10, 0);
} catch (error) {
  // Handle error
}
```

---

### Custom Error Types

```javascript
class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

class NotFoundError extends Error {
  constructor(resource, id) {
    super(`${resource} with id ${id} not found`);
    this.name = 'NotFoundError';
    this.resource = resource;
    this.id = id;
  }
}

// Usage
try {
  const user = await getUser(123);
  if (!user) {
    throw new NotFoundError('User', 123);
  }
} catch (error) {
  if (error instanceof NotFoundError) {
    // Handle not found
  }
}
```

---

### Don't Return Null

```javascript
// ❌ Bad - Returns null
function getUser(id) {
  const user = db.find(id);
  return user || null;
}

const user = getUser(123);
if (user) {
  // Must check for null everywhere
  console.log(user.name);
}

// ✅ Good - Throw or return default
function getUser(id) {
  const user = db.find(id);
  if (!user) {
    throw new NotFoundError('User', id);
  }
  return user;
}

// Or return empty object (Null Object Pattern)
function getUser(id) {
  const user = db.find(id);
  return user || { name: 'Guest', isGuest: true };
}
```

---

## 👃 Code Smells

### Common Code Smells

**1. Long Method**
```javascript
// ❌ Smell: Function too long
function processOrder() {
  // 100+ lines
}

// ✅ Fix: Extract methods
function processOrder() {
  validateOrder();
  calculateTotal();
  processPayment();
  updateInventory();
  sendConfirmation();
}
```

**2. Large Class**
```javascript
// ❌ Smell: Class doing too much
class User {
  // 50+ methods
}

// ✅ Fix: Split into multiple classes
class User { }
class UserValidator { }
class UserRepository { }
```

**3. Duplicate Code**
```javascript
// ❌ Smell: Copy-paste code
function formatUserName(user) {
  return user.firstName + ' ' + user.lastName;
}

function formatCustomerName(customer) {
  return customer.firstName + ' ' + customer.lastName;
}

// ✅ Fix: Extract common function
function formatFullName(person) {
  return person.firstName + ' ' + person.lastName;
}
```

**4. Magic Numbers**
```javascript
// ❌ Smell: Unclear numbers
if (user.age > 18) { }
setTimeout(callback, 86400000);

// ✅ Fix: Named constants
const LEGAL_AGE = 18;
const ONE_DAY_MS = 24 * 60 * 60 * 1000;

if (user.age > LEGAL_AGE) { }
setTimeout(callback, ONE_DAY_MS);
```

**5. Dead Code**
```javascript
// ❌ Smell: Unused code
function oldFunction() {
  // Never called
}

let unusedVariable;

// ✅ Fix: Delete it (use git if needed later)
```

---

## 🔧 Refactoring Techniques

### Extract Method

```javascript
// Before
function printOwing(invoice) {
  console.log('***********************');
  console.log('**** Customer Owes ****');
  console.log('***********************');

  let outstanding = 0;
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}

// After
function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice.customer, outstanding);
}

function printBanner() {
  console.log('***********************');
  console.log('**** Customer Owes ****');
  console.log('***********************');
}

function calculateOutstanding(invoice) {
  return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(customer, outstanding) {
  console.log(`name: ${customer}`);
  console.log(`amount: ${outstanding}`);
}
```

---

### Replace Conditional with Polymorphism

```javascript
// Before
function getSpeed(vehicle) {
  switch (vehicle.type) {
    case 'car':
      return vehicle.engine.power * 1.5;
    case 'bike':
      return vehicle.engine.power * 2;
    case 'truck':
      return vehicle.engine.power * 1.2;
  }
}

// After
class Vehicle {
  getSpeed() {
    throw new Error('Must implement getSpeed');
  }
}

class Car extends Vehicle {
  getSpeed() {
    return this.engine.power * 1.5;
  }
}

class Bike extends Vehicle {
  getSpeed() {
    return this.engine.power * 2;
  }
}

class Truck extends Vehicle {
  getSpeed() {
    return this.engine.power * 1.2;
  }
}
```

---

### Replace Magic Number with Constant

```javascript
// Before
function calculatePrice(quantity) {
  return quantity * 29.99 * 1.1; // What are these numbers?
}

// After
const ITEM_PRICE = 29.99;
const TAX_RATE = 1.1;

function calculatePrice(quantity) {
  return quantity * ITEM_PRICE * TAX_RATE;
}
```

---

## 👁️ Code Review Guidelines

### Review Checklist

**Functionality:**
- ✅ Does it work as intended?
- ✅ Are edge cases handled?
- ✅ Are there tests?

**Code Quality:**
- ✅ Is it readable?
- ✅ Are names descriptive?
- ✅ Is it DRY?
- ✅ Is it SOLID?

**Performance:**
- ✅ Are there obvious bottlenecks?
- ✅ Is complexity reasonable?
- ✅ Are database queries optimized?

**Security:**
- ✅ Are inputs validated?
- ✅ Is sensitive data protected?
- ✅ Are there SQL injection risks?

**Maintainability:**
- ✅ Is it well-documented?
- ✅ Is it testable?
- ✅ Will future developers understand it?

---

### Review Comments

**✅ Good Review Comments:**
```
"Consider extracting this into a separate function for clarity"
"Could we use Array.map() here instead of the loop?"
"What happens if user is null here?"
"Nice use of the Strategy pattern!"
```

**❌ Bad Review Comments:**
```
"This is wrong" (not helpful)
"Just use X" (no explanation)
"I would have done it differently" (not constructive)
```

---

## 💰 Technical Debt Management

### Identifying Technical Debt

**Types:**
1. **Deliberate** - Shortcuts taken knowingly
2. **Accidental** - Learning as you go
3. **Bit rot** - Code that degrades over time

**Tracking:**
```javascript
// TODO: Refactor this function - too complex
// HACK: Temporary workaround for library bug
// FIXME: Race condition possible here
// OPTIMIZE: N+1 query issue
```

---

### Paying Down Debt

**Strategies:**
1. **Boy Scout Rule** - Clean as you go
2. **Dedicated Time** - 20% time for refactoring
3. **Before New Features** - Refactor related code first
4. **Incremental** - Don't rewrite everything at once

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,400+
**Status:** Production Ready ✅
