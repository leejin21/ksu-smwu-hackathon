from django.urls import path
from toy.views import posts

urlpatterns = [
    path('posts', posts)
]
