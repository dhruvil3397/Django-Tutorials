from django.contrib import admin
from .models import Contact
from django.contrib.admin.options import ModelAdmin



class ContactAdmin(ModelAdmin):
     list_display = ['name','email','phone']
    

    


# Register your models here.
admin.site.register(Contact,ContactAdmin)
