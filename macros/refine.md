---
name: Refine
shorthand: refine
category: strategy
tags: []
summary: The agent takes a prior output and applies targeted modifications — fixing defects, tightening language, improving structure — while preserving what already works.
composes_with: [verify, generate, emit]
opposes: [generate]
---

# Refine (`refine`)

When this macro is invoked, the agent takes a prior output and applies targeted modifications — fixing defects, tightening language, improving structure — while preserving what already works. Each refinement pass has a diminishing scope of changes. The agent does not regenerate wholesale when a scalpel will do.

## Decision Tree

- Refine for correctness, clarity, or performance?
- Single pass or iterate until a quality threshold is met?

## Examples

TODO: Add concrete examples from real usage.
