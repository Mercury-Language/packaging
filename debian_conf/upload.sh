#/bin/bash

set -e

# Uncomment the latter for testing.
DRY_RUN=""
# DRY_RUN="--dry-run -i"

# -rlto are some of the --archive options except they won't change file
# permissions or ownership.

echo Test
rsync -rltov --del $DRY_RUN \
    --exclude conf \
    --exclude db \
    --exclude incoming \
    --exclude temp \
    test/ sodium:/mnt/tank/deb/test/

echo deimos
rsync -rltov --del $DRY_RUN \
    --exclude conf \
    --exclude db \
    --exclude incoming \
    --exclude temp \
    deimos/ deimos:/srv/dl1/deb/ || true

echo sodium
rsync -rltov --del $DRY_RUN \
    --exclude conf \
    --exclude db \
    --exclude incoming \
    --exclude temp \
    sodium/ sodium:/mnt/tank/deb/deb/

