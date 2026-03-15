# Session: new-research-item-confluence-embeddings

**Date:** 2026-03-15
**Issue:** New research item — latent concept extraction from Confluence wiki

## What was done

Created a new research backlog item in `Research/backlog/2026-03-15-latent-concept-extraction-confluence.md`.

The item covers four interconnected topics raised in the issue:

1. **Latent concept extraction from Confluence wiki** — topic modelling (Latent Dirichlet Allocation (LDA), BERTopic), Named Entity Recognition (NER), and implicit relation extraction applied to Confluence page content.
2. **Word embeddings into a Vector DataBase (VDB)** — sentence-transformer model selection, chunking strategy, VDB schema design (Qdrant, Weaviate, Chroma, pgvector), and retrieval query patterns.
3. **Knowledge graph construction** — entity/relation extraction, graph schema (Resource Description Framework (RDF) vs. property graphs), and how the graph complements the VDB for Retrieval-Augmented Generation (RAG).
4. **Epistemic evaluation** — distinguishing "true" (factually grounded, sourced, recent) from "useful" (operationally relevant, frequently adopted) and whether the distinction is meaningful in an organisational knowledge base.

## Files created

- `Research/backlog/2026-03-15-latent-concept-extraction-confluence.md`
- `progress/2026-03-15-new-research-item-confluence-embeddings.md` (this file)

## Mini-Retro

1. **Did the process work?** Yes — the template was followed correctly, all acronyms expanded on first use, and the item covers all four topics from the issue in a single coherent research question.
2. **What slowed down or went wrong?** An accidental double blank line was introduced during an edit to the scope section; caught immediately by reviewing the file.
3. **What single change would prevent this next time?** Use the `python -m src.main research add` CLI to scaffold the item rather than creating the file manually, to eliminate manual template transcription errors.
4. **Is this a pattern?** No — isolated file-creation mishap, not a recurring class of error.
