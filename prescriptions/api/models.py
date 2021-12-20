from django.db import models

# Create your models here.
class Prescript(models.Model):
    idDr = models.IntegerField()
    NationalIDPationt = models.CharField(max_length=20)
    comment = models.CharField(max_length=20)
    drugllist = models.CharField(max_length=100)
