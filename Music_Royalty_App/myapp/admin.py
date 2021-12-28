from django.contrib import admin
from django.db.models import fields
from .models import Altafonte,Rbt,Kisom,UserProfile
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin, ImportExportMixin
from django.contrib.auth.admin import UserAdmin
from import_export.forms import ImportForm
from django import forms
from django.contrib.auth.models import User
from django.utils.text import slugify


# Register your models here.
#----------------------------------------UserProfileInline----------------------------------------------

class ProfileInline(admin.StackedInline):
    model = UserProfile 
    can_delete = False
    verbose_name_plural = 'User_Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    
   

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# -----------------------------------Altafonte------------------------------------------------------------
class AltafonteResource(resources.ModelResource):
    class Meta:
        model = Altafonte
    # event :2-----------open--------------
    def __init__(self, ret=None, cambio=None,date = None):
        super()
        self.ret =ret
        print(self.ret,'----------self.ret1-----------')
        self.cambio = cambio
        self.date = date

     # Insert the ret,cambio,date into each row
    def before_import_row(self, row, **kwargs):
        row['ret'] = self.ret
        row['cambio'] = self.cambio
        row['date'] = self.date

        # Before import the row,slugify the artist
        # row['artist'] = slugify(row['artist'])
        
        print(row['artist'],'******************')
        username = row['artist']
        # Here slugify is used for remove some special characters like */-@+ from the username,
        # before saving to the database
        username = slugify(username) 
        print(username,'-------------')
        user = User.objects.get_or_create(username=username)
        print(user)
   

class AltafonteAdmin(ImportExportActionModelAdmin):
    list_display = ('id','service_Id', 'country', 'artist',
                    'track', 'net','ret', 'cambio', 'altafonte_aoa','date','admin_approval')
    list_filter = ['artist']

    resource_class = AltafonteResource
  

    # Send the extra value to the resource constructor using kwargs.
	# This overrides an existing hook method in `ImportMixin`.
    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        print(rk,'---------rk-------')
            # This method may be called by the initial form GET request, before
		    # the ret is chosen. So we default to None.
        rk['ret'] = None
        rk['cambio'] = None
        rk['date'] = None
        # event 1 ------------------open-----------: 
        if request.POST: # *Now* we should have a non-null value
            # In the dry-run import, the ret is included as a form field.
            ret = request.POST.get('ret', None)
            cambio = request.POST.get('cambio',None)
            date = request.POST.get('date',None)
            print(cambio,'-------------')
            if ret and cambio and date :
                # If we have it, save it in the session so we have it for the confirmed import.
                request.session['ret'] = ret
                request.session['cambio'] = cambio
                request.session['date'] = date
                print(request.session['date'],'++++++++++++')
                
            else:
                try:
                     # If we don't have it from a form field, we should find it in the session.
                    ret = request.session['ret']
                    cambio = request.session['cambio']
                    date = request.session['date']
                    print(ret,'....................')
                except KeyError as e:
                    raise Exception("Context failure on row import, " +
                                         f"check admin.py for more info: {e}")
            rk['ret'] = ret
            rk['cambio'] = cambio
            rk['date'] = date
        return rk

admin.site.register(Altafonte, AltafonteAdmin)

#----------------------------------------------------Rbt---------------------------------------------------
class RbtResource(resources.ModelResource):
    class Meta:
        model = Rbt
    # event :2-----------open--------------
    def __init__(self, ret=None,date = None):
        super()
        self.ret =ret
        print(self.ret,'----------self.ret1-----------')
        self.date = date

     # Insert the ret,cambio,date into each row
    def before_import_row(self, row, **kwargs):
        row['ret'] = self.ret
        row['date'] = self.date

        # Before import the row,slugify the artist_name 
        # row['artist_name'] = slugify(row['artist_name'])

        username = row['artist_name'] 
        username = slugify(username) 
        user = User.objects.get_or_create(username=username)
        print(user)


class RbtAdmin(ImportExportActionModelAdmin):
    list_display = ('id','artist_name',
                    'content_name','rev_x_2','count','ret', 'date','admin_approval')
    list_filter = ['artist_name']
    resource_class = RbtResource

    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)
        print(rk,'---------rk-------')
            # This method may be called by the initial form GET request, before
		    # the ret is chosen. So we default to None.
        rk['ret'] = None
        rk['date'] = None
        # event 1 ------------------open-----------: 
        if request.POST: # *Now* we should have a non-null value
            # In the dry-run import, the ret is included as a form field.
            ret = request.POST.get('ret', None)
            date = request.POST.get('date',None)
            if ret and date :
                # If we have it, save it in the session so we have it for the confirmed import.
                request.session['ret'] = ret
                request.session['date'] = date
                print(request.session['date'],'++++++++++++')
                
            else:
                try:
                     # If we don't have it from a form field, we should find it in the session.
                    ret = request.session['ret']
                    date = request.session['date']
                    print(ret,'....................')
                except KeyError as e:
                    raise Exception("Context failure on row import, " +
                                         f"check admin.py for more info: {e}")
            rk['ret'] = ret
            rk['date'] = date
        return rk

admin.site.register(Rbt,RbtAdmin)


#-------------------------------------------------Kisom-----------------------------------------------------
class KisomResource(resources.ModelResource):
    class Meta:
        model = Kisom
    # event :2-----------open--------------
    def __init__(self, ret=None,date = None):
        super()
        self.ret =ret
        print(self.ret,'----------self.ret1-----------')
        self.date = date

     # Insert the ret,date into each row
    def before_import_row(self, row, **kwargs):
        row['ret'] = self.ret
        row['date'] = self.date
        # Before import the row,slugify the artist_name 
        # row['artist_name'] = slugify(row['artist_name'])
        
        username = row['artist_name'] 
        username = slugify(username) 
        user = User.objects.get_or_create(username=username)
        print(user)


class KisomAdmin(ImportExportActionModelAdmin):
    list_display = ('id','artist_name',
                    'content_name','net_royalty_total', 'count','ret', 'date','admin_approval')
    list_filter = ['artist_name']
    resource_class = KisomResource

    def get_resource_kwargs(self, request, *args, **kwargs):
        rk = super().get_resource_kwargs(request, *args, **kwargs)

            # This method may be called by the initial form GET request, before
		    # the ret is chosen. So we default to None.
        rk['ret'] = None
        rk['date'] = None
        # event 1 ------------------open-----------: 
        if request.POST: # *Now* we should have a non-null value
            # In the dry-run import, the ret is included as a form field.
            ret = request.POST.get('ret', None)
            date = request.POST.get('date',None)
            if ret and date :
                # If we have it, save it in the session so we have it for the confirmed import.
                request.session['ret'] = ret
                request.session['date'] = date
                print(request.session['date'],'++++++++++++')
                
            else:
                try:
                     # If we don't have it from a form field, we should find it in the session.
                    ret = request.session['ret']
                    date = request.session['date']
                    print(ret,'....................')
                except KeyError as e:
                    raise Exception("Context failure on row import, " +
                                         f"check admin.py for more info: {e}")
            rk['ret'] = ret
            rk['date'] = date
        return rk

admin.site.register(Kisom,KisomAdmin)

