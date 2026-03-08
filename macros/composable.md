---
name: Composable
shorthand: composable
category: principle
tags: []
summary: Examine every component for whether it can be used in contexts its author didn't anticipate, proposing interface changes that enable free connection through simple, consistent contracts.
composes_with: [SoC, DRY, explicit]
opposes: [minimal]
---

# Composable (`composable`)

When this macro is invoked, the agent examines every component and asks: "Can this be used in a context its author didn't anticipate?" It flags components that work only in their original context, outputs that require transformation before the next step can consume them, tightly coupled pairs that cannot be recombined, and interfaces that demand knowledge of internal implementation. For each, it proposes interface changes that enable free connection through simple, consistent contracts.

## Examples

TODO: Add concrete examples from real usage.
