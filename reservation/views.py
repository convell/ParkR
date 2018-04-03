from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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


# not being used -- saving for reference
@login_required()
def new_reservation(request, id):
    return render(request, "reservation/reserve_form.html", {"id": id})


@login_required()
def reservation_history(request):
    reserved_spaces = Reservation.objects.filter(reserved_user=request.user)
    return render(request, 'reservation/reservation_history.html', {'reserved_spaces': reserved_spaces})


@login_required()
def reservation_receipt(request):
    return render(request, 'reservation/reservation_receipt.html')


@login_required()
def process(request):
    stripe.api_key = "sk_test_8d5pC3u5kOvxymlk0U0x5JPJ"

    if request.user.is_authenticated:
        parking_space = get_object_or_404(ParkingSpace, pk=int(request.POST['spot_id']))
        reservation = Reservation(reserved_user=request.user, reserved_space=parking_space,
                                  start_time=request.POST['start_time'], end_time=request.POST['end_time'])
        reservation.save()

        charge = processPayment(request.POST['stripeToken'], "1000");

        if charge is not "false":
            return render(request, 'payment/process.html', charge)

    return redirect('reservation_receipt')
