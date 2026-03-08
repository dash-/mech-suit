---
name: Publishable
shorthand: publishable
category: modifier
tags: []
summary: The agent treats the output as audience-facing, applying a higher quality bar with mandatory review and verification steps.
composes_with: [compose, verify, gate, content-factory, adversarial-review, configurable-hitl]
opposes: [lazy, speculative]
---

# Publishable (`publishable`)

When this modifier is applied, the agent treats the output as audience-facing: it must be self-contained, properly formatted, and free of internal shorthand, TODOs, or draft markers. The agent applies a higher quality bar, reasons about the target audience and medium, and makes review and verification steps mandatory rather than optional.

## Decision Tree

```
Publish to **file**, **API**, **message channel**, or **external service**?
Audience: **technical peers**, **non-technical stakeholders**, or **general public**?
```

## Examples

TODO: Add concrete examples from real usage.
