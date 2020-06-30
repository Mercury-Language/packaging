#!/bin/sh

for DIST in buster stretch; do
    for ARCH in amd64 i386; do
        export DIST
        export ARCH
        pbuilder update
    done
done

# plus amd64 only distros
for DIST in sid disco; do
    for ARCH in amd64; do
        export DIST
        export ARCH
        pbuilder update
    done
done

