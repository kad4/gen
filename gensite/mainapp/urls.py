from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^signup/',views.signup,name='signup'),
	)