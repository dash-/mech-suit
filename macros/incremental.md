---
name: Incremental
shorthand: incremental
category: modifier
tags: []
summary: The agent processes only what has changed since the last execution, computing a delta from a baseline and operating on that delta rather than the full corpus.
composes_with: [refine, verify, cache, progressive-refinement, verification-loop]
opposes: [eager, exhaustive]
---

# Incremental (`incremental`)

When this modifier is applied, the agent processes only what has changed since the last execution. It must first establish a baseline (what was the prior state?), then compute a delta. All downstream logic operates on the delta, not the full corpus. The agent must reason about change detection, staleness, and whether partial updates preserve correctness of the whole.

## Decision Tree

```
Detect changes by **hash comparison**, **timestamp**, **diff against prior output**, or **explicit signal from caller**?
```

## Examples

TODO: Add concrete examples from real usage.
