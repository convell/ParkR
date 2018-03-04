from django.shortcuts import render
import stripe

def payment(request):
    out = {}
    out["cost"] = "499"
    return render(request, 'payment/payment.html', out)

def process(request):
    stripe.api_key = "***REMOVED***"
    cost = "499" #insert your var
    #if request.method == 'POST':
        #form = PostForm(request.POST)
#       if request.user.is_authenticated():
    print (request.POST.items())
    token = request.POST['stripeToken']

    charge = stripe.Charge.create(
      amount = cost,
      currency = "usd",
      description = "Test charge",
      source = token,
    )

    print (stripe.Charge.retrieve(charge["id"]).items())

    return render(request, 'payment/process.html')
# Create your views here.
