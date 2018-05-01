from django.shortcuts import render
import json
from listing.models import ParkingSpace


# Create your views here.
def home(request):
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

    return render(request, 'ParkR/home.html', {"djangoMapMarkers":jsonList,"notes":noteList, "pidList":pidList})

def privacy(request):
    return render(request, 'account/privacypolicy.htm')
