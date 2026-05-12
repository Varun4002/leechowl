from abc import ABC, abstractmethod
from pathlib import Path


class BaseDownloader(ABC):
    def __init__(self, dest_dir: Path, quiet: bool = False):
        self.dest_dir = dest_dir
        self.quiet = quiet

    def log(self, msg: str):
        if not self.quiet:
            print(f"  {msg}")

    @abstractmethod
    def download(self, url: str) -> bool:
        ...
