from django.db import models
from accounts.models import Accounts
import random
# Create your models here.


class Blog(models.Model):

    pickup = models.CharField(max_length=100, null=False, default='')
    drop = models.CharField(max_length=100, null=False, default='')
    username = models.ForeignKey(
        Accounts, on_delete=models.CASCADE, null=False, default='')
    space = models.IntegerField(null=False, default=0)
    contact_num = models.BigIntegerField(null=False, default=0)
    fare = models.IntegerField(null=False, default=0)
    date = models.DateField(null=False)
    time = models.TimeField(null=False)
    color = models.CharField(max_length=20, default='#007bff')

    @staticmethod
    def get_random_colour():
        l = ["#007bff", "#6c757d", "#28a745", "#dc3545",
             "#ffc107", "#17a2b8", "#f8f9fa", "#343a40", ]
        x = random.randint(0, 7)
        return (l[x])
