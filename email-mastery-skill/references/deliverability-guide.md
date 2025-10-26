# Email Deliverability Guide: Avoid Spam, Reach the Inbox

## The Deliverability Crisis

**Reality Check:**
- Average inbox placement rate: 79% (21% go to spam/promotions)
- Cost of poor deliverability: Missing 1 in 5 customers
- Good deliverability: 95%+ inbox placement
- Excellent deliverability: 98%+ inbox placement

**Goal:** Maximize inbox placement, minimize spam folder placement

---

## The 4 Pillars of Deliverability

### Pillar 1: Technical Authentication (Foundation)

#### SPF (Sender Policy Framework)

**What it is:** Verifies you're authorized to send from your domain

**How to set up:**
```
1. Access your domain's DNS settings
2. Add TXT record:
   v=spf1 include:_spf.youresp.com ~all

   Replace "youresp.com" with your ESP's SPF record:
   - ConvertKit: include:_spf.convertkit.com
   - Mailchimp: include:servers.mcsv.net
   - ActiveCampaign: include:_spf.actcmp.com
   - SendGrid: include:sendgrid.net

3. Test with: mxtoolbox.com/spf.aspx
```

**Common mistakes:**
- Multiple SPF records (only 1 allowed)
- Missing "include" for ESP
- Using "+all" instead of "~all" (too permissive)

---

#### DKIM (DomainKeys Identified Mail)

**What it is:** Cryptographic signature proving email authenticity

**How to set up:**
```
1. Your ESP generates a public/private key pair
2. ESP provides you with DNS record
3. Add CNAME or TXT record to DNS
4. ESP signs outgoing emails with private key
5. Receiving servers verify with public key

Example DKIM record:
cm._domainkey.yourdomain.com CNAME cm._domainkey.youresp.com
```

**Testing:**
- Send email to mail-tester.com
- Check for green DKIM status

---

#### DMARC (Domain-based Message Authentication)

**What it is:** Policy telling servers what to do with failed authentication

**How to set up:**
```
1. Add TXT record to DNS:
   _dmarc.yourdomain.com

2. Record value (start with "none" policy):
   v=DMARC1; p=none; rua=mailto:dmarc@yourdomain.com

3. After monitoring, upgrade to:
   v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com
   (quarantine = send to spam if fails)

4. Eventually:
   v=DMARC1; p=reject; rua=mailto:dmarc@yourdomain.com
   (reject = don't deliver if fails)
```

**Policy levels:**
- p=none → Monitor only (start here)
- p=quarantine → Send to spam
- p=reject → Block entirely

**Why it matters:**
- Gmail/Outlook prioritize DMARC-authenticated senders
- Prevents spoofing/impersonation
- Shows you're legitimate

---

#### Custom Domain Sending

**Why it matters:**
- Sending from "@yourbusiness.com" vs "@convertkit.com"
- Builds domain reputation (not shared with others)
- Looks more professional
- Required for best deliverability

**How to set up:**
```
Most ESPs offer custom domain sending:

1. Verify domain ownership
2. Add DNS records (ESP provides)
3. Wait for verification (24-48 hours)
4. Start sending from your domain

Cost: Usually free, but some ESPs charge
```

---

### Pillar 2: Sender Reputation

#### Your Reputation Score

Email providers score your domain/IP based on:
- Complaint rate (aim: <0.1%)
- Bounce rate (aim: <2%)
- Spam trap hits (aim: 0)
- Engagement rates (opens, clicks, replies)
- Sending volume consistency
- List quality

**Check your reputation:**
- Google Postmaster Tools (for Gmail)
- Microsoft SNDS (for Outlook)
- SenderScore.org (overall score)

**Good score:** 90+
**Excellent score:** 95+

---

#### Warming Up New Domains/IPs

**Why warm-up matters:**
New senders have no reputation. Sudden high volume = spam filter trigger.

**Warm-up schedule (over 4-6 weeks):**

```
Week 1:
- Day 1: 50 emails to most engaged
- Day 2: 100 emails
- Day 3: 200 emails
- Day 4-7: 500 emails/day

Week 2:
- 1,000 emails/day

Week 3:
- 2,500 emails/day

Week 4:
- 5,000 emails/day

Week 5-6:
- 10,000+ emails/day (full volume)

Rules:
- Start with hottest subscribers (recent openers)
- Monitor bounce/complaint rates closely
- If issues arise, slow down
- Gradual increase only
```

**Tools for automated warm-up:**
- Mailwarm.com
- Lemwarm.com
- Warmup Inbox

---

#### Maintaining Good Reputation

**Do:**
- ✅ Send consistently (don't disappear then blast)
- ✅ Remove hard bounces immediately
- ✅ Clean list every 60-90 days
- ✅ Use double opt-in
- ✅ Make unsubscribe easy
- ✅ Monitor complaint rates
- ✅ Re-engage inactive subscribers
- ✅ Sunset unengaged (remove after 6-12 months)

**Don't:**
- ❌ Buy email lists (death sentence)
- ❌ Scrape emails
- ❌ Send to old lists (3+ years old)
- ❌ Ignore bounces/complaints
- ❌ Spike volume suddenly
- ❌ Hide unsubscribe link
- ❌ Send from free email (Gmail, Yahoo)

---

### Pillar 3: Content Quality

#### Spam Trigger Words (Use Sparingly or Avoid)

**Financial:**
- Free, $$$, 100% free, Save $, Earn $, Credit, Cash bonus
- Guarantee, No cost, Prize, Winner
- Act now, Limited time, Urgent

**Overpromising:**
- Amazing, Incredible, Unbelievable
- Once in a lifetime, Revolutionary
- Secret, Hidden, Exclusive (use carefully)

**Excessive urgency:**
- Click now!!!, Don't wait!!!, Hurry!!!
- Last chance!!!

**Spammy formatting:**
- ALL CAPS WORDS
- Excessive exclamation marks!!!!
- Weird spacing: F R E E
- Colored fonts (in HTML)

**Important:** These don't automatically = spam. Context matters. One "free" in subject is fine. "FREE!!! CLICK NOW!!!" is not.

---

#### Content Best Practices

**Text-to-Image Ratio:**
```
Ideal: 80% text, 20% images
Acceptable: 60% text, 40% images
Risky: 40% text, 60% images
Spam territory: All-image emails
```

**Why:** Spam filters can't read images. All-image emails look like spam.

**HTML Structure:**
```
✅ Do:
- Clean HTML (use ESP templates)
- Alt text for images
- Plain text version available
- Proper heading tags
- Mobile responsive
- Test in multiple clients

❌ Don't:
- Excessive CSS
- JavaScript (gets stripped)
- Forms in emails
- Complex tables
- Embedded videos (use thumbnail + link)
```

**Link Best Practices:**
```
✅ Do:
- Use HTTPS links
- Link to your domain
- Descriptive anchor text
- 3-5 links max per email

❌ Don't:
- URL shorteners (bit.ly, tinyurl)
- Too many links (10+)
- Links to suspicious domains
- Broken links
- Misleading anchor text
```

**Personalization:**
```
✅ Improves deliverability:
- Using subscriber's name
- Behavioral personalization
- Dynamic content blocks

Why: Shows email is targeted, not blasted
```

---

#### Subject Line Deliverability

**Spam triggers in subject lines:**

❌ Avoid:
```
"FREE!!! CLICK NOW!!!"
"You've won $1,000,000"
"URGENT: Act immediately"
"Re: Re: Re:" (when it's not a reply)
"Fwd:" (when it's not forwarded)
```

✅ Safe:
```
"{Name}, quick question"
"The 3 mistakes I see most often"
"Here's what worked for me"
"Your {topic} question answered"
"This reminded me of you"
```

**Testing:**
- SubjectLine.com (free spam check)
- Mail-tester.com (full email test)
- IsNotSpam.com

---

### Pillar 4: Engagement Optimization

#### Why Engagement Matters

Gmail/Outlook track:
- Opens (implied interest)
- Clicks (strong interest signal)
- Replies (strongest signal - "this is a real conversation")
- Forwards (social proof)
- Move to primary/inbox (user-initiated signal)
- Deletes without opening (negative signal)
- Mark as spam (very negative signal)

**High engagement = Better deliverability**

---

#### Engagement Tactics

**1. Segment by Engagement**
```
Hot (opened in 30 days):
- Send 3-7x/week
- Mix of content + offers

Warm (31-90 days):
- Send 2-3x/week
- More value, less selling

Cold (90+ days):
- Send 1x/month (re-engagement)
- Remove if no response after 3 attempts
```

**2. Re-engagement Campaigns**
```
Inactive for 60 days → Send:
"Are you still interested in {topic}?"

Options:
- Yes, keep me subscribed [link]
- No, unsubscribe [link]
- Change email frequency [link]

No response after 3 attempts → Remove
```

**3. Sunset Policy**
```
No opens in 180 days → Final email:
"We're removing you from our list in 7 days.
Click here to stay: [link]"

No click → Remove from list

Result: Higher average engagement, better deliverability
```

**4. Encourage Replies**
```
Tactics:
- "Hit reply and let me know..."
- "What's your biggest challenge with {topic}?"
- "I read every response"
- Make it personal, conversational

Why: Replies = strongest engagement signal
Gmail sees: "This is a real conversation, not spam"
```

**5. Whitelist Requests**
```
Welcome email:
"To make sure you get my emails, add me to your contacts:
1. Click the 3 dots in Gmail
2. Select 'Add {sender} to contacts'"

Or: "Drag this email to your Primary inbox"
```

---

## Email Provider Specific Tips

### Gmail (Biggest Provider - 1.8B users)

**Keys to Gmail deliverability:**

1. **Gmail Postmaster Tools**
   - Monitor reputation
   - Track spam rate
   - See authentication status
   - Free: postmaster.google.com

2. **Primary vs Promotions Tab**
   - Personal emails → Primary
   - Marketing emails → Promotions (usually)
   - To increase Primary placement:
     - More text, fewer images
     - Conversational tone
     - Encourage replies
     - No "unsubscribe" in text (keep in footer only)

3. **Gmail's Priorities:**
   - Engagement (opens, clicks, replies)
   - Not marked as spam
   - Proper authentication
   - Clean sending reputation

---

### Outlook/Microsoft (2nd Biggest)

**Keys to Outlook deliverability:**

1. **Smart Network Data Services (SNDS)**
   - Monitor Outlook reputation
   - Free: sendersupport.olc.protection.outlook.com/snds

2. **Junk E-mail Reporting Program (JMRP)**
   - See complaint data
   - Apply: jmrp@microsoft.com

3. **Outlook Specifics:**
   - More strict on images (keep ratio 60/40 text/image min)
   - Check links against SmartScreen filter
   - Focused Inbox (like Gmail Primary)

---

### Yahoo/AOL (Now Together)

**Keys to Yahoo/AOL deliverability:**

1. **Complaint Feedback Loop**
   - Essential for monitoring
   - Sign up at Yahoo/AOL postmaster sites

2. **Yahoo Specifics:**
   - Very strict on authentication
   - Must have DMARC
   - High penalty for complaints

---

## Testing & Monitoring

### Pre-Send Testing

**Mail-Tester.com (Essential)**
```
1. Send test email to provided address
2. Get score out of 10
3. See what's wrong
4. Fix issues
5. Aim for 9/10 or 10/10

Checks:
- SPF, DKIM, DMARC
- Spam score
- Blacklist status
- Content issues
```

**GlockApps or Email on Acid**
- Tests placement across providers
- Shows inbox vs spam vs promotions
- Identifies specific issues
- Paid tools ($$$)

**Litmus Spam Testing**
- Checks against major spam filters
- Shows spam score
- Content analysis
- Paid ($)

---

### Monitoring (Ongoing)

**Key Metrics to Track:**

**Delivery Rate:**
```
Formula: (Delivered ÷ Sent) × 100
Target: 98%+
Warning: <95%

Low delivery = bounces, invalid emails
```

**Bounce Rate:**
```
Hard Bounces: Invalid emails (remove immediately)
Soft Bounces: Temporary (full inbox, server issue)

Target: <2%
Warning: >5%
Critical: >10%
```

**Complaint Rate:**
```
Formula: (Complaints ÷ Delivered) × 100
Target: <0.1%
Warning: >0.1%
Critical: >0.5%

Complaints = "Mark as spam" clicks
```

**Open Rate (Indirect engagement measure):**
```
Target: 25-40% (industry dependent)
Warning: <15%

Low opens hurt deliverability over time
```

---

## Blacklist Management

### Major Blacklists

**Check your domain/IP:**
- Spamhaus.org
- Barracuda Central
- SORBS
- SpamCop
- MXToolbox Blacklist Check (checks multiple)

**If blacklisted:**
1. Identify reason (check blacklist site)
2. Fix underlying issue
3. Request removal (each blacklist has process)
4. Wait for removal (24-48 hours usually)
5. Prevent recurrence

**Prevention:**
- Clean list regularly
- Remove bounces immediately
- Use double opt-in
- Monitor complaint rates
- Don't buy lists (ever)

---

## List Hygiene (Critical)

### Email Validation

**When to validate:**
- Before importing old list
- Every 3-6 months (ongoing)
- Before major campaign

**What validation does:**
- Removes invalid emails
- Identifies spam traps
- Finds role addresses (info@, sales@)
- Checks typos (gamil.com → gmail.com)

**Tools:**
- NeverBounce
- ZeroBounce
- BriteVerify
- Hunter.io Email Verifier

**Cost:** ~$0.005-0.01 per email
**ROI:** Massive (prevents blacklisting, improves deliverability)

---

### Bounce Management

**Hard Bounces (Remove immediately):**
- Invalid email address
- Domain doesn't exist
- Rejected by server

**Soft Bounces (Monitor):**
- Mailbox full
- Server temporarily unavailable
- Email too large

**Automation:**
```
Most ESPs automatically:
- Remove hard bounces
- Retry soft bounces (3-5 times)
- Remove persistent soft bounces

But verify this is enabled!
```

---

### Inactive Subscriber Removal

**Sunset Policy Example:**

```
No opens in 90 days:
→ Tag as "Inactive"
→ Send re-engagement sequence (3 emails over 2 weeks)

No engagement from re-engagement:
→ Remove from list

Result:
- Higher engagement rate
- Better deliverability
- Lower costs
- Cleaner data
```

**Counter-intuitive truth:** Smaller, engaged list > Large, unengaged list

---

## Advanced Deliverability Tactics

### Dedicated IP vs Shared IP

**Shared IP (Most common):**
- Your emails sent through shared server with others
- Shared reputation
- Pros: Easier, managed by ESP, lower volume OK
- Cons: Others' bad behavior can affect you

**Dedicated IP:**
- Your own server/IP address
- Your reputation only
- Pros: Full control, not affected by others
- Cons: Must warm up, requires consistent volume (10K+/month), more expensive

**When to get dedicated IP:**
- Sending 100K+ emails/month
- High-value list (can't risk others' behavior)
- Need full control

---

### Reply Tracking (Advanced)

**Set up reply-to email that:**
- Accepts replies
- Ideally same domain as sending domain
- Monitored by real person

**Why:**
- Gmail/Outlook track if emails get replies
- Replies = strong "not spam" signal
- Encourages engagement
- Builds relationships

**Tactic:**
- "Hit reply and let me know..."
- "Questions? Just respond to this email"
- "I read every reply"

---

### Preference Center

**What it is:**
- Page where subscribers control preferences
- Email frequency
- Topics of interest
- Email format

**Why it helps deliverability:**
- Reduces unsubscribes (they adjust vs leave)
- Improves relevance
- Better engagement
- Shows you respect subscribers

**Include options for:**
- Daily, weekly, monthly emails
- Topics (if you cover multiple)
- Special offers only
- All emails

---

## Deliverability Checklist

**Before First Send:**
- [ ] SPF record configured
- [ ] DKIM enabled
- [ ] DMARC policy set (start with p=none)
- [ ] Custom domain sending configured
- [ ] Mail-tester.com score 9/10 or 10/10
- [ ] Welcome email tested in major clients
- [ ] Unsubscribe link works and is visible

**Ongoing (Weekly):**
- [ ] Monitor bounce rate (<2%)
- [ ] Monitor complaint rate (<0.1%)
- [ ] Check open rates by campaign
- [ ] Remove hard bounces
- [ ] Review spam complaints

**Monthly:**
- [ ] Check sender reputation (SenderScore.org)
- [ ] Review engagement by segment
- [ ] Re-engagement campaign for inactive
- [ ] Check blacklist status
- [ ] Analyze top performing content

**Quarterly:**
- [ ] List validation (remove invalid emails)
- [ ] Review DMARC reports
- [ ] Test emails across all major clients
- [ ] Sunset policy enforcement
- [ ] Strategy adjustment based on data

---

## Emergency: What If You're Already in Spam?

### Diagnosis

**Check:**
1. Blacklists (MXToolbox)
2. Sender reputation (SenderScore.org)
3. Bounce rate
4. Complaint rate
5. Gmail Postmaster Tools

---

### Recovery Plan

**Week 1: Stop the Bleeding**
```
1. Pause all campaigns
2. Identify issue (blacklist? complaints? content?)
3. Fix technical issues (SPF, DKIM, DMARC)
4. Remove hard bounces
5. Validate entire list
6. Request removal from blacklists
```

**Week 2-3: Clean List**
```
1. Segment by engagement (last 30 days)
2. Send ONLY to most engaged (10-20% of list)
3. Remove anyone who hasn't opened in 90+ days
4. Set up double opt-in for new subscribers
```

**Week 4-6: Rebuild Reputation**
```
1. Gradually increase volume (warm-up process)
2. Focus on high-quality content
3. Encourage replies/engagement
4. Monitor metrics closely
5. Adjust based on response
```

**Week 7+: Scale Carefully**
```
1. Expand to warm subscribers
2. Continue monitoring
3. Re-engagement for cold subscribers
4. Maintain list hygiene
```

---

## Key Takeaways

**The Big 3 Priorities:**

1. **Technical Setup:** SPF + DKIM + DMARC
2. **List Quality:** Clean, engaged, permission-based
3. **Content:** Valuable, relevant, well-formatted

**Quick Wins:**
- Set up authentication (SPF, DKIM, DMARC) - do this NOW
- Remove bounces immediately
- Sunset unengaged subscribers
- Test with Mail-tester.com before sending
- Make unsubscribe easy

**Long-term Success:**
- Send consistently (don't blast then disappear)
- Focus on engagement over list size
- Segment and personalize
- Monitor metrics religiously
- Clean list every 60-90 days

**Remember:** Deliverability is not one-time setup. It's ongoing maintenance. Treat it seriously and you'll reach the inbox consistently.
