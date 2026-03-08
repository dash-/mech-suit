---
name: Persona Injection
shorthand: persona-injection
category: pattern
tags: [context, setup]
summary: Giving an agent a specific identity, expertise, or perspective to shape its behavior.
composes_with: []
opposes: []
---

# Persona Injection (`persona-injection`)

**Tags:** `context` `setup`

Giving an agent a specific identity, expertise, or perspective to shape its behavior. More than a system prompt — it includes domain knowledge, decision-making frameworks, and behavioral norms.

**When to use:**
- You want agents specialized for specific industries or client types
- Different agents in the same system need genuinely different perspectives
- You want consistent behavior across sessions

**Examples:**
- Healthcare persuasion specialist (knows FDA messaging rules, health literacy levels)
- Political campaign strategist (knows FEC rules, voter psychology research)
- CPG brand expert (knows category dynamics, retail media norms)

**Key decisions:**
- Static vs. dynamic personas (fixed at design time or assembled at runtime from components?)
- Persona depth: light touch (a paragraph) or deep (pages of domain knowledge)?
- Persona testing: how do you verify the persona produces the right behavioral changes?

## Examples

TODO: Add concrete examples from real usage.
