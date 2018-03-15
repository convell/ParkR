import stripe

def processPayment(token, cost):
    charge = stripe.Charge.create(
      amount = cost,
      currency = "usd",
      description = "Test charge",
      source = token,
    )

    print (stripe.Charge.retrieve(charge["id"]).items())

    return errors( stripe.Charge.retrieve(charge["id"]) )

def errors(charge):
    if charge["failure_code"]:
        return "handleshit"
    return "false"
