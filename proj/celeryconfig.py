# -*- coding: utf-8 -*-
BROKER_URL = 'redis://localhost'
CELERY_RESULT_BACKEND = 'redis://localhost'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_RESULT_EXPIRES = 60 * 60
CELERY_ACCEPT_CONTENT = ['json']
