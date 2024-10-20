from django.urls import path
from .import views

urlpatterns=[
    path("posts-api/", views.api_list, name="posts-api"),
    path("api-create-post/", views.apiblogpost, name="apiblogpost"),
    path("register-user/", views.registeruser, name="registeruser"),
    #path("login-user/", views.loginuser, name="loginuser"),
    path("api/<slug:slug>/", views.postdetails, name="post_details"),
    path("all-api/", views.apipage, name="apipage"),
]