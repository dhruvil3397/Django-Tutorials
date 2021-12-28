from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):  
    user = models.OneToOneField(User,related_name='profile', on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)  
    active = models.BooleanField(default=False)
    

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)


class Product(models.Model):
    product_id = models.AutoField
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200)

  

    def __str__(self) -> str:
        return self.category