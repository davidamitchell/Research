---
review_count: 2
title: "Interpretation risks from ambiguous Artificial Intelligence (AI) policy guidance"
added: 2026-05-17T20:33:05+00:00
status: completed
priority: high
blocks: []
tags: [llm, organisation, evaluation]
started: 2026-05-18T09:51:20+00:00
completed: 2026-05-18T10:13:58+00:00
output: [knowledge]
cites: [2026-04-26-ai-governance-culture-incentives-behaviour, 2026-04-30-human-bias-ai-trust-rlhf-sycophancy, 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp, 2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls, 2026-05-12-iso-iec-42001-aims-controls-adoption-history]
related: [2026-04-26-human-in-the-loop-ai-automated-workflows, 2026-04-28-uelgf-human-oversight-accountability-layer, 2026-04-30-explainable-ai-xai-regulation-governance]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: a2bee7186528a2560ebe2344223b7673563b2f4f
    changed: 2026-05-18
    progress: progress/2026-05-18-ai-policy-ambiguity-epistemic-risk.md
    summary: Initial completion
---

# Interpretation risks from ambiguous Artificial Intelligence (AI) policy guidance

## Research Question

How do Large Language Model (LLM) response style and self-reported confidence change how accurately users judge uncertainty and downstream risk when interpreting ambiguous policy and compliance requirements?

## Scope

**In scope:**
- Measure calibration effects from hedged versus non-hedged AI language in policy-guidance contexts
- Test whether syntactic fluency and polished formatting increase willingness to bypass formal verification channels such as legal, compliance, or policy-owner review
- Compare model self-stated confidence against measured interpretation accuracy on ambiguous bylaws, legal questions, and policy-like excerpts

**Out of scope:**
- Implementing production policy-assistant software
- Entity-specific legal advice
- Exhaustive jurisdiction-by-jurisdiction legal analysis

**Constraints:** Use publicly available sources, distinguish demonstrated evidence from inference, expand acronyms on first use, and prioritise sources with explicit governance or empirical grounding.

## Context

Ambiguous internal policies and compliance rules already require documented governance, role clarity, and human oversight, but those controls only work if users recognise uncertainty and escalate unclear cases. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-05-12-iso-iec-42001-aims-controls-adoption-history.html]

This item isolates the user-judgment failure in that control chain: a polished or confident LLM answer can make an uncertain interpretation look more settled than it is, which may reduce verification or escalation. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html]

## Approach

1. Measure how hedged versus non-hedged LLM language changes whether user reliance is appropriately matched to uncertainty and willingness to verify ambiguous guidance.
2. Test whether fluent explanations, polished formatting, or aggregated dashboards increase acceptance of AI advice without improving correctness.
3. Compare verbalised model confidence with measured calibration, ambiguity handling, and error awareness on ambiguous or legal-policy-like tasks.
4. Translate the evidence into governance controls for enterprise policy and compliance assistants.

## Sources

- [x] [Bansal et al. (2021) Does the Whole Exceed its Parts? The Effect of AI Explanations on Complementary Team Performance](https://arxiv.org/abs/2006.14779)
- [x] [Bergman et al. (2024) Advice from Artificial Intelligence: A Review and Practical Framework](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full)
- [x] [Dietvorst et al. (2015) Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err](https://colab.ws/articles/10.1037/xge0000033)
- [x] [Kojima et al. (2024) "I'm Not Sure, But...": Examining the Impact of Large Language Models' Uncertainty Expression on User Reliance and Trust](https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/)
- [x] [Xiong et al. (2024) Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs](https://arxiv.org/abs/2306.13063)
- [x] [Shukla et al. (2024) Overconfidence Is Key: Verbalized Uncertainty Evaluation in Large Language and Vision-Language Models](https://aclanthology.org/2024.trustnlp-1.13/)
- [x] [Agrawal et al. (2024) Do Language Models Know When They're Hallucinating References?](https://aclanthology.org/2024.findings-eacl.62/)
- [x] [Dahl et al. (2024) Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models](https://arxiv.org/html/2401.01301v1)
- [x] [Kamath et al. (2024) Scope Ambiguities in Large Language Models](https://arxiv.org/abs/2404.04332)
- [x] [Schubert et al. (2023) Strategies to Reduce Automation Bias in AI-Based Personnel Preselection](https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/)
- [x] [Okamura and Yamada (2020) Adaptive Trust Calibration for Human-AI Collaboration](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229132)
- [x] [Stump et al. (2024) The Illusory Certainty: Information Repetition and Impressions of Truth Enhance Subjective Confidence in Validity Judgments Independently of the Factual Truth](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/)
- [x] [National Institute of Standards and Technology (NIST) (2023) Artificial Intelligence Risk Management Framework (AI RMF) Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/)

### Identified but not consulted

- [ ] [Dzindolet et al. (2003) The Role of Trust in Automation Reliance](https://doi.org/10.1207/S15327051HCI1812_19)

## Related

- [Mitchell (2026) When and how should human intervention be incorporated into Artificial Intelligence (AI)-driven and automated workflows?](https://davidamitchell.github.io/Research/research/2026-04-26-human-in-the-loop-ai-automated-workflows.html)
- [Mitchell (2026) Universal Entity Lifecycle Governance Framework (UELGF) extension: human oversight and accountability layer, named owners, escalation paths, and accountability alignment with emerging agentic Artificial Intelligence (AI) governance standards](https://davidamitchell.github.io/Research/research/2026-04-28-uelgf-human-oversight-accountability-layer.html)
- [Mitchell (2026) Explainable Artificial Intelligence (XAI): current research state, leading institutions, and regulatory intersection in heavily regulated industries](https://davidamitchell.github.io/Research/research/2026-04-30-explainable-ai-xai-regulation-governance.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation; section 6 seeds the Findings section below.)*

### §0 Initialise

- Question: how LLM response style, fluency, and self-reported confidence affect user judgment of uncertainty and downstream risk when policy or compliance language is ambiguous.
- Scope: ambiguous policy, compliance, and legal-rule interpretation by users of AI assistants, not production implementation detail or jurisdiction-specific legal advice.
- Constraints: full mode, public sources only, primary empirical or official governance sources preferred, and every non-factual claim explicitly labeled.
- Output: knowledge synthesis with Executive Summary, Key Findings, Evidence Map, Assumptions, Analysis, Risks, and Open Questions.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Prior completed items in this repository already show that governance adherence falls when sanctioned review paths are slow or overloaded, so this item focuses on whether the assistant's language makes ambiguous cases look settled enough to suppress escalation.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.html] A directly adjacent completed item already concluded that automation bias and polished explanations can make AI outputs appear more correct and more explainable than they really are, which is the nearest repository-level prior art for this question.
- [assumption; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://arxiv.org/html/2401.01301v1] Evidence from legal, personnel-selection, and general decision-support settings is a reasonable proxy for internal policy interpretation because the shared mechanism is human review of uncertain recommendations rather than domain-specific physical control.

### §1 Question Decomposition

- Root question: how do response style, fluency, and self-reported confidence change user verification behavior and risk calibration when policy guidance is ambiguous?
- A. Trust-calibration branch
  - A1. Do explicit uncertainty expressions reduce overreliance on AI advice?
  - A2. Which interface cues improve user reliance behavior when system reliability is imperfect?
- B. Fluency-and-format branch
  - B1. Do explanations or polished presentation increase acceptance of AI advice independently of correctness?
  - B2. Do aggregation and ease-of-processing cues reduce verification intensity?
- C. Model-confidence branch
  - C1. Are LLM verbalized confidence statements well calibrated?
  - C2. Can LLMs detect their own mistakes or ambiguity reliably enough for user-facing confidence claims to be trusted?
  - C3. How well do LLMs handle ambiguity in legal-policy-like language?
- D. Governance branch
  - D1. What does the evidence imply for enterprise policy and compliance assistants?
  - D2. Which control surfaces should absorb the residual ambiguity risk?

### §2 Investigation

- Prior completed-item sweep:
  - [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://davidamitchell.github.io/Research/research/2026-05-02-incentive-misalignment-shadow-ai-skill-decay-controls.html] The closest completed items already establish that incentive pressure, overloaded review queues, automation bias, and polished explanations can push organisations toward bypass behaviour, nominal review, and reduced human scrutiny.
  - [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] The open gap is about user judgment rather than structure: if an assistant's wording makes ambiguity feel resolved, the sanctioned escalation path may be bypassed even when governance roles are formally clear.

#### A. Hedging, uncertainty expression, and reliance adjustment

- [fact; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/] In a preregistered human-subject experiment with 404 participants answering medical questions, first-person uncertainty expressions such as "I'm not sure, but..." reduced agreement with the system and increased participant accuracy by reducing overreliance on incorrect LLM answers.
- [fact; source: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229132] Okamura and Yamada show that adaptively presented interface cues can significantly improve how closely user reliance tracks system reliability during over-trust, which means reliance behavior can be shifted by interface design rather than only by underlying model quality.
- [fact; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full] The 2024 review of advice from artificial intelligence says advice outcomes depend on the interaction between advisor characteristics, user characteristics, and the advice environment, not on raw model accuracy alone.
- [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229132] For ambiguous policy guidance, hedged language is not just stylistic softening; it is a control cue that can preserve user willingness to verify or escalate.

#### B. Fluency, explanations, and verification intensity

- [fact; source: https://arxiv.org/abs/2006.14779] Bansal et al. found that explanations did not improve complementary human-AI team performance when model accuracy was comparable to human accuracy, but explanations did increase the chance that humans would accept the AI recommendation regardless of whether it was correct.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/] Schubert et al. found that informing reviewers about possible system errors increased verification-intensity indicators and objective decision quality, while merely reminding them of their responsibility did not have the same effect.
- [fact; source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/] The same experiment found that higher data aggregation reduced time spent on the evidence layer, which means presentation format changed how much checking users actually performed.
- [fact; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/] Stump et al. found that repetition and impressions of truth systematically increased subjective confidence independently of factual truth, which is direct evidence that fluency can raise confidence without improving correctness.
- [inference; source: https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/] A fluent or highly structured policy answer can therefore create a double risk: it can feel more correct because it is easier to process, and it can reduce the user time spent inspecting the supporting evidence.

#### C. LLM confidence, self-awareness, and ambiguity handling

- [fact; source: https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/] Two recent evaluations report that LLMs are often overconfident when verbalising their uncertainty and still show high calibration error on difficult tasks, even though prompt design and response-consistency methods can improve calibration somewhat.
- [fact; source: https://arxiv.org/html/2401.01301v1] Dahl et al. found that LLMs hallucinated between 69% and 88% of the time on direct, verifiable federal-case questions, often failed to correct users' wrong legal premises, and could not reliably gauge their own certainty without post-hoc recalibration.
- [fact; source: https://aclanthology.org/2024.findings-eacl.62/] Agrawal et al. found that language models can sometimes expose their own hallucinated references through inconsistent follow-up answers, but that detection requires additional probing rather than trusting the original answer at face value.
- [fact; source: https://arxiv.org/abs/2404.04332] Kamath et al. found that modern LLMs can identify human-preferred readings across nearly 1,000 scope-ambiguous sentences, with over 90% accuracy in some cases, which suggests that ambiguity sensitivity exists, but the paper does not show that user-facing confidence statements are calibrated on those tasks.
- [inference; source: https://arxiv.org/html/2401.01301v1; https://aclanthology.org/2024.findings-eacl.62/; https://arxiv.org/abs/2404.04332] Ambiguity competence and confidence calibration are separate properties: a model may parse some ambiguities correctly while still presenting wrong or weakly supported interpretations with misleading certainty.

#### D. Governance implications for policy and compliance assistants

- [fact; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/] The NIST AI RMF says organisations should document knowledge limits, define human oversight processes, document operator proficiency and trustworthiness, and map context-specific laws, norms, and risks before relying on AI outputs.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-05-12-iso-iec-42001-aims-controls-adoption-history.html] The repository's International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC) 42001 item concluded that management-system controls are strongest at process quality and due diligence rather than as a standalone guarantee of model-specific correctness.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] A safe policy-assistant design should therefore treat answer wording, evidence display, and escalation routing as first-class governance controls, because raw model accuracy and a generic human-review requirement do not by themselves stop confident misinterpretation.

### §3 Reasoning

- [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229132; https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://arxiv.org/abs/2306.13063; https://arxiv.org/html/2401.01301v1] Taken together, the evidence shows that language cues and interface design change reliance behavior, explanations can increase acceptance without improving correctness, and LLM confidence statements remain poorly calibrated on challenging tasks across multiple benchmark families.
- [inference; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/; https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/] The strongest causal chain for this item is not "confidence wording changes truth" but "confidence wording and fluency change user checking behavior," which is enough to increase governance risk when policy language is ambiguous.
- [assumption; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://arxiv.org/html/2401.01301v1] Internal policy interpretation is sufficiently similar to legal and organisational decision support that evidence from those domains can inform control design, even though no retrieved study tested the exact enterprise policy-assistant scenario.

### §4 Consistency Check

- [inference; source: https://arxiv.org/abs/2404.04332; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2306.13063] There is no contradiction between "LLMs can resolve some ambiguity patterns well" and "LLMs are unsafe to trust for ambiguous policy interpretation," because the first claim concerns task capability while the second concerns calibration, failure detection, and user reliance.
- [inference; source: https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/] There is no contradiction between "explanations can help users inspect evidence" and "explanations can increase blind acceptance," because explanation usefulness depends on whether the interface prompts checking or substitutes for it.
- [fact; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2306.13063] The evidence base is directionally consistent that uncertainty communication improves calibration at the user layer more reliably than current LLM self-confidence improves calibration at the model layer.

### §5 Depth and Breadth Expansion

- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-05-12-iso-iec-42001-aims-controls-adoption-history.html] Technical lens: governance should bind answers to source text, knowledge limits, and explicit escalation paths rather than treat the model's prose style as an adequate reliability signal.
- [inference; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/] Behavioural lens: fluency, explanation, and aggregation cues act on user effort allocation, so interface design can change verification behavior without changing the underlying answer quality.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html] Organisational lens: if escalation or policy-owner review is slower than the assistant, confident answers will compound the already observed tendency for users to prefer the fast lane over the sanctioned one.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/] Regulatory lens: meaningful human oversight for policy and compliance use cases depends on preserving user recognition of uncertainty, not just on naming a reviewer somewhere in the process.

### §6 Synthesis

**Executive summary:**

Confident, fluent LLM policy answers are likely to make users underweight ambiguity and overestimate correctness unless the system explicitly signals uncertainty and keeps evidence inspection visible. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2006.14779; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/]

The strongest direct evidence is at the user-interface layer: natural-language uncertainty expressions reduce overreliance, while explanations and polished presentation can increase acceptance of advice without improving correctness. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/]

Current LLM self-reported confidence is too weakly matched to actual correctness to substitute for external verification on its own, because recent evaluations show overconfidence and weak error awareness on difficult or legal-style tasks even when some ambiguity-handling capability exists. [inference; source: https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2404.04332]

For enterprise policy and compliance assistants, a safer default control pattern is uncertainty-forward wording that is matched to evidence and task stakes, direct quotation of governing text, and escalation of ambiguous or high-impact cases rather than a single authoritative answer path. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://colab.ws/articles/10.1037/xge0000033]

**Key findings:**

1. **Natural-language uncertainty expressions can materially improve whether user reliance matches answer reliability, because participants exposed to first-person LLM hedging relied on the system less blindly and answered medical questions more accurately than participants shown more assertive wording.** ([fact]; medium confidence; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/)
2. **Explanations and polished answer structures do not automatically create better human-AI decisions, and multiple studies show they can increase acceptance of recommendations even when the underlying recommendation quality does not improve.** ([fact]; high confidence; source: https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/)
3. **Information that is easier to process because it is repeated or smoothly presented can raise subjective confidence independently of factual truth, which means a polished policy explanation can feel more reliable than it is before any substantive validation occurs.** ([fact]; medium confidence; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/)
4. **Current LLMs are not dependable narrators of their own certainty, because recent benchmark studies find persistent overconfidence and large gaps between stated confidence and actual correctness even when prompt engineering and consistency checks improve performance somewhat.** ([fact]; high confidence; source: https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/)
5. **On legal-style questions that resemble policy interpretation more closely than general trivia does, state-of-the-art LLMs still produce frequent hallucinations, fail to correct false premises reliably, and often need extra probing before their uncertainty becomes visible.** ([fact]; high confidence; source: https://arxiv.org/html/2401.01301v1; https://aclanthology.org/2024.findings-eacl.62/)
6. **Ambiguity handling skill does not eliminate interpretation risk, because Kamath et al. report over 90% accuracy in some ambiguity datasets while other studies still show weak matching between stated confidence and actual correctness, plus frequent legal-task hallucinations in real user-facing settings.** ([inference]; medium confidence; source: https://arxiv.org/abs/2404.04332; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2306.13063)
7. **For policy and compliance assistants, the main governance control should be preserving the user's motivation to verify or escalate, not merely improving prose quality, because wording, aggregation, queue pressure, and the risk of under-reliance all affect whether human review remains meaningful.** ([inference]; medium confidence; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://colab.ws/articles/10.1037/xge0000033)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Hedged LLM wording reduced blind agreement and improved participant accuracy in a preregistered experiment. | https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/ | Medium | Single directly aligned study |
| [fact] Explanations increased acceptance of AI advice without improving complementary team performance, and error briefings improved verification intensity more than responsibility reminders did. | https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/ | High | Two independent experimental studies |
| [fact] Easier-to-process information and impressions of truth raised subjective confidence independently of factual truth. | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/ | Medium | General cognitive mechanism, not AI-specific |
| [fact] Recent LLM uncertainty-evaluation papers report systematic overconfidence and large gaps between stated confidence and actual correctness. | https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/ | High | Direct model-evaluation evidence |
| [fact] Legal-task studies show frequent hallucinations, weak false-premise correction, and imperfect self-detection of errors. | https://arxiv.org/html/2401.01301v1; https://aclanthology.org/2024.findings-eacl.62/ | High | Closest public analogue to policy interpretation |
| [inference] Ambiguity competence alone is insufficient because some ambiguity datasets show high task accuracy while confidence-quality matching and user-facing certainty remain separate failure modes. | https://arxiv.org/abs/2404.04332; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2306.13063 | Medium | Capability-versus-confidence distinction |
| [inference] Policy-assistant safety depends on uncertainty signaling matched to evidence and task stakes, visible evidence, and escalation routing more than on fluent prose alone. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://colab.ws/articles/10.1037/xge0000033 | Medium | Governance synthesis with under-reliance tradeoff |

**Assumptions:**

- [assumption; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://arxiv.org/html/2401.01301v1] Evidence from legal, medical, and personnel-selection decision support transfers well enough to enterprise policy interpretation because the relevant mechanism is human reliance on uncertain recommendations rather than the substantive domain alone.
- [assumption; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html] Internal policy assistants will often operate in organisations where escalation is slower than answering, so reliance and bypass incentives are practical governance concerns rather than only laboratory effects.

**Analysis:**

The evidence is strongest on two points: users change their verification behavior when wording or interface cues change, and current LLMs remain weak at matching stated confidence to actual correctness. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/]

The main alternative explanation is that better explanations or better model capability could remove the need for explicit uncertainty or escalation controls. [inference; source: https://arxiv.org/abs/2006.14779; https://arxiv.org/abs/2404.04332] The retrieved evidence does not support that stronger claim, because explanations increased acceptance without improving complementary performance, and ambiguity competence did not come with proven confidence-quality matching or error self-awareness. [inference; source: https://arxiv.org/abs/2006.14779; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2306.13063]

I therefore weighted evidence about how wording changes user reliance more heavily than raw ambiguity-performance evidence when answering the research question. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://arxiv.org/abs/2306.13063] This does not imply that stronger uncertainty cues should be maximised without limit, because Dietvorst's algorithm-aversion study and later reliance-adjustment work both show that visible error or poorly tuned cues can also produce under-reliance. [inference; source: https://colab.ws/articles/10.1037/xge0000033; https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229132] For governance design, the relevant failure is not only whether the model can sometimes get ambiguity right, but whether users can tell when they should stop trusting the first answer and seek authoritative review without being pushed into blanket disuse. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://colab.ws/articles/10.1037/xge0000033]

**Risks, gaps, uncertainties:**

- [fact; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full] The retrieved literature did not include a direct experiment on ambiguous internal corporate policies, so the conclusion relies on adjacent decision-support domains rather than a perfect task match.
- [fact; source: https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/] LLM confidence-estimation methods are moving quickly, so absolute error rates may change faster than the broader human-factors pattern.
- [inference; source: https://arxiv.org/abs/2404.04332; https://arxiv.org/html/2401.01301v1] Policy interpretation risk will vary by task type, because some ambiguity classes are easier for models than open-ended legal or organisational interpretation tasks.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html] Organisational incentives may dominate interface improvements if escalation remains materially slower or more costly than accepting the assistant's answer.

**Open questions:**

- Does numeric confidence plus direct quotation of the governing policy text outperform verbal hedging alone for enterprise users?
- Which escalation trigger best preserves verification without making the assistant unusably slow: ambiguity detection, policy-domain risk tiering, or explicit user uncertainty declarations?
- Can audit logs capture whether users inspected source text before acting on a policy answer strongly enough to support meaningful review?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Artificial Intelligence (AI), Large Language Model (LLM), National Institute of Standards and Technology (NIST), and Artificial Intelligence Risk Management Framework (AI RMF) are expanded on first use in the document.
- Claim audit: Findings and synthesis claims are labeled and source-bound; confidence levels are aligned to source type and independence.
- Cross-item audit: cited and related completed items are linked with GitHub Pages URLs rather than repository-relative paths.

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Confident, fluent LLM policy answers are likely to make users underweight ambiguity and overestimate correctness unless the system explicitly signals uncertainty and keeps evidence inspection visible. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2006.14779; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/]

The strongest direct evidence is at the user-interface layer: natural-language uncertainty expressions reduce overreliance, while explanations and polished presentation can increase acceptance of advice without improving correctness. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/]

Current LLM self-reported confidence is too weakly matched to actual correctness to substitute for external verification on its own, because recent evaluations show overconfidence and weak error awareness on difficult or legal-style tasks even when some ambiguity-handling capability exists. [inference; source: https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2404.04332]

For enterprise policy and compliance assistants, a safer default control pattern is uncertainty-forward wording that is matched to evidence and task stakes, direct quotation of governing text, and escalation of ambiguous or high-impact cases rather than a single authoritative answer path. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://colab.ws/articles/10.1037/xge0000033]

### Key Findings

1. **Natural-language uncertainty expressions can materially improve whether user reliance matches answer reliability, because participants exposed to first-person LLM hedging relied on the system less blindly and answered medical questions more accurately than participants shown more assertive wording.** ([fact]; medium confidence; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/)
2. **Explanations and polished answer structures do not automatically create better human-AI decisions, and multiple studies show they can increase acceptance of recommendations even when the underlying recommendation quality does not improve.** ([fact]; high confidence; source: https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/)
3. **Information that is easier to process because it is repeated or smoothly presented can raise subjective confidence independently of factual truth, which means a polished policy explanation can feel more reliable than it is before any substantive validation occurs.** ([fact]; medium confidence; source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/)
4. **Current LLMs are not dependable narrators of their own certainty, because recent benchmark studies find persistent overconfidence and large gaps between stated confidence and actual correctness even when prompt engineering and consistency checks improve performance somewhat.** ([fact]; high confidence; source: https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/)
5. **On legal-style questions that resemble policy interpretation more closely than general trivia does, state-of-the-art LLMs still produce frequent hallucinations, fail to correct false premises reliably, and often need extra probing before their uncertainty becomes visible.** ([fact]; high confidence; source: https://arxiv.org/html/2401.01301v1; https://aclanthology.org/2024.findings-eacl.62/)
6. **Ambiguity handling skill does not eliminate interpretation risk, because Kamath et al. report over 90% accuracy in some ambiguity datasets while other studies still show weak matching between stated confidence and actual correctness, plus frequent legal-task hallucinations in real user-facing settings.** ([inference]; medium confidence; source: https://arxiv.org/abs/2404.04332; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2306.13063)
7. **For policy and compliance assistants, the main governance control should be preserving the user's motivation to verify or escalate, not merely improving prose quality, because wording, aggregation, queue pressure, and the risk of under-reliance all affect whether human review remains meaningful.** ([inference]; medium confidence; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://colab.ws/articles/10.1037/xge0000033)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Hedged LLM wording reduced blind agreement and improved participant accuracy in a preregistered experiment. | https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/ | Medium | Single directly aligned study |
| [fact] Explanations increased acceptance of AI advice without improving complementary team performance, and error briefings improved verification intensity more than responsibility reminders did. | https://arxiv.org/abs/2006.14779; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/ | High | Two independent experimental studies |
| [fact] Easier-to-process information and impressions of truth raised subjective confidence independently of factual truth. | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11143013/ | Medium | General cognitive mechanism, not AI-specific |
| [fact] Recent LLM uncertainty-evaluation papers report systematic overconfidence and large gaps between stated confidence and actual correctness. | https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/ | High | Direct model-evaluation evidence |
| [fact] Legal-task studies show frequent hallucinations, weak false-premise correction, and imperfect self-detection of errors. | https://arxiv.org/html/2401.01301v1; https://aclanthology.org/2024.findings-eacl.62/ | High | Closest public analogue to policy interpretation |
| [inference] Ambiguity competence alone is insufficient because some ambiguity datasets show high task accuracy while confidence-quality matching and user-facing certainty remain separate failure modes. | https://arxiv.org/abs/2404.04332; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2306.13063 | Medium | Capability-versus-confidence distinction |
| [inference] Policy-assistant safety depends on uncertainty signaling matched to evidence and task stakes, visible evidence, and escalation routing more than on fluent prose alone. | https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://colab.ws/articles/10.1037/xge0000033 | Medium | Governance synthesis with under-reliance tradeoff |

### Assumptions

- [assumption; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://arxiv.org/html/2401.01301v1] Evidence from legal, medical, and personnel-selection decision support transfers well enough to enterprise policy interpretation because the relevant mechanism is human reliance on uncertain recommendations rather than the substantive domain alone.
- [assumption; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html] Internal policy assistants will often operate in organisations where escalation is slower than answering, so reliance and bypass incentives are practical governance concerns rather than only laboratory effects.

### Analysis

The evidence is strongest on two points: users change their verification behavior when wording or interface cues change, and current LLMs remain weak at matching stated confidence to actual correctness. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/]

The main alternative explanation is that better explanations or better model capability could remove the need for explicit uncertainty or escalation controls. [inference; source: https://arxiv.org/abs/2006.14779; https://arxiv.org/abs/2404.04332] The retrieved evidence does not support that stronger claim, because explanations increased acceptance without improving complementary performance, and ambiguity competence did not come with proven confidence-quality matching or error self-awareness. [inference; source: https://arxiv.org/abs/2006.14779; https://arxiv.org/html/2401.01301v1; https://arxiv.org/abs/2306.13063]

I therefore weighted evidence about how wording changes user reliance more heavily than raw ambiguity-performance evidence when answering the research question. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://pmc.ncbi.nlm.nih.gov/articles/PMC10113449/; https://arxiv.org/abs/2306.13063] This does not imply that stronger uncertainty cues should be maximised without limit, because Dietvorst's algorithm-aversion study and later reliance-adjustment work both show that visible error or poorly tuned cues can also produce under-reliance. [inference; source: https://colab.ws/articles/10.1037/xge0000033; https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229132] For governance design, the relevant failure is not only whether the model can sometimes get ambiguity right, but whether users can tell when they should stop trusting the first answer and seek authoritative review without being pushed into blanket disuse. [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.html; https://colab.ws/articles/10.1037/xge0000033]

### Risks, Gaps, and Uncertainties

- [fact; source: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1390182/full] The retrieved literature did not include a direct experiment on ambiguous internal corporate policies, so the conclusion relies on adjacent decision-support domains rather than a perfect task match.
- [fact; source: https://arxiv.org/abs/2306.13063; https://aclanthology.org/2024.trustnlp-1.13/] LLM confidence-estimation methods are moving quickly, so absolute error rates may change faster than the broader human-factors pattern.
- [inference; source: https://arxiv.org/abs/2404.04332; https://arxiv.org/html/2401.01301v1] Policy interpretation risk will vary by task type, because some ambiguity classes are easier for models than open-ended legal or organisational interpretation tasks.
- [inference; source: https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-governance-culture-incentives-behaviour.html] Organisational incentives may dominate interface improvements if escalation remains materially slower or more costly than accepting the assistant's answer.

### Open Questions

- Does numeric confidence plus direct quotation of the governing policy text outperform verbal hedging alone for enterprise users?
- Which escalation trigger best preserves verification without making the assistant unusably slow: ambiguity detection, policy-domain risk tiering, or explicit user uncertainty declarations?
- Can audit logs capture whether users inspected source text before acting on a policy answer strongly enough to support meaningful review?

---

## Output

- Type: knowledge
- Description: This item shows that policy-assistant safety depends less on fluent certainty than on uncertainty signaling matched to evidence and task stakes, evidence visibility, and escalation design. [inference; source: https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/; https://arxiv.org/abs/2306.13063; https://airc.nist.gov/airmf-resources/airmf/5-sec-core/; https://colab.ws/articles/10.1037/xge0000033]
- Links:
  - https://www.microsoft.com/en-us/research/publication/im-not-sure-but-examining-the-impact-of-large-language-models-uncertainty-expression-on-user-reliance-and-trust/
  - https://arxiv.org/html/2401.01301v1
  - https://arxiv.org/abs/2306.13063
