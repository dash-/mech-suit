---
name: Output Register
shorthand: output-register
category: pattern
tags: [communication]
summary: How the agent calibrates detail level, language complexity, and information density.
composes_with: [output-posture, persona-injection]
opposes: []
---

# Output Register (`output-register`)

**Tags:** `communication`

How the agent calibrates detail level, language complexity, and information density. Not about what to say — about how to say it. Like a musician adjusting volume and tempo to the room.

**Named registers:**
- **Brief** — short, direct, minimal. Lead with the answer. Skip reasoning unless asked. Good for experienced users, simple tasks, chat-style interaction.
- **Detailed** — thorough, includes reasoning and context. Good for complex decisions, unfamiliar domains, documentation-style output.
- **Simple** — plain language, short sentences, no jargon. Good for broad audiences, client-facing content, cross-functional communication.
- **Dense** — high conceptual density, assumes shared vocabulary, packs maximum information per sentence. Good for expert-to-expert communication, technical specs, internal notes.
- **Pedagogical** — explains concepts as it goes, builds understanding, uses examples and analogies. Good for teaching, onboarding, knowledge transfer.

**When to use:**
- Agent output goes to audiences with different expertise levels
- The same information needs different presentations (executive summary vs. technical deep-dive)
- User preference varies — some people want "just the answer," others want the full reasoning chain

**Tradeoffs:**
- **Pro:** Matching register to audience dramatically improves comprehension and trust
- **Pro:** Same agent can serve expert and novice users by shifting register
- **Con:** Wrong register wastes time (too detailed) or loses information (too brief)
- **Con:** Dense register can feel exclusionary; Simple register can feel condescending

**Key decisions:**
- Default register: Brief or Detailed? Depends on the primary audience.
- Audience detection: explicit configuration? inferred from the user's own language? task-based?
- Mixing: can an agent use Brief for the answer and Detailed for the appendix?

**Notes:** Pairs with **Persona Injection** (persona may imply a default register) and **Output Posture** (posture and register are independent axes — you can be Brief+Proactive or Detailed+Passive).

## Examples

TODO: Add concrete examples from real usage.
