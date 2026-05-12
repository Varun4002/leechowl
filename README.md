<![CDATA[
<div align="center">

```
                ,     ,
               (\____/)
                (_''_)
                 (oo)
        __,.--'" ":--'":.
       <'._ _  _.' _ _.'>
        _\_ `' `' '` '_)
   __,-' _ _ _  _,_ <_
Am--'""--'""""--'"""--'--'
```

# leechowl

**Universal CLI downloader — videos, direct files, and torrents.**

[![Python](https://img.shields.io/badge/python-%3E=3.10-2d2b3e?style=flat-square)](https://python.org)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-required-2d2b3e?style=flat-square)](https://github.com/yt-dlp/yt-dlp)
[![aria2c](https://img.shields.io/badge/aria2c-required-2d2b3e?style=flat-square)](https://github.com/aria2/aria2)

</div>

Leechowl silently swoops in and grabs whatever you throw at it — YouTube videos, direct files, magnet links, `.torrent` files. One command, no friction.

## Requirements

| Tool | Purpose |
|---|---|
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | Media & audio downloads |
| [aria2c](https://github.com/aria2/aria2) | Direct file & torrent downloads |

```bash
sudo apt install yt-dlp aria2
```

## Install

```bash
git clone https://github.com/Varun4002/leechowl ~/projects/leechowl
pip install -e ~/projects/leechowl
```

Or run directly without install:

```bash
python -m leechowl https://...
```

## Usage

```text
leechowl [options] <URL> [URL ...]
```

### Auto-detect best quality

```bash
leechowl https://youtube.com/watch?v=dQw4w9WgXcQ
```

Leechowl probes the URL with yt-dlp first. If it's media, it downloads the best stream. Falls back to aria2c for direct files.

### Format selection

```bash
leechowl -l https://youtube.com/watch?v=xxx       # list available formats
leechowl -c 22 https://youtube.com/watch?v=xxx    # download specific format
```

### Audio extraction

```bash
leechowl -a mp3 https://youtu.be/xxx
leechowl -a opus https://youtu.be/xxx
```

Supported formats: `mp3`, `m4a`, `opus`, `flac`, `wav`.

### Torrents

```bash
leechowl magnet:?xt=urn:btih:xxxxxxxxxxxxxxxxxxxx
leechowl https://example.com/file.torrent
```

### Batch mode

```bash
leechowl -f urls.txt
```

One URL per line. Lines starting with `#` are skipped.

### Custom output directory

```bash
leechowl -o ~/videos https://youtu.be/xxx
```

Default: `~/Downloads/leechowl/`

## Output Structure

```
~/Downloads/leechowl/
├── yt-video/       # media downloads
├── files/          # direct file downloads
└── torrents/       # torrent downloads
```

## Options

| Flag | Description |
|---|---|
| `-o`, `--output` | Download directory (default: `~/Downloads/leechowl`) |
| `-f`, `--file` | Read URLs from file (one per line) |
| `-l`, `--list-formats` | List available formats for media URL |
| `-c`, `--format-code` | Download specific format code |
| `-a`, `--audio-format` | Extract audio (`mp3`, `m4a`, `opus`, `flac`, `wav`) |
| `-q`, `--quiet` | Suppress progress output |

## Project Structure

```
leechowl/
├── pyproject.toml
└── leechowl/
    ├── __init__.py          # exports Leechowl
    ├── __main__.py          # python -m leechowl
    ├── cli.py               # argparse CLI
    ├── constants.py         # file extensions, directory names
    ├── core.py              # Leechowl orchestrator
    ├── downloaders/
    │   ├── base.py          # abstract base downloader
    │   ├── media.py         # yt-dlp media downloads
    │   ├── direct.py        # aria2c direct downloads
    │   └── torrent.py       # aria2c torrent downloads
    └── utils/
        └── classify.py      # URL type detection
```
]]># leechowl
