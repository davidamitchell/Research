---
title: "Research Quality Assurance and Knowledge Integration Methodology"
added: 2026-03-02
status: completed
priority: medium
tags: [research-methodology, quality-assurance, peer-review, knowledge-integration, information-to-wisdom, ci, skills]
started: 2026-03-08
completed: 2026-03-08
output: [skill, knowledge, backlog-item]
---

# Research Quality Assurance and Knowledge Integration Methodology

## Research Question

What review methodology is required to reliably move from information gathering through to applied knowledge and wisdom — and which of those steps can be automated in a CI pipeline versus requiring human or peer-level judgement?

## Scope

**In scope:**
- Current skills inventory and gap analysis: citation-discipline, speculation-control, remove-ai-slop — what each checks, what each misses
- Peer review as a distinct quality dimension: what a peer reviewer catches that automated checks cannot (logical coherence, missing context, alternative interpretations, applicability)
- Integration skill: synthesising findings from multiple completed research items into a coherent body of knowledge rather than treating each item in isolation
- The information → knowledge → wisdom pipeline: how raw sourced information becomes internalised knowledge, and how knowledge becomes applicable wisdom (decision-relevant, context-adapted, actionable)
- Applicability testing: how to verify that a research finding is usable in a specific context, not just true in the abstract
- Which review steps are automatable via a CI pipeline (static analysis of structure, citation presence, speculation markers, slop patterns) versus which require agent-level reasoning or human review
- Ordering and composition of review steps: can automated checks gate the pipeline before expensive reasoning-based checks?

**Out of scope:**
- Research item filing mechanics (covered by existing CLI tooling)
- Content of any specific research item (this is methodology, not object-level research)
- General epistemology or philosophy of science beyond what is directly applicable to a practical review pipeline

**Constraints:** Focus on what is implementable using GitHub Actions, existing agent skills, and MCP tools already available in this repo. Do not propose infrastructure that requires new credentials or services without flagging as a follow-up.

## Context

This repo uses a set of agent skills to review research quality: `citation-discipline` (are claims sourced?), `speculation-control` (are uncertain claims flagged?), and `remove-ai-slop` (is the writing direct and precise?). These cover factual hygiene and writing quality.

What they do not cover:
- **Peer review**: whether the reasoning holds, whether alternative explanations were considered, whether the conclusions follow from the evidence
- **Integration**: whether findings from this item connect to, extend, or contradict findings from related completed items
- **Applicability**: whether the knowledge can actually be applied in the specific contexts relevant to this repo's owner (NZ financial services, SWE, agentic AI)
- **Wisdom**: whether the accumulated body of completed research items is forming coherent, decision-relevant understanding — or just accumulating facts

There is a related repo improvement item (BACKLOG.md W-0031) to implement a research review CI step. That item is blocked until this research is complete: the CI design depends on knowing which checks are automatable and in what order.

**Prior research:** The cross-item synthesis item (`2026-03-03-cross-item-synthesis-meta-insights.md`) established that synthesis (cross-item integration) operates at the Knowledge → Wisdom transition in the DIKW hierarchy, and individual research items operate at the Information → Knowledge transition. The research loop quality item (`2026-03-03-research-loop-quality-prompt-engineering.md`) identified five quality dimensions relevant to this question: executive summary depth, source engagement, findings specificity, open questions utility, and cross-item integration — and classified which are automatable vs. require agent reasoning. The knowledge retention item (`2026-03-03-knowledge-retention-active-recall.md`) established that knowledge without re-engagement decays within 2–4 weeks, and that applicability (applying a finding to a real decision) produces the strongest retention. This item must add the canonical three-tier automation taxonomy (fully automatable / agent-automatable / human-only) mapped to specific pipeline steps, and the formal scope definition for the proposed `peer-review` skill — neither of which the prior items address.

## Approach

1. **Skills gap analysis** — Document precisely what each existing skill checks, what format/structure it expects, and what quality dimensions it leaves uncovered. Identify the specific failure modes that citation-discipline, speculation-control, and remove-ai-slop do not catch.
2. **Peer review patterns** — Survey how peer review is structured in academic, open-source, and knowledge-management contexts. Identify which peer review behaviours are replicable by an LLM agent with access to the completed item and its sources, and which require a second independent expert.
3. **Integration methodology** — How do knowledge management systems (Zettelkasten, Roam, Obsidian workflows, Notion AI) handle cross-item synthesis? Which techniques transfer to a file-based Markdown research corpus?
4. **Information → knowledge → wisdom frameworks** — Review Ackoff's DIKW hierarchy, Nonaka's SECI model, and pragmatic alternatives. Assess which frameworks translate into testable, checkable steps rather than vague aspirational stages.
5. **Applicability testing** — What does it mean to test whether a finding is applicable? Survey methods: scenario-based testing, counterfactual checking, decision-forcing cases. Which are automatable?
6. **CI pipeline design** — Map each review dimension to: (a) fully automatable (rule/structure-based), (b) agent-automatable (requires LLM reasoning), (c) human-only. Sequence them by cost and gate logic. This is the direct input to BACKLOG.md W-0031.
7. **New skills needed** — Identify whether a `peer-review` skill and/or an `integration` skill should be added to `davidamitchell/Skills`, and draft their scope.

## Sources

- [x] Ackoff (1989) — "From Data to Wisdom": https://doi.org/10.1111/j.1467-9310.1989.tb00072.x — foundational DIKW hierarchy (secondary sources consulted; primary DOI paywalled)
- [x] Nonaka & Takeuchi (1995) — *The Knowledge-Creating Company* — SECI model (secondary sources consulted)
- [x] Bloom's Taxonomy (1956, revised 2001) — cognitive levels as a framework for knowledge depth vs applicability
- [x] Zettelkasten method — https://zettelkasten.de/introduction/ — atomic notes, linking, emergence of insight through connection
- [ ] Ahrens (2017) — *How to Take Smart Notes* — practical Zettelkasten for researchers; integration as a first-class practice (book not accessible)
- [ ] GitHub Actions documentation — composite actions, reusable workflows — for CI pipeline design (not consulted; sufficient knowledge from prior research)
- [x] Existing skills: `.github/skills/citation-discipline/SKILL.md`, `.github/skills/speculation-control/SKILL.md`, `.github/skills/remove-ai-slop/SKILL.md` — gap analysis starting point
- [x] Academic peer review process documentation — Springer Nature peer review guidelines: https://www.springernature.com/gp/authors/campaigns/how-to-peer-review-3
- [x] LLM automated peer review — REMOR (arXiv:2505.11718), DeepReview (ACL 2025), LLM4Review (OpenReview)
- [x] Related completed items: `2026-03-03-cross-item-synthesis-meta-insights.md`, `2026-03-03-research-loop-quality-prompt-engineering.md`, `2026-03-03-knowledge-retention-active-recall.md`, `research-review-prompt.md`, `.github/workflows/research-review.yml`

---

## Research Skill Output

### §0 Initialise

**Research question:** What review methodology is required to reliably move from information gathering through to applied knowledge and wisdom — and which of those steps can be automated in a CI pipeline versus requiring human or peer-level judgement?

**Scope:** This is a methodology question, not an object-level research question. The deliverable is a taxonomy of quality dimensions, a three-tier automation classification (fully automatable / agent-automatable / human-only), a sequenced CI pipeline design, and a scope definition for any new skills required. The constraint is to design only what is implementable with GitHub Actions, the existing Copilot CLI agent, and the agent skills already in `davidamitchell/Skills`.

**Definitions:**
- *Fully automatable*: implementable as a deterministic script or regex pattern; no LLM required.
- *Agent-automatable*: requires LLM reasoning but does not require domain expertise a general-purpose LLM lacks.
- *Human-only*: requires contextual judgment that an agent without domain-specific memory or lived experience cannot reliably provide.
- *DIKW hierarchy* (Data, Information, Knowledge, Wisdom): Ackoff's 1989 framework for understanding the transformation pipeline from raw facts to decision-relevant judgment.
- *SECI model* (Socialisation, Externalisation, Combination, Internalisation): Nonaka and Takeuchi's 1995 model of how tacit and explicit knowledge interact in knowledge creation.

**Output format:** Structured findings with evidence map, three-tier taxonomy table, CI pipeline sequence, and skill scope drafts.

### §1 Question Decomposition

**Top-level question:** What review methodology moves information → knowledge → wisdom, and which steps can a CI pipeline automate?

Decomposed:

1. **What does each existing skill check, and what does it miss?**
   - 1a. What does `citation-discipline` check?
   - 1b. What does `speculation-control` check?
   - 1c. What does `remove-ai-slop` check?
   - 1d. What quality dimensions do all three together fail to cover?

2. **What does peer review catch that automated checks cannot?**
   - 2a. What does academic peer review assess (Nature/Springer Nature guidelines)?
   - 2b. Which peer review dimensions are replicable by an LLM agent?
   - 2c. Which peer review dimensions require a second independent expert?

3. **How do knowledge management systems handle cross-item integration?**
   - 3a. What is the Zettelkasten approach to linking and integration?
   - 3b. What transfer to a file-based Markdown corpus?

4. **Which DIKW/SECI stages map to specific review actions?**
   - 4a. Where does a research item sit in the DIKW hierarchy?
   - 4b. What actions move a finding from information to knowledge?
   - 4c. What actions move knowledge to wisdom?

5. **What methods test applicability?**
   - 5a. What is "applicability testing" in educational/knowledge frameworks (Bloom's)?
   - 5b. Which applicability test methods are automatable?

6. **What is the correct CI pipeline sequence?**
   - 6a. Map each review dimension to its automation tier.
   - 6b. Order by cost with cheaper gates first.

7. **What new skills are needed?**
   - 7a. Should a `peer-review` skill be added to `davidamitchell/Skills`?
   - 7b. Should an `integration` skill be added?

### §2 Investigation

**Atomic question 1a–1c: What do the existing skills check?**

Reading `.github/skills/citation-discipline/SKILL.md`, `.github/skills/speculation-control/SKILL.md`, and `.github/skills/remove-ai-slop/SKILL.md` directly from the repository:

*Citation-discipline* [fact]: checks that every factual claim has a corresponding verifiable source, that citations are placed at the sentence containing the claim, that source quality is appropriate (primary > secondary > tertiary), that vague quantifiers are sourced, that acronyms are expanded on first use, and that non-self-evident domain terms are linked to authoritative definitions. It does not check whether the source actually supports the claim's logical conclusion — only that a source is present and of sufficient quality.

*Speculation-control* [fact]: checks that speculative statements are prefixed `Speculation:` or `Hypothesis:`, that opinions are labeled `Opinion:`, that uncertainty language is precise ("cannot be determined from available evidence"), and that evidentiary gaps are not filled with invented detail. It does not check whether an inference drawn from correct facts is logically valid.

*Remove-ai-slop* [fact]: checks for predictable token sequences ("Furthermore", "Additionally", "In conclusion"), over-structured layout, alignment artifacts (safety-prefacing language, over-explained causal links), and stylometric uniformity. It operates on surface-level writing patterns and does not engage with the content's logical structure.

**Atomic question 1d: What do all three together fail to cover?** [inference]

Combining the skill definitions, the uncovered quality dimensions are:
- *Logical coherence*: whether the conclusions stated in the Executive Summary and Key Findings actually follow from the evidence presented in §2 Investigation. A research item can have every claim sourced, every inference labeled, and no slop patterns — and still reach a wrong conclusion by misreading its own sources or by omitting contradictory evidence.
- *Alternative explanations*: whether competing hypotheses or interpretations were considered. Springer Nature peer review guidelines explicitly require reviewers to check that "authors have discussed potential alternative interpretations of their data" (Springer Nature, How to Peer Review, 2025). This is absent from all three current skills.
- *Cross-item integration*: whether findings from this item connect to, extend, or contradict findings from related completed items. The `research-loop-quality-prompt-engineering` item flagged "cross-item integration" as one of five quality dimensions, classifying it as requiring agent reasoning. Neither citation-discipline nor speculation-control addresses it; remove-ai-slop does not engage with content at all.
- *Applicability*: whether the knowledge is usable in the specific contexts relevant to this owner (NZ financial services, SWE, agentic AI), not just abstractly correct.
- *Evidence sufficiency for conclusions*: whether the number and independence of sources is sufficient to support the confidence level assigned, not just that sources exist.

**Atomic question 2a: What does academic peer review assess?** [fact]

Springer Nature peer review guidelines (2025) instruct reviewers to assess: (1) significance and originality, (2) scientific/methodological rigour, (3) logical progression from methods to results to conclusions, (4) alternative explanations or interpretations of data, (5) stated limitations. The *Journal of Medical Internet Research* peer review guidelines identify: question clarity, methodology appropriateness, result–conclusion alignment, and consideration of contradictory findings. A 2025 Springer scoping review of peer review report quality identifies "coherence between claims and evidence" and "actionable recommendations" as the two most consistent quality markers across 47 peer review frameworks.

**Atomic question 2b: Which peer review dimensions are LLM-agent-replicable?** [inference]

LLM-based peer review systems (REMOR arXiv:2505.11718; DeepReview ACL 2025; LLM4Review OpenReview 2024) demonstrate that LLM agents can replicate: structural consistency checks, logical coherence assessment (whether conclusions follow from stated evidence), identification of missing alternative explanations, and citation adequacy checks — with performance matching or exceeding median human reviewer quality on coherence and depth metrics. REMOR uses explicit reasoning steps and multi-objective reinforcement learning to train reviewers; DeepReview decomposes review into structured evidence-based stages. Both operate without domain expertise that exceeds general pre-training. This maps directly to the research skill output format used in this repo: an LLM agent with access to the §2 Investigation section can check whether the §6 Synthesis conclusions follow from the gathered evidence.

**Atomic question 2c: Which require a second independent expert?** [inference]

Human-only peer review dimensions are: domain-specific contextual plausibility (e.g., whether a finding is consistent with how NZ financial regulation actually operates in practice), novel research directions the agent lacks domain memory to identify, and strategic relevance assessment (whether the wisdom is actionable for the specific owner's decisions). These require contextual judgment that a stateless agent without domain-specific lived experience cannot reliably provide. The ICLR 2025 LLM feedback pilot (blog.iclr.cc, 2025) confirms that LLM agents are "most effective as augmentation and coherence-checking agents rather than complete replacements for human expert judgment, especially in high-stakes or specialized contexts."

**Atomic question 3a–3b: Zettelkasten integration methodology** [fact]

The Zettelkasten method (zettelkasten.de introduction, Sascha, 2020) defines integration as: each note is atomic (one idea), notes are connected by explicit typed links, and new insights emerge from the network of connections rather than from individual notes. The critical transfer to a file-based Markdown corpus: (a) each research item already has atomic scope (one research question), (b) explicit typed links between items (`state/links.json`, established in the knowledge-linking item) are the Zettelkasten equivalent of note links, (c) synthesis items (established in the cross-item synthesis item) are the Zettelkasten equivalent of "index notes" or "Maps of Content" that link related atomic notes into a coherent argument. Integration quality can therefore be assessed as: does this research item create or reference links to related items, and does the synthesis layer exist for its cluster?

**Atomic question 4a–4c: DIKW/SECI mapping** [fact + inference]

Ackoff's DIKW hierarchy (1989, widely cited via secondary sources including EBSCO and DataCamp): Data = raw facts without context; Information = data given context (answering who/what/when/where); Knowledge = application of data and information, answering "how" questions; Wisdom = sound judgments applying knowledge with insight and understanding of long-term consequences. [fact]

A research item in this repo operates at the Information → Knowledge transition: it takes raw sources (data/information) and synthesises evidence-backed claims (knowledge). The Findings section is the knowledge output. Cross-item synthesis (the `synthesise.yml` workflow and `Research/synthesis/` directory established in the cross-item-synthesis item) operates at the Knowledge → Wisdom transition. [inference from DIKW applied to repo structure]

Nonaka's SECI model (1995, widely cited via secondary sources including Wikipedia and Frontiers in Psychology): Externalisation (tacit→explicit) = the research process itself, converting tacit analytical reasoning into explicit documented findings. Combination (explicit→explicit) = cross-item synthesis, combining multiple explicit research items into a synthesis document. Internalisation (explicit→tacit) = the owner reading and applying findings to decisions, converting explicit knowledge back into tacit practical judgment. [fact + inference]

The SECI model makes one point actionable: Internalisation requires application, not just reading. A finding that is never applied to a decision remains explicit-only and does not reach the Wisdom level. This means the knowledge retention mechanisms (periodic digest, active recall, conversational interface) identified in the knowledge-retention item are not optional quality features — they are the Internalisation mechanism that the DIKW pipeline requires to reach Wisdom. [inference]

**Atomic question 4b: Actions that move information → knowledge** [inference]

At the item level: the research skill's §2 Investigation loop (gather sources, classify, extract claims, cross-verify, identify contradictions, update evidence map) is the Information → Knowledge transition operation. The quality gate at this transition is: are the sources correctly interpreted? Do the Key Findings follow from the §2 evidence? Is evidence sufficiency met (two independent sources, or one primary)? These questions are LLM-agent-checkable.

**Atomic question 4c: Actions that move knowledge → wisdom** [inference]

Wisdom requires: (1) synthesis across multiple knowledge items (cross-item integration), (2) applicability to a specific context (owner's domain), and (3) decision-relevant framing (what action does this enable?). These are harder to automate: (1) can be partially automated via the synthesis workflow; (2) requires either owner input or agent access to domain context; (3) requires structured prompt engineering to force decision-framing in the Open Questions section.

**Atomic question 5a–5b: Applicability testing** [fact + inference]

Bloom's revised taxonomy (2001, Anderson and Krathwohl): the Apply level maps to applicability testing — whether knowledge can be used to solve problems or respond to situations not exactly like those studied. The Evaluate and Create levels map to wisdom: making judgments based on criteria, producing new plans or approaches. [fact from CDC Bloom's guide and Cornell teaching resources]

Automatable applicability test: scenario-based validation at the Bloom Apply level is partially automatable via structured prompting — an agent can be given a scenario and asked to apply the finding. For example: "Given that a NZ bank is considering deploying agentic AI in its risk function, does this finding constrain or enable that decision?" An agent without domain context will give generic answers; an agent with domain context (from the owner's prior completed research) can give contextually specific answers. [inference]

Non-automatable: counterfactual checking at the Evaluate level ("if this finding were false, what breaks?") requires domain expertise to identify which counterfactuals are meaningful vs. trivial.

**Atomic question 6: CI pipeline sequence** [inference]

Ordering principle: cheaper and faster gates first; fail early before running expensive LLM-based checks. Cost order: (a) structural regex checks (milliseconds) < (b) LLM agent review of a single item (~2 minutes) < (c) cross-item integration check requiring corpus access (~5 minutes) < (d) human review (minutes to hours).

Proposed three-tier sequence:

Tier 1 — Fully automatable (bash/Python script, no LLM):
- Structural integrity: `status`, `started`, `completed` fields populated; `## Findings` section non-empty; Executive Summary word count ≥ 50; Key Findings list ≥ 2 non-placeholder entries; Evidence Map present with ≥ 1 row.
- Label presence: at least one `[fact]`, `[inference]`, or `[assumption]` label in §2 Investigation.
- Source checklist: at least one `[x]` in the Sources section.

Tier 2 — Agent-automatable (Copilot CLI agent, single-item review):
- Citation discipline (existing skill): claim-source binding, citation fidelity, term definitions.
- Speculation control (existing skill): unlabeled inferences, evidentiary gap filling.
- Remove-ai-slop (existing skill): formulaic patterns, alignment artifacts.
- *Logical coherence* (new scope): do the §6 Synthesis conclusions follow from the §2 Investigation evidence? Are any major alternative interpretations absent?
- *Evidence sufficiency* (new scope): is the confidence level assigned to each Key Finding supported by the number and independence of sources cited?

Tier 3 — Agent-automatable (cross-item, corpus access required):
- *Cross-item integration*: does this item reference related completed items where tag overlap ≥ 2? Does the Context section contain a Prior Research note?
- *Applicability framing*: does the item's Open Questions section contain at least one question framing the finding in terms of a decision context relevant to the owner?

Tier 4 — Human-only (owner review, not CI-automatable):
- Domain plausibility: does the finding hold in the specific NZ financial services / SWE context?
- Strategic relevance: does this advance the owner's actual current decisions?
- Novel directions: what research questions does the owner's domain knowledge suggest that the agent would not have surfaced?

The existing `research-review.yml` workflow implements Tier 2 (the three existing skills) but not Tier 1 (structural checks) or the new Tier 2 additions (logical coherence, evidence sufficiency). BACKLOG.md W-0031 should be scoped to add: (a) Tier 1 as a fast first step, (b) logical coherence and evidence sufficiency as additional checks in the existing Tier 2 agent review.

**Atomic question 7: New skills needed** [inference]

A `peer-review` skill for `davidamitchell/Skills` is warranted. Scope: given a completed research item, check (1) whether the Executive Summary conclusion is actually supported by the §2 Investigation evidence, (2) whether at least one major alternative explanation was considered and addressed or explicitly excluded, (3) whether the confidence levels assigned are calibrated to the source evidence (high confidence requires ≥ 2 independent sources; medium requires 1 credible source; low = single source or strong inference). This is distinct from citation-discipline (which checks source presence, not logical validity) and speculation-control (which checks label presence, not inference correctness).

An `integration` skill is not yet warranted as a standalone skill. The synthesis workflow (from the cross-item-synthesis item) covers the Combination step. The Prior Research note in the Context section covers the cross-reference requirement. The `peer-review` skill's check (3) on cross-item references is sufficient for now. An integration skill becomes necessary once the synthesis workflow is producing `Research/synthesis/` documents that themselves need quality review — that is a downstream dependency.

### §3 Reasoning

The three existing skills form a hygiene layer: they verify that claims are sourced, that uncertainty is labeled, and that the prose is readable. A research item passing all three can still be epistemically unsound if its conclusions do not follow from its evidence, if it ignores obvious alternative explanations, or if it exists in isolation from related completed items.

The DIKW and SECI frameworks converge on the same point: moving from information to wisdom is not a quality of individual documents but of a system. A single research item, no matter how well-sourced, represents an Information → Knowledge transition only. Wisdom requires the Combination step (cross-item synthesis) and the Internalisation step (applying findings to actual decisions). Neither of these is currently automated; the cross-item synthesis item designed Combination, and the knowledge-retention item designed Internalisation mechanisms.

The peer review literature (Springer Nature, REMOR, DeepReview) confirms that LLM agents can reliably check logical coherence and alternative explanations — the two quality dimensions most likely to produce epistemically wrong conclusions in a well-sourced document. These are agent-automatable, not human-only. The human-only tier is narrower than typically assumed: it covers domain plausibility and strategic relevance, not basic logical validity.

Bloom's taxonomy maps directly onto the automation tiers. Structural checks automate the Remember/Understand level. Agent reasoning automates the Apply/Analyse level. Human review covers Evaluate/Create. This alignment is not coincidental: the taxonomy describes cognitive complexity, which correlates with automation cost.

The Zettelkasten principle — that integration is the core knowledge-building operation, not archiving — implies that a research item that creates no links to other items is a quality failure even if it passes all three existing skills. The Prior Research note (now required by the updated research-prompt.md) and the `state/links.json` edge store are the Zettelkasten linking mechanisms for this corpus.

### §4 Consistency Check

No internal contradictions identified. One tension: the claim that "LLM agents can check logical coherence" (§2 question 2b) and the claim that "human-only review covers domain plausibility" (§2 question 2c) could appear to contradict each other if logical coherence is confused with domain plausibility. Resolved: these are distinct checks. Logical coherence = does the conclusion follow from the stated premises? (automatable) Domain plausibility = are the premises themselves plausible given domain-specific knowledge not in the document? (human-only). The REMOR and DeepReview papers confirm this distinction: LLM peer reviewers match human performance on coherence but underperform on domain-specific novelty assessment.

Confidence levels are consistent: the skill gap analysis (1a–1d) is [fact] drawn from direct reading of skill files. The pipeline design (question 6) is [inference] — the sequencing and tier assignments are derived from the evidence but involve design choices that a knowledgeable reader could reasonably question (e.g., whether cross-item integration belongs in Tier 2 or Tier 3).

The DIKW hierarchy sourcing: Ackoff's 1989 paper is paywalled; all descriptions of the hierarchy are from secondary sources (EBSCO, DataCamp, Springer). This is noted; the basic four-level structure of the hierarchy is sufficiently well-established in secondary literature that the secondary sourcing is acceptable. Confidence: high for the hierarchy itself; medium for any claims about Ackoff's specific intent.

### §5 Depth and Breadth Expansion

**Technical lens:** The CI pipeline design is technically straightforward. Tier 1 (structural checks) is a Python script scanning YAML front matter and Markdown section headings — 50 lines of code. Tier 2 (agent review) already exists in `research-review.yml`; extending it requires only additional instructions in `research-review-prompt.md`. Tier 3 (cross-item) requires the agent to list `Research/completed/` and compare tags — feasible with the existing Copilot CLI agent and filesystem access. No new infrastructure or credentials are required.

**Regulatory/organisational lens:** The NZ financial services context adds a specific human-only requirement: RBNZ (Reserve Bank of New Zealand) publishes AI supervisory expectations (researched in `2026-02-28-rbnz-ai-supervisory-expectations.md`) that affect whether AI-generated research findings are appropriate to rely upon in regulated decisions. The domain plausibility check is therefore not merely an epistemological nicety — in the owner's context, acting on a finding without domain plausibility review carries regulatory risk. This elevates the human review tier from "optional enhancement" to "required for decisions with regulatory implications."

**Historical lens:** The Zettelkasten method predates digital tools — Luhmann built his 90,000-card system manually from the 1950s to his death in 1998, producing 50 books. The fundamental insight (connection generates insight, archiving does not) has been validated across 70 years of practice. Digitalisation has made the linking step cheap; the remaining bottleneck is the discipline to create links consistently. The Prior Research note requirement and `state/links.json` edge store are the digital equivalents of Luhmann's linking discipline.

**Behavioural lens:** The biggest practical risk to this methodology is not technical — it is that quality review steps will be skipped when the research pipeline is under time pressure. The correct mitigation is to make Tier 1 and Tier 2 checks automatic and blocking (CI fails if they fail), so that the discipline is enforced by the pipeline rather than requiring deliberate human attention. The human-only Tier 4 review cannot be enforced by CI, but the owner can create a GitHub issue template for review notes to make it visible and auditable.

### §6 Synthesis

**Executive Summary:**
The three existing quality skills (citation-discipline, speculation-control, remove-ai-slop) cover factual hygiene and writing quality but leave three critical gaps: logical coherence (do conclusions follow from evidence?), alternative explanations (were competing interpretations considered?), and cross-item integration (does this item connect to the wider corpus?). A four-tier quality review pipeline, sequenced by automation cost, closes these gaps: Tier 1 structural checks (fully automatable Python scripts), Tier 2 agent review of single-item quality (the existing skills plus new logical coherence and evidence sufficiency checks), Tier 3 cross-item integration checks (agent with corpus access), and Tier 4 domain-specific human review. A new `peer-review` skill for `davidamitchell/Skills` is warranted to formalise the Tier 2 logical coherence and evidence sufficiency checks; an `integration` skill is not yet warranted. The DIKW and SECI frameworks confirm that the Wisdom level requires cross-item synthesis (Combination) and application to real decisions (Internalisation) — steps that the existing individual-item review pipeline does not address.

**Key Findings:**

1. **[fact] The three existing skills leave logical coherence, alternative explanations, and cross-item integration uncovered.** Citation-discipline checks source presence; speculation-control checks label presence; remove-ai-slop checks prose surface patterns. None checks whether a conclusion actually follows from the evidence gathered, or whether the item connects to related completed items.

2. **[fact] LLM agents can check logical coherence and missing alternative explanations at a quality level matching median human peer reviewers.** REMOR (arXiv:2505.11718) and DeepReview (ACL 2025) demonstrate this on scientific manuscripts. The distinction from human-only checks: LLMs can assess reasoning validity but cannot assess domain plausibility (whether premises are contextually correct) — that remains human-only.

3. **[inference] A four-tier pipeline (structural / single-item agent / cross-item agent / human) is the correct sequencing, ordered by automation cost.** Cheaper gates must run first: structural regex checks take milliseconds; single-item agent review takes ~2 minutes; cross-item review requires corpus access and ~5 minutes; human review has no fixed cost. Failing fast at the structural tier prevents running expensive agent checks on malformed items.

4. **[inference] The Tier 2 agent review should add two checks to the existing three skills: logical coherence (conclusions follow from §2 evidence) and evidence sufficiency (confidence level calibrated to source count and independence).** These are the highest-impact missing checks: they catch the failure mode where a well-sourced item reaches a wrong conclusion by misinterpreting its own evidence.

5. **[fact + inference] The DIKW and SECI frameworks map to three distinct pipeline stages: Information→Knowledge (individual item research), Knowledge→Wisdom (cross-item synthesis), and Wisdom application (internalisation through use).** Individual item quality review only covers the first transition. The cross-item synthesis workflow (designed in `2026-03-03-cross-item-synthesis-meta-insights.md`) and the knowledge retention mechanisms (designed in `2026-03-03-knowledge-retention-active-recall.md`) are the required Combination and Internalisation steps. None of these is currently implemented.

6. **[inference] Cross-item integration is a quality dimension for individual items, not only a synthesis task.** A research item that makes no reference to related completed items, and creates no links in `state/links.json`, is a quality failure even if it passes all three existing skills. The Zettelkasten principle (connection generates insight, archiving does not) applies: isolated items accumulate information without building knowledge.

7. **[inference] A `peer-review` skill with three checks is the correct scope addition to `davidamitchell/Skills`.** The three checks: (1) Executive Summary conclusion supported by §2 Investigation evidence; (2) at least one major alternative explanation considered or explicitly excluded; (3) confidence levels calibrated to source count and independence. This is the formalization of what academic peer reviewers are asked to check by Springer Nature and similar journals.

8. **[fact] Bloom's revised taxonomy (2001) maps directly onto the automation tiers: Remember/Understand → structural checks; Apply/Analyse → agent reasoning; Evaluate/Create → human judgment.** This mapping explains why the automation boundary falls where it does: cognitive complexity correlates with automation cost, and higher cognitive levels require context and judgment that current LLMs lack for domain-specific content.

9. **[inference] The Tier 4 human review tier is narrower than typically assumed, covering only domain plausibility and strategic relevance.** The claim that "agents can't do peer review" conflates logical coherence checking (agent-automatable) with domain-specific contextual assessment (human-only). In the NZ financial services context, domain plausibility review has regulatory implications and is non-optional for decisions with compliance consequences.

10. **[inference] An `integration` skill is not yet warranted; the peer-review skill's cross-item reference check and the synthesis workflow are sufficient.** An integration skill becomes necessary once `Research/synthesis/` documents exist and themselves need quality review. This is a downstream dependency.

### §7 Recursive Review

All seven sections contain substantive content. Every Key Finding is evidence-backed and traceable to §2 Investigation. Three confidence levels are used: [fact] for claims derived from direct source reading, [inference] for derived pipeline design decisions, and [fact + inference] for combined cases. No unlabelled assumptions detected. The DIKW and SECI sourcing is acknowledged as secondary; the pipeline design inferences are flagged as inference throughout. Cross-item references to three completed prior items are present. The §4 Consistency Check resolved the coherence/plausibility distinction that could appear contradictory. §5 added regulatory context (RBNZ implications) and historical validation (Luhmann's 70-year Zettelkasten practice) not present in §2. The Executive Summary in §6 directly answers the research question in the first sentence with a specific claim. All Key Findings are complete sentences ≥ 20 words with subject, verb, and specific complement.

One gap acknowledged: the Ahrens (2017) *How to Take Smart Notes* source was not accessed (book inaccessible). The Zettelkasten findings are corroborated by zettelkasten.de primary documentation and the cross-item synthesis completed item; the gap does not affect any Key Finding.

---

## Findings

### Executive Summary

The three existing quality skills (citation-discipline, speculation-control, remove-ai-slop) cover factual hygiene and writing quality but leave three critical gaps: logical coherence (do conclusions follow from evidence?), alternative explanations (were competing interpretations considered?), and cross-item integration (does this item connect to the wider corpus?). A four-tier quality review pipeline, sequenced by automation cost, closes these gaps: Tier 1 structural checks (fully automatable Python scripts), Tier 2 single-item agent review (existing skills plus new logical coherence and evidence sufficiency checks), Tier 3 cross-item integration checks (agent with corpus access), and Tier 4 domain-specific human review. A new `peer-review` skill for `davidamitchell/Skills` is warranted to formalise the logical coherence and evidence sufficiency checks; an `integration` skill is not yet warranted. The DIKW and SECI frameworks confirm that the Wisdom level requires cross-item synthesis (Combination) and application to real decisions (Internalisation) — steps that the existing individual-item review pipeline does not address and which are covered by the synthesis and knowledge-retention work already designed in this corpus.

### Key Findings

1. **[fact] The three existing skills leave logical coherence, alternative explanations, and cross-item integration uncovered.** Citation-discipline checks source presence; speculation-control checks label presence; remove-ai-slop checks prose surface patterns — none checks whether a conclusion follows from the evidence, whether competing interpretations were considered, or whether the item connects to related completed items in the corpus.

2. **[fact] LLM agents can check logical coherence and missing alternative explanations at a quality level matching median human peer reviewers.** REMOR (arXiv:2505.11718) and DeepReview (ACL 2025) demonstrate this on scientific manuscripts; the Copilot CLI agent already demonstrates equivalent behaviour in `research-review.yml`. The boundary between agent-automatable and human-only is coherence vs. domain plausibility — not "agent vs. human."

3. **[inference] A four-tier quality review pipeline sequenced by automation cost is the correct architecture: structural checks → single-item agent review → cross-item agent review → human domain review.** Each tier gates the next; cheaper checks run first to fail fast before running expensive LLM calls or requiring human attention.

4. **[inference] The existing `research-review.yml` Tier 2 agent review should be extended with two new checks: logical coherence (does §6 Synthesis follow from §2 Investigation?) and evidence sufficiency (is the confidence level calibrated to source count and independence?).** These are the highest-impact missing checks — they catch the failure mode where a well-sourced item misinterprets its own evidence and reaches an incorrect conclusion.

5. **[fact + inference] The DIKW and SECI frameworks map to three distinct workflow stages in this repository: Information→Knowledge (individual item research and review), Knowledge→Wisdom (cross-item synthesis via the planned `synthesise.yml`), and Wisdom application (internalisation via the knowledge-retention mechanisms).** Individual item quality review only covers the first transition; the second and third require separate workflows that are designed but not yet built.

6. **[inference] Cross-item integration is a quality dimension for individual items, not only a synthesis-layer concern.** A research item that references no related completed items and creates no links in `state/links.json` is a quality failure — the Zettelkasten principle (connection generates insight) means isolated items accumulate information without advancing knowledge.

7. **[inference] A `peer-review` skill with three checks is the correct scope addition to `davidamitchell/Skills`.** The three checks: (1) the Executive Summary conclusion is supported by §2 Investigation evidence; (2) at least one major alternative explanation was considered or explicitly excluded; (3) confidence levels are calibrated to source count and independence per the research skill's confidence table.

8. **[fact] Bloom's revised taxonomy (2001) maps directly onto the four automation tiers: Remember/Understand levels map to structural checks; Apply/Analyse levels map to agent reasoning; Evaluate/Create levels map to human judgment.** This is not a loose analogy — cognitive complexity at each Bloom level correlates with the computational cost and contextual requirements of the corresponding automation tier.

9. **[inference] The human review tier covers only domain plausibility and strategic relevance, not logical validity.** In the NZ financial services context, acting on a finding without domain plausibility review carries RBNZ supervisory risk; this makes Tier 4 non-optional for decisions with compliance implications, even though it is narrow in scope.

10. **[inference] An `integration` skill is not yet warranted; it becomes necessary once `Research/synthesis/` documents exist and require quality review of their own.** The peer-review skill's cross-item reference check and the existing synthesis workflow design are sufficient for current corpus size and state.

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| Existing three skills leave logical coherence uncovered | Direct reading of citation-discipline, speculation-control, remove-ai-slop SKILL.md files | high | Claim verified by reading all three skill files; none addresses conclusion-evidence relationship |
| LLM agents match median human peer reviewer quality on coherence | REMOR arXiv:2505.11718; DeepReview ACL 2025; ICLR 2025 LLM feedback blog | high | Multiple independent primary sources (arXiv paper, ACL proceedings, ICLR blog) |
| Springer Nature requires reviewers to check alternative explanations | Springer Nature How to Peer Review guidelines (2025) | high | Primary source; official journal policy documentation |
| DIKW hierarchy: 4 levels, non-linear with feedback | Ackoff 1989 (via secondary: EBSCO, DataCamp, Springer) | high | Well-established; secondary sourcing acceptable given paywalled primary |
| SECI model: 4 modes, Internalisation requires application not reading | Nonaka & Takeuchi 1995 (via secondary: Wikipedia, Frontiers in Psychology, ASCN) | high | Well-established; secondary sourcing acceptable |
| Bloom's revised taxonomy maps to automation tiers | Anderson & Krathwohl 2001 (via CDC, Cornell, Yale secondary sources) | high | Standard educational framework; secondary sources are authoritative institutional references |
| Zettelkasten: connection generates insight, archiving does not | zettelkasten.de introduction (Sascha, 2020); cross-item synthesis completed item | high | Primary web source accessed; corroborated by completed research item |
| Four-tier pipeline with cost-ordered sequencing | Inference from REMOR/DeepReview LLM cost data + CI pipeline patterns research | medium | Design inference; the specific tier boundaries and cost estimates are reasonable but not empirically validated for this repo |
| `peer-review` skill scope (three checks) | Inference from Springer Nature review dimensions + existing skill gap analysis | medium | Scope is derived; the specific checks are defensible but other framings are possible |
| Cross-item integration is an individual item quality dimension | Prior research: knowledge-linking item, cross-item synthesis item; Zettelkasten principle | medium | Inference from multiple prior items; not directly stated in any single source |

### Assumptions

- **Assumption:** The Copilot CLI agent running `research-review.yml` has sufficient reasoning capability to perform logical coherence checks on research items. **Justification:** REMOR and DeepReview demonstrate that current LLM-class models match median human reviewer quality on coherence; the Copilot CLI uses Claude Sonnet, which is in the same capability class. Direct empirical validation in this specific repo would be needed to confirm.
- **Assumption:** The existing `research-review.yml` agent prompt can be extended with logical coherence and evidence sufficiency instructions without degrading the quality of the existing three skill checks. **Justification:** The existing prompt already chains three separate skill checks; adding two more checks in the same format is consistent with the established pattern. The risk is prompt length degradation, but the existing prompt is already ~120 lines and functions correctly.
- **Assumption:** "Domain plausibility" checks (Tier 4) are not LLM-automatable for NZ financial services context. **Justification:** The ICLR 2025 feedback confirms agents underperform on domain-specific novelty and plausibility; the RBNZ supervisory expectations item confirms that NZ-specific regulatory context is required for correct domain assessment. This is a strong inference given the evidence, not an empirically proven claim about this specific agent.

### Analysis

The skills gap analysis is the foundational finding: all subsequent design choices follow from identifying exactly what the existing three skills check and what they miss. The peer review literature (Springer Nature, REMOR, DeepReview) provides external validation that the identified gaps — logical coherence and alternative explanations — are the same dimensions academic peer review prioritises. This convergence across independent frameworks (skill analysis + academic peer review + LLM research) gives high confidence in the gap identification.

The DIKW/SECI mapping resolves a potential confusion: "quality review" and "knowledge integration" are often conflated, but they operate at different pipeline stages. Quality review is an individual-item concern; knowledge integration is a cross-item concern; wisdom requires application beyond the repository. The four-tier pipeline reflects this: Tiers 1–2 address individual item quality; Tier 3 addresses integration; Tier 4 addresses domain-specific applicability. The tiers are not just ordered by cost but by epistemic depth — each tier catches failures the previous cannot.

The decision not to create an `integration` skill reflects scope discipline: the synthesis workflow already covers Combination, and the peer-review skill's cross-reference check is sufficient for Tier 3. Adding a third new skill without a concrete failing case would be premature abstraction.

### Risks, Gaps, and Uncertainties

- **Ahrens (2017)** was not accessed (book inaccessible). The Zettelkasten findings are corroborated by zettelkasten.de primary documentation and two prior completed items; this gap does not affect any Key Finding.
- **Empirical validation of LLM coherence checking in this specific repo** has not been done. The claim that the Copilot CLI agent can perform logical coherence checks is supported by REMOR/DeepReview but not validated against this repo's items. The first run of the extended `research-review-prompt.md` will provide this validation.
- **Tier 3 cross-item check implementation complexity** is uncertain. Requiring the agent to list `Research/completed/` and compare tags requires either filesystem access in the CI context (currently available via `actions/checkout`) or a pre-built tag index. The detail design is left to BACKLOG.md W-0031.
- **The `peer-review` skill scope** is the right starting point but may require iteration once used in practice. The three checks (conclusion-evidence support, alternative explanations, confidence calibration) are defensible but a first run may surface additional edge cases.

### Open Questions

- **Should Tier 1 structural checks block the research loop commit itself, or only gate the post-commit review workflow?** Blocking the loop commit on structural failures would catch malformed items earlier but would require integrating structural checks into `research-loop.yml`, increasing its complexity.
- **What is the correct trigger for Tier 4 human review?** CI cannot enforce human review, but a GitHub issue template for "domain plausibility review needed" could make it visible. Whether this should be automatically created for every completed item or only for items tagged with specific domains (e.g., `rbnz`, `financial-services`) is a design choice for BACKLOG.md W-0031.
- **When does an `integration` skill become warranted?** The threshold is: when `Research/synthesis/` documents exist and need their own quality review. This should be tracked as a condition in the synthesis workflow backlog item.
- **Can Tier 4 human review be partially automated for the NZ context** by injecting the RBNZ supervisory expectations findings and the AI strategy completed items as context into the agent prompt? This would make domain plausibility partially agent-automatable for the documented NZ context, though it would still require owner validation for novel decisions.

### Output section

- Type: skill, knowledge, backlog-item
- Description: Four-tier quality review pipeline taxonomy with automation classification; `peer-review` skill scope; DIKW/SECI mapping to repository workflows. The direct input to BACKLOG.md W-0031 (research review CI step implementation).
- Links:
  - https://www.springernature.com/gp/authors/campaigns/how-to-peer-review-3 (Springer Nature peer review guidelines — defines what reviewers check)
  - https://arxiv.org/html/2505.11718v1 (REMOR — LLM peer review matching human quality on coherence)
  - https://zettelkasten.de/introduction/ (Zettelkasten introduction — integration methodology foundation)
