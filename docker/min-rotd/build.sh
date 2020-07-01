#!/bin/sh

set -e

cp ../install.sh .

docker build -t paulbone/mercury:rotd -t paulbone/mercury:latest .
docker push paulbone/mercury:rotd
docker push paulbone/mercury:latest

