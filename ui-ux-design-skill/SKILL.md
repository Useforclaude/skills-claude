---
name: ui-ux-design-skill
description: Master UI/UX design principles and user-centered design. Use for: user research, personas, user flows, wireframing, prototyping, usability testing, information architecture, visual hierarchy, Gestalt principles, Fitts's Law, Hick's Law, accessibility (WCAG), mobile-first design, responsive layouts, and creating intuitive, user-friendly interfaces.. Also use for Thai keywords "UI", "ส่วนติดต่อผู้ใช้", "หน้าจอ", "อินเทอร์เฟซ", "UX", "ประสบการณ์ผู้ใช้", "การใช้งาน", "ใช้งานง่าย", "ออกแบบ", "ดีไซน์", "การออกแบบ", "design"
---

# 🎨 UI/UX Design Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [UX Design Fundamentals](#ux-design-fundamentals)
2. [User Research](#user-research)
3. [Information Architecture](#information-architecture)
4. [Wireframing & Prototyping](#wireframing-prototyping)
5. [UI Design Principles](#ui-design-principles)
6. [Visual Hierarchy](#visual-hierarchy)
7. [Psychology & Laws](#psychology-laws)
8. [Accessibility](#accessibility)
9. [Responsive Design](#responsive-design)
10. [Usability Testing](#usability-testing)

---

## 🎯 UX Design Fundamentals

### What is UX Design?

**User Experience (UX):** The overall experience a user has with a product.

**UX vs UI:**
```
UX (User Experience)
├── User research
├── Information architecture
├── User flows
├── Wireframing
└── Usability testing

UI (User Interface)
├── Visual design
├── Colors & typography
├── Icons & imagery
├── Animations
└── Style guides
```

**UX is how it works. UI is how it looks.**

---

### The UX Design Process

**5 Stages:**

```
1. Research
   ↓ Understand users & problems
2. Define
   ↓ Synthesize insights, define problems
3. Ideate
   ↓ Brainstorm solutions
4. Prototype
   ↓ Build interactive mockups
5. Test
   ↓ Validate with real users
   (Iterate & repeat)
```

---

### Design Thinking

**5 Phases (Stanford d.school):**

1. **Empathize** - Understand users
2. **Define** - Frame the problem
3. **Ideate** - Generate ideas
4. **Prototype** - Build solutions
5. **Test** - Get feedback

**Key Principle:** User-centered, iterative, fail fast.

---

## 👥 User Research

### Research Methods

**Qualitative (Why):**
- User interviews
- Contextual inquiry (observe in context)
- Usability testing
- Focus groups

**Quantitative (What/How many):**
- Surveys & questionnaires
- Analytics (Google Analytics, Hotjar)
- A/B testing
- Card sorting

---

### User Personas

**Template:**
```
Name: Sarah Johnson
Age: 32
Occupation: Marketing Manager

Photo: [headshot]

Bio:
- Lives in San Francisco
- Works at tech startup
- Manages team of 5

Goals:
- Track campaign performance
- Generate reports quickly
- Collaborate with team

Frustrations:
- Too many tools
- Manual data entry
- Slow dashboards

Quote:
"I need insights fast, not hours of digging through data."

Tech Savviness: ███████░░░ (7/10)
```

**Example Persona:**
```markdown
# Sarah - The Busy Manager

**Demographics:**
- 32 years old
- Marketing Manager
- $80K salary
- Lives in SF

**Behaviors:**
- Checks phone 50+ times/day
- Uses Slack, Asana, Google Analytics
- Prefers mobile for quick tasks

**Goals:**
- Save time on reporting
- Make data-driven decisions
- Stay ahead of trends

**Pain Points:**
- Data scattered across tools
- Slow loading dashboards
- Difficult to share insights

**How we help:**
- Unified dashboard
- Real-time updates
- One-click sharing
```

---

### User Journey Map

```
Stage:     Awareness → Consideration → Purchase → Onboarding → Usage → Support

Actions:   Google search → Read reviews → Sign up → Tutorial → Create project → Contact help
           Visit site      Compare         Enter card    Watch video   Invite team      Email

Thoughts:  "Need solution" → "Is it worth it?" → "Hope it's easy" → "Looks complex" → "This works!" → "Stuck here"

Emotions:  😐 Neutral → 🤔 Curious → 😰 Anxious → 😕 Confused → 😊 Happy → 😤 Frustrated

Pain:      ❌ Hard to find → ❌ Expensive → ❌ Long form → ❌ Too much info → ✅ Smooth → ❌ No answer

Improve:   Better SEO → Free trial → Simplify → Progressive → Great! → Chatbot
```

---

## 📐 Information Architecture

### Site Map

```
Homepage
├── Products
│   ├── Product A
│   ├── Product B
│   └── Product C
├── Solutions
│   ├── For Marketing
│   ├── For Sales
│   └── For Support
├── Pricing
├── Resources
│   ├── Blog
│   ├── Guides
│   ├── Webinars
│   └── Case Studies
└── About
    ├── Team
    ├── Careers
    └── Contact
```

---

### Card Sorting

**Open Card Sorting:**
- Users group items into categories they create
- Discover natural mental models

**Closed Card Sorting:**
- Users sort items into predefined categories
- Validate existing structure

**Example:**
```
Given: 30 product feature cards
Task: Group them into categories that make sense

Results:
- "Analytics" category: 8 cards (80% agreement)
- "Collaboration" category: 6 cards (65% agreement)
- "Settings" category: 4 cards (90% agreement)
```

---

### User Flows

**Login Flow:**
```
[Start] → [Enter email] → Email valid?
                             ↓ No → [Show error] → [Enter email]
                             ↓ Yes
                          [Enter password] → Correct?
                             ↓ No → [Show error + "Forgot?"] → [Enter password]
                             ↓ Yes
                          [Dashboard]
```

**Checkout Flow:**
```
[Cart] → [Shipping info] → [Payment] → [Review] → [Confirm] → [Success]
   ↑                                       ↓
   └────────── Edit cart ─────────────────┘
```

---

## ✏️ Wireframing & Prototyping

### Fidelity Levels

**Low-Fidelity (Lo-Fi):**
- Sketches or basic shapes
- No colors/images
- Focus on structure
- Fast iteration

**Mid-Fidelity:**
- Grayscale wireframes
- Realistic layout
- Placeholder content
- Test flows

**High-Fidelity (Hi-Fi):**
- Full visual design
- Real content
- Interactions
- Final look & feel

---

### Wireframe Example (Text)

```
┌──────────────────────────────────────┐
│  [Logo]        Nav1  Nav2  Nav3  [🔍] │
├──────────────────────────────────────┤
│                                       │
│        ┌─────────────────────┐       │
│        │                     │       │
│        │    Hero Image       │       │
│        │                     │       │
│        └─────────────────────┘       │
│                                       │
│     Headline Goes Here               │
│     Subheadline with more detail     │
│                                       │
│     [Primary CTA]  [Secondary CTA]   │
│                                       │
├──────────────────────────────────────┤
│  Feature 1  │  Feature 2  │ Feature 3│
│  [Icon]     │  [Icon]     │  [Icon]  │
│  Description│  Description│ Descriptn│
├──────────────────────────────────────┤
│  © 2025 Company | Privacy | Terms    │
└──────────────────────────────────────┘
```

---

### Prototyping Tools

**Figma** (Recommended)
- Free for individuals
- Collaborative
- Auto layout
- Components

**Adobe XD**
- Auto-animate
- Voice prototyping
- Repeat grids

**Sketch**
- Mac only
- Plugins ecosystem
- Symbols & overrides

**Axure**
- Advanced interactions
- Conditional logic
- Documentation

---

## 🎨 UI Design Principles

### Gestalt Principles

**1. Proximity**
```
Items close together = Related

○ ○     ○ ○
○ ○     ○ ○
  ↑       ↑
Group A  Group B
```

**2. Similarity**
```
Similar items = Related

● ● ● ○ ○ ○
● ● ● ○ ○ ○
  ↑     ↑
 Group  Group
```

**3. Closure**
```
Brain completes incomplete shapes

  ___
 /   \    → Seen as circle
 \___/      even if incomplete
```

**4. Continuity**
```
Eye follows paths

A ───────→ B
    ↓
    C

Eye naturally follows A→B, not A→C
```

**5. Figure/Ground**
```
Distinguish foreground from background

Example: Rubin's vase (face or vase?)
```

---

### White Space

**Macro White Space:**
- Between major sections
- Page margins
- Gutters

**Micro White Space:**
- Between lines (line-height)
- Between letters (letter-spacing)
- Padding inside elements

**Benefits:**
- ✅ Improves readability
- ✅ Creates focus
- ✅ Looks premium
- ✅ Reduces cognitive load

---

### Consistency

**Visual Consistency:**
- Same button styles
- Same colors for actions
- Same spacing grid

**Functional Consistency:**
- Same icon means same action
- Same gesture does same thing
- Same position (logo top-left)

**External Consistency:**
- Follow platform conventions (iOS, Android)
- Use familiar patterns (hamburger menu)

---

## 👁️ Visual Hierarchy

### Size & Scale

```
Headline          ← Largest (48px)

Subheadline       ← Large (24px)

Body text         ← Medium (16px)

Caption           ← Small (12px)
```

**Typographic Scale:** 1.25 ratio
```
12px → 15px → 18px → 24px → 30px → 36px → 48px
```

---

### Color & Contrast

**High Contrast = Important:**
```
██████  BLACK on WHITE  ← Primary action
██████  GRAY on WHITE   ← Secondary action
██████  LIGHT on WHITE  ← Disabled
```

**Example:**
```html
<button class="primary">Sign Up</button>  <!-- High contrast -->
<button class="secondary">Learn More</button>  <!-- Medium contrast -->
<button class="tertiary">Skip</button>  <!-- Low contrast -->
```

---

### Weight & Emphasis

```
Bold = Important
Regular = Normal
Light = Less important

Heavy ━━━ Primary heading
Medium ─── Subheading
Light ··· Caption
```

---

### Position & Layout

**F-Pattern (Reading):**
```
Users scan in F-shape:

█████████████        ← Horizontal scan
█████
█████████            ← Horizontal scan
█████
███                  ← Vertical scan
```

**Z-Pattern (Visual Flow):**
```
Logo ──────────→ CTA    ← Top left to top right
  ↓              ↗
Content ──────────→     ← Diagonal to bottom left, then right
```

**Visual Weight:**
- Top-left = Highest priority
- Bottom-right = Lowest priority

---

## 🧠 Psychology & Laws

### Fitts's Law

**Formula:** Time = a + b × log₂(Distance/Size + 1)

**Principle:** Larger, closer targets = Faster to click

**Applications:**
```
✅ DO:
- Large buttons (min 44×44px for touch)
- Place primary CTA in path of thumb (mobile)
- Common actions close together

❌ DON'T:
- Tiny clickable areas
- Important buttons in corners
- Spread related actions far apart
```

---

### Hick's Law

**Formula:** Time = b × log₂(n + 1)

**Principle:** More choices = Longer decision time

**Applications:**
```
✅ DO:
- Limit menu items (5-7)
- Progressive disclosure
- Categorize options

❌ DON'T:
- 20 navigation items
- Show all options at once
- Overwhelm with choices
```

**Example:**
```
❌ Bad: 15 pricing plans
✅ Good: 3 pricing plans (Starter, Pro, Enterprise)
```

---

### Miller's Law

**Principle:** Average person can hold 7±2 items in working memory

**Applications:**
```
✅ DO:
- Chunk information into groups
- Phone: (555) 123-4567 (not 5551234567)
- Lists of 5-9 items

❌ DON'T:
- Long lists without grouping
- 20-step forms without progress
```

---

### Jakob's Law

**Principle:** Users prefer your site to work like other sites they know

**Applications:**
```
✅ DO:
- Logo top-left
- Search top-right
- Shopping cart icon top-right
- Footer for legal/social

❌ DON'T:
- Reinvent common patterns
- Unexpected navigation
- Unconventional icons
```

---

### Von Restorff Effect

**Principle:** Items that stand out are remembered better

**Applications:**
```
✅ DO:
- Make CTA visually distinct
- Highlight errors in red
- Use color for important items

Example:
[ Learn More ]  [ Learn More ]  [✓ Sign Up ]
                                     ↑
                               Stands out!
```

---

## ♿ Accessibility

### WCAG 2.1 Principles

**POUR:**

**Perceivable:**
- Alt text for images
- Captions for videos
- Color is not sole indicator

**Operable:**
- Keyboard accessible
- Enough time to interact
- No flashing content

**Understandable:**
- Clear language
- Predictable navigation
- Input assistance

**Robust:**
- Compatible with assistive tech
- Valid HTML/ARIA

---

### Color Contrast

**WCAG AA (minimum):**
- 4.5:1 for normal text
- 3:1 for large text (18pt+)
- 3:1 for UI components

**WCAG AAA (enhanced):**
- 7:1 for normal text
- 4.5:1 for large text

**Tool:** https://contrast-ratio.com

**Examples:**
```
✅ PASS: #2196F3 on #FFFFFF (5.88:1)
❌ FAIL: #FFEB3B on #FFFFFF (1.09:1)
```

---

### Keyboard Navigation

```html
<!-- Tab order -->
<input tabindex="1">  <!-- First -->
<button tabindex="2">  <!-- Second -->
<a href="#" tabindex="-1">  <!-- Skip (not in tab order) -->

<!-- Focus visible -->
<style>
  button:focus {
    outline: 2px solid blue;
    outline-offset: 2px;
  }
</style>

<!-- Skip to content -->
<a href="#main-content" class="skip-link">
  Skip to main content
</a>
```

---

### ARIA (Accessible Rich Internet Applications)

```html
<!-- Landmarks -->
<header role="banner">
<nav role="navigation" aria-label="Main">
<main role="main" id="main-content">
<aside role="complementary">
<footer role="contentinfo">

<!-- Labels -->
<button aria-label="Close dialog">×</button>

<!-- States -->
<button aria-pressed="true">Bold</button>
<div aria-expanded="false">Menu</div>

<!-- Live regions -->
<div aria-live="polite">  <!-- Announce when changed -->
  3 new messages
</div>
```

---

## 📱 Responsive Design

### Mobile-First Approach

```css
/* Mobile (default) */
.container {
  padding: 16px;
}

/* Tablet (768px+) */
@media (min-width: 768px) {
  .container {
    padding: 24px;
  }
}

/* Desktop (1024px+) */
@media (min-width: 1024px) {
  .container {
    padding: 32px;
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

---

### Breakpoints

**Common Breakpoints:**
```
320px   → Mobile S (iPhone SE)
375px   → Mobile M (iPhone 12)
425px   → Mobile L (iPhone 12 Pro Max)
768px   → Tablet
1024px  → Laptop
1440px  → Desktop
2560px  → 4K
```

---

### Touch Targets

**Minimum Sizes:**
```
Apple:    44 × 44 px
Android:  48 × 48 px
WCAG:     44 × 44 px

✅ Good:
┌──────────┐
│  Button  │  (48px tall)
└──────────┘

❌ Bad:
[Button]  (20px tall - too small!)
```

---

### Responsive Typography

```css
/* Fluid typography */
html {
  font-size: 16px;  /* Base */
}

h1 {
  font-size: clamp(2rem, 5vw, 3rem);
  /*         ↑ min  ↑ scale ↑ max */
}

@media (min-width: 768px) {
  html {
    font-size: 18px;  /* Larger base on tablet */
  }
}
```

---

## 🧪 Usability Testing

### Test Methods

**Moderated Testing:**
- In-person or remote
- Observer guides user
- Ask questions, probe deeper

**Unmoderated Testing:**
- User completes tasks alone
- Recorded for later review
- Scalable, faster

---

### Test Plan

**Template:**
```markdown
# Usability Test Plan

## Goals
- Test checkout flow
- Identify pain points
- Validate navigation

## Participants
- 5-8 users
- Target persona: Busy professionals
- Recruited via UserTesting.com

## Tasks
1. Find and add product to cart (2 min)
2. Complete checkout (5 min)
3. Find help/support (1 min)

## Metrics
- Task completion rate
- Time on task
- Error rate
- Satisfaction (1-5 scale)

## Success Criteria
- 80%+ completion rate
- Avg time < 5 min
- Satisfaction > 4/5
```

---

### Think-Aloud Protocol

**Instructions to user:**
```
"As you complete tasks, please say out loud what you're:
- Thinking
- Looking for
- Trying to do
- Confused about

There are no wrong answers. We're testing the design, not you."
```

**Example:**
```
User: "Okay, I need to find pricing... I'll look in the top menu...
       I see Products, Solutions... hmm, no Pricing.
       Maybe under Products?
       Oh wait, there it is in the footer.
       That's a weird place for pricing..."

→ Insight: Pricing should be in main nav!
```

---

### Metrics

**Quantitative:**
- **Task success rate:** % who completed
- **Time on task:** Avg seconds
- **Error rate:** # of errors
- **Clicks to complete:** # of clicks

**Qualitative:**
- **Satisfaction:** 1-5 scale
- **Ease of use:** SUS (System Usability Scale)
- **NPS:** Net Promoter Score
- **Quotes:** Memorable feedback

---

### A/B Testing

**Example:**
```
Test: Button color

Version A (Control):
[Blue Button] → 5% click rate

Version B (Variant):
[Green Button] → 7% click rate

Result: Green wins! (+40% lift)
```

**Tools:**
- Google Optimize
- Optimizely
- VWO

---

## ✅ Best Practices Checklist

**UX:**
- [ ] User research conducted
- [ ] Personas created
- [ ] User flows mapped
- [ ] Wireframes tested
- [ ] Usability testing done

**UI:**
- [ ] Visual hierarchy clear
- [ ] Consistent spacing (8px grid)
- [ ] Color contrast WCAG AA+
- [ ] Typography scale applied
- [ ] Responsive on all devices

**Accessibility:**
- [ ] Keyboard navigable
- [ ] Screen reader compatible
- [ ] Focus states visible
- [ ] ARIA labels where needed
- [ ] Color not sole indicator

**Performance:**
- [ ] Fast load time (<3s)
- [ ] Smooth animations (60fps)
- [ ] Optimized images
- [ ] Mobile-friendly

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,500+
**Status:** Production Ready ✅
