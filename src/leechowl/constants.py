from pathlib import Path

DOWNLOAD_ROOT = Path.home() / "leech_downloads"

DIR_NAMES = {
    "yt_music": "yt-music",
    "yt_video": "yt-video",
    "files": "files",
    "torrents": "torrents",
}

FILE_EXTENSIONS = {
    ".zip", ".tar", ".tar.gz", ".tgz", ".tar.bz2", ".tar.xz",
    ".gz", ".bz2", ".xz", ".7z", ".rar",
    ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
    ".mp3", ".mp4", ".avi", ".mkv", ".mov", ".flv", ".wmv",
    ".iso", ".img", ".bin",
    ".deb", ".rpm", ".appimage", ".exe", ".msi",
    ".dmg", ".pkg",
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg",
    ".apk", ".aab",
    ".whl", ".tar.gz",
    ".csv", ".json", ".xml", ".yaml", ".toml",
}
