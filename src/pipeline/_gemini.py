"""Gemini generative AI client with model discovery and cascade fallback.

_MODEL_CASCADE lists flash-class models to try in order (newest → oldest).
At runtime, build_cascade() prepends any newer models discovered via the
ListModels API, so Gemini 3.x (and beyond) surfaces automatically without
code changes.

Usage:
    import os
    from src.pipeline._gemini import build_cascade, generate_with_fallback

    api_key = os.environ["GEMINI_API_KEY"]
    cascade = build_cascade(api_key)
    text, model_used = generate_with_fallback(api_key, "Hello!", cascade)
"""

from __future__ import annotations

import re
import time
from typing import Any

import httpx

_BASE = "https://generativelanguage.googleapis.com/v1beta"

# Static fallback cascade — maintained when new models ship.
# Ordered newest → oldest; gemini-2.5-flash is confirmed working (2026-05-11).
_MODEL_CASCADE: list[str] = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
]

# Statuses that mean "this model won't serve the request — try the next one".
_SKIP_STATUSES: frozenset[int] = frozenset({404, 429, 500, 502, 503, 504})
# Statuses that mean the request itself is broken — no point trying other models.
_FATAL_STATUSES: frozenset[int] = frozenset({401, 403})


# ---------------------------------------------------------------------------
# Model discovery
# ---------------------------------------------------------------------------


def list_models(api_key: str, *, timeout: float = 15.0) -> list[str]:
    """Return all model IDs that support generateContent.

    Calls the ListModels REST endpoint.  Returns [] on any network or API
    error so callers can fall back to _MODEL_CASCADE without crashing.
    """
    try:
        resp = httpx.get(
            f"{_BASE}/models",
            params={"key": api_key},
            timeout=timeout,
        )
        resp.raise_for_status()
        data: dict[str, Any] = resp.json()
    except Exception:
        return []

    return [
        m["name"].removeprefix("models/")
        for m in data.get("models", [])
        if "generateContent" in m.get("supportedGenerationMethods", [])
        and m.get("name", "").startswith("models/")
    ]


def _flash_sort_key(model_id: str) -> tuple[int, int, int] | None:
    """Parse a sort key (major, minor, is_lite) from a flash model ID.

    Returns None for non-flash models.  is_lite=0 sorts before is_lite=1 so
    base flash ranks above flash-lite at the same version.

    Examples:
        "gemini-3.1-flash"      → (3, 1, 0)
        "gemini-2.5-flash"      → (2, 5, 0)
        "gemini-2.5-flash-lite" → (2, 5, 1)
        "gemini-2.0-flash"      → (2, 0, 0)
    """
    m = re.match(r"^gemini-(\d+)\.(\d+)-flash(-lite)?$", model_id)
    if not m:
        return None
    return (int(m.group(1)), int(m.group(2)), 0 if m.group(3) is None else 1)


def build_cascade(api_key: str) -> list[str]:
    """Build a flash-model cascade by calling ListModels, newest-first.

    Steps:
      1. Call ListModels to discover all models available to this API key.
      2. Keep only models whose IDs match the gemini-X.Y-flash[-lite] pattern.
      3. Sort: major desc → minor desc → base before lite.
      4. Append any _MODEL_CASCADE entries not already present as a safety net.

    Falls back entirely to _MODEL_CASCADE if the API call fails or returns no
    flash models — e.g. when the key is not yet valid in CI before the secret
    is set.
    """
    all_models = list_models(api_key)

    keyed: list[tuple[tuple[int, int, int], str]] = []
    for mid in all_models:
        key = _flash_sort_key(mid)
        if key is not None:
            keyed.append((key, mid))

    if not keyed:
        return list(_MODEL_CASCADE)

    # Sort newest-first: negate major+minor so larger = earlier in list.
    keyed.sort(key=lambda x: (-x[0][0], -x[0][1], x[0][2]))

    seen: set[str] = set()
    result: list[str] = []
    for _, mid in keyed:
        if mid not in seen:
            seen.add(mid)
            result.append(mid)

    # Append static fallbacks not found by ListModels.
    for mid in _MODEL_CASCADE:
        if mid not in seen:
            seen.add(mid)
            result.append(mid)

    return result


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------


def generate(
    api_key: str,
    model: str,
    prompt: str,
    *,
    max_tokens: int = 512,
    temperature: float = 0.2,
    timeout: float = 30.0,
) -> str:
    """Call generateContent for a single model.  Raises on any error."""
    payload: dict[str, Any] = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": max_tokens,
            "temperature": temperature,
        },
    }
    resp = httpx.post(
        f"{_BASE}/models/{model}:generateContent",
        params={"key": api_key},
        json=payload,
        timeout=timeout,
    )
    if resp.status_code in _FATAL_STATUSES:
        resp.raise_for_status()  # auth errors — no point continuing
    resp.raise_for_status()

    data: dict[str, Any] = resp.json()
    candidates = data.get("candidates", [])
    if not candidates:
        raise ValueError(f"No candidates in response from {model}")
    parts = candidates[0].get("content", {}).get("parts", [])
    if not parts:
        raise ValueError(f"No parts in candidate from {model}")
    return str(parts[0].get("text", ""))


def generate_with_fallback(
    api_key: str,
    prompt: str,
    cascade: list[str],
    *,
    max_tokens: int = 512,
    temperature: float = 0.2,
) -> tuple[str, str]:
    """Try each model in cascade until one succeeds.

    Returns (response_text, model_id_used).
    Raises RuntimeError if every model in the cascade fails.
    """
    last_exc: Exception | None = None

    for model in cascade:
        try:
            text = generate(
                api_key,
                model,
                prompt,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return text, model
        except httpx.HTTPStatusError as exc:
            status = exc.response.status_code
            if status in _FATAL_STATUSES:
                raise  # auth failure — abort immediately
            last_exc = exc
        except Exception as exc:
            last_exc = exc

        time.sleep(0.5)  # brief pause before next model

    raise RuntimeError(
        f"All {len(cascade)} models in cascade failed. Last error: {last_exc}"
    ) from last_exc
