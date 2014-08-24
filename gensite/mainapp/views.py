from django import forms
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from mainapp.models import Post,Rating,Site,UserData
from django.contrib.auth.models import User

from datetime import datetime
from random import sample,choice,randint
import json
import pytz

from genpy import crawler,parser

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

# Homepage
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

# Admin site for crawler
@staff_member_required
def crawleradmin(request):
	sites=Site.objects.all()
	return render(request,'mainapp/crawler.html',{'title':'Crawler','sites':sites})

# Link for crawler
@staff_member_required
def crawlsite(request,id):
	crawl_site=site.objects.get(pk=id)
	try:
		obj=crawler.sitecrawler({crawl_site.url})
		obj.startCrawl()
		
		utc=pytz.UTC

		for items in obj.Articles:
			new_post=Post(title=items[0],created_at=utc.localize(items[1]),url=items[2],site_id=id)
			new_post.save()

		return HttpResponse('Crawling Completed')
	except:
		return HttpResponse('Errors occured')

# Seeder for ratings
@staff_member_required
def seedrating(request):
	num_users=randint(15,30)
	scores=[1,2]

	total_users=User.objects.all()
	total_posts=Post.objects.all()

	users=sample(set(total_users),num_users)

	for user in users:
		num_posts=randint(10,20)
		posts= sample(set(total_posts),num_posts)
		for post in posts:
			score=choice(scores)

			rating= Rating.objects.filter(user_id=user.id,post_id=post.id)

			if(not(rating)):
				new_rating=Rating(user_id=user.id,post_id=post.id,score=score)
				new_rating.save()

	return HttpResponse('Rating Completed')

# Dashboard for logged in users
@login_required(redirect_field_name='index')
def home(request):
	total_posts=Post.objects.all().order_by('-created_at')[:300]
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

	for post in posts:
		rating = Rating.objects.filter(post_id=post.id,user_id=request.user.id)
		if (rating):
			post.is_rated=True
		else:
			post.is_rated=False
	return render(request,'mainapp/home.html',{'posts':posts})

# Trending page to show recommendations
@login_required(redirect_field_name='index')
def trending(request):
	userdata=UserData.objects.get(user_id=request.user.id)

	# Retrives posts without repeating them
	total_posts=list(set(
		Post.objects.filter(rating__user__userdata__cluster_class=userdata.cluster_class,rating__score=2)
		.exclude(rating__user__id=request.user.id)[:100]))

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

	for post in posts:
		rating= Rating.objects.filter(post_id=post.id,user_id=request.user.id)
		if (rating):
			post.is_rated=True
		else:
			post.is_rated=False

	return render(request,'mainapp/home.html',{'posts':posts})


# Ajax link to rate post
@login_required
def ratepost(request):
	rating_score=request.GET['score']
	id=request.GET['id']
	new_rating=Rating(user_id=request.user.id,post_id=id,score=rating_score)
	new_rating.save()
	return HttpResponse('Rating Done')

def clientconnect(request):
	action=request.POST['action']
	if (action=='login'):
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			session_id=''
			while True:
				for i in range(1,30):
					session_id=session_id+str(randint(0,9))
				ids=UserData.objects.values_list('session_id')
				if (session_id not in ids):
					userdata=UserData.objects.filter(user__username=username)[0]
					userdata.session_id=session_id
					userdata.save()
					break;
				else:
					sesion_id=''
			return HttpResponse(json.dumps([True,session_id]))
		else:
			return HttpResponse(json.dumps(False))

	elif(action=='checksession'):
		session_id=request.POST['session_id']
		userdata=UserData.objects.filter(session_id=session_id)
		if (userdata is not None):
			return HttpResponse(json.dumps([True]))
		else:
			return HttpResponse(json.dumps([False]))

	else:
		session_id=request.POST['session_id']
		userdata=UserData.objects.filter(session_id=session_id)[0]
		if (action=='like'):
			id=request.POST['id']
			rating_score=request.POST['state']
			new_rating=Rating(user_id=userdata.user.id,post_id=id,score=rating_score)
			new_rating.save()

		elif(action=='logout'):
			userdata.session_id=''

		elif(action=='retrievePost'):
			post_type=request.POST['type']
			if(post_type=='Recommended'):
				total_posts=list(set(
					Post.objects.filter(rating__user__userdata__cluster_class=userdata.cluster_class,rating__score=2)
					.exclude(rating__user__id=request.user.id)[:100]))
			else:
				total_posts=Post.objects.all().order_by('-created_at')[:300]

			post_list=[]
			for post in total_posts:
				post_dict={'title':post.title,'id':post.id,'url':post.url}
				post_list.append(post_dict)

			return HttpResponse(json.dumps(post_list))


		elif(action=='retreiveContent'):
			id=request.POST['id']
			post=Post.objects.get(id=id)
			post_text=parser.parser(post.url)
			return HttpResponse(json.dumps(post_text))


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

	return HttpResponse(json.dumps('के छ मुला '))