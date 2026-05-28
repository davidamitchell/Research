# 2026-05-28 -- Complete: jepa-video-outcome-prediction-physical-action-problem-class

**Completed:**
- `Research/completed/2026-05-25-jepa-video-outcome-prediction-physical-action-problem-class.md` — completed from backlog; answers whether the text→JEPA and JEPA→action transitions are the same problem class: they are not. Text→JEPA is within-class (passive prediction); JEPA→action crosses the prediction/control boundary per Sutton and Barto's reinforcement learning framework and is confirmed empirically by V-JEPA 2's two-stage architecture.
- `learnings.md` — added Thread 23 on the prediction/control structural boundary for physical AI.

**Key findings:**
- The shift from text to video JEPA is a within-class transition (both passive, observational).
- The shift from JEPA video prediction to physical action crosses the prediction/control boundary.
- V-JEPA 2 (2025) required a separate Stage 2 with 62 hours of robot-trajectory data after Stage 1 video pre-training — empirical evidence of the structural boundary.
- Cognitive science (Free Energy Principle, predictive processing) independently supports the distinction.

**Sources used:**
- LeCun (2022) OpenReview (primary)
- Assran et al. (2023) I-JEPA arXiv:2301.08243 (primary)
- Assran et al. (2025) V-JEPA 2 arXiv:2506.09985 (primary)
- Hafner et al. (2023) DreamerV3 arXiv:2301.04104 (primary)
- Sutton and Barto (2018) RL textbook (primary)
- Friston (2010) Free Energy Principle Nature Reviews Neuroscience (primary)
- Clark (2013) Predictive Brains BBS (primary)
- Christiano et al. (2017) RLHF arXiv:1706.03741 (primary)

**Review history:**
- Pass 1/2: FAIL — 3 citation-discipline violations (FAIR acronym, Friston/Clark URLs, RLHF citation) + 2 peer-reviewer violations (KF2/KF3 high confidence with single sources)
- Pass 2/2: FAIL — 1 remaining violation (FAIR expanded in code block, not narrative prose). Review cap reached; no issue raised.
- Fixed all violations before completing; item completed post-cap with corrected content.

---

## Mini-Retro

1. **Did the process work?** Mostly yes. The research skill output was structurally sound; the main failure points were citation formatting precision (acronym expansion scope — code blocks do not satisfy the requirement) and confidence calibration (HIGH requires multiple independent sources or widely-accepted theory, not a single paper or textbook citation alone). The two-review cycle is the right safety check.

2. **What slowed down or went wrong?** Three distinct rounds of violations:
   - Round 1: Fully bolded Key Findings (`**Claim text.**`) — wrong format; fixed before first review trigger.
   - Review 1: FAIR acronym, Friston/Clark URLs, RLHF wrong citation source, KF2/KF3 HIGH with single sources.
   - Review 2: FAIR expanded inside code block — not counted as narrative expansion. This is subtle and easy to miss.

3. **What single change would prevent this next time?** Before triggering review, run a targeted grep: `grep -n "\\b[A-Z]{2,}\\b"` over all narrative prose sections (§2–§6, Findings) and confirm every acronym initialism has its expansion in prose (not in code blocks, YAML, or metadata fences). Code-block expansions are invisible to the citation-discipline check.

4. **Is this a pattern?** The acronym-in-code-block issue is a new variant of the known "acronym not expanded on first use" pattern. The original pattern covers forgetting to expand at all; this variant covers expanding only inside a fenced metadata block. This should be added to the Known Recurring Patterns table.

5. **Does any documentation need updating?** The Known Recurring Patterns table in `.github/copilot-instructions.md` should be updated with the code-block expansion variant. The research-prompt.md acronym audit step should explicitly call out: "Code-block expansions do not count; acronym must be expanded on first narrative prose use."

6. **Do the default instructions need updating?** Yes — the acronym audit instruction should explicitly state that expansions inside fenced code blocks, YAML frontmatter, or metadata fragments do not satisfy the first-use requirement. The first narrative prose occurrence is what the citation-discipline check audits.
