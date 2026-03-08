---
name: Progressive Refinement
shorthand: progressive-refinement
category: pattern
tags: [convergent, quality]
summary: Output passes through successive improvement stages, each focused on a specific quality dimension.
composes_with: []
opposes: []
---

# Progressive Refinement (`progressive-refinement`)

**Tags:** `convergent` `quality`

Output passes through successive improvement stages, each focused on a specific quality dimension.

```
Draft → Clarity Agent → Accuracy Agent → Tone Agent → Conciseness Agent → Final
```

**When to use:**
- Output quality has multiple independent dimensions
- A single agent optimizing all simultaneously produces mediocre results
- You want predictable, incremental improvement

**Tradeoffs:**
- **Pro:** Each agent has a simple, focused job
- **Pro:** Add or remove stages without redesigning the system
- **Con:** Later stages can undo earlier improvements
- **Con:** Order matters and has diminishing returns

## Examples

TODO: Add concrete examples from real usage.
