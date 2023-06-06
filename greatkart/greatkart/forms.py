from django import forms as f
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Registerform(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','username','email','password1','password2']