---
name: Budget-Aware Execution
shorthand: budget-aware-execution
category: pattern
tags: [cost, decisions]
summary: Agents know their cost budget and make quality/cost tradeoffs accordingly.
composes_with: [confidence-signaling, escalation-ladder]
opposes: []
---

# Budget-Aware Execution (`budget-aware-execution`)

**Tags:** `cost` `decisions`

Agents know their cost budget and make quality/cost tradeoffs accordingly. An orchestrator allocates budget to subtasks based on their importance and difficulty. Agents choose which quality patterns to apply based on their allocation.

```
Orchestrator: "Generate content variants. Budget: $5 LLM cost. Importance: high."

Agent reasoning:
  - $5 budget, high importance
  - Redundant Generation (3 agents) = ~$3
  - Hybrid Synthesis = ~$1
  - Verification Loop = ~$1
  - Total: $5 → use full quality stack

vs.

Orchestrator: "Format results for display. Budget: $0.50 LLM cost. Importance: low."

Agent reasoning:
  - $0.50 budget, low importance
  - Reflection only = ~$0.30
  - Total: $0.30 → use budget quality play
```

**When to use:**
- Total system budget is constrained
- Not all subtasks deserve the same quality investment
- You want the system to be cost-aware without manually tuning every step

**Tradeoffs:**
- **Pro:** Automatically allocates quality effort where it matters most
- **Pro:** Prevents the Kitchen Sink anti-pattern — expensive patterns used only when justified
- **Pro:** Makes cost predictable and auditable
- **Con:** Budget estimation is imprecise — actual LLM costs vary
- **Con:** Agents may under-invest in tasks that seem unimportant but turn out to matter

**Key decisions:**
- Budget unit: dollars? tokens? abstract "quality points"?
- Allocation strategy: orchestrator decides up-front? agents negotiate? fixed percentages?
- Over-budget handling: hard stop? borrow from reserve? alert human?

**Notes:** Natural partner to **Confidence Signaling** (high confidence → spend less on verification) and **Escalation Ladder** (start cheap, escalate only if needed).


**Router-agent architecture:**
A practical implementation combines three agents: a Router (classifies input complexity and selects the appropriate model/pipeline), an Answering Agent (executes with the selected resources), and a Critique Agent (evaluates response quality and feeds back into routing logic to improve allocation over time).

**Scaling Inference Law:** LLM performance predictably improves with increased compute at inference time. A smaller model with more "thinking budget" (structured reasoning steps, self-correction passes) can surpass a larger model with simpler generation. This provides the theoretical foundation for budget allocation decisions — investing in inference compute is a legitimate alternative to model upgrades.

## Examples

TODO: Add concrete examples from real usage.
