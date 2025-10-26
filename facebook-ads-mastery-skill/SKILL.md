---
name: facebook-ads-mastery-skill
description: Master Facebook Ads campaigns for maximum ROI and precise targeting. Use for: campaign strategy, interest targeting, audience segmentation, lookalike audiences, persona development, ad creative, placement optimization, budget allocation, metrics analysis (CTR, CPC, CPM, ROAS, CPA), A/B testing, conversion tracking, pixel implementation, and scaling profitable campaigns.
---

# Facebook Ads Mastery Skill

> **Master data-driven Facebook advertising for maximum ROI and precision targeting**

---

## 🎯 Core Principles

### 1. **Campaign Structure Hierarchy**

```
Business Manager
  └─ Ad Account
       └─ Campaign (Objective)
            └─ Ad Set (Audience + Placement + Budget)
                 └─ Ad (Creative + Copy)
```

**Best Practice:**
- 1 Campaign = 1 Objective
- 3-5 Ad Sets per Campaign (different audiences)
- 2-3 Ads per Ad Set (different creatives)

---

## 📊 Campaign Objectives Framework

### **Awareness Stage**
1. **Brand Awareness** - Maximize reach
2. **Reach** - Show to max people

### **Consideration Stage**
3. **Traffic** - Drive clicks to website
4. **Engagement** - Boost posts, page likes
5. **App Installs** - Drive downloads
6. **Video Views** - Watch video content
7. **Lead Generation** - Collect leads via forms
8. **Messages** - Start conversations

### **Conversion Stage**
9. **Conversions** - Drive purchases/actions
10. **Catalog Sales** - Dynamic product ads
11. **Store Traffic** - Drive offline visits

### **Choosing the Right Objective:**

| Goal | Objective |
|------|-----------|
| Build awareness | Brand Awareness / Reach |
| Drive website traffic | Traffic |
| Collect emails | Lead Generation |
| Sell products online | Conversions / Catalog Sales |
| Get app downloads | App Installs |
| Get messages/inquiries | Messages |
| Boost engagement | Engagement |

---

## 🎯 Audience Targeting Mastery

### **1. Core Audiences (Manual Targeting)**

#### **Demographics:**
- Age range (minimum 18+)
- Gender (All, Male, Female)
- Location (Country, Region, City, ZIP)
- Language
- Education level
- Job title
- Relationship status
- Life events (Engaged, Newlywed, New parent)

#### **Interests (The Gold Mine):**

**How to find winning interests:**

1. **Layered Targeting** (Narrow Audience)
   ```
   Interest 1: "Small Business Owners"
   AND
   Interest 2: "Accounting Software"
   = Hyper-targeted audience
   ```

2. **Broad + Narrow Stacking**
   ```
   Age: 25-65
   Interest: "Entrepreneurship"
   AND (Narrow): "Marketing"
   AND (Narrow): "Facebook Marketing"
   ```

3. **Competitor Targeting**
   ```
   Interests:
   - [Competitor Brand 1]
   - [Competitor Brand 2]
   - [Industry Magazine]
   - [Industry Influencer]
   ```

**Top Interest Categories:**

| Industry | Winning Interests |
|----------|-------------------|
| **E-commerce Fashion** | Online shopping, Fashion, [Competitor brands], Fashion bloggers |
| **B2B SaaS** | Small business, Entrepreneurship, [Tools they use], Business software |
| **Fitness** | Health and wellness, Gym, [Fitness influencers], Weight loss |
| **Real Estate** | Real estate, Home buying, [Local news], Property investment |
| **Education** | Online learning, [Skill topic], Professional development |

#### **Behaviors:**
- Purchase behavior (Engaged shoppers, High-value purchasers)
- Device usage (iPhone users, Android users)
- Travel (Frequent travelers, Commuters)
- Business (Small business owners, IT decision makers)

#### **Connections:**
- People who like your Page
- Friends of people who like your Page
- Exclude people who like your Page (prospecting)

---

### **2. Custom Audiences (Your Data)**

#### **Website Traffic (via Pixel):**
```
Pixel Events:
- View Content (visited product page)
- Add to Cart (added but didn't buy)
- Initiate Checkout (started checkout)
- Purchase (completed transaction)
- Lead (submitted form)
```

**Retargeting Funnel:**
```
30 days: All website visitors
14 days: Product page viewers (exclude buyers)
7 days: Cart abandoners (exclude buyers)
1 day: Checkout abandoners (HOT LEADS!)
```

**Pixel Implementation:**
```html
<!-- Facebook Pixel Base Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'YOUR_PIXEL_ID');
fbq('track', 'PageView');
</script>

<!-- Standard Events -->
<script>
fbq('track', 'ViewContent', {
  content_ids: ['1234'],
  content_type: 'product',
  value: 29.99,
  currency: 'USD'
});
</script>
```

#### **Customer List Upload:**
- Email list (existing customers)
- Phone numbers
- App user IDs

#### **Engagement Audiences:**
- Video viewers (25%, 50%, 75%, 95%)
- Instagram profile engagers
- Facebook Page engagers
- Lead form openers

---

### **3. Lookalike Audiences (Scaling Gold)**

**How it works:**
Facebook finds people similar to your best customers.

**Best Lookalike Sources:**
1. ✅ **Purchasers** (Top 1% - best ROI)
2. ✅ **High LTV Customers** (Top 5% spenders)
3. ✅ **Email Subscribers** (engaged list)
4. ✅ **Website Visitors** (180 days, min 1000 people)
5. ✅ **Engaged Video Viewers** (watched 75%+)

**Lookalike Size Strategy:**

| Audience % | Use Case | Quality |
|------------|----------|---------|
| 1% | Testing, highest quality | ⭐⭐⭐⭐⭐ |
| 2-3% | Scaling winners | ⭐⭐⭐⭐ |
| 5-6% | Broad reach | ⭐⭐⭐ |
| 10% | Max scale (lower quality) | ⭐⭐ |

**Advanced Stacking:**
```
1% Lookalike (Purchasers)
AND
Interest: [Related topic]
AND
Age: 25-54
= Hyper-targeted lookalike
```

---

## 👥 Persona Development for FB Ads

### **Framework: 5W Persona Builder**

For each persona, define:

#### **1. WHO are they?**
- Age range
- Gender
- Location
- Job title/role
- Income level
- Education

#### **2. WHAT do they want?**
- Primary goal
- Pain points
- Desires
- Frustrations
- Current solutions (competitors)

#### **3. WHERE do they hang out?**
- Facebook Groups they join
- Pages they follow
- Brands they like
- Influencers they follow
- Publications they read

#### **4. WHEN do they buy?**
- Time of day (check Ads Manager data)
- Day of week (weekday vs weekend)
- Season/month
- Trigger events (life events, holidays)

#### **5. WHY will they buy from YOU?**
- Unique value proposition
- Trust factors
- Social proof needed
- Objections to overcome

---

### **Example Persona: "Busy Mom Entrepreneur"**

```yaml
WHO:
  Age: 30-45
  Gender: Female
  Location: US, Urban/Suburban
  Job: Self-employed, Side hustler
  Income: $40k-80k
  Education: College graduate

WHAT:
  Goals:
    - Work from home flexibility
    - Extra income
    - Be present for kids
  Pain Points:
    - No time
    - Overwhelmed
    - Tech confusion
    - Analysis paralysis
  Desires:
    - Simple solutions
    - Step-by-step guidance
    - Community support
  Frustrations:
    - Complicated software
    - Hidden fees
    - Lack of support

WHERE:
  FB Groups:
    - "Boss Moms"
    - "Work From Home Moms"
    - "Side Hustle Nation"
  Pages:
    - Rachel Hollis
    - Amy Porterfield
    - Jenna Kutcher
  Brands:
    - Canva
    - Kajabi
    - ConvertKit
  Publications:
    - Entrepreneur Magazine
    - Inc.

WHEN:
  Best Times: 8-10pm (after kids sleep)
  Best Days: Tuesday-Thursday
  Season: January (New Year goals), September (back to school)
  Triggers: Maternity leave, Kids starting school

WHY (Our Angle):
  USP: "Done-for-you templates - No tech skills needed"
  Trust: Testimonials from other moms
  Social Proof: "10k+ moms using this"
  Objection: "30-day money back guarantee - Risk free"
```

**Targeting This Persona:**

```
Demographics:
- Women, 30-45
- US (all states)
- Married
- Parents (Children ages 3-12)

Interests (Narrow):
- Work from home
  AND
- Entrepreneurship
  AND
- Small business

Behaviors:
- Online shopping (engaged shoppers)
- Device: iPhone/iPad users
- Business: Small business owners

Exclude:
- People who purchased (retarget separately)
```

---

## 🎨 Ad Creative Best Practices

### **Image/Video Specs:**

| Placement | Recommended Size | Aspect Ratio |
|-----------|------------------|--------------|
| Feed | 1200 x 1200 px | 1:1 (square) |
| Stories/Reels | 1080 x 1920 px | 9:16 (vertical) |
| Carousel | 1080 x 1080 px | 1:1 (square) |

### **Creative Principles:**

#### **1. Pattern Interrupt (Stop the scroll)**
- Bright colors (contrasts with FB blue/white)
- Movement (in first 3 seconds for video)
- Faces looking at camera
- Text overlays (big, bold)
- Unexpected imagery

#### **2. Benefit-Focused**
```
❌ "Our software has 50 features"
✅ "Save 10 hours per week on admin tasks"
```

#### **3. Social Proof**
- Customer count: "Join 50,000+ users"
- Ratings: "4.9/5 stars (2,387 reviews)"
- Media mentions: "As seen on Forbes, Inc, Entrepreneur"
- Testimonials (with photo)

#### **4. Clear CTA**
- "Shop Now"
- "Learn More"
- "Get Started"
- "Claim Offer"
- "Download Free Guide"

### **Video Ad Formula (Hook-Story-CTA):**

```
0-3s: HOOK (pattern interrupt)
  → "Still wasting 2 hours daily on [pain]?"

3-15s: PROBLEM (agitate)
  → "Most [target audience] struggle with [pain]"

15-30s: SOLUTION (introduce product)
  → "That's why we created [product]"

30-45s: PROOF (testimonials/demo)
  → "See how Sarah saved [benefit]"

45-60s: CTA (clear action)
  → "Click below to get started free"
```

---

## 📍 Placement Optimization

### **Automatic Placements vs Manual:**

**Start:** Automatic (let FB optimize)

**After data:** Manual (turn off losers)

### **Placement Performance Ranking (General):**

1. ⭐⭐⭐⭐⭐ **Facebook Feed** (highest engagement)
2. ⭐⭐⭐⭐⭐ **Instagram Feed**
3. ⭐⭐⭐⭐ **Facebook Stories**
4. ⭐⭐⭐⭐ **Instagram Stories**
5. ⭐⭐⭐⭐ **Instagram Reels**
6. ⭐⭐⭐ **Facebook Right Column**
7. ⭐⭐⭐ **Messenger Inbox**
8. ⭐⭐ **Audience Network** (external apps - often lower quality)

### **When to Use Manual Placements:**

- E-commerce: Feed + Stories only (visual products)
- B2B: Feed + LinkedIn (if available)
- App installs: Stories + Reels (full screen)
- Lead gen: Feed only (forms work better)

---

## 💰 Budget & Bidding Strategy

### **Campaign Budget Optimization (CBO)**

**How it works:**
Set budget at campaign level → FB auto-distributes to best ad sets

**When to use:**
- ✅ Scaling proven campaigns
- ✅ Multiple similar audiences
- ✅ Budget > $50/day

**When NOT to use:**
- ❌ Testing new audiences (use ABO)
- ❌ Very different audiences
- ❌ Budget < $20/day

---

### **Ad Set Budget Optimization (ABO)**

**How it works:**
Set individual budgets per ad set

**When to use:**
- ✅ Testing phase
- ✅ Very different audiences (cold vs warm)
- ✅ Want manual control
- ✅ Small budgets

---

### **Budget Guidelines:**

| Campaign Type | Minimum Daily Budget | Recommended |
|---------------|---------------------|-------------|
| Testing new audience | $10/day | $20-50/day |
| Retargeting | $5/day | $10-30/day |
| Scaling winner | $50/day | $100-500/day |
| Lookalike testing | $20/day | $50-100/day |

**Budget Scaling Rule:**
Don't increase budget more than **20% per day** (causes learning reset)

```
Day 1: $50
Day 2: $60 (20% increase) ✅
Day 3: $72 (20% increase) ✅
NOT: Day 2: $100 (100% increase) ❌
```

---

### **Bidding Strategies:**

| Strategy | How It Works | Best For |
|----------|-------------|----------|
| **Lowest Cost** | FB gets cheapest results | Testing, small budgets |
| **Cost Cap** | Max cost per result | Profit margin control |
| **Bid Cap** | Max bid per auction | Advanced, high competition |
| **Target Cost** | Avg cost target | Stable CPA needed |

**Recommendation:** Start with **Lowest Cost** → Switch to **Cost Cap** after data.

---

## 📊 Metrics Analysis Framework

### **Key Metrics by Objective:**

#### **Awareness Campaigns:**
- **CPM** (Cost Per 1000 Impressions)
  - Good: < $10
  - Average: $10-20
  - High: > $20
- **Reach**
- **Frequency** (aim for 1-3)

#### **Traffic Campaigns:**
- **CPC** (Cost Per Click)
  - Good: < $0.50
  - Average: $0.50-1.50
  - High: > $1.50
- **CTR** (Click-Through Rate)
  - Good: > 2%
  - Average: 0.5-2%
  - Low: < 0.5%
- **Bounce Rate** (check GA)

#### **Conversion Campaigns:**
- **CPA** (Cost Per Acquisition)
  - Compare to LTV (Lifetime Value)
  - Target: CPA < 30% of LTV
- **ROAS** (Return on Ad Spend)
  - Good: > 4.0 (4x return)
  - Break-even: 2.0-3.0
  - Losing: < 2.0
- **Conversion Rate**
  - E-commerce: 1-3%
  - Lead gen: 5-15%
  - High-ticket: 0.5-2%

---

### **The Metrics Dashboard You Need:**

```
Campaign Performance:
┌─────────────────────────────────────────┐
│ Spend: $1,000                           │
│ Revenue: $4,500                         │
│ ROAS: 4.5x ✅                           │
│ Profit: $3,500                          │
└─────────────────────────────────────────┘

Traffic Metrics:
┌─────────────────────────────────────────┐
│ Impressions: 150,000                    │
│ Clicks: 3,000                           │
│ CTR: 2.0% ✅                            │
│ CPC: $0.33 ✅                           │
└─────────────────────────────────────────┘

Conversion Metrics:
┌─────────────────────────────────────────┐
│ Landing Page Visits: 3,000              │
│ Purchases: 90                           │
│ Conversion Rate: 3.0% ✅                │
│ CPA: $11.11                             │
│ AOV (Avg Order Value): $50              │
└─────────────────────────────────────────┘

Per-Ad Set Breakdown:
┌─────────────────────────────────────────┐
│ Ad Set 1 (Lookalike 1%): ROAS 5.2x ⭐  │
│ Ad Set 2 (Interest: Competitor): 3.8x  │
│ Ad Set 3 (Broad 25-65): 1.5x ❌ KILL   │
└─────────────────────────────────────────┘
```

---

### **Analysis Decision Tree:**

```
Is ROAS > Target?
├─ YES: Scale by 20% daily
└─ NO:
    ├─ Is CTR > 1%?
    │   ├─ YES: Landing page problem → Fix LP
    │   └─ NO: Ad creative problem → Test new ads
    │
    ├─ Is CPC > $2?
    │   ├─ YES: Audience too narrow → Broaden
    │   └─ NO: Creative issue → Test new hooks
    │
    └─ Is Frequency > 3?
        ├─ YES: Ad fatigue → New creative
        └─ NO: Offer/product-market fit issue
```

---

## 🧪 A/B Testing Framework

### **What to Test (Priority Order):**

1. **Audience** (biggest impact)
   - Cold vs Warm
   - Lookalike 1% vs 3%
   - Interest A vs Interest B

2. **Creative** (second biggest)
   - Image vs Video
   - Different hooks
   - Different visuals

3. **Copy** (third)
   - Headlines
   - Body copy
   - CTA wording

4. **Placement**
   - Feed only vs All placements
   - Stories vs Reels

5. **Offer**
   - 20% off vs Free shipping
   - Lead magnet A vs B

### **Testing Protocol:**

```
Step 1: Duplicate ad set
Step 2: Change ONE variable only
Step 3: Run both for 3-7 days
Step 4: Need min 1000 impressions each
Step 5: Check significance:
  - CTR difference > 0.5% = significant
  - CPC difference > 20% = significant
  - ROAS difference > 0.5x = significant
Step 6: Kill loser, scale winner
```

### **Statistical Significance Calculator:**

Need at least:
- **1000 impressions** per variation
- **50 clicks** per variation
- **10 conversions** per variation (for conversion tests)

Don't make decisions before reaching these minimums!

---

## 🚀 Scaling Strategy (The Winning Formula)

### **Phase 1: Testing (Week 1-2)**

```
Budget: $20-50/day per ad set
Goal: Find winners (ROAS > 3x)

Test:
- 3-5 audiences
- 2-3 creatives per audience
- Automatic placements
- Lowest cost bidding

Kill criteria:
- After 3 days, CPA > target → Kill
- After 5 days, ROAS < 2x → Kill
```

### **Phase 2: Validation (Week 3-4)**

```
Budget: $100-200/day
Goal: Confirm consistency

Action:
- Take winning ad set
- Run for 2 weeks
- Monitor daily

Success = ROAS stays > 3x
Fail = ROAS drops < 2x → back to testing
```

### **Phase 3: Scaling (Month 2+)**

**Vertical Scaling** (same ad set, more budget):
```
Day 1: $100
Day 2: $120 (+20%)
Day 3: $144 (+20%)
Day 4: $173 (+20%)
...
Week 2: $500+

⚠️ Watch for performance drops!
If ROAS drops > 20% → pause scaling
```

**Horizontal Scaling** (more ad sets):
```
Winning Ad Set: Lookalike 1% Purchasers
↓
Add:
- Lookalike 2-3% Purchasers
- Lookalike 1% Email List
- Lookalike 1% Video Viewers
- Interest stack (similar audiences)

Each new ad set: $50-100/day
Total budget: $300-500/day across all
```

---

## 🛠️ Advanced Tactics

### **1. Dynamic Product Ads (DPA)**

**Setup:**
1. Create Product Catalog (via Business Manager)
2. Install Pixel + Catalog events
3. Create Dynamic Ad template
4. Use "Catalog Sales" objective

**Best for:**
- E-commerce retargeting
- Cross-sells/upsells
- Abandoned cart recovery

**Template Variables:**
```
{{product.name}}
{{product.price}}
{{product.description}}
```

---

### **2. Lead Ads (Native Forms)**

**Benefits:**
- No landing page needed
- Pre-filled info (from FB profile)
- Mobile-optimized
- Higher conversion rates

**Setup:**
```
Objective: Lead Generation
↓
Create Form:
- Intro (headline + description)
- Questions (max 5 fields recommended)
- Privacy policy
- Thank you screen

Integration:
- Connect to CRM (Zapier, native integration)
- Or download CSV daily
```

---

### **3. Advantage+ Shopping Campaigns**

**What:** AI-powered campaigns (formerly Dynamic Ads)

**Best for:**
- E-commerce with product catalog
- Min $50/day budget
- Proven pixel data (50+ conversions/week)

**How it works:**
FB automates:
- Audience targeting
- Creative testing
- Placement optimization
- Budget distribution

**Your job:**
- Provide good creative
- Set budget
- Monitor ROAS

---

### **4. Retargeting Funnel (Complete System)**

```
Top of Funnel (Awareness):
┌───────────────────────────────────┐
│ Ad: Value content / Education     │
│ Audience: Cold (Interests/LAL)    │
│ Budget: 60% of total              │
└───────────────────────────────────┘
         ↓ (Pixel: View Content)

Middle Funnel (Consideration):
┌───────────────────────────────────┐
│ Ad: Social proof / Benefits       │
│ Audience: Website visitors 30d    │
│ Budget: 25% of total              │
└───────────────────────────────────┘
         ↓ (Pixel: Add to Cart)

Bottom Funnel (Conversion):
┌───────────────────────────────────┐
│ Ad: Discount / Urgency            │
│ Audience: Cart abandoners 7d      │
│ Budget: 15% of total              │
└───────────────────────────────────┘
         ↓ (Pixel: Purchase)

Post-Purchase:
┌───────────────────────────────────┐
│ Ad: Upsell / Cross-sell           │
│ Audience: Purchasers 30d          │
│ Exclude: Already bought upsell    │
└───────────────────────────────────┘
```

---

## 📱 iOS 14+ / Privacy Changes Adaptation

### **The Challenge:**
Apple's App Tracking Transparency (ATT) limits pixel tracking.

### **Solutions:**

#### **1. Conversions API (CAPI)**
Server-side tracking (bypasses iOS restrictions)

**Setup:**
- Implement on your server
- Use Facebook Conversion API
- Send events directly to FB (not via pixel)

#### **2. Aggregated Event Measurement**
- Verify domain
- Prioritize 8 conversion events
- Use manual attribution

#### **3. Modeling & Estimation**
FB estimates conversions (modeled data)

**Optimize for:**
- First-party data (email lists, phone numbers)
- Longer attribution windows (7-day click)
- Broader audiences (less affected)

---

## ✅ Pre-Launch Checklist

**Account Setup:**
- [ ] Business Manager created
- [ ] Ad Account added
- [ ] Payment method verified
- [ ] Facebook Pixel installed
- [ ] Pixel firing correctly (use Pixel Helper)
- [ ] Domain verified
- [ ] Conversion events set up

**Campaign Setup:**
- [ ] Objective matches goal
- [ ] Budget sufficient (min $10/day)
- [ ] Audience size 50k-2M (not too narrow/broad)
- [ ] Placements optimized
- [ ] Bidding strategy chosen

**Creative:**
- [ ] Image/video meets specs (1200x1200 min)
- [ ] Text < 20% of image (use Text Overlay tool)
- [ ] Ad copy proofread
- [ ] CTA button selected
- [ ] Landing page loads fast (<3s)
- [ ] Mobile-optimized

**Tracking:**
- [ ] Pixel events firing
- [ ] Conversions API (if available)
- [ ] UTM parameters in URL
- [ ] Google Analytics connected

**Compliance:**
- [ ] Ad follows FB policies
- [ ] No prohibited content
- [ ] Claims substantiated
- [ ] Privacy policy linked (for lead ads)

---

## 🚨 Common Mistakes to Avoid

### **1. Audience Too Narrow**
❌ 10,000 people
✅ 500,000 - 2,000,000 people

### **2. Not Enough Budget**
❌ $5/day testing 5 ad sets ($1/day each)
✅ $20/day per ad set minimum

### **3. Changing Too Soon**
❌ Editing ad after 1 day
✅ Wait 3-7 days for data

### **4. Too Many Variables**
❌ Testing audience + creative + copy simultaneously
✅ Test ONE thing at a time

### **5. Ignoring Mobile**
❌ Desktop-only optimized LP
✅ Mobile-first design (80%+ traffic is mobile)

### **6. No Retargeting**
❌ Cold traffic only
✅ 60% cold, 40% retargeting

### **7. Stopping Winners**
❌ "ROAS is good, let me change creative"
✅ Don't fix what's not broken! Duplicate and test separately.

### **8. Analysis Paralysis**
❌ Perfect audience research for weeks
✅ Ship fast, test, iterate

---

## 📚 Recommended Tools

### **Research & Spying:**
- **Facebook Ad Library** (free) - See all active ads
- **AdSpy** - Competitor ad research
- **BigSpy** - Find winning ads

### **Creative:**
- **Canva** - Ad images
- **InVideo / CapCut** - Video ads
- **Loom** - Quick video testimonials

### **Analytics:**
- **Facebook Ads Manager** (native)
- **Google Analytics** (traffic behavior)
- **Triple Whale** (e-commerce attribution)
- **Hyros** (advanced attribution)

### **Automation:**
- **Zapier** - Lead ads to CRM
- **Revealbot** - Auto rules (pause bad ads)
- **Madgicx** - AI optimization

---

## 🎯 Quick Win Templates

### **Template 1: E-commerce Product Launch**

```
Campaign: Conversions
Ad Set 1: Lookalike 1% (Past Purchasers) - $50/day
Ad Set 2: Interest Stack (Competitors) - $50/day
Ad Set 3: Broad 25-55 + Interest Layer - $30/day

Creative:
- Video: Unboxing + Benefits (30s)
- Image: Lifestyle shot + Social proof
- Carousel: 5 products / 5 benefits

Copy:
Headline: [Benefit + Number]
"Get Glowing Skin in 7 Days (Without Harsh Chemicals)"

Body:
- Problem (2 lines)
- Solution (your product)
- Proof (testimonials / results)
- CTA: "Shop Now - Free Shipping"

Budget: $130/day
Timeline: 7 days
KPI: ROAS > 3x
```

---

### **Template 2: B2B Lead Generation**

```
Campaign: Lead Generation
Ad Set 1: Job Title (Decision Makers) - $30/day
Ad Set 2: Lookalike 2% (Email List) - $30/day
Ad Set 3: Interest (Industry Tools) - $20/day

Creative:
- Static Image: Screenshot of lead magnet
- Text overlay: "Free Guide: [Outcome]"

Lead Form:
- Email (required)
- Name (required)
- Company (optional)
- "Download Now" CTA

Offer:
"Free Checklist: 10 Ways to [Solve Problem]"

Budget: $80/day
Timeline: 14 days
KPI: CPL < $15
```

---

### **Template 3: Webinar/Event Registration**

```
Campaign: Conversions
Ad Set 1: Warm (Email list LAL) - $40/day
Ad Set 2: Interest (Topic) - $40/day

Creative:
- Video: Talking head (you) + hook
  "On [Date] I'm revealing [big promise]"
- Thumbnail: Your face + text overlay

Copy:
"🔴 LIVE Training: [Big Promise]

[Date] at [Time]

You'll learn:
✅ [Outcome 1]
✅ [Outcome 2]
✅ [Outcome 3]

Seats limited → Reserve yours free"

Landing Page:
- Registration form (email + name)
- Countdown timer
- Social proof (attendees count)

Budget: $80/day
Timeline: 7-14 days before event
KPI: CPR (Cost per Registration) < $5
```

---

## 📖 Glossary

- **CPM**: Cost Per 1000 Impressions
- **CPC**: Cost Per Click
- **CTR**: Click-Through Rate (clicks ÷ impressions)
- **CPA**: Cost Per Acquisition (spend ÷ conversions)
- **ROAS**: Return on Ad Spend (revenue ÷ spend)
- **AOV**: Average Order Value
- **LTV**: Lifetime Value
- **Frequency**: Avg times same person saw ad
- **Relevance Score**: (Deprecated) Ad quality rating
- **LAL**: Lookalike Audience
- **CBO**: Campaign Budget Optimization
- **ABO**: Ad Set Budget Optimization
- **DPA**: Dynamic Product Ads
- **Pixel**: Facebook tracking code
- **CAPI**: Conversions API

---

## 🎓 Skill Mastery Path

### **Beginner (Month 1-3):**
- [ ] Set up Business Manager + Pixel
- [ ] Run first traffic campaign ($10/day)
- [ ] Create 5 different audiences
- [ ] Test 3 ad creatives
- [ ] Understand Ads Manager metrics
- [ ] Get first conversion

### **Intermediate (Month 4-6):**
- [ ] Build complete retargeting funnel
- [ ] Create lookalike audiences
- [ ] Scale campaign to $100/day
- [ ] Achieve ROAS > 3x consistently
- [ ] A/B test 10+ variations
- [ ] Master custom conversions

### **Advanced (Month 7-12):**
- [ ] Implement Conversions API
- [ ] Manage $500+/day profitably
- [ ] Build automated rules
- [ ] Multi-product campaigns
- [ ] Advanced attribution modeling
- [ ] Teach others FB Ads

---

## 🚀 Final Checklist: Am I Ready to Scale?

Before scaling to $500+/day, ensure:

- [ ] ROAS > 3x for 14+ days straight
- [ ] Profitable on at least 3 ad sets
- [ ] Retargeting funnel live
- [ ] Product/service can handle volume
- [ ] Conversion rate > 2% (e-com) or 10% (leads)
- [ ] Customer support ready
- [ ] Cash flow sufficient (ad spend paid upfront)
- [ ] Pixel tracking accurate
- [ ] Multiple creative variations ready
- [ ] Lookalike audiences built

---

**Remember:**
> "Data beats opinions. Test everything. Scale what works. Kill what doesn't. Repeat."

**Master these principles and you'll join the top 5% of Facebook advertisers.** 🚀
