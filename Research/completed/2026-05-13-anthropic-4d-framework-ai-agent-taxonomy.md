---
review_count: 2
title: "What is Anthropic's '4D' framework for Artificial Intelligence (AI) fluency, what are its four components and their definitions, and how does it compare to other published frameworks for taxonomising and compartmentalising AI agent terminology and concepts?"
added: 2026-05-13T21:41:19+00:00
status: completed
priority: medium
blocks: []
tags: [agentic-ai, llm, evaluation, workflow]
started: 2026-05-14T09:56:14+00:00
completed: 2026-05-14T10:19:49+00:00
output: [knowledge]
cites:
  - 2026-03-10-ai-concept-classification-taxonomy
related:
  - 2026-03-02-integrative-framework-agent-decision-making
  - 2026-03-08-ai-coding-harnesses-agent-philosophy
  - 2026-03-10-agent-evaluation-cross-repo-analysis
superseded_by: ~
supersedes: ~
item_type: primary
confidence: medium
versions:
  - version: "1.0"
    sha: "bdf2909d52f3fc049e164750427ba82dcbf99090"
    changed: 2026-05-14
    progress: "progress/2026-05-14-anthropic-4d-framework-ai-agent-taxonomy.md"
    summary: "Initial completion"
---

# What is Anthropic's '4D' framework for Artificial Intelligence (AI) fluency, what are its four components and their definitions, and how does it compare to other published frameworks for taxonomising and compartmentalising AI agent terminology and concepts?

## Research Question

What is Anthropic's "4D" framework for Artificial Intelligence (AI) fluency, what do each of the four Ds, Delegation, Description, Discernment, and Diligence, mean in practice, and how does this framework compare to other published frameworks for taxonomising or compartmentalising AI terminology and concepts, both in scope and in practical design guidance for teams building or governing AI systems?

## Scope

**In scope:**
- Anthropic's 4D framework as presented in the AI Fluency course, Delegation, Description, Discernment, and Diligence, validated from official Anthropic materials
- Published frameworks from other major organisations for categorising AI concepts or systems, including the National Institute of Standards and Technology (NIST) AI Use Taxonomy, the Organisation for Economic Co-operation and Development (OECD) classification framework, Anthropic's workflows-versus-agents distinction, and one contrasting capability taxonomy from Google DeepMind
- Comparison across scope, target audience, granularity, and practical utility
- Practical design and governance guidance each framework provides for practitioners

**Out of scope:**
- Implementation details of specific AI products or models
- Non-agent task taxonomies such as narrow computer vision or Natural Language Processing (NLP) benchmark catalogues
- Legal liability analysis beyond what classification frameworks themselves say
- Exhaustive coverage of every academic AI taxonomy

**Constraints:**
- Prefer primary sources from the named organisations
- Every source must have a verifiable URL
- Focus on frameworks published or updated from 2022 through 2025

## Context

Shared vocabulary reduces coordination cost in human-AI work because classification schemes make it easier to describe activities, system properties, and evaluation needs across teams and domains. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification]

Anthropic presents AI fluency as practical skill in interacting with AI systems effectively, efficiently, ethically, and safely, which makes the 4D model relevant as a working framework for teams even though it is not itself a full system taxonomy. [inference; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf]

## Approach

1. Validate Anthropic's 4D framework from official Anthropic sources.
2. Define each D and its sub-components in practical terms.
3. Compare 4D with at least three other published frameworks that classify AI activities, systems, harms, or capability levels.
4. Evaluate where the frameworks overlap, where they differ, and what each is best for.
5. Produce practical guidance for teams choosing a shared vocabulary for building or governing AI agents.

## Sources

- [x] [Anthropic (n.d.) AI Fluency](https://www.anthropic.com/ai-fluency)
- [x] [Anthropic (2025) The AI Fluency Framework](https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf)
- [x] [Anthropic (2025) AI Fluency key terminology cheat sheet](https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf)
- [x] [Anthropic (2024) Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [x] [Theofanos et al. (2024) AI Use Taxonomy: A Human-Centered Approach](https://doi.org/10.6028/NIST.AI.200-1)
- [x] [OECD (2022) OECD Framework for Classifying AI Systems](https://oecd.ai/en/classification)
- [x] [OECD (2022) OECD Framework for Classifying AI Systems, two-page overview](https://oecd.ai/en/wonk/documents/oecd-framework-for-classifying-ai-systems-two-page-overview)
- [x] [Benbouzid et al. (2024) A Collaborative, Human-Centred Taxonomy of AI, Algorithmic, and Automation Harms](https://arxiv.org/html/2407.01294v2)
- [x] [Morris et al. (2025) Levels of AGI for Operationalizing Progress on the Path to AGI](https://arxiv.org/abs/2311.02462)
- [x] [Mitchell (2026) AI concept classification taxonomy: prompts, instructions, memory, failure modes, controls, and problem domains](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md)
- [x] [Mitchell (2026) AI coding harnesses: agent execution model, memory, and context management across commercial and OSS tools](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md)
- [x] [Mitchell (2026) Agent evaluation framework: cross-repo pattern analysis, commonality detection, and regression identification](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md)
- [x] [Mitchell (2026) An Integrative Framework for Agent Decision-Making](https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-integrative-framework-agent-decision-making.md)

---

## Research Skill Output

### §0 Initialise

- Question: What Anthropic's 4D framework is, how each D works in practice, and how the framework compares with published AI classification frameworks.
- Scope: Anthropic 4D, NIST activity taxonomy, OECD system classification, Anthropic workflows-versus-agents architecture guidance, Benbouzid et al. harms taxonomy, and Google DeepMind's Artificial General Intelligence (AGI) levels as a contrasting capability taxonomy.
- Constraints: primary-source preference, URL-backed citations only, 2022 to 2025 focus.
- Output: full structured synthesis with executive summary, key findings, evidence map, assumptions, analysis, risks, and open questions.
- Prior completed items consulted: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md ; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-02-integrative-framework-agent-decision-making.md
- Direct cross-reference selected for citation: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md

### §1 Question Decomposition

```
What is Anthropic's 4D framework and how does it compare with other AI taxonomies?
|
|-- Q1. What does Anthropic officially say the 4D framework is?
|   |-- Q1a. What is the top-level purpose of the framework?
|   |-- Q1b. What does Delegation mean?
|   |-- Q1c. What does Description mean?
|   |-- Q1d. What does Discernment mean?
|   `-- Q1e. What does Diligence mean?
|
|-- Q2. What practical work does each D correspond to?
|   |-- Q2a. What decisions or actions happen under Delegation?
|   |-- Q2b. What specifications happen under Description?
|   |-- Q2c. What evaluation work happens under Discernment?
|   `-- Q2d. What responsibility and governance work happens under Diligence?
|
|-- Q3. What comparable published frameworks exist?
|   |-- Q3a. How does the NIST AI Use Taxonomy classify AI-related work?
|   |-- Q3b. How does the OECD framework classify AI systems?
|   |-- Q3c. How does Anthropic's workflows-versus-agents framing classify agentic systems?
|   |-- Q3d. How does the collaborative harms taxonomy classify harm categories?
|   `-- Q3e. How does DeepMind's AGI framework classify capability and autonomy?
|
|-- Q4. How do these frameworks differ?
|   |-- Q4a. Which one classifies user competencies?
|   |-- Q4b. Which ones classify system properties or activities?
|   |-- Q4c. Which ones provide design guidance versus governance guidance?
|   `-- Q4d. Which ones are most useful for teams building or governing AI agents?
|
`-- Q5. What synthesis best answers the original question?
    |-- Q5a. Where does 4D fit in the taxonomy landscape?
    `-- Q5b. What framework combination should practitioners use?
```

### §2 Investigation

#### Prior completed-item cross-reference

- **[fact]** The repository's completed item on concept classification organises prompts, memory, failure modes, controls, tools, and problem domains as system concepts, which makes it a concept-first taxonomy rather than a user-competency framework. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md. Source class: prior completed research.
- **[fact]** The completed item on agent evaluation treats shared vocabulary as a prerequisite for comparing agent designs, which makes this 4D item relevant to evaluation only if 4D is paired with a more structural taxonomy. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-agent-evaluation-cross-repo-analysis.md. Source class: prior completed research.
- **[fact]** The completed item on AI coding harnesses already cites Anthropic's workflows-versus-agents distinction as an architecture framing for agentic systems, which makes it a directly adjacent comparison point to 4D. Source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-08-ai-coding-harnesses-agent-philosophy.md. Source class: prior completed research.

#### Anthropic 4D framework

- **[fact]** Anthropic's AI Fluency course page says the course teaches practical skills for effective, efficient, ethical, and safe AI interaction. Source: https://www.anthropic.com/ai-fluency. Source class: primary.
- **[fact]** Anthropic's "The AI Fluency Framework" document defines the 4D framework as "four interconnected competencies necessary to ensure our interactions with AI are effective, efficient, ethical and safe." Source: https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf. Source class: primary.
- **[fact]** The same Anthropic framework document defines Delegation as "setting goals and deciding whether, when and how to engage with AI," Description as "effectively describing goals to prompt useful AI behaviors and outputs," Discernment as "accurately assessing the usefulness of AI outputs and behaviours," and Diligence as "taking responsibility for what we do with AI and how we do it." Source: https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf. Source class: primary.
- **[fact]** Anthropic's framework document presents three modes of AI interaction under Delegation: automation, augmentation, and agency. Source: https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf. Source class: primary.
- **[fact]** Official Anthropic course-page content identifies Delegation's three sub-components as problem awareness, platform awareness, and task delegation. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf. Source class: primary.
- **[fact]** The same Anthropic course-page content defines problem awareness as clarifying goals and success metrics before using AI, platform awareness as understanding different AI capabilities and limitations, and task delegation as dividing work to use human strengths and AI strengths appropriately. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf. Source class: primary.
- **[fact]** Official Anthropic materials identify Description's three sub-components as product description, process description, and performance description. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf. Source class: primary.
- **[fact]** Anthropic's course-page content defines product description as specifying the final result in terms such as length, audience, style, and format; process description as guiding the system's approach, such as step-by-step thinking or multiple perspectives; and performance description as defining the system's behaviour during the interaction, such as acting as a critical editor or supportive brainstormer. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf. Source class: primary.
- **[fact]** Official Anthropic course-page content identifies Discernment's three sub-components as product discernment, process discernment, and performance discernment. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf. Source class: primary.
- **[fact]** Anthropic's course-page content defines product discernment as evaluating the quality of AI outputs, including accuracy, helpfulness, and whether new perspectives are useful; process discernment as examining reasoning and assumptions; and performance discernment as assessing whether the system behaved helpfully in the requested role. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf. Source class: primary.
- **[fact]** Official Anthropic course-page content identifies Diligence's three sub-components as creation diligence, transparency diligence, and deployment diligence. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf. Source class: primary.
- **[fact]** Anthropic's course-page content defines creation diligence as choosing AI systems thoughtfully with privacy, security, and appropriateness in view; transparency diligence as honest disclosure of AI assistance; and deployment diligence as taking ownership of AI-assisted outputs and verifying their appropriateness. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf. Source class: primary.
- **[inference]** The 4D framework is organised around the lifecycle of responsible collaboration with AI, first deciding the human-AI split, then specifying the collaboration, then evaluating the result, and finally accepting responsibility for use and disclosure. Source: https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://www.anthropic.com/ai-fluency. Source class: inference from primary sources.

#### Anthropic workflows-versus-agents comparison

- **[fact]** Anthropic's "Building effective agents" defines agentic systems as the umbrella term and draws an architectural distinction between workflows, where Large Language Models (LLMs) and tools follow predefined code paths, and agents, where LLMs dynamically direct their own processes and tool usage. Source: https://www.anthropic.com/research/building-effective-agents. Source class: primary.
- **[fact]** The same Anthropic post recommends using the simplest solution possible, preferring no agentic system or a workflow before moving to agents when flexibility and model-driven decision-making are actually needed. Source: https://www.anthropic.com/research/building-effective-agents. Source class: primary.
- **[inference]** Anthropic's workflows-versus-agents distinction is a system-architecture classifier, not a fluency model, because it sorts implementations by orchestration pattern rather than by user competencies. Source: https://www.anthropic.com/research/building-effective-agents; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf. Source class: inference from primary sources.

#### NIST AI Use Taxonomy comparison

- **[fact]** NIST's AI Use Taxonomy aims to classify how an AI system contributes to an outcome and sets out 16 AI use activities that are independent of techniques and domains. Source: https://doi.org/10.6028/NIST.AI.200-1. Source class: primary.
- **[fact]** NIST says the taxonomy provides common terminology for describing outcome-based human-AI activities, enables cross-domain insights, highlights common measurement needs, facilitates use-case development, and supports evaluation of trustworthiness and usability. Source: https://doi.org/10.6028/NIST.AI.200-1. Source class: primary.
- **[fact]** The 16 NIST activity types include content creation, content synthesis, decision making, detection, digital assistance, discovery, image analysis, information retrieval/search, monitoring, performance improvement, personalization, prediction, process automation, recommendation, robotic automation, and vehicular automation. Source: https://doi.org/10.6028/NIST.AI.200-1. Source class: primary.
- **[inference]** NIST's taxonomy is broader than 4D because it classifies what AI systems do in human tasks across domains, while 4D classifies what a person must do to collaborate well with AI. Source: https://doi.org/10.6028/NIST.AI.200-1; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf. Source class: inference from primary sources.

#### OECD framework comparison

- **[fact]** The OECD framework classifies AI systems along five dimensions, People and Planet, Economic Context, Data and Input, AI Model, and Task and Output. Source: https://oecd.ai/en/classification; https://oecd.ai/en/wonk/documents/oecd-framework-for-classifying-ai-systems-two-page-overview. Source class: primary.
- **[fact]** OECD positions the framework as a tool for policymakers, regulators, legislators, and others to assess opportunities and risks, support registries or inventories, and inform sector-specific frameworks, risk assessment, incident reporting, and risk management. Source: https://oecd.ai/en/classification; https://oecd.ai/en/wonk/classification. Source class: primary.
- **[inference]** OECD's framework covers governance surfaces that 4D does not attempt to classify, including stakeholders, economic setting, input data characteristics, and model properties. Source: https://oecd.ai/en/classification; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf. Source class: inference from primary sources.

#### Human-centred harms taxonomy comparison

- **[fact]** Benbouzid et al. introduce a collaborative, human-centred taxonomy of AI, algorithmic, and automation harms intended for civil society organisations, educators, policymakers, product teams, and the general public. Source: https://arxiv.org/html/2407.01294v2. Source class: primary.
- **[fact]** The paper says existing taxonomies are often narrow, unclear, and oriented toward practitioners and government, and proposes a clearer, more extensible harms taxonomy built from existing taxonomies, incident repositories, expert review, and public annotation testing. Source: https://arxiv.org/html/2407.01294v2. Source class: primary.
- **[fact]** The proposed harms taxonomy is clustered into nine top-level and sixty-nine sub-categories. Source: https://arxiv.org/html/2407.01294v2. Source class: primary.
- **[inference]** The harms taxonomy is closer to OECD than to 4D in purpose because it helps people classify harms and governance concerns, not collaboration skills. Source: https://arxiv.org/html/2407.01294v2; https://oecd.ai/en/classification; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf. Source class: inference from primary sources.

#### DeepMind capability taxonomy comparison

- **[fact]** Morris et al. propose a framework for classifying the capabilities and behaviour of AGI models and their precursors using levels of performance, generality, and autonomy. Source: https://arxiv.org/abs/2311.02462. Source class: primary.
- **[fact]** The paper states that the framework is intended to provide a common language to compare models, assess risks, and measure progress on the path to AGI. Source: https://arxiv.org/abs/2311.02462. Source class: primary.
- **[assumption]** It is reasonable to include the DeepMind AGI framework as a comparator even though it is aimed at capability classification rather than day-to-day agent practice, because the research question explicitly asks about frameworks for compartmentalising AI terminology and concepts and the DeepMind paper supplies a contrasting axis, capability and autonomy, used by a major research lab. Source: https://arxiv.org/abs/2311.02462.
- **[inference]** DeepMind's framework occupies a different layer of abstraction than 4D, because it classifies what systems are capable of and how autonomous they are, while 4D classifies how people should work with AI systems responsibly. Source: https://arxiv.org/abs/2311.02462; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf. Source class: inference from primary sources.

#### Comparative synthesis before formal §6

- **[inference]** Across the comparison set, 4D is the only framework centred on user competency rather than system activity, system attributes, harms, or capability levels. Source: https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://arxiv.org/abs/2311.02462. Source class: inference from primary sources.
- **[inference]** 4D is strong as practical team guidance because each D corresponds to a concrete working move, delegation choice, specification, evaluation, or accountability, while NIST and OECD are stronger as registry, governance, and analysis tools because they classify systems or activities more explicitly. Source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://www.anthropic.com/research/building-effective-agents. Source class: inference from primary sources.
- **[inference]** Anthropic's 4D framework complements rather than replaces structural taxonomies, because teams still need a separate vocabulary for activity type, architecture pattern, harms, and governance surface. Source: https://www.anthropic.com/research/building-effective-agents; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md. Source class: inference from primary and prior completed sources.

### §3 Reasoning

- **[fact]** Anthropic's own materials support the four top-level definitions and the named sub-components for each D. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf.
- **[inference]** The decisive comparison criterion is what each framework is trying to classify. On that criterion, 4D classifies human collaboration competencies, NIST classifies AI contribution types, OECD classifies system characteristics in context, Benbouzid et al. classify harms, Anthropic's workflows-versus-agents post classifies orchestration patterns, and DeepMind classifies capability and autonomy levels. Source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://www.anthropic.com/research/building-effective-agents; https://arxiv.org/abs/2311.02462.
- **[inference]** Because the frameworks classify different objects, asking which one is "best" without specifying purpose is the wrong comparison; the right comparison is fitness for a use case such as training, system registry, architecture choice, or harms analysis. Source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification.
- **[inference]** The practical value of 4D comes from sequencing decisions people already have to make in real projects, while its main limitation is that it leaves architecture, risk taxonomy, and deployment context to other frameworks. Source: https://www.anthropic.com/ai-fluency; https://www.anthropic.com/research/building-effective-agents; https://oecd.ai/en/classification.

### §4 Consistency Check

- **[fact]** No source contradiction was found on the names or top-level definitions of Delegation, Description, Discernment, and Diligence. Source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf.
- **[fact]** The comparison set spans different target objects, competencies, activities, system dimensions, harms, architecture patterns, and capability levels, so differences in scope are expected rather than contradictory. Source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://arxiv.org/abs/2311.02462; https://www.anthropic.com/research/building-effective-agents.
- **[inference]** Confidence should remain medium overall because the Anthropic definitions are well supported by official materials, but the comparison section combines frameworks designed for different purposes and therefore requires interpretive judgment rather than one-to-one equivalence. Source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification.

### §5 Depth and Breadth Expansion

- **[inference]** Technical lens: Anthropic's workflows-versus-agents distinction gives the 4D model an immediate technical complement by identifying when dynamic agent autonomy is warranted and when fixed workflows are preferable. Source: https://www.anthropic.com/research/building-effective-agents.
- **[fact]** Governance lens: OECD and the harms taxonomy explicitly address policy, stakeholder, and incident-reporting concerns that 4D does not enumerate. Source: https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2.
- **[fact]** Evaluation lens: NIST's taxonomy is deliberately measurement-oriented and can support trustworthiness and usability evaluation across human-AI tasks. Source: https://doi.org/10.6028/NIST.AI.200-1.
- **[inference]** Organisational lens: 4D is easier to teach to mixed teams than OECD or NIST because its categories map to common work habits instead of formal classification fields, but mixed teams still need a structural taxonomy when they move from training to governance or architecture review. Source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification.
- **[inference]** Historical lens: the 4D framework fits the recent shift from prompt-only advice toward broader human-AI operating practices, while NIST and OECD continue the longer tradition of formal taxonomies for measurement and governance. Source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification.

### §6 Synthesis

**Executive summary:**

Anthropic's 4D framework is a human-AI fluency model rather than a full taxonomy of AI systems, because it organises the user's work into deciding, specifying, evaluating, and taking responsibility instead of classifying activities, system attributes, harms, or capability levels. [inference; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification]

Its four components are clear in Anthropic's official materials: Delegation decides the human-AI split, Description specifies the output, process, and interaction style, Discernment evaluates the result and the reasoning behind it, and Diligence governs responsible choice, disclosure, and ownership. [fact; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf]

Compared with NIST, OECD, the collaborative harms taxonomy, Anthropic's workflows-versus-agents framing, and DeepMind's AGI levels, 4D is narrower in analytical coverage but stronger as a day-to-day operating heuristic for teams learning how to work with AI. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://www.anthropic.com/research/building-effective-agents; https://arxiv.org/abs/2311.02462]

Teams building or governing AI agents should therefore pair 4D with a structural taxonomy such as NIST or OECD and, when architecture decisions matter, with Anthropic's workflows-versus-agents distinction. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://www.anthropic.com/research/building-effective-agents]

**Key findings:**

1. **Anthropic defines the 4D framework as four interconnected competencies necessary for AI interactions to remain effective, efficient, ethical, and safe, which makes it a fluency model for human practice rather than a classification scheme for AI systems themselves.** ([inference]; medium confidence; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf)
2. **Delegation in Anthropic's materials means setting goals and deciding whether, when, and how to engage with AI, and the framework breaks that work into problem awareness, platform awareness, and task delegation across automation, augmentation, and agency modes.** ([fact]; medium confidence; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf)
3. **Description is the framework's specification layer because Anthropic divides it into product, process, and performance description that respectively define the desired output, the system's method, and the behaviour expected during collaboration.** ([inference]; medium confidence; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf)
4. **Discernment and Diligence make the framework explicitly evaluative and accountability-oriented, since Anthropic asks users to assess product, process, and performance while also selecting systems carefully, disclosing AI use honestly, and taking responsibility for deployed outputs.** ([inference]; medium confidence; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf)
5. **NIST's AI Use Taxonomy is broader and more operationally neutral than 4D because it classifies 16 human-AI activity types independent of technique or domain, whereas 4D focuses on competencies a person should apply in any interaction with AI.** ([inference]; high confidence; source: https://doi.org/10.6028/NIST.AI.200-1; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf)
6. **The OECD framework and the collaborative harms taxonomy both cover governance surfaces that 4D leaves largely implicit, including stakeholders, economic context, data inputs, model properties, task outputs, and harms categories, so they are better suited to policy, registry, and risk mapping work.** ([inference]; high confidence; source: https://oecd.ai/en/classification; https://oecd.ai/en/wonk/documents/oecd-framework-for-classifying-ai-systems-two-page-overview; https://arxiv.org/html/2407.01294v2)
7. **Anthropic's separate workflows-versus-agents guidance complements 4D by supplying an architecture choice model that the fluency framework does not provide, which means teams can use 4D to structure human practice and use workflows-versus-agents to structure system design.** ([inference]; medium confidence; source: https://www.anthropic.com/research/building-effective-agents; https://www.anthropic.com/ai-fluency)
8. **DeepMind's AGI framework shows that 4D sits on a different taxonomy axis from capability and autonomy taxonomies, because it explains collaboration quality while other frameworks explain what systems do, what risks they present, or how capable they are.** ([inference]; medium confidence; source: https://arxiv.org/abs/2311.02462; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2)

**Evidence map:**

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Anthropic's 4D framework is a fluency model for human practice, not a full system taxonomy. | https://www.anthropic.com/ai-fluency ; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf ; https://doi.org/10.6028/NIST.AI.200-1 ; https://oecd.ai/en/classification | medium | Object of classification differs |
| [fact] Delegation covers problem awareness, platform awareness, task delegation, and the automation, augmentation, and agency modes. | https://www.anthropic.com/ai-fluency ; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf ; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf | medium | Official Anthropic materials agree |
| [inference] Description functions as the framework's specification layer through product, process, and performance description. | https://www.anthropic.com/ai-fluency ; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf | medium | Specification lens |
| [inference] Discernment and Diligence add evaluation, disclosure, and ownership to the framework. | https://www.anthropic.com/ai-fluency ; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf | medium | Accountability lens |
| [fact] NIST classifies 16 AI use activities independent of technique or domain. | https://doi.org/10.6028/NIST.AI.200-1 | high | Activity taxonomy |
| [inference] OECD and the collaborative harms taxonomy classify governance and harms surfaces that 4D does not enumerate. | https://oecd.ai/en/classification ; https://oecd.ai/en/wonk/documents/oecd-framework-for-classifying-ai-systems-two-page-overview ; https://arxiv.org/html/2407.01294v2 | high | Governance focus |
| [inference] Anthropic's workflows-versus-agents post supplies an architecture distinction missing from 4D. | https://www.anthropic.com/research/building-effective-agents ; https://www.anthropic.com/ai-fluency | medium | Architecture complement |
| [inference] DeepMind's AGI framework sits on a capability-and-autonomy axis different from 4D's collaboration axis. | https://arxiv.org/abs/2311.02462 ; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf | medium | Cross-axis comparison |

**Assumptions:**

- **[assumption]** DeepMind's AGI levels are included as a valid comparator because the research question asks about frameworks that compartmentalise AI terminology and concepts broadly, not only about narrow agent-operating models. Source: https://arxiv.org/abs/2311.02462.

**Analysis:**

The strongest evidence is around Anthropic's own definitions, because the course page, framework summary, and terminology sheet align on the names and practical meaning of the four Ds. [inference; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf]

The main analytical move is therefore not recovering what 4D says, but determining what kind of framework it is relative to other schemes. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://arxiv.org/abs/2311.02462]

On that comparison, 4D resembles a user operating model more than a taxonomy in the NIST or OECD sense, because it tells people how to structure collaboration rather than how to catalogue system features or risk surfaces. [inference; source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification]

That distinction also aligns with the repository's earlier concept-first taxonomy, which classifies prompts, memory, controls, and tools as system concepts rather than as human competencies, making the two frameworks complementary rather than contradictory. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf]

For practitioners, the trade-off is straightforward: 4D is easier to teach and apply in day-to-day work, while NIST, OECD, harms taxonomies, and architecture taxonomies are better for system inventory, formal evaluation, policy review, and design governance. [inference; source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://www.anthropic.com/research/building-effective-agents; https://arxiv.org/html/2407.01294v2]

**Risks, gaps, uncertainties:**

- Anthropic's public evidence base currently exposes the 4D framework through course assets and downloadable teaching materials rather than through a single standalone technical paper, so the official definitions are clear but the public explanatory depth is thinner than in the NIST and OECD publications. [inference; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification]
- The comparison set mixes frameworks designed for different classification objects, which means some "differences" are purpose differences rather than rival claims about the same object. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://arxiv.org/abs/2311.02462]
- The DeepMind comparator is informative but less directly relevant to day-to-day agent-building teams than NIST, OECD, or Anthropic's own workflows-versus-agents guidance. [inference; source: https://arxiv.org/abs/2311.02462; https://www.anthropic.com/research/building-effective-agents]

**Open questions:**

- Will Anthropic publish a fuller public paper or transcript that explains the pedagogical rationale behind 4D beyond course assets and summaries?
- Are there other training-oriented AI fluency frameworks from major model providers that are comparable to 4D on pedagogy rather than on governance or architecture?
- How should organisations map 4D-style user competencies onto formal assurance or audit controls without losing the practical simplicity that makes the framework useful?

### §7 Recursive Review

- Review result: pass
- Acronym audit: Artificial Intelligence (AI), National Institute of Standards and Technology (NIST), Organisation for Economic Co-operation and Development (OECD), Large Language Model (LLM), Natural Language Processing (NLP), and Artificial General Intelligence (AGI) are expanded on first use.
- Claim audit: Findings claims are mirrored in §6, and each key claim is either sourced or labelled as inference or assumption.
- Cross-item integration: direct citation added to the repository's concept-first taxonomy, with related links to agent evaluation, agent decision-making, and AI coding harnesses items.

---

## Findings

### Executive Summary

Anthropic's 4D framework is a human-AI fluency model rather than a full taxonomy of AI systems, because it organises the user's work into deciding, specifying, evaluating, and taking responsibility instead of classifying activities, system attributes, harms, or capability levels. [inference; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification]

Its four components are clear in Anthropic's official materials: Delegation decides the human-AI split, Description specifies the output, process, and interaction style, Discernment evaluates the result and the reasoning behind it, and Diligence governs responsible choice, disclosure, and ownership. [fact; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf]

Compared with NIST, OECD, the collaborative harms taxonomy, Anthropic's workflows-versus-agents framing, and DeepMind's AGI levels, 4D is narrower in analytical coverage but stronger as a day-to-day operating heuristic for teams learning how to work with AI. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://www.anthropic.com/research/building-effective-agents; https://arxiv.org/abs/2311.02462]

Teams building or governing AI agents should therefore pair 4D with a structural taxonomy such as NIST or OECD and, when architecture decisions matter, with Anthropic's workflows-versus-agents distinction. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://www.anthropic.com/research/building-effective-agents]

### Key Findings

1. **Anthropic defines the 4D framework as four interconnected competencies necessary for AI interactions to remain effective, efficient, ethical, and safe, which makes it a fluency model for human practice rather than a classification scheme for AI systems themselves.** ([inference]; medium confidence; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf)
2. **Delegation in Anthropic's materials means setting goals and deciding whether, when, and how to engage with AI, and the framework breaks that work into problem awareness, platform awareness, and task delegation across automation, augmentation, and agency modes.** ([fact]; medium confidence; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf)
3. **Description is the framework's specification layer because Anthropic divides it into product, process, and performance description that respectively define the desired output, the system's method, and the behaviour expected during collaboration.** ([inference]; medium confidence; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf)
4. **Discernment and Diligence make the framework explicitly evaluative and accountability-oriented, since Anthropic asks users to assess product, process, and performance while also selecting systems carefully, disclosing AI use honestly, and taking responsibility for deployed outputs.** ([inference]; medium confidence; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf)
5. **NIST's AI Use Taxonomy is broader and more operationally neutral than 4D because it classifies 16 human-AI activity types independent of technique or domain, whereas 4D focuses on competencies a person should apply in any interaction with AI.** ([inference]; high confidence; source: https://doi.org/10.6028/NIST.AI.200-1; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf)
6. **The OECD framework and the collaborative harms taxonomy both cover governance surfaces that 4D leaves largely implicit, including stakeholders, economic context, data inputs, model properties, task outputs, and harms categories, so they are better suited to policy, registry, and risk mapping work.** ([inference]; high confidence; source: https://oecd.ai/en/classification; https://oecd.ai/en/wonk/documents/oecd-framework-for-classifying-ai-systems-two-page-overview; https://arxiv.org/html/2407.01294v2)
7. **Anthropic's separate workflows-versus-agents guidance complements 4D by supplying an architecture choice model that the fluency framework does not provide, which means teams can use 4D to structure human practice and use workflows-versus-agents to structure system design.** ([inference]; medium confidence; source: https://www.anthropic.com/research/building-effective-agents; https://www.anthropic.com/ai-fluency)
8. **DeepMind's AGI framework shows that 4D sits on a different taxonomy axis from capability and autonomy taxonomies, because it explains collaboration quality while other frameworks explain what systems do, what risks they present, or how capable they are.** ([inference]; medium confidence; source: https://arxiv.org/abs/2311.02462; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2)

### Evidence Map

| Claim | Source | Confidence | Notes |
|---|---|---|---|
| [inference] Anthropic's 4D framework is a fluency model for human practice, not a full system taxonomy. | https://www.anthropic.com/ai-fluency ; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf ; https://doi.org/10.6028/NIST.AI.200-1 ; https://oecd.ai/en/classification | medium | Classification target differs |
| [fact] Delegation covers problem awareness, platform awareness, task delegation, and the automation, augmentation, and agency modes. | https://www.anthropic.com/ai-fluency ; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf ; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf | medium | Official Anthropic materials agree |
| [inference] Description functions as the framework's specification layer through product, process, and performance description. | https://www.anthropic.com/ai-fluency ; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf | medium | Specification lens |
| [inference] Discernment and Diligence add evaluation, disclosure, and ownership to the framework. | https://www.anthropic.com/ai-fluency ; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf | medium | Accountability lens |
| [fact] NIST classifies 16 AI use activities independent of technique or domain. | https://doi.org/10.6028/NIST.AI.200-1 | high | Activity taxonomy |
| [inference] OECD and the collaborative harms taxonomy classify governance and harms surfaces that 4D does not enumerate. | https://oecd.ai/en/classification ; https://oecd.ai/en/wonk/documents/oecd-framework-for-classifying-ai-systems-two-page-overview ; https://arxiv.org/html/2407.01294v2 | high | Governance comparison |
| [inference] Anthropic's workflows-versus-agents post supplies an architecture distinction missing from 4D. | https://www.anthropic.com/research/building-effective-agents ; https://www.anthropic.com/ai-fluency | medium | Architecture complement |
| [inference] DeepMind's AGI framework sits on a capability-and-autonomy axis different from 4D's collaboration axis. | https://arxiv.org/abs/2311.02462 ; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf | medium | Contrasting abstraction level |

### Assumptions

- **DeepMind's AGI levels are included as a valid comparator because the question asks about frameworks that compartmentalise AI terminology and concepts broadly, not only about narrow agent-operating models.** [assumption; source: https://arxiv.org/abs/2311.02462]

### Analysis

The strongest evidence is around Anthropic's own definitions, because the course page, framework summary, and terminology sheet align on the names and practical meaning of the four Ds. [inference; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://www-cdn.anthropic.com/4286688a2f9d88c74d98f740778a9fc81fb18ba7.pdf]

The main analytical move is therefore not recovering what 4D says, but determining what kind of framework it is relative to other schemes. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://arxiv.org/abs/2311.02462]

On that comparison, 4D resembles a user operating model more than a taxonomy in the NIST or OECD sense, because it tells people how to structure collaboration rather than how to catalogue system features or risk surfaces. [inference; source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification]

That distinction also aligns with the repository's earlier concept-first taxonomy, which classifies prompts, memory, controls, and tools as system concepts rather than as human competencies, making the two frameworks complementary rather than contradictory. [inference; source: https://github.com/davidamitchell/Research/blob/main/Research/completed/2026-03-10-ai-concept-classification-taxonomy.md; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf]

For practitioners, the trade-off is straightforward: 4D is easier to teach and apply in day-to-day work, while NIST, OECD, harms taxonomies, and architecture taxonomies are better for system inventory, formal evaluation, policy review, and design governance. [inference; source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://www.anthropic.com/research/building-effective-agents; https://arxiv.org/html/2407.01294v2]

### Risks, Gaps, and Uncertainties

- Anthropic's public evidence base currently exposes the 4D framework through course assets and downloadable teaching materials rather than through a single standalone technical paper, so the official definitions are clear but the public explanatory depth is thinner than in the NIST and OECD publications. [inference; source: https://www.anthropic.com/ai-fluency; https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification]
- The comparison set mixes frameworks designed for different classification objects, which means some differences are purpose differences rather than rival claims about the same object. [inference; source: https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://arxiv.org/html/2407.01294v2; https://arxiv.org/abs/2311.02462]
- The DeepMind comparator is informative but less directly relevant to day-to-day agent-building teams than NIST, OECD, or Anthropic's own workflows-versus-agents guidance. [inference; source: https://arxiv.org/abs/2311.02462; https://www.anthropic.com/research/building-effective-agents]

### Open Questions

- Will Anthropic publish a fuller public paper or transcript that explains the pedagogical rationale behind 4D beyond course assets and summaries?
- Are there other training-oriented AI fluency frameworks from major model providers that are comparable to 4D on pedagogy rather than on governance or architecture?
- How should organisations map 4D-style user competencies onto formal assurance or audit controls without losing the practical simplicity that makes the framework useful?

---

## Output

- Type: knowledge
- Description: Comparative research item defining Anthropic's 4D framework and positioning it against activity, governance, harms, architecture, and capability taxonomies so teams can choose an appropriate shared AI vocabulary. [inference; source: https://www.anthropic.com/ai-fluency; https://doi.org/10.6028/NIST.AI.200-1; https://oecd.ai/en/classification; https://www.anthropic.com/research/building-effective-agents]
- Links:
  - https://www-cdn.anthropic.com/334975cdec18f744b4fa511dc8518bd8d119d29d.pdf
  - https://doi.org/10.6028/NIST.AI.200-1
  - https://oecd.ai/en/classification
