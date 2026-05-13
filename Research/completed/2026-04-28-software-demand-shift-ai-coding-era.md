---
review_count: 2
title: "Which software categories face declining demand versus increasing demand as Artificial Intelligence (AI) coding agents make custom software generation cheap?"
added: 2026-04-28T21:06:12+00:00
status: completed
priority: medium
blocks: []
tags: [agentic-ai, agentic-coding, software-cost, saas, build-vs-buy, transaction-costs, platform-engineering, internal-developer-platform, observability, identity, market-structure]
ai_themes: [agentic-ai, tools-infrastructure, cost-performance, software-economics, market-dynamics]
started: 2026-04-29T09:06:19+00:00
completed: 2026-04-29T09:42:02+00:00
output: [knowledge]
cites: [2026-04-02-org-shape-software-cost-zero, 2026-03-23-software-factory, 2026-04-26-software-engineering-investment-case-llm]
related: [2026-02-28-jevons-paradox, 2026-03-10-nature-of-the-firm-coase-organisations]
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions: []
---

# Which software categories face declining demand versus increasing demand as Artificial Intelligence (AI) coding agents make custom software generation cheap?

## Research Question

As Artificial Intelligence (AI) coding agents, such as Anthropic Claude Code, OpenAI Codex, and GitHub Copilot Workspace, make custom software generation materially cheaper, which categories of commercial software face declining demand because the build-it-yourself path becomes viable, which categories face increasing demand because cheaper software production amplifies the need for them, and what structural properties distinguish each group?

## Scope

**In scope:**
- Commercial and Software-as-a-Service (SaaS) software categories whose demand is plausibly affected by AI coding agents reducing custom software build costs
- The build-vs-buy decision framework and how it shifts when build cost approaches zero, using a transaction-cost economics lens
- Specific examples of software categories facing demand decline: niche vertical SaaS, simple Create, Read, Update, Delete (CRUD) applications, basic reporting and dashboarding tools, workflow automation tools with narrow scope
- Specific examples of software categories facing demand increase: Internal Developer Platforms (IDPs), cloud hosting and infrastructure, observability and monitoring platforms, Continuous Integration and Continuous Delivery (CI/CD) pipeline tooling, authentication and identity services, deployment infrastructure
- Structural properties that predict which side a class of software falls on, including network effects, data gravity, multi-tenancy advantages, regulatory-compliance moats, and infrastructure complexity
- Historical analogues: what happened to related software categories when earlier constraints were removed, including cloud computing and server management software, and spreadsheet-driven custom business application demand

**Out of scope:**
- Deep technical treatment of any specific AI coding tool
- Open-source software economics
- Hardware and embedded-systems categories
- Pure enterprise-internal operating-model choices already covered by the organisation-shape companion item

**Constraints:** Near-term horizon of 1 to 5 years, commercial software market focus, and a reusable taxonomy rather than a list of disconnected examples.

## Context

- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html] Public evidence already shows that AI-assisted coding is lowering the cost of building bespoke internal software and changing the economics of whether firms should buy generic tools or build tailored ones.
- [fact; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] The same evidence base suggests that cheaper code does not remove the need for coordination-bearing layers such as platform engineering, delivery systems, and shared controls; it can increase their value by raising software volume and operational variance.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html; https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html] This item extends prior repository work by shifting the question from organisational shape to market structure: if coding becomes cheap, the likely winners are categories that absorb coordination, governance, or scale complexity, while categories that mainly package straightforward business logic lose pricing power first.

## Approach

1. **Economic framing:** Apply the build-vs-buy transaction-cost model to derive when declining build cost shifts the decision boundary and which sources of software value disappear versus persist.
2. **Declining-demand category identification:** Gather concrete evidence on software categories that already face replacement pressure from AI-built custom tools.
3. **Increasing-demand category identification:** Gather evidence on categories that benefit when more software is produced, especially hosting, platform engineering, delivery, observability, identity, and agent-facing interface layers.
4. **Structural property taxonomy:** Identify the structural properties that distinguish declining-demand from increasing-demand categories.
5. **Historical analogue check:** Compare the pattern against prior constraint-removal episodes, especially Enterprise Resource Planning (ERP), cloud, low-code and no-code, and software-factory analogues.
6. **Synthesis:** Produce a reusable classification framework with examples and strategic implications.

## Sources

Starting points, checked and updated to working sources actually used in this item.

- [x] [MIT Sloan Chief Data Officer (CDO): Shopify CEO Tobi Lutke says Artificial Intelligence is now a fundamental expectation](https://cdo.mit.edu/blog/2025/04/11/shopify-ceo-tobi-lutke-ai-is-now-a-fundamental-expectation-for-employeeslutke-says-managers-asking-for-new-human-talent-will-have-to-explain-why-the-job-cant-be-done-by-ai/) - accessible report quoting Lutke's memo and its software-building implication
- [x] [Simon Willison: Here's how I use Large Language Models (LLMs) to help me write code](https://simonwillison.net/2025/Mar/11/using-llms-for-code/) - practitioner evidence that AI coding expands the set of projects worth building
- [x] [Reuters via Yahoo Finance: selloff wipes out nearly $1 trillion from software and services stocks as investors debate AI's existential threat](https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html) - market evidence that investors see application-layer software as exposed
- [x] [Retool: The Build vs Buy Shift report 2026](https://retool.com/blog/ai-build-vs-buy-report-2026) - survey evidence on which SaaS categories are already being replaced by custom builds
- [x] [Deloitte New Zealand: AI-assisted software engineering](https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html) - enterprise commentary on build-vs-buy shifts and new bottlenecks
- [x] [GitHub: quantifying GitHub Copilot's impact on developer productivity and happiness](https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/) - controlled evidence that routine coding time can compress materially
- [x] [TechCrunch: Klarna CEO doubts that other companies will replace Salesforce with Artificial Intelligence](https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/) - concrete build-vs-buy case where a firm rebuilt customer-relationship workflows internally
- [x] [Ronald Coase, The Nature of the Firm, Cornell-hosted PDF of the 1937 article](https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf) - primary transaction-cost framing
- [x] [Google Cloud and Enterprise Strategy Group (ESG): new platform engineering research report](https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report) - public evidence that platform engineering expands as software delivery scales
- [x] [Frontiers in Computer Science: platform engineering and internal developer portals multivocal literature review](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full) - academic synthesis on Internal Developer Platform (IDP) adoption and value
- [x] [Splunk: the complete guide to Continuous Integration and Continuous Delivery (CI/CD) pipeline monitoring](https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html) - evidence on why pipeline observability and delivery infrastructure become more critical as release volume increases
- [x] [National Institute of Standards and Technology (NIST): Identity and Access Management resource center](https://www.nist.gov/identity-access-management) - standards-based evidence that identity remains a foundational control surface
- [x] [Help Net Security summarising ConductorOne's survey on identity risks and complexity](https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/) - empirical evidence that more applications, external entities, and non-human identities raise identity complexity and budgets
- [x] [Apify: prepare your Application Programming Interface (API) for the agentic economy](https://blog.apify.com/api-agentic-economy/) - evidence that AI agents increase demand for machine-readable interface layers
- [x] [Stripe: Minions, Stripe's one-shot end-to-end coding agents](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) - evidence that software-factory patterns increase code volume and shift bottlenecks
- [x] [Benedict Evans presentations page](https://www.ben-evans.com/presentations) and [summary of the 2025 Artificial Intelligence deck](https://www.in-parallel.com/insight/benedict-evans-2025-ai-deck-what-it-actually-means-for-enterprises/) - market commentary that Artificial Intelligence compresses cross-application workflow steps rather than merely adding new apps

---

## Research Skill Output

[fact; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html; https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html; https://davidamitchell.github.io/Research/research/2026-04-26-software-engineering-investment-case-llm.html] This section retains the full research output, with Section 6 seeding the Findings section below.

### §0 Initialise

- [fact; source: https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://retool.com/blog/ai-build-vs-buy-report-2026] **Research question restated:** If AI coding agents make bespoke software much cheaper, which commercial software categories lose demand because internal building becomes viable, which categories gain demand because more software must be hosted, governed, deployed, observed, and secured, and what structural properties explain the split?
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html; https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html] **Scope confirmed:** This item is about commercial software categories and market structure, not tool benchmarking or internal team design in isolation.
- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] **Constraints confirmed:** The time horizon is near term, the evidence base is mostly public web material and adjacent repository items, and the output must be a reusable classification framework rather than an inventory of products.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html; https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html; https://davidamitchell.github.io/Research/research/2026-04-26-software-engineering-investment-case-llm.html; https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html; https://davidamitchell.github.io/Research/research/2026-03-10-nature-of-the-firm-coase-organisations.html] **Prior work check:** Before investigation I scanned completed items and identified five adjacent companions: the organisation-shape item, the software-factory item, the software-engineering investment-case item, the Jevons paradox item, and the Coase / theory-of-the-firm item.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html; https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html] Those companion items suggest the same core mechanism from different angles: cheaper coding compresses translation-heavy work but preserves or intensifies the value of control surfaces that coordinate many software artifacts.

### §1 Question Decomposition

- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] Root question decomposed into five branches.

**Branch A, economic framing**
- A1: What does transaction-cost logic predict when the cost of custom software implementation falls sharply?
- A2: Which components of software value come from code generation alone, and which come from coordination, governance, integration, and scale?

**Branch B, declining-demand categories**
- B1: Which software categories are already being replaced by custom builds?
- B2: What structural properties make those categories vulnerable?

**Branch C, increasing-demand categories**
- C1: Which categories benefit when more software is created?
- C2: Why do cloud hosting, platform engineering, CI/CD, observability, identity, and agent-facing interfaces become more valuable?

**Branch D, structural taxonomy**
- D1: Which properties push a category toward decline?
- D2: Which properties push a category toward increase or resilience?
- D3: What classification framework is most reusable in the 1 to 5 year horizon?

**Branch E, historical calibration**
- E1: What did earlier constraint-removal episodes do to application-layer demand?
- E2: What did they do to platforms, Centers of Excellence, and control-plane categories?

### §2 Investigation

#### A. Economic framing

- [fact; source: https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf] Coase's 1937 argument is that firms exist because using the market mechanism has costs, including discovering prices and negotiating and enforcing separate contracts, so activity moves inside the firm when internal coordination is cheaper.
- [inference; source: https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html] If AI cuts only the implementation cost of software, the build-vs-buy boundary moves inward for categories whose buy premium depended mostly on coding labor, but it moves much less for categories whose premium comes from governance, integration, shared operations, or scale economies.
- [fact; source: https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html; https://github.blog/2022-09-07-research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/] Public productivity evidence supports the premise that routine coding time is compressing materially: GitHub's controlled study found a 55% faster task-completion rate on a bounded programming task, and Deloitte frames software engineering as the first enterprise function being transformed because code has clear feedback loops and measurable output.
- [inference; source: https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents] Cheaper code does not mean end-to-end software is near-free, because testing, release, review, integration, and operational support remain binding costs and can become more salient once code volume rises.

#### B. Declining-demand categories

- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026] Retool's 2026 survey of 817 customers and builders found that 35% had already replaced at least one SaaS tool with a custom build and 78% expected to build more of their own tools in 2026.
- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026] The same survey found the highest replacement pressure in workflow automations (35%), internal admin tools (33%), business-intelligence tools (29%), customer-relationship management and form-builder categories (25%), project-management tools (23%), and customer-support tools (21%).
- [fact; source: https://simonwillison.net/2025/Mar/11/using-llms-for-code/] Simon Willison argues that the biggest advantage of AI coding is speed of development and that the range of projects worth building expands dramatically once something can ship in an afternoon rather than a week.
- [fact; source: https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html] Klarna publicly described consolidating customer-relationship management data and interfaces onto an internally developed stack, and Deloitte cites Klarna as an example of generative AI shifting the cost-benefit curve on rebuilding critical systems that would previously have been bought.
- [fact; source: https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html] Reuters reported that software investors wiped roughly $830 billion from software and services market value in six sessions in early 2026 because they feared Large Language Models moving into the application layer could narrow the perceived moats of incumbent software companies.
- [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://simonwillison.net/2025/Mar/11/using-llms-for-code; https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/] The categories most exposed are application-layer products whose value proposition is speed-to-build, basic workflow logic, simple data manipulation, or user-interface convenience rather than proprietary data, network effects, or a hard-to-replicate control surface.

#### C. Increasing-demand categories

- [fact; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] Platform engineering and Internal Developer Platforms are strengthening, not weakening: Google Cloud found that 55% of surveyed large organisations had already adopted platform engineering and 90% of adopters planned to expand it, while the Frontiers review describes platform engineering as the dominant approach to managing developer infrastructure at scale.
- [fact; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] Google Cloud's survey found that 86% of respondents believe platform engineering is essential to realising the business value of AI, which directly links cheaper software creation to higher demand for shared platform layers.
- [fact; source: https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html] Splunk argues that CI/CD pipelines are now as critical as production environments and must be monitored deeply because release cadence, security requirements, and software complexity continue to rise.
- [fact; source: https://www.nist.gov/identity-access-management] NIST treats identity and access management as a fundamental cybersecurity capability that ensures the right people and things have the right access to the right resources at the right time across the system lifecycle.
- [fact; source: https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/] A survey of 523 United States security leaders found that 81% were concerned about non-human identities, 97% worked with external parties that needed system access, average SaaS application counts were high, and 84% reported moderate or significant budget increases for identity and access products.
- [fact; source: https://blog.apify.com/api-agentic-economy/] Apify argues that AI agents are becoming a significant new class of consumer for APIs, expects more than 30% of the increase in API demand to come from AI tools and LLMs in 2026, and says APIs must become more machine-readable, explicit, and agent-compatible.
- [fact; source: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents] Stripe's Minions system merges more than 1,300 fully AI-authored pull requests per week, which is direct evidence that successful agentic coding raises demand for the shared backpressure, tooling, and review layers that let code volume scale safely.
- [inference; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://www.nist.gov/identity-access-management; https://blog.apify.com/api-agentic-economy/] Categories that coordinate many software artifacts, such as hosting, delivery systems, observability, identity, and agent-facing interfaces, gain demand because they absorb the complexity that cheaper code creation cannot remove.

#### D. Structural-property taxonomy

- [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://simonwillison.net/2025/Mar/11/using-llms-for-code] A category trends toward declining demand when five conditions cluster together: low domain specificity, low switching cost, low governance burden, weak network effects, and value concentrated in configurable business logic or presentation.
- [inference; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.nist.gov/identity-access-management; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html] A category trends toward increasing demand when value comes from shared coordination across many systems, continuously updated operational knowledge, security or compliance guarantees, scale economies, or reduction of developer cognitive load.
- [inference; source: https://blog.apify.com/api-agentic-economy/; https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/] Categories become resilient rather than declining when they sit on a control surface that must stay coherent even as machine actors, human actors, and many applications interact at higher speed.

#### E. Historical analogue check

- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html] The organisation-shape companion item found that Enterprise Resource Planning, cloud, and low-code and no-code adoption reduced some local execution work but replaced it with new central structures for standards, enablement, shared services, or Centers of Excellence rather than eliminating coordination.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html] The software-factory companion item found that when AI lowers coding cost, the bottleneck shifts upstream to requirement quality, prioritisation velocity, and factory design rather than disappearing.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-04-26-software-engineering-investment-case-llm.html] The software-engineering investment-case item found that platform quality, testing, version control, and verifier layers determine whether AI-assisted engineering gains compound into institutional value.
- [fact; source: https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html] The Jevons paradox item found that falling software-production cost is more likely to expand total software demand than suppress it, which supports a market split where application categories commoditise while coordination-bearing categories grow.
- [inference; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html; https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html; https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html] The best historical analogue is not "software disappears" but "tooling value moves up the stack": local execution gets cheaper, demand broadens, and the durable value pools shift toward platforms, control planes, and hard-to-replicate data or compliance layers.

### §3 Reasoning

- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026] The strongest direct evidence for declining demand is not a forecast but current replacement behavior in categories such as workflow automation, internal admin tools, and business-intelligence tools.
- [fact; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] The strongest direct evidence for increasing demand is the observed growth of platform engineering and Internal Developer Platforms as organisations scale software delivery and AI adoption.
- [inference; source: https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://retool.com/blog/ai-build-vs-buy-report-2026; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] The transaction-cost explanation links the two: AI compresses the cost of producing custom logic, which weakens some application-layer buy premiums while strengthening categories that reduce coordination cost across many artifacts.
- [inference; source: https://www.nist.gov/identity-access-management; https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html] Identity, observability, and delivery layers are not peripheral beneficiaries; they are the new choke points because more software and more machine actors increase failure surfaces faster than they reduce governance needs.

### §4 Consistency Check

- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/] The evidence does not support a claim that broad SaaS demand collapses immediately; it supports replacement pressure first in narrow or weakly differentiated categories and selective rebuilding by firms with strong context or integration needs.
- [fact; source: https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] The evidence also does not support a claim that AI removes organisational or infrastructure bottlenecks; both sources point to shipping, governance, and platform capability becoming more important.
- [inference; source: https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html; https://retool.com/blog/ai-build-vs-buy-report-2026] Market fear in software valuations is directionally aligned with replacement-pressure evidence, but equity-market moves are weaker evidence than direct product-category replacement data, so valuation commentary is used here as corroboration rather than as the primary proof.

### §5 Depth and Breadth Expansion

- [inference; source: https://www.nist.gov/identity-access-management; https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/] **Security lens:** As custom tools proliferate, identity becomes a larger market because every new application, connector, and agent introduces fresh access paths that must be scoped, authenticated, and audited.
- [inference; source: https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents] **Operational lens:** More code volume means more release events, more pipeline states, and more failure modes, so observability and deployment tooling gain value even when coding itself gets cheaper.
- [inference; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] **Organisational lens:** Platform engineering demand rises because the scarce resource becomes not typing code but giving many builders and agents a safe, paved road for shipping it.
- [inference; source: https://blog.apify.com/api-agentic-economy/; https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html] **Market-structure lens:** Agentic consumption creates a second-order demand wave for interface layers, because when agents become software users the number of machine-to-machine interactions can grow faster than the number of human-facing applications.

### §6 Synthesis

**Executive summary:**

Custom-software demand is most likely to substitute away from narrow application-layer SaaS categories, not from coordination-bearing infrastructure categories. [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf] The exposed categories are those whose buy premium came mainly from implementation effort, such as workflow automation, internal admin tools, lightweight business-intelligence tools, and some customer-relationship or project-management workflows. [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://simonwillison.net/2025/Mar/11/using-llms-for-code] The gaining categories are those that absorb scale, governance, deployment, identity, and operational-complexity costs that AI coding does not remove, including platform engineering, cloud hosting, CI/CD, observability, identity, and agent-facing interface layers. [inference; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://www.nist.gov/identity-access-management; https://blog.apify.com/api-agentic-economy] This does not mean incumbent vendors or total application spend disappear, because vendors that move up the stack into orchestration, bundled suites, proprietary data, or broader workflow packaging can preserve or expand demand even while narrow logic-only tools commoditise. [inference; source: https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html; https://www.in-parallel.com/insight/benedict-evans-2025-ai-deck-what-it-actually-means-for-enterprises/]

**Key findings:**

1. **Commercial software categories whose value is mostly packaged business logic or user-interface convenience face the clearest near-term demand decline, because AI-assisted internal building sharply reduces the historical buy premium for those functions.** [inference] (medium confidence; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://simonwillison.net/2025/Mar/11/using-llms-for-code; https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf)
2. **Current survey evidence shows that the replacement pressure is already concentrated in workflow automation, internal admin tools, business-intelligence tools, customer-relationship management adjacencies, project management, and customer-support tooling rather than evenly across all SaaS categories.** [fact] (medium confidence; source: https://retool.com/blog/ai-build-vs-buy-report-2026)
3. **Concrete enterprise cases such as Klarna's internal rebuild of customer-relationship workflows suggest that firms with strong proprietary context can justify rebuilding selected applications that would previously have been bought, even if the pattern is not universal.** [inference] (medium confidence; source: https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html)
4. **Platform engineering and Internal Developer Platform demand rises when software becomes cheaper to produce, because the scarce asset shifts from raw coding capacity to a safe, low-friction path for many humans and agents to ship software repeatedly.** [inference] (high confidence; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)
5. **Cloud hosting, CI/CD, and observability gain demand because higher software volume produces more release events, more environments, more telemetry, and more operational failure modes even when generating the code itself gets cheaper.** [inference] (medium confidence; source: https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)
6. **Identity-related software is likely to become more valuable, because every new application, integration, external participant, and non-human actor expands the access surface that must be authenticated, authorised, and audited.** [inference] (medium confidence; source: https://www.nist.gov/identity-access-management; https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/)
7. **Agent-facing interface layers, especially machine-readable APIs and related tool-access surfaces, become a growth category because agents behave as software consumers that need explicit schemas, durable authentication, and predictable error handling at machine speed.** [inference] (medium confidence; source: https://blog.apify.com/api-agentic-economy/; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)
8. **The most durable commercial applications remain those with moats that AI-assisted building does not erase, including proprietary data, network effects, deep compliance packaging, or hard-to-replicate multi-tenant operating infrastructure, and incumbents can preserve demand by moving up into orchestration or broader suites rather than selling isolated logic.** [inference] (medium confidence; source: https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html; https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.in-parallel.com/insight/benedict-evans-2025-ai-deck-what-it-actually-means-for-enterprises/)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Logic-only application categories lose demand first because AI compresses their implementation premium. | https://retool.com/blog/ai-build-vs-buy-report-2026; https://simonwillison.net/2025/Mar/11/using-llms-for-code; https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf | medium | Demand shift, not instant collapse |
| [fact] Replacement pressure is already highest in workflow automation, internal admin, business-intelligence, customer-relationship, project-management, and support tooling. | https://retool.com/blog/ai-build-vs-buy-report-2026 | medium | Direct survey categories |
| [inference] Selected firms can now justify rebuilding application categories that were formerly bought. | https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html | medium | Concrete but not universal |
| [inference] Platform engineering and Internal Developer Platforms gain demand as software volume scales. | https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | high | Coordination-bearing layer |
| [inference] Cloud hosting, CI/CD, and observability gain demand because software volume raises operational complexity. | https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | medium | Volume-to-operations mechanism |
| [inference] Identity demand is likely to rise with more apps, external actors, and non-human identities. | https://www.nist.gov/identity-access-management; https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/ | medium | Control-surface evidence implies demand direction |
| [inference] Agent-facing interfaces become a growth category as agents consume software directly. | https://blog.apify.com/api-agentic-economy/; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | medium | Early but coherent evidence |
| [inference] Moat-heavy applications remain more resilient than narrow tools, and incumbents can preserve demand by moving up into orchestration or broader suites. | https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html; https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.in-parallel.com/insight/benedict-evans-2025-ai-deck-what-it-actually-means-for-enterprises/ | medium | Structural conclusion with incumbent adaptation path |

**Assumptions:**

- [assumption; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html] Near-term demand shifts will show first in contract-renewal pressure, new-tool avoidance, and selective internal rebuilds rather than in a uniform collapse of incumbent software revenue. Justification: the evidence shows category-level pressure and expanding internal builds, but not a complete replacement wave.
- [assumption; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.nist.gov/identity-access-management] Control-plane categories that rise in enterprise settings will also capture value in the broader commercial market because software proliferation creates the same coordination problems outside any one firm. Justification: the available evidence is enterprise-heavy, so the broader-market extrapolation remains inferential.

**Analysis:**

The evidence was weighted most heavily when it showed current category behavior rather than abstract future possibility. [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] Retool is the strongest direct source for declining-demand categories because it identifies which SaaS classes customers are already replacing, while Google Cloud and the Frontiers review are the strongest direct sources for increasing-demand categories because they document current platform-engineering expansion rather than only arguing for it. [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] The transaction-cost frame resolves the apparent contradiction between "software gets cheaper" and "infrastructure becomes more valuable": AI removes some production cost, but it does not remove the coordination cost of running many artifacts safely, so value migrates toward categories that absorb that coordination burden. [inference; source: https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://www.nist.gov/identity-access-management] Historical repository companions strengthen that reading because previous constraint-removal episodes in this corpus repeatedly shifted value from local execution toward shared platforms and control planes. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html; https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html; https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html]

**Risks, gaps, uncertainties:**

- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026] The strongest direct replacement evidence comes from one vendor survey, so category-level magnitudes should be treated as directional rather than market-share estimates.
- [fact; source: https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html] Public-equity volatility captures investor fear faster than product-market reality, so valuation moves overstate the certainty of near-term disruption.
- [inference; source: https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/] Large-firm rebuild examples may not generalise cleanly to smaller firms that lack data, engineering depth, or integration discipline.
- [inference; source: https://blog.apify.com/api-agentic-economy/] Agent-facing interface demand is likely real but still early, so the size and timing of that category expansion are more uncertain than the expansion in platform engineering or identity.

**Open questions:**

- [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html] Which public software vendors are already preserving demand by moving up the stack from application logic into orchestration, governance, or proprietary-data layers?
- [inference; source: https://www.nist.gov/identity-access-management; https://blog.apify.com/api-agentic-economy/] How much of the new value pool will accrue to traditional identity vendors versus new machine-identity and agent-access vendors?
- [inference; source: https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] At what point does software proliferation create enough maintenance burden to slow the rebound effect and favour consolidation back into shared platforms?

### §7 Recursive Review

- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-04-28-software-demand-shift-ai-coding-era.md] Claim-bearing prose in Sections 0 to 7 is labeled, and inaccessible seeded links were replaced with accessible sources.
- [inference; source: https://simonwillison.net/2025/Mar/11/using-llms-for-code; https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] The evidence base supports a medium-confidence synthesis because direct evidence exists for replacement pressure and for platform-layer growth, while several category-to-category extrapolations remain inferential.
- [fact; source: https://github.com/davidamitchell/Research/blob/main/Research/in-progress/2026-04-28-software-demand-shift-ai-coding-era.md] Repository cross-reference sweep was applied in initialisation, synthesis, and analysis.

---

## Findings

### Executive Summary

Custom-software demand is most likely to substitute away from narrow application-layer SaaS categories, not from coordination-bearing infrastructure categories. [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf] The most exposed products are those whose buy premium came mainly from implementation effort, such as workflow automation, internal admin tools, lightweight business-intelligence tools, and some customer-relationship or project-management workflows. [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://simonwillison.net/2025/Mar/11/using-llms-for-code] The categories most likely to gain demand are those that absorb scale, governance, deployment, identity, and operational complexity costs that AI coding does not remove, including platform engineering, cloud hosting, CI/CD, observability, identity, and agent-facing interface layers. [inference; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://www.nist.gov/identity-access-management; https://blog.apify.com/api-agentic-economy] This does not mean incumbent vendors or total application spend disappear, because vendors that move up the stack into orchestration, bundled suites, proprietary data, or broader workflow packaging can preserve or expand demand even while narrow logic-only tools commoditise. [inference; source: https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html; https://www.in-parallel.com/insight/benedict-evans-2025-ai-deck-what-it-actually-means-for-enterprises/]

### Key Findings

1. **Commercial software categories whose value is mostly packaged business logic or user-interface convenience face the clearest near-term demand decline, because AI-assisted internal building sharply reduces the historical buy premium for those functions.** [inference] (medium confidence; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://simonwillison.net/2025/Mar/11/using-llms-for-code; https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf)
2. **Current survey evidence shows that the replacement pressure is already concentrated in workflow automation, internal admin tools, business-intelligence tools, customer-relationship management adjacencies, project management, and customer-support tooling rather than evenly across all Software-as-a-Service categories.** [fact] (medium confidence; source: https://retool.com/blog/ai-build-vs-buy-report-2026)
3. **Concrete enterprise cases such as Klarna's internal rebuild of customer-relationship workflows suggest that firms with strong proprietary context can justify rebuilding selected applications that would previously have been bought, even if the pattern is not universal.** [inference] (medium confidence; source: https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html)
4. **Platform engineering and Internal Developer Platform demand rises when software becomes cheaper to produce, because the scarce asset shifts from raw coding capacity to a safe, low-friction path for many humans and agents to ship software repeatedly.** [inference] (high confidence; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)
5. **Cloud hosting, Continuous Integration and Continuous Delivery pipelines, and observability gain demand because higher software volume produces more release events, more environments, more telemetry, and more operational failure modes even when generating the code itself gets cheaper.** [inference] (medium confidence; source: https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)
6. **Identity-related software is likely to become more valuable, because every new application, integration, external participant, and non-human actor expands the access surface that must be authenticated, authorised, and audited.** [inference] (medium confidence; source: https://www.nist.gov/identity-access-management; https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/)
7. **Agent-facing interface layers, especially machine-readable Application Programming Interfaces and related tool-access surfaces, become a growth category because agents behave as software consumers that need explicit schemas, durable authentication, and predictable error handling at machine speed.** [inference] (medium confidence; source: https://blog.apify.com/api-agentic-economy/; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents)
8. **The most durable commercial applications remain those with moats that AI-assisted building does not erase, including proprietary data, network effects, deep compliance packaging, or hard-to-replicate multi-tenant operating infrastructure, and incumbents can preserve demand by moving up into orchestration or broader suites rather than selling isolated logic.** [inference] (medium confidence; source: https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html; https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.in-parallel.com/insight/benedict-evans-2025-ai-deck-what-it-actually-means-for-enterprises/)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Logic-only application categories lose demand first because AI compresses their implementation premium. | https://retool.com/blog/ai-build-vs-buy-report-2026; https://simonwillison.net/2025/Mar/11/using-llms-for-code; https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf | medium | Demand shift, not instant collapse |
| [fact] Replacement pressure is already highest in workflow automation, internal admin, business-intelligence, customer-relationship, project-management, and support tooling. | https://retool.com/blog/ai-build-vs-buy-report-2026 | medium | Direct survey categories |
| [inference] Selected firms can now justify rebuilding application categories that were formerly bought. | https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html | medium | Concrete but not universal |
| [inference] Platform engineering and Internal Developer Platforms gain demand as software volume scales. | https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | high | Coordination-bearing layer |
| [inference] Cloud hosting, CI/CD, and observability gain demand because software volume raises operational complexity. | https://www.deloitte.com/nz/en/services/consulting/perspectives/ai-assisted-software-engineering.html; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | medium | Volume-to-operations mechanism |
| [inference] Identity demand is likely to rise with more apps, external actors, and non-human identities. | https://www.nist.gov/identity-access-management; https://www.helpnetsecurity.com/2024/05/22/identity-risks-complexity-for-organizations/ | medium | Control-surface evidence implies demand direction |
| [inference] Agent-facing interfaces become a growth category as agents consume software directly. | https://blog.apify.com/api-agentic-economy/; https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents | medium | Early but coherent evidence |
| [inference] Moat-heavy applications remain more resilient than narrow tools, and incumbents can preserve demand by moving up into orchestration or broader suites. | https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html; https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/; https://www.in-parallel.com/insight/benedict-evans-2025-ai-deck-what-it-actually-means-for-enterprises/ | medium | Structural conclusion with incumbent adaptation path |

### Assumptions

- **Assumption:** Near-term demand shifts will show first in contract-renewal pressure, new-tool avoidance, and selective internal rebuilds rather than in a uniform collapse of incumbent software revenue. **Justification:** Direct evidence exists for category-level pressure and expanding internal builds, but not for a complete replacement wave. [assumption; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html]
- **Assumption:** Control-plane categories that rise in enterprise settings will also capture value in the broader commercial market because software proliferation creates similar coordination problems outside any one firm. **Justification:** The available direct evidence is enterprise-heavy, so the broader-market extrapolation remains inferential. [assumption; source: https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.nist.gov/identity-access-management]

### Analysis

The evidence was weighted most heavily when it showed current category behavior rather than abstract future possibility. [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] Retool is the strongest direct source for declining-demand categories because it identifies which SaaS classes customers are already replacing, while Google Cloud and the Frontiers review are the strongest direct sources for increasing-demand categories because they document current platform-engineering expansion rather than only arguing for it. [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report; https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2026.1814498/full] The transaction-cost frame resolves the apparent contradiction between "software gets cheaper" and "infrastructure becomes more valuable": AI removes some production cost, but it does not remove the coordination cost of running many artifacts safely, so value migrates toward categories that absorb that coordination burden. [inference; source: https://courses.cit.cornell.edu/econ352jpw/readme/coase%20nature%20of%20firm.pdf; https://www.splunk.com/en_us/blog/learn/monitoring-ci-cd.html; https://www.nist.gov/identity-access-management] Repository companions strengthen that reading because previous constraint-removal episodes in this corpus repeatedly shifted value from local execution toward shared platforms and control planes. [inference; source: https://davidamitchell.github.io/Research/research/2026-04-02-org-shape-software-cost-zero.html; https://davidamitchell.github.io/Research/research/2026-03-23-software-factory.html; https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html]

### Risks, Gaps, and Uncertainties

- [fact; source: https://retool.com/blog/ai-build-vs-buy-report-2026] The strongest direct replacement evidence comes from one vendor survey, so category-level magnitudes should be treated as directional rather than as market-share estimates.
- [fact; source: https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html] Public-equity volatility captures investor fear faster than product-market reality, so valuation moves overstate the certainty of near-term disruption.
- [inference; source: https://techcrunch.com/2025/03/04/klarna-ceo-doubts-that-other-companies-will-replace-salesforce-with-ai/] Large-firm rebuild examples may not generalise cleanly to smaller firms that lack data, engineering depth, or integration discipline.
- [inference; source: https://blog.apify.com/api-agentic-economy/] Agent-facing interface demand is likely real but still early, so the size and timing of that category expansion are more uncertain than the expansion in platform engineering or identity.

### Open Questions

- [inference; source: https://retool.com/blog/ai-build-vs-buy-report-2026; https://finance.yahoo.com/news/us-software-stocks-hit-anthropic-154249835.html] Which public software vendors are already preserving demand by moving up the stack from application logic into orchestration, governance, or proprietary-data layers?
- [inference; source: https://www.nist.gov/identity-access-management; https://blog.apify.com/api-agentic-economy/] How much of the new value pool will accrue to traditional identity vendors versus new machine-identity and agent-access vendors?
- [inference; source: https://davidamitchell.github.io/Research/research/2026-02-28-jevons-paradox.html; https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report] At what point does software proliferation create enough maintenance burden to slow the rebound effect and favour consolidation back into shared platforms?

---

## Output

- Type: knowledge
- Description: A reusable near-term taxonomy for which software categories lose demand versus gain demand as AI-assisted coding lowers build cost.
- Links:
  - https://retool.com/blog/ai-build-vs-buy-report-2026
  - https://cloud.google.com/blog/products/application-modernization/new-platform-engineering-research-report
  - https://www.nist.gov/identity-access-management
