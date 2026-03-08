---
name: Context Windowing
shorthand: context-windowing
category: pattern
tags: [context]
summary: The general principle of deliberately curating what information an agent sees.
composes_with: []
opposes: []
---

# Context Windowing (`context-windowing`)

**Tags:** `context`

The general principle of deliberately curating what information an agent sees. Too much context = noise and distraction. Too little = blind spots and bad decisions. This is the umbrella pattern; **TOC Index** and **Retrieval Subagent** are specific implementations.

**When to use:**
- The total available context exceeds what an agent can process effectively
- Different agents need different slices of the same information
- Sensitive information should only be visible to certain agents

**Techniques:**
- **Relevance filtering** — only include context related to the current subtask
- **Summarization layers** — compress verbose context into key points
- **Progressive disclosure** — start with summary, let agent request detail
- **Role-based access** — ethics agent sees everything, content generator sees only the brief

**Context efficiency progression:**
```
Full context (naive) → Context Windowing (curated) → TOC Index (indexed) → Retrieval Subagent (delegated)
```
Each level trades latency for context efficiency.

**Implementations:** **TOC Index** and **Retrieval Subagent** are specific implementations of this pattern, listed separately below because they're substantial enough to stand alone.

## Examples

TODO: Add concrete examples from real usage.
