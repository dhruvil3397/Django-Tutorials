from django.contrib import admin
from .models import Product,Contact
from django.contrib.admin.options import ModelAdmin


class ProductAdmin(ModelAdmin):
    list_display = ['category','type','brand','model','price']
    search_fields=  ['brand','model']
    list_filter = ['type']

class ContactAdmin(ModelAdmin):
     list_display = ['name']

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Contact,ContactAdmin)
