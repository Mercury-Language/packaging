#!/bin/sh

set -e

docker build -t paulbone/mercury-full:rel-2006 .
docker push paulbone/mercury-full:rel-2006

