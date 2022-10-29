from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name="post_list"),
    path('blog/', views.post_list, name="post_list"),
    path('recipes_search/', views.post_list, name="recipes_search"),
    path("create_post/", views.create_blog_post, name="create_post"),
    path('like/<int:pk>/', views.post_like, name="post_like"),
    path('edit_comment/<int:pk>/',
         views.edit_blog_comment, name='edit_blog_comment'
         ),
    path('delete_comment/<int:pk>/',
         views.delete_blog_comment,
         name='delete_blog_comment'
         ),
    path('<int:pk>/', views.post_detail, name="post_detail"),
    path("<int:pk>/edit", views.edit_blog_post, name="edit_blog_post"),
    path("<int:pk>/delete",
         views.delete_blog_post, name="delete_blog_post"
         ),
]
