---
name: Multi-Source Context Assembly
shorthand: context-assembly
category: pattern
tags: [context, setup]
summary: Gather context from multiple heterogeneous sources in parallel, then synthesize into a unified brief before work begins.
composes_with: []
opposes: []
---

# Multi-Source Context Assembly (`context-assembly`)

**Tags:** `context` `setup`

Gather context from multiple heterogeneous sources in parallel, then synthesize into a unified brief before work begins. Different from **Decomposition & Reassembly** (which breaks a *task* apart) — this assembles *context* from existing sources.

```
Linear ticket ──┐
PR history     ──┼→ Parallel fetch → Synthesis Agent → Unified Brief → Ready to work
Figma designs  ──┤
Doc links      ──┤
Comments       ──┘
```

**When to use:**
- Work requires understanding from multiple systems (ticketing, code, design, docs)
- Context sources are independent and can be fetched in parallel
- The agent doing the work shouldn't have to know where context lives

**Tradeoffs:**
- **Pro:** Agent starts work with complete context, not a partial view
- **Pro:** Parallel fetching minimizes wall-clock time
- **Pro:** Synthesis step eliminates redundancy and contradiction across sources
- **Con:** Synthesis can lose important nuance from individual sources
- **Con:** Some sources may be unavailable — need graceful degradation

## Examples

TODO: Add concrete examples from real usage.
