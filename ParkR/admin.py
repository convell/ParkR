from django.contrib import admin
from listing.models import ParkingSpace
from reservation.models import Reservation, PastReservation, Payment
from account.models import Profile, Reviews

admin.site.register(ParkingSpace)
admin.site.register(Reservation)
admin.site.register(PastReservation)
admin.site.register(Payment)
admin.site.register(Profile)
admin.site.register(Reviews)