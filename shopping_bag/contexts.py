from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def shopping_bag_contents(request):
    shopping_bag_items = []
    total = 0
    registered_discount = settings.REGISTERED_DISCOUNT
    discount = 0
    gross_total = 0
    product_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, item_data in shopping_bag.items():
        if isinstance(item_data, int):
            print("if")
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            shopping_bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'total': total,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                sub_total = quantity * product.price
                product_count += quantity
                shopping_bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'sub_total': sub_total,
                })
                total += sub_total
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
    else:
        delivery = 0

    if request.user.is_authenticated:
        discount = (
            total * Decimal(registered_discount/100))
    gross_total = delivery + total - discount

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'registered_discount': registered_discount,
        'discount': discount,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'gross_total': gross_total,
    }

    return context
