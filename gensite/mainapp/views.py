from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import timezone
from django import forms
from mainapp.models import post,member


# Create your views here.
class SignupForm(forms.Form):
	first_name= forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class':'form-control input-xlarge'}))
	last_name= forms.CharField(max_length=70,widget=forms.TextInput(attrs={'class':'form-control input-xlarge'}))
	email= forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control input-xlarge'}))
	username= forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control input-xlarge'}))
	password= forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control input-xlarge'}))
	repassword= forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control input-xlarge'}))


def index(request):
	post_list=post.objects.all()
	return render(request,'mainapp/index.html',{'post_list':post_list})

def about(request):
	return render(request,'mainapp/about.html')


def login(request):
	return render(request,'mainapp/login.html')

def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if (form.is_valid()):
			first_name=form.cleaned_data['first_name']
			last_name=form.cleaned_data['last_name']
			email=form.cleaned_data['email']
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			repassword=form.cleaned_data['repassword']
			
			if( password==repassword ):
				new_member=member()
			

	else:
		form= SignupForm()

	return render(request,'mainapp/signup.html', {
		'form':form,
		})
