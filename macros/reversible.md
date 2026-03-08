---
name: Reversible
shorthand: reversible
category: [principle, modifier]
tags: []
summary: The agent identifies every point of no return and captures sufficient state before acting to enable rollback, biasing execution order toward safety.
composes_with: [non-destructive, idempotent, incremental, delegate, gate, escalate, orchestrator-subagent, configurable-hitl]
opposes: [eager]
---

# Reversible (`reversible`)

## As Principle

When this macro is invoked, the agent identifies every point of no return in the current context — destructive operations without backup, one-way deployments, writes that overwrite without preserving the original. For each, it proposes an alternative that preserves a recovery path: soft deletes, backup-before-write, staged rollouts, or undo mechanisms. The test: "If this turns out to be wrong, what's the recovery path?"

## As Modifier

When this modifier is applied, the agent captures sufficient state before acting to enable rollback. It reasons about what "undo" means for each step, what state to snapshot, and whether partial rollback is meaningful. Execution order is biased toward safety: reversible steps first, irreversible ones last and only after confirmation.

## Examples

TODO: Add concrete examples from real usage.
