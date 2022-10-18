from . import views
from django.urls import path


urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('blog/', views.post_list, name="post_list"),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path("create_post/", views.create_blog_post, name="create_post"),
    path("<slug:slug>/edit", views.edit_blog_post, name="edit_blog_post"),
    path("<slug:slug>/delete", views.delete_blog_post, name="delete_blog_post"),
    path('like/<slug:slug>/', views.post_like, name="post_like"),
]