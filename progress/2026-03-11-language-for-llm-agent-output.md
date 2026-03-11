# 2026-03-11 — Research Loop (language-for-llm-agent-output)

**Completed:**

Research item:
- `Research/completed/2026-03-10-language-for-llm-agent-output.md` — completed; no programming language designed specifically for LLM agents to produce as primary output (as distinct from existing languages constrained at generation time) has been identified in 2022–2025 literature; the structured generation field has reached production maturity at specification hierarchy level 2 (Outlines, Guidance) and research frontier at level 3 (ETH Zurich PLDI 2025 type-constrained TypeScript decoding); all current approaches address only Layer 1 structural failures, with Layers 2–5 of the failure mode taxonomy entirely unaddressed by output grammar or language design.

Sources consulted:
- https://arxiv.org/abs/2504.09246 (ETH Zurich PLDI 2025: type-constrained code generation for TypeScript — prefix automata enforcing type safety at decoding time)
- https://github.com/dottxt-ai/outlines (Outlines by dottxt-ai — FSM-based schema/grammar enforcement at token level; ~13,500 GitHub stars, $11.9M funding, production-grade)
- https://arxiv.org/abs/2212.06094 (LMQL: "Prompting Is Programming" — Beurer-Kellner et al., PLDI 2023; academic progenitor of constrained LLM generation field)
