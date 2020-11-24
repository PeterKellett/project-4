from django.shortcuts import render


# Create your views here.
def view_shopping_bag(request):
    """ A view to return the shopping bag contents page page """

    return render(request, 'shopping_bag/shopping-bag.html')
