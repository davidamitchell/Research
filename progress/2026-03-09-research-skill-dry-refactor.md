# 2026-03-09 — Research Skill DRY Refactor

**Completed:**

Skill and prompt consolidation:
- `.github/skills/research/SKILL.md` bumped to v1.1; absorbed all operational rules that were split across the skill and `research-prompt.md`:
  - §0: Prior Work Check (search completed items before starting)
  - §2: Source Marking Discipline ([x]/[ ] protocol, inaccessible source handling)
  - §6: Output Quality Requirements (no placeholder headings, executive summary must state the finding)
  - §8: replaced with explicit three-part checklist — §8.1 citation-discipline, §8.2 speculation-control, §8.3 remove-ai-slop — each listing every check by name
- `research-prompt.md` DRY refactored: collapsed source-marking, output-quality, prior-work-check, and companion-skill steps into references to the skill; removed redundant Step 8 self-review; renumbered steps 9–11 to 8–10
