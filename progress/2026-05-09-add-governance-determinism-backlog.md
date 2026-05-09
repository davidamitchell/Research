# 2026-05-09 -- Add governance and LLM determinism backlog items

**Completed:**

- `Research/backlog/2026-05-09-data-governance-standards-ai-agentic-applicability.md` — from issue: How do ISO/IEC 38505, DAMA-DMBOK, NIST, GDPR, CCPA, and HIPAA apply to AI and agentic AI deployments? (priority: high)
- `Research/backlog/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md` — from issue: To what extent must governance policy application be deterministic vs allowing stochastic/probabilistic LLM elements? (priority: high)
- `Research/backlog/2026-05-09-llm-determinism-limits-temperature-zero.md` — from issue: What are the practical limits of LLM determinism even at temperature=0, fixed seeds, and constrained prompts? (priority: high)
- `Research/backlog/2026-05-09-hybrid-architecture-probabilistic-llm-deterministic-governance.md` — from issue: How should hybrid architectures separate probabilistic LLM interpretation from deterministic governance enforcement? (priority: high)
- `Research/backlog/2026-05-09-policy-as-code-guardrails-regulatory-ai-governance.md` — from issue: Which implementation patterns (Policy-as-Code, guardrails, output validation) best satisfy regulatory accountability requirements? (priority: high)
- `Research/backlog/2026-05-09-data-governance-frameworks-llm-nondeterminism-extension.md` — from issue: How can traditional data governance frameworks be extended to address LLM non-determinism and alignment uncertainty? (priority: medium)
- `Research/backlog/2026-05-09-compliance-risks-stochastic-llm-governance-decisions.md` — from issue: What evidence exists on compliance risks from relying on stochastic LLM outputs for governance/regulatory decisions? (priority: high)

**Research-question skill applied:** Five-test quality check (Specific, Answerable, Scoped, Motivated, Decomposable) run on each question. All 7 questions passed or were refined to pass. Acronyms expanded on first use in each file (ISO/IEC, DAMA-DMBOK, NIST, GDPR, CCPA, HIPAA, LLM, OPA, PaC, COBIT, EDPB, FCA, OCC, ICO, FINRA, EBA).

**Blocks relationships noted:**
- Q4 (hybrid architecture) blocks on Q3 (LLM determinism limits) — must understand actual determinism envelope before designing the boundary
- Q5 (policy patterns) and Q6 (framework extension) both block on Q1 (standards applicability) — need to know what is required before designing what implements it

**Cross-links set:** All items reference their thematically related siblings in the `related` field.

## Mini-Retro

1. **Did the process work?** Yes. The research-question skill framework (Specific, Answerable, Scoped, Motivated, Decomposable) applied cleanly to all 7 questions. The problem statement questions were well-formed; refinement was minor (adding scope boundaries, expanding acronyms).

2. **What slowed down or went wrong?** The skills submodule is not initialised in the cloud runner environment, so the `research-question` skill was applied by following the documented process from `.github/copilot-instructions.md` rather than reading `SKILL.md` directly. This is expected in this environment.

3. **What single change would prevent this next time?** Nothing to prevent — the fallback process worked correctly. The key pattern to remember: always expand acronyms on first use in each file, not just in the session log.

4. **Is this a pattern?** The acronym expansion requirement is a recurring pattern. Added a reminder in the Mini-Retro rather than raising a new issue — it is already documented as a known recurring failure in the instructions.

5. **Does any documentation need updating?** No changes required. The backlog items follow the template correctly.

6. **Do the default instructions need updating?** No new conventions emerged from this session.
