# Scheduler on sulaco

The systemd timers dispatch the existing GitHub Actions workflows. The Actions
runner continues to execute jobs, upload artifacts and publish results. The
dispatcher uses Python's standard library; GitHub CLI is not required.
The service runs on CPU 0, outside sulaco's benchmark affinity of CPUs 183-191.

| Timer | UTC schedule | Workflow |
| --- | --- | --- |
| `pyperf-scheduler-pin` | Daily at 23:00 | `_pin_commit.yml` |
| `pyperf-scheduler-nightly` | Daily at 01:45 | `nightly.yml` |
| `pyperf-scheduler-profiling` | Sunday at 04:00 | `profiling.yml` |

This migration changes the trigger only. It preserves commit selection,
benchmark configuration and job dependencies. Nightly and profiling can still
wait for the same runner; explicit sequencing is a separate change.

## Install without activation

Copy this directory to sulaco (`ssh psf-machine`) and run:

```sh
sudo sh scheduler/install.sh
```

The installer creates an unprivileged `pyperf-scheduler` service account and
installs the dispatcher and units. It does not start or enable timers, restart
the Actions runner, or overwrite an existing configuration or token.

Create a fine-grained GitHub token limited to `diegorusso/pyperf-bench`, with
**Actions: read and write**. Store only the token in
`/etc/pyperf-scheduler/github-token`, owned by root and mode `0600`. Do not put
the token in this repository or command-line arguments. systemd supplies it to
the service through `LoadCredential`.

The configuration file `/etc/pyperf-scheduler/config` is also root-owned and
mode `0600`. It contains:

```ini
SCHEDULER_REPOSITORY=diegorusso/pyperf-bench
SCHEDULER_START_AT=2026-09-18T22:00:00Z
```

The example cutover date must be replaced with a future UTC time at deployment.
The installer defaults to the year 9999 so a fresh installation cannot dispatch
anything accidentally.

## Cut over

1. Install the dispatcher and disabled timers, validate the token with a
   read-only request, and check the three timer schedules. Keep the workflow
   changes unmerged while preparing the host so GitHub cron continues to run.
2. Choose a cutover after the current nightly has started and before the next
   23:00 UTC pin occurrence. Set `SCHEDULER_START_AT` to that cutover time so the
   first externally dispatched nightly uses a freshly pinned revision.
3. Merge the workflow changes just before the chosen cutover time. They add
   `scheduler_slot` to the inputs and run names and remove the three GitHub
   `on.schedule` definitions. Do not disable the workflows themselves: they
   must remain enabled for API dispatch and manual use.
4. Enable the timers:

   ```sh
   sudo systemctl enable --now pyperf-scheduler-pin.timer \
       pyperf-scheduler-nightly.timer pyperf-scheduler-profiling.timer
   ```

5. Verify the first scheduled runs in both the journal and GitHub Actions.

Avoid running GitHub cron and these timers for the same scheduled occurrence.
The duplicate guard recognizes runs dispatched with `scheduler_slot`; it does
not treat an ordinary GitHub cron run as the same occurrence.

## Timing, recovery and duplicate protection

Timers use UTC, `AccuracySec=1s`, no randomized delay, and `Persistent=true`.
After downtime, only the most recent occurrence is eligible, and only within
twelve hours of its scheduled time. Earlier missed occurrences are not replayed.
An occurrence before the configured cutover is always skipped.

The dispatcher locks each workflow locally and saves state under
`/var/lib/pyperf-scheduler`. It checks GitHub for the exact scheduled run name
before submitting a request. A successful dispatch is recorded once regardless
of the benchmark's eventual outcome; this scheduler does not retry failed
benchmark runs.

The service retries failures up to three starts within ten minutes. If an API
timeout or server error leaves the dispatch outcome uncertain, subsequent starts
look for the run but do not submit another POST. An unresolved occurrence leaves
a failed service and a journal error for investigation. After confirming that no
run was created, an operator may remove that occurrence's JSON state and restart
the service while the slot is still eligible. Do not delete state for an accepted
or visible run.

This bypasses GitHub's cron scheduler. GitHub API availability, runner
availability and host load can still delay actual execution. The scheduler is
offline whenever sulaco is offline; external outage notifications are not
provided by this setup.

## Inspect and test

```sh
systemctl list-timers 'pyperf-scheduler-*'
journalctl -u 'pyperf-scheduler@*' --since today
python3 scheduler/dispatch.py nightly --dry-run
python3 -m unittest discover -s scheduler/tests -v
```

Dry-run prints the intended dispatch without reading credentials, making network
requests or writing state. Service logs and GitHub run names expose the intended
UTC occurrence, allowing trigger delay and runner queue delay to be tracked
separately.

## Roll back

Disable all three timers before restoring the GitHub cron definitions. Leave
the workflows enabled. Keep scheduler state if it may be reactivated later.
