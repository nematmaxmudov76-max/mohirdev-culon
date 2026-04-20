import time

from celery import shared_task

@shared_task
def task():
    time.sleep(7)
    print("hello world")
    return True