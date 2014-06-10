from django.contrib import admin
from mainapp.models import member,post,rating,site

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
	list_display=['username','email','first_name','last_name','last_access']

class PostAdmin(admin.ModelAdmin):
	list_display=['title','url','created_at']

class RatingAdmin(admin.ModelAdmin):
	list_display=['post_id','user_id','score']

class SiteAdmin(admin.ModelAdmin):
	list_display=['name','feed_url','last_access','frequency']

admin.site.register(member,MemberAdmin)
admin.site.register(post,PostAdmin)
admin.site.register(rating,RatingAdmin)
admin.site.register(site,SiteAdmin)