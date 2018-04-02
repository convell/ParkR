from django.db import models
from django.contrib.auth.models import User
from listing.models import ParkingSpace

RESERVATION_STATUS_CHOICES = (
    ('P', 'Past Reservation'),
    ('C', 'Current Reservation'),
    ('F', 'Future Reservation'),
)


# Create your models here.
class Reservation(models.Model):
    reserved_user = models.ForeignKey(User, related_name="reserved_user", on_delete=models.CASCADE)
    reserved_space = models.ForeignKey(ParkingSpace, related_name="reserved_space", on_delete=models.CASCADE)
    reservation_price = models.IntegerField(default=0)
    status = models.CharField(max_length=1, default='F',
                              choices=RESERVATION_STATUS_CHOICES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    processed_time = models.DateTimeField(auto_now_add=True)


class PastReservation(models.Model):
    reserved_user = models.ForeignKey(User, related_name="past_reserved_user", on_delete=models.CASCADE)
    reserved_space = models.ForeignKey(ParkingSpace, related_name="past_reserved_space", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, default='F',
                              choices=RESERVATION_STATUS_CHOICES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    processed_time = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    reservation_price = models.IntegerField()
    paying_user = models.ForeignKey(User, related_name="paying_user", on_delete=models.CASCADE)
    space_to_reserve = models.ForeignKey(ParkingSpace, related_name="space_to_reserve", on_delete=models.CASCADE)
