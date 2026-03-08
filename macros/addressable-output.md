---
name: Addressable Output
shorthand: addressable-output
category: pattern
tags: [communication]
summary: Structure agent output so every item is uniquely referenceable.
composes_with: [configurable-hitl, inversion-of-control]
opposes: []
---

# Addressable Output (`addressable-output`)

**Tags:** `communication`

Structure agent output so every item is uniquely referenceable. Use numbers for top-level items (issues, decisions, steps) and letters for sub-options within each. This lets humans (or downstream agents) respond precisely — "approve 2B, reject 3A" — instead of ambiguously quoting text.

```
Agent output:
  1. Database migration strategy
     A. Run migrations in-place (recommended)
     B. Blue-green deployment with cutover
     C. Shadow writes during transition period
  2. API versioning approach
     A. URL path versioning (recommended)
     B. Header-based versioning

Human response: "1A, 2A" → unambiguous, complete
```

**When to use:**
- Agent presents multiple decisions or recommendations that need human approval
- Output contains lists where the human needs to accept, reject, or modify individual items
- Downstream agents need to parse human feedback and map it back to specific items
- Any multi-turn interaction where "which one?" ambiguity would waste a round-trip

**Tradeoffs:**
- **Pro:** Eliminates ambiguity — "2B" is unambiguous, "the second option" is not
- **Pro:** Humans can respond in shorthand, which is faster
- **Pro:** Machine-parseable — downstream agents can reliably extract choices from "1A, 2B, 3C"
- **Con:** Can feel overly formal for simple, single-choice interactions
- **Con:** Deep nesting (1A-ii-b) defeats the purpose — keep it to two levels max

**Key decisions:**
- Numbering scheme: numbers + letters? hierarchical (1.1, 1.2)? flat?
- Recommended option: always list it first? mark it explicitly?
- Response format: do you tell the human how to respond (e.g., "reply with 1A or 1B")?

**Notes:** Natural partner to **Inversion of Control** (agent drives the process, human picks from addressable options) and **Configurable HITL** (addressable items map to approval checkpoints).

## Examples

TODO: Add concrete examples from real usage.
