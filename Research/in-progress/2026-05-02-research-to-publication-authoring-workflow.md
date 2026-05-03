---
review_count: 1
title: "What structured approaches and Artificial Intelligence (AI) agent workflow patterns best convert synthesised research findings into polished papers and practical frameworks, and what are the critical failure modes of research-to-publication pipelines?"
added: 2026-05-02T06:11:10+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, llm, workflow, evaluation, hallucinations]
started: 2026-05-03T07:33:40+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-02-systematic-review-methodology-ai-synthesis, 2026-05-02-automated-claim-verification-academic-literature, 2026-04-29-knowledge-scaffolding-context-engineering, 2026-03-10-dikw-transformation-functions, 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp]
related: [2026-04-27-uelgf-synthesis-complete-framework, 2026-05-02-cross-item-synthesis-knowledge-map-architecture, 2026-05-02-adversarial-review-methods-ai-research-quality]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What structured approaches and Artificial Intelligence (AI) agent workflow patterns best convert synthesised research findings into polished papers and practical frameworks, and what are the critical failure modes of research-to-publication pipelines?

## Research Question

What structured approaches, from academic writing pedagogy, Artificial Intelligence (AI)-assisted writing tools, and agent workflow design, exist for converting synthesised research findings into polished papers and practical decision frameworks, what Data-Information-Knowledge-Wisdom (DIKW) chain steps are typically skipped or corrupted in AI-assisted research-to-publication pipelines, and what `authoring-prompt.md` design and `authoring-loop.yml` workflow structure best support producing a finished paper or framework artifact from specified synthesis and primary research items while avoiding the most critical failure modes?

## Scope

**In scope:**
- Academic writing structure: standard paper templates, including IMRaD (Introduction, Methods, Results, and Discussion), argument essay, policy brief, decision framework, and capability maturity model, plus when each output type is appropriate
- AI-assisted writing tools: Elicit, Semantic Scholar, Paperpal, and Generative Pre-trained Transformer 4 (GPT-4)-class writing assistants, plus the workflow stages they support and the controls they expose
- DIKW chain gap analysis: where AI-assisted pipelines jump from retrieved information to recommendation or publication without an explicit knowledge-synthesis layer
- Failure mode survey: hallucinated citations, nuance loss, unsupported generalisation, inappropriate certainty, provenance loss, and review bottlenecks
- Authoring agent prompt design: how to require source-item reading, staged drafting, source-bound references, and post-generation checking
- Workflow design: `workflow_dispatch` trigger, input parameters, output structure, and automated review stages for authored outputs

**Out of scope:**
- Journal submission logistics and peer review administration
- Copyright and intellectual property analysis for AI-generated outputs
- Marketing, distribution, or publication-channel strategy
- Synthesis workflow design itself, which is covered by W-0051

**Constraints:**
- Expand all acronyms on first use
- The authoring workflow must be manual-trigger-only through `workflow_dispatch`
- Authored outputs must cite source items by slug, and the references section must be generated from `cites:` fields
- The design assumes synthesis items already exist and are trustworthy enough to serve as controlled inputs

## Context

W-0052 proposes an authoring workflow that turns primary and synthesis items into finished papers or frameworks, but the repository does not yet define the structure-selection, provenance, and verification rules needed to make that step reliable. [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md]

The decision risk is not only stylistic. A weak authoring workflow can turn well-grounded synthesis into persuasive but weakly supported recommendations by flattening nuance, losing traceability, or inventing references during the final drafting step. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md; https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/]

This item therefore asks for a design that routes the same evidence into the right output form, keeps the knowledge layer explicit before drafting, and adds enough review structure to preserve provenance without turning publication into an unbounded human bottleneck. [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md]

## Approach

1. **Structure survey:** compare IMRaD, policy brief, decision framework, and capability maturity model structures and map each to its best-fit evidence shape and audience.
2. **Tool architecture review:** examine how Elicit, Semantic Scholar, and Paperpal divide research gathering, screening, extraction, drafting, editing, and report generation.
3. **DIKW gap analysis:** identify which intermediate artifacts are required to move from evidence collection to defensible authored outputs.
4. **Failure mode survey:** catalogue the most damaging failure modes in AI-assisted academic and framework authoring.
5. **Prompt design:** derive a staged `authoring-prompt.md` pattern that forces source reading, outline generation, drafting, critique, and verification.
6. **Workflow design:** recommend `authoring-loop.yml` inputs, outputs, and review gates for a manual repository workflow.

## Sources

- [x] [University of British Columbia IMRaD](https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/) - accessible guidance on IMRaD section purpose and structure
- [x] [International Centre for Policy Advocacy Guide to Policy Briefs](https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf) - policy brief structure and audience orientation
- [x] [O'Regan (2022) Capability Maturity Model Integration](https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20) - maturity-model structure and staged improvement logic
- [x] [Elicit Systematic Reviews](https://support.elicit.com/en/articles/7927169) - stepwise evidence-gathering, screening, extraction, and report workflow
- [x] [Tannou et al. (2025) Using artificial intelligence for systematic review: the example of Elicit](https://link.springer.com/article/10.1186/s12874-025-02528-y) - peer-reviewed evaluation of Elicit as a complementary tool
- [x] [Semantic Scholar](https://www.semanticscholar.org/) - large-scale AI-powered academic search and discovery surface
- [x] [Paperpal](https://paperpal.com/) - end-to-end academic drafting, editing, and submission-readiness tooling
- [x] [Floridi et al. (2020) GPT-3: Its Nature, Scope, Limits, and Consequences](https://link.springer.com/article/10.1007/s11023-020-09548-1) - capabilities and limits of fluent text generation
- [x] [Bang et al. (2023) A Multitask, Multilingual, Multimodal Evaluation of ChatGPT on Reasoning, Hallucination, and Interactivity](https://arxiv.org/abs/2302.04023) - hallucination and reasoning limitations in general-purpose language models
- [x] [Fricke (2022) Data-Information-Knowledge-Wisdom Pyramid, Framework, Continuum](https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331) - accessible DIKW reference point and links to Ackoff and Rowley
- [x] [Chelli et al. (2024) Hallucination Rates and Reference Accuracy of ChatGPT and Bard for Systematic Reviews](https://www.jmir.org/2024/1/e53164) - empirical evidence on reference hallucination and retrieval accuracy
- [x] [Agrawal et al. (2024) Do Language Models Know When They're Hallucinating References?](https://aclanthology.org/2024.findings-eacl.62/) - consistency-check evidence for post-generation citation review
- [x] [Anthropic Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) - prompt chaining and evaluator-optimizer workflow patterns
- [x] [Anthropic Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - just-in-time context loading and minimal high-signal context design
- [x] [GitHub Docs on workflow_dispatch](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch) - manual workflow trigger and input support
- [x] [Mitchell (2026) Systematic review methodology for AI synthesis](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md) - provenance-preserving synthesis controls already selected for this corpus
- [x] [Mitchell (2026) Automated claim verification against academic literature](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md) - support-critical-claim verification loop for authored outputs
- [x] [Mitchell (2026) Knowledge scaffolding and context engineering](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md) - staged context-loading patterns relevant to authoring prompts
- [x] [Mitchell (2026) The DIKW pyramid: transformation functions](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md) - repository interpretation of data, information, knowledge, and wisdom transitions
- [x] [Mitchell (2026) Human-in-the-loop design under review-volume pressure](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md) - review bottleneck and selective oversight evidence

## Related

- [Mitchell (2026) Systematic review methodology for AI synthesis](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md)
- [Mitchell (2026) Automated claim verification against academic literature](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md)
- [Mitchell (2026) Knowledge scaffolding and context engineering](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: determine which structure choices, authoring stages, and review controls best convert synthesis outputs into publication-grade papers or practical frameworks without breaking provenance.
- Scope: output-type routing, AI-tool stage coverage, DIKW transition controls, failure modes, prompt design, workflow design, and review gates.
- Constraints: manual `workflow_dispatch` trigger, source-item citation by slug, acronym expansion on first use, and repository-compatible quality checks.
- Output: one knowledge item that recommends a staged `authoring-prompt.md` and `authoring-loop.yml` design.
- Prior completed items reviewed: [Systematic review methodology for AI synthesis](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md), [Automated claim verification against academic literature](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md), [Knowledge scaffolding and context engineering](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md), [The DIKW pyramid: transformation functions](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md), and [Human-in-the-loop design under review-volume pressure](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md).

### §1 Question Decomposition

- **A. Output-form selection**
  - A1. When is IMRaD the right structure?
  - A2. When is a policy brief the right structure?
  - A3. When is a decision framework or capability maturity model the right structure?
- **B. Tool-stage coverage**
  - B1. Which tools support search and screening?
  - B2. Which tools support drafting and editing?
  - B3. Where does no single tool provide trustworthy end-to-end publication?
- **C. DIKW control points**
  - C1. Which artifact turns retrieved information into explicit knowledge?
  - C2. Which jump produces unsupported wisdom-level recommendations?
- **D. Failure modes**
  - D1. Which authoring errors are most damaging?
  - D2. Which are most preventable with workflow structure?
- **E. Workflow design**
  - E1. What stages should `authoring-prompt.md` enforce?
  - E2. What inputs and outputs should `authoring-loop.yml` require?
  - E3. Which review steps must run before commit?

### §2 Investigation

#### Source checks and substitutions

- [assumption; source: https://support.elicit.com/en/articles/7927169; https://link.springer.com/article/10.1186/s12874-025-02528-y] Access note: the seeded Elicit `how-it-works` page was not accessible in this runtime, so downstream Elicit claims rely on accessible workflow documentation and peer-reviewed evaluation instead.
- [assumption; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20] Access note: the seeded Swales and Feak publisher catalog page does not carry the structural detail needed for support-critical claims, so output-structure claims rely on accessible IMRaD and maturity-model guidance instead.
- [assumption; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md] Access note: the seeded Atkinson and Claxton entry is not a DIKW-specific source, so DIKW claims below rely on Fricke's DIKW reference entry and the repository's completed DIKW item.

#### A. Output structures and fit

- [fact; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/] IMRaD is optimized for research communication where the reader needs a transparent account of context, method, results, and interpretation, and it explicitly separates evidential description from downstream discussion.
- [fact; source: https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf] Policy briefs are designed for decision audiences that need a concise statement of the problem, the policy relevance of the evidence, and actionable recommendations rather than a full method narrative.
- [fact; source: https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20; https://www.isaca.org/resources/reference-guide/cmmi-model-quick-reference-guide] Capability maturity models organize guidance as staged process improvement, with explicit maturity levels, process areas, and a roadmap for institutionalization rather than a one-off argument.
- [inference; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20] The authoring workflow should route outputs by decision need: use IMRaD when method transparency is central, use a policy brief when the audience needs compact action guidance, use a decision framework when the task is choosing among options, and use a maturity model when the task is sequencing organizational capability growth.

#### B. Tool architecture and stage coverage

- [fact; source: https://support.elicit.com/en/articles/7927169; https://link.springer.com/article/10.1186/s12874-025-02528-y] Elicit structures the review process as protocol setup, evidence gathering, screening, extraction, and report generation, and the peer-reviewed evaluation concludes that it is a valuable complementary tool rather than a replacement for rigorous human review.
- [fact; source: https://www.semanticscholar.org/] Semantic Scholar presents itself as an AI-powered discovery tool for literature search, ranking, and exploration rather than as a controlled end-to-end authoring pipeline.
- [fact; source: https://paperpal.com/] Paperpal positions itself as an academic drafting and editing assistant with contextual rewriting, reference support, multi-document reading, and submission-readiness checks inside writing environments.
- [inference; source: https://support.elicit.com/en/articles/7927169; https://www.semanticscholar.org/; https://paperpal.com/] These tools split the research-to-publication path into distinct layers, discovery, evidence handling, and prose refinement, which implies that the repository should orchestrate those layers explicitly rather than expect one product pattern to guarantee publication-quality outputs.

#### C. DIKW transition and missing artifacts

- [fact; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md] The DIKW model distinguishes retrieved or organized information from knowledge and from wisdom, and the completed DIKW item in this repository argues that the fragile transition is usually from information to knowledge and then from knowledge to value-directed judgment.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md] The repository's synthesis and context-engineering work already favors explicit claim extraction, evidence maps, staged context loading, and provenance-preserving summaries before long-form generation.
- [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md] The authoring artifact that prevents a DIKW shortcut is an explicit knowledge layer, for example a claim table, structured outline, or evidence map, because that layer forces the system to stabilize what the evidence says before it turns those claims into recommendations, framing, and rhetoric.

#### D. Failure modes in AI-assisted authoring

- [fact; source: https://www.jmir.org/2024/1/e53164] In a systematic-review retrieval task, GPT-4 achieved 13.4% precision and a 28.6% hallucination rate for references, which shows that fluent output quality is not a reliable proxy for bibliography reliability.
- [fact; source: https://aclanthology.org/2024.findings-eacl.62/] Agrawal et al. show that language models often reveal internal inconsistency when pressed about hallucinated references, which supports post-generation consistency checks rather than blind trust in the first draft.
- [fact; source: https://link.springer.com/article/10.1007/s11023-020-09548-1; https://arxiv.org/abs/2302.04023] Fluent language models can produce high-quality surface text while remaining unreliable reasoners and hallucinators, especially when they are asked to generate content without grounded external evidence.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/; https://link.springer.com/article/10.1007/s11023-020-09548-1] The most damaging research-to-publication failure modes are fabricated references, over-smoothed synthesis that erases disagreement, unsupported generalization from narrow evidence, and certainty drift introduced during the prose-polishing stage.

#### E. Workflow patterns for prompt and pipeline design

- [fact; source: https://www.anthropic.com/research/building-effective-agents] Prompt chaining is appropriate when a task decomposes cleanly into fixed substeps, and evaluator-optimizer loops are appropriate when quality improves through critique and revision.
- [fact; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents] Context engineering guidance recommends minimal high-signal context, explicit prompt sections, and just-in-time loading of source material rather than front-loading every available token.
- [fact; source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch] GitHub Actions supports manual `workflow_dispatch` triggers with structured inputs for workflow runs.
- [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch; https://www.anthropic.com/research/building-effective-agents] Manual dispatch is a better fit for authoring tasks than scheduled automation because title, audience, source-item set, and output form are deliberate user choices.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md] The repository's verification research recommends extracting support-critical claims, claims that a key finding directly depends on, retrieving direct evidence, and downgrading unsupported facts to inferences rather than leaving them unqualified.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md] The repository's human-review research shows that oversight becomes nominal when queues grow without risk tiering, sampling rules, or clear override surfaces.
- [inference; source: https://www.anthropic.com/research/building-effective-agents; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md] The best repository design is a staged manual workflow: load source items, extract claims and evidence, select an output template, draft from the structured outline, run critique and verification passes, then require a focused human check on support-critical claims and output-structure compliance.

### §3 Reasoning

- [inference; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20] Output selection is a routing problem, not a generic writing problem, because each format encodes a different contract about evidence presentation, decision support, and process maturity.
- [inference; source: https://support.elicit.com/en/articles/7927169; https://paperpal.com/; https://www.semanticscholar.org/] Tool review suggests a layered architecture rather than a monolith: discovery tools reduce search cost, structured-review tools stabilize evidence, and drafting tools improve readability but should not be trusted as evidence authorities.
- [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md] The DIKW failure point is the unrecorded jump from information to recommendation, because once the agent starts writing polished prose without a stable claim structure it becomes difficult to audit which sentence came from evidence and which came from rhetorical interpolation.
- [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/; https://www.anthropic.com/research/building-effective-agents] The right review design therefore targets the publication-stage risks directly: bibliography validation, support-critical-claim checking, and output-form conformity matter more than generic copy-editing.

### §4 Consistency Check

- [fact; source: https://support.elicit.com/en/articles/7927169; https://paperpal.com/; https://www.semanticscholar.org/] No reviewed tool contradicts the stage-splitting conclusion: Elicit emphasizes evidence workflow, Semantic Scholar emphasizes discovery, and Paperpal emphasizes drafting and editing.
- [fact; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/; https://link.springer.com/article/10.1007/s11023-020-09548-1] No reviewed source supports fully autonomous final publication without verification, and all support either direct caution or indirect caution about ungrounded fluent generation.
- [inference; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20] The structure-routing recommendation is internally consistent because it maps each output type to the rhetorical and procedural needs described by the corresponding format guidance.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md] From a technical lens, the authoring prompt should prefer just-in-time loading of source-item sections and claim tables rather than whole-file stuffing, because that keeps the active context aligned with the current drafting stage.
- [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch] From an operational lens, manual dispatch is a feature rather than a limitation because it forces explicit declaration of title, output type, audience, and source set before generation begins.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md] From a governance lens, the review step should be selective and claim-focused, because asking humans to review every sentence in every draft would recreate the throughput and rubber-stamping failure that this repository is already trying to avoid.
- [inference; source: https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20] From an organizational lens, framework outputs need explicit dimensions, stages, and transition criteria or they collapse into persuasive narrative rather than an operational model.

### §6 Synthesis

**Executive summary:**

An effective research-to-publication workflow should be staged, source-bound, and output-routed rather than single-pass, because the dangerous jump is from synthesized information directly to polished recommendations without an explicit knowledge layer. [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://www.anthropic.com/research/building-effective-agents]
The best design for this repository is a manual `workflow_dispatch` authoring loop that first extracts claim-level evidence from specified items, then routes that evidence into the right template, drafts in stages, and runs verification before commit. [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
The most important failure modes are fabricated references, provenance loss, nuance flattening, and certainty drift during final prose generation, so bibliography and support-critical-claim checks must be first-class review gates rather than optional cleanup. [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/; https://link.springer.com/article/10.1007/s11023-020-09548-1]
Papers and frameworks should not share one generic prompt, because IMRaD, policy briefs, decision frameworks, and maturity models impose different evidence and audience contracts. [inference; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20]

**Key findings:**

1. **The strongest authoring pattern is a staged workflow that separates evidence loading, outline construction, drafting, critique, and verification, because each stage reduces a different publication risk that a single-pass draft cannot control.** ([inference]; medium confidence; source: https://www.anthropic.com/research/building-effective-agents; https://support.elicit.com/en/articles/7927169; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md)
2. **Output type should be selected by the audience's decision need and the evidence shape, with IMRaD fitting method-centered papers, policy briefs fitting action-oriented readers, decision frameworks fitting option choice, and maturity models fitting staged capability improvement.** ([inference]; medium confidence; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20)
3. **The reviewed AI research-writing tools cover different stages of the pipeline, with Elicit centered on evidence workflow, Semantic Scholar on discovery, and Paperpal on drafting and submission polish.** ([fact]; medium confidence; source: https://support.elicit.com/en/articles/7927169; https://www.semanticscholar.org/; https://paperpal.com/)
4. **The control that prevents a DIKW shortcut is an explicit knowledge artifact, such as a claim table or evidence-bound outline, because that artifact keeps the transition from retrieved information to recommendation auditable before rhetoric is added.** ([inference]; medium confidence; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)
5. **Generated bibliographies must be treated as untrusted until checked, because GPT-4 and Bard both showed poor reference precision and substantial hallucination rates in systematic-review retrieval experiments.** ([fact]; medium confidence; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/)
6. **Post-generation citation checks are worthwhile because language models often expose hallucinated references through internal inconsistency when asked follow-up questions about the cited work.** ([fact]; medium confidence; source: https://aclanthology.org/2024.findings-eacl.62/)
7. **A manual `workflow_dispatch` loop is preferable to scheduled authoring automation because authored outputs require explicit selection of title, audience, source items, and output form, and those choices materially shape what a valid artifact looks like.** ([inference]; medium confidence; source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch; https://www.anthropic.com/research/building-effective-agents)
8. **Framework outputs need stricter structural checks than papers, because a maturity model or decision framework without explicit dimensions, stage definitions, and progression criteria becomes persuasive narrative instead of an operational tool.** ([inference]; medium confidence; source: https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-uelgf-synthesis-complete-framework.md)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Staged authoring beats single-pass drafting for reliability and inspectability. | https://www.anthropic.com/research/building-effective-agents; https://support.elicit.com/en/articles/7927169; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md | medium | Stage decomposition aligns with prompt chaining and structured review practice. |
| [inference] Output structure should be routed by evidence shape and audience need. | https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20 | medium | Each format implies a different contract for evidence display and actionability. |
| [fact] The reviewed tools cover different workflow stages, with Elicit focused on evidence workflow, Semantic Scholar on discovery, and Paperpal on drafting and submission polish. | https://support.elicit.com/en/articles/7927169; https://www.semanticscholar.org/; https://paperpal.com/ | medium | Tool docs are product descriptions, not comparative benchmarks. |
| [inference] An explicit knowledge artifact is required between synthesis and publication. | https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md | medium | This is the central DIKW control point for authoring. |
| [fact] Generated references are unreliable enough to require mandatory checking. | https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/ | medium | JMIR gives empirical error rates, and Agrawal et al. support post-generation checking. |
| [fact] Consistency checks can reveal hallucinated references after generation. | https://aclanthology.org/2024.findings-eacl.62/ | medium | Helpful as a gate, not a substitute for evidence retrieval. |
| [inference] Manual dispatch is the correct trigger model for authoring. | https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch; https://www.anthropic.com/research/building-effective-agents | medium | Manual input quality matters more than automation frequency. |
| [inference] Framework outputs require stronger structural validation than papers. | https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-uelgf-synthesis-complete-framework.md | medium | Stage and dimension definitions are what make a framework operational. |

**Assumptions:**

- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md] Synthesis items supplied to the authoring loop already meet the repository's provenance and evidence standards closely enough to be treated as controlled inputs.
- [assumption; source: https://www.anthropic.com/research/building-effective-agents; https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch] The owner will provide output type, title, intended audience, and source-item slugs at workflow start rather than expect the workflow to infer them safely.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md] Selective human review focused on support-critical claims is feasible, while full line-by-line review of every authored output is not.

**Analysis:**

The evidence points away from a single magical writing assistant and toward a pipeline in which each stage has a different reliability profile. [inference; source: https://support.elicit.com/en/articles/7927169; https://www.semanticscholar.org/; https://paperpal.com/]
Search and screening tools reduce discovery cost, but they do not solve the later problem of turning evidence into defensible argument structure. [inference; source: https://support.elicit.com/en/articles/7927169; https://link.springer.com/article/10.1186/s12874-025-02528-y]
Drafting and editing tools improve fluency and submission readiness, but the literature on hallucinated references shows that fluency is exactly where trust can become dangerous. [inference; source: https://paperpal.com/; https://www.jmir.org/2024/1/e53164; https://link.springer.com/article/10.1007/s11023-020-09548-1]
That is why the best workflow inserts an explicit knowledge layer, routes into the right output template, and treats verification as a publication-stage control rather than an optional polish step. [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md]
Alternative remedies, such as relying on better base models or more human reviewers, do not eliminate the need for staged structure, because better fluent generation does not remove provenance risk and more review capacity still scales poorly without claim prioritization. [inference; source: https://www.jmir.org/2024/1/e53164; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md; https://www.anthropic.com/research/building-effective-agents]

**Risks, gaps, uncertainties:**

- Direct comparative evaluations across Elicit, Semantic Scholar, Paperpal, and other authoring tools are limited, so tool-stage conclusions rely partly on product documentation rather than head-to-head empirical benchmarks. [fact; source: https://link.springer.com/article/10.1186/s12874-025-02528-y; https://www.semanticscholar.org/; https://paperpal.com/]
- The DIKW hierarchy is a conceptual framework rather than a validated engineering law, so the proposed knowledge-layer control is best treated as a design heuristic that is strongly supported by adjacent workflow evidence rather than as a mathematically complete theory of publication quality. [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md]

**Open questions:**

- Should the future `authoring-loop.yml` support audience-specific variants inside one output type, for example board memo versus technical white paper?
- Should framework outputs receive a stronger schema validator than papers, for example required dimensions, levels, and transition criteria before commit?
- Should the repository generate both a short policy brief and a full paper from the same evidence bundle, or force one primary output per run?

### §7 Recursive Review

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-02-research-to-publication-authoring-workflow.md] Acronym sweep completed for AI, DIKW, IMRaD, GPT-4, and workflow-specific terms used in the document.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-02-research-to-publication-authoring-workflow.md] All visible claims in `## Findings` carry inline suffix labels and URL-backed sources.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-02-research-to-publication-authoring-workflow.md] `§6 Synthesis` and `## Findings` are aligned on wording, labels, confidence, and citations.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-05-02-research-to-publication-authoring-workflow.md] No em dashes remain in the document text.

---

## Findings

### Executive Summary

An effective research-to-publication workflow should be staged, source-bound, and output-routed rather than single-pass, because the dangerous jump is from synthesized information directly to polished recommendations without an explicit knowledge layer. [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://www.anthropic.com/research/building-effective-agents]
The best design for this repository is a manual `workflow_dispatch` authoring loop that first extracts claim-level evidence from specified items, then routes that evidence into the right template, drafts in stages, and runs verification before commit. [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents]
The most important failure modes are fabricated references, provenance loss, nuance flattening, and certainty drift during final prose generation, so bibliography and support-critical-claim checks must be first-class review gates rather than optional cleanup. [inference; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/; https://link.springer.com/article/10.1007/s11023-020-09548-1]
Papers and frameworks should not share one generic prompt, because IMRaD, policy briefs, decision frameworks, and maturity models impose different evidence and audience contracts. [inference; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20]

### Key Findings

1. **The strongest authoring pattern is a staged workflow that separates evidence loading, outline construction, drafting, critique, and verification, because each stage reduces a different publication risk that a single-pass draft cannot control.** ([inference]; medium confidence; source: https://www.anthropic.com/research/building-effective-agents; https://support.elicit.com/en/articles/7927169; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md)
2. **Output type should be selected by the audience's decision need and the evidence shape, with IMRaD fitting method-centered papers, policy briefs fitting action-oriented readers, decision frameworks fitting option choice, and maturity models fitting staged capability improvement.** ([inference]; medium confidence; source: https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20)
3. **The reviewed AI research-writing tools cover different stages of the pipeline, with Elicit centered on evidence workflow, Semantic Scholar on discovery, and Paperpal on drafting and submission polish.** ([fact]; medium confidence; source: https://support.elicit.com/en/articles/7927169; https://www.semanticscholar.org/; https://paperpal.com/)
4. **The control that prevents a DIKW shortcut is an explicit knowledge artifact, such as a claim table or evidence-bound outline, because that artifact keeps the transition from retrieved information to recommendation auditable before rhetoric is added.** ([inference]; medium confidence; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md)
5. **Generated bibliographies must be treated as untrusted until checked, because GPT-4 and Bard both showed poor reference precision and substantial hallucination rates in systematic-review retrieval experiments.** ([fact]; medium confidence; source: https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/)
6. **Post-generation citation checks are worthwhile because language models often expose hallucinated references through internal inconsistency when asked follow-up questions about the cited work.** ([fact]; medium confidence; source: https://aclanthology.org/2024.findings-eacl.62/)
7. **A manual `workflow_dispatch` loop is preferable to scheduled authoring automation because authored outputs require explicit selection of title, audience, source items, and output form, and those choices materially shape what a valid artifact looks like.** ([inference]; medium confidence; source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch; https://www.anthropic.com/research/building-effective-agents)
8. **Framework outputs need stricter structural checks than papers, because a maturity model or decision framework without explicit dimensions, stage definitions, and progression criteria becomes persuasive narrative instead of an operational tool.** ([inference]; medium confidence; source: https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-uelgf-synthesis-complete-framework.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Staged authoring beats single-pass drafting for reliability and inspectability. | https://www.anthropic.com/research/building-effective-agents; https://support.elicit.com/en/articles/7927169; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md | medium | Stage decomposition aligns with prompt chaining and structured review practice. |
| [inference] Output structure should be routed by evidence shape and audience need. | https://scwrl.ubc.ca/stem-writing-resources/features-of-academic-stem-research-writing/imrad/; https://icpolicyadvocacy.org/sites/default/files/2024-04/icpa-policy-briefs-essential-guide.pdf; https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20 | medium | Each format implies a different contract for evidence display and actionability. |
| [fact] The reviewed tools cover different workflow stages, with Elicit focused on evidence workflow, Semantic Scholar on discovery, and Paperpal on drafting and submission polish. | https://support.elicit.com/en/articles/7927169; https://www.semanticscholar.org/; https://paperpal.com/ | medium | Tool docs are product descriptions, not comparative benchmarks. |
| [inference] An explicit knowledge artifact is required between synthesis and publication. | https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-29-knowledge-scaffolding-context-engineering.md | medium | This is the central DIKW control point for authoring. |
| [fact] Generated references are unreliable enough to require mandatory checking. | https://www.jmir.org/2024/1/e53164; https://aclanthology.org/2024.findings-eacl.62/ | medium | JMIR gives empirical error rates, and Agrawal et al. support post-generation checking. |
| [fact] Consistency checks can reveal hallucinated references after generation. | https://aclanthology.org/2024.findings-eacl.62/ | medium | Helpful as a gate, not a substitute for evidence retrieval. |
| [inference] Manual dispatch is the correct trigger model for authoring. | https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch; https://www.anthropic.com/research/building-effective-agents | medium | Manual input quality matters more than automation frequency. |
| [inference] Framework outputs require stronger structural validation than papers. | https://link.springer.com/chapter/10.1007/978-3-031-07816-3_20; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-27-uelgf-synthesis-complete-framework.md | medium | Stage and dimension definitions are what make a framework operational. |

### Assumptions

- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md] Synthesis items supplied to the authoring loop already meet the repository's provenance and evidence standards closely enough to be treated as controlled inputs.
- [assumption; source: https://www.anthropic.com/research/building-effective-agents; https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch] The owner will provide output type, title, intended audience, and source-item slugs at workflow start rather than expect the workflow to infer them safely.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md] Selective human review focused on support-critical claims is feasible, while full line-by-line review of every authored output is not.

### Analysis

The evidence points away from a single magical writing assistant and toward a pipeline in which each stage has a different reliability profile. [inference; source: https://support.elicit.com/en/articles/7927169; https://www.semanticscholar.org/; https://paperpal.com/]
Search and screening tools reduce discovery cost, but they do not solve the later problem of turning evidence into defensible argument structure. [inference; source: https://support.elicit.com/en/articles/7927169; https://link.springer.com/article/10.1186/s12874-025-02528-y]
Drafting and editing tools improve fluency and submission readiness, but the literature on hallucinated references shows that fluency is exactly where trust can become dangerous. [inference; source: https://paperpal.com/; https://www.jmir.org/2024/1/e53164; https://link.springer.com/article/10.1007/s11023-020-09548-1]
That is why the best workflow inserts an explicit knowledge layer, routes into the right output template, and treats verification as a publication-stage control rather than an optional polish step. [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md]
Alternative remedies, such as relying on better base models or more human reviewers, do not eliminate the need for staged structure, because better fluent generation does not remove provenance risk and more review capacity still scales poorly without claim prioritization. [inference; source: https://www.jmir.org/2024/1/e53164; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md; https://www.anthropic.com/research/building-effective-agents]

### Risks, Gaps, and Uncertainties

- Direct comparative evaluations across Elicit, Semantic Scholar, Paperpal, and other authoring tools are limited, so tool-stage conclusions rely partly on product documentation rather than head-to-head empirical benchmarks. [fact; source: https://link.springer.com/article/10.1186/s12874-025-02528-y; https://www.semanticscholar.org/; https://paperpal.com/]
- The DIKW hierarchy is a conceptual framework rather than a validated engineering law, so the proposed knowledge-layer control is best treated as a design heuristic that is strongly supported by adjacent workflow evidence rather than as a mathematically complete theory of publication quality. [inference; source: https://link.springer.com/rwe/10.1007/978-3-319-32010-6_331; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-dikw-transformation-functions.md]

### Open Questions

- Should the future `authoring-loop.yml` support audience-specific variants inside one output type, for example board memo versus technical white paper?
- Should framework outputs receive a stronger schema validator than papers, for example required dimensions, levels, and transition criteria before commit?
- Should the repository generate both a short policy brief and a full paper from the same evidence bundle, or force one primary output per run?

---

## Output

- Type: knowledge
- Description: This item recommends a staged, manual, provenance-preserving authoring workflow for turning completed research items into papers or frameworks, with explicit structure routing and verification gates. [inference; source: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#onworkflow_dispatch; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://www.jmir.org/2024/1/e53164]
- Links:
  - https://support.elicit.com/en/articles/7927169
  - https://www.jmir.org/2024/1/e53164
  - https://www.anthropic.com/research/building-effective-agents
