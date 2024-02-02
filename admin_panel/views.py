from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
import os




# from django.shortcuts import render
# from .forms import ProductForm

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ProductForm()

#     return render(request, 'admin_panel/add_product.html', {'form': form})


from django.shortcuts import render, redirect
from .models import Product

def add_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        # Perform any additional validation if needed

        Product.objects.create(
            product_name=product_name,
            price=price,
            quantity=quantity
        )
    return render(request, 'admin_panel/add_product.html')



def product_list(request):
    products = Product.objects.all()
    return render(request, 'admin_panel/product_list.html', {'products': products})