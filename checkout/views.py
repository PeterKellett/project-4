from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from .forms import OrderForm
from shopping_bag.contexts import shopping_bag_contents

import stripe
import jsonify
# This is your real test secret API key.
stripe.api_key = 'sk_test_51Hc6RJCM38ctaxuaBv8hgRtrgRqfLRfgmDHWPNOdmyN6qctu8YXmpW4N0Q0b70IRzcMw1lj2CbV9itmphqZ6ZsS800R1QCl4WP'


# Create your views here.
def checkout(request):
    print("checkout")
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Hc6RJCM38ctaxuamPwSiRWXRaZdcUO0lkMBtah39LWPAWeZ5miVTI5AFZ6HKoKxramtCHnNbWN65KpnsG8zwhHq00PNDuqE0S',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)


def create_checkout_session():
    print("create_checkout_session")
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='checkout/success.html',
            cancel_url='checkout/cancel.html',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403
