#!/bin/sh
# Take the first backup if none exists, then run backups on schedule
wal-g backup-list | grep -q base_ || backup.sh
exec supercronic /etc/supercronic/crontab
