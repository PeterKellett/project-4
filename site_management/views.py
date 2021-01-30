from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from products.models import Product, Category
from products.forms import ProductForm


# Create your views here.
def site_management(request):
    return render(request, 'site_management/landing.html')


def site_management_products(request):
    products = Product.objects.all().order_by('name')
    context = {
        'products': products,
    }
    return render(request, 'site_management/products.html', context)
