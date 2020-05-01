from django.shortcuts import render
from django.http import HttpResponse
from .models import Hack

# Create your views here.

def homepage(request):
    # return HttpResponse("<p>Hello, world!</p><p>Welcome to <strong>hacksite</strong></p>")

    return render(request=request,
                  template_name="main/home.html",
                  context={"hacks":Hack.objects.all})