# Session: 2026-04-02 — anthropic-claude-code-leak

## Goal

Research and complete a new item addressing the March 31, 2026 accidental leak of Anthropic's Claude Code source code (GitHub issue: "Anthropic leak of Claude code"). The issue asked for analysis across eight dimensions: codebase architecture, problem-solving approaches, prompting strategy, feature-flagging, hidden features, product roadmap, practitioner prompting lessons, and any other insights.

## Work done

1. Explored the repository structure and confirmed the research workflow (CLI: `add` → `start` → `complete`).
2. Searched multiple credible secondary sources (Layer5, Superframeworks, VentureBeat, Wavespeed AI, DEV.to, Winbuzzer, MindStudio, Verdent AI, smol.ai AINews, DataNorth, BuildFastWithAI, ctol.digital, SFEIR Institute, Claude Code official docs, and more) to reconstruct the key findings from the leak.
3. Created `Research/backlog/2026-04-02-anthropic-claude-code-leak-architecture-prompting-and-hidden-features.md` via `python -m src.main research add`.
4. Moved to in-progress via `python -m src.main research start`.
5. Wrote the full research item with:
   - Metadata and tags
   - Research question covering all eight issue sub-questions
   - Scoped approach with eight investigation threads
   - 30 sourced references with URLs
   - Full Research Skill Output (§0 Initialise through §7 Recursive Review)
   - Findings section with Executive Summary, 12 Key Findings, Evidence Map, Assumptions, Analysis, Risks/Gaps, and Open Questions
6. Completed the item via `python -m src.main research complete`.

## Key findings summary

- Leak cause: missing `.npmignore` entry, not a security breach. No model weights or user data exposed.
- Architecture: modular permissioned TypeScript harness, 40-60 tools, five-level config cascade, seven-stage bootstrap.
- Memory: three-tier system (session compaction, pointer-index MEMORY.md, AutoDream async consolidation).
- Prompting: CLAUDE.md hierarchy acts as RAG-style persistent instruction layer (up to 40,000 chars); parallel tool invocation is explicitly unlocked by phrasing; conditional skill triggers.
- Feature flags: 44+ found; five major unreleased features: KAIROS (always-on daemon), BUDDY (virtual pet), Undercover Mode (AI-attribution stripping), UltraPlan (30-min planning), Voice/Bridge Mode.
- Roadmap: persistent, proactive, multi-agent platform; codenames Capybara, Fennec, Numbat.
- Anti-distillation traps (fake decoy tools in system prompts) and binary attestation were already in place.
- Ethical concern: Undercover Mode's automatic AI-attribution stripping for public repos was undisclosed to users.

## Files changed

- `Research/completed/2026-04-02-anthropic-claude-code-leak-architecture-prompting-and-hidden-features.md` (new)
- `progress/2026-04-02-anthropic-claude-code-leak.md` (this file)
