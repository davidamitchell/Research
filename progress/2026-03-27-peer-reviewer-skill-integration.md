# 2026-03-27 -- Peer Reviewer Skill Integration

**Completed:**

Changed files:
- `research-review-prompt.md` -- updated from three-skill to four-skill review; added Step 4 (`peer-reviewer`) and updated output format to include nested `peer-reviewer` sub-checks (`logical-coherence-and-evidence-sufficiency`, `alternative-explanations`, `cross-item-integration`); added reference to `research-reviewer/SKILL.md` as the orchestration skill
- `.github/workflows/research-review.yml` -- updated comment header to list all four skills; updated auto-pass cap report to include `peer-reviewer: PASS` and its three sub-checks
- `research-prompt.md` -- updated Step 4 companion skill check count from "three" to "four" to match `.github/skills/research/SKILL.md §8` which already defines §8.4 Peer-review pre-output check

## Mini-Retro

1. **Did the process work?** Yes. The skills submodule contains `peer-reviewer/SKILL.md`, `research-reviewer/SKILL.md`, and `feedback/SKILL.md` -- all available for use. The existing `research-reviewer/SKILL.md` already serves as the orchestration layer applying all four checks in sequence, and the `research/SKILL.md §8` already includes §8.4 peer-review. The only gap was that the review prompt and workflow had not been updated to use them.
2. **What slowed down or went wrong?** Nothing significant. The submodule content clarified the design immediately.
3. **What single change would prevent this next time?** Keep the skill orchestration description in `research-reviewer/SKILL.md` as the single source of truth, and reference it from the prompt rather than re-implementing the steps inline.
4. **Is this a pattern?** Yes. The skills submodule is ahead of the prompts and workflows that consume it. When skills are updated, the consuming prompts need a corresponding update.
