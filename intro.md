# The Macro Library

A mech suit for building things with agents.

## What This Is

A library of named, precise, reusable concepts — **macros** — that any agent (human or AI) can invoke, compose, and rely on for predictable behavior. Each macro expands into specific agent behavior that is the same every time, across any context.

## The Problem It Solves

When you tell an agent "make this incremental," the result depends on the agent's interpretation. Two agents will do two different things. Repeated instructions drift. This is the genie problem: you asked for what you wanted but got what you said.

Macros raise the floor of interpretation quality. Instead of vague instructions that each agent interprets differently, you invoke a named concept with a precise expansion. The agent restates the expansion applied to your specific context. You confirm or adjust. Then execution happens.

## How to Use It

1. **Invoke** with the `/with` command: `/with collapse, non-destructive`
2. The agent **expands** each macro and synthesizes them in context
3. The agent **restates** the combined behavior: "Here's what I'll do: resolve all references into a flat artifact, but preserve the compositional source alongside it. Does that match your intent?"
4. You **confirm or adjust** — this is contract negotiation, not deployment
5. Execution happens

Macros compose freely. Tensions between macros (e.g., `/with lazy, fail-fast`) are surfaced explicitly for resolution rather than silently resolved by the agent.

## Who It's For

- **Humans** instructing agents — precise shorthand for complex behavior
- **Agents** delegating to subagents — compressed instructions that decompress losslessly via catalog lookup
- **Skill authors** designing new capabilities — composable building blocks with known behaviors
