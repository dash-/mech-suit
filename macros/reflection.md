---
name: Reflection & Self-Critique
shorthand: reflection
category: pattern
tags: [convergent, quality, cost]
summary: An agent reviews its own output before submitting — identifies weaknesses, then revises.
composes_with: []
opposes: []
---

# Reflection & Self-Critique (`reflection`)

**Tags:** `convergent` `quality` `cost`

An agent reviews its own output before submitting — identifies weaknesses, then revises.

```
Agent produces draft → Agent critiques own draft → Agent revises → Submit
```

**When to use:**
- You want better output without a separate verification agent
- The task benefits from a "step back and think" moment
- Budget pattern, not quality ceiling pattern

**Tradeoffs:**
- **Pro:** Cheap — one agent, ~1.5-2x cost
- **Pro:** Agent has full context on its own reasoning
- **Con:** Systematic blind spots persist through self-critique
- **Con:** Can be performative rather than substantive

**When NOT to use:** When stakes justify external verification. Self-critique is a budget play.

## Examples

TODO: Add concrete examples from real usage.
