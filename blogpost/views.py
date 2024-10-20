from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from api.models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import AuthenticationForm
from . forms import songdetailsForm


def index(request):
 return render(request,"index.html")

def createpost(request):
    form=PostForm()

    #save the data to database
    if request.method=="POST":
       form=PostForm(request.POST)
   

       if form.is_valid():
          form.save()
          return HttpResponse("Post created Successful!")

    return render(request,"create-post.html",{"form":form})


def postlist(request ):
  Postlist=Post.objects.all()

  return render(request,"post-list.html",{"Postlist":Postlist})


def postdetails(request,slug):
  post=Post.objects.filter(slug=slug)

  return render(request,"postdetails.html",{"post":post})

def signup(request):
  if request.method=="POST":
     firstname=request.POST.get("firstname")
     secondname=request.POST.get("secondname")
     username=request.POST.get("username")
     email=request.POST.get("email")
     password=request.POST.get("password")
     
     user=User.objects.filter(username=username)
     if user.exists():
       messages.info(request,"username already taken")
       return redirect("/register/")
    
     user=User.objects.create(first_name=firstname,last_name=secondname,email=email,username=username,password=password)
     user.save()
     messages.info(request,"account created succesfully")
     return redirect("/login/")

  return render(request,"register.html")

def profile(request):

  return render(request,"profile.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Try again! username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)

#artist ssong upload

def songupload(request):
   uploadform=songdetailsForm()
   if request.method=="POST":
      uploadform=songdetailsForm(request.POST)
      if uploadform.is_valid():
         uploadform.save()
         messages.info(request,"You have successfully uploaded a song")
         return redirect("/profile/")
   return render(request,"uploadsong.html", {"uploadform":uploadform})



