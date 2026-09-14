import gzip
import json
import os
import shutil
import sys
import urllib.error
import urllib.request
from http import HTTPStatus
from pathlib import Path

if len(sys.argv) != 3:
    raise SystemExit(f"usage: {sys.argv[0]} URL DATABASE")

url = sys.argv[1]
database_path = Path(sys.argv[2])
database_part_path = Path(f"{database_path}.part")
cache_state_path = Path(f"{database_path}.http-cache.json")
cache_state_part_path = Path(f"{cache_state_path}.part")
database_path.parent.mkdir(parents=True, exist_ok=True)

cache_state = {}
if database_path.is_file():
    try:
        cache_state = json.loads(cache_state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass
if not isinstance(cache_state, dict):
    cache_state = {}

headers = {}
if cache_state.get("etag"):
    headers["If-None-Match"] = cache_state["etag"]
if cache_state.get("last_modified"):
    headers["If-Modified-Since"] = cache_state["last_modified"]

try:
    response = urllib.request.urlopen(
        urllib.request.Request(url, headers=headers), timeout=60
    )
except urllib.error.HTTPError as error:
    if error.code == HTTPStatus.NOT_MODIFIED and database_path.is_file():
        error.close()
        print(f"using cached RIPE database at {database_path}")
        raise SystemExit(0)
    raise

remote_cache_state = {
    "etag": response.headers.get("ETag"),
    "last_modified": response.headers.get("Last-Modified"),
}
cache_key = remote_cache_state["etag"] or remote_cache_state["last_modified"]
previous_cache_key = cache_state.get("etag") or cache_state.get("last_modified")
if database_path.is_file() and cache_key and cache_key == previous_cache_key:
    response.close()
    print(f"using cached RIPE database at {database_path}")
    raise SystemExit(0)

print(f"downloading and decompressing {url}")
try:
    with response, gzip.GzipFile(fileobj=response) as compressed, database_part_path.open(
        "wb"
    ) as database:
        shutil.copyfileobj(compressed, database, length=1024 * 1024)
        database.flush()
        os.fsync(database.fileno())

    cache_state_part_path.write_text(
        json.dumps(remote_cache_state, sort_keys=True) + "\n", encoding="utf-8"
    )
    os.replace(database_part_path, database_path)
    os.replace(cache_state_part_path, cache_state_path)
finally:
    database_part_path.unlink(missing_ok=True)
    cache_state_part_path.unlink(missing_ok=True)

print(f"prepared {database_path.stat().st_size} bytes")
