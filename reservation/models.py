from django.db import models
from listing.models import ParkingSpace

RESERVATION_STATUS_CHOICES = (
    ('P', 'Past Reservation'),
    ('C', 'Current Reservation'),
    ('F', 'Future Reservation'),
)


# Create your models here.
class Reservation(models.Model):
    reservee = models.ForeignKey(ParkingSpace, related_name="reservee", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='F',
                              choices=RESERVATION_STATUS_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    reserved_time = models.DateTimeField(auto_now_add=True)

