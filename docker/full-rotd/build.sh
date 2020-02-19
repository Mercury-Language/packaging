#!/bin/sh

set -e

docker build -t paulbone/mercury-full:rotd -t paulbone/mercury-full:latest .
docker push paulbone/mercury-full:rotd
docker push paulbone/mercury-full:latest

