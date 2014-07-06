from django import forms
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from mainapp.models import post,rating 

from mainapp.genpy import crawler

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
	posts=post.objects.all()
	return render(request,'mainapp/home.html',{'posts':posts})

def test(request):
	sitecrawler=crawler.sitecrawler()
	sitecrawler.start()
	return HttpResponse('Success')
	
