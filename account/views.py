from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from listing.models import ParkingSpace, User


# Create your views here.
@login_required()
def profile(request):
    spaces = ParkingSpace.objects.filter(owner=request.user)
    return render(request, 'account/profile.html', {'owned_spaces': spaces})


def show(request, id):
    showUser = get_object_or_404(User, pk=id)
    spaces = ParkingSpace.objects.filter(owner=showUser)
    return render(request,
                  "account/show.html",
                  {'owned_spaces': spaces,
                   'showUser': showUser}
                  )


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "account/signup_form.html"
    success_url = reverse_lazy('user_login')
