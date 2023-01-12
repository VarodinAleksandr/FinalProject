from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shopproject.settings")

django.setup()

app = Celery('shopproject', broker='amqp://localhost', backend='redis://localhost')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
