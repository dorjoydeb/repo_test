from django.shortcuts import render
from layout_app.models import Footar
from .models import *

post_page = 'post.html'

def home(request):
    social_data = Footar.objects.all()
    post_top_bar = Post_top_bar.objects.all()
    post_blog_section = Post_Blog_sections.objects.all()

    super = {
        'social': social_data,
        'p_t_data': post_top_bar,
        'p_b_data': post_blog_section
    }


    return render(request, post_page, super)

# Create your views here.