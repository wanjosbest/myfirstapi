from django.shortcuts import render,redirect,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PostSerializer,UserSerializer,UserloginSerializer
from api.models import Post, songdetails
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib import messages





        
#api user registration
@api_view(["POST"])
def registeruser(request,):
    if request.method=="POST":
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(["POST"])
def loginserialization(request):
  if request.method=="POST":
     serializer=UserloginSerializer(data=request.data)
     if serializer.is_valid():
        return HttpResponse("you are already logged in")
  return Response(serializer.data, status=status.HTTP_302_FOUND)
     

 


#api post list
@api_view(["GET"])
def api_list(request):
    if request.method=="GET":
        title_list= Post.objects.all()
        serializer=PostSerializer(title_list, many=True)
        return Response(serializer.data)
    
# api create blog post
@api_view(["POST"])
def apiblogpost(request):
    if request.method=="POST":
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

 

        
# other  api practices  
@api_view(["GET","POST","DELETE"])
def postdetails(request,slug):
    try:
        post=Post.objects.get(slug=slug)
    except post.DoestNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method=="GET":
        
        serializer=PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method=="POST":
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
           
    elif request.method=="DELETE":
        post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#list of all API
def apipage(request):
    return render(request,"apipage.html")
        



