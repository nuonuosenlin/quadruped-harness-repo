"""Fetch the pinned Go2 meshes and policy; no Git/Isaac installation is needed."""
from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import urllib.request


def fetch_assets(asset_dir: Path, *, verify_only: bool = False) -> None:
    project = Path(__file__).resolve().parents[1]
    manifest = json.loads((project / "assets.lock.json").read_text(encoding="utf-8"))
    asset_dir = asset_dir.resolve()

    def process(entry: dict) -> str:
        path = (asset_dir / entry["path"]).resolve()
        if not path.is_relative_to(asset_dir):
            raise ValueError("Asset manifest contains a path outside the asset directory")
        if path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]:
            return f"OK {entry['path']}"
        if verify_only:
            raise RuntimeError(f"Missing or corrupted asset: {path}; rerun without --verify")
        request = urllib.request.Request(entry["url"], headers={"User-Agent": "go2-harness-demo/0.1"})
        data = b""
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=60) as response:
                    data = response.read()
                break
            except Exception:
                if attempt == 2:
                    raise
        if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
            raise RuntimeError(f"Asset checksum mismatch: {entry['path']}")
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(path.name + ".download")
        temporary.write_bytes(data)
        temporary.replace(path)
        return f"FETCHED {entry['path']}"

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for result in executor.map(process, manifest["files"]):
            print(result)
    print(f"Verified {len(manifest['files'])} pinned files at {asset_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--asset-dir", type=Path, default=Path(__file__).resolve().parents[1] / "assets")
    parser.add_argument("--verify", action="store_true", help="Only verify existing files; never download")
    arguments = parser.parse_args()
    fetch_assets(arguments.asset_dir, verify_only=arguments.verify)
