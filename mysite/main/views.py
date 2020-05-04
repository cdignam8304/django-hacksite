from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hack, HackCategory, HackSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.

def single_slug(request, single_slug):
    """"
        Determine whether single_slug relates to a Category or a Tutorial
        Params:
            - single_slug: e.g. in  "localhost:8000/admin/", admin is the single_slug
    """
    categories = [c.category_slug for c in HackCategory.objects.all()]
    if single_slug in categories:
        
        # Get the series that relate to the category that was selected:
        matching_series = HackSeries.objects.filter(hack_category__category_slug=single_slug)
        
        # Find the tutorials that are part 1s from the matching series and
        # store each matching series object and the first tutorial of each series in a dict:
        series_urls = {}
        for m in matching_series.all():
            part_one = Hack.objects.filter(hack_series__hack_series=m.hack_series).earliest("hack_published")
            series_urls[m] = part_one.hack_slug
        
        return render(request=request,
                      template_name="main/category.html",
                      context={"part_ones":series_urls})
    
    hacks = [h.hack_slug for h in Hack.objects.all()]
    if single_slug in hacks:
        # return HttpResponse(f"{single_slug} is a Hack!!!")
        this_hack = Hack.objects.get(hack_slug=single_slug)
        hacks_from_series = Hack.objects.filter(hack_series__hack_series=this_hack.hack_series)
        this_hack_idx = list(hacks_from_series).index(this_hack)
        return render(request=request,
                      template_name="main/hack.html",
                      context={"hack":this_hack,
                               "sidebar":hacks_from_series,
                               "this_hack_idx":this_hack_idx})
        
    
    return HttpResponse(f"{single_slug} is not a HackCategory or a Hack!!!")


def homepage(request):
    # return render(request=request,
    #               template_name="main/home.html",
    #               context={"hacks":Hack.objects.all})
    return render(request=request,
                  template_name="main/categories.html",
                  context={"categories":HackCategory.objects.all})


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
            
    
    
    
    
    
    