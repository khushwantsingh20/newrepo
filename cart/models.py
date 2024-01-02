from django.db import models
import datetime
# Create your models here.
from django.db import models

# Create your models here.
# models.py

from django.contrib.auth.models import User
from django.db import models

from home.models import Product
from accounts.models import Profile

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,null=True,blank=True)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        if self.product:
            return self.quantity * self.product.price
        else:
            return 0

    def __str__(self):
        if self.product:
          return f"{self.user.username} - {self.product.name}"
        
            






class Orders(models.Model):
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,null=True,blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE ,null=True ,blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)
    quantity=models.IntegerField( default=1)

    # class Meta:
    #     # Remove the unique_together constraint to allow multiple entries for the same product and user
    #     unique_together = ('product', 'profile', 'status', 'quantity')


    def price(self):
        return self.quantity * self.product.price
    
    

    

    
        
