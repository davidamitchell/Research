# 2026-09-01 -- Research Loop (neuro-symbolic-nuance-loss-explainability)

**Completed:**

Research item:
- `Research/completed/2026-08-20-neuro-symbolic-nuance-loss-explainability.md` -- completed; enforcing strict logical completeness in a neuro-symbolic ontology pipeline does force discretization of ambiguous or contested human-context data because classical Description Logic represents class membership as binary, and fuzzy Description Logic extensions only partly remediate this because they do not fix the separate, often opaque neural extraction step that assigns raw input to a symbolic class. The explainability gain from symbolic structure is real but bounded to the mapped portion of a decision, and the best-supported architectural guidance is a tiered design: strict symbolic bounds for stable class boundaries, fuzzy or probabilistic layers for known graded boundaries, and an explicit escalation path for cases the ontology cannot represent at all.

Sources consulted:
- https://arxiv.org/abs/2411.04383 (Colelough & Regli 2024 systematic review of neuro-symbolic architectures and intermediate representation opacity)
- https://arxiv.org/abs/1009.3391 (Bobillo & Straccia 2011 primary source on fuzzy Description Logic and fuzzy Web Ontology Language)
- https://ieeexplore.ieee.org/document/10731866 (IEEE user study on ontology-grounded explanation and prediction quality)
- https://arxiv.org/abs/2309.14517 (Kumar et al. 2023 measured accuracy of LLM rule-based content moderation on ambiguous cases)
- https://www.russellsage.org/publications/book/street-level-bureaucracy (Lipsky's foundational study of discretionary rule application and its harms)
- https://www.nimh.nih.gov/research/research-funded-by-nimh/rdoc (dimensional alternative to categorical psychiatric diagnosis, used as a cross-domain analogy for nuance loss under rigid categorization)
- https://yalebooks.yale.edu/9780300078152/seeing-like-a-state/ (Scott's historical analysis of legibility and loss of local knowledge)

## Mini-Retro

1. **Did the process work?** Yes. The item arrived at review pass 2 of 2 with `review_count: 1` already set, and the prior pass 1 failure was purely an infrastructure quota error ("You have exceeded your monthly quota") with no `VIOLATION:` lines, not a content problem. I re-triggered review once (bringing the count to 2, which auto-passes per workflow rules) and used the resulting log to fix three genuine, low-effort violations before completing: an unexpanded IEEE acronym, an unlabeled interpretive closing sentence in §3 Reasoning, and a Key Finding whose medium confidence was inconsistent with its own documented single-source, abstract-only verification gap.
2. **What slowed down or went wrong?** Nothing major. The main friction was distinguishing an infrastructure failure (Copilot review agent hitting its monthly quota mid-run) from an actual content failure in the pass-1 log, since both produce `OVERALL: FAIL`-shaped output in different forms.
3. **What single change would prevent this next time?** None needed for the research-prompt process itself. It might help the review workflow's own log format to include a stable, dedicated marker (e.g. `AGENT_FAILURE: quota_exceeded`) distinct from `OVERALL: FAIL` so the resuming session does not have to reconstruct that distinction by reading raw log text.
4. **Is this a pattern?** The Copilot review agent hitting a monthly quota mid-run is a new observation, not previously documented in the Known Recurring Failure Patterns table. It is plausibly a pattern worth watching if it recurs, but a single occurrence does not yet meet the three-strikes threshold used elsewhere in that table, so no new row was added this session.

## Applied improvements

None required in `research-prompt.md` this session; the retro's question 3 did not surface an actionable prompt change (see above).
