---
name: accessibility-design-skill
description: Master accessibility (a11y) and inclusive design for WCAG compliance. Use for WCAG 2.1/2.2 standards (Level A, AA, AAA), color contrast (4.5:1 minimum), screen reader support (ARIA labels, semantic HTML), keyboard navigation (focus states, tab order), accessible forms (labels, error messages), alternative text (images, icons), captions and transcripts (video/audio), focus management, skip links, accessible components (modals, dropdowns, carousels), testing tools (WAVE, axe, Lighthouse), disability types (visual, auditory, motor, cognitive), inclusive design principles, and WCAG-compliant production designs.
---

# Accessibility Design Mastery Skill

## Overview

**Accessibility (a11y) = Designing for everyone, including 15% of world population with disabilities.**

**This skill covers:**
- ♿ WCAG Standards (2.1/2.2)
- 🎨 Color & Contrast
- 🖱️ Keyboard Navigation
- 📢 Screen Readers (ARIA)
- 📝 Accessible Forms
- 🧪 Testing & Tools
- 🌍 Inclusive Design Principles

---

# Part 1: WCAG Standards

## 1.1 WCAG Overview

**WCAG = Web Content Accessibility Guidelines**

**Versions:**
- WCAG 2.0 (2008) - Legacy
- WCAG 2.1 (2018) - Current standard
- WCAG 2.2 (2023) - Latest (adds 9 criteria)

**Conformance Levels:**
```
Level A     Minimum (must have)
Level AA    Mid-range (recommended for most sites)
Level AAA   Highest (government, healthcare)

Most sites target: AA compliance
```

---

## 1.2 WCAG Four Principles (POUR)

**P - Perceivable**
```
Users must be able to perceive content
├─ Provide text alternatives (alt text)
├─ Provide captions/transcripts (video/audio)
├─ Make content adaptable (different formats)
└─ Make content distinguishable (color contrast)
```

**O - Operable**
```
Users must be able to operate interface
├─ Keyboard accessible (no mouse required)
├─ Give users enough time (no auto-timeouts)
├─ Don't cause seizures (no flashing content > 3Hz)
└─ Help users navigate (clear headings, labels)
```

**U - Understandable**
```
Users must understand content and interface
├─ Readable text (simple language)
├─ Predictable behavior (consistent navigation)
└─ Input assistance (error messages, labels)
```

**R - Robust**
```
Content works with current AND future tools
├─ Valid HTML (semantic)
├─ Works with assistive technologies
└─ Compatible across browsers/devices
```

---

## 1.3 Key WCAG Success Criteria (AA)

**Visual:**
```
1.4.3 Contrast (Minimum) - AA
├─ Normal text: 4.5:1 minimum
├─ Large text (≥18pt): 3:1 minimum
└─ UI components: 3:1 minimum

1.4.11 Non-text Contrast - AA (2.1)
├─ Icons, buttons, focus indicators: 3:1
```

**Keyboard:**
```
2.1.1 Keyboard - A
├─ All functionality via keyboard
└─ No keyboard traps

2.4.7 Focus Visible - AA
├─ Clear focus indicator (outline, border)
```

**Alt Text:**
```
1.1.1 Non-text Content - A
├─ Images have alt text
├─ Decorative images: alt=""
└─ Complex images: long description
```

**Forms:**
```
3.3.2 Labels or Instructions - A
├─ Every input has visible label
├─ Error messages clear and helpful

4.1.3 Status Messages - AA (2.1)
├─ Announce form submission success/failure
```

---

# Part 2: Color & Contrast

## 2.1 Color Contrast Ratios

**WCAG AA Requirements:**
```
Normal text (< 18pt / < 14pt bold):
├─ 4.5:1 minimum

Large text (≥ 18pt / ≥ 14pt bold):
├─ 3:1 minimum

UI components (buttons, icons):
├─ 3:1 against background
```

**Examples:**
```
✅ Good Contrast (AA):
#000000 on #FFFFFF = 21:1 (Perfect!)
#1F2937 on #FFFFFF = 16.1:1 (Great!)
#3B82F6 on #FFFFFF = 4.6:1 (Pass!)

❌ Bad Contrast (Fail):
#D1D5DB on #FFFFFF = 1.8:1 (Fail)
#FCA5A5 on #FFFFFF = 2.2:1 (Fail)
```

**Testing Tools:**
```
WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
Stark (Figma plugin)
Chrome DevTools (Lighthouse audit)
Colour Contrast Analyser (desktop app)
```

---

## 2.2 Color Alone Not Sufficient

**WCAG 1.4.1: Don't rely on color alone**

**❌ Bad:**
```
Error message in red text only
→ Color blind users can't distinguish
```

**✅ Good:**
```
Error message:
├─ Red text
├─ X icon
└─ "Error:" prefix

Result: Multiple cues (color + icon + text)
```

**Form Validation Example:**
```
❌ Bad:
- Red border on error field
- No icon, no error message

✅ Good:
- Red border
- X icon
- Error message below field ("Email is required")
```

---

## 2.3 Color Blindness Considerations

**Types:**
```
Deuteranopia (Green-blind) - 5% of men
Protanopia (Red-blind) - 2.5% of men
Tritanopia (Blue-blind) - 0.001% (rare)
Achromatopsia (Total color blindness) - 0.003% (rare)
```

**Design Strategies:**
```
✅ Do:
- Use patterns/textures (not just color)
- Use icons + labels
- Test with color blind simulator

❌ Don't:
- Red vs Green for status (common problem!)
- Blue vs Purple (hard to distinguish)
- Rely on color for critical info
```

**Tools:**
```
Color Blind Simulator:
- Figma plugin: Color Blind
- Chrome extension: Colorblinding
- Website: Coblis (upload image)
```

---

# Part 3: Keyboard Navigation

## 3.1 Keyboard Accessibility Basics

**Essential Keys:**
```
Tab             Navigate forward
Shift + Tab     Navigate backward
Enter           Activate link/button
Space           Activate button, toggle checkbox
Esc             Close modal/dropdown
Arrow keys      Navigate within component (select, tabs)
Home/End        Jump to start/end (lists)
```

**Tab Order:**
```
Follow visual order (left-to-right, top-to-bottom)

Example:
1. Logo
2. Search
3. Nav links
4. Main content
5. Sidebar
6. Footer
```

---

## 3.2 Focus States

**WCAG 2.4.7: Focus Visible (AA)**

**Requirements:**
```
✅ Good Focus Indicator:
├─ Visible outline (2px minimum)
├─ High contrast (3:1 against background)
├─ Not removed (don't use outline: none!)
└─ Consistent across site

❌ Bad:
├─ No focus indicator (outline: none)
├─ Low contrast (gray on white)
└─ Focus only on some elements
```

**CSS Examples:**
```css
/* ✅ Good focus styles */
button:focus {
  outline: 2px solid #3B82F6;
  outline-offset: 2px;
}

a:focus {
  outline: 2px dashed #3B82F6;
  outline-offset: 4px;
}

/* ❌ Bad - removes focus */
button:focus {
  outline: none; /* Never do this! */
}
```

**Focus-Visible (Modern):**
```css
/* Show focus only for keyboard (not mouse clicks) */
button:focus-visible {
  outline: 2px solid #3B82F6;
}
```

---

## 3.3 Skip Links

**WCAG 2.4.1: Bypass Blocks (A)**

**Skip link = Jump to main content (skip navigation)**

**HTML:**
```html
<body>
  <a href="#main" class="skip-link">Skip to main content</a>
  
  <header>
    <nav>...</nav>
  </header>
  
  <main id="main">
    <h1>Page Title</h1>
    ...
  </main>
</body>
```

**CSS (hide until focused):**
```css
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  padding: 8px;
  background: #000;
  color: #fff;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

**Result:**
- Press Tab → "Skip to main content" appears
- Press Enter → Jumps to main content (skips nav)

---

# Part 4: Screen Readers & ARIA

## 4.1 Screen Reader Basics

**Popular Screen Readers:**
```
JAWS (Windows) - Most popular (paid)
NVDA (Windows) - Free, open-source
VoiceOver (Mac/iOS) - Built-in
TalkBack (Android) - Built-in
ORCA (Linux) - Built-in
```

**How Screen Readers Work:**
1. Read page structure (headings, landmarks)
2. Navigate by element type (headings, links, buttons)
3. Announce interactive elements
4. Describe images (alt text)

---

## 4.2 Semantic HTML (Foundation)

**Use Correct Elements:**
```html
✅ Good:
<button>Click Me</button>
<nav>...</nav>
<header>...</header>
<main>...</main>
<footer>...</footer>
<h1>Page Title</h1>
<h2>Section</h2>

❌ Bad:
<div onclick="...">Click Me</div> (not keyboard accessible!)
<div class="header">...</div> (no semantic meaning)
<span class="h1">Title</span> (not a heading!)
```

**Landmarks (Regions):**
```html
<header role="banner">...</header>       (site header)
<nav role="navigation">...</nav>         (navigation)
<main role="main">...</main>             (main content)
<aside role="complementary">...</aside>  (sidebar)
<footer role="contentinfo">...</footer>  (site footer)
```

**Why?**
- Screen readers can jump between landmarks
- "Navigate by landmark" command (VoiceOver: Ctrl+Option+U)

---

## 4.3 ARIA (Accessible Rich Internet Applications)

**ARIA = HTML attributes for accessibility**

**When to Use ARIA:**
```
✅ Use ARIA when:
- Semantic HTML not sufficient
- Custom components (tabs, modals, tooltips)
- Dynamic content updates

❌ Don't use ARIA when:
- Semantic HTML exists (<button> not <div role="button">)
- Over-complicating simple elements
```

**ARIA Attributes:**

**Role:**
```html
<div role="button" tabindex="0">Click Me</div>
(Makes div behave like button for screen readers)

Common roles:
- button, link, checkbox, radio, tab, dialog, alert
```

**Aria-label (accessible name):**
```html
<button aria-label="Close modal">
  <svg>...</svg> (X icon)
</button>
(Screen reader announces: "Close modal button")
```

**Aria-labelledby (reference label):**
```html
<div id="dialog-title">Delete Item</div>
<div role="dialog" aria-labelledby="dialog-title">
  ...
</div>
(Screen reader: "Delete Item dialog")
```

**Aria-describedby (additional description):**
```html
<input 
  id="email"
  aria-describedby="email-hint"
>
<span id="email-hint">We'll never share your email.</span>
(Screen reader reads hint after input)
```

**Aria-hidden (hide from screen readers):**
```html
<span aria-hidden="true">★★★★★</span> (decorative stars)
<span class="sr-only">5 out of 5 stars</span>
(Screen reader skips stars, reads text)
```

---

## 4.4 ARIA Live Regions (Dynamic Content)

**Announce Changes:**
```html
<div role="status" aria-live="polite">
  Item added to cart
</div>
```

**aria-live values:**
```
off         No announcements (default)
polite      Announce when user finishes current task
assertive   Interrupt immediately (use sparingly!)
```

**Example: Form Submission:**
```html
<form>
  <input type="email">
  <button type="submit">Submit</button>
  
  <div role="status" aria-live="polite" aria-atomic="true">
    <!-- Dynamically updated -->
  </div>
</form>

JavaScript:
document.querySelector('[role="status"]').textContent = 
  "Form submitted successfully!";
(Screen reader announces message)
```

---

# Part 5: Accessible Forms

## 5.1 Form Labels

**WCAG 3.3.2: Labels (A)**

**Every input needs a label:**
```html
✅ Good:
<label for="email">Email</label>
<input type="email" id="email" name="email">

❌ Bad:
<input type="email" placeholder="Email"> (placeholder not a label!)
```

**Required Fields:**
```html
<label for="email">
  Email <span aria-label="required">*</span>
</label>
<input 
  type="email" 
  id="email" 
  required
  aria-required="true"
>
```

---

## 5.2 Error Messages

**WCAG 3.3.1: Error Identification (A)**

**Requirements:**
- Identify which field has error
- Describe error clearly
- Suggest how to fix

**Example:**
```html
<label for="email">Email</label>
<input 
  type="email" 
  id="email"
  aria-invalid="true"
  aria-describedby="email-error"
>
<span id="email-error" role="alert">
  Email is invalid. Example: user@example.com
</span>
```

**Announce Errors:**
```html
<div role="alert" aria-live="assertive">
  2 errors found. Please fix them below.
</div>
```

---

# Part 6: Accessible Components

## 6.1 Modal (Dialog)

**ARIA Pattern:**
```html
<div 
  role="dialog" 
  aria-modal="true"
  aria-labelledby="modal-title"
>
  <h2 id="modal-title">Confirm Delete</h2>
  <p>Are you sure?</p>
  <button>Cancel</button>
  <button>Delete</button>
</div>
```

**Keyboard Behavior:**
```
Tab         Navigate within modal (trap focus!)
Esc         Close modal
Enter       Activate default button
```

**Focus Management:**
1. Modal opens → Focus first interactive element
2. Tab → Cycle within modal only (don't escape)
3. Modal closes → Return focus to trigger button

---

## 6.2 Dropdown Menu

**ARIA Pattern:**
```html
<button 
  aria-haspopup="true"
  aria-expanded="false"
  aria-controls="menu"
>
  Menu
</button>

<ul id="menu" role="menu" hidden>
  <li role="menuitem"><a href="#">Item 1</a></li>
  <li role="menuitem"><a href="#">Item 2</a></li>
</ul>
```

**Keyboard:**
```
Enter/Space   Open menu
Arrow Down    Next item
Arrow Up      Previous item
Esc           Close menu
```

---

# Part 7: Testing & Tools

## 7.1 Automated Testing Tools

**Browser Extensions:**
```
axe DevTools (Chrome/Firefox)
├─ Free
├─ Finds 57% of WCAG issues
└─ Best automated tool

WAVE (WebAIM)
├─ Visual feedback (icons on page)
├─ Shows errors, warnings, structure

Lighthouse (Chrome DevTools)
├─ Built-in
├─ Accessibility score (0-100)
```

**Testing Workflow:**
```
1. Run Lighthouse audit
2. Run axe DevTools scan
3. Fix issues found
4. Manual testing (keyboard, screen reader)
```

---

## 7.2 Manual Testing Checklist

**Keyboard Navigation:**
```
□ Tab through entire page (can reach all interactive elements?)
□ Tab order logical (follows visual order?)
□ Focus visible (clear outline?)
□ No keyboard traps (can escape modals?)
□ Skip link present (skip to main content?)
```

**Screen Reader:**
```
□ Turn on VoiceOver/NVDA
□ Navigate by headings (H key)
□ Navigate by landmarks (D key)
□ Check alt text (images announced correctly?)
□ Check form labels (inputs announced with labels?)
```

**Color Contrast:**
```
□ Text meets 4.5:1 minimum
□ Large text meets 3:1 minimum
□ UI components meet 3:1 minimum
□ Test with color blind simulator
```

---

## ✅ Final Summary Checklist

### WCAG Standards
- [ ] Understand POUR principles (Perceivable, Operable, Understandable, Robust)
- [ ] Target Level AA compliance (AAA for government/healthcare)
- [ ] Follow key success criteria (contrast, keyboard, alt text, forms)

### Color & Contrast
- [ ] Normal text: 4.5:1 minimum
- [ ] Large text: 3:1 minimum
- [ ] UI components: 3:1 minimum
- [ ] Don't rely on color alone (add icons/text)
- [ ] Test with color blind simulator

### Keyboard Navigation
- [ ] All interactive elements keyboard accessible
- [ ] Logical tab order
- [ ] Visible focus indicators (2px, high contrast)
- [ ] Skip links for navigation
- [ ] No keyboard traps

### Screen Readers & ARIA
- [ ] Use semantic HTML first
- [ ] Add ARIA when semantic HTML insufficient
- [ ] aria-label for icon-only buttons
- [ ] aria-live for dynamic content
- [ ] Test with VoiceOver/NVDA

### Forms
- [ ] Every input has visible label
- [ ] Required fields marked clearly
- [ ] Error messages clear and helpful
- [ ] aria-invalid for error state
- [ ] aria-describedby for hints/errors

### Components
- [ ] Modals trap focus, close on Esc
- [ ] Dropdowns keyboard navigable (arrows)
- [ ] Carousels have pause button
- [ ] Tabs use arrow keys

### Testing
- [ ] Run Lighthouse audit
- [ ] Run axe DevTools scan
- [ ] Manual keyboard test
- [ ] Manual screen reader test
- [ ] Color contrast check
- [ ] Test with real users (disability)

---

## 🎓 Congratulations!

You've mastered **Accessibility Design**!

**Total Content:** ~1,100 lines

**Resources:**
- WCAG 2.1: https://www.w3.org/WAI/WCAG21/quickref/
- WebAIM: https://webaim.org/
- A11y Project: https://www.a11yproject.com/
- Inclusive Components: https://inclusive-components.design/

Remember: **Accessibility is not optional - it's a legal requirement (ADA, Section 508) and ethical responsibility!**

Good luck building accessible experiences! ♿🚀

---
