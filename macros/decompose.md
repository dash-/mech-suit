---
name: Decompose
shorthand: decompose
category: strategy
tags: []
summary: The agent splits a complex input or task along natural boundaries into independent, addressable parts that can be understood or acted on without reference to each other.
composes_with: [compose, delegate, isolate]
opposes: []
---

# Decompose (`decompose`)

When this macro is invoked, the agent splits a complex input or task along natural boundaries into independent, addressable parts. Each part can be understood, acted on, or delegated without reference to the others. The agent ensures loose coupling — changing one part must not require changing another.

## Decision Tree

- Split by responsibility, by data shape, or by lifecycle stage?
- Flat decomposition (all parts peer-level) or hierarchical (parts contain sub-parts)?

## Examples

TODO: Add concrete examples from real usage.
