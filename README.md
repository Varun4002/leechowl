<div align="center">

<pre>
             ,     ,
            (\____/)
             (_''_)
              (oo)
     __,.--'" ":--'":.
    <'._ _  _.' _ _.'>
     _\_ `' `' '` '_)
__,-' _ _ _  _,_ <_
Am--'""--'""""--'"""--'--'
</pre>

# ⚡ leechowl

**Universal CLI downloader — videos, direct files, and torrents.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![yt-dlp](https://img.shields.io/badge/yt--dlp-Required-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://github.com/yt-dlp/yt-dlp)
[![aria2](https://img.shields.io/badge/aria2-Required-00ADD8?style=for-the-badge&logo=aria&logoColor=white)](https://github.com/aria2/aria2)
[![MIT License](https://img.shields.io/badge/License-MIT-2d2b3e?style=for-the-badge)](LICENSE)
[![Linux](https://img.shields.io/badge/Platform-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)]()

<br>

> **Leechowl silently swoops in and grabs whatever you throw at it.**  
> YouTube videos, direct files, magnet links, `.torrent` files — one command, no friction.

---

<br>



## 🚀 Features

</div>

| | Feature | |
|---|---|---|
| 🎬 | **Media downloads** — yt-dlp powered, auto-selects best quality | 🎬 |
| 🔊 | **Audio extraction** — MP3, OPUS, FLAC, WAV, M4A | 🔊 |
| 📁 | **Direct file download** — aria2c for fast, resumable downloads | 📁 |
| 🧲 | **Torrent support** — magnet links & `.torrent` files | 🧲 |
| 📋 | **Batch mode** — read URLs from a file, one per line | 📋 |
| 🎯 | **Format selection** — list & pick specific format codes | 🎯 |

<div align="center">

<br>



## 📦 Requirements

</div>

| Tool | Purpose | Install |
|---|---|---|
| <kbd>yt-dlp</kbd> | Media & audio downloads | `sudo apt install yt-dlp` |
| <kbd>aria2c</kbd> | Direct file & torrent downloads | `sudo apt install aria2` |

<div align="center">

## 🔧 Install

</div>

```bash
git clone https://github.com/Varun4002/leechowl ~/projects/leechowl
pip install -e ~/projects/leechowl
```

Or run directly without installing:

```bash
python -m leechowl https://...
```

<div align="center">

## 🎯 Usage

</div>

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

Supported formats: <kbd>mp3</kbd>, <kbd>m4a</kbd>, <kbd>opus</kbd>, <kbd>flac</kbd>, <kbd>wav</kbd>

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

Default: <kbd>~/Downloads/leechowl/</kbd>

<div align="center">

## ⚙️ Options

</div>

| Flag | Description |
|---|---|
| <kbd>-o</kbd>, <kbd>--output</kbd> | Download directory (default: `~/Downloads/leechowl`) |
| <kbd>-f</kbd>, <kbd>--file</kbd> | Read URLs from file (one per line) |
| <kbd>-l</kbd>, <kbd>--list-formats</kbd> | List available formats for media URL |
| <kbd>-c</kbd>, <kbd>--format-code</kbd> | Download specific format code |
| <kbd>-a</kbd>, <kbd>--audio-format</kbd> | Extract audio (`mp3`, `m4a`, `opus`, `flac`, `wav`) |
| <kbd>-q</kbd>, <kbd>--quiet</kbd> | Suppress progress output |

## 📂 Output Structure

```
~/Downloads/leechowl/
├── yt-video/       # media downloads
├── files/          # direct file downloads
└── torrents/       # torrent downloads
```

## 📁 Project Structure

```
leechowl/
├── .gitignore
├── pyproject.toml
├── README.md
└── src/
    └── leechowl/
        ├── __init__.py
        ├── __main__.py
        ├── cli.py
        ├── constants.py
        ├── core.py
        ├── downloaders/
        │   ├── __init__.py
        │   ├── base.py
        │   ├── direct.py
        │   ├── media.py
        │   └── torrent.py
        └── utils/
            ├── __init__.py
            └── classify.py
```

<div align="center">

---

<p>
  <sub>Built by <a href="https://github.com/Varun4002">Varun4002</a></sub>
</p>

</div>
