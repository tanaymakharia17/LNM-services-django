from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from accounts.models import Accounts
import random


class Products(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.BigIntegerField()
    username = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='products_imgs', blank=True, null=True)
    contact_num = models.BigIntegerField(default=0)
    color = models.CharField(max_length=20, default='#007bff')

    @staticmethod
    def get_random_colour():
        l = ["#007bff", "#6c757d", "#28a745", "#dc3545",
             "#ffc107", "#17a2b8", "#f8f9fa", "#343a40"]
        x = random.randint(0, 7)
        return (l[x])


class Wishlist(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    username = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, null=False)
