from django.db import models
# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    telephone = models.IntegerField()

class Product(models.Model):
    #image= models.CharField(max_length=1000)
    image=models.ImageField(upload_to='static/img')
    category = models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    rate=models.IntegerField()