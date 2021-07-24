from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from layout_app.models import Footar

index_page = 'index.html'
def home(request):
    index_data = Index_Top_bar.objects.all()
    layout_data = Footar.objects.all()

    super = {
        'all_data': index_data,
        'social': layout_data,
    }

    return render(request, index_page, super)

# Create your views here.
