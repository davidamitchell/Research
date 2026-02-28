"""Load and validate the sources configuration from config/sources.yaml."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

from src.logger import get_logger

logger = get_logger(__name__)

_DEFAULT_CONFIG_PATH = Path(__file__).parent.parent / "config" / "sources.yaml"


def load_config(path: Path | None = None) -> dict[str, Any]:
    """Load and validate the sources configuration.

    Parameters
    ----------
    path:
        Path to the YAML config file. Defaults to ``config/sources.yaml``.

    Returns
    -------
    dict
        Validated configuration dictionary.

    Raises
    ------
    ValueError
        If the config file is missing required keys or has invalid values.
    FileNotFoundError
        If the config file does not exist.
    """
    config_path = path or _DEFAULT_CONFIG_PATH
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with config_path.open(encoding="utf-8") as fh:
        raw: dict[str, Any] = yaml.safe_load(fh) or {}

    _validate(raw, config_path)
    logger.debug("Loaded config from %s", config_path)
    return raw


def _validate(config: dict[str, Any], path: Path) -> None:
    """Raise ValueError if the config structure is invalid."""
    # youtube section
    yt = config.get("youtube", {}) or {}
    if not isinstance(yt, dict):
        raise ValueError(f"{path}: 'youtube' must be a mapping, got {type(yt).__name__}")

    for i, source in enumerate(yt.get("channels") or []):
        if not isinstance(source, dict):
            raise ValueError(f"{path}: youtube.channels[{i}] must be a mapping")
        if "id" not in source:
            raise ValueError(f"{path}: youtube.channels[{i}] missing required key 'id'")
        if not isinstance(source.get("max_videos", 5), int):
            raise ValueError(f"{path}: youtube.channels[{i}].max_videos must be an integer")

    for i, video in enumerate(yt.get("videos") or []):
        if not isinstance(video, dict):
            raise ValueError(f"{path}: youtube.videos[{i}] must be a mapping")
        if "url" not in video:
            raise ValueError(f"{path}: youtube.videos[{i}] missing required key 'url'")

    # rss section
    rss = config.get("rss", {}) or {}
    if not isinstance(rss, dict):
        raise ValueError(f"{path}: 'rss' must be a mapping")
    for i, feed in enumerate(rss.get("sources") or []):
        if not isinstance(feed, dict):
            raise ValueError(f"{path}: rss.sources[{i}] must be a mapping")
        if "url" not in feed:
            raise ValueError(f"{path}: rss.sources[{i}] missing required key 'url'")

    # arxiv section
    arxiv = config.get("arxiv", {}) or {}
    if not isinstance(arxiv, dict):
        raise ValueError(f"{path}: 'arxiv' must be a mapping")
    for i, q in enumerate(arxiv.get("queries") or []):
        if not isinstance(q, str):
            raise ValueError(f"{path}: arxiv.queries[{i}] must be a string")
