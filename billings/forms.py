from django import forms

# import GeeksModel from models.py
from .models import Client


class ClientNewforms(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['amount_due']


class ClientEditforms(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['amount_due']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': True})
        }
