---
name: Confidence Signaling
shorthand: confidence-signaling
category: pattern
tags: [quality, cost, decisions]
summary: Agents report their confidence level alongside their output.
composes_with: [budget-aware-execution, escalation-ladder, verification-loop]
opposes: []
---

# Confidence Signaling (`confidence-signaling`)

**Tags:** `quality` `cost` `decisions`

Agents report their confidence level alongside their output. Downstream agents or orchestrators use this signal to decide whether to verify, escalate, or accept. Low confidence triggers **Verification Loop** or **Redundant Generation**. High confidence allows skipping expensive quality checks.

```
Agent Output: {
  result: "Peer testimonial framing recommended",
  confidence: 0.85,
  confidence_rationale: "Strong historical signal from 47 similar studies"
}

Orchestrator: confidence > 0.8 → accept
              confidence 0.5-0.8 → verify
              confidence < 0.5 → escalate to redundant generation
```

**When to use:**
- You want adaptive quality assurance — not every output needs the same scrutiny
- Agents vary in how certain they are about different tasks
- You're budget-conscious and want to skip expensive checks when confidence is high

**Tradeoffs:**
- **Pro:** Enables cost-efficient quality assurance — expensive patterns only where needed
- **Pro:** Surfacing uncertainty is itself valuable information for downstream decisions
- **Con:** Agents may be miscalibrated — high confidence doesn't guarantee correctness
- **Con:** Agents may learn to game confidence scores if they're rewarded for high confidence

**Key decisions:**
- Confidence format: numeric (0-1)? categorical (low/medium/high)? multi-dimensional?
- Calibration: how do you verify that stated confidence correlates with actual accuracy?
- Routing rules: what confidence thresholds trigger which quality patterns?

**Notes:** Natural partner to **Verification Loop**, **Escalation Ladder**, and **Budget-Aware Execution**. The confidence signal is what drives adaptive routing through quality patterns.

## Examples

TODO: Add concrete examples from real usage.
