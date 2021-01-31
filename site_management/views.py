from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from products.models import Product, Category
from products.forms import ProductForm
from checkout.models import Order, OrderLineItem
from profiles.models import Reviews


# Create your views here.
def site_management(request):
    return render(request, 'site_management/landing.html')


def site_management_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'site_management/products.html', context)


def site_management_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders,
    }
    return render(request, 'site_management/orders.html', context)


def site_management_reviews(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'site_management/reviews.html', context)
