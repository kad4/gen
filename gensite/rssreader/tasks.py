from __future__ import absolute_import

from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from mainapp.models import Post,Site,UserData,Rating
from django.contrib.auth.models import User

from datetime import datetime
import pytz

from genpy import parser

# sklean module uses scipy module
# Importing scipy raises a deprecationwarning 
import warnings
with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	from sklearn.cluster import KMeans

logger = get_task_logger(__name__)

# @periodic_task(run_every=(crontab(hour="*")))
# def extractnews():
# 	sites=Site.objects.all()
# 	for site in sites:
# 		data=parser.parser(site.rssurl)

# 		for items in data:
# 			new_post=Post(title=items[0],created_at=utc.localize(items[1]),url=items[2],site_id=site.id)
# 			new_post.save()

@periodic_task(run_every=(crontab(minute="*")))
def cluster_user():
	logger.info('Started')

	users=User.objects.all()
	# posts=Post.objects.all()
	# ratings=Rating.objects.all()
	# usersdata=UserData.objects.all()

	# Parameter to be used
	parameter_posts=Post.objects.all().order_by('-created_at')[:100]
	
	user_index=0
	X_data=[]
	
	for count,user in enumerate(users):
		X_user=[]

		user_posts = Post.objects.filter(rating__user__id=user.id).order_by('-created_at')[:100]
		for post in parameter_posts:
			if post in user_posts:
				rating= Rating.objects.filter(post_id=post.id,user_id=user.id)[0]
				X_user.append(rating.score)
			else:
				X_user.append(0)

		X_data.append(X_user)

	# K-means clustering algorithm
	estimator=KMeans(n_clusters=10)
	estimator.fit_predict(X_data)

	for count,user in enumerate(users):
		userdata=UserData.objects.get(user_id=user.id)
		if userdata:
			userdata.cluster_class=estimator.labels__[count]
			userdata.save()
		else:
			new_userdata=UserData(user_id=user.id,cluster_class=estimator.labels_[count])
			userdata.save()