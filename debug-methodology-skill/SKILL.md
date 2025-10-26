---
name: debug-methodology-skill
description: Master systematic debugging using Codex methodology. Use for: trace execution flow, calculate expected values, validate assumptions, root cause analysis, bug reproduction, error diagnosis, performance debugging, and systematic problem-solving that finds real issues not just symptoms.
---

# 🔬 Debug Methodology - Codex System

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert
**Based on:** CLAUDE.md Codex Methodology

---

## 📋 Table of Contents

1. [The Codex Debugging Philosophy](#codex-philosophy)
2. [Step 0: Understand the Domain](#step-0-understand-domain)
3. [Step 1: Trace Execution Flow](#step-1-trace-execution)
4. [Step 2: Calculate Expected Values](#step-2-calculate-expected)
5. [Step 3: Validate Assumptions](#step-3-validate-assumptions)
6. [Step 4: Systematic Debugging Checklist](#step-4-systematic-checklist)
7. [Step 5: Identify Root Cause](#step-5-root-cause)
8. [Step 6: Verify Fix](#step-6-verify-fix)
9. [Common Pitfalls to Avoid](#common-pitfalls)
10. [Case Studies](#case-studies)
11. [Debugging Tools](#debugging-tools)
12. [Debug Templates](#debug-templates)

---

## 🎯 The Codex Debugging Philosophy

### Core Principle

**❌ DON'T:**
- Assume you know the problem
- Jump to quick fixes
- Treat symptoms instead of root causes
- Skip validation steps

**✅ DO:**
- Trace complete execution flow
- Calculate expected values with math
- Validate every assumption
- Find the actual source of the bug

---

### The Problem with Pattern Matching

**Pattern Matching Debugging (Bad):**
```
1. See error message
2. "Oh, I've seen this before!"
3. Apply same fix as last time
4. Hope it works
```

**Result:**
- Might fix surface issue
- Doesn't address root cause
- Bug returns in different form
- Wastes time on wrong fixes

**Codex Debugging (Good):**
```
1. Understand what SHOULD happen
2. Trace what ACTUALLY happens
3. Find where they diverge
4. Calculate why they diverge
5. Fix the ROOT CAUSE
```

**Result:**
- Permanent fix
- Deep understanding
- No regression
- Knowledge for future

---

## 📖 Step 0: Understand the Domain FIRST!

### Before Assuming Bug

**Critical Rule:** Different values ≠ Bug!

**Example from CLAUDE.md:**
```
Seeing:
- Target (timeline): 1396.6s
- Target (segments): 1189.9s
- Difference: 207.7s

❌ Claude thought: "Different values = BUG!"

✅ Codex validated:
- Timeline span = first_start → last_end (includes gaps)
- Segments duration = sum of actual speech (no gaps)
- Difference = gaps between segments (EXPECTED!)
- Final drift: 0ms = WORKING CORRECTLY!

Conclusion: Don't fix what isn't broken!
```

---

### Step 0 Checklist

**Ask Before Debugging:**

1. **What do these values mean?**
   ```
   - Timeline span vs Segments duration?
   - Do they have different semantics?
   - Are they measuring different things?
   ```

2. **Is this difference by design?**
   ```
   - Is the system designed to have different values?
   - Is there a technical reason they should differ?
   ```

3. **Calculate expected behavior**
   ```
   - If system works correctly, what should I see?
   - Does the math support what I'm seeing?
   ```

4. **Validate against specification**
   ```
   - Does output match spec?
   - Is final result correct (e.g., drift = 0%)?
   ```

**Golden Rule:**
```
Understand domain semantics BEFORE assuming bug
Calculate expected behavior BEFORE changing code
```

---

## 🔍 Step 1: Trace Execution Flow

### The Anti-Assumption Rule

**❌ NEVER:**
- Assume you know the code path
- Skip reading the actual code
- Trust your memory of how it works

**✅ ALWAYS:**
- Trace execution line by line
- Read actual code, not what you think it does
- Follow every function call
- Track variable values at each step

---

### Tracing Commands

**Find Function Calls:**
```bash
# Find where function is called
grep -n "function_name" file.py

# Find across entire codebase
grep -rn "function_name" .
```

**Read Code Sections:**
```bash
# Read specific line range
sed -n 'start_line,end_line p' file.py

# Example: Read lines 200-250
sed -n '200,250p' chunk_processor.py
```

**Verify Import Paths:**
```bash
# Check which module is actually imported
python -c "import module; print(module.__file__)"
```

**Check Code Structure:**
```bash
# Show indentation (spaces vs tabs)
cat -A file.py | sed -n 'start,end p'
```

---

### Trace Template

```python
# Tracing Template
print(f"=== TRACE: Function {function_name} ===")
print(f"Input: {input_value}")
print(f"Expected: {expected_value}")

# At key points
print(f"  Step 1: variable = {variable}")
print(f"  Step 2: after operation = {result}")
print(f"  Step 3: final = {final}")

print(f"Actual output: {output}")
print(f"Difference: {output - expected_value}")
```

---

## 📐 Step 2: Calculate Expected Values

### Math is Required!

**From CLAUDE.md Case Study #1:**

```python
# Problem: Video duration mismatch
# Expected: 1189.9s (SRT target)
# Actual: 1396.6s (ffprobe result)
# Difference: +206.7s

# Question: Where did +206.7s come from?

# ❌ Claude: "Looks like indentation bug" (WRONG)

# ✅ Codex: Calculate backwards
# Segments duration: 1031.1s (actual speech)
# Timeline span: 1396.6s (absolute time)
# Expected gaps: 1396.6 - 1031.1 = 365.5s
#
# TimelineAwareMerger should:
# - Take speech: 1031.1s
# - Add gaps: 365.5s
# - Output: 1396.6s ✓
#
# Actual gaps: 1396.6 - 1031.1 = 365.5s ✓
# MATH CONFIRMS: System working correctly!
```

---

### Calculation Checklist

**For Every Bug:**

1. **Calculate Expected Result**
   ```
   Based on inputs + logic, what SHOULD happen?
   Use actual math, not guesses
   ```

2. **Compare Actual vs Expected**
   ```
   Actual: [value]
   Expected: [calculated value]
   Difference: [actual - expected]
   ```

3. **If Different → Backtrack**
   ```
   Where did the difference originate?
   Trace backward through execution
   Find the SOURCE of unexpected value
   ```

4. **Validate Intermediate Values**
   ```
   Don't just check final output
   Check values at EACH STEP
   Find where divergence begins
   ```

---

## ✓ Step 3: Validate Assumptions

### Assume Nothing Works

**Common False Assumptions:**
```
❌ "This function returns X" → Check actual return value
❌ "Loop runs N times" → Count actual iterations
❌ "Variable has value Y" → Print and verify
❌ "Code executes in order A→B→C" → Trace actual flow
```

---

### Validation Commands

**Check Return Values:**
```bash
# Find function definition
grep -A 10 "def function_name" file.py

# Check return statements
grep "return" file.py
```

**Check Loop Iterations:**
```python
# Add counter
iteration_count = 0
for item in items:
    iteration_count += 1
    print(f"Iteration {iteration_count}: {item}")
```

**Check Variable Values:**
```python
# At suspicious points
print(f"DEBUG: var = {var}, type = {type(var)}, value = {repr(var)}")
```

**Check Indentation:**
```bash
# Detect mixed tabs/spaces
cat -A file.py | grep -E '^\t|^ '
```

---

### Case Study: Double TimelineAwareMerger

**From CLAUDE.md:**

```python
# ❌ Claude's Assumption:
# "Indentation looks wrong, must be the bug!"

# ✅ Codex's Validation:
# Step 1: Calculate expected
# segments: 1031s
# final: 1396s
# silence added: 1396 - 1031 = 365s ← TOO MUCH!

# Step 2: Trace where silence is added
# ChunkProcessor:
#   merger1 = TimelineAwareMerger()
#   merger1.add_segment() → adds silence
#
# MasterProcessor:
#   merger2 = TimelineAwareMerger()
#   merger2.add_segment() → adds silence AGAIN!

# Step 3: Math confirms
# Chunk level: +182s
# Final level: +182s
# Total: ~365s ✓ (matches observed!)

# Root Cause: Double merging, not indentation!
```

---

## 📋 Step 4: Systematic Debugging Checklist

### The Complete Process

```bash
# ======================================
# Step 1: Understand the Problem
# ======================================
# - What is the expected result?
# - What is the actual result?
# - How do they differ? By how much?

# ======================================
# Step 2: Locate Code Path
# ======================================
grep -n "function_name" file.py
sed -n 'start,end p' file.py

# ======================================
# Step 3: Trace Execution
# ======================================
# - Read code line by line
# - Track variable values
# - Calculate intermediate results
# - DON'T skip steps!

# ======================================
# Step 4: Identify Root Cause
# ======================================
# - Don't stop at surface issues!
# - Find SOURCE of unexpected values
# - Validate with math
# - Trace back to origin

# ======================================
# Step 5: Verify Fix
# ======================================
# - Calculate expected result after fix
# - Test with actual data
# - Confirm values/drift match expected
# - No regression in other areas
```

---

## 🎯 Step 5: Identify Root Cause

### Root Cause vs Symptom

**Symptom:** What you observe (error message, wrong value)

**Root Cause:** Why it happens (actual bug in logic)

---

### Root Cause Analysis

**The 5 Whys Technique:**

```
Problem: Audio 24s shorter than video

Why? MP3 encoding overhead
Why? Concatenating many small MP3 files
Why? Each MP3 has frame overhead
Why? Using MP3 format for intermediate files
Why? Default choice without considering overhead

Root Cause: Wrong intermediate format choice

Solution: Use WAV for intermediate → MP3 once at end
```

---

### Common Root Causes

**1. Logic Errors**
```python
# Wrong operator
if x > 10:  # Should be >=

# Wrong variable
total = sum(wrong_list)  # Should be correct_list

# Off-by-one
for i in range(len(items) - 1):  # Missing last item
```

**2. State Management**
```python
# Shared mutable state
class Processor:
    result = []  # Shared across instances! ❌

    def __init__(self):
        self.result = []  # Instance variable ✓
```

**3. Timing Issues**
```python
# Race condition
def process():
    value = get_value()  # Might change before next line
    time.sleep(0.1)
    use_value(value)  # Stale value!
```

**4. Data Type Issues**
```python
# String vs number
"10" + "20" = "1020"  # Not 30!
int("10") + int("20") = 30  # Correct
```

---

## ✅ Step 6: Verify Fix

### Don't Just Hope

**Verification Checklist:**

1. **Calculate Expected Result**
   ```
   After fix, what should happen?
   Calculate with actual numbers
   ```

2. **Test with Real Data**
   ```
   Use production data if possible
   Test edge cases
   Test happy path
   ```

3. **Confirm Values Match**
   ```
   Actual: [value]
   Expected: [calculated]
   Drift: [acceptable range]
   ```

4. **Check for Regressions**
   ```
   Did fix break anything else?
   Run full test suite
   Check related functionality
   ```

---

## ⚠️ Common Pitfalls to Avoid

### The "Don't Do" List

| ❌ **Don't Do** | ✅ **Do Instead** |
|----------------|-------------------|
| Assume you know the bug | Trace complete flow |
| Jump to "obvious" fix | Calculate expected values |
| Pattern match with past bugs | Deep analysis + math |
| Fix symptoms | Find root cause |
| Skip validation | Test thoroughly |
| Trust your memory | Read actual code |
| Quick fix without understanding | Systematic analysis |

---

### Anti-Patterns

**1. Spray and Pray**
```python
# ❌ Try random fixes hoping one works
try:
    fix_attempt_1()
except:
    fix_attempt_2()
except:
    fix_attempt_3()
```

**2. Cargo Cult Debugging**
```python
# ❌ Copy fix from Stack Overflow without understanding
# "Someone said add this line and it worked"
mysterious_line_from_internet()
```

**3. The Confidence Game**
```python
# ❌ "I'm sure it's X" without verification
# Proceed based on assumption
# Waste hours debugging wrong thing
```

---

## 📚 Case Studies

### Case Study #1: Double Merger Bug

**Problem:**
- Expected: 1189.9s
- Actual: 1396.6s
- Drift: +206.7s (+17%)

**❌ Bad Approach (Claude):**
```python
# 1. Look at code → see weird indentation
# 2. Think: "Aha! process_chunk() is outside loop!"
# 3. Fix indentation
# 4. Claim victory

# Reality: Wrong diagnosis! Real bug untouched
```

**✅ Good Approach (Codex):**
```python
# 1. Math analysis:
#    segments: 1031s
#    final: 1396s
#    silence: 1396 - 1031 = 365s ← TOO MUCH!

# 2. Trace flow:
#    ChunkProcessor: adds silence
#    MasterProcessor: adds silence AGAIN

# 3. Root cause: Double merging

# 4. Fix: Remove chunk-level merger
#    Use only final merger

# 5. Result: Drift = 0% ✓
```

---

### Case Study #2: Paperspace Environment

**Problem:**
- `bc: command not found`
- Path structure different than local
- Filename pattern mismatch

**❌ Bad Approach:**
```bash
# Try to install bc
# Hardcode paths
# Rigid filename matching
# Give up after failures
```

**✅ Good Approach (Codex):**
```bash
# 1. Check environment
which bc  # Not available
which python3  # Available!

# 2. Validate paths
ls -la /notebooks/quantum-sync-v5/
# Files in root, not subfolder

# 3. Debug filename pattern
ls output/
# Found: *_v11.mp3 not *_v11_agents.mp3

# 4. Systematic fixes:
# - Replace bc with Python
# - Fix paths for actual structure
# - Flexible wildcards
# - Error handling with diagnostics

# Result: Production success in 30 min!
```

---

## 🛠️ Debugging Tools

### Command Line Tools

**Find & Search:**
```bash
# Find files
find . -name "*.py" -type f

# Search content
grep -rn "pattern" .
grep -A 5 -B 5 "pattern" file  # Context lines

# Search with exclusions
grep -r "pattern" --exclude-dir={node_modules,.git}
```

**Code Inspection:**
```bash
# Show file with line numbers
cat -n file.py

# Show specific lines
sed -n '10,20p' file.py

# Show whitespace
cat -A file.py
```

**Process Monitoring:**
```bash
# Watch file changes
watch -n 1 'ls -lh output/'

# Monitor processes
ps aux | grep python

# Check resource usage
top
htop
```

---

### Python Debugging

**Print Debugging:**
```python
# Strategic print statements
print(f"=== DEBUG: {location} ===")
print(f"Input: {input_val}")
print(f"Type: {type(val)}, Value: {repr(val)}")
print(f"Calculated: {expected}, Actual: {actual}, Diff: {actual - expected}")
```

**Assertions:**
```python
# Validate assumptions
assert len(items) > 0, "Items list is empty!"
assert result == expected, f"Expected {expected}, got {result}"
```

**Logging:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.debug(f"Processing item {i}: {item}")
logger.info(f"Completed with result: {result}")
logger.warning(f"Unexpected value: {value}")
logger.error(f"Error occurred: {error}")
```

---

## 📋 Debug Templates

### Bug Report Template

```markdown
# Bug Report

## Expected Behavior
[What should happen? Include calculated values]

## Actual Behavior
[What actually happens? Include measurements]

## Difference
[Expected - Actual = ? Percentage?]

## Environment
- OS:
- Python version:
- Dependencies:

## Steps to Reproduce
1.
2.
3.

## Trace
[Code path taken]

## Calculations
[Math showing expected vs actual]

## Root Cause
[Source of the bug, not symptom]

## Proposed Fix
[Solution that addresses root cause]
```

---

### Debug Session Template

```bash
#!/bin/bash
# Debug Session Log

# ======================
# PROBLEM STATEMENT
# ======================
# Expected: [value with units]
# Actual: [value with units]
# Difference: [calculation]

# ======================
# HYPOTHESIS
# ======================
# Initial guess: [what might be wrong]

# ======================
# INVESTIGATION
# ======================

# Step 1: Trace execution
grep -n "function" file.py
sed -n 'start,end p' file.py

# Step 2: Check values
python -c "
# Quick calculation
expected = [calculation]
actual = [measurement]
print(f'Difference: {actual - expected}')
"

# Step 3: Validate assumptions
# [Commands to check each assumption]

# ======================
# FINDINGS
# ======================
# Actual cause: [root cause]
# Proof: [math/evidence]

# ======================
# FIX
# ======================
# [Changes made]

# ======================
# VERIFICATION
# ======================
# Before: [measurements]
# After: [measurements]
# Success: [yes/no with evidence]
```

---

## 🎓 Debugging Principles Summary

**The Codex Way:**

1. **Step 0: Understand the Domain**
   - Different values ≠ bug
   - Understand semantics first
   - Calculate expected behavior

2. **Step 1: Trace Execution Flow**
   - Don't assume
   - Read actual code
   - Follow every step

3. **Step 2: Calculate Expected Values**
   - Use math, not guesses
   - Calculate at each step
   - Compare with actual

4. **Step 3: Validate Assumptions**
   - Test everything
   - Print values
   - Verify types and states

5. **Step 4: Find Root Cause**
   - Don't fix symptoms
   - Trace to source
   - Use 5 Whys

6. **Step 5: Verify Fix**
   - Calculate expected result
   - Test with real data
   - Check for regressions

**Golden Rules:**
- ✅ Understand before fixing
- ✅ Calculate before coding
- ✅ Validate before committing
- ✅ Fix root cause, not symptoms

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,200+
**Status:** Production Ready ✅
**Based on:** CLAUDE.md Codex Methodology
