from django.shortcuts import render
from django.http import HttpResponse

index_page = 'index.html'


def home(request):
    return render(request, index_page)

# Create your views here.
