"""
    CLI tool to download youtube videos into current directory.

    Usage

        python cli.py -U https://youtu.be/Rc5K5zkwOcM https://youtu.be/Jpnj4rLlEvI

"""
import argparse
import logging

import yt_dlp


logger = logging.getLogger(__name__)


def get_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-U",
        "--url",
        type=str,
        nargs="+",
        required=True,
    )

    parser.add_argument(
        "--log-level",
        default="info",
        choices=(
            "debug",
            "info",
            "warning",
            "error",
            "critical",
        ),
    )

    parser.add_argument(
        "--log-format",
        default="%(message)s",
    )

    return parser


def download_youtube_video(urls: list[str]) -> None:
    with yt_dlp.YoutubeDL(options := {}) as ydl:
        ydl.download(urls)


def main():
    cli = get_cli()
    parsed_args = cli.parse_args()

    logging.basicConfig(
        level=getattr(logging, parsed_args.log_level.upper()),
        format=parsed_args.log_format,
    )
    logger.warning(
        "logger configured with level [%s] and format [%s]",
        parsed_args.log_level,
        parsed_args.log_format,
    )

    logger.info("going to download youtube videos [%s]", parsed_args.url)
    download_youtube_video(parsed_args.url)

    logger.info("download completed")


if __name__ == "__main__":
    main()
