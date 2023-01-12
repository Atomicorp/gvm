# GVM / Openvas Packaging Project 

The GVM (Formerly: Openvas) project is an Atomicorp designed effort to install and configure the [Openvas](http://www.openvas.org) vulnerability scanner Version 21.04 on a Redhat, Rocky, Centos or Fedora Linux platforms.


Visit our website for the latest information.  [www.atomicorp.com](http://www.atomicorp.com)


## Currently Supported Platforms 

* RHEL 8/9
* Rocky 8/9
* Fedora 36
* Fedora 37



## Yum/DNF Automatic Installation ##


1) Install the Atomic Yum Repository

```
    wget -q -O - https://updates.atomicorp.com/installers/atomic | sudo sh
```

2) Install the GVM/openvas package

```
	# Redhat/Rocky/Centos 8 Only
	yum config-manager --set-enabled powertools
	yum install epel-release

	# Redhat/Rocky 9 Only
	yum config-manager --set-enabled crb
	yum install epel-release

	# 
	yum install gvm
```


3) Configure openvas
```
    gvm-setup
```


## Docker Installation ##

The [Atomicorp Openvas Docker Project](https://github.com/atomicorp/openvas-docker) is available from docker hub:

```
    docker pull atomicorp/openvas  
```


## Join us on Slack ##

Need help? Want to collaborate? 

[Join Atomicorp Slack](https://atomicorp-support.slack.com/)


## Credits and Thanks ##

* Michael Meyer @Greenbone

* Jan-Oliver Wagner @Greenbone

* Everyone at Greenbone that made this project possible

* Fredrik Hilmersson https://libellux.com

* Cody Woods @hcw2016

