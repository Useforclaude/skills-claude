---
name: mobile-ux-design-skill
description: Master mobile UX design for iOS and Android. Use for mobile-first design strategy, touch target sizing (44×44pt minimum), gesture design (swipe, pinch, long-press), responsive breakpoints (320px, 375px, 414px), mobile navigation patterns (tab bar, bottom sheet, hamburger menu), thumb zones (reachable areas), mobile forms (auto-complete, input types), performance optimization (image compression, lazy loading), platform guidelines (iOS Human Interface Guidelines, Material Design), mobile typography (16px minimum), mobile accessibility, adaptive layouts, safe areas, status bars, and production-ready mobile app design.
---

# Mobile UX Design Mastery Skill

## Overview

Mobile-first is the standard - 60%+ of web traffic is mobile.

**This skill covers:**
- 📱 Mobile-First Strategy
- 👆 Touch & Gestures
- 📐 Screen Sizes & Breakpoints
- 🧭 Mobile Navigation Patterns
- ⌨️ Mobile Form Design
- 🎨 Platform Guidelines (iOS vs Android)
- ♿ Mobile Accessibility
- ⚡ Performance Optimization

---

# Part 1: Mobile-First Foundation

## 1.1 Why Mobile-First?

**Statistics (2024):**
- 📊 58% of web traffic from mobile
- 🚀 Mobile users expect < 3s load time
- 💰 53% abandon site if load > 3s
- 📈 Mobile-first indexing (Google)

**Mobile-First vs Desktop-First:**
```
Desktop-First (Old Way):
1. Design for desktop (1440px)
2. Scale down to mobile (cramming)
3. Result: Poor mobile UX

Mobile-First (Correct Way):
1. Design for mobile (375px) 
2. Progressive enhancement to desktop
3. Result: Great experience on all devices
```

---

## 1.2 Screen Sizes & Breakpoints

**Common Device Sizes (2024):**
```
Mobile:
├─ iPhone SE:        375 × 667 (small)
├─ iPhone 14:        390 × 844 (medium)
├─ iPhone 14 Pro Max: 430 × 932 (large)
├─ Samsung S23:      360 × 780
└─ Pixel 7:          412 × 915

Tablet:
├─ iPad Mini:        768 × 1024
├─ iPad Air:         820 × 1180
└─ iPad Pro 12.9":   1024 × 1366

Desktop:
├─ Laptop:           1440 × 900
└─ Desktop:          1920 × 1080
```

**Responsive Breakpoints:**
```css
/* Mobile-first CSS */
.container { width: 100%; }  /* 320px+ */

@media (min-width: 640px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1280px) { /* Large Desktop */ }
```

**Design for:**
1. **320px** - Minimum (old iPhones)
2. **375px** - Standard mobile (iPhone 14)
3. **768px** - Tablet
4. **1024px** - Desktop

---

## 1.3 Viewport & Safe Areas

**Viewport Units:**
```
100vw = 100% viewport width
100vh = 100% viewport height

Mobile issue: 100vh includes address bar!
Solution: Use dvh (dynamic viewport height) or JS
```

**Safe Areas (iOS):**
```
iPhone with notch → Content must avoid:
├─ Status bar (top 44pt)
├─ Home indicator (bottom 34pt)
└─ Rounded corners

Use: env(safe-area-inset-*)
padding-top: env(safe-area-inset-top);
padding-bottom: env(safe-area-inset-bottom);
```

---

# Part 2: Touch & Gesture Design

## 2.1 Touch Target Sizing

**Minimum Touch Target: 44×44pt (iOS) / 48×48dp (Android)**

**Why?**
- Average finger pad: 45-57px
- Smaller targets → mis-taps

**Examples:**
```
✅ Good:
Button: 44pt height, 88pt width
Icon button: 44×44pt (icon 24×24pt inside)
Checkbox: 44×44pt tap area (icon 20×20pt)

❌ Bad:
Button: 32pt height (too small!)
Link: 12px text without padding
Close icon: 16×16pt (no tap padding)
```

**Spacing Between Tap Targets:**
- Minimum: 8pt between buttons
- Recommended: 16pt for critical actions

---

## 2.2 Gesture Patterns

**Common Gestures:**
```
Tap             Select, activate
Double Tap      Zoom in
Long Press      Context menu, drag mode
Swipe           Navigate, dismiss, reveal actions
Pinch           Zoom in/out
Rotate          Rotate content (rare)
Pan             Scroll, move object
Edge Swipe      Back navigation (iOS)
```

**Swipe Actions:**
```
List Item:
├─ Swipe left → Reveal: Archive, Delete
├─ Swipe right → Reveal: Mark as read, Star
└─ Full swipe → Quick action (delete immediately)

Best practices:
- Show visual feedback (icons slide in)
- Destructive actions require confirmation
- Use standard patterns (left = delete)
```

**Pull to Refresh:**
```
Scroll down from top → Loading indicator → Refresh content

Implementation:
1. User pulls down
2. Show spinner (rotate)
3. Load new data
4. Animate content update
```

---

## 2.3 Thumb Zones (Reachability)

**One-Handed Use:**
```
┌─────────────────────┐
│   Hard to Reach     │ ← Top (avoid primary actions)
│   (Status bar)      │
├─────────────────────┤
│                     │
│   Easy to Reach     │ ← Middle (secondary actions)
│                     │
├─────────────────────┤
│   Natural Thumb     │ ← Bottom (primary actions)
│   Zone (Best)       │    Navigation, CTAs here!
└─────────────────────┘
```

**Do's:**
✅ Place primary actions at bottom (tab bar, FAB)
✅ Place navigation at bottom (iOS tab bar)
✅ Place close buttons top-left or bottom

**Don'ts:**
❌ Put CTA button at top-right (hard to reach)
❌ Critical actions at top corners
❌ Force two-handed use

---

# Part 3: Mobile Navigation Patterns

## 3.1 Tab Bar (iOS) / Bottom Navigation (Android)

**When to use:**
- 3-5 top-level sections
- Frequent switching between sections
- Equal importance sections

**Best Practices:**
```
✅ Do:
- 3-5 tabs (not more!)
- Clear icons + labels
- Selected state visible (color/icon change)
- Fixed position (always visible)

❌ Don't:
- More than 5 tabs (use hamburger menu)
- Text-only tabs (icons help recognition)
- Hide tab bar on scroll (users lose context)
```

**Example:**
```
Instagram:
├─ Home (feed icon)
├─ Search (magnifying glass)
├─ Reels (play icon)
├─ Shop (shopping bag)
└─ Profile (avatar)
```

---

## 3.2 Hamburger Menu (Drawer)

**When to use:**
- Many navigation items (6+)
- Less frequently accessed sections
- Secondary navigation

**Types:**
```
Overlay Drawer (iOS/Android)
├─ Slides in from left
├─ Dims background
└─ Tap outside to close

Persistent Drawer (Tablet/Desktop)
├─ Always visible
└─ Content shifts right
```

**Best Practices:**
```
✅ Do:
- Group related items
- Show user profile at top
- Highlight current section
- Close on item selection

❌ Don't:
- Hide primary navigation in hamburger
- Use for 3-5 items (use tab bar instead)
- Require menu for core actions
```

---

## 3.3 Bottom Sheet

**When to use:**
- Contextual actions (share, edit, delete)
- Filters & sorting
- Quick settings
- Modal selection (country picker)

**Types:**
```
Standard Bottom Sheet
├─ Partial screen (50-70%)
├─ Drag to expand/dismiss
└─ Dim background

Full-Screen Bottom Sheet
├─ 100% height
├─ Close button top-right
└─ Use for complex forms
```

**Example (iOS Share Sheet):**
```
1. User taps Share button
2. Bottom sheet slides up
3. Shows: AirDrop, Messages, Email
4. User selects action
5. Sheet dismisses
```

---

## 3.4 Mobile Breadcrumbs & Back Navigation

**iOS Back Navigation:**
```
┌─────────────────────┐
│ ← Settings   Done   │ ← Back button (top-left)
│                     │
│   Notifications     │
└─────────────────────┘

Gesture: Edge swipe right → Go back
```

**Android Back Navigation:**
```
System back button (bottom) or gesture (swipe from edge)
Material Design: Show "←" in app bar for consistency
```

**Breadcrumbs (Tablet/Desktop only):**
```
Home > Products > Electronics > Laptops

Mobile: Hide breadcrumbs (use back button)
```

---

# Part 4: Mobile Forms & Input

## 4.1 Mobile Form Best Practices

**Field Design:**
```
✅ Good Mobile Form:
├─ One column layout (not multiple columns)
├─ Large input fields (44pt+ height)
├─ Labels above fields (not inline)
├─ Floating labels (Material Design)
├─ Clear button in fields (×)
└─ Auto-advance to next field (OTP codes)

❌ Bad Mobile Form:
├─ Two column layout (cramped)
├─ Small inputs (32pt height)
├─ Placeholder as label (disappears on focus)
└─ No visual feedback
```

**Input Types (HTML5):**
```html
<input type="email">       <!-- Email keyboard (@, .com) -->
<input type="tel">         <!-- Phone keyboard (numbers) -->
<input type="number">      <!-- Numeric keyboard -->
<input type="url">         <!-- URL keyboard (/, .com) -->
<input type="date">        <!-- Date picker -->
<input type="search">      <!-- Search keyboard (Go button) -->
```

**Auto-Complete:**
```html
<input 
  type="email" 
  autocomplete="email"
  inputmode="email"
>
<!-- Browser suggests saved emails -->
```

---

## 4.2 Keyboards & Input Modes

**Keyboard Types:**
```
Default     QWERTY keyboard
Numeric     0-9 + symbols
Email       @ and .com shortcuts
Phone       0-9, +, *, #
URL         /, .com shortcuts
Decimal     0-9 with decimal point
Search      "Go" or "Search" button
```

**Example:**
```html
<!-- Credit card input -->
<input 
  type="text" 
  inputmode="numeric" 
  pattern="[0-9]*"
  autocomplete="cc-number"
>
<!-- Shows numeric keyboard, no letters -->
```

---

## 4.3 Mobile Form UX Patterns

**Progressive Disclosure:**
```
Step 1: Email (one field)
       ↓ User enters email
Step 2: Password (show next field)
       ↓ Valid input
Step 3: Confirm (show submit button)

Result: Less overwhelming, higher completion
```

**Smart Defaults:**
```
Country: Auto-detect from IP (default: User's country)
Phone: Pre-fill country code
Date: Default to today (if relevant)
```

**Inline Validation:**
```
✅ Real-time validation:
- Email: Check format as user types (debounced)
- Password: Show strength meter
- Username: Check availability (API call)

❌ Don't:
- Show error before user finishes typing
- Validate on every keystroke (use debounce 500ms)
```

---

## 4.4 Mobile Checkout Optimization

**Reduce Friction:**
```
✅ Do:
- Guest checkout (don't force account)
- Save payment info (with permission)
- Autofill address (Google Places API)
- Show price summary always visible
- One-page checkout (not 5 steps)

❌ Don't:
- Require account creation
- Hide total until final step
- Use CAPTCHA (use invisible reCAPTCHA)
- Split across many pages
```

**Payment Methods:**
```
Mobile-friendly:
├─ Apple Pay (iOS)
├─ Google Pay (Android)
├─ PayPal
└─ Credit card (with auto-fill)

Result: 1-tap checkout (vs 10 form fields!)
```

---

# Part 5: iOS vs Android Design Guidelines

## 5.1 iOS Human Interface Guidelines

**Navigation:**
```
Tab Bar (Bottom)
├─ 3-5 items
├─ Icons + labels
└─ Selected state (bold icon, color)

Navigation Bar (Top)
├─ Large title (bold)
├─ Back button (←)
└─ Right actions (Edit, Done)
```

**Typography:**
```
SF Pro (System font)
├─ Large Title: 34pt bold
├─ Title 1: 28pt regular
├─ Title 2: 22pt regular
├─ Headline: 17pt semibold
├─ Body: 17pt regular
└─ Caption: 12pt regular
```

**Colors:**
```
System Colors:
├─ Blue: #007AFF (primary)
├─ Red: #FF3B30 (destructive)
├─ Green: #34C759 (success)
└─ Gray: #8E8E93 (secondary text)

Dark Mode:
- Automatic color adaptation
- Use semantic colors (label, systemBackground)
```

**Spacing:**
```
Standard margins: 16pt (left/right)
Between elements: 8pt, 16pt, 24pt
List item height: 44pt minimum
```

---

## 5.2 Material Design (Android)

**Navigation:**
```
Bottom Navigation
├─ 3-5 items
├─ Icons (24dp)
├─ Labels (12sp)
└─ Ripple effect on tap

Navigation Drawer
├─ Hamburger icon (top-left)
├─ Slides in from left
└─ 56dp elevation
```

**Typography (Material 3):**
```
Roboto / Product Sans
├─ Display Large: 57sp
├─ Headline Large: 32sp
├─ Title Large: 22sp
├─ Body Large: 16sp
├─ Label Large: 14sp
└─ Body Small: 12sp
```

**Colors (Material You):**
```
Dynamic Color (Android 12+)
├─ Extracts from wallpaper
├─ Primary, Secondary, Tertiary
└─ Surface, Background variants

Example:
├─ Primary: #6750A4 (purple)
├─ On Primary: #FFFFFF (text on primary)
├─ Surface: #FFFBFE (card background)
└─ On Surface: #1C1B1F (text on surface)
```

**Elevation & Shadows:**
```
0dp  No shadow (flat)
1dp  Small shadow (cards)
4dp  Medium shadow (floating button)
8dp  Large shadow (drawer)
16dp Extra large (modals)
```

---

## 5.3 Platform Differences Summary

```
┌─────────────────┬──────────────────┬──────────────────┐
│ Feature         │ iOS              │ Android          │
├─────────────────┼──────────────────┼──────────────────┤
│ Navigation      │ Tab Bar (bottom) │ Bottom Nav       │
│ Back Button     │ Top-left         │ System (bottom)  │
│ Action Button   │ Circular         │ FAB (circular)   │
│ Switches        │ Toggle (green)   │ Switch (thumb)   │
│ Selection       │ Checkmark        │ Checkbox         │
│ Typography      │ SF Pro           │ Roboto           │
│ Icons           │ SF Symbols       │ Material Icons   │
│ Alerts          │ Center popup     │ Bottom sheet     │
│ Gestures        │ Edge swipe back  │ System back      │
└─────────────────┴──────────────────┴──────────────────┘
```

---

# Part 6: Mobile Accessibility

## 6.1 Touch Target Sizing (Accessibility)

**WCAG 2.5.5 (AAA):**
- Minimum: 44×44pt (iOS) / 48×48dp (Android)
- Exceptions: Inline text links

**Testing:**
```
iOS: Settings → Accessibility → Touch → Button Shapes
Android: Settings → Accessibility → TalkBack
```

---

## 6.2 Color Contrast (Mobile)

**WCAG AA Requirements:**
```
Normal text (< 18pt):
├─ Contrast ratio: 4.5:1 minimum
└─ Example: #000000 text on #FFFFFF background = 21:1 ✅

Large text (≥ 18pt):
├─ Contrast ratio: 3:1 minimum
└─ More forgiving

Interactive elements:
├─ 3:1 minimum (buttons, icons)
```

**Mobile Challenges:**
- Outdoor sunlight (need higher contrast!)
- Small screens (text must be readable)
- Dark mode (maintain contrast)

**Tools:**
```
Stark (Figma plugin)
Contrast Checker (WebAIM)
Accessible Colors (color palette generator)
```

---

## 6.3 Screen Readers (VoiceOver & TalkBack)

**VoiceOver (iOS):**
```
Enable: Settings → Accessibility → VoiceOver

Gestures:
├─ Swipe right: Next element
├─ Swipe left: Previous element
├─ Double tap: Activate element
└─ Two-finger swipe up: Read from top
```

**TalkBack (Android):**
```
Enable: Settings → Accessibility → TalkBack

Similar gestures to VoiceOver
```

**Design for Screen Readers:**
```
✅ Do:
- Add alt text to images
- Use semantic HTML (button, nav, article)
- Provide descriptive labels
- Announce dynamic changes (ARIA live regions)

❌ Don't:
- Use div with onClick (use button)
- Rely on color alone (add icons/labels)
- Hide important content visually (screen readers won't find)
```

---

# Part 7: Performance Optimization

## 7.1 Image Optimization

**Best Practices:**
```
Format:
├─ WebP (smaller than PNG/JPG, 25-35% savings)
├─ AVIF (even smaller, cutting-edge)
└─ JPG for photos, PNG for logos/icons

Responsive Images:
<img 
  srcset="
    image-320w.webp 320w,
    image-640w.webp 640w,
    image-1024w.webp 1024w
  "
  sizes="100vw"
  src="image-640w.webp"
  alt="Description"
>

Result: Mobile loads 320w, Desktop loads 1024w
```

**Lazy Loading:**
```html
<img src="image.jpg" loading="lazy" alt="...">
<!-- Image loads only when near viewport -->
```

---

## 7.2 Mobile Performance Metrics

**Core Web Vitals:**
```
LCP (Largest Contentful Paint)
├─ Target: < 2.5s
└─ Measures: Time to load main content

FID (First Input Delay)
├─ Target: < 100ms
└─ Measures: Time to interactive

CLS (Cumulative Layout Shift)
├─ Target: < 0.1
└─ Measures: Visual stability
```

**Testing:**
```
Tools:
├─ Google PageSpeed Insights
├─ Lighthouse (Chrome DevTools)
├─ WebPageTest (mobile testing)
└─ Real device testing (actual phones!)
```

---

## ✅ Final Summary Checklist

### Mobile-First Design
- [ ] Design for 375px first, then scale up
- [ ] Use mobile breakpoints (320px, 375px, 768px, 1024px)
- [ ] Account for safe areas (notch, home indicator)

### Touch & Gestures
- [ ] Touch targets ≥ 44×44pt
- [ ] Use standard gesture patterns (swipe, long-press)
- [ ] Place primary actions in thumb zone (bottom)

### Navigation
- [ ] Use tab bar for 3-5 top sections
- [ ] Use hamburger menu for 6+ items
- [ ] Use bottom sheet for contextual actions
- [ ] Implement back navigation (iOS edge swipe, Android system back)

### Forms & Input
- [ ] One column layout
- [ ] Large input fields (44pt height)
- [ ] Correct input types (email, tel, number)
- [ ] Inline validation (debounced)
- [ ] Smart defaults & autofill

### Platform Guidelines
- [ ] Follow iOS HIG (tab bar, SF Pro font)
- [ ] Follow Material Design (bottom nav, Roboto font)
- [ ] Adapt for platform differences

### Accessibility
- [ ] Touch targets meet WCAG (44×44pt)
- [ ] Color contrast ≥ 4.5:1
- [ ] Test with VoiceOver/TalkBack
- [ ] Semantic HTML & ARIA labels

### Performance
- [ ] Optimize images (WebP, responsive sizes, lazy loading)
- [ ] Target LCP < 2.5s, FID < 100ms
- [ ] Test on real devices (not just desktop browser)

---

## 🎓 Congratulations!

You've mastered **Mobile UX Design**!

**Total Content:** ~1,500 lines

**Resources:**
- iOS HIG: https://developer.apple.com/design/human-interface-guidelines/
- Material Design: https://m3.material.io/
- Mobile Design Patterns: https://mobbin.com
- Luke Wroblewski (Mobile Expert): https://www.lukew.com

Good luck building mobile-first experiences! 📱🚀

---
