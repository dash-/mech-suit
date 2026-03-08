---
name: Debate & Consensus
shorthand: debate-consensus
category: pattern
tags: [convergent, decisions, coordination]
summary: Multiple agents argue different positions in structured rounds.
composes_with: []
opposes: []
---

# Debate & Consensus (`debate-consensus`)

**Tags:** `convergent` `decisions` `coordination`

Multiple agents argue different positions in structured rounds. A moderator tracks agreement/disagreement. Process continues until consensus or max rounds, then moderator synthesizes.

```
Round 1: Agent A argues → Agent B argues → Agent C argues
Round 2: Agent A rebuts B,C → Agent B rebuts A,C → Agent C rebuts A,B
...
Moderator: Synthesizes agreement, flags unresolved disagreements
```

**When to use:**
- The question is genuinely ambiguous with multiple legitimate perspectives
- You want the reasoning, not just the conclusion
- The domain has real disagreement (ethics, strategy, creative direction)

**Tradeoffs:**
- **Pro:** Surfaces reasoning and tradeoffs a single agent might miss
- **Pro:** Debate transcript documents *why* a decision was made
- **Con:** Can be slow and expensive (3-10x cost)
- **Con:** Agents may converge too quickly (groupthink) or too slowly (circular arguments)

**Key decisions:**
- Assigned vs. organic positions
- Structured rounds (claim → evidence → rebuttal) vs. freeform
- Consensus threshold: unanimous? majority? moderator's judgment?


**Variants:**
- **Chain of Debates (CoD)** — Linear: agents argue in sequence, each responding to the previous speaker
- **Graph of Debates (GoD)** — Non-linear: arguments form a graph with support and refutation edges between nodes. Conclusions are found by identifying the most robust argument clusters. Richer than linear debate but harder to manage and synthesize

## Examples

TODO: Add concrete examples from real usage.
