# 2026-07-20 — Add backlog item (tbox-abox-graphrag)

**Completed:**
- `Research/backlog/2026-07-20-tbox-abox-graphrag.md` — added from issue #628; asks to what extent TBox-driven vs ABox-emergent ontology approaches outperform or complement each other in GraphRAG system construction, maintenance, and downstream performance

## Mini-Retro

1. **Did the process work?** Yes. The issue provided a well-structured research question with explicit sub-questions, key failure modes, and suggested investigation directions, making the research-question skill application straightforward. The question passed all five quality checks (Specific, Answerable, Scoped, Motivated, Decomposable) without requiring revision.

2. **What slowed down or went wrong?** The `.github/skills/` submodule was not initialised in the cloned environment, so the research-question skill was applied from memory of the process rather than reading `SKILL.md` directly. This is an expected fallback per the instructions.

3. **What single change would prevent this next time?** Nothing structural — the fallback path works. The skills submodule is initialised by the research loop's own setup step when it runs.

4. **Is this a pattern?** Yes — the submodule is consistently absent in the coding agent environment. This is already documented in the instructions as the expected fallback.

---

# 2026-07-20 — Research and complete (tbox-abox-graphrag)

**Completed:**
- `Research/completed/2026-07-20-tbox-abox-graphrag.md` — full research skill investigation (§0-§7) and Findings completed; concludes that TBox-guided extraction gains a small, isolated accuracy improvement on internally-consistent benchmarks but degrades faster than schema-free extraction on noisy, inconsistently-referenced corpora, and that the largest combined gains come from an expansible "seed schema" hybrid design rather than either pure endpoint. Corpus internal consistency, not domain label, is the key moderator identified.
- `learnings.md` — added a Thread 22 evidence entry sharpening the domain-dependency boundary into a corpus-consistency mechanism, and extended the thread's open question with a replication question raised by this item.

**Review outcome:** Two automated review passes ran (`review_count: 2`, cap reached, auto-pass per workflow design). Both passes surfaced genuine, fixable violations rather than false positives: pass 1 flagged six single-source Key Findings incorrectly labelled "high confidence" (fixed by downgrading to medium per the peer-reviewer multi-source rule), several unlabeled interpretive sentences in §2, an inline-header bold list in Risks/Gaps, and a banned word ("additionally"). Pass 2 flagged a genuinely inaccurate Executive Summary claim (a whole-system 16.62% accuracy figure was being presented as an "isolated margin ... attributable to TBox guidance," contradicting the item's own Analysis section), a mis-cited noise-robustness claim, an acronym expanded in the wrong section (RAG expanded in §0 rather than at its true first use in Scope), an unexpanded proper noun (SPOKE), and an alternative-explanations gap (the corpus-consistency reframing did not acknowledge that the three compared systems differ on backbone model, benchmark design, and implementation stack, not only on corpus consistency). All violations from both passes were fixed in the committed item rather than left to the cap-reached auto-pass.

## Mini-Retro

1. **Did the process work?** Yes, overall. The full §0-§7 research skill process, self-review, and companion-skill checks caught the large majority of issues before the first review; the two review passes then caught a smaller number of real, non-trivial issues (a genuine accuracy misstatement and a real alternative-explanations gap) that self-review missed because I was too close to my own synthesis to see the corpus-consistency reframing needed a confound check.
2. **What slowed down or went wrong?** The first review-workflow run's commit failed to push due to a race with an unrelated `docs/` rebuild commit landing on `main` between my draft push and the review job's own commit attempt; that pass was silently lost (never recorded in `review_count`) and had to be effectively re-run. The self-review process is thorough but linear-costly: verifying acronym first-use *order* (not just presence) required cross-checking Sources-section text against Research Skill Output text, since Sources appears earlier in the document than most of §2 but is easy to treat as exempt boilerplate.
3. **What single change would prevent this next time?** When self-reviewing acronym expansion, explicitly note the *document order* of every section (Title → Research Question → Scope → Context → Approach → Sources → Research Skill Output → Findings → Output) before running the acronym scan, rather than assuming Research Skill Output is where "first use" audits start. Sources and Scope routinely contain the true first prose use of domain acronyms in this template.
4. **Is this a pattern?** Partially — acronym-expansion-in-the-wrong-section is a variant of the already-documented "acronym expanded only inside a code block" pattern in the Known Recurring Failure Patterns table, but specifically about section *order* rather than block type. This session's finding (Sources/Scope routinely precede Research Skill Output for the first prose use of a term) is worth adding to that table's guidance if it recurs on a future item.
5. **Does any documentation need updating?** No structural changes needed; the existing acronym-audit guidance in `research-prompt.md` already instructs a full-document scan, this session simply under-applied it to the Sources section specifically. Noting the pattern here rather than adding a new instructions rule.
6. **Do the default instructions need updating?** Not yet — this is a single occurrence of the section-order acronym miss, not yet a three-strikes pattern. Flagging it here so a second occurrence gets tracked as one.
