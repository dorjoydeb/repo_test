from django.shortcuts import render
from django.http import HttpResponse
from layout_app.models import *

register_page = 'register.html'
login_page = 'login.html'
forget_page = 'forget.html'


def register(request):
    socialdata = Footar.objects.all()
    
    super = {
        'social': socialdata
    }
    return render(request, register_page, super)


def login(request):
    return render(request, login_page)


def forget(request):
    return render(request, forget_page)

# Create your views here.
