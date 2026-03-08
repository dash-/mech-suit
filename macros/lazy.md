---
name: Lazy
shorthand: lazy
category: modifier
tags: []
summary: The agent defers all work until the result is actually needed, operating in just-in-time mode and actively resisting speculative work.
composes_with: [delegate, cache, decompose, catalog, cascade-fallback]
opposes: [eager, publishable]
---

# Lazy (`lazy`)

When this modifier is applied, the agent defers all work until the result is actually needed by a downstream consumer. Instead of building everything upfront, it identifies the immediate need and produces only that. Downstream steps are planned but not executed — the agent operates in just-in-time mode and actively resists speculative work.

## Examples

TODO: Add concrete examples from real usage.
