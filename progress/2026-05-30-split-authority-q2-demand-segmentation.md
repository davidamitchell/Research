# 2026-05-30 -- Complete split-authority Q2 demand segmentation

**Completed:**
- `Research/completed/2026-05-29-split-authority-q2-demand-segmentation.md` — researched and completed; answers which work items qualify for fast-path handling vs. slower expert review using three axes (risk level, reversibility, standardisation) and three boundary-condition tests (template, recovery, blast radius)

**Sources used:** AXELOS ITIL 4 Change Enablement, Google SRE workbook/book, Reinertsen *Principles of Product Development Flow*, AHRQ Emergency Severity Index, DORA metrics, BCBS 328, and completed repository items on governance controls, do-mode demand persistence, AI/low-code risk tiers, and human-in-the-loop boundaries.

**Review passes required:** 10 (9 fail, 1 pass). All violations were citation-discipline or speculation-control; no structural rewrites needed.

**Violation pattern log:**
- Pass 1–2: Bold Key Findings; unlabeled §2/§6 causal sentences
- Pass 3: Executive Summary "worsening the bottleneck" unlabeled; "strongly supports" subjective intensifier
- Pass 4: BCBS 328 scope mismatch; §6 confidence parity gap; unlabeled §3/§6 Analysis claims
- Pass 5: CTAS cited with US-only AHRQ source; §5 Organisational lens unlabeled sentences; Historical lens unqualified "globally" claim
- Pass 6: ITIL facts cited with third-party personal-website PDF (mafranci.com); line 404 [fact] on interpretive comparison
- Pass 7: Cross-framework "is consistent with" claim labeled [fact] instead of [inference]
- Pass 8: Executive Summary opening sentence unlabeled; §6 Risks "most" vague quantifier without source
- Pass 9: §2 fast-track claim scope mismatch (ESI source for ED design claim); §6 summary three sentences unlabeled; Analysis four-class rejection sentence unlabeled

## Mini-Retro

1. **Did the process work?** Yes, eventually. The structured §0–§7 skill output and Findings were sound from early passes; violations were consistently label/scope issues, not structural problems.

2. **What slowed down or went wrong?** Nine review failures over one research item. The dominant failure mode was epistemic label omission on claims that appeared "obvious" or were summary/concluding sentences. Cross-framework synthesis claims were repeatedly labeled [fact] when they required [inference] because only one side of the comparison was directly supported by the cited source.

3. **What single change would prevent this next time?** Before triggering any review, run a targeted grep for: (a) sentences that end a paragraph with no label, (b) opening sentences of Executive Summary and §6 Synthesis, (c) any word "most", "all", "globally", "always", or "clearly" without a label. These are the recurrence points.

4. **Is this a pattern?** Yes — this extends the "unlabeled evaluative judgments in Analysis" and "cross-framework comparison without both-sides sourcing" patterns already in the Known Recurring Patterns table. The specific new sub-pattern: **closing/summary sentences of a paragraph inherit no label from the preceding sentences and must be labeled independently.** The §6 Synthesis opening paragraph is particularly vulnerable because authors treat it as a summary restatement rather than a claim.

5. **Does any documentation need updating?** The Known Recurring Patterns table in `.github/copilot-instructions.md` should gain an entry for "unlabeled closing/summary sentences" and "opening sentences of §6 Synthesis and Findings Executive Summary."

6. **Do the default instructions need updating?** Yes — add to the self-review checklist: explicitly audit the opening sentence of §6 Synthesis and the first sentence of Findings Executive Summary, plus every sentence that ends a paragraph without a label.
