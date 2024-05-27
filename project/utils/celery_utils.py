import functools

from celery import Task
from celery import current_app as current_celery_app
from celery import shared_task


def make_celery(app):
    celery = current_celery_app
    celery.config_from_object(app.config, namespace="CELERY")
    celery.conf.task_default_queue = "{queue_name}"
    celery.conf.task_default_exchange = "{exchange_name}"
    celery.conf.task_default_routing_key = "{routing_key_name}"
    if not hasattr(celery, "flask_app"):
        celery.flask_app = app
    celery.Task = AppContextTask
    return celery


class AppContextTask(Task):
    def __call__(self, *args, **kwargs):
        with self.app.flask_app.app_context():
            Task.__call__(self, *args, **kwargs)


class custom_celery_task:
    def __init__(self, *args, **kwargs):
        self.task_args = args
        self.task_kwargs = kwargs

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_func(*args, **kwargs):
            # CUSTOM CODE HERE
            return func(*args, **kwargs)

        task_func = shared_task(*self.task_args, **self.task_kwargs)(wrapper_func)
        return task_func
