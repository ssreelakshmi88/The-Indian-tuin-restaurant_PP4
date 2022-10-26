from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Comment
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from .forms import CommentForm, PostForm
from django.db.models import Count
from django.contrib import messages


def post_list(request):
    post_list = Post.objects.all()
    comments = Post.objects.annotate(post_comments=Count('comments')) \
        .order_by('-post_comments')[:3]

    if request.method == 'POST':
        recipe = request.POST.get('recipe_name')
        if recipe != '' and recipe is not None:
            blog_recipes = post_list.filter(title__icontains=recipe) \
                .order_by('created_on')

            if not blog_recipes:
                messages.warning(request, 'No Recipes Found For Your Search')
                
                return redirect('blog/post_list.html')
            context = {
                'recipes': blog_recipes,
                'comments': comments,
                'post_list': post_list
                }
            messages.success(request, 'Recipe(s) Found.')
            return render(request, 'blog/recipes_search.html', context)
            
    paginator = Paginator(post_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'post_list': post_list,
        'page_obj': page_obj,
    }
    return render(
        request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post_detail = Post.objects.all()
    post = get_object_or_404(Post, slug=slug)
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
        'comment_form': comment_form
    }
    return render(
        request, 'blog/post_detail.html', context)


def post_like(request, slug):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, slug=slug)
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            liked = True

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

    else:
        messages.warning(
            request,
            'You must be logged in to perform that action!'
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
            return redirect("post_detail", slug=post.slug)

    context = {'form': form}
    return render(request, 'blog/create_post.html', context)


def edit_blog_post(request, slug):
    """
    This view to render a form to edit existing blog posts.
    """
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, f'{post.title} Updated.')
            return redirect("post_detail", slug=post.slug)

    context = {'post': post, 'form': form}
    return render(request, 'blog/edit_post.html', context)


def delete_blog_post(request, slug):
    """
    This view is to delete blog posts.
    """
    post = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    context = {"post": post}

    return render(request, "blog/delete_post.html", context,)


def edit_blog_comment(request, slug):
    """
    This view is to edit commment on a blog post.
    """
    comment = get_object_or_404(Comment, slug=slug)
    post = comment.post.id
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Comment Updated.')
            return redirect('post_detail')

    context = {'post': comment, 'form': form, 'slug': slug}
    return render(request, 'blog/edit_comment.html', context)


def delete_blog_comment(request, slug):
    """
    This view is to delete commment on a blog post.
    """
    comment = get_object_or_404(Comment, slug=slug)
    post = comment.post.id

    if request.method == 'POST':
        comment.delete()
        messages.success(request, f'Comment Deleted.')
        return redirect('post_detail')

    context = {'post': comment}
    return render(request, 'blog/delete_comment.html', context)
