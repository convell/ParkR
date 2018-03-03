from django.forms import ModelForm
from .models import ParkingSpace


class ListingForm(ModelForm):
    class Meta:
        model = ParkingSpace
        exclude = ('owner', 'timeOpen', 'timeClose')