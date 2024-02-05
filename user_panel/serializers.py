from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class wallet_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'



class Add_reward_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_reward
        fields = '__all__'


class Add_Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Order
        fields = '__all__'       