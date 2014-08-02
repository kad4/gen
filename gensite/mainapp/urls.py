from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.home, name='home'),	
	url(r'^signup/',views.signup,name='signup'),
	url(r'^logout/',views.logout,name='logout'),

	url(r'^admin/crawler',views.crawleradmin,name='crawleradmin'),
	url(r'^crawl/(?P<id>\d+)/',views.crawlsite,name='crawlsite'),
	
	url(r'^seedrating/',views.seedrating,name='seedrating'),
	url(r'^rate/',views.ratepost,name='ratepost'),
	
	url(r'^test/',views.test,name='test'),
	)