from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
user_choice = (('Artist','Artist'),
            ('Editor','Editor'),
            ('Admin','Admin'))

type_choice = (('Group','Group'),
                ('Solo','Solo'))

nationality_choices = (('National','National'),
                        ('International','International'))

distribution_choices = (('Ang + Moz','Ang + Moz'),
                        ('Mundo','Mundo'))

class UserProfile(models.Model):  
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20,choices=user_choice,null=True, blank=True)
    user_type_id = models.CharField(max_length=50,null=True, blank=True)
    mobile_no = models.CharField(max_length=20,null=True, blank=True)
    type = models.CharField(max_length=50,choices=type_choice,null=True, blank=True)
    file_no = models.CharField(max_length=50,null=True, blank=True)
    Bank_Name = models.CharField(max_length=100,null=True, blank=True)
    Bank_Account_No = models.CharField(max_length=100,null=True, blank=True)
    Bank_Account_Holder_Name = models.CharField(max_length=100,null=True, blank=True)
    IBAN = models.CharField(max_length=50,null=True, blank=True)
    NIF_No = models.CharField(max_length=50,null=True, blank=True)
    Paypal_Account_No = models.CharField(max_length=50,null=True, blank=True)
    Paypal_Email_Id = models.CharField(max_length=50,null=True, blank=True)
    nationality = models.CharField(max_length=50,choices=nationality_choices,null=True, blank=True)
    distribution_id = models.CharField(max_length=50,choices=distribution_choices,null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    service_in_percentage = models.FloatField(default=50.0,null=True, blank=True)
    is_deactivated = models.BooleanField(default=False)
    is_blacklisted = models.BooleanField(default=False)
    admin_approval = models.BooleanField(default=False)



class Kisom(models.Model):
    artist_name = models.CharField(max_length=20, null=True, blank=True)
    content_name = models.CharField(max_length=100,null=True,blank=True)
    net_royalty_total = models.FloatField(default=0.0, null=True, blank=True)
    count = models.CharField(max_length=20, null=True, blank=True)
    ret = models.FloatField(default=0.0, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    admin_approval = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.artist_name

class Rbt(models.Model):
    artist_name = models.CharField(max_length=20, null=True, blank=True)
    content_name = models.CharField(max_length=100,null=True,blank=True)
    rev_x_2 = models.FloatField(default=0.0, null=True, blank=True)
    count = models.CharField(max_length=20, null=True, blank=True)
    ret = models.FloatField(default=0.0, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    admin_approval = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.artist_name



class Altafonte(models.Model):
    service_Id = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    artist = models.CharField(max_length=20, null=True, blank=True)
    track = models.CharField(max_length=100, null=True, blank=True)
    net = models.FloatField(default=0.0, null=True, blank=True)
    count = models.CharField(max_length=20, null=True, blank=True)
    ret = models.FloatField(default=0.0, null=True, blank=True)
    cambio = models.FloatField(default=0.0, null=True, blank=True)
    altafonte_aoa = models.FloatField(default=0.0, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    admin_approval = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.altafonte_aoa = self.net * self.cambio
        super(Altafonte, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.artist

    # class Meta:
    #     verbose_name_plural = 'Altafonte'
