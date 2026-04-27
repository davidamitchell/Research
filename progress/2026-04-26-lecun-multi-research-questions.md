# 2026-04-26 — Add backlog items: LeCun LLM critique multi-research-questions series

**Completed:**
- `Research/backlog/2026-04-26-lecun-llm-critique-primary-sources.md` — added from issue "Multi research questions" (Q1); asks what LeCun's complete argument against LLMs as a path to autonomous machine intelligence is, drawing exclusively on primary sources
- `Research/backlog/2026-04-26-llm-verifiability-asymmetry-code-world-action.md` — added from issue "Multi research questions" (Q2); asks what the precise technical distinction between code generation and other LLM outputs is in terms of external verifiability, and what this asymmetry implies for safe deployment in a regulated financial institution
- `Research/backlog/2026-04-26-lecun-critique-citizen-development-enterprise-risk.md` — added from issue "Multi research questions" (Q3); asks what synthesising LeCun's architectural critique with systems capability debt and citizen development arguments produces as a unified risk framework for regulated financial institutions
- `Research/backlog/2026-04-26-software-engineering-investment-case-llm.md` — added from issue "Multi research questions" (Q4); asks for the strongest evidence-based argument that engineering capability investment rather than citizen development tooling investment is both the correct response to systems capability debt and the correct way to capture genuine LLM value

Dependency ordering applied:
- Q1 (`lecun-llm-critique-primary-sources`) blocks Q3 and Q4
- Q2 (`llm-verifiability-asymmetry-code-world-action`) blocks Q3 and Q4
- Q3 (`lecun-critique-citizen-development-enterprise-risk`) blocks Q4

## Mini-Retro

1. **Did the process work?** Yes — the four questions in the issue decomposed cleanly into four backlog items with a clear dependency chain. The research-question skill protocol (Specific, Answerable, Scoped, Motivated, Decomposable) was applied to each. All four items are specific, answerable from primary sources, scoped with explicit in/out-of-scope constraints, motivated by the regulated financial services context, and decomposed into structured investigation sub-questions.

2. **What slowed down or went wrong?** The issue's Q3 and Q4 reference "the systems capability debt and citizen development argument already in this corpus" without identifying which specific backlog items that refers to. The backlog items created here include a note to identify those specific slugs during the research phase, as the cross-references cannot be resolved without inspecting the corpus at research time.

3. **What single change would prevent this next time?** Nothing structural — the issue format was clear and the template pattern is well-established. The only gap is the unresolvable cross-reference at backlog creation time; this is inherent to forward references and is already handled by the "identify during research" instruction in the Approach sections.

4. **Is this a pattern?** The forward-reference gap (Q3/Q4 reference corpus items not yet identified) is a known pattern for issues that assume prior corpus knowledge. The mitigation (defer cross-reference resolution to research time) is established and applied here.

5. **Does any documentation need updating?** No changes to instructions or conventions needed — this session followed the documented backlog creation process without needing to deviate.

6. **Do the default instructions need updating?** No.
