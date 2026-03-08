---
name: Adversarial Review
shorthand: adversarial-review
category: pattern
tags: [convergent, quality, coordination]
summary: A producer agent generates an artifact (plan, content, code, hypothesis — any output).
composes_with: [configurable-hitl, ethics-gating, inversion-of-control]
opposes: []
---

# Adversarial Review (`adversarial-review`)

**Tags:** `convergent` `quality` `coordination`

A producer agent generates an artifact (plan, content, code, hypothesis — any output). A red team of adversarial agents attacks it, finding weaknesses, gaps, and failure modes. A blue team proposes patches. Judge agents evaluate whether patches are sufficient. The cycle repeats until judges are satisfied or iteration limit is reached.

```
Producer → Artifact → Red Team (attack) → Blue Team (patch) → Judges (grade)
    ↑                                                               │
    └──────────────── iterate if insufficient ─────────────────────┘
```

**Applies to any artifact:**
- **Plans** — find methodological gaps, budget risks, unstated assumptions
- **Content** — find off-brand messaging, weak arguments, ethical issues
- **Code** — find bugs, security vulnerabilities, performance issues
- **Hypotheses** — find confounds, alternative explanations, measurement problems
- **Experiment designs** — find sources of bias, power issues, missing controls

**When to use:**
- The artifact has high consequences for failure
- You want to surface non-obvious failure modes before committing resources
- The domain has known adversarial dynamics

**Tradeoffs:**
- **Pro:** Dramatically reduces shipping artifacts with obvious holes
- **Pro:** Red team agents can be specialized by failure mode (ethical, methodological, statistical, budgetary)
- **Con:** Expensive — multiple agents, multiple rounds (5-15x single agent cost)
- **Con:** Can be overly conservative if judges have low risk tolerance

**Key decisions:**
- Red team specialization: one generalist or multiple specialists?
- Convergence criteria: score threshold? unanimous agreement? max rounds?
- Patch granularity: individual issues or full artifact regeneration?
- Scope: review the whole artifact each round, or focus on previously identified weaknesses?

**Notes:** Often preceded by **Inversion of Control** (interview → then red-team the result). Pairs with **Ethics Gating** (ethics as a specialized red team dimension) and **Configurable HITL** (human approves after judges).

## Examples

TODO: Add concrete examples from real usage.
