from django.forms import ModelForm, CharField, HiddenInput
from .models import ParkingSpace
import googlemaps
import json

with open(".creds", "r+") as file:
    creds = json.loads(file.read())
    gmaps = googlemaps.Client(key=creds["google-api"])

class ParkingSpaceForm(ModelForm):

    class Meta:
        model = ParkingSpace
        fields = ('note','lat','lng')
        exclude = ('owner', 'timeOpen', 'timeClose',)

    def __init__(self, *args, **kwargs):
        super(ParkingSpaceForm, self).__init__(*args, **kwargs)
        self.fields['lat'].widget = HiddenInput()
        self.fields['lng'].widget = HiddenInput()

    def clean_lat(self):
        data = self.cleaned_data.get('address',)
        print (data)
        geocode_result = gmaps.geocode(data)
        geocode = json.load(geocode_result)
        data = geocode["result"]["geometry"]["location"]["lat"]
        print (data)
        return data

    def clean_lng(self):
        data = self.cleaned_data.get('address', '')
        print ("whats up")
        geocode_result = gmaps.geocode(data)
        geocode = json.load(geocode_result)
        data = geocode["result"]["geometry"]["location"]["lng"]
        print (data)
        return data

    def clean(self):
        print("hello")

class ListingForm(ParkingSpaceForm):
    address = CharField()
    class Meta(ParkingSpaceForm.Meta):
        fields = ParkingSpaceForm.Meta.fields + ('address',)

    def clean(self):
        super(ParkingSpaceForm, self).clean_lat()
        #print (cleaned_data)
        #return cleaned_data