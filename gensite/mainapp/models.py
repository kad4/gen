from django.db import models

# Create your models here.

class member(models.Model):
	username= models.CharField(max_length=50)
	password= models.CharField(max_length=50)
	email= models.CharField(max_length=70)
	first_name= models.CharField(max_length=50)
	last_name= models.CharField(max_length=50)
	last_access= models.DateTimeField()

	def __str__(self):
		return self.username

class post(models.Model):
	title= models.TextField()
	url= models.URLField()
	created_at= models.DateTimeField()

	def __str__(self):
		return self.title

class rating(models.Model):
	user_id= models.ForeignKey(member)
	post_id= models.ForeignKey(post)
	score= models.PositiveSmallIntegerField()

class site(models.Model):
	name= models.CharField(max_length=30)
	feed_url= models.URLField()
	last_access= models.DateTimeField()
	frequency= models.DateTimeField()

	def __str__(self):
		return self.name


