---
name: Divergent Brainstorm
shorthand: divergent-brainstorm
category: pattern
tags: [divergent, coordination, quality]
summary: Multiple agents independently generate ideas, approaches, or solutions without evaluating them.
composes_with: [adversarial-review, persona-injection, redundant-generation, tournament-selection]
opposes: []
---

# Divergent Brainstorm (`divergent-brainstorm`)

**Tags:** `divergent` `coordination` `quality`

Multiple agents independently generate ideas, approaches, or solutions without evaluating them. Quantity over quality. No filtering, no critique, no convergence — just raw option generation. Evaluation happens later via convergent patterns.

```
Prompt → Agent A generates ideas ─┐
Prompt → Agent B generates ideas ──┼→ Collect all → Deduplicate → Pass to convergent pattern
Prompt → Agent C generates ideas ─┘
```

**Different from Redundant Generation:** Redundant Generation gives agents the same task and judges pick the best *output*. Divergent Brainstorm asks agents to generate *many ideas each* — the goal is volume and variety, not polished outputs.

**When to use:**
- The solution space is large and you don't know where the best ideas live
- You want to avoid premature convergence (anchoring on the first decent idea)
- The downstream convergent pattern (Adversarial Review, Tournament Selection) needs a rich candidate pool

**Tradeoffs:**
- **Pro:** Surfaces non-obvious options that a single agent would never consider
- **Pro:** Different agent personas/temperatures produce genuinely different ideas
- **Pro:** Cheap per idea — agents generate without the overhead of evaluation
- **Con:** Produces many bad ideas alongside good ones — requires strong downstream filtering
- **Con:** Deduplication can be tricky when ideas overlap partially

**Key decisions:**
- Agent diversity: same prompt with different temperatures? different personas? different framings?
- Volume target: how many ideas per agent? When is enough enough?
- Deduplication: exact match? semantic similarity? human review?

**Notes:** Natural precursor to **Adversarial Review** (brainstorm then attack), **Tournament Selection** (brainstorm then compete), or **Redundant Generation** (brainstorm then judge). Pairs with **Persona Injection** to ensure genuine diversity of perspective.

## Examples

TODO: Add concrete examples from real usage.
