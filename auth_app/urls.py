from django.urls import path
from . import views

urlpatterns =[
    path('', views.register, name='register'),
    path('login/', views.userlogin, name='login'),
    path('forget_password/', views.forget, name='forget'),
    path('user_profile/', views.profile, name='profile'),
    path('user_logout/', views.userlogout, name='user_logout')
]