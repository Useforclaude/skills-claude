# Prospect Theory: Complete Framework

## Overview

**Authors:** Daniel Kahneman & Amos Tversky (1979)
**Paper:** "Prospect Theory: An Analysis of Decision Under Risk"
**Citation:** Econometrica, 47(2), 263-291
**Impact:** Foundation of behavioral economics; Kahneman awarded Nobel Prize 2002

**Revolutionary Claim:** Expected Utility Theory (dominant since 1738) fails to describe how humans actually make decisions under risk.

---

## Problems with Expected Utility Theory (EUT)

### Classical EUT Assumptions

People maximize expected utility:
```
U = Σ p(x) × u(x)

Where:
- p(x) = probability of outcome x
- u(x) = utility of outcome x
- u is concave (risk averse for all wealth levels)
```

### Violations Discovered

**1. Allais Paradox (1953)**

**Choice 1:**
- A: $1M (certain)
- B: $5M (10%), $1M (89%), $0 (1%)
- Most people choose A (certainty)

**Choice 2:**
- C: $1M (11%), $0 (89%)
- D: $5M (10%), $0 (90%)
- Most people choose D

**Violation:** A > B and D > C is inconsistent with EUT!
- If A > B, then u($1M) > 0.10×u($5M) + 0.89×u($1M)
- Simplifies to: 0.11×u($1M) > 0.10×u($5M)
- But this implies C > D (contradiction!)

**2. Fourfold Pattern of Risk Attitudes**

| Probability | Gains | Losses |
|-------------|-------|--------|
| High | Risk averse | Risk seeking |
| Low | Risk seeking | Risk averse |

**Examples:**

**High probability gains (risk averse):**
- 80% chance $4,000 vs $3,000 certain
- Most choose certain $3,000

**Low probability gains (risk seeking):**
- 0.1% chance $5,000 vs $5 certain
- Most choose lottery (why people buy lottery tickets!)

**High probability losses (risk seeking):**
- 80% chance lose $4,000 vs lose $3,000 certain
- Most choose gamble (avoid sure loss)

**Low probability losses (risk averse):**
- 0.1% chance lose $5,000 vs lose $5 certain
- Most choose certain loss (why people buy insurance!)

**3. Reflection Effect**

Risk preferences reverse for losses vs gains:

**Gains (risk averse):**
- 50% chance $1,000 vs $450 certain
- Most choose certain $450

**Losses (risk seeking):**
- 50% chance lose $1,000 vs lose $450 certain
- Most choose gamble

**4. Isolation Effect**

People focus on differences, not total outcomes.

**Problem 1:**
- Stage 1: 75% advance to Stage 2
- Stage 2 if advanced: Choose A ($4,000 certain) or B ($3,000 or 0, 80%/20%)

**Problem 2 (equivalent):**
- Choose C (75% × 100% = 75% chance $4,000) or D (75% × 80% = 60% chance $3,000)

People choose differently (A>B but D>C) because they ignore first stage!

---

## Prospect Theory Framework

### Two-Phase Model

**Phase 1: Editing**
- Frame reference point
- Simplify prospects
- Detect dominance
- Cancel common components

**Phase 2: Evaluation**
```
V = Σ π(p) × v(x)

Where:
- π(p) = decision weight (transformed probability)
- v(x) = value function (transformed outcome)
```

### Value Function v(x)

**Properties:**

1. **Reference Dependence**: Defined over gains/losses, not final wealth
   - v(0) = 0 (reference point)
   - Outcomes coded as deviations from reference

2. **Loss Aversion**: Steeper for losses than gains
   - v(-x) < -v(x) for all x > 0
   - λ = loss aversion coefficient ≈ 2.25
   - Losing $100 ≈ 2.25× worse than gaining $100 is good

3. **Diminishing Sensitivity**: Concave for gains, convex for losses
   - Risk averse for gains: v(x) + v(y) < v(x+y) for x,y > 0
   - Risk seeking for losses: v(-x) + v(-y) > v(-x-y)
   - Explains fourfold pattern

**Mathematical Form:**
```
v(x) = { x^α           if x ≥ 0
       { -λ(-x)^β      if x < 0

Parameters (typical):
- α ≈ 0.88 (diminishing sensitivity for gains)
- β ≈ 0.88 (diminishing sensitivity for losses)
- λ ≈ 2.25 (loss aversion)
```

**Graphical Representation:**
```
Value
  ^
  |     /
  |    /  (gains: concave)
  |   /
  |  /
--|-------------------> Outcome
  | \
  |  \
  |   \  (losses: convex, steeper)
  |    \
```

### Probability Weighting Function π(p)

**Properties:**

1. **Overweight small probabilities**: π(p) > p for small p
   - 1% feels more important than it is
   - Why people buy lottery tickets (overweight small chance of jackpot)
   - Why people buy insurance (overweight small chance of disaster)

2. **Underweight large probabilities**: π(p) < p for large p
   - 99% feels less certain than it is
   - Certainty effect (100% > 99% gap larger than 50% > 49%)

3. **Subadditivity**: π(p) + π(1-p) < 1
   - Probabilities don't add to 1 (people are not probabilistically coherent)

4. **Subcertainty**: π(p) + π(q) < π(p+q) for complementary p,q
   - Combined probability weighted more than separate

**Mathematical Forms:**

**Original (Kahneman & Tversky, 1979):**
```
π(p) = { p^α / (p^α + (1-p)^α)^(1/α)   for gains
       { p^β / (p^β + (1-p)^β)^(1/β)   for losses

Typical parameters:
- α ≈ 0.61 (gains)
- β ≈ 0.69 (losses)
```

**Graphical Representation:**
```
π(p)
  ^
1 |         ,--------
  |       ,'
  |     ,'
  |   ,'
  | ,'
0 |'-------------------> p
  0                     1

- Crosses 45° line around p=0.3
- Steep near 0 (overweight small p)
- Flat near 1 (underweight large p)
```

**Cumulative Prospect Theory (1992):**

Updated to use rank-dependent utility:
```
π+(p) = p^γ / (p^γ + (1-p)^γ)^(1/γ)    [gains]
π-(p) = p^δ / (p^δ + (1-p)^δ)^(1/δ)    [losses]

Typical parameters:
- γ ≈ 0.61 (gains)
- δ ≈ 0.69 (losses)
```

---

## Key Predictions & Phenomena

### 1. Certainty Effect

Reduction from certainty is weighted more than equivalent reduction from uncertainty.

**Example:**
- ($3,000, 100%) vs ($4,000, 80%)
  - Most choose $3,000 (certain)
- ($3,000, 25%) vs ($4,000, 20%)
  - Most choose $4,000 (higher EV)

**Explanation:**
- π(1.0) = 1.0, π(0.8) ≈ 0.6 → Large gap
- π(0.25) ≈ 0.3, π(0.2) ≈ 0.25 → Small gap

### 2. Reflection Effect

Risk preference reverses for losses.

**Explanation:**
- Gains domain: v(x) concave → risk averse
- Loss domain: v(x) convex → risk seeking

### 3. Isolation Effect

Focus on differences between prospects, ignore common elements.

**Example:**
- ($200, 50%; $100, 50%) vs ($150, 100%)
- People code as: "$50 more or $50 less with 50% each" vs "0 gain/loss"
- Ignore base $150 common to both

### 4. Framing Effects

Outcomes framed as gains or losses relative to reference point.

**Asian Disease Problem:**

*Gain frame:*
- A: Save 200 (certain)
- B: 1/3 save 600, 2/3 save 0
- Result: 72% choose A

*Loss frame:*
- C: 400 die (certain)
- D: 1/3 nobody dies, 2/3 all 600 die
- Result: 78% choose D

Same outcomes, different reference points!

### 5. Disposition Effect (Shefrin & Statman, 1985)

Investors hold losing stocks too long, sell winning stocks too soon.

**Explanation:**
- Gains domain (winning stock): Risk averse → realize gains
- Loss domain (losing stock): Risk seeking → hold, gamble for recovery

### 6. House Money Effect (Thaler & Johnson, 1990)

Prior gains → More willing to take risks.

**Explanation:**
- Prior gain shifts reference point
- Current risky choice coded as potential loss of prior gain
- Loss aversion reduced (vs loss of "own" money)

### 7. Break-Even Effect

After loss, increased risk-seeking to break even.

**Example:**
- Gambling: Losing gamblers bet more on long shots (try to break even)
- Trading: Losing traders take excessive risks

**Explanation:**
- Reference point = initial wealth
- Current position = loss
- Risk-seeking in loss domain

---

## Empirical Evidence

### Classic Experiments

**Problem 1 (Certainty Effect):**
- A: $2,500 (33%), $2,400 (66%), $0 (1%)
- B: $2,400 (100%)
- Result: 82% choose B (certainty)

**Problem 2:**
- C: $2,500 (33%), $0 (67%)
- D: $2,400 (34%), $0 (66%)
- Result: 83% choose C

**Inconsistency:** Violates EUT (B>A should imply D>C)

**Problem 3 (Reflection):**
- E: Lose $2,500 (33%), Lose $2,400 (66%), $0 (1%)
- F: Lose $2,400 (100%)
- Result: 70% choose E (avoid certain loss)

**Problem 4:**
- G: Lose $2,500 (33%), $0 (67%)
- H: Lose $2,400 (34%), $0 (66%)
- Result: 58% choose H

**Finding:** Risk preferences reverse for losses vs gains

### Real-World Applications

**1. Insurance:**
- Deductibles: People choose low deductibles (overpay for small risk reduction)
- Extended warranties: Overinsure small risks
- Explanation: Overweight small probability of loss

**2. Lottery:**
- Expected value negative, but people play
- Explanation: Overweight small probability of jackpot

**3. Investment:**
- Disposition effect: Hold losers, sell winners
- January effect: Tax-loss selling in December
- Explanation: Loss aversion + risk-seeking in loss domain

**4. Labor Supply:**
- Taxi drivers (Camerer et al., 1997):
  - Daily income target (reference point)
  - Good day (ahead of target): Quit early
  - Bad day (behind target): Work longer
- Explanation: Diminishing sensitivity (stop when ahead), loss aversion (work harder when behind)

**5. Consumption:**
- Mental accounting: Segregate gains, integrate losses
- Cash vs credit card: Cash = immediate loss (more painful)
- Explanation: Value function + payment decoupling

---

## Extensions & Refinements

### Cumulative Prospect Theory (1992)

**Improvements:**
1. Rank-dependent probability weighting (resolves violations)
2. Separate weighting functions for gains/losses
3. More general mathematical formulation

**Formula:**
```
V = Σ [w+(p_i) × v(x_i)]  for gains
  + Σ [w-(p_j) × v(x_j)]  for losses

Where w+ and w- are cumulative decision weights
```

### Reference Point Formation

**Endogenous vs Exogenous:**
- Exogenous: Status quo, aspiration level, social norm
- Endogenous: Expectations, recent outcomes

**Koszegi & Rabin (2006):**
- Reference point = Rational expectations
- Explains dynamic choice behavior

### Applications to Intertemporal Choice

**Quasi-hyperbolic Discounting (β-δ model):**
```
U(c_0, c_1, ..., c_T) = u(c_0) + β Σ δ^t u(c_t)

Where:
- δ = long-run discount factor
- β < 1 = present bias
```

Combines prospect theory insights with time preferences.

---

## Criticisms & Limitations

### Theoretical Critiques

**1. Descriptive vs Normative:**
- Describes behavior but doesn't prescribe optimal choices
- Should people follow prospect theory or EUT?

**2. Reference Point Ambiguity:**
- Not always clear what reference point is
- Can be manipulated/framed
- May change dynamically

**3. Parameter Instability:**
- Loss aversion coefficient varies by context
- Probability weighting varies by domain
- Individual differences substantial

**4. Editing Phase:**
- Less formalized than evaluation phase
- Framing rules not fully specified
- Context-dependent

### Empirical Challenges

**1. Preference Reversals:**
- Some choice patterns still not explained
- Context effects beyond prospect theory

**2. Small Stakes:**
- Theory developed for moderate-large stakes
- May not apply to trivial decisions

**3. Individual Differences:**
- Large heterogeneity in parameters
- Demographics, expertise, domain matter

**4. Learning & Experience:**
- Expert traders show reduced biases
- Repeated decisions may converge to EUT

---

## Practical Applications

### Business Strategy

**Pricing:**
- Frame as avoiding loss vs gaining benefit
- Use reference prices (MSRP anchoring)
- Bundle to reduce loss salience

**Product Design:**
- Free trials create endowment effect
- Money-back guarantees reduce perceived risk
- Default options exploit status quo bias

**Marketing:**
- Loss-framed messaging for risk-averse behavior
- Gain-framed for risk-seeking behavior
- Scarcity creates loss aversion ("Don't miss out")

### Investment & Finance

**Portfolio Design:**
- Avoid disposition effect (set rules)
- Mental accounting for risk buckets
- Frame contributions as avoiding future regret

**Retirement Savings:**
- Auto-enrollment (status quo bias)
- Save More Tomorrow (future reference point)
- Loss framing ("Don't leave money on table")

**Risk Communication:**
- Frame benefits in gains for low-risk options
- Frame costs in losses for high-risk options
- Use probability weighting insights (e.g., insurance)

### Public Policy

**Health:**
- Frame surgery success rates (90% survive vs 10% die)
- Default organ donation (opt-out)
- Medication adherence (loss framing)

**Environment:**
- Energy bill feedback (loss framing for high use)
- Default green energy enrollment
- Carbon tax vs rebate framing

**Retirement:**
- Auto-enrollment (default)
- Escalation clauses (future commitment)
- Employer match (loss framing for not contributing)

### Legal & Regulatory

**Securities Disclosure:**
- Recognize framing effects in prospectuses
- Standardize reference points
- Require probability communication standards

**Consumer Protection:**
- Regulate misleading reference prices
- Require clear framing of terms
- Limit exploitation of probability weighting

---

## Key Takeaways

**For Researchers:**
1. Reference dependence is fundamental to choice
2. Loss aversion (λ≈2.25) is robust, large effect
3. Probability weighting explains insurance + lottery behavior
4. Framing effects are powerful, context-dependent
5. Individual differences matter but patterns are consistent

**For Practitioners:**
1. Frame choices carefully (gains vs losses)
2. Manage reference points (anchoring, status quo)
3. Use defaults strategically
4. Recognize probability weighting in risk communication
5. Test empirically (context matters)

**For Policy Makers:**
1. Choice architecture affects outcomes significantly
2. Libertarian paternalism possible (nudge while preserving freedom)
3. Framing is not neutral (design for good outcomes)
4. Defaults are powerful tools
5. Evaluate policies empirically, not just theoretically

---

## Further Reading

**Original Papers:**
- Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263-291.
- Tversky, A., & Kahneman, D. (1992). Advances in prospect theory: Cumulative representation of uncertainty. *Journal of Risk and Uncertainty*, 5(4), 297-323.

**Books:**
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Thaler, R. H. (2015). *Misbehaving: The Making of Behavioral Economics*. W.W. Norton.

**Reviews:**
- Barberis, N. C. (2013). Thirty years of prospect theory in economics: A review and assessment. *Journal of Economic Perspectives*, 27(1), 173-196.

**Applications:**
- Thaler, R. H., & Sunstein, C. R. (2008). *Nudge: Improving decisions about health, wealth, and happiness*. Yale University Press.

---

**Total: ~3,000 words**

This complete framework provides mathematical foundations, empirical evidence, applications, and critical evaluation of Prospect Theory - the cornerstone of modern behavioral economics.
