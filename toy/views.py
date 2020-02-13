from django.shortcuts import render
from toy.models import Post


# Create your views here.
def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'toy/posts.html', context)
