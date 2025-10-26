---
name: animation-microinteractions-skill
description: Master UI animations and microinteractions for delightful user experiences. Use for: CSS animations, transition timing functions, keyframes, scroll animations, hover effects, loading states, skeleton screens, spring physics, Framer Motion, GSAP, performance optimization (will-change, transform), and creating smooth, polished, engaging interfaces that feel alive.
---

# ✨ Animation & Microinteractions Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [Animation Fundamentals](#animation-fundamentals)
2. [CSS Transitions](#css-transitions)
3. [CSS Animations](#css-animations)
4. [Microinteractions](#microinteractions)
5. [Scroll Animations](#scroll-animations)
6. [Loading States](#loading-states)
7. [Framer Motion](#framer-motion)
8. [GSAP](#gsap)
9. [Performance](#performance)
10. [Best Practices](#best-practices)

---

## 🎯 Animation Fundamentals

### The 12 Principles of Animation

**From Disney (apply to UI):**

1. **Squash & Stretch** - Objects deform when moving
2. **Anticipation** - Prepare before action
3. **Staging** - Direct attention
4. **Straight Ahead vs Pose-to-Pose** - Animation approach
5. **Follow Through** - Movement continues after stop
6. **Slow In/Slow Out** - Ease timing
7. **Arcs** - Natural motion paths
8. **Secondary Action** - Supporting movements
9. **Timing** - Speed = personality
10. **Exaggeration** - Emphasize for effect
11. **Solid Drawing** - Consistency
12. **Appeal** - Make it engaging

---

### Timing Functions (Easing)

```css
/* Linear - No easing (robotic) */
transition: all 0.3s linear;

/* Ease (default) - Slow start, fast middle, slow end */
transition: all 0.3s ease;

/* Ease-in - Slow start */
transition: all 0.3s ease-in;

/* Ease-out - Slow end (MOST COMMON for UI) */
transition: all 0.3s ease-out;

/* Ease-in-out - Slow start and end */
transition: all 0.3s ease-in-out;

/* Cubic-bezier - Custom easing */
transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);  /* Material Design */
```

**Common UI Easings:**
```css
/* Material Design */
--ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
--ease-decelerate: cubic-bezier(0, 0, 0.2, 1);  /* Entering */
--ease-accelerate: cubic-bezier(0.4, 0, 1, 1);  /* Exiting */

/* iOS */
--ease-ios: cubic-bezier(0.25, 0.1, 0.25, 1);

/* Bouncy (playful) */
--ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

---

### Animation Duration Guide

```css
/* Micro-interactions: 100-300ms */
.button-hover {
    transition: 150ms;  /* Fast, responsive */
}

/* UI elements entering: 200-400ms */
.modal-enter {
    transition: 300ms;  /* Noticeable but quick */
}

/* Complex transitions: 400-600ms */
.page-transition {
    transition: 500ms;  /* Smooth, considered */
}

/* Decorative/large: 600-1000ms */
.hero-animation {
    transition: 800ms;  /* Dramatic, attention-grabbing */
}

/* Rule of thumb: Keep under 400ms for most UI! */
```

---

## 🎨 CSS Transitions

### Basic Syntax

```css
.button {
    background: #3498db;
    color: white;
    padding: 12px 24px;
    border-radius: 4px;

    /* Transition syntax */
    transition: background 0.3s ease-out;
    /*          ↑ property  ↑ duration ↑ timing */
}

.button:hover {
    background: #2980b9;  /* Transitions from #3498db */
}
```

---

### Multiple Properties

```css
.button {
    /* Transition specific properties */
    transition:
        background 0.3s ease-out,
        transform 0.2s ease-out,
        box-shadow 0.3s ease-out;
}

/* OR all properties */
.button {
    transition: all 0.3s ease-out;  /* ⚠️ Less performant */
}
```

---

### Hover Effects

**Button Hover:**
```css
.button {
    background: #3498db;
    transform: translateY(0);
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.2s ease-out;
}

.button:hover {
    background: #2980b9;
    transform: translateY(-2px);  /* Lift up */
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);  /* Bigger shadow */
}

.button:active {
    transform: translateY(0);  /* Press down */
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}
```

**Card Hover:**
```css
.card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 24px rgba(0,0,0,0.15);
}
```

**Link Underline:**
```css
.link {
    position: relative;
    text-decoration: none;
}

.link::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background: currentColor;
    transition: width 0.3s ease-out;
}

.link:hover::after {
    width: 100%;  /* Underline expands */
}
```

---

## 🎬 CSS Animations

### Keyframes

```css
@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

/* Multi-step animation */
@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.05);
    }
    100% {
        transform: scale(1);
    }
}

/* Usage */
.modal {
    animation: fadeIn 0.3s ease-out;
}

.notification {
    animation: pulse 2s ease-in-out infinite;
}
```

---

### Animation Properties

```css
.element {
    animation-name: fadeIn;
    animation-duration: 0.5s;
    animation-timing-function: ease-out;
    animation-delay: 0.2s;
    animation-iteration-count: 1;  /* or 'infinite' */
    animation-direction: normal;  /* or 'reverse', 'alternate' */
    animation-fill-mode: forwards;  /* Keep final state */
    animation-play-state: running;  /* or 'paused' */

    /* Shorthand */
    animation: fadeIn 0.5s ease-out 0.2s 1 normal forwards;
}
```

---

### Common Animations

**Fade In:**
```css
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}
```

**Slide In:**
```css
@keyframes slideInLeft {
    from {
        transform: translateX(-100%);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}
```

**Bounce:**
```css
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-20px);
    }
    60% {
        transform: translateY(-10px);
    }
}
```

**Spin:**
```css
@keyframes spin {
    from {
        transform: rotate(0deg);
    }
    to {
        transform: rotate(360deg);
    }
}
```

**Shake:**
```css
@keyframes shake {
    0%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }
    20%, 40%, 60%, 80% { transform: translateX(10px); }
}
```

---

## 🎮 Microinteractions

### Definition

**Microinteractions** = Small, focused animations that provide feedback.

**Examples:**
- Button hover states
- Like button animation
- Toggle switches
- Form validation feedback
- Loading indicators
- Tooltips appearing

---

### Toggle Switch

```html
<label class="toggle">
    <input type="checkbox">
    <span class="slider"></span>
</label>
```

```css
.toggle {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
}

.toggle input {
    opacity: 0;
    width: 0;
    height: 0;
}

.slider {
    position: absolute;
    inset: 0;
    background: #ccc;
    border-radius: 34px;
    transition: 0.3s;
    cursor: pointer;
}

.slider::before {
    content: '';
    position: absolute;
    width: 26px;
    height: 26px;
    left: 4px;
    bottom: 4px;
    background: white;
    border-radius: 50%;
    transition: 0.3s;
}

input:checked + .slider {
    background: #2196F3;
}

input:checked + .slider::before {
    transform: translateX(26px);
}
```

---

### Like Button

```html
<button class="like-button">
    <svg class="heart" viewBox="0 0 24 24">
        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
    </svg>
</button>
```

```css
.like-button {
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
}

.heart {
    width: 32px;
    height: 32px;
    fill: #ccc;
    transition: fill 0.3s, transform 0.3s;
}

.like-button:hover .heart {
    fill: #ff6b6b;
}

.like-button.liked .heart {
    fill: #ff6b6b;
    animation: like 0.5s ease-in-out;
}

@keyframes like {
    0% { transform: scale(1); }
    25% { transform: scale(1.3); }
    50% { transform: scale(0.9); }
    75% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
```

---

### Form Validation Feedback

```css
.input {
    border: 2px solid #ccc;
    transition: border-color 0.3s, transform 0.3s;
}

.input:focus {
    border-color: #3498db;
    outline: none;
}

.input.error {
    border-color: #e74c3c;
    animation: shake 0.5s;
}

.input.success {
    border-color: #2ecc71;
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
    20%, 40%, 60%, 80% { transform: translateX(5px); }
}
```

---

## 📜 Scroll Animations

### Scroll-Triggered Fade In

```css
.fade-in {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.fade-in.visible {
    opacity: 1;
    transform: translateY(0);
}
```

```javascript
// Intersection Observer (modern, performant)
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, {
    threshold: 0.1  // Trigger when 10% visible
});

document.querySelectorAll('.fade-in').forEach(el => {
    observer.observe(el);
});
```

---

### Parallax Scrolling

```css
.parallax {
    background-image: url('bg.jpg');
    background-attachment: fixed;  /* Simple parallax */
    background-position: center;
    background-size: cover;
    height: 500px;
}
```

**Advanced Parallax (JavaScript):**
```javascript
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallax = document.querySelector('.parallax');
    parallax.style.transform = `translateY(${scrolled * 0.5}px)`;
});
```

---

### Progress Bar on Scroll

```html
<div class="progress-bar"></div>
```

```css
.progress-bar {
    position: fixed;
    top: 0;
    left: 0;
    height: 4px;
    background: linear-gradient(to right, #3498db, #2ecc71);
    width: 0;
    z-index: 1000;
    transition: width 0.1s ease-out;
}
```

```javascript
window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    document.querySelector('.progress-bar').style.width = scrolled + '%';
});
```

---

## ⏳ Loading States

### Spinner

```html
<div class="spinner"></div>
```

```css
.spinner {
    width: 40px;
    height: 40px;
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
```

---

### Skeleton Screen

```html
<div class="skeleton-card">
    <div class="skeleton skeleton-image"></div>
    <div class="skeleton skeleton-title"></div>
    <div class="skeleton skeleton-text"></div>
    <div class="skeleton skeleton-text"></div>
</div>
```

```css
.skeleton {
    background: linear-gradient(
        90deg,
        #f0f0f0 25%,
        #e0e0e0 50%,
        #f0f0f0 75%
    );
    background-size: 200% 100%;
    animation: loading 1.5s infinite;
    border-radius: 4px;
}

@keyframes loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}

.skeleton-image {
    width: 100%;
    height: 200px;
    margin-bottom: 12px;
}

.skeleton-title {
    width: 60%;
    height: 24px;
    margin-bottom: 8px;
}

.skeleton-text {
    width: 100%;
    height: 16px;
    margin-bottom: 8px;
}
```

---

### Pulse Loading

```css
.pulse {
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
}
```

---

## 🎨 Framer Motion

### Installation

```bash
npm install framer-motion
```

---

### Basic Animation

```jsx
import { motion } from 'framer-motion';

function Box() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 50 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            style={{
                width: 100,
                height: 100,
                background: '#3498db'
            }}
        />
    );
}
```

---

### Hover & Tap

```jsx
<motion.button
    whileHover={{ scale: 1.1 }}
    whileTap={{ scale: 0.95 }}
    transition={{ type: "spring", stiffness: 300 }}
>
    Click me
</motion.button>
```

---

### Variants (Reusable Animations)

```jsx
const variants = {
    hidden: { opacity: 0, y: 50 },
    visible: { opacity: 1, y: 0 }
};

function Card() {
    return (
        <motion.div
            variants={variants}
            initial="hidden"
            animate="visible"
            transition={{ duration: 0.5 }}
        >
            Card content
        </motion.div>
    );
}
```

---

### Stagger Children

```jsx
const container = {
    hidden: { opacity: 0 },
    show: {
        opacity: 1,
        transition: {
            staggerChildren: 0.1
        }
    }
};

const item = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0 }
};

function List({ items }) {
    return (
        <motion.ul variants={container} initial="hidden" animate="show">
            {items.map(item => (
                <motion.li key={item.id} variants={item}>
                    {item.text}
                </motion.li>
            ))}
        </motion.ul>
    );
}
```

---

## 🚀 GSAP

### Installation

```bash
npm install gsap
```

---

### Basic Tween

```javascript
import gsap from 'gsap';

// Animate to specific values
gsap.to('.box', {
    x: 200,
    duration: 1,
    ease: 'power2.out'
});

// Animate from specific values
gsap.from('.box', {
    opacity: 0,
    y: 50,
    duration: 1
});

// Set initial values then animate
gsap.fromTo('.box',
    { opacity: 0, scale: 0 },
    { opacity: 1, scale: 1, duration: 1 }
);
```

---

### Timeline

```javascript
const tl = gsap.timeline();

tl.to('.box1', { x: 100, duration: 1 })
  .to('.box2', { x: 100, duration: 1 }, '-=0.5')  // Overlap by 0.5s
  .to('.box3', { x: 100, duration: 1 });
```

---

### Scroll Trigger

```javascript
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

gsap.to('.box', {
    scrollTrigger: {
        trigger: '.box',
        start: 'top center',  // When top of .box hits center of viewport
        end: 'bottom top',
        scrub: true,  // Link animation to scroll position
        markers: true  // Debug markers
    },
    x: 500
});
```

---

## ⚡ Performance

### GPU Acceleration

```css
/* ✅ GPU-accelerated properties (fast) */
.fast {
    transform: translateX(100px);  /* ✅ */
    opacity: 0.5;  /* ✅ */
}

/* ❌ Layout-triggering properties (slow) */
.slow {
    left: 100px;  /* ❌ Triggers layout */
    width: 200px;  /* ❌ Triggers layout */
    margin-left: 50px;  /* ❌ Triggers layout */
}
```

---

### will-change

```css
/* Tell browser property will animate */
.button {
    will-change: transform;  /* Prepare for transform animation */
}

.button:hover {
    transform: scale(1.1);
}

/* ⚠️ Don't overuse! Remove after animation */
.element {
    will-change: transform;
}

.element.animating {
    animation: slide 0.5s;
}

.element.done {
    will-change: auto;  /* Remove optimization */
}
```

---

### Reduce Motion

```css
/* Respect user preference */
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

---

## ✅ Best Practices

### Do's

✅ **Use transform & opacity** (GPU-accelerated)
✅ **Keep animations under 400ms** (feels responsive)
✅ **Use ease-out for UI** (feels natural)
✅ **Provide purpose** (not decoration)
✅ **Test on low-end devices** (ensure smooth)
✅ **Respect prefers-reduced-motion**

### Don'ts

❌ **Don't animate layout properties** (width, height, left, top)
❌ **Don't overuse animations** (overwhelming)
❌ **Don't use long durations** (feels slow)
❌ **Don't auto-play critical content** (accessibility)
❌ **Don't forget performance** (60fps target)

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,200+
**Status:** Production Ready ✅
