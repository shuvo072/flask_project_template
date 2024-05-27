from celery import shared_task
from celery.exceptions import Ignore
from celery.utils.log import get_task_logger
from flask import current_app as app

from project import ext_celery

logger = get_task_logger(__name__)


@shared_task
def divide(x, y):
    import time

    logger.info("Initialized")
    time.sleep(3)

    return x / y


@ext_celery.celery.task(bind=True)
def demo_task_with_json_parameter(self, demo_dict, **data_dict):
    logger.info(data_dict)
    return
