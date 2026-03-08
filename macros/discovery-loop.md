---
name: Discovery Loop
shorthand: discovery-loop
category: pattern
tags: [learning, decisions]
summary: **Bayesian Steering** → **Escalation Ladder** → **Memory & Retrieval** → **Verification Loop**
composes_with: []
opposes: []
---

# Discovery Loop (`discovery-loop`)

**Tags:** `learning` `decisions`

**Bayesian Steering** → **Escalation Ladder** → **Memory & Retrieval** → **Verification Loop**

Use information gain to decide what to explore, escalate modality as uncertainty narrows, learn from history, verify each step.

**When to use:**
- Iterative exploration with a budget constraint
- Each iteration should inform the next (not independent trials)
- Historical data exists to set meaningful priors


**Generate-Debate-Evolve variant (from scientific discovery systems):**
A richer instantiation using specialized agents: Generation agents produce hypotheses → Reflection agents critique them (peer review) → Ranking agents evaluate via Elo-style tournament → Evolution agents refine top candidates → Proximity agents cluster similar ideas → Meta-review agents synthesize across clusters. This mirrors the scientific method and is particularly effective for open-ended exploration where the solution space is poorly understood.

## Examples

TODO: Add concrete examples from real usage.
