=== Setting up development environment ===

== Ubuntu Server 14.04 LTS ==
:Standard installation procedure
:Network setup as needed (if you have proxy)
:Manually manage updates
:Update/ Upgrade initially (apt-get update/upgrade)
:Python3-based
:libapache2-mod-wsgi-py3 (performance related, run inside apache2)

= pip3 =
:Django (pip install Django)
:pyGit (pip install pyGit)
:svn (pip install svn)

= apache wsgi configuration =
<code>
WSGIDaemonProcess esciforge python-path=/var/www/esciforge/django threads=8 processes=1
WSGIScriptAlias / /var/www/esciforge/django/esciforge/wsgi.py
WSGIProcessGroup esciforge
</code>
