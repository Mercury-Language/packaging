#/bin/bash

set -e

# Uncomment the latter for testing.
DRY_RUN=""
# DRY_RUN="--dry-run -i"


for REPO in test deimos sodium; do
    reprepro -b /mnt/hdd-dev/deb/$REPO processincoming incoming
    reprepro -b /mnt/hdd-dev/deb/$REPO export
    reprepro -b /mnt/hdd-dev/deb/$REPO createsymlinks 
done

# -rlto are some of the --archive options except they won't change file
# permissions or ownership.

rsync -rltov --del $DRY_RUN \
    --exclude conf \
    --exclude db \
    --exclude incoming \
    --exclude temp \
    test/ sodium:/mnt/tank/deb/test/

rsync -rltov --del $DRY_RUN \
    --exclude conf \
    --exclude db \
    --exclude incoming \
    --exclude temp \
    deimos/ deimos:/srv/dl1/deb/ || true

rsync -rltov --del $DRY_RUN \
    --exclude conf \
    --exclude db \
    --exclude incoming \
    --exclude temp \
    sodium/ sodium:/mnt/tank/deb/deb/

