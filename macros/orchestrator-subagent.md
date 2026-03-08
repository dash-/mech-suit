---
name: Orchestrator-Subagent
shorthand: orchestrator-subagent
category: pattern
tags: [coordination]
summary: A single orchestrator agent holds the overall goal and state.
composes_with: []
opposes: []
---

# Orchestrator-Subagent (`orchestrator-subagent`)

**Tags:** `coordination`

A single orchestrator agent holds the overall goal and state. It delegates specific tasks to specialized subagents, collects their outputs, and decides what to do next. Subagents have no awareness of each other or the broader plan — they receive a task and return a result.

**When to use:**
- The overall task requires coordination across multiple capabilities
- You need a single point of control for state, budget, and decision-making
- Subtasks are relatively independent and can be specified clearly

**Tradeoffs:**
- **Pro:** Clear accountability. The orchestrator owns the outcome.
- **Pro:** Subagents can be simple and focused — easier to build, test, and swap.
- **Con:** Single point of failure. If the orchestrator makes a bad decision, subagents can't correct it.
- **Con:** The orchestrator needs enough context to delegate well, which can be a bottleneck.

**Variants:**
- **Flat** — orchestrator talks to all subagents directly
- **Hierarchical** — orchestrators delegate to sub-orchestrators (fractal)
- **Dynamic** — orchestrator decides at runtime which subagents to invoke


**Communication topologies:**
- **Flat (Supervisor)** — Orchestrator talks to all subagents directly. Simple but doesn't scale
- **Hierarchical** — Orchestrators delegate to sub-orchestrators, each overseeing a tier below. Enables structured scalability for large systems
- **Network (Peer-to-Peer)** — Agents communicate directly with each other without a central coordinator. Resilient but hard to maintain coherent decision-making
- **Agent-as-Tool** — A subagent is wrapped as a callable tool, making invocation look like a function call. Reduces autonomy but simplifies integration and makes the agent composable with any tool-using system

## Examples

TODO: Add concrete examples from real usage.
