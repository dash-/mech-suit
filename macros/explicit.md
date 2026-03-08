---
name: Explicit over Implicit
shorthand: explicit
category: principle
tags: []
summary: Hunt for anything that requires "you just have to know" to understand and propose stating the intention, dependency, or assumption directly.
composes_with: [transparent, least-surprise, fail-fast]
opposes: [composable]
---

# Explicit over Implicit (`explicit`)

When this macro is invoked, the agent hunts for anything that requires "you just have to know" to understand. It flags magic values, hidden coupling between modules, behavior that depends on execution order or ambient state, and undocumented prerequisites. For each finding, it proposes stating the intention, dependency, or assumption directly — accepting verbosity as the price of eliminating mystery.

## Examples

TODO: Add concrete examples from real usage.
