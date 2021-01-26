from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
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
    redirect_url = request.POST.get('redirect_url')
    print('redirect_url', redirect_url)
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
            messages.warning(request,
                             f'You already have this item in your basket. \
                                 {product.name} {size.upper()}.')
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
    return redirect(redirect_url)


def edit_shopping_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    previous_quantity = int(request.POST.get('previous_quantity'))
    quantity = int(request.POST.get('quantity'))
    previous_size = request.POST.get('previous_size')
    size = request.POST['product_size']
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})
    shopping_bag[item_id]['items_by_size'].pop(previous_size)

    if item_id in list(shopping_bag.keys()):
        if size in shopping_bag[item_id]['items_by_size'].keys():
            shopping_bag[item_id]['items_by_size'][size] += quantity
        else:
            shopping_bag[item_id]['items_by_size'][size] = quantity
    if previous_size != size:
        if previous_quantity != quantity:
            messages.success(request,
                             f'You have changed {product.name} size {previous_size.title()}\
                             x {previous_quantity} to \
                             {size.title()} x {quantity}.')
        else:
            messages.success(request,
                             f'You have changed {product.name} size {previous_size.title()}\
                              to {size.title()}.')
    else:
        if previous_quantity != quantity:
            messages.success(request,
                             f'You have changed {product.name} size {previous_size.title()}\
                             x {previous_quantity} to \
                             {size.title()} x {quantity}.')
        else:
            messages.info(request,
                          "It's ok, you have not made any changes.")
    print(shopping_bag)

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def remove_from_shopping_bag(request, item_id):
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = request.POST['product_size']
        shopping_bag = request.session.get('shopping_bag', {})

        del shopping_bag[item_id]['items_by_size'][size]
        if shopping_bag[item_id]['items_by_size'] == {}:
            shopping_bag.pop(item_id)
        messages.success(request,
                         f'Removed {product.name} size {size.upper()}\
                                  from your bag.')
        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
