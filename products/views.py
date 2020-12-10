from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib import sessions
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    """A view to show all products including sorting and search queries"""
    products = Product.objects.all()
    categories = Category.objects.all()

    query = None
    current_category = None
    """
    Filters 2 step process:
    1. Filter the sizes into individual querysets and amalgamate all into one 
        queryset before eliminating categories.
    """
    if request.GET:
        if 'small' in request.GET:
            small = bool(request.GET['small'])
            small_queryset = products.filter(size_s=True)
        else:
            small = False
            small_queryset = products.filter(size_s=None)

        if 'medium' in request.GET:
            medium = bool(request.GET['medium'])
            medium_queryset = products.filter(size_m=True)
        else:
            medium = False
            medium_queryset = products.filter(size_m=None)

        if 'large' in request.GET:
            large = bool(request.GET['large'])
            large_queryset = products.filter(size_lg=True)
        else:
            large = False
            large_queryset = products.filter(size_lg=None)

        if 'xlarge' in request.GET:
            xlarge = bool(request.GET['xlarge'])
            xlarge_queryset = products.filter(size_xl=True)
        else:
            xlarge = False
            xlarge_queryset = products.filter(size_xl=None)
        products = small_queryset | medium_queryset | large_queryset | xlarge_queryset
        """
        2. Now exclude the products from the queryset if the category is not checked.
            If the category is checked the queryset remains untouched.
        """
        if 'soccer' in request.GET:
            soccer = bool(request.GET['soccer'])
            products = products
        else:
            soccer = False
            category = ['soccer']
            products = products.exclude(category__name__in=category)

        if 'rugby' in request.GET:
            rugby = bool(request.GET['rugby'])
            products = products
        else:
            rugby = False
            category = ['rugby']
            products = products.exclude(category__name__in=category)

        if 'gaa' in request.GET:
            gaa = bool(request.GET['gaa'])
            products = products
        else:
            gaa = False
            category = ['gaa']
            products = products.exclude(category__name__in=category)

        if 'other' in request.GET:
            other = bool(request.GET['other'])
            products = products
        else:
            other = False
            category = ['other']
            products = products.exclude(category__name__in=category)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query)
                       | Q(description__icontains=query))
            products = products.filter(queries)

    else:
        soccer = True
        rugby = True
        gaa = True
        other = True
        small = True
        medium = True
        large = True
        xlarge = True

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
        'current_category': current_category,
        'soccer': soccer,
        'rugby': rugby,
        'gaa': gaa,
        'other': other,
        'small': small,
        'medium': medium,
        'large': large,
        'xlarge': xlarge,
    }
    print("END")
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to an individual product details """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'products/product-detail.html', context)
