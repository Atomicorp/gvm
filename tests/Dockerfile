# Build tester
FROM centos:latest
MAINTAINER Support <support@atomicorp.com>

#VOLUME ["/var/lib/openvas"]

ADD run.sh /run.sh
ADD config/gsad /etc/sysconfig/gsad
ADD config/redis.conf /etc/redis.conf
# This is only used for pdf reports, something we cant test in here anyway
# Its a massive download
#ADD config/texlive.repo /etc/yum.repos.d/texlive.repo

# Uses the internal atomic-testing repo
ADD config/internal-testing.repo /etc/yum.repos.d/internal-testing.repo

RUN yum -y install wget
RUN cd /root; NON_INT=1 wget -q -O - https://updates.atomicorp.com/installers/atomic |sh


RUN \
	yum clean all && \
	yum -y update &&  \
	yum -y install deltarpm  yum-plugin-fastestmirror && \
	yum -y install alien bzip2 useradd net-tools openssh texlive-changepage texlive-titlesec  texlive-collection-latexextra

# PDF fixes
RUN mkdir -p /usr/share/texlive/texmf-local/tex/latex/comment
ADD config/comment.sty /usr/share/texlive/texmf-local/tex/latex/comment/comment.sty
RUN texhash

# Scanners
RUN yum -y install openvas OSPd-nmap OSPd


#RUN \
#	/usr/sbin/greenbone-nvt-sync && \
#	/usr/sbin/greenbone-certdata-sync && \
#	/usr/sbin/greenbone-scapdata-sync && \
#	BUILD=true /run.sh 


RUN rm -rf /var/cache/yum/*

CMD /run.sh
EXPOSE 443
