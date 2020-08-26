from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pilatescenter.settings')
app = Celery('pilatescenter')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'print_names': {
        'task': 'your_name',
        'schedule': crontab(minute='*'),
    },
    'print_greeting': {
        'task': 'comida',
        'schedule': 1,
        'args': ('')
        # 'schedule': crontab(minute='*'),
    },
}