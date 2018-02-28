from django.db import models

class parkingSpace(models.Model):

    class Meta:
        verbose_name = 'Parking Space'
        verbose_name_plural = 'Parking Spaces'

    def __unicode__(self):
        return 'Parking Space: ' + self.note

    owner = models.CharField(max_length=300,default="0")
    lat = models.CharField(max_length=300,default="0")
    lng = models.CharField(max_length=300,default="0")
    note = models.CharField(max_length=300,default="0")
    timeOpen = models.CharField(max_length=300,default="0")
    timeClose = models.CharField(max_length=300,default="0")
# Create your models here.
