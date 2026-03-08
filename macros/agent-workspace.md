---
name: Agent Workspace
shorthand: agent-workspace
category: pattern
tags: [setup]
summary: **Permission Warm-up** → **Workspace Isolation** → **Session Forking** → **Multi-Source Context Assembly**
composes_with: []
opposes: []
---

# Agent Workspace (`agent-workspace`)

**Tags:** `setup`

**Permission Warm-up** → **Workspace Isolation** → **Session Forking** → **Multi-Source Context Assembly**

Frontload permissions, create an isolated environment, fork a context-rich session, assemble context from all relevant sources, then start working.

**When to use:**
- Agent needs to operate on a codebase or project with multiple context sources
- Parallel tasks must not contaminate each other
- The environment has permission gates that could block mid-task

## Examples

TODO: Add concrete examples from real usage.
