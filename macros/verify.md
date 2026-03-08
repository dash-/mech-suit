---
name: Verify
shorthand: verify
category: strategy
tags: []
summary: The agent checks produced output against defined criteria before passing it downstream, rejecting failures with explanation or routing them to refine.
composes_with: [gate, refine, emit]
opposes: []
---

# Verify (`verify`)

When this macro is invoked, the agent checks produced output against defined criteria — correctness, completeness, format, or constraints — before passing it downstream. Verification happens before handoff, never after. When verification fails, the agent either rejects the output with a clear explanation or routes it to `refine`.

## Examples

TODO: Add concrete examples from real usage.
