"""State persistence for the fetch pipeline.

Tracks which URLs have already been processed so that the pipeline does not
reprocess the same content on subsequent runs.

Schema of ``state/index.json``::

    {
        "processed": {
            "<url>": {
                "fetched_at": "2026-02-28T09:00:00+00:00",
                "title": "Video title",
                "source_id": "youtube"
            }
        }
    }

Writes are atomic: data is written to a temporary file in the same directory
then renamed into place, so a crash mid-write cannot corrupt the state file.
"""

from __future__ import annotations

import contextlib
import json
import os
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from src.fetchers import FetchedItem
from src.logger import get_logger

logger = get_logger(__name__)

_DEFAULT_STATE_PATH = Path("state/index.json")


class StateStore:
    """Persistent store of processed URLs.

    Parameters
    ----------
    path:
        Path to the JSON state file.  Defaults to ``state/index.json``
        relative to the current working directory.
    """

    def __init__(self, path: Path | str = _DEFAULT_STATE_PATH) -> None:
        self._path = Path(path)
        self._data: dict[str, Any] = self._load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def is_processed(self, url: str) -> bool:
        """Return True if *url* has already been recorded as processed."""
        return url in self._data.get("processed", {})

    def record(self, item: FetchedItem) -> None:
        """Record *item* as processed and persist the state file atomically."""
        processed = self._data.setdefault("processed", {})
        processed[item.url] = {
            "fetched_at": datetime.now(tz=UTC).isoformat(),
            "title": item.title,
            "source_id": item.source_id,
        }
        self._save()
        logger.debug("Recorded: %s", item.url)

    def processed_urls(self) -> set[str]:
        """Return the set of all processed URLs."""
        return set(self._data.get("processed", {}).keys())

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _load(self) -> dict[str, Any]:
        """Load state from disk, returning an empty structure if absent."""
        if not self._path.exists():
            logger.debug("State file not found at %s; starting empty", self._path)
            return {}
        try:
            with self._path.open(encoding="utf-8") as fh:
                data = json.load(fh)
            if not isinstance(data, dict):
                logger.warning("State file %s has unexpected format; starting empty", self._path)
                return {}
            logger.debug("Loaded %d processed entries", len(data.get("processed", {})))
            return data
        except (json.JSONDecodeError, OSError) as exc:
            logger.warning("Could not read state file %s: %s; starting empty", self._path, exc)
            return {}

    def _save(self) -> None:
        """Write state to disk atomically."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        # Write to a sibling temp file then rename — atomic on POSIX.
        fd, tmp = tempfile.mkstemp(dir=self._path.parent, suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(self._data, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
            os.replace(tmp, self._path)
        except Exception:
            # Best-effort cleanup of the temp file on failure.
            with contextlib.suppress(OSError):
                os.unlink(tmp)
            raise
