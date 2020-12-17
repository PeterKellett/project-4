from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# Create your views here.
def view_shopping_bag(request):
    """ A view to return the shopping bag contents page page """

    return render(request, 'shopping_bag/shopping-bag.html')


def add_to_shopping_bag(request, item_id):
    print("add_to_shopping_bag")
    # Get the product from the Product model \
    # using the item_id as the primary key
    product = get_object_or_404(Product, pk=item_id)
    # Obtain the quantity value from the form
    quantity = int(request.POST.get('quantity'))
    # Obtain the size value from the form
    size = request.POST['product_size']
    print(size)

    # For storing the shopping_bag contents to the session
    """
    1. Request the shopping_bag from the session variables
       or return an empty dictionary.
    """
    shopping_bag = request.session.get('shopping_bag', {})
    """
    2. Check if the item_id of the product to be added
       is already in the shopping_bag.
       If it is then just update the quantity.
       Else add the item_id and the quantity to
       the shopping_bag
    """
    if item_id in list(shopping_bag.keys()):
        if size in shopping_bag[item_id]['items_by_size'].keys():
            shopping_bag[item_id]['items_by_size'][size] += quantity
            messages.success(request,
                             f'Updates size {size.upper()} {product.name}\
                             quantity to \
                             {shopping_bag[item_id]["items_by_size"][size]}.')
        else:
            shopping_bag[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             f'Added size {size.upper()}\
                             {product.name} to your bag.')
    else:
        shopping_bag[item_id] = {'items_by_size': {size: quantity}}
        messages.success(request,
                         f'Added size {size.upper()}\
                         {product.name} to your bag.')

    """
    3. Now store the shopping_bag to the session
    variables as session.shopping_bag
    """
    request.session['shopping_bag'] = shopping_bag
    """
    4. Now redirect the user back to the url they were on previously
    """
    print("bag")
    print(request.session['shopping_bag'])
    return redirect(reverse('view_shopping_bag'))


def edit_shopping_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    previous_quantity = int(request.POST.get('previous_quantity'))
    quantity = int(request.POST.get('quantity'))
    previous_size = request.POST.get('previous_size')
    size = request.POST['product_size']
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})
    print(shopping_bag)
    shopping_bag[item_id]['items_by_size'].pop(previous_size)
    print(shopping_bag)

    if item_id in list(shopping_bag.keys()):
        if size in shopping_bag[item_id]['items_by_size'].keys():
            shopping_bag[item_id]['items_by_size'][size] += quantity
        else:
            shopping_bag[item_id]['items_by_size'][size] = quantity
    if previous_size != size:
        if previous_quantity != quantity:
            messages.success(request,
                             f'1 Updated {product.name} size {previous_size.title()}\
                             x {previous_quantity} to \
                             {size.title()} x {quantity}.')
        else:
            messages.success(request,
                             f'2 Updated {product.name} size {previous_size.title()}\
                             x {previous_quantity} to \
                             {size.title()}.')
    else:
        if previous_quantity != quantity:
            messages.success(request,
                             f'3 Updated {product.name} size {previous_size.title()}\
                             x {previous_quantity} to \
                             {size.title()} x {quantity}.')
        else:
            messages.success(request,
                             '4 You have not made any changes.')
    print(shopping_bag)

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def remove_from_shopping_bag(request, item_id):
    try:
        size = request.POST['product_size']
        shopping_bag = request.session.get('shopping_bag', {})

        del shopping_bag[item_id]['items_by_size'][size]
        if shopping_bag[item_id]['items_by_size'] == {}:
            shopping_bag.pop(item_id)

        request.session['shopping_bag'] = shopping_bag
        print(shopping_bag)
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
