#!/bin/sh
# Install files without enabling or starting timers.
set -eu

if [ "$(id -u)" -ne 0 ]; then
    echo "Run this installer with sudo." >&2
    exit 1
fi

scheduler_source=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)

if ! getent passwd pyperf-scheduler >/dev/null; then
    useradd --system --user-group --no-create-home --home-dir /nonexistent \
        --shell /usr/sbin/nologin pyperf-scheduler
fi
install -d -m 0755 /usr/local/lib/pyperf-scheduler
install -m 0644 "$scheduler_source/dispatch.py" /usr/local/lib/pyperf-scheduler/dispatch.py
install -d -m 0700 /etc/pyperf-scheduler
if [ ! -f /etc/pyperf-scheduler/config ]; then
    # Fail closed until an explicit cutover date and token have been supplied.
    printf '%s\n' 'SCHEDULER_REPOSITORY=diegorusso/pyperf-bench' \
        'SCHEDULER_START_AT=9999-01-01T00:00:00Z' > /etc/pyperf-scheduler/config
    chmod 0600 /etc/pyperf-scheduler/config
fi
for scheduler_unit in "$scheduler_source"/systemd/*; do
    install -m 0644 "$scheduler_unit" /etc/systemd/system/
done
systemd-analyze verify /etc/systemd/system/pyperf-scheduler@.service \
    /etc/systemd/system/pyperf-scheduler-pin.timer \
    /etc/systemd/system/pyperf-scheduler-nightly.timer \
    /etc/systemd/system/pyperf-scheduler-profiling.timer
systemctl daemon-reload
echo 'Installed. Timers have not been enabled or started.'
