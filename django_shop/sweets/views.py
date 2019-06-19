from django.shortcuts import render
from .models import Category, Product


def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'sweets/base.html', context)


def product_view(request, product_slug):

    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    context = {
        'product': product,

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
