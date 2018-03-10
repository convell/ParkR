from django.forms import ModelForm, CharField
from .models import ParkingSpace
import googlemaps
import json

with open(".creds", "r+") as file:
    creds = json.loads(file.read())
    gmaps = googlemaps.Client(key=creds["google-api"])

class ParkingSpaceForm(ModelForm):
    class Meta:
        model = ParkingSpace
        fields = ('note',)
        exclude = ('owner', 'timeOpen', 'timeClose', 'lat','lng')

class ListingForm(ParkingSpaceForm):
    address = CharField()
    class Meta(ParkingSpaceForm.Meta):
        fields = ParkingSpaceForm.Meta.fields + ('address',)

    def clean_lat(self):
        data = self.cleaned_data.get('address', '')
        geocode_result = gmaps.geocode(data)
        geocode = json.load(geocode_result)
        data = geocode["result"]["geometry"]["location"]["lat"]
        print (data)
        return data

    def clean_lng(self):
        data = self.cleaned_data.get('address', '')
        geocode_result = gmaps.geocode(data)
        geocode = json.load(geocode_result)
        data = geocode["result"]["geometry"]["location"]["lng"]
        print (data)
        return data