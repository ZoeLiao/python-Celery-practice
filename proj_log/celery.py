# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import Celery

# app: Celery的实例
app = Celery(
    'proj_log',
    include=['proj_log.tasks'])
app.config_from_object('proj_log.celeryconfig')


if __name__ == '__main__':
    app.start()
