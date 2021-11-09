from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
# Create your views here.

# def home(request):
#     return HttpResponse("Hello!")

def home(request):
    return render(request, "myapp/home.html")

def about(request):
    return render(request, "myapp/about.html")

def contact(request):
    return render(request, "myapp/contact.html")


def test(request, name):
    return render(request, "myapp/test.html",
        {
        'name' : name,
        'date' : datetime.now()
        }
    )

