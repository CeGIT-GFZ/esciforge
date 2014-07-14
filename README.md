#esciforge

Since software already has become an integral part of science, it’s time to integrated software properly into the scientific discourse with published and citable software. esciforge shall become a prototype platform for the publication of scientific software source code with persistent identifiers so that software becomes citable. esciforge will be a prototype only paving the way for further discussions and follow-up prototypes.

We will look at the requirements for software publication, code archives, metadata and persistent identification of software. We want to make software recognized as scientific achievement and want to establish best practices for publishing software, whilst promoting Open Science. Join us.

## Install

### Setup python virtual environment

```shell
$ pyvenv-3.4 ~/Projects/pyvenv/esciforge --without-pip
$ source ~/Projects/pyvenv/esciforge/bin/activate
$ cd ~/Projects/pyvenv/esciforge
$ mkdir pypioffline
$ cd pypioffline
$ wget https://pypi.python.org/packages/source/s/setuptools/setuptools-5.4.tar.gz
$ tar xvzf setuptools-5.4.tar.gz 
$ cd setuptools-5.4/
$ python ez_setup.py
$ easy_install pip
```

### Install python packages
```shell
$ pip install Django
$ pip install pygit
$ pip install svn
```

### Get esciforge
```shell 
$ sudo apt-get install git
$ cd ~/Projects/
$ git clone https://github.com/sciforge/esciforge.git
```

### Run esciforge
```shell 
$ source ~/Projects/pyvenv/esciforge/bin/activate
$ ~/Projects/esciforge/django/manage.py runserver
```
