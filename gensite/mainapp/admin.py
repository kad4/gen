from django.contrib import admin
from mainapp.models import Post,Rating,Site

class Siteadmin(admin.ModelAdmin):
	list_display=('name','url','rssurl','last_access','frequency')

class Ratingadmin(admin.ModelAdmin):
	search_fields=['post__title']
	list_display=('post','user','score')

class Postadmin(admin.ModelAdmin):
	search_fields=['title']
	list_display=('site','title','created_at')

admin.site.register(Post,Postadmin)
admin.site.register(Rating,Ratingadmin)
admin.site.register(Site,Siteadmin)