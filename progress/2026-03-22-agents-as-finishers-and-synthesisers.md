# Session: New Research Item — Agents as finishers and synthesisers

**Date:** 2026-03-22
**Issue:** Agents as finishers and synthesisers
**Slug:** agents-as-finishers-and-synthesisers

## What was done

Created `Research/backlog/2026-03-22-agents-as-finishers-and-synthesisers.md` — a fully formed research backlog item addressing the question of how AI agents can be configured to complement a human whose strengths are ideation and pattern recognition but whose weaknesses are execution, finishing, and organisation.

## Conventions followed

- Copied structure from `Research/_template.md`
- File named `YYYY-MM-DD-short-slug.md` in `Research/backlog/`
- All frontmatter fields present; `status: backlog`, `started: ~`, `completed: ~`
- Acronyms expanded on first use: Large Language Model (LLM), Getting Things Done (GTD), IDEO (no expansion needed — proper name), Double Diamond (design framework proper name)
- Research Skill Output and Findings sections left blank for the research agent to fill
- Priority set to `high` — directly shapes how this repo's agent workflows and skills should evolve
- `output: [knowledge, backlog-item]` — expected to produce both a knowledge summary and concrete backlog items for repo configuration changes

## Research question framed

The item asks: *What agent configurations, prompt strategies, orchestration patterns, and tooling choices allow an AI agent (or agent team) to act as a reliable finisher and synthesiser — completing work that a human has started but not followed through on — and what are the practical limits of this complementary model?*

The approach decomposes this into five investigative steps:
1. Map cognitive frameworks (divergent vs. convergent thinking) to agent capability profiles
2. Survey agent roles and orchestration patterns from existing frameworks
3. Identify prompt and instruction patterns for task handoff and completion
4. Review failure modes and mitigations
5. Assess tooling fit given no-local-IDE constraint

## Next step

Run the research loop against this item when ready:
```bash
python -m src.main research start 2026-03-22-agents-as-finishers-and-synthesisers.md
```
Then trigger the research-loop workflow from the Actions tab.
