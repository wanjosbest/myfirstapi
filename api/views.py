from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PostSerializer
from api.models import Post, songdetails
from rest_framework import status




@api_view(["GET","POST"])
def post_list(request):
    if request.method=="GET":
        title_list= Post.objects.all()
        serializer=PostSerializer(title_list, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
@api_view(["GET","PUT","DELETE"])
def postdetails(request,pk):
    try:
        post=Post.objects.get(pk=pk)
    except post.DoestNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method=="GET":
        
        serializer=PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=PostSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
           
    elif request.method=="DELETE":
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        




