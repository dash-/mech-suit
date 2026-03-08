---
name: Generate
shorthand: generate
category: strategy
tags: []
summary: The agent produces multiple distinct outputs intentionally favoring breadth over efficiency, deferring convergence to a subsequent verify or refine pass.
composes_with: [verify, refine, decompose]
opposes: [refine, compose]
---

# Generate (`generate`)

When this macro is invoked, the agent produces multiple distinct outputs — ideas, drafts, solutions — intentionally favoring breadth over efficiency. Redundancy is the point: overlapping candidates increase the chance of finding high-quality results. The agent does not self-filter during generation; convergence happens in a subsequent `verify` or `refine` pass.

## Decision Tree

- Generate N candidates with variation in what dimension (approach, style, scope)?
- Constrained generation (within guardrails) or unconstrained (maximize diversity)?

## Examples

TODO: Add concrete examples from real usage.
