from django.db import models
class reg(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone = models.IntegerField()
    email=models.EmailField()
    user=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
class login(models.Model):
    username=models.CharField(max_length=51)
    password=models.CharField(max_length=15)
# Create your models here.
