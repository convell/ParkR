from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from listing.models import ParkingSpace
from .models import Reservation
from .functions import *


def information(request, id):
    space = get_object_or_404(ParkingSpace, pk=id)
    space_owner = space.owner

    return render(request, "reservation/space_info.html", {"id": id,
                                                           'space': space,
                                                           'owner': space_owner})


@login_required()
def new_reservation(request, id):

    return render(request, "reservation/reserve_form.html", {"id": id})


@login_required()
def reservation_history(request):
    reserved_spaces = Reservation.objects.filter(reserved_user=request.user)
    return render(request, 'reservation/reservation_history.html', {'reserved_spaces': reserved_spaces})


@login_required()
def process(request):
    stripe.api_key = "***REMOVED***"
    cost = "499"  # where to pull this cost from...
    #    if request.user.is_authenticated():
    print(request.POST['spot_id'], type(request.POST['spot_id']))
    parking_space = get_object_or_404(ParkingSpace, pk=int(request.POST['spot_id']))
    reservation = Reservation(reserved_user=request.user, reserved_space=parking_space,
                              start_time=request.POST['start_time'], end_time=request.POST['end_time'])
    reservation.save()

    charge = processPayment(request.POST['stripeToken'], "1000");

    #print(charge)

    if charge is not "false":
        return render(request, 'payment/process.html', charge)

    fine = "success"
    print(fine)
    return HttpResponse(fine)


