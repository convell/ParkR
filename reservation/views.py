from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from listing.models import ParkingSpace
from .models import Reservation
from .forms import ReservationForm


def information(request, id):
    space = get_object_or_404(ParkingSpace, pk=id)
    space_owner = space.owner
    return render(request,
                  "reservation/space_info.html",
                  {'space': space,
                   'owner': space_owner}
                  )


@login_required
def new_reservation(request, id):
    if request.method == "POST":
        parking_space = get_object_or_404(ParkingSpace, pk=id)
        reservation = Reservation(reserved_user=request.user, reserved_space=parking_space)
        form = ReservationForm(instance=reservation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ReservationForm()
    return render(request, "reservation/reserve_form.html", {"id": id,
                                                             'form': form})


@login_required()
def reservation_history(request):
    reserved_spaces = Reservation.objects.filter(reserved_user=request.user)
    return render(request, 'reservation/reservation_history.html', {'reserved_spaces': reserved_spaces})
