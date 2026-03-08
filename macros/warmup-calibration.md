---
name: Warm-up & Calibration
shorthand: warmup-calibration
category: pattern
tags: [deployment, quality]
summary: Before the system goes live, run it against known historical cases to verify it produces reasonable outputs.
composes_with: []
opposes: []
---

# Warm-up & Calibration (`warmup-calibration`)

**Tags:** `deployment` `quality`

Before the system goes live, run it against known historical cases to verify it produces reasonable outputs. Like backtesting in finance or shadow deployment in ML.

**Process:**
1. Select historical cases with known outcomes
2. Run the system against those cases
3. Compare system outputs to known-good human outputs
4. Identify systematic biases or failure modes
5. Adjust prompts, parameters, or patterns before going live

**When to use:**
- Before deploying a new agent system or major revision
- When you have historical data to calibrate against (Swayable's 6,600+ studies)
- When the cost of a bad first impression with clients is high

**Key insight:** This is not just testing — it's calibrating. The system may need its priors adjusted, its confidence thresholds tuned, or its escalation triggers recalibrated based on how it performs on known cases.

## Examples

TODO: Add concrete examples from real usage.
