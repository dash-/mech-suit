---
name: Isolate
shorthand: isolate
category: strategy
tags: [setup]
summary: The agent sets up boundaries so that a risky or uncertain operation cannot affect anything outside its designated area.
composes_with: [delegate, gate, defer, session-forking]
opposes: []
---

# Isolate (`isolate`)

When this macro is invoked, the agent sets up boundaries — sandboxes, scoped permissions, or working copies — so that a risky or uncertain operation cannot affect anything outside its designated area. Isolation is applied before the risky action, not as cleanup after. If the operation fails, damage is contained to the isolated scope.

```
Ticket A → Worktree A (isolated branch, files, state)
Ticket B → Worktree B (isolated branch, files, state)
  (no cross-contamination)
```

## Decision Tree

- Isolate by process boundary, filesystem copy (worktree), or permission scope?
- Shared resources (databases, ports) — isolate those too, or accept the risk?
- Cleanup: auto-dispose on completion, or preserve for debugging?

## When to Use

- Multiple tasks run in parallel on the same codebase or system
- Tasks might conflict (touching the same files, conflicting dependencies)
- You need to context-switch between tasks without stashing/resetting
- An operation is risky and you want to contain the blast radius

## Tradeoffs

- **Pro:** Zero cross-contamination between parallel work
- **Pro:** Instant context switching between isolated environments
- **Con:** Disk space / resource cost for multiple copies
- **Con:** Shared resources can still conflict despite isolation

## Examples

TODO: Add concrete examples from real usage.
