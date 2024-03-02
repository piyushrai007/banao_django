from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import views as auth_views

class LogoutView(auth_views.LogoutView):
    allowed_methods = ['GET', 'POST']
    next_page = 'home'  # URL name of your home view

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.user_type == 'doctor':
                    return redirect('doctor_dashboard')
                elif user.user_type == 'patient':
                    return redirect('patient_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
# ... rest of your views ...
def home(request):
    return redirect('register')
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            return redirect('login')  # redirect to the login page
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

def doctor_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == 'doctor':
        return render(request, 'doctor_dashboard.html', {'user': request.user})
    else:
        return redirect('login')

def patient_dashboard(request):
    if request.user.is_authenticated and request.user.user_type == 'patient':
        return render(request, 'patient_dashboard.html', {'user': request.user})
    else:
        return redirect('login')