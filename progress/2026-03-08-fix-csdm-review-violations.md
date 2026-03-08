# 2026-03-08 — Fix citation-discipline violations in CSDM research

## Session purpose

Fix the four citation-discipline violations flagged by the research review for
`Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`.

## What was done

Four violations were identified and fixed:

1. **[fact] label on unverified-inference SPM claim (§2 C3)**
   - The SPM minimum viable CSDM paragraph was labelled `[fact]` but every cited
     source was an unverified `[inference]`.
   - Fix: changed the opening label from `[fact]` to `[inference]`.

2. **ITBM and PPM unexpanded on first use (§2 C3)**
   - "formerly ITBM/PPM" appeared without spelling out the acronyms.
   - Fix: expanded to "formerly IT Business Management (ITBM)/Project Portfolio
     Management (PPM)".

3. **OOB unexpanded on first use (§5 Historical lens)**
   - "customised away from CSDM OOB tables" used the acronym without expansion.
   - Fix: expanded to "out-of-the-box (OOB)".

4. **AIOps unexpanded on first use (§5 Open Questions + Findings Open Questions)**
   - Both occurrences of "AIOps" lacked a full-form expansion.
   - Fix: first occurrence (§5) expanded to "Artificial Intelligence for IT
     Operations (AIOps)"; second occurrence (Findings) expanded inline as
     "AIOps (Artificial Intelligence for IT Operations)".

## Files changed

- `Research/completed/2026-03-08-servicenow-csdm-data-modelling.md`
