---
name: Learning Loop
shorthand: learning-loop
category: pattern
tags: [learning]
summary: **Background Observation** → **Memory & Retrieval** → **Scoped Promotion** → **Decision Calibration**
composes_with: []
opposes: []
---

# Learning Loop (`learning-loop`)

**Tags:** `learning`

**Background Observation** → **Memory & Retrieval** → **Scoped Promotion** → **Decision Calibration**

Passively observe agent behavior, store learnings in scoped memory, promote proven patterns to broader scope, review decisions to calibrate future heuristics.

**When to use:**
- The system operates across multiple projects or engagements
- You want institutional memory that compounds over time
- Learnings should be validated before being applied broadly


**Variants:**
- **Self-modification** — The agent reviews an archive of its own past versions and performance scores, proposes modifications to its own codebase or prompts, tests the modifications, and records results. Requires containerized execution and an asynchronous overseer for safety
- **Evolutionary optimization** — An ensemble of LLMs generates code/algorithm proposals, automated evaluators score them, and an evolutionary selection process iteratively refines the population. Combines **Tournament Selection** with LLM-generated mutations

## Examples

TODO: Add concrete examples from real usage.
