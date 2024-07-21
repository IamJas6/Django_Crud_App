from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#index page or main page
def index(request):
    return render(request, 'crud_app/index.html')


#Register form rendering in register page
def register(request):
    form = CustomUserCreationForm()                     #import the form in a variable
    if request.method == 'POST':                        #check whether the request method is post
        form = CustomUserCreationForm(request.POST)     #post all the data filled into this form
        if form.is_valid():                             #verifying whether the form is valid or not
            form.save()                                 #posting or saving the form details in database
            messages.success(request, 'Your Account Is Created Successfully!')                              
            return redirect('login')                    #redirecting to login page if form is valid
    context = {'form':form}                             #creating context of form to render on html page
    return render(request, 'crud_app/register_page.html', context)


#User registration form handling
def login(request):
    return render(request, 'crud_app/login_page.html')


def logout(request):
    pass


def dashboard(request):
    return render(request, 'crud_app/dashboard.html')
