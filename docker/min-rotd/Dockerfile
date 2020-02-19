FROM debian

RUN apt-get update && apt-get -yq install \
    gnupg \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /tmp
COPY paul.asc .
RUN apt-key add paul.asc

COPY mercury.list /etc/apt/sources.list.d/

# Install some mercury dependencies, this creates another docker layer
# allowing some caching.
RUN apt-get update && apt-get install -yq \
    gcc \
    libhwloc-dev \
    libreadline-dev \
    perl \
    && rm -rf /var/lib/apt/lists/*

# Install a minimal set of Mercury grades
RUN apt-get update && apt-get install -yq \
    mercury-rotd-llc-dev \
    mercury-rotd-tools \
    && rm -rf /var/lib/apt/lists/*

