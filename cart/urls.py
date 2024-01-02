# urls.py

from django.urls import path
from .views import add_to_cart, cart_detail,remove,orderdelail,checkout,cartbuy,remove_to_cart

app_name = 'cart'

urlpatterns = [
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('detail/', cart_detail, name='cart_detail'),
    path('remove/<int:id>/', remove, name='remove'),
    path('orderdelail/', orderdelail, name='orderdelail'),
    path('order/<int:id>/checkout/',checkout, name='checkout'),
    path('cartbuy/',cartbuy, name='cartbuy'),
    path('remove_to_cart/<int:id>/',remove_to_cart, name='remove_to_cart'),
]
