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
    path('hood/<int:id>' , views.hood , name ='hood'),
    path('joinhood/<id>', views.joinhood, name='joinhood'),
    path('leavehood/<id>', views.leavehood, name='leavehood'),
    path('newhood/', views.newhood , name = 'newhood'),
    path('business/' , views.business , name='business'),
    path('logout/', views.logout_user, name='logout'),

]