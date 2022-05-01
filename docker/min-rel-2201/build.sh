#!/bin/sh

set -e

docker build -t paulbone/mercury:rel-2201 .
docker push paulbone/mercury:rel-2201

