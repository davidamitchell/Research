# 2026-06-10 -- Research and complete: AI productivity, quality, and governance open questions

---

## Research completion session

**Completed:**
- `Research/completed/2026-06-10-ai-productivity-quality-governance-open-questions.md` — full research item completed on 2026-06-10T11:43:14+00:00; empirical evidence distinguishing sustainable AI-enabled delivery gains from short-lived throughput effects and hidden quality/governance costs over a 12-to-24-month horizon.

**Key findings:**
- DORA 2024: 7.2% stability decrease and 1.5% throughput decrease per 25% AI adoption increase; rework rate added as fifth delivery metric
- GitClear 2025: 211M lines; code churn +84%, copy-paste +48%, refactoring -60%, maintenance cost +30-41%
- METR 2025 RCT: 16 experienced open-source developers; 19% slower with frontier AI tools
- Faros AI 2025: 10,000 developers, 1,255 teams; pull request review time +91%, PR size +154%, org velocity flat
- Agarwal et al. 2026: autonomous agents +18% warnings and +39% complexity vs IDE suggestion baseline

**Review passes:**
- Pass 1 (run 27272256847): FAILED — 9 citation-discipline violations, 3 speculation-control, 2 remove-ai-slop
- Pass 2 (run 27272942332): FAILED then auto-passed (review_count=2); remaining violations fixed before completing

**Violations fixed in pass 2:** 15 Q-section header em dashes, 3 Findings Output em dashes, KF3/KF5/KF6/KF7 [fact]→[inference] for interpretive clauses, unlabeled Analysis sentences in §6 and Findings, causal clause separated in §2 Q1a, selection-bias alternative explanation added to Risks/Gaps

## Research completion Mini-Retro

1. **Did the process work?** Mostly. The evidence discipline was applied correctly throughout and both review passes identified real violations rather than false positives.

2. **What slowed down or went wrong?**
   - Em dashes in Q-section headers (Q1a — Label format) slipped through §7 self-audit in both passes.
   - [fact] labels on interpretive Key Finding clauses — where the source proves the data but the framing ("primary mechanism", "primary hidden cost") is an inference drawn from the data.
   - Multi-sentence Analysis paragraphs where only the final sentence got a trailing label.
   - Selection-bias alternative explanation missing from Risks/Gaps despite DORA's own acknowledgment.

3. **What single change would prevent this next time?** Add explicit §7 self-audit checklist item: scan all Q-section headers for dash separators; scan every sentence in Analysis paragraphs for per-sentence labels.

4. **Is this a pattern?** Yes — all four violation classes are documented in `.github/copilot-instructions.md` Known Recurring Patterns table.

5. **Does any documentation need updating?** No new patterns.

6. **Do the default instructions need updating?** The §7 self-review checklist in `research-prompt.md` could add explicit Q-header and Analysis per-sentence checks.

---

## Backlog intake session (original entry below)

# 2026-06-10 -- Add backlog item (ai-productivity-quality-governance-open-questions)

**Completed:**
- `Research/backlog/2026-06-10-ai-productivity-quality-governance-open-questions.md` — added from issue #621; the validated question asks how to distinguish durable Artificial Intelligence (AI)-enabled productivity gains from deferred quality and governance costs over a 12-to-24-month horizon.

## Mini-Retro

1. **Did the process work?** Yes. The issue contained sufficient context to extract decision intent, constraints, and an evidence-oriented output shape without follow-up questions.
2. **What slowed down or went wrong?** The issue references `[1]` through `[11]` but does not include URL mappings in the body, so only the issue URL could be safely recorded as a starting source at intake time.
3. **What single change would prevent this next time?** Include explicit reference links (or a bibliography block) directly in the issue body so backlog intake can preserve all seed sources.
4. **Is this a pattern?** Not yet established as a recurring repository pattern; this session surfaced it, but one confirmed instance is insufficient to classify it as recurring.
5. **Does any documentation need updating?** No immediate update required for this slice; existing instructions already require URL-backed sources and expose the gap clearly.
6. **Do the default instructions need updating?** No. Current rules already prevent unsupported source placeholders from being treated as complete references.
