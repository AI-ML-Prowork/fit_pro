from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
import os



@login_required(login_url='signin/')
def base(request):
    return render(request, 'user_base.html')





def signup(request):

    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':

        first_name = request.POST.get('First_Name')
        last_name = request.POST.get('Last_Name')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        confirm_password = request.POST.get('Confirm_Password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('/signup/')
        
        # Create a new user
        user = User.objects.create_user(
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        login(request, user)
        messages.success(request, 'Account created successfully')
        return redirect('/signin/') 
    
    return render(request, 'user_panel/authenticate/signup.html')



def signin(request):

    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/') 
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'user_panel/authenticate/signin.html')


from user_panel.models import UserProfile
@login_required(login_url='signin/')
def add_user_profile(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        age = request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        any_disease = request.POST.get('any_disease')
        allergies = request.POST.get('allergies')

        # Validate the form data here if needed

        user_profile = UserProfile.objects.create(
            user_name=user_name,
            age=age,
            height=height,
            weight=weight,
            any_disease=any_disease,
            allergies=allergies
        )
        user_profile.save()

        # Redirect to a success page or another view
        return redirect('/')  # Replace 'success_page' with your actual URL name
    else:
        return render(request, 'user_panel/add_user_profile.html')
    


from django.utils import timezone
from user_panel.models import Add_reward

@login_required(login_url='signin/')
def add_reward(request):
    if request.method == 'POST':
        # Retrieve data from the request
        steps_count = request.POST.get('steps_count')
        calories_burn = request.POST.get('calories_burn')
        rewards = request.POST.get('rewards')
        age = request.POST.get('age')

        # Create Add_reward instance and save it to the database
        reward_instance = Add_reward.objects.create(
            username=request.user,
            steps_count=steps_count,
            calories_burn=calories_burn,
            rewards=rewards,
            last_login=timezone.now(),
            age=age
        )
        reward_instance.save()

        # Redirect to a success page or any other page you prefer
        return redirect('/')

    return render(request, 'user_panel/add_reward.html')
@login_required(login_url='signin/')
def reward_history(request):
    rewards = Add_reward.objects.filter(username=request.user)
    return render(request, 'user_panel/reward_history.html', {'rewards': rewards})



from .models import Wallet

@login_required(login_url='signin/')
def add_wallet_transaction(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_mode = request.POST.get('payment_mode')

        Wallet.objects.create(
            amount=amount,
            payment_mode=payment_mode
        )

    return render(request, 'user_panel/wallet.html')

def wallet_history(request):
    transactions = Wallet.objects.all().order_by('-date')
    return render(request, 'user_panel/wallet_history.html', {'transactions': transactions})



from user_panel.models import Add_Order


@login_required(login_url='signin/')
def add_order(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        amount = request.POST.get('amount')
        user_id = request.POST.get('user')  # Assuming user_id is submitted as part of the form
        user = User.objects.get(pk=user_id)
        steps_count = request.POST.get('steps_count')
        calories_burn = request.POST.get('calories_burn')
        rewards = request.POST.get('rewards')

        Add_Order.objects.create(
            item_name=item_name,
            amount=amount,
            user=user,
            steps_count=steps_count,
            calories_burn=calories_burn,
            rewards=rewards
        )

        return redirect('/')  
    else:

        users = User.objects.all()
        return render(request, 'user_panel/add_order.html', {'users': users})


@login_required(login_url='signin/')
def orders_history(request):
    orders = Add_Order.objects.all()
    return render(request, 'user_panel/orders_history.html', {'orders': orders})


@login_required(login_url='signin/')
def logout(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('/signin/')




# API VIEWS.PY

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserProfileSerializer
from .serializers import UserSerializer
@api_view(['GET'])
def profile_list_api(request):
    profiles = UserProfile.objects.all()
    profiles_serializer = UserProfileSerializer(profiles, many=True)

    return Response({'status': 200, 'payload': profiles_serializer.data})



@api_view(['POST'])
def add_profile_api(request):
    if request.method == 'POST':
        serializer2 = UserProfileSerializer(data=request.data)
        if serializer2.is_valid():
            serializer2.save()
            return Response({'status': 201, 'message': 'Profile added successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer2.errors}, status=status.HTTP_400_BAD_REQUEST)
    


from .serializers import wallet_Serializer
@api_view(['GET'])
def wallet_list_api(request):
    wallets = Wallet.objects.all()
    wallets_serializer = wallet_Serializer(wallets, many=True)

    return Response({'status': 200, 'payload': wallets_serializer.data})





@api_view(['POST'])
def add_money_to_wallet(request):
    if request.method == 'POST':
        print(request.data)
        serializer = wallet_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'message': 'Money added to wallet successfully'}, status=status.HTTP_201_CREATED)
        return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




from .serializers import UserProfileSerializer
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
    

from .serializers import Add_reward_Serializer
from .models import Add_reward
class rewards_api(APIView):

    def get(self, request):
        rewards = Add_reward.objects.all()
        rewards_serializer = Add_reward_Serializer(rewards, many=True)
        return Response({'status': 200, 'payload': rewards_serializer.data})
    
    def post(self, request):
        if request.method == 'POST':
            print(request.data)
            serializer5 = Add_reward_Serializer(data=request.data)
            if serializer5.is_valid():
                serializer5.save()
                return Response({'status': 201, 'message': 'Reward added successfully'}, status=status.HTTP_201_CREATED)
            return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer5.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    
    def patch( self, request):
        rewards = Add_reward.objects.get(pk=request.data["id"])
        serializer5 = Add_reward_Serializer(rewards, data=request.data, partial=True)
        if serializer5.is_valid():
            serializer5.save()
            return Response({'status': 200, 'message': 'Reward updated successfully'}, status=status.HTTP_200_OK)
        return Response({'status': 400, 'message': 'Invalid data provided', 'errors': serializer5.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request):
        id = request.data['id']
        rewards = Add_reward.objects.get(id=id)
        rewards.delete()
        return Response({'status': 200, 'message': 'Reward deleted successfully'}, status=status.HTTP_200_OK)
    


from .serializers import Add_Order_Serializer
from .models import Add_Order


class orders_api(APIView):

    def get(self, request):
        orders = Add_Order.objects.all()
        orders_serializer = Add_Order_Serializer(orders, many=True)
        return Response({'status': 200, 'payload': orders_serializer.data})
    
    def post(self, request):
        if request.method == 'POST':
            print(request.data)
            serializer6 = Add_Order_Serializer(data=request.data)
            if serializer6.is_valid():
                serializer6.save()
                return Response({'status': 201, 'message': 'Order added successfully'}, status=status.HTTP_201_CREATED)
            return Response({'status': 400, 'message': 'Invalid data provided','errors': serializer6.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def patch( self, request):
        orders = Add_Order.objects.get(pk=request.data["id"])
        serializer6 = Add_Order_Serializer(orders, data=request.data, partial=True)
        if serializer6.is_valid():
            serializer6.save()
            return Response({'status': 200, 'message': 'Order updated successfully'}, status=status.HTTP_200_OK)
        return Response({'status': 400, 'message': 'Invalid data provided', 'errors': serializer6.errors}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request):
        id= request.GET.get["id"]
        orders = Add_Order.objects.get(id=id)
        orders.delete()
        return Response({'status': 200, 'message': 'Order deleted successfully'}, status=status.HTTP_200_OK)