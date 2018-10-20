# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import Celery

# app: Celery的实例
app = Celery(
    'proj_beat',
    include=['proj_beat.tasks'])
app.config_from_object('proj_beat.celeryconfig')


if __name__ == '__main__':
    app.start()
