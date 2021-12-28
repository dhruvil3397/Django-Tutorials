from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Contact

# Register your models here.
class ContactAdmin(ModelAdmin):
     list_display = ['name','email','phone']


admin.site.register(Contact,ContactAdmin)