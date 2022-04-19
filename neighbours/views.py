from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile, Neighbourhood, Business, Post
from .forms import BusinessForm , PostForm , ProfileUpdateForm , NewHoodForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  logout
# Create your views here.

def landing(request):
    message = "landing page"

    return render (request ,'landing.html' , {'message':message})

@login_required(login_url='/accounts/login/')
def home(request):
    message = "Home page"

    hood = Neighbourhood.objects.all()

    return render (request,'home.html',{'message':message , 'hood':hood})

@login_required(login_url='/accounts/login/')
def profile(request):
    message = "Profile page"

    return render (request, 'profile.html' , {'message':message})

@login_required(login_url='/accounts/login/')
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
    return render(request, 'post.html' , {'messsage':message , 'form':form})

@login_required(login_url='/accounts/login/')
def hood(request,id):
    message = "hoods page"
    hood=Neighbourhood.objects.get(id=id)
    current_hood=hood.name
    buseness=Business.objects.filter(neighbourhood=id)
    posts=Post.objects.filter(neighborhood=id)
    

    return render (request , 'hood.html' , {'message':message,'hood':hood ,'business':buseness,'current_hood':current_hood,'posts':posts})


@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def updateProfile(request):
    message = "update profile"

    current_user = request.user
    if request.method == 'POST':

        
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()

            return redirect('profile')

    else:
        form = ProfileUpdateForm(instance=request.user)

        context = {
            'form': form

        }

    return render(request, 'updateProfile.html', context)



@login_required(login_url='/accounts/login/')
def joinhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    profile.user.neighbourhood = hood
    profile.user.save()
    return redirect('hood')


@login_required(login_url='/accounts/login/')
def leavehood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url='/accounts/login/')
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


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('home')
