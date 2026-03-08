---
name: Eager
shorthand: eager
category: modifier
tags: []
summary: The agent invests in pre-computation, pre-fetching, or pre-validation before results are explicitly requested, trading compute cost for reduced latency later.
composes_with: [compose, generate, cache, content-factory, verification-loop]
opposes: [lazy, incremental]
---

# Eager (`eager`)

When this modifier is applied, the agent invests in pre-computation, pre-fetching, or pre-validation before results are explicitly requested. It anticipates what will be needed and produces it now, trading compute cost for reduced latency later. The agent must distinguish what is *likely* needed from what is *certainly* needed — over-eagerness wastes resources.

## Examples

TODO: Add concrete examples from real usage.
