---
name: Prompt Configuration
shorthand: prompt-configuration
category: pattern
tags: [setup, quality]
summary: Treat prompt templates as first-class configurable artifacts — versioned, tested, and swappable without code changes.
composes_with: [canary-shadow-mode, persona-injection, warm-up-calibration]
opposes: []
---

# Prompt Configuration (`prompt-configuration`)

**Tags:** `setup` `quality`

Treat prompt templates as first-class configurable artifacts — versioned, tested, and swappable without code changes. Prompts are not hardcoded strings; they're configuration that shapes agent behavior, and they deserve the same rigor as any other configuration.

```
Prompt template (versioned, stored externally)
  → Variables injected at runtime (context, task, constraints)
  → Agent executes with assembled prompt
  → Output quality tracked per prompt version
  → A/B test: version A vs version B on same inputs → compare quality
```

**Different from Persona Injection:** Persona Injection shapes *who the agent is* (identity, expertise, norms). Prompt Configuration shapes *how the agent is instructed* (task framing, output format, constraints). A persona is one component that might be assembled into a prompt configuration.

**When to use:**
- Multiple people tune prompts and need version control / rollback
- You want to A/B test different prompt strategies on the same task
- Prompt changes are frequent and shouldn't require code deployments
- You need an audit trail of which prompt version produced which outputs

**Tradeoffs:**
- **Pro:** Prompts can be iterated without code changes — faster experimentation
- **Pro:** Version history enables rollback when a new prompt underperforms
- **Pro:** A/B testing reveals which prompt strategies actually work vs which seem clever
- **Con:** Adds infrastructure — template storage, variable injection, version management
- **Con:** Prompt interactions are complex — changing one section can break behavior elsewhere

**Key decisions:**
- Storage: files in a repo? database? config service?
- Templating: simple variable substitution? conditional sections? composable fragments?
- Testing: manual review? automated quality regression? A/B with statistical significance?
- Versioning: semantic versioning? hash-based? per-agent or global?

**Notes:** Pairs with **Persona Injection** (persona is a composable fragment within prompt configuration), **Warm-up & Calibration** (test new prompt versions against historical cases before going live), and **Canary & Shadow Mode** (shadow-test new prompts against production).

## Examples

TODO: Add concrete examples from real usage.
