from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

#Create home function
def index(request):
    """The Home Page for Penny algo"""
    return render(request, 'website_picam/index.html')

#Create login function
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'website_picam/login.html')
