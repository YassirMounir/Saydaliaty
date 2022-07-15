from django import forms
from django.forms import ModelForm
from .models import Clients
from django.contrib.auth.models import User


class ClientForm(ModelForm):

    class Meta:
        model = Clients
        fields = ['clt_lastname', 'clt_firstname',
                  'clt_tel', 'clt_city', 'clt_zip', 'clt_adresse']
        widgets = {
            'clt_lastname': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'clt_firstname': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'clt_tel': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'clt_city': forms.TextInput(attrs={
                'class': "form-control",
                'type': 'text'
            }),
            'clt_zip': forms.TextInput(attrs={
                'class': "form-control",
                'type': 'text'
            }),
            'clt_adresse': forms.TextInput(attrs={
                'class': "form-control",
                'type': 'text'
            })
        }


class ClientLogin(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control"
            }),
            'password': forms.PasswordInput(attrs={
                'class': "form-control"
            }),
        }
