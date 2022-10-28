"""
Importing libraries to use in system.
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Comment
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm
from django.db.models import Count
from django.contrib import messages


def post_list(request):
    """
    This view is to render the blog page and all the posts.
    This view limits the posts to 4 per page and then creates page arrows.
    """
    post_list = Post.objects.all()
    comments = Post.objects.annotate(post_comments=Count('comments')) \
        .order_by('-post_comments')[:3]

    paginator = Paginator(post_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'post_list': post_list,
        'page_obj': page_obj,
    }
    return render(
        request, 'blog/post_list.html', context)


def post_detail(request, pk):
    """
    This view is to render single blog post.
    This view allows the user to like and unlike the posts.
    Registered users can leave comments.
    """
    post_detail = Post.objects.all()
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(approved=True).order_by("-created_on")
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True

    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        messages.success(
                    request, 'Comment awaiting approval.'
                    )
    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'liked': liked,
        "comment_form": CommentForm(),
        'commented': True,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)


def post_like(request, pk):
    """
    This view allows users to like or unlike a blog post.
    """
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

    else:
        messages.warning(
            request,
            'You have to log in!'
        )
        return redirect('login')


def create_blog_post(request):
    """
    This view to render a form to create new blog posts.
    """
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post Created.')
            return redirect("post_detail", pk=pk)

    context = {'form': form}
    return render(request, 'blog/create_post.html', context)


def edit_blog_post(request, pk):
    """
    This view to render a form to edit existing blog posts.
    """
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'{post.title} Updated.')
            return redirect("post_detail", pk=pk)

    context = {'post': post, 'form': form}
    return render(request, 'blog/edit_post.html', context)


def delete_blog_post(request, pk):
    """
    This view is to delete blog posts.
    """
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    context = {"post": post}

    return render(request, "blog/delete_post.html", context,)


def edit_blog_comment(request, pk):
    """
    This view is to edit commment on a blog post.
    """
    comment = get_object_or_404(Comment, id=pk)
    post = comment.post.id
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment is updated.')
            return redirect(f'/blog/{post}')

    context = {'post': comment, 'form': form, }
    return render(request, 'blog/edit_comment.html', context)


def delete_blog_comment(request, pk):
    """
    This view is to delete commment on a blog post.
    """
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post.id

    if request.method == 'POST':
        comment.delete()
        messages.success(request, f'Comment is deleted.')
        return redirect(f'/blog/{post}')

    context = {'post': comment}
    return render(request, 'blog/delete_comment.html', context)
