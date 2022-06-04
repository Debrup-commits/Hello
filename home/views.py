from http.client import HTTPResponse
from urllib.robotparser import RequestRate
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'x': 'yea maine variable k thru bheja hai'
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        Email=request.POST.get('Email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, Email=Email, phone=phone, desc=desc, date=datetime.today())
        contact.save()

        messages.success(request, 'Your message has been submitted!')

    return render(request, "contact.html")

