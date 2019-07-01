from django.shortcuts import render
from sweets.function import cart_create
from sweets.models import (
    Category,
    Product,
    )


def product_view(request, product_slug):
    cart = cart_create(request)
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'cart': cart,
        'categories': categories,
    }
    return render(request, 'sweets/product.html', context)

