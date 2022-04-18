from django.contrib import admin
from django.urls import path , include, re_path
from . import views

urlpatterns = [
    path('', views.landing , name='landing'),
    path('home/', views.home , name='home'),
    path('profile/', views.profile , name = "profile"),
    path('search/' , views.search , name = "search"),
    path('updateProfile/' , views.updateProfile , name = "updateProfile"),
    path('post/', views.post, name='post'),
    path('hood/' , views.hood , name ='hood'),

]