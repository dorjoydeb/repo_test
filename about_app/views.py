from django.shortcuts import render
from .models import *
from layout_app.models import Footar

about_page = 'about.html'
def home(request):
    top_bar_data = About_top_bar.objects.all()
    main_content_data = About_main_content.objects.all()
    layout_data = Footar.objects.all()

    super ={
        't_b_data': top_bar_data,
        'm_c_data': main_content_data,
        'social': layout_data
    }

    return render(request, about_page, super)

# Create your views here.
