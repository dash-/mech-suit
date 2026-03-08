---
name: Inversion of Control
shorthand: inversion-of-control
category: pattern
tags: [coordination, communication]
summary: The agent drives the process; the human (or calling agent) provides input on demand.
composes_with: [adversarial-review, configurable-hitl]
opposes: []
---

# Inversion of Control (`inversion-of-control`)

**Tags:** `coordination` `communication`

The agent drives the process; the human (or calling agent) provides input on demand. Instead of "human tells agent what to do," the agent asks the human targeted questions, drives through a framework, and assembles the result. The agent has better judgment about *process*; the human has better judgment about *content*.

```
Traditional:    Human → "Do X" → Agent → Output
Inverted:       Agent → "What is your goal?" → Human answers
                Agent → "What constraints?" → Human answers
                Agent → "Here are 3 options..." → Human picks
                Agent → Output
```

**Applies at multiple levels:**
- **Agent ↔ Human** — Planning Agent interviews the client instead of taking a brief
- **Agent ↔ Agent** — Orchestrator asks a subagent "what should I do next?" and follows its recommendation
- **Skill ↔ User** — `/decide` drives the user through a decision framework rather than accepting a pre-formed decision

**When to use:**
- The process has known structure but the content is unique each time
- Humans skip important steps when left to drive themselves (incomplete briefs, missing constraints)
- You want consistent, thorough process regardless of who the human is
- The agent has access to a framework or checklist the human might not know

**Tradeoffs:**
- **Pro:** Ensures completeness — the agent asks about things humans forget
- **Pro:** Consistent process quality regardless of human expertise level
- **Pro:** Captures structured data that downstream agents can consume directly
- **Con:** Can feel paternalistic if the human already knows what they want
- **Con:** Rigid interview flows frustrate expert users — consider adaptive depth
- **Con:** Agent must handle unexpected answers gracefully (humans go off-script)

**Key decisions:**
- Adaptive vs. fixed flow: does the agent skip questions based on prior answers?
- Escape hatch: can the human say "just take this brief and run with it"?
- Depth calibration: expert users get fewer questions, novices get more?

**Notes:** Natural entry point for **Adversarial Review** (agent interviews, then red-teams the result) and **Configurable HITL** (the interview itself sets the HITL level for execution).

## Examples

TODO: Add concrete examples from real usage.
