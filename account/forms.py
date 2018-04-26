from django.forms import ModelForm
from .models import Reviews


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        exclude = ('reviewed_user', 'reviewing_user')