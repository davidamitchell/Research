---
review_count: 2
title: "Contract theory formulation and statistical criteria for contracts"
added: 2026-05-21T11:12:00+00:00
status: reviewing
priority: medium
blocks: []
tags: [economics, evaluation, invariants]
started: 2026-05-22T06:56:33+00:00
completed: ~
output: [knowledge]
cites: []
related:
  - 2026-05-18-rq1-3-instrumentalism-failure-modes
  - 2026-05-18-rq2-4-causal-hierarchy-formal-limits
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Contract theory formulation and statistical criteria for contracts

## Research Question

What is contract theory, how is a contract-theory model formally formulated, what is meant by a statistical contract, meaning a contract or protocol whose payoffs depend on statistical evidence, and what statistical criteria should be used to evaluate such contracts?

## Scope

**In scope:**
- Core definitions and goals of contract theory in economics
- Standard formal formulation of contract-theory models, including actors, information structure, objectives, and constraints
- Definitions of statistical contracts in relevant economics and applied statistics literature
- Statistical criteria used to evaluate contracts, including identification, fit, predictive validity, robustness, and incentive effects

**Out of scope:**
- Legal advice or jurisdiction-specific contract drafting requirements
- Clause-by-clause review of commercial legal contracts
- Building or calibrating a full empirical model in this item

**Constraints:**
- Use publicly accessible sources with URLs
- Focus on conceptual and methodological criteria, not case-specific legal recommendations

## Context

This item is meant to support later research that needs contract models which are economically coherent, empirically estimable, and resistant to naive use of predictive fit alone as an adequacy test. [inference; source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html]

## Approach

1. Define contract theory and summarize its main problem classes, for example principal-agent settings, where one party delegates to another under asymmetric information.
2. Decompose the canonical formulation of a contract-theory model, including utility functions, incentive-compatibility constraints, meaning constraints that make the agent prefer the intended action, and participation constraints, meaning constraints that keep the agent willing to enter the contract.
3. Clarify how "statistical contract" is used in the literature and which contexts it applies to.
4. Extract and compare statistical evaluation criteria used to assess contract models.
5. Synthesize a practical checklist of criteria for deciding whether a contract model is statistically adequate for a stated use case.

## Sources

**Consulted:**

- [x] [Holmstrom (1979) Moral Hazard and Observability](https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html)
- [x] [Royal Swedish Academy of Sciences (2016) Contract theory](https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/)
- [x] [Curriculum Open-access Resources in Economics (CORE Econ) (n.d.) Principal-agent relationships, hidden actions, and incomplete contracts](https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html)
- [x] [Acemoglu (2011) Moral Hazard and Applications](https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf)
- [x] [Bates et al. (2024) Principal-Agent Hypothesis Testing](https://arxiv.org/abs/2205.06812)
- [x] [Galiani and Pantano (2021) Structural Models: Inception and Frontier](https://www.nber.org/papers/w28698)
- [x] [Reiss and Wolak (2007) Structural Econometric Modeling: Rationales and Examples from Industrial Organization](https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf)
- [x] [Low and Meghir (2017) The Use of Structural Models in Econometrics](https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33)
- [x] [Heckman and Vytlacil (2005) Structural Equations, Treatment Effects and Econometric Policy Evaluation](https://www.nber.org/papers/w11259)
- [x] [Mitchell (2026) Research Question 1.3: Failure Modes of Instrumentalism When Applied to Complex Dynamic Systems Under Distribution Shift](https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html)
- [x] [Mitchell (2026) Research Question 2.4: Pearl's Causal Hierarchy and the formal limits of observational data for intervention and counterfactual reasoning](https://davidamitchell.github.io/Research/research/2026-05-18-rq2-4-causal-hierarchy-formal-limits.html)

**Identified but not consulted:**

- [ ] [Laffont and Martimort (2002) The Theory of Incentives: The Principal-Agent Model](https://press.princeton.edu/books/hardcover/9780691091846/the-theory-of-incentives)
- [ ] [Organisation for Economic Co-operation and Development (OECD) Handbook on Constructing Composite Indicators](https://www.oecd.org/en/publications/handbook-on-constructing-composite-indicators_9789264043466-en.html)

---

## Research Skill Output

### §0 Initialise

- Question: what is contract theory, how is a contract-theory model formulated, what is a statistical contract, and which statistical criteria should be used to evaluate such a contract?
- Scope: economic contract theory, canonical principal-agent formulation, meaning a principal delegates to an agent under asymmetric information, current usage of statistical contract, and statistical adequacy criteria for empirical or incentive-aware contract models.
- Constraints: full-mode investigation, URL-backed sources only, public-source replacements for blocked seed links, canonical tags only, and mirrored §6 plus Findings output.
- Output: executive summary, key findings, evidence map, assumptions, analysis, risks and gaps, open questions, and knowledge output metadata.
- prior_completed_item_sweep: no direct overlap found; adjacent items on invariance under shift and observational limits treated as thematic context only.

### §1 Question Decomposition

1. Core definition
   1.1 What problem does contract theory solve in economics?
   1.2 Which recurring settings anchor the field, for example moral hazard, meaning hidden actions that create incentive problems, adverse selection, multitasking, and incomplete contracts?
2. Canonical formulation
   2.1 Who are the principal and the agent?
   2.2 What observables, hidden actions, hidden types, payoffs, and uncertainty terms must be specified?
   2.3 How are participation and incentive-compatibility constraints written in a standard model?
3. Statistical contract terminology
   3.1 Does the literature use "statistical contract" as a settled older economics term, or mainly in newer work?
   3.2 What distinguishes a statistical contract from a standard incentive contract?
4. Statistical evaluation
   4.1 Which criteria establish whether a contract model is identified and estimable?
   4.2 Which criteria establish whether the model fits data, predicts out of sample, and supports credible counterfactuals, meaning claims about what would happen under a different policy or contract?
   4.3 Which criteria establish whether the statistical rule remains robust when strategic agents adapt to it?
5. Synthesis
   5.1 Which criteria are necessary for any empirical contract model?
   5.2 Which extra criteria are necessary when payoffs depend directly on statistical evidence?

### §2 Investigation

#### 2.1 Contract theory definition and problem class

- [fact] The Royal Swedish Academy of Sciences describes contract theory as a general way to understand contract design and to explain why contracts take different forms when parties need to regulate future actions, share risk, and manage conflicting interests under imperfect measurement. [source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]
- [fact] Curriculum Open-access Resources in Economics (CORE Econ) explains principal-agent problems as cases of asymmetric information and incomplete contracts in which the principal cannot observe or verify the agent's action well enough to write a complete enforceable contract around it. [source: https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html]
- [fact] Holmstrom's 1979 abstract states the canonical moral-hazard problem as a principal-agent relationship under imperfect information and derives conditions under which information beyond realized payoff improves contracting. [source: https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html]
- [inference] The common core across these sources is that contract theory is about designing incentives and allocating risk or control when relevant actions, types, or contingencies are only imperfectly observable or not contractible at all. [source: https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html]

#### 2.2 Canonical formal formulation

- [fact] Acemoglu's lecture notes write a basic moral-hazard model with a worker as agent and employer as principal, agent utility H(w,a) = U(w) - c(a), an outside option for the agent, output x(a,θ) that depends on effort and a random term, and principal payoff V(x - w). [source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf]
- [fact] The same notes define the participation constraint as the requirement that the agent's expected utility from the contract is at least as large as the outside option or reservation utility. [source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf]
- [fact] The same notes define the incentive-compatibility constraint as the requirement that the desired action yields at least as much expected utility to the agent as any alternative action. [source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf]
- [fact] Nobel's overview adds that later contract-theory work extends this baseline to multitasking, team production, ownership, and incomplete contracts, where the design variable may be decision rights rather than only pay-for-performance terms. [source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]
- [inference] A minimally explicit contract-theory model therefore needs at least: parties, action or type space, information structure, outcome technology, stochastic term, utility or payoff functions, feasible contract space, participation constraint, incentive-compatibility constraint, and the objective the principal is optimizing. [source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]

#### 2.3 Meaning of "statistical contract"

- Access note: seeded Princeton Press textbook URL -> 404 this session.
- Access note: seeded stable-link URL -> 403 this session.
- [fact] Bates et al. use the phrase "statistical contracts" for statistical protocols whose payoffs depend on statistical evidence and whose design must account for strategic agent responses to evidentiary rules. [source: https://arxiv.org/abs/2205.06812]
- [fact] In their setup, the principal offers a menu of license functions, the agent decides whether to incur the cost of generating evidence, and the payoff cap depends on the realized evidence, so the contract is defined jointly by the incentive rule and the statistical test or evidence-generating mechanism. [source: https://arxiv.org/abs/2205.06812]
- [fact] Bates et al. show with a stylized drug-approval example that a protocol with fixed type-I error and power can still induce bad entry incentives when the agent's approval payoff is large enough, so inferential validity alone does not determine social performance. [source: https://arxiv.org/abs/2205.06812]
- [inference] In the accessible literature, "statistical contract" is not a dominant older label for all empirical contract models; instead, it is a newer, narrower term for contracts or approval protocols where evidence rules and incentives are explicitly designed together. [source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html]
- [assumption] Because the exact phrase appears mainly in recent incentive-aware inference work rather than in classical open-access expositions, this item treats the Bates et al. usage as the current source-backed operational meaning of "statistical contract." [source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]

#### 2.4 Statistical criteria for evaluation

- [fact] Reiss and Wolak state that structural econometric models should be developed and evaluated with explicit attention to sources of unobservables, the stochastic model, identification, estimation, and the role of nonexperimental data. [source: https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf]
- [fact] Galiani and Pantano argue that structural models should be judged by identification, estimation, external validity, and validation, including reserving credible exogenous variation for validation and using randomized controlled trials as a first-best opportunity for out-of-sample validation when possible. [source: https://www.nber.org/papers/w28698]
- [fact] Low and Meghir describe the central payoff of structural models as identifying mechanisms and supporting counterfactual policy analysis, which means adequacy depends on more than in-sample fit or reduced-form correlation. [source: https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33]
- [fact] Heckman and Vytlacil frame econometric policy evaluation around parameters intended to remain stable when policy changes, which makes credible policy or contract evaluation depend on whether the model structure travels beyond the observed sample. [source: https://www.nber.org/papers/w11259]
- [fact] Bates et al. add an extra criterion specific to statistical contracts: the evidence rule must be robust to strategic behavior because looser evidence standards can amplify low-value or manipulative participation by the agent. [source: https://arxiv.org/abs/2205.06812]
- [inference] For empirical contract models, the relevant statistical criteria are at least identification, estimability, fit to observed behavior, out-of-sample predictive validity, sensitivity or robustness to modeling assumptions, and counterfactual credibility under changed environments. [source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf; https://www.nber.org/papers/w11259]
- [inference] For statistical contracts in the narrower Bates et al. sense, the evaluation set must also include incentive robustness, meaning whether the contract still performs acceptably once strategic agents adapt trial entry, effort, or evidence-generation behavior to the rule itself. [source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]

#### 2.5 Practical adequacy checklist

- [inference] A statistically adequate contract model should first specify the use case, for example explanation, estimation, prediction, screening, or policy design, because different uses require different tolerances for fit error, instability, and counterfactual extrapolation. [source: https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://www.nber.org/papers/w28698]
- [inference] The model should then demonstrate observable linkage, meaning each key latent construct, such as effort, type, or quality, has either a direct measure, a justified proxy, or an explicit identification strategy. [source: https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf; https://www.nber.org/papers/w28698]
- [inference] The model should be checked for predictive and policy discipline separately, because a model that fits current data can still fail as a decision aid if its deeper parameters are not stable under intervention or environmental change. [source: https://www.nber.org/papers/w28698; https://www.nber.org/papers/w11259; https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-4-causal-hierarchy-formal-limits.html]
- [inference] When statistical evidence is itself part of the contract, adequacy also requires simulating or otherwise analyzing strategic adaptation to the evidentiary threshold, because false-positive and false-negative properties are not policy sufficient once entry incentives are endogenous. [source: https://arxiv.org/abs/2205.06812]

### §3 Reasoning

- [inference] Classical contract theory and modern statistical-contract work both treat incentives and the information structure governing what is observed and rewarded as jointly determining contract performance. [source: https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://arxiv.org/abs/2205.06812]
- [inference] The best way to answer the research question is therefore to distinguish two layers of evaluation: baseline structural-model adequacy and the extra incentive-aware adequacy needed when statistical evidence directly drives payoffs or approval. [source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://arxiv.org/abs/2205.06812]
- [assumption] This item treats identification, out-of-sample validation, and counterfactual credibility as statistical criteria even when some economists would classify them partly as econometric or methodological criteria, because the question asks for criteria used to evaluate statistical adequacy in practice. [source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf]

### §4 Consistency Check

- [inference] The consulted sources align on the core principal-agent formulation with participation and incentive-compatibility constraints, even though they emphasize different extensions such as pay-for-performance, multitasking, or incomplete contracts. [source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]
- [inference] The main ambiguity is terminological rather than substantive: classical open-access sources define contract theory broadly, while the exact phrase "statistical contract" is concentrated in newer work on incentive-aware statistical protocols. [source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://arxiv.org/abs/2205.06812]
- [inference] The ambiguity is resolved by treating "statistical contract" as a narrower subclass of contract or mechanism, not as a synonym for contract theory as a whole. [source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]
- [inference] No source supports using fit alone as a sufficient evaluation criterion for contract models; every consulted evaluation source requires some combination of identification, validation, or counterfactual discipline beyond in-sample agreement. [source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf; https://www.nber.org/papers/w11259]

### §5 Depth and Breadth Expansion

- [inference] Technical lens: the model must specify which variables are latent, which are observed, what generates outcome noise, and how the contract maps observations into transfers or decision rights. [source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf]
- [inference] Economic lens: the adequacy of a contract is tied to the agent's outside option, risk exposure, and adaptation incentives, alongside whether the econometrician can estimate coefficients. [source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://arxiv.org/abs/2205.06812]
- [fact] Historical lens: contract theory widened from simple moral-hazard pay schedules to multitasking, ownership, and incomplete contracts, so a modern evaluation standard cannot assume that all relevant contract terms reduce to one observable performance measure. [source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]
- [inference] Behavioral lens: once evidentiary thresholds become known, strategic agents can change entry or effort decisions to exploit them, so testing rules become part of the incentive environment rather than neutral measurement devices. [source: https://arxiv.org/abs/2205.06812]
- [inference] These lenses imply that a statistically adequate contract model is one whose measurements, incentives, and decision use remain aligned, rather than one that merely recovers stable coefficients inside one sample. [source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://arxiv.org/abs/2205.06812]

### §6 Synthesis

**Executive summary:**

Contract theory is an incentive-design framework for economic relationships with conflicting interests, hidden information, or incomplete observability. [fact; source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html]

A canonical contract-theory model specifies a principal, an agent, an outcome technology with uncertainty, payoff or utility functions, an information structure, a feasible contract space, and participation plus incentive-compatibility constraints, meaning constraints that make the agent prefer the intended action. [fact; source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]

In the accessible evidence base for this item, the exact phrase "statistical contract" appears as a narrow label for a contract or protocol whose payoffs depend on statistical evidence and whose design must anticipate strategic adaptation to the evidence rule itself. [inference; source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html]

The relevant statistical criteria therefore combine standard structural-model tests, identification, estimation discipline, fit, validation, robustness, and counterfactual credibility, with an extra incentive-robustness test that asks whether strategic agents can profitably distort participation or evidence generation under the rule. [inference; source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf; https://www.nber.org/papers/w11259; https://arxiv.org/abs/2205.06812]

**Key findings:**

1. **Contract theory studies how principals structure incentives, risk sharing, and decision rights when agents possess hidden actions, hidden types, or non-contractible contingencies that prevent complete ex ante contracting.** ([fact]; high confidence; source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html)
2. **A standard contract-theory formulation requires explicit specification of the parties, the information structure, the stochastic outcome process, the agent's utility and outside option, the principal's payoff, and the participation and incentive-compatibility constraints that define feasible inducement.** ([fact]; high confidence; source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/)
3. **In the accessible evidence base for this item, the exact phrase "statistical contract" appears as a narrow label for incentive-aware evidence protocols, especially in recent principal-agent hypothesis-testing work, rather than as a demonstrated blanket synonym for any empirical contract model.** ([inference]; medium confidence; source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html)
4. **For ordinary empirical contract models, statistical adequacy starts with identification and estimability, because the analyst must show how latent constructs such as effort, type, or quality are linked to observables or justified proxies.** ([inference]; high confidence; source: https://www.nber.org/papers/w28698; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf)
5. **Fit and prediction are necessary but not sufficient evaluation criteria, because structural contract models are valued partly for mechanism recovery and counterfactual policy analysis rather than only for reproducing the current sample.** ([inference]; high confidence; source: https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://www.nber.org/papers/w28698; https://www.nber.org/papers/w11259)
6. **Robust evaluation of a contract model requires sensitivity checks on functional-form, stochastic, and environmental assumptions, because external validity and structure that remains stable under policy change determine whether conclusions travel beyond the estimation setting.** ([inference]; high confidence; source: https://www.nber.org/papers/w28698; https://www.nber.org/papers/w11259; https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-4-causal-hierarchy-formal-limits.html)
7. **Bates et al. show in their regulator-firm hypothesis-testing model that inferential error rates must be evaluated together with strategic response, because a statistically valid threshold can still make weak candidates profitable to submit when approval payoffs are large enough.** ([fact]; medium confidence; source: https://arxiv.org/abs/2205.06812)
8. **A practical adequacy checklist is sequential: define the contractual objective, specify observables and latent variables, prove or justify identification, test fit and out-of-sample behavior, examine counterfactual stability, and then test whether the evidence rule remains incentive compatible once agents adapt to it.** ([inference]; medium confidence; source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://arxiv.org/abs/2205.06812)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Contract theory is an incentive-design field for hidden-information and incomplete-contract problems. | https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/ ; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html ; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html | high | Core field definition |
| [fact] Canonical formulation includes parties, uncertainty, utilities, information structure, participation, and incentive compatibility. | https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf ; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/ | high | Baseline model structure |
| [inference] In the accessible evidence base for this item, the exact phrase "statistical contract" appears as a narrow evidence-linked term. | https://arxiv.org/abs/2205.06812 ; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/ ; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html | medium | Term-usage boundary |
| [inference] Adequacy begins with identification and observables-to-latents discipline. | https://www.nber.org/papers/w28698 ; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf | high | Structural estimation baseline |
| [inference] Fit alone is insufficient because structural models are used for mechanism and counterfactual analysis. | https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33 ; https://www.nber.org/papers/w28698 ; https://www.nber.org/papers/w11259 | high | Beyond in-sample fit |
| [inference] Robustness and external-validity checks are required for credible use beyond one environment. | https://www.nber.org/papers/w28698 ; https://www.nber.org/papers/w11259 ; https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html ; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-4-causal-hierarchy-formal-limits.html | high | Stability under change |
| [fact] Bates et al.'s statistical-contract model requires incentive-robustness checks against strategic adaptation to evidence thresholds. | https://arxiv.org/abs/2205.06812 | medium | Extra criterion |
| [inference] A sequential adequacy checklist is a practical synthesis for applied use. | https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf ; https://www.nber.org/papers/w28698 ; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33 ; https://arxiv.org/abs/2205.06812 | medium | Applied synthesis |

**Assumptions:**

- [assumption] The recent Bates et al. usage is the operational definition used in this item because it is the strongest accessible source using the exact phrase and binding it to a principal-agent formalism. [source: https://arxiv.org/abs/2205.06812]
- [assumption] Structural-model evaluation criteria transfer to empirical contract models because contract models are a strategic subset of structural econometric models rather than a separate statistical genus. [source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf]

**Analysis:**

Core evidence for the field definition and canonical formulation comes from the Nobel overview, Curriculum Open-access Resources in Economics (CORE Econ), Holmstrom's abstract, and Acemoglu's lecture notes, because these sources directly define the problem class and write down the underlying moral-hazard structure. [inference; source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html; https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf]

An alternative reading of "statistical contract" would treat it as any contract studied with econometric data, but the accessible exact-phrase evidence does not support that broader meaning as the dominant usage. [inference; source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]

The evaluation criteria can be synthesized from structural-econometrics sources because they explicitly discuss formulation, identification, estimation, validation, and policy use, which map directly onto what an empirical contract model must accomplish. [inference; source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf; https://www.nber.org/papers/w11259]

Bates et al. sharpen this synthesis by showing that once evidence thresholds affect agent entry or effort decisions, statistical adequacy must include incentive robustness alongside nominal inferential properties such as type-I error or power. [inference; source: https://arxiv.org/abs/2205.06812]

Related completed items on instrumentalism and causal hierarchy reinforce, rather than replace, the external sources by clarifying why invariance and counterfactual travel matter when the model will be used outside the estimation environment. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-4-causal-hierarchy-formal-limits.html; https://www.nber.org/papers/w28698; https://www.nber.org/papers/w11259]

**Risks, gaps, uncertainties:**

- [inference] The exact phrase "statistical contract" may have additional niche uses outside the accessible source set, so the terminology conclusion should be read as current-source-backed rather than exhaustive. [source: https://arxiv.org/abs/2205.06812]
- [inference] This item synthesizes open-access summaries and lecture material for classical contract theory, so a deeper full-text reading of older monographs could refine wording without likely changing the main adequacy checklist. [source: https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf]
- [inference] The checklist is strongest for empirical or policy-use models and may be heavier than necessary for purely pedagogical toy models that are not intended for estimation or decision support. [source: https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://www.nber.org/papers/w28698]

**Open questions:**

- [inference] Which empirical papers provide the clearest worked examples of estimating adverse-selection and moral-hazard contracts with modern causal-validation practice? [source: https://www.nber.org/papers/w28698; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf]
- [inference] How should e-value-based statistical contracts be compared empirically with p-value-threshold and Bayesian approval rules under the same strategic-entry environment? [source: https://arxiv.org/abs/2205.06812]

### §7 Recursive Review

review_result: pass
acronym_audit: passed
claim_label_audit: passed
source_url_audit: passed
findings_synthesis_parity: aligned
confidence_rating: medium

---

## Findings

### Executive Summary

Contract theory is an incentive-design framework for economic relationships with conflicting interests, hidden information, or incomplete observability. [fact; source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html]

A canonical contract-theory model specifies a principal, an agent, an outcome technology with uncertainty, payoff or utility functions, an information structure, a feasible contract space, and participation plus incentive-compatibility constraints, meaning constraints that make the agent prefer the intended action. [fact; source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]

In the accessible evidence base for this item, the exact phrase "statistical contract" appears as a narrow label for a contract or protocol whose payoffs depend on statistical evidence and whose design must anticipate strategic adaptation to the evidence rule itself. [inference; source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html]

The relevant statistical criteria therefore combine standard structural-model tests, identification, estimation discipline, fit, validation, robustness, and counterfactual credibility, with an extra incentive-robustness test that asks whether strategic agents can profitably distort participation or evidence generation under the rule. [inference; source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf; https://www.nber.org/papers/w11259; https://arxiv.org/abs/2205.06812]

### Key Findings

1. **Contract theory studies how principals structure incentives, risk sharing, and decision rights when agents possess hidden actions, hidden types, or non-contractible contingencies that prevent complete ex ante contracting.** ([fact]; high confidence; source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html)
2. **A standard contract-theory formulation requires explicit specification of the parties, the information structure, the stochastic outcome process, the agent's utility and outside option, the principal's payoff, and the participation and incentive-compatibility constraints, meaning the constraints that make the agent prefer the intended action and accept the contract.** ([fact]; high confidence; source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/)
3. **In the accessible evidence base for this item, the exact phrase "statistical contract" appears as a narrow label for incentive-aware evidence protocols, especially in recent principal-agent hypothesis-testing work, rather than as a demonstrated blanket synonym for any empirical contract model.** ([inference]; medium confidence; source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html)
4. **For ordinary empirical contract models, statistical adequacy starts with identification and estimability, because the analyst must show how latent constructs such as effort, type, or quality are linked to observables or justified proxies.** ([inference]; high confidence; source: https://www.nber.org/papers/w28698; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf)
5. **Fit and prediction are necessary but not sufficient evaluation criteria, because structural contract models are valued partly for mechanism recovery and counterfactual policy analysis rather than only for reproducing the current sample.** ([inference]; high confidence; source: https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://www.nber.org/papers/w28698; https://www.nber.org/papers/w11259)
6. **Robust evaluation of a contract model requires sensitivity checks on functional-form, stochastic, and environmental assumptions, because external validity and structure that remains stable under policy change determine whether conclusions travel beyond the estimation setting.** ([inference]; high confidence; source: https://www.nber.org/papers/w28698; https://www.nber.org/papers/w11259; https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-4-causal-hierarchy-formal-limits.html)
7. **Bates et al. show in their regulator-firm hypothesis-testing model that inferential error rates must be evaluated together with strategic response, because a statistically valid threshold can still make weak candidates profitable to submit when approval payoffs are large enough.** ([fact]; medium confidence; source: https://arxiv.org/abs/2205.06812)
8. **A practical adequacy checklist is sequential: define the contractual objective, specify observables and latent variables, prove or justify identification, test fit and out-of-sample behavior, examine counterfactual stability, and then test whether the evidence rule remains incentive compatible once agents adapt to it.** ([inference]; medium confidence; source: https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://arxiv.org/abs/2205.06812)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Contract theory is an incentive-design field for hidden-information and incomplete-contract problems. | https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/ ; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html ; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html | high | Core field definition |
| [fact] Canonical formulation includes parties, uncertainty, utilities, information structure, participation, and incentive compatibility, meaning the contract must make the agent accept and prefer the intended action. | https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf ; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/ | high | Baseline model structure |
| [inference] In the accessible evidence base for this item, the exact phrase "statistical contract" appears as a narrow evidence-linked term. | https://arxiv.org/abs/2205.06812 ; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/ ; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html | medium | Term-usage boundary |
| [inference] Adequacy begins with identification and observables-to-latents discipline. | https://www.nber.org/papers/w28698 ; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf | high | Structural estimation baseline |
| [inference] Fit alone is insufficient because structural models are used for mechanism and counterfactual analysis. | https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33 ; https://www.nber.org/papers/w28698 ; https://www.nber.org/papers/w11259 | high | Beyond in-sample fit |
| [inference] Robustness and external-validity checks are required for credible use beyond one environment. | https://www.nber.org/papers/w28698 ; https://www.nber.org/papers/w11259 ; https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html ; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-4-causal-hierarchy-formal-limits.html | high | Stability under change |
| [fact] Bates et al.'s statistical-contract model requires incentive-robustness checks against strategic adaptation to evidence thresholds. | https://arxiv.org/abs/2205.06812 | medium | Extra criterion |
| [inference] A sequential adequacy checklist is a practical synthesis for applied use. | https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf ; https://www.nber.org/papers/w28698 ; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33 ; https://arxiv.org/abs/2205.06812 | medium | Applied synthesis |

### Assumptions

- [assumption] The recent Bates et al. usage is the operational definition used in this item because it is the strongest accessible source using the exact phrase and binding it to a principal-agent formalism. [source: https://arxiv.org/abs/2205.06812]
- [assumption] Structural-model evaluation criteria transfer to empirical contract models because contract models are a strategic subset of structural econometric models rather than a separate statistical genus. [source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf]

### Analysis

Core evidence for the field definition and canonical formulation comes from the Nobel overview, Curriculum Open-access Resources in Economics (CORE Econ), Holmstrom's abstract, and Acemoglu's lecture notes, because these sources directly define the problem class and write down the underlying moral-hazard structure. [fact; source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://books.core-econ.org/the-economy/microeconomics/10-market-successes-failures-08-principal-agent-relationships.html; https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html; https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf]

An alternative reading of "statistical contract" would treat it as any contract studied with econometric data, but the accessible exact-phrase evidence does not support that broader meaning as the dominant usage. [inference; source: https://arxiv.org/abs/2205.06812; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/]

The evaluation criteria can be synthesized from structural-econometrics sources because they explicitly discuss formulation, identification, estimation, validation, and policy use, which map directly onto what an empirical contract model must accomplish. [inference; source: https://www.nber.org/papers/w28698; https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf; https://www.nber.org/papers/w11259]

Bates et al. sharpen this synthesis by showing that once evidence thresholds affect agent entry or effort decisions, statistical adequacy must include incentive robustness alongside nominal inferential properties such as type-I error or power. [fact; source: https://arxiv.org/abs/2205.06812]

Related completed items on instrumentalism and causal hierarchy reinforce, rather than replace, the external sources by clarifying why invariance and counterfactual travel matter when the model will be used outside the estimation environment. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-18-rq1-3-instrumentalism-failure-modes.html; https://davidamitchell.github.io/Research/research/2026-05-18-rq2-4-causal-hierarchy-formal-limits.html; https://www.nber.org/papers/w28698; https://www.nber.org/papers/w11259]

### Risks, Gaps, and Uncertainties

- [inference] The exact phrase "statistical contract" may have additional niche uses outside the accessible source set, so the terminology conclusion should be read as current-source-backed rather than exhaustive. [source: https://arxiv.org/abs/2205.06812]
- [inference] This item synthesizes open-access summaries and lecture material for classical contract theory, so a deeper full-text reading of older monographs could refine wording without likely changing the main adequacy checklist. [source: https://ideas.repec.org/a/rje/bellje/v10y1979ispringp74-91.html; https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf]
- [inference] The checklist is strongest for empirical or policy-use models and may be heavier than necessary for purely pedagogical toy models that are not intended for estimation or decision support. [source: https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33; https://www.nber.org/papers/w28698]

### Open Questions

- [inference] Which empirical papers provide the clearest worked examples of estimating adverse-selection and moral-hazard contracts with modern causal-validation practice? [source: https://www.nber.org/papers/w28698; https://web.stanford.edu/group/fwolak/cgi-bin/sites/default/files/files/Structural%20Econometric%20Modeling_Rationales%20and%20Examples%20From%20Industrial%20Organization_Reiss,%20Wolak.pdf]
- [inference] How should e-value-based statistical contracts be compared empirically with p-value-threshold and Bayesian approval rules under the same strategic-entry environment? [source: https://arxiv.org/abs/2205.06812]

---

## Output

- Type: knowledge
- Description: Research note defining contract theory, formalizing a canonical contract-theory model, and synthesizing a statistical adequacy checklist for empirical and evidence-linked contracts. [inference; source: https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/; https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf; https://arxiv.org/abs/2205.06812; https://www.nber.org/papers/w28698]
- Links:
  - https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/
  - https://economics.mit.edu/sites/default/files/inline-files/Lecture%206%20and%207%20-%20Moral%20Hazard%20and%20Applicaitons.pdf
  - https://arxiv.org/abs/2205.06812
