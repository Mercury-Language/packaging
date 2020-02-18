#!/bin/sh

set -e

docker build -t paulbone/mercury:rotd .
docker tag paulbone/mercury:rotd paulbone/mercury:latest
docker push paulbone/mercury:rotd
docker push paulbone/mercury:latest

