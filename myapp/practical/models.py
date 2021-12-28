from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email  = models.EmailField()
    mobile = models.IntegerField()
    course = models.CharField(max_length=100)




    def __str__(self):
        return self.name