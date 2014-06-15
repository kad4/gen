from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/',views.about,name='about'),
	url(r'^login/',views.login,name='login'),
	url(r'^signup/',views.signup,name='signup'),
	)