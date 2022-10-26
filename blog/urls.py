from . import views
from django.urls import path


urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('blog/', views.post_list, name="post_list"),
    path('recipes_search/', views.post_list, name="recipe_search"),
    path("create_post/", views.create_blog_post, name="create_post"),
    path('like/<slug:slug>/', views.post_like, name="post_like"),
    path('edit_comment/<slug:slug>/',
         views.edit_blog_comment, name='edit_blog_comment'
         ),
    path('delete_comment/<slug:slug>/',
         views.delete_blog_comment,
         name='delete_blog_comment'
         ),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path("<slug:slug>/edit", views.edit_blog_post, name="edit_blog_post"),
    path("<slug:slug>/delete",
         views.delete_blog_post, name="delete_blog_post"
         ),
]
