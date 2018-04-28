from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from listing.models import ParkingSpace
from .models import Reservation
from .functions import *
import json, googlemaps

fromFile = True

if fromFile == True:
    with open(".creds", "r+") as file:
        creds = json.loads(file.read())
        gmaps = googlemaps.Client(key=creds["google-api"])
else:
    gmaps = googlemaps.Client(key=os.environ['GOOGLE'])


def information(request, id):
    space = get_object_or_404(ParkingSpace, pk=id)
    space_owner = space.owner
    address = "Middle of Nowhere"
    if not space.lat == "0":
        lat = space.lat
        lng = space.lng
        address = gmaps.reverse_geocode((lat,lng))[0]["formatted_address"]
    return render(request, "reservation/space_info.html", {"id": id,
                                                           'space': space,
                                                           'owner': space_owner,
                                                           'address': address})


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
                                  start_time=request.POST['start_data'], end_time=request.POST['end_data'])
        reservation.save()

        charge = processPayment(request.POST['stripeToken'], "1000");

        print("res", charge)

        if charge is not "false":
            return HttpResponse('payment/process.html')

    out = {
      "route": "reservation_receipt"
    }

    return JsonResponse(out)
