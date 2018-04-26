from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from listing.models import ParkingSpace, User
from .forms import ReviewsForm
from .models import Reviews


# Create your views here.
@login_required()
def profile(request):
    spaces = ParkingSpace.objects.filter(owner=request.user)
    return render(request, 'account/profile.html', {'owned_spaces': spaces})


def show(request, id):
    showUser = get_object_or_404(User, pk=id)
    spaces = ParkingSpace.objects.filter(owner=showUser)
    reviews = Reviews.objects.filter(reviewed_user=showUser)
    return render(request,
                  "account/show.html",
                  {'owned_spaces': spaces,
                   'showUser': showUser,
                   'reviews' :reviews}
                  )


@login_required
def leave_review(request, id):
    if request.method == "POST":
        current_user = get_object_or_404(User, pk=id)
        review = Reviews(reviewed_user=current_user, reviewing_user=request.user)
        form = ReviewsForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_show', id=id)
    else:
        form = ReviewsForm()
    return render(request, "account/review_form.html", {'form': form,
                                                        'id': id})


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "account/signup_form.html"
    success_url = reverse_lazy('user_login')
