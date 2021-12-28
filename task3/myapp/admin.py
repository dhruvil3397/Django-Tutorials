from django.contrib import admin
from .models import Student
from .views import uploadfiles
from django.contrib.admin.options import ModelAdmin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Student)
class BrandAdmin(ImportExportModelAdmin):
    list_diaplay =('name','email','num1','num2')
