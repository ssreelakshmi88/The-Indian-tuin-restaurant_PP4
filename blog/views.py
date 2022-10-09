from django.shortcuts import render
from .models import Post, Comment
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


def post_list(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list,
    }
    return render(
        request, 'posts/post_list.html', context)
