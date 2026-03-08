---
name: Modifier
type: category
---

# Modifier

**Role:** Cross-cutting constraints — the "with what adjustment" of execution.

**Form:** Adjectives. Modifiers attach to other macros to change how they execute. A modifier never fires alone.

**Distinguishing trait:** Modifiers change the agent's execution contract without changing the goal. `verify + incremental` still verifies — but only the delta. If removing the modifier wouldn't change behavior, it doesn't belong in this category.

**Examples:** `non-destructive`, `lazy`, `incremental`, `publishable`, `scoped`, `versionable`

**Relationship to other categories:** Modifiers are orthogonal — they can attach to strategies, patterns, or skills. Multiple modifiers can stack. Some pairs create productive tension (`lazy + fail-fast`) that must be resolved explicitly. Some concepts like `idempotent` and `transparent` are both principles and modifiers.
