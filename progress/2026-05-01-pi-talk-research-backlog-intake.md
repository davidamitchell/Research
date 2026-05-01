# 2026-05-01 -- Extract research questions from Pi coding agent talk

**Completed:**

Added 8 primary backlog items and 1 synthesis backlog item extracted from a 2026 developer conference talk by Mario (creator of the Pi coding agent harness). The talk covered three thematic arcs: harness design, OSS ecosystem health under AI-generated contributions, and development discipline for working sustainably with AI coding agents.

Primary backlog items added:

- `Research/backlog/2026-05-01-terminal-bench-minimal-coding-agent-benchmarks.md` — what TerminalBench (minimal tmux+keystroke harness outperforming native harnesses) reveals about coding agent toolset design
- `Research/backlog/2026-05-01-coding-agent-context-management-transparency.md` — best practices for transparent, user-controlled context management in LLM coding agent harnesses
- `Research/backlog/2026-05-01-self-modifying-agent-architectures.md` — design tradeoffs of self-modifying/malleable agent architectures vs. fixed-architecture agents (Pi vs. Claude Code/aider)
- `Research/backlog/2026-05-01-extension-systems-ai-coding-agents.md` — design patterns for extension/plugin systems in AI coding agent harnesses; hot-reload; safety; developer experience
- `Research/backlog/2026-05-01-oss-sustainability-ai-generated-contributions.md` — strategies for OSS maintainers dealing with AI-generated low-quality contributions ("clankers"); vouch pattern, embedding triage, OSS vacation
- `Research/backlog/2026-05-01-compound-error-accumulation-ai-codebases.md` — how errors compound in AI-agent-heavy codebases without human bottlenecks; local patch / global regression; AI-generated test reliability
- `Research/backlog/2026-05-01-appropriate-task-selection-coding-agents.md` — empirical criteria for tasks where coding agents reliably add value vs. introduce systemic risk; bounded scope, evaluability, modularity
- `Research/backlog/2026-05-01-human-oversight-ai-software-development.md` — evidence for human oversight / bottleneck as a quality gate in AI-assisted development; Fagan, Bacchelli & Bird, throughput limits

Synthesis backlog item added:

- `Research/backlog/2026-05-01-sustainable-ai-software-development-synthesis.md` — capstone synthesis across all 8 primary items; blocked on all 8 completing; produces unified principles and governance practices for sustainable AI-assisted software development

## Mini-Retro

1. **Did the process work?** Yes. The talk was dense with practitioner observations spanning harness design, ecosystem health, and development discipline. Decomposing it into 8 distinct primary questions and one synthesis produced well-scoped items that each have a single answerable question with clear scope boundaries.

2. **What slowed down or went wrong?** The talk transcript contained no formal citations — all sources in the backlog items are starting points inferred from topic area, not references from the talk itself. This means every backlog item will need independent source discovery during the research phase.

3. **What single change would prevent this next time?** When a research intake comes from a talk or video, note explicitly in the Context section that sources must be independently discovered (no bibliography). This is already implied by the template but worth flagging per-item to set expectations for the research agent.

4. **Is this a pattern?** Partly. The "no formal citations in talk transcript" situation is common for conference talks. The existing template handles this fine — Sources section starts empty or with inferred starting points, which is correct.

5. **Does any documentation need updating?** No — the existing research intake process and template handle this case. The per-item Context notes are sufficient guidance.

6. **Do the default instructions need updating?** No structural change required. The existing process for handling new research request issues covers this case.
