---
name: Specialization Ensemble
shorthand: specialization-ensemble
category: pattern
tags: [divergent, quality, coordination]
summary: Multiple agents, each expert in a different aspect of the task, independently analyze the same input.
composes_with: []
opposes: []
---

# Specialization Ensemble (`specialization-ensemble`)

**Tags:** `divergent` `quality` `coordination`

Multiple agents, each expert in a different aspect of the task, independently analyze the same input. A synthesis agent merges their outputs.

```
Input → Expert A (messaging) ─┐
Input → Expert B (audience)  ──┼→ Synthesis Agent → Integrated Output
Input → Expert C (format)    ─┘
```

**When to use:**
- The task has multiple dimensions requiring genuinely different expertise
- A single generalist can't go deep enough on all dimensions
- You want deep analysis per dimension rather than shallow coverage of all

**Tradeoffs:**
- **Pro:** Each expert goes deeper than a generalist could
- **Pro:** Easy to add new specialists without redesigning the system
- **Con:** Specialists may produce conflicting recommendations — synthesis is the hard part
- **Con:** Specialists lack awareness of each other's constraints

**Different from Redundant Generation:** Specialization gives *different aspects* to different agents and merges. Redundant Generation gives the *same task* and selects.

## Examples

TODO: Add concrete examples from real usage.
