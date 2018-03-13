from django import forms
from django.forms import ModelForm
from .models import Reservation
from bootstrap3_datetime.widgets import DateTimePicker


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        exclude = ('reserved_user', 'reserved_space', 'status', 'processed_time')
        widgets = {
            'start_time': DateTimePicker(options={"format": "YYYY-MM-DD",
                                                  "pickTime": True}),
            'end_time': DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
                                                "pickTime": True})
        }
