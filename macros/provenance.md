---
name: Provenance & Audit Trail
shorthand: provenance
category: pattern
tags: [monitoring, reliability]
summary: Every decision, output, and agent interaction is logged with rationale, inputs, and timestamps.
composes_with: []
opposes: []
---

# Provenance & Audit Trail (`provenance`)

**Tags:** `monitoring` `reliability`

Every decision, output, and agent interaction is logged with rationale, inputs, and timestamps. Creates a complete record of how the system arrived at its outputs.

**When to use:**
- Clients or stakeholders need visibility into what the system did and why
- Debugging requires tracing back through the decision chain
- Regulatory or organizational compliance demands audit trails
- You want retrospectives to identify which patterns and decisions led to good/bad outcomes

**Tradeoffs:**
- **Pro:** Builds trust — clients and admins can see exactly what happened
- **Pro:** Debugging becomes tracing a log, not guessing what went wrong
- **Pro:** Retrospectives have concrete data to analyze
- **Con:** Logging adds storage and (minor) latency overhead
- **Con:** Verbose logs can be hard to navigate without good tooling
- **Con:** Sensitive information in logs requires access control

**What to log:**
- Agent identity and role
- Input received (or summary if large)
- Decision made and rationale
- Output produced
- Confidence level
- Time and cost

**Key decisions:**
- Granularity: every tool call? every agent decision? only major milestones?
- Storage: structured (database) vs. append-only (JSONL) vs. integrated (Linear/GitHub comments)?
- Retention: how long do you keep logs? Compliance may dictate minimums.

## Examples

TODO: Add concrete examples from real usage.
