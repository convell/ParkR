from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import ListingForm
from .models import ParkingSpace


# Create your views here.
@login_required
def new_space(request):
    if request.method == "POST":
        listing = ParkingSpace(owner=request.user)
        form = ListingForm(instance=listing, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = ListingForm()
    return render(request, "listing/new_space_form.html", {'form': form})