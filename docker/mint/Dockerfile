FROM vcatechnology/ubuntu:16.04
MAINTAINER support <support@atomicorp.com>


RUN REPO_LIST=/etc/apt/sources.list.d/mint.list \
 && echo "deb http://packages.linuxmint.com/ sonya main upstream import backport " > ${REPO_LIST} \
 && LINUX_MINT_KEY=$(apt update 2>&1 | grep -o '[0-9A-Z]\{16\}$' | xargs) \
 && apt-key adv --recv-keys --keyserver keyserver.ubuntu.com ${LINUX_MINT_KEY} \
 && vca-install-package --allow-unauthenticated linuxmint-keyring \
 && unset LINUX_MINT_KEY REPO_LIST

# Install the necessary packages to convert to Linux Mint
RUN vca-install-package base-files

# Update all packages
RUN apt-get -q update \
 && echo console-setup console-setup/charmap select UTF-8 | debconf-set-selections \
 && apt-get -fqy -o Dpkg::Options::="--force-confnew" -o APT::Immediate-Configure=false dist-upgrade \
 && apt-get -qy autoremove \
 && apt-get -q clean


RUN apt-get build-dep -y linux 
RUN apt-get install -y fakeroot devscripts bc 
RUN apt-get clean 

RUN install --directory -m 0755 /data && \
    install --directory -m 0755 /patches


WORKDIR /data

VOLUME /data
VOLUME /patches

RUN groupadd -r gitlab-runner -g 478
RUN useradd -u 480 -r -g gitlab-runner gitlab-runner

# we have to run as root so that we can apt-get update
ENTRYPOINT ["/data/builder.sh"]
