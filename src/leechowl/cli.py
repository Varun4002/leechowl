import argparse
import sys
from pathlib import Path

from .core import Leechowl

DEFAULT_DOWNLOAD_DIR = Path.home() / "Downloads" / "leechowl"


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        prog="leechowl",
        description="Universal CLI downloader - videos, files, torrents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  leechowl https://youtube.com/watch?v=xxx           auto-detect best quality
  leechowl https://example.com/file.zip              direct download
  leechowl magnet:?xt=urn:btih:xxx                   torrent download
  leechowl -l https://youtube.com/watch?v=xxx        list available formats
  leechowl -c 22 https://youtube.com/watch?v=xxx     download specific format
  leechowl -a mp3 https://youtu.be/xxx               extract audio as mp3
  leechowl -f urls.txt                               batch from file
  leechowl -o ~/videos https://youtu.be/xxx          custom output dir
        """,
    )
    parser.add_argument(
        "urls",
        nargs="*",
        metavar="URL",
        help="URL(s) to download",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_DOWNLOAD_DIR,
        help=f"download directory (default: {DEFAULT_DOWNLOAD_DIR})",
    )
    parser.add_argument(
        "-f",
        "--file",
        type=Path,
        help="read URLs from file (one per line)",
    )
    parser.add_argument(
        "-l",
        "--list-formats",
        action="store_true",
        help="list available formats for media URL",
    )
    parser.add_argument(
        "-c",
        "--format-code",
        help="download with specific format code (use -l to see codes)",
    )
    parser.add_argument(
        "-a",
        "--audio-format",
        metavar="FMT",
        choices=["mp3", "m4a", "opus", "flac", "wav"],
        help="extract audio and convert to format (mp3, m4a, opus, flac, wav)",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="suppress progress output",
    )
    return parser.parse_args(argv)


def main():
    args = parse_args()

    urls = list(args.urls)
    if args.file:
        if not args.file.exists():
            print(f"error: file not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(args.file) as f:
            urls.extend(
                line.strip() for line in f
                if line.strip() and not line.startswith("#")
            )

    if not urls:
        print("error: no URLs provided", file=sys.stderr)
        sys.exit(1)

    leechowl = Leechowl(args.output, quiet=args.quiet)

    if args.list_formats:
        for url in urls:
            if not leechowl.list_formats(url):
                sys.exit(1)
        sys.exit(0)

    exit_code = 0
    for i, url in enumerate(urls):
        if len(urls) > 1:
            leechowl.log(f"[{i + 1}/{len(urls)}] {url}")
        if not leechowl.download(url, format_code=args.format_code, audio_format=args.audio_format):
            exit_code = 1

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
