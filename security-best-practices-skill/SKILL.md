---
name: security-best-practices-skill
description: Master application security and secure coding practices. Use for: OWASP Top 10 vulnerabilities, authentication/authorization, input validation, SQL injection prevention, XSS protection, CSRF tokens, secure password handling, API security, encryption, security headers, penetration testing, and building secure, hack-resistant applications.. Also use for Thai keywords "เขียนโค้ด", "โปรแกรม", "พัฒนา", "coding", "programming", "สถาปัตยกรรม", "โครงสร้าง", "ออกแบบระบบ", "architecture"
---

# 🔒 Security Best Practices Skill

**Version:** 1.0
**Last Updated:** 2025-10-26
**Expertise Level:** Expert

---

## 📋 Table of Contents

1. [Security Fundamentals](#security-fundamentals)
2. [OWASP Top 10 Vulnerabilities](#owasp-top-10)
3. [Authentication & Authorization](#authentication-authorization)
4. [Input Validation & Sanitization](#input-validation)
5. [SQL Injection Prevention](#sql-injection)
6. [XSS Protection](#xss-protection)
7. [CSRF Protection](#csrf-protection)
8. [Password Security](#password-security)
9. [API Security](#api-security)
10. [Encryption & Hashing](#encryption-hashing)
11. [Security Headers](#security-headers)
12. [Security Testing](#security-testing)

---

## 🎯 Security Fundamentals

### CIA Triad

**Core Security Principles:**
```
┌─────────────────────────────────┐
│    Confidentiality              │  ← Only authorized access
│    Integrity                    │  ← Data not tampered
│    Availability                 │  ← Service always accessible
└─────────────────────────────────┘
```

---

### Defense in Depth

**Multiple Security Layers:**
```
Layer 1: Network Security (Firewall, VPN)
Layer 2: Application Security (Input validation)
Layer 3: Data Security (Encryption)
Layer 4: Access Control (Authentication)
Layer 5: Monitoring (Logging, Alerts)
```

**Principle:** No single layer is perfect. Multiple layers ensure security even if one fails.

---

### Security by Design

**Rules:**
- ✅ Security from day one (not an afterthought)
- ✅ Principle of least privilege
- ✅ Fail securely (errors don't expose data)
- ✅ Never trust user input
- ✅ Defense in depth

---

## 🚨 OWASP Top 10 Vulnerabilities

### 1. Broken Access Control

**Problem:** Users accessing resources they shouldn't.

```javascript
// ❌ Vulnerable - No access control
app.get('/api/user/:id', (req, res) => {
  const user = db.getUser(req.params.id);
  res.json(user);  // Any user can access any user's data!
});

// ✅ Secure - Proper access control
app.get('/api/user/:id', authenticate, (req, res) => {
  const requestedId = req.params.id;
  const currentUserId = req.user.id;

  // Users can only access their own data
  if (requestedId !== currentUserId && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' });
  }

  const user = db.getUser(requestedId);
  res.json(user);
});
```

---

### 2. Cryptographic Failures

**Problem:** Sensitive data exposed due to weak encryption.

```javascript
// ❌ Vulnerable - Plaintext password
db.save({ email, password });  // NEVER!

// ✅ Secure - Hashed password
const bcrypt = require('bcrypt');
const hashedPassword = await bcrypt.hash(password, 10);
db.save({ email, password: hashedPassword });

// ❌ Vulnerable - Weak encryption
const encrypted = Buffer.from(data).toString('base64');  // NOT encryption!

// ✅ Secure - Strong encryption
const crypto = require('crypto');
const algorithm = 'aes-256-gcm';
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16);

const cipher = crypto.createCipheriv(algorithm, key, iv);
let encrypted = cipher.update(data, 'utf8', 'hex');
encrypted += cipher.final('hex');
const authTag = cipher.getAuthTag();
```

---

### 3. Injection Attacks

**Covered in detail:** [SQL Injection Prevention](#sql-injection)

---

### 4. Insecure Design

**Problem:** Security not considered in architecture.

**✅ Secure Design Patterns:**
```javascript
// Rate limiting
const rateLimit = require('express-rate-limit');
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 100,  // Limit each IP to 100 requests per window
  message: 'Too many requests from this IP'
});
app.use('/api/', limiter);

// Account lockout after failed attempts
const loginAttempts = {};

app.post('/login', (req, res) => {
  const ip = req.ip;

  if (loginAttempts[ip] >= 5) {
    return res.status(429).json({
      error: 'Account locked. Try again in 30 minutes.'
    });
  }

  // ... login logic
  if (loginFailed) {
    loginAttempts[ip] = (loginAttempts[ip] || 0) + 1;
  }
});
```

---

### 5. Security Misconfiguration

**Common Mistakes:**

```javascript
// ❌ Vulnerable - Debug mode in production
app.set('env', 'development');  // Exposes stack traces!

// ✅ Secure
app.set('env', 'production');

// ❌ Vulnerable - Default credentials
const dbPassword = 'admin';  // NEVER!

// ✅ Secure - Environment variables
const dbPassword = process.env.DB_PASSWORD;

// ❌ Vulnerable - Unnecessary features enabled
app.use(bodyParser.json({ limit: '50mb' }));  // Too large!

// ✅ Secure - Reasonable limits
app.use(bodyParser.json({ limit: '1mb' }));
```

---

### 6. Vulnerable Components

**Problem:** Using outdated libraries with known vulnerabilities.

```bash
# Check for vulnerabilities
npm audit

# Fix automatically
npm audit fix

# Update dependencies
npm update

# package.json - Use specific versions
{
  "dependencies": {
    "express": "4.18.2",  // Not "^4.0.0" or "*"
    "bcrypt": "5.1.0"
  }
}
```

---

### 7. Authentication Failures

**Covered in detail:** [Authentication & Authorization](#authentication-authorization)

---

### 8. Software & Data Integrity Failures

**Problem:** Code or data modified without verification.

```javascript
// ✅ Verify file integrity
const crypto = require('crypto');

function verifyFileIntegrity(filePath, expectedHash) {
  const hash = crypto.createHash('sha256');
  const fileBuffer = fs.readFileSync(filePath);
  hash.update(fileBuffer);
  const actualHash = hash.digest('hex');

  if (actualHash !== expectedHash) {
    throw new Error('File integrity check failed!');
  }
}

// ✅ Use Subresource Integrity (SRI) for CDN scripts
<script
  src="https://cdn.example.com/lib.js"
  integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
  crossorigin="anonymous">
</script>
```

---

### 9. Logging & Monitoring Failures

**Problem:** Attacks not detected because no logging.

```javascript
// ✅ Comprehensive logging
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

// Log security events
app.post('/login', (req, res) => {
  if (loginFailed) {
    logger.warn({
      event: 'failed_login',
      ip: req.ip,
      email: req.body.email,
      timestamp: new Date()
    });
  }
});

// Log access to sensitive data
app.get('/api/admin/users', (req, res) => {
  logger.info({
    event: 'admin_access',
    user: req.user.id,
    resource: '/admin/users',
    timestamp: new Date()
  });
});
```

---

### 10. Server-Side Request Forgery (SSRF)

**Problem:** Attacker tricks server into making requests.

```javascript
// ❌ Vulnerable - No URL validation
app.get('/fetch', async (req, res) => {
  const url = req.query.url;
  const response = await fetch(url);  // Attacker can access internal servers!
  res.send(response);
});

// ✅ Secure - Whitelist allowed domains
const ALLOWED_DOMAINS = ['api.example.com', 'cdn.example.com'];

app.get('/fetch', async (req, res) => {
  const url = new URL(req.query.url);

  if (!ALLOWED_DOMAINS.includes(url.hostname)) {
    return res.status(403).json({ error: 'Domain not allowed' });
  }

  // Block internal IP ranges
  const ip = await dns.lookup(url.hostname);
  if (ip.startsWith('192.168.') || ip.startsWith('10.') || ip === '127.0.0.1') {
    return res.status(403).json({ error: 'Internal IP not allowed' });
  }

  const response = await fetch(url);
  res.send(response);
});
```

---

## 🔐 Authentication & Authorization

### Authentication (Who are you?)

**Password-Based Authentication:**

```javascript
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Register
app.post('/register', async (req, res) => {
  const { email, password } = req.body;

  // Validate password strength
  if (password.length < 8) {
    return res.status(400).json({ error: 'Password too short' });
  }

  // Hash password
  const hashedPassword = await bcrypt.hash(password, 10);

  // Save user
  await db.users.create({ email, password: hashedPassword });

  res.json({ message: 'User created' });
});

// Login
app.post('/login', async (req, res) => {
  const { email, password } = req.body;

  // Find user
  const user = await db.users.findOne({ email });
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // Verify password
  const isValid = await bcrypt.compare(password, user.password);
  if (!isValid) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // Create JWT token
  const token = jwt.sign(
    { userId: user.id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: '1h' }
  );

  res.json({ token });
});
```

---

### Multi-Factor Authentication (MFA)

```javascript
const speakeasy = require('speakeasy');
const qrcode = require('qrcode');

// Setup MFA
app.post('/mfa/setup', authenticate, async (req, res) => {
  const secret = speakeasy.generateSecret({
    name: `MyApp (${req.user.email})`
  });

  // Save secret to user
  await db.users.update(req.user.id, { mfaSecret: secret.base32 });

  // Generate QR code
  const qrCodeUrl = await qrcode.toDataURL(secret.otpauth_url);

  res.json({ qrCode: qrCodeUrl, secret: secret.base32 });
});

// Verify MFA token
app.post('/mfa/verify', authenticate, (req, res) => {
  const { token } = req.body;

  const verified = speakeasy.totp.verify({
    secret: req.user.mfaSecret,
    encoding: 'base32',
    token: token,
    window: 2  // Allow 2 time steps before/after
  });

  if (!verified) {
    return res.status(401).json({ error: 'Invalid MFA token' });
  }

  res.json({ message: 'MFA verified' });
});
```

---

### Authorization (What can you do?)

**Role-Based Access Control (RBAC):**

```javascript
// Middleware to check roles
function authorize(allowedRoles) {
  return (req, res, next) => {
    if (!req.user) {
      return res.status(401).json({ error: 'Not authenticated' });
    }

    if (!allowedRoles.includes(req.user.role)) {
      return res.status(403).json({ error: 'Not authorized' });
    }

    next();
  };
}

// Usage
app.get('/api/admin/users',
  authenticate,
  authorize(['admin']),
  (req, res) => {
    // Only admins can access
  }
);

app.delete('/api/posts/:id',
  authenticate,
  authorize(['admin', 'moderator']),
  (req, res) => {
    // Admins and moderators can delete
  }
);
```

---

## 📝 Input Validation & Sanitization

### Never Trust User Input!

```javascript
const validator = require('validator');

// ❌ Vulnerable - No validation
app.post('/user', (req, res) => {
  const { email, age, website } = req.body;
  db.save({ email, age, website });  // Dangerous!
});

// ✅ Secure - Validate everything
app.post('/user', (req, res) => {
  const { email, age, website } = req.body;

  // Validate email
  if (!validator.isEmail(email)) {
    return res.status(400).json({ error: 'Invalid email' });
  }

  // Validate age
  if (!Number.isInteger(age) || age < 0 || age > 150) {
    return res.status(400).json({ error: 'Invalid age' });
  }

  // Validate URL
  if (website && !validator.isURL(website)) {
    return res.status(400).json({ error: 'Invalid website' });
  }

  // Sanitize inputs
  const sanitizedData = {
    email: validator.normalizeEmail(email),
    age: parseInt(age, 10),
    website: website ? validator.trim(website) : null
  };

  db.save(sanitizedData);
  res.json({ message: 'User created' });
});
```

---

### Whitelist vs Blacklist

```javascript
// ❌ Blacklist (incomplete, easy to bypass)
function isValidUsername(username) {
  const blacklist = ['<', '>', '&', '"', "'"];
  return !blacklist.some(char => username.includes(char));
}

// ✅ Whitelist (secure, explicit)
function isValidUsername(username) {
  const whitelist = /^[a-zA-Z0-9_-]+$/;
  return whitelist.test(username) && username.length >= 3 && username.length <= 20;
}
```

---

## 💉 SQL Injection Prevention

### The Problem

```javascript
// ❌ VULNERABLE TO SQL INJECTION!
app.get('/user', (req, res) => {
  const userId = req.query.id;
  const query = `SELECT * FROM users WHERE id = ${userId}`;
  //                                              ↑ User input directly in query!
  db.query(query, (err, result) => {
    res.json(result);
  });
});

// Attack: /user?id=1 OR 1=1  (Returns all users!)
// Attack: /user?id=1; DROP TABLE users;  (Deletes table!)
```

---

### Solution: Parameterized Queries

```javascript
// ✅ SECURE - Parameterized queries
app.get('/user', (req, res) => {
  const userId = req.query.id;
  const query = 'SELECT * FROM users WHERE id = ?';
  //                                             ↑ Placeholder
  db.query(query, [userId], (err, result) => {
    //              ↑ Value passed separately
    res.json(result);
  });
});

// OR using named parameters
const query = 'SELECT * FROM users WHERE id = :id';
db.query(query, { id: userId });
```

---

### ORM (Object-Relational Mapping)

```javascript
// ✅ SECURE - ORM handles escaping automatically
const { User } = require('./models');

app.get('/user', async (req, res) => {
  const userId = req.query.id;

  // Sequelize (Node.js)
  const user = await User.findByPk(userId);

  // Prisma
  const user = await prisma.user.findUnique({
    where: { id: userId }
  });

  res.json(user);
});
```

---

## 🛡️ XSS Protection

### Cross-Site Scripting (XSS)

**Problem:** Attacker injects malicious JavaScript into your site.

**Types:**
1. **Stored XSS** - Saved to database
2. **Reflected XSS** - In URL parameters
3. **DOM-based XSS** - Client-side JS manipulation

---

### Stored XSS Prevention

```javascript
// ❌ Vulnerable - Renders user input as HTML
app.get('/comments', async (req, res) => {
  const comments = await db.getComments();
  const html = comments.map(c => `<p>${c.text}</p>`).join('');
  //                                    ↑ If c.text = "<script>alert('XSS')</script>"
  res.send(html);
});

// ✅ Secure - Escape HTML
const escapeHtml = require('escape-html');

app.get('/comments', async (req, res) => {
  const comments = await db.getComments();
  const html = comments.map(c => `<p>${escapeHtml(c.text)}</p>`).join('');
  //                                    ↑ Converts < to &lt;, > to &gt;, etc.
  res.send(html);
});

// ✅ Better - Use template engine with auto-escaping
// React, Vue, Angular auto-escape by default
<p>{comment.text}</p>  {/* React automatically escapes */}
```

---

### Reflected XSS Prevention

```javascript
// ❌ Vulnerable - Search query reflected in page
app.get('/search', (req, res) => {
  const query = req.query.q;
  res.send(`<h1>Results for: ${query}</h1>`);
  //                          ↑ Attack: /search?q=<script>alert('XSS')</script>
});

// ✅ Secure - Escape output
app.get('/search', (req, res) => {
  const query = escapeHtml(req.query.q);
  res.send(`<h1>Results for: ${query}</h1>`);
});
```

---

### Content Security Policy (CSP)

```javascript
// ✅ Prevent inline scripts from executing
app.use((req, res, next) => {
  res.setHeader(
    'Content-Security-Policy',
    "default-src 'self'; script-src 'self' https://trusted-cdn.com; style-src 'self' 'unsafe-inline';"
  );
  next();
});

// This blocks:
<script>alert('XSS')</script>  // ❌ Blocked (inline script)
<script src="https://evil.com/malware.js"></script>  // ❌ Blocked (untrusted domain)

// This allows:
<script src="/app.js"></script>  // ✅ Allowed (same origin)
<script src="https://trusted-cdn.com/lib.js"></script>  // ✅ Allowed (whitelisted)
```

---

## 🔓 CSRF Protection

### Cross-Site Request Forgery

**Problem:** Attacker tricks user into making unwanted requests.

**Attack Example:**
```html
<!-- Attacker's website -->
<img src="https://bank.com/transfer?to=attacker&amount=1000">
<!-- If user is logged into bank.com, this executes! -->
```

---

### Solution: CSRF Tokens

```javascript
const csrf = require('csurf');
const csrfProtection = csrf({ cookie: true });

// Add CSRF token to forms
app.get('/form', csrfProtection, (req, res) => {
  res.render('form', { csrfToken: req.csrfToken() });
});

// Verify CSRF token on submission
app.post('/transfer', csrfProtection, (req, res) => {
  // CSRF token automatically verified
  // If invalid, request is rejected
  const { to, amount } = req.body;
  performTransfer(to, amount);
  res.json({ message: 'Transfer successful' });
});
```

**HTML Form:**
```html
<form method="POST" action="/transfer">
  <input type="hidden" name="_csrf" value="{{csrfToken}}">
  <input type="text" name="to">
  <input type="number" name="amount">
  <button>Transfer</button>
</form>
```

---

### SameSite Cookies

```javascript
// ✅ Modern browsers support SameSite attribute
res.cookie('sessionId', sessionId, {
  httpOnly: true,      // Not accessible via JavaScript
  secure: true,        // Only sent over HTTPS
  sameSite: 'strict',  // Not sent on cross-site requests
  maxAge: 3600000      // 1 hour
});

// SameSite options:
// - 'strict': Never sent on cross-site requests
// - 'lax': Sent on top-level navigation (e.g., clicking link)
// - 'none': Always sent (requires secure: true)
```

---

## 🔑 Password Security

### Password Hashing

```javascript
const bcrypt = require('bcrypt');

// ❌ NEVER store plaintext passwords!
db.save({ email, password });  // NEVER!

// ❌ NEVER use weak hashing!
const hash = crypto.createHash('md5').update(password).digest('hex');  // NEVER!

// ✅ Use bcrypt (or argon2, scrypt)
const saltRounds = 10;  // Higher = more secure but slower
const hashedPassword = await bcrypt.hash(password, saltRounds);
db.save({ email, password: hashedPassword });

// Verify password
const isValid = await bcrypt.compare(inputPassword, storedHash);
```

---

### Password Strength Requirements

```javascript
function validatePassword(password) {
  const errors = [];

  if (password.length < 8) {
    errors.push('Password must be at least 8 characters');
  }

  if (!/[a-z]/.test(password)) {
    errors.push('Password must contain lowercase letter');
  }

  if (!/[A-Z]/.test(password)) {
    errors.push('Password must contain uppercase letter');
  }

  if (!/[0-9]/.test(password)) {
    errors.push('Password must contain number');
  }

  if (!/[!@#$%^&*]/.test(password)) {
    errors.push('Password must contain special character');
  }

  // Check against common passwords
  const commonPasswords = ['password', '12345678', 'qwerty'];
  if (commonPasswords.includes(password.toLowerCase())) {
    errors.push('Password too common');
  }

  return errors;
}
```

---

### Password Reset Security

```javascript
const crypto = require('crypto');

// Generate secure reset token
app.post('/forgot-password', async (req, res) => {
  const { email } = req.body;
  const user = await db.users.findOne({ email });

  if (!user) {
    // Don't reveal if email exists!
    return res.json({ message: 'If email exists, reset link sent' });
  }

  // Generate random token
  const resetToken = crypto.randomBytes(32).toString('hex');
  const resetTokenHash = crypto.createHash('sha256').update(resetToken).digest('hex');

  // Save hashed token with expiration
  await db.users.update(user.id, {
    resetToken: resetTokenHash,
    resetTokenExpires: Date.now() + 3600000  // 1 hour
  });

  // Send email with token
  const resetUrl = `https://example.com/reset-password?token=${resetToken}`;
  await sendEmail(user.email, 'Password Reset', resetUrl);

  res.json({ message: 'If email exists, reset link sent' });
});

// Verify token and reset password
app.post('/reset-password', async (req, res) => {
  const { token, newPassword } = req.body;

  // Hash token to compare
  const tokenHash = crypto.createHash('sha256').update(token).digest('hex');

  const user = await db.users.findOne({
    resetToken: tokenHash,
    resetTokenExpires: { $gt: Date.now() }
  });

  if (!user) {
    return res.status(400).json({ error: 'Invalid or expired token' });
  }

  // Hash new password
  const hashedPassword = await bcrypt.hash(newPassword, 10);

  // Update password and clear reset token
  await db.users.update(user.id, {
    password: hashedPassword,
    resetToken: null,
    resetTokenExpires: null
  });

  res.json({ message: 'Password reset successful' });
});
```

---

## 🔌 API Security

### API Authentication

**Bearer Tokens (JWT):**

```javascript
// Middleware to verify JWT
function authenticate(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'No token provided' });
  }

  const token = authHeader.substring(7);  // Remove "Bearer "

  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}

// Usage
app.get('/api/protected', authenticate, (req, res) => {
  res.json({ message: 'Access granted', user: req.user });
});
```

---

### API Rate Limiting

```javascript
const rateLimit = require('express-rate-limit');

// General API rate limit
const apiLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,  // 15 minutes
  max: 100,  // Limit each IP to 100 requests per window
  message: 'Too many requests, please try again later',
  standardHeaders: true,
  legacyHeaders: false
});

app.use('/api/', apiLimiter);

// Stricter limit for authentication endpoints
const authLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,  // Only 5 login attempts per 15 minutes
  skipSuccessfulRequests: true  // Don't count successful logins
});

app.post('/api/login', authLimiter, loginHandler);
```

---

### API Input Validation

```javascript
const Joi = require('joi');

// Define schema
const userSchema = Joi.object({
  email: Joi.string().email().required(),
  age: Joi.number().integer().min(0).max(150).required(),
  name: Joi.string().min(3).max(50).required()
});

// Validate middleware
function validate(schema) {
  return (req, res, next) => {
    const { error, value } = schema.validate(req.body);

    if (error) {
      return res.status(400).json({
        error: error.details[0].message
      });
    }

    req.body = value;  // Use validated data
    next();
  };
}

// Usage
app.post('/api/user', validate(userSchema), (req, res) => {
  // req.body is now validated and sanitized
  db.save(req.body);
  res.json({ message: 'User created' });
});
```

---

## 🔐 Encryption & Hashing

### Encryption (Two-way)

**Use Case:** Encrypt data that needs to be decrypted later.

```javascript
const crypto = require('crypto');

class Encryption {
  constructor(encryptionKey) {
    this.algorithm = 'aes-256-gcm';
    this.key = Buffer.from(encryptionKey, 'hex');  // 32 bytes
  }

  encrypt(text) {
    const iv = crypto.randomBytes(16);
    const cipher = crypto.createCipheriv(this.algorithm, this.key, iv);

    let encrypted = cipher.update(text, 'utf8', 'hex');
    encrypted += cipher.final('hex');

    const authTag = cipher.getAuthTag();

    return {
      iv: iv.toString('hex'),
      encrypted: encrypted,
      authTag: authTag.toString('hex')
    };
  }

  decrypt(encryptedData) {
    const decipher = crypto.createDecipheriv(
      this.algorithm,
      this.key,
      Buffer.from(encryptedData.iv, 'hex')
    );

    decipher.setAuthTag(Buffer.from(encryptedData.authTag, 'hex'));

    let decrypted = decipher.update(encryptedData.encrypted, 'hex', 'utf8');
    decrypted += decipher.final('utf8');

    return decrypted;
  }
}

// Usage
const encryption = new Encryption(process.env.ENCRYPTION_KEY);

// Encrypt sensitive data before storing
const creditCard = '4111-1111-1111-1111';
const encrypted = encryption.encrypt(creditCard);
db.save({ creditCard: JSON.stringify(encrypted) });

// Decrypt when needed
const stored = JSON.parse(db.get().creditCard);
const decrypted = encryption.decrypt(stored);
console.log(decrypted);  // 4111-1111-1111-1111
```

---

### Hashing (One-way)

**Use Case:** Hash data that never needs to be retrieved (passwords, checksums).

```javascript
const crypto = require('crypto');

// SHA-256 hash
function hash(data) {
  return crypto.createHash('sha256').update(data).digest('hex');
}

// HMAC (Hash-based Message Authentication Code)
function hmac(data, secret) {
  return crypto.createHmac('sha256', secret).update(data).digest('hex');
}

// Usage
const fileHash = hash(fileContent);  // Verify file integrity
const signature = hmac(apiPayload, apiSecret);  // Sign API requests
```

---

## 🛡️ Security Headers

### Essential HTTP Headers

```javascript
const helmet = require('helmet');

// Use helmet (sets multiple security headers)
app.use(helmet());

// Or set manually:
app.use((req, res, next) => {
  // Prevent clickjacking
  res.setHeader('X-Frame-Options', 'DENY');

  // Prevent MIME sniffing
  res.setHeader('X-Content-Type-Options', 'nosniff');

  // Enable XSS filter
  res.setHeader('X-XSS-Protection', '1; mode=block');

  // Strict Transport Security (HTTPS only)
  res.setHeader('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');

  // Content Security Policy
  res.setHeader('Content-Security-Policy', "default-src 'self'");

  // Referrer Policy
  res.setHeader('Referrer-Policy', 'strict-origin-when-cross-origin');

  // Permissions Policy
  res.setHeader('Permissions-Policy', 'geolocation=(), microphone=()');

  next();
});
```

---

## 🧪 Security Testing

### Penetration Testing Checklist

**Authentication:**
- [ ] Test weak passwords
- [ ] Test account lockout
- [ ] Test session expiration
- [ ] Test password reset flow

**Authorization:**
- [ ] Test accessing other users' data
- [ ] Test privilege escalation
- [ ] Test forced browsing

**Input Validation:**
- [ ] Test SQL injection on all inputs
- [ ] Test XSS on all inputs
- [ ] Test file upload vulnerabilities
- [ ] Test special characters

**Session Management:**
- [ ] Test session fixation
- [ ] Test session hijacking
- [ ] Test concurrent sessions
- [ ] Test logout functionality

**Error Handling:**
- [ ] Test if errors reveal sensitive info
- [ ] Test stack traces in production
- [ ] Test error messages

---

### Automated Security Scanning

```bash
# npm audit - Check for vulnerable dependencies
npm audit

# OWASP ZAP - Web app security scanner
docker run -t owasp/zap2docker-stable zap-baseline.py -t https://example.com

# Snyk - Vulnerability scanning
npm install -g snyk
snyk test

# SonarQube - Code quality & security
docker run -d -p 9000:9000 sonarqube
```

---

### Security Testing Tools

**Static Analysis (SAST):**
- ESLint (JavaScript)
- Bandit (Python)
- Brakeman (Ruby)
- SonarQube (Multi-language)

**Dynamic Analysis (DAST):**
- OWASP ZAP
- Burp Suite
- Nmap
- Metasploit

**Dependency Scanning:**
- npm audit
- Snyk
- Dependabot
- WhiteSource

---

## ✅ Security Checklist

**Before Deployment:**
- [ ] All secrets in environment variables (not code)
- [ ] HTTPS enabled (SSL certificate)
- [ ] Security headers configured
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS protection (escape output)
- [ ] CSRF protection enabled
- [ ] Rate limiting configured
- [ ] Strong password policy
- [ ] Logging & monitoring enabled
- [ ] Error messages don't reveal sensitive info
- [ ] Dependencies up to date (no known vulnerabilities)
- [ ] Database access restricted
- [ ] File upload validation
- [ ] Session management secure
- [ ] Authentication & authorization tested
- [ ] Security testing completed

---

**Last Updated:** 2025-10-26
**Version:** 1.0
**Lines:** 1,500+
**Status:** Production Ready ✅
