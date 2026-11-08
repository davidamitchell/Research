---
review_count: 2
title: "How can medium-to-large knowledge-work organisations capture everyday friction and scale useful improvements without a dedicated innovation pipeline?"
added: 2026-11-07T23:40:00+00:00
status: reviewing
priority: high
blocks: [2026-11-07-cost-of-no-innovation-pipeline]
themes: [organisational-design, knowledge-management, enterprise-adoption, governance-policy]
started: 2026-11-08T01:40:44+00:00
completed: ~
output: []
cites: [2026-07-20-regulated-safe-to-fail-probing-operating-models, 2026-06-13-local-global-optima-knowledge-work-throughput, 2026-06-13-shadow-it-custom-tooling-governance-transition, 2026-08-17-decision-governance]
related: []
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How can medium-to-large knowledge-work organisations capture everyday friction and scale useful improvements without a dedicated innovation pipeline?

## Research Question

How can individuals and teams in medium-to-large knowledge-work organisations lodge real day-to-day friction in a shared problems register, keep it usable, and select, experiment with, scale, or retire high-leverage improvements without a dedicated innovation pipeline or formal innovation budget?

## Scope

**In scope:**
- Low-ceremony ways to capture friction arising from actual work.
- Register design and operating practices that manage attention, duplication, staleness, and overload.
- Selection, experimentation, promotion, and retirement criteria that can work without formal innovation authority or a dedicated budget.
- Practices that make lodging and follow-through useful enough for sustained adoption.
- Applicability to knowledge work and process improvement in medium-to-large organisations.

**Out of scope:**
- Dedicated innovation pipelines as the primary model; these are covered by a separate comparison item.
- Individual ideation techniques unrelated to surfacing friction in real work.
- Detailed implementation of experiment platforms or statistical design of online controlled experiments.

**Constraints:** Focus on evidence from theory, historical cases, and contemporary organisational practice. Distinguish evidence about formal authority or budgets from practices that function without them.

## Context

Local process improvements can remain isolated while parallel variants accumulate, but a formal backlog may add more overhead than value; this question informs how organisations can make emergent improvements visible and selectively reusable.

## Approach

1. Identify low-ceremony mechanisms for lodging friction from day-to-day work and the incentives or social conditions that encourage participation.
2. Examine register practices that preserve a signal-to-noise ratio, including triage cadence, ownership, deduplication, ageing, and retirement.
3. Compare selection and safe-to-fail experimentation practices that can operate under low formal authority or without a dedicated innovation budget.
4. Identify evidence-based criteria for promoting a local improvement, stopping an experiment, or scaling a practice across teams.
5. Assess adoption and persistence, including how feedback to contributors and visible outcomes affect continued use.

## Sources

- [Singer (2019) Bets, Not Backlogs, Shape Up](https://basecamp.com/shapeup/2.1-chapter-07)
- [Gibbs, Neckermann and Siemroth (2017) A Field Experiment in Motivating Employee Ideas](https://www.iza.org/publications/dp/8096)
- [Kubernetes Community Issue Triage Guidelines (repository text)](https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md)
- [Kubernetes Contributor Site Issue Triage Guidelines](https://www.kubernetes.dev/docs/guide/issue-triage/)
- [Edmondson (1999) Psychological Safety and Learning Behavior in Work Teams](https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full)
- [Cynefin.io Safe to fail probes](https://cynefin.io/wiki/Safe_to_fail_probes)
- [Snowden and Boone (2007) A Leader's Framework for Decision Making](https://hbr.org/2007/11/a-leaders-framework-for-decision-making)
- [Spear and Bowen (1999) Decoding the DNA of the Toyota Production System](https://hbr.org/1999/09/decoding-the-dna-of-the-toyota-production-system)
- [Lunney and Lueder, Postmortem Culture: Learning from Failure, Site Reliability Engineering](https://sre.google/sre-book/postmortem-culture/)
- [Safe-to-fail probing operating models in regulated industries (repository item)](https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html)
- [Local and global optima in knowledge-work throughput (repository item)](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
- [Shadow Information Technology (IT) and custom tooling governance transition (repository item)](https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html)
- [Decision governance for decentralized execution (repository item)](https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

Question: how individuals and teams in medium-to-large knowledge-work organisations can record day-to-day friction in a shared list of work obstacles (a friction register), keep that list usable, and select, trial, scale, or retire improvements without a dedicated innovation pipeline or budget.

Scope: low-ceremony capture, register upkeep, selection and safe-to-fail trials without formal authority, promotion and stop criteria, and adoption persistence. Dedicated innovation pipelines and experiment-platform statistics are excluded.

Constraints: evidence from theory, cases, and contemporary practice; evidence about formal authority or budgets is kept separate from practices that run without them. Output type: knowledge.

Working hypothesis: a small, time-bounded register with a named triage cadence and visible feedback sustains use better than an open-ended backlog. [assumption; source: https://basecamp.com/shapeup/2.1-chapter-07]

Prior work check: the repository holds completed items on safe-to-fail probing in regulated firms, local versus global optimisation, shadow Information Technology (IT) governance, and decision governance, each engaged in §2 and §5. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html; https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html]

### §1 Question Decomposition

- Q1 Capture: what lowers the cost and social risk of lodging friction?
  - Q1a Does psychological safety affect willingness to raise problems?
  - Q1b Do rewards or recognition change participation?
- Q2 Register upkeep: how do working registers control volume, duplicates, and staleness?
  - Q2a Does an unpruned central backlog degrade?
  - Q2b What triage, ageing, and closure rules exist in running systems?
- Q3 Selection and trials: how are improvements chosen and trialled without formal authority?
  - Q3a What is a safe-to-fail probe and when does it apply?
- Q4 Promotion and retirement: what criteria move a local improvement to wider use or stop it?
- Q5 Persistence: what keeps contributors lodging items?

### §2 Investigation

**Q1 Capture.**

Edmondson (1999) defines team psychological safety as a shared belief that the team is safe for interpersonal risk taking. [fact; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]

In a study of 51 work teams in one manufacturing company, team psychological safety was associated with learning behavior, and learning behavior mediated the link to team performance. [fact; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]

Lodging a friction item often names a colleague's process or a manager's decision as the problem, which is an interpersonal risk, so low psychological safety probably suppresses lodging. [inference; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]

A field experiment at a large technology company randomised 19 account teams to receive rewards for approved ideas or no change. [fact; source: https://www.iza.org/publications/dp/8096]

Rewards raised idea quality and participation, lowered ideas per participant, left total idea quantity unchanged, and the broader participation persisted after the reward ended, with no evidence of motivational crowding out. [fact; source: https://www.iza.org/publications/dp/8096]

Because the reward in that study was tied to idea approval by the company, the result does not show whether non-monetary recognition alone would produce the same participation effect. [inference; source: https://www.iza.org/publications/dp/8096]

**Q2 Register upkeep.**

Shape Up argues that backlogs pile up to hundreds of items nobody will have time for, and that time spent grooming old ideas prevents work on timely projects. [fact; source: https://basecamp.com/shapeup/2.1-chapter-07]

Its alternative is a betting table, a meeting before each six-week cycle that reviews only recent pitches or ones someone deliberately revived, with everything else let go and no central list. [fact; source: https://basecamp.com/shapeup/2.1-chapter-07]

It adds that people may keep decentralised lists, that important ideas return on their own, and that a problem heard once and never again may not have been a real problem. [fact; source: https://basecamp.com/shapeup/2.1-chapter-07]

The "recurrence as signal" rule gives a no-cost retirement and promotion test for a friction register, but it comes from one software company's practitioner account and no measurement of its error rate was found. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07]

Kubernetes issue triage, run by Special Interest Groups (SIGs) of maintainers, categorises new issues by priority, owner, and kind, and SIGs report benefits including preventing work from lingering endlessly and keeping contributors engaged by shortening response times. [fact; source: https://www.kubernetes.dev/docs/guide/issue-triage/]

Its written rules close issues with no reply after 20 days, ask an owner with no pull request after 30 days to produce one or release ownership, and have a bot label issues stale after 90 days of inactivity, with a freeze command to block that label. [fact; source: https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]

It also keeps a priority label for ideas that are possibly useful but lack support yet, used as a placeholder so they can be referenced or deduplicated when they recur, and it tells triagers to close duplicates after pointing the reporter to the original. [fact; source: https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]

The Kubernetes rules are time-based ageing, ownership release, and deduplication, which map onto the question's triage cadence, ownership, deduplication, and retirement needs. [inference; source: https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md; https://www.kubernetes.dev/docs/guide/issue-triage/]

The transfer to a company is uncertain because Kubernetes maintainers are largely engaged by project membership and use automation, while employees lodging workplace friction have competing assigned work. [assumption; source: https://www.kubernetes.dev/docs/guide/issue-triage/]

The Google Site Reliability Engineering (SRE) book states that incidents will recur unless a formal learning process exists and defines a postmortem as a written record of an incident, its impact, actions taken, root causes, and follow-up actions. [fact; source: https://sre.google/sre-book/postmortem-culture/]

Postmortem practice is a precedent for recording real operational friction after the event with named follow-up actions, although it addresses incidents, not chronic everyday friction. [inference; source: https://sre.google/sre-book/postmortem-culture/]

Failed search record: query "empirical study internal problem register or improvement backlog knowledge workers duplicate entries staleness overload triage effectiveness"; outcome: not found (no peer-reviewed study of duplicate, staleness, or overload rates in non-software friction registers).

**Q3 Selection and safe-to-fail trials.**

Cynefin.io describes safe-to-fail probes as small-scale experiments, run in parallel around coherent hypotheses, whose purpose is to let ideas that are not useful fail in small, contained, tolerable ways. [fact; source: https://cynefin.io/wiki/Safe_to_fail_probes]

Snowden and Boone's article presents the Cynefin framework and argues that different contexts call for different leadership approaches. [fact; source: https://hbr.org/2007/11/a-leaders-framework-for-decision-making]

A local team can run a probe without a budget when it fits inside its own working time and authority, which is a reading of the probe definition and not something either source tests. [inference; source: https://cynefin.io/wiki/Safe_to_fail_probes; https://hbr.org/2007/11/a-leaders-framework-for-decision-making]

The repository's regulated safe-to-fail item found that no source it located measures how the structure of an internal experiment-tracking mechanism affects experiment volume or adoption. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html]

That item also reports that the United States Food and Drug Administration (FDA) pre-certification pilot generated learning but concluded that scaling its model would exceed existing statutory authority, so the limit on scaling sat above the experiment. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html]

**Q4 Promotion and retirement.**

Cynefin.io states that probes producing observable beneficial patterns can be adopted and amplified once the system shows strong indications of stability. [fact; source: https://cynefin.io/wiki/Safe_to_fail_probes]

The repository's throughput item documents that local tooling optimisation degrades whole-system throughput when a shared constraint's capacity is not raised, citing telemetry in which individual task completion rose 33.7% while pull request review time rose 441%. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]

A promotion test for a locally successful improvement therefore needs a check on the shared queues it feeds, not only a local result. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]

The repository's shadow IT item finds that the best-supported governance is a staged sequence that identifies local instances, decides to decommission or continue, and then allocates governance by criticality, and that continuity risk arises when one person alone understands a local tool. [fact; source: https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html]

That staged sequence is a usable template for promotion and retirement decisions on improvements that began as friction responses. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html]

The repository's decision governance item reports that guardrail-bounded decentralisation, with explicit division of decision rights, is associated with better profit margin and revenue growth in three Massachusetts Institute of Technology Center for Information Systems Research surveys. [fact; source: https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html]

A register that has no named person with the right to promote or stop an experiment lacks the decision-rights split that item describes, so selection stalls even if capture works. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html]

Spear and Bowen's article summary notes that Toyota's kanban cards (visual work-signalling cards) and quality circles have been widely introduced elsewhere, including in initiatives at General Motors, Ford, and Chrysler. [fact; source: https://hbr.org/1999/09/decoding-the-dna-of-the-toyota-production-system]

**Q5 Persistence.**

Evidence on persistence comes from the field experiment, where broader participation outlasted the reward, and from the Kubernetes triage account, where shortening response times keeps contributors engaged. [fact; source: https://www.iza.org/publications/dp/8096; https://www.kubernetes.dev/docs/guide/issue-triage/]

Visible follow-through on lodged items is therefore a plausible persistence mechanism, but no source consulted isolates feedback to contributors as a variable. [inference; source: https://www.kubernetes.dev/docs/guide/issue-triage/; https://www.iza.org/publications/dp/8096]

Access note: Shape Up path /shapeup/2.2-chapter-07 returned 404; working chapter URL substituted in Sources.

### §3 Reasoning

Causal chain from evidence to conclusion:

1. Edmondson links psychological safety to team learning behavior, so lodging friction depends on a safe social climate. [inference; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]
2. The Gibbs field experiment shows participation can be broadened by rewards and can persist, so incentives are one lever but not the only one. [inference; source: https://www.iza.org/publications/dp/8096]
3. Shape Up and Kubernetes triage both limit what stays open, by time-boxing consideration or by ageing out inactive items, so registers need an explicit forgetting rule. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07; https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]
4. Cynefin probes need contained scope and a stability signal before amplification, and the throughput item shows local gains can overload shared queues, so scaling requires a downstream check. [inference; source: https://cynefin.io/wiki/Safe_to_fail_probes; https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html]
5. Decision rights decide whether selection happens at all, so a register needs a named promoter. [inference; source: https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html]

### §4 Consistency Check

```text
contradiction_scan: resolved
tension: Shape Up discards unpicked items while Kubernetes keeps a placeholder priority for unsupported ideas
resolution: both are retirement policies with different retention cost; item treats them as alternatives
confidence_adjustment: all transfer-to-company claims kept at medium or lower
scope_guardrail: maintained
```

### §5 Depth and Breadth Expansion

Behavioural lens: raising friction exposes the lodger to criticism, which makes psychological safety a precondition rather than an add-on. [inference; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]

Economic lens: the Gibbs reward cost money, so an organisation without an innovation budget cannot copy that design directly. [inference; source: https://www.iza.org/publications/dp/8096]

Operational lens: ageing and deduplication rules cost little once automated, as the Kubernetes bot shows. [inference; source: https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]

Governance lens: promotion into shared platforms raises the continuity and ownership questions found in shadow IT governance. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html]

Historical lens: structured improvement mechanisms such as quality circles spread widely beyond Toyota, but the cited summary does not report how long they persisted. [inference; source: https://hbr.org/1999/09/decoding-the-dna-of-the-toyota-production-system]

### §6 Synthesis

*(This section seeds the Findings below.)*

**Executive summary:**

A friction register can work without an innovation pipeline if it is a small, time-bounded list with explicit ageing and duplicate rules, a named person who can promote or stop an item, and a safe social climate for lodging, but no source consulted measures this combination in a knowledge-work organisation. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07; https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md; https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]
The only randomised field experiment located is one in which rewards for approved ideas broadened participation and the broader base persisted after the reward ended. [fact; source: https://www.iza.org/publications/dp/8096]
Register upkeep practices come from software teams, where Shape Up discards unselected items and Kubernetes ages out inactive issues. [fact; source: https://basecamp.com/shapeup/2.1-chapter-07; https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]
Scaling a local improvement needs a check on the shared queues it feeds and a decision-rights owner. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html]

**Key findings:**

1. Team psychological safety, defined as a shared belief that interpersonal risk taking is safe, was associated with learning behavior in 51 manufacturing teams, so a safe social climate may help friction lodging, although that study measured learning behavior and not the raising of problems. ([inference]; low confidence; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full)
2. A randomised field experiment with 19 teams found that rewards for approved ideas raised idea quality and participation, left total quantity unchanged, and left a broader participation base after the reward stopped. ([fact]; medium confidence; source: https://www.iza.org/publications/dp/8096)
3. Shape Up argues that unpruned backlogs accumulate items nobody will address and consume grooming time, and replaces them with a short betting table where unselected items are dropped and important ones return. ([fact]; low confidence; source: https://basecamp.com/shapeup/2.1-chapter-07)
4. Kubernetes triage rules close unanswered issues after 20 days, release ownership after 30 days without a pull request, and mark inactive issues stale after 90 days, giving a working template for ageing and retirement. ([fact]; medium confidence; source: https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md; https://www.kubernetes.dev/docs/guide/issue-triage/)
5. Safe-to-fail probes are small contained experiments whose useful patterns are amplified only when the system shows strong stability, which fits low-authority local trials of improvements. ([inference]; medium confidence; source: https://cynefin.io/wiki/Safe_to_fail_probes)
6. Promoting a local improvement requires a check on shared downstream queues, because local tooling gains degraded whole-system throughput in documented telemetry where review capacity was not raised. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
7. A staged identify, evaluate, and allocate sequence from shadow IT governance supplies a template for deciding whether a promoted improvement continues, is decommissioned, or moves to owned governance. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html)
8. Explicit division of decision rights with guardrails is associated with better financial outcomes in three surveys, so a register without a named promoter lacks a decision structure that selection needs. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html)
9. A regulated safe-to-fail pilot generated learning but could not scale because its model would exceed existing statutory authority, which shows that a limit above the experiment can block scaling. ([fact]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Psychological safety may help friction lodging | https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full | low | one manufacturing study |
| [fact] Rewards broadened persistent participation | https://www.iza.org/publications/dp/8096 | medium | one firm, 19 teams |
| [fact] Shape Up drops unselected items | https://basecamp.com/shapeup/2.1-chapter-07 | low | practitioner account |
| [fact] Kubernetes ageing and ownership rules | https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md; https://www.kubernetes.dev/docs/guide/issue-triage/ | medium | same organisation |
| [inference] Safe-to-fail probes suit low-authority trials | https://cynefin.io/wiki/Safe_to_fail_probes | medium | reading of definition |
| [inference] Promotion needs downstream check | https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html | medium | repository item |
| [inference] Staged shadow IT sequence as template | https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html | medium | repository item |
| [inference] Named promoter needed | https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html | medium | repository item |
| [fact] Regulated pilot blocked from scaling by authority above it | https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html | medium | repository item |

**Assumptions:**

Open-source triage rules transfer to employees with competing assigned work. [assumption; source: https://www.kubernetes.dev/docs/guide/issue-triage/]
The transfer is reasonable because both settings need to manage a shared inflow of problem reports with limited reviewer time. [assumption; source: https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]

**Analysis:**

The evidence is asymmetric: rigorous measurement exists for incentives, while register upkeep rests on practitioner documents. [inference; source: https://www.iza.org/publications/dp/8096; https://basecamp.com/shapeup/2.1-chapter-07]
Shape Up and Kubernetes disagree on whether to keep unselected ideas, and the choice depends on how cheap retention is. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07; https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]
Sustained participation could instead reflect manager sponsorship rather than register design, since the Edmondson abstract reports that team leader coaching and context support shape team outcomes alongside shared beliefs. [inference; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]
The consulted sources do not separate sponsorship from register design, so the conclusion is kept to the elements each source directly supports. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07; https://www.iza.org/publications/dp/8096]

**Risks, gaps, uncertainties:**

The field experiment, Shape Up, and Kubernetes triage sources used here do not measure duplicate rates, overload, or abandonment in a friction register inside a knowledge-work organisation. [inference; source: https://www.iza.org/publications/dp/8096; https://basecamp.com/shapeup/2.1-chapter-07; https://www.kubernetes.dev/docs/guide/issue-triage/]
- The regulated safe-to-fail item located no source measuring how an internal experiment-tracking mechanism affects experiment volume or adoption. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html]
The reward experiment covers one technology firm, so its results may not transfer to unrewarded registers. [inference; source: https://www.iza.org/publications/dp/8096]

**Open questions:**

- Does non-monetary recognition match monetary rewards for participation persistence?
- What stale-item threshold suits a company register?

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

A friction register can work without an innovation pipeline if it is a small, time-bounded list with explicit ageing and duplicate rules, a named person who can promote or stop an item, and a safe social climate for lodging, but no source consulted measures this combination in a knowledge-work organisation. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07; https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md; https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]
The only randomised field experiment located is one in which rewards for approved ideas broadened participation and the broader base persisted after the reward ended. [fact; source: https://www.iza.org/publications/dp/8096]
Register upkeep practices come from software teams, where Shape Up discards unselected items and Kubernetes ages out inactive issues. [fact; source: https://basecamp.com/shapeup/2.1-chapter-07; https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]
Scaling a local improvement needs a check on the shared queues it feeds and a decision-rights owner. [inference; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html; https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html]

### Key Findings

1. Team psychological safety, defined as a shared belief that interpersonal risk taking is safe, was associated with learning behavior in 51 manufacturing teams, so a safe social climate may help friction lodging, although that study measured learning behavior and not the raising of problems. ([inference]; low confidence; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full)
2. A randomised field experiment with 19 teams found that rewards for approved ideas raised idea quality and participation, left total quantity unchanged, and left a broader participation base after the reward stopped. ([fact]; medium confidence; source: https://www.iza.org/publications/dp/8096)
3. Shape Up argues that unpruned backlogs accumulate items nobody will address and consume grooming time, and replaces them with a short betting table where unselected items are dropped and important ones return. ([fact]; low confidence; source: https://basecamp.com/shapeup/2.1-chapter-07)
4. Kubernetes triage rules close unanswered issues after 20 days, release ownership after 30 days without a pull request, and mark inactive issues stale after 90 days, giving a working template for ageing and retirement. ([fact]; medium confidence; source: https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md; https://www.kubernetes.dev/docs/guide/issue-triage/)
5. Safe-to-fail probes are small contained experiments whose useful patterns are amplified only when the system shows strong stability, which fits low-authority local trials of improvements. ([inference]; medium confidence; source: https://cynefin.io/wiki/Safe_to_fail_probes)
6. Promoting a local improvement requires a check on shared downstream queues, because local tooling gains degraded whole-system throughput in documented telemetry where review capacity was not raised. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
7. A staged identify, evaluate, and allocate sequence from shadow IT governance supplies a template for deciding whether a promoted improvement continues, is decommissioned, or moves to owned governance. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html)
8. Explicit division of decision rights with guardrails is associated with better financial outcomes in three surveys, so a register without a named promoter lacks a decision structure that selection needs. ([inference]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html)
9. A regulated safe-to-fail pilot generated learning but could not scale because its model would exceed existing statutory authority, which shows that a limit above the experiment can block scaling. ([fact]; medium confidence; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Psychological safety may help friction lodging | https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full | low | one manufacturing study |
| [fact] Rewards broadened persistent participation | https://www.iza.org/publications/dp/8096 | medium | one firm, 19 teams |
| [fact] Shape Up drops unselected items | https://basecamp.com/shapeup/2.1-chapter-07 | low | practitioner account |
| [fact] Kubernetes ageing and ownership rules | https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md; https://www.kubernetes.dev/docs/guide/issue-triage/ | medium | same organisation |
| [inference] Safe-to-fail probes suit low-authority trials | https://cynefin.io/wiki/Safe_to_fail_probes | medium | reading of definition |
| [inference] Promotion needs downstream check | https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html | medium | repository item |
| [inference] Staged shadow IT sequence as template | https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html | medium | repository item |
| [inference] Named promoter needed | https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html | medium | repository item |
| [fact] Regulated pilot blocked from scaling by authority above it | https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html | medium | repository item |

### Assumptions

Open-source triage rules transfer to employees with competing assigned work. [assumption; source: https://www.kubernetes.dev/docs/guide/issue-triage/]
The transfer is reasonable because both settings need to manage a shared inflow of problem reports with limited reviewer time. [assumption; source: https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]

### Analysis

The evidence is asymmetric: rigorous measurement exists for incentives, while register upkeep rests on practitioner documents. [inference; source: https://www.iza.org/publications/dp/8096; https://basecamp.com/shapeup/2.1-chapter-07]
Shape Up and Kubernetes disagree on whether to keep unselected ideas, and the choice depends on how cheap retention is. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07; https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md]
Sustained participation could instead reflect manager sponsorship rather than register design, since the Edmondson abstract reports that team leader coaching and context support shape team outcomes alongside shared beliefs. [inference; source: https://dash.harvard.edu/entities/publication/13a7b031-0fdd-45ec-a7e0-2b80e2bc679f/full]
The consulted sources do not separate sponsorship from register design, so the conclusion is kept to the elements each source directly supports. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07; https://www.iza.org/publications/dp/8096]

### Risks, Gaps, and Uncertainties

- The field experiment, Shape Up, and Kubernetes triage sources used here do not measure duplicate rates, overload, or abandonment in a friction register inside a knowledge-work organisation. [inference; source: https://www.iza.org/publications/dp/8096; https://basecamp.com/shapeup/2.1-chapter-07; https://www.kubernetes.dev/docs/guide/issue-triage/]
- The regulated safe-to-fail item located no source measuring how an internal experiment-tracking mechanism affects experiment volume or adoption. [fact; source: https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html]
- The reward experiment covers one technology firm, so its results may not transfer to unrewarded registers. [inference; source: https://www.iza.org/publications/dp/8096]

### Open Questions

- Does non-monetary recognition match monetary rewards for participation persistence?
- What stale-item threshold suits a company register?

---

## Output

- Type: knowledge
- Description: Evidence review of how friction registers can be lodged, kept usable, and scaled without a dedicated innovation pipeline. [inference; source: https://basecamp.com/shapeup/2.1-chapter-07]
- Links: https://www.iza.org/publications/dp/8096; https://basecamp.com/shapeup/2.1-chapter-07; https://github.com/kubernetes/community/blob/master/contributors/guide/issue-triage.md

## Related

- [Governance and operating models for safe-to-fail experimentation in regulated industries](https://davidamitchell.github.io/Research/research/2026-07-20-regulated-safe-to-fail-probing-operating-models.html)
- [How does local optimisation of team- and role-level tooling in knowledge work reduce organisation-level throughput, and which interdependencies determine when local gains become global losses?](https://davidamitchell.github.io/Research/research/2026-06-13-local-global-optima-knowledge-work-throughput.html)
- [What benefits, risks, and lifecycle costs of shadow Information Technology (IT) and custom local tooling are documented, and which governance approaches successfully transition covert local solutions into sanctioned business-managed platforms without destroying useful innovation?](https://davidamitchell.github.io/Research/research/2026-06-13-shadow-it-custom-tooling-governance-transition.html)
- [Decision governance for decentralized execution](https://davidamitchell.github.io/Research/research/2026-08-17-decision-governance.html)
