---
name: Decision Calibration
shorthand: decision-calibration
category: pattern
tags: [learning, decisions]
summary: At the time of making a decision, record the decision, the reasoning, the predicted outcome, and a mandatory future review date.
composes_with: []
opposes: []
---

# Decision Calibration (`decision-calibration`)

**Tags:** `learning` `decisions`

At the time of making a decision, record the decision, the reasoning, the predicted outcome, and a mandatory future review date. At review time, compare the prediction to the actual outcome. Use the delta to update decision-making heuristics.

```
Decide → Record prediction → Set review date → ... time passes ...
  → Review: Did we predict correctly? → Update beliefs / heuristics
```

**When to use:**
- The organization makes recurring decisions of similar types
- You want to get better at predicting outcomes over time
- Decisions are consequential enough to warrant structured review
- You want to build institutional memory about what works

**Tradeoffs:**
- **Pro:** Systematic improvement of decision quality over time
- **Pro:** Creates an audit trail of why decisions were made
- **Pro:** Surfaces overconfidence and blind spots
- **Con:** Requires discipline to actually do the review
- **Con:** Outcome quality is often ambiguous — hard to say definitively if a decision was "right"

**Relationship to Bayesian Steering:** This is **Bayesian Steering** applied to organizational decisions rather than automated experiments. The "priors" are the team's intuitions, the "test" is the real-world outcome, and the "posterior update" is the lesson learned.

## Examples

TODO: Add concrete examples from real usage.
