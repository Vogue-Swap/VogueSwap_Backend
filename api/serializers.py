from django.db import models
from .models import (AboutCloth,Barter,UserManager,User)
from rest_framework import serializers
from datetime import datetime
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import (RefreshToken,TokenError)
from dataclasses import field, fields
from importlib.metadata import files

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)

    permission_classes=[IsAuthenticated]
    class Meta:
        model=User
        fields=['email','username','password']

    def validate(self,attrs):
        email=attrs.get('email','')
        username=attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError("username should contain only alpha numeric chars")
        return attrs

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']

class BarterSerializer(serializers.ModelSerializer):
    class Meta:
          model=Barter
          fields='__all__'

class AboutClothSerializer(serializers.ModelSerializer):
    class Meta:
         model=AboutCloth
         fields='__all__'
        
                   