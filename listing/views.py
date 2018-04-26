from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import googlemaps
import json
import os
from .forms import ListingForm
from .models import ParkingSpace

fromFile = False

if fromFile == True:
    with open(".creds", "r+") as file:
        creds = json.loads(file.read())
        gmaps = googlemaps.Client(key=creds["google-api"])
else:
    gmaps = googlemaps.Client(key=os.environ['GOOGLE'])
    
# Create your views here.
@login_required
def new_space(request):
    if request.method == "POST":
        listing = ParkingSpace(owner=request.user)
        form = ListingForm(instance=listing, data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            address = form.cleaned_data['address']
            geocode_result = gmaps.geocode(address)
            print(geocode_result)
            if geocode_result:
                print(geocode_result[0]["geometry"]["location"]["lat"])
                instance.lat=geocode_result[0]["geometry"]["location"]["lat"]
                instance.lng=geocode_result[0]["geometry"]["location"]["lng"]
                instance.save()
            else:
                print("oh snap")
            return redirect('user_profile')
    else:
        form = ListingForm()
    return render(request, "listing/new_space_form.html", {'form': form})
