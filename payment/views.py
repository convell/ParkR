from django.shortcuts import render
from django.http import HttpResponse
from .functions import *

def payment(request):
    out = {}
    out["cost"] = "499"
    return render(request, 'payment/payment.html', out)

def process(request):
    stripe.api_key = "UGHNOTREAL"
    cost = "499" #where to pull this cost from...
#    if request.user.is_authenticated():

    charge = processPayment(request.POST['stripeToken'], "1000");

    print(charge)

    if charge is not "false":
        return render(request, 'payment/process.html', charge)

    fine = "success"
    print(fine)
    return HttpResponse(fine)
#    return render(request, 'payment/process.html')
# Create your views here.
