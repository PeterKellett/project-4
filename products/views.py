from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib import sessions
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    request.session['color'] = 'blue'
    sess = request.session
    print(sess)
    print("color = ")
    print(request.session['color'])
    """A view to show all products including sorting and search queries"""
    products = Product.objects.all()
    categories = Category.objects.all()

    medium = None
    large = None
    xlarge = None
    query = None
    current_category = None

    if request.GET:
        if 'medium' in request.GET:
            small = request.session['small']
            print(small)
            if small == 'False':
                request.session['small'] = False
                small_queryset = products.filter(size_s=None)
                print("exclude small_queryset")
                print(small_queryset)
            else:
                small_queryset = products.filter(size_s=True)
                print("include small_queryset")
                print(small_queryset)
            medium = request.GET['medium']
            if medium == 'False':
                medium = False
                medium_queryset = products.filter(size_m=None)
                print("exclude medium_queryset")
                print(medium_queryset)
            else:
                medium_queryset = products.filter(size_m=True)
                print("include medium_queryset")
                print(medium_queryset)

            large = request.GET['large']
            if large == 'False':
                large = False
                large_queryset = products.filter(size_lg=None)
                print("exclude large_queryset")
                print(large_queryset)
            else:
                large_queryset = products.filter(size_lg=True)
                print("include large_queryset")
                print(large_queryset)
            xlarge = request.GET['xlarge']
            if xlarge == 'False':
                xlarge = False
                xlarge_queryset = products.filter(size_xl=None)
                print("exclude xlarge_queryset")
                print(xlarge_queryset)
            else:
                xlarge_queryset = products.filter(size_xl=True)
                print("include xlarge_queryset")
                print(xlarge_queryset)
            products = small_queryset | medium_queryset | large_queryset | xlarge_queryset
        print("products result")
        print(products)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (Q(name__icontains=query)
                       | Q(description__icontains=query))
            products = products.filter(queries)

        if 'category' in request.GET:
            current_category = request.GET['category'].split(',')
            products = products.filter(category__name__in=current_category)
            current_category = request.GET['category']
    else:
        request.session['small'] = None
        medium = None
        large = None
        xlarge = None
    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
        'current_category': current_category,
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
