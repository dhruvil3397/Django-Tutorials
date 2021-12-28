from django.contrib import admin
from .models import Student
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class StudentAdmin(ModelAdmin):
    list_display = ['name','email','num1','num2']

admin.site.register(Student,StudentAdmin)