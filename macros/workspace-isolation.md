---
name: Workspace Isolation
shorthand: workspace-isolation
category: pattern
tags: [setup]
summary: Create isolated execution environments per task — separate file trees, branches, configs, or runtime contexts.
composes_with: [session-forking]
opposes: []
---

# Workspace Isolation (`workspace-isolation`)

**Tags:** `setup`

Create isolated execution environments per task — separate file trees, branches, configs, or runtime contexts. Prevents cross-contamination between parallel work. Physical/filesystem analog of **Session Forking** (which isolates AI conversation context).

```
Ticket A → Worktree A (ui + swaypi) → isolated branch, files, state
Ticket B → Worktree B (ui + swaypi) → isolated branch, files, state
  (no cross-contamination)
```

**When to use:**
- Multiple tasks run in parallel on the same codebase
- Tasks might conflict (touching the same files, conflicting dependencies)
- You need to context-switch between tasks without stashing/resetting

**Tradeoffs:**
- **Pro:** Zero cross-contamination between parallel work
- **Pro:** Instant context switching — just cd to the other worktree
- **Pro:** Each workspace can have its own test state, running servers, etc.
- **Con:** Disk space for multiple copies of the codebase
- **Con:** Shared resources (databases, ports) can still conflict

**Notes:** Pairs with **Session Forking** — each workspace gets its own AI session forked from a base.

## Examples

TODO: Add concrete examples from real usage.
