---
review_count: 1
title: "Meta-analysis standards and Artificial Intelligence (AI) skill evaluation: what do professional systematic-review frameworks require, and how do existing repository research workflows measure up?"
added: 2026-05-02T06:05:57+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []  # slugs (filename without .md) of backlog items that cannot start until this one is complete
tags: [evaluation, research-methodology, workflow, agent-tooling, agentic-ai]
started: 2026-05-03T07:13:02+00:00
completed: ~
output: [knowledge]  # skill | tool | agent | knowledge | backlog-item
cites: [2026-05-02-systematic-review-methodology-ai-synthesis, 2026-05-02-adversarial-review-methods-ai-research-quality]          # slugs of items this item directly depends on or quotes
related: [2026-03-03-cross-item-synthesis-meta-insights, 2026-05-02-automated-claim-verification-academic-literature, 2026-05-01-coding-agent-context-management-transparency]
superseded_by: ~   # slug of a later item that overrides this one (null if not superseded)
supersedes: ~      # slug of an older item this one replaces (null if not applicable)
item_type: primary # primary | synthesis
confidence: medium # high | medium | low
versions: []       # entries: {version: "1.0", sha: "<commit-hash>", changed: YYYY-MM-DD, progress: "<path>", summary: "<one-line>"}
---

# Meta-analysis standards and Artificial Intelligence (AI) skill evaluation: what do professional systematic-review frameworks require, and how do existing repository research workflows measure up?

## Research Question

What are the established standards and best practices for meta-analysis and systematic review, and how do the existing Artificial Intelligence (AI) research skills and prompts in this repository measure up against them?

## Scope

**In scope:**
- Internationally recognised systematic review and meta-analysis standards, for example Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA), the Cochrane Handbook, and Campbell Collaboration guidance
- Study quality assessment tools and criteria, for example Grading of Recommendations Assessment, Development and Evaluation (GRADE), Risk Of Bias In Non-randomized Studies of Interventions (ROBINS-I), Newcastle-Ottawa Scale (NOS), and Joanna Briggs Institute (JBI) critical appraisal tools
- Study selection protocols, including search strategies, inclusion and exclusion criteria, and the Population, Intervention, Comparator, Outcome (PICO) framework
- Best practices for synthesis and summarisation of multiple studies, including narrative synthesis and evidence mapping
- Evaluation frameworks or quality benchmarks proposed for Artificial Intelligence-assisted literature review or evidence synthesis
- Inventory of research workflow artifacts currently used in this repository, including `research-prompt.md`, `research-review-prompt.md`, and documented fallback behavior when `.github/skills/` is not initialised
- Identified gaps and a recommended design for a dedicated systematic-review or meta-analysis skill

**Out of scope:**
- Conducting an actual meta-analysis on any domain topic
- Domain-specific clinical statistical methods such as pooled effect sizes, forest plots, and heterogeneity statistics
- Skills in repositories other than `davidamitchell/Research` and `davidamitchell/Skills`

**Constraints:**
- Focus on methodological and process standards, not domain-specific findings
- Prioritise frameworks transferable to non-clinical research domains, especially software and Artificial Intelligence research synthesis
- Sources must be publicly accessible

## Context

- [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md] The repository already requires a structured research question, explicit scope, a full investigation record, an Evidence Map, inline citations, and a formal review gate before a research item can be completed.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The documented fallback path for research work tells agents to follow `research-prompt.md` when the `.github/skills/` submodule is not initialised, which makes the prompt files themselves part of the enforceable repository method.
- [inference; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583; https://training.cochrane.org/handbook/current/chapter-03; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] This means the comparison that matters is not whether the repository cites sources carefully, which it does, but whether its current workflow artifacts cover the upstream controls that professional systematic-review standards treat as mandatory.

## Approach

1. **Standards inventory**: identify the main systematic-review and meta-analysis standards and extract transferable requirements.
2. **Study quality criteria**: examine how GRADE, ROBINS-I, NOS, JBI, and A MeaSurement Tool to Assess Systematic Reviews 2 (AMSTAR 2) assess quality, bias, and certainty.
3. **Study selection protocols**: document inclusion and exclusion criteria design, PICO framing, and search strategy requirements.
4. **Synthesis best practices**: survey narrative synthesis and evidence-mapping methods for heterogeneous evidence.
5. **Artificial Intelligence-assisted review evidence**: examine what current evidence says about screening tools such as Rayyan and Large Language Model (LLM)-assisted review pipelines.
6. **Repository workflow audit**: inspect the current prompts and review workflow, then map their controls against the standards identified above.
7. **Gap analysis and skill design**: identify the missing controls and recommend a dedicated systematic-review or meta-analysis skill design.

## Sources

- [x] [Page et al. (2021) The PRISMA 2020 statement: An updated guideline for reporting systematic reviews](https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583)
- [x] [PRISMA Statement (2021) PRISMA 2020 checklist](https://www.prisma-statement.org/prisma-2020-checklist)
- [x] [Cochrane Handbook (2024) Chapter 3: Defining the criteria for including studies and how they will be grouped for the synthesis](https://training.cochrane.org/handbook/current/chapter-03)
- [x] [Cochrane Handbook (2025) Chapter 4: Searching for and selecting studies](https://training.cochrane.org/handbook/current/chapter-04)
- [x] [Cochrane Handbook (2024) Chapter 9: Summarizing study characteristics and preparing for synthesis](https://training.cochrane.org/handbook/current/chapter-09)
- [x] [Cochrane Handbook (2024) Chapter 12: Synthesizing and presenting findings using other methods](https://training.cochrane.org/handbook/current/chapter-12)
- [x] [Cochrane Handbook (2024) Chapter 14: Completing Summary of Findings tables and grading the certainty of the evidence](https://training.cochrane.org/handbook/current/chapter-14)
- [x] [Campbell Collaboration (2026) Start a review or evidence and gap map](https://www.campbellcollaboration.org/get-involved/start-a-review/)
- [x] [Campbell Collaboration (2026) Standards for reviews](https://www.campbellcollaboration.org/methods/standards/)
- [x] [GRADE Working Group (2013) GRADE Handbook](https://gdt.gradepro.org/app/handbook/handbook.html)
- [x] [AMSTAR 2 (2017) A MeaSurement Tool to Assess Systematic Reviews 2](https://amstar.ca/Amstar-2.php)
- [x] [Cochrane Bias Methods Group (2025) Risk Of Bias In Non-Randomized Studies of Interventions (ROBINS-I)](https://methods.cochrane.org/bias/risk-bias-non-randomized-studies-interventions)
- [x] [Wells et al. (n.d.) The Newcastle-Ottawa Scale (NOS) for assessing the quality of nonrandomised studies in meta-analyses](http://www.ohri.ca/programs/clinical_epidemiology/oxford.asp)
- [x] [Joanna Briggs Institute (JBI) Critical appraisal tools](https://jbi.global/critical-appraisal-tools)
- [x] [Popay et al. (2006) Guidance on the conduct of narrative synthesis in systematic reviews](http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf)
- [x] [Rayyan (2026) Artificial Intelligence-powered systematic review tool](https://rayyan.ai/)
- [x] [Chakhtoura et al. (2025) Streamlining systematic reviews with large language models: comparing Rayyan Artificial Intelligence and Generative Pre-trained Transformer 4 (GPT-4)](https://link.springer.com/article/10.1186/s12874-025-02583-5)
- [x] [Research Synthesis Methods (2025) Generative artificial intelligence use in evidence synthesis: A systematic review](https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675)
- [x] [Mitchell (2026) What systematic review methodologies and Artificial Intelligence-assisted synthesis tool architectures are most appropriate for cross-item synthesis of a growing file-based research corpus, and what design prevents hallucination and claim conflation across source items?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md)
- [x] [Mitchell (2026) What adversarial review and red-teaming methods are most effective for detecting shallow reasoning in Artificial Intelligence-generated research findings before finalisation, and how should they be implemented as prompt-only instructions?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md)
- [x] [Mitchell (2026) Research Loop Prompt](https://github.com/davidamitchell/Research/blob/main/research-prompt.md)
- [x] [Mitchell (2026) Research Quality Review](https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md)
- [x] [Mitchell (2026) Copilot Instructions](https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: What do professional systematic-review and meta-analysis frameworks require, and how does the repository's current Artificial Intelligence research workflow compare?
- Scope: standards, appraisal tools, search and selection rules, synthesis methods, Artificial Intelligence-assisted review evidence, repository workflow audit, and recommended skill design.
- Constraints: public sources only, transferable principles only, and no quantitative effect-size meta-analysis.
- Output: knowledge, specifically a standards comparison plus a recommended design for a dedicated systematic-review or meta-analysis skill.
- Prior completed items reviewed: [Mitchell (2026) What systematic review methodologies and Artificial Intelligence-assisted synthesis tool architectures are most appropriate for cross-item synthesis of a growing file-based research corpus, and what design prevents hallucination and claim conflation across source items?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md), [Mitchell (2026) What adversarial review and red-teaming methods are most effective for detecting shallow reasoning in Artificial Intelligence-generated research findings before finalisation, and how should they be implemented as prompt-only instructions?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md), [Mitchell (2026) Cross-item synthesis: methodology and tooling for extracting meta-insights from the research corpus](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-03-cross-item-synthesis-meta-insights.md), [Mitchell (2026) Automated claim verification for academic literature and research repositories](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-automated-claim-verification-academic-literature.md), and [Mitchell (2026) What are best practices for transparent, user-controlled context management in Artificial Intelligence coding agent harnesses?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-coding-agent-context-management-transparency.md).

### §1 Question Decomposition

- **Root question:** Is the repository's current research workflow methodologically equivalent to a professional systematic-review or meta-analysis workflow?
- **A. Standards and scope**
  - A1. What does PRISMA require for transparent reporting?
  - A2. What do Cochrane and Campbell require for protocol, search, selection, and synthesis conduct?
  - A3. Which parts of these standards transfer to a heterogeneous non-clinical corpus?
- **B. Appraisal and certainty**
  - B1. What do GRADE and Cochrane require for certainty judgments?
  - B2. What do AMSTAR 2, ROBINS-I, NOS, and JBI require for methodological or study-level appraisal?
  - B3. What is the minimum transferable appraisal structure for this repository?
- **C. Artificial Intelligence-assisted review evidence**
  - C1. What do current tools such as Rayyan automate well?
  - C2. What do current studies say about error rates and human oversight needs?
  - C3. Do current Artificial Intelligence review tools justify a fully autonomous workflow?
- **D. Repository workflow audit**
  - D1. Which current prompt artifacts match professional standards?
  - D2. Which required upstream controls are absent?
  - D3. Which existing repository controls are stronger than conventional review standards for Artificial Intelligence-specific failure modes?
- **E. Recommended design**
  - E1. Should the current research skill be relabelled, or should a separate systematic-review or meta-analysis skill be introduced?
  - E2. Which artifacts must that skill require?
  - E3. When should the heavier workflow be invoked instead of the default research workflow?

### §2 Investigation

#### A. Review standards and protocol discipline

- [fact; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583; https://www.prisma-statement.org/prisma-2020-checklist] PRISMA 2020 is a reporting standard, not a synthesis algorithm, and it updates reporting guidance for how reviews identify, select, appraise, and synthesise studies through a 27-item checklist plus revised flow diagrams.
- [fact; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583] PRISMA explicitly frames a valuable systematic review as a transparent, complete, and accurate account of why the review was done, what was done, and what was found.
- [fact; source: https://training.cochrane.org/handbook/current/chapter-03] Cochrane Chapter 3 requires pre-specified eligibility criteria based on review PICO, discourages outcome-based exclusion except in limited circumstances, and requires authors to plan how included studies will be grouped for synthesis at protocol stage.
- [fact; source: https://training.cochrane.org/handbook/current/chapter-04] Cochrane Chapter 4 requires a comprehensive, reproducible, multi-source search process, states that a single bibliographic database is inadequate, and recommends collaboration with an information specialist or librarian.
- [fact; source: https://training.cochrane.org/handbook/current/chapter-09] Cochrane Chapter 9 defines a general synthesis framework that starts with planned comparisons, study-characteristics tables, explicit grouping decisions, documented protocol deviations, and structured synthesis of study characteristics before any statistical or non-statistical synthesis.
- [fact; source: https://training.cochrane.org/handbook/current/chapter-12; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf] Cochrane Chapter 12 and Popay et al. both treat narrative synthesis as a disciplined alternative for heterogeneous evidence, and both require transparent tabulation or structured displays rather than free-form descriptive prose.
- [fact; source: https://www.campbellcollaboration.org/get-involved/start-a-review/; https://www.campbellcollaboration.org/methods/standards/] Campbell requires title registration, protocol approval, and a review or evidence-and-gap-map stage, and it makes adherence to a mandatory standards checklist part of editorial submission.

#### B. Appraisal and certainty frameworks

- [fact; source: https://gdt.gradepro.org/app/handbook/handbook.html; https://training.cochrane.org/handbook/current/chapter-14] GRADE rates certainty in a body of evidence by outcome and requires explicit consideration of risk of bias, inconsistency, indirectness, imprecision, and publication bias, with four certainty levels from high to very low.
- [fact; source: https://amstar.ca/Amstar-2.php] AMSTAR 2 contains 16 items, bases overall confidence on weaknesses in critical domains, and explicitly rejects a simple additive total score as a substitute for domain judgment.
- [fact; source: https://methods.cochrane.org/bias/risk-bias-non-randomized-studies-interventions; https://www.riskofbias.info/welcome/robins-i-v2] ROBINS-I is a domain-based risk-of-bias tool for non-randomized intervention studies that uses signalling questions and domain judgments rather than a single undifferentiated quality label.
- [fact; source: http://www.ohri.ca/programs/clinical_epidemiology/oxford.asp] The Newcastle-Ottawa Scale assesses nonrandomized studies through structured judgments across selection, comparability, and exposure or outcome ascertainment.
- [fact; source: https://jbi.global/critical-appraisal-tools] JBI provides study-design-specific critical appraisal checklists rather than one universal checklist for every evidence type.
- [inference; source: https://gdt.gradepro.org/app/handbook/handbook.html; https://amstar.ca/Amstar-2.php; https://methods.cochrane.org/bias/risk-bias-non-randomized-studies-interventions; http://www.ohri.ca/programs/clinical_epidemiology/oxford.asp; https://jbi.global/critical-appraisal-tools] The transferable principle across these frameworks is not one mandatory tool, but the need to record structured, domain-level judgments about evidence quality instead of relying on implicit source trust.

#### C. Synthesis methods and Artificial Intelligence-assisted review evidence

- [fact; source: http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf; https://training.cochrane.org/handbook/current/chapter-12] Narrative synthesis is designed for situations where evidence is heterogeneous or statistical pooling is inappropriate, but it still requires explicit stages, structured comparison, and transparent display of results.
- [fact; source: https://rayyan.ai/; https://link.springer.com/article/10.1186/s12874-025-02583-5] Rayyan is positioned as an Artificial Intelligence-assisted screening platform with deduplication, PICO filters, and review workbench features, and current evaluation work still treats it as a semi-automated screening aid rather than a full evidence-synthesis replacement.
- [fact; source: https://link.springer.com/article/10.1186/s12874-025-02583-5] Recent comparison work on Rayyan Artificial Intelligence and a GPT-4 pipeline states that title and abstract screening in systematic reviews is normally conducted independently in duplicate, and it evaluates automation against that manual gold standard rather than replacing methodological safeguards.
- [fact; source: https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675] A 2025 systematic review of generative Artificial Intelligence in evidence synthesis concludes that current Generative Artificial Intelligence is not suitable for evidence synthesis without caution and human oversight because it still makes substantial numbers of mistakes across synthesis tasks.
- [inference; source: https://link.springer.com/article/10.1186/s12874-025-02583-5; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675] Current Artificial Intelligence review evidence supports automation for prioritisation and screening efficiency, but it does not support treating a single-agent workflow as methodologically equivalent to a professional systematic review without additional control artifacts and oversight.

#### D. Current repository workflow audit

- [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The repository's research loop requires a Research Question, Scope, Context, Approach, a full `## Research Skill Output` from sections 0 through 7, inline epistemic labels, an Evidence Map, and a structured Findings section.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The workflow also requires a self-review covering acronym expansion, inline citations, Evidence Map completeness, confidence alignment, related-item cross-references, and staged-content sanity checks before draft commit.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md] The automated review gate audits citation discipline, speculation control, hollow prose, and evidence sufficiency in Executive Summary, Key Findings, and Analysis.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/.github/copilot-instructions.md; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The documented fallback path for missing skill files directs the agent to follow `research-prompt.md`, so the prompt files and repository instructions are themselves the operational method baseline for current research work.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md] The documented workflow does not require protocol registration or freezing, exact search-string capture, source-coverage declarations, duplicate independent screening, duplicate extraction, exclusion logs with reasons, or a PRISMA-style flow diagram.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The repository uses a three-level `confidence:` field, but its current definition does not require domain-by-domain downgrading for bias, inconsistency, indirectness, imprecision, or missing evidence.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-systematic-review-methodology-ai-synthesis.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md] Prior completed repository work already emphasises provenance preservation, hallucination control, and adversarial review, which shows that downstream claim-integrity controls are an explicit repository design concern.

#### E. Alignment and gap analysis

- [inference; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583; https://training.cochrane.org/handbook/current/chapter-09; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The repository aligns meaningfully with professional standards on transparent question framing, explicit synthesis structure, tabulated evidence, and reviewable reporting artifacts.
- [inference; source: https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04; https://www.campbellcollaboration.org/get-involved/start-a-review/; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The largest gap is upstream, because professional standards require protocolized search and selection artifacts that the current repository workflow does not yet capture.
- [inference; source: https://gdt.gradepro.org/app/handbook/handbook.html; https://amstar.ca/Amstar-2.php; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The second major gap is appraisal and certainty, because professional frameworks require structured bias or certainty judgments while the current workflow mostly infers source credibility from citations and reviewer prose.
- [inference; source: https://link.springer.com/article/10.1186/s12874-025-02583-5; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md] The repository is stronger than conventional review frameworks on Artificial Intelligence-specific output safeguards such as explicit `[fact]`, `[inference]`, and `[assumption]` labeling plus adversarial review, but those controls act after evidence collection and therefore cannot substitute for search, screening, and appraisal controls.
- [inference; source: https://training.cochrane.org/handbook/current/chapter-12; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] The current workflow is therefore best described as a disciplined narrative-synthesis workflow with strong claim-traceability, not as a professional systematic-review or meta-analysis workflow.

### §3 Reasoning

- [fact; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583; https://training.cochrane.org/handbook/current/chapter-03; https://www.campbellcollaboration.org/get-involved/start-a-review/] PRISMA governs reporting transparency, while Cochrane and Campbell govern protocol, search, and synthesis conduct.
- [fact; source: https://gdt.gradepro.org/app/handbook/handbook.html; https://amstar.ca/Amstar-2.php; https://methods.cochrane.org/bias/risk-bias-non-randomized-studies-interventions] GRADE, AMSTAR 2, and ROBINS-I show that professional evidence synthesis expects structured appraisal artifacts rather than only prose-level judgments.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md; https://training.cochrane.org/handbook/current/chapter-04] The right comparison axis is therefore end-to-end method coverage, not whether the repository has high citation discipline in its final write-up.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://training.cochrane.org/handbook/current/chapter-12; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675] On that axis, the repository is strongest in reporting and review, partial in question framing and synthesis discipline, and weakest in search-selection-appraisal controls.

### §4 Consistency Check

- [inference; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583; https://training.cochrane.org/handbook/current/chapter-03; https://www.campbellcollaboration.org/methods/standards/] No contradiction surfaced between PRISMA, Cochrane, and Campbell, because they address complementary layers of review quality rather than competing methods.
- [inference; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://training.cochrane.org/handbook/current/chapter-12] No contradiction surfaced between the repository's Evidence Map discipline and professional standards, because transparent tables and explicit synthesis artifacts are compatible with both.
- [inference; source: https://link.springer.com/article/10.1186/s12874-025-02583-5; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675] No external evidence supports the stronger claim that current Artificial Intelligence tools make upstream review controls unnecessary, so the gap analysis remains one of omission rather than one of deliberate replacement by a validated alternative.

### §5 Depth and Breadth Expansion

- [inference; source: https://training.cochrane.org/handbook/current/chapter-04; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] From a technical lens, the repository optimises for reproducible drafting and review artifacts, but not yet for reproducible evidence retrieval and selection decisions.
- [inference; source: https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md] From a behavioural lens, explicit epistemic labels and adversarial review reduce overconfident prose, but they can become approval theater if the underlying evidence pool was never systematically assembled.
- [inference; source: https://training.cochrane.org/handbook/current/chapter-03; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf] From a historical methods lens, systematic-review standards emerged to control selective citation and opaque judgment, which are the same failure classes a single-agent research loop risks reproducing.
- [inference; source: https://training.cochrane.org/handbook/current/chapter-12; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] From an economic lens, imposing full systematic-review overhead on every repository research item would be wasteful, which argues for a separate heavier skill rather than replacing the current general research workflow.

### §6 Synthesis

**Executive summary:**

The repository's current Artificial Intelligence research workflow is a disciplined narrative-synthesis process, not a professional systematic-review or meta-analysis workflow. [inference; source: https://training.cochrane.org/handbook/current/chapter-12; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf; https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
The current prompts require explicit question framing, Evidence Maps, inline source binding, epistemic labeling, and recursive review. [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md]
However, it does not require frozen protocol artifacts, reproducible search ledgers, inclusion and exclusion decisions with reasons, duplicate screening or extraction, or formal source-appraisal and certainty-grading structures, all of which Cochrane, Campbell, GRADE, and AMSTAR 2 treat as core controls. [inference; source: https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04; https://www.campbellcollaboration.org/get-involved/start-a-review/; https://gdt.gradepro.org/app/handbook/handbook.html; https://amstar.ca/Amstar-2.php; https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
Because current Artificial Intelligence-assisted review evidence still shows meaningful error rates and recommends human oversight, the right design move is a separate systematic-review or meta-analysis skill that adds upstream control artifacts rather than relabeling the current research workflow. [inference; source: https://link.springer.com/article/10.1186/s12874-025-02583-5; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675]

**Key findings:**

1. **Professional review frameworks distinguish reporting quality from review conduct, so PRISMA compliance by itself does not make a workflow methodologically equivalent to a systematic review unless protocol, search, selection, and synthesis controls are also present.** ([fact]; high confidence; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583; https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04)
2. **Cochrane and Campbell treat pre-specified eligibility criteria, reproducible multi-source search, planned grouping for synthesis, and documented protocol stages as core method artifacts rather than optional reviewer preferences.** ([fact]; high confidence; source: https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04; https://www.campbellcollaboration.org/get-involved/start-a-review/; https://www.campbellcollaboration.org/methods/standards/)
3. **The repository's current prompts require explicit scope, question decomposition, Evidence Maps, inline source binding, and recursive review before completion.** ([fact]; high confidence; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md)
4. **The repository's current workflow does not require auditable search strings, source-coverage declarations, exclusion reasons, duplicate screening, or duplicate extraction, which leaves it materially short of professional systematic-review conduct standards.** ([inference]; high confidence; source: https://training.cochrane.org/handbook/current/chapter-04; https://www.campbellcollaboration.org/get-involved/start-a-review/; https://github.com/davidamitchell/Research/blob/main/research-prompt.md)
5. **The current `confidence:` field is directionally similar to certainty grading, but it is much weaker than GRADE because it does not require explicit domain-by-domain judgments about bias, inconsistency, indirectness, imprecision, or missing evidence.** ([inference]; high confidence; source: https://gdt.gradepro.org/app/handbook/handbook.html; https://training.cochrane.org/handbook/current/chapter-14; https://github.com/davidamitchell/Research/blob/main/research-prompt.md)
6. **Current Artificial Intelligence-assisted review evidence supports automation as a screening and triage aid, but it still treats human oversight and methodological safeguards as necessary because Generative Artificial Intelligence systems continue to make substantial synthesis errors.** ([fact]; medium confidence; source: https://link.springer.com/article/10.1186/s12874-025-02583-5; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675; https://rayyan.ai/)
7. **The repository is stronger than many conventional review workflows on Artificial Intelligence-specific output-integrity controls, especially claim labeling, inline provenance, and adversarial review, but those safeguards operate after evidence collection and therefore cannot compensate for upstream selection bias.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md)
8. **A dedicated systematic-review or meta-analysis skill should add a protocol block, search ledger, screening log, source-appraisal matrix, synthesis matrix, and adapted certainty rubric, while leaving the current research workflow in place for lighter narrative-synthesis questions.** ([inference]; medium confidence; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://gdt.gradepro.org/app/handbook/handbook.html; https://github.com/davidamitchell/Research/blob/main/research-prompt.md)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] PRISMA alone is reporting guidance, not full review conduct. | https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583 ; https://training.cochrane.org/handbook/current/chapter-03 | high | reporting layer |
| [fact] Cochrane and Campbell require protocol, search, and documented stages. | https://training.cochrane.org/handbook/current/chapter-03 ; https://training.cochrane.org/handbook/current/chapter-04 ; https://www.campbellcollaboration.org/get-involved/start-a-review/ ; https://www.campbellcollaboration.org/methods/standards/ | high | conduct layer |
| [fact] The current repository prompts require explicit scope, question decomposition, Evidence Maps, inline source binding, and recursive review before completion. | https://github.com/davidamitchell/Research/blob/main/research-prompt.md ; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md | high | prompt-defined |
| [inference] The repository lacks upstream selection artifacts expected by systematic-review standards. | https://training.cochrane.org/handbook/current/chapter-04 ; https://www.campbellcollaboration.org/get-involved/start-a-review/ ; https://github.com/davidamitchell/Research/blob/main/research-prompt.md | high | omission-based |
| [inference] The repository's confidence field is weaker than GRADE certainty grading. | https://gdt.gradepro.org/app/handbook/handbook.html ; https://training.cochrane.org/handbook/current/chapter-14 ; https://github.com/davidamitchell/Research/blob/main/research-prompt.md | high | certainty gap |
| [fact] Artificial Intelligence-assisted review tools improve efficiency but still require oversight. | https://link.springer.com/article/10.1186/s12874-025-02583-5 ; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675 ; https://rayyan.ai/ | medium | automation evidence |
| [inference] Current repository safeguards are stronger on downstream claim integrity than on upstream evidence assembly. | https://github.com/davidamitchell/Research/blob/main/research-prompt.md ; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md | medium | control-surface contrast |
| [inference] The best next step is a separate heavier skill, not a relabel of the current workflow. | https://training.cochrane.org/handbook/current/chapter-09 ; https://training.cochrane.org/handbook/current/chapter-12 ; https://gdt.gradepro.org/app/handbook/handbook.html ; https://github.com/davidamitchell/Research/blob/main/research-prompt.md | medium | design recommendation |

**Assumptions:**

- [assumption; source: https://training.cochrane.org/handbook/current/chapter-12; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] An adapted narrative-synthesis control set is the correct benchmark for most repository research items, because the corpus is heterogeneous and quantitative meta-analysis is explicitly out of scope.
- [assumption; source: https://gdt.gradepro.org/app/handbook/handbook.html; https://amstar.ca/Amstar-2.php; https://jbi.global/critical-appraisal-tools] A repository-specific appraisal rubric can borrow principles from GRADE, AMSTAR 2, and JBI without copying any one clinical-review tool verbatim, because the transferable need is structured domain judgment rather than clinical terminology.

**Analysis:**

The strongest alternative interpretation is that the repository never intended to be a professional systematic-review workflow, so the observed gaps are scope choices rather than defects. [inference; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://training.cochrane.org/handbook/current/chapter-12]
That interpretation is partly correct, because the current workflow is optimized for high-quality narrative synthesis over heterogeneous sources rather than exhaustive study inclusion. [inference; source: https://training.cochrane.org/handbook/current/chapter-12; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf; https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
Even so, the item's question asks whether the workflow measures up against professional standards, and on that stricter test the missing protocol, search, screening, appraisal, and certainty artifacts are decisive gaps. [inference; source: https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04; https://gdt.gradepro.org/app/handbook/handbook.html]
The best design response is therefore two-tiered: keep the current research workflow for exploratory or strategic knowledge notes, and add a dedicated systematic-review or meta-analysis skill for questions where exhaustive capture, formal appraisal, or stronger reproducibility claims are required. [inference; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675]

**Risks, gaps, uncertainties:**

- [inference; source: https://training.cochrane.org/handbook/current/chapter-03; https://www.campbellcollaboration.org/get-involved/start-a-review/] Most formal systematic-review guidance was written for health and social-science evidence synthesis, so some adaptation judgment is unavoidable when applying it to a software and Artificial Intelligence research corpus.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md] This item assesses the documented repository workflow artifacts, not an experimental new skill implementation, so the recommended design has not yet been benchmarked on live repository tasks.
- [inference; source: https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675; https://link.springer.com/article/10.1186/s12874-025-02583-5] Artificial Intelligence-assisted review evidence is improving quickly, so the balance between automation and mandatory human oversight may shift, but the current evidence base still supports caution rather than full autonomy.

**Open questions:**

- What is the smallest protocol and screening ledger that would materially improve repository review quality without making ordinary research items too expensive?
- Should the repository define a source-type appraisal rubric for heterogeneous web sources, or should the dedicated skill only be used for article-heavy evidence sets?
- Should `confidence:` be replaced by a structured certainty table, or should certainty become a separate field only for systematic-review mode?

### §7 Recursive Review

- Coverage check: completed.
- Acronym expansion audit: completed.
- Cross-item sweep: completed.
- [inference; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583; https://training.cochrane.org/handbook/current/chapter-04; https://github.com/davidamitchell/Research/blob/main/research-prompt.md] Overall confidence remains medium because the external standards are strong and consistent, but the repository-alignment judgment still requires adaptation from formal health-review methods to a heterogeneous non-clinical workflow.

---

## Findings

### Executive Summary

The repository's current Artificial Intelligence research workflow is a disciplined narrative-synthesis process, not a professional systematic-review or meta-analysis workflow. [inference; source: https://training.cochrane.org/handbook/current/chapter-12; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf; https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
The current prompts require explicit question framing, Evidence Maps, inline source binding, epistemic labeling, and recursive review. [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md]
However, it does not require frozen protocol artifacts, reproducible search ledgers, inclusion and exclusion decisions with reasons, duplicate screening or extraction, or formal source-appraisal and certainty-grading structures, all of which Cochrane, Campbell, GRADE, and AMSTAR 2 treat as core controls. [inference; source: https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04; https://www.campbellcollaboration.org/get-involved/start-a-review/; https://gdt.gradepro.org/app/handbook/handbook.html; https://amstar.ca/Amstar-2.php; https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
Because current Artificial Intelligence-assisted review evidence still shows meaningful error rates and recommends human oversight, the right design move is a separate systematic-review or meta-analysis skill that adds upstream control artifacts rather than relabeling the current research workflow. [inference; source: https://link.springer.com/article/10.1186/s12874-025-02583-5; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675]

### Key Findings

1. **Professional review frameworks distinguish reporting quality from review conduct, so PRISMA compliance by itself does not make a workflow methodologically equivalent to a systematic review unless protocol, search, selection, and synthesis controls are also present.** ([fact]; high confidence; source: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583; https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04)
2. **Cochrane and Campbell treat pre-specified eligibility criteria, reproducible multi-source search, planned grouping for synthesis, and documented protocol stages as core method artifacts rather than optional reviewer preferences.** ([fact]; high confidence; source: https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04; https://www.campbellcollaboration.org/get-involved/start-a-review/; https://www.campbellcollaboration.org/methods/standards/)
3. **The repository's current prompts require explicit scope, question decomposition, Evidence Maps, inline source binding, and recursive review before completion.** ([fact]; high confidence; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md)
4. **The repository's current workflow does not require auditable search strings, source-coverage declarations, exclusion reasons, duplicate screening, or duplicate extraction, which leaves it materially short of professional systematic-review conduct standards.** ([inference]; high confidence; source: https://training.cochrane.org/handbook/current/chapter-04; https://www.campbellcollaboration.org/get-involved/start-a-review/; https://github.com/davidamitchell/Research/blob/main/research-prompt.md)
5. **The current `confidence:` field is directionally similar to certainty grading, but it is much weaker than GRADE because it does not require explicit domain-by-domain judgments about bias, inconsistency, indirectness, imprecision, or missing evidence.** ([inference]; high confidence; source: https://gdt.gradepro.org/app/handbook/handbook.html; https://training.cochrane.org/handbook/current/chapter-14; https://github.com/davidamitchell/Research/blob/main/research-prompt.md)
6. **Current Artificial Intelligence-assisted review evidence supports automation as a screening and triage aid, but it still treats human oversight and methodological safeguards as necessary because Generative Artificial Intelligence systems continue to make substantial synthesis errors.** ([fact]; medium confidence; source: https://link.springer.com/article/10.1186/s12874-025-02583-5; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675; https://rayyan.ai/)
7. **The repository is stronger than many conventional review workflows on Artificial Intelligence-specific output-integrity controls, especially claim labeling, inline provenance, and adversarial review, but those safeguards operate after evidence collection and therefore cannot compensate for upstream selection bias.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md)
8. **A dedicated systematic-review or meta-analysis skill should add a protocol block, search ledger, screening log, source-appraisal matrix, synthesis matrix, and adapted certainty rubric, while leaving the current research workflow in place for lighter narrative-synthesis questions.** ([inference]; medium confidence; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://gdt.gradepro.org/app/handbook/handbook.html; https://github.com/davidamitchell/Research/blob/main/research-prompt.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] PRISMA alone is reporting guidance, not full review conduct. | https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583 ; https://training.cochrane.org/handbook/current/chapter-03 | high | reporting layer |
| [fact] Cochrane and Campbell require protocol, search, and documented stages. | https://training.cochrane.org/handbook/current/chapter-03 ; https://training.cochrane.org/handbook/current/chapter-04 ; https://www.campbellcollaboration.org/get-involved/start-a-review/ ; https://www.campbellcollaboration.org/methods/standards/ | high | conduct layer |
| [fact] The current repository prompts require explicit scope, question decomposition, Evidence Maps, inline source binding, and recursive review before completion. | https://github.com/davidamitchell/Research/blob/main/research-prompt.md ; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md | high | prompt-defined |
| [inference] The repository lacks upstream selection artifacts expected by systematic-review standards. | https://training.cochrane.org/handbook/current/chapter-04 ; https://www.campbellcollaboration.org/get-involved/start-a-review/ ; https://github.com/davidamitchell/Research/blob/main/research-prompt.md | high | omission-based |
| [inference] The repository's confidence field is weaker than GRADE certainty grading. | https://gdt.gradepro.org/app/handbook/handbook.html ; https://training.cochrane.org/handbook/current/chapter-14 ; https://github.com/davidamitchell/Research/blob/main/research-prompt.md | high | certainty gap |
| [fact] Artificial Intelligence-assisted review tools improve efficiency but still require oversight. | https://link.springer.com/article/10.1186/s12874-025-02583-5 ; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675 ; https://rayyan.ai/ | medium | automation evidence |
| [inference] Current repository safeguards are stronger on downstream claim integrity than on upstream evidence assembly. | https://github.com/davidamitchell/Research/blob/main/research-prompt.md ; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-02-adversarial-review-methods-ai-research-quality.md | medium | control-surface contrast |
| [inference] The best next step is a separate heavier skill, not a relabel of the current workflow. | https://training.cochrane.org/handbook/current/chapter-09 ; https://training.cochrane.org/handbook/current/chapter-12 ; https://gdt.gradepro.org/app/handbook/handbook.html ; https://github.com/davidamitchell/Research/blob/main/research-prompt.md | medium | design recommendation |

### Assumptions

- **Assumption:** An adapted narrative-synthesis control set is the correct benchmark for most repository research items. **Justification:** The corpus is heterogeneous and quantitative effect-size pooling is out of scope. [assumption; source: https://training.cochrane.org/handbook/current/chapter-12; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf; https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
- **Assumption:** A repository-specific appraisal rubric can borrow principles from GRADE, AMSTAR 2, and JBI without copying any one clinical-review tool verbatim. **Justification:** The transferable need is structured domain judgment rather than clinical terminology. [assumption; source: https://gdt.gradepro.org/app/handbook/handbook.html; https://amstar.ca/Amstar-2.php; https://jbi.global/critical-appraisal-tools]

### Analysis

The strongest alternative interpretation is that the repository never intended to be a professional systematic-review workflow, so the observed gaps are scope choices rather than defects. [inference; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://training.cochrane.org/handbook/current/chapter-12]
That interpretation is partly correct, because the current workflow is optimized for high-quality narrative synthesis over heterogeneous sources rather than exhaustive study inclusion. [inference; source: https://training.cochrane.org/handbook/current/chapter-12; http://www.lancaster.ac.uk/shm/research/nssr/research/dissemination/publications/NSsynthesis%20guidance_v1.pdf; https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
Even so, the item's question asks whether the workflow measures up against professional standards, and on that stricter test the missing protocol, search, screening, appraisal, and certainty artifacts are decisive gaps. [inference; source: https://training.cochrane.org/handbook/current/chapter-03; https://training.cochrane.org/handbook/current/chapter-04; https://gdt.gradepro.org/app/handbook/handbook.html]
The best design response is therefore two-tiered: keep the current research workflow for exploratory or strategic knowledge notes, and add a dedicated systematic-review or meta-analysis skill for questions where exhaustive capture, formal appraisal, or stronger reproducibility claims are required. [inference; source: https://training.cochrane.org/handbook/current/chapter-09; https://training.cochrane.org/handbook/current/chapter-12; https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675]

### Risks, Gaps, and Uncertainties

- [inference; source: https://training.cochrane.org/handbook/current/chapter-03; https://www.campbellcollaboration.org/get-involved/start-a-review/] Most formal systematic-review guidance was written for health and social-science evidence synthesis, so some adaptation judgment is unavoidable when applying it to a software and Artificial Intelligence research corpus.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/research-prompt.md; https://github.com/davidamitchell/Research/blob/main/research-review-prompt.md] This item assesses the documented repository workflow artifacts, not an experimental new skill implementation, so the recommended design has not yet been benchmarked on live repository tasks.
- [inference; source: https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis-a-systematic-review/2DACF6D129AA6E46CB8A8740A03D0675; https://link.springer.com/article/10.1186/s12874-025-02583-5] Artificial Intelligence-assisted review evidence is improving quickly, so the balance between automation and mandatory human oversight may shift, but the current evidence base still supports caution rather than full autonomy.

### Open Questions

- What is the smallest protocol and screening ledger that would materially improve repository review quality without making ordinary research items too expensive?
- Should the repository define a source-type appraisal rubric for heterogeneous web sources, or should the dedicated skill only be used for article-heavy evidence sets?
- Should `confidence:` be replaced by a structured certainty table, or should certainty become a separate field only for systematic-review mode?

---

## Output

- Type: knowledge
- Description: This item establishes that the current repository workflow is a narrative-synthesis standard with strong downstream citation controls and recommends a separate systematic-review or meta-analysis skill that adds protocol, search, screening, appraisal, and certainty artifacts. [inference; source: https://training.cochrane.org/handbook/current/chapter-12; https://gdt.gradepro.org/app/handbook/handbook.html; https://github.com/davidamitchell/Research/blob/main/research-prompt.md]
- Links:
  - https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003583
  - https://training.cochrane.org/handbook/current/chapter-04
  - https://gdt.gradepro.org/app/handbook/handbook.html
