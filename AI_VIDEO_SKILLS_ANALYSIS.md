# 🎬 AI Video Generation Skills Analysis

**Date:** 2025-10-24
**Context:** User ต้องการ skills สำหรับเขียน prompts สำหรับ Text-to-Video และ Image-to-Video

---

## 🎯 Problem Statement

**สิ่งที่ต้องการ:**
- เขียน prompts สำหรับ AI Video Generation
- ควบคุมมุมกล้อง (Camera Angles)
- ควบคุมการเคลื่อนไหวกล้อง (Camera Movements)
- เขียนเนื้อเรื่อง (Narrative/Story)
- ควบคุมการพูด/dialogue ของตัวละคร
- ควบคุมการเคลื่อนไหวตัวละคร (Character Actions)
- ออกแบบฉาก (Scene Design)

---

## 🔍 AI Video Platforms Analysis

### 1. **Runway Gen-3 Alpha**
- Text-to-Video (5-10s clips)
- Image-to-Video
- Camera controls: pan, tilt, zoom, orbit
- Motion control: speed, direction
- Prompt structure มีความสำคัญมาก

### 2. **Pika Labs 1.0**
- Text-to-Video
- Image-to-Video
- Camera controls
- Modify regions
- Extend video length

### 3. **Stable Video Diffusion**
- Image-to-Video
- Motion control
- Open source (customizable)

### 4. **Kling AI (Kuaishou)**
- Text-to-Video (5s, 720p/1080p)
- Image-to-Video
- High quality output
- Chinese platform (แต่มี English interface)

### 5. **Luma Dream Machine**
- Text-to-Video
- Fast generation (~120s)
- Natural motion

### 6. **HeyGen / D-ID**
- Avatar-based video
- Text-to-speech sync
- Presentation style

### 7. **Leonardo.ai Motion**
- Image-to-Video
- Motion strength control

---

## 📊 Recommended Skills to Create

### **Priority 1: Core Prompting** ⭐⭐⭐⭐⭐

#### 1. **ai-video-prompting-skill** (สำคัญที่สุด!)
**Purpose:** Expert prompting สำหรับ Text-to-Video และ Image-to-Video

**เนื้อหาควรมี:**
- Prompt structure ที่ทำงานได้ดีกับแต่ละ platform
- Camera angles vocabulary (wide shot, close-up, POV, bird's eye, etc.)
- Camera movements (pan, tilt, dolly, zoom, orbit, tracking shot)
- Lighting terminology (golden hour, studio lighting, volumetric)
- Motion descriptors (slow motion, fast, smooth, cinematic)
- Subject descriptions (detailed character/object)
- Scene/environment descriptions
- Style modifiers (cinematic, documentary, anime, etc.)
- Negative prompts (what to avoid)

**Example Prompt Structure:**
```
[Shot Type] of [Subject] [Action] in [Environment],
[Camera Movement], [Lighting], [Style], [Mood]

Example:
"Wide shot of a woman walking through Tokyo street at night,
slow dolly forward, neon lighting, cinematic style, moody atmosphere"
```

**ROI:** ⭐⭐⭐⭐⭐ (5/5)
- Claude รู้พื้นฐาน ~20% (video prompting ยังใหม่มาก)
- ประหยัดเวลา: 2-3 ชั่วโมงต่อโปรเจค (trial-error prompts)
- ใช้บ่อย: ถ้าทำงาน video generation ทุกวัน

---

#### 2. **cinematography-skill**
**Purpose:** ภาษาทางภาพยนตร์สำหรับควบคุม visual storytelling

**เนื้อหาควรมี:**
- Shot types (ECU, CU, MCU, MS, MLS, LS, ELS, etc.)
- Shot angles (eye level, low angle, high angle, Dutch angle)
- Camera movements (dolly, truck, pedestal, tilt, pan, zoom, handheld)
- Lens effects (wide angle, telephoto, bokeh, depth of field)
- Composition rules (rule of thirds, leading lines, symmetry)
- Lighting setups (3-point, Rembrandt, butterfly, rim)
- Color grading terminology
- Frame rates และ motion blur

**ROI:** ⭐⭐⭐⭐ (4/5)
- Claude รู้พื้นฐาน ~30% (ทั่วไป)
- จำเป็นสำหรับ professional output
- ใช้ร่วมกับ ai-video-prompting-skill

---

### **Priority 2: Platform-Specific** ⭐⭐⭐⭐

#### 3. **runway-prompting-skill**
**Purpose:** Runway Gen-3 specific prompting และ workflows

**เนื้อหาควรมี:**
- Runway Gen-3 prompt syntax
- Motion brush techniques
- Camera control parameters
- Best practices สำหรับ consistency
- Image-to-Video workflows
- Text-to-Video workflows
- Extend/interpolation techniques

**ROI:** ⭐⭐⭐⭐ (4/5)
- Platform-specific knowledge
- Runway เป็น industry standard

---

#### 4. **pika-prompting-skill**
**Purpose:** Pika Labs specific features

**เนื้อหาควรมี:**
- Pika 1.0 prompt structure
- Modify region feature
- Camera controls
- Sound effects generation
- Lip sync features

**ROI:** ⭐⭐⭐ (3/5)
- Pika มี unique features (modify region)
- แต่ยัง developing

---

### **Priority 3: Storytelling** ⭐⭐⭐⭐

#### 5. **video-storyboarding-skill**
**Purpose:** วางแผน video narrative และ shot sequences

**เนื้อหาควรมี:**
- Storyboard structure
- Shot sequencing
- Scene transitions
- Pacing and rhythm
- Visual continuity
- Character blocking
- Shot list creation
- Scene breakdown

**ROI:** ⭐⭐⭐⭐ (4/5)
- Essential สำหรับ multi-shot videos
- ช่วยวางแผนก่อน generate

---

#### 6. **character-animation-prompting-skill**
**Purpose:** ควบคุมการเคลื่อนไหวและ expressions ของตัวละคร

**เนื้อหาควรมี:**
- Action verbs (walking, running, dancing, gesturing)
- Facial expressions
- Body language
- Character interactions
- Movement speed/style
- Emotion portrayal
- Dialogue sync considerations

**ROI:** ⭐⭐⭐⭐ (4/5)
- Character-focused videos
- Hard to control without proper vocabulary

---

### **Priority 4: Technical** ⭐⭐⭐

#### 7. **video-consistency-skill**
**Purpose:** รักษา consistency across multiple shots

**เนื้อหาควรมี:**
- Character consistency techniques
- Style reference methods
- Color palette consistency
- Lighting consistency
- Setting/environment consistency
- Reference image workflows
- Seed control (platforms ที่รองรับ)

**ROI:** ⭐⭐⭐ (3/5)
- สำคัญสำหรับ series/longer videos
- แต่ยังมีข้อจำกัดทาง technical ของ AI

---

## 🎯 Recommended Implementation Plan

### Phase 1: Foundation (Priority 1) ✅
สร้าง 2 skills พื้นฐานก่อน:

1. **ai-video-prompting-skill** (ต้องมี!)
   - ครอบคลุม all platforms
   - Prompt engineering techniques
   - Camera + lighting vocabulary

2. **cinematography-skill**
   - Professional cinematography knowledge
   - Shot types, angles, movements
   - Composition และ lighting

**เหตุผล:**
- ใช้งานได้ทันทีกับทุก platform
- Foundation สำหรับทุกประเภท video
- ROI สูงสุด

---

### Phase 2: Platform Specific (ถ้าใช้งาน platform นั้นๆ)

3. **runway-prompting-skill** (ถ้าใช้ Runway)
4. **pika-prompting-skill** (ถ้าใช้ Pika)

---

### Phase 3: Advanced (ถ้าทำ complex projects)

5. **video-storyboarding-skill**
6. **character-animation-prompting-skill**
7. **video-consistency-skill**

---

## 💡 Key Insights

### 1. **AI Video Generation ยังใหม่มาก**
- Claude's knowledge: ~15-25% (ยังไม่ใช่ mainstream)
- Best practices ยัง evolving
- **ROI สูงมาก** ถ้าทำงานด้านนี้

### 2. **Prompt Engineering เป็นทักษะหลัก**
- การเขียน prompt ที่ดี = output ที่ดี 80%
- ต้องรู้ cinematography vocabulary
- แต่ละ platform มี syntax ต่างกัน

### 3. **Cross-Platform Knowledge**
- ควรสร้าง skill ที่ใช้ได้กับหลาย platforms
- ไม่ควร lock เฉพาะ platform เดียว (ยกเว้นมีเหตุผล)

### 4. **Visual Storytelling มีความสำคัญ**
- ไม่ใช่แค่ generate clips แยก
- ต้องมี narrative continuity
- Shot sequencing เป็น art

---

## 🚀 Quick Start Recommendation

**ถ้ามีเวลาจำกัด → สร้างแค่:**

### **ai-video-prompting-skill** (1 skill เดียว)

ครอบคลุม:
- ✅ Prompt structure (all platforms)
- ✅ Camera vocabulary
- ✅ Lighting and style
- ✅ Motion control
- ✅ Character animation basics
- ✅ Scene design
- ✅ Platform-specific tips (Runway, Pika, Kling, Luma)

**Size:** ~1,500-2,000 lines
**Time to create:** ~1-2 ชั่วโมง
**Value:** ใช้ได้ทันทีกับทุกงาน video generation

---

**ถ้ามีเวลา → สร้าง 2 skills:**

1. **ai-video-prompting-skill** (prompt engineering)
2. **cinematography-skill** (visual language)

**Combined value:** Professional-grade video prompts

---

## 📝 Sample Prompt Templates to Include

### Text-to-Video Template
```
[SHOT TYPE] of [SUBJECT] [ACTION] in [ENVIRONMENT],
[CAMERA MOVEMENT], [LIGHTING CONDITION], [TIME OF DAY],
[STYLE MODIFIER], [MOOD/ATMOSPHERE], [TECHNICAL SPECS]

Example:
Medium close-up of a woman sipping coffee in a modern café,
slow push-in, soft window lighting, late afternoon,
cinematic style, peaceful atmosphere, shallow depth of field
```

### Image-to-Video Template
```
[Starting with image], [CAMERA MOVEMENT], [SUBJECT MOVEMENT],
[MOTION SPEED], [STYLE CONSISTENCY], [DURATION PREFERENCE]

Example:
Starting with portrait, slow zoom out, subject turns head left,
smooth motion, maintain photographic style, 5 seconds
```

### Camera Movement Vocabulary
- **Static:** No camera movement
- **Pan:** Horizontal rotation (left/right)
- **Tilt:** Vertical rotation (up/down)
- **Dolly:** Camera moves forward/backward
- **Truck:** Camera moves left/right (parallel)
- **Pedestal:** Camera moves up/down (vertical)
- **Zoom:** Lens zoom in/out (no camera movement)
- **Orbit:** Camera circles around subject
- **Tracking shot:** Camera follows moving subject
- **Crane shot:** Sweeping vertical movement
- **Handheld:** Shaky, documentary style
- **Steadicam:** Smooth movement while walking

### Shot Types
- **ECU (Extreme Close-Up):** Eyes, lips, small details
- **CU (Close-Up):** Face fills frame
- **MCU (Medium Close-Up):** Head and shoulders
- **MS (Medium Shot):** Waist up
- **MLS (Medium Long Shot):** Knees up
- **LS (Long Shot):** Full body
- **ELS (Extreme Long Shot):** Establishing shot, landscape
- **POV (Point of View):** Camera is character's eyes
- **OTS (Over-The-Shoulder):** Looking past character

---

## ✅ Final Recommendation

**สำหรับ User นี้:**

### Option 1: Quick Start (1 skill)
สร้าง **ai-video-prompting-skill** เดียว
- เวลา: ~1-2 ชั่วโมง
- ครอบคลุม 80% use cases
- ใช้ได้ทันทีกับทุก platform

### Option 2: Professional (2 skills) ⭐ แนะนำ
สร้าง:
1. **ai-video-prompting-skill**
2. **cinematography-skill**

- เวลา: ~2-3 ชั่วโมง
- Professional-grade output
- ครอบคลุม 95% use cases

### Option 3: Complete Suite (7 skills)
สร้างครบทั้ง 7 skills
- เวลา: ~6-8 ชั่วโมง
- Platform-specific mastery
- Advanced workflows

---

**คำถามสำหรับ User:**

1. **ใช้ platform ไหนบ่อยสุด?** (Runway, Pika, Kling, Luma, อื่นๆ)
2. **ทำ video แบบไหน?** (Short clips, storytelling, commercial, etc.)
3. **มีเวลาเท่าไหร่?** (1-2 ชม. vs 6-8 ชม.)

**Recommendation ของผม:**
→ **เริ่มจาก Option 2** (ai-video-prompting-skill + cinematography-skill)
→ ครอบคลุมทุก use case แต่ไม่ใช้เวลามาก
→ สามารถเพิ่ม platform-specific skills ภายหลังได้ตามความต้องการ
