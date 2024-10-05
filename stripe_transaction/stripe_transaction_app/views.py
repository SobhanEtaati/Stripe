from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transaction_response
import stripe
import json

def landing_page(request):
    return render(request, 'landing.html')


def checkout_session(request):
    stripe.api_key = 'YOUR_STRIPE_API_KEY'

    product = stripe.Product.create(
        # set a test product to see if your gateway is working properly 
        name = 'Test Product!',
        type = 'service',
    )

    price = stripe.Price.create(
        product = product.id,
        # set your desired unit amount and currency here
        unit_amount = 5000,
        currency = 'usd'
    )

    session = stripe.checkout.Session.create(
        # the payment type here is by Card
        payment_method_types = ['card'],
        line_items = [{
            'price' : price.id,
            'quantity' : 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
        
    id = session.get('id') 
    response_id = Transaction_response.objects.create(response_text = id)
    response_id.save()

    return redirect(session.url) 

def success(request):
    return HttpResponse("Payment successful! Check console for details.")

def cancel(request):
    return HttpResponse("Payment canceled.")

