from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('register/', views.register, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create_record/', views.createrecord, name="createrecord"),
    path('update_record/<int:pk>', views.updaterecord, name="updaterecord"),
    path('view_record/<int:pk>', views.viewrecord, name="viewrecord"),
]