---
name: Delegate
shorthand: delegate
category: strategy
tags: [coordination, cost]
summary: The agent identifies work outside its core responsibility and passes it to a specialist with only the authority and context needed.
composes_with: [decompose, isolate, gate]
opposes: [escalate]
---

# Delegate (`delegate`)

When this macro is invoked, the agent identifies work that falls outside its core responsibility or optimal scope and passes it to a specialist with only the authority and context needed for that sub-task. It defines the interface clearly — inputs, expected outputs, constraints — and reclaims control when the delegate returns.

The delegating agent doesn't need to know *how* the delegate works — just what it does and what it returns.

```
/ticket needs to check for duplicates
  → delegates to /find-ticket (a reusable search skill)
    → delegates to Linear search MCP
      → returns matching tickets
```

## Decision Tree

- Delegate to subagent, external service, or human?
- Pass full context or minimal context (need-to-know)?
- Is the capability a named, reusable skill (exists before and after this task) or a one-off worker (created and dissolved for this task)?

## When to Use

- The capability already exists as a tested, named skill or service
- Multiple commands/agents need the same capability
- Work falls outside the current agent's specialization

## Tradeoffs

- **Pro:** DRY — build once, use everywhere
- **Pro:** Delegates can be tested and improved independently of their consumers
- **Con:** Interfaces become implicit contracts — changing a delegate can break consumers
- **Con:** Indirection makes debugging harder (failure chains across delegates)

## Examples

TODO: Add concrete examples from real usage.
