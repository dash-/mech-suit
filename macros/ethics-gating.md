---
name: Ethics Gating
shorthand: ethics-gating
category: pattern
tags: [convergent, quality, reliability]
summary: Dedicated ethics agent evaluates plans/content/actions against codified ethical framework.
composes_with: []
opposes: []
---

# Ethics Gating (`ethics-gating`)

**Tags:** `convergent` `quality` `reliability`

Dedicated ethics agent evaluates plans/content/actions against codified ethical framework. Hard veto power — can block any action regardless of other agents. Only human intervention can override.

```
Proposed Action → Ethics Agent → Approve → Execute
                               → Veto → Block + Explanation → Human Review
```

**When to use:**
- System outputs affect real people
- Defined ethical boundaries that must never be crossed
- Regulatory or organizational compliance requires audit trail

**Tradeoffs:**
- **Pro:** Prevents harmful outputs reaching production
- **Pro:** Audit trail; can be a positive selling point
- **Con:** False positives block legitimate work
- **Con:** Can only catch violations it's trained to recognize

**Key decisions:**
- Scope: plans only? content only? both?
- Framework source: regulatory, organizational, industry standards?
- Override mechanism: which humans, what escalation path?


**Scope beyond ethics:** While the core pattern is ethics-focused, production systems apply the same gating structure to broader safety concerns: jailbreak detection, off-topic filtering, brand safety, competitive information blocking, and regulatory compliance. The structural pattern is identical — a dedicated gate with veto power — but the evaluation criteria differ.

**Variants:**
- **Rule-based** — Allow/deny lists, regex filters, schema validation. Fast and deterministic but brittle against novel threats
- **LLM-as-guardrail** — A fast, cheap model acts as a dedicated policy enforcer, screening inputs/outputs against detailed safety directives. Semantically aware — catches threats that rules miss (prompt injection, subtle policy violations)
- **Layered defense** — Input gate (pre-processing) + behavioral constraints (prompt-level) + tool-use restrictions (callback-based) + output gate (post-processing). Defense in depth

## Examples

TODO: Add concrete examples from real usage.
