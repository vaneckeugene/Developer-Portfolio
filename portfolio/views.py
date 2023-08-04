from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    """This view renders the home page
        :param request: takes in request object

        :returns: response of resulting strings after interpolating templates and context data

        :rtype: response object
    """
    return render(request, 'home.html', {'user': request.user})

def skills(request):
    """This view renders the skills page
        :param request: takes in request object

        :returns: response of resulting strings after interpolating templates and context data

        :rtype: response object
    """
    return render(request, 'skills.html')

def logoutView(request):
    """This view logs the user out and redirects to login page
        :param request: takes in request object

        :returns: logs out the user and redirects to the login page

        :rtype: response object
    """
    logout(request)
    return redirect('portfolio:login')

def loginView(request):
    """This view enables the user to log in using their credentials
        :param request: takes in request object

        :returns: the login page which enables the user to access the project

        :rtype: response object
    """
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('portfolio:skills')

    return render(request, 'login_and_signup.html')

def registerView(request):
    """This view registers new users and redirects them to the login page
        :param request: takes in request object

        :returns: registration form which, after completion redirects to the login page

        :rtype: response object
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(f"New user has been saved.")
            return redirect('portfolio:login')
    else:
        form = UserCreationForm()
    
    return render(request, 'registration.html', {'form':form})