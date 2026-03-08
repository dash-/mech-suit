---
name: Prioritization
shorthand: prioritization
category: pattern
tags: [decisions, cost]
summary: Agents assess and rank competing tasks, objectives, or actions based on urgency, importance, dependencies, resource availability, and cost/benefit.
composes_with: [budget-aware-execution, rate-limiting-backpressure]
opposes: []
---

# Prioritization (`prioritization`)

**Tags:** `decisions` `cost`

Agents assess and rank competing tasks, objectives, or actions based on urgency, importance, dependencies, resource availability, and cost/benefit. Ensures focus on the most critical work first. Distinct from **Budget-Aware Execution** (which manages *resource allocation*) — Prioritization manages *task ordering*.

```
Task Queue → Prioritization Agent → Ranked Tasks
  → Execute highest priority
  → Re-prioritize when circumstances change (new events, completed tasks, deadlines)
```

**When to use:**
- An agent must autonomously manage multiple, potentially conflicting tasks
- Resources (time, compute, budget) are insufficient to do everything at once
- Priorities shift dynamically as new information arrives

**Tradeoffs:**
- **Pro:** Prevents wasted effort on low-value tasks when high-value work is waiting
- **Pro:** Dynamic re-prioritization keeps the system adaptive to changing conditions
- **Con:** Sophisticated ranking criteria require more computation
- **Con:** Low-priority tasks may starve if re-prioritization always favors new urgent work

**Levels:**
- **Strategic** — Which goals to pursue (OKR-level)
- **Tactical** — Which plan steps to execute next (within a goal)
- **Immediate** — Which action to take right now (within a step)

**Key decisions:**
- Ranking criteria: urgency? importance? dependencies? cost/benefit ratio? Weighted combination?
- Re-prioritization trigger: on every new task? on schedule? on significant events only?
- Starvation prevention: age-based priority boost? reserved capacity for low-priority work?

**Notes:** Natural partner to **Budget-Aware Execution** (budget constrains how far down the priority list you can go) and **Rate Limiting & Backpressure** (backpressure signals trigger re-prioritization).

## Examples

TODO: Add concrete examples from real usage.
