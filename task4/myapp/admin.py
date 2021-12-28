
# Register your models here.
from django.contrib import admin
from .models import Student
from import_export import resources

from import_export.admin import ImportExportMixin


# Register your models here.


class StudentResource(resources.ModelResource):

    class Meta:
        model = Student
        import_id_fields = ('num2',)

    def before_import_row(self, row, **kwargs):
        row['num2'] = row['num1']*3


class StudentAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = ('name', 'email', 'num1', 'num2')
    list_filter = ['name']

    resource_class = StudentResource


admin.site.register(Student, StudentAdmin)
