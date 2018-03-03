from django.shortcuts import render
import json
from listing.models import ParkingSpace


# Create your views here.
def home(request):
    latlngList = []
    noteList = []
    allObjects = ParkingSpace.objects.all()
    for result in allObjects.values():
        lat = result.get("lat")
        lng = result.get("lng")
        note = result.get("note")
        latlng = {"lat": float(lat), "lng": float(lng)}
        latlngList.append(latlng)
        noteList.append(note)
    jsonList = json.dumps(latlngList)
    noteList = json.dumps(noteList)

    return render(request, 'ParkR/home.html', {"djangoMapMarkers":jsonList,"notes":noteList})
