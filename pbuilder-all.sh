#!/bin/sh

SUDO="sudo --preserve-env"
CMD=$1

# plus amd64 only distros
for DIST in sid trixie bookworm noble jammy focal bionic; do
    for ARCH in amd64; do
        export DIST
        export ARCH
        $SUDO pbuilder $CMD
    done
done

