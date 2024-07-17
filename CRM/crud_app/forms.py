from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # used to creeate form with authentication
from django.contrib.auth.models import User  # used for registering username and password
from django.forms.widgets import PasswordInput, TextInput, EmailInput  # used for password and text input based on imported form
from django import forms 

#Register or Create a user
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


#Login a user
class LoginForm(AuthenticationForm): #including authentication in the form
    username = forms.CharField(widget=TextInput)
    email = forms.CharField(widget=EmailInput)
    password = forms.CharField(widget=PasswordInput)