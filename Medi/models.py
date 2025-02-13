from django.db import models
from django.db import models
from django.contrib.auth.models import User  # Ensure this import is present

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=100, name="name")
    specialization = models.CharField(max_length=100, name="specialization")
    experience = models.IntegerField(name="experience")
    phone = models.CharField(max_length=10, name="phone")
    email = models.EmailField(name="email")
    address = models.TextField(name="address")
    date = models.DateField()

# Create your models here.
class User(models.Model):
     name=models.CharField(max_length=50)
     doc=models.BooleanField(default=False)
     email=models.EmailField(unique=True)
     pswd=models.CharField(max_length=128)
     city=models.CharField(max_length=50)
     state=models.CharField(max_length=50)
     country=models.CharField(max_length=50)

'''class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, name="name")
    specialization = models.CharField(max_length=100, name="specialization")
    experience = models.IntegerField(name="experience")
    phone = models.CharField(max_length=10,name="phone")
    email = models.EmailField(name="email")
    address = models.TextField(name="address")
    date=models.DateField()'''


'''

class Availability(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'doc': True}, default=2)  # Use an existing doctor ID
    date = models.DateField()
    morning_start = models.TimeField()
    morning_end = models.TimeField()
    evening_start = models.TimeField()
    evening_end = models.TimeField()
'''
class Availability(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'doc': True})  # Removed default=2
    date = models.DateField()
    morning_start = models.TimeField()
    morning_end = models.TimeField()
    evening_start = models.TimeField()
    evening_end = models.TimeField()
