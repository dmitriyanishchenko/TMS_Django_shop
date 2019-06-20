from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import (
    Category,
    Product,
    CartItem,
    Cart
)


def base_view(request):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'cart': cart
    }
    return render(request, 'sweets/base.html', context)


def product_view(request, product_slug):
    cart = Cart.objects.first()
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,
        'cart': cart,
        'categories': categories,
    }
    return render(request, 'sweets/product.html', context)


def category_view(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products_of_category = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products_of_category': products_of_category
    }
    return render(request, 'sweets/category.html', context)


def cart_view(request):
    categories = Category.objects.all()
    cart = Cart.objects.first()
    context = {
        'cart': cart,
        'categories': categories
    }
    return render(request, 'sweets/cart.html', context)


def add_to_cart_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
    cart = Cart.objects.first()
    if new_item not in cart.items.all():
        cart.items.add(new_item)
        cart.save()
        return HttpResponseRedirect('/cart/')





