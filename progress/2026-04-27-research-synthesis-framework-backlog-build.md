# 2026-04-27 — Research synthesis framework: backlog build

**Session branch:** `claude/research-synthesis-framework-NZwVX`

## Completed

- Discussion and analysis of academic journal practices for updating, cross-referencing, and tagging (how corrigenda, retractions, controlled vocabulary, systematic reviews, and citation graphs work)
- Survey of open-source autonomous research projects (GPT Researcher, STORM, Open Deep Research, smolagents, LangGraph, Knowledge Explorer, Letta) — key patterns identified for adoption
- Architecture decisions for the four goals (gap follow-up, synthesis, authoring, frameworks)
- Evaluated existing research backlog (14 items): strong overall, two issues found
  - `vendor-platform-governance-constraints-compensating-controls`: stale `blocks` reference to already-completed item → fixed (cleared to `[]`)
  - Agentic-ai-foundational-conditions synthesis item: all 5 prerequisites already in `completed/` — ready to pick now but may be delayed by PBAC cluster's non-empty `blocks` lists in picker sort
- Confirmed picker bug: `blocks` field only influences sort order, does not gate picking — items can be picked before their dependencies complete
- Added W-0038 through W-0050 to `BACKLOG.md` (13 new repo improvement items)
- Created `Research/backlog/2026-04-27-academic-post-publication-amendment-practices.md` (high priority, informs W-0038)

## New BACKLOG.md items summary

| Item | Purpose |
|---|---|
| W-0038 | Research immutability — amendment + rebuttal mechanism |
| W-0039 | Gap register — structured Open Questions extraction |
| W-0040 | Cross-reference frontmatter (cites, related) |
| W-0041 | Supersession field (superseded_by) |
| W-0042 | Item type field (primary-research / synthesis / paper / framework) |
| W-0043 | Tag co-occurrence review workflow (organic normalization, no predefined taxonomy) |
| W-0044 | Evidence confidence field |
| W-0045 | Synthesis workflow + Knowledge/ directory |
| W-0046 | Authoring workflow + Outputs/ directories |
| W-0047 | STORM-style multi-perspective questioning in research prompt |
| W-0048 | Memory MCP integration in research workflow |
| W-0049 | arXiv claim verification step in research prompt |
| W-0050 | Dependency enforcement in picker (depends_on field) |

## Key design decisions

- **Tags**: NOT a predefined taxonomy. Organic/emergent vocabulary with a post-hoc co-occurrence review that surfaces synonym candidates for human curation (W-0043)
- **Immutability**: Completed items are immutable with three narrow silent-edit exceptions (broken URLs, tag updates, citation URL fixes). All other changes via amendment items or supersession (W-0038)
- **Synthesis**: Separate workflow, separate directory (Knowledge/), separate item type — not conflated with primary research (W-0042, W-0045)
- **Dependency enforcement**: New `depends_on` field that actually gates picking, distinct from `blocks` which remains as priority signal (W-0050)
- **Memory MCP**: Already configured but unused — integrate into research workflow for cross-session accumulation (W-0048)

## Mini-Retro

1. **Did the process work?** Yes — the discussion → research → backlog sequence produced well-scoped items grounded in the actual state of the repo.
2. **What slowed down or went wrong?** Skills submodule not initialised (empty). Applied backlog-manager conventions from copilot-instructions.md directly.
3. **What single change would prevent this next time?** W-0036 (devcontainer setup) would ensure submodule is initialised automatically.
4. **Is this a pattern?** Yes — submodule initialisation is a recurring gap in cloud agent environments (see Known Recurring Patterns table).
5. **Does any documentation need updating?** No — all design decisions are captured in the new BACKLOG.md items themselves.
6. **Do the default instructions need updating?** The picker's `blocks` field semantics gap (W-0050) is now documented in BACKLOG.md. The copilot-instructions.md does not need updating until W-0050 is implemented.
