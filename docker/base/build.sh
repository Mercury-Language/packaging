#!/bin/sh

set -e

docker build -t paulbone/mercury-base:latest .
docker push paulbone/mercury-base:latest

