---
review_count: 2
title: "Endsley Model of Situational Awareness deep dive"
added: 2026-05-14T10:08:59+00:00
status: reviewing
priority: medium  # low | medium | high
blocks: []
tags: [agentic-ai, evaluation]
started: 2026-05-15T09:40:32+00:00
completed: ~
output: [knowledge]
cites: [2026-05-02-hitl-review-volume-bottleneck-rubber-stamp, 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates, 2026-04-26-human-in-the-loop-ai-automated-workflows]
related: [2026-04-28-uelgf-human-oversight-accountability-layer, 2026-05-01-human-oversight-ai-software-development, 2026-04-30-human-bias-ai-trust-rlhf-sycophancy]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Endsley Model of Situational Awareness deep dive

## Research Question

What is the Endsley Model of situational awareness, meaning the perception of relevant elements, comprehension of their meaning, and projection of their near-future status, how are its three levels defined and operationalised in human factors literature, and what current evidence exists on its usefulness and limitations for evaluating human oversight in highly automated and Artificial Intelligence (AI)-assisted systems?

## Scope

**In scope:**
- The original Endsley definition of Situational Awareness and the three-level model (perception, comprehension, projection)
- Theoretical assumptions behind the model and common measurement approaches used in practice
- Recent peer-reviewed evidence (roughly 2018 onward) on where the model performs well and where critiques identify limitations
- Implications for designing and evaluating Human-in-the-Loop (HITL) oversight in automated and AI-assisted workflows

**Out of scope:**
- Exhaustive survey of all non-Endsley Situational Awareness theories
- Full treatment of domains that do not involve meaningful human oversight decisions
- Product-specific implementation guidance for one vendor tool

**Constraints:**
- Prefer primary sources and peer-reviewed literature over secondary summaries
- Every source listed must include a verifiable web link
- Focus on evidence that can inform practical evaluation criteria for oversight design

## Context

[fact; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/] Human factors literature still treats the Endsley model as the dominant decomposition of situational awareness, so it remains a plausible candidate lens for evaluating what a human reviewer must know before approving, overriding, or halting an automated system.

[fact; source: https://bura.brunel.ac.uk/handle/2438/1422] In the measurement literature, Situation Awareness Global Assessment Technique (SAGAT) means freezing a task and probing state knowledge, Situation Present Assessment Method (SPAM) means real-time probing during ongoing work, and Situation Awareness Rating Technique (SART) means a subjective rating scale for rating awareness-related components.

[inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] This question matters because adjacent repository work already shows that oversight can degrade under queue pressure, and the remaining issue is whether situational awareness explains that failure mechanism well enough to guide measurement and design.

## Approach

1. Reconstruct the original model from primary sources and define each Situational Awareness level precisely.
2. Identify how the model is measured in empirical work (for example, Situation Awareness Global Assessment Technique (SAGAT) and related operational proxies).
3. Review contemporary studies and reviews that apply or critique the model in high-automation settings.
4. Compare supportive vs. critical findings to identify where the model is robust, contested, or misapplied.
5. Translate findings into concrete implications for Human-in-the-Loop oversight design and evaluation in AI-assisted systems.

## Sources

- [ ] [Endsley (1995) Toward a Theory of Situation Awareness in Dynamic Systems](https://doi.org/10.1518/001872095779049543) - foundational paper identified; downstream definitional claims rely on accessible later quotations rather than direct page-cited use of the original article
- [x] [Salmon et al. (2006) Situation awareness measurement: A review of applicability for command, control, communication, computers and intelligence (C4i) environments](https://bura.brunel.ac.uk/handle/2438/1422) - accessible review quoting the canonical definition, summarising the three-level model, and comparing measurement approaches
- [x] [Endsley (2021) A Systematic Review and Meta-Analysis of Direct Objective Measures of Situation Awareness: A Comparison of Situation Awareness Global Assessment Technique (SAGAT) and Situation Present Assessment Method (SPAM)](https://pubmed.ncbi.nlm.nih.gov/31560575/) - meta-analysis of 243 studies on direct objective situational-awareness measures
- [x] [Artman and Garbis (1998) Team communication and coordination as distributed cognition](https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674) - distributed-cognition critique of individual-centred situational-awareness models in team settings
- [x] [Kupfer et al. (2023) Check the box! How to deal with automation bias in AI-based personnel selection](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full) - experiment linking verification intensity to better human review quality
- [x] [Romeo and Conti (2025) Exploring automation bias in human-AI collaboration: a review and implications for explainable AI](https://link.springer.com/article/10.1007/s00146-025-02422-7) - review of workload, trust calibration, and blind reliance in human-AI decision-making
- [x] [Gao et al. (2023) Agent Teaming Situation Awareness (ATSA): A Situation Awareness Framework for Human-AI Teaming](https://arxiv.org/abs/2308.16785) - accessible framework paper extending situational-awareness concepts to human-AI teaming
- [x] [Ignatious et al. (2023) Analyzing Factors Influencing Situation Awareness in Autonomous Vehicles, A Survey](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/) - recent survey showing why highly automated systems need accurate contextual awareness and why maintaining it is technically difficult
- [x] [European Union (2024) AI Act Article 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14) - official human-oversight requirements including automation-bias awareness, override, reverse, and stop capabilities
- [x] [European Union (2024) AI Act Article 26](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26) - official deployer duties covering competent human oversight, monitoring, suspension, and log retention
- [x] [Information Commissioner's Office (ICO) (n.d.) Human review toolkit](https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/) - official guidance on meaningful review, sampling, caseload, independence, and override logs
- [x] [National Institute of Standards and Technology (NIST) (2023) Artificial Intelligence Risk Management Framework (AI RMF) Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) - governance framework for ongoing monitoring, role clarity, and risk-proportionate review

## Related

- [Mitchell (2026) How should human-in-the-loop design be adapted when AI review volume makes human reviewers a bottleneck or causes rubber-stamping?](https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html)
- [Mitchell (2026) What tiered human oversight models maintain meaningful human-in-the-loop control at scale under high-volume multi-step AI adoption, and how should organisations measure oversight quality when productivity mandates exist without explicit quality Key Performance Indicators?](https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html)
- [Mitchell (2026) When and how should human intervention be incorporated into AI-driven and automated workflows?](https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation; Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: assess what the Endsley model says, how the literature operationalises it, and whether it is a useful evaluation lens for human oversight in highly automated and AI-assisted systems.
- Scope: model definition, measurement approaches, recent evidence on usefulness and limitations, and practical implications for Human-in-the-Loop (HITL) oversight design.
- Constraints: prefer primary and peer-reviewed sources, expand acronyms on first use, and separate what the situational-awareness literature supports from what broader oversight-governance sources add.
- Output: knowledge.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html] Prior completed items already show that oversight quality can collapse under volume, that tiered review models outperform universal line-by-line checking at scale, and that meaningful intervention requires authority, telemetry, and escalation design.
- [assumption; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/] Working definition: the item treats the Endsley model as the canonical three-level decomposition of situational awareness because later accessible reviews quote that definition consistently even though this item does not rely on a direct page-cited reading of the 1995 article.

### §1 Question Decomposition

- **Root question:** When does the Endsley model help evaluate human oversight in automated and AI-assisted systems, and where does it fail to capture the real control problem?
- **A. Model-definition branch**
  - A1. How does the literature define situational awareness and its three levels?
  - A2. What assumptions about cognition, decision-making, workload, and interface design are built into the model?
- **B. Measurement branch**
  - B1. Which measures operationalise the three levels in practice?
  - B2. What strengths and weaknesses do review studies report for freeze-probe, real-time-probe, subjective, and observer methods?
- **C. Contemporary automation branch**
  - C1. What recent evidence says the model remains useful for automated or AI-assisted work?
  - C2. What recent evidence says the model becomes incomplete or distorted in highly automated settings?
- **D. Oversight-evaluation branch**
  - D1. Which parts of meaningful oversight map cleanly onto perception, comprehension, and projection?
  - D2. Which parts of meaningful oversight, such as authority, workload, verification behaviour, or distributed coordination, require additional constructs?

### §2 Investigation

#### Source-access and substitution notes

- Access note: the original Endsley (1995) source link was checked, but this item uses accessible later quotations and reviews for downstream definitional claims.
- Access note: the seeded Frontiers and Springer web links resolved to automation-bias evidence rather than to the titles listed in the initial source notes, so the source names were corrected to match the consulted articles.

#### Prior work sweep

- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html] The closest completed repository items converge on the same adjacent oversight prerequisites: intervention rights, queue and caseload visibility, tiered review, and measurable override behaviour.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://bura.brunel.ac.uk/handle/2438/1422] The gap this item must fill is narrower: whether situational awareness is a root explanatory lens for oversight quality, or only one necessary ingredient inside a broader control design.

#### A. Definition and theoretical assumptions

- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422] Salmon et al. quote Endsley's canonical definition of situational awareness as "the perception of the elements in the environment within a volume of time and space, the comprehension of their meaning, and the projection of their status in the near future."
- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422] The same review states that the three-level model treats situational awareness as a product with three hierarchical levels, level 1 perception, level 2 comprehension, and level 3 projection, distinct from the processes used to achieve it.
- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422] Salmon et al. report that the model depicts situational awareness as an essential component of human decision-making activity and that experience, training, workload, and interface design all influence how well operators achieve and maintain it.
- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422] The review also says the model's neat decomposition is one reason most existing situational-awareness measurement techniques are based on it.

#### B. Operationalisation and measurement

- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422] Salmon et al. identify Situation Awareness Global Assessment Technique (SAGAT), Situation Awareness Rating Technique (SART), real-time probes such as Situation Present Assessment Method (SPAM), and observer ratings as major operational families for measuring situational awareness.
- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422] The review explains that SAGAT and related freeze-probe methods pause the task and query participants on task-relevant information, while SPAM uses real-time probes and response times during ongoing work.
- [fact; source: https://pubmed.ncbi.nlm.nih.gov/31560575/] Endsley's 2021 meta-analysis of 243 studies found that SAGAT and SPAM were equally predictive of performance, but SAGAT was more sensitive, 94% versus 64%, and SPAM showed more issues with intrusiveness, sampling bias, speed-accuracy tradeoffs, and workload confounds.
- [fact; source: https://pubmed.ncbi.nlm.nih.gov/31560575/] The same meta-analysis concludes that SAGAT is a highly sensitive, reliable, and predictive direct objective measure that is useful across a wide variety of domains and experimental settings.
- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422] Salmon et al. nonetheless conclude that current measurement techniques are inadequate by themselves for complex command and team environments, and recommend a multiple-measure approach rather than a single metric.
- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422] Salmon et al. further report that most existing measurement approaches still focus on individual operator situational awareness, and that a robust measure of overall or shared team situational awareness had not yet emerged in the literature they reviewed.

#### C. Usefulness in recent automated and AI-assisted settings

- [fact; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full] Kupfer et al. describe automation bias as the thoughtless acceptance of AI-based recommendations and show that higher verification intensity correlates with higher objective decision quality in AI-assisted personnel selection.
- [fact; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full] In the same experiment, briefing decision makers about possible system errors increased verification intensity, while simply reminding them of responsibility did not, and less aggregated data encouraged deeper evidence inspection.
- [fact; source: https://link.springer.com/article/10.1007/s00146-025-02422-7] Romeo and Conti report that high workload shifts attention away from checking automation, increases delayed detection of errors, and makes trust calibration central to preventing blind reliance in human-AI decision-making.
- [fact; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/] Ignatious et al. argue that accurate situational awareness is a crucial prerequisite for effective decision-making in highly automated driving, while also showing that heterogeneous sensors, multimodal data fusion, and context ambiguity make that awareness difficult to maintain.
- [fact; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14] Article 14 of the European Union AI Act makes the oversight relevance of situational awareness explicit by requiring reviewers to understand relevant capacities and limitations, detect anomalies and unexpected performance, interpret outputs correctly, and remain aware of automation bias.
- [fact; source: https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] The Information Commissioner's Office human review toolkit extends this into practice by requiring meaningful review, documented sampling and tolerances, override logs, reviewer independence, and manageable caseload.

#### D. Limits and critiques

- [fact; source: https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674] Artman and Garbis argue that predominant situational-awareness models are inadequate for team-operated systems because they rely on mentalistic assumptions focused almost exclusively on individuals.
- [fact; source: https://bura.brunel.ac.uk/handle/2438/1422; https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674] Salmon et al. report the same critique in their review and quote distributed-cognition work that treats team situational awareness as partly shared and partly distributed across agents and artefacts.
- [fact; source: https://arxiv.org/abs/2308.16785] Gao et al.'s Agent Teaming Situation Awareness framework says classical individual and team models need extension for human-AI teaming because AI agents introduce bidirectional, dynamic interactions and new coordination constructs such as teaming understanding and teaming control.
- [assumption; source: https://arxiv.org/abs/2308.16785; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/] The human-AI extension literature is still less mature than the classical situational-awareness measurement literature, so claims about the best human-AI-specific situational-awareness framework should be treated as emerging rather than settled.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://link.springer.com/article/10.1007/s00146-025-02422-7] For oversight evaluation, the practical limitation is that the three levels omit reviewer authority, queue pressure, team coordination, and other socio-technical conditions that determine whether awareness turns into intervention.

### §3 Reasoning

- [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/] The strongest evidence supports two narrow propositions: the three-level model remains the dominant decomposition in human factors, and direct objective measurement with SAGAT is useful and often robust.
- [inference; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] The modern oversight question is broader than raw awareness, because verification behaviour, workload, and intervention rights determine whether a human who could in principle perceive and understand a situation will actually challenge the machine.
- [inference; source: https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674; https://arxiv.org/abs/2308.16785; https://bura.brunel.ac.uk/handle/2438/1422] The evidence therefore supports a limited-scope interpretation: Endsley's levels help specify what information an overseer needs, while additional team and governance constructs are required before the model can evaluate real oversight quality in highly automated systems.

### §4 Consistency Check

- [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/] Salmon et al. and Endsley (2021) point in the same direction on direct measurement, while Salmon et al. remain more sceptical about the sufficiency of any single measure in complex team environments.
- [inference; source: https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674; https://arxiv.org/abs/2308.16785] The distributed-cognition and human-AI teaming sources extend the individual model by preserving awareness as important while shifting the unit of analysis toward a joint cognitive system.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/] Official oversight guidance fits that extended reading because it requires understanding and interpretation while also adding controls for authority, override, independence, and workload.

### §5 Depth and Breadth Expansion

- [fact; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/] Technical lens: highly automated systems make situational awareness harder because relevant cues are assembled through sensor fusion, model inference, and rapidly changing context rather than through a simple visible operating picture.
- [fact; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7] Behavioural lens: verification intensity and trust calibration are observable intermediaries between awareness and intervention, so any oversight assessment that measures awareness alone can miss the actual failure mode.
- [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] Governance lens: current policy and regulator guidance combine reviewer competence, monitoring, logs, fallback options, and real stop-or-override power, which means situational awareness is only one control surface among several.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full] This repo's earlier oversight items remain valid under the Endsley lens, and this item adds a more specific explanation for why rubber-stamping often reflects degraded comprehension and projection rather than only missing policy.

### §6 Synthesis

**Executive summary:**

- Endsley's three-level model remains a useful decomposition for evaluating human oversight because it specifies the minimum information a reviewer must perceive, understand, and project before intervening in an automated system. [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/]
- Current evidence does not support using the model as a complete oversight-evaluation framework in highly automated or AI-assisted settings, because modern failure modes also depend on workload, automation bias, reviewer authority, and coordination across people and artefacts. [inference; source: https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674; https://link.springer.com/article/10.1007/s00146-025-02422-7; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]
- Human factors measurement research supports using direct objective measures such as SAGAT, supplemented by workload, override-log, and review-quality metrics, rather than relying on a single situational-awareness score. [inference; source: https://pubmed.ncbi.nlm.nih.gov/31560575/; https://bura.brunel.ac.uk/handle/2438/1422; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]
- For modern AI oversight, the best-supported use of the Endsley model is as one component of a broader governance assessment that combines interface legibility, reviewer verification behaviour, caseload, and real stop-or-override power. [inference; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]

**Key findings:**

1. **The Endsley model still anchors human factors work because it decomposes situational awareness into perception, comprehension, and projection, and later reviews treat that three-level structure as the dominant conceptual basis for measurement and interface evaluation.** ([fact]; high confidence; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/)
2. **Human factors literature operationalises the model through several measurement families, especially SAGAT freeze probes, SPAM real-time probes, SART subjective ratings, and observer assessments, but review work recommends combining methods because no single measure captures complex team environments well enough on its own.** ([fact]; high confidence; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/)
3. **The strongest current direct-measure evidence appears to favour SAGAT, because Endsley's 2021 meta-analysis found it more sensitive than SPAM and free of several confounds that affect real-time probe methods, even though both predict performance.** ([inference]; medium confidence; source: https://pubmed.ncbi.nlm.nih.gov/31560575/)
4. **Recent AI-assisted decision-support evidence suggests that situational awareness improves oversight quality only when the interface and workflow sustain active verification, since error briefings and less aggregated evidence improve review quality more reliably than generic reminders of reviewer responsibility.** ([inference]; medium confidence; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7)
5. **Highly automated systems still require accurate situational awareness for safe decisions, and the technical challenge rises because context is assembled through sensor fusion, model inference, and rapidly changing machine behaviour rather than through a stable human-observable operating picture.** ([inference]; medium confidence; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/; https://arxiv.org/abs/2308.16785)
6. **The main theoretical limitation for oversight evaluation is that classical situational-awareness models are primarily individual-centred, while team and distributed-cognition critiques argue that effective oversight in complex socio-technical systems is distributed across people, artefacts, and coordination practices.** ([fact]; medium confidence; source: https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674; https://bura.brunel.ac.uk/handle/2438/1422; https://arxiv.org/abs/2308.16785)
7. **Official oversight guidance supports a limited-scope reading of the model, because regulators require understanding system limits and outputs while also requiring override rights, stop capability, competent staffing, monitoring, logs, independence, and manageable caseload.** ([inference]; high confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
8. **Compared with prior repository work, the evidence here suggests that queue pressure and weak governance often erode Level 2 comprehension and Level 3 projection before they eliminate nominal human sign-off.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] The three-level model remains the dominant decomposition of situational awareness in later human factors reviews. | https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/ | high | Definition and decomposition |
| [fact] Situational-awareness measurement is usually operationalised through SAGAT, SPAM, SART, and observer or mixed methods, with multi-measure use recommended for complex settings. | https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/ | high | Operationalisation |
| [inference] SAGAT currently appears to have the strongest direct objective evidence base among mainstream situational-awareness measures. | https://pubmed.ncbi.nlm.nih.gov/31560575/ | medium | Sensitivity and confounds |
| [inference] Verification behaviour mediates whether situational awareness improves human review quality in AI-assisted decisions. | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7 | medium | Automation bias evidence |
| [inference] Highly automated systems need accurate situational awareness, and sensor fusion and contextual ambiguity make it harder to sustain. | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/; https://arxiv.org/abs/2308.16785 | medium | Technical complexity |
| [fact] Distributed and team critiques show that classical individual-centred situational-awareness models are incomplete for complex socio-technical oversight. | https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674; https://bura.brunel.ac.uk/handle/2438/1422; https://arxiv.org/abs/2308.16785 | medium | Unit of analysis |
| [inference] Official oversight guidance requires situational awareness plus override, staffing, logging, and monitoring controls. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | high | Governance bundle |
| [inference] Prior repository rubber-stamp findings are partly explainable as degraded comprehension and projection rather than only missing policy. | https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full | medium | Cross-item synthesis |

**Assumptions:**

- [assumption; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/] Later accessible reviews quote the 1995 definition accurately enough that this item can analyse the model without a direct page-cited reading of the original article.
- [assumption; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/] Evidence from AI-assisted personnel selection, general human-AI decision support, and highly automated driving transfers to enterprise oversight because the common mechanism is human verification under automation, uncertainty, and workload.
- [assumption; source: https://arxiv.org/abs/2308.16785; https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674] Recent human-AI teaming extensions are directionally useful for this item even though the accessible ATSA source is a preprint rather than a peer-reviewed journal article.

**Analysis:**

The evidence clusters into model, measurement, behavioural, and governance strands that point in the same direction. [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14]
Within the model strand, the Endsley framework remains valuable because it makes oversight legibility testable, namely whether reviewers can see the right cues, understand them, and anticipate what will happen next if they do or do not intervene. [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14]
Measurement studies support direct probes such as SAGAT, yet the review literature also shows that team settings, dynamic queues, and real-time work require mixed measures because a single situational-awareness score can miss workload and coordination failures. [inference; source: https://pubmed.ncbi.nlm.nih.gov/31560575/; https://bura.brunel.ac.uk/handle/2438/1422]
Recent automation-bias studies materially strengthen the case for broader oversight metrics, because better awareness cues only help when the workflow produces active checking instead of passive acceptance. [inference; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7]
Official oversight sources complete the picture by adding authority, competence, staffing, logs, monitoring, and fallback, which makes the Endsley model most useful as a sub-framework inside a broader oversight assessment. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/]

**Risks, gaps, uncertainties:**

- The foundational 1995 paper is represented here through later accessible quotations and reviews rather than direct page-cited use of the original article, so claims about subtle theoretical nuances should be treated cautiously. [assumption; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/]
- Recent human-AI situational-awareness extension work is thinner and less settled than the classical measurement literature, and one important accessible source in this item is a 2023 preprint rather than a peer-reviewed journal paper. [assumption; source: https://arxiv.org/abs/2308.16785]
- Most direct objective measurement evidence comes from simulations or bounded experimental tasks rather than from live enterprise oversight queues, which limits external validity for large-scale production review environments. [inference; source: https://pubmed.ncbi.nlm.nih.gov/31560575/; https://bura.brunel.ac.uk/handle/2438/1422; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]

**Open questions:**

- Which mixed measurement bundle best captures team-level situational awareness in production human-AI oversight queues without interrupting work?
- Can verification-intensity signals be instrumented cheaply enough to serve as a routine enterprise oversight metric rather than only an experimental construct?
- Which interface patterns most reliably improve Level 2 comprehension and Level 3 projection for reviewers supervising Large Language Model (LLM) systems?
### §7 Recursive Review

- Review result: provisional pass after internal logic, acronym, citation, and parity checks.
- Acronym audit: Artificial Intelligence (AI), Human-in-the-Loop (HITL), Situation Awareness Global Assessment Technique (SAGAT), Situation Present Assessment Method (SPAM), Situation Awareness Rating Technique (SART), Artificial Intelligence Risk Management Framework (AI RMF), command, control, communication, computers and intelligence (C4i), Large Language Model (LLM), Agent Teaming Situation Awareness (ATSA).
- Claim audit: all factual and inferential prose in Research Skill Output is labeled; Findings mirror Section 6 content.
- Remaining uncertainty: human-AI-specific framework claims stay at medium confidence because the accessible extension literature is thinner than the classical situational-awareness measurement literature.

---

## Findings

### Executive Summary

Endsley's three-level model remains a useful decomposition for evaluating human oversight because it specifies the minimum information a reviewer must perceive, understand, and project before intervening in an automated system. [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/]

Current evidence does not support using the model as a complete oversight-evaluation framework in highly automated or AI-assisted settings, because modern failure modes also depend on workload, automation bias, reviewer authority, and coordination across people and artefacts. [inference; source: https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674; https://link.springer.com/article/10.1007/s00146-025-02422-7; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]

Human factors measurement research supports using direct objective measures such as SAGAT, supplemented by workload, override-log, and review-quality metrics, rather than relying on a single situational-awareness score. [inference; source: https://pubmed.ncbi.nlm.nih.gov/31560575/; https://bura.brunel.ac.uk/handle/2438/1422; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]

For modern AI oversight, the best-supported use of the Endsley model is as one component of a broader governance assessment that combines interface legibility, reviewer verification behaviour, caseload, and real stop-or-override power. [inference; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html]

### Key Findings

1. **The Endsley model still anchors human factors work because it decomposes situational awareness into perception, comprehension, and projection, and later reviews treat that three-level structure as the dominant conceptual basis for measurement and interface evaluation.** ([fact]; high confidence; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/)
2. **Human factors literature operationalises the model through several measurement families, especially SAGAT freeze probes, SPAM real-time probes, SART subjective ratings, and observer assessments, but review work recommends combining methods because no single measure captures complex team environments well enough on its own.** ([fact]; high confidence; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/)
3. **The strongest current direct-measure evidence appears to favour SAGAT, because Endsley's 2021 meta-analysis found it more sensitive than SPAM and free of several confounds that affect real-time probe methods, even though both predict performance.** ([inference]; medium confidence; source: https://pubmed.ncbi.nlm.nih.gov/31560575/)
4. **Recent AI-assisted decision-support evidence suggests that situational awareness improves oversight quality only when the interface and workflow sustain active verification, since error briefings and less aggregated evidence improve review quality more reliably than generic reminders of reviewer responsibility.** ([inference]; medium confidence; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7)
5. **Highly automated systems still require accurate situational awareness for safe decisions, and the technical challenge rises because context is assembled through sensor fusion, model inference, and rapidly changing machine behaviour rather than through a stable human-observable operating picture.** ([inference]; medium confidence; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/; https://arxiv.org/abs/2308.16785)
6. **The main theoretical limitation for oversight evaluation is that classical situational-awareness models are primarily individual-centred, while team and distributed-cognition critiques argue that effective oversight in complex socio-technical systems is distributed across people, artefacts, and coordination practices.** ([fact]; medium confidence; source: https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674; https://bura.brunel.ac.uk/handle/2438/1422; https://arxiv.org/abs/2308.16785)
7. **Official oversight guidance supports a limited-scope reading of the model, because regulators require understanding system limits and outputs while also requiring override rights, stop capability, competent staffing, monitoring, logs, independence, and manageable caseload.** ([inference]; high confidence; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)
8. **Compared with prior repository work, the evidence here suggests that queue pressure and weak governance often erode Level 2 comprehension and Level 3 projection before they eliminate nominal human sign-off.** ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] The three-level model remains the dominant decomposition of situational awareness in later human factors reviews. | https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/ | high | Definition and decomposition |
| [fact] Situational-awareness measurement is usually operationalised through SAGAT, SPAM, SART, and observer or mixed methods, with multi-measure use recommended for complex settings. | https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/ | high | Operationalisation |
| [inference] SAGAT currently appears to have the strongest direct objective evidence base among mainstream situational-awareness measures. | https://pubmed.ncbi.nlm.nih.gov/31560575/ | medium | Sensitivity and confounds |
| [inference] Verification behaviour mediates whether situational awareness improves human review quality in AI-assisted decisions. | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7 | medium | Automation bias evidence |
| [inference] Highly automated systems need accurate situational awareness, and sensor fusion and contextual ambiguity make it harder to sustain. | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/; https://arxiv.org/abs/2308.16785 | medium | Technical complexity |
| [fact] Distributed and team critiques show that classical individual-centred situational-awareness models are incomplete for complex socio-technical oversight. | https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674; https://bura.brunel.ac.uk/handle/2438/1422; https://arxiv.org/abs/2308.16785 | medium | Unit of analysis |
| [inference] Official oversight guidance requires situational awareness plus override, staffing, logging, and monitoring controls. | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/ | high | Governance bundle |
| [inference] Prior repository rubber-stamp findings are partly explainable as degraded comprehension and projection rather than only missing policy. | https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.html; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full | medium | Cross-item synthesis |

### Assumptions

- [assumption; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/] Later accessible reviews quote the 1995 definition accurately enough that this item can analyse the model without a direct page-cited reading of the original article.
- [assumption; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10142809/] Evidence from AI-assisted personnel selection, general human-AI decision support, and highly automated driving transfers to enterprise oversight because the common mechanism is human verification under automation, uncertainty, and workload.
- [assumption; source: https://arxiv.org/abs/2308.16785; https://www.diva-portal.org/smash/record.jsf?pid=diva2:479674] Recent human-AI teaming extensions are directionally useful for this item even though the accessible ATSA source is a preprint rather than a peer-reviewed journal article.

### Analysis

The evidence clusters into model, measurement, behavioural, and governance strands that point in the same direction. [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14]

Within the model strand, the Endsley framework remains valuable because it makes oversight legibility testable, namely whether reviewers can see the right cues, understand them, and anticipate what will happen next if they do or do not intervene. [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14]

Measurement studies support direct probes such as SAGAT, yet the review literature also shows that team settings, dynamic queues, and real-time work require mixed measures because a single situational-awareness score can miss workload and coordination failures. [inference; source: https://pubmed.ncbi.nlm.nih.gov/31560575/; https://bura.brunel.ac.uk/handle/2438/1422]

Recent automation-bias studies materially strengthen the case for broader oversight metrics, because better awareness cues only help when the workflow produces active checking instead of passive acceptance. [inference; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1118723/full; https://link.springer.com/article/10.1007/s00146-025-02422-7]

Official oversight sources complete the picture by adding authority, competence, staffing, logs, monitoring, and fallback, which makes the Endsley model most useful as a sub-framework inside a broader oversight assessment. [inference; source: https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/]

### Risks, Gaps, and Uncertainties

- The foundational 1995 paper is represented here through later accessible quotations and reviews rather than direct page-cited use of the original article, so claims about subtle theoretical nuances should be treated cautiously. [assumption; source: https://bura.brunel.ac.uk/handle/2438/1422; https://pubmed.ncbi.nlm.nih.gov/31560575/]
- Recent human-AI situational-awareness extension work is thinner and less settled than the classical measurement literature, and one important accessible source in this item is a 2023 preprint rather than a peer-reviewed journal paper. [assumption; source: https://arxiv.org/abs/2308.16785]
- Most direct objective measurement evidence comes from simulations or bounded experimental tasks rather than from live enterprise oversight queues, which limits external validity for large-scale production review environments. [inference; source: https://pubmed.ncbi.nlm.nih.gov/31560575/; https://bura.brunel.ac.uk/handle/2438/1422; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]

### Open Questions

- Which mixed measurement bundle best captures team-level situational awareness in production human-AI oversight queues without interrupting work?
- Can verification-intensity signals be instrumented cheaply enough to serve as a routine enterprise oversight metric rather than only an experimental construct?
- Which interface patterns most reliably improve Level 2 comprehension and Level 3 projection for reviewers supervising Large Language Model (LLM) systems?

---

## Output

- Type: knowledge
- Description: This item produces a research synthesis that treats the Endsley model as a necessary but incomplete control lens for evaluating human oversight in highly automated and AI-assisted systems. [inference; source: https://bura.brunel.ac.uk/handle/2438/1422; https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14; https://ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/artificial-intelligence/human-review/]
- Links:
  - https://bura.brunel.ac.uk/handle/2438/1422
  - https://pubmed.ncbi.nlm.nih.gov/31560575/
  - https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14
