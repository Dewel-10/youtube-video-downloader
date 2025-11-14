thonimport aiofiles
import json
from pathlib import Path

async def export_results(results: list, output_path: Path):
    async with aiofiles.open(output_path, "w") as f:
        await f.write(json.dumps(results, indent=4))