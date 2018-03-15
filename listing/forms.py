from django.forms import ModelForm, CharField, HiddenInput
from .models import ParkingSpace

class ParkingSpaceForm(ModelForm):

    class Meta:
        model = ParkingSpace
        fields = ('note','lat','lng')
        exclude = ('owner', 'timeOpen', 'timeClose',)

    def __init__(self, *args, **kwargs):
        super(ParkingSpaceForm, self).__init__(*args, **kwargs)
        self.fields['lat'].widget = HiddenInput()
        self.fields['lng'].widget = HiddenInput()

    def clean(self):
        print("hello")

class ListingForm(ParkingSpaceForm):
    address = CharField()
    class Meta(ParkingSpaceForm.Meta):
        fields = ParkingSpaceForm.Meta.fields + ('address',)

    #def clean_lat(self):
    #    data = self.cleaned_data.get('address',)
    #    print (data)
    #    geocode_result = gmaps.geocode(data)
    #    geocode = json.load(geocode_result)
    #    data = geocode["result"]["geometry"]["location"]["lat"]
    #    print (data)
    #    return data

    #def clean_lng(self):
    #    data = self.cleaned_data.get('address',)
    #    print ("whats up")
    #    geocode_result = gmaps.geocode(data)
    #    geocode = json.load(geocode_result)
    #    data = geocode["result"]["geometry"]["location"]["lng"]
    #    print (data)
    #    return data

    def clean(self):
        print("hi")
        #return cleaned_data