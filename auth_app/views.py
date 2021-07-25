from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from layout_app.models import *
from django.contrib import messages

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
        name = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully login complete')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid User and password')
    return render(request, login_page)


def exep(request):
     return HttpResponse('i am exep')

@login_required
def profile(request):
    return render(request, 'Profile.html')

def forget(request):
    return render(request, forget_page)

def userlogout(request):
    logout(request)
    return redirect('blog.home')

# Create your views here.
