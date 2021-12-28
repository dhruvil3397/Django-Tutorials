from django.db import models
from django.db.models.fields import TextField


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()
  
    def __str__(self) -> str:
        return self.name
