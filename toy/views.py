from django.shortcuts import render
from toy.models import Post


# Create your views here.
def posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'toy/posts.html', context)

def post_list(request):
    return render(request, 'toy/post_list.html', {})


def main(request):
    return render(request, 'toy/main.html', {})

def page2(request):
    return render(request, 'toy/page2.html', {})

def page3(request):
    return render(request, 'toy/page3.html', {})
