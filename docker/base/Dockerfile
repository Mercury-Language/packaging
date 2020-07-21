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

COPY paul.gpg /etc/apt/trusted.gpg.d/paul-6507444DBDF4EAD2.gpg
COPY mercury.list /etc/apt/sources.list.d/

