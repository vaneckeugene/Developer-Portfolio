from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'home.html', {'user': request.user})

def skills(request):
    return render(request, 'skills.html')

def logoutView(request):
    logout(request)
    return redirect('portfolio:login')

def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('portfolio:skills')

    return render(request, 'login_and_signup.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(f"New user has been saved.")
            return redirect('portfolio:login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration.html', {'form':form})