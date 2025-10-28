---
name: figma-mastery-skill
description: Master Figma design tool for UI/UX workflow. Use for Figma components (variants, properties, instances), auto-layout (spacing, alignment, constraints), prototyping (interactions, animations, smart animate), design systems (styles, libraries, tokens), collaboration (comments, Dev Mode, inspect), plugins (FigJam, community plugins), advanced features (variables, conditional logic, branching), Figma API (automation, integration), design handoff, responsive design, component architecture, design tokens export, version control, team libraries, and production-ready design workflows. Also use for Thai keywords "Figma", "ฟิกม่า", "ออกแบบ UI", "ออกแบบ UX", "component Figma", "auto-layout", "prototype", "ต้นแบบ", "design system", "Dev Mode", "plugins", "FigJam", "ส่งงานโปรแกรมเมอร์", "design handoff", "responsive design", "ทำงานร่วมกัน", "collaborate", "design token", "ห้องสมุดคอมโพเนนต์".. Also use for Thai keywords "Figma", "ฟิกม่า", "เครื่องมือออกแบบ", "ออกแบบ", "ดีไซน์", "การออกแบบ", "UI", "ส่วนติดต่อผู้ใช้", "อินเทอร์เฟซ"
---

# Figma Mastery Skill

## Overview

Figma is the industry-standard UI/UX design tool - web-based, collaborative, and powerful.

**This skill covers:**
- 🎨 Interface & Fundamentals
- 🧩 Components & Variants (reusable design elements)
- 📐 Auto-Layout (responsive, flexible layouts)
- ⚡ Prototyping & Interactions
- 🎭 Design Systems & Libraries
- 🔌 Plugins & Automation
- 🚀 Advanced Features (Variables, Conditional Logic)
- 👥 Collaboration & Dev Mode
- 📤 Design Handoff & Export

**Target Users:** UI/UX Designers, Product Designers, Frontend Developers

---

# Part 1: Figma Fundamentals

## 1.1 Interface Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    FIGMA INTERFACE                          │
└─────────────────────────────────────────────────────────────┘

Top Toolbar
├─ File, Edit, View, Object, Vector, Text, Arrange, Plugins
├─ Share button (collaboration)
└─ Present (prototype preview)

Left Sidebar (Layers Panel)
├─ Pages (organize different screens)
├─ Frames (artboards)
└─ Layers hierarchy (groups, components)

Right Sidebar (Properties Panel)
├─ Design tab (properties, fill, stroke, effects)
├─ Prototype tab (interactions, animations)
└─ Inspect tab (code export, measurements)

Canvas (Center)
├─ Infinite workspace
├─ Frames (artboards)
└─ Design elements

Bottom Bar
├─ Zoom controls
├─ Comments
└─ Version history
```

---

## 1.2 Keyboard Shortcuts (Essential)

**Navigation:**
```
Space + Drag          Pan canvas
Cmd/Ctrl + Scroll     Zoom in/out
Cmd/Ctrl + 0          Zoom to fit
Cmd/Ctrl + 1          Zoom to 100%
Z                     Zoom tool
```

**Selection & Tools:**
```
V                     Move tool (default)
F                     Frame tool
R                     Rectangle
O                     Ellipse
T                     Text
P                     Pen tool
L                     Line
Cmd/Ctrl + D          Duplicate
```

**Layout & Alignment:**
```
Option/Alt + H        Distribute horizontal
Option/Alt + V        Distribute vertical
Cmd/Ctrl + G          Group
Cmd/Ctrl + Shift + G  Ungroup
Option/Alt + A        Create component
```

**Components:**
```
Cmd/Ctrl + Option/Alt + K    Create component
Cmd/Ctrl + Option/Alt + B    Detach instance
Option/Alt + 1               Layers panel
Option/Alt + 2               Components panel
Option/Alt + 8               Design panel
Option/Alt + 9               Prototype panel
```

---

## 1.3 Frames vs Groups

**Frames (Artboards):**
- Have fixed size (width × height)
- Used for screens, components, sections
- Support Auto Layout
- Can be exported individually
- Clip content by default

```
Create Frame: Press F
Common sizes:
- iPhone 14 Pro: 393 × 852
- Desktop: 1440 × 900
- iPad Pro 12.9": 1024 × 1366
```

**Groups:**
- No fixed size (resize with content)
- Used for organizing layers
- Don't support Auto Layout
- Cannot be exported alone
- Don't clip content

```
Create Group: Cmd/Ctrl + G
Use for: Organizing related elements
```

**When to use:**
- Frame: Screens, components, sections with fixed/responsive size
- Group: Temporary organization, non-layout grouping

---

## 1.4 Constraints (Responsive Behavior)

Constraints control how layers resize when parent frame resizes.

**Horizontal Constraints:**
```
Left              Pin to left edge
Right             Pin to right edge
Left & Right      Stretch horizontally
Center            Center horizontally
Scale             Scale proportionally
```

**Vertical Constraints:**
```
Top               Pin to top edge
Bottom            Pin to bottom edge
Top & Bottom      Stretch vertically
Center            Center vertically
Scale             Scale proportionally
```

**Example: Responsive Header**
```
Frame: Header (1440px wide)
├─ Logo (Left constraint)
├─ Navigation (Center constraint)
└─ User Avatar (Right constraint)

When frame resizes:
- Logo stays left
- Nav stays centered
- Avatar stays right
```

---

# Part 2: Components & Variants

## 2.1 Creating Components

**Component = Reusable design element**

**Create Component:**
1. Select layer(s)
2. Press `Cmd/Ctrl + Option/Alt + K`
3. Or: Right-click → Create Component

**Component Instance:**
- Use component: Drag from Assets panel
- Instance = copy linked to main component
- Changes to main = updates all instances

**Example: Button Component**
```
1. Create rectangle (rounded corners)
2. Add text "Click Me"
3. Select both → Create Component
4. Name: "Button/Primary"

Usage:
- Drag "Button/Primary" from Assets
- Instances auto-update when main changes
```

---

## 2.2 Component Properties (Figma Variables)

**Properties allow customization without variants**

**Text Property:**
```
Component: Button
1. Select text layer
2. Right panel → "Create text property"
3. Name: "Label"
4. Default value: "Click Me"

Usage: Instances can change text without breaking link
```

**Boolean Property (Show/Hide):**
```
Component: Card
1. Select icon layer
2. Create boolean property: "Show Icon"
3. Default: True

Usage: Toggle icon visibility per instance
```

**Instance Swap Property:**
```
Component: Card
1. Select image slot
2. Create instance swap property: "Image"
3. Default: Placeholder component

Usage: Swap image component per instance
```

---

## 2.3 Variants (State Management)

**Variants = Multiple states of same component**

**Create Variant:**
1. Create component (e.g., Button)
2. Duplicate component (Cmd/Ctrl + D)
3. Modify duplicate (e.g., change color for hover state)
4. Select both → Right-click → Combine as Variants

**Variant Properties:**
```
Component: Button
Properties:
├─ State: Default, Hover, Pressed, Disabled
├─ Size: Small, Medium, Large
└─ Type: Primary, Secondary, Ghost

Result: 4 × 3 × 3 = 36 variants!
```

**Example: Button with Variants**
```
1. Create "Button/Default"
2. Duplicate → Change to "Button/Hover" (darker)
3. Duplicate → Change to "Button/Disabled" (gray)
4. Select all 3 → Combine as Variants

Variant Properties:
- State = Default | Hover | Disabled

Usage:
- Drag button instance
- Change State property in right panel
```

---

## 2.4 Nested Components

**Component inside component = powerful patterns**

**Example: Card with Button**
```
1. Create Button component
2. Create Card frame
3. Drag Button instance into Card
4. Add image, text to Card
5. Select Card → Create Component

Result:
- Card component contains Button instance
- Update Button main → all Cards update!
```

**Example: Icon Library**
```
1. Create Icon components (Arrow, Check, X)
2. Create Button component
3. Add Icon instance to Button (instance swap property)
4. Each Button instance can swap icon
```

---

## 2.5 Component Best Practices

**Naming Convention:**
```
Component/Variant/State

Examples:
Button/Primary/Default
Button/Primary/Hover
Button/Secondary/Default
Card/Product/WithImage
Icon/Arrow/Left
```

**Organization:**
```
Components Panel:
├─ Buttons
│   ├─ Button/Primary
│   └─ Button/Secondary
├─ Cards
│   ├─ Card/Product
│   └─ Card/User
└─ Icons
    ├─ Icon/Arrow
    └─ Icon/Check
```

**Do's:**
✅ Use clear, descriptive names
✅ Create variants for all states (hover, active, disabled)
✅ Add properties for customization (text, icons)
✅ Document usage in component description

**Don'ts:**
❌ Create too many variants (use properties instead)
❌ Hardcode text (use text properties)
❌ Deep nesting (max 2-3 levels)

---

# Part 3: Auto-Layout (Responsive Design)

## 3.1 What is Auto-Layout?

**Auto-Layout = CSS Flexbox in Figma**

- Automatically arrange children
- Add padding, spacing between items
- Resize dynamically when content changes
- Horizontal or vertical direction

**Create Auto-Layout:**
```
1. Select frame/group
2. Press Shift + A
3. Or: Right-click → Add Auto-Layout
```

---

## 3.2 Auto-Layout Properties

**Direction:**
```
Horizontal (→)    Items side by side (row)
Vertical (↓)      Items stacked (column)
Wrap              Wrap to next line (like CSS flex-wrap)
```

**Spacing:**
```
Gap between items: 8px, 16px, 24px
Use consistent spacing (8px grid)
```

**Padding:**
```
Padding: Space inside frame (all sides, or individual)
Example: 16px top, 24px horizontal, 16px bottom
```

**Alignment:**
```
Primary axis (direction):
├─ Packed (flex-start)
├─ Space between (space-between)
└─ Packed center (center)

Counter axis (perpendicular):
├─ Align top/left
├─ Align center
└─ Align bottom/right
```

**Resizing:**
```
Hug contents     Frame shrinks to fit children (width/height: auto)
Fixed            Frame has fixed size
Fill container   Child expands to fill parent
```

---

## 3.3 Auto-Layout Examples

**Example 1: Button with Auto-Layout**
```
Frame: Button (Auto-Layout)
├─ Direction: Horizontal
├─ Padding: 12px (vertical), 24px (horizontal)
├─ Spacing: 8px (between icon and text)
├─ Children:
    ├─ Icon (16×16, fixed)
    └─ Text (Hug, resizes with text)

Result: Button auto-resizes when text changes!
```

**Example 2: Card with Auto-Layout**
```
Frame: Card (Auto-Layout)
├─ Direction: Vertical
├─ Padding: 24px
├─ Spacing: 16px
├─ Children:
    ├─ Image (Fill width, Hug height)
    ├─ Title (Hug)
    ├─ Description (Hug)
    └─ Button (Hug)

Result: Card height adjusts to content!
```

**Example 3: Navigation Bar**
```
Frame: Nav (Auto-Layout)
├─ Direction: Horizontal
├─ Padding: 16px 24px
├─ Spacing: Space between
├─ Children:
    ├─ Logo (Hug, align left)
    ├─ Menu (Hug, align center)
    └─ Avatar (Hug, align right)

Result: Responsive nav bar!
```

---

## 3.4 Nested Auto-Layout

**Auto-Layout inside Auto-Layout = powerful layouts**

**Example: List Item**
```
Frame: ListItem (Auto-Layout Horizontal)
├─ Padding: 16px
├─ Spacing: 12px
├─ Children:
    ├─ Avatar (48×48, fixed)
    └─ Frame: Info (Auto-Layout Vertical, Fill width)
        ├─ Spacing: 4px
        ├─ Name (Hug)
        └─ Email (Hug)

Result: Avatar stays fixed, Info expands to fill!
```

---

## 3.5 Auto-Layout Tips & Tricks

**Tip 1: Use Hug for Dynamic Content**
```
Text, Button, Tag → Hug contents (auto-resize)
Container, Section → Fixed or Fill
```

**Tip 2: Use Fill for Full-Width Elements**
```
Image, Divider, Footer → Fill container
```

**Tip 3: Spacing Tokens**
```
Use consistent spacing scale:
4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px

Small spacing: 8px
Medium spacing: 16px
Large spacing: 24px
```

**Tip 4: Absolute Position Layers**
```
Remove from Auto-Layout: Right-click → Absolute Position
Use for: Badges, overlays, floating elements
```

---

# Part 4: Prototyping & Interactions

## 4.1 Creating Prototypes

**Prototype = Interactive mockup**

**Setup:**
1. Switch to Prototype tab (right panel)
2. Select layer (e.g., button)
3. Drag connection to target frame
4. Configure interaction

---

## 4.2 Interaction Types

**On Click:**
```
Trigger: Click/Tap
Action: Navigate to → Target Frame
Transition: Instant, Dissolve, Move, Slide, Push
Duration: 300ms (default)
Easing: Ease In/Out
```

**On Hover:**
```
Trigger: While hovering
Action: Change to → Button/Hover variant
Use for: Hover states
```

**On Press:**
```
Trigger: While pressing
Action: Change to → Button/Pressed variant
Use for: Active states
```

**After Delay:**
```
Trigger: After delay
Action: Navigate to → Next Frame
Delay: 2000ms
Use for: Auto-advance, splash screens
```

---

## 4.3 Smart Animate (Magic Animations)

**Smart Animate = Auto-animate matching layers**

**Requirements:**
- Layers have **same name** in both frames
- Frames connected with Smart Animate transition

**Example: Modal Animation**
```
Frame 1: Home
├─ Button "Open Modal"
└─ Modal (0% opacity, scale 0.8)

Frame 2: Home with Modal
├─ Button "Open Modal"
└─ Modal (100% opacity, scale 1.0)  ← Same name!

Interaction:
Button → On Click → Frame 2 (Smart Animate, 300ms)

Result: Modal fades in and scales up smoothly!
```

**Smart Animate Use Cases:**
- Expand/collapse cards
- Modal open/close
- Progress bars
- Loading spinners
- Page transitions

---

## 4.4 Overflow Behavior

**Horizontal/Vertical Scrolling:**
```
1. Select frame (e.g., long content)
2. Prototype tab → Overflow behavior
3. Choose: Horizontal scroll / Vertical scroll

Use for: Long lists, galleries, carousels
```

**Fixed Position (Sticky Header):**
```
1. Select layer (e.g., header)
2. Prototype tab → Fix position when scrolling

Use for: Sticky nav, floating buttons
```

---

## 4.5 Prototype Preview & Sharing

**Preview:**
```
1. Click Present button (top-right)
2. Or: Press Cmd/Ctrl + Enter
3. Test interactions in browser
```

**Share Prototype:**
```
1. Click Share button
2. Choose: "Anyone with link can view"
3. Copy link → Send to stakeholders
4. Options:
   - Show prototype only (no design)
   - Allow comments
   - Password protect
```

**Mobile Preview:**
```
Download Figma Mirror app (iOS/Android)
Test prototype on real device
```

---

# Part 5: Design Systems & Libraries

## 5.1 Styles (Reusable Properties)

**Color Styles:**
```
1. Select layer with color
2. Fill section → Click style icon (+)
3. Name: "Primary/500" or "Text/Primary"
4. Save

Usage: Apply color style to any layer (auto-updates)
```

**Text Styles:**
```
1. Select text layer
2. Text section → Click style icon
3. Name: "Heading 1" or "Body/Regular"
4. Save (includes font, size, weight, line-height)

Usage: Apply text style (updates everywhere)
```

**Effect Styles (Shadows, Blurs):**
```
1. Add drop shadow to layer
2. Effects section → Click style icon
3. Name: "Shadow/Medium"
4. Save

Usage: Consistent shadows across design
```

**Grid Styles:**
```
1. Add layout grid to frame
2. Grid section → Click style icon
3. Name: "12-Column Grid"
4. Save

Usage: Consistent grid system
```

---

## 5.2 Design Tokens

**Design Tokens = Design decisions as data**

**Token Types:**
```
Colors:
├─ Primary/500: #3B82F6
├─ Gray/100: #F3F4F6
└─ Success/500: #10B981

Spacing:
├─ Space/1: 4px
├─ Space/2: 8px
├─ Space/3: 12px
└─ Space/4: 16px

Typography:
├─ Font/Heading: Inter Bold 24px/1.2
└─ Font/Body: Inter Regular 16px/1.5

Border Radius:
├─ Radius/SM: 4px
├─ Radius/MD: 8px
└─ Radius/LG: 16px
```

**Export Tokens:**
```
Plugins:
- Design Tokens (export JSON)
- Style Dictionary (convert to CSS/iOS/Android)
- Tokens Studio (advanced token management)
```

---

## 5.3 Component Libraries

**Team Library = Shared components across files**

**Publish Library:**
```
1. Create components in file
2. File → Publish Library
3. Add description, version
4. Click Publish

Result: Components available to team
```

**Use Library:**
```
1. Other file → Assets panel
2. Click book icon (Team Libraries)
3. Enable your library
4. Drag components from Assets

Updates: When library updated, Figma prompts to update instances
```

**Library Structure:**
```
Foundation Library:
├─ Colors (styles)
├─ Typography (styles)
├─ Spacing (variables)
└─ Grids (styles)

Component Library:
├─ Buttons
├─ Form inputs
├─ Cards
├─ Navigation
└─ Modals

Icons Library:
├─ Icon/Arrow
├─ Icon/Check
└─ Icon/Close
```

---

## 5.4 Variables (Figma's New Feature)

**Variables = Dynamic values (colors, numbers, strings)**

**Create Variables:**
```
1. Right panel → Variables icon
2. Create collection: "Light Theme"
3. Add variables:
   - Color/Primary: #3B82F6
   - Color/Background: #FFFFFF
   - Spacing/Base: 8

4. Create collection: "Dark Theme"
   - Color/Primary: #3B82F6
   - Color/Background: #1F2937
   - Spacing/Base: 8
```

**Apply Variables:**
```
1. Select layer
2. Fill → Click variable icon
3. Choose: Color/Primary

Result: Layer color linked to variable (switches with theme!)
```

**Variable Modes (Themes):**
```
Collection: Theme
Modes:
├─ Light
└─ Dark

Variables:
├─ Color/Background
│   ├─ Light: #FFFFFF
│   └─ Dark: #1F2937
└─ Color/Text
    ├─ Light: #111827
    └─ Dark: #F9FAFB

Usage: Switch mode → entire design updates!
```

---

# Part 6: Plugins & Automation

## 6.1 Essential Plugins

**Content Generation:**
```
Content Reel            Real user data (names, photos, text)
Unsplash                Free stock photos
Iconify                 Icon library (100,000+ icons)
Lorem ipsum             Placeholder text
```

**Design Tools:**
```
Remove BG               Remove image backgrounds
Stark                   Accessibility checker (contrast, color blind)
Autoflow                Draw user flow diagrams
Chart                   Create charts/graphs
```

**Development:**
```
Anima                   Export to HTML/CSS/React
Zeplin                  Design handoff (specs, assets)
Figmotion               Advanced animations
Design Lint             Check design consistency
```

**Productivity:**
```
Similayer               Select similar layers
Sorter                  Sort layers alphabetically
Instance Finder         Find all component instances
Rename It               Batch rename layers
```

---

## 6.2 FigJam (Figma's Whiteboard)

**FigJam = Collaborative brainstorming**

**Use Cases:**
- User journey mapping
- Brainstorming sessions
- Wireframing (low-fidelity)
- Team workshops
- Sticky notes, voting

**Tools:**
```
Shapes                  Rectangles, circles, arrows
Sticky notes            Post-its (drag from toolbar)
Text                    Type anywhere
Connectors              Link elements (auto-routing)
Stamp                   Emoji reactions
Timer                   Time-box activities
```

---

## 6.3 Figma API & Automation

**REST API:**
```javascript
// Get file data
const fileKey = 'YOUR_FILE_KEY';
const response = await fetch(
  `https://api.figma.com/v1/files/${fileKey}`,
  {
    headers: {
      'X-Figma-Token': 'YOUR_ACCESS_TOKEN'
    }
  }
);
const data = await response.json();
console.log(data);
```

**Plugin API (JavaScript):**
```javascript
// Example: Export all components as PNG
figma.currentPage.findAll(node => node.type === 'COMPONENT').forEach(async component => {
  const bytes = await component.exportAsync({ format: 'PNG', constraint: { type: 'SCALE', value: 2 } });
  figma.ui.postMessage({ name: 'export', bytes, componentName: component.name });
});
```

**Use Cases:**
- Automated design token export
- Bulk component updates
- Design linting (check naming, colors)
- Screenshot generation for documentation

---

# Part 7: Collaboration & Dev Mode

## 7.1 Collaboration Features

**Comments:**
```
Shortcut: C (comment mode)
- Click anywhere → Add comment
- @ mention teammates
- Resolve when done
```

**Cursors & Live Collaboration:**
```
- See teammates' cursors in real-time
- See what they're editing
- Zoom to their viewport (click avatar)
```

**Version History:**
```
File → Show version history
- See all changes (auto-saved every 30 min)
- Restore previous version
- Name versions ("v1.0 - Final Design")
```

**Branching:**
```
File → New branch
- Experiment without affecting main file
- Merge back when ready
- Use for: Feature exploration, A/B testing
```

---

## 7.2 Dev Mode (Design Handoff)

**Dev Mode = Specs & code export for developers**

**Enable Dev Mode:**
```
1. Top-right → Dev Mode toggle
2. Developer plan required (or free for small teams)
```

**Features:**
```
Inspect
├─ CSS code (copy-paste)
├─ iOS Swift code
├─ Android XML code
└─ Measurements (spacing, sizes)

Assets
├─ Export images (SVG, PNG, JPG)
├─ Download icons
└─ Copy SVG code

Code Syntax
├─ Tailwind CSS
├─ CSS-in-JS
└─ React Native
```

**Example: CSS Export**
```
Select button → Dev Mode → Copy CSS

.button {
  width: 120px;
  height: 44px;
  background: #3B82F6;
  border-radius: 8px;
  font-family: Inter;
  font-size: 16px;
  font-weight: 600;
  color: #FFFFFF;
}
```

---

## 7.3 Design Handoff Best Practices

**For Designers:**
✅ Use clear layer names (Button, Header, Footer - not Layer 1, Group 12)
✅ Organize layers in logical groups
✅ Mark exportable assets (File → Export settings)
✅ Add component descriptions (usage notes)
✅ Use consistent spacing (8px grid)
✅ Document design decisions in comments

**For Developers:**
✅ Use Dev Mode to inspect (not Design Mode)
✅ Export assets in required formats (SVG for icons, PNG for photos)
✅ Check responsive behavior (constraints, auto-layout)
✅ Verify colors match design system
✅ Ask questions in comments (don't guess!)

---

# Part 8: Advanced Techniques

## 8.1 Component Properties (Advanced)

**Conditional Visibility:**
```
Component: Notification
Properties:
├─ Type: Success | Error | Warning | Info
└─ Show Icon: Boolean

Logic:
- If Type = Success → Icon color = Green
- If Type = Error → Icon color = Red
- If Show Icon = False → Hide icon layer
```

**Text Properties with Placeholder:**
```
Component: Input Field
Properties:
├─ Label: "Email"
├─ Placeholder: "Enter your email"
└─ Value: (empty)

Conditional:
- If Value empty → Show placeholder (gray)
- If Value filled → Show value (black)
```

---

## 8.2 Boolean Operations (Vector Editing)

**Combine Shapes:**
```
Union (Cmd/Ctrl + Alt + U)
└─ Merge shapes (OR)

Subtract (Cmd/Ctrl + Alt + S)
└─ Cut out shape (NOT)

Intersect (Cmd/Ctrl + Alt + I)
└─ Keep overlap only (AND)

Exclude (Cmd/Ctrl + Alt + X)
└─ Remove overlap (XOR)
```

**Example: Icon Creation**
```
1. Create circle (100×100)
2. Create smaller circle inside (60×60)
3. Select both → Subtract
4. Result: Ring icon
```

---

## 8.3 Performance Optimization

**Large Files:**
```
Slow file? Try:
├─ Reduce image resolution (max 2× for Retina)
├─ Flatten unused layers (Cmd/Ctrl + E)
├─ Remove unused components
├─ Archive old pages
└─ Split into multiple files (use Team Library)
```

**Component Optimization:**
```
├─ Use instances (not duplicates)
├─ Avoid deep nesting (max 3 levels)
├─ Use boolean properties (not multiple variants)
└─ Detach instances if no longer needed
```

---

## ✅ Final Summary Checklist

### Fundamentals
- [ ] Understand Frames vs Groups
- [ ] Use keyboard shortcuts fluently
- [ ] Apply constraints for responsive design

### Components
- [ ] Create components with variants
- [ ] Use component properties (text, boolean, instance swap)
- [ ] Build nested components
- [ ] Follow naming conventions

### Auto-Layout
- [ ] Create responsive layouts (Hug, Fill, Fixed)
- [ ] Use nested auto-layout
- [ ] Apply consistent spacing (8px grid)

### Prototyping
- [ ] Create interactive prototypes
- [ ] Use Smart Animate for transitions
- [ ] Add overflow scrolling
- [ ] Share prototypes with stakeholders

### Design Systems
- [ ] Create color, text, effect styles
- [ ] Set up design tokens
- [ ] Publish team libraries
- [ ] Use variables for themes

### Collaboration
- [ ] Comment and @ mention teammates
- [ ] Use version history
- [ ] Enable Dev Mode for handoff
- [ ] Export assets correctly

### Advanced
- [ ] Use plugins (Content Reel, Iconify, Stark)
- [ ] Optimize file performance
- [ ] Create complex variants with conditions
- [ ] Automate with Figma API

---

## 🎓 Congratulations!

You've mastered **Figma** - the industry-standard design tool!

**Total Content:** ~1,800 lines of Figma expertise

**Next Steps:**
1. Practice daily (build real projects!)
2. Join Figma Community (free resources, templates)
3. Watch Config (Figma's annual conference)
4. Contribute to design system in your team

**Resources:**
- Figma Learn: https://www.figma.com/resources/learn-design/
- Figma Community: https://www.figma.com/community
- Config Videos: https://config.figma.com
- YouTube: Figma (official channel)

Good luck designing! 🎨🚀

---
