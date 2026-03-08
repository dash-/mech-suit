---
name: Anti-pattern
type: category
---

# Anti-pattern

**Role:** Known failure modes — the "watch out" layer.

**Form:** Cautionary descriptions. Anti-patterns are cross-cutting — they can manifest at any category level.

**Distinguishing trait:** Anti-patterns describe what goes wrong and why. They aren't instructions — they're warnings that help agents and humans recognize when they're heading toward a known failure mode.

**Examples:** `kitchen-sink`, `rubber-stamp`, `echo-chamber`, `expensive-default`, `infinite-loop`

**Relationship to other categories:** Anti-patterns often emerge from misapplied macros. The `kitchen-sink` is what happens when `compose` runs without `minimal`. The `rubber-stamp` is `verify` without teeth. Recognizing anti-patterns helps calibrate macro usage.
