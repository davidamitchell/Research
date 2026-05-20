#!/usr/bin/env python3
"""Vector search index generation for the static site build."""

from __future__ import annotations

import json
from typing import Any

PYTHON_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
BROWSER_MODEL_ID = "Xenova/all-MiniLM-L6-v2"


def _item_text_payload(item: dict[str, Any], named_concepts: list[str], themes: list[str]) -> str:
    all_text_parts = [item["title"]] + list(item["sections"].values()) + named_concepts + themes
    return " ".join(part for part in all_text_parts if part)


def build_vector_search_index(
    items: list[dict[str, Any]],
    metadata: dict[str, Any],
    slug_to_threads: dict[str, list[str]],
) -> str:
    """Build a static vector index JSON document for browser-side Orama search."""
    from sentence_transformers import SentenceTransformer

    meta_items: dict[str, Any] = metadata.get("items", {})

    records: list[dict[str, Any]] = []
    texts: list[str] = []
    for item in items:
        slug = item["slug"]
        item_meta: dict[str, Any] = meta_items.get(slug, {})
        named_concepts = item_meta.get("named_concepts", [])
        themes = item.get("ai_themes", [])
        full_text = _item_text_payload(item, named_concepts, themes)
        texts.append(full_text)
        records.append(
            {
                "id": slug,
                "slug": slug,
                "title": item["display_title"],
                "full_title": item["title"],
                "tags": item["tags"],
                "added": item["added_str"],
                "question_excerpt": item["question_excerpt"],
                "findings_excerpt": item.get("findings_excerpt", ""),
                "thread_slugs": slug_to_threads.get(slug, []),
                "url": item.get("page_url", f"/Research/research/{slug}.html"),
            }
        )

    model = SentenceTransformer(PYTHON_MODEL_ID)
    vectors = model.encode(texts, normalize_embeddings=True)
    vector_rows = [[float(value) for value in row.tolist()] for row in vectors]
    dimension = len(vector_rows[0]) if vector_rows else 0

    payload = {
        "schema_version": 1,
        "model": {
            "python_model_id": PYTHON_MODEL_ID,
            "browser_model_id": BROWSER_MODEL_ID,
            "pooling": "mean",
            "normalize": True,
            "dimension": dimension,
        },
        "items": records,
        "vectors": vector_rows,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)
