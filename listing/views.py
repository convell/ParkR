from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
import googlemaps
import json
import os
from .forms import ListingForm
from .models import ParkingSpace

fromFile = True

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
            print(request.POST)
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


@login_required()
def delete_space(request, id):
    parking_space = get_object_or_404(ParkingSpace, pk=id)
    parking_space.delete()

    latlngList = []
    noteList = []
    pidList = []
    allObjects = ParkingSpace.objects.all()
    for result in allObjects.values():
        lat = result.get("lat")
        lng = result.get("lng")
        note = result.get("note")
        pid = int(result.get("id"))
        latlng = {"lat": float(lat), "lng": float(lng)}
        pidList.append(pid)
        latlngList.append(latlng)
        noteList.append(note)
    jsonList = json.dumps(latlngList)
    noteList = json.dumps(noteList)
    pidList = json.dumps(pidList)

    return render(request, 'ParkR/home.html', {"djangoMapMarkers": jsonList, "notes": noteList, "pidList": pidList})
