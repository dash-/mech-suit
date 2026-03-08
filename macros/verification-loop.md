---
name: Verification Loop
shorthand: verification-loop
category: pattern
tags: [convergent, quality, reliability]
summary: After output is produced, a separate verifier checks against defined criteria.
composes_with: []
opposes: []
---

# Verification Loop (`verification-loop`)

**Tags:** `convergent` `quality` `reliability`

After output is produced, a separate verifier checks against defined criteria. If verification fails, output goes back with feedback for revision. Repeats until pass or retry limit.

```
Producer → Output → Verifier
              ↑         │
              └── fail ──┘ (with feedback)
              pass → Continue
```

**When to use:**
- Clear, checkable criteria for output quality
- Cost of bad output propagating downstream is high
- The producer can meaningfully improve given specific feedback

**Tradeoffs:**
- **Pro:** Catches errors before propagation
- **Pro:** Targeted feedback is more useful than "try again"
- **Con:** Can loop indefinitely without retry limits
- **Con:** Verifier has its own false positive/negative rate

**Variants:**
- **Multi-verifier** — different verifiers for different dimensions
- **Graduated** — cheap/fast first pass, expensive/thorough only if flagged

## Examples

TODO: Add concrete examples from real usage.
