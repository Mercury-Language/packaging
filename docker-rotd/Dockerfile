
FROM debian

RUN apt-get -yqq update
RUN apt-get -yqq install gnupg

WORKDIR /tmp

COPY paul.asc .
RUN apt-key add paul.asc
# RUN apt-key finger
COPY mercury.list /etc/apt/sources.list.d/

RUN apt-get update
RUN apt-get install -yqq mercury-rotd-recommended

