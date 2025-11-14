thonimport asyncio
import json
import logging
from pathlib import Path

from extractors.youtube_parser import fetch_video_info
from outputs.exporters import export_results

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
URLS_FILE = DATA_DIR / "urls.sample.txt"
OUTPUT_FILE = DATA_DIR / "sample_output.json"

async def process_url(url: str, quality: str, fmt: str) -> dict:
    try:
        info = await fetch_video_info(url, quality=quality, file_format=fmt)
        return info
    except Exception as e:
        logging.error(f"Failed to process {url}: {e}")
        return {"url": url, "error": str(e)}

async def main():
    quality = "best"
    file_format = "mp4"

    if not URLS_FILE.exists():
        logging.error("URL list file not found.")
        return

    with open(URLS_FILE, "r") as f:
        urls = [u.strip() for u in f.readlines() if u.strip()]

    tasks = [process_url(url, quality, file_format) for url in urls]
    results = await asyncio.gather(*tasks)

    await export_results(results, OUTPUT_FILE)
    logging.info(f"Results exported to {OUTPUT_FILE}")

if __name__ == "__main__":
    asyncio.run(main())