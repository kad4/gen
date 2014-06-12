from django.shortcuts import render

from mainapp.models import post
# Create your views here.

def index(request):
	post_list=post.objects.all()
	return render(request,'mainapp/index.html',{'post_list':post_list})

