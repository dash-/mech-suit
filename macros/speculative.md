---
name: Speculative
shorthand: speculative
category: modifier
tags: []
summary: The agent treats its output as explicitly provisional — a hypothesis to validate, not a final answer — making uncertainty visible and expecting downstream validation.
composes_with: [generate, refine, divergent-brainstorm, redundant-generation, progressive-refinement]
opposes: [publishable, idempotent]
---

# Speculative (`speculative`)

When this modifier is applied, the agent treats its output as explicitly provisional — a hypothesis to validate, not a final answer. This frees the agent to explore broadly, generate multiple candidates, and tolerate lower individual confidence. Uncertainty must be made visible rather than hidden behind confident-sounding language; every speculative output expects a downstream validation step.

## Examples

TODO: Add concrete examples from real usage.
