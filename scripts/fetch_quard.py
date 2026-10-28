"""Fetch small, hash-locked QUARD clips without downloading whole task archives."""
from __future__ import annotations

import argparse
import concurrent.futures
import errno
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import ssl
import tarfile
import tempfile
import time
import urllib.error
import urllib.request


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LOCK = ROOT / "datasets/quard.lock.json"
DEFAULT_DATA_DIR = ROOT / "data/quard"
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_DECOMPRESSED_BYTES = 2 * 1024 * 1024 * 1024
DEFAULT_DOWNLOAD_BYTES = 128 * 1024 * 1024


class DatasetFetchError(RuntimeError):
    """A clip is missing, corrupt, or cannot be downloaded within its budget."""


class DownloadLimitError(DatasetFetchError):
    pass


def _relative_path(value: str) -> PurePosixPath:
    if (not isinstance(value, str) or not value or "\\" in value or "\0" in value
            or value.startswith("/") or ".." in value.split("/")):
        raise DatasetFetchError(f"Unsafe dataset path: {value!r}")
    path = PurePosixPath(value)
    if path.is_absolute() or path == PurePosixPath("."):
        raise DatasetFetchError(f"Unsafe dataset path: {value!r}")
    return path


def _destination(directory: Path, value: str) -> Path:
    path = (directory / _relative_path(value)).resolve()
    if not path.is_relative_to(directory):
        raise DatasetFetchError(f"Dataset path escapes the data directory: {value!r}")
    return path


def _entries(task: dict) -> dict[str, dict]:
    task_id, episode_id = task.get("task_id"), task.get("episode_id")
    if (not isinstance(task_id, str) or not re.fullmatch(r"[a-z0-9_]+", task_id)
            or not isinstance(episode_id, str) or not re.fullmatch(r"[0-9]+", episode_id)):
        raise DatasetFetchError("Invalid task or episode identifier in QUARD lock")
    entries = {}
    for entry in task.get("files", []):
        relative = _relative_path(entry.get("path"))
        if relative.parts[:2] != (task_id, episode_id):
            raise DatasetFetchError(f"Locked file belongs to another task/episode: {relative}")
        size, digest = entry.get("bytes"), entry.get("sha256")
        if (isinstance(size, bool) or not isinstance(size, int) or not 0 < size <= MAX_FILE_BYTES
                or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            raise DatasetFetchError(f"Invalid file size or SHA-256 in QUARD lock: {relative}")
        path = relative.as_posix()
        if path in entries:
            raise DatasetFetchError(f"Duplicate locked QUARD file: {path}")
        entries[path] = entry
    if not entries:
        raise DatasetFetchError(f"No sample files locked for task {task_id}")
    return entries


def _source_paths(task: dict, entries: dict[str, dict]) -> dict[str, str]:
    """Map explicit source archive paths to canonical local file paths."""
    archive_root = _relative_path(task.get("archive", {}).get("root", task["task_id"]))
    if len(archive_root.parts) != 1:
        raise DatasetFetchError("Archive root must be one directory name")
    paths = {}
    for local_path, entry in entries.items():
        source = _relative_path(entry.get("source_path", local_path))
        if source.parts[:2] != (archive_root.as_posix(), task["episode_id"]):
            raise DatasetFetchError(f"Source file belongs to another task/episode: {source}")
        source_path = source.as_posix()
        if source_path in paths:
            raise DatasetFetchError(f"Duplicate locked QUARD source path: {source_path}")
        paths[source_path] = local_path
    return paths


def load_lock(lock_path: Path = DEFAULT_LOCK) -> dict:
    lock = json.loads(Path(lock_path).read_text(encoding="utf-8"))
    if lock.get("schema_version") != 1 or not isinstance(lock.get("tasks"), list):
        raise DatasetFetchError("Unsupported QUARD lock format")
    ids = set()
    for task in lock["tasks"]:
        _source_paths(task, _entries(task))
        task_id = task["task_id"]
        if task_id in ids:
            raise DatasetFetchError(f"Duplicate task in QUARD lock: {task_id}")
        ids.add(task_id)
        if not isinstance(task.get("archive", {}).get("url"), str):
            raise DatasetFetchError(f"Missing source archive URL for {task_id}")
    if not ids:
        raise DatasetFetchError("QUARD lock contains no tasks")
    return lock


def select_tasks(lock: dict, task_ids: list[str] | None = None) -> list[dict]:
    if not task_ids or task_ids == ["all"]:
        return lock["tasks"]
    lookup = {task["task_id"]: task for task in lock["tasks"]}
    unknown = set(task_ids) - lookup.keys()
    if unknown:
        raise DatasetFetchError("Unknown QUARD task(s): " + ", ".join(sorted(unknown)))
    return [lookup[task_id] for task_id in dict.fromkeys(task_ids)]


def _verified(path: Path, entry: dict) -> bool:
    return (path.is_file() and path.stat().st_size == entry["bytes"]
            and hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"])


class _BoundedReader:
    def __init__(self, response, limit: int):
        self.response, self.limit, self.bytes_read = response, limit, 0

    def read(self, size: int = -1) -> bytes:
        remaining = self.limit - self.bytes_read
        if remaining <= 0:
            raise DownloadLimitError(
                f"Compressed download limit ({self.limit / 1024**2:g} MiB) reached; "
                "increase --max-download-mb for this task"
            )
        size = min(remaining, size) if size >= 0 else remaining
        result = self.response.read(size)
        self.bytes_read += len(result)
        return result


def fetch_task(task: dict, data_dir: Path, *, verify_only: bool = False,
               max_download_bytes: int = DEFAULT_DOWNLOAD_BYTES, opener=None) -> dict:
    """Read only the source archive prefix needed for the locked member files.

    A pinned archive revision and HTTPS identify the source. Individual file
    SHA-256 values are checked; a partial archive cannot verify its whole hash.
    """
    if isinstance(max_download_bytes, bool) or not isinstance(max_download_bytes, int) or max_download_bytes <= 0:
        raise DatasetFetchError("Download budget must be a positive number of bytes")
    directory = Path(data_dir).resolve()
    entries = _entries(task)
    source_paths = _source_paths(task, entries)
    destinations = {name: _destination(directory, name) for name in entries}
    missing = {name for name, entry in entries.items() if not _verified(destinations[name], entry)}
    result = {"task_id": task["task_id"], "files_verified": len(entries),
              "download_bytes": 0, "full_archive_sha256_verified": False}
    if not missing:
        result["status"] = "verified"
        return result
    if verify_only:
        raise DatasetFetchError(
            f"Missing or corrupt QUARD sample for {task['task_id']}: {sorted(missing)[0]}; "
            "run python scripts/fetch_quard.py without --verify"
        )
    source = task["archive"]["url"]
    request = urllib.request.Request(source, headers={
        "User-Agent": "go2-harness-quard-samples/0.1",
        "Range": f"bytes=0-{max_download_bytes - 1}",
    })
    open_source = opener or urllib.request.urlopen
    try:
        with open_source(request, timeout=60) as response:
            reader = _BoundedReader(response, max_download_bytes)
            with tarfile.open(fileobj=reader, mode="r|gz") as archive:
                for member in archive:
                    relative = _relative_path(member.name).as_posix()
                    if member.issym() or member.islnk():
                        raise DatasetFetchError(f"Archive links are not supported: {member.name}")
                    if member.offset_data + member.size > MAX_DECOMPRESSED_BYTES:
                        raise DownloadLimitError("Decompressed archive scan limit reached")
                    local_path = source_paths.get(relative)
                    if local_path not in missing:
                        continue
                    entry = entries[local_path]
                    if not member.isfile() or member.size != entry["bytes"] or member.size > MAX_FILE_BYTES:
                        raise DatasetFetchError(f"Unexpected source member type/size: {relative}")
                    stream = archive.extractfile(member)
                    if stream is None:
                        raise DatasetFetchError(f"Cannot read source member: {relative}")
                    content = stream.read(MAX_FILE_BYTES + 1)
                    if (len(content) != entry["bytes"]
                            or hashlib.sha256(content).hexdigest() != entry["sha256"]):
                        raise DatasetFetchError(f"QUARD sample SHA-256 mismatch: {relative}")
                    destination = destinations[local_path]
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    # NamedTemporaryFile avoids following a pre-existing temporary symlink.
                    with tempfile.NamedTemporaryFile(dir=destination.parent, prefix=".quard-", delete=False) as temporary:
                        temporary_path = Path(temporary.name)
                        try:
                            temporary.write(content)
                            temporary.flush()
                            temporary.close()
                            temporary_path.replace(destination)
                        finally:
                            temporary_path.unlink(missing_ok=True)
                    missing.remove(local_path)
                    if not missing:
                        break
            result["download_bytes"] = reader.bytes_read
    except (tarfile.TarError, EOFError) as error:
        raise DatasetFetchError(f"Incomplete or invalid QUARD source archive: {task['task_id']}: {error}") from error
    if missing:
        raise DatasetFetchError(f"Source archive is missing locked sample member: {sorted(missing)[0]}")
    result["status"] = "fetched"
    return result


def _transient_network_error(error: OSError) -> bool:
    if isinstance(error, urllib.error.HTTPError):
        return error.code in {408, 425, 429, 500, 502, 503, 504}
    if isinstance(error, urllib.error.URLError):
        return True
    if isinstance(error, (TimeoutError, ConnectionError, ssl.SSLEOFError, ssl.SSLZeroReturnError)):
        return True
    return error.errno in {errno.ENETUNREACH, errno.EHOSTUNREACH, errno.ECONNRESET,
                           errno.ECONNABORTED, errno.ETIMEDOUT, errno.EPIPE}


def fetch_task_with_retries(task: dict, data_dir: Path, *, verify_only: bool = False,
                            max_download_bytes: int = DEFAULT_DOWNLOAD_BYTES,
                            opener=None, attempts: int = 3, sleeper=None) -> dict:
    """Retry transient transport failures; keep verified files between attempts."""
    if isinstance(attempts, bool) or not isinstance(attempts, int) or not 1 <= attempts <= 3:
        raise DatasetFetchError("Network attempts must be between 1 and 3")
    pause = sleeper or time.sleep
    for attempt in range(attempts):
        try:
            return fetch_task(task, data_dir, verify_only=verify_only,
                              max_download_bytes=max_download_bytes, opener=opener)
        except OSError as error:
            if verify_only or not _transient_network_error(error) or attempt + 1 == attempts:
                raise
            print(f"RETRY {task['task_id']}: transient {type(error).__name__}; "
                  f"attempt {attempt + 2}/{attempts}", flush=True)
            pause(0.5 * (attempt + 1))
    raise AssertionError("unreachable")


def fetch_dataset(data_dir: Path = DEFAULT_DATA_DIR, *, lock_path: Path = DEFAULT_LOCK,
                  task_ids: list[str] | None = None, verify_only: bool = False,
                  max_download_bytes: int = DEFAULT_DOWNLOAD_BYTES, workers: int = 3) -> list[dict]:
    if not 1 <= workers <= 8:
        raise DatasetFetchError("--workers must be between 1 and 8")
    tasks = select_tasks(load_lock(lock_path), task_ids)

    def process(task):
        result = fetch_task_with_retries(task, data_dir, verify_only=verify_only,
                                        max_download_bytes=max_download_bytes)
        print(f"{result['status'].upper()} {task['task_id']}: {result['files_verified']} files, "
              f"{result['download_bytes'] / 1024**2:.2f} MiB downloaded", flush=True)
        return result

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(process, tasks))
    print(f"Verified {len(results)} QUARD clips / {sum(row['files_verified'] for row in results)} files. "
          "Per-file SHA-256 checked; full archive hashes are not checked for prefix downloads.", flush=True)
    return results


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     epilog="Transient network failures are retried up to 3 attempts; verified files are reused.")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--lock-path", type=Path, default=DEFAULT_LOCK)
    parser.add_argument("--task", action="append", help="repeat to select tasks; default: all locked sample tasks")
    parser.add_argument("--verify", action="store_true", help="verify local sample files without network access")
    parser.add_argument("--list", action="store_true", help="list task archive sizes and local sample status without downloading")
    parser.add_argument("--max-download-mb", type=int, default=128, help="compressed prefix download limit per task attempt (MiB)")
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args(argv)
    try:
        if args.max_download_mb <= 0:
            raise DatasetFetchError("--max-download-mb must be positive")
        if args.list:
            directory = args.data_dir.resolve()
            for task in select_tasks(load_lock(args.lock_path), args.task):
                entries = _entries(task)
                valid = sum(_verified(_destination(directory, path), entry) for path, entry in entries.items())
                archive_bytes = task["archive"].get("bytes", 0)
                print(f"{task['task_id']} | {task['category']} | archive {archive_bytes / 1024**3:.2f} GiB "
                      f"| sample {valid}/{len(entries)} files")
            return 0
        fetch_dataset(args.data_dir, lock_path=args.lock_path, task_ids=args.task, verify_only=args.verify,
                      max_download_bytes=args.max_download_mb * 1024**2, workers=args.workers)
        return 0
    except (DatasetFetchError, OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(1, f"QUARD sample error: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
