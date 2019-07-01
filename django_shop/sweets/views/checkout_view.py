from django.shortcuts import render
from sweets.function import cart_create
from sweets.models import Category


def checkout_view(request):
    cart = cart_create(request)
    categories = Category.objects.all()
    context = {
        'cart': cart,
        'categories': categories
            }
    return render(request, 'sweets/checkout.html', context)