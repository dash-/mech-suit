---
name: Escalation Ladder
shorthand: escalation-ladder
category: pattern
tags: [cost, quality, decisions]
summary: Start with cheapest/fastest approach.
composes_with: [budget-aware-execution, confidence-signaling]
opposes: []
---

# Escalation Ladder (`escalation-ladder`)

**Tags:** `cost` `quality` `decisions`

Start with cheapest/fastest approach. If quality threshold isn't met, escalate to more expensive/slower/higher-quality approach. Continue up the ladder.

```
Level 1 (fast/cheap) → meets threshold? → yes → done
                                         → no  → Level 2 (slower/better) → ...
```

**When to use:**
- Wide range of task difficulty — many easy, some hard
- Natural ordering from cheap/fast to expensive/thorough
- You're exploring a space and want to narrow before investing in rich artifacts

**Tradeoffs:**
- **Pro:** Dramatic cost reduction when most tasks handled by lower levels
- **Pro:** Higher levels benefit from information gathered at lower levels
- **Con:** Escalation criteria must be well-calibrated

**Variants:**
- **Modality escalation** — text → image → video
- **Model escalation** — small model → large model
- **Agent escalation** — single agent → ensemble → full adversarial pipeline

**Notes:** Natural partner to **Confidence Signaling** (confidence drives escalation decisions) and **Budget-Aware Execution** (budget determines how far up the ladder you can go).

## Examples

TODO: Add concrete examples from real usage.
