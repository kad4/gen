from __future__ import absolute_import

from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task

@periodic_task(run_every=(crontab(hour="*", minute="*",day_of_week="*")))
def scraper_example():
	logger.info("Running")
	
