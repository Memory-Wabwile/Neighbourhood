from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile, Neighbourhood, Business, Post
from .forms import BusinessForm , PostForm , ProfileUpdateForm , NewHoodForm
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

    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user

            post.save()

        return redirect('hood')

    else:
        form = PostForm()
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

   
    if 'business' in request.GET and request.GET["business"]:
        searched = request.GET.get("business")
        searched_bussiness = Business.find_business(searched)
        message = f"{searched}"

        return render(request, 'search.html',{"message":message,"searched_business": searched_bussiness})

    else:
        message = "You haven't searched for any term"
        

    return render (request , 'search.html' , {'message':message})

def updateProfile(request):
    message = "update profile"

    return render (request , 'updateProfile.html' , {'message':message})

def joinhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('hood')


def leavehood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')

def business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user

            business.save()

        return redirect('hood')

    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form})


