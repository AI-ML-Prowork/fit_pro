from django.shortcuts import render, redirect,HttpResponse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
import os



# Create your views here.
def home(request):
    return render(request, 'home.html')


from user_panel.models import UserProfile

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

def reward_history(request):
    rewards = Add_reward.objects.filter(username=request.user)
    return render(request, 'user_panel/reward_history.html', {'rewards': rewards})



from .models import Wallet

def add_wallet_transaction(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_mode = request.POST.get('payment_mode')

        Wallet.objects.create(
            amount=amount,
            payment_mode=payment_mode
        )

    return render(request, 'user_panel/wallet.html')