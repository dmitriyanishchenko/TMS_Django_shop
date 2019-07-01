from django.shortcuts import render
from sweets.forms import OrderForm
from sweets.function import cart_create
from sweets.models import Category


def order_create_view(request):
    categories = Category.objects.all()
    cart = cart_create(request)
    form = OrderForm(request.POST or None)
    context = {
        'form': form,
        'cart': cart,
        'categories': categories
    }
    return render(request, 'sweets/order.html', context)