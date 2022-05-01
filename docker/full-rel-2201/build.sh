#!/bin/sh

set -e

docker build -t paulbone/mercury-full:rel-2201 .
docker push paulbone/mercury-full:rel-2201

