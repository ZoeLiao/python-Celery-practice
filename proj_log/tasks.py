# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(bind=True)
def div(self, x, y):
    logger.info(('run task: id{0.id}, args:1 {0.args!r},'\
                 'kwargs: {0.kwargs!r}').format(self.request))
    try:
        result = x/y
    except ZeroDivisionError as e:
        raise self.retry(exc=e, countdown=5, max_retries=3)
    return result
