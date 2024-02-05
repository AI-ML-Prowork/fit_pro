from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout 
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
import os



# def index(request):
#         return render(request, 'index.html')   


def custom_login(request):
    if request.user.is_authenticated:

        return redirect('admin_panel:dashboard')  # Replace 'admin_panel:dashboard' with your dashboard URL

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user using Django's authentication system
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login successful
            login(request, user)
            return redirect('admin_panel:dashboard')  # Replace 'admin_panel:dashboard' with your dashboard URL
        else:
            # Login failed
            messages.error(request, 'Invalid username or password')

    return render(request, 'admin_panel/authenticate/login.html')   


@login_required(login_url='admin_panel:login')
def custom_logout(request):
    logout(request)
    return redirect('admin_panel:login')


# def index(request):
#     return render(request, 'index.html')


from user_panel.models import Add_reward
from user_panel.models import Add_Order
from admin_panel.models import Add_Product


@login_required(login_url='admin_panel:login')
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


@login_required(login_url='admin_panel:login')
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


@login_required(login_url='admin_panel:login')
def product_list(request):
    products = Add_Product.objects.all()
    return render(request, 'admin_panel/product_list.html', {'products': products})




from user_panel.models import Add_reward


@login_required(login_url='admin_panel:login')
def all_user_rewards(request):
    rewards = Add_reward.objects.all()
    return render(request, 'admin_panel/rewards_list.html', {'rewards': rewards})


from user_panel.models import UserProfile


@login_required(login_url='admin_panel:login')
def all_user_profiles(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'admin_panel/all_user_profiles.html', {'user_profiles': user_profiles})










# API VIEWS.PY

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from .serializers import Add_ProductSerializer
@api_view(['GET'])
def product_list_api(request):
    products = Add_Product.objects.all()
    product_serializer = Add_ProductSerializer(products, many=True)

    return Response({'status': 200, 'payload': product_serializer.data})


@api_view(['POST'])
def add_product_api(request):
    if request.method == 'POST':
        serializer3 = Add_ProductSerializer(data=request.data)
        if serializer3.is_valid():
            serializer3.save()
            return Response({'status': 201, 'message': 'Product added successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)
    


from .serializers import UserSerializer
@api_view(['GET'])
def user_list_api(request):
    users = User.objects.all()
    users_serializer = UserSerializer(users, many=True)

    return Response({'status': 200, 'payload': users_serializer.data})


@api_view(['POST'])
def add_user_api(request):
    if request.method == 'POST':
        serializer4 = UserSerializer(data=request.data)
        if serializer4.is_valid():
            # Create a new user with secure password handling
            user1 = serializer4.save()
            user1.set_password(request.data['password'])
            user1.save()

            return Response({'status': 201, 'message': 'User added successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided', 'errors': serializer4.errors}, status=status.HTTP_400_BAD_REQUEST)
    






# from .serializers import Ordered_ProductSerializer
# @api_view(['GET'])
# def order_list_api(request):
#     orders = Ordered_Product.objects.all()
#     orders_serializer = Ordered_ProductSerializer(orders, many=True)

#     return Response({'status': 200, 'payload': orders_serializer.data})


# @api_view(['POST'])
# def add_order_api(request):
#     if request.method == 'POST':
#         serializer1 = Ordered_ProductSerializer(data=request.data)
#         if serializer1.is_valid():
#             serializer1.save()
#             return Response({'status': 201, 'message': 'Order added successfully'}, status=status.HTTP_201_CREATED)
#         return Response({'status': 400, 'message': 'Invalid data provided'}, status=status.HTTP_400_BAD_REQUEST)