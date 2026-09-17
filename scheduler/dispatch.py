#!/usr/bin/env python3
"""Dispatch one GitHub Actions run per scheduled UTC slot from systemd."""

import argparse
import datetime as dt
import fcntl
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request

UTC = dt.timezone.utc
WORKFLOWS = {
    "pin": ("_pin_commit.yml", "_pin_commit", 23, 0, None),
    "nightly": ("nightly.yml", "nightly", 1, 45, None),
    "profiling": ("profiling.yml", "Weekly Profiling", 4, 0, 6),
}


def parse_time(value):
    value = dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    if value.tzinfo is None:
        raise ValueError("timestamps must include a timezone")
    return value.astimezone(UTC)


def timestamp(value):
    return value.astimezone(UTC).isoformat(timespec="seconds").replace("+00:00", "Z")


def scheduled_slot(workflow, now):
    _, _, hour, minute, weekday = WORKFLOWS[workflow]
    slot = now.astimezone(UTC).replace(hour=hour, minute=minute, second=0, microsecond=0)
    if slot > now:
        slot -= dt.timedelta(days=1)
    while weekday is not None and slot.weekday() != weekday:
        slot -= dt.timedelta(days=1)
    return slot


def atomic_write(path, data):
    temporary = path.with_suffix(".tmp")
    with temporary.open("w") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)
    directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(directory)
    finally:
        os.close(directory)


class GitHub:
    def __init__(self, repository, token):
        self.repository = repository
        self.token = token

    def request(self, path, body=None):
        request = urllib.request.Request(
            "https://api.github.com/" + path,
            data=json.dumps(body).encode() if body is not None else None,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": "Bearer " + self.token,
                "Content-Type": "application/json",
                "X-GitHub-Api-Version": "2026-03-10",
                "User-Agent": "pyperf-bench-scheduler",
            },
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            content = response.read()
            return json.loads(content) if content else None

    def find_run(self, workflow, title, slot):
        filename = WORKFLOWS[workflow][0]
        page = 1
        while True:
            query = urllib.parse.urlencode({
                "per_page": 100, "page": page,
                "created": ">=" + timestamp(slot),
            })
            result = self.request(
                f"repos/{self.repository}/actions/workflows/{filename}/runs?{query}"
            )
            for run in result["workflow_runs"]:
                if run["event"] == "workflow_dispatch" and run["display_title"] == title:
                    return {"workflow_run_id": run["id"], "html_url": run["html_url"]}
            if len(result["workflow_runs"]) < 100:
                return None
            page += 1

    def dispatch(self, workflow, slot):
        filename = WORKFLOWS[workflow][0]
        return self.request(
            f"repos/{self.repository}/actions/workflows/{filename}/dispatches",
            {"ref": "main", "inputs": {"scheduler_slot": timestamp(slot)}},
        )


def dispatch_once(github, workflow, slot, state_directory):
    """Persist intent before POST; ambiguous outcomes are reconciled, never resent."""
    title = f"{WORKFLOWS[workflow][1]} [scheduled {timestamp(slot)}]"
    key = f"{workflow}-{slot.strftime('%Y%m%dT%H%M%SZ')}"
    path = state_directory / (key + ".json")
    with (state_directory / (workflow + ".lock")).open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        state = json.loads(path.read_text()) if path.exists() else None
        if state and state["status"] in ("accepted", "confirmed"):
            return state
        existing = github.find_run(workflow, title, slot)
        if existing:
            state = {"slot": timestamp(slot), "status": "confirmed", "run": existing}
            atomic_write(path, state)
            return state
        if state:
            raise RuntimeError(
                f"An earlier dispatch has an unknown outcome: {path}. "
                "No matching run is visible yet; refusing to submit a duplicate. "
                "Run this service again to reconcile, or inspect GitHub before resetting the state."
            )
        state = {"slot": timestamp(slot), "status": "sending", "title": title}
        atomic_write(path, state)
        try:
            result = github.dispatch(workflow, slot)
        except urllib.error.HTTPError as error:
            error.close()
            # These are explicit refusals; a later service retry may safely try again.
            if error.code in (400, 401, 403, 404, 422, 429):
                path.unlink()
            raise
        state = {"slot": timestamp(slot), "status": "accepted", "run": result}
        atomic_write(path, state)
        return state


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workflow", choices=WORKFLOWS)
    parser.add_argument("--dry-run", action="store_true", help="print the planned request without network access")
    parser.add_argument("--start-at", default=os.environ.get("SCHEDULER_START_AT"),
                        help="earliest eligible UTC slot; required outside dry-run")
    args = parser.parse_args()
    now = dt.datetime.now(UTC)
    slot = scheduled_slot(args.workflow, now)
    repository = os.environ.get("SCHEDULER_REPOSITORY", "diegorusso/pyperf-bench")
    if args.start_at and slot < parse_time(args.start_at):
        print(f"Skipping {timestamp(slot)}: before cutover {args.start_at}")
        return
    if args.dry_run:
        print(json.dumps({"repository": repository, "workflow": WORKFLOWS[args.workflow][0],
                          "ref": "main", "inputs": {"scheduler_slot": timestamp(slot)}}, indent=2))
        return
    if not args.start_at:
        parser.error("set SCHEDULER_START_AT to the cutover timestamp")
    # On restart, catch up only the most recent slot and only for twelve hours.
    if now - slot > dt.timedelta(hours=12):
        print(f"Skipping stale slot {timestamp(slot)}: more than twelve hours late")
        return
    credentials = Path(os.environ["CREDENTIALS_DIRECTORY"])
    token = (credentials / "github-token").read_text().strip()
    if not token:
        raise ValueError("empty GitHub token")
    state_directory = Path(os.environ["STATE_DIRECTORY"])
    state_directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    result = dispatch_once(GitHub(repository, token), args.workflow, slot, state_directory)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, KeyError) as error:
        print(f"Scheduler failed: {error}", file=sys.stderr)
        sys.exit(1)
