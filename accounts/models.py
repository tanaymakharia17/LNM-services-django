from django.db import models


class Accounts(models.Model):

    user_name = models.CharField(max_length=25, primary_key=True)
    email = models.EmailField(unique=True)
    phone_num = models.BigIntegerField()
    password = models.CharField(max_length=25)
