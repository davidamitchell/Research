# 2026-06-02 -- Research Loop (sre-slo-threshold-justification)

**Completed:**

Research item:
- `Research/completed/2026-05-31-sre-slo-threshold-justification.md` — completed; SRE establishes SLO thresholds as contractual capability boundaries through a three-part chain: evidence selection (user-impact data as primary input, telemetry as practical first-pass proxy), three-party stakeholder negotiation (product manager, development team, SRE team), and error budget enforcement. The threshold number alone has no contractual force; all three steps are required. SLOs adopted without an enforced error budget policy become passive reporting metrics (the "SLO without teeth" failure mode documented in the SRE Workbook).

Sources consulted:
- https://sre.google/workbook/implementing-slos/ (SRE Workbook: Implementing SLOs — primary source for evidence types, stakeholder agreement, and failure modes)
- https://sre.google/workbook/error-budget-policy/ (SRE Workbook: Error Budget Policy — primary source for error budget mechanics, escalation path, and enforcement mechanism)
- https://sre.google/sre-book/embracing-risk/ (SRE Book: Embracing Risk — primary source for min/max SLO framing, economic cost/benefit framework, YouTube business lifecycle case)
- https://sre.google/sre-book/service-level-objectives/ (SRE Book: Service Level Objectives — primary source for user-impact grounding and Chubby planned outage case)
- https://sre.google/workbook/slo-engineering-case-studies/ (SRE Workbook: SLO Engineering Case Studies — Evernote practitioner case study)

## Mini-Retro

1. **Did the process work?** Yes. The item came in at review_count: 1 with OVERALL: FAIL and 6 violations. Fixed all violations, re-triggered review. Second pass also returned OVERALL: FAIL (different violations — source description mismatch, [fact]/[inference] inconsistency between §2 and Findings, unlabeled Risks/Gaps sentences, unsupported superlative in Executive Summary). Fixed all second-pass violations before completing, even though review_count: 2 auto-passed.

2. **What slowed down or went wrong?** Two patterns: (a) "The SRE book" was used in three places where the cited URL was actually the SRE Workbook — a careless source-attribution mismatch that required a pass over §2 and §6 to correct. (b) The same claim was labeled [fact] in Findings KF5 and KF10 but [inference] in §2 and §5 — the parity check between Research Skill Output and Findings was not run carefully enough before the first draft commit.

3. **What single change would prevent this next time?** Before committing, run `grep -n "\[fact\]" Findings` and compare each [fact] label against its corresponding §2/§3 label. If §2 says [inference] for the same claim, the Findings label must match. This is the §2/Findings parity rule (rule 2aa) and it is already documented but not being executed as a checklist step before the first draft commit.

4. **Is this a pattern?** Yes — this matches the known recurring pattern "Unlabeled closing/summary sentences and §6 Synthesis / Findings Executive Summary" and the [fact]/[inference] inconsistency between §2 and Findings. Both are in the Known Recurring Patterns table. No new pattern to add, but the source-description mismatch ("The SRE book" vs. "The SRE Workbook") is a specific instance of citation inaccuracy worth noting: when citing from two distinct sources in the same ecosystem (book vs. workbook), the display name must match the URL path.
