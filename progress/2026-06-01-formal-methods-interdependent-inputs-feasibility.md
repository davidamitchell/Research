# 2026-06-01 -- Complete research item: formal-methods-interdependent-inputs-feasibility

**Item:** `Research/completed/2026-05-31-formal-methods-interdependent-inputs-feasibility.md`

**Completed:**
- `Research/completed/2026-05-31-formal-methods-interdependent-inputs-feasibility.md` — completed; characterises decidability and scale limits of Z notation, Alloy, and TLA+ for automated feasibility checking of interdependent constraint inputs; finds the tractable enterprise class is bounded, finite-state, decomposed modules
- `learnings.md` — added Thread 4 evidence entry for the formal methods tractability boundary finding
- Two review passes (review_count: 2); first pass returned OVERALL: FAIL (10+ violations fixed); second pass returned OVERALL: FAIL with residual violations (acronyms, unlabeled Analysis sentences, KF confidence issues); violations fixed before completion

**Review violations fixed in first pass:**
- Em-dash (U+2014) occurrences removed document-wide (Research Question, Sources, §0, §3 code block)
- §2 Q3 unlabelled sentence (TLC lasso detection): added `[fact; source: ...]`
- §3 Reasoning: three unlabelled closing/opening sentences in Z, Alloy, and TLA+ sections labelled
- §6/Findings KF 7 (AWS bug count): [fact] high → [inference] medium (primary CACM source inaccessible HTTP 403)
- §6/Findings KF 8 (model design cost): high → medium confidence (single secondary source)
- §6 Evidence Map rows for KF 7 and 8 updated to match
- §6/Findings Analysis "most comprehensive" superlative rewritten to "provides detailed public evidence"
- §6/Findings Analysis cross-reference added: Z3 soft-constraint tiering finding from companion item `2026-05-17-policy-enforcement-formal-verification-energy-functions`
- Findings Executive Summary final sentence: added `[inference; source: ...]` label
- Findings Key Findings 1–11: removed full-sentence bold (inline-header list pattern violation)

**Review violations fixed in second pass:**
- Acronyms: NP expanded to "nondeterministic polynomial (NP)"; ACM, HTTP expanded in Sources; CACM expanded in §6 Evidence Map note
- §5 Historical lens closing sentence: added `[inference; source: ...]`
- §5 Economic lens closing sentence: added `[inference; source: ...]`
- §6 Analysis paragraphs 1–4 opening sentences: all labelled with `[inference; source: ...]`
- Findings Analysis paragraphs 1–4 opening sentences: mirrored same labels (parity fix)
- KF 2 (Alloy SAT/Kodkod encoding): added second source (`https://alloytools.org/documentation.html`) alongside Jackson (2012) to justify high confidence
- KF 6 (TLA+ liveness undecidability): downgraded from [fact] high → [inference] medium (single source)
- Evidence Map rows for KF 2 and KF 6 updated to match in both §6 and Findings

## Mini-Retro

1. **Did the process work?** Partially. The review loop caught real violations and the fix cycle was systematic. Two full review passes were needed; the auto-pass at review_count ≥ 2 allowed completion without a third full cycle, but the remaining violations (Analysis opening sentences, acronym NP) were genuine quality gaps that benefited from being fixed.

2. **What slowed down or went wrong?** The most time-consuming part was the Analysis opening-sentence pattern: every paragraph in both §6 and Findings Analysis had unlabelled first sentences. This is a direct instance of the "Unlabeled closing/summary sentences and §6 Synthesis / Findings Executive Summary opening sentences" known recurring pattern. The pattern was in the table but the fix was not applied during initial authorship.

3. **What single change would prevent this next time?** Before triggering review for any research item, run: `grep -n "^[A-Z]" <Analysis sections>` and manually check that every paragraph-opening sentence ends with a `[inference/fact/assumption; source: ...]` label. The known patterns table already documents this but it is not being caught in the pre-review self-check.

4. **Is this a pattern?** Yes — this is the "Unlabeled closing/summary sentences" pattern already in the Known Recurring Patterns table. The item was authored before the pattern was documented but the pre-commit check step should have caught it. The root fix is applying the check more rigorously in the pre-review self-audit (Step 6 of the research-loop prompt).

5. **Does any documentation need updating?** The Known Recurring Patterns table entry for "Unlabeled closing/summary sentences" already covers this, but could be strengthened to explicitly name "Analysis paragraph opening sentences" as a distinct failure subtype rather than grouping them only under "closing/summary sentences."

6. **Do the default instructions need updating?** The self-review checklist (Step 6 item 2c) already mentions this, but consider adding an explicit mechanical check: `grep -n "^\(Z notation\|The enterprise\|The gap\|A plausible\)" <item>` as a worked example of the analysis-opening-sentence audit. A named regex that matches sentences starting with capital letters at the start of Analysis paragraphs would make this check actionable rather than advisory.
