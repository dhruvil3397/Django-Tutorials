from __future__ import print_function
from django.db import models
#from django.db.models import signals
#from django.db.models.signals import pre_save, post_save
#from django.dispatch import receiver


# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    num1 = models.IntegerField()
    num2 = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        print('save() is called.')
        self.num2 = self.num1*3

    #     super(Student, self).save(*args, **kwargs)
        # for i in Student.objects.all():
        #     data = i.num1*2
        #     Student.objects.filter(name=str(i)).update(num2 =data)

    def __str__(self):
        return self.name
