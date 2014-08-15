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


# RSS reader to extract news
# @periodic_task(run_every=(crontab(minute="*")))
def extractnews():
	sites=Site.objects.all()
	for site in sites:
		posts=parser.parser(site.rssurl)

		for post in posts:
			old_post= Post.objects.filter(url=post[2])
			if (not(old_post)):
				new_post= Post(title=post[0],created_at=utc.localize(post[1]),url=post[2],site_id=site.id)
				new_post.save()


# K-means clustering algorithm to cluster users
@periodic_task(run_every=(crontab(minute="*")))
def cluster_user():

	# Database models
	users=User.objects.all()
	# posts=Post.objects.all()
	# ratings=Rating.objects.all()
	# usersdata=UserData.objects.all()

	# Parameter to be used
	parameter_posts=Post.objects.all().order_by('-created_at')[:100]
	
	# Input matrix for K-means clustering
	X_data=[]

	for user in users:
		# Row for each user
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
		userdata=UserData.objects.filter(user_id=user.id)
		if (userdata):
			userdata[0].cluster_class=estimator.labels_[count]
			userdata[0].save()
		else:
			new_userdata=UserData(user_id=user.id,cluster_class=estimator.labels_[count])
			new_userdata.save()