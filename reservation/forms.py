from django.forms import ModelForm
from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = ('reserved_user', 'reserved_space', 'status', 'processed_time')

