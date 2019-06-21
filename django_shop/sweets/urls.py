from django.urls import path
from .views import (
    base_view,
    category_view,
    product_view,
    cart_view,
    add_to_cart_view,
    remove_from_cart_view
)

urlpatterns = [

    path('', base_view, name='base'),
    path('category/<str:category_slug>/', category_view, name='category_detail'),
    path('product/<slug:product_slug>/', product_view, name='product_detail'),
    path('cart/', cart_view, name='cart'),
    path('add_to_cart/<slug:product_slug>/', add_to_cart_view, name='add_to_cart'),
    path('remove_from_cart/<slug:product_slug>/', remove_from_cart_view, name='remove_from_cart'),

]
