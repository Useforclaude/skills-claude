---
name: design-systems-skill
description: Master design system creation and maintenance for scalable, consistent UIs. Use for: design tokens (colors, typography, spacing), component libraries, documentation (Storybook), atomic design methodology, accessibility standards, design-dev handoff, version control for design, brand guidelines, and building production-ready design systems that scale across teams and products. Also use for Thai keywords "ระบบดีไซน์", "design system", "design token", "สี", "ฟอนต์", "ระยะห่าง", "คอมโพเนนต์", "component library", "Storybook", "atomic design", "มาตรฐานการออกแบบ", "ส่งงานให้โปรแกรมเมอร์", "design handoff", "brand guideline", "แนวทางแบรนด์", "ระบบออกแบบที่ขยายได้", "ความสอดคล้อง", "UI สอดคล้อง".
---

# 🎨 Design Systems Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [Design System Fundamentals](#design-system-fundamentals)
2. [Design Tokens](#design-tokens)
3. [Typography System](#typography-system)
4. [Color System](#color-system)
5. [Spacing & Layout](#spacing-layout)
6. [Component Library](#component-library)
7. [Atomic Design](#atomic-design)
8. [Documentation](#documentation)
9. [Accessibility](#accessibility)
10. [Tooling & Workflow](#tooling-workflow)

---

## 🎯 Design System Fundamentals

### What is a Design System?

**Definition:** A collection of reusable components, guided by clear standards, that can be assembled to build applications.

**Components:**
```
Design System
├── Design Tokens (variables)
├── Component Library (UI building blocks)
├── Documentation (how to use)
├── Guidelines (principles & patterns)
└── Tools (Figma, Storybook, etc.)
```

---

### Why Design Systems?

**Benefits:**
- ✅ **Consistency** - Same look across products
- ✅ **Speed** - Reuse components, build faster
- ✅ **Scalability** - Easy to maintain & grow
- ✅ **Collaboration** - Shared language for design & dev
- ✅ **Quality** - Pre-tested, accessible components

---

### Famous Design Systems

**Material Design** (Google)
- Comprehensive, opinionated
- https://material.io

**Human Interface Guidelines** (Apple)
- iOS/macOS design principles
- https://developer.apple.com/design/

**Carbon** (IBM)
- Enterprise-focused
- https://carbondesignsystem.com

**Ant Design** (Ant Financial)
- React components
- https://ant.design

**Polaris** (Shopify)
- E-commerce focused
- https://polaris.shopify.com

---

## 🎨 Design Tokens

### What are Design Tokens?

**Definition:** Named variables that store design decisions (colors, spacing, etc.).

**Benefits:**
- Single source of truth
- Easy to update globally
- Platform-agnostic
- Design-dev sync

---

### Token Structure

**tokens.json:**
```json
{
  "color": {
    "primary": {
      "50": { "value": "#E3F2FD" },
      "100": { "value": "#BBDEFB" },
      "500": { "value": "#2196F3" },
      "900": { "value": "#0D47A1" }
    },
    "text": {
      "primary": { "value": "#212121" },
      "secondary": { "value": "#757575" },
      "disabled": { "value": "#BDBDBD" }
    }
  },
  "spacing": {
    "xs": { "value": "4px" },
    "sm": { "value": "8px" },
    "md": { "value": "16px" },
    "lg": { "value": "24px" },
    "xl": { "value": "32px" }
  },
  "fontSize": {
    "xs": { "value": "12px" },
    "sm": { "value": "14px" },
    "md": { "value": "16px" },
    "lg": { "value": "20px" },
    "xl": { "value": "24px" }
  },
  "borderRadius": {
    "sm": { "value": "4px" },
    "md": { "value": "8px" },
    "lg": { "value": "16px" },
    "full": { "value": "9999px" }
  },
  "shadow": {
    "sm": { "value": "0 1px 2px rgba(0,0,0,0.05)" },
    "md": { "value": "0 4px 6px rgba(0,0,0,0.1)" },
    "lg": { "value": "0 10px 15px rgba(0,0,0,0.1)" }
  }
}
```

---

### CSS Variables (Implementation)

**styles/tokens.css:**
```css
:root {
  /* Colors */
  --color-primary-50: #E3F2FD;
  --color-primary-500: #2196F3;
  --color-primary-900: #0D47A1;

  --color-text-primary: #212121;
  --color-text-secondary: #757575;

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;

  /* Typography */
  --font-size-xs: 12px;
  --font-size-sm: 14px;
  --font-size-md: 16px;
  --font-size-lg: 20px;

  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-bold: 700;

  /* Border */
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-full: 9999px;

  /* Shadow */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
}

/* Usage */
.button {
  background: var(--color-primary-500);
  color: white;
  padding: var(--spacing-sm) var(--spacing-md);
  border-radius: var(--border-radius-md);
  font-size: var(--font-size-md);
  box-shadow: var(--shadow-sm);
}
```

---

### JavaScript Tokens

**tokens.js:**
```javascript
export const tokens = {
  color: {
    primary: {
      50: '#E3F2FD',
      500: '#2196F3',
      900: '#0D47A1'
    },
    text: {
      primary: '#212121',
      secondary: '#757575'
    }
  },
  spacing: {
    xs: 4,
    sm: 8,
    md: 16,
    lg: 24,
    xl: 32
  },
  fontSize: {
    xs: 12,
    sm: 14,
    md: 16,
    lg: 20,
    xl: 24
  }
};

// Usage (Styled Components)
import styled from 'styled-components';
import { tokens } from './tokens';

const Button = styled.button`
  background: ${tokens.color.primary[500]};
  padding: ${tokens.spacing.sm}px ${tokens.spacing.md}px;
  font-size: ${tokens.fontSize.md}px;
`;
```

---

## 📝 Typography System

### Type Scale

**Modular Scale (1.25 ratio):**
```css
:root {
  --font-size-xs: 12px;    /* 12 */
  --font-size-sm: 14px;    /* 14 */
  --font-size-md: 16px;    /* 16 (base) */
  --font-size-lg: 20px;    /* 16 × 1.25 */
  --font-size-xl: 24px;    /* 20 × 1.2 */
  --font-size-2xl: 30px;   /* 24 × 1.25 */
  --font-size-3xl: 36px;   /* 30 × 1.2 */
  --font-size-4xl: 48px;   /* 36 × 1.33 */
}
```

---

### Font Families

```css
:root {
  /* Primary (body text) */
  --font-family-primary: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;

  /* Secondary (headings) */
  --font-family-secondary: 'Georgia', serif;

  /* Monospace (code) */
  --font-family-mono: 'Fira Code', 'Courier New', monospace;
}
```

---

### Font Weights

```css
:root {
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
}
```

---

### Typography Components

```css
/* Headings */
h1 {
  font-size: var(--font-size-4xl);
  font-weight: var(--font-weight-bold);
  line-height: 1.2;
  margin-bottom: var(--spacing-md);
}

h2 {
  font-size: var(--font-size-3xl);
  font-weight: var(--font-weight-bold);
  line-height: 1.3;
}

h3 {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-semibold);
}

/* Body text */
p {
  font-size: var(--font-size-md);
  line-height: 1.6;
  margin-bottom: var(--spacing-md);
}

/* Small text */
.text-sm {
  font-size: var(--font-size-sm);
}

/* Lead text (intro paragraphs) */
.lead {
  font-size: var(--font-size-lg);
  line-height: 1.8;
}
```

---

## 🎨 Color System

### Color Palette Structure

**Primary Color Scale:**
```css
:root {
  --color-primary-50: #E3F2FD;   /* Lightest */
  --color-primary-100: #BBDEFB;
  --color-primary-200: #90CAF9;
  --color-primary-300: #64B5F6;
  --color-primary-400: #42A5F5;
  --color-primary-500: #2196F3;  /* Base */
  --color-primary-600: #1E88E5;
  --color-primary-700: #1976D2;
  --color-primary-800: #1565C0;
  --color-primary-900: #0D47A1;  /* Darkest */
}
```

---

### Semantic Colors

```css
:root {
  /* State colors */
  --color-success: #10B981;  /* Green */
  --color-warning: #F59E0B;  /* Orange */
  --color-error: #EF4444;    /* Red */
  --color-info: #3B82F6;     /* Blue */

  /* Neutral colors */
  --color-gray-50: #F9FAFB;
  --color-gray-100: #F3F4F6;
  --color-gray-500: #6B7280;
  --color-gray-900: #111827;

  /* Text colors */
  --color-text-primary: var(--color-gray-900);
  --color-text-secondary: var(--color-gray-500);
  --color-text-disabled: var(--color-gray-400);

  /* Background colors */
  --color-bg-primary: #FFFFFF;
  --color-bg-secondary: var(--color-gray-50);
  --color-bg-tertiary: var(--color-gray-100);

  /* Border colors */
  --color-border-light: var(--color-gray-200);
  --color-border-medium: var(--color-gray-300);
  --color-border-dark: var(--color-gray-400);
}
```

---

### Dark Mode

```css
:root {
  --color-bg-primary: #FFFFFF;
  --color-text-primary: #111827;
}

[data-theme="dark"] {
  --color-bg-primary: #111827;
  --color-text-primary: #F9FAFB;
}

/* Usage */
body {
  background: var(--color-bg-primary);
  color: var(--color-text-primary);
}
```

---

## 📐 Spacing & Layout

### Spacing Scale (8px Grid)

```css
:root {
  --spacing-0: 0;
  --spacing-1: 4px;    /* 0.5 × 8 */
  --spacing-2: 8px;    /* 1 × 8 */
  --spacing-3: 12px;   /* 1.5 × 8 */
  --spacing-4: 16px;   /* 2 × 8 */
  --spacing-5: 20px;   /* 2.5 × 8 */
  --spacing-6: 24px;   /* 3 × 8 */
  --spacing-8: 32px;   /* 4 × 8 */
  --spacing-10: 40px;  /* 5 × 8 */
  --spacing-12: 48px;  /* 6 × 8 */
  --spacing-16: 64px;  /* 8 × 8 */
}
```

---

### Layout Grid

```css
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 var(--spacing-4);
}

.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--spacing-4);
}

.col-4 {
  grid-column: span 4;
}

.col-6 {
  grid-column: span 6;
}
```

---

## 🧩 Component Library

### Button Component

```jsx
// Button.jsx
import './Button.css';

function Button({
  variant = 'primary',  // primary | secondary | outline
  size = 'md',          // sm | md | lg
  children,
  ...props
}) {
  return (
    <button
      className={`button button--${variant} button--${size}`}
      {...props}
    >
      {children}
    </button>
  );
}

export default Button;
```

**Button.css:**
```css
.button {
  /* Base styles */
  border: none;
  border-radius: var(--border-radius-md);
  font-weight: var(--font-weight-medium);
  cursor: pointer;
  transition: all 0.2s;
  font-family: var(--font-family-primary);
}

/* Sizes */
.button--sm {
  padding: var(--spacing-1) var(--spacing-3);
  font-size: var(--font-size-sm);
}

.button--md {
  padding: var(--spacing-2) var(--spacing-4);
  font-size: var(--font-size-md);
}

.button--lg {
  padding: var(--spacing-3) var(--spacing-6);
  font-size: var(--font-size-lg);
}

/* Variants */
.button--primary {
  background: var(--color-primary-500);
  color: white;
}

.button--primary:hover {
  background: var(--color-primary-600);
}

.button--secondary {
  background: var(--color-gray-200);
  color: var(--color-text-primary);
}

.button--outline {
  background: transparent;
  border: 2px solid var(--color-primary-500);
  color: var(--color-primary-500);
}
```

---

### Input Component

```jsx
// Input.jsx
function Input({
  label,
  error,
  helperText,
  ...props
}) {
  return (
    <div className="input-wrapper">
      {label && <label className="input-label">{label}</label>}
      <input
        className={`input ${error ? 'input--error' : ''}`}
        {...props}
      />
      {error && <span className="input-error">{error}</span>}
      {helperText && <span className="input-helper">{helperText}</span>}
    </div>
  );
}
```

**Input.css:**
```css
.input-wrapper {
  margin-bottom: var(--spacing-4);
}

.input-label {
  display: block;
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-medium);
  margin-bottom: var(--spacing-1);
  color: var(--color-text-primary);
}

.input {
  width: 100%;
  padding: var(--spacing-2) var(--spacing-3);
  border: 2px solid var(--color-border-medium);
  border-radius: var(--border-radius-md);
  font-size: var(--font-size-md);
  transition: border-color 0.2s;
}

.input:focus {
  outline: none;
  border-color: var(--color-primary-500);
}

.input--error {
  border-color: var(--color-error);
}

.input-error {
  display: block;
  color: var(--color-error);
  font-size: var(--font-size-sm);
  margin-top: var(--spacing-1);
}

.input-helper {
  display: block;
  color: var(--color-text-secondary);
  font-size: var(--font-size-sm);
  margin-top: var(--spacing-1);
}
```

---

## ⚛️ Atomic Design

### Methodology

**5 Levels:**

1. **Atoms** - Basic building blocks (buttons, inputs, labels)
2. **Molecules** - Simple groups of atoms (form field with label + input)
3. **Organisms** - Complex components (header with logo + nav + search)
4. **Templates** - Page layouts (wireframes)
5. **Pages** - Specific instances (homepage, about page)

---

### File Structure

```
src/
├── atoms/
│   ├── Button/
│   │   ├── Button.jsx
│   │   ├── Button.css
│   │   └── Button.test.jsx
│   ├── Input/
│   └── Label/
├── molecules/
│   ├── FormField/  # Label + Input + Error
│   ├── Card/
│   └── SearchBox/
├── organisms/
│   ├── Header/
│   ├── Footer/
│   └── Sidebar/
├── templates/
│   ├── MainLayout/
│   └── DashboardLayout/
└── pages/
    ├── HomePage/
    └── AboutPage/
```

---

## 📚 Documentation

### Storybook Setup

```bash
# Install Storybook
npx storybook@latest init

# Run Storybook
npm run storybook
```

---

### Component Story

**Button.stories.jsx:**
```jsx
import Button from './Button';

export default {
  title: 'Atoms/Button',
  component: Button,
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'outline']
    },
    size: {
      control: 'select',
      options: ['sm', 'md', 'lg']
    }
  }
};

// Default story
export const Primary = {
  args: {
    children: 'Button',
    variant: 'primary',
    size: 'md'
  }
};

// Variants
export const Secondary = {
  args: {
    ...Primary.args,
    variant: 'secondary'
  }
};

export const Outline = {
  args: {
    ...Primary.args,
    variant: 'outline'
  }
};

// Sizes
export const Small = {
  args: {
    ...Primary.args,
    size: 'sm'
  }
};

export const Large = {
  args: {
    ...Primary.args,
    size: 'lg'
  }
};
```

---

### MDX Documentation

**Button.mdx:**
```mdx
import { Canvas, Meta, Story } from '@storybook/blocks';
import * as ButtonStories from './Button.stories';

<Meta of={ButtonStories} />

# Button

Buttons allow users to perform actions with a single tap.

## Usage

<Canvas of={ButtonStories.Primary} />

## Variants

### Primary
Use for main actions.

<Canvas of={ButtonStories.Primary} />

### Secondary
Use for secondary actions.

<Canvas of={ButtonStories.Secondary} />

### Outline
Use for tertiary actions.

<Canvas of={ButtonStories.Outline} />

## Sizes

<Canvas of={ButtonStories.Small} />
<Canvas of={ButtonStories.Large} />

## Accessibility

- Keyboard accessible (focus, enter/space)
- Screen reader support
- Color contrast WCAG AA compliant
```

---

## ♿ Accessibility

### WCAG 2.1 Standards

**Level A (minimum):**
- Text alternatives for images
- Keyboard accessible
- Color not sole indicator

**Level AA (recommended):**
- 4.5:1 contrast ratio (text)
- 3:1 contrast ratio (UI components)
- Resize text to 200%

**Level AAA (enhanced):**
- 7:1 contrast ratio
- No time limits
- No flashing content

---

### Color Contrast Checker

```javascript
// Check if color contrast meets WCAG AA
function getContrastRatio(color1, color2) {
  const lum1 = getLuminance(color1);
  const lum2 = getLuminance(color2);
  const lighter = Math.max(lum1, lum2);
  const darker = Math.min(lum1, lum2);
  return (lighter + 0.05) / (darker + 0.05);
}

function meetsWCAG_AA(foreground, background) {
  const ratio = getContrastRatio(foreground, background);
  return ratio >= 4.5;  // AA for normal text
}

// Usage
meetsWCAG_AA('#2196F3', '#FFFFFF');  // true (5.88:1)
meetsWCAG_AA('#FFEB3B', '#FFFFFF');  // false (1.09:1)
```

---

### Accessible Components

**Button:**
```jsx
<button
  aria-label="Close dialog"  // Screen reader text
  disabled={isDisabled}
  aria-disabled={isDisabled}
>
  <CloseIcon aria-hidden="true" />  {/* Hide icon from SR */}
</button>
```

**Input:**
```jsx
<label htmlFor="email">Email</label>
<input
  id="email"
  type="email"
  aria-required="true"
  aria-invalid={hasError}
  aria-describedby="email-error"
/>
{hasError && (
  <span id="email-error" role="alert">
    Please enter a valid email
  </span>
)}
```

---

## 🛠️ Tooling & Workflow

### Design Tools

**Figma:**
- Design components
- Design tokens plugin
- Auto layout (responsive)
- Component library
- Design handoff

**Sketch:**
- Symbols (components)
- Shared libraries
- Plugins for tokens

**Adobe XD:**
- Components & states
- Design systems panel

---

### Token Generation

**Style Dictionary:**
```bash
npm install style-dictionary
```

**config.json:**
```json
{
  "source": ["tokens/**/*.json"],
  "platforms": {
    "css": {
      "transformGroup": "css",
      "buildPath": "build/css/",
      "files": [{
        "destination": "variables.css",
        "format": "css/variables"
      }]
    },
    "js": {
      "transformGroup": "js",
      "buildPath": "build/js/",
      "files": [{
        "destination": "tokens.js",
        "format": "javascript/es6"
      }]
    }
  }
}
```

---

### Version Control

**Semantic Versioning:**
```
1.2.3
↑ ↑ ↑
│ │ └─ Patch (bug fixes)
│ └─── Minor (new features, backwards compatible)
└───── Major (breaking changes)
```

**Changelog:**
```markdown
# Changelog

## [2.0.0] - 2025-01-15
### Breaking Changes
- Renamed `btn` class to `button`

### Added
- Dark mode support
- New `Input` component

### Fixed
- Button focus outline in Safari
```

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,400+
**Status:** Production Ready ✅
