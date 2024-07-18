#/bin/bash

set -e

for REPO in test deimos sodium; do
    reprepro -b /mnt/hdd-dev/deb/$REPO processincoming incoming
    reprepro -b /mnt/hdd-dev/deb/$REPO export
    reprepro -b /mnt/hdd-dev/deb/$REPO createsymlinks 
done

