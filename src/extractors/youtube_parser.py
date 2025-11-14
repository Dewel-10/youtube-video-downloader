thonimport asyncio
import logging
from yt_dlp import YoutubeDL

from .format_utils import choose_format

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

async def fetch_video_info(url: str, quality: str = "best", file_format: str = "mp4") -> dict:
    logging.info(f"Fetching info for: {url}")

    ydl_opts = {
        "quiet": True,
        "skip_download": False,
        "format": choose_format(quality, file_format),
        "outtmpl": "%(title)s.%(ext)s",
    }

    loop = asyncio.get_event_loop()
    info = await loop.run_in_executor(None, lambda: _fetch_sync(url, ydl_opts))
    return info

def _fetch_sync(url: str, ydl_opts: dict) -> dict:
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return {
            "title": info.get("title"),
            "downloadURL": ydl.prepare_filename(info)
        }