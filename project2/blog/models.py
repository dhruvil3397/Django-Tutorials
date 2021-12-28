from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=20)   
    slug = models.CharField(max_length=120)  
    timestamp = models.DateTimeField(blank=True)
    thumbnail = models.ImageField(upload_to = 'blog/images')

    def __str__(self) -> str:
        return self.title + ' by ' + self.author

class Blogcomment(models.Model):
    com_id = models.AutoField(primary_key= True)
    comment = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp = models.DateTimeField(default=now) 

    def __str__(self) -> str:
        return self.comment