from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib import messages
from .models import Product,Contact
from django.views import View  
from .forms import ProductFilterForm
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
    
    context = {'Product' : Product.objects.all()[:10],
                'Laptop':Product.objects.filter(product_type='laptop'),
               'phone':Product.objects.filter(product_type='phone'),
               'mouse':Product.objects.filter(product_type='Mouse'),
               'book':Product.objects.filter(product_type='Book'),
               'keyboard':Product.objects.filter(product_type='Keyboard'),
               'shoes':Product.objects.filter(product_type='Shoes'),
               'tshirt':Product.objects.filter(product_type='Tshirt'),
               'electonics':Product.objects.filter(product_type='Electronics')
              }
    return render(request,'index.html', context)

from django.views.generic import TemplateView


# class index(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Product'] = Product.objects.all()
#         context['Laptop'] = Product.objects.filter(product_type='laptop')
#         context['phone'] = Product.objects.filter(product_type='phone')
#         return context



#objects.all()

# def profile(request):
#     return render(request,'profile.html')

# def contact(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         desc = request.POST.get('desc')
#         contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
#         contact.save()
#         messages.success(request, 'Your Query has been sent!')
#     return render(request,'contact.html')

class ContactView(View):
    def get(self,request, *args ,**kwargs):
        return render(request,'contact.html')
    
    def post(self,request,*args,**kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Query has been sent!')
        return render(request,'contact.html')


        
        


def product(request, id):
  
  mydata = Product.objects.filter(id=id).values()
#   template = loader.get_template('product.html')
  product = get_object_or_404(Product, id=id)
  pr = product.product_type

  print(pr)
  context = {
    'product': mydata,
    'recomend' : Product.objects.filter(product_type= pr)
  }

  return render(request,'product.html', context)


def order(request, id):
  mydata = Product.objects.filter(id=id).values()
  context = {
    'product': mydata,}
  return render(request,'order.html', context)





class Product_list(View): 
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        form = ProductFilterForm(request.GET)

        if form.is_valid():
            product_type = form.cleaned_data['product_type']
            if product_type:
                products = products.filter(product_type=product_type)

        # Pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 8)  # Set the number of products per page
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        return render(request, 'products.html', {'products': products, 'form': form})

           
        

# def product_list(request):

#     products = Product.objects.all()
#     filter_form = ProductFilterForm(request.GET)

#     if filter_form.is_valid():
#         product_type = filter_form.cleaned_data['product_type']
#         if product_type:
#             products = products.filter(product_type=product_type)

#     return render(request, 'products.html', {'products': products, 'filter_form': filter_form})


from django.http import JsonResponse
from accounts.models import Profile
from django.shortcuts import render


def update_profile(request):
    if request.method == 'POST':
        
        address = request.POST.get('address')
        landmark = request.POST.get('landmark')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')

        profile = Profile.objects.get(user=request.user)
        # # print(profile)
        # if not profile:
        #     profile = Profile.objects.create( address=address, landmark=landmark, state=state, postcode=postcode)
            
        # else:
          
        profile.address = address
        profile.landmark = landmark
        profile.state = state
        profile.postcode = postcode
        profile.save()

        return JsonResponse({'message': 'Profile updated successfully'})
    return JsonResponse({'error': 'Invalid request method'})