from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from shopping_bag.contexts import shopping_bag_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'shopping_bag': json.dumps(request.session.get('shopping_bag', {})),
            'save_info': request.POST.get('save-info'),
            'username': request.user
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry your payment could not be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


# Create your views here.
def checkout(request):
    print("checkout")
    # Stripe paymentIntent
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag = request.session.get('shopping_bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False) # Prevent 1st save happening
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(shopping_bag)
            order.save()
            for item_id, item_data in shopping_bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your shopping bag wasn't \
                            found in our database. Please try again."
                    ))
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form, \
                Please try again')
    else:
        shopping_bag = request.session.get('shopping_bag', {})
        if not shopping_bag:
            messages.error(request,
                           "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_shopping_bag = shopping_bag_contents(request)
        total = current_shopping_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing.')
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order was successfully processed, \
        Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    print("checkout success")
    return render(request, template, context)
