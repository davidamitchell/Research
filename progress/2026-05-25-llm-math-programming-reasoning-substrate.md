# 2026-05-25 -- LLM math/programming reasoning substrate (backlog → completed)

## Session 1: Add backlog item

**Completed:**
- `Research/backlog/2026-05-25-llm-math-programming-reasoning-substrate.md` — added from the "New research question" issue; scopes whether mathematics and programming are especially strong Large Language Model (LLM) use cases because of formal language structure, and seeds prior learnings to revisit first.

---

## Session 2: Research and completion

**Item completed:** `Research/completed/2026-05-25-llm-math-programming-reasoning-substrate.md`

**Work done:**
- Full §0–§7 Research Skill Output written
- Complete Findings section with all subsections
- Three review cycles: two failures, auto-passed at review cap on third
- `learnings.md` Thread 11 updated with calibrated decomposition finding

**Key findings:**
- The formal symbolic alignment thesis conflates three independent mechanisms: training data domain coverage (most directly observable), compositional structure + chain-of-thought (CoT) alignment (real but partly a training-data artifact), and external verifiability (operationally distinctive — closed correction loop)
- AlphaProof's International Mathematical Olympiad (IMO) 2024 silver-medal result depended on Lean formal verification as the reinforcement learning (RL) reward signal; without the verifier the result does not hold
- Benchmark contamination is a material confound for HumanEval/code benchmark scores
- The formal specification hierarchy (informal → type-constrained → full verification) maps onto a graded performance curve

## Mini-Retro

1. **Did the process work?** Mostly yes. The research content is solid and all sections are populated with evidence. The review workflow correctly caught real violations across three passes.

2. **What slowed down or went wrong?**
   - Three review failures were all due to the same class of issue: missing epistemic labels ([fact]/[inference]) in Findings Key Findings and improper bold formatting (full sentence bolded, not just key term).
   - The KF bold-format violation (entire sentences bolded) was flagged as AI slop but was missed in all manual passes before the workflow caught it.
   - KF7 used "(not model scale)" to make a causal negation that the evidence only supports as a correlation; the review correctly flagged this.
   - `python -m src.main research complete Research/in-progress/<path>` required the filename only, not the full relative path.

3. **What single change would prevent this next time?** Run a targeted grep before committing: every numbered KF line should match the pattern `\([inference\|fact\|assumption\]; .* confidence; source:`. Any KF that doesn't match has a missing label.

4. **Is this a pattern?** Yes — missing epistemic labels in Key Findings is the most common violation across review cycles in this repo. Also new: the bold-formatting of entire KF sentences is a recurring AI slop trigger.

5. **Does any documentation need updating?** The Known Recurring Failure Patterns table in `.github/copilot-instructions.md` should add the KF bold-formatting failure.

6. **Do the default instructions need updating?** Yes — add a Known Recurring Pattern entry: "Key Finding full-sentence bold — bolding the entire claim sentence triggers remove-ai-slop; only term-level bold is allowed."
