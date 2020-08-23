# GVM / Openvas Packaging Project 

The Openvas packaging project is an Atomicorp designed project to install and configure the [Openvas](http://www.openvas.org) vulnerability scanner Version 11 on a Redhat, Centos or Fedora system.



Visit our website for the latest information.  [www.atomicorp.com](http://www.atomicorp.com)



## Currently Supported Platforms 

* Redhat 8
* Centos 8
* Fedora 32
* Docker




## Yum/DNF Automatic Installation ##


1) Install the Atomic Yum Repository

```
    wget -q -O - https://updates.atomicorp.com/installers/atomic | sudo sh
```

2) Install the GVM/openvas package

```
	# Redhat/Centos 8 Only
	yum config-manager --set-enabled PowerTools
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



## Credits and Thanks ##

* Michael Meyer @Greenbone

* Jan-Oliver Wagner @Greenbone

* Everyone at Greenbone that made this project possible

* Fredrik Hilmersson https://libellux.com

* Cody Woods @Atomicorp

