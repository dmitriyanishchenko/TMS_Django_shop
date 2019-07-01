from decimal import Decimal
from django.http import JsonResponse
from sweets.function import cart_create
from sweets.models import CartItem


def change_item_qty(request):
    cart = cart_create(request)
    qty = request.GET.get('qty')
    item_id = request.GET.get('item_id')
    cart_item = CartItem.objects.get(id=int(item_id))
    cart_item.qty = int(qty)
    cart_item.item_total = cart_item.qty * Decimal(cart_item.product.price)
    cart_item.save()
    new_cart_total = 0.00
    for item in cart.items.all():
        new_cart_total += float(item.item_total)
    cart.cart_total = new_cart_total
    cart.save()
    return JsonResponse(
        {'cart_total': cart.items.count(),
         'item_total': cart_item.item_total,
         'cart_total_price': cart.cart_total})