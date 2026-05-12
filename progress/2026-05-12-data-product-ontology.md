# 2026-05-12 — Add backlog item (data-product-ontology)

**Date:** 2026-05-12
**Slug:** data-product-ontology
**Issue:** "New research — What is data product ontology"

## What was done

Created `Research/backlog/2026-05-12-data-product-ontology.md` as a new research backlog item, sourced from a GitHub issue asking: what is data product ontology, who uses it, how is it used, is it useful or outdated, and what are related standards?

The validated research question is: *What is the data product ontology, which organisations and communities use it, how is it applied in practice within data mesh and data management architectures, and is it still current relative to competing and complementary standards?*

Key choices made:
- **Priority: medium** — important for data governance work but not blocking any current active research
- **Tags:** `knowledge-graph`, `governance`, `data-product` — ontology work sits in the knowledge-graph cluster; `governance` covers the standards/policy angle; `data-product` is introduced as a new tag because no existing canonical tag covers the data product concept
- **Acronyms expanded on first use:** Resource Description Framework (RDF), Web Ontology Language (OWL), SPARQL, Data Catalog Vocabulary (DCAT), Data Privacy Vocabulary (DPV), Object Management Group (OMG), Semantic Interoperability Community (SEMIC), Findable Accessible Interoperable Reusable (FAIR), ISO
- **Sources include URLs:** all six starting sources have verifiable public URLs
- Approach decomposed into 7 concrete investigation steps: enumerate candidates, document structure, identify adopters, document usage, assess currency, map to adjacent standards, synthesise verdict

## Conventions followed

- Copied and populated `Research/_template.md` format exactly
- File named `YYYY-MM-DD-short-slug.md` in `Research/backlog/`
- All frontmatter fields present; `status: backlog`, `started: ~`, `completed: ~`, `versions: []`
- Acronyms expanded on first use throughout the document
- Every source in `## Sources` includes a URL in `[Display Name](https://url)` format
- Research Skill Output and Findings sections left blank for the research agent to fill

## Mini-Retro

1. **Did the process work?** Yes. The issue description was brief but provided four clear angles (definition, users, usage, relevance/freshness, related standards) that mapped directly to a decomposable research question.
2. **What slowed down or went wrong?** Minor uncertainty about which existing canonical tag to use for the data product concept — none in the vocabulary covers it directly. Added `data-product` as a new tag.
3. **What single change would prevent friction next time?** Consider adding `data-product` and `data-governance` to the canonical tag vocabulary once there are two or more items using them.
4. **Is this a pattern?** No — this is a new topic area for the backlog.
