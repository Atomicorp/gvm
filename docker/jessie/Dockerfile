FROM  debian:jessie

MAINTAINER support <support@atomicorp.com>

RUN \
  apt-get update && \
  apt-get -y upgrade 

RUN \
  apt-get install -y fakeroot devscripts && \
  apt-get clean

RUN \
  install --directory -m 0755 /data 


WORKDIR /data

VOLUME /data
VOLUME /patches

RUN groupadd -r gitlab-runner -g 478
RUN useradd -u 480 -r -g gitlab-runner gitlab-runner

# we have to run as root so that we can apt-get update
ENTRYPOINT ["/data/builder.sh"]
