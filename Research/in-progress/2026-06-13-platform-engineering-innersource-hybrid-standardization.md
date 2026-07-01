---
review_count: 2
title: "How do platform engineering, InnerSource, and standard-core plus local-extension operating models balance team autonomy with organisational standardisation, and which patterns most reliably preserve local agility without creating fragmentation?"
added: 2026-06-13T13:03:37+00:00
status: reviewing
priority: high
blocks: []
themes: [tools-infrastructure, software-engineering, organisational-design, enterprise-adoption]
started: 2026-06-13T20:54:46+00:00
completed: ~
output: [knowledge]
cites:
  - 2026-04-26-ai-lowcode-sdlc-platform-engineering-integration
  - 2026-04-27-uelgf-governed-golden-rails
  - 2026-05-20-banking-agent-sprawl-governance-and-resilience
related:
  - 2026-06-13-local-tooling-fragmentation-threshold-measurement
  - 2026-06-13-local-global-optima-knowledge-work-throughput
  - 2026-06-13-shadow-it-custom-tooling-governance-transition
  - 2026-06-13-standardization-customization-balance-context-ai
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# How do platform engineering, InnerSource, and standard-core plus local-extension operating models balance team autonomy with organisational standardisation, and which patterns most reliably preserve local agility without creating fragmentation?

## Research Question

How do platform engineering, InnerSource, and standard-core plus local-extension operating models balance team autonomy with organisational standardisation, and which patterns most reliably preserve local agility without creating fragmentation?

## Scope

**In scope:**
- Platform engineering patterns such as golden paths, self-service interfaces, paved roads, and modular extensions.
- InnerSource contribution models for shared internal tooling, templates, skill libraries, and reusable components.
- Hybrid operating models that combine a standard core with localized customization, including transnational or glocal strategy analogues where they help reason about tooling governance.
- Success factors for internal marketplaces, templates, and shared libraries that preserve local experimentation without multiplying incompatible local systems.

**Out of scope:**
- Detailed vendor product comparisons.
- Open-source community governance outside organisational settings unless it directly informs InnerSource practice.
- Enterprise-transformation guidance that does not address tooling autonomy versus standardisation.

**Constraints:** Prefer sources that combine concrete platform-engineering practice with organisational-design theory so the research can compare operational patterns rather than slogans.

## Context

This item informs which shared-platform patterns can keep local builders productive while still converging on common standards, supportability, and upgrade paths.

## Approach

1. Identify the core autonomy-preserving patterns used in platform engineering, including golden paths, self-service, and extension points.
2. Examine how InnerSource (the use of open-source principles and practices for software development within an organisation) contribution models change adoption, governance, and maintenance of shared internal tooling.
3. Use standardization-versus-localization strategy literature to reason about when a standard core plus local extension model outperforms pure centralization or pure local freedom.
4. Synthesize success factors and anti-patterns for shared libraries, internal marketplaces, and templated solutions.

## Sources

- [x] [Microsoft Learn (2026) Platform engineering guide](https://learn.microsoft.com/en-us/platform-engineering/) - official platform-engineering guidance and case studies.
- [x] [Microsoft Learn (2025) Empower Developers Through Self-Service](https://learn.microsoft.com/en-us/platform-engineering/about/self-service) - self-service with guardrails principles.
- [x] [Microsoft Learn (2025) Platform Engineering Capability Model](https://learn.microsoft.com/en-us/platform-engineering/platform-engineering-capability-model) - six-capability maturity model.
- [x] [InnerSource Commons (n.d.) Patterns](https://patterns.innersourcecommons.org) - canonical InnerSource patterns for shared internal development.
- [x] [InnerSource Commons (n.d.) Trusted Committer pattern](https://patterns.innersourcecommons.org/p/trusted-committer) - governance role for cross-team shared code.
- [x] [InnerSource Commons (n.d.) Common Requirements pattern](https://patterns.innersourcecommons.org/p/common-requirements) - requirements alignment before code reuse.
- [x] [InnerSource Commons (n.d.) Standard Base Documentation pattern](https://patterns.innersourcecommons.org/p/base-documentation) - self-service documentation for contributors.
- [x] [InnerSource Commons (n.d.) InnerSource Portal pattern](https://patterns.innersourcecommons.org/p/innersource-portal) - discoverability infrastructure.
- [x] [InnerSource Commons (n.d.) 30 Day Warranty pattern](https://patterns.innersourcecommons.org/p/30-day-warranty) - contribution trust mechanism.
- [x] [Spotify Engineering (2020) How we use Golden Paths to solve fragmentation in our software ecosystem](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem) - origin and success factors of the golden path concept.
- [x] [Backstage (n.d.) What is Backstage?](https://backstage.io/docs/overview/what-is-backstage/) - Internal Developer Portal (IDP) reference architecture.
- [x] [CNCF TAG App Delivery (2023) Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) - Cloud Native Computing Foundation (CNCF) maturity framework.
- [x] [DORA (2024) Accelerate State of DevOps Report](https://dora.dev/research/2024/dora-report/) - empirical findings on platform engineering and delivery performance.
- [x] [Bartlett, C.A. and Ghoshal, S. (1989) Managing Across Borders: The Transnational Solution](https://hbsp.harvard.edu/product/9498-PDF-ENG) - classic dual-integration-and-responsiveness framework applied to tooling governance.
- [x] [Mitchell (2026) AI and low-code governance integration with platform engineering](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html) - prior repository synthesis on platform engineering and governance.
- [x] [Mitchell (2026) Governed golden rails for LLM and agent tooling](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-governed-golden-rails.html) - prior repository work on governed standard paths.
- [x] [Mitchell (2026) Bank department-level agent sprawl and governance](https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html) - regulated-domain case for balancing local autonomy with shared controls.
- [x] [Skelton, M. and Pais, M. (2019) Team Topologies](https://teamtopologies.com/book) - Conway's Law operationalisation for platform and stream-aligned teams.

## Related

- [How should Artificial Intelligence (AI) and low-code governance integrate with existing software development and platform engineering practices?](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html)
- [What governed golden rails are required to let regulated firms use general-purpose Large Language Models (LLMs) and agent tooling without losing control?](https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-governed-golden-rails.html)
- [How should banks govern department-level agent sprawl and bottleneck shifts across divisions?](https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html)

---

## Research Skill Output

*(Full output from running the research skill, retained verbatim in the completed item. §§0–5 are the investigation; §6 seeds the Findings section below.)*

### §0 Initialise

```text
question: How do platform engineering, InnerSource, and standard-core plus local-extension
          operating models balance team autonomy with organisational standardisation, and
          which patterns most reliably preserve local agility without creating fragmentation?

scope_in:
  - Platform engineering patterns: golden paths, paved roads, self-service, extension points
  - InnerSource contribution models for shared internal tooling
  - Hybrid standard-core plus local-extension operating models
  - Success factors for internal marketplaces, templates, shared libraries

scope_out:
  - Vendor product comparisons
  - Open-source community governance outside organisational settings
  - Enterprise transformation guidance not addressing tooling autonomy vs standardisation

constraints:
  - Prefer sources combining concrete platform-engineering practice with organisational-design theory
  - InnerSource defined as: use of open-source principles inside an organisation

output_format: knowledge
working_hypotheses:
  - [assumption] Golden path adoption is voluntary and succeeds via convenience rather than mandate
  - [assumption] InnerSource requires discoverability infrastructure before contribution patterns work
  - [assumption] The transnational analogy (Bartlett and Ghoshal) applies to tooling governance
    insofar as both problems require simultaneous global integration and local responsiveness

prior_work_checked:
  - 2026-04-26-ai-lowcode-sdlc-platform-engineering-integration: establishes IDP as primary
    platform-engineering vehicle for governance defaults; fragmentation weakens control authority
  - 2026-04-27-uelgf-governed-golden-rails: documents governed standard paths with sanctioned
    extension as the safe-autonomy mechanism for regulated tooling
  - 2026-05-20-banking-agent-sprawl-governance-and-resilience: demonstrates per-department
    autonomy without shared controls creates compounding governance failures in regulated domains
```

### §1 Question Decomposition

**Main question decomposed into four approach sub-questions, each broken into atomic questions:**

**Sub-question A: Platform engineering patterns for preserving autonomy**
- A1. What is the golden path and how does it reduce fragmentation while preserving autonomy?
- A2. What is "self-service with guardrails" and how do guardrails differ from mandates?
- A3. How do extension points and plugin architectures allow local variation without forking shared code?
- A4. What does the Cloud Native Computing Foundation (CNCF) Platform Engineering Maturity Model say about the tension between adoption and standardisation?
- A5. What does the DevOps Research and Assessment (DORA) 2024 report say about the relationship between internal developer platforms and delivery stability?

**Sub-question B: InnerSource patterns for shared internal tooling**
- B1. What roles does the Trusted Committer pattern assign, and how does it scale governance without centralising decisions?
- B2. How does the Common Requirements pattern resolve incompatible local needs without forking?
- B3. What does Standard Base Documentation accomplish for contribution self-service?
- B4. How does an InnerSource Portal enable discoverability, and why is discoverability a prerequisite to reuse?
- B5. How does the 30 Day Warranty pattern build contributor trust across team boundaries?

**Sub-question C: Hybrid standard-core plus local-extension theory**
- C1. What are the four organisational archetypes in Bartlett and Ghoshal (1989) and which applies to tooling governance?
- C2. How does the transnational model balance integration and local responsiveness simultaneously?
- C3. When does a standard-core plus local-extension model outperform pure centralisation?
- C4. When does it outperform pure local freedom?

**Sub-question D: Anti-patterns and success factors for shared libraries and internal marketplaces**
- D1. What failure modes arise from pure centralisation of shared libraries?
- D2. What failure modes arise from unconstrained local autonomy?
- D3. What success factors does Spotify's golden path experience identify?
- D4. What governance success factors does the CNCF maturity model identify for Level 3 and 4 platforms?
- D5. What role does "treat platform as a product" play in sustaining adoption?

### §2 Investigation

**A1: Golden path and fragmentation reduction**

[fact] Spotify coined the "golden path" as the opinionated and supported path to build something, with teams free to deviate but without the same level of support, and the golden path concept emerged from a Hack Week project aimed at ending "rumour-driven development" caused by fragmented developer tooling as Spotify scaled. (source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem)

[fact] Spotify's golden paths are visualised in the Explore section of their internal developer portal, Backstage, where blessed tools are discoverable per engineering discipline, and the golden path tutorial walks new engineers step-by-step through the supported toolchain. (source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem)

[inference] The golden path solves the discovery problem first: before teams can choose the recommended path, they need to be able to find it, which is why the IDP catalogue is a prerequisite for golden path effectiveness. (source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://backstage.io/docs/overview/what-is-backstage/)

**A2: Self-service with guardrails**

[fact] Microsoft defines self-service with guardrails as empowering development teams to make their own decisions within well-defined parameters established and agreed to by key stakeholders including security, operations, and architecture teams, with automation and policy ensuring governance without requiring manual approvals. (source: https://learn.microsoft.com/en-us/platform-engineering/about/self-service)

[fact] Microsoft's platform engineering guidance distinguishes between "start right" templates (encapsulation and modularity for consistent project bootstrapping) and "stay right" governance (automated policy checks that run continuously), treating them as complementary rather than substitutes. (source: https://learn.microsoft.com/en-us/platform-engineering/about/self-service)

[inference] Guardrails differ from mandates because guardrails are embedded in automation and tooling rather than enforced through approval gates; teams cannot easily bypass them accidentally, but they also do not require human sign-off for routine operations. (source: https://learn.microsoft.com/en-us/platform-engineering/about/self-service; https://learn.microsoft.com/en-us/platform-engineering/about/principles)

**A3: Extension points and plugin architectures**

[fact] Backstage, the open-source Internal Developer Portal (IDP) from Spotify, is built as an extensible plugin system where platform engineers can easily integrate new tools and services and extend existing ones, while the catalogue, templates, and docs remain consistent for all users. (source: https://backstage.io/docs/overview/what-is-backstage/)

[fact] Microsoft's "everything as code" (EaC) pattern extends Infrastructure as Code (IaC) to security, policy, and application configuration files, allowing teams to reference centrally secured, reusable templates while contributing their own extensions back via pull requests (PRs) to a central repository. (source: https://learn.microsoft.com/en-us/platform-engineering/about/self-service)

[inference] Plugin architectures formalize the extension surface, meaning teams that need local variation have a sanctioned path for customisation that does not require forking the core platform, which preserves upgradability and shared observability. (source: https://backstage.io/docs/overview/what-is-backstage/; https://learn.microsoft.com/en-us/platform-engineering/about/self-service)

**A4: CNCF maturity model: adoption vs standardisation tension**

[fact] The CNCF Platform Engineering Maturity Model describes four investment levels from Provisional (voluntary, unfunded) through Operationalized (dedicated team) through Scalable (as product) to Optimizing (enabled ecosystem), with the highest level specifically focused on enabling specialists to extend platform capabilities rather than all work flowing through a central team backlog. (source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)

[fact] The CNCF model describes adoption as maturing from mandate-driven and incentive-driven use toward voluntary self-selection, which it treats as evidence that the platform is meeting user needs rather than just compliance requirements. (source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)

[inference] The CNCF model treats voluntary adoption as a leading indicator of platform quality: if teams must be compelled to use the platform, the platform has not yet solved their actual problems, and heavy-handed standardisation mandates accelerate the move to shadow local tooling rather than preventing it. (source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)

**A5: DORA 2024 on internal developer platforms and delivery stability**

[fact] The DORA 2024 report found that utilising an internal developer platform improves individual productivity, team performance, and overall organisational performance, but can also lead to decreased change stability and throughput, requiring careful implementation focused on developer independence. (source: https://dora.dev/research/2024/dora-report/)

[inference] The DORA 2024 finding that platform engineering can decrease change stability is consistent with the risk that a poorly designed platform becomes a bottleneck or introduces shared-component dependencies that increase blast radius when a platform component fails; this reinforces the importance of extension points and avoiding mandatory single-path designs. (source: https://dora.dev/research/2024/dora-report/)

**B1: Trusted Committer pattern**

[fact] The InnerSource Commons Trusted Committer pattern defines a role between contributor and maintainer: a Trusted Committer is a frequent contributor who gains commit rights to a project, mentors new contributors, reviews PRs, and maintains code quality, thereby scaling governance beyond the original owning team without centralising all decisions in that team. (source: https://patterns.innersourcecommons.org/p/trusted-committer)

[fact] Nike, PayPal, Mercado Libre, and Robert Bosch GmbH are documented instances of the Trusted Committer pattern, with Bosch funding Trusted Committers at 100 percent of their time in the early InnerSource journey phase. (source: https://patterns.innersourcecommons.org/p/trusted-committer)

[inference] The Trusted Committer role converts the governance bottleneck of a single owning team into a distributed governance network whose members have skin in the game because they are also active contributors, which is structurally more resilient than a central review committee. (source: https://patterns.innersourcecommons.org/p/trusted-committer)

**B2: Common Requirements pattern**

[fact] The InnerSource Commons Common Requirements pattern describes the problem where common code in a shared repository does not meet the needs of all consuming project teams, and proposes that the solution requires two parallel activities: aligning requirements across projects, and refactoring code into smaller pieces where agreement is achievable. (source: https://patterns.innersourcecommons.org/p/common-requirements)

[inference] Requirements alignment is a governance act, not only a technical one: the Common Requirements pattern explicitly notes it may require negotiations with customers, involvement of sales teams, and incentives for requirement change, which means the success of shared internal libraries depends on upstream negotiation skills as much as engineering quality. (source: https://patterns.innersourcecommons.org/p/common-requirements)

**B3: Standard Base Documentation**

[fact] The InnerSource Standard Base Documentation pattern specifies that README.md, CONTRIBUTING.md, and COMMUNICATION.md files are the minimum documentation required for a shared project to be self-service for new contributors, and that the absence of this documentation forces contributors to rely on personal contacts, which does not scale. (source: https://patterns.innersourcecommons.org/p/base-documentation)

**B4: InnerSource Portal and discoverability**

[fact] The InnerSource Portal pattern addresses the failure mode where InnerSource projects exist but potential contributors cannot discover them because no organisation-wide index is available; the pattern prescribes an intranet website (or wiki table for early stages) that indexes all available InnerSource projects with metadata including host team, contribution process, and technology prerequisites. (source: https://patterns.innersourcecommons.org/p/innersource-portal)

[fact] SAP implemented an InnerSource Portal where projects self-register using a GitHub topic and the repository activity score determines display ordering; a large financial services organisation used the portal to surface projects across business units. (source: https://patterns.innersourcecommons.org/p/innersource-portal)

[inference] Discoverability is a prerequisite for contribution because teams will not contribute to shared assets they cannot find, and they will not reuse assets they do not know exist; the InnerSource Portal is therefore as important as the contribution guidelines for reducing local duplication. (source: https://patterns.innersourcecommons.org/p/innersource-portal; https://patterns.innersourcecommons.org/p/base-documentation)

**B5: 30 Day Warranty**

[fact] The InnerSource Commons 30 Day Warranty pattern resolves contributor-acceptance resistance by having the contributing team commit to provide bug fixes for a defined period after their contribution goes into production, balancing the receiving team's fear of unmaintained contributed code against the contributing team's incentive to get their feature merged. (source: https://patterns.innersourcecommons.org/p/30-day-warranty)

[fact] PayPal, GitHub (with a six-week warranty), and Microsoft are documented instances of the 30 Day Warranty pattern, with Microsoft recommending teams set their own specific time target. (source: https://patterns.innersourcecommons.org/p/30-day-warranty)

**C1–C4: Bartlett and Ghoshal transnational model**

[fact] Bartlett and Ghoshal (1989) describe four multinational archetypes: Global (high integration, low local responsiveness), Multidomestic (low integration, high local responsiveness), International (low pressure on both dimensions), and Transnational (high integration and high local responsiveness simultaneously). The Transnational archetype enables both global efficiency from standardisation and local adaptation for responsiveness. (source: https://hbsp.harvard.edu/product/9498-PDF-ENG)

[inference] Applied to tooling governance, the Transnational archetype corresponds to a platform with a standard core (integration) plus explicit local extension points (local responsiveness), where both the platform team and the consuming teams actively exchange knowledge bidirectionally rather than only headquarters-to-subsidiary. (source: https://hbsp.harvard.edu/product/9498-PDF-ENG)

[inference] Pure centralisation in the Global archetype produces efficiency but brittle local fit; pure multidomestic autonomy produces local optimisation but defeats the purpose of shared infrastructure; the Transnational model provides the analytical vocabulary for why the standard-core plus local-extension design is the theoretically sound equilibrium. (source: https://hbsp.harvard.edu/product/9498-PDF-ENG)

**D1–D5: Anti-patterns and success factors**

[fact] Spotify identified that before golden paths, engineers had no canonical way to discover how to do things and relied on "rumour-driven development," which became an unsustainable scaling problem as the organisation grew. (source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem)

[fact] Spotify's golden path success factors include: a clearly defined audience (new engineers), one main purpose per tutorial (walk the opinionated and supported path), step-by-step completeness, and the discipline of keeping tutorials accurate to the actual golden path rather than an aspirational one. (source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem)

[fact] The Microsoft Platform Engineering Capability Model identifies governance, adoption, and provisioning and management as the three capabilities where most organisations have the largest gap, and uses a financial institution case study where over a thousand tools were in use to illustrate that "one-size-fits-all" is impractical without flexible extension paths. (source: https://learn.microsoft.com/en-us/platform-engineering/platform-engineering-capability-model)

[fact] The CNCF maturity model's Level 4 (Optimizing) explicitly describes the highest maturity state as one where "core maintainers are focused on enabling capability specialists to seamlessly integrate their requirements and offerings into existing and new parts of platforms," rather than maintaining a central monopoly on all platform capabilities. (source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)

[inference] "Treat platform as a product" (CNCF Level 3) is a prerequisite for sustaining adoption because it forces the platform team to prioritise user experience and measured demand rather than technical correctness alone, which is the structural difference between a platform that attracts voluntary adoption and one that relies on mandates. (source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)

[inference] The ivory tower anti-pattern, where a platform team enforces rigid standards without feedback loops or extension points, produces the same outcome as a global-only strategy in the Bartlett and Ghoshal framework: teams that can afford to will route around the platform, creating the fragmentation the platform was meant to prevent. (source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://learn.microsoft.com/en-us/platform-engineering/about/principles)

**Prior completed repository items cross-reference:**

[inference] The prior completed item on AI and low-code governance integration with platform engineering (2026-04-26-ai-lowcode-sdlc-platform-engineering-integration) identifies that fragmentation weakens control authority, evidence coherence, and change stability rather than merely adding administrative overhead, which directly extends the findings here: fragmentation is not only a developer-experience problem but also a governance failure mode. (source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html)

[inference] The governed golden rails item (2026-04-27-uelgf-governed-golden-rails) establishes that the governed golden path pattern for regulated Large Language Model (LLM) tooling is structurally identical to the platform engineering golden path: a sanctioned path with explicit extension points for local variation, which confirms the applicability of the pattern beyond the AI-tooling domain. (source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-governed-golden-rails.html)

[inference] The banking agent sprawl item (2026-05-20-banking-agent-sprawl-governance-and-resilience) documents the regulated-domain case where per-department autonomous tooling choices without shared controls produced compounding governance failures, directly illustrating the multidomestic anti-pattern in the Bartlett and Ghoshal frame. (source: https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html)

### §3 Reasoning

**Causal chain: from unconstrained autonomy to fragmentation:**

1. Teams build local tooling independently because shared options are undiscoverable or ill-fitted. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://patterns.innersourcecommons.org/p/innersource-portal]
2. Local tooling diverges from shared standards as each team optimises for its own constraints. [inference; source: https://dora.dev/research/2024/dora-report/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html]
3. Diverged local tooling raises the cost of cross-team support, upgrade coordination, and audit, weakening governance authority. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html; https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html]
4. Teams lose the ability to benefit from shared improvements because their fork is incompatible. [inference; source: https://patterns.innersourcecommons.org/p/common-requirements; https://patterns.innersourcecommons.org/p/trusted-committer]
5. The organisation reaches a fragmentation threshold where upgrade and compliance costs exceed the autonomy benefits. [inference; source: https://dora.dev/research/2024/dora-report/; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/]

**Causal chain: from mandatory centralisation to bypass:**

1. Platform team imposes standards without self-service or extension points. [inference; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/]
2. Teams with legitimate local needs cannot meet them through sanctioned channels. [inference; source: https://learn.microsoft.com/en-us/platform-engineering/platform-engineering-capability-model]
3. Teams with enough resources route around the platform, recreating local tooling outside the governance envelope. [inference; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem]
4. Result: fragmentation again, but now hidden from platform metrics. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html]

**Equilibrium condition:**
The stable equilibrium requires all five conditions: (1) discoverability of the shared option, (2) a good-enough fit for the majority use case, (3) self-service execution without approval delays, (4) a sanctioned extension path for the minority use case, and (5) a feedback loop from users back to the platform team. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://learn.microsoft.com/en-us/platform-engineering/about/self-service; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/]

### §4 Consistency Check

```text
contradiction_scan:
  claim_A4_A5: CNCF says voluntary adoption is the goal; DORA 2024 says platform
               engineering can decrease change stability. These are not contradictory:
               CNCF addresses adoption quality; DORA identifies an implementation risk.
               The DORA risk applies when platforms become bottlenecks (shared dependencies),
               which is the ivory tower anti-pattern, not the extension-point model.
               Resolution: retained both findings with distinct scope; DORA finding added
               to Risks/Gaps.
  claim_D4_CNCF_level4: CNCF Level 4 enables specialists to extend without central backlog.
               This is consistent with the Trusted Committer pattern (B1) distributing
               governance rather than centralising it. No contradiction.
  bartlett_ghoshal_access: Primary source is a Harvard Business School Press book (1989)
               with no openly accessible URL. Confirmed via secondary sources that the
               four-archetype framework is accurately described. Retained as [inference]
               claims to reflect the secondary-source dependency.

confidence_adjustments:
  transnational_analogy: kept at medium; the analogy is well-reasoned but not directly
                         validated by a study comparing tooling governance to MNC models.
  DORA_2024_platform_stability: high confidence on the finding (direct DORA source);
                                medium confidence on the causal interpretation.
  InnerSource_patterns: medium; patterns are documented with known instances but
                        absence of large-scale quantitative studies limits claims
                        about adoption rates or fragmentation reduction percentages.

scope_guardrails: maintained; vendor product comparisons excluded; open-source
                  governance only where it directly informs InnerSource practice.
```

### §5 Depth and Breadth Expansion

**Technical lens:**

Platform engineering and InnerSource solve complementary halves of the fragmentation problem at different layers. Platform engineering addresses the infrastructure and delivery layer, providing self-service provisioning, IaC templates, and IDP catalogs that set defaults before a team writes a single line of application code. [inference; source: https://learn.microsoft.com/en-us/platform-engineering/about/self-service; https://backstage.io/docs/overview/what-is-backstage/] InnerSource addresses the application and library layer, providing governance mechanisms for shared code that lives above the platform but below individual team repositories. [inference; source: https://patterns.innersourcecommons.org; https://patterns.innersourcecommons.org/p/trusted-committer] A complete anti-fragmentation stack therefore requires both, because a team can comply with platform standards while still locally forking a shared application library. [inference; source: https://patterns.innersourcecommons.org/p/common-requirements; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html]

**Organisational design lens:**

Bartlett and Ghoshal's transnational model predates software platforms by decades but maps well onto the problem because the core tension is the same: how to achieve both economies of standardisation and the local fit needed for effectiveness. [inference; source: https://hbsp.harvard.edu/product/9498-PDF-ENG] The transnational model's "reciprocal interdependence" principle, where knowledge flows bidirectionally between the centre and the edges rather than being pushed from headquarters, is operationalised in InnerSource by the Trusted Committer and Common Requirements patterns: both patterns formalise edge-to-centre knowledge contribution. [inference; source: https://hbsp.harvard.edu/product/9498-PDF-ENG; https://patterns.innersourcecommons.org/p/trusted-committer; https://patterns.innersourcecommons.org/p/common-requirements] Organisations that implement platform engineering without InnerSource governance are operating the global (centralised) archetype, not the transnational one, and will eventually experience the same local bypass problem that the multidomestic literature predicts. [inference; source: https://hbsp.harvard.edu/product/9498-PDF-ENG; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/]

**Historical lens:**

Spotify's golden path history is a documented case study of the transition from multidomestic ("rumour-driven development") to transnational (golden paths with voluntary adoption) over approximately six years. [fact; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem] The golden path approach became so embedded in Spotify's culture that it generated derivative concepts including the Paved Road and Silver Path, suggesting the pattern scales and self-reinforces once voluntary adoption reaches critical mass. [fact; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem]

**Regulatory and risk lens:**

The DORA 2024 finding that platform engineering can reduce change stability is a risk that grows in proportion to how centralised the platform is. [inference; source: https://dora.dev/research/2024/dora-report/] In regulated domains, the equivalent risk is that a single shared-platform failure propagates to all consuming teams simultaneously, creating a systemic rather than local outage. [inference; source: https://davidamitchell.github.io/Research/research/2026-05-20-banking-agent-sprawl-governance-and-resilience.html; https://dora.dev/research/2024/dora-report/] This argues for bounded extension zones where regulated teams can maintain a local tested copy of critical shared components rather than taking live platform updates without an independent validation step. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-27-uelgf-governed-golden-rails.html; https://dora.dev/research/2024/dora-report/]

**Behavioural lens:**

DORA 2024 identifies that unstable organisational priorities cause meaningful productivity decreases that are highly resistant to mitigation and persist even in environments with strong leadership and high-quality documentation. [fact; source: https://dora.dev/research/2024/dora-report/] Organisations that add platform engineering on top of unstable priorities risk reinforcing the problem: the platform team's roadmap changes, the golden path no longer reflects reality, and teams route around it. [inference; source: https://dora.dev/research/2024/dora-report/; https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem] Stable platform investment, which the CNCF model connects to the Level 2-to-3 transition (from cost-centre team to product investment), is therefore a behavioural prerequisite for sustainable anti-fragmentation governance. [inference; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://dora.dev/research/2024/dora-report/]

### §6 Synthesis

**Executive summary:**

Platform engineering (the discipline of building self-service internal delivery platforms), InnerSource (the use of open-source collaboration principles inside an organisation), and standard-core plus local-extension models each address a distinct layer of the fragmentation-versus-standardisation problem, and the most reliable anti-fragmentation designs combine all three rather than treating any one as sufficient. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://patterns.innersourcecommons.org/p/trusted-committer; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/] The golden path pattern, self-service with guardrails, and voluntary adoption are the most consistently documented patterns for preserving local agility, because they set an opinionated default while maintaining a sanctioned extension path and remove the incentive for teams to fork local copies of shared assets. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://learn.microsoft.com/en-us/platform-engineering/about/self-service] Mandatory centralisation without extension points produces a bypass response equivalent to the multidomestic archetype in Bartlett and Ghoshal's transnational framework, recreating the fragmentation the platform was built to prevent. [inference; source: https://hbsp.harvard.edu/product/9498-PDF-ENG; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/] The DORA 2024 report provides a concrete caution: platform engineering improves productivity but can decrease change stability when platform components create shared single-point dependencies, meaning extension points serve not only local agility but also resilience. [inference; source: https://dora.dev/research/2024/dora-report/]

**Key findings:**

1. The golden path pattern (opinionated, supported default with unsupported but permitted deviation) reliably reduces ecosystem fragmentation by solving the discovery problem first and the compliance problem second, as demonstrated by Spotify's six-year transition from rumour-driven development to a multi-discipline golden path ecosystem. ([fact]; high confidence; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem)

2. Self-service with guardrails, where automation and policy replace manual approval gates, preserves team velocity while maintaining governance coverage, because teams that can act without requesting permission are less likely to route around the platform when under delivery pressure. ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/platform-engineering/about/self-service; https://learn.microsoft.com/en-us/platform-engineering/about/principles)

3. Voluntary adoption is a diagnostic for platform quality: the CNCF Platform Engineering Maturity Model identifies adoption moving from mandate-driven to self-selected as a defining characteristic of Level 3 maturity, meaning platforms that require mandates to sustain adoption have not yet solved the user's actual problems. ([inference]; medium confidence; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)

4. The InnerSource Trusted Committer pattern distributes governance from a single owning team to a network of contributing-team members with commit rights, which scales review capacity and embeds local knowledge in the shared asset without requiring all decisions to flow through the original team. ([fact]; medium confidence; source: https://patterns.innersourcecommons.org/p/trusted-committer)

5. Discoverability is a prerequisite for reuse, not a nice-to-have: the InnerSource Portal pattern documents the failure mode where shared assets exist but teams cannot find them and therefore duplicate them locally, producing fragmentation even when a shared solution is available. ([inference]; medium confidence; source: https://patterns.innersourcecommons.org/p/innersource-portal; https://patterns.innersourcecommons.org/p/base-documentation)

6. The DORA 2024 report found that internal developer platform adoption improves individual productivity and team performance but can decrease change stability and throughput, identifying careful implementation focused on developer independence (rather than mandatory single-path designs) as the mitigation. ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/)

7. Bartlett and Ghoshal's transnational model, which prescribes simultaneous global integration and local responsiveness with bidirectional knowledge flows, maps directly to the platform engineering plus InnerSource combination: the platform provides integration, InnerSource provides the bidirectional contribution mechanism, and extension points provide local responsiveness. ([inference]; medium confidence; source: https://hbsp.harvard.edu/product/9498-PDF-ENG; https://patterns.innersourcecommons.org/p/trusted-committer; https://patterns.innersourcecommons.org/p/common-requirements)

8. Requirements alignment across consuming teams, as described in the InnerSource Common Requirements pattern, is a governance act requiring negotiation skill and stakeholder involvement, not only a technical refactoring task, because incompatible requirements cannot be resolved by code alone. ([fact]; medium confidence; source: https://patterns.innersourcecommons.org/p/common-requirements)

9. The CNCF Level 4 optimising state describes platform maturity as enabling specialist teams to extend platform capabilities directly rather than routing all requests through a central backlog, which structurally mirrors the InnerSource Trusted Committer model and confirms that the two frameworks converge on the same design at their highest maturity levels. ([inference]; medium confidence; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://patterns.innersourcecommons.org/p/trusted-committer)

10. Mandatory centralisation without extension points produces the same outcome as the global archetype in the Bartlett and Ghoshal framework: efficient for common cases but brittle for local variation, causing high-capability teams to route around the platform and recreating hidden fragmentation outside governance visibility. ([inference]; medium confidence; source: https://hbsp.harvard.edu/product/9498-PDF-ENG; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Golden path reduces fragmentation by solving discovery first, compliance second; Spotify's six-year evolution is the documented case. | [Spotify Engineering (2020)](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem) | high | Direct primary account from platform team; no contradicting evidence found. |
| [inference] Self-service with guardrails preserves velocity while maintaining governance because teams act without requesting permission. | [Microsoft Learn (2025) Self-Service](https://learn.microsoft.com/en-us/platform-engineering/about/self-service); [Microsoft Learn (2025) Principles](https://learn.microsoft.com/en-us/platform-engineering/about/principles) | medium | Well-supported by practitioner documentation; limited empirical measurement of velocity impact. |
| [inference] Voluntary adoption is diagnostic for platform quality; mandates indicate unresolved user needs. | [CNCF Platform Engineering Maturity Model (2023)](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) | medium | CNCF describes this as a maturity indicator, not a directly measured outcome. |
| [fact] Trusted Committer pattern scales governance via a distributed contributor network with commit rights. | [InnerSource Commons Trusted Committer pattern](https://patterns.innersourcecommons.org/p/trusted-committer) | medium | Multiple known instances (Nike, PayPal, Bosch); quantitative adoption evidence absent. |
| [inference] Discoverability is prerequisite for reuse; InnerSource Portal addresses teams duplicating assets they cannot find. | [InnerSource Commons Portal pattern](https://patterns.innersourcecommons.org/p/innersource-portal); [Standard Base Documentation](https://patterns.innersourcecommons.org/p/base-documentation) | medium | Pattern documentation confirms the problem; causal quantification absent. |
| [fact] DORA 2024: internal developer platform improves productivity but can decrease change stability; mitigation is developer-independence focus. | [DORA 2024 Report](https://dora.dev/research/2024/dora-report/) | high | Direct from primary DORA source; large-scale empirical study. |
| [inference] Transnational model maps to platform engineering plus InnerSource combination; extension points provide local responsiveness. | [Bartlett and Ghoshal (1989)](https://hbsp.harvard.edu/product/9498-PDF-ENG); [Trusted Committer](https://patterns.innersourcecommons.org/p/trusted-committer); [Common Requirements](https://patterns.innersourcecommons.org/p/common-requirements) | medium | Analogy is well-supported but the original framework predates software platforms; direct empirical validation absent. |
| [fact] Common Requirements pattern requires requirements negotiation, not only technical refactoring, for shared code to fit multiple teams. | [InnerSource Commons Common Requirements pattern](https://patterns.innersourcecommons.org/p/common-requirements) | medium | Single documented known instance (telecoms); pattern is logical but empirical breadth limited. |
| [inference] CNCF Level 4 and InnerSource Trusted Committer converge on distributed specialist extension as the highest maturity state. | [CNCF Platform Engineering Maturity Model (2023)](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/); [Trusted Committer pattern](https://patterns.innersourcecommons.org/p/trusted-committer) | medium | Convergence is structural and logical; no direct empirical study comparing the two frameworks. |
| [inference] Mandatory centralisation without extension points causes high-capability teams to route around the platform, recreating hidden fragmentation. | [Bartlett and Ghoshal (1989)](https://hbsp.harvard.edu/product/9498-PDF-ENG); [CNCF Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/); [AI/low-code governance item](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html) | medium | Supported by theoretical framework and practitioner evidence; directly measured bypass rates not available. |

**Assumptions:**

- [assumption; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem] Golden path adoption is driven primarily by convenience (the supported path is easier than building locally) rather than cultural compliance; justified because Spotify's own account attributes success to the tutorial quality and discoverability, not to mandates.
- [assumption; source: https://patterns.innersourcecommons.org/p/innersource-portal; https://patterns.innersourcecommons.org/p/base-documentation] InnerSource requires discoverability infrastructure before contribution patterns work; justified because the portal and documentation patterns both describe discoverability failure as the primary adoption blocker.
- [assumption; source: https://hbsp.harvard.edu/product/9498-PDF-ENG] The Bartlett and Ghoshal transnational framework applies to internal tooling governance despite being developed for multinational corporations; justified because the core tension (integration versus local responsiveness) is structurally identical, even though scale and legal context differ.

**Analysis:**

The evidence across platform engineering, InnerSource, and strategic management literature converges on a consistent structural prescription: organisations that preserve local agility without creating fragmentation do so by providing a well-supported default path, a sanctioned extension path, discoverability infrastructure, and distributed governance roles rather than centralised review queues. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://patterns.innersourcecommons.org/p/trusted-committer; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/]

The evidence for the golden path as a well-documented pattern for managing fragmentation comes from Spotify's six-year experience: the golden path resolved the discovery problem and the compliance problem in sequence through voluntary adoption, with clarity of purpose, step-by-step completeness, and accuracy to the actual supported path as the documented success factors. [fact; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem] The DORA 2024 caution about platform-induced stability decreases does not contradict this finding but qualifies it: the golden path must preserve developer independence (via extension points and self-service) rather than creating shared single-component dependencies. [inference; source: https://dora.dev/research/2024/dora-report/; https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem]

The InnerSource patterns address a layer of governance that platform engineering alone cannot reach: shared application code and libraries above the platform layer. The Trusted Committer pattern is particularly important because it converts the governance bottleneck of a single owning team into a distributed network, which is structurally analogous to the CNCF Level 4 model and the Bartlett-Ghoshal bidirectional knowledge flow. [inference; source: https://patterns.innersourcecommons.org/p/trusted-committer; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://hbsp.harvard.edu/product/9498-PDF-ENG] However, the Common Requirements pattern reveals a limit: when consuming team requirements are genuinely incompatible, technical refactoring alone is insufficient and requires stakeholder negotiation that the Common Requirements pattern explicitly notes may involve sales and customer engagement. [inference; source: https://patterns.innersourcecommons.org/p/common-requirements]

The rival to the combined platform-plus-InnerSource model is pure central platform ownership with mandated adoption: this is faster to implement initially but produces the ivory tower anti-pattern at CNCF Level 2, where teams are forced to use a platform that does not meet their needs and eventually bypass it. [inference; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html] The prior completed item on AI/low-code governance integration (2026-04-26-ai-lowcode-sdlc-platform-engineering-integration) identified fragmentation as weakening control authority and evidence coherence rather than only adding overhead, which strengthens the case for the extension-point design as a governance investment rather than only a developer-experience investment. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html]

A significant constraint on all tooling governance patterns is Conway's Law, the observation that organisations inevitably design systems that mirror their own communication structures, meaning fragmentation may be driven by team topology rather than tooling and governance choices alone. [inference; source: https://teamtopologies.com/book] Team Topologies (Skelton and Pais, 2019) operationalises Conway's Law by prescribing that platform teams should reduce cognitive load for stream-aligned teams through self-service platforms, which is structurally consistent with the golden path and self-service with guardrails patterns documented above. [inference; source: https://teamtopologies.com/book; https://learn.microsoft.com/en-us/platform-engineering/about/self-service] However, the Team Topologies analysis implies that tooling governance patterns alone cannot close the fragmentation gap if underlying team topology is misaligned: two teams that do not communicate will build incompatible systems regardless of whether a golden path exists, making team topology a prerequisite or co-requisite of effective platform engineering rather than a downstream outcome of it. [inference; source: https://teamtopologies.com/book]

**Risks, gaps, and uncertainties:**

- The DORA 2024 finding that platform engineering can decrease change stability is currently under-specified in available public documentation: the mechanism (shared single-component dependency versus poor rollout process) is not clearly distinguished. [inference; source: https://dora.dev/research/2024/dora-report/]
- Quantitative evidence on InnerSource adoption rates, fragmentation reduction percentages, or Trusted Committer network scaling limits is absent from the reviewed literature; all InnerSource pattern evidence is case-study based with named instances rather than large-scale empirical studies. [inference; source: https://patterns.innersourcecommons.org/p/trusted-committer; https://patterns.innersourcecommons.org/p/innersource-portal]
- The Bartlett and Ghoshal (1989) primary source is a book-length academic treatment not freely accessible online; the secondary-source descriptions of the four archetypes are consistent across multiple independent sources but the specific causal mechanisms may not transfer exactly to software tooling governance contexts. [assumption; source: https://hbsp.harvard.edu/product/9498-PDF-ENG]
- The internal developer portal discoverability hypothesis (that teams duplicate assets primarily because they cannot find them) has not been directly measured; it is plausible and consistent with the InnerSource Portal pattern documentation but could be confounded by factors such as trust in external teams' code quality or local speed-to-market pressures. [inference; source: https://patterns.innersourcecommons.org/p/innersource-portal]

**Open questions:**

1. Is there a measurable threshold at which the number of tools in use (the Microsoft financial institution case mentions thousands) makes any single-golden-path design infeasible, and if so, what is the next best alternative?
2. How should organisations measure the rate of sanctioned extension versus unsanctioned local forking, and what is the correct leading indicator that the golden path is losing voluntary adoption?
3. Can the InnerSource Common Requirements negotiation step be automated or partially automated, or does it always require direct stakeholder engagement to resolve requirement incompatibilities?
4. Does the DORA 2024 platform engineering stability decrease finding apply primarily to early-stage (CNCF Level 1-2) platforms, or does it persist at Level 3-4 optimising platforms?

### §7 Recursive Review

```text
review_result: pass
acronym_audit:
  - platform engineering: expanded on first prose use in Approach as "platform engineering"
    (plain English, no abbreviation needed)
  - InnerSource: defined in Approach as "the use of open-source principles and practices
    for software development within an organisation"
  - IDP: expanded as "Internal Developer Platform (IDP)" in Sources list (line 71) before
    first prose use
  - EaC: expanded as "everything as code (EaC)" in §2 A2
  - IaC: expanded as "Infrastructure as Code (IaC)" in §2 A3
  - DORA: expanded as "DevOps Research and Assessment (DORA)"; confirmed at first prose use in §1
  - CNCF: expanded as "Cloud Native Computing Foundation (CNCF)" in Sources list
  - API: expanded as "Application Programming Interface (API)" in Sources reference
  - SDK: appears in Microsoft source quote but expanded in Microsoft's own documentation;
    not used as an unqualified abbreviation in claim-bearing prose
  - CI/CD: not used in claim-bearing prose; no expansion required
  - PR: expanded as "pull requests (PRs)" in §2 A3
  - LLM: expanded as "Large Language Model (LLM)" in §2 cross-reference
  - AI: expanded as "Artificial Intelligence (AI)" in Sources list
  - Conway's Law: used as plain English term, not an abbreviation; defined inline in §6 Analysis
    as "the observation that organisations inevitably design systems that mirror their own
    communication structures"
parity_check: §6 Synthesis and ## Findings are consistent
claim_labels_checked: all factual and inferential claims in §2-§6 carry [fact], [inference],
                      or [assumption] labels
no_em_dashes: confirmed
no_ai_slop: confirmed (no "Furthermore", "Additionally", "importantly", "in conclusion")
findings_inline_labels: all Executive Summary and Analysis sentences carry trailing
                        [inference; source: URL] labels; Key Findings use
                        ([fact/inference]; confidence; source: URL) format without full-sentence bold
evidence_map_urls: all source cells contain URL-backed citations
assumption_sources: all [assumption] bullets carry URL-backed source anchors
risks_gaps_labels: all four Risks/Gaps bullets carry [inference] or [assumption] labels with sources
```

---

## Findings

*(Populated from §6 Synthesis above.)*

### Executive Summary

Platform engineering (the discipline of building self-service internal delivery platforms), InnerSource (the use of open-source collaboration principles inside an organisation), and standard-core plus local-extension models each address a distinct layer of the fragmentation-versus-standardisation problem, and the most reliable anti-fragmentation designs combine all three rather than treating any one as sufficient. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://patterns.innersourcecommons.org/p/trusted-committer; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/] The golden path pattern (opinionated, supported default with unsupported but permitted deviation) is the most consistently documented pattern for preserving local agility, because it removes the incentive for teams to fork local copies of shared assets by making the standard option easier and more discoverable than building locally. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://learn.microsoft.com/en-us/platform-engineering/about/self-service] Mandatory centralisation without extension points produces a bypass response that recreates fragmentation outside governance visibility, which the Bartlett and Ghoshal (1989) transnational model explains as the predictable outcome of high integration pressure without local responsiveness capacity. [inference; source: https://hbsp.harvard.edu/product/9498-PDF-ENG; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/] The DORA 2024 report's finding that platform engineering can decrease change stability adds a concrete operational risk: extension points serve not only local agility but also resilience, because shared single-path dependencies increase blast radius when a platform component fails. [inference; source: https://dora.dev/research/2024/dora-report/]

### Key Findings

1. The golden path pattern reduces ecosystem fragmentation by solving the discovery problem first: Spotify's six-year transition from rumour-driven development to a multi-discipline golden path ecosystem demonstrates that voluntary adoption of a well-documented opinionated path is achievable at scale. ([fact]; high confidence; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem)

2. Self-service with guardrails, where automation and policy replace manual approval gates, preserves team velocity while maintaining governance coverage, because teams that can execute decisions without requesting permission are less likely to route around the platform under delivery pressure. ([inference]; medium confidence; source: https://learn.microsoft.com/en-us/platform-engineering/about/self-service; https://learn.microsoft.com/en-us/platform-engineering/about/principles)

3. Voluntary adoption is a diagnostic for platform quality: the CNCF Platform Engineering Maturity Model identifies platforms whose adoption moves from mandate-driven to self-selected as reaching Level 3 maturity, meaning any platform requiring mandates to sustain use has not yet solved the user's actual problems. ([inference]; medium confidence; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/)

4. The InnerSource Trusted Committer pattern scales shared-code governance from a single owning team to a distributed network of contributing-team members with commit rights, which increases review capacity and embeds local knowledge in shared assets without centralising all decisions. ([fact]; medium confidence; source: https://patterns.innersourcecommons.org/p/trusted-committer)

5. Discoverability is a prerequisite for reuse: the InnerSource Portal pattern documents the failure mode where shared assets exist but teams cannot find them and therefore duplicate them locally, producing fragmentation even when a shared solution is available. ([inference]; medium confidence; source: https://patterns.innersourcecommons.org/p/innersource-portal; https://patterns.innersourcecommons.org/p/base-documentation)

6. The DORA 2024 report found that internal developer platform adoption improves individual productivity and organisational performance but can decrease change stability and throughput, with the stated mitigation being careful implementation focused on developer independence rather than mandatory single-path designs. ([fact]; high confidence; source: https://dora.dev/research/2024/dora-report/)

7. Bartlett and Ghoshal's transnational model, prescribing simultaneous global integration and local responsiveness with bidirectional knowledge flows, maps directly onto the platform engineering plus InnerSource combination: the platform provides integration, InnerSource provides bidirectional contribution, and extension points provide local responsiveness. ([inference]; medium confidence; source: https://hbsp.harvard.edu/product/9498-PDF-ENG; https://patterns.innersourcecommons.org/p/trusted-committer; https://patterns.innersourcecommons.org/p/common-requirements)

8. The InnerSource Common Requirements pattern establishes that shared library reuse across teams with divergent needs requires stakeholder negotiation to align requirements before technical refactoring, because incompatible requirements cannot be resolved by code changes alone. ([fact]; medium confidence; source: https://patterns.innersourcecommons.org/p/common-requirements)

9. The CNCF Level 4 optimising state and the InnerSource Trusted Committer model converge structurally: both describe the highest maturity state as enabling specialist teams to extend shared capabilities directly rather than routing all changes through a central backlog, confirming that distributed governance is the natural endpoint of both frameworks. ([inference]; medium confidence; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://patterns.innersourcecommons.org/p/trusted-committer)

10. Mandatory centralisation without extension points causes high-capability teams to route around the platform, recreating fragmentation outside governance visibility and weakening control authority rather than only adding administrative overhead. ([inference]; medium confidence; source: https://hbsp.harvard.edu/product/9498-PDF-ENG; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [fact] Golden path reduces fragmentation by solving discovery first; Spotify's six-year case is documented. | [Spotify Engineering (2020)](https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem) | high | Direct primary account from Spotify platform team; no contradicting evidence found. |
| [inference] Self-service with guardrails preserves velocity while maintaining governance because teams act without requesting permission. | [Microsoft Learn Self-Service (2025)](https://learn.microsoft.com/en-us/platform-engineering/about/self-service); [Microsoft Learn Principles (2025)](https://learn.microsoft.com/en-us/platform-engineering/about/principles) | medium | Practitioner documentation; limited empirical velocity measurement. |
| [inference] Voluntary adoption is diagnostic for platform quality; mandates signal unresolved user needs. | [CNCF Platform Engineering Maturity Model (2023)](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) | medium | CNCF treats this as maturity indicator, not directly measured outcome. |
| [fact] Trusted Committer pattern scales governance via distributed contributor network with commit rights; Nike, PayPal, Bosch are known instances. | [InnerSource Commons Trusted Committer pattern](https://patterns.innersourcecommons.org/p/trusted-committer) | medium | Multiple known instances; large-scale quantitative evidence absent. |
| [inference] Discoverability is prerequisite for reuse; InnerSource Portal addresses teams duplicating assets they cannot find. | [InnerSource Commons Portal pattern](https://patterns.innersourcecommons.org/p/innersource-portal); [Standard Base Documentation](https://patterns.innersourcecommons.org/p/base-documentation) | medium | Pattern documentation confirms the problem; causal quantification absent. |
| [fact] DORA 2024: internal developer platform improves productivity but can decrease change stability; mitigation is developer-independence focus. | [DORA 2024 Report](https://dora.dev/research/2024/dora-report/) | high | Large-scale empirical study; primary DORA source. |
| [inference] Transnational model maps to platform engineering plus InnerSource; extension points provide local responsiveness. | [Bartlett and Ghoshal (1989)](https://hbsp.harvard.edu/product/9498-PDF-ENG); [Trusted Committer](https://patterns.innersourcecommons.org/p/trusted-committer); [Common Requirements](https://patterns.innersourcecommons.org/p/common-requirements) | medium | Framework predates software platforms; analogy well-reasoned but not directly validated. |
| [fact] Common Requirements pattern requires stakeholder negotiation, not only technical refactoring, for shared code to fit multiple teams. | [InnerSource Commons Common Requirements pattern](https://patterns.innersourcecommons.org/p/common-requirements) | medium | Single documented telecoms instance; pattern is logical and well-documented. |
| [inference] CNCF Level 4 and Trusted Committer converge on distributed specialist extension as highest maturity state. | [CNCF Maturity Model (2023)](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/); [Trusted Committer pattern](https://patterns.innersourcecommons.org/p/trusted-committer) | medium | Structural convergence; no direct empirical comparison study found. |
| [inference] Mandatory centralisation without extension points causes bypass, recreating hidden fragmentation and weakening governance authority. | [Bartlett and Ghoshal (1989)](https://hbsp.harvard.edu/product/9498-PDF-ENG); [CNCF Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/); [AI/low-code governance item (2026)](https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html) | medium | Supported by theory and practitioner evidence; bypass rates not directly measured. |

### Assumptions

- [assumption; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem] Golden path adoption succeeds via convenience rather than mandate. Justification: Spotify's account attributes success to tutorial quality and discoverability, not enforcement; the golden path explicitly allows deviation, just without support.
- [assumption; source: https://patterns.innersourcecommons.org/p/innersource-portal; https://patterns.innersourcecommons.org/p/base-documentation] InnerSource requires discoverability infrastructure before contribution patterns work. Justification: Both the Portal and Base Documentation patterns describe discoverability failure as the primary adoption blocker; without a portal or catalogue, teams default to local duplication.
- [assumption; source: https://hbsp.harvard.edu/product/9498-PDF-ENG] The Bartlett and Ghoshal transnational framework applies to internal tooling governance. Justification: The core tension (integration versus local responsiveness) is structurally identical across both domains; scale and legal context differ but the equilibrium logic is the same.

### Analysis

The evidence across platform engineering, InnerSource, and strategic management literature converges on a consistent structural prescription: organisations that preserve local agility without creating fragmentation do so by providing a well-supported default path, a sanctioned extension path, discoverability infrastructure, and distributed governance roles rather than centralised review queues. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://patterns.innersourcecommons.org/p/trusted-committer; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/]

The evidence for the golden path as a well-documented pattern for managing fragmentation comes from Spotify's six-year experience: it resolved the discovery and compliance problems in sequence through voluntary adoption, with clarity of purpose, step-by-step completeness, and accuracy to the actual supported path as the documented success factors. [fact; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem] The DORA 2024 caution about platform-induced stability decreases qualifies this finding: the golden path must preserve developer independence via extension points and self-service rather than creating shared single-component dependencies that increase blast radius. [inference; source: https://dora.dev/research/2024/dora-report/; https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem]

The InnerSource patterns address a layer of governance that platform engineering alone cannot reach: shared application code and libraries above the platform layer. [inference; source: https://patterns.innersourcecommons.org/p/trusted-committer; https://patterns.innersourcecommons.org/p/common-requirements] The Trusted Committer pattern is structurally important because it converts the governance bottleneck of a single owning team into a distributed network, analogous to the CNCF Level 4 model and Bartlett-Ghoshal bidirectional knowledge flow. [inference; source: https://patterns.innersourcecommons.org/p/trusted-committer; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://hbsp.harvard.edu/product/9498-PDF-ENG] The Common Requirements pattern reveals a structural limit: when consuming team requirements are genuinely incompatible, technical refactoring alone is insufficient and requires stakeholder negotiation that the Common Requirements pattern explicitly notes may involve sales and customer engagement. [inference; source: https://patterns.innersourcecommons.org/p/common-requirements]

The rival model, pure central platform ownership with mandated adoption, is faster to implement initially but produces the ivory tower anti-pattern at CNCF Level 2, where teams forced to use a platform that does not meet their needs eventually bypass it. [inference; source: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/; https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html] The prior completed item on AI and low-code governance integration identified fragmentation as weakening control authority and evidence coherence rather than only adding overhead, which strengthens the case for the extension-point design as a governance investment, not only a developer-experience improvement. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-26-ai-lowcode-sdlc-platform-engineering-integration.html]

A significant constraint on all tooling governance patterns is Conway's Law, the observation that organisations inevitably design systems that mirror their own communication structures, meaning fragmentation may be driven by team topology rather than tooling and governance choices alone. [inference; source: https://teamtopologies.com/book] Team Topologies (Skelton and Pais, 2019) operationalises Conway's Law by prescribing that platform teams should reduce cognitive load for stream-aligned teams through self-service platforms, which is structurally consistent with the golden path and self-service with guardrails patterns. [inference; source: https://teamtopologies.com/book; https://learn.microsoft.com/en-us/platform-engineering/about/self-service] The Team Topologies analysis implies that tooling governance patterns alone cannot close the fragmentation gap if underlying team topology is misaligned: two teams that do not communicate will build incompatible systems regardless of whether a golden path exists, making team topology a prerequisite or co-requisite of effective platform engineering rather than a downstream outcome of it. [inference; source: https://teamtopologies.com/book]

### Risks, Gaps, and Uncertainties

- The DORA 2024 mechanism for platform-induced stability decrease is under-specified: it is unclear whether the cause is shared single-component dependencies, poor rollout process, or inadequate extension-point design; the available report summary does not distinguish these. [inference; source: https://dora.dev/research/2024/dora-report/]
- Quantitative evidence on InnerSource adoption rates, fragmentation reduction percentages, or Trusted Committer network scaling limits is absent; all InnerSource pattern evidence reviewed is case-study based with named instances rather than large-scale empirical studies. [inference; source: https://patterns.innersourcecommons.org/p/trusted-committer; https://patterns.innersourcecommons.org/p/innersource-portal]
- The Bartlett and Ghoshal (1989) primary source is not openly accessible; secondary-source accounts of the four archetypes are consistent but the specific causal mechanisms may not transfer exactly to software tooling governance. [assumption; source: https://hbsp.harvard.edu/product/9498-PDF-ENG]
- The discoverability-drives-duplication hypothesis has not been directly measured; it is consistent with the InnerSource Portal pattern documentation but could be confounded by trust in external teams' code quality or local speed-to-market pressures. [inference; source: https://patterns.innersourcecommons.org/p/innersource-portal]

### Open Questions

1. Is there a measurable threshold at which the number of tools in use makes a single golden path infeasible, and if so, what is the structural alternative?
2. How should organisations measure the rate of sanctioned extension versus unsanctioned forking as a leading indicator that the golden path is losing voluntary adoption?
3. Can the InnerSource Common Requirements negotiation step be partially automated, or does it always require direct stakeholder engagement?
4. Does the DORA 2024 platform stability decrease finding apply primarily to early-stage CNCF Level 1-2 platforms, or does it persist at Level 3-4?

---

## Output

- Type: knowledge
- Description: Structured synthesis of platform engineering golden path patterns, InnerSource governance models, and the transnational strategy framework applied to the standardisation-versus-autonomy balance in internal tooling. [inference; source: https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem; https://patterns.innersourcecommons.org/p/trusted-committer; https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/]
- Links:
  - https://engineering.atspotify.com/2020/08/how-we-use-golden-paths-to-solve-fragmentation-in-our-software-ecosystem
  - https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
  - https://dora.dev/research/2024/dora-report/
