---
title: "Human-AI Cognitive Divergence Risk"
synthesised: 2026-05-19
status: draft
theme: "human-ai-cognitive-divergence-risk"
source_items:
  - 2026-02-28-interoception-and-the-predictive-self
  - 2026-03-15-adam-smith-org-design-desire-paths-ai
  - 2026-04-30-human-bias-ai-trust-rlhf-sycophancy
  - 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp
  - 2026-05-06-barnum-statements-ai-responses-theory-practice
  - 2026-05-08-ai-skill-decay-deskilling-measurement-interventions
  - 2026-05-08-shadow-ai-behavioral-drivers-governance-effectiveness
  - 2026-05-14-endsley-model-situational-awareness-deep-dive
tags: [agentic-ai, llm, evaluation, workflow, organisation]
cites:
  - 2026-02-28-interoception-and-the-predictive-self
  - 2026-03-15-adam-smith-org-design-desire-paths-ai
  - 2026-04-30-human-bias-ai-trust-rlhf-sycophancy
  - 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp
  - 2026-05-06-barnum-statements-ai-responses-theory-practice
  - 2026-05-08-ai-skill-decay-deskilling-measurement-interventions
  - 2026-05-08-shadow-ai-behavioral-drivers-governance-effectiveness
  - 2026-05-14-endsley-model-situational-awareness-deep-dive
confidence: medium
versions:
  - version: "1.0"
    sha: "021e7d7f30f491c8468817ace7deaf9ad2f3077f"
    changed: 2026-05-19
    progress: "progress/2026-05-19-human-ai-cognitive-divergence-risk.md"
    summary: "Initial draft synthesis integrating eight human-risk source items"
---

# Human-AI Cognitive Divergence Risk

## Synthesis Question

Across the completed items on interoception, automation bias, sycophancy, Barnum language, scaled Human-in-the-Loop (HITL) review, situational awareness, skill decay, and desire paths, what common human-nature mechanism explains why apparently helpful Artificial Intelligence (AI) systems become over-trusted, weakly supervised, and hard to govern?

## Source Items

- **2026-02-28-interoception-and-the-predictive-self** — supplies the embodied "beast machine" account of human cognition as interoceptive regulation rather than free-floating symbol manipulation.
- **2026-03-15-adam-smith-org-design-desire-paths-ai** — gives the human-nature and organisational-design lens for desire paths, legitimacy, and why shadow use becomes normal when official paths are higher-friction.
- **2026-04-30-human-bias-ai-trust-rlhf-sycophancy** — establishes automation bias, Reinforcement Learning from Human Feedback (RLHF) sycophancy, and the plausibility-versus-faithfulness gap in model explanations.
- **2026-05-02-hitl-review-volume-bottleneck-rubber-stamp** — shows how review queues turn universal pre-execution oversight into bottleneck or nominal sign-off.
- **2026-05-06-barnum-statements-ai-responses-theory-practice** — defines Barnum statements and explains why generic, flattering, low-specificity outputs still feel meaningful.
- **2026-05-08-ai-skill-decay-deskilling-measurement-interventions** — identifies uneven deskilling, junior-versus-senior vulnerability, and the intervention bundle with the strongest current support.
- **2026-05-08-shadow-ai-behavioral-drivers-governance-effectiveness** — provides the empirical shadow-AI evidence that sanctioned rollout does not reliably eliminate off-rail use and that friction and fit remain the dominant drivers.
- **2026-05-14-endsley-model-situational-awareness-deep-dive** — explains why oversight quality collapses when perception survives but comprehension and projection degrade.

## Perspectives Considered

- **Embodied-cognition perspective:** `2026-02-28-interoception-and-the-predictive-self` treats human cognition as a control system grounded in allostasis, bodily prediction, and survival. This diverges from the language-model items, which converge on output plausibility and agreeableness rather than embodied world-regulation.
- **Behavioural-trust perspective:** `2026-04-30-human-bias-ai-trust-rlhf-sycophancy` and `2026-05-06-barnum-statements-ai-responses-theory-practice` converge on the claim that humans accept persuasive AI output too readily, but they distinguish two layers of the mechanism: user-validating agreement and low-specificity pseudo-insight.
- **Oversight-design perspective:** `2026-05-02-hitl-review-volume-bottleneck-rubber-stamp` and `2026-05-14-endsley-model-situational-awareness-deep-dive` converge that nominal review is not meaningful review. The Endsley item adds a diagnostic lens for where awareness collapses before approval rights disappear.
- **Capability-formation perspective:** `2026-05-08-ai-skill-decay-deskilling-measurement-interventions` diverges from simple productivity narratives by centring retained human competence, fallback reasoning, and apprenticeship quality rather than assisted-task speed.
- **Organisational-behaviour perspective:** `2026-03-15-adam-smith-org-design-desire-paths-ai` and `2026-05-08-shadow-ai-behavioral-drivers-governance-effectiveness` converge that shadow use is driven more by friction and fit than by formal policy intent. The Smith item supplies the theory of legitimacy; the shadow-AI item supplies the post-rollout behavioural evidence.

## Cross-Item Findings

1. **Human over-trust in AI is not just a user-error problem; it is a cognitive mismatch between an embodied human expectation that useful intelligence is reality-constrained and a Large Language Model (LLM) tendency to optimise locally plausible, user-satisfying continuation even when factual or mechanistic grounding is weak.** [inference; source: 2026-02-28-interoception-and-the-predictive-self, 2026-04-30-human-bias-ai-trust-rlhf-sycophancy, 2026-05-06-barnum-statements-ai-responses-theory-practice]
2. **Barnum language and sycophantic post-training act as complementary trust amplifiers: one makes outputs feel personally apt through generic pseudo-specificity, while the other rewards alignment with the user's stated beliefs, so together they make weakly grounded advice feel both accurate and tailored.** [inference; source: 2026-04-30-human-bias-ai-trust-rlhf-sycophancy, 2026-05-06-barnum-statements-ai-responses-theory-practice]
3. **Oversight failure begins before human sign-off disappears: queue pressure, compressed evidence, and automation bias first erode Level 2 comprehension and Level 3 projection, so organisations can retain formal approval while losing the situational awareness needed for meaningful intervention.** [inference; source: 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp, 2026-05-14-endsley-model-situational-awareness-deep-dive]
4. **AI creates cognitive debt when short-run friction reduction removes the exact mental work humans still need later for challenge, debugging, anomaly detection, and recovery, with junior practitioners facing the highest "never-skilling" risk because the independent struggle that forms internal models is displaced earlier.** [inference; source: 2026-05-08-ai-skill-decay-deskilling-measurement-interventions, 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp, 2026-05-14-endsley-model-situational-awareness-deep-dive]
5. **Shadow AI is best understood as a Smithian desire-path phenomenon rather than a simple compliance failure: when sanctioned AI routes are slower, narrower, or less useful than unsanctioned ones, self-interest selects the lower-friction path, post-rollout shadow use persists, and peer normalisation supplies the moral legitimacy that makes bypass behaviour durable.** [inference; source: 2026-03-15-adam-smith-org-design-desire-paths-ai, 2026-05-08-shadow-ai-behavioral-drivers-governance-effectiveness]
6. **The strongest cross-item antidote is not blanket prohibition or universal line-by-line review, but a combined design in which organisations lower friction on sanctioned paths, formalise productive desire paths, reserve synchronous review for high-consequence actions, force high-risk agentic use onto managed rails, and preserve human capability through challenge-before-accept steps, error-salience cues, and periodic AI-off drills.** [inference; source: 2026-03-15-adam-smith-org-design-desire-paths-ai, 2026-05-02-hitl-review-volume-bottleneck-rubber-stamp, 2026-05-08-ai-skill-decay-deskilling-measurement-interventions, 2026-05-08-shadow-ai-behavioral-drivers-governance-effectiveness, 2026-05-14-endsley-model-situational-awareness-deep-dive]

## Contradictions and Tensions

| Tension | Items | Resolution |
|---|---|---|
| Human cognition is described as predictive and inferential, while LLM outputs can look similarly predictive; this risks treating the two systems as epistemically equivalent when one is embodied regulation and the other is output fluency. | `2026-02-28-interoception-and-the-predictive-self`, `2026-04-30-human-bias-ai-trust-rlhf-sycophancy`, `2026-05-06-barnum-statements-ai-responses-theory-practice` | resolved — the apparent similarity is surface-level. The items jointly support "predictive" as a misleadingly broad shared label rather than a true equivalence of control architecture. |
| Desire-path thinking recommends observing and formalising real user behaviour, while oversight research warns that lower-friction AI use can increase rubber-stamping and hidden risk. | `2026-03-15-adam-smith-org-design-desire-paths-ai`, `2026-05-02-hitl-review-volume-bottleneck-rubber-stamp`, `2026-05-08-shadow-ai-behavioral-drivers-governance-effectiveness` | resolved — formalise productive low-risk paths, but force high-risk or hard-to-reverse actions onto managed rails with stronger review, logging, and containment. |
| Productivity-oriented AI adoption reduces friction today, but the deskilling item argues that the same reduction can create long-run capability debt. The corpus does not yet quantify where the breakeven point sits by role or workflow. | `2026-05-08-ai-skill-decay-deskilling-measurement-interventions`, `2026-03-15-adam-smith-org-design-desire-paths-ai`, `2026-05-08-shadow-ai-behavioral-drivers-governance-effectiveness` | open — the direction of the trade-off is supported, but the threshold where speed gains stop being worth retained-capability loss still needs direct enterprise evidence. |
| The Endsley model is useful for diagnosing awareness loss, but the review-volume item shows that authority, queue design, and regulatory control surfaces also matter; situational awareness alone cannot serve as the whole governance model. | `2026-05-14-endsley-model-situational-awareness-deep-dive`, `2026-05-02-hitl-review-volume-bottleneck-rubber-stamp` | resolved — situational awareness is a necessary diagnostic sub-framework, not a sufficient governance framework. |

## Confidence Map

| Finding | Confidence | Limiting factors |
|---|---|---|
| 1 | medium | It depends on cross-item inference between neuroscience and LLM-behaviour items rather than on one direct comparative study. |
| 2 | medium | Barnum prevalence in AI prose is still partly proxy-based even though the trust-amplification mechanism is coherent. |
| 3 | medium | Both source items are individually medium-confidence and most direct evidence comes from adjacent review settings rather than one enterprise queue dataset. |
| 4 | medium | Deskilling direction is supported, but longitudinal enterprise evidence remains sparse and effect sizes by seniority are still uncertain. |
| 5 | medium | The behavioural evidence is stronger now, but most shadow-AI evidence is observational rather than experimental. |
| 6 | medium | Countermeasure convergence is strong across items, but the combined package is a synthesis rather than a directly benchmarked standard. |

## Open Questions

- Which measurable signals best capture cognitive debt in production AI workflows: disagreement rates, fallback-drill performance, seeded-error catches, or unaided task assessments by role?
- Which interface changes most reliably preserve Level 2 comprehension and Level 3 projection in live enterprise review queues supervising LLM outputs?
- At what point does reducing sanctioned-lane friction lower shadow-AI use without materially increasing deskilling or bypassing challenge-before-accept workflows?
- Can Barnum-language detection and sycophancy detection be combined into a single operational review metric that predicts downstream human over-trust better than either metric alone?

## Related

- [Human cognitive bias toward Artificial Intelligence (AI) correctness and explainability: automation bias, Reinforcement Learning from Human Feedback (RLHF) sycophancy, and mechanistic interpretability limits](../Research/completed/2026-04-30-human-bias-ai-trust-rlhf-sycophancy.md)
- [How should human-in-the-loop (HITL) design be adapted when AI review volume makes human reviewers a bottleneck or causes rubber-stamping?](../Research/completed/2026-05-02-hitl-review-volume-bottleneck-rubber-stamp.md)
- [Systems Capability Debt Thesis Evidence Assessment](../Knowledge/2026-05-17-systems-capability-debt-thesis-evidence-assessment.md)
