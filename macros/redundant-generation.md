---
name: Redundant Generation with Judging
shorthand: redundant-generation
category: pattern
tags: [divergent, quality]
summary: N agents (typically 3-5) do the same task independently.
composes_with: []
opposes: []
---

# Redundant Generation with Judging (`redundant-generation`)

**Tags:** `divergent` `quality`

N agents (typically 3-5) do the same task independently. Judge agents evaluate, rank, and provide rationale.

```
Task → Agent A ─┐
Task → Agent B ──┼→ Judge Panel → Ranked Results + Rationale
Task → Agent C ─┘
```

**When to use:**
- Output quality matters more than cost
- The task has a wide solution space
- You want to reduce single-agent variance

**Tradeoffs:**
- **Pro:** Significantly reduces bad output risk — best of N
- **Pro:** Ranking rationale is itself valuable signal
- **Con:** Linear cost scaling (N+1x)
- **Con:** Judges can have systematic biases

**Variants:**
- **Diverse generation** — different instructions/temperatures per agent to increase diversity
- **Blind judging** — judges don't know which agent produced which output
- **Multi-criteria judging** — independent scores on multiple dimensions, then composite

## Examples

TODO: Add concrete examples from real usage.
