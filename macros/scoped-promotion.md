---
name: Scoped Promotion
shorthand: scoped-promotion
category: pattern
tags: [learning]
summary: Learnings, patterns, and behaviors start scoped to a specific context (project, client, industry, engagement).
composes_with: [confidence-signaling, memory-retrieval, workspace-isolation]
opposes: []
---

# Scoped Promotion (`scoped-promotion`)

**Tags:** `learning`

Learnings, patterns, and behaviors start scoped to a specific context (project, client, industry, engagement). They're promoted to broader scope only when consensus is reached — the same pattern independently emerges across multiple contexts.

```
Project A learns: "validate user input at API boundary"  (confidence: 0.8)
Project B learns: "validate user input at API boundary"  (confidence: 0.7)
  → Consensus: 2+ projects, avg confidence ≥ 0.75
  → Promote to global scope
```

**When to use:**
- A system operates across multiple projects, clients, or domains
- You want to learn from each context without overfitting to one
- Universal patterns should be shared; context-specific ones should not

**Tradeoffs:**
- **Pro:** Prevents overfitting — a React pattern doesn't leak into Python projects
- **Pro:** Universal patterns get stronger evidence before being broadly applied
- **Pro:** Promotion creates a natural quality filter
- **Con:** Consensus threshold must be calibrated — too high and nothing promotes, too low and noise leaks through
- **Con:** Context detection must be reliable (project identity, domain classification)

**Key decisions:**
- Scope levels: project → team → organization → global? Or simpler?
- Promotion criteria: N contexts + confidence threshold? Manual review?
- Demotion: can promoted patterns be demoted if they stop working in new contexts?

**Notes:** Natural partner to **Memory & Retrieval** (scoped memories), **Confidence Signaling** (drives promotion), and **Workspace Isolation** (defines the scope boundaries).

## Examples

TODO: Add concrete examples from real usage.
