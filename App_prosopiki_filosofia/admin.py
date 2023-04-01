from django.contrib import admin

from App_prosopiki_filosofia.models import Blog, Blogimg,Blogcomment

# Register your models here.

admin.site.register(Blog)
admin.site.register(Blogimg)
admin.site.register(Blogcomment)