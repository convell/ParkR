from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import parkingSpace

class PostForm(forms.ModelForm):
    class Meta:
        model = parkingSpace
        fields = ('lat','lng', 'note',)
        widgets = {
        'lat': forms.TextInput(attrs={'class':'reserveForm','placeholder':'lattitude'}),
        'lng': forms.TextInput(attrs={'class':'reserveForm','placeholder':'longitude'}),
        'note': forms.TextInput(attrs={'class':'reserveForm','placeholder':'note'}),
        }

class UserCreationFormEmail(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    def save(self, commit=True):
        user=super(UserCreationFormEmail,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user
