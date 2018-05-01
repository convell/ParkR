from django.contrib.auth.models import User
from django.db import models
import googlemaps
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class ParkingSpace(models.Model):
    class Meta:
        verbose_name = 'Parking Space'
        verbose_name_plural = 'Parking Spaces'

    def __str__(self):
        return 'Parking Space: ' + self.note

    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    lat = models.CharField(max_length=300, default="0")
    lng = models.CharField(max_length=300, default="0")
    note = models.CharField(max_length=300)
    timeOpen = models.CharField(max_length=300, default="0")
    timeClose = models.CharField(max_length=300, default="0")
    parkingPrice = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
