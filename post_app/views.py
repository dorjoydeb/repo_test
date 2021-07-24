from django.shortcuts import render

post_page = 'post.html'


def home(request):
    return render(request, post_page)

# Create your views here.