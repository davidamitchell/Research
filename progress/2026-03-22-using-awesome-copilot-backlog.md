# Session: Backlog item — Using awesome-copilot across repos

**Date:** 2026-03-22
**Slug:** using-awesome-copilot-backlog
**Issue:** How to use awesome-copilot (https://github.com/davidamitchell/awesome-copilot) in this repo and in Personal-Assistant-, Latest-developments-, Memory-System, and Agent-Evaluation

## What was done

- Created research backlog item `Research/backlog/2026-03-22-using-awesome-copilot-across-repos.md`
- The item captures the research question, scope, approach, and starting sources for investigating how to apply GitHub Copilot (GHC) resources from `awesome-copilot` across the five target repos
- Priority set to `high` because it has immediate practical value across multiple active repos

## Conventions followed

- Copied structure from `Research/_template.md`
- File named `YYYY-MM-DD-short-slug.md` in `Research/backlog/`
- All frontmatter fields present; `status: backlog`, `started: ~`, `completed: ~`
- Research Skill Output and Findings sections left blank for the research agent to fill
- Acronyms expanded on first use: GitHub Copilot (GHC)
- `output: [knowledge, backlog-item]` — expected to produce both a knowledge summary and concrete adoption backlog items for each target repo

## Next step

Run the research loop against this item when ready:
```bash
python -m src.main research start 2026-03-22-using-awesome-copilot-across-repos.md
```
Then trigger the research-loop workflow.
