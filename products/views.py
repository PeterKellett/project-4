from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """A view to show all products including sorting and search queries"""
    # Get all products
    # Result <class 'products.models.Category'>
    products = Product.objects.all().order_by('name')
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

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to an individual product details """
    product = get_object_or_404(Product, pk=product_id)
    all_reviews = product.reviews.all().order_by('-date')
    total_reviews = all_reviews.count()

    context = {
        'product': product,
        'all_reviews': all_reviews,
        'total_reviews': total_reviews,
    }
    return render(request, 'products/product-detail.html', context)


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only users with admin rights can access this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'New product added successfully.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only users with admin \
                            rights can access this')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'You have successfully updated product')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product. \
                               Please ensure all fields are correct.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, 'You are editing product.')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry only users with admin \
                            rights can access this')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))
