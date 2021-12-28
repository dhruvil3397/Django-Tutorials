from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    category = models.CharField(max_length=100,default = "")
    type = models.CharField(max_length=100,default = "")
    brand = models.CharField(max_length=100,default = "")
    model = models.CharField(max_length=100,defau = "")
    color = models.CharField(max_length=100,default = "")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200,default = "")
    pub_date = models.DateField()
    image = models.ImageField(upload_to = 'shop/images',default = "")

    def __str__(self) -> str:
        return self.category
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(blank=True,null=True)
    message = models.CharField(max_length=500,)

    def __str__(self) -> str:
        return self.name