from django.contrib import admin
from listing.models import ParkingSpace
from reservation.models import Reservation, PastReservation

admin.site.register(ParkingSpace)
admin.site.register(Reservation)
admin.site.register(PastReservation)