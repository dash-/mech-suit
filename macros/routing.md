---
name: Routing
shorthand: routing
category: pattern
tags: [decisions, cost]
summary: Evaluate incoming input (intent, type, complexity) and dispatch to the most appropriate handler, tool, or sub-agent.
composes_with: [cascade-fallback, escalation-ladder, orchestrator-subagent]
opposes: []
---

# Routing (`routing`)

**Tags:** `decisions` `cost`

Evaluate incoming input (intent, type, complexity) and dispatch to the most appropriate handler, tool, or sub-agent. Unlike **Cascade & Fallback** (which tries options sequentially on failure), Routing classifies first and dispatches to the *best* handler directly.

```
Input → Classifier → Category A → Handler A
                   → Category B → Handler B
                   → Category C → Handler C
```

**When to use:**
- The system must choose between multiple distinct workflows based on input characteristics
- Different input types require genuinely different processing (not just fallback alternatives)
- You want to optimize cost/latency by routing simple inputs to cheaper handlers

**Tradeoffs:**
- **Pro:** Each handler is optimized for its input type — better quality than one-size-fits-all
- **Pro:** Cost savings by routing simple queries to cheap/fast models, complex to expensive
- **Con:** Misclassification sends input to the wrong handler — errors are systematic, not random
- **Con:** Routing logic itself adds latency and requires maintenance

**Variants:**
- **LLM-based** — Use the LLM itself to classify input and output a routing label
- **Embedding-based** — Convert input to a vector embedding, compare against route embeddings, dispatch to nearest match
- **Rule-based** — Deterministic rules (regex, keyword matching, input length)
- **ML-classifier** — Train a small discriminative model on labeled routing data (cheaper and faster than LLM routing at inference, but requires training data)

**Key decisions:**
- Classification method: LLM, embedding similarity, trained classifier, or rules?
- Fallback: what happens when no route matches confidently? (Default handler? Escalate?)
- Monitoring: track misrouting rate to detect classification drift

**Notes:** Distinct from **Cascade & Fallback** (failure-triggered sequential fallback) and **Escalation Ladder** (cost-triggered escalation). Routing is classification-triggered dispatch. Often precedes **Orchestrator-Subagent** (router dispatches to specialized sub-agents).

## Examples

TODO: Add concrete examples from real usage.
