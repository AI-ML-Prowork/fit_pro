from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

        

class Add_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Product
        fields = '__all__'


# class UserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = '__all__'


class Ordered_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordered_Product
        fields = '__all__'


# class wallet_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Wallet
#         fields = '__all__'