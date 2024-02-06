
# from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')

# def about(request):
#     return render(request, 'about.html')

from django.shortcuts import render, get_object_or_404
from.models import Post
from django.http import Http404

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    # Méthode 1
    # try:
    #     post =Post.objects.get(id=id)
    # except post.DoesNotExist:
    #     raise Http404('NoPost Found!')
    # return render(request, 'blog/post/detail.html', {'post': post})

    # Méthode 2
    post = get_object_or_404(Post, id=id, status=Post.Status.DRAFT)
    return render(request, 'blog/post/detail.html', {'post': post})


