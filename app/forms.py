from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nume', 'prenume', 'telefon', 'adresa']
