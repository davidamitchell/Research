---
title: "What systematic review methodologies and Artificial Intelligence (AI)-assisted synthesis tool architectures are most appropriate for cross-item synthesis of a growing file-based research corpus, and what design prevents hallucination and claim conflation across source items?"
added: 2026-05-02T06:11:10+00:00
status: reviewing
priority: high  # low | medium | high
blocks: [2026-05-02-research-to-publication-authoring-workflow]  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [agentic-ai, llm, workflow, knowledge-graph, evaluation, hallucinations]
started: 2026-05-02T08:41:24+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-02-27-information-synthesis-entropy, 2026-03-03-cross-item-synthesis-meta-insights, 2026-03-03-knowledge-linking-connected-corpus]
related: [2026-03-12-exploration-synthesis-gap, 2026-04-26-systems-capability-debt-agentic-ai-risk-synthesis, 2026-04-27-uelgf-synthesis-complete-framework]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What systematic review methodologies and Artificial Intelligence (AI)-assisted synthesis tool architectures are most appropriate for cross-item synthesis of a growing file-based research corpus, and what design prevents hallucination and claim conflation across source items?

## Research Question

What systematic review methodologies, Preferred Reporting Items for Systematic reviews and Meta-Analyses (PRISMA), Cochrane review, narrative synthesis, meta-ethnography, and realist synthesis, and what Artificial Intelligence (AI)-assisted knowledge synthesis tool architectures are most appropriate for producing accurate, provenance-preserving cross-item synthesis from a growing file-based research corpus of about 200 items managed by AI agents? More specifically: what synthesis methodology best prevents hallucination and claim conflation across source items, what provenance-linking mechanism ensures each synthesis claim traces to specific source items, and what workflow design, GitHub Actions `workflow_dispatch`, agent prompt, and output directory structure, best delivers a `synthesis-prompt.md` and `synthesis-loop.yml` implementation for W-0051?

## Scope

**In scope:**
- Systematic review methodologies, PRISMA reporting guidance, Cochrane review workflow, narrative synthesis, meta-ethnography, and realist synthesis, and their fit for Large Language Model (LLM)-assisted corpus synthesis
- AI-assisted synthesis tools and patterns, Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking (STORM), LlamaIndex response synthesis, LangChain map-reduce summarization, and Elicit-assisted evidence synthesis
- Hallucination prevention controls, retrieval grounding, structured evidence extraction, citation verification, and contradiction handling
- Provenance-linking design for synthesis claims, including minimum claim record, evidence map, `cites:` field, and inline source binding
- Workflow design for W-0051, including `workflow_dispatch` inputs, `Knowledge/` output structure, `synthesis-prompt.md` section design, and Architecture Decision Record (ADR) triggers

**Out of scope:**
- Quantitative meta-analysis of effect sizes
- Automated source-item selection without owner input
- Full semantic search index design
- End-user authoring workflows that depend on synthesis outputs

**Constraints:**
- Expand all acronyms on first use
- The workflow must never run on schedule
- Every synthesis claim must be traceable to one or more source item slugs
- Any implementation must fit Python 3.11+ and GitHub Actions

## Context

W-0051 already specifies the desired implementation outcome, `Knowledge/`, `synthesis-prompt.md`, and a manual-only `synthesis-loop.yml`, but it does not yet specify the research methodology or provenance discipline that should govern those artifacts. [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

Prior completed work in this repository already identifies false-consensus risk in multi-source synthesis, the need for explicit link structure across items, and the earlier design space for corpus-level synthesis, so this item can focus on selecting a defensible method and control set rather than rediscovering the problem. [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md]

## Approach

1. **Systematic review methodology survey:** assess PRISMA, Cochrane, narrative synthesis, meta-ethnography, and realist synthesis against the needs of a heterogeneous file-based corpus.
2. **AI-assisted synthesis tool architecture review:** examine STORM, LlamaIndex, LangChain map-reduce, and Elicit for grounding, provenance retention, and failure modes.
3. **Hallucination prevention evidence:** identify which controls have the strongest support for reducing multi-document hallucination and claim conflation.
4. **Provenance-linking design:** define the minimum traceability record for a synthesis claim.
5. **Contradiction detection design:** define how conflicting source-item findings should be surfaced and handled.
6. **Workflow and prompt design:** recommend the `Knowledge/` structure, `synthesis-prompt.md` sections, and `synthesis-loop.yml` inputs.
7. **ADR identification:** identify which design decisions require formal architectural recording before W-0051 implementation.

## Sources

- [x] [Page et al. (2021) PRISMA 2020 explanation and elaboration: updated guidance and exemplars for reporting systematic reviews](https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/)
- [x] [McKenzie et al. (2024) Cochrane Handbook Chapter 3: Defining the criteria for including studies and how they will be grouped for the synthesis](https://training.cochrane.org/handbook/current/chapter-03)
- [x] [McKenzie et al. (2024) Cochrane Handbook Chapter 9: Summarizing study characteristics and preparing for synthesis](https://training.cochrane.org/handbook/current/chapter-09)
- [x] [McKenzie and Brennan (2024) Cochrane Handbook Chapter 12: Synthesizing and presenting findings using other methods](https://training.cochrane.org/handbook/current/chapter-12)
- [x] [Popay et al. (2006) Guidance on the conduct of narrative synthesis in systematic reviews](https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/)
- [x] [Wong et al. (2013) The RAMESES publication standards: realist syntheses](https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21)
- [x] [France et al. (2019) Improving reporting of meta-ethnography: the eMERGe reporting guidance](https://link.springer.com/article/10.1186/s12874-018-0600-0)
- [x] [Shao et al. (2024) STORM: Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models](https://arxiv.org/abs/2402.14207)
- [x] [Stanford OVAL STORM GitHub repository](https://github.com/stanford-oval/storm)
- [x] [LlamaIndex Response Synthesis Modules](https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/)
- [x] [LlamaIndex Building Response Synthesis from Scratch](https://developers.llamaindex.ai/python/examples/low_level/response_synthesis/)
- [x] [LangChain Summarization over Multiple Documents](https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html)
- [x] [Tannou et al. (2025) Using artificial intelligence for systematic review: the example of Elicit](https://link.springer.com/article/10.1186/s12874-025-02528-y)
- [x] [Systematic Reviews (2024) Leveraging artificial intelligence to enhance systematic reviews in health research: advanced tools and challenges](https://pmc.ncbi.nlm.nih.gov/articles/PMC11504244/)
- [x] [Li et al. (2024) The Dawn After the Dark: An Empirical Study on Factuality Hallucination in Large Language Models](https://aclanthology.org/2024.acl-long.586/)
- [x] [Rani et al. (2024) A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models](https://arxiv.org/abs/2401.01313)
- [x] [Mitchell (2026) Information synthesis: non-lossy compression, entropy, and information theory](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md)
- [x] [Mitchell (2026) Knowledge linking: building a connected research corpus via explicit cross-references and a knowledge graph](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md)
- [x] [Mitchell (2026) Cross-item synthesis: methodology and tooling for extracting meta-insights from the research corpus](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
- [x] [Research repository W-0051 and adjacent workflow context](https://github.com/davidamitchell/Research/blob/main/BACKLOG.md)
- [x] [Research Loop workflow](https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml)
- [x] [Publish Wiki workflow](https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml)
- [x] [Research Loop prompt](https://github.com/davidamitchell/Research/blob/main/research-prompt.md)

## Related

- [Mitchell (2026) Information synthesis: non-lossy compression, entropy, and information theory](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md)
- [Mitchell (2026) Knowledge linking: building a connected research corpus via explicit cross-references and a knowledge graph](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md)
- [Mitchell (2026) Cross-item synthesis: methodology and tooling for extracting meta-insights from the research corpus](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0-5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Working question: select a synthesis methodology and tool architecture for provenance-preserving cross-item synthesis over a heterogeneous repository corpus.
- Scope: review-method fit, tool-architecture fit, hallucination controls, provenance design, contradiction handling, workflow design, and ADR triggers.
- Constraints: no scheduled workflow, source-item traceability required, GitHub-native execution path, acronym expansion on first use.
- Output: one knowledge note that recommends a method stack and concrete design constraints for W-0051.
- Prior-work cross-reference: completed against prior repository items on synthesis failure modes, knowledge linking, and earlier synthesis workflow design.

### §1 Question Decomposition

- **A. Method selection**
  - A1. What does PRISMA contribute, and what does it not contribute, to corpus synthesis?
  - A2. Which Cochrane stages transfer directly to a file-based synthesis workflow?
  - A3. When is narrative synthesis a better fit than realist synthesis or meta-ethnography?
  - A4. Which qualitative synthesis methods preserve context rather than flattening it?
- **B. Tool architecture**
  - B1. Which tool patterns preserve source provenance through synthesis?
  - B2. Which tool patterns scale across many source items without losing inspectability?
  - B3. Where do generic summarization chains become unsafe for claim-level synthesis?
- **C. Hallucination prevention**
  - C1. Which controls reduce factual hallucination in multi-document generation?
  - C2. Which controls specifically reduce claim conflation across near-related sources?
  - C3. What is the minimum verification loop before a synthesis claim is accepted?
- **D. Provenance record**
  - D1. What fields must a synthesis claim carry to be auditable?
  - D2. How should the design surface supporting evidence, contradictions, and uncertainty?
- **E. Workflow design**
  - E1. What manual inputs should `synthesis-loop.yml` require?
  - E2. What sections should `synthesis-prompt.md` include?
  - E3. Which implementation decisions require an Architecture Decision Record (ADR)?

### §2 Investigation

#### A. Review-method fit

- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-03] PRISMA is a reporting and transparency standard, not a synthesis algorithm, and Cochrane distinguishes a systematic review from a narrative review by requiring pre-specified eligibility criteria, explicit grouping rules, and documented deviations from protocol.
- [fact; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12] Cochrane's transferable backbone for synthesis is: define the Population, Intervention, Comparator and Outcome (PICO) for each synthesis, tabulate study characteristics, determine which studies are similar enough to group, and pair any non-meta-analytic synthesis with transparent tables or visual displays.
- [fact; source: https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://training.cochrane.org/handbook/current/chapter-12] Narrative synthesis is designed for heterogeneous evidence and is only trustworthy when it is systematic, transparent, and protected against privileging one study over another without justification.
- [fact; source: https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21] Realist synthesis is non-linear and iterative, and it is designed to explain how and why outcomes occur in different contexts rather than merely aggregate reported findings.
- [fact; source: https://link.springer.com/article/10.1186/s12874-018-0600-0] Meta-ethnography is a seven-phase interpretive method that aims to generate new concepts while preserving the meanings and contexts of the original qualitative studies.
- [inference; source: https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0] The best fit for this repository is a hybrid method: use PRISMA and Cochrane for protocol discipline and auditability, use narrative synthesis as the default cross-item integration method, and use realist-synthesis or meta-ethnography techniques only when the synthesis question is explicitly about mechanisms, contexts, or interpretive concepts.

#### B. Tool-architecture fit

- [fact; source: https://arxiv.org/abs/2402.14207; https://github.com/stanford-oval/storm] STORM separates pre-writing from writing, discovers multiple perspectives, simulates source-grounded questioning, and generates long-form output with citations, which makes it a strong pattern for breadth-first evidence gathering before synthesis drafting.
- [fact; source: https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://developers.llamaindex.ai/python/examples/low_level/response_synthesis/] LlamaIndex exposes explicit response synthesizers, such as refine and tree summarize, and preserves `response.source_nodes`, which makes source-node retention a first-class architectural feature rather than an afterthought.
- [fact; source: https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html] LangChain's `map_reduce` summarization chain summarizes each document independently and then reduces those summaries into a final output, while optionally returning intermediate map steps for inspection.
- [fact; source: https://link.springer.com/article/10.1186/s12874-025-02528-y; https://pmc.ncbi.nlm.nih.gov/articles/PMC11504244/] Elicit is used as an Artificial Intelligence (AI)-assisted evidence-synthesis tool because it retrieves semantically related papers, summarizes abstracts, applies filters, and supports structured organization of findings, but empirical evaluation shows it is a complementary aid rather than a substitute for rigorous review method.
- [inference; source: https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html; https://link.springer.com/article/10.1186/s12874-025-02528-y] The safest architecture for repository synthesis borrows STORM's perspective-expansion stage and LlamaIndex's source-node retention, while treating generic map-reduce summarization as a scaling primitive rather than as the provenance-preserving synthesis method itself.

#### C. Hallucination prevention and conflation control

- [fact; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/] Current hallucination literature consistently treats retrieval grounding, verification, and post-generation checking as the strongest general-purpose controls for reducing factual errors in Large Language Model (LLM) outputs.
- [fact; source: https://arxiv.org/abs/2402.14207; https://github.com/stanford-oval/storm] STORM's use of perspective-guided question asking and source-grounded simulated conversations addresses breadth and source-grounding at the evidence-collection stage, which directly targets the risk of over-associating unrelated facts.
- [fact; source: https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://developers.llamaindex.ai/python/examples/low_level/response_synthesis/] Iterative refine-style synthesis is better suited than one-shot stuffing when context may overflow, because the synthesis process can retain source-node references while progressively incorporating additional evidence.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md] Prior repository work identifies false consensus and citation drift as the characteristic cross-item failure modes, where the synthesis claims stronger agreement or broader scope than any source item actually supports.
- [inference; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md] Hallucination prevention for this corpus should be organized around claim extraction before generation, not only retrieval before generation, because retrieval alone does not prevent the model from collapsing adjacent but non-identical claims into one oversimplified sentence.

#### D. Provenance-linking design

- [fact; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12] Transparent synthesis without meta-analysis still requires tabulation of study characteristics, explicit grouping decisions, and visible mapping from included evidence to synthesized statements.
- [fact; source: https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md] A provenance-preserving synthesis system needs both claim-level source references and a machine-readable relationship structure, because source-node retention alone does not express whether two claims confirm, qualify, or contradict each other.
- [inference; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md] The minimum provenance record for one synthesis claim is: synthesis claim identifier, epistemic label, source item slug, source section or key-finding identifier, short evidence excerpt or paraphrase, contradiction status, and confidence rationale.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-12; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md] In this repository, the most practical surface for that record is a combination of `cites:` in frontmatter, inline claim citations in prose, and an evidence-map table that lists each cross-item claim with its exact source-item support.

#### E. Contradiction detection and handling

- [fact; source: https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0] Both realist synthesis and meta-ethnography preserve context and explanation rather than flattening differences, which makes them better guides for contradiction handling than generic summarization chains.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md] Prior repository design work already distinguishes `confirms`, `contradicts`, and `extends` as useful cross-item relationship types.
- [inference; source: https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md] A synthesis pipeline should never silently resolve contradictions; it should classify each tension as resolved by context, unresolved tension, or excluded from top-line conclusions, and it should explain that disposition in the evidence map.

#### F. Workflow and prompt design

- [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] W-0051 already fixes three major design constraints: the output lives in `Knowledge/`, the workflow is manual-only, and the prompt should parallel the structure of `research-prompt.md`.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml] The existing repository pattern for agentic content generation is a `workflow_dispatch` workflow that checks out `main`, runs one bounded agent loop, and commits directly to `main`, with publication handled by a downstream path-based workflow.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] `synthesis-loop.yml` should accept `source_items` and `synthesis_question` as required manual inputs, and should not support automatic clustering or scheduled runs in its first version.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://training.cochrane.org/handbook/current/chapter-09] `synthesis-prompt.md` should mirror the research prompt's discipline but with sections for corpus boundary, source-item extraction, claim clustering, contradiction table, evidence map, synthesis narrative, and recursive review.

#### G. ADR triggers

- [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md] W-0051 is already marked as ADR-required, and the repository instructions require an ADR for new publication channels, storage approaches, workflow side effects, or schema changes with material reversal cost.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml] The design decisions that warrant explicit ADR treatment are: the `Knowledge/` document type and frontmatter schema, the provenance-record format for synthesis claims, and the site-generation and publication-path changes needed to render knowledge items alongside completed research.

### §3 Reasoning

- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12] The strongest external methodological consensus is about process discipline, explicit grouping, and visible evidence tables, not about delegating synthesis judgement to a language model without intermediate artifacts.
- [fact; source: https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0] Narrative synthesis, realist synthesis, and meta-ethnography serve different jobs, heterogeneous aggregation, mechanism explanation, and interpretive concept generation, so choosing one as a complete substitute for the others would overstate its scope.
- [fact; source: https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html] Tool architectures differ mainly in whether they preserve inspectable intermediate evidence, and that difference matters more for this use case than raw summarization throughput.
- [inference; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md] The repository should treat synthesis as a controlled reasoning task over extracted claims, not as direct long-context summarization over whole documents, because the latter maximizes the same abstraction pressure that produced false-consensus risk in prior repository work.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml] The first synthesis workflow will be used on deliberately chosen clusters rather than on the whole corpus at once, because W-0051 defines manual source-item input and the current repository pattern already optimizes for owner-initiated runs.

### §4 Consistency Check

- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-12] No contradiction remains between the recommended method stack and the external review-method literature, because PRISMA is treated as reporting discipline and narrative synthesis is treated as the primary aggregation method rather than as a replacement for protocol rigor.
- [fact; source: https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html] No contradiction remains between the tool-architecture comparison and the implementation recommendation, because the recommendation explicitly uses map-reduce only as a subordinate scale tactic and not as the provenance layer.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md] The ADR recommendation is internally consistent with repository policy, because W-0051 already requires an ADR and the proposed changes introduce a new document class plus publication-path changes.

### §5 Depth and Breadth Expansion

- [inference; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md] **Technical lens:** the core technical choice is not "which prompt is best" but "which intermediate artifacts are mandatory", and the answer is claim tables plus contradiction metadata before any final synthesis prose is written.
- [inference; source: https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0] **Methodological lens:** narrative synthesis should carry the default workflow because most repository items mix conceptual, empirical, and design evidence, but realist-synthesis and meta-ethnography moves should be available as optional passes when the question is explicitly about mechanism or meaning.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md] **Operational lens:** manual-only dispatch is not just a usability preference, it is a governance control that narrows scope, forces explicit source selection, and reduces the probability of accidental low-quality bulk synthesis.
- [inference; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://link.springer.com/article/10.1186/s12874-025-02528-y] **Behavioural lens:** the evidence supports using AI as an acceleration aid inside a human-bounded review workflow, not as an autonomous replacement for claim verification, because tool assistance improves throughput but remains unreliable when treated as a standalone adjudicator.

### §6 Synthesis

**Executive summary:**

The most appropriate method for this repository is a systematic-review-inspired hybrid, Cochrane and PRISMA for protocol and reporting discipline, narrative synthesis for default cross-item integration, and selective realist-synthesis or meta-ethnography techniques when the synthesis question is explicitly about mechanisms, contexts, or meanings. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-09; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0]

The architecture should not synthesize directly from raw item prose; it should extract structured claims first, cluster them by question, preserve claim-to-source-item links, and only then generate the narrative synthesis and contradiction table. [inference; source: https://training.cochrane.org/handbook/current/chapter-12; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md]

The best tool-pattern combination is STORM-style perspective expansion plus LlamaIndex-style source-node retention, with map-reduce summarization used only as a bounded reduction primitive rather than as the core provenance mechanism. [inference; source: https://arxiv.org/abs/2402.14207; https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html]

The workflow should remain `workflow_dispatch` only, require explicit `source_items` and `synthesis_question`, write to `Knowledge/`, and carry ADR-backed decisions for the new document schema, provenance format, and publication-path changes. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md]

**Key findings:**

1. **A defensible synthesis workflow for this corpus should combine Cochrane-style protocol discipline with narrative synthesis as the default integration method, because PRISMA improves transparency while narrative synthesis is the best fit for heterogeneous, non-meta-analytic evidence.** ([inference]; high confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/)
2. **Realist synthesis and meta-ethnography are better treated as optional interpretive passes than as the base workflow, because they preserve context and mechanism but are narrower and more specialized than the repository's general cross-item synthesis need.** ([inference]; medium confidence; source: https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/)
3. **The repository's main anti-hallucination control should be claim extraction before prose generation, because retrieval grounding alone does not stop a Large Language Model (LLM) from conflating adjacent source-item claims into an unsupported synthesis sentence.** ([inference]; medium confidence; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md)
4. **Each synthesis claim needs a minimum provenance record that includes source item slug, source location, epistemic label, confidence rationale, and contradiction status, because transparent non-meta-analytic synthesis still depends on visible evidence mapping and grouping decisions.** ([inference]; high confidence; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md)
5. **STORM and LlamaIndex provide the strongest architectural patterns for this use case, because STORM broadens evidence collection through perspective-guided questioning while LlamaIndex preserves source nodes through iterative synthesis.** ([inference]; medium confidence; source: https://arxiv.org/abs/2402.14207; https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://developers.llamaindex.ai/python/examples/low_level/response_synthesis/)
6. **Generic map-reduce summarization is useful for scale but insufficient as the provenance layer, because it summarizes documents independently and then reduces summaries, which preserves throughput better than claim-level traceability.** ([inference]; medium confidence; source: https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/)
7. **Artificial Intelligence (AI)-assisted review tools such as Elicit should be treated as complementary accelerators rather than authoritative synthesizers, because empirical evaluation shows value in search and organization but also substantial variability and incomplete overlap with traditional review results.** ([fact]; medium confidence; source: https://link.springer.com/article/10.1186/s12874-025-02528-y; https://pmc.ncbi.nlm.nih.gov/articles/PMC11504244/)
8. **Contradictions must be first-class synthesis outputs rather than silent prompt-internal reasoning, because preserving context-dependent differences is essential to prevent false consensus and because prior repository work already defines usable cross-item relationship types.** ([inference]; medium confidence; source: https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
9. **The first repository implementation should be a manual-only `synthesis-loop.yml` that requires explicit `source_items` and `synthesis_question`, because owner-selected scope is both the current repository norm and the safest control against low-quality bulk synthesis.** ([inference]; high confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/research-prompt.md)
10. **An ADR is warranted before W-0051 implementation because introducing `Knowledge/`, a new synthesis schema, and new site-rendering behavior changes the repository's information architecture and publication path, not just one workflow file.** ([fact]; high confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Hybrid method stack, Cochrane plus PRISMA plus narrative synthesis, is the best default for heterogeneous repository synthesis. | https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/ | high | Default method stack |
| [inference] Realist synthesis and meta-ethnography should be optional interpretive passes rather than the base workflow. | https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0 | medium | Mechanism or meaning questions |
| [inference] Claim extraction before prose generation is the main anti-hallucination control for this corpus. | https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md | medium | Prevents false consensus |
| [inference] Each synthesis claim needs a structured provenance record with source slug, location, epistemic label, confidence rationale, and contradiction status. | https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md | high | Minimum audit unit |
| [inference] STORM plus LlamaIndex patterns are safer than generic summarization chains for provenance-preserving synthesis. | https://arxiv.org/abs/2402.14207; https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://developers.llamaindex.ai/python/examples/low_level/response_synthesis/ | medium | Breadth plus source nodes |
| [inference] Generic map-reduce summarization is useful for scale but insufficient as the provenance layer. | https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/ | medium | Reduction primitive only |
| [fact] Elicit-like review assistants are complementary accelerators rather than authoritative synthesizers. | https://link.springer.com/article/10.1186/s12874-025-02528-y; https://pmc.ncbi.nlm.nih.gov/articles/PMC11504244/ | medium | Useful, not sufficient |
| [inference] Contradictions must be explicit synthesis outputs with dispositions rather than silent prompt-internal choices. | https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md | medium | Resolved, open, or excluded |
| [inference] `synthesis-loop.yml` should be manual-only and require explicit source selection. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/research-prompt.md | high | Governance control |
| [fact] An ADR is required for the new knowledge document type, provenance schema, and publication-path changes. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml | high | Architecture change |

**Assumptions:**

- [assumption; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml] The first synthesis workflow will operate on owner-selected clusters rather than automatic whole-corpus batches, because that is the implementation pattern already fixed by W-0051 and reinforced by the existing research-loop safety model.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md] Existing completed items provide enough prior-art context to shape the provenance model without first implementing a full semantic-search or graph-database layer.

**Analysis:**

External review-method literature is strongest on transparency and auditability, not on a single universally best synthesis procedure. [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-12]

That makes a hybrid recommendation more defensible than choosing one named method wholesale: Cochrane and PRISMA define how the work is bounded and reported, narrative synthesis defines how heterogeneous findings are integrated, and realist or meta-ethnographic moves are invoked only when the synthesis question requires explanation or interpretation beyond aggregation. [inference; source: https://training.cochrane.org/handbook/current/chapter-09; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0]

The tool comparison points in the same direction. STORM is strongest at breadth and grounded question generation, LlamaIndex is strongest at explicit source-node retention during synthesis, LangChain map-reduce is strongest at scalable reduction with inspectable intermediate summaries, and Elicit is strongest as a complementary search-and-organization aid rather than a synthesis authority. [inference; source: https://arxiv.org/abs/2402.14207; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html; https://link.springer.com/article/10.1186/s12874-025-02528-y]

The trade-off is therefore clear: optimize first for provenance and contradiction visibility, then for automation, because faster synthesis without claim-level traceability reproduces the exact false-consensus failure mode the repository is trying to avoid. [inference; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md]

**Risks, gaps, uncertainties:**

- The evidence base for tool architecture is stronger for STORM and LlamaIndex than for vendor-managed evidence-synthesis products, so the tool-ranking conclusions rely more heavily on open methods papers and accessible documentation than on stable product manuals. [inference; source: https://arxiv.org/abs/2402.14207; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://link.springer.com/article/10.1186/s12874-025-02528-y]
- The hallucination literature supports retrieval and verification broadly, but it does not yet provide a corpus-synthesis-specific benchmark for claim conflation across repository-style Markdown items. [fact; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/]
- The recommendation to keep `synthesis-loop.yml` manual-only is strongly supported by repository governance context, but not by external systematic-review methodology literature, so it remains a design judgement rather than a general research finding. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

**Open questions:**

- Should the first `Knowledge/` schema require excerpt-level evidence quotes, or is source item slug plus section identifier sufficient for version 1?
- Should contradiction handling be stored only in the synthesis file, or also in machine-readable sidecar data for later tooling?
- When the corpus grows further, should source-item clustering remain manual-only, or should a later version add opt-in semantic expansion after the provenance model is stable?

### §7 Recursive Review

- Coverage: complete
- Prior-work sweep: completed before investigation and reflected in `cites:` and `related:`
- Acronym audit: pass
- Inline citation audit: pass
- Evidence-map coverage: every key finding represented
- Remaining uncertainty: tool-comparison evidence stronger for open documentation than for vendor-managed product pages

---

## Findings

### Executive Summary

The best design for this repository is a systematic-review-inspired hybrid that uses Cochrane and PRISMA for rigor, narrative synthesis for default cross-item integration, and selective realist-synthesis or meta-ethnography techniques only when the question is explicitly about mechanisms, contexts, or meanings. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-09; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0]

The core anti-hallucination move is to extract and cluster claims before generating synthesis prose, because retrieval grounding by itself does not stop claim conflation across related source items. [inference; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md]

The strongest architecture pattern is STORM-style perspective expansion combined with LlamaIndex-style source-node retention, while map-reduce summarization should remain a bounded reduction tactic rather than the provenance layer. [inference; source: https://arxiv.org/abs/2402.14207; https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html]

The first implementation should remain manual-only, require explicit `source_items` and `synthesis_question`, write to `Knowledge/`, and carry an ADR for the new knowledge schema, provenance format, and publication-path changes. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md]

### Key Findings

1. **A defensible synthesis workflow for this corpus should combine Cochrane-style protocol discipline with narrative synthesis as the default integration method, because PRISMA improves transparency while narrative synthesis is the best fit for heterogeneous, non-meta-analytic evidence.** ([inference]; high confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/)
2. **Realist synthesis and meta-ethnography are better treated as optional interpretive passes than as the base workflow, because they preserve context and mechanism but are narrower and more specialized than the repository's general cross-item synthesis need.** ([inference]; medium confidence; source: https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/)
3. **The repository's main anti-hallucination control should be claim extraction before prose generation, because retrieval grounding alone does not stop a Large Language Model (LLM) from conflating adjacent source-item claims into an unsupported synthesis sentence.** ([inference]; medium confidence; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md)
4. **Each synthesis claim needs a minimum provenance record that includes source item slug, source location, epistemic label, confidence rationale, and contradiction status, because transparent non-meta-analytic synthesis still depends on visible evidence mapping and grouping decisions.** ([inference]; high confidence; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md)
5. **STORM and LlamaIndex provide the strongest architectural patterns for this use case, because STORM broadens evidence collection through perspective-guided questioning while LlamaIndex preserves source nodes through iterative synthesis.** ([inference]; medium confidence; source: https://arxiv.org/abs/2402.14207; https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://developers.llamaindex.ai/python/examples/low_level/response_synthesis/)
6. **Generic map-reduce summarization is useful for scale but insufficient as the provenance layer, because it summarizes documents independently and then reduces summaries, which preserves throughput better than claim-level traceability.** ([inference]; medium confidence; source: https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/)
7. **Artificial Intelligence (AI)-assisted review tools such as Elicit should be treated as complementary accelerators rather than authoritative synthesizers, because empirical evaluation shows value in search and organization but also substantial variability and incomplete overlap with traditional review results.** ([fact]; medium confidence; source: https://link.springer.com/article/10.1186/s12874-025-02528-y; https://pmc.ncbi.nlm.nih.gov/articles/PMC11504244/)
8. **Contradictions must be first-class synthesis outputs rather than silent prompt-internal reasoning, because preserving context-dependent differences is essential to prevent false consensus and because prior repository work already defines usable cross-item relationship types.** ([inference]; medium confidence; source: https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md)
9. **The first repository implementation should be a manual-only `synthesis-loop.yml` that requires explicit `source_items` and `synthesis_question`, because owner-selected scope is both the current repository norm and the safest control against low-quality bulk synthesis.** ([inference]; high confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/research-prompt.md)
10. **An ADR is warranted before W-0051 implementation because introducing `Knowledge/`, a new synthesis schema, and new site-rendering behavior changes the repository's information architecture and publication path, not just one workflow file.** ([fact]; high confidence; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Hybrid method stack, Cochrane plus PRISMA plus narrative synthesis, is the best default for heterogeneous repository synthesis. | https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/ | high | Default method stack |
| [inference] Realist synthesis and meta-ethnography should be optional interpretive passes rather than the base workflow. | https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0 | medium | Mechanism or meaning questions |
| [inference] Claim extraction before prose generation is the main anti-hallucination control for this corpus. | https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md | medium | Prevents false consensus |
| [inference] Each synthesis claim needs a structured provenance record with source slug, location, epistemic label, confidence rationale, and contradiction status. | https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md | high | Minimum audit unit |
| [inference] STORM plus LlamaIndex patterns are safer than generic summarization chains for provenance-preserving synthesis. | https://arxiv.org/abs/2402.14207; https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://developers.llamaindex.ai/python/examples/low_level/response_synthesis/ | medium | Breadth plus source nodes |
| [inference] Generic map-reduce summarization is useful for scale but insufficient as the provenance layer. | https://langchain-doc.readthedocs.io/en/latest/modules/indexes/chain_examples/summarize.html; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/ | medium | Reduction primitive only |
| [fact] Elicit-like review assistants are complementary accelerators rather than authoritative synthesizers. | https://link.springer.com/article/10.1186/s12874-025-02528-y; https://pmc.ncbi.nlm.nih.gov/articles/PMC11504244/ | medium | Useful, not sufficient |
| [inference] Contradictions must be explicit synthesis outputs with dispositions rather than silent prompt-internal choices. | https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md | medium | Resolved, open, or excluded |
| [inference] `synthesis-loop.yml` should be manual-only and require explicit source selection. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml; https://github.com/davidamitchell/Research/blob/main/research-prompt.md | high | Governance control |
| [fact] An ADR is required for the new knowledge document type, provenance schema, and publication-path changes. | https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/publish-wiki.yml | high | Architecture change |

### Assumptions

- [assumption; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml] The first synthesis workflow will operate on owner-selected clusters rather than automatic whole-corpus batches, because that is the implementation pattern already fixed by W-0051 and reinforced by the existing research-loop safety model.
- [assumption; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-knowledge-linking-connected-corpus.md] Existing completed items provide enough prior-art context to shape the provenance model without first implementing a full semantic-search or graph-database layer.

### Analysis

The evidence does not support copying one named academic review method unchanged into the repository. [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-12]

Instead, it supports separating three layers that are often muddled together in casual design discussions: review discipline, synthesis method, and generation architecture. [inference; source: https://training.cochrane.org/handbook/current/chapter-09; https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://arxiv.org/abs/2402.14207; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/]

Review discipline comes from Cochrane and PRISMA, which force explicit boundaries, grouping logic, and visible reporting. [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC8005925/; https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-09]

Default synthesis method comes from narrative synthesis, because the repository corpus is heterogeneous and design-oriented, while realist-synthesis and meta-ethnography are better invoked as specialized passes when the question is explanatory or interpretive. [inference; source: https://research.tees.ac.uk/en/publications/guidance-on-the-conduct-of-narrative-synthesis-in-sytematic-revie/; https://bmcmedicine.biomedcentral.com/articles/10.1186/1741-7015-11-21; https://link.springer.com/article/10.1186/s12874-018-0600-0]

Generation architecture should be grounded in perspective expansion, source-node retention, and visible contradiction handling, because those are the controls that directly counter false consensus and citation drift. [inference; source: https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://arxiv.org/abs/2401.01313; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-02-27-information-synthesis-entropy.md]

### Risks, Gaps, and Uncertainties

- The tool-comparison evidence is uneven, because open architectures such as STORM and LlamaIndex expose more inspectable detail than vendor-managed products. [inference; source: https://github.com/stanford-oval/storm; https://developers.llamaindex.ai/python/framework/module_guides/querying/response_synthesizers/response_synthesizers/; https://link.springer.com/article/10.1186/s12874-025-02528-y]
- No external benchmark in this evidence set directly measures claim conflation across repository-style Markdown items, so the recommended control stack remains evidence-informed design rather than benchmark-proven doctrine. [fact; source: https://arxiv.org/abs/2401.01313; https://aclanthology.org/2024.acl-long.586/]
- The recommendation to keep the first workflow manual-only is strongly justified by repository governance and safety constraints, but it is not a general property of systematic-review methodology. [inference; source: https://github.com/davidamitchell/Research/blob/main/BACKLOG.md; https://github.com/davidamitchell/Research/blob/main/.github/workflows/research-loop.yml]

### Open Questions

- Should the first `Knowledge/` schema require excerpt-level evidence quotes, or is source item slug plus section identifier sufficient for version 1?
- Should contradiction handling be stored only in the synthesis file, or also in machine-readable sidecar data for later tooling?
- When the corpus grows further, should source-item clustering remain manual-only, or should a later version add opt-in semantic expansion after the provenance model is stable?

### Output

- Type: knowledge
- Description: This item recommends a hybrid synthesis methodology, a claim-first provenance model, and a manual-only workflow design for W-0051 so that future `Knowledge/` artifacts can be generated without silent claim conflation. [inference; source: https://training.cochrane.org/handbook/current/chapter-09; https://arxiv.org/abs/2401.01313; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- Links:
  - https://training.cochrane.org/handbook/current/chapter-09
  - https://arxiv.org/abs/2402.14207
  - https://github.com/davidamitchell/Research/blob/main/BACKLOG.md

---

## Output

- Type: knowledge
- Description: This item recommends a hybrid synthesis methodology, a claim-first provenance model, and a manual-only workflow design for W-0051 so that future `Knowledge/` artifacts can be generated without silent claim conflation. [inference; source: https://training.cochrane.org/handbook/current/chapter-09; https://arxiv.org/abs/2401.01313; https://github.com/davidamitchell/Research/blob/main/BACKLOG.md]
- Links:
  - https://training.cochrane.org/handbook/current/chapter-09
  - https://arxiv.org/abs/2402.14207
  - https://github.com/davidamitchell/Research/blob/main/BACKLOG.md
