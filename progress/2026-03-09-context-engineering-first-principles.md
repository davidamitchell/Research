# 2026-03-09 — Research Loop (context-engineering-first-principles)

**Completed:**

Research item:
- `Research/completed/2026-03-08-context-engineering-first-principles.md` — completed; context engineering operates through two empirically separable mechanisms (token-level steering of P(next_token|context) and goal-level steering of outcome achievement), with sycophancy as the prototypical failure of optimising the first while neglecting the second (56–62% rates in leading models); adjacent-field frameworks from information theory (entropy reduction), control theory (open-loop vs closed-loop), and cognitive linguistics (presupposition, framing, priming) provide first-principles insight; novel techniques include presupposition injection, negative constraint framing, entropy-weighted example selection, tool schema as implicit instruction, and progressive context disclosure.

Sources consulted:
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (Anthropic primary source: definition, attention budget, context modalities, tool schema, progressive disclosure, compaction)
- https://www.anthropic.com/research/reward-tampering (Anthropic sycophancy-to-subterfuge: two-mechanism failure empirics, arXiv:2406.10162)
- https://research.trychroma.com/context-rot (Chroma context rot empirical evidence: model recall degrades with context length across all tested models)
- https://aclanthology.org/2024.findings-acl.877.pdf (ACL 2024: structural priming in LLMs, human-like effects confirmed)
- https://arxiv.org/html/2502.17091 (WildFrame 2025: framing effects in LLMs comparable to humans)
- https://arxiv.org/abs/2402.01817 (Kambhampati et al.: LLMs can't plan — token fluency does not imply goal-level validity)
