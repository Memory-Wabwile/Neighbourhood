from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Neighbourhood,Business,Post

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)