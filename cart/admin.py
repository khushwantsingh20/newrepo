from django.contrib import admin

# Register your models here.
from cart.models import CartItem,Orders



# Register your models here.
admin.site.register(CartItem)
admin.site.register(Orders)