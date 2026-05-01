---
review_count: 1
title: "What strategies are effective for open-source software maintainers dealing with Artificial Intelligence (AI)-generated low-quality contributions at scale?"
added: 2026-05-01T08:17:39+00:00
status: reviewing
priority: high
blocks: []
tags: [open-source, agentic-ai, governance, workflow]
started: 2026-05-01T22:21:59+00:00
completed: ~
output: [knowledge]
cites: [2026-04-26-human-in-the-loop-ai-automated-workflows, 2026-05-01-compound-error-accumulation-ai-codebases, 2026-05-01-human-oversight-ai-software-development]
related: [2026-04-30-ai-code-entropy-quality-metrics, 2026-05-01-appropriate-task-selection-coding-agents, 2026-05-01-coding-agent-context-management-transparency]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# What strategies are effective for open-source software maintainers dealing with Artificial Intelligence (AI)-generated low-quality contributions at scale?

## Research Question

What strategies are effective for open-source software (OSS) maintainers in filtering, managing, and sustaining project health against a rising volume of low-quality Artificial Intelligence (AI) agent-generated contributions, including pull requests, issues, and comments?

## Scope

**In scope:**
- Scale and evidence of AI-generated low-quality contributions to OSS projects: what data exists on volume and quality
- Detection heuristics: how maintainers identify AI-generated contributions, including linguistic patterns, lack of follow-through, and pull request structure
- Mitigation strategies deployed in practice: contribution filters, human-voice requirements, automated triage, contribution gates, including the "vouch" pattern
- Community norms and governance responses: how OSS communities are updating their contributing guidelines
- Tooling approaches: bot detection, label systems, issue embeddings for cluster analysis
- Sustainability impact: maintainer burnout, project closure, and the long-term effect on OSS health

**Out of scope:**
- Legal and intellectual property questions about AI-generated code
- AI-assisted contributions that are high quality
- Detailed treatment of specific commercial products producing the contributions

**Constraints:**
- Distinguish anecdote and practitioner observation from empirical research
- Prefer sources with data, including contribution counts or filter effectiveness metrics, over opinion pieces

## Context

- [fact; source: https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json] Mario Zechner's April 2026 talk describes a flood of low-context "clanker" issues and pull requests against Pi, OpenClaw-linked repositories, and tldraw, and it documents concrete countermeasures such as auto-closing unsolicited pull requests, requiring a short human-written issue, labeling likely agent traffic, de-prioritizing known agent-origin accounts, clustering issues by embeddings, and temporarily closing trackers.
- [fact; source: https://github.com/mitchellh/vouch; https://github.com/mitchellh/vouch/blob/main/FAQ.md] Mitchell Hashimoto's Vouch project turns one of those countermeasures into an explicit trust-management pattern: contributors can be required to earn a vouch before interacting with selected project surfaces, while first-time contributors can still enter by introducing themselves and describing intended work.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-compound-error-accumulation-ai-codebases.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-human-oversight-ai-software-development.md] Prior completed repository work already establishes the adjacent control logic used here: selective human oversight matters, error costs rise when output outruns verification, and reviewer attention is a governance surface rather than a mere etiquette issue.

## Approach

1. **Quantify the problem**: What data exists on the volume of AI-generated pull requests and issues across major OSS projects? Survey GitHub data, published studies, and maintainer reports.
2. **Detection methods**: What signals reliably distinguish AI-generated from human contributions? Review published classifiers, heuristics, and maintainer accounts.
3. **Mitigation strategies in practice**: Document the strategies deployed, including contribution filters, vouch systems, issue de-prioritisation, tracker shutdown, and embedding-based triage. Assess effectiveness where data exists.
4. **Community governance responses**: How are `CONTRIBUTING.md` files, community codes of conduct, and GitHub repository settings evolving to address this? Survey GitHub's own tooling responses.
5. **Sustainability impact**: Is there evidence that AI-generated contributions are increasing maintainer burnout or project closures? Survey burnout literature and recent OSS health reports.

## Sources

- [x] [The Focus AI (2026) Building pi in a World of Slop transcript](https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json)
- [x] [Zechner (2025) What I learned building an opinionated and minimal coding agent](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/)
- [x] [Hashimoto (2026) Vouch repository](https://github.com/mitchellh/vouch)
- [x] [Hashimoto (2026) Vouch FAQ](https://github.com/mitchellh/vouch/blob/main/FAQ.md)
- [x] [GitHub (2024) Open Source Survey](https://opensourcesurvey.org/2024/)
- [x] [Bacchelli and Bird (2013) Expectations, Outcomes, and Challenges of Modern Code Review](https://research.tudelft.nl/en/publications/expectations-outcomes-and-challenges-of-modern-code-review/)
- [x] [Pinna et al. (2026) Comparing AI Coding Agents: A Task-Stratified Analysis of Pull Request Acceptance](https://arxiv.org/html/2602.08915v1)
- [x] [Yang et al. (2026) Beyond Banning AI: A First Look at GenAI Governance in Open Source Software Communities](https://arxiv.org/html/2603.26487v1)
- [x] [Baltes et al. (2026) "An Endless Stream of AI Slop": The Growing Burden of AI-Assisted Software Development](https://arxiv.org/abs/2603.27249)
- [x] [Liu et al. (2026) Debt Behind the AI Boom: A Large-Scale Empirical Study of AI-Generated Code in the Wild](https://arxiv.org/abs/2603.28592)
- [x] [Ghostty (2026) AI Usage Policy](https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md)
- [x] [Electronic Frontier Foundation (EFF) (2026) Policy on Large Language Model (LLM)-Assisted Contributions](https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects)
- [x] [Python Software Foundation (2026) Generative AI policy for CPython](https://devguide.python.org/getting-started/generative-ai/)
- [x] [Matplotlib (2026) Use of Generative AI](https://matplotlib.org/devdocs/devel/contribute.html#generative-ai)
- [x] [Apache Airflow (2026) Gen-AI Assisted contributions](https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions)
- [x] [Apache DataFusion (2026) AI-Assisted contributions](https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions)
- [x] [tldraw (2026) Contributions policy issue #7695](https://github.com/tldraw/tldraw/issues/7695)
- [x] [Stenberg (2026) Daniel's week, January 16, 2026](https://lists.haxx.se/pipermail/daniel/2026-January/000143.html)
- [x] [cURL (2026) On AI use in curl](https://curl.se/dev/contribute.html#on-ai-use-in-curl)
- [x] [GitHub Docs (2026) About issue and pull request templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)
- [x] [GitHub Docs (2026) Limiting interactions in your repository](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository)
- [x] [GitHub Docs (2026) Best practices for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
- [x] [Linux Foundation Research (2023) Open Source Maintainers](https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en)
- [x] [Tidelift (2024) The 2024 Tidelift Maintainer Impact Report](https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf)
- [ ] [Kalliamvakou et al. (2014) The Promises and Perils of Mining GitHub](https://dl.acm.org/doi/10.1145/2597073.2597074)
- [ ] [Eghbal (2020) Working in Public: The Making and Maintenance of Open Source Software](https://press.stripe.com/working-in-public)

## Related

- [When and how should human intervention be incorporated into Artificial Intelligence (AI)-driven and automated workflows?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md)
- [How do errors compound in Artificial Intelligence (AI)-agent-heavy codebases, and what review strategies can manage this risk?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-compound-error-accumulation-ai-codebases.md)
- [What is the evidence for human oversight as an effective quality gate in Artificial Intelligence (AI)-assisted software development?](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-human-oversight-ai-software-development.md)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. Sections 0 to 5 are the investigation, and section 6 seeds the Findings below.)*

### §0 Initialise

- [assumption] Research question restated: which strategies most effectively protect OSS maintainer capacity and project health when AI tools make it cheap to generate low-context pull requests, issues, and comments? Justification: this is the operational restatement of the item's own question rather than an externally evidenced domain claim.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-04-26-human-in-the-loop-ai-automated-workflows.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-compound-error-accumulation-ai-codebases.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-human-oversight-ai-software-development.md] Prior completed repository work already contributes three relevant controls to this item: proportional human oversight, throughput versus verification mismatch, and the need to preserve independent review capacity when AI output scales.
- [assumption] Constraint mode: full. Justification: the workflow requires full decomposition, full synthesis, and mirrored Findings.
- [assumption] Output target: knowledge item with structured Findings, Evidence Map, assumptions, analysis, risks, and open questions. Justification: this line records workflow metadata rather than an external domain claim.
- [assumption] Working definition: "effective" means preserving maintainer review capacity and project health while still allowing legitimate contributions where possible, not maximizing raw contributor throughput. Justification: the retrieved evidence is strongest on review load, governance response, and sustainability rather than on contribution-count growth.
- [assumption] Working definition: "low-quality AI-generated contribution" includes contributions that are superficially plausible but show weak codebase understanding, weak follow-through, or weak verification. Justification: the retrieved project policies and discussion sources converge on that operational pattern even when they use different terms.

### §1 Question Decomposition

- **Root question:** which strategies effectively protect OSS projects from low-quality AI-generated contribution volume without destroying legitimate collaboration?
- **A. Problem scale and shape**
  - A1. What evidence shows that AI-generated contribution volume is materially changing OSS intake pressure?
  - A2. What evidence shows that contribution quality varies by task type or project surface?
- **B. Detection and triage**
  - B1. What signals do maintainers actually use to identify likely AI-generated low-context submissions?
  - B2. Which parts of that detection problem can platforms structure, and which parts still require judgment?
- **C. Mitigation strategies**
  - C1. What accountability rules are projects adopting short of a full ban?
  - C2. What hard-throttle or gatekeeping strategies are projects adopting under overload?
  - C3. What reusable platform primitives support these controls?
- **D. Sustainability**
  - D1. What evidence shows that maintainer capacity is already fragile before AI-generated intake is added?
  - D2. What does that imply for acceptable trade-offs between openness and protection?
- **E. Synthesis**
  - E1. Which strategy mix is best supported for most public GitHub projects?
  - E2. Which strategies look justified only in higher-overload cases?

### §2 Investigation

#### Source-access and search notes

- [assumption] Access note: the seeded GitHub repository URL for Mario Zechner's talk resolved only to the repository homepage, so the raw transcript JSON and the follow-up Pi essay were used as the accessible primary sources for the motivating practitioner account. Justification: those sources expose the actual talk text and the author's directly related control philosophy.
- [assumption] Failed primary-source search note: the seeded Association for Computing Machinery (ACM) DOI for Kalliamvakou et al. returned a 403 page in this runtime, so it was retained only as an identified methodological reference and not used for downstream factual claims. Justification: the item's core claims are supported by newer, directly on-topic OSS and AI-governance sources.
- [assumption] Access note: the seeded Stripe Press URL for *Working in Public* resolved to unrelated podcast content in this session, so maintainer-sustainability grounding was taken from the accessible Linux Foundation and Tidelift survey reports instead. Justification: those reports provide newer and more directly quotable maintainer-capacity evidence.

#### A. AI lowers contribution cost faster than it lowers review cost

- [fact; source: https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json] Mario Zechner's transcript states that OpenClaw-linked agents were posting garbage issues and pull requests across his projects and other repositories, and it records direct countermeasures such as auto-closing pull requests, requiring a short human-written issue, labeling likely agent traffic, and temporarily closing trackers.
- [fact; source: https://arxiv.org/html/2603.26487v1] Yang et al. analyze 67 highly visible OSS policy sources and conclude that cheaper generation does not mean cheaper review, which has pushed projects to experiment with rules across contribution guides, security policies, templates, and repository-level instructions.
- [fact; source: https://arxiv.org/abs/2603.27249] Baltes et al. analyze 1,154 posts across 15 developer discussion threads and group the recurring concerns into review friction, quality degradation, and systemic incentives, framing AI slop as a tragedy of the commons that externalizes review costs onto maintainers and reviewers.
- [fact; source: https://opensourcesurvey.org/2024/] GitHub's 2024 Open Source Survey reports that 72% to 73% of open-source respondents use AI tools for coding or documentation, which supports the baseline claim that AI-assisted contribution generation is already widespread even before a project measures low-quality submission volume directly.
- [inference; source: https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json; https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://opensourcesurvey.org/2024/] The core structural problem is therefore asymmetry, not merely annoyance: AI compresses contribution-generation effort broadly enough that maintainers experience intake pressure before they gain equivalent new review capacity.

#### B. Quality and acceptance vary sharply by task shape, and long-term debt remains material

- [fact; source: https://arxiv.org/html/2602.08915v1] Pinna et al. analyze 7,156 AI-generated pull requests and report that documentation tasks reach 82.1% acceptance while new-feature tasks reach 66.1%, with no single agent dominating every category.
- [fact; source: https://arxiv.org/abs/2603.28592] Liu et al. build a dataset of 302.6 thousand verified AI-authored commits across 6,299 GitHub repositories and identify 484,366 distinct issues, with code smells accounting for 89.3% of them.
- [fact; source: https://arxiv.org/abs/2603.28592] The same study reports that more than 15% of commits from every studied AI coding assistant introduce at least one issue, and 22.7% of tracked AI-introduced issues still survive at the latest repository version.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-compound-error-accumulation-ai-codebases.md] Maintainers should therefore expect superficially acceptable localized changes to coexist with persistent repository-level debt, which makes uniform intake rules weaker than task-shaped review thresholds.

#### C. Projects are converging on accountability-first policies before full bans

- [fact; source: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md] Ghostty requires all AI usage to be disclosed, requires contributors to fully understand submitted code, forbids external bots or low-effort AI interaction patterns, and states that repeated bad AI contributions can lead to public denouncement and future blocking.
- [fact; source: https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects] The Electronic Frontier Foundation states that contributors must understand submitted code and that comments and documentation must be human-authored, because Large Language Model output can look plausible while still exhausting small review teams.
- [fact; source: https://devguide.python.org/getting-started/generative-ai/; https://matplotlib.org/devdocs/devel/contribute.html#generative-ai] CPython and Matplotlib both state that maintainers may close low-value or fully AI-generated issues and pull requests, and Matplotlib explicitly rejects external bots directly interacting with project channels.
- [fact; source: https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions] Apache Airflow and Apache DataFusion allow AI-assisted work only when contributors understand it, can justify it, disclose tool use where required, run checks, and avoid offloading unrelated or unexplained changes onto maintainers.
- [fact; source: https://curl.se/dev/contribute.html#on-ai-use-in-curl] cURL's contribution guidance requires disclosure for AI-assisted security findings, demands that reporters verify issues themselves, warns that copy-pasted AI reports waste scarce security-team time, and states that fake reports lead to immediate bans.
- [inference; source: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://devguide.python.org/getting-started/generative-ai/; https://matplotlib.org/devdocs/devel/contribute.html#generative-ai; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions; https://curl.se/dev/contribute.html#on-ai-use-in-curl] The most common practical response is not "ban AI," but "ban unaccountable AI use": require disclosure, force human understanding, keep changes small, and preserve maintainer discretion to close or block repeat offenders.

#### D. Explicit trust gates and hard throttles appear when accountability rules are not enough

- [fact; source: https://github.com/mitchellh/vouch; https://github.com/mitchellh/vouch/blob/main/FAQ.md] Vouch implements an explicit trust model in which contributors can be required to earn a vouch before interacting with selected project surfaces, while preserving normal code review and merge controls behind that intake filter.
- [fact; source: https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json; https://github.com/mitchellh/vouch] Zechner's "write a short issue in your human voice, then get a maintainer's looks-good-to-me before future pull requests are allowed" pattern is the direct operational antecedent that Vouch generalizes into reusable tooling.
- [fact; source: https://github.com/tldraw/tldraw/issues/7695] tldraw announced that it would automatically close pull requests from external contributors because many recent AI-generated submissions showed incomplete context, misunderstanding of the codebase, and little follow-up engagement.
- [fact; source: https://lists.haxx.se/pipermail/daniel/2026-January/000143.html] Daniel Stenberg wrote that cURL received twenty Hackerone submissions already in early 2026, that the current torrent placed a high load on the security team, and that the bug bounty was being shut down to remove incentives for badly researched reports, whether AI generated or not.
- [inference; source: https://github.com/mitchellh/vouch; https://github.com/mitchellh/vouch/blob/main/FAQ.md; https://github.com/tldraw/tldraw/issues/7695; https://lists.haxx.se/pipermail/daniel/2026-January/000143.html] Explicit social-trust gates preserve some openness when a project still wants new contributors, while hard throttles such as auto-closing external pull requests or shutting down a bounty become rational when reviewer load has already crossed a sustainability threshold.

#### E. GitHub supplies useful gating primitives, but not the maintainers' judgment

- [fact; source: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates] GitHub issue forms and pull request templates let maintainers require structured information and surface contribution expectations on the default branch before review begins.
- [fact; source: https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository] GitHub interaction limits can temporarily restrict who may open issues, pull requests, comments, or reactions, with options keyed to existing users, prior contributors, or collaborators.
- [fact; source: https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories] GitHub recommends protected branches with required status checks and pull request reviews to maintain branch quality when outside contributions are accepted.
- [inference; source: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories] Platform primitives can raise the floor on structure and access control, but they do not determine admissibility by themselves, so projects still need local policies about disclosure, accountability, and trust.

#### F. Maintainer capacity is already fragile, which changes the openness trade-off

- [fact; source: https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en] The Linux Foundation's 2023 maintainer report says only 35% of interviewees describe their projects as having a strong new-contributor pipeline, 39% feel their open-source work is highly valued by their organization, and 38% feel a high degree of employer support.
- [fact; source: https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en] The same report highlights that maintainers view timely pull request handling, contributor guidance, and explicit onboarding as central to a healthy contributor experience.
- [fact; source: https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf] Tidelift's 2024 maintainer report says 60% of maintainers are unpaid hobbyists, only 12% earn most or all of their income from maintenance work, and paid maintainers are on average 55% more likely to implement critical security and maintenance practices than unpaid maintainers.
- [fact; source: https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf] The same report says 60% of maintainers have quit or considered quitting project maintenance, including 22% who already have quit and 38% who have considered quitting.
- [inference; source: https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf; https://arxiv.org/abs/2603.27249] AI-generated low-quality contribution volume lands on a labor pool that is already fragile, under-supported, and bottlenecked, which makes intake friction an ecosystem-protection measure rather than merely a social preference.

### §3 Reasoning

- [inference; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json] The strongest synthesis is that maintainers should optimize for review-capacity preservation first, because the main harm mechanism is asymmetry between generation cost and verification cost.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592] Because AI-generated contribution outcomes differ by task type and long-term debt persists even when code gets merged, the defensible control variable is not "AI versus non-AI" but task scope, contributor accountability, and the amount of project surface affected.
- [inference; source: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions] Disclosure and understanding requirements work as filters because they make it costly to remain a pure pass-through for an agent, while still allowing skilled contributors to use AI tools responsibly.
- [inference; source: https://github.com/mitchellh/vouch; https://github.com/tldraw/tldraw/issues/7695; https://lists.haxx.se/pipermail/daniel/2026-January/000143.html] Trust gates and hard throttles occupy different points on the same response ladder: projects that still want broader intake can add identity and relationship friction, while projects already saturated move to explicit closure or shutdown of high-cost channels.
- [assumption] No retrieved source quantifies the false-positive and false-negative rates of human-voice rules, vouch gates, or tracker shutdowns across many repositories. Justification: the governance evidence is policy-rich but metric-poor on comparative effectiveness.

### §4 Consistency Check

- [fact; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592] The pull-request acceptance study measures AI-generated pull requests broadly, not only low-quality ones, while the debt study measures repository-level issue introduction and persistence rather than maintainer burnout directly.
- [fact; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249] The governance and discussion studies are strong on recurring concerns and policy patterns, but they do not provide experimental estimates of which policy mix is best in every repository context.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592; https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249] Confidence should therefore remain medium overall: the direction of the problem and the response ladder are well supported, but precise effectiveness rankings for individual controls remain under-measured.
- [inference; source: https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf] The sustainability claims are bounded correctly when framed as aggravation of pre-existing maintainer fragility rather than as proof that AI-generated contributions alone cause maintainer exits.

### §5 Depth and Breadth Expansion

- [inference; source: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://github.com/mitchellh/vouch] **Technical lens:** the most robust controls act at the intake boundary, before deep review begins, because once a maintainer opens a pull request seriously the main cost has already been incurred.
- [inference; source: https://arxiv.org/abs/2603.27249; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf] **Economic lens:** AI-generated slop is a cost-externalization problem, where contributors or tool users capture speed while maintainers pay the verification bill.
- [inference; source: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions] **Behavioural lens:** "human voice," disclosure, and explain-your-work rules are not cosmetic, because they test whether a contributor will stay engaged after the first automated submission.
- [inference; source: https://github.com/mitchellh/vouch; https://github.com/mitchellh/vouch/blob/main/FAQ.md] **Historical lens:** the vouch pattern formalizes an older OSS norm, namely graduated trust based on repeated socially legible participation rather than unrestricted anonymous access to every high-cost channel from day one.
- [inference; source: https://arxiv.org/html/2603.26487v1; https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository] **Platform lens:** GitHub can supply templates and coarse-grained interaction controls, but the decisive governance work still lives in project policy because admissibility, trust, and sanctions are community choices rather than generic platform defaults.

### §6 Synthesis

**Executive summary:**

- [inference; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://github.com/mitchellh/vouch; https://github.com/tldraw/tldraw/issues/7695] The most effective strategies are layered intake controls that make human accountability hard to fake and maintainer review time easy to protect, rather than a single universal ban on AI use.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592] Empirical evidence shows that AI-generated contributions vary sharply by task type and can leave persistent maintenance debt, so maintainers should gate by scope and verification burden, not by AI provenance alone.
- [fact; source: https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf] OSS maintainer capacity is already fragile, with weak contributor pipelines, weak institutional support, and high quit-or-considered-quitting rates before AI-generated intake is added.
- [inference; source: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions; https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository] Across the cited public GitHub project examples, the best-supported default is a ladder of structured templates, disclosure rules, human-understanding requirements, small-change expectations, and selective trust gates, with harder throttles reserved for overload cases.

**Key findings:**

1. [inference] AI-generated OSS contribution pressure is best understood as a review-capacity asymmetry, because multiple sources show that generation has become cheaper while review, triage, and follow-up still consume scarce human attention. [source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json]
2. [fact] Real-world studies of AI-generated code show that outcomes depend heavily on task shape and that persistent debt remains material, which means maintainers should not treat all AI-assisted contributions as equally risky or equally cheap to review. [source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592]
3. [fact] The dominant OSS governance response in 2025 to 2026 is accountability-first rather than blanket prohibition, with projects requiring disclosure, human understanding, focused changes, tests, and the right to close or block repeated low-value AI-assisted submissions. [source: https://arxiv.org/html/2603.26487v1; https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://devguide.python.org/getting-started/generative-ai/; https://matplotlib.org/devdocs/devel/contribute.html#generative-ai; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions]
4. [inference] Explicit trust gates, including the "vouch" pattern, are a defensible middle path because they preserve legitimate newcomer entry while filtering the one-shot, low-engagement interaction style that many agent-generated submissions exhibit. [source: https://github.com/mitchellh/vouch; https://github.com/mitchellh/vouch/blob/main/FAQ.md; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json]
5. [inference] Hard throttles, including auto-closing external pull requests or shutting down bounty channels, become rational once overload is already acute, because some projects are explicitly trading openness for reviewer survival and signal preservation. [source: https://github.com/tldraw/tldraw/issues/7695; https://lists.haxx.se/pipermail/daniel/2026-January/000143.html; https://curl.se/dev/contribute.html#on-ai-use-in-curl]
6. [inference] GitHub already provides useful but incomplete platform controls, including issue forms, pull request templates, interaction limits, and protected branches, so the main implementation gap is not missing mechanics alone but project willingness to define admissibility rules. [source: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories]
7. [fact] Maintainer sustainability data show that projects are defending an already fragile labor pool, not a healthy surplus of review capacity, because contributor pipelines, employer support, compensation, and retention all look weak in recent surveys. [source: https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf]
8. [inference] The best-supported operating model is therefore selective openness: keep low-cost discussion and structured issue intake open, but add progressively stronger friction as the expected maintainer review cost and the amount of project surface affected by a submission rises. [source: https://github.com/mitchellh/vouch; https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://github.com/tldraw/tldraw/issues/7695]

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Review-cost asymmetry is the main problem shape. | https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json | high | qualitative convergence |
| [fact] Task type materially changes acceptance and debt outcomes. | https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592 | high | empirical studies |
| [fact] Accountability-first policies dominate current project responses. | https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://devguide.python.org/getting-started/generative-ai/; https://matplotlib.org/devdocs/devel/contribute.html#generative-ai; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions; https://arxiv.org/html/2603.26487v1 | high | policy text + survey |
| [inference] Trust gates preserve some openness while filtering one-shot low-engagement submissions. | https://github.com/mitchellh/vouch; https://github.com/mitchellh/vouch/blob/main/FAQ.md; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json | medium | practitioner pattern |
| [inference] Hard throttles are used when overload becomes unsustainable. | https://github.com/tldraw/tldraw/issues/7695; https://lists.haxx.se/pipermail/daniel/2026-January/000143.html; https://curl.se/dev/contribute.html#on-ai-use-in-curl | medium | primary project statements plus synthesis |
| [inference] GitHub controls help structure intake but do not replace policy judgment. | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories | medium | platform docs plus synthesis |
| [fact] Maintainer capacity is already fragile before AI-generated intake is added. | https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf | high | survey data |
| [inference] Selective openness is the best-supported default operating model. | https://github.com/mitchellh/vouch; https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://github.com/tldraw/tldraw/issues/7695 | medium | synthesis claim |

**Assumptions:**

- [assumption] "Effective" is defined primarily as preserving maintainer capacity and project health rather than maximizing total contribution count. Justification: the empirical and policy evidence is concentrated on review burden and sustainability.
- [assumption] Project-policy case studies are used as operational exemplars rather than as prevalence estimates across all OSS repositories. Justification: the retrieved policy corpus is rich enough for pattern extraction but not for global frequency claims.
- [assumption] The absence of comparative filter-accuracy metrics means recommended strategy order should be read as a response ladder, not as a mathematically proven optimum. Justification: current evidence is stronger on problem shape than on exact control-effect sizes.

**Analysis:**

- [inference; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf] The evidence weights toward intake friction before detailed review because OSS maintainers are defending a scarce human resource, not operating a surplus review function that can absorb more plausible-looking noise.
- [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-compound-error-accumulation-ai-codebases.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-human-oversight-ai-software-development.md] Task heterogeneity matters because the same AI provenance can be harmless in documentation or narrowly scoped maintenance work but costly in high-context feature or security work, so gating should track review cost and the amount of project surface affected rather than ideology.
- [inference; source: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions; https://github.com/mitchellh/vouch; https://github.com/tldraw/tldraw/issues/7695; https://curl.se/dev/contribute.html#on-ai-use-in-curl] The strategies line up into a coherent ladder: start with structured intake and accountability requirements, escalate to explicit social trust gates when noise remains high, and reserve full channel throttles for cases where maintainers are already underwater.
- [inference; source: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://github.com/mitchellh/vouch] The platform can help by making structure and access control easier, but the decisive governance work stays local because a project must still decide what counts as enough understanding, enough relationship, and enough verification to deserve review time.

**Risks, gaps, uncertainties:**

- [fact; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249] Current research is strong on qualitative pattern recognition, but weak on controlled comparisons of policy effectiveness across repositories.
- [fact; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592] Acceptance-rate and debt studies show task heterogeneity and persistence, but they do not isolate the exact share of maintainer pain caused by low-quality AI-generated intake versus other concurrent workflow pressures.
- [assumption] Smaller or lower-traffic repositories may experience different trade-offs from flagship projects such as Ghostty, tldraw, or cURL. Justification: the retrieved policy examples are skewed toward visible projects with enough volume to publish explicit responses.
- [assumption] Human-voice and trust-gate filters may exclude some legitimate contributors who are unfamiliar, anxious, or writing in a non-native language. Justification: no retrieved source reports systematic false-positive rates for these controls.

**Open questions:**

- [assumption] What false-positive and false-negative rates do human-voice gates, disclosure rules, and vouch systems produce in practice? Justification: no retrieved dataset measures them directly.
- [assumption] Which combinations of issue forms, interaction limits, and trust gating minimize maintainer hours per accepted change? Justification: retrieved evidence identifies the components, not the optimal bundle.
- [assumption] Can GitHub expose richer contributor-trust and follow-through signals without unduly harming pseudonymous participation or newcomer access? Justification: current GitHub controls are coarse relative to the policy problem.

### §7 Recursive Review

- Review pass: completed.
- Claim-source binding: checked across Research Skill Output and Findings.
- Cross-item integration: aligned with `cites:` and `related:` fields.
- Confidence selected: medium.

---

## Findings

### Executive Summary

The most effective strategies are layered intake controls that make human accountability hard to fake and maintainer review time easy to protect, rather than a single universal ban on AI use. [inference; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://github.com/mitchellh/vouch; https://github.com/tldraw/tldraw/issues/7695]

Empirical evidence shows that AI-generated contributions vary sharply by task type and can leave persistent maintenance debt, so maintainers should gate by scope and verification burden, not by AI provenance alone. [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592]

OSS maintainer capacity is already fragile, with weak contributor pipelines, weak institutional support, and high quit-or-considered-quitting rates before AI-generated intake is added. [fact; source: https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf]

Across the cited public GitHub project examples, the best-supported default is a ladder of structured templates, disclosure rules, human-understanding requirements, small-change expectations, and selective trust gates, with harder throttles reserved for overload cases. [inference; source: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions; https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository]

### Key Findings

1. **AI-generated OSS contribution pressure is best understood as a review-capacity asymmetry, because multiple sources show that generation has become cheaper while review, triage, and follow-up still consume scarce human attention.** ([inference]; high confidence; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json)
2. **Real-world studies of AI-generated code show that outcomes depend heavily on task shape and that persistent debt remains material, which means maintainers should not treat all AI-assisted contributions as equally risky or equally cheap to review.** ([fact]; high confidence; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592)
3. **The dominant OSS governance response in 2025 to 2026 is accountability-first rather than blanket prohibition, with projects requiring disclosure, human understanding, focused changes, tests, and the right to close or block repeated low-value AI-assisted submissions.** ([fact]; high confidence; source: https://arxiv.org/html/2603.26487v1; https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://devguide.python.org/getting-started/generative-ai/; https://matplotlib.org/devdocs/devel/contribute.html#generative-ai; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions)
4. **Explicit trust gates, including the "vouch" pattern, are a defensible middle path because they preserve legitimate newcomer entry while filtering the one-shot, low-engagement interaction style that many agent-generated submissions exhibit.** ([inference]; medium confidence; source: https://github.com/mitchellh/vouch; https://github.com/mitchellh/vouch/blob/main/FAQ.md; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json)
5. **Hard throttles, including auto-closing external pull requests or shutting down bounty channels, become rational once overload is already acute, because some projects are explicitly trading openness for reviewer survival and signal preservation.** ([inference]; medium confidence; source: https://github.com/tldraw/tldraw/issues/7695; https://lists.haxx.se/pipermail/daniel/2026-January/000143.html; https://curl.se/dev/contribute.html#on-ai-use-in-curl)
6. **GitHub already provides useful but incomplete platform controls, including issue forms, pull request templates, interaction limits, and protected branches, so the main implementation gap is not missing mechanics alone but project willingness to define admissibility rules.** ([inference]; medium confidence; source: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)
7. **Maintainer sustainability data show that projects are defending an already fragile labor pool, not a healthy surplus of review capacity, because contributor pipelines, employer support, compensation, and retention all look weak in recent surveys.** ([fact]; high confidence; source: https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf)
8. **The best-supported operating model is therefore selective openness: keep low-cost discussion and structured issue intake open, but add progressively stronger friction as the expected maintainer review cost and the amount of project surface affected by a submission rises.** ([inference]; medium confidence; source: https://github.com/mitchellh/vouch; https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://github.com/tldraw/tldraw/issues/7695)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Review-cost asymmetry is the main problem shape. | https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json | high | qualitative convergence |
| [fact] Task type materially changes acceptance and debt outcomes. | https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592 | high | empirical studies |
| [fact] Accountability-first policies dominate current project responses. | https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://devguide.python.org/getting-started/generative-ai/; https://matplotlib.org/devdocs/devel/contribute.html#generative-ai; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions; https://arxiv.org/html/2603.26487v1 | high | policy text plus corpus study |
| [inference] Trust gates preserve some openness while filtering one-shot low-engagement submissions. | https://github.com/mitchellh/vouch; https://github.com/mitchellh/vouch/blob/main/FAQ.md; https://raw.githubusercontent.com/The-Focus-AI/youtube-feed/main/ai-engineer/videos/RjfbvDXpFls.json | medium | practitioner pattern |
| [inference] Hard throttles are used when overload becomes unsustainable. | https://github.com/tldraw/tldraw/issues/7695; https://lists.haxx.se/pipermail/daniel/2026-January/000143.html; https://curl.se/dev/contribute.html#on-ai-use-in-curl | medium | primary project statements plus synthesis |
| [inference] GitHub controls help structure intake but do not replace policy judgment. | https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories | medium | platform docs plus synthesis |
| [fact] Maintainer capacity is already fragile before AI-generated intake is added. | https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf | high | survey data |
| [inference] Selective openness is the best-supported default operating model. | https://github.com/mitchellh/vouch; https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://github.com/tldraw/tldraw/issues/7695 | medium | synthesis claim |

### Assumptions

- [assumption] "Effective" is defined primarily as preserving maintainer capacity and project health rather than maximizing total contribution count. Justification: the empirical and policy evidence is concentrated on review burden and sustainability.
- [assumption] Project-policy case studies are operational exemplars rather than prevalence estimates across all OSS repositories. Justification: the retrieved policy corpus supports pattern extraction more strongly than global frequency measurement.
- [assumption] The absence of comparative filter-accuracy metrics means recommended strategy order should be read as a response ladder, not as a mathematically proven optimum. Justification: current evidence is stronger on problem shape than on exact control effect sizes.

### Analysis

The evidence weights toward intake friction before detailed review because OSS maintainers are defending a scarce human resource, not operating a surplus review function that can absorb more plausible-looking noise. [inference; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249; https://project.linuxfoundation.org/hubfs/LF%20Research/Open%20Source%20Maintainers%202023%20-%20Report.pdf?hsLang=en; https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf]

Task heterogeneity matters because the same AI provenance can be harmless in documentation or narrowly scoped maintenance work but costly in high-context feature or security work, so gating should track review cost and the amount of project surface affected rather than ideology. [inference; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-compound-error-accumulation-ai-codebases.md; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-05-01-human-oversight-ai-software-development.md]

The strategies line up into a coherent ladder: start with structured intake and accountability requirements, escalate to explicit social trust gates when noise remains high, and reserve full channel throttles for cases where maintainers are already underwater. [inference; source: https://raw.githubusercontent.com/ghostty-org/ghostty/main/AI_POLICY.md; https://www.eff.org/deeplinks/2026/02/effs-policy-llm-assisted-contributions-our-open-source-projects; https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions; https://datafusion.apache.org/contributor-guide/index.html#ai-assisted-contributions; https://github.com/mitchellh/vouch; https://github.com/tldraw/tldraw/issues/7695; https://curl.se/dev/contribute.html#on-ai-use-in-curl]

The platform can help by making structure and access control easier, but the decisive governance work stays local because a project must still decide what counts as enough understanding, enough relationship, and enough verification to deserve review time. [inference; source: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates; https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository; https://github.com/mitchellh/vouch]

### Risks, Gaps, and Uncertainties

- [fact; source: https://arxiv.org/html/2603.26487v1; https://arxiv.org/abs/2603.27249] Current research is strong on qualitative pattern recognition, but weak on controlled comparisons of policy effectiveness across repositories.
- [fact; source: https://arxiv.org/html/2602.08915v1; https://arxiv.org/abs/2603.28592] Acceptance-rate and debt studies show task heterogeneity and persistence, but they do not isolate the exact share of maintainer pain caused by low-quality AI-generated intake versus other concurrent workflow pressures.
- [assumption] Smaller or lower-traffic repositories may experience different trade-offs from flagship projects such as Ghostty, tldraw, or cURL. Justification: the retrieved policy examples are skewed toward visible projects with enough volume to publish explicit responses.
- [assumption] Human-voice and trust-gate filters may exclude some legitimate contributors who are unfamiliar, anxious, or writing in a non-native language. Justification: no retrieved source reports systematic false-positive rates for these controls.

### Open Questions

- [assumption] What false-positive and false-negative rates do human-voice gates, disclosure rules, and vouch systems produce in practice? Justification: no retrieved dataset measures them directly.
- [assumption] Which combinations of issue forms, interaction limits, and trust gating minimize maintainer hours per accepted change? Justification: retrieved evidence identifies the components, not the optimal bundle.
- [assumption] Can GitHub expose richer contributor-trust and follow-through signals without unduly harming pseudonymous participation or newcomer access? Justification: current GitHub controls are coarse relative to the policy problem.

---

## Output

- Type: knowledge
- Description: A synthesis of how OSS maintainers can defend scarce review capacity against low-quality AI-generated contribution volume by combining accountability rules, structured intake, trust gates, and overload throttles. [inference; source: https://arxiv.org/html/2603.26487v1; https://github.com/mitchellh/vouch; https://github.com/tldraw/tldraw/issues/7695]
- Links:
  - https://arxiv.org/html/2603.26487v1
  - https://github.com/mitchellh/vouch
  - https://www.sonarsource.com/the-2024-tidelift-maintainer-impact-report.pdf
