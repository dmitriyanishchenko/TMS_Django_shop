from django.shortcuts import render
from sweets.models import (
    Category,
    Order
)


def account_view(request):
    order = Order.objects.filter(user=request.user).order_by('-id')
    categories = Category.objects.all()
    context = {
        'order': order,
        'categories': categories
    }
    return render(request, 'sweets/account.html', context)
