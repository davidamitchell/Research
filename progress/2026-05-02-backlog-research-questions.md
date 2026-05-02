# 2026-05-02 — Backlog research questions (issue: review-coding-backlog)

## Summary

Reviewed all open items in `BACKLOG.md` and created 9 research backlog items in `Research/backlog/` targeting the knowledge gaps that must be resolved before each open coding item can be implemented effectively.

### Open BACKLOG.md items reviewed

| W-item | Status | Action |
|---|---|---|
| W-0004 | open | devcontainer setup — implementation task, no knowledge gap; skip |
| W-0028 | open | strategy-author skill update — execution task against already-completed research; skip |
| W-0034 | open | **Research item created:** cross-item synthesis + knowledge map architecture |
| W-0035 | open | Research already completed: `Research/completed/2026-03-28-agent-instruction-loading-and-skills-access.md` |
| W-0036 | open | Research already completed: `Research/completed/2026-03-28-environment-setup-consistency.md` |
| W-0037 | open | Research already completed: `Research/completed/2026-03-28-environment-setup-consistency.md` |
| W-0038 | open | **Research item created:** STORM perspective discovery multi-perspective question generation |
| W-0039 | open | **Research item created:** adversarial review methods for AI research quality |
| W-0040 | open | **Research item created:** knowledge gap tracking and promotion patterns in PKM |
| W-0041 | open | **Research item created:** knowledge graph schema for cross-session research provenance (MCP memory) |
| W-0042 | open | **Research item created:** automated claim verification against academic literature (arXiv) |
| W-0048 | open | **Research item created:** research item versioning and amendment norms |
| W-0051 | open | **Research item created:** systematic review methodology for AI-assisted synthesis |
| W-0052 | open | **Research item created:** research-to-publication authoring workflow |
| W-0054 | open | dependency-aware picker — straightforward implementation; no knowledge gap requiring research |
| W-0055 | open | split BACKLOG.md to per-item files — engineering decision; no knowledge gap requiring research |
| W-0056 | open | citation display name migration — bulk implementation task; no knowledge gap requiring research |
| W-0057 | open | source display name normalisation — implementation task; no knowledge gap requiring research |

### Research items created

1. `Research/backlog/2026-05-02-cross-item-synthesis-knowledge-map-architecture.md` — for W-0034; priority: high
2. `Research/backlog/2026-05-02-storm-perspective-discovery-multi-perspective-question-generation.md` — for W-0038; priority: medium
3. `Research/backlog/2026-05-02-adversarial-review-methods-ai-research-quality.md` — for W-0039; priority: medium
4. `Research/backlog/2026-05-02-knowledge-gap-tracking-promotion-patterns-pkm.md` — for W-0040; priority: medium
5. `Research/backlog/2026-05-02-knowledge-graph-schema-cross-session-research-mcp.md` — for W-0041; priority: medium
6. `Research/backlog/2026-05-02-automated-claim-verification-academic-literature.md` — for W-0042; priority: medium
7. `Research/backlog/2026-05-02-research-item-versioning-amendment-norms.md` — for W-0048; priority: high
8. `Research/backlog/2026-05-02-systematic-review-methodology-ai-synthesis.md` — for W-0051; priority: high
9. `Research/backlog/2026-05-02-research-to-publication-authoring-workflow.md` — for W-0052; priority: medium (blocks: systematic-review-methodology-ai-synthesis)

### Checks run

- `make check` (ruff lint + format): passed ✅
- `python -m pytest tests/ -q`: 339 passed, 1 skipped, 1 pre-existing failure (TAVILY_API_KEY not set in sandbox — unrelated to changes) ✅

## Mini-Retro

1. **Did the process work?** Yes — reviewing the BACKLOG.md systematically and matching open items to knowledge gaps was the right approach. Items requiring execution (W-0028, W-0056, W-0057) were correctly excluded; items with completed research (W-0035, W-0036, W-0037) were noted.

2. **What slowed down or went wrong?** The BACKLOG.md file is large enough to require multiple view_range reads. The `research-question` skill is in the submodule (`.github/skills/`) which requires `git submodule update --init` to populate — not done in this session. Applied the skill manually following the instructions in `.github/copilot-instructions.md`.

3. **What single change would prevent this next time?** Nothing structural — the process followed the instructions correctly. The `research-question` skill application was done manually from the documented process.

4. **Is this a pattern?** No new pattern identified. The submodule dependency for skills is a known constraint.

5. **Does any documentation need updating?** No — the process followed the documented workflow for handling a new research request issue.

6. **Do the default instructions need updating?** No new conventions emerged from this session.
