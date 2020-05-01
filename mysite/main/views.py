from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hack
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"hacks":Hack.objects.all})

def register(request): # NB: The default request is a GET request
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): # check the form filled out correctly
            user = form.save() # commit the new user record to the database
            login(request=request, user=user) # so new user doesn't have to login again afer registering
            return redirect("main:homepage") # arg using the variable names created in urls.py in main
        else:
            # Implement a short-term error handling solution:
            for msg in form.error_messages: # form.error_messages is a dict
                print(form.error_messages[msg]) # prints errors to console

    form = UserCreationForm
    return render(request=request, # This handles the default GET request
                  template_name="main/register.html",
                  context={"form": form})

