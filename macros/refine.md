---
name: Refine
shorthand: refine
category: strategy
tags: [convergent, quality]
summary: The agent takes a prior output and applies targeted modifications while preserving what already works, with each pass having diminishing scope.
composes_with: [verify, generate, emit]
opposes: [generate]
---

# Refine (`refine`)

When this macro is invoked, the agent takes a prior output and applies targeted modifications — fixing defects, tightening language, improving structure — while preserving what already works. Each refinement pass has a diminishing scope of changes. The agent does not regenerate wholesale when a scalpel will do.

```
Draft → Clarity Agent → Accuracy Agent → Tone Agent → Conciseness Agent → Final
```

## Decision Tree

- Refine for correctness, clarity, or performance?
- Single pass or iterate until a quality threshold is met?
- Single agent refining all dimensions, or successive specialized agents each focused on one dimension?

## When to Use

- Output quality has multiple independent dimensions
- A single agent optimizing all simultaneously produces mediocre results
- You want predictable, incremental improvement

## Tradeoffs

- **Pro:** Each refinement agent has a simple, focused job
- **Pro:** Add or remove refinement stages without redesigning the system
- **Con:** Later stages can undo earlier improvements
- **Con:** Order matters and has diminishing returns

## Examples

TODO: Add concrete examples from real usage.
