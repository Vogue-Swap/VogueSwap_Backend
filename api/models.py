from django.db import models
from distutils.command.upload import upload
from inspect import modulesbyfile
from unittest.util import _MAX_LENGTH
from django.conf import settings
from email.policy import default
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser,BaseUserManager,PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if username is None:
            raise TypeError("Users should have a username")

        if email is None:
            raise TypeError("Users should have a email")

        user=self.model(username=username,email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        if password is None:
            raise TypeError("Password should not be none")
        
        # user=self.create_user(username,email,password)
        user=self.create_user(username,email,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=255,unique=True,db_index=True)
    email=models.EmailField(max_length=255,unique=True,db_index=True)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()
    def __str__(self):
        return self.username

    def tokens(self):
        return ''

class AboutCloth(models.Model):
     category=models.CharField(max_length=100)
     size=models.CharField(max_length=10)
     '''image=models.ImageField(upload_to='images')'''

     def __str__(self):
        return self.category

class Barter(models.Model):
      '''user_foreign = models.ForeignKey(User, on_delete=models.CASCADE)'''
      name=models.CharField(max_length=50)
      state=models.CharField(max_length=50)
      district=models.CharField(max_length=50)
      pincode=models.CharField(max_length=6)
      email=models.EmailField(max_length=100)
      phone=models.CharField(max_length=10)

      def __str__(self):
        return self.name