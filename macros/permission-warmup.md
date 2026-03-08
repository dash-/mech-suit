---
name: Permission Warm-up
shorthand: permission-warmup
category: pattern
tags: [setup]
summary: Before starting real work, identify every distinct permission category the plan requires and trigger each one with a small, harmless, *relevant* operation.
composes_with: [configurable-hitl, provenance]
opposes: []
---

# Permission Warm-up (`permission-warmup`)

**Tags:** `setup`

Before starting real work, identify every distinct permission category the plan requires and trigger each one with a small, harmless, *relevant* operation. This frontloads all access prompts to the beginning of execution, so the agent can confirm it has the access it needs before investing effort that might be blocked mid-stream.

```
Plan work → Identify permission categories (file writes, MCP tools, shell commands, git, etc.)
  → For each category: trigger with small, relevant operation
    (e.g., read the first file you'll actually edit, run a benign form of the command you'll use)
  → All granted? → Proceed with real work
  → Any denied? → Stop and discuss before proceeding
```

**When to use:**
- The agent operates in a permission-gated environment (approval prompts, sandboxes, ACLs)
- The plan touches multiple permission categories that the user must approve
- Mid-task permission denial would waste significant work already done
- You want the human to see the full scope of access needed up front, not piecemeal

**Tradeoffs:**
- **Pro:** No wasted work — if a permission is denied, you find out before investing effort
- **Pro:** Human sees the full access scope at once, which builds trust and reduces surprise
- **Pro:** Forces the agent to plan before acting — the permission audit is itself a planning step
- **Con:** Adds a small upfront latency cost for the warm-up operations
- **Con:** Warm-up operations must be genuinely relevant — contrived triggers feel like busywork

**Key decisions:**
- Granularity: warm up every individual file, or one file per permission category?
- Failure handling: if one category is denied, abort entirely or proceed with reduced scope?
- Caching: if permissions were granted in a recent session, skip warm-up?

**Notes:** Natural partner to **Configurable HITL** (warm-up happens at the most restrictive HITL level). Pairs with **Provenance** (log which permissions were requested and granted).

## Examples

TODO: Add concrete examples from real usage.
