---
name: python-best-practices-skill
description: Master Python best practices and idioms. Use for: PEP 8 style guide, Pythonic code patterns, list comprehensions, generators, context managers, decorators, type hints, virtual environments, package management, and writing clean professional Python code.. Also use for Thai keywords "Python", "ไพธอน", "เขียน Python", "โปรแกรม Python", "เขียนโค้ด", "โปรแกรม", "พัฒนา", "coding", "programming"
---

# 🐍 Python Best Practices Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [PEP 8 Style Guide](#pep-8-style-guide)
2. [Pythonic Idioms](#pythonic-idioms)
3. [Data Structures](#data-structures)
4. [Functions & Arguments](#functions-arguments)
5. [Classes & Objects](#classes-objects)
6. [Type Hints](#type-hints)
7. [Error Handling](#error-handling)
8. [File & Context Managers](#file-context-managers)
9. [Virtual Environments](#virtual-environments)
10. [Common Patterns](#common-patterns)

---

## 📏 PEP 8 Style Guide

### Naming Conventions

```python
# Variables & Functions: snake_case
user_name = "John"
def calculate_total():
    pass

# Constants: SCREAMING_SNAKE_CASE
MAX_RETRIES = 3
API_KEY = "secret"

# Classes: PascalCase
class UserManager:
    pass

# Private: prefix with _
_internal_variable = 42
def _private_method():
    pass

# Really private: prefix with __
class MyClass:
    def __init__(self):
        self.__private = "secret"
```

---

### Indentation & Spacing

```python
# ✅ 4 spaces per indentation level
def example():
    if condition:
        do_something()

# ✅ Blank lines
class MyClass:  # 2 blank lines before class

    def method_one(self):
        pass

    def method_two(self):  # 1 blank line between methods
        pass


def function():  # 2 blank lines before function
    pass

# ✅ Whitespace around operators
x = 1 + 2
result = x * (y + z)

# ✅ No trailing whitespace
name = "John"  # comment (2 spaces before #)
```

---

### Line Length

```python
# ✅ Max 79 characters per line

# Long function arguments - vertical alignment
result = some_function(
    very_long_argument_name_one,
    very_long_argument_name_two,
    very_long_argument_name_three
)

# Or hanging indent
result = some_function(
    very_long_argument_name_one, very_long_argument_name_two,
    very_long_argument_name_three
)

# Long strings
message = (
    "This is a very long string that "
    "spans multiple lines for better "
    "readability"
)
```

---

## 🐍 Pythonic Idioms

### List Comprehensions

```python
# ❌ Not Pythonic
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)

# ✅ Pythonic - List comprehension
squares = [n ** 2 for n in numbers]

# With condition
evens = [n for n in numbers if n % 2 == 0]

# Nested
matrix = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Dict comprehension
word_lengths = {word: len(word) for word in ['hello', 'world']}
# {'hello': 5, 'world': 5}

# Set comprehension
unique_lengths = {len(word) for word in words}
```

---

### Enumerate & Zip

```python
# ❌ Not Pythonic
names = ['Alice', 'Bob', 'Charlie']
for i in range(len(names)):
    print(f"{i}: {names[i]}")

# ✅ Pythonic - enumerate
for i, name in enumerate(names):
    print(f"{i}: {name}")

# With custom start
for i, name in enumerate(names, start=1):
    print(f"{i}: {name}")

# ❌ Not Pythonic
names = ['Alice', 'Bob']
ages = [25, 30]
for i in range(len(names)):
    print(f"{names[i]} is {ages[i]}")

# ✅ Pythonic - zip
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Unzip
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
# numbers = (1, 2, 3), letters = ('a', 'b', 'c')
```

---

### Unpacking

```python
# ✅ Multiple assignment
x, y = 1, 2
x, y = y, x  # Swap

# ✅ Extended unpacking
first, *middle, last = [1, 2, 3, 4, 5]
# first = 1, middle = [2, 3, 4], last = 5

# ✅ Ignore values with _
name, _, age = ("John", "middle", 30)

# ✅ Function arguments
def greet(name, age):
    print(f"{name} is {age}")

data = {"name": "John", "age": 30}
greet(**data)  # Unpack dict as kwargs
```

---

### Truthiness

```python
# ✅ Use implicit boolean conversion
if users:  # Instead of: if len(users) > 0
    print("Has users")

if not name:  # Instead of: if name == ""
    print("No name")

# ✅ is vs ==
if x is None:  # Not: if x == None
    pass

if x is True:  # For singleton comparisons
    pass
```

---

## 📊 Data Structures

### Default Dict

```python
from collections import defaultdict

# ❌ Verbose
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# ✅ defaultdict
word_count = defaultdict(int)
for word in words:
    word_count[word] += 1
```

---

### Named Tuples

```python
from collections import namedtuple

# ❌ Regular tuple (hard to remember order)
user = ("John", 30, "john@example.com")
name = user[0]  # What is index 0?

# ✅ namedtuple (self-documenting)
User = namedtuple('User', ['name', 'age', 'email'])
user = User("John", 30, "john@example.com")
name = user.name  # Clear!
```

---

### Dataclasses (Python 3.7+)

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str
    active: bool = True  # Default value

user = User("John", 30, "john@example.com")
print(user.name)  # John

# Immutable dataclass
@dataclass(frozen=True)
class ImmutableUser:
    name: str
    age: int
```

---

## ⚙️ Functions & Arguments

### Default Arguments

```python
# ❌ Dangerous! Mutable default
def add_item(item, items=[]):
    items.append(item)
    return items

list1 = add_item(1)  # [1]
list2 = add_item(2)  # [1, 2] - Shared list!

# ✅ Correct - Use None
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

### *args and **kwargs

```python
def example(*args, **kwargs):
    # args = tuple of positional arguments
    # kwargs = dict of keyword arguments
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

example(1, 2, 3, name="John", age=30)
# Positional: (1, 2, 3)
# Keyword: {'name': 'John', 'age': 30}

# Unpacking
def greet(name, age):
    print(f"{name} is {age}")

args = ["John", 30]
greet(*args)  # Unpack list as positional args

kwargs = {"name": "John", "age": 30}
greet(**kwargs)  # Unpack dict as keyword args
```

---

### Keyword-Only Arguments

```python
# Force keyword arguments (after *)
def create_user(name, *, age, email):
    pass

# Must call with keywords
create_user("John", age=30, email="john@example.com")
# create_user("John", 30, "john@example.com")  # Error!
```

---

## 🏛️ Classes & Objects

### Properties

```python
class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """Getter"""
        return self._name

    @name.setter
    def name(self, value):
        """Setter with validation"""
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def display_name(self):
        """Read-only property"""
        return f"User: {self._name}"

# Usage
user = User("John")
print(user.name)  # Calls getter
user.name = "Jane"  # Calls setter
print(user.display_name)  # Read-only
```

---

### Magic Methods

```python
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        """String representation for users"""
        return f"${self.amount:.2f}"

    def __repr__(self):
        """String representation for developers"""
        return f"Money({self.amount})"

    def __add__(self, other):
        """+ operator"""
        return Money(self.amount + other.amount)

    def __eq__(self, other):
        """== operator"""
        return self.amount == other.amount

    def __lt__(self, other):
        """< operator"""
        return self.amount < other.amount

# Usage
m1 = Money(10)
m2 = Money(20)
print(m1 + m2)  # $30.00
print(m1 < m2)  # True
```

---

## 🔤 Type Hints

```python
from typing import List, Dict, Optional, Union, Callable

# Basic types
def greet(name: str) -> str:
    return f"Hello, {name}"

# Collections
def process_users(users: List[str]) -> Dict[str, int]:
    return {user: len(user) for user in users}

# Optional (can be None)
def find_user(id: int) -> Optional[str]:
    return user_db.get(id)  # May return None

# Union (multiple types)
def process(data: Union[str, int]) -> str:
    return str(data)

# Callable
def apply(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# Type aliases
UserId = int
UserData = Dict[str, Union[str, int]]

def get_user(user_id: UserId) -> UserData:
    return {"name": "John", "age": 30}
```

---

## 🚨 Error Handling

### Exceptions

```python
# ✅ Specific exceptions
try:
    result = risky_operation()
except ValueError as e:
    print(f"Invalid value: {e}")
except KeyError as e:
    print(f"Missing key: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    cleanup()

# ✅ Custom exceptions
class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

def validate_age(age):
    if age < 0:
        raise ValidationError("Age cannot be negative")

# ✅ EAFP (Easier to Ask Forgiveness than Permission)
try:
    value = dictionary[key]
except KeyError:
    value = default

# ❌ LBYL (Look Before You Leap) - Not Pythonic
if key in dictionary:
    value = dictionary[key]
else:
    value = default
```

---

## 📁 File & Context Managers

### with Statement

```python
# ✅ Automatic file closing
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed

# ❌ Manual closing (error-prone)
f = open('file.txt', 'r')
content = f.read()
f.close()  # Might not be reached if error occurs

# Multiple context managers
with open('input.txt', 'r') as f_in, \
     open('output.txt', 'w') as f_out:
    f_out.write(f_in.read())
```

---

### Custom Context Manager

```python
from contextlib import contextmanager

@contextmanager
def timer(name):
    import time
    start = time.time()
    yield
    end = time.time()
    print(f"{name} took {end - start:.2f}s")

# Usage
with timer("Database query"):
    # Code to time
    result = db.query()
```

---

## 🐍 Virtual Environments

### Creating & Using

```bash
# Create virtual environment
python -m venv venv

# Activate
source venv/bin/activate  # Unix/Mac
venv\Scripts\activate     # Windows

# Install packages
pip install requests numpy

# Save dependencies
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt

# Deactivate
deactivate
```

---

### requirements.txt

```txt
# requirements.txt
requests==2.28.0
numpy>=1.21.0,<2.0.0
flask~=2.0.0  # Compatible release
```

---

## 🎯 Common Patterns

### Singleton Pattern

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

### Decorators

```python
from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"

# Decorator with arguments
def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}")
```

---

### Generators

```python
# ✅ Memory efficient
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(10):
    print(num)

# Generator expression (like list comprehension)
squares = (x**2 for x in range(10))
```

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,400+
**Status:** Production Ready ✅

---

## 🔧 CODING ULTIMATE STACK: Must Load Together

**This skill is Layer 3: Implementation of THE CODING ULTIMATE STACK system.**

### Same Layer (Implementation - Load All 8):
- `javascript-modern-skill` - ES6+, async/await, modern JS
- `code-quality-standards-skill` - Clean code, SOLID, refactoring, code smells
- `automation-workflows-skill` - Workflow automation, batch processing
- `document-conversion-skill` - MD → PDF, HTML → PDF, Pandoc
- `odoo-development-skill` - ERP development, Odoo customization
- `excel-expert-skill` - Data manipulation, advanced Excel
- `ffmpeg-video-processing-skill` - Video processing pipelines

### Next Layer (Quality & Testing - Load 3-5):
- `code-quality-standards-skill` - Clean code, SOLID, refactoring, code smells
- `debug-methodology-skill` - Codex systematic debugging, trace execution
- `security-best-practices-skill` - OWASP, authentication, security audit
- `git-safety-skill` - Safe version control, branching strategies

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
3. **Expert:** Full Layer 3 + all layers → Production-grade code

**Power Level:** This skill + full stack = 800/1000 (maximum development expertise)
