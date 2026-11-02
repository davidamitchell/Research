---
title: "Temporary specialist ring-fencing and re-convergence"
added: 2026-10-23T23:44:48+00:00
status: completed
priority: high
blocks: []
themes: [organisational-design, software-engineering, cost-performance, regulatory-compliance, enterprise-adoption]
started: 2026-11-02T05:18:26+00:00
completed: 2026-11-02T05:22:37+00:00
output: []
cites:
  - 2026-10-23-dependency-properties-coordination-mechanisms
related:
  - 2026-06-13-platform-engineering-innersource-hybrid-standardization
  - 2026-06-13-local-global-optima-knowledge-work-throughput
superseded_by: ~
supersedes: ~
item_type: primary
confidence: low
versions: []
---

# Temporary specialist ring-fencing and re-convergence

## Research Question

Given the dependency properties identified in the prior item (recurrence, uncertainty, and required speed, alongside terminus properties such as the cost of a wrong outcome and required certainty), under what combinations does temporarily ring-fencing specialist capacity in an autonomous, self-contained team with positive capacity produce higher delivery certainty at lower total life-cycle cost than remaining coupled to a shared specialist pool? What does the evidence measure about the cost and success rate of later re-converging the duplicated capability?

## Scope

**In scope:**
- Map the existing link-property and terminus-property set to the choice between sustained shared-specialist coordination and temporary ring-fencing.
- Compare delivery certainty and total life-cycle cost, including duplicated capacity, coordination, divergence, re-convergence, and failed convergence where evidence permits.
- Examine evidence on the conditions and outcomes of re-converging a capability after temporary duplication.
- Assess whether software clone-and-own cost evidence transfers to organisational team structures, and identify where that analogy breaks.
- Focus on specialist dependencies with high required certainty, including cases with substantial regulatory exposure.

**Out of scope:**
- A general catalogue of team-topology patterns.
- Detailed implementation recipes for positive-capacity models.
- Non-specialist, purely peer-to-peer dependencies.

**Constraints:** Separate direct evidence about organisational structures from software-reuse analogies. Distinguish measured costs and success rates from qualitative claims; treat missing measurements as gaps. Clarify how sources define positive capacity and re-convergence rather than assuming consistent definitions.

## Context

The completed item [Dependency properties and coordination mechanisms over time](https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html) established a candidate property set but left the high-certainty, specialist-ring-fencing case unresolved; this item narrows that decision to whether temporary duplication pays for itself after convergence is included. Related items on [platform engineering and InnerSource](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html) and [local versus global optimisation](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html) provide adjacent context, not an answer to this comparison.

## Approach

1. Map the prior item's candidate dependency and terminus properties to the ring-fencing decision. Identify any additional moderators, such as specialist scarcity or regulatory exposure, only where sources justify them.
2. Compare sustained shared-pool coordination with temporary autonomous ring-fencing on delivery certainty and full life-cycle cost. Record how each source defines and measures those outcomes.
3. Find organisational evidence on temporary duplication and later convergence, including the conditions associated with successful convergence, failure, and measured costs or rates.
4. Examine software clone-and-own cost evidence and assess which mechanisms plausibly transfer to teams, which do not, and what evidence supports the transfer.
5. Synthesize a property-based decision rule if evidence supports one; otherwise specify which combinations remain unmeasured and what evidence would resolve them.

## Related

- [Dependency properties and coordination mechanisms over time](https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html): supplies the candidate property set this item applies.
- [How do platform engineering, InnerSource, and standard-core plus local-extension operating models balance team autonomy with organisational standardisation?](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html): adjacent evidence on autonomy and shared capability.
- [How does local optimisation of team- and role-level tooling reduce organisation-level throughput?](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html): adjacent framing for local gains versus organisation-level costs.

## Sources

- [Ghabach et al. (2018) Clone-and-Own Software Product Derivation Based on Developer Preferences and Cost Estimation](https://hal.science/hal-01903006v1/document): software clone-and-own derivation and cost-estimation evidence.
- [Krüger and Berger (2020) An Empirical Analysis of the Costs of Clone- and Platform-Oriented Software Reuse](https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf): empirical software reuse-cost evidence relevant to convergence and transferability.
- [Dependency properties and coordination mechanisms over time](https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html): prior local research defining the candidate property set.
- [Jalbă and Nedelcu (2025) Exploring Success and Failure in Organizational Ambidexterity: Insights from a Systematic Literature Review](https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf): organisational evidence on separation followed by reintegration.
- [Tushman and O'Reilly (1996) Ambidextrous Organizations](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Organizational_Learning_and_Change/Tushman_&_OReilly_1996_Ambidextrous_Organizations.pdf): primary ambidexterity paper; scan not readable as text here.
- [How do platform engineering, InnerSource, and standard-core plus local-extension operating models balance team autonomy with organisational standardisation?](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html): prior local item on standard-core designs.
- [How does local optimisation of team- and role-level tooling reduce organisation-level throughput?](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html): prior local item on shared-constraint throughput.

---

## Research Skill Output

*(Full output from running the research skill: retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: under which combinations of dependency properties does temporarily ring-fencing specialist capacity (dedicating specialists to one autonomous, self-contained team instead of sharing them across teams) yield higher delivery certainty at lower total life-cycle cost than staying coupled to a shared specialist pool, and what is measured about the cost and success of later re-converging the duplicated capability?

Scope: link and terminus properties from the prior item; delivery certainty and life-cycle cost; evidence on re-convergence; transfer of software clone-and-own cost evidence (copying a system and adapting the copy) to teams.

Constraints: separate organisational evidence from software analogies; label measured values apart from qualitative claims; treat missing measurements as gaps.

Prior work cross-reference: the completed item on [dependency properties and coordination mechanisms](https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html) supplies the property set and already reports that convergence-cost quantification rests on eight cost estimations from one organisation. [fact; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
The completed items on [platform engineering, InnerSource and standard-core models](https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html) and on [local versus global optimisation](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html) are used in §2 and §5 as adjacent evidence. [assumption; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]

Working hypothesis: ring-fencing pays off only when the divergence period is short and the later convergence is planned, because the one measured convergence-cost result links cost to divergence duration. [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

### §1 Question Decomposition

- Q1: Which dependency properties from the prior item bear on the ring-fencing choice, and what moderators do sources justify?
- Q2: How do sources define and measure delivery certainty, life-cycle cost, positive capacity and re-convergence?
- Q3: What does organisational evidence measure about temporary separation followed by reintegration?
- Q4: What does software clone-and-own evidence measure about convergence cost, and which mechanisms transfer to teams?
- Q5: Does the evidence support a property-based decision rule, and which combinations remain unmeasured?

### §2 Investigation

Q1: property mapping.

The prior item reports that high recurrence with reversible work favours delegation or standard interfaces, while high required certainty and regulatory exposure favour synchronisation, and it grades both low confidence. [fact; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
That prior item reports required speed only as a hypothesis, and it reports no source that sets the time-pressure effect on duplication. [fact; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
The repository item on local optimisation reports that local tooling gains reduce whole-system throughput when the shared constraint's capacity does not grow with them, which is a reason a shared specialist pool can become the bottleneck and a reason duplicated local capacity can fail to help elsewhere. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]
The properties that most plausibly favour ring-fencing are high uncertainty and high required speed against a congested shared pool, with high cost of a wrong outcome pulling towards specialist control. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]
Specialist scarcity and regulatory exposure are named in the question as moderators, and no source retrieved here measures their effect on the ring-fencing choice. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Q2: definitions and measures.

Krüger and Berger define costs as money or developers' effort and cost factors as project properties that affect cost, and they elicited costs as percentage distributions across ten activities. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Neither retrieved source defines delivery certainty, positive capacity or an organisational re-convergence outcome. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
This item therefore uses positive capacity to mean specialist capacity in the team that is not diluted by shared-pool allocation, which is a working definition and not a sourced one. [assumption; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

Q3: organisational evidence on temporary separation and reintegration.

Jalbă and Nedelcu's theory-driven literature review states that failure of ambidexterity (balancing exploration of new capabilities with exploitation of existing ones) often arises from leadership misalignment, excessive structural rigidity or a lack of dynamic reintegration following exploration initiatives. [fact; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
The same review describes a sequence of separate units followed by strategic reintegration, with integration mechanisms such as interdependent subunits, defined interfaces and bridging roles, and attributes the sequence to O'Reilly and Tushman (2004) and later work. [fact; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
The review is qualitative and reports no cost or success rate for reintegration. [inference; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
Its subject is exploration units and not specialist-capacity duplication, so it supports the importance of planned reintegration but not a cost figure for it. [inference; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
Search note: "temporary ring-fenced specialist team re-convergence cost success rate" and an ambidexterity reintegration-rate query returned no quantitative rate; outcome not found. [assumption; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
The primary O'Reilly and Tushman papers were not read in text, because the 1996 scan at web.mit.edu returned image-only pages, so their claims are cited only as reported by the review. [assumption; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]

Q4: software clone-and-own evidence.

Krüger and Berger combined 26 interviews at one organisation (Axis) with a systematic literature review (SLR) of 57 publications, and they obtained eight quantitative datasets for clone and own and seven for platform-oriented reuse. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
They report eight cost estimations for integrating cloned variants into a platform, four for either strategy, and report that re-integrating a short-living clone takes considerably less time than a long-living clone. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Integration cost depends on co-evolution of the variant and platform and on the size of the variant's delta, and one interviewee said waiting one and a half years to merge means "everything [has] changed". [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
At Axis, short-living clones are re-integrated, often before major platform changes, while some long-living clones are re-integrated after years or possibly not at all, and clone and own was mostly used to enter new markets independently or test new features. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
The SLR gave median savings of 52 percent for platform-oriented reuse, with feature development for a platform 20 percent more expensive, variant development 67 percent cheaper against 35 percent cheaper for clone and own, and quality-assurance cost 60 percent lower. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Coordination was similarly expensive, with medians of 5 percent for clone and own and 7 percent for a platform. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
The authors state that the two strategies are not strictly distinct in practice and that the question may be which strategy fits which variant. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Ghabach et al. propose a method that estimates the cost of clone-and-own derivation operations and validate it preliminarily on a case study the authors built, so it offers a cost-estimation approach and no field measurement of convergence. [fact; source: https://hal.science/hal-01903006v1/document]

Q4 transfer to teams.

Co-evolution drift, where the duplicated capability changes while the shared original also changes, has a plausible organisational analogue in diverging procedures, tooling and specialist knowledge. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
Code merges are mechanical operations on explicit artefacts, while team convergence involves people, tacit knowledge, accountability and possibly regulator-facing records, so the software cost curve may understate or misshape the organisational one. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
The repository item on platform engineering finds that anti-fragmentation designs combine self-service platforms, shared contribution models and a standard core with local extensions, which is a rival to ring-fencing because it builds the convergence path in from the start. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html]

Q5: decision rule.

The evidence supports a conditional rule only for the convergence side, in which short divergence, small delta and an identified general solution lower convergence cost. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
No retrieved source measures delivery certainty or total life-cycle cost of ring-fencing against a shared pool, so the combination rule is unmeasured. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]

### §3 Reasoning

1. Convergence cost rises with divergence duration and delta in the only measured source. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
2. Organisational failure of separation-then-reintegration is attributed to missing reintegration, without rates. [fact; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
3. A time-bounded ring-fence with a named convergence plan is therefore the version of the option the evidence does not contradict. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
4. Whether it beats the shared pool on certainty and total cost is not derivable from the retrieved evidence. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

### §4 Consistency Check

```text
contradiction_scan: resolved
confidence_adjustment: convergence-cost claims kept at medium (single organisation); decision-rule claims kept at low
scope_guardrail: organisational evidence and software analogy kept separate
```

### §5 Depth and Breadth Expansion

Technical lens: the software numbers describe reuse of variants across customers, and the 52 percent median saving is a platform-versus-clone comparison, so it does not measure a temporary team duplication. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Regulatory lens: the prior item reports that governance-infrastructure standardisation rises with regulatory exposure, which suggests duplicated controls under high regulatory exposure add a duty to keep each copy compliant, but no retrieved source measures that duty. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

Economic lens: duplicated capacity is a certain upfront cost, while convergence cost is uncertain and grows with duration, so a fixed end date and an owner for convergence cap the exposed amount. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Behavioural lens: one Axis interviewee preferred staying current with the main line, which suggests that people in a ring-fenced team may also drift from shared practice without a forcing event. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

The retrieved evidence does not show that temporarily ring-fencing specialist capacity yields higher delivery certainty at lower total life-cycle cost than a shared specialist pool, because no source measures that comparison. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
The only measured convergence evidence comes from software clone and own at one organisation, where re-integration cost rose with how long the copy diverged and with the size of its delta. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Organisational literature attributes failed separate-then-reintegrate efforts to missing reintegration and reports no rates. [fact; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
A time-bounded ring-fence with a named convergence path is the variant the evidence does not contradict, which makes it a conditional design hypothesis and not a validated rule. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]

**Key findings:**

1. Re-integration cost grew with divergence duration and with the size of the variant's delta, and short-living clones took considerably less time to re-integrate than long-living ones, in eight cost estimations from one organisation. ([fact]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf)
2. At Axis, long-living clones used to enter new markets or test new features were sometimes re-integrated only after years or possibly not at all, and the paper reports no rate of failed convergence. ([fact]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf)
3. The software evidence quantifies platform-oriented reuse against clone and own, with a median saving of 52 percent in the systematic literature review, and therefore does not measure a temporary team duplication against a shared pool. ([fact]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf)
4. A 2025 systematic review of ambidexterity attributes failure of separate-then-reintegrate arrangements often to a lack of dynamic reintegration, and the review reports no cost or success rate for reintegration. ([inference]; medium confidence; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf)
5. No retrieved source measures delivery certainty or total life-cycle cost for ring-fencing against a shared specialist pool, so any property-combination rule for that comparison is unmeasured. ([inference]; low confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf)
6. The best-supported conditional rule is that ring-fencing fits high uncertainty and urgency against a congested pool only when the divergence period is short, the delta small and the convergence path and owner are named in advance. ([inference]; low confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
7. High required certainty and regulatory exposure favoured synchronisation and standardisation in earlier repository evidence, so ring-fencing there would add a duty to keep each copy compliant, which no retrieved source measures. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html)
8. Co-evolution drift between a copy and its original plausibly transfers from software to teams, while the mechanical cost of merging code does not transfer to people, tacit knowledge and accountability. ([inference]; low confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf)
9. A standard core with local extensions, self-service platforms and shared contribution models is a rival remedy that builds the convergence path in from the start. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)

**Evidence map:** see `## Findings` Evidence Map; rows 1 to 9 correspond to the Key Findings above.

**Assumptions:**

Positive capacity is defined here as specialist capacity in the team that shared-pool allocation does not dilute. [assumption; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
No retrieved source defines the term, so the working definition is the item's own. [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Software convergence mechanisms are treated as a partial analogue for team convergence. [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
The analogue is bounded by the differences in Key Finding 8. [assumption; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]

The review of ambidexterity is treated as an accurate report of the primary papers it cites. [assumption; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
The primary papers were not read in text here. [assumption; source: https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Organizational_Learning_and_Change/Tushman_&_OReilly_1996_Ambidextrous_Organizations.pdf]

**Analysis:**

Evidence was weighted by whether a source measured a cost or only described a mechanism, and only the software study measured one. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
The software result concerns copies of a system, so it supports the direction of the cost-duration relationship and not its size for teams. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Rival remedies are adding capacity to the shared pool, embedding specialists, and a standard core with local extensions, and the retrieved evidence neither ranks nor rejects them against ring-fencing. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]
Ring-fencing is preferred over a shared pool only if the pool's queue cost exceeds duplication plus expected convergence cost, and no source quantifies either side. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
Under high regulatory exposure the added duty to keep each copy compliant weighs against ring-fencing, while a congested pool weighs for it, and the sources do not settle the balance. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

**Risks, gaps, uncertainties:**

The convergence-cost evidence rests on eight cost estimations from one organisation. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Delivery-certainty outcomes, specialist scarcity effects and regulatory-exposure effects are unmeasured in the retrieved sources. [inference; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
Ghabach et al. validate their cost-estimation method only on an author-built case study. [fact; source: https://hal.science/hal-01903006v1/document]

**Open questions:**

How is the convergence date, owner and general solution chosen before the ring-fence starts? [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Does a ring-fenced regulated team accrue measurable extra audit or compliance cost per duplicated control? [assumption; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

### §7 Recursive Review

```text
review_result: pass
acronym_audit: passed
parity_check: passed
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

The retrieved evidence does not show that temporarily ring-fencing specialist capacity yields higher delivery certainty at lower total life-cycle cost than a shared specialist pool, because no source measures that comparison. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
The only measured convergence evidence comes from software clone and own at one organisation, where re-integration cost rose with how long the copy diverged and with the size of its delta. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Organisational literature attributes failed separate-then-reintegrate efforts to missing reintegration and reports no rates. [fact; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
A time-bounded ring-fence with a named convergence path is the variant the evidence does not contradict, which makes it a conditional design hypothesis and not a validated rule. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]

### Key Findings

1. Re-integration cost grew with divergence duration and with the size of the variant's delta, and short-living clones took considerably less time to re-integrate than long-living ones, in eight cost estimations from one organisation. ([fact]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf)
2. At Axis, long-living clones used to enter new markets or test new features were sometimes re-integrated only after years or possibly not at all, and the paper reports no rate of failed convergence. ([fact]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf)
3. The software evidence quantifies platform-oriented reuse against clone and own, with a median saving of 52 percent in the systematic literature review, and therefore does not measure a temporary team duplication against a shared pool. ([fact]; medium confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf)
4. A 2025 systematic review of ambidexterity attributes failure of separate-then-reintegrate arrangements often to a lack of dynamic reintegration, and the review reports no cost or success rate for reintegration. ([inference]; medium confidence; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf)
5. No retrieved source measures delivery certainty or total life-cycle cost for ring-fencing against a shared specialist pool, so any property-combination rule for that comparison is unmeasured. ([inference]; low confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf)
6. The best-supported conditional rule is that ring-fencing fits high uncertainty and urgency against a congested pool only when the divergence period is short, the delta small and the convergence path and owner are named in advance. ([inference]; low confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
7. High required certainty and regulatory exposure favoured synchronisation and standardisation in earlier repository evidence, so ring-fencing there would add a duty to keep each copy compliant, which no retrieved source measures. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html)
8. Co-evolution drift between a copy and its original plausibly transfers from software to teams, while the mechanical cost of merging code does not transfer to people, tacit knowledge and accountability. ([inference]; low confidence; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf)
9. A standard core with local extensions, self-service platforms and shared contribution models is a rival remedy that builds the convergence path in from the start. ([inference]; low confidence; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Re-integration cost rises with divergence duration and delta | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf | medium | KF1; eight estimations |
| [fact] Long-living clones re-integrated after years or not at all at Axis | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf | medium | KF2; no rate |
| [fact] Software savings compare platform and clone and own | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf | medium | KF3 |
| [inference] Failure often tied to missing reintegration; no rates | https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf | medium | KF4; single review |
| [inference] Certainty and life-cycle cost comparison unmeasured | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf | low | KF5 |
| [inference] Conditional rule: short, small delta, named convergence path | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html | low | KF6 |
| [inference] Regulatory exposure adds per-copy compliance duty | https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html | low | KF7; unmeasured |
| [inference] Drift transfers, merge mechanics do not | https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf | low | KF8 |
| [inference] Standard core is a rival remedy | https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html | low | KF9 |

### Assumptions

Positive capacity is defined here as specialist capacity in the team that shared-pool allocation does not dilute. [assumption; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
No retrieved source defines the term, so the working definition is the item's own. [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]

Software convergence mechanisms are treated as a partial analogue for team convergence. [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
The analogue is bounded by the differences in Key Finding 8. [assumption; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]

The review of ambidexterity is treated as an accurate report of the primary papers it cites. [assumption; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
The primary papers were not read in text here. [assumption; source: https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Organizational_Learning_and_Change/Tushman_&_OReilly_1996_Ambidextrous_Organizations.pdf]

### Analysis

Evidence was weighted by whether a source measured a cost or only described a mechanism, and only the software study measured one. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
The software result concerns copies of a system, so it supports the direction of the cost-duration relationship and not its size for teams. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
Rival remedies are adding capacity to the shared pool, embedding specialists, and a standard core with local extensions, and the retrieved evidence neither ranks nor rejects them against ring-fencing. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-platform-engineering-innersource-hybrid-standardization.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]
Ring-fencing is preferred over a shared pool only if the pool's queue cost exceeds duplication plus expected convergence cost, and no source quantifies either side. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]
Under high regulatory exposure the added duty to keep each copy compliant weighs against ring-fencing, while a congested pool weighs for it, and the sources do not settle the balance. [inference; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

### Risks, Gaps, and Uncertainties

- The convergence-cost evidence rests on eight cost estimations from one organisation. [fact; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- Delivery-certainty outcomes, specialist scarcity effects and regulatory-exposure effects are unmeasured in the retrieved sources. [inference; source: https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf]
- Ghabach et al. validate their cost-estimation method only on an author-built case study. [fact; source: https://hal.science/hal-01903006v1/document]

### Open Questions

- How is the convergence date, owner and general solution chosen before the ring-fence starts? [assumption; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- Does a ring-fenced regulated team accrue measurable extra audit or compliance cost per duplicated control? [assumption; source: https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html]

---

## Output

- Type: knowledge
- Description: A graded assessment of when temporary ring-fencing of specialist capacity might pay off, with measured convergence evidence from software clone and own separated from unmeasured organisational outcomes. [inference; source: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf]
- Links: https://www.cse.chalmers.se/~bergert/paper/2020-fse-reusecosts.pdf; https://conference.management.ase.ro/archives/2025/pdf_IMC2025/1_8.pdf; https://davidamitchell.github.io/Research/research/2026-10-23-dependency-properties-coordination-mechanisms.html
