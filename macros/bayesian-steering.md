---
name: Bayesian Steering
shorthand: bayesian-steering
category: pattern
tags: [decisions, learning]
summary: The system maintains hypotheses with probabilities.
composes_with: [checkpoint-resume, escalation-ladder, memory-retrieval]
opposes: []
---

# Bayesian Steering (`bayesian-steering`)

**Tags:** `decisions` `learning`

The system maintains hypotheses with probabilities. Actions are chosen to maximize expected information gain. After each observation, beliefs update via Bayes' rule.

```
Hypotheses (with priors) → Select action maximizing E[info gain] → Execute
         ↑                                                            │
         └──────────── Update posteriors with observation ────────────┘
```

**When to use:**
- Iterative process with a budget (time, money, compute)
- Each iteration produces results bearing on multiple hypotheses
- Meaningful priors exist (historical data, domain knowledge)

**Tradeoffs:**
- **Pro:** Provably optimal resource allocation for uncertainty reduction
- **Pro:** Natural stopping criteria (Bayes factor thresholds)
- **Pro:** Priors from historical data encode institutional knowledge
- **Con:** Requires well-defined hypothesis space
- **Con:** Prior miscalibration can misdirect early iterations
- **Con:** More computationally complex than simple heuristics

**Key decisions:**
- Prior source: expert judgment, historical data, literature, uninformative?
- Hypothesis granularity: broad or specific?
- Multi-hypothesis actions: can one action update multiple hypotheses? (Yes — this is where efficiency comes from)

**Notes:** Pairs with **Memory & Retrieval** (historical data informs priors), **Escalation Ladder** (escalate modality as uncertainty narrows), and **Checkpoint & Resume** (save hypothesis state across sessions).

## Examples

TODO: Add concrete examples from real usage.
