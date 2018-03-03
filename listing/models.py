from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ParkingSpace(models.Model):
    class Meta:
        verbose_name = 'Parking Space'
        verbose_name_plural = 'Parking Spaces'

    def __unicode__(self):
        return 'Parking Space: ' + self.note

    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    lat = models.CharField(max_length=300, default="0")
    lng = models.CharField(max_length=300, default="0")
    note = models.CharField(max_length=300)
    timeOpen = models.CharField(max_length=300, default="0")
    timeClose = models.CharField(max_length=300, default="0")
