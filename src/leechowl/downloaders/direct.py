import subprocess
from pathlib import Path

from .base import BaseDownloader


class DirectDownloader(BaseDownloader):
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

        self.log("direct download start...")
        try:
            subprocess.run(
                [
                    self._aria2c,
                    "--dir", str(self.dest_dir),
                    "--console-log-level=warn",
                    "--continue=true",
                    "--max-connection-per-server=4",
                    "--split=4",
                    "--min-split-size=1M",
                    url,
                ],
                check=True,
            )
            self.log("done")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"direct download failed: {e}")
            return False
