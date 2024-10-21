from rest_framework import serializers
from api.models import Post
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=("category","title","content","image","slug",)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("first_name","last_name","username","email","password",)
class UserloginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("username","password",)