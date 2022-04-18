from django.shortcuts import render

# Create your views here.

def home(request):
    message = "Home page"

    return render (request ,'home.html' , {'message':message})
