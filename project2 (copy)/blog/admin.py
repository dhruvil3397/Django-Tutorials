from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Post,Blogcomment


#class PostAdmin(ModelAdmin):
    # list_display = ['title','author']
    

class BlogcommentAdmin(ModelAdmin):
     list_display = ['user','comment']

    


# Register your models here.
#admin.site.register(Post,PostAdmin)
admin.site.register(Blogcomment,BlogcommentAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
     class Media :
          js = ('tinyInject.js',)
