import subprocess
from pathlib import Path

from .base import BaseDownloader


class MediaDownloader(BaseDownloader):
    def __init__(self, dest_dir: Path, quiet: bool = False):
        super().__init__(dest_dir, quiet)
        self._ytdlp = self._find_ytdlp()

    def _find_ytdlp(self) -> str | None:
        import shutil
        return shutil.which("yt-dlp")

    def list_formats(self, url: str) -> bool:
        if not self._ytdlp:
            print("yt-dlp not found", file=__import__("sys").stderr)
            return False

        result = subprocess.run(
            [self._ytdlp, "--list-formats", url],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            err = result.stderr.lower()
            if "unsupported url" in err:
                print("not a media URL -- no formats to list")
                return False
            print(result.stderr.strip(), file=__import__("sys").stderr)
            return False

        print(result.stdout)
        return True

    def download_format(self, url: str, format_code: str) -> bool:
        if not self._ytdlp:
            self.log("yt-dlp not found")
            return False

        self.log(f"downloading format {format_code}...")
        cmd = [
            self._ytdlp,
            "-o", f"{self.dest_dir}/%(title)s.%(ext)s",
            "-f", format_code,
            url,
        ]
        if self.quiet:
            cmd.insert(1, "-q")

        try:
            subprocess.run(cmd, check=True)
            self.log("done")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"download failed: {e}")
            return False

    def download_audio(self, url: str, audio_format: str) -> bool:
        if not self._ytdlp:
            self.log("yt-dlp not found")
            return False

        self.log(f"downloading as {audio_format}...")
        cmd = [
            self._ytdlp,
            "-x",
            "--audio-format", audio_format,
            "-o", f"{self.dest_dir}/%(title)s.%(ext)s",
            url,
        ]
        if self.quiet:
            cmd.insert(1, "-q")

        try:
            subprocess.run(cmd, check=True)
            self.log("done")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"audio download failed: {e}")
            return False

    def try_download(self, url: str) -> bool:
        if not self._ytdlp:
            return False

        self.log("checking URL type...")
        result = subprocess.run(
            [self._ytdlp, "--dump-json", url],
            capture_output=True,
            text=True,
            timeout=15,
        )

        if result.returncode != 0:
            err = result.stderr.lower()
            if "unsupported url" in err or "not a valid url" in err:
                return False
            self.log(f"yt-dlp failed: {result.stderr.strip()}")
            return False

        self.log("media detected")
        cmd = [
            self._ytdlp,
            "-o", f"{self.dest_dir}/%(title)s.%(ext)s",
            "--no-playlist",
            url,
        ]
        if self.quiet:
            cmd.insert(1, "-q")

        try:
            subprocess.run(cmd, check=True)
            self.log("done")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"download failed: {e}")
            return False

    def download(self, url: str) -> bool:
        return self.try_download(url)
