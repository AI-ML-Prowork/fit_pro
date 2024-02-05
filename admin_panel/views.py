from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
import os

def base(request):
    return render(request, 'base.html')


from user_panel.models import Add_reward
from user_panel.models import Add_Order
from admin_panel.models import Add_Product

def dashboard(request):
    total_users = User.objects.count()
    total_rewards = Add_reward.objects.count()
    total_products = Add_Product.objects.count()
    total_orders = Add_Order.objects.count()

    context = {
        'total_users': total_users,
        'total_rewards': total_rewards,
        'total_products': total_products,
        'total_orders': total_orders,
    }

    return render(request, 'admin_panel/dashboard.html', context)


from django.shortcuts import render, redirect
from .models import Add_Product

#___________USING FORMS _____________________
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


#_____________USING TEMPLATES_______________________
def add_product(request):
    SIZE_CHOICES = Add_Product.SIZE_CHOICES
    MATERIAL_CHOICES = Add_Product.MATERIAL_CHOICES
    SUITABLE_FOR_CHOICES = Add_Product.SUITABLE_FOR_CHOICES
    PATTERN_CHOICES = Add_Product.PATTERN_CHOICES

    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        size = request.POST.get('size')
        colour = request.POST.get('colour')
        material = request.POST.get('material')
        suitable_for = request.POST.get('suitable_for')
        pattern = request.POST.get('pattern')

        Add_Product.objects.create(
            product_name=product_name,
            description=description,
            price=price,
            quantity=quantity,
            size=size,
            colour=colour,
            material=material,
            suitable_for=suitable_for,
            pattern=pattern
        )
        return redirect('admin_panel:product_list')

    else:
        return render(request, 'admin_panel/add_product.html', {
            'SIZE_CHOICES': SIZE_CHOICES,
            'MATERIAL_CHOICES': MATERIAL_CHOICES,
            'SUITABLE_FOR_CHOICES': SUITABLE_FOR_CHOICES,
            'PATTERN_CHOICES': PATTERN_CHOICES,
        })



def product_list(request):
    products = Add_Product.objects.all()
    return render(request, 'admin_panel/product_list.html', {'products': products})




from user_panel.models import Add_reward

def all_user_rewards(request):
    rewards = Add_reward.objects.all()
    return render(request, 'admin_panel/rewards_list.html', {'rewards': rewards})


from user_panel.models import UserProfile

def all_user_profile(request):
    profiles = UserProfile.objects.all()
    return render(request, 'admin_panel/user_profile_list.html', {'profiles': profiles})