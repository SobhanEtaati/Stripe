from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transaction_response
import stripe
import json

def landing_page(request):
    return render(request, 'landing.html')


def checkout_session(request):
    stripe.api_key = 'sk_test_51OAdGsFWdpagdbCvzvF0RIx1kUklCPIV6AMmhGLChsMdiYH3OHMFSDFT5ZkNAeTahYpwWZmIneEyzZ3pKfkQIVil00VW3kvF5a'

    product = stripe.Product.create(
        name = 'Test Product!',
        type = 'service',
    )

    price = stripe.Price.create(
        product = product.id,
        unit_amount = 5000,
        currency = 'usd'
    )

    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = [{
            'price' : price.id,
            'quantity' : 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
        

    print('**************************************')  
    id = session.get('id') 
    print(id)

    response_id = Transaction_response.objects.create(response_text = id)
    response_id.save()

    print(f'Redirecting to: {session.url}')
    return redirect(session.url) 

def success(request):
    return HttpResponse("Payment successful! Check console for details.")

def cancel(request):
    return HttpResponse("Payment canceled.")

