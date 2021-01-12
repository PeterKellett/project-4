from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """A view to show all products including sorting and search queries"""
    # Get all products
    # Result <class 'products.models.Category'>
    products = Product.objects.all()
    # Get all categories
    # Result <class 'products.models.Category'>
    categories = Category.objects.all()
    filter_dict = {}
    query = None
    """
    1. First get all the products based on the individual sizes
        and store as individual querysets.
    """
    if request.GET:
        if 'all' in request.GET:
            filter_dict['all'] = True
        else:
            filter_dict['all'] = False
        if 'small' in request.GET:
            filter_dict['small'] = True
            small_queryset = products.filter(size_s=True)
        else:
            filter_dict['small'] = False
            small_queryset = products.filter(size_s=None)

        if 'medium' in request.GET:
            filter_dict['medium'] = True
            medium_queryset = products.filter(size_m=True)
        else:
            filter_dict['medium'] = False
            medium_queryset = products.filter(size_m=None)

        if 'large' in request.GET:
            filter_dict['large'] = True
            large_queryset = products.filter(size_lg=True)
        else:
            filter_dict['large'] = False
            large_queryset = products.filter(size_lg=None)

        if 'xlarge' in request.GET:
            filter_dict['xlarge'] = True
            xlarge_queryset = products.filter(size_xl=True)
        else:
            filter_dict['xlarge'] = False
            xlarge_queryset = products.filter(size_xl=None)
        """
        2: Now combine the sizes querysets into one queryset
        """
        products = small_queryset \
            | medium_queryset \
            | large_queryset \
            | xlarge_queryset
        """
        3. For each category not selected remove the items \
            from the combined queryset
        """
        for category in categories:
            category = str(category)
            if category in request.GET:
                filter_dict[category] = True
            else:
                filter_dict[category] = False
                category = [category]
                products = products.exclude(category__name__in=category)
                print("products exclude")
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

    else:
        filter_dict = {
            'all': True,
            'small': True,
            'medium': True,
            'large': True,
            'xlarge': True,
        }
        for category in categories:
            category = str(category)
            filter_dict[category] = True

    context = {
        'filter_dict': filter_dict,
        'products': products,
        'categories': categories,
        'search_term': query,
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


def add_product(request):
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
