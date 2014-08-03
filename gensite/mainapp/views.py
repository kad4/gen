from django import forms
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from mainapp.models import Post,Rating,Site
from django.contrib.auth.models import User

from datetime import datetime
from random import sample,choice,randint
import pytz

# sklean module uses scipy module
# Importing scipy raises a deprecationwarning 
import warnings
with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	from sklearn.cluster import KMeans

from genpy import crawler

class SignupForm(forms.ModelForm):
	class Meta:
		model= auth.models.User
		fields= ['username','email','first_name','last_name','password']
		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control input-xlarge'}),
			'email': forms.TextInput(attrs={'class':'form-control input-xlarge'}),
			'first_name': forms.TextInput(attrs={'class':'form-control input-xlarge'}),
			'last_name': forms.TextInput(attrs={'class':'form-control input-xlarge'}),
			'password': forms.PasswordInput(attrs={'class':'form-control input-xlarge'}),
		}

	repassword=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control input-xlarge'}))

class LoginForm(forms.Form):
	username=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control input-xlarge'}))	
	password=forms.CharField(max_length=30,widget=forms.PasswordInput(attrs={'class':'form-control input-xlarge'}))	

def index(request):
	if(request.method=='POST'):
		form=LoginForm(request.POST)
		if(form.is_valid()):
			user=auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					auth.login(request,user)
					return redirect('home')
				else:
					# Disabled account
					pass
			else:
				new_form=LoginForm()
				return render(request,'mainapp/index.html',{'message':'Wrong Username or password','form':new_form})
		else:
			new_form=LoginForm()
			return render(request,'mainapp/index.html',{'message':'Wrong Username or password','form':new_form})

	else:
		if(request.user.is_authenticated()):
			return redirect('home')
		else:
			new_form=LoginForm()
			return render(request, 'mainapp/index.html',{'form':new_form})

def signup(request):
	if (request.method== 'POST'):
		form=SignupForm(request.POST)
		if (form.is_valid()):
			username=form.cleaned_data['username']
			email=form.cleaned_data['email']
			password=form.cleaned_data['password']
			repassword=form.cleaned_data['repassword']
			first_name=form.cleaned_data['first_name']
			last_name=form.cleaned_data['last_name']

			if(password!=repassword):
				return render(request,'mainapp/signup.html',{'form':form})
			
			user = auth.models.User.objects.create_user(username, email, password)
			user.first_name=first_name
			user.last_name=last_name
			user.save()

			new_form=SignupForm()
			return render(request,'mainapp/signup.html',{'form':new_form,'message':'User has been created'})

		else:
			return render(request,'mainapp/signup.html',{'form':form})
	form=SignupForm()
	return render(request,'mainapp/signup.html',{'form':form})

def logout(request):
	auth.logout(request)
	return redirect('index')

@login_required(redirect_field_name='index')
def home(request):
	total_posts=Post.objects.all().order_by('-created_at')
	paginator = Paginator(total_posts, 10)

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return render(request,'mainapp/home.html',{'posts':posts})

def crawleradmin(request):
	sites=Site.objects.all()
	return render(request,'mainapp/crawler.html',{'title':'Crawler','sites':sites})

def crawlsite(request,id):
	crawl_site=site.objects.get(pk=id)
	try:
		obj=crawler.sitecrawler({crawl_site.url})
		obj.startCrawl()
		
		utc=pytz.UTC

		for items in obj.Articles:
			# new_post=Post(title=items[0],created_at=utc.localize(datetime.strptime(items[1], "%Y-%m-%d")),url=items[2],site_id=id)
			new_post=Post(title=items[0],created_at=utc.localize(items[1]),url=items[2],site_id=id)
			new_post.save()

		return HttpResponse('Crawling Completed')
	except:
		return HttpResponse('Errors occured')

def seedrating(request):
	users=User.objects.all()
	posts=Post.objects.all()
	scores=[0,1,2]
	num_posts=randint(180,200)

	for user in users:
		sample_posts= sample(set(posts),num_posts)
		for post in sample_posts:
			score=choice(scores)
			new_rating=Rating(user_id=user.id,post_id=post.id,score=score)
			new_rating.save()

	return HttpResponse('Rating Completed')

def ratepost(request):
	rating_score=request.GET['score']
	id=request.GET['id']
	if request.user.is_authenticated:
		new_rating=Rating(user_id=request.user.id,post_id=id,score=rating_score)
		new_rating.save()
		return HttpResponse('Rating Done')
	else:
		return HttpResponse('Login Required')

def usernews(request):
	pass


def test(request):
	# User table seeder

	# cursor=connection.cursor()
	# cursor.execute("SELECT * FROM MOCK_DATA")
	# rows=cursor.fetchall()
	# print(rows[0])
	# for row in rows:
	# 	try:
	# 		user = auth.models.User.objects.create_user(row[4], row[7], 'kathmandu')
	# 		user.first_name=row[5]
	# 		user.last_name=row=[6]
	# 		user.save()
	# 	except:
	# 		pass


	return HttpResponse('Alldone')