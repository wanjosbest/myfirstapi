from django.urls import path
from .import views

urlpatterns=[
    path("blog-posts/", views.post_list, name="post_list"),
    path("details/<str:pk>/", views.postdetails, name="post_details"),
]