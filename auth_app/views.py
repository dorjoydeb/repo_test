from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
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


def userlogin(request):
    if request.method == 'POST':
        name = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request,user)
            return redirect('blog.home')
        else:
            print('invalit user')

    return render(request, login_page)

def profile(request):
    return render(request, 'Profile.html')

def forget(request):
    return render(request, forget_page)

def userlogout(request):
    logout(request)
    return redirect('blog.home')

# Create your views here.
