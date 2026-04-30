# 2026-04-30 -- Add backlog items: SE fundamentals and AI code generation (seven primary + one synthesis)

**Completed:**
- `Research/backlog/2026-04-30-grill-me-ai-alignment-shared-design.md` — added from issue #(research-questions-multiple); asks how effectively the "Grill Me" technique (iterative structured interviewing of the developer by the AI before any code is written) reduces misalignment between human intent and AI-generated output, and what measurable outcome differences exist compared to jumping directly to plan/code generation
- `Research/backlog/2026-04-30-ai-code-entropy-quality-metrics.md` — added from issue; asks whether repeated AI code generation without architectural guardrails demonstrably increases software entropy and complexity over time (as predicted by *The Pragmatic Programmer*), and what objective metrics (cyclomatic complexity, coupling, cognitive complexity, time-to-change, defect rate) best capture the difference between AI-assisted "vibe-coded" and architecturally-guarded codebases
- `Research/backlog/2026-04-30-deep-modules-ai-augmented-codebases.md` — added from issue; asks how much more effective AI is at understanding and correctly modifying codebases composed of deep modules with simple interfaces versus shallow module structures, and whether iterative architectural improvement ("Improve Codebase Architecture" skill) can rescue AI-generated "ball of mud" codebases
- `Research/backlog/2026-04-30-ubiquitous-language-ai-code-consistency.md` — added from issue; asks how significantly maintaining a living Ubiquitous Language (UL) (Domain-Driven Design (DDD)-style domain glossary) improves AI-generated code precision, reduces AI verbosity, and prevents naming drift across a growing codebase
- `Research/backlog/2026-04-30-tdd-feedback-loops-ai-augmented-dev.md` — added from issue; asks how Test-Driven Development (TDD) with AI changes output quality and stability compared to "write large chunks then test", and what the impact of fast feedback loops (typed languages, automated tests, browser tools) is on AI self-correction versus the "outrunning headlights" failure mode
- `Research/backlog/2026-04-30-strategic-tactical-division-ai-teams.md` — added from issue; asks what the optimal division of labour is between human (strategic design, interface definition, architectural oversight) and AI (tactical implementation) in AI-augmented teams, and whether Kent Beck's daily design investment advice produces compounding returns in this context
- `Research/backlog/2026-04-30-fundamentals-first-vs-specs-to-code.md` — added from issue; asks what empirical patterns emerge when comparing real-world projects built with strict fundamentals-first AI workflows versus pure specs-to-code or agent-only approaches, and which specific Software Engineering (SE) practices deliver the highest Return on Investment (ROI) in AI-augmented contexts
- `Research/backlog/2026-04-30-se-fundamentals-ai-code-synthesis.md` — synthesis item (`item_type: synthesis`); depends on all seven primary items completing first; will integrate findings into a coherent model, map relationships between practices, and produce practical recommendations and follow-up research directions

**Structural decisions:**
- Each primary item has `blocks: [2026-04-30-se-fundamentals-ai-code-synthesis]` — the synthesis cannot start until all seven primary items are completed
- The synthesis item has `cites: [all seven primary item slugs]` and `related: [same]`
- Seven items rather than twenty-plus individual sub-questions: the issue's 21 deep research questions naturally group into seven coherent themes, each scoped to a single researchable question; individual sub-questions are preserved in the `## Approach` section of each item
- Tags used: `agentic-coding` (canonical for AI-assisted development), `software-engineering`, `tdd`, `llm`, `agentic-ai`, `evaluation`, `technical-debt`, `organisational-design`, `synthesis`
- All sources include URLs; all acronyms expanded on first use

## Mini-Retro

1. **Did the process work?** Yes. The issue contained a well-structured set of 21 research sub-questions grouped into seven themes, plus an explicit request for a synthesis item. The natural grouping made it straightforward to produce seven scoped primary items and one synthesis item. The `blocks` / `cites` linking structure correctly represents the dependency: the synthesis waits for all seven primary items.

2. **What slowed down or went wrong?** One item (`2026-04-30-strategic-tactical-division-ai-teams.md`) had the Research Question heading duplicated by a copy error; corrected before commit. No other issues.

3. **What single change would prevent this next time?** Nothing structural to fix. For multi-question issues, the pattern of one-item-per-theme is reusable and produces well-scoped, individually researchable items. Document this in the instructions if multi-question issues become common.

4. **Is this a pattern?** The issue is the second large multi-question intake after the XAI/governance intake on the same date. If this becomes routine, consider adding a note to `.github/copilot-instructions.md` to guide grouping decisions (when to split by sub-question vs. by theme).
