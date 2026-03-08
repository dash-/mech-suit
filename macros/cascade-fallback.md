---
name: Cascade & Fallback
shorthand: cascade-fallback
category: pattern
tags: [reliability]
summary: Primary agent attempts the task.
composes_with: []
opposes: []
---

# Cascade & Fallback (`cascade-fallback`)

**Tags:** `reliability`

Primary agent attempts the task. On failure, system falls back to alternative agent/approach. Each level has different characteristics, not necessarily "better."

```
Primary → success → done
       → failure → Fallback A → success → done
                              → failure → Fallback B → ...
```

**When to use:**
- Reliability is critical — you need *some* output
- Different approaches have different failure modes
- Integrating external services that may be unavailable

**Tradeoffs:**
- **Pro:** Dramatically improves system reliability
- **Con:** Fallback quality may be lower — inconsistent experience
- **Con:** Silent quality degradation if not monitored


**Distinction from Routing:** Cascade & Fallback is *failure-triggered* — try the primary, fall back on failure. **Routing** is *classification-triggered* — classify the input and dispatch to the best handler directly. Both select among alternatives, but the trigger mechanism and error model are different. Cascade assumes a preferred option that might fail; Routing assumes multiple equally valid options selected by input characteristics.

## Examples

TODO: Add concrete examples from real usage.
