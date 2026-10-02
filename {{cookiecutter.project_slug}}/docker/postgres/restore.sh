#!/bin/sh
# Restore the database into an empty volume mounted at /restore
#
# Usage:
#   restore.sh                     restore to the latest state
#   restore.sh "2026-10-02 14:25"  restore to this moment (UTC), also "10 minutes ago"
set -e

if [ -n "$1" ]; then
    target_time=$(date -u -d "$1" +%Y-%m-%dT%H:%M:%SZ)    # WAL-G format, to pick the backup
    pg_time=$(date -u -d "$1" '+%Y-%m-%d %H:%M:%S+00')    # PostgreSQL format
fi

if [ -n "$(ls -A /restore)" ]; then
    echo "/restore is not empty" >&2
    exit 1
fi

if pg_isready -q; then
    echo "Stop the database first: docker compose stop backend postgres-backup postgres" >&2
    exit 1
fi

# 1. Fetch the newest backup that finished before the target time
backup=LATEST
if [ -n "$target_time" ]; then
    backup=$(wal-g backup-list --detail | awk -v t="$target_time" \
        'NR > 1 && $6 < t && $6 > last {last = $6; name = $1} END {print name}')
fi
wal-g backup-fetch /restore "$backup"

# 2. Add the old server's unarchived WAL so nothing is lost
cp "$PGDATA"/pg_wal/0* /restore/pg_wal/ || true

# 3. Replay WAL in a temporary server, then promote it
touch /restore/recovery.signal
postgres -D /restore -c listen_addresses= \
    -c archive_mode=on -c "archive_command=wal-g wal-push %p" \
    -c "restore_command=wal-g wal-fetch %f %p" \
    -c "recovery_target_time=$pg_time" -c recovery_target_action=promote &

until psql -h /var/run/postgresql -XtAc "SELECT NOT pg_is_in_recovery()" 2>/dev/null | grep -q t; do
    kill -0 $! || exit 1
    sleep 2
done

psql -h /var/run/postgresql -Xc "SELECT pg_last_xact_replay_timestamp() AS restored_up_to"
kill -INT $! && wait $!
