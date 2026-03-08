---
name: Structured Reasoning
shorthand: structured-reasoning
category: pattern
tags: [quality, decisions]
summary: 'Make an agent''s reasoning process explicit and auditable by structuring it as a sequence of intermediate steps rather than producing answers in a single pass.'
composes_with: [adversarial-review, budget-aware-execution, reflection-self-critique]
opposes: []
---

# Structured Reasoning (`structured-reasoning`)

**Tags:** `quality` `decisions`

Make an agent's reasoning process explicit and auditable by structuring it as a sequence of intermediate steps rather than producing answers in a single pass. The foundational technique that underpins many other quality patterns — when an agent "thinks step by step," it decomposes complex problems, catches errors, and produces more reliable outputs.

```
Single-pass:    Question → Answer (opaque)
Structured:     Question → Step 1 → Step 2 → ... → Step N → Answer (auditable)
```

**When to use:**
- Complex problems requiring multi-step logic, decomposition, or tool interaction
- When transparency of reasoning is as important as the final answer
- When you want self-correction opportunities between steps

**Tradeoffs:**
- **Pro:** Dramatically improves accuracy on complex tasks
- **Pro:** Transparent, auditable reasoning chains — you can see *where* it went wrong
- **Pro:** Enables self-correction at each step rather than only at the end
- **Con:** Higher token usage and latency (more generation per answer)
- **Con:** Reasoning steps can be confabulated — coherent-sounding but wrong
- **Con:** Requires compute budget allocation (more thinking = better results, but costs more)

**Variants:**
- **Chain-of-Thought (CoT)** — Linear sequence of reasoning steps. Can be few-shot (with worked examples) or zero-shot ("think step by step")
- **Tree-of-Thought (ToT)** — Explores multiple branching reasoning paths simultaneously, evaluates branches, and backtracks from dead ends. Richer than linear CoT but more expensive
- **ReAct** — Interleaved thought-action-observation loop: reason about what to do, execute a tool/action, observe the result, incorporate it into the next reasoning step. The core agentic operational loop

**Key decisions:**
- Reasoning depth: how many steps? Fixed or adaptive? (Scaling Inference Law: more compute at inference time = predictably better quality)
- Branching: linear chain sufficient, or does the problem require exploring alternatives (ToT)?
- Grounding: pure reasoning, or interleaved with tool use (ReAct)?

**Notes:** This is an enabling pattern — it makes other patterns more effective. **Reflection & Self-Critique** is structured reasoning applied to self-evaluation. **Adversarial Review** works better when agents show their reasoning chains. Pairs with **Budget-Aware Execution** (allocate reasoning budget proportional to task importance).

## Examples

TODO: Add concrete examples from real usage.
