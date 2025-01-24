from django.db import models

# Create your models here.
class User(models.Model):
     name=models.CharField(max_length=50)
     doc=models.BooleanField(default=False)
     email=models.EmailField(unique=True)
     pswd=models.CharField(max_length=128)
     city=models.CharField(max_length=50)
     state=models.CharField(max_length=50)
     country=models.CharField(max_length=50)

# class Doctor(models.Model):