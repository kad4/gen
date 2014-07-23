from django.contrib import admin
from mainapp.models import post,rating,site

class siteadmin(admin.ModelAdmin):
	list_display=('name','last_access','frequency')

admin.site.register(post)
admin.site.register(rating)
admin.site.register(site,siteadmin)