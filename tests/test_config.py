"""Tests for config loading and validation."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from src.config import load_config


def _write_config(tmp_path: Path, content: dict) -> Path:
    p = tmp_path / "sources.yaml"
    p.write_text(yaml.dump(content), encoding="utf-8")
    return p


def test_load_config_loads_valid_file(tmp_path: Path) -> None:
    cfg = _write_config(
        tmp_path,
        {
            "youtube": {
                "videos": [{"url": "https://youtu.be/abc123"}],
                "channels": [{"id": "UCtest", "name": "Test", "max_videos": 3}],
            },
            "rss": {"sources": []},
            "arxiv": {"queries": []},
        },
    )
    result = load_config(cfg)
    assert result["youtube"]["videos"][0]["url"] == "https://youtu.be/abc123"


def test_load_config_empty_sections_valid(tmp_path: Path) -> None:
    cfg = _write_config(tmp_path, {"youtube": {}, "rss": {}, "arxiv": {}})
    result = load_config(cfg)
    assert "youtube" in result


def test_load_config_raises_on_missing_file() -> None:
    with pytest.raises(FileNotFoundError):
        load_config(Path("/nonexistent/sources.yaml"))


def test_load_config_raises_on_channel_missing_id(tmp_path: Path) -> None:
    cfg = _write_config(
        tmp_path,
        {"youtube": {"channels": [{"name": "No ID channel"}]}},
    )
    with pytest.raises(ValueError, match="missing required key 'id'"):
        load_config(cfg)


def test_load_config_raises_on_video_missing_url(tmp_path: Path) -> None:
    cfg = _write_config(
        tmp_path,
        {"youtube": {"videos": [{"title": "No URL"}]}},
    )
    with pytest.raises(ValueError, match="missing required key 'url'"):
        load_config(cfg)


def test_load_config_raises_on_rss_missing_url(tmp_path: Path) -> None:
    cfg = _write_config(
        tmp_path,
        {"rss": {"sources": [{"name": "No URL feed"}]}},
    )
    with pytest.raises(ValueError, match="missing required key 'url'"):
        load_config(cfg)


def test_load_config_raises_on_arxiv_non_string(tmp_path: Path) -> None:
    cfg = _write_config(tmp_path, {"arxiv": {"queries": [123]}})
    with pytest.raises(ValueError, match="must be a string"):
        load_config(cfg)


def test_load_config_accepts_real_sources_yaml() -> None:
    """The committed config/sources.yaml must be valid."""
    result = load_config()
    assert "youtube" in result
