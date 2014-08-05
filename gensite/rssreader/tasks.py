from __future__ import absolute_import

from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from mainapp.models import Post,Site

from datetime import datetime
import pytz

from genpy import parser

logger = get_task_logger(__name__)

@periodic_task(run_every=(crontab(hour="*", minute="*",day_of_week="*")))
def extractnews():
	sites=Site.objects.all()
	for site in sites:
		data=parser.parser(site.rssurl)

		for items in data:
			new_post=Post(title=items[0],created_at=utc.localize(items[1]),url=items[2],site_id=site.id)
			new_post.save()

