from django import forms
from .models import *

class Accountforms(forms.ModelForm):

    class Meta:
        model = Accounts
        fields = "__all__"
