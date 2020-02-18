
FROM debian

RUN apt-get -yqq update
RUN apt-get -yqq install gnupg

WORKDIR /tmp

COPY paul.asc .
RUN apt-key add paul.asc
# RUN apt-key finger
COPY mercury.list /etc/apt/sources.list.d/

RUN apt-get update

# Install some mercury dependencies, this creates another docker layer
# allowing some caching.
RUN apt-get install -yqq gcc perl libreadline-dev libhwloc-dev

# Install a minimal set of Mercury grades
RUN apt-get install -yqq mercury-rotd-tools mercury-rotd-llc-dev

