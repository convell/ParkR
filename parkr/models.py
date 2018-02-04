from django.db import models

class parkingSpace(models.Model):
    owner = models.CharField(max_length="300",default="0")
    lat = models.CharField(max_length="300",default="0")
    lng = models.CharField(max_length="300",default="0")
    note = models.CharField(max_length="300",default="0")
    timeOpen = models.CharField(max_length="300",default="0")
    timeClose = models.CharField(max_length="300",default="0")
# Create your models here.
