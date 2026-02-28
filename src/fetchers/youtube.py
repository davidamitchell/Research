"""YouTube transcript fetcher.

Supports:
- Fetching the latest N videos from a channel (via Atom feed)
- Fetching a single video by URL or video ID

Transcripts are retrieved via ``youtube-transcript-api``.  When transcripts are
blocked (common on cloud CI IPs) the fetcher falls back to the video description
sourced from the Atom feed entry.
"""

from __future__ import annotations

import re
import time
from typing import Any
from xml.etree import ElementTree as ET

import httpx

from src.fetchers import FetchedItem
from src.logger import get_logger

try:
    from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore[import-untyped]
except ImportError:  # pragma: no cover
    YouTubeTranscriptApi = None  # type: ignore[assignment,misc]

logger = get_logger(__name__)

_CHANNEL_FEED_URL = "https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
_VIDEO_WATCH_URL = "https://www.youtube.com/watch?v={video_id}"

_RETRY_ATTEMPTS = 3
_RETRY_BACKOFF = 2.0  # seconds; doubles on each retry

_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
    "media": "http://search.yahoo.com/mrss/",
}


def _video_id_from_url(url: str) -> str:
    """Extract the YouTube video ID from a URL or return as-is if bare ID."""
    patterns = [
        r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})",
    ]
    for pat in patterns:
        m = re.search(pat, url)
        if m:
            return m.group(1)
    # Assume the input is already a raw video ID
    return url


def _fetch_with_retry(url: str, client: httpx.Client) -> httpx.Response:
    """GET *url* with exponential-backoff retry on network errors."""
    delay = _RETRY_BACKOFF
    last_exc: Exception = RuntimeError("unreachable")
    for attempt in range(1, _RETRY_ATTEMPTS + 1):
        try:
            response = client.get(url, follow_redirects=True, timeout=15)
            response.raise_for_status()
            return response
        except (httpx.HTTPError, httpx.TransportError) as exc:
            last_exc = exc
            if attempt < _RETRY_ATTEMPTS:
                logger.warning(
                    "Attempt %d/%d failed for %s: %s — retrying in %.0fs",
                    attempt,
                    _RETRY_ATTEMPTS,
                    url,
                    exc,
                    delay,
                )
                time.sleep(delay)
                delay *= 2
    raise last_exc


def _fetch_transcript(video_id: str) -> str | None:
    """Return the full transcript text for *video_id*, or None on failure."""
    if YouTubeTranscriptApi is None:
        logger.warning("youtube-transcript-api not installed; transcript unavailable")
        return None
    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        return " ".join(snippet.text for snippet in transcript)
    except Exception as exc:  # noqa: BLE001
        logger.warning("Transcript unavailable for %s: %s", video_id, exc)
        return None


def _parse_channel_feed(xml_text: str, max_videos: int) -> list[dict[str, Any]]:
    """Parse a YouTube channel Atom feed and return up to *max_videos* entries."""
    root = ET.fromstring(xml_text)
    entries: list[dict[str, Any]] = []
    for entry in root.findall("atom:entry", _NS)[:max_videos]:
        video_id_el = entry.find("yt:videoId", _NS)
        title_el = entry.find("atom:title", _NS)
        link_el = entry.find("atom:link", _NS)
        desc_el = entry.find("media:group/media:description", _NS)

        video_id = video_id_el.text if video_id_el is not None else None
        title = title_el.text if title_el is not None else "(no title)"
        url = (link_el.get("href") if link_el is not None else None) or (
            _VIDEO_WATCH_URL.format(video_id=video_id) if video_id else ""
        )
        description = desc_el.text if desc_el is not None else ""

        entries.append(
            {
                "video_id": video_id,
                "title": title,
                "url": url,
                "description": description or "",
            }
        )
    return entries


class YouTubeFetcher:
    """Fetch transcripts from a YouTube channel or individual videos."""

    def __init__(
        self,
        channel_id: str | None = None,
        max_videos: int = 5,
        video_urls: list[str] | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.channel_id = channel_id
        self.max_videos = max_videos
        self.video_urls = video_urls or []
        self._client = http_client or httpx.Client()

    def fetch(self) -> list[FetchedItem]:
        """Fetch transcripts and return a list of FetchedItem objects."""
        items: list[FetchedItem] = []

        # Channel-based fetch
        if self.channel_id:
            items.extend(self._fetch_channel())

        # Individual video fetch
        for url in self.video_urls:
            item = self._fetch_video(url)
            if item:
                items.append(item)

        return items

    def _fetch_channel(self) -> list[FetchedItem]:
        """Fetch the latest videos from the configured channel."""
        feed_url = _CHANNEL_FEED_URL.format(channel_id=self.channel_id)
        try:
            response = _fetch_with_retry(feed_url, self._client)
        except Exception as exc:  # noqa: BLE001
            logger.error("Failed to fetch channel feed %s: %s", self.channel_id, exc)
            return []

        entries = _parse_channel_feed(response.text, self.max_videos)
        results: list[FetchedItem] = []
        for entry in entries:
            video_id = entry["video_id"]
            if not video_id:
                continue
            content = _fetch_transcript(video_id) or entry["description"]
            if not content:
                logger.warning("No content for video %s — skipping", video_id)
                continue
            results.append(
                FetchedItem(
                    url=entry["url"],
                    title=entry["title"],
                    content=content,
                    source_id=self.channel_id or video_id,
                )
            )
        return results

    def _fetch_video(self, url: str) -> FetchedItem | None:
        """Fetch transcript for a single video URL."""
        video_id = _video_id_from_url(url)
        content = _fetch_transcript(video_id)
        if not content:
            # Fall back: try fetching the watch page description
            try:
                resp = _fetch_with_retry(_VIDEO_WATCH_URL.format(video_id=video_id), self._client)
                # Extract og:description meta tag as a rough description fallback
                m = re.search(r'<meta name="description" content="([^"]+)"', resp.text)
                content = m.group(1) if m else ""
            except Exception as exc:  # noqa: BLE001
                logger.warning("Description fallback failed for %s: %s", video_id, exc)
                content = ""

        if not content:
            logger.warning("No content for video %s — skipping", video_id)
            return None

        return FetchedItem(
            url=url,
            title=video_id,  # title not known without an API call
            content=content,
            source_id=video_id,
        )
