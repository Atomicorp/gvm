# Openvas Packaging Project 

The Openvas packaging project is an Atomicorp designed project to install and configure the [Openvas](http://www.openvas.org) vulnerability scanner on a self contained Redhat, Centos or Fedora system.



Visit our website for the latest information.  [www.atomicorp.com](http://www.atomicorp.com)



## Currently Supported Platforms 

* Redhat 7
* Centos 7
* Fedora 24, 25, 26, 27
* Docker




## Yum/DNF Automatic Installation ##


1) Install the Atomic Yum Repository

```
    wget -q -O - https://updates.atomicorp.com/installers/atomic | sudo sh
```

2) Install the openvas package

```
    yum install openvas
```


3) Configure openvas
```
    openvas-setup
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

