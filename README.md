esciforge
=========

## Install

```shell
# setup python virtual environment 
$ pyvenv-3.4 ./Projects/pyvenv/esciforge --without-pip
$ source ./Projects/pyvenv/esciforge/bin/activate
$ cd ./Projects/pyvenv/esciforge
$ mkdir pypioffline
$ cd pypioffline
$ wget https://pypi.python.org/packages/source/s/setuptools/setuptools-5.4.tar.gz
$ tar xvzf setuptools-5.4.tar.gz 
$ cd setuptools-5.4/
$ python ez_setup.py
$ easy_install pip

# install python packages
$ pip install Django
$ pip install pygit
$ pip install svn

# get and run esciforge
$ sudo apt-get install git
$ cd ~/Projects/
$ git clone https://github.com/sciforge/esciforge.git

# run esciforge
$ source ./Projects/pyvenv/esciforge/bin/activate
$ ~/Projects/esciforge/django/manage.py runserver
```
