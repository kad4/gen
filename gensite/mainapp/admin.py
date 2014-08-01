from django.contrib import admin
from mainapp.models import Post,Rating,Site

class siteadmin(admin.ModelAdmin):
	list_display=('name','last_access','frequency')

admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(Site,siteadmin)