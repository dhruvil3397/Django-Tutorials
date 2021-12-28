from django.contrib import admin
from . models import Branch, StudentScore,Profile
from django.contrib.admin.options import ModelAdmin


# Register your models here.
class StudentAdmin(ModelAdmin):
    list_display  = ['name','enroll_no','maths_m','sci_m','guj_m']
    list_filter = ['name']
    search_fields = ['name']

class BranchAdmin(ModelAdmin):
    list_display  = ['name']

class ProfileAdmin(ModelAdmin):
    list_display  = ['user']

  

admin.site.register(StudentScore,StudentAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(Profile,ProfileAdmin)