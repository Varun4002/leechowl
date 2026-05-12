import subprocess
from pathlib import Path

from .base import BaseDownloader


class TorrentDownloader(BaseDownloader):
    def __init__(self, dest_dir: Path, quiet: bool = False):
        super().__init__(dest_dir, quiet)
        self._aria2c = self._find_aria2c()

    def _find_aria2c(self) -> str | None:
        import shutil
        return shutil.which("aria2c")

    def download(self, url: str) -> bool:
        if not self._aria2c:
            self.log("aria2c not found. install it: sudo apt install aria2")
            return False

        self.log("torrent download start...")
        try:
            subprocess.run(
                [
                    self._aria2c,
                    "--dir", str(self.dest_dir),
                    "--seed-time=0",
                    "--console-log-level=warn",
                    url,
                ],
                check=True,
            )
            self.log("done")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"torrent download failed: {e}")
            return False
