from django.shortcuts import render
from .models import Post, Comment
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


def post_list(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'post_list': post_list,
    }
    return render(
        request, 'posts/post_list.html', context)


def post_detail(request):
    post_detail = Post.objects.all()
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
        'page_obj': page_obj,
    }
    return render(
        request, 'posts/post_detail.html', context)
