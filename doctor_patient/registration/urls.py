# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),

    ]
