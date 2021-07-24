from django.shortcuts import render

contact_page = 'contact.html'


def home(request):
    return render(request, contact_page)

# Create your views here.