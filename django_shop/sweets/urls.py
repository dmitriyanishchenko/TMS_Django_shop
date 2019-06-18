from django.urls import path
from .views import (
    base_view,
    category_view,
    product_view,

)

urlpatterns = {

    path('', base_view, name='base'),
    path('category/<str:category_slug>/', category_view, name='category_detail'),
    path('product/<slug:product_slug>/', product_view, name='product_detail'),
}
