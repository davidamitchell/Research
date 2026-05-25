# 2026-05-25 -- Add backlog item (ontology-world-model-llm-prediction-forcing-functions)

**Completed:**
- `Research/backlog/2026-05-25-ontology-world-model-llm-prediction-forcing-functions.md` — added from issue "RQ"; frames whether ontology completeness can approximate LeCun-style world-model prediction for Large Language Models (LLMs), and what forcing functions slow progress.

## Mini-Retro

1. **Did the process work?** Yes. The issue was converted into a specific, scoped, decomposed research question and recorded as a backlog item without prematurely starting research.
2. **What slowed down or went wrong?** The skills submodule was not initialised in the fresh clone, so the `research-question` skill file was unavailable until submodule setup was run.
3. **What single change would prevent this next time?** Initialize `.github/skills` at session start in fresh clones before applying repository skill workflows.
4. **Is this a pattern?** Yes. Missing skills submodule is a recurring setup issue on fresh runners.
5. **Does any documentation need updating?** No. Existing instructions already document the required submodule initialisation and research-request issue flow.
6. **Do the default instructions need updating?** No new update needed; current instructions already cover this class of task.

---

# 2026-05-25 -- Complete: ontology-world-model-llm-prediction-forcing-functions

**Completed:**
- `Research/completed/2026-05-25-ontology-world-model-llm-prediction-forcing-functions.md` — research on whether ontology completeness can serve as a world model for LLM prediction; concluded that a complete ontology can function as a constraint layer for bounded declarative tasks but cannot satisfy five of LeCun's seven world-model requirements; identified seven structural forcing functions; recommended neuro-symbolic hybrid framing.

## Summary of findings

A sufficiently complete ontology satisfies at most two of LeCun's seven CPWM properties (hierarchical abstraction and relational structural constraints); the five unmet properties (continuous latent dynamics, counterfactual configurability, temporal multi-step forecasting, robustness to partial observation, self-supervised training) are categorically outside ontology scope. KG-enhanced LLMs show measurable factuality gains on structured fact-retrieval tasks (Pan et al. 2024; Fang et al. 2024 report 88% symbolic task performance with modules). Seven forcing functions slow completeness: expert-labour scarcity, incentive misalignment, standards fragmentation, temporal staleness, open-world coverage gaps, governance deficits, and construction cost. The productive design direction is neuro-symbolic hybrid (ontology as constraint layer/type-checker over neural backbone).

## Review cycle summary

- Review run 1 (FAIL): AI/IJCAI/AAAI/W3C expansion; em-dashes; full-sentence bold KFs; KF3/KF8 confidence
- Review run 2 (FAIL): IEEE/TKDE/HR expansion; §7 code-block em-dashes; §6 Evidence Map KF8 confidence; predictive-processing citation gap; KF8 dismissal reasoning
- Review run 3 (FAIL): OWL-S unexpanded; Wikipedia sole source for Cyc claim; "active inference"/"free-energy principle" undefined; fabricated 90%/20% percentages; false-attribution "published estimates" framing
- Review run 4 (PASS): all violations resolved

## Mini-Retro

1. **Did the process work?** The research skill and review cycle worked as designed. The review caught genuine quality gaps (fabricated statistics, unexpanded acronyms, Wikipedia as sole substantive evidence) that would have weakened the item's credibility. Four review iterations is above average.

2. **What slowed down or went wrong?** Three failure modes compounded: (a) domain-specific terms ("active inference", "free-energy principle", "OWL-S") used without first-use definitions; (b) fabricated specific quantitative claims in `[inference]` bullets not caught in self-review; (c) Wikipedia used as sole source for the Cyc historical case.

3. **What single change would prevent this next time?** After drafting §2 Investigation, grep for numeric claims (digits followed by %, "person-month", "range from", "order of magnitude") and verify each maps directly to a cited source. Remove or rewrite as `[assumption]` with "not empirically measured" note if uncited.

4. **Is this a pattern?** Yes — acronym expansion failures are the most-documented recurring violation (19+ failed reviews). Fabricated quantitative estimates in inference bullets is a new variant worth documenting. Wikipedia-sole-source for named historical cases is a documented pattern.

5. **Does any documentation need updating?** Yes — add two new entries to the Known Recurring Patterns table: (a) fabricated specific quantitative estimates in `[inference]` claims; (b) Wikipedia as sole source for named historical cases.

6. **Do the default instructions need updating?** Yes — see two new entries to add to Known Recurring Patterns in `.github/copilot-instructions.md` listed in the sections below.
