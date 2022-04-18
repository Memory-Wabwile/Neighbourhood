from django.shortcuts import render

# Create your views here.

def landing(request):
    message = "landing page"

    return render (request ,'landing.html' , {'message':message})

def home(request):
    message = "Home page"

    return render (request,'home.html',{'message':message})

def profile(request):
    message = "Profile page"

    return render (request, 'profile.html' , {'message':message})

def post(request):
    message = "create a post"

    return render(request, 'post.html' , {'messsage':message})

def search(request):
    message = "searched items"

    return render (request , 'search.html' , {'message':message})

def updateProfile(request):
    message = "update profile"

    return render (request , 'updateProfile.html' , {'message':message})
