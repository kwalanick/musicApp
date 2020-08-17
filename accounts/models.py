from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

# Create your models here.
import random


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have email')

        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=254,unique=True)
    username = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20)
    otp = models.CharField(max_length=128, blank=True)
    password = models.CharField(max_length=128, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    gender = models.CharField(max_length=1, default='N')
    county = models.CharField(max_length=100, default='')
    town = models.CharField(max_length=100, default='')
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'



