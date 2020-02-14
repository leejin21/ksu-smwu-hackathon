from django.urls import path
from toy.views import posts
from . import views

urlpatterns = [
    path('posts', posts),
    # path('', views.post_list, name = 'post_list'),
    path('', views.main, name = 'main'),
    path('main.css', views.main, name = 'main.css'),
    path('page2/', views.page2, name = "page2"),
    path('page2/page3/', views.page3, name = "page3"),
]
