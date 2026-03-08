---
name: Tool-Native Communication
shorthand: tool-native-communication
category: pattern
tags: [communication]
summary: Agents output directly into the systems humans already use — ticketing (Linear), PRs (GitHub), chat (Slack), docs (Notion) — rather than creating parallel artifacts that require manual integration.
composes_with: []
opposes: []
---

# Tool-Native Communication (`tool-native-communication`)

**Tags:** `communication`

Agents output directly into the systems humans already use — ticketing (Linear), PRs (GitHub), chat (Slack), docs (Notion) — rather than creating parallel artifacts that require manual integration.

**The principle:** If an agent writes a plan to a markdown file that a human then copy-pastes into Linear, that's a manual integration step that defeats the purpose of automation.

**When to use:**
- The team already has established tools for tracking work, communication, and documentation
- Agent outputs need to be visible, commentable, and trackable by humans
- You want agents to participate in existing workflows, not create parallel ones

**Examples:**
- Write research plans directly to Linear tickets, not markdown files
- Add review comments directly on PRs, not in separate text files
- Post status updates to Slack channels, not log files
- Update Notion docs directly, not generate replacement text

**Tradeoffs:**
- **Pro:** Output is immediately visible in existing workflows — zero "last mile" friction
- **Pro:** Output is commentable, trackable, and integrated with existing processes
- **Pro:** Agents become participants in the team's process, not external tools
- **Con:** Each tool has its own formatting conventions, API quirks, and permission models
- **Con:** Tool outages or API changes can break agent output channels
- **Con:** Agents may produce output that doesn't match the team's conventions for that tool

**Key decisions:**
- Which tools to integrate with? (Start with the ones the team actually uses daily)
- Permission model: what can agents create vs. update vs. comment on?
- Formatting: agents must understand each tool's conventions (Linear markdown vs. GitHub markdown vs. Slack blocks)

## Examples

TODO: Add concrete examples from real usage.
