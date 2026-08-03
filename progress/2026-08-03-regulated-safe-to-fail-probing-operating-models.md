# 2026-08-03 -- Regulated safe-to-fail probing operating models

**Completed:**
- `Research/completed/2026-07-20-regulated-safe-to-fail-probing-operating-models.md` -- researched and completed the item on governance structures and team models for safe-to-fail experimentation in regulated industries (financial services, healthcare, pharmaceuticals). Investigated four recurring governance archetypes (regulator-run sandbox, health-sector sandbox, organisation-level precertification, embedded-control team) and the relationship between experiment-tracking structure and outcomes. Went through two full `research-review.yml` cycles (both FAILED, budget exhausted at pass 2/2 with no blocking issue raised) before completing.
- `learnings.md` -- added the item as a new evidence bullet to Thread 13 (bureaucracy/control-accumulation), contributing the containment-side counterpart: governance archetypes can operate exactly as designed and still fail to reach a durable outcome ceiling (US Food and Drug Administration (FDA) Digital Health Software Precertification (Pre-Cert) Pilot Program discontinuation), independent of whether internal controls degrade.

## Mini-Retro

1. **Did the process work?** Yes. The research → draft → review → fix → re-review → complete loop worked end-to-end, and both review cycles caught real, substantive issues (missing sources for heavily-cited analogical material, unlabeled evaluative sentences, single-source confidence overreach) that materially improved the item's rigor.

2. **What slowed down or went wrong?** Two separate instances of the `research-review.yml` commit-push race were observed: the review job's own commit (incrementing `review_count`) was rejected by a concurrent commit on `main` on the first review run, so that FAIL did not count toward the two-review budget and had to be re-verified via `git log origin/main` before proceeding. This is a known, already-documented recurring pattern (see the Known Recurring Failure Patterns table in `.github/copilot-instructions.md`), and this session is a third and fourth confirming occurrence of the same class of race. A new, not-previously-documented failure mode also appeared: two heavily and repeatedly cited sources (Kohavi et al.'s Cambridge experimentation-platform book, Cooper's Stage-Gate model) were used substantively across four sections of the item but never added to the `## Sources` list, because they were discovered and folded in as analogical evidence during §2/§3/§5 writing rather than during the initial source-gathering pass.

3. **What single change would prevent this next time?** Add an explicit checklist step to `research-prompt.md` immediately before the draft commit: grep every URL cited inline in `## Research Skill Output` and `## Findings`, and confirm each one also has a corresponding entry in `## Sources`. This would have caught the missing-sources violation before triggering the first review, saving one full review cycle.

4. **Is this a pattern?** The push-race issue is a confirmed, recurring pattern already tracked in `copilot-instructions.md` -- no new table entry needed, this session is corroborating evidence. The missing-sources-for-analogically-cited-material issue is new; added as an actionable process fix below (not yet promoted to the Known Recurring Patterns table since this is only its first observed instance -- will add if it recurs).

5. **Does any documentation need updating?** Yes -- `research-prompt.md` updated (see below) to add an inline-citation-to-Sources completeness check before the draft commit step.

6. **Do the default instructions need updating?** Not yet -- the missing-sources pattern has only appeared once; per the repo's own three-strikes convention for promoting a pattern to the Known Recurring Patterns table, this is being tracked here in the session log rather than added to `.github/copilot-instructions.md` prematurely.

## Review budget note

Both review passes for this item ended in FAIL:
- Pass 1/2: DOI unexpanded, unsupported FDA corroboration claim, three unlabeled ranking-judgment sentences, two single-source High-confidence claims. All fixed.
- Pass 2/2: PDF/HTTP unexpanded at first use, two missing Sources entries, three more unlabeled evaluative sentences. All fixed. Pass 2/2 result was FAIL but **no blocking issue was raised** (confirmed via `gh issue list --label research-review` showing no open issue for this item), consistent with the two-review budget being exhausted without escalation. The item was completed with `confidence: medium` in frontmatter, reflecting that several Key Findings rest on single-source or analogical (non-regulated-sector) evidence.
