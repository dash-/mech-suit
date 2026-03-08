---
name: Output Posture
shorthand: output-posture
category: pattern
tags: [communication]
summary: How assertive and proactive the agent is in its communication.
composes_with: [addressable-output, inversion-of-control]
opposes: []
---

# Output Posture (`output-posture`)

**Tags:** `communication`

How assertive and proactive the agent is in its communication. A spectrum from "just answer what was asked" to "actively drive the conversation forward." Configured per agent, per context, or per user preference.

```
Passive:     User asks → Agent answers → stops
Suggestive:  User asks → Agent answers → "You might want to also consider X"
Proactive:   User asks → Agent answers → "Here's what I'd do next: ..." → drives forward
Opinionated: User asks → Agent recommends → "I'd go with B because ..." → defends position
```

**Named postures:**
- **Passive** — answer only what's asked, add nothing. Good for expert users who know what they want.
- **Suggestive** — answer, then offer a next step or related consideration. Good default for most interactions.
- **Proactive** — actively suggest the next action and offer to execute it. Good for workflows where the agent should drive.
- **Opinionated** — lead with a recommendation and rationale. Good for decision support where the human wants a point of view, not a menu.

**When to use:**
- Different users want different levels of agent initiative (experts vs. novices)
- Different tasks call for different postures (brainstorming → proactive, code review → passive)
- You want agents to feel helpful without being overbearing

**Tradeoffs:**
- **Pro:** Matching posture to context makes agents feel natural rather than robotic or pushy
- **Pro:** Proactive posture catches things the user didn't think to ask about
- **Con:** Wrong posture is jarring — proactive when the user wants passive feels paternalistic
- **Con:** Opinionated agents can anchor the human on a premature conclusion

**Key decisions:**
- Default posture: suggestive is usually safest
- Override mechanism: can the user say "just answer, don't suggest"?
- Task-adaptive: should posture shift automatically based on task type?

**Notes:** Pairs with **Inversion of Control** (proactive posture is a light version of IoC). Interacts with **Addressable Output** (opinionated posture should still present alternatives, just with a clear recommendation).

## Examples

TODO: Add concrete examples from real usage.
