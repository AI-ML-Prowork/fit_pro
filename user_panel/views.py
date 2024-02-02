from django.shortcuts import render, redirect,HttpResponse
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.models import User
import os



# Create your views here.
def base(request):
    return render(request, 'base.html')




