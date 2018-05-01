from django.forms import ModelForm
from .models import Reviews, Profile


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        exclude = ('reviewed_user', 'reviewing_user')


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)
