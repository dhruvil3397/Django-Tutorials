from django.db import models

# Create your models here.
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)
   

    def __str__(self) -> str:
        return self.name

