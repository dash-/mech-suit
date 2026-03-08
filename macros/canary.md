---
name: Canary & Shadow Mode
shorthand: canary
category: pattern
tags: [deployment]
summary: Run the new system in parallel with the existing human process.
composes_with: []
opposes: []
---

# Canary & Shadow Mode (`canary`)

**Tags:** `deployment`

Run the new system in parallel with the existing human process. Compare outputs, but don't let AI outputs reach production. Build confidence before switching over.

```
Client Request → Human Process → Production Output
              → AI Process → Shadow Output (logged, not delivered)
              → Compare → Learning
```

**When to use:**
- Replacing an existing human process with AI
- You need to demonstrate equivalence or superiority before switching
- Stakeholders need to see the system working before they trust it

**Differs from Warm-up:** Warm-up uses historical cases. Canary uses live cases in real time, but shields the client from the AI output.

## Examples

TODO: Add concrete examples from real usage.
