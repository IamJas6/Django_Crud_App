from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'crud_app/index.html')


def login(request):
    return render(request, 'crud_app/login.html')


def register(request):
    return render(request, 'crud_app/register.html')


def dashboard(request):
    return render(request, 'crud_app/dashboard.html')


def logout(request):
    pass