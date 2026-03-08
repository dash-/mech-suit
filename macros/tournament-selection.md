---
name: Tournament Selection
shorthand: tournament-selection
category: pattern
tags: [convergent, quality]
summary: Candidates evaluated in pairwise or bracket-style comparisons rather than absolute rankings.
composes_with: []
opposes: []
---

# Tournament Selection (`tournament-selection`)

**Tags:** `convergent` `quality`

Candidates evaluated in pairwise or bracket-style comparisons rather than absolute rankings.

```
A vs B → winner₁ ─┐
                    ├→ winner₁ vs winner₂ → Final Winner
C vs D → winner₂ ─┘
```

**When to use:**
- Many candidates (10+) where absolute ranking is expensive
- Pairwise comparison is more reliable than absolute scoring
- You need O(n log n) comparisons instead of O(n²)

**Tradeoffs:**
- **Pro:** Pairwise is more reliable than "rate this 1-10"
- **Pro:** Scales well to large candidate pools
- **Con:** Strong candidates can be eliminated by slightly stronger ones early
- **Con:** Doesn't produce full ranking, just a winner

**Variants:** Double elimination, round-robin, Swiss system

## Examples

TODO: Add concrete examples from real usage.
