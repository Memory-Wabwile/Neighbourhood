from django.shortcuts import render
from .models import Profile, Neighbourhood, Business, Post

# Create your views here.

def landing(request):
    message = "landing page"

    return render (request ,'landing.html' , {'message':message})

def home(request):
    message = "Home page"

    hood = Neighbourhood.objects.all()

    return render (request,'home.html',{'message':message , 'hood':hood})

def profile(request):
    message = "Profile page"

    return render (request, 'profile.html' , {'message':message})

def post(request):
    message = "create a post"

    return render(request, 'post.html' , {'messsage':message})

def hood(request,id):
    message = "hoods page"
    hood=Neighbourhood.objects.get(id=id)
    current_hood=hood.name
    buseness=Business.objects.filter(neighbourhood=id)
    posts=Post.objects.filter(neighborhood=id)
    

    return render (request , 'hood.html' , {'message':message,'hood':hood ,'business':buseness,'current_hood':current_hood,'posts':posts})


def search(request):
    message = "searched items"

    return render (request , 'search.html' , {'message':message})

def updateProfile(request):
    message = "update profile"

    return render (request , 'updateProfile.html' , {'message':message})
