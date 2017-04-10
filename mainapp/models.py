from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
	name= models.CharField(max_length=30)
	url= models.URLField()
	rssurl= models.URLField()

	def __str__(self):
		return self.name

class Post(models.Model):
	title= models.TextField()
	url= models.URLField()
	created_at= models.DateTimeField()
	site= models.ForeignKey(Site)

	def __str__(self):
		return self.title

class Rating(models.Model):
	user= models.ForeignKey(User)
	post= models.ForeignKey(Post)
	score= models.PositiveSmallIntegerField()

	def __str__(self):
		return (self.user.username + ' rated post with id ' + str(self.post.id) + ' ' + str(self.score))

class UserData(models.Model):
	user= models.ForeignKey(User)
	cluster_class= models.IntegerField()
	session_id= models.TextField()

	def __str__(self):
		return (self.user.username + ' belongs to class ' + str(self.cluster_class))



