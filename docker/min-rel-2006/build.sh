#!/bin/sh

set -e

docker build -t paulbone/mercury:rel-2006 .
docker push paulbone/mercury:rel-2006

