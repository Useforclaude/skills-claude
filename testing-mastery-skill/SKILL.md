---
name: testing-mastery-skill
description: Master comprehensive testing strategies for quality software. Use for unit testing (pytest, Jest, unittest, JUnit), integration testing, E2E testing (Cypress, Selenium, Playwright), TDD/BDD methodology, mocking and fixtures, code coverage analysis, test automation, CI/CD testing integration, performance testing, and building robust test suites. Also use for Thai keywords (ทดสอบ, unit test, integration test, mock, coverage, TDD, BDD, automated testing, เทสต์).
---

# Testing Mastery Skill

> **Master comprehensive testing strategies for production-ready quality software**

## Table of Contents

1. [Testing Fundamentals](#testing-fundamentals)
2. [Unit Testing](#unit-testing)
3. [Integration Testing](#integration-testing)
4. [End-to-End (E2E) Testing](#end-to-end-e2e-testing)
5. [Test-Driven Development (TDD)](#test-driven-development-tdd)
6. [Behavior-Driven Development (BDD)](#behavior-driven-development-bdd)
7. [Mocking and Fixtures](#mocking-and-fixtures)
8. [Code Coverage Analysis](#code-coverage-analysis)
9. [Test Automation Best Practices](#test-automation-best-practices)
10. [CI/CD Integration](#cicd-integration)
11. [Performance and Load Testing](#performance-and-load-testing)
12. [Testing Patterns and Anti-Patterns](#testing-patterns-and-anti-patterns)

---

## Testing Fundamentals

### The Testing Pyramid

```
       /\
      /E2E\        ← Few (5-10%) - Slow, expensive, brittle
     /------\
    /Integration\ ← Some (20-30%) - Medium speed/cost
   /------------\
  /  Unit Tests  \ ← Many (60-75%) - Fast, cheap, stable
 /________________\
```

**Key Principles:**
- ✅ **Fast feedback** - Unit tests run in milliseconds
- ✅ **Isolation** - Each test independent
- ✅ **Repeatability** - Same input → same output
- ✅ **Self-validating** - Pass/fail, no manual checking
- ✅ **Timely** - Write tests before/during development

### When to Use Each Test Type

| Test Type | When to Use | Example |
|-----------|-------------|---------|
| **Unit** | Testing single functions/methods | `calculate_discount(100, 0.2)` returns `80` |
| **Integration** | Testing multiple components together | Database + API layer working together |
| **E2E** | Testing complete user workflows | User login → browse → checkout → payment |
| **Performance** | Testing speed/load capacity | API handles 1000 requests/second |
| **Security** | Testing vulnerabilities | SQL injection, XSS prevention |

---

## Unit Testing

### Python - pytest

**Installation:**
```bash
pip install pytest pytest-cov pytest-mock
```

**Basic Structure:**
```python
# test_calculator.py
import pytest
from calculator import Calculator

class TestCalculator:
    """Test suite for Calculator class"""

    @pytest.fixture
    def calc(self):
        """Fixture: Create calculator instance for each test"""
        return Calculator()

    def test_add_positive_numbers(self, calc):
        """Test: Adding positive numbers"""
        result = calc.add(5, 3)
        assert result == 8

    def test_add_negative_numbers(self, calc):
        """Test: Adding negative numbers"""
        result = calc.add(-5, -3)
        assert result == -8

    def test_divide_by_zero_raises_error(self, calc):
        """Test: Division by zero raises ValueError"""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
    ])
    def test_add_multiple_cases(self, calc, a, b, expected):
        """Test: Parametrized test for multiple inputs"""
        assert calc.add(a, b) == expected
```

**Run Tests:**
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_calculator.py

# Run specific test
pytest tests/test_calculator.py::TestCalculator::test_add_positive_numbers

# Run with verbose output
pytest -v

# Run tests matching pattern
pytest -k "test_add"
```

---

### JavaScript/TypeScript - Jest

**Installation:**
```bash
npm install --save-dev jest @types/jest ts-jest
```

**Basic Structure:**
```javascript
// calculator.test.js
import { Calculator } from './calculator';

describe('Calculator', () => {
  let calc;

  beforeEach(() => {
    // Setup: Create fresh calculator for each test
    calc = new Calculator();
  });

  afterEach(() => {
    // Cleanup: Reset state after each test
    calc = null;
  });

  test('should add two positive numbers', () => {
    const result = calc.add(5, 3);
    expect(result).toBe(8);
  });

  test('should handle negative numbers', () => {
    const result = calc.add(-5, -3);
    expect(result).toBe(-8);
  });

  test('should throw error when dividing by zero', () => {
    expect(() => calc.divide(10, 0)).toThrow('Cannot divide by zero');
  });

  test.each([
    [2, 3, 5],
    [0, 0, 0],
    [-1, 1, 0],
    [100, 200, 300],
  ])('add(%i, %i) should return %i', (a, b, expected) => {
    expect(calc.add(a, b)).toBe(expected);
  });
});
```

**Run Tests:**
```bash
# Run all tests
npm test

# Run with coverage
npm test -- --coverage

# Run in watch mode
npm test -- --watch

# Run specific test file
npm test calculator.test.js
```

---

### Java - JUnit 5

**Basic Structure:**
```java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private Calculator calc;

    @BeforeEach
    void setUp() {
        // Setup: Create calculator before each test
        calc = new Calculator();
    }

    @Test
    @DisplayName("Should add two positive numbers")
    void testAddPositiveNumbers() {
        int result = calc.add(5, 3);
        assertEquals(8, result, "5 + 3 should equal 8");
    }

    @Test
    void testDivideByZeroThrowsException() {
        Exception exception = assertThrows(
            ArithmeticException.class,
            () -> calc.divide(10, 0)
        );
        assertTrue(exception.getMessage().contains("Cannot divide by zero"));
    }

    @ParameterizedTest
    @CsvSource({
        "2, 3, 5",
        "0, 0, 0",
        "-1, 1, 0",
        "100, 200, 300"
    })
    void testAddMultipleCases(int a, int b, int expected) {
        assertEquals(expected, calc.add(a, b));
    }
}
```

---

## Integration Testing

### Testing Database + API Layer (Python + FastAPI)

```python
# test_integration_api_db.py
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models import User

# Setup test database
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def test_db():
    """Create fresh database for each test"""
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(test_db):
    """Create test client with test database"""
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)

def test_create_user_integration(client, test_db):
    """Integration test: API + Database"""
    # Step 1: Create user via API
    response = client.post("/users/", json={
        "email": "test@example.com",
        "username": "testuser",
        "password": "securepass123"
    })

    # Verify API response
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

    # Step 2: Verify user exists in database
    user = test_db.query(User).filter(User.email == "test@example.com").first()
    assert user is not None
    assert user.username == "testuser"
    assert user.password != "securepass123"  # Should be hashed

    # Step 3: Verify user can be retrieved via API
    user_id = data["id"]
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    assert get_response.json()["email"] == "test@example.com"
```

---

## End-to-End (E2E) Testing

### Cypress (JavaScript)

**Installation:**
```bash
npm install --save-dev cypress
npx cypress open
```

**E2E Test Example:**
```javascript
// cypress/e2e/checkout_flow.cy.js
describe('E2E: Complete Checkout Flow', () => {
  beforeEach(() => {
    // Setup: Visit homepage
    cy.visit('https://example.com');
  });

  it('should complete full checkout process', () => {
    // Step 1: Login
    cy.get('[data-testid="login-button"]').click();
    cy.get('input[name="email"]').type('user@example.com');
    cy.get('input[name="password"]').type('password123');
    cy.get('button[type="submit"]').click();
    cy.url().should('include', '/dashboard');

    // Step 2: Browse products
    cy.get('[data-testid="products-link"]').click();
    cy.get('.product-card').first().click();

    // Step 3: Add to cart
    cy.get('[data-testid="add-to-cart"]').click();
    cy.get('.cart-badge').should('contain', '1');

    // Step 4: Checkout
    cy.get('[data-testid="cart-icon"]').click();
    cy.get('[data-testid="checkout-button"]').click();

    // Step 5: Fill shipping info
    cy.get('input[name="address"]').type('123 Main St');
    cy.get('input[name="city"]').type('Bangkok');
    cy.get('input[name="zip"]').type('10110');
    cy.get('button[type="submit"]').click();

    // Step 6: Payment
    cy.get('input[name="cardNumber"]').type('4242424242424242');
    cy.get('input[name="expiry"]').type('12/25');
    cy.get('input[name="cvc"]').type('123');
    cy.get('[data-testid="pay-button"]').click();

    // Verify: Order confirmation
    cy.url().should('include', '/order-confirmation');
    cy.get('.success-message').should('be.visible');
    cy.get('.order-number').should('exist');
  });
});
```

**Run Cypress:**
```bash
# Open Cypress UI
npx cypress open

# Run headless
npx cypress run

# Run specific test
npx cypress run --spec "cypress/e2e/checkout_flow.cy.js"
```

---

### Playwright (Modern E2E)

**Installation:**
```bash
npm install --save-dev @playwright/test
npx playwright install
```

**E2E Test Example:**
```javascript
// tests/e2e/login.spec.js
import { test, expect } from '@playwright/test';

test.describe('User Authentication Flow', () => {
  test('should login successfully with valid credentials', async ({ page }) => {
    // Navigate to login page
    await page.goto('https://example.com/login');

    // Fill login form
    await page.fill('input[name="email"]', 'user@example.com');
    await page.fill('input[name="password"]', 'password123');
    await page.click('button[type="submit"]');

    // Verify redirect to dashboard
    await expect(page).toHaveURL(/.*dashboard/);
    await expect(page.locator('.welcome-message')).toContainText('Welcome back');
  });

  test('should show error with invalid credentials', async ({ page }) => {
    await page.goto('https://example.com/login');
    await page.fill('input[name="email"]', 'invalid@example.com');
    await page.fill('input[name="password"]', 'wrongpass');
    await page.click('button[type="submit"]');

    // Verify error message
    await expect(page.locator('.error-message')).toBeVisible();
    await expect(page.locator('.error-message')).toContainText('Invalid credentials');
  });
});
```

---

## Test-Driven Development (TDD)

### The TDD Cycle (Red-Green-Refactor)

```
1. RED:    Write failing test
           ↓
2. GREEN:  Write minimum code to pass
           ↓
3. REFACTOR: Improve code quality
           ↓
           [Repeat]
```

### TDD Example (Python)

**Step 1: Write Failing Test (RED)**
```python
# test_shopping_cart.py
import pytest
from shopping_cart import ShoppingCart

def test_new_cart_is_empty():
    """Test: New cart should have zero items"""
    cart = ShoppingCart()
    assert cart.item_count() == 0  # ❌ FAILS - ShoppingCart doesn't exist yet
```

**Step 2: Write Minimum Code (GREEN)**
```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = []

    def item_count(self):
        return len(self.items)  # ✅ PASSES
```

**Step 3: Add Next Test (RED again)**
```python
def test_add_item_increases_count():
    """Test: Adding item should increase count"""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    assert cart.item_count() == 1  # ❌ FAILS - add_item() doesn't exist
```

**Step 4: Implement Feature (GREEN)**
```python
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def item_count(self):
        return len(self.items)  # ✅ PASSES
```

**Step 5: Refactor (improve quality)**
```python
from dataclasses import dataclass
from typing import List

@dataclass
class CartItem:
    name: str
    price: float

class ShoppingCart:
    def __init__(self):
        self.items: List[CartItem] = []

    def add_item(self, name: str, price: float) -> None:
        """Add item to cart"""
        self.items.append(CartItem(name, price))

    def item_count(self) -> int:
        """Get number of items in cart"""
        return len(self.items)

    def total_price(self) -> float:
        """Calculate total price"""
        return sum(item.price for item in self.items)
```

---

## Behavior-Driven Development (BDD)

### Gherkin Syntax

```gherkin
# features/shopping_cart.feature
Feature: Shopping Cart Management
  As a customer
  I want to add items to my shopping cart
  So that I can purchase multiple items

  Scenario: Add single item to empty cart
    Given I have an empty shopping cart
    When I add "Apple" with price 1.50
    Then the cart should contain 1 item
    And the total price should be 1.50

  Scenario: Add multiple items
    Given I have an empty shopping cart
    When I add "Apple" with price 1.50
    And I add "Orange" with price 2.00
    Then the cart should contain 2 items
    And the total price should be 3.50
```

### Python - behave

**Installation:**
```bash
pip install behave
```

**Step Definitions:**
```python
# features/steps/shopping_cart_steps.py
from behave import given, when, then
from shopping_cart import ShoppingCart

@given('I have an empty shopping cart')
def step_empty_cart(context):
    context.cart = ShoppingCart()

@when('I add "{item}" with price {price:f}')
def step_add_item(context, item, price):
    context.cart.add_item(item, price)

@then('the cart should contain {count:d} item(s)')
def step_verify_count(context, count):
    assert context.cart.item_count() == count

@then('the total price should be {total:f}')
def step_verify_total(context, total):
    assert context.cart.total_price() == total
```

**Run BDD Tests:**
```bash
behave
```

---

## Mocking and Fixtures

### Python - pytest Fixtures

```python
# conftest.py (shared fixtures)
import pytest
from unittest.mock import Mock, patch
from database import Database
from api_client import APIClient

@pytest.fixture
def mock_database():
    """Mock database for testing"""
    db = Mock(spec=Database)
    db.get_user.return_value = {"id": 1, "name": "John"}
    db.save_user.return_value = True
    return db

@pytest.fixture
def mock_api_client():
    """Mock external API client"""
    client = Mock(spec=APIClient)
    client.fetch_data.return_value = {"status": "success", "data": [1, 2, 3]}
    return client

@pytest.fixture
def sample_user_data():
    """Sample user data for testing"""
    return {
        "id": 1,
        "email": "test@example.com",
        "username": "testuser",
        "created_at": "2024-01-01T00:00:00Z"
    }
```

**Using Fixtures:**
```python
# test_user_service.py
def test_get_user_returns_correct_data(mock_database, sample_user_data):
    """Test: UserService.get_user() returns data from database"""
    from user_service import UserService

    # Setup mock
    mock_database.get_user.return_value = sample_user_data

    # Test
    service = UserService(mock_database)
    user = service.get_user(1)

    # Verify
    assert user["email"] == "test@example.com"
    mock_database.get_user.assert_called_once_with(1)
```

---

### Mocking External APIs

```python
# test_weather_service.py
import pytest
from unittest.mock import patch, Mock
import requests

def test_get_weather_returns_temperature():
    """Test: WeatherService returns temperature from external API"""
    from weather_service import WeatherService

    # Mock external API response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "temperature": 25.5,
        "condition": "Sunny"
    }

    with patch('requests.get', return_value=mock_response) as mock_get:
        service = WeatherService()
        weather = service.get_weather("Bangkok")

        # Verify
        assert weather["temperature"] == 25.5
        mock_get.assert_called_once_with(
            "https://api.weather.com/v1/weather",
            params={"city": "Bangkok"}
        )
```

---

## Code Coverage Analysis

### Python - pytest-cov

**Run with coverage:**
```bash
# Terminal output
pytest --cov=src tests/

# HTML report
pytest --cov=src --cov-report=html tests/
open htmlcov/index.html

# XML report (for CI/CD)
pytest --cov=src --cov-report=xml tests/
```

**Coverage Configuration (.coveragerc):**
```ini
[run]
source = src
omit =
    */tests/*
    */venv/*
    */__pycache__/*

[report]
precision = 2
show_missing = True
skip_covered = False

[html]
directory = htmlcov
```

---

### JavaScript - Jest Coverage

**Run with coverage:**
```bash
npm test -- --coverage

# Coverage thresholds in package.json
```

**package.json configuration:**
```json
{
  "jest": {
    "collectCoverageFrom": [
      "src/**/*.{js,jsx,ts,tsx}",
      "!src/**/*.test.{js,jsx,ts,tsx}",
      "!src/index.js"
    ],
    "coverageThreshold": {
      "global": {
        "branches": 80,
        "functions": 80,
        "lines": 80,
        "statements": 80
      }
    }
  }
}
```

---

## Test Automation Best Practices

### 1. Test Naming Conventions

**Good Test Names:**
```python
# ✅ Descriptive, intention-revealing
def test_calculate_discount_returns_20_percent_off_for_premium_members():
    pass

def test_user_registration_fails_when_email_already_exists():
    pass

def test_order_total_includes_tax_and_shipping():
    pass
```

**Bad Test Names:**
```python
# ❌ Vague, unclear intention
def test_discount():
    pass

def test_user():
    pass

def test_order():
    pass
```

---

### 2. AAA Pattern (Arrange-Act-Assert)

```python
def test_add_item_to_cart():
    # ARRANGE: Set up test data
    cart = ShoppingCart()
    item = Product("Apple", 1.50)

    # ACT: Perform action
    cart.add_item(item)

    # ASSERT: Verify result
    assert cart.item_count() == 1
    assert cart.total_price() == 1.50
```

---

### 3. Test Independence

```python
# ✅ GOOD: Each test is independent
def test_add_item():
    cart = ShoppingCart()  # Fresh cart
    cart.add_item("Apple", 1.50)
    assert cart.item_count() == 1

def test_remove_item():
    cart = ShoppingCart()  # Fresh cart
    cart.add_item("Apple", 1.50)
    cart.remove_item("Apple")
    assert cart.item_count() == 0
```

```python
# ❌ BAD: Tests depend on each other
cart = ShoppingCart()  # Global state!

def test_add_item():
    cart.add_item("Apple", 1.50)
    assert cart.item_count() == 1  # Works

def test_remove_item():
    cart.remove_item("Apple")
    assert cart.item_count() == 0  # Fails if test_add_item didn't run first!
```

---

## CI/CD Integration

### GitHub Actions (Python)

```yaml
# .github/workflows/test.yml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov

      - name: Run tests with coverage
        run: |
          pytest --cov=src --cov-report=xml --cov-report=term

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage.xml
          fail_ci_if_error: true
```

---

### GitLab CI (JavaScript)

```yaml
# .gitlab-ci.yml
test:
  stage: test
  image: node:18
  script:
    - npm ci
    - npm test -- --coverage
  coverage: '/All files[^|]*\|[^|]*\s+([\d\.]+)/'
  artifacts:
    reports:
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

---

## Performance and Load Testing

### Python - locust

**Installation:**
```bash
pip install locust
```

**Load Test Example:**
```python
# locustfile.py
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Wait 1-3 seconds between tasks

    @task(3)  # 3x more frequent than other tasks
    def view_products(self):
        self.client.get("/products")

    @task(1)
    def view_product_detail(self):
        product_id = random.randint(1, 100)
        self.client.get(f"/products/{product_id}")

    @task(1)
    def add_to_cart(self):
        self.client.post("/cart", json={
            "product_id": 42,
            "quantity": 1
        })

    def on_start(self):
        """Login before starting tasks"""
        self.client.post("/login", json={
            "email": "test@example.com",
            "password": "password123"
        })
```

**Run Load Test:**
```bash
# Start Locust web UI
locust -f locustfile.py

# Run headless (1000 users, 100/sec spawn rate, 5 minutes)
locust -f locustfile.py --headless -u 1000 -r 100 -t 5m --host https://example.com
```

---

## Testing Patterns and Anti-Patterns

### ✅ Good Patterns

**1. Test One Thing Per Test**
```python
# ✅ GOOD: Each test has single responsibility
def test_user_registration_creates_user():
    user = register_user("test@example.com", "password")
    assert user.id is not None

def test_user_registration_sends_welcome_email():
    user = register_user("test@example.com", "password")
    assert email_was_sent_to("test@example.com")
```

**2. Use Factories for Test Data**
```python
# factories.py
from factory import Factory, Faker

class UserFactory(Factory):
    class Meta:
        model = User

    email = Faker('email')
    username = Faker('user_name')
    created_at = Faker('date_time')

# Usage in tests
def test_user_can_login():
    user = UserFactory.create(email="test@example.com")
    assert login(user.email, "password") is True
```

---

### ❌ Anti-Patterns

**1. Testing Implementation Instead of Behavior**
```python
# ❌ BAD: Testing private method
def test_internal_calculation():
    cart = ShoppingCart()
    assert cart._calculate_tax(100) == 7.0  # Testing private method!

# ✅ GOOD: Testing public behavior
def test_total_price_includes_tax():
    cart = ShoppingCart()
    cart.add_item("Item", 100)
    assert cart.total_price() == 107.0  # 100 + 7% tax
```

**2. Flaky Tests (Time-Dependent)**
```python
# ❌ BAD: Time-dependent test
def test_session_expires_after_1_hour():
    session = create_session()
    time.sleep(3600)  # Wait 1 hour!
    assert session.is_expired() is True

# ✅ GOOD: Mock time
def test_session_expires_after_1_hour():
    with freeze_time("2024-01-01 12:00:00") as frozen_time:
        session = create_session()
        frozen_time.tick(delta=timedelta(hours=1))
        assert session.is_expired() is True
```

**3. Over-Mocking**
```python
# ❌ BAD: Mocking everything (brittle test)
def test_process_order():
    mock_db = Mock()
    mock_payment = Mock()
    mock_email = Mock()
    mock_inventory = Mock()
    # ... too many mocks!

# ✅ GOOD: Integration test with real database
def test_process_order(test_db):
    order = create_order()
    process_order(order)
    assert test_db.query(Order).filter_by(id=order.id).first().status == "completed"
```

---

## Quick Reference - Testing Commands

### Python (pytest)
```bash
pytest                              # Run all tests
pytest -v                           # Verbose output
pytest -k "test_add"                # Run tests matching pattern
pytest --cov=src --cov-report=html  # Coverage report
pytest -x                           # Stop on first failure
pytest --lf                         # Run last failed tests
pytest --pdb                        # Drop into debugger on failure
```

### JavaScript (Jest)
```bash
npm test                    # Run all tests
npm test -- --watch         # Watch mode
npm test -- --coverage      # Coverage report
npm test -- --verbose       # Verbose output
npm test -- calculator.test # Run specific file
```

### E2E (Cypress)
```bash
npx cypress open            # Open UI
npx cypress run             # Headless
npx cypress run --browser chrome
npx cypress run --spec "cypress/e2e/login.cy.js"
```

### E2E (Playwright)
```bash
npx playwright test                 # Run all tests
npx playwright test --ui            # UI mode
npx playwright test --debug         # Debug mode
npx playwright test --project=chromium
npx playwright show-report          # Show HTML report
```

---

## Summary: Testing Checklist

**Before Committing Code:**
- [ ] All unit tests pass
- [ ] Code coverage ≥ 80%
- [ ] Integration tests pass
- [ ] E2E tests pass (critical flows)
- [ ] No flaky tests
- [ ] Tests are independent
- [ ] Tests are fast (unit < 1s, integration < 10s)
- [ ] Tests follow AAA pattern
- [ ] Tests have clear, descriptive names

**For Production Deployment:**
- [ ] All tests pass in CI/CD
- [ ] Performance tests complete successfully
- [ ] Load tests verify capacity
- [ ] Security tests pass
- [ ] Regression tests complete

---

**Power Level:** Testing mastery + full CODING ULTIMATE STACK = 800/1000 development expertise

---

## 🔧 CODING ULTIMATE STACK: Must Load Together

**This skill is Layer 4: Quality & Testing of THE CODING ULTIMATE STACK system.**

### Same Layer (Quality & Testing - Load All 5):
- `code-quality-standards-skill` - Clean code, SOLID, refactoring, code smells
- `debug-methodology-skill` - Codex systematic debugging, trace execution
- `security-best-practices-skill` - OWASP, authentication, security audit
- `git-safety-skill` - Safe version control, branching strategies

### Next Layer (Deployment & Collaboration - Load 3-5):
- `docker-containerization-skill` - Docker, Kubernetes, container orchestration
- `git-safety-skill` - Safe version control, branching strategies
- `automation-workflows-skill` - Workflow automation, batch processing
- `security-best-practices-skill` - OWASP, authentication, security audit
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
3. **Expert:** Full Layer 4 + all layers → Production-grade code

**Power Level:** This skill + full stack = 800/1000 (maximum development expertise)
