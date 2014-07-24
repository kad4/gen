from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.home, name='home'),	
	url(r'^signup/',views.signup,name='signup'),
	url(r'^logout/',views.logout,name='logout'),
	url(r'^crawler/',views.crawler,name='crawler'),
	)