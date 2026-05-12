from urllib.parse import urlparse

from leechowl.constants import FILE_EXTENSIONS


def classify_url(url: str) -> str:
    if url.startswith("magnet:"):
        return "torrent"

    path = urlparse(url).path.lower()
    if path.endswith(".torrent"):
        return "torrent"

    for ext in FILE_EXTENSIONS:
        if path.endswith(ext):
            return "direct"

    return "unknown"
