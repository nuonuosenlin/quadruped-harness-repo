"""Archive download tests use local streams; pytest never downloads QUARD data."""
import hashlib
from io import BytesIO
import json
import random
import tarfile
import urllib.error

import pytest

from scripts.fetch_quard import (
    DatasetFetchError, DownloadLimitError, fetch_task, fetch_task_with_retries, load_lock, main, select_tasks,
)


def make_archive(entries):
    buffer = BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
        for name, content in entries:
            member = tarfile.TarInfo(name)
            if isinstance(content, tarfile.TarInfo):
                archive.addfile(content)
            else:
                member.size = len(content)
                archive.addfile(member, BytesIO(content))
    return buffer.getvalue()


def make_task(files):
    return {"task_id": "go_to_red_cube", "category": "go_to", "episode_id": "000099",
            "archive": {"url": "https://example.invalid/source.tar.gz", "bytes": 10_000, "sha256": "a" * 64},
            "files": [{"path": name, "bytes": len(content), "sha256": hashlib.sha256(content).hexdigest()}
                      for name, content in files]}


def opener_for(content, requests=None):
    def open_source(request, *, timeout):
        if requests is not None:
            requests.append(request)
        return BytesIO(content)
    return open_source


def test_fetch_selects_locked_files_and_subsequent_verification_is_offline(tmp_path):
    wanted = [("go_to_red_cube/000099/info.csv", b"instruction\ngo to red cube\n"),
              ("go_to_red_cube/000099/image/000.png", b"real-image-bytes")]
    archive = make_archive([(wanted[0][0], wanted[0][1]), ("unlocked/extra.txt", b"ignore"), wanted[1]])
    requests = []
    task = make_task(wanted)
    result = fetch_task(task, tmp_path, opener=opener_for(archive, requests))
    assert result["status"] == "fetched" and result["files_verified"] == 2
    assert result["download_bytes"] > 0
    assert result["full_archive_sha256_verified"] is False
    assert requests[0].get_header("Range") == "bytes=0-134217727"
    assert not (tmp_path / "unlocked").exists()
    for name, content in wanted:
        assert (tmp_path / name).read_bytes() == content

    def must_not_open(*args, **kwargs):
        pytest.fail("Valid local samples must not perform network access")

    assert fetch_task(task, tmp_path, opener=must_not_open)["download_bytes"] == 0
    assert fetch_task(task, tmp_path, verify_only=True, opener=must_not_open)["status"] == "verified"


def test_corrupt_local_file_is_refetched_and_wrong_remote_hash_is_never_committed(tmp_path):
    name = "go_to_red_cube/000099/image/000.png"
    path = tmp_path / name
    path.parent.mkdir(parents=True)
    path.write_bytes(b"bad!")
    task = make_task([(name, b"good")])
    with pytest.raises(DatasetFetchError, match="SHA-256 mismatch"):
        fetch_task(task, tmp_path, opener=opener_for(make_archive([(name, b"evil")])))
    assert path.read_bytes() == b"bad!"
    assert not list(path.parent.glob(".quard-*"))
    assert fetch_task(task, tmp_path, opener=opener_for(make_archive([(name, b"good")])))["status"] == "fetched"
    assert path.read_bytes() == b"good"


def test_verify_missing_sample_is_actionable_without_network(tmp_path):
    task = make_task([("go_to_red_cube/000099/info.csv", b"csv")])
    with pytest.raises(DatasetFetchError, match="without --verify"):
        fetch_task(task, tmp_path, verify_only=True, opener=lambda *args, **kwargs: pytest.fail("network"))


def test_missing_archive_member_fails(tmp_path):
    task = make_task([("go_to_red_cube/000099/info.csv", b"csv")])
    with pytest.raises(DatasetFetchError, match="missing locked sample member"):
        fetch_task(task, tmp_path, opener=opener_for(make_archive([("other.csv", b"csv")])))


def test_fetch_stops_before_large_unused_archive_tail(tmp_path):
    name = "go_to_red_cube/000099/info.csv"
    task = make_task([(name, b"csv")])
    archive = make_archive([(name, b"csv"), ("unused.bin", random.Random(7).randbytes(256 * 1024))])
    result = fetch_task(task, tmp_path, opener=opener_for(archive))
    assert result["download_bytes"] < len(archive) // 4
    assert not (tmp_path / "unused.bin").exists()


def test_explicit_source_path_preserves_space_in_archive_but_writes_canonical_task_id(tmp_path):
    task_id = "go_through_green_rectangle_tunnel"
    archive_root = "go_through_green_rectangle tunnel"
    local_path = f"{task_id}/000422/image/000.png"
    source_path = f"{archive_root}/000422/image/000.png"
    content = b"original-frame"
    task = {"task_id": task_id, "category": "go_through", "episode_id": "000422",
            "archive": {"url": "https://example.invalid/tunnel.tar.gz", "root": archive_root},
            "files": [{"path": local_path, "source_path": source_path, "bytes": len(content),
                       "sha256": hashlib.sha256(content).hexdigest()}]}
    result = fetch_task(task, tmp_path, opener=opener_for(make_archive([(source_path, content)])))
    assert result["status"] == "fetched"
    assert (tmp_path / local_path).read_bytes() == content
    assert not (tmp_path / archive_root).exists()
    assert fetch_task(task, tmp_path, verify_only=True)["status"] == "verified"


@pytest.mark.parametrize("source_path", ["../outside", "wrong_task/000099/info.csv",
                                         "go_to_red_cube/999999/info.csv"])
def test_locked_source_path_must_match_explicit_archive_root_and_episode(tmp_path, source_path):
    task = make_task([("go_to_red_cube/000099/info.csv", b"csv")])
    task["files"][0]["source_path"] = source_path
    with pytest.raises(DatasetFetchError, match="Unsafe dataset path|another task/episode"):
        fetch_task(task, tmp_path, verify_only=True)


@pytest.mark.parametrize("name", ["../outside", "/absolute", "go_to_red_cube/../../outside", "bad\\path"])
def test_unsafe_archive_paths_are_rejected(tmp_path, name):
    task = make_task([("go_to_red_cube/000099/info.csv", b"csv")])
    with pytest.raises(DatasetFetchError, match="Unsafe dataset path"):
        fetch_task(task, tmp_path, opener=opener_for(make_archive([(name, b"bad")])))
    assert not (tmp_path / "outside").exists()


def test_symlinks_in_archive_and_output_directory_are_rejected(tmp_path):
    name = "go_to_red_cube/000099/info.csv"
    link = tarfile.TarInfo(name)
    link.type, link.linkname = tarfile.SYMTYPE, "/tmp/unwanted"
    task = make_task([(name, b"csv")])
    with pytest.raises(DatasetFetchError, match="Archive links"):
        fetch_task(task, tmp_path, opener=opener_for(make_archive([(name, link)])))
    outside = tmp_path.parent / "outside-quard-test"
    (tmp_path / "go_to_red_cube").symlink_to(outside, target_is_directory=True)
    with pytest.raises(DatasetFetchError, match="escapes the data directory"):
        fetch_task(task, tmp_path, verify_only=True)


def test_download_limit_is_enforced_even_when_server_ignores_range(tmp_path):
    name = "go_to_red_cube/000099/info.csv"
    task = make_task([(name, b"csv")])
    data = make_archive([("large.bin", bytes(range(256)) * 50), (name, b"csv")])
    class CountingResponse(BytesIO):
        bytes_delivered = 0

        def read(self, count=-1):
            value = super().read(count)
            self.bytes_delivered += len(value)
            return value

    source = CountingResponse(data)
    with pytest.raises(DownloadLimitError):
        fetch_task(task, tmp_path, max_download_bytes=100, opener=lambda *args, **kwargs: source)
    assert source.bytes_delivered == 100
    assert not (tmp_path / name).exists()


def test_lock_validation_rejects_duplicate_files_and_unknown_tasks(tmp_path):
    task = make_task([("go_to_red_cube/000099/info.csv", b"csv")])
    lock = {"schema_version": 1, "tasks": [task]}
    path = tmp_path / "lock.json"
    path.write_text(json.dumps(lock))
    assert select_tasks(load_lock(path), ["all"])[0]["task_id"] == "go_to_red_cube"
    with pytest.raises(DatasetFetchError, match="Unknown QUARD"):
        select_tasks(lock, ["not_available"])
    task["files"].append(task["files"][0])
    path.write_text(json.dumps(lock))
    with pytest.raises(DatasetFetchError, match="Duplicate locked"):
        load_lock(path)


def test_list_uses_only_local_data_and_prints_archive_and_sample_sizes(tmp_path, capsys):
    task = make_task([("go_to_red_cube/000099/info.csv", b"csv")])
    path = tmp_path / "lock.json"
    path.write_text(json.dumps({"schema_version": 1, "tasks": [task]}))
    assert main(["--list", "--data-dir", str(tmp_path / "data"), "--lock-path", str(path)]) == 0
    output = capsys.readouterr().out
    assert "go_to_red_cube" in output and "sample 0/1 files" in output


def test_transient_network_failures_retry_at_most_three_attempts_without_waiting_in_tests(tmp_path):
    name = "go_to_red_cube/000099/info.csv"
    task = make_task([(name, b"csv")])
    calls, delays = [], []

    def unreliable(request, *, timeout):
        calls.append(request)
        if len(calls) < 3:
            raise urllib.error.URLError("intermittent TLS EOF")
        return BytesIO(make_archive([(name, b"csv")]))

    result = fetch_task_with_retries(task, tmp_path, opener=unreliable, sleeper=delays.append)
    assert result["status"] == "fetched"
    assert len(calls) == 3 and delays == [0.5, 1.0]


def test_permanent_transport_and_hash_errors_are_not_retried(tmp_path):
    name = "go_to_red_cube/000099/info.csv"
    task = make_task([(name, b"csv")])
    calls = []

    def corrupt_source(request, *, timeout):
        calls.append(request)
        return BytesIO(make_archive([(name, b"bad")]))

    def must_not_pause(delay):
        pytest.fail("Permanent failures must not be retried")

    with pytest.raises(DatasetFetchError, match="SHA-256 mismatch"):
        fetch_task_with_retries(task, tmp_path, opener=corrupt_source, sleeper=must_not_pause)
    assert len(calls) == 1
    calls.clear()

    def forbidden(request, *, timeout):
        calls.append(request)
        raise urllib.error.HTTPError(request.full_url, 403, "Forbidden", {}, None)

    with pytest.raises(urllib.error.HTTPError):
        fetch_task_with_retries(task, tmp_path, opener=forbidden, sleeper=must_not_pause)
    assert len(calls) == 1


def test_persistent_connection_failure_stops_after_three_attempts(tmp_path):
    task = make_task([("go_to_red_cube/000099/info.csv", b"csv")])
    calls = []

    def disconnected(request, *, timeout):
        calls.append(request)
        raise ConnectionResetError("connection reset")

    with pytest.raises(ConnectionResetError):
        fetch_task_with_retries(task, tmp_path, opener=disconnected, sleeper=lambda delay: None)
    assert len(calls) == 3


def test_retry_reuses_members_verified_before_connection_interruption(tmp_path):
    first = ("go_to_red_cube/000099/info.csv", b"csv")
    second = ("go_to_red_cube/000099/image/000.png", b"image")
    task = make_task([first, second])
    initial = make_archive([first, ("large-unused.bin", random.Random(5).randbytes(256 * 1024)), second])

    class InterruptedResponse(BytesIO):
        reads = 0

        def read(self, count=-1):
            self.reads += 1
            if self.reads > 1:
                raise ConnectionResetError("connection interrupted after first member")
            return super().read(count)

    calls = []

    def open_source(request, *, timeout):
        calls.append(request)
        if len(calls) == 1:
            return InterruptedResponse(initial)
        assert (tmp_path / first[0]).read_bytes() == first[1]
        # The replacement archive lacks the first member. Success therefore
        # requires rechecking and reusing the already verified local file.
        return BytesIO(make_archive([second]))

    assert fetch_task_with_retries(task, tmp_path, opener=open_source, sleeper=lambda delay: None)["status"] == "fetched"
    assert len(calls) == 2
    assert (tmp_path / second[0]).read_bytes() == second[1]
