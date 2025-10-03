from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_register,name='register'),
    path('login/', views.user_login,name='login'),
    path('dashboard/', views.admin_dashboard,name='dashboard'),
    path('userdashboard/', views.user_dashboard,name='userdashboard'),
    path('staffdashboard/', views.staff_dashboard,name='staffdashboard'),
]
