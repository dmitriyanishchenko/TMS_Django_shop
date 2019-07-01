from django.shortcuts import render
from sweets.function import cart_create
from sweets.models import (
    Category,
    Product
    )


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cart = cart_create(request)
    context = {
        'categories': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'sweets/base.html', context)
