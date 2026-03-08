# Deduplication Report

Total macros: 97
Candidate pairs to review: 20

Scoring: combined = name_similarity * 0.4 + word_overlap * 0.6
Higher score = more likely to overlap

---

## reversible ([principle, modifier]) vs transparent ([principle, modifier])
Score: 0.26 (name: 0.00, content: 0.26)

**reversible:** The agent identifies every point of no return and captures sufficient state before acting to enable rollback, biasing execution order toward safety.

**transparent:** The agent identifies black boxes and externalizes its reasoning process, intermediate states, and decision points to enable auditability and reconstru

Shared key words: agent, applied, context, current, every, identifies, invoked, macro, modifier, point, proposes, state, without

---

## scoped-promotion (pattern) vs scoped (modifier) **CROSS-CATEGORY**
Score: 0.25 (name: 0.50, content: 0.08)

**scoped-promotion:** Learnings, patterns, and behaviors start scoped to a specific context (project, client, industry, engagement).

**scoped:** The agent establishes an explicit boundary before acting and constrains all subsequent reasoning to that boundary, actively rejecting drift beyond sco

Shared key words: boundary, scope, scoped

---

## agent-workspace (pattern) vs workspace-isolation (pattern)
Score: 0.23 (name: 0.33, content: 0.16)

**agent-workspace:** **Permission Warm-up** → **Workspace Isolation** → **Session Forking** → **Multi-Source Context Assembly**

**workspace-isolation:** Create isolated execution environments per task — separate file trees, branches, configs, or runtime contexts.

Shared key words: codebase, context, create, forking, isolated, multiple, parallel, session, tasks

---

## least-priv (principle) vs least-surprise (principle)
Score: 0.20 (name: 0.33, content: 0.12)

**least-priv:** Audit every permission grant, scope, and capability in the current context and propose the minimum viable permission for each.

**least-surprise:** Audit naming, return values, defaults, and side effects for anything that would confuse a person or system encountering them for the first time withou

Shared key words: agent, audits, flags, invoked, macro

---

## output-posture (pattern) vs output-register (pattern)
Score: 0.18 (name: 0.33, content: 0.08)

**output-posture:** How assertive and proactive the agent is in its communication.

**output-register:** How the agent calibrates detail level, language complexity, and information density.

Shared key words: agent, answer, asked, context

---

## planning-pipeline (pattern) vs research-pipeline (pattern)
Score: 0.18 (name: 0.33, content: 0.08)

**planning-pipeline:** **Orchestrator-Subagent** → **Adversarial Review** → **Debate & Consensus** → **Ethics Gating** → **Configurable HITL**

**research-pipeline:** **Structured Reasoning** → **Retrieval Subagent** → **Verification Loop** → **Progressive Refinement**

Shared key words: budget, multiple, subagent

---

## permission-warmup (pattern) vs warmup-calibration (pattern)
Score: 0.17 (name: 0.33, content: 0.07)

**permission-warmup:** Before starting real work, identify every distinct permission category the plan requires and trigger each one with a small, harmless, *relevant* opera

**warmup-calibration:** Before the system goes live, run it against known historical cases to verify it produces reasonable outputs.

Shared key words: agent, before, identify, prompts

---

## context-assembly (pattern) vs context-windowing (pattern)
Score: 0.17 (name: 0.33, content: 0.06)

**context-assembly:** Gather context from multiple heterogeneous sources in parallel, then synthesize into a unified brief before work begins.

**context-windowing:** The general principle of deliberately curating what information an agent sees.

Shared key words: agent, context, different

---

## memory-retrieval (pattern) vs retrieval-subagent (pattern)
Score: 0.17 (name: 0.33, content: 0.05)

**memory-retrieval:** Agents query a knowledge base to inform decisions.

**retrieval-subagent:** One step beyond **TOC Index**.

Shared key words: agent, context, receives, retrieval

---

## addressable-output (pattern) vs output-register (pattern)
Score: 0.17 (name: 0.33, content: 0.05)

**addressable-output:** Structure agent output so every item is uniquely referenceable.

**output-register:** How the agent calibrates detail level, language complexity, and information density.

Shared key words: agent, decisions, level, output

---

## agent-discovery (pattern) vs agent-workspace (pattern)
Score: 0.16 (name: 0.33, content: 0.05)

**agent-discovery:** 'Enable agents to discover each other''s capabilities at runtime rather than hardcoding agent references.'

**agent-workspace:** **Permission Warm-up** → **Workspace Isolation** → **Session Forking** → **Multi-Source Context Assembly**

Shared key words: agent, other

---

## discovery-loop (pattern) vs learning-loop (pattern)
Score: 0.16 (name: 0.33, content: 0.04)

**discovery-loop:** **Bayesian Steering** → **Escalation Ladder** → **Memory & Retrieval** → **Verification Loop**

**learning-loop:** **Background Observation** → **Memory & Retrieval** → **Scoped Promotion** → **Decision Calibration**

Shared key words: memory, retrieval, should

---

## orchestrator-subagent (pattern) vs retrieval-subagent (pattern)
Score: 0.16 (name: 0.33, content: 0.04)

**orchestrator-subagent:** A single orchestrator agent holds the overall goal and state.

**retrieval-subagent:** One step beyond **TOC Index**.

Shared key words: agent

---

## discovery-loop (pattern) vs verification-loop (pattern)
Score: 0.15 (name: 0.33, content: 0.04)

**discovery-loop:** **Bayesian Steering** → **Escalation Ladder** → **Memory & Retrieval** → **Verification Loop**

**verification-loop:** After output is produced, a separate verifier checks against defined criteria.

Shared key words: verification

---

## decision-calibration (pattern) vs warmup-calibration (pattern)
Score: 0.15 (name: 0.33, content: 0.03)

**decision-calibration:** At the time of making a decision, record the decision, the reasoning, the predicted outcome, and a mandatory future review date.

**warmup-calibration:** Before the system goes live, run it against known historical cases to verify it produces reasonable outputs.

Shared key words: compare

---

## agent-versioning (pattern) vs agent-workspace (pattern)
Score: 0.15 (name: 0.33, content: 0.03)

**agent-versioning:** Manage the lifecycle of agent configurations (prompts, tools, parameters) as versioned artifacts.

**agent-workspace:** **Permission Warm-up** → **Workspace Isolation** → **Session Forking** → **Multi-Source Context Assembly**

Shared key words: agent, tasks

---

## agent-discovery (pattern) vs agent-versioning (pattern)
Score: 0.15 (name: 0.33, content: 0.02)

**agent-discovery:** 'Enable agents to discover each other''s capabilities at runtime rather than hardcoding agent references.'

**agent-versioning:** Manage the lifecycle of agent configurations (prompts, tools, parameters) as versioned artifacts.

Shared key words: agent

---

## addressable-output (pattern) vs output-posture (pattern)
Score: 0.15 (name: 0.33, content: 0.02)

**addressable-output:** Structure agent output so every item is uniquely referenceable.

**output-posture:** How assertive and proactive the agent is in its communication.

Shared key words: agent

---

## agent-discovery (pattern) vs discovery-loop (pattern)
Score: 0.15 (name: 0.33, content: 0.02)

**agent-discovery:** 'Enable agents to discover each other''s capabilities at runtime rather than hardcoding agent references.'

**discovery-loop:** **Bayesian Steering** → **Escalation Ladder** → **Memory & Retrieval** → **Verification Loop**


---

## learning-loop (pattern) vs verification-loop (pattern)
Score: 0.14 (name: 0.33, content: 0.01)

**learning-loop:** **Background Observation** → **Memory & Retrieval** → **Scoped Promotion** → **Decision Calibration**

**verification-loop:** After output is produced, a separate verifier checks against defined criteria.


---

