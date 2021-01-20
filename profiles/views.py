from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Reviews, Product
from .forms import UserProfileForm
from checkout.models import Order


# Create your views here.
@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    total_orders = orders.count()
    all_reviews = profile.reviews.all()
    total_reviews = all_reviews.count()
    reviews_subset = all_reviews[:5]

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'total_orders': total_orders,
        'all_reviews': all_reviews,
        'reviews_subset': reviews_subset,
        'total_reviews': total_reviews,
        'profile': profile,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order {order_number}'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile_page': True,
    }
    return render(request, template, context)


@login_required
def add_review(request, product_id):
    redirect_url = request.POST.get('redirect_url')
    comment = request.POST.get('comment')
    print("comment = ", comment)
    profile = get_object_or_404(UserProfile, user=request.user)
    print("profile = ", profile)
    product = get_object_or_404(Product, pk=product_id)
    print("product = ", product)
    review = Reviews(
                    user_profile=profile,
                    product=product,
                    comment=comment,
                )
    review.save()
    messages.success(request, 'You have successfully added a review. Thank you!')
    return redirect(redirect_url)
