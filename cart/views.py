from pyexpat.errors import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import render
from django.views import View  
# Create your views here.
# views.py

from django.shortcuts import render, redirect
from requests import request

from home.models import Product
from .models import *
from .forms import AddToCartForm





def add_to_cart(request,id):
    
    product = Product.objects.get(id=id)
    quantity=1
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += quantity
        # print(cart_item.quantity)
    else:
        cart_item.quantity = quantity

    cart_item.save()
    # return HttpResponseRedirect(request.path_info)  
    return redirect('cart:cart_detail')

def remove_to_cart(request,id):
    
    product = Product.objects.get(id=id)
    
    cart_item = CartItem.objects.get(user=request.user, product=product)
    quantity=cart_item.quantity
    if quantity > 1:
     
     cart_item.quantity = quantity - 1
    else:
        return redirect('cart:cart_detail')

    cart_item.save()
        
    return redirect('cart:cart_detail')

    
    #return render(request, 'cart_detail.html', {'form': form, 'product': product})

def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if cart_items.count() != 0 :
        total_price = sum(item.total_price() for item in cart_items)
        return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})
    else:
        
        return render(request, 'emptycart.html')

    


def remove(request, id):

    product = CartItem.objects.get(id=id)
    try:
        product.delete()   
    except CartItem.DoesNotExist:
        pass
    return redirect('cart:cart_detail')



def cartbuy(request):

    try:
        # Retrieve the user's cart items
        cart_items = CartItem.objects.filter(user=request.user)

        # Create a new order for each cart item
        for cart_item in cart_items:
            product=cart_item.product
            if product.stock >= cart_item.quantity:
              
              Orders.objects.create(product=product,profile=request.user.profile,quantity=cart_item.quantity,status=False)  
              product.stock -= cart_item.quantity
              product.save()
              
            
            else:
                messages.warning(request, f'Not enough stock for {product.name} product stock is {product.stock}')
                return redirect('cart:cart_detail')
         
        cart_items.delete()
        messages.success(request,'your product ordered successfully')
        return redirect("/")    
        
    except Exception as e:
       
        return render(request, 'error_page.html', {'error': str(e)})
    
    
    # product = Book.objects.get(id=id)
    # print(id,"********************************************************************************************")
    
    # cart = CartItem.objects.get(user=request.user)
    # try:
    #     cart_item = cart.cartitem_set.get(product=product)
    #     if cart_item.quantity >= 1:
    #          cart_item.delete()
    # except CartItem.DoesNotExist:
    #     pass
    
    # return redirect('cart_detail')
   

# class orderdetail(TemplateView):
#     template_name = "order.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['orders'] = Orders.objects.filter(profile= request.user.profile)

#         return context

   
def orderdelail(request):
   try:
       orders = Orders.objects.filter(profile=request.user.profile)
       return render(request,'orderl.html',{'orders':orders})
   except Exception as e:
       return render(request,'orderl.html')
       
       
       
   




def checkout(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        try:
            quantity = request.POST.get('quantity')

            if product.stock >= int(quantity):
                order = Orders.objects.create(profile=request.user.profile, product=product)
                order.quantity = int(quantity)
                order.save()
                product.stock -= int(quantity)
                product.save()
                
                messages.success(request, 'Your product is ordered')
                return redirect('home')
                    
            else:
                messages.warning(request, f'Product is out of Stock,product item is {product.stock} ')
                return redirect('home')
                
                
            
        except Exception as e:
            messages.warning(request, f'An error occurred: {e}')
            print("----------------------------------------------------------------------------------------")
            return redirect('home')

    