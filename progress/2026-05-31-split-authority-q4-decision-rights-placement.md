# 2026-05-31 -- Complete split-authority-q4-decision-rights-placement

**Completed:**
- `Research/completed/2026-05-29-split-authority-q4-decision-rights-placement.md` — research item answering which execution decisions must sit with delivery teams (daily sequencing, minor scope adjustment, SLO-bounded reliability choices, capacity-band technical debt, below-ceiling environment spend, live incident response) versus which must be retained by governance (catalog deviations, cost ceiling breaches, blast-radius overflows, external commitments); three pre-defined parameters replace per-decision approval; confidence: medium.
- `learnings.md` Thread 18 — added Q3 and Q4 evidence entries; extended open thread.
- `progress/2026-05-31-split-authority-q4-decision-rights-placement.md` — this session log.

## Mini-Retro

1. **Did the process work?** Mostly. The research itself was well-structured and produced a complete §0–§7 plus full Findings. The three-review cycle was necessary but preventable — all three failures were systematic patterns documented in the Known Recurring Patterns table that I did not check aggressively enough before the first draft commit.

2. **What slowed down or went wrong?**
   - **Pass 1 failure:** Bounded delegation was defined only by citing the P1 companion item, not an external source. The first-use rule is document-wide — the Approach section counts, not just §0. Fixed by adding DORA State of DevOps external source.
   - **Pass 1 failure (secondary):** Blast radius and Little's Law were used without first-use definitions.
   - **Pass 2 failure — citation-discipline:** Two ICS historical-origin claims were labeled `[fact]` citing only the Google SRE Workbook, which is a secondary practitioner source. The Known Recurring Patterns table explicitly warns: "`[fact]` claim with only a tertiary source." This applied equally to a reputable secondary source.
   - **Pass 2 failure — remove-ai-slop (em-dash):** A pass 1 fix introduced an em-dash (`—`) in §0 by rewriting a sentence. The Known Recurring Patterns table and the review skill both prohibit em-dashes. Should have run `python3 -c "content=open(file).read(); print(content.count('\u2014'))"` after every edit.
   - **Pass 2 failure — remove-ai-slop (bold Key Findings):** All 10 Key Findings were fully bolded (`**Claim text.**`) following the format string in the research prompt. This directly conflicts with the Known Recurring Patterns rule: "Never bold a full sentence." The prompt format and the review skill are contradictory. The review skill wins.

3. **What single change would prevent this next time?**
   Add a pre-commit bash check to the research workflow that detects the three systematic patterns before the first draft commit:
   ```bash
   # Check 1: em-dashes
   python3 -c "c=open(f).read(); assert c.count('\u2014')==0, 'em-dash found'"
   # Check 2: fully-bolded Key Findings (bullets opening with **)
   grep -n "^\d\+\. \*\*" Research/in-progress/*.md
   # Check 3: [fact] labels on secondary-source claims (ICS, Google SRE, etc.)
   grep -n "\[fact\].*Google SRE\|\[fact\].*Wikipedia\|\[fact\].*Britannica" Research/in-progress/*.md
   ```

4. **Is this a pattern?** Yes — all three are documented in the Known Recurring Patterns table in `.github/copilot-instructions.md`. The em-dash and bold-Key-Findings failures are recurring; the `[fact]` on secondary sources is partially covered by the `[fact]` claim with only a tertiary source pattern but extends to respected secondary sources (Google SRE Workbook is not tertiary, but still insufficient for a historical origin claim about a 1968 incident command system). The table should be updated for the secondary-source extension.

5. **Does any documentation need updating?** The Known Recurring Patterns table should be updated to extend the `[fact]`/tertiary-source rule to secondary sources for historical-origin claims (original invention/creation claims require primary archival or primary author sources, not practitioner handbooks). Adding this precision would prevent the same failure on future items about DORA origins, SRE history, ITIL history, etc.

6. **Do the default instructions need updating?** Yes — add a note to the Known Recurring Patterns table: historical origin claims (`[fact]` about when something was invented or created) require a primary source (original paper, contemporaneous record, or first-person account). Secondary practitioner sources (SRE Workbook, ITIL Foundation Guide, DORA State of DevOps report) are insufficient for `[fact]` on historical origin claims; the label must be `[inference]` unless a primary source is added.
