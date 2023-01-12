#!/usr/bin/env sh

python manage.py migrate --noinput

python manage.py runserver 127.0.0.1:8001