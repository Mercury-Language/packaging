#!/bin/sh

set -e

docker build -t paulbone/mercury:rotd -t paulbone/mercury:latest .
docker push paulbone/mercury:rotd
docker push paulbone/mercury:latest

