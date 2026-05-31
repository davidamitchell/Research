# 2026-05-31 — split-authority-q1-flow-constraint

**Completed:**
- `Research/completed/2026-05-29-split-authority-q1-flow-constraint.md` — researched and completed. The validated research question asks which delivery constraint is dominant in split-authority systems; the answer is governance-generated queueing (approval latency and fragmented decision rights), not capacity shortage. Supported by DORA multi-firm survey data, Value Stream Mapping (VSM) case study evidence (97% wait time, 200-engineer firm), and Theory of Constraints (TOC) policy-constraint theory.

**Key findings:**
- Governance-generated queueing (approval latency + fragmented decision rights) is the dominant throughput constraint in split-authority delivery systems.
- Constraint hierarchy: fragmented decision rights (structural root) → approval latency (direct mechanism) → dependency coupling (amplifier) → funding gates (coarser cycle). Capacity shortage is secondary and partially endogenous.
- DORA 2019 report: pre-approval gates add two to four weeks per feature cycle in low-performing teams; elite teams eliminate most pre-approval latency via automated gates or pre-authorisation.
- VSM case evidence shows 97% of cycle time is approval wait in a 200-engineer firm (Org Topologies / James Shore).
- TOC policy-constraint theory predicts that the constraint resides in organisational rules and decision structures rather than physical resources.

**Review cycle:** Four automated review passes; passed on pass 4.

**Pass-3 violations fixed in this session:**
- §2 C4: Removed Reinertsen name attribution without a URL to Reinertsen's own work; replaced with generic queueing theory language.
- Findings Analysis §3: Added per-sentence `[inference; source:]` labels; removed "No strong rival explanation supports capacity shortage" evaluative opener.
- Findings Analysis §4: Removed binary contrast "not merely slow; they are dynamically unstable"; replaced with direct assertion with per-sentence label.

---

## Mini-Retro

1. **Did the process work?** Largely yes. The research skill produced a well-structured item and the automated review caught real violations across four passes. The passes converged — each successive failure set was smaller and more targeted.

2. **What slowed down or went wrong?** Four review passes were needed before PASS. Three patterns recurred: (a) named-author attribution without a direct URL to the author's own work; (b) Analysis paragraph opening sentences lacking their own `[inference; source:]` label; (c) evaluative openers ("No strong rival", "most compelling") needing their own labels even mid-paragraph. These are all in the Known Recurring Patterns table but still required multiple fix cycles.

3. **What single change would prevent this next time?** Before the draft commit, run a sentence-by-sentence scan specifically of all Analysis paragraphs — confirm every sentence (including the first) carries its own inline label. The trailing-label pattern (where the paragraph-end label is mistakenly assumed to cover the whole paragraph) is the most common root cause.

4. **Is this a pattern?** Yes — "unlabeled opening/closing sentences" and "named-author attribution without direct URL" are both in the Known Recurring Patterns table. This session adds another data point confirming that the Analysis section is the highest-risk location for per-sentence label violations.

5. **Does any documentation need updating?** No new patterns to add; existing Known Recurring Patterns table already covers the failures seen here.

6. **Do the default instructions need updating?** No. The instructions already call out per-sentence Analysis labeling explicitly. The gap is in execution rather than in the instructions.
