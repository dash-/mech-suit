---
name: Hybrid Synthesis
shorthand: hybrid-synthesis
category: pattern
tags: [convergent, quality]
summary: Given multiple outputs, a synthesis agent identifies the strongest elements of each and combines them into a single superior output.
composes_with: [redundant-generation, verification-loop]
opposes: []
---

# Hybrid Synthesis (`hybrid-synthesis`)

**Tags:** `convergent` `quality`

Given multiple outputs, a synthesis agent identifies the strongest elements of each and combines them into a single superior output. Not selecting a winner — extracting and recombining the best parts.

```
Output A ─┐                    ┌→ Strength Analysis
Output B ──┼→ Synthesis Agent ──┼→ Combination Strategy
Output C ─┘                    └→ Synthesized Output
```

**When to use:**
- Multiple outputs each have different strengths
- No single attempt nails every dimension
- You're willing to spend additional compute for higher quality

**Tradeoffs:**
- **Pro:** Can produce outputs strictly better than any individual attempt
- **Con:** Synthesis can introduce incoherence if elements don't compose well
- **Con:** Requires deep task understanding to judge what "best parts" means

**Notes:** Almost always follows **Redundant Generation**. Often followed by **Verification Loop**.

## Examples

TODO: Add concrete examples from real usage.
