FROM paulbone/mercury:rotd

# Install a minimal set of Mercury grades
RUN apt-get update && apt-get -yq install \
    mercury-rotd-examples \
    mercury-rotd-maintainers \
    mercury-rotd-recommended \
    && rm -rf /var/lib/apt/lists/*

