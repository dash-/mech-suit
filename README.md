# Macro Library

A mech suit for building things with agents. Each macro is a named concept with a precise expansion that any agent — human or AI — can invoke, compose, and rely on for predictable behavior.

## What a Macro Is

A macro is a **named, precise, reusable concept** that expands into specific agent behavior. It's not a suggestion or a definition — it's a tool. When invoked:

1. The agent **looks up** the macro's expansion
2. The agent **restates** the expansion applied to the current context ("Here's what I'll do: ...")
3. The invoker **confirms or adjusts** — this is a contract negotiation, not a deployment
4. Then execution happens

This solves the genie problem. Instead of "make it incremental" (vague, interpreted differently every time), you say `incremental` and the agent expands it into precise behavior that the invoker can validate before it fires.

## Why Agents Benefit Too

Macros aren't just for humans instructing agents. When an orchestrator delegates to a subagent, "apply `collapse + non-destructive`" is a compressed instruction that decompresses losslessly via catalog lookup. Without it, the orchestrator burns context window spelling out the full behavior — or paraphrases imprecisely and the subagent interprets differently. Same genie problem, just between agents.

## Categories

Macros are tagged by category. These are organizational aids, not rigid layers:

| Category | What it is | How it reads | Examples |
|----------|-----------|-------------|---------|
| **Principle** | A value or invariant | "Examine through this lens" | `DRY`, `SoC`, `fail-fast` |
| **Strategy** | An approach to action | "Do it this way" | `compose`, `collapse`, `delegate` |
| **Pattern** | A concrete reusable structure | "Follow this recipe" | `orchestrator-subagent`, `verification-loop` |
| **Modifier** | A cross-cutting property | "With this constraint" | `non-destructive`, `lazy`, `incremental` |
| **Anti-pattern** | A known failure mode | "Watch out for this" | `kitchen-sink`, `rubber-stamp` |

Some macros have multiple category tags. `idempotent` is both a principle ("value re-runnability") and a modifier ("make this specific operation re-runnable"). `transparent` is a principle, a modifier, and the basis for the `emit` strategy. This isn't a bug — the same concept genuinely operates differently depending on context.

Skills (`/pr-review`, `/deck`) are executable macro compositions — they live in skill files, not here.

## Composition

Macros compose. When you combine macros, the agent expands each one, synthesizes them in context, and restates the combined behavior for confirmation. No pre-authored combinations needed — the precision comes from two well-defined starting positions being merged.

Examples:
- `collapse + non-destructive` → "Resolve all references into a flat artifact, but preserve the compositional source alongside it"
- `verify + incremental` → "Check only what changed since last verification against the original spec"
- `delegate + scoped + transparent` → "Hand this sub-task to a specialist constrained to this boundary, with reasoning visible"

**Tensions** are valid compositions too. `lazy + fail-fast` creates a real tradeoff: defer work, but surface errors early. The agent should surface the tension and propose a resolution rather than silently picking a side.

**Deliberate violations:** A macro can *oppose* another. `generate` is intentionally anti-DRY — redundancy for quality. The opposition is the point, not a mistake.

## Decision Trees

Some macros trigger decision trees when composed — cross-cutting choices that must be resolved before execution.

Example: adding `versionable` to any expression opens:

```
How is versioning implemented?
  A. Git (branch/commit per version)
  B. Filename versioning (v1, v2, ...)
  C. Single file + version metadata (frontmatter, headers)
  D. External system (database, API)
  E. Append-only log (all versions in sequence)
```

The agent should present the decision tree, recommend an option based on context, and let the invoker choose. Decision trees are documented per-macro when they exist.

## Growing the Library

When a restatement keeps recurring — the agent keeps expanding the same concept from scratch — it earns a name and becomes a new macro. The library grows from use, not from speculation.

## Structure

```
layered-concepts/
  README.md          ← you are here
  intro.md           ← purpose, audience, how to use (for publishing)
  outro.md           ← growth model, open questions (for publishing)
  index.md           ← assembly instructions for publishing
  macros/            ← one file per macro, with frontmatter
    DRY.md
    compose.md
    non-destructive.md
    orchestrator-subagent.md
    ...
  taxonomy/          ← category and tag definitions
    principle.md
    strategy.md
    pattern.md
    modifier.md
    skill.md
    anti-pattern.md
```

### Macro file format

Each macro file has YAML frontmatter for machine-readable metadata, followed by the human-readable expansion:

```yaml
---
name: Collapse
shorthand: collapse
category: strategy
tags: []
summary: Resolve all references at build time into a flat, self-contained artifact.
composes_with: [normalize, verify, cache]
opposes: [defer]
---
```

### Legacy files

The flat category files (`principles.md`, `strategies.md`, `modifiers.md`, `patterns.md`, `skills.md`) remain as browsable overviews. The `macros/` directory is the source of truth.
