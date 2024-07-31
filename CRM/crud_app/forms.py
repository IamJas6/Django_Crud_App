from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # used to creeate form with authentication
from django.contrib.auth.models import User  # used for registering username and password
from django.forms.widgets import PasswordInput, TextInput, EmailInput  # used for password and text input based on imported form
from django import forms 
from .models import CreateRecord

class CustomUserCreationForm(UserCreationForm):     #Register or Create a user
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):    #Login a user ,   including authentication in the form
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput)


#CRUD Operation forms

#Create Record Form
class CreateRecordForm(forms.ModelForm): 
    class Meta:
        model = CreateRecord
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


#Upodate Record Form
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = CreateRecord
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']