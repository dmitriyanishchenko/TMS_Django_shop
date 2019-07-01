from django.http import JsonResponse
from sweets.function import cart_create


def remove_from_cart_view(request):
    cart = cart_create(request)
    product_slug = request.GET.get('product_slug')
    cart.remove_from_cart(product_slug)
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse({'cart_total': cart.items.count(), 'cart_total_price': cart.cart_total})
