FROM debian:buster
RUN apt-get update; apt-get upgrade -yq

WORKDIR /tmp
COPY install.sh .

# Install some mercury dependencies, this creates another docker layer
# allowing some caching.
RUN ./install.sh \
    gcc \
    libhwloc-dev \
    libreadline-dev \
    perl

RUN ./install.sh gnupg
COPY paul.asc .
RUN apt-key add paul.asc
COPY mercury.list /etc/apt/sources.list.d/

