from django.shortcuts import render
from sweets.function import cart_create
from sweets.models import Category


def cart_view(request):
    categories = Category.objects.all()
    cart = cart_create(request)
    context = {
        'cart': cart,
        'categories': categories
    }
    return render(request, 'sweets/cart.html', context)

