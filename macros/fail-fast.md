---
name: Fail Fast
shorthand: fail-fast
category: principle
tags: []
summary: Trace every error path and identify where bad state can travel far from its origin before detection, proposing to move detection to the earliest possible moment.
composes_with: [explicit, transparent, verify]
opposes: [lazy]
---

# Fail Fast (`fail-fast`)

When this macro is invoked, the agent traces every error path and identifies where bad state can travel far from its origin before detection. It flags silent failures, bare exception handlers that swallow errors, functions returning ambiguous sentinel values, and late validation of input that was available earlier. For each finding, the agent proposes moving detection to the earliest possible moment.

## Decision Tree

```
How should the early failure surface?
  A. Throw/raise (halt execution with a clear error)
  B. Return typed error (let the caller decide)
  C. Validate at boundary (reject bad input before it enters the system)
  D. Assert invariant (crash on impossible state in development)
```

## Examples

TODO: Add concrete examples from real usage.
