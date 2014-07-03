from django.db import models
from django.contrib.auth.models import User

class site(models.Model):
	name= models.CharField(max_length=30)
	feed_url= models.URLField()
	last_access= models.DateTimeField()
	frequency= models.IntegerField()

	def __str__(self):
		return self.name

class post(models.Model):
	title= models.TextField()
	url= models.URLField()
	created_at= models.DateTimeField()
	site= models.ForeignKey(site)

	def __str__(self):
		return self.title

class rating(models.Model):
	user= models.ForeignKey(User)
	post= models.ForeignKey(post)
	score= models.PositiveSmallIntegerField()



