---
name: Decomposition & Reassembly
shorthand: decomposition-reassembly
category: pattern
tags: [coordination]
summary: A complex task is broken into smaller subtasks, solved independently (potentially in parallel), then reassembled into a coherent whole.
composes_with: []
opposes: []
---

# Decomposition & Reassembly (`decomposition-reassembly`)

**Tags:** `coordination`

A complex task is broken into smaller subtasks, solved independently (potentially in parallel), then reassembled into a coherent whole.

```
Complex Task → Decomposer → Subtask 1 → Result 1 ─┐
                           → Subtask 2 → Result 2 ──┼→ Reassembly Agent → Final
                           → Subtask 3 → Result 3 ─┘
```

**When to use:**
- The task is too complex for a single agent
- Subtasks are relatively independent (low coupling)
- You want to parallelize execution

**Tradeoffs:**
- **Pro:** Makes complex tasks tractable and parallelizable
- **Con:** Bad decomposition = bad results
- **Con:** Information loss at boundaries — subtask agents lack full context
- **Con:** Reassembly must handle cross-subtask dependencies and ensure coherence

## Examples

TODO: Add concrete examples from real usage.
