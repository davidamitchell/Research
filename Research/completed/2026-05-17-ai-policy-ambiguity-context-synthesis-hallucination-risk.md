---
review_count: 1
title: "Context mismatch and hallucination risks in Artificial Intelligence (AI) policy interpretation"
added: 2026-05-17T20:33:05+00:00
status: completed
priority: high
blocks: []
started: 2026-05-17T22:24:35+00:00
completed: 2026-05-17T22:45:49+00:00
output: [knowledge]
themes: [llm-reasoning, memory-context, governance-policy, security-risk, agentic-ai, organisational-design, benchmarks-eval]
cites:
  - 2026-05-17-ai-policy-ambiguity-accountability-governance-risk
  - 2026-05-17-ai-policy-ambiguity-cognitive-closure-confirmation-bias-risk
  - 2026-05-09-governance-policy-determinism-vs-stochastic-llm
  - 2026-04-30-human-bias-ai-trust-rlhf-sycophancy
  - 2026-04-26-policy-coherence-machine-checkable-prerequisite
related:
  - 2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates
  - 2026-04-26-human-in-the-loop-ai-automated-workflows
  - 2026-04-26-policy-coherence-machine-checkable-prerequisite
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: "49573db72d0f085ad0d22f95ded8b9bdc91e1a73"
    changed: 2026-05-17
    progress: "progress/2026-05-17-ai-policy-ambiguity-context-synthesis-hallucination-risk.md"
    summary: "Initial completion"
---

# Context mismatch and hallucination risks in Artificial Intelligence (AI) policy interpretation

## Research Question

What failure modes emerge when Large Language Models (LLMs) combine generic public legal knowledge with proprietary organisational policy in compliance interpretation tasks?

## Scope

**In scope:**
- Catalogue cases where the model recommends plausible but inapplicable external standards, laws, or policy readings.
- Assess how training priors and broad public knowledge can misalign with local risk appetite, internal controls, and organisation-specific exceptions.
- Evaluate the evidence that users miss context mismatch or fabricated applicability when reviewing policy outputs.

**Out of scope:**
- Implementing production policy-assistant software.
- Entity-specific legal advice.
- Exhaustive jurisdiction-by-jurisdiction legal analysis.

**Constraints:** Use publicly available sources, distinguish demonstrated evidence from inference, and prioritise sources with explicit governance or empirical grounding.

## Context

[inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-cognitive-closure-confirmation-bias-risk.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md] Adjacent completed repository items already show that ambiguous policy interpretation becomes harder to justify when accountability blurs, when users seek quick closure, and when stochastic model outputs sit too close to the final governance decision surface, so this item isolates the narrower question of how generic public knowledge and weak local grounding produce authoritative but inapplicable answers.

## Approach

1. Identify the main ways Large Language Models produce plausible but inapplicable answers in legal and policy interpretation.
2. Assess whether weak use of long or noisy context lets public legal priors override local policy text.
3. Evaluate how users respond to such outputs, especially whether they detect mismatch or over-trust the answer.
4. Synthesize the strongest assurance and workflow controls for organisation-specific policy interpretation.

## Sources

- [x] [National Institute of Standards and Technology (NIST) AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [x] [Autio et al. (2024) Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [x] [United Kingdom (UK) Government Introduction to Artificial Intelligence Assurance](https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance)
- [x] [United Kingdom (UK) Government Portfolio of Artificial Intelligence Assurance Techniques](https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques)
- [x] [United Kingdom (UK) Government Guidance to Civil Servants on Use of Generative Artificial Intelligence](https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai)
- [x] [United Kingdom (UK) Government Generative Artificial Intelligence Framework for His Majesty's Government (HMG)](https://www.gov.uk/government/publications/generative-ai-framework-for-hmg)
- [x] [Government Digital Service (2024) The findings of our first generative Artificial Intelligence experiment: GOV.UK Chat](https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/)
- [x] [OpenAI et al. (2024) Generative Pre-trained Transformer 4 (GPT-4) Technical Report](https://arxiv.org/abs/2303.08774)
- [x] [Dahl et al. (2024) Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models](https://arxiv.org/abs/2401.01301)
- [x] [Stanford Human-Centered Artificial Intelligence (2024) Hallucinating Law: Legal Mistakes with Large Language Models are Pervasive](https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive)
- [x] [Chen et al. (2023) Large Language Models Can Be Easily Distracted by Irrelevant Context](https://arxiv.org/abs/2302.00093)
- [x] [Liu et al. (2023) Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [x] [BehnamGhader et al. (2023) Can Retriever-Augmented Language Models Reason? The Blame Game Between the Retriever and the Language Model](https://aclanthology.org/2023.findings-emnlp.1036/)
- [x] [Li et al. (2025) Large Language Models are overconfident and amplify human bias](https://arxiv.org/abs/2505.02151)
- [x] [Goddard et al. (2012) Automation bias: a systematic review of frequency, effect mediators, and mitigators](https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/)
- [x] [Vicente and Matute (2024) The impact of Artificial Intelligence errors in a human-in-the-loop process](https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/)
- [x] [Jussupow et al. (2024) Putting a human in the loop: Increasing uptake, but decreasing accuracy of automated decision-making](https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/)
- [x] [Mitchell (2026) Accountability and governance risks in Artificial Intelligence-assisted policy interpretation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md)
- [x] [Mitchell (2026) Pressure for quick closure and confirmation-bias risks in Artificial Intelligence policy interpretation](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-cognitive-closure-confirmation-bias-risk.md)
- [x] [Mitchell (2026) Governance Policy Application: Deterministic Requirements vs Stochastic Large Language Model Elements](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md)
- [x] [Mitchell (2026) Human cognitive bias toward Artificial Intelligence correctness and explainability](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md)
- [x] [Mitchell (2026) Policy coherence as a machine-checkable prerequisite](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md)

## Related

- [Mitchell (2026) What tiered human oversight models maintain meaningful human-in-the-loop control at scale?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.md)
- [Mitchell (2026) When and how should human intervention be incorporated into Artificial Intelligence-driven and automated workflows?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md)
- [Mitchell (2026) Policy coherence as a machine-checkable prerequisite](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and Section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: what failure modes emerge when an LLM combines broad public legal knowledge with proprietary organisational policy in a compliance interpretation task?
- Scope: plausible but inapplicable standards, weak use of local context, user detection of mismatch, and assurance controls that reduce those failures.
- Constraints: public sources only, URL-backed citations, explicit fact-inference-assumption labels, and prior completed-item cross-reference before synthesis.
- Output: knowledge, full mode.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-cognitive-closure-confirmation-bias-risk.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md] Prior-work cross-reference: the closest completed items already establish the adjacent control surfaces, namely blurred accountability, quick-closure pressure, deterministic-governance requirements, and human over-trust of polished Artificial Intelligence output.
- [assumption; source: https://arxiv.org/abs/2401.01301; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/] Working assumption: legal question answering, public-sector grounded chat, and human-review experiments are close enough proxies for enterprise policy assistants because each setting requires humans to evaluate authoritative-seeming machine output against a controlling text under uncertainty. Justification: direct public studies of proprietary internal policy corpora remain sparse.

### §1 Question Decomposition

- **Root question:** when a policy assistant mixes public legal priors with local policy text, what specific failure modes appear and why do users miss them?
- **A. Baseline model failure**
  - A1. Do general-purpose Large Language Models generate false legal statements, fabricated applicability, or confident answers to false premises?
  - A2. Are these failures worse on complex, local, or lower-salience legal questions?
- **B. Context-use failure**
  - B1. Do Large Language Models reliably use long or noisy context?
  - B2. Do retrieval-augmented systems reliably fetch and reason over all required local statements?
  - B3. What happens when the controlling policy text is long, buried, exception-heavy, or ambiguous?
- **C. Human detection failure**
  - C1. Do humans catch erroneous machine recommendations when shown the recommendation first?
  - C2. Does a human-in-the-loop design itself guarantee correction?
  - C3. Do confidence and institutional trust make wrong answers feel safer than they are?
- **D. Governance and mitigation**
  - D1. Which official sources require context-specific testing, compliance audit, and human review?
  - D2. Which workflow controls reduce the risk that public priors override local policy?
- **E. Synthesis**
  - E1. What is the dominant failure mode?
  - E2. Which controls belong in the model-drafting step and which belong in the final decision step?

### §2 Investigation

#### Source replacement and prior-item sweep

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-cognitive-closure-confirmation-bias-risk.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md] Repeated completed-item sweep: adjacent repository work strengthens the interpretation that this item is about a specific blend of hallucination, closure pressure, and governance-boundary failure rather than about generic model error alone.

#### A. General-purpose legal interpretation already fails in ways that map onto policy-applicability risk

- [fact; source: https://arxiv.org/abs/2303.08774] OpenAI's GPT-4 technical report states that GPT-4 is not fully reliable, can suffer from hallucinations, has a limited context window, and requires care in contexts where reliability is important.
- [fact; source: https://arxiv.org/abs/2401.01301] Dahl et al. report that legal hallucinations occurred between 58 percent of the time with ChatGPT 4 and 88 percent with Llama 2 on specific verifiable legal queries.
- [fact; source: https://arxiv.org/abs/2401.01301] The same paper finds that Large Language Models often fail to correct a user's incorrect legal assumptions and do not always know when they are hallucinating.
- [fact; source: https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive] The Stanford summary of the same study says hallucinations worsen on more complex legal tasks, on localized lower-court material, and on prompts built on false premises.
- [fact; source: https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive] The Stanford summary also says current models show overconfidence on complex legal tasks and on lower-court material where actual accuracy is weaker.
- [inference; source: https://arxiv.org/abs/2303.08774; https://arxiv.org/abs/2401.01301; https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive] In a compliance assistant, this baseline legal failure mode translates into authoritative but inapplicable answers, because the model can confidently compose a broadly plausible legal or policy rule without proving that the rule actually governs the organisation's local policy context.

#### B. Long, noisy, or weakly retrieved local context makes public priors harder to override

- [fact; source: https://arxiv.org/abs/2302.00093] Chen et al. find that model performance drops dramatically when irrelevant context is added to a task, which shows that even non-adversarial noise can derail reasoning.
- [fact; source: https://arxiv.org/abs/2307.03172] Liu et al. find that language-model performance is highest when relevant information appears at the beginning or end of long context and significantly degrades when the relevant information sits in the middle.
- [fact; source: https://aclanthology.org/2023.findings-emnlp.1036/] BehnamGhader et al. find that simple similarity-based retrieval is insufficient to fetch all statements required for reasoning, and that the language models still do not reason strongly even when provided only the required statements.
- [fact; source: https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/] The GOV.UK Chat team reports that some queries could not be answered because the GOV.UK page was too long, that chunking strategy needed improvement, and that a few hallucinations appeared mostly on ambiguous or inappropriate queries.
- [fact; source: https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai] United Kingdom civil-service guidance says generative Artificial Intelligence output can mislead, can derive answers from sources a user would not trust in other contexts, and requires the user to consider what context the tool might have missed.
- [inference; source: https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai] When organisation-specific policy is long, buried in the middle of a large context window, or retrieved imperfectly, the model has multiple paths to a wrong answer that still sounds valid, including ignoring the controlling exception, overweighting a generic public norm, or blending both into a synthetic but non-authoritative interpretation.

#### C. Users do not reliably detect these mismatches once the model speaks first

- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] Goddard et al. define automation bias as over-reliance on automated decision support and identify workload, task complexity, time pressure, trust, and confidence as mediators.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] The same review identifies mitigators including training, emphasizing user accountability, confidence cues, and providing information rather than bare recommendations.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/] Vicente and Matute find that incorrect Artificial Intelligence support reduces human accuracy more strongly when participants receive it before providing their own judgment.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/] Vicente and Matute also note that many real public-sector human-in-the-loop flows present system support first and then ask the human to validate or modify it.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/] Jussupow et al. find that participants followed algorithmic recommendations more closely than equally accurate human recommendations and were less likely to intervene on the least accurate recommendations.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/] The same study concludes that keeping a human in the loop increased uptake of algorithmic support but decreased decision accuracy.
- [fact; source: https://arxiv.org/abs/2505.02151] Li et al. find that all five studied Large Language Models were overconfident and that Large Language Model input more than doubled the extent of human overconfidence in answers.
- [fact; source: https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/] The GOV.UK Chat team found that some users underestimated or dismissed inaccuracy risks because of the credibility and duty of care associated with the GOV.UK brand.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://arxiv.org/abs/2505.02151; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/] A policy assistant therefore does not just risk saying the wrong thing, it also risks making the wrong thing harder to catch, especially when the answer is shown before independent analysis and is wrapped in the trust signals of a familiar internal tool or authoritative information brand.

#### D. Official guidance points to assurance and workflow controls, not generic trust in model capability

- [fact; source: https://www.nist.gov/itl/ai-risk-management-framework] NIST describes the Artificial Intelligence Risk Management Framework as a voluntary framework for incorporating trustworthiness considerations into the design, development, use, and evaluation of Artificial Intelligence products, services, and systems.
- [fact; source: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence] NIST's Generative Artificial Intelligence Profile is a cross-sectoral profile for generative Artificial Intelligence risk pursuant to Executive Order 14110 and is meant to help organizations incorporate trustworthiness considerations into use and evaluation.
- [fact; source: https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance] The United Kingdom Introduction to Artificial Intelligence assurance says assurance is part of wider organisational risk management and builds confidence by measuring and evaluating evidence that systems will work as intended, what limitations they hold, and what risks they pose.
- [fact; source: https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques] The United Kingdom portfolio says assurance checks whether an Artificial Intelligence system meets regulation, standards, ethical guidelines, and organisational values, and lists compliance audits, performance testing, formal verification, and impact assessment as relevant techniques across the lifecycle.
- [fact; source: https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai] The civil-service guidance says outputs from generative Artificial Intelligence are susceptible to bias and misinformation and must be checked and cited appropriately.
- [fact; source: https://www.gov.uk/government/publications/generative-ai-framework-for-hmg; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/] The United Kingdom government positioned the Generative Artificial Intelligence Framework and the GOV.UK Chat pilot as guidance for careful phased experimentation, and the pilot relied on internal testing, red teaming, expert human assessment of responses, and iterative evaluation before broader exposure.
- [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai; https://www.gov.uk/government/publications/generative-ai-framework-for-hmg; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md] The strongest supported operating model is therefore to use the model only to draft or suggest an interpretation, not to let it own the final policy interpretation, with local-document grounding, applicability checks, abstention when authority is missing, and escalation or deterministic rules owning the final consequential interpretation.

### §3 Reasoning

- [fact; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/] The direct evidence base supports three distinct facts: Large Language Models already make authoritative legal mistakes, they do not use long or retrieved context robustly, and humans do not reliably correct erroneous machine recommendations.
- [inference; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/] The most decision-useful synthesis is that policy-interpretation risk is not only about fabricated text, but about wrong applicability, because local policy assistants fail when they select the wrong authority or blend authorities that should stay separate.
- [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://arxiv.org/abs/2505.02151] Human review does not neutralize this by default, because the same behavioural evidence that explains automation bias also explains why a polished first answer can suppress challenge and inflate reviewer confidence.
- [assumption; source: https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai] The public-sector pilot and guidance evidence is treated as a governance proxy for enterprise policy assistants rather than as a direct measurement of corporate compliance flows. Justification: both settings depend on grounded retrieval, trust calibration, and authoritative public or institutional content.

### §4 Consistency Check

- [fact; source: https://arxiv.org/abs/2401.01301; https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive] No contradiction appears between the legal-hallucination preprint and the Stanford summary; the summary sharpens, rather than reverses, the main claims about false-premise bias, localization weakness, and overconfidence.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] No contradiction appears between the human-review studies and the automation-bias review; all support the narrower conclusion that first-presented machine advice is hard to correct consistently.
- [inference; source: https://aclanthology.org/2023.findings-emnlp.1036/; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172] A plausible rival explanation is that retrieval or interface design alone causes the problem, but the evidence does not support a retrieval-only account because the reviewed studies also show weak reasoning over retrieved statements and weak use of relevant context even when it is present.
- [assumption; source: https://arxiv.org/abs/2401.01301; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/] The remaining unresolved gap is direct public evidence from proprietary enterprise policy assistants, so confidence should stay medium rather than high even though the cross-source pattern is coherent. Justification: the core synthesis depends on proxy domains.

### §5 Depth and Breadth Expansion

- [fact; source: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques] Regulatory and assurance lens: official guidance treats generative Artificial Intelligence risk as context-specific and lifecycle-wide, which means benchmark strength does not substitute for local applicability testing.
- [fact; source: https://arxiv.org/abs/2307.03172; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/] Technical lens: long, exception-heavy policy corpora are structurally risky because middle-position information and poor chunking can hide the controlling clause from the model.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://arxiv.org/abs/2505.02151] Behavioural lens: review quality depends on trust calibration, workload, and confidence management as much as on raw model quality.
- [inference; source: https://arxiv.org/abs/2401.01301; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md] Organisational lens: the most dangerous pattern is not a visibly absurd answer but a locally persuasive answer that removes the felt need to escalate an ambiguous case.
- [inference; source: https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md] Architecture lens: the control point that matters most is the final applicability decision, so deterministic policy rules, cited source displays, and logged escalations belong outside the raw model response.

### §6 Synthesis

**Executive summary:**

In policy interpretation, a Large Language Model can return an authoritative answer that applies the wrong rule or the wrong level of authority. [inference; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/]

This risk grows when general-purpose models hallucinate legal authority and when long or weakly retrieved local context gives them multiple ways to miss the controlling internal rule. [inference; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2303.08774; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/]

This risk also grows when the underlying policy estate is contradictory or stale, because prior repository research shows that incoherent policy sets are already unsafe for automated enforcement before model synthesis adds another error source. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md]

Users are then poorly positioned to catch the mismatch if the model answer appears first, because automation-bias evidence shows that early machine advice reduces human accuracy, human-in-the-loop designs can increase uptake while lowering decision quality, and model input can amplify reviewer overconfidence. [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://arxiv.org/abs/2505.02151]

Official assurance guidance therefore supports treating policy assistants as proposal systems that must be tested against local authority boundaries, checked against organisational values and compliance requirements, and paired with explicit abstention and escalation paths for ambiguous cases. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai]

**Key findings:**

1. **General-purpose Large Language Models already show a strong tendency to generate legally plausible but factually wrong answers, to accept false legal premises, and to remain overconfident about those answers, which means policy assistants start from a baseline risk of fabricated or misapplied authority before any local-document problem is added.** ([fact]; medium confidence; source: https://arxiv.org/abs/2401.01301; https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive; https://arxiv.org/abs/2303.08774)
2. **Organisation-specific policy interpretation is especially exposed when the controlling clause is long, exception-heavy, noisy, or poorly placed in context, because models are distractible by irrelevant material, weaker on information in the middle of long context, and still limited at reasoning over retrieved statements even when retrieval is partly successful.** ([fact]; high confidence; source: https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/)
3. **The most important policy-assistant failure mode is wrong applicability, where the model blends public legal priors, retrieved fragments, and local policy into a coherent answer that sounds authoritative while applying the wrong rule or the wrong level of authority.** ([inference]; medium confidence; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/)
4. **Contradictory or stale policy corpora are a separate but interacting source of failure, because policy-coherence work in this repository shows that incoherent policy estates already create unsafe conditions for automated enforcement before Large Language Model synthesis adds another error channel.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md)
5. **User review is an unreliable backstop once the model answer appears first, because incorrect Artificial Intelligence support shown before independent judgment lowers human accuracy, participants follow algorithmic recommendations more closely than equally accurate human ones, and even larger recommendation errors are often insufficient to trigger intervention.** ([fact]; high confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.md)
6. **Policy-assistant outputs can become more dangerous when they increase user confidence rather than raw correctness, because Large Language Model input can more than double human overconfidence and institutionally trusted interfaces can lead users to discount known inaccuracy risks.** ([fact]; medium confidence; source: https://arxiv.org/abs/2505.02151; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md)
7. **Official assurance guidance does not support generic trust in benchmarked model capability as proof of policy safety, because NIST and United Kingdom guidance both frame generative Artificial Intelligence assurance as context-specific evaluation against regulation, standards, limitations, organisational values, and lifecycle monitoring duties.** ([fact]; high confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques)
8. **The safest architecture for consequential policy interpretation is to use the model only to draft or suggest an interpretation, require citations to the controlling local source, abstain when applicability is not established from authorised documents, and route ambiguous cases into deterministic rules or human escalation rather than letting the model own the final interpretation.** ([inference]; medium confidence; source: https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai; https://www.gov.uk/government/publications/generative-ai-framework-for-hmg; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] General-purpose Large Language Models hallucinate legal authority, accept false premises, and remain overconfident. | https://arxiv.org/abs/2401.01301 ; https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive ; https://arxiv.org/abs/2303.08774 | medium | Baseline legal-risk family |
| [fact] Long, noisy, and weakly retrieved context degrades use of the controlling policy text. | https://arxiv.org/abs/2302.00093 ; https://arxiv.org/abs/2307.03172 ; https://aclanthology.org/2023.findings-emnlp.1036/ ; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/ | high | Context-use limitation |
| [inference] The dominant policy-assistant failure mode is wrong applicability, where the model selects or blends the wrong authority. | https://arxiv.org/abs/2401.01301 ; https://arxiv.org/abs/2302.00093 ; https://arxiv.org/abs/2307.03172 ; https://aclanthology.org/2023.findings-emnlp.1036/ ; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/ | medium | Wrong authority selection |
| [inference] Contradictory or stale policy estates create a separate automation risk before model synthesis is added. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md | medium | Alternative explanation integrated |
| [fact] Human review often fails when machine advice appears first. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.md | high | Detection weakness |
| [fact] Model and interface trust signals can amplify reviewer confidence beyond correctness. | https://arxiv.org/abs/2505.02151 ; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md | medium | Confidence inflation |
| [fact] Official assurance guidance requires context-specific evaluation against organisational and compliance criteria. | https://www.nist.gov/itl/ai-risk-management-framework ; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence ; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance ; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques | high | Assurance baseline |
| [inference] Draft-only model use with citation, abstention, and escalation is safer than model-owned final interpretation. | https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques ; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai ; https://www.gov.uk/government/publications/generative-ai-framework-for-hmg ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md | medium | Control-boundary recommendation |

**Assumptions:**

- [assumption; source: https://arxiv.org/abs/2401.01301; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/] Legal-question answering and grounded public-information chat are used as proxies for enterprise policy assistants because both require selecting the controlling authority from a broader textual environment, but they are not direct measurements of internal corporate policy use.
- [assumption; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] Human-review findings from judicial, prediction, and clinical decision-support settings are treated as behavioural proxies for compliance review because the underlying task is evaluation of a machine recommendation under uncertainty.

**Analysis:**

The strongest direct evidence is the combination of legal-domain hallucination studies with context-use studies, because together they explain both why the model can state a wrong rule and why the local controlling rule can fail to displace that error. [inference; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/]

One competing explanation is that retrieval quality alone causes the problem. The retriever-augmented reasoning paper and long-context papers make that explanation too narrow, because they show weaknesses both in getting the right evidence and in using it correctly once present. [inference; source: https://aclanthology.org/2023.findings-emnlp.1036/; https://arxiv.org/abs/2307.03172; https://arxiv.org/abs/2302.00093]

Another competing explanation is that the policy source itself is incoherent, contradictory, or stale. The policy-coherence item in this repository supports that qualification, and it narrows the central claim here: wrong applicability can arise from weak local policy design alone, and model-plus-context synthesis adds a second error channel on top of that pre-existing condition. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md]

The behavioural evidence matters because an enterprise might otherwise conclude that ordinary reviewer sign-off closes the risk, yet the reviewed studies show the opposite pattern: first-presented machine output can lower human accuracy, and human-in-the-loop workflows can still drift toward rubber-stamping. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.md]

For that reason, the evidence weighs in favour of workflow and assurance controls rather than prompt-only fixes, because official guidance repeatedly frames safe use as a matter of context-specific testing, compliance audit, and documented review responsibilities. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques]

**Risks, gaps, uncertainties:**

- Direct public evidence on proprietary internal-policy assistants remains limited, so this synthesis rests on legal-question answering, public-sector policy chat, and broader human-review studies rather than on a large benchmark of enterprise compliance deployments. [assumption; source: https://arxiv.org/abs/2401.01301; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/]
- The evidence is stronger on failure mechanisms than on measured mitigation effect sizes for enterprise policy work, because official guidance specifies the control types to use but rarely publishes controlled before-and-after outcome data for organisational deployments. [inference; source: https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance]
- The legal-hallucination evidence is strongest for public legal authorities, not for internal corporate standards, so the claim about local-policy applicability remains inferential even though the context-use evidence makes the transfer plausible. [assumption; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/]
- This item does not quantify which user-interface changes best improve detection of inapplicable answers, because the available sources support independent-first review and verification intensity broadly more strongly than any single interface pattern. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/]

**Open questions:**

- What benchmark best measures local-policy applicability rather than generic legal correctness?
- How much does mandatory citation of the controlling internal clause improve reviewer detection of context mismatch?
- Which abstention threshold is most practical before a policy assistant should escalate to a deterministic rule or a human specialist?
- How much does chunking or document-layout design change error rates on long policy manuals with exceptions and appendices?

### §7 Recursive Review

- Review outcome: pass
- Acronym audit: completed
- Claim audit: completed
- Cross-item integration audit: completed

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

In policy interpretation, a Large Language Model can return an authoritative answer that applies the wrong rule or the wrong level of authority. [inference; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/]

This risk grows when general-purpose models hallucinate legal authority and when long or weakly retrieved local context gives them multiple ways to miss the controlling internal rule. [inference; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2303.08774; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/]

This risk also grows when the underlying policy estate is contradictory or stale, because prior repository research shows that incoherent policy sets are already unsafe for automated enforcement before model synthesis adds another error source. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md]

Users are then poorly positioned to catch the mismatch if the model answer appears first, because automation-bias evidence shows that early machine advice reduces human accuracy, human-in-the-loop designs can increase uptake while lowering decision quality, and model input can amplify reviewer overconfidence. [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://arxiv.org/abs/2505.02151]

Official assurance guidance therefore supports treating policy assistants as proposal systems that must be tested against local authority boundaries, checked against organisational values and compliance requirements, and paired with explicit abstention and escalation paths for ambiguous cases. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai]

### Key Findings

1. **General-purpose Large Language Models already show a strong tendency to generate legally plausible but factually wrong answers, to accept false legal premises, and to remain overconfident about those answers, which means policy assistants start from a baseline risk of fabricated or misapplied authority before any local-document problem is added.** ([fact]; medium confidence; source: https://arxiv.org/abs/2401.01301; https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive; https://arxiv.org/abs/2303.08774)
2. **Organisation-specific policy interpretation is especially exposed when the controlling clause is long, exception-heavy, noisy, or poorly placed in context, because models are distractible by irrelevant material, weaker on information in the middle of long context, and still limited at reasoning over retrieved statements even when retrieval is partly successful.** ([fact]; high confidence; source: https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/)
3. **The most important policy-assistant failure mode is wrong applicability, where the model blends public legal priors, retrieved fragments, and local policy into a coherent answer that sounds authoritative while applying the wrong rule or the wrong level of authority.** ([inference]; medium confidence; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/)
4. **Contradictory or stale policy corpora are a separate but interacting source of failure, because policy-coherence work in this repository shows that incoherent policy estates already create unsafe conditions for automated enforcement before Large Language Model synthesis adds another error channel.** ([inference]; medium confidence; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md)
5. **User review is an unreliable backstop once the model answer appears first, because incorrect Artificial Intelligence support shown before independent judgment lowers human accuracy, participants follow algorithmic recommendations more closely than equally accurate human ones, and even larger recommendation errors are often insufficient to trigger intervention.** ([fact]; high confidence; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.md)
6. **Policy-assistant outputs can become more dangerous when they increase user confidence rather than raw correctness, because Large Language Model input can more than double human overconfidence and institutionally trusted interfaces can lead users to discount known inaccuracy risks.** ([fact]; medium confidence; source: https://arxiv.org/abs/2505.02151; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md)
7. **Official assurance guidance does not support generic trust in benchmarked model capability as proof of policy safety, because NIST and United Kingdom guidance both frame generative Artificial Intelligence assurance as context-specific evaluation against regulation, standards, limitations, organisational values, and lifecycle monitoring duties.** ([fact]; high confidence; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques)
8. **The safest architecture for consequential policy interpretation is to use the model only to draft or suggest an interpretation, require citations to the controlling local source, abstain when applicability is not established from authorised documents, and route ambiguous cases into deterministic rules or human escalation rather than letting the model own the final interpretation.** ([inference]; medium confidence; source: https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai; https://www.gov.uk/government/publications/generative-ai-framework-for-hmg; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] General-purpose Large Language Models hallucinate legal authority, accept false premises, and remain overconfident. | https://arxiv.org/abs/2401.01301 ; https://hai.stanford.edu/news/hallucinating-law-legal-mistakes-large-language-models-are-pervasive ; https://arxiv.org/abs/2303.08774 | medium | Baseline legal-risk family |
| [fact] Long, noisy, and weakly retrieved context degrades use of the controlling policy text. | https://arxiv.org/abs/2302.00093 ; https://arxiv.org/abs/2307.03172 ; https://aclanthology.org/2023.findings-emnlp.1036/ ; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/ | high | Context-use limitation |
| [inference] The dominant policy-assistant failure mode is wrong applicability, where the model selects or blends the wrong authority. | https://arxiv.org/abs/2401.01301 ; https://arxiv.org/abs/2302.00093 ; https://arxiv.org/abs/2307.03172 ; https://aclanthology.org/2023.findings-emnlp.1036/ ; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/ | medium | Wrong authority selection |
| [inference] Contradictory or stale policy estates create a separate automation risk before model synthesis is added. | https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md | medium | Alternative explanation integrated |
| [fact] Human review often fails when machine advice appears first. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.md | high | Detection weakness |
| [fact] Model and interface trust signals can amplify reviewer confidence beyond correctness. | https://arxiv.org/abs/2505.02151 ; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/ ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md | medium | Confidence inflation |
| [fact] Official assurance guidance requires context-specific evaluation against organisational and compliance criteria. | https://www.nist.gov/itl/ai-risk-management-framework ; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence ; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance ; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques | high | Assurance baseline |
| [inference] Draft-only model use with citation, abstention, and escalation is safer than model-owned final interpretation. | https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques ; https://www.gov.uk/government/publications/guidance-to-civil-servants-on-use-of-generative-ai/guidance-to-civil-servants-on-use-of-generative-ai ; https://www.gov.uk/government/publications/generative-ai-framework-for-hmg ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-09-governance-policy-determinism-vs-stochastic-llm.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-17-ai-policy-ambiguity-accountability-governance-risk.md | medium | Control-boundary recommendation |

### Assumptions

- [assumption; source: https://arxiv.org/abs/2401.01301; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/] Legal-question answering and grounded public-information chat are used as proxies for enterprise policy assistants because both require selecting the controlling authority from a broader textual environment, but they are not direct measurements of internal corporate policy use.
- [assumption; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/] Human-review findings from judicial, prediction, and clinical decision-support settings are treated as behavioural proxies for compliance review because the underlying task is evaluation of a machine recommendation under uncertainty.

### Analysis

The strongest direct evidence is the combination of legal-domain hallucination studies with context-use studies, because together they explain both why the model can state a wrong rule and why the local controlling rule can fail to displace that error. [inference; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2302.00093; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/]

One competing explanation is that retrieval quality alone causes the problem. The retriever-augmented reasoning paper and long-context papers make that explanation too narrow, because they show weaknesses both in getting the right evidence and in using it correctly once present. [inference; source: https://aclanthology.org/2023.findings-emnlp.1036/; https://arxiv.org/abs/2307.03172; https://arxiv.org/abs/2302.00093]

Another competing explanation is that the policy source itself is incoherent, contradictory, or stale. The policy-coherence item in this repository supports that qualification, and it narrows the central claim here: wrong applicability can arise from weak local policy design alone, and model-plus-context synthesis adds a second error channel on top of that pre-existing condition. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-policy-coherence-machine-checkable-prerequisite.md]

The behavioural evidence matters because an enterprise might otherwise conclude that ordinary reviewer sign-off closes the risk, yet the reviewed studies show the opposite pattern: first-presented machine output can lower human accuracy, and human-in-the-loop workflows can still drift toward rubber-stamping. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-08-scaled-hitl-oversight-quality-measurement-productivity-mandates.md]

For that reason, the evidence weighs in favour of workflow and assurance controls rather than prompt-only fixes, because official guidance repeatedly frames safe use as a matter of context-specific testing, compliance audit, and documented review responsibilities. [inference; source: https://www.nist.gov/itl/ai-risk-management-framework; https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques]

### Risks, Gaps, and Uncertainties

- Direct public evidence on proprietary internal-policy assistants remains limited, so this synthesis rests on legal-question answering, public-sector policy chat, and broader human-review studies rather than on a large benchmark of enterprise compliance deployments. [assumption; source: https://arxiv.org/abs/2401.01301; https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/]
- The evidence is stronger on failure mechanisms than on measured mitigation effect sizes for enterprise policy work, because official guidance specifies the control types to use but rarely publishes controlled before-and-after outcome data for organisational deployments. [inference; source: https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques; https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance]
- The legal-hallucination evidence is strongest for public legal authorities, not for internal corporate standards, so the claim about local-policy applicability remains inferential even though the context-use evidence makes the transfer plausible. [assumption; source: https://arxiv.org/abs/2401.01301; https://arxiv.org/abs/2307.03172; https://aclanthology.org/2023.findings-emnlp.1036/]
- This item does not quantify which user-interface changes best improve detection of inapplicable answers, because the available sources support independent-first review and verification intensity broadly more strongly than any single interface pattern. [inference; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10857587/; https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/]

### Open Questions

- What benchmark best measures local-policy applicability rather than generic legal correctness?
- How much does mandatory citation of the controlling internal clause improve reviewer detection of context mismatch?
- Which abstention threshold is most practical before a policy assistant should escalate to a deterministic rule or a human specialist?
- How much does chunking or document-layout design change error rates on long policy manuals with exceptions and appendices?

---

## Output

- Type: knowledge
- Description: This item concludes that the main policy-interpretation risk is authoritative misapplication of the wrong rule, caused by weak local grounding and weak human detection, so the safest pattern is to use the model only to draft or suggest an interpretation, with local citations, abstention, and escalation for ambiguous cases. [inference; source: https://arxiv.org/abs/2401.01301; https://aclanthology.org/2023.findings-emnlp.1036/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/; https://www.gov.uk/guidance/portfolio-of-ai-assurance-techniques]
- Links:
  - https://arxiv.org/abs/2401.01301
  - https://aclanthology.org/2023.findings-emnlp.1036/
  - https://pmc.ncbi.nlm.nih.gov/articles/PMC10772030/
