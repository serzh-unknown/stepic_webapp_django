#!/bin/sh

pip3 install django
pip3 install gunicorn
nano /usr/sbin/gunicorn-debian 
nano /usr/bin/gunicorn 
nano /usr/bin/gunicorn_django
nano /usr/bin/gunicorn_paster
