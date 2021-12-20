from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=20,)
    nationalCode = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20,)

class Patient(models.Model):
    name = models.CharField(max_length=20,)
    nationalCode = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20,)
