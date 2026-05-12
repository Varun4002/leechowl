from pathlib import Path

from leechowl.constants import DIR_NAMES
from leechowl.downloaders import MediaDownloader, DirectDownloader, TorrentDownloader
from leechowl.utils import classify_url


class Leechowl:
    def __init__(self, base_dir: Path, quiet: bool = False):
        self.base_dir = base_dir.resolve()
        self.quiet = quiet

        self.media_dir = self.base_dir / DIR_NAMES["yt_video"]
        self.files_dir = self.base_dir / DIR_NAMES["files"]
        self.torrents_dir = self.base_dir / DIR_NAMES["torrents"]

        self.media_dir.mkdir(parents=True, exist_ok=True)
        self.files_dir.mkdir(parents=True, exist_ok=True)
        self.torrents_dir.mkdir(parents=True, exist_ok=True)

        self._media_dl = MediaDownloader(self.media_dir, quiet=quiet)
        self._direct_dl = DirectDownloader(self.files_dir, quiet=quiet)
        self._torrent_dl = TorrentDownloader(self.torrents_dir, quiet=quiet)

    def log(self, msg: str):
        if not self.quiet:
            print(f"  {msg}")

    def download(self, url: str, format_code: str | None = None, audio_format: str | None = None) -> bool:
        url = url.strip()
        if not url:
            return False

        url_type = classify_url(url)

        if audio_format:
            return self._media_dl.download_audio(url, audio_format)

        if format_code:
            return self._media_dl.download_format(url, format_code)

        if url_type == "torrent":
            return self._torrent_dl.download(url)

        if url_type == "direct":
            return self._direct_dl.download(url)

        if not self._media_dl.try_download(url):
            return self._direct_dl.download(url)

        return True

    def list_formats(self, url: str) -> bool:
        return self._media_dl.list_formats(url)
