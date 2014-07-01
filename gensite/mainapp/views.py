from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from mainapp.models import post,rating


class SignupForm(forms.ModelForm):
	class Meta:
		model= User
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

def home(request):
	if(request.method=='POST'):
		form=LoginForm(request.POST)
		if(form.is_valid()):
			user= authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			return HttpResponse('Arrived you have')
	else:
		form=LoginForm()

	return render(request,'mainapp/index.html',{'form':form})	

def signup(request):
	if (request.method== 'POST'):
		form=SignupForm(request.POST)
		if (form.is_valid()):
			username=form.cleaned_data['username']
			email=form.cleaned_data['email']
			password=form.cleaned_data['password']
			first_name=form.cleaned_data['first_name']
			last_name=form.cleaned_data['last_name']
			
			user = User.objects.create_user(username, email, password)
			user.first_name=first_name
			user.last_name=last_name
			user.save()

			return HttpResponseRedirect(reverse('home',))
	else:
		form=SignupForm()

	return render(request,'mainapp/signup.html',{'form':form})
