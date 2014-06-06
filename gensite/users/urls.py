from django.conf.urls import patterns, url

from users import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
)