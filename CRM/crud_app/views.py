from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import CreateRecord
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
    form = LoginForm()                                 #import the form in a variable
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You Are Now Logged In Successfully!')
                return redirect('dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return redirect('login')
        else:
            messages.info(request, 'Username not registered, Register Now!')
            return redirect('register')
    context = {'form':form}
    return render(request, 'crud_app/login_page.html', context)


#Logout user
def logout(request):
    auth.logout(request)
    messages.success(request, 'You havve been logged out!')
    return redirect('/')


#user dashboard
@login_required(login_url='login')
def dashboard(request):
    my_records = CreateRecord.objects.all()
    context = {'my_records': my_records}
    return render(request, 'crud_app/dashboard.html', context)


#Create a record
@login_required(login_url='login')
def createrecord(request):
    form = CreateRecordForm()

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'crud_app/create_record.html', context)



#Update a record
@login_required(login_url='login')
def updaterecord(request, pk):
    record = CreateRecord.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid:
            form.save()
            messages.success(request, 'Updated Successfully!')
            return redirect('dashboard')
    context = {'form':form}
    return render(request, 'crud_app/update_record.html', context)



#View individual records
@login_required(login_url='login')
def viewrecord(request, pk):
    all_records = CreateRecord.objects.get(id=pk)
    context = {'records': all_records}
    return render(request, 'crud_app/view_record.html', context)