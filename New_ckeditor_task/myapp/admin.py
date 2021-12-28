from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile,Product
from django.contrib.auth.models import User


# Register your models here.

class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User_Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super().get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Product)