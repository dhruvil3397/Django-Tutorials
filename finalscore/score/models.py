from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here..
class Branch(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:   
        return self.name

class StudentScore(models.Model):
    name = models.CharField(max_length=50)
    enroll_no = models.IntegerField()
    maths_m = models.IntegerField()
    sci_m = models.IntegerField()
    guj_m = models.IntegerField()
    branch = models.ForeignKey(to=Branch,on_delete=CASCADE,null=True,blank=True)

    def __str__(self) -> str:
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(to=User ,on_delete=CASCADE)
    branch = models.ForeignKey(to=Branch,on_delete=CASCADE,null=True,blank=True)
    