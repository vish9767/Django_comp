from django.db import models

# Create your models here.
class slid(models.Model):
    dec=models.TextField(max_length=200)
    Name=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='pics')


class dev(models.Model):
    Name=models.CharField(max_length=50)
    dec=models.TextField(max_length=200)
    price=models.IntegerField()
    pic=models.ImageField(upload_to='pics')


class complaint(models.Model):
    user_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=30)
    company_name=models.CharField(max_length=50)
    mobile_name=models.CharField(max_length=50)
    problem=models.TextField(max_length=200)
    pic=models.ImageField(upload_to='pics')