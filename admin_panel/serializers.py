from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class Add_ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_Product
        fields = '__all__'


