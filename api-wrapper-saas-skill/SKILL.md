---
name: api-wrapper-saas-skill
description: Master API Wrapper SaaS and API Reselling business models. Use for API Gateway design, API proxy architecture, wrapping third-party APIs (OpenAI, Anthropic, Stability AI, ElevenLabs), building SaaS on top of existing APIs, API monetization strategies, usage-based pricing, API key management, rate limiting, user authentication, subscription systems, payment integration, UI/UX for API products, API abstraction layers, multi-provider routing, cost optimization, and launching profitable API reselling businesses without building core technology. Also use for Thai keywords "ขาย API", "ห้อ API", "ทำ SaaS จาก API", "API Gateway", "ขายต่อ API", "OpenAI wrapper", "ต่อ API", "รายได้จาก API", "เก็บเงินตามใช้งาน", "จัดการ API key", "ระบบสมาชิก API", "ปั้นธุรกิจจาก API", "ทำเงินจาก API", "ขาย OpenAI", "ขาย ChatGPT API", "multi-provider", "ลดต้นทุน API".. Also use for Thai keywords "ธุรกิจ", "ทำธุรกิจ", "การทำธุรกิจ", "เขียนโค้ด", "โปรแกรม", "พัฒนา", "programming", "กลยุทธ์", "ยุทธศาสตร์", "วางแผน"
---

# API Wrapper SaaS Skill

> **Master the art of building profitable SaaS businesses by wrapping existing APIs with superior UX and monetization.**

---

## 📋 Table of Contents

1. [What is API Wrapper SaaS?](#what-is-api-wrapper-saas)
2. [Business Model Overview](#business-model-overview)
3. [Architecture Patterns](#architecture-patterns)
4. [Tech Stack Recommendations](#tech-stack-recommendations)
5. [API Integration Best Practices](#api-integration-best-practices)
6. [Monetization Strategies](#monetization-strategies)
7. [User Management & Authentication](#user-management--authentication)
8. [Usage Tracking & Billing](#usage-tracking--billing)
9. [Rate Limiting & Cost Control](#rate-limiting--cost-control)
10. [UI/UX Design Principles](#uiux-design-principles)
11. [Multi-Provider Strategy](#multi-provider-strategy)
12. [Legal & Compliance](#legal--compliance)
13. [Launch Checklist](#launch-checklist)
14. [Real-World Examples](#real-world-examples)

---

## What is API Wrapper SaaS?

**API Wrapper SaaS** is a business model where you:
1. Integrate with existing third-party APIs (OpenAI, Anthropic, Stability AI, etc.)
2. Add value through better UX, workflow automation, or specialized features
3. Charge customers for access through your platform
4. Handle billing, rate limiting, and user management
5. **Don't build the core AI/technology yourself**

**Alternative Names:**
- API Reselling
- API Gateway Business
- API Proxy SaaS
- Aggregator SaaS
- API-First SaaS

---

## Business Model Overview

### 💰 Revenue Models

#### 1. **Markup Pricing**
```
Your Cost:  OpenAI GPT-4: $0.03/1K tokens
Your Price: Your Platform: $0.05/1K tokens
Margin:     $0.02/1K tokens (66% markup)
```

#### 2. **Subscription + Usage**
```
Base Plan: $29/month (includes 100K tokens)
Overage:   $0.04/1K tokens (above quota)
```

#### 3. **Flat-Rate Unlimited** (risky but attractive)
```
Pro Plan:  $99/month (unlimited GPT-3.5)
Enterprise: $499/month (unlimited GPT-4)
```

#### 4. **Freemium Model**
```
Free:   1,000 requests/month
Starter: $19/month - 10,000 requests
Pro:    $99/month - 100,000 requests
```

### 🎯 Value Propositions (Why Users Pay You vs Direct API)

1. **Better UX**: Clean interface vs raw API calls
2. **No-Code Solution**: Non-developers can use AI tools
3. **Workflow Integration**: Connect multiple APIs in one flow
4. **Template Library**: Pre-built prompts and use cases
5. **Team Management**: Multi-user accounts with role-based access
6. **Unified Billing**: One invoice for multiple services
7. **Better Support**: Customer service vs reading docs
8. **Privacy/Compliance**: GDPR-compliant, SOC2, data handling
9. **Multi-Provider**: Auto-fallback if one provider is down
10. **Cost Optimization**: Automatic routing to cheapest provider

---

## Architecture Patterns

### Pattern 1: Simple Proxy (Basic)

```
User Request → Your Server → Third-Party API → Response
                  ↓
            Track Usage
            Apply Rate Limits
            Log for Billing
```

**Tech Stack:**
- Backend: Node.js/Express, Python/FastAPI, Go
- Database: PostgreSQL (user data, usage logs)
- Cache: Redis (rate limiting, API key validation)

**Code Example (Node.js):**
```javascript
// Simple OpenAI Proxy
app.post('/api/chat', authenticate, rateLimit, async (req, res) => {
  const { messages } = req.body;
  const userId = req.user.id;

  try {
    // Call OpenAI
    const response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: messages
    });

    // Track usage
    await trackUsage(userId, {
      tokens: response.usage.total_tokens,
      cost: calculateCost(response.usage),
      timestamp: new Date()
    });

    res.json(response);
  } catch (error) {
    handleAPIError(error, res);
  }
});
```

### Pattern 2: Aggregator (Multi-Provider)

```
User Request → Your Server → Route to Best Provider
                  ↓
        ┌─────────┼─────────┐
        ↓         ↓         ↓
    OpenAI   Anthropic   Cohere
        ↓         ↓         ↓
    Response ← Choose Best
```

**Routing Logic:**
```javascript
async function routeRequest(request, userPreferences) {
  // 1. Check user preference
  if (userPreferences.provider) {
    return providers[userPreferences.provider];
  }

  // 2. Check cost optimization
  if (userPreferences.optimize === 'cost') {
    return getCheapestProvider(request);
  }

  // 3. Check availability
  const available = await getHealthyProviders();

  // 4. Fallback logic
  return available[0] || fallbackProvider;
}
```

### Pattern 3: Workflow Builder (Advanced)

```
User Defines Workflow:
1. Generate image (Stability AI)
2. Describe image (GPT-4 Vision)
3. Create variations (DALL-E)

Your Platform:
- Orchestrates API calls
- Handles errors/retries
- Combines results
- Bills for entire workflow
```

**Database Schema:**
```sql
-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  api_key VARCHAR(64) UNIQUE,
  subscription_tier VARCHAR(50),
  created_at TIMESTAMP
);

-- Usage logs
CREATE TABLE usage_logs (
  id BIGSERIAL PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  endpoint VARCHAR(100),
  provider VARCHAR(50),
  tokens_used INTEGER,
  cost_usd DECIMAL(10, 6),
  timestamp TIMESTAMP,
  INDEX idx_user_timestamp (user_id, timestamp)
);

-- Rate limits
CREATE TABLE rate_limits (
  user_id UUID REFERENCES users(id),
  window_start TIMESTAMP,
  request_count INTEGER,
  PRIMARY KEY (user_id, window_start)
);
```

---

## Tech Stack Recommendations

### 🚀 Minimum Viable Product (MVP)

**Frontend:**
- Next.js (React framework with API routes)
- Tailwind CSS (rapid UI development)
- shadcn/ui (pre-built components)

**Backend:**
- Next.js API Routes (serverless, easy deployment)
- Vercel (hosting, zero-config)

**Database:**
- Supabase (PostgreSQL + Auth + realtime)
- Prisma ORM (type-safe queries)

**Payment:**
- Stripe (subscription + usage-based billing)

**Deployment:**
- Vercel (frontend + API)
- Railway/Render (if you need long-running servers)

**Total Time to MVP:** 2-4 weeks

### ⚡ Production-Ready Stack

**Frontend:**
- Next.js 14 (App Router)
- TypeScript (type safety)
- React Query (API state management)
- Zustand (client state)

**Backend:**
- Node.js + Express (if complex logic)
- Python + FastAPI (if heavy AI processing)
- Go (if high performance needed)

**Database:**
- PostgreSQL (primary data)
- Redis (caching, rate limiting, session)
- ClickHouse (analytics, usage logs)

**Infrastructure:**
- Docker + Kubernetes (scalability)
- AWS/GCP (enterprise needs)
- Cloudflare (CDN, DDoS protection)

**Monitoring:**
- Sentry (error tracking)
- PostHog (product analytics)
- Grafana + Prometheus (infrastructure)

---

## API Integration Best Practices

### 1. **Error Handling & Retries**

```javascript
async function callAPIWithRetry(apiCall, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await apiCall();
    } catch (error) {
      // Retry on rate limits or server errors
      if (error.status === 429 || error.status >= 500) {
        const delay = Math.pow(2, i) * 1000; // Exponential backoff
        await sleep(delay);
        continue;
      }
      throw error; // Don't retry on client errors
    }
  }
  throw new Error('Max retries exceeded');
}
```

### 2. **API Key Management**

```javascript
// Environment-based configuration
const API_KEYS = {
  openai: [
    process.env.OPENAI_KEY_1,
    process.env.OPENAI_KEY_2, // Backup key
    process.env.OPENAI_KEY_3  // Load balancing
  ],
  anthropic: [process.env.ANTHROPIC_KEY]
};

// Rotate keys for load balancing
function getAPIKey(provider) {
  const keys = API_KEYS[provider];
  const index = Math.floor(Math.random() * keys.length);
  return keys[index];
}
```

### 3. **Streaming Responses**

```javascript
// Stream API responses to user (better UX)
app.post('/api/stream', async (req, res) => {
  res.setHeader('Content-Type', 'text/event-stream');

  const stream = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: req.body.messages,
    stream: true
  });

  let totalTokens = 0;

  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content || '';
    res.write(`data: ${JSON.stringify({ content })}\n\n`);
    totalTokens += estimateTokens(content);
  }

  // Track usage after stream completes
  await trackUsage(req.user.id, totalTokens);
  res.end();
});
```

### 4. **Caching Strategy**

```javascript
// Cache identical requests (save costs)
async function getCachedResponse(request) {
  const cacheKey = hashRequest(request);

  // Check Redis cache
  const cached = await redis.get(cacheKey);
  if (cached) {
    return JSON.parse(cached);
  }

  // Call API if not cached
  const response = await callAPI(request);

  // Cache for 1 hour
  await redis.setex(cacheKey, 3600, JSON.stringify(response));

  return response;
}
```

---

## Monetization Strategies

### Strategy 1: Usage-Based Pricing (Recommended)

**Pros:**
- Fair: users pay for what they use
- Scales with customer value
- Predictable margins

**Cons:**
- Complex billing logic
- Bill shock risk

**Implementation:**
```javascript
// Pricing tiers
const PRICING = {
  'gpt-4': {
    input: 0.03,  // per 1K tokens
    output: 0.06
  },
  'gpt-3.5-turbo': {
    input: 0.001,
    output: 0.002
  }
};

// Add your margin (50%)
const YOUR_PRICING = Object.fromEntries(
  Object.entries(PRICING).map(([model, prices]) => [
    model,
    {
      input: prices.input * 1.5,
      output: prices.output * 1.5
    }
  ])
);
```

### Strategy 2: Credit System

**How it works:**
1. User buys credits upfront ($10 = 1,000 credits)
2. Each API call costs credits (GPT-4 = 10 credits/request)
3. Credits never expire (or expire in 1 year)

**Benefits:**
- Prepaid revenue (better cash flow)
- Reduces refund requests
- Easier pricing communication

**Code:**
```javascript
async function deductCredits(userId, amount) {
  const result = await db.query(
    'UPDATE users SET credits = credits - $1 WHERE id = $2 AND credits >= $1 RETURNING credits',
    [amount, userId]
  );

  if (result.rowCount === 0) {
    throw new Error('Insufficient credits');
  }

  return result.rows[0].credits;
}
```

### Strategy 3: Freemium + Upsells

**Free Tier:**
- 100 requests/month
- Basic models only (GPT-3.5)
- Community support

**Pro Tier ($29/month):**
- 5,000 requests/month
- All models (GPT-4, Claude, etc.)
- Email support
- API access

**Enterprise (Custom):**
- Unlimited requests
- Dedicated support
- SLA guarantees
- Custom integrations

---

## User Management & Authentication

### Authentication Methods

#### 1. **Session-Based (Web App)**
```javascript
// Login endpoint
app.post('/auth/login', async (req, res) => {
  const { email, password } = req.body;

  const user = await authenticateUser(email, password);

  req.session.userId = user.id;
  res.json({ success: true, user });
});
```

#### 2. **API Key (Developers)**
```javascript
// Generate unique API key
function generateAPIKey() {
  return `sk_${crypto.randomBytes(32).toString('hex')}`;
}

// Middleware to validate API key
async function authenticateAPIKey(req, res, next) {
  const apiKey = req.headers['x-api-key'];

  const user = await db.query(
    'SELECT * FROM users WHERE api_key = $1',
    [apiKey]
  );

  if (!user) {
    return res.status(401).json({ error: 'Invalid API key' });
  }

  req.user = user;
  next();
}
```

#### 3. **OAuth (Social Login)**
```javascript
// NextAuth.js example
import NextAuth from 'next-auth';
import GoogleProvider from 'next-auth/providers/google';

export default NextAuth({
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET
    })
  ],
  callbacks: {
    async session({ session, token }) {
      session.userId = token.sub;
      return session;
    }
  }
});
```

---

## Usage Tracking & Billing

### Real-Time Usage Tracking

```javascript
// Track every API call
async function trackUsage(userId, usage) {
  await db.query(`
    INSERT INTO usage_logs (user_id, endpoint, tokens_used, cost_usd, timestamp)
    VALUES ($1, $2, $3, $4, NOW())
  `, [userId, usage.endpoint, usage.tokens, usage.cost]);

  // Update user's current month usage
  await db.query(`
    UPDATE users
    SET current_month_usage = current_month_usage + $1
    WHERE id = $2
  `, [usage.cost, userId]);
}

// Get user's current usage
async function getCurrentUsage(userId) {
  const result = await db.query(`
    SELECT
      SUM(tokens_used) as total_tokens,
      SUM(cost_usd) as total_cost,
      COUNT(*) as request_count
    FROM usage_logs
    WHERE user_id = $1
      AND timestamp >= date_trunc('month', NOW())
  `, [userId]);

  return result.rows[0];
}
```

### Stripe Integration (Usage-Based)

```javascript
// Report usage to Stripe
async function reportUsageToStripe(userId, usage) {
  const user = await getUser(userId);

  if (!user.stripe_subscription_id) return;

  await stripe.subscriptionItems.createUsageRecord(
    user.stripe_subscription_item_id,
    {
      quantity: usage.tokens, // or cost in cents
      timestamp: Math.floor(Date.now() / 1000),
      action: 'increment'
    }
  );
}

// Stripe webhook for payment
app.post('/webhooks/stripe', async (req, res) => {
  const event = stripe.webhooks.constructEvent(
    req.body,
    req.headers['stripe-signature'],
    process.env.STRIPE_WEBHOOK_SECRET
  );

  switch (event.type) {
    case 'invoice.payment_succeeded':
      // Reset usage limits
      await resetUserUsage(event.data.object.customer);
      break;
    case 'invoice.payment_failed':
      // Suspend user access
      await suspendUser(event.data.object.customer);
      break;
  }

  res.json({ received: true });
});
```

---

## Rate Limiting & Cost Control

### Token Bucket Algorithm (Recommended)

```javascript
// Redis-based rate limiter
class RateLimiter {
  constructor(redis) {
    this.redis = redis;
  }

  async checkLimit(userId, limit, windowSeconds) {
    const key = `rate_limit:${userId}`;
    const now = Date.now();

    // Remove old entries outside window
    await this.redis.zremrangebyscore(key, 0, now - windowSeconds * 1000);

    // Count current requests
    const count = await this.redis.zcard(key);

    if (count >= limit) {
      const oldestEntry = await this.redis.zrange(key, 0, 0, 'WITHSCORES');
      const resetTime = parseInt(oldestEntry[1]) + windowSeconds * 1000;

      throw new Error(`Rate limit exceeded. Resets at ${new Date(resetTime)}`);
    }

    // Add current request
    await this.redis.zadd(key, now, `${now}-${Math.random()}`);
    await this.redis.expire(key, windowSeconds);

    return {
      allowed: true,
      remaining: limit - count - 1
    };
  }
}

// Middleware
async function rateLimitMiddleware(req, res, next) {
  const limiter = new RateLimiter(redis);
  const userTier = req.user.subscription_tier;

  const limits = {
    free: { requests: 100, window: 3600 },      // 100/hour
    pro: { requests: 1000, window: 3600 },      // 1000/hour
    enterprise: { requests: 10000, window: 3600 } // 10000/hour
  };

  const { requests, window } = limits[userTier];

  try {
    const result = await limiter.checkLimit(req.user.id, requests, window);
    res.setHeader('X-RateLimit-Remaining', result.remaining);
    next();
  } catch (error) {
    res.status(429).json({ error: error.message });
  }
}
```

### Cost Control (Daily Budget)

```javascript
// Check user's daily spend limit
async function checkBudgetLimit(userId) {
  const user = await getUser(userId);
  const todaySpend = await getTodaySpend(userId);

  if (todaySpend >= user.daily_budget_usd) {
    throw new Error('Daily budget exceeded. Resets at midnight UTC.');
  }
}

// Auto-suspend on overage
async function checkOverage(userId) {
  const usage = await getCurrentUsage(userId);
  const user = await getUser(userId);

  const quota = SUBSCRIPTION_QUOTAS[user.tier];

  if (usage.total_cost > quota.max_monthly_spend) {
    await db.query(
      'UPDATE users SET status = $1 WHERE id = $2',
      ['suspended', userId]
    );

    await sendEmail(user.email, {
      subject: 'Account Suspended - Usage Limit Exceeded',
      body: `Your monthly usage (${usage.total_cost}) exceeded your plan limit ($${quota.max_monthly_spend}).`
    });
  }
}
```

---

## UI/UX Design Principles

### 1. **Playground Interface** (Key Differentiator)

Instead of raw API:
```json
// Raw API (intimidating)
{
  "model": "gpt-4",
  "messages": [{"role": "user", "content": "Hello"}],
  "temperature": 0.7,
  "max_tokens": 500
}
```

Provide:
```
┌─────────────────────────────────────┐
│ 💬 Chat Playground                  │
├─────────────────────────────────────┤
│                                     │
│ Message: [Type your message...]    │
│                                     │
│ Model: [GPT-4 ▼]                   │
│ Temperature: [●────] 0.7           │
│ Max Length: [●──────] 500 tokens   │
│                                     │
│         [Generate Response]         │
└─────────────────────────────────────┘
```

**React Example:**
```jsx
export default function Playground() {
  const [message, setMessage] = useState('');
  const [model, setModel] = useState('gpt-4');
  const [response, setResponse] = useState('');

  async function handleSubmit() {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, model })
    });

    const data = await res.json();
    setResponse(data.content);
  }

  return (
    <div className="playground">
      <textarea
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message..."
      />

      <select value={model} onChange={(e) => setModel(e.target.value)}>
        <option value="gpt-4">GPT-4 ($0.05/1K tokens)</option>
        <option value="gpt-3.5-turbo">GPT-3.5 Turbo ($0.002/1K tokens)</option>
        <option value="claude-3-opus">Claude 3 Opus ($0.04/1K tokens)</option>
      </select>

      <button onClick={handleSubmit}>Generate</button>

      {response && (
        <div className="response">
          <ReactMarkdown>{response}</ReactMarkdown>
        </div>
      )}
    </div>
  );
}
```

### 2. **Template Library**

Pre-built prompts for common use cases:

```javascript
const TEMPLATES = [
  {
    id: 'blog-post',
    name: 'Blog Post Writer',
    description: 'Generate SEO-optimized blog posts',
    prompt: 'Write a comprehensive blog post about {topic}. Include: introduction, 3-5 main points, conclusion. Tone: {tone}. Length: {length} words.',
    variables: ['topic', 'tone', 'length']
  },
  {
    id: 'code-review',
    name: 'Code Reviewer',
    description: 'Review code for bugs and improvements',
    prompt: 'Review this {language} code and provide feedback on:\n1. Bugs\n2. Performance\n3. Best practices\n\n```{language}\n{code}\n```',
    variables: ['language', 'code']
  }
];
```

### 3. **Usage Dashboard**

```jsx
export default function UsageDashboard({ userId }) {
  const { data } = useQuery(['usage', userId], () =>
    fetch(`/api/usage/${userId}`).then(r => r.json())
  );

  return (
    <div className="dashboard">
      <div className="stat-card">
        <h3>This Month</h3>
        <div className="stat">{data.requestCount.toLocaleString()}</div>
        <p>requests</p>
      </div>

      <div className="stat-card">
        <h3>Tokens Used</h3>
        <div className="stat">{data.totalTokens.toLocaleString()}</div>
        <Progress value={data.tokenUsagePercent} />
      </div>

      <div className="stat-card">
        <h3>Current Bill</h3>
        <div className="stat">${data.totalCost.toFixed(2)}</div>
        <p>of ${data.monthlyQuota} quota</p>
      </div>

      <div className="chart">
        <h3>Daily Usage</h3>
        <LineChart data={data.dailyUsage} />
      </div>
    </div>
  );
}
```

---

## Multi-Provider Strategy

### When to Use Multiple Providers

**Benefits:**
1. **Redundancy**: If OpenAI is down, fallback to Anthropic
2. **Cost Optimization**: Route to cheapest provider
3. **Feature Coverage**: Use best model for each task
4. **Compliance**: Some regions require specific providers

### Provider Abstraction Layer

```javascript
// Abstract API differences
class AIProvider {
  async chat(messages, options) {
    throw new Error('Not implemented');
  }
}

class OpenAIProvider extends AIProvider {
  async chat(messages, options) {
    const response = await openai.chat.completions.create({
      model: options.model || 'gpt-4',
      messages: messages,
      temperature: options.temperature,
      max_tokens: options.maxTokens
    });

    return {
      content: response.choices[0].message.content,
      tokens: response.usage.total_tokens,
      cost: this.calculateCost(response.usage)
    };
  }
}

class AnthropicProvider extends AIProvider {
  async chat(messages, options) {
    const response = await anthropic.messages.create({
      model: options.model || 'claude-3-opus-20240229',
      messages: messages,
      temperature: options.temperature,
      max_tokens: options.maxTokens
    });

    return {
      content: response.content[0].text,
      tokens: response.usage.input_tokens + response.usage.output_tokens,
      cost: this.calculateCost(response.usage)
    };
  }
}

// Unified interface
class AIGateway {
  constructor() {
    this.providers = {
      openai: new OpenAIProvider(),
      anthropic: new AnthropicProvider(),
      cohere: new CohereProvider()
    };
  }

  async chat(messages, options = {}) {
    const provider = this.selectProvider(options);

    try {
      return await provider.chat(messages, options);
    } catch (error) {
      // Fallback to alternative provider
      const fallback = this.getFallbackProvider(provider);
      return await fallback.chat(messages, options);
    }
  }

  selectProvider(options) {
    // Custom routing logic
    if (options.optimize === 'cost') {
      return this.providers.openai; // GPT-3.5 is cheapest
    }

    if (options.optimize === 'quality') {
      return this.providers.anthropic; // Claude is best
    }

    return this.providers[options.provider] || this.providers.openai;
  }
}
```

---

## Legal & Compliance

### Terms of Service Requirements

**Must Include:**
1. **Prohibited Uses**: No illegal content, spam, abuse
2. **API Quotas**: Usage limits per tier
3. **Refund Policy**: Credits/subscriptions
4. **Data Retention**: How long you keep logs
5. **Liability Limits**: Not responsible for AI output
6. **Provider Attribution**: Mention underlying technology (OpenAI, etc.)

**Example Clause:**
> "This service uses third-party AI models including OpenAI GPT-4 and Anthropic Claude. We are not responsible for the accuracy, legality, or appropriateness of AI-generated content. Users must review all outputs before use."

### Privacy Policy (GDPR Compliance)

**Required Disclosures:**
1. **Data Collection**: What you collect (prompts, usage, email)
2. **Data Usage**: How you use it (billing, analytics)
3. **Data Sharing**: Third parties (OpenAI, Stripe, analytics)
4. **User Rights**: Access, deletion, export data
5. **Data Retention**: How long you keep logs

**Example:**
```
Data We Collect:
- Account info (email, name)
- API requests (prompts, responses)
- Usage metrics (tokens, costs)

Third-Party Sharing:
- OpenAI: API requests for processing
- Stripe: Payment processing
- PostHog: Anonymous analytics

Your Rights:
- Request data export (account settings)
- Delete your account (deletes all data within 30 days)
- Opt out of analytics
```

### Provider Terms Compliance

**OpenAI:**
- ✅ Allowed: Build apps on top
- ❌ Prohibited: Compete with OpenAI products (e.g., ChatGPT clone)
- ⚠️ Attribution: Mention "Powered by OpenAI" (recommended)

**Anthropic:**
- ✅ Allowed: Commercial use, reselling
- ❌ Prohibited: Training competing models
- ⚠️ Rate limits: Respect tier limits

**Stability AI:**
- ✅ Allowed: Commercial use
- ⚠️ License: Some models require attribution

**Always Read Provider TOS Before Launching!**

---

## Launch Checklist

### Pre-Launch (MVP)

- [ ] **Core Features**
  - [ ] User registration/login
  - [ ] API integration working
  - [ ] Usage tracking implemented
  - [ ] Rate limiting active
  - [ ] Payment integration (Stripe)

- [ ] **Legal**
  - [ ] Terms of Service written
  - [ ] Privacy Policy written
  - [ ] Cookie consent (if EU users)
  - [ ] Provider TOS reviewed

- [ ] **Security**
  - [ ] HTTPS enabled
  - [ ] Environment variables secured
  - [ ] API keys rotated regularly
  - [ ] SQL injection prevention
  - [ ] Rate limiting on auth endpoints

- [ ] **Monitoring**
  - [ ] Error tracking (Sentry)
  - [ ] Uptime monitoring (UptimeRobot)
  - [ ] Cost alerts (AWS Budgets, Stripe alerts)

### Post-Launch

- [ ] **Marketing**
  - [ ] Landing page with clear value prop
  - [ ] Demo video/screenshots
  - [ ] Documentation/API docs
  - [ ] Launch on ProductHunt, HackerNews

- [ ] **Customer Support**
  - [ ] Support email/chat
  - [ ] FAQ page
  - [ ] Status page (for outages)

- [ ] **Analytics**
  - [ ] User activation tracking
  - [ ] Conversion funnel analysis
  - [ ] Churn monitoring

---

## Real-World Examples

### 1. **ChatGPT Wrapper Examples**

**Jasper.ai** (acquired for $125M+)
- Wraps: OpenAI GPT models
- Value-add: Marketing copy templates, brand voice, team collaboration
- Pricing: $49-$125/month

**Copy.ai**
- Wraps: OpenAI GPT models
- Value-add: 90+ copywriting templates, workflow automation
- Pricing: $49/month (unlimited)

### 2. **Image Generation Wrappers**

**Playground.ai**
- Wraps: Stability AI, DALL-E
- Value-add: Better UI, editing tools, canvas
- Pricing: Freemium ($15/month Pro)

**Leonardo.ai**
- Wraps: Stable Diffusion
- Value-add: Model training, prompt magic
- Pricing: $12-$48/month

### 3. **Multi-Modal Wrappers**

**Descript**
- Wraps: OpenAI Whisper (transcription), ElevenLabs (TTS)
- Value-add: Video editing + AI tools integrated
- Pricing: $24-$50/month

### 4. **Developer Tools**

**Helicone.ai**
- Wraps: OpenAI, Anthropic APIs
- Value-add: Logging, caching, analytics for developers
- Pricing: Usage-based ($0.0001/request)

### 5. **Niche-Specific**

**Otter.ai** (Meeting Transcription)
- Wraps: Speech-to-text APIs
- Value-add: Meeting-specific features, integrations (Zoom, Teams)
- Pricing: $10-$30/user/month

---

## Quick Start Code Template

```bash
# Create Next.js app
npx create-next-app@latest my-api-wrapper --typescript --tailwind --app

cd my-api-wrapper

# Install dependencies
npm install @prisma/client openai stripe
npm install -D prisma

# Setup database
npx prisma init

# Create .env.local
cat > .env.local << EOF
DATABASE_URL="postgresql://user:pass@localhost:5432/mydb"
OPENAI_API_KEY="sk-..."
STRIPE_SECRET_KEY="sk_test_..."
NEXTAUTH_SECRET="your-secret"
EOF
```

**Minimal API Route** (`app/api/chat/route.ts`):
```typescript
import { NextRequest, NextResponse } from 'next/server';
import OpenAI from 'openai';
import { getServerSession } from 'next-auth';

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

export async function POST(req: NextRequest) {
  // 1. Authenticate
  const session = await getServerSession();
  if (!session) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  // 2. Parse request
  const { messages } = await req.json();

  // 3. Call OpenAI
  const completion = await openai.chat.completions.create({
    model: 'gpt-4',
    messages: messages
  });

  // 4. Track usage (simplified)
  await trackUsage(session.user.id, completion.usage.total_tokens);

  // 5. Return response
  return NextResponse.json({
    content: completion.choices[0].message.content,
    tokens: completion.usage.total_tokens
  });
}
```

---

## Common Pitfalls & Solutions

### Pitfall 1: Thin Margin Trap
**Problem**: Provider charges $0.03, you charge $0.035 (17% margin)
**Solution**: Charge 2-3x API cost OR add value beyond price

### Pitfall 2: Bill Shock
**Problem**: User runs up $1000 bill unexpectedly
**Solution**: Default spending limits, email alerts at 50%/80%/100%

### Pitfall 3: Provider Lock-In
**Problem**: Build entire product on OpenAI, they raise prices 50%
**Solution**: Abstract providers, support 2+ alternatives

### Pitfall 4: TOS Violation
**Problem**: Reselling without reading provider terms
**Solution**: Legal review, provider attribution, avoid prohibited uses

### Pitfall 5: No Differentiation
**Problem**: "It's just ChatGPT with a login"
**Solution**: Add templates, workflows, integrations, niche focus

---

## Success Metrics

**MVP Stage (Month 1-3):**
- 100 signups
- 10 paying customers
- $500 MRR (Monthly Recurring Revenue)
- 60% API cost margin

**Growth Stage (Month 6-12):**
- 1,000 signups
- 100 paying customers
- $5,000 MRR
- 70% gross margin

**Scale Stage (Year 2+):**
- 10,000+ users
- $50,000+ MRR
- Positive cash flow
- Team of 3-5

---

## Resources

### Tools & Services
- **API Providers**: OpenAI, Anthropic, Cohere, Stability AI, ElevenLabs
- **Payment**: Stripe, Paddle, LemonSqueezy
- **Auth**: NextAuth, Clerk, Supabase Auth
- **Database**: Supabase, PlanetScale, Neon
- **Hosting**: Vercel, Railway, Render, Fly.io
- **Monitoring**: Sentry, LogRocket, PostHog

### Learning Resources
- OpenAI API Docs: https://platform.openai.com/docs
- Stripe Usage-Based Billing: https://stripe.com/docs/billing/subscriptions/usage-based
- Next.js Docs: https://nextjs.org/docs

### Communities
- r/SaaS (Reddit)
- Indie Hackers
- MicroConf
- SaaS subreddits

---

## Final Thoughts

**API Wrapper SaaS is viable if you:**
1. ✅ Add 10x better UX than raw API
2. ✅ Target non-technical users or specific niche
3. ✅ Charge 2-3x API cost (healthy margin)
4. ✅ Build defensibility (data, integrations, brand)
5. ✅ Stay compliant with provider TOS

**It won't work if you:**
1. ❌ Compete with provider's own product (ChatGPT clone)
2. ❌ Have thin margins (<30%)
3. ❌ Offer no differentiation
4. ❌ Ignore legal/compliance
5. ❌ Can't justify price vs. direct API

**The key: Solve a SPECIFIC problem for a SPECIFIC audience using APIs as building blocks, not as the product itself.**

---

**Ready to build? Start with the Quick Start template above and launch your MVP in 2 weeks!** 🚀
