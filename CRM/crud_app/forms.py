from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # used to creeate form with authentication
from django.contrib.auth.models import User  # used for registering username and password
from django.forms.widgets import PasswordInput, TextInput, EmailInput  # used for password and text input based on imported form
from django import forms 


class CustomUserCreationForm(UserCreationForm):     #Register or Create a user
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):    #Login a user ,   including authentication in the form
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput)
