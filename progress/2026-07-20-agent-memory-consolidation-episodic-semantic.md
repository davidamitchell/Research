# 2026-07-20 -- Complete research item: episodic-to-semantic memory consolidation

**Completed:**
- `Research/completed/2026-07-20-agent-memory-consolidation-episodic-semantic.md` -- researched and completed the item on episodic-to-semantic memory consolidation architectures for AI agents. Investigated MemGPT, Generative Agents, MemoryOS, A-MEM, sleep-time compute, Voyager, GitHub Copilot's production memory system, a 2026 agent-memory survey, and an Agent Drift paper, plus two cognitive-neuroscience sources on human memory consolidation and reconsolidation. Corrected two mislabeled source attributions in the seed list (verified via Crossref) and found a corrected arXiv ID for the MemoryOS paper.
- `learnings.md` -- added a paragraph to Thread 5 (Agent memory architecture mirrors organisational knowledge management) citing this item's findings on trigger-design trade-offs and the absence of confidence/uncertainty fields across all four surveyed architectures.

**Key findings:** GitHub Copilot's citation-anchored, just-in-time-verified consolidation is the only reviewed design tested against adversarial input and validated with production data; the trigger-design question (threshold-gated vs. scheduled vs. inline) resolves to a latency-versus-staleness trade-off with no evidence-backed winner; no architecture carries an explicit confidence field through consolidation; cognitive-neuroscience reconsolidation has no direct analogue in any surveyed agent architecture.

## Mini-Retro

1. **Did the process work?** Yes, end to end -- research, draft, two review passes, fixes, completion. The review cycle correctly caught real issues both times (unlabeled claims, full-sentence bold, single-source high-confidence, unexpanded BLEU-1, a banned word, and epistemic-label inconsistencies between leading markers and per-sentence trailing tags).

2. **What slowed down or went wrong?** The first review run's own commit-and-push step raced with a concurrent commit and failed to land (`error: failed to push some refs`), so `review_count` was never incremented even though the workflow logs showed a full FAIL verdict. This is the exact "commit race" pattern already documented in `.github/copilot-instructions.md`'s Known Recurring Failure Patterns table (last row), so no new pattern needed to be added -- but it did cost one wasted review cycle's worth of triage time confirming the pass didn't count before re-fixing and re-triggering.

3. **What single change would prevent this next time?** None needed for the commit-race pattern itself (it's already documented and the recovery procedure worked as written: check `git log` / frontmatter before counting the pass). One refinement worth capturing: leading `[fact]`/`[inference]` markers on a bullet must match the label on that bullet's *own first sentence*, not just be internally consistent with later sentences in the same bullet -- this was a distinct, newly observed failure mode (pass-2 violation) not yet in the recurring-patterns table.

4. **Is this a pattern?** Partially. The commit-race pattern is confirmed for a third-plus time (already tracked). The leading-marker-must-match-first-sentence-label issue is new; adding it below.

5. **Does any documentation need updating?** Yes -- added a new row to the Known Recurring Failure Patterns table in `.github/copilot-instructions.md` for the leading-vs-trailing epistemic label mismatch pattern.

6. **Do the default instructions need updating?** Same as above; the new table row captures the concrete rule (leading bullet marker must match the label bound to the bullet's own first sentence, not a later sentence in the same bullet).
