from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hack
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"hacks":Hack.objects.all})

def register(request): # NB: The default request is a GET request
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid(): # check the form filled out correctly
            user = form.save() # commit the new user record to the database
            username = form.cleaned_data.get("username")
            messages.success(request, f"New Account Created: {username}")
            login(request=request, user=user) # so new user doesn't have to login again afer registering
            messages.info(request, f"You are now logged in as: {username}")
            return redirect("main:homepage") # arg using the variable names created in urls.py in main
        else:
            # Implement a short-term error handling solution:
            for msg in form.error_messages: # form.error_messages is a dict
                # print(form.error_messages[msg]) # prints errors to console
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request=request, # This handles the default GET request
                  template_name="main/register.html",
                  context={"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request=request,
                                  data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,
                                password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as: {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    
    form = AuthenticationForm()
    return render(request=request,
                  template_name="main/login.html",
                  context={"form": form})
            
    
    
    
    
    
    