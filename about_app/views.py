from django.shortcuts import render

about_page = 'about.html'


def home(request):
    return render(request, about_page)

# Create your views here.
