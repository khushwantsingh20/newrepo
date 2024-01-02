from django.urls import path, include

from .views import *
urlpatterns = [
    path("",index, name='home'),
    path("contact",ContactView.as_view(), name='contact'),
    # path("profile",profile, name='profile'),
    path('product/<int:id>/',product, name='product'),
    path('order/<int:id>/',order, name='order'),
    path('update_profile',update_profile, name='update_profile'),
    path('product_list/',  Product_list.as_view(), name='product_list'),
    
]

